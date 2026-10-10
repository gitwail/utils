# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4", "markdownify"]
# ///
"""Export Confluence Data Center / Server pages to Markdown for RAG.

One Markdown file per page with YAML front matter (title, breadcrumb, labels,
version, source URL). Reruns only re-download pages whose version changed.

Auth (environment variables, never written to disk):
    CONFLUENCE_URL       base URL, e.g. https://confluence.example.com
    CONFLUENCE_PAT       personal access token (preferred), or
    CONFLUENCE_USER + CONFLUENCE_PASSWORD   basic auth, or
    CONFLUENCE_COOKIE    browser session cookie, e.g. "JSESSIONID=..." (check IT policy)

Usage:
    uv run scripts/confluence_to_md.py --space LINUX --out confluence/LINUX
    uv run scripts/confluence_to_md.py --page-id 123456 --out confluence/some-tree
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlparse

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

PAGE_EXPAND = "ancestors,version,metadata.labels,space"
PANEL_LABELS = {"information": "Info", "note": "Note", "warning": "Warning", "tip": "Tip"}
DROP_MACROS = {"toc", "children", "pagetree", "recently-updated", "contentbylabel", "livesearch",
               "create-from-template", "excerpt-include-placeholder"}


# --------------------------------------------------------------------------- API


class Confluence:
    def __init__(self, base: str, delay: float, ca_bundle: str | None):
        self.base = base.rstrip("/")
        self.delay = delay
        self.s = requests.Session()
        self.s.verify = ca_bundle or os.environ.get("REQUESTS_CA_BUNDLE") or True
        if pat := os.environ.get("CONFLUENCE_PAT"):
            self.s.headers["Authorization"] = f"Bearer {pat}"
        elif os.environ.get("CONFLUENCE_USER"):
            self.s.auth = (os.environ["CONFLUENCE_USER"], os.environ.get("CONFLUENCE_PASSWORD", ""))
        elif cookie := os.environ.get("CONFLUENCE_COOKIE"):
            self.s.headers["Cookie"] = cookie
        else:
            sys.exit("set CONFLUENCE_PAT (or CONFLUENCE_USER/CONFLUENCE_PASSWORD, or CONFLUENCE_COOKIE)")
        self.s.headers["Accept"] = "application/json"

    def get(self, path: str, params: dict | None = None, raw: bool = False):
        url = path if path.startswith("http") else self.base + path
        for attempt in range(5):
            try:
                resp = self.s.get(url, params=params, timeout=120)
            except requests.RequestException as exc:
                if attempt == 4:
                    raise
                print(f"  retry {attempt + 1}: {exc}", file=sys.stderr)
                time.sleep(5 * (attempt + 1))
                continue
            if resp.status_code == 429 or resp.status_code >= 500:
                wait = int(resp.headers.get("Retry-After", 5 * (attempt + 1)))
                print(f"  HTTP {resp.status_code}, waiting {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            if resp.status_code in (401, 403):
                sys.exit(f"HTTP {resp.status_code} for {url}: check your token and that you can read this space")
            resp.raise_for_status()
            time.sleep(self.delay)
            return resp if raw else resp.json()
        resp.raise_for_status()

    def paged(self, path: str, params: dict):
        start = 0
        while True:
            data = self.get(path, {**params, "start": start, "limit": 50})
            results = data.get("results", [])
            yield from results
            if not results or "next" not in data.get("_links", {}):
                return
            start += len(results)

    def space_pages(self, space: str):
        return self.paged("/rest/api/content", {"spaceKey": space, "type": "page", "expand": PAGE_EXPAND})

    def page_tree(self, page_id: str):
        yield self.get(f"/rest/api/content/{page_id}", {"expand": PAGE_EXPAND})
        yield from self.paged(f"/rest/api/content/{page_id}/descendant/page", {"expand": PAGE_EXPAND})

    def body(self, page_id: str) -> str:
        data = self.get(f"/rest/api/content/{page_id}", {"expand": "body.export_view"})
        return data["body"]["export_view"]["value"]


# ------------------------------------------------------------------ HTML -> MD


class Converter(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags):
        code = el.get_text().replace("\xa0", " ").strip("\n")
        lang = el.get("data-lang", "")
        fence = "````" if "```" in code else "```"
        return f"\n\n{fence}{lang}\n{code}\n{fence}\n\n"


def clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()


def blockquote(soup: BeautifulSoup, label: str, title: str, content: list) -> Tag:
    bq = soup.new_tag("blockquote")
    p = soup.new_tag("p")
    strong = soup.new_tag("strong")
    strong.string = f"{label}: {title}" if title else label
    p.append(strong)
    bq.append(p)
    for child in content:
        bq.append(child.extract())
    return bq


def clean_html(html: str, page_url: str, base: str, attachments: dict[str, str]) -> BeautifulSoup:
    soup = BeautifulSoup(f"<div>{html}</div>", "html.parser")
    root = soup.div

    for el in root.find_all(attrs={"data-macro-name": True}):
        if el.get("data-macro-name") in DROP_MACROS:
            el.decompose()
    for el in root.find_all(["script", "style"]):
        el.decompose()
    for el in root.find_all("img", class_="emoticon"):
        el.decompose()

    # code macro: language lives in data-syntaxhighlighter-params="brush: bash; ..."
    for pre in root.find_all("pre"):
        params = pre.get("data-syntaxhighlighter-params", "")
        m = re.search(r"brush:\s*([\w+#-]+)", params)
        lang = m.group(1) if m else ""
        pre["data-lang"] = "" if lang in ("text", "plain", "none") else lang
        code_div = pre.find_parent("div", class_="code")
        header = code_div.find(class_="codeHeader") if code_div else None
        if header:
            title = soup.new_tag("p")
            em = soup.new_tag("em")
            em.string = clean_text(header.get_text())
            title.append(em)
            header.replace_with(title)

    # info / note / warning / tip macros
    for div in root.find_all("div", class_="confluence-information-macro"):
        kind = next((c.rsplit("-", 1)[-1] for c in div.get("class", [])
                     if c.startswith("confluence-information-macro-") and c.rsplit("-", 1)[-1] in PANEL_LABELS),
                    "information")
        title_el = div.find(class_="title", recursive=False)
        title = clean_text(title_el.get_text()) if title_el else ""
        body = div.find(class_="confluence-information-macro-body") or div
        div.replace_with(blockquote(soup, PANEL_LABELS[kind], title, list(body.children)))

    # generic panel macro
    for div in root.find_all("div", class_="panel"):
        if "code" in div.get("class", []):
            continue
        header = div.find(class_="panelHeader")
        content = div.find(class_="panelContent") or div
        div.replace_with(blockquote(soup, "Panel", clean_text(header.get_text()) if header else "",
                                    list(content.children)))

    # expand macro: keep the (hidden) content under its title
    for div in root.find_all("div", class_="expand-container"):
        ctrl = div.find(class_="expand-control-text")
        content = div.find(class_="expand-content") or div
        p = soup.new_tag("p")
        strong = soup.new_tag("strong")
        strong.string = clean_text(ctrl.get_text()) if ctrl else "Details"
        p.append(strong)
        div.insert_before(p)
        for child in list(content.children):
            div.insert_before(child.extract())
        div.decompose()

    # table cells: flatten paragraphs so rows stay on one line
    for cell in root.find_all(["td", "th"]):
        for p in cell.find_all("p"):
            p.insert_after(NavigableString(" "))
            p.unwrap()

    # links and images
    for a in root.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#"):
            a["href"] = page_url + href
        elif not href.startswith(("http://", "https://", "mailto:")):
            a["href"] = urljoin(base + "/", href.lstrip("/"))
    for img in root.find_all("img"):
        src = img.get("data-image-src") or img.get("src", "")
        if not src or src.startswith("data:"):
            img.decompose()
            continue
        absolute = urljoin(base + "/", src.lstrip("/"))
        alt = clean_text(img.get("alt", "")) or unquote(Path(urlparse(absolute).path).name) or "image"
        link = soup.new_tag("a", href=attachments.get(absolute, absolute))
        link.string = f"Image: {alt}"
        img.replace_with(link)

    # page title becomes h1, so push body headings down a level
    for h in root.find_all(re.compile(r"^h[1-5]$")):
        h.name = f"h{int(h.name[1]) + 1}"
    return soup


def to_markdown(soup: BeautifulSoup) -> str:
    md = Converter(heading_style="ATX", bullets="-", escape_underscores=False,
                   escape_asterisks=False).convert_soup(soup)
    md = md.replace("\xa0", " ")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


# --------------------------------------------------------------------- output


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80] or "page"


def front_matter(meta: dict) -> str:
    lines = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items()] + ["---", ""]
    return "\n".join(lines)


def download_attachments(api: Confluence, html: str, page_id: str, out: Path) -> dict[str, str]:
    soup = BeautifulSoup(html, "html.parser")
    mapping = {}
    for img in soup.find_all("img"):
        src = img.get("data-image-src") or img.get("src", "")
        if "/download/" not in src:
            continue
        absolute = urljoin(api.base + "/", src.lstrip("/"))
        name = unquote(Path(urlparse(absolute).path).name)
        rel = Path("_attachments") / page_id / name
        target = out / rel
        if not target.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(api.get(absolute, raw=True).content)
        mapping[absolute] = quote(rel.as_posix())
    return mapping


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    scope = ap.add_mutually_exclusive_group(required=True)
    scope.add_argument("--space", help="space key, e.g. LINUX")
    scope.add_argument("--page-id", help="export this page and all its descendants")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--url", default=os.environ.get("CONFLUENCE_URL"), help="base URL (or CONFLUENCE_URL)")
    ap.add_argument("--ca-bundle", help="CA bundle for an internal TLS certificate")
    ap.add_argument("--delay", type=float, default=0.2, help="seconds between requests")
    ap.add_argument("--limit", type=int, help="export at most N pages (smoke test; skips deletions)")
    ap.add_argument("--attachments", action="store_true", help="download embedded images")
    ap.add_argument("--force", action="store_true", help="re-export pages even if unchanged")
    args = ap.parse_args()
    if not args.url:
        sys.exit("set CONFLUENCE_URL or pass --url")

    api = Confluence(args.url, args.delay, args.ca_bundle)
    args.out.mkdir(parents=True, exist_ok=True)
    state_path = args.out / "state.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}

    pages = api.space_pages(args.space) if args.space else api.page_tree(args.page_id)
    seen, tree, exported, skipped = {}, [], 0, 0
    for i, page in enumerate(pages):
        if args.limit and i >= args.limit:
            break
        pid = page["id"]
        version = page["version"]["number"]
        ancestors = [a["title"] for a in page.get("ancestors", [])]
        fname = f"{pid}-{slugify(page['title'])}.md"
        seen[pid] = {"version": version, "file": fname}
        tree.append((ancestors, page["title"], fname))

        prev = state.get(pid)
        if prev and not args.force and prev["version"] == version and (args.out / fname).exists():
            skipped += 1
            continue
        if prev and prev["file"] != fname:
            (args.out / prev["file"]).unlink(missing_ok=True)

        print(f"- {' / '.join(ancestors + [page['title']])}")
        page_url = api.base + page.get("_links", {}).get("webui", f"/pages/viewpage.action?pageId={pid}")
        html = api.body(pid)
        attachments = download_attachments(api, html, pid, args.out) if args.attachments else {}
        body = to_markdown(clean_html(html, page_url, api.base, attachments))
        meta = {
            "title": page["title"],
            "space": page.get("space", {}).get("key", args.space or ""),
            "page_id": pid,
            "ancestors": ancestors,
            "labels": [l["name"] for l in page.get("metadata", {}).get("labels", {}).get("results", [])],
            "version": version,
            "last_modified": page["version"].get("when", ""),
            "author": page["version"].get("by", {}).get("displayName", ""),
            "source_url": page_url,
        }
        (args.out / fname).write_text(front_matter(meta) + f"# {page['title']}\n\n" + body, encoding="utf-8")
        exported += 1

    removed = 0
    if not args.limit:
        for pid, prev in state.items():
            if pid not in seen:
                (args.out / prev["file"]).unlink(missing_ok=True)
                shutil.rmtree(args.out / "_attachments" / pid, ignore_errors=True)
                removed += 1
        state = seen
    else:
        state.update(seen)
    state_path.write_text(json.dumps(state, indent=1, sort_keys=True), encoding="utf-8")

    tree.sort(key=lambda t: [x.lower() for x in t[0] + [t[1]]])
    lines = [f"# {args.space or f'Page tree {args.page_id}'}", "", f"Exported from {api.base}", ""]
    lines += [f"{'  ' * len(anc)}- [{title}]({fname})" for anc, title, fname in tree]
    (args.out / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"done: {exported} exported, {skipped} unchanged, {removed} removed -> {args.out}")


if __name__ == "__main__":
    main()
