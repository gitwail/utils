# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4", "markdownify"]
# ///
"""Convert a Red Hat documentation set (docs.redhat.com) into Markdown for RAG.

Each guide is fetched as single-page HTML and split into one Markdown file per
preface/chapter/appendix, each with YAML front matter pointing back to the source.

Usage:
    uv run scripts/rh_docs_to_md.py --product red_hat_satellite --version 6.19 --out satellite-6.19
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

BASE = "https://docs.redhat.com"
TOP_LEVEL = ("preface", "chapter", "appendix")
SKIP_ID = re.compile(r"providing-feedback|proc_providing-feedback")
TITLE_RE = re.compile(r"^(Chapter|Appendix|Part)\s+([\w.]+)\.\s+(.*)$")


def fetch(url: str, cache: Path, delay: float) -> str:
    key = re.sub(r"[^\w.-]+", "_", url.removeprefix(BASE))
    path = cache / f"{key}.html"
    if path.exists():
        return path.read_text(encoding="utf-8")
    for attempt in range(4):
        try:
            resp = requests.get(url, timeout=120)
            resp.raise_for_status()
            break
        except requests.RequestException as exc:
            if attempt == 3:
                raise
            print(f"  retry {attempt + 1} for {url}: {exc}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    time.sleep(delay)
    cache.mkdir(parents=True, exist_ok=True)
    path.write_text(resp.text, encoding="utf-8")
    return resp.text


def guide_slugs(landing_html: str, product: str, version: str) -> list[str]:
    pat = re.compile(rf"/{re.escape(product)}/{re.escape(version)}/html/([^/\"#?]+)")
    return list(dict.fromkeys(pat.findall(landing_html)))


def clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("\xa0", " ")).strip()


class Converter(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags):
        code = el.get_text().replace("\xa0", " ").strip("\n")
        lang = ""
        for cls in el.get("class") or []:
            if cls.startswith("language-"):
                lang = cls.removeprefix("language-")
        lang = "" if lang == "plaintext" else lang
        fence = "````" if "```" in code else "```"
        return f"\n\n{fence}{lang}\n{code}\n{fence}\n\n"


def to_markdown(el: Tag) -> str:
    md = Converter(heading_style="ATX", bullets="-", escape_underscores=False,
                   escape_asterisks=False).convert_soup(el)
    md = md.replace("\xa0", " ")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n"


def clean_section(sec: Tag, soup: BeautifulSoup, page_url: str) -> None:
    # UI chrome
    for t in sec.find_all(["rh-tooltip", "rh-button", "button", "rh-icon"]):
        t.decompose()
    for t in sec.find_all(attrs={"hidden": True}):
        t.decompose()
    # headings: drop the self-link anchor, keep its text
    for h in sec.find_all(re.compile(r"^h[1-6]$")):
        for a in h.find_all("a", class_="anchor-heading"):
            a.unwrap()
    # admonitions -> blockquote
    for alert in sec.find_all("rh-alert"):
        header = alert.find(class_="admonition_header")
        label = clean_text(header.get_text()) if header else "Note"
        if header:
            header.decompose()
        bq = soup.new_tag("blockquote")
        p = soup.new_tag("p")
        strong = soup.new_tag("strong")
        strong.string = label
        p.append(strong)
        bq.append(p)
        for child in list(alert.children):
            bq.append(child.extract())
        alert.replace_with(bq)
    # code blocks: unwrap web components so <pre> is converted directly
    for t in sec.find_all(["rh-code-block", "rh-table"]):
        t.unwrap()
    # table cells: flatten paragraphs so rows stay on one line
    for cell in sec.find_all(["td", "th"]):
        for p in cell.find_all("p"):
            p.insert_after(NavigableString(" "))
            p.unwrap()
    # links and images -> absolute
    for a in sec.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#"):
            a["href"] = page_url + href
        elif not href.startswith(("http://", "https://", "mailto:")):
            a["href"] = urljoin(page_url, href)
    for img in sec.find_all("img"):
        src = img.get("src", "")
        if src.startswith("data:"):
            img.decompose()
            continue
        alt = clean_text(img.get("alt", "")) or "image"
        link = soup.new_tag("a", href=urljoin(page_url, src))
        link.string = f"Image: {alt}"
        img.replace_with(link)
    # shift headings up one level so the chapter title (h2) becomes h1
    for h in sec.find_all(re.compile(r"^h[2-6]$")):
        h.name = f"h{int(h.name[1]) - 1}"


def top_level_sections(book: Tag) -> list[Tag]:
    out = []
    for sec in book.find_all("section"):
        classes = sec.get("class") or []
        if not any(c in TOP_LEVEL for c in classes):
            continue
        if sec.find_parent("section", class_=list(TOP_LEVEL)):
            continue
        out.append(sec)
    return out


def front_matter(meta: dict) -> str:
    lines = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items()] + ["---", ""]
    return "\n".join(lines)


def convert_guide(slug: str, args, cache: Path, out: Path) -> dict:
    page_url = f"{BASE}/en/documentation/{args.product}/{args.version}/html-single/{slug}/index"
    html = fetch(page_url, cache, args.delay)
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    if article is None:
        raise RuntimeError(f"no <article> in {page_url}")
    h1 = article.find("h1")
    guide_title = clean_text(h1.get_text()) if h1 else slug
    subtitle = article.find("h2", class_="subtitle")
    abstract = article.find(class_="abstract")
    description = clean_text(subtitle.get_text()) if subtitle else ""
    abstract_text = ""
    if abstract:
        t = abstract.find(class_="title")
        if t:
            t.decompose()
        abstract_text = clean_text(abstract.get_text())

    book = article.find(class_="book") or article
    sections = [s for s in top_level_sections(book) if not SKIP_ID.search(s.get("id", ""))]
    if not sections:
        # guides without chapters: emit the whole body as one file
        for t in book.find_all(class_=["titlepage", "legalnotice"]):
            t.decompose()
        sections = [book]

    gdir = out / slug
    gdir.mkdir(parents=True, exist_ok=True)
    for old in gdir.glob("*.md"):
        old.unlink()

    chapters = []
    for idx, sec in enumerate(sections, 1):
        sec_id = sec.get("id") or f"section-{idx}"
        clean_section(sec, soup, page_url)
        heading = sec.find(re.compile(r"^h[1-6]$"))
        raw_title = clean_text(heading.get_text()) if heading else guide_title
        m = TITLE_RE.match(raw_title)
        number, title = (m.group(2), m.group(3)) if m else ("", raw_title)
        body = to_markdown(sec)
        meta = {
            "title": title,
            "product": args.product_name,
            "version": args.version,
            "guide": slug,
            "guide_title": guide_title,
            "chapter_number": number,
            "section_type": next((c for c in sec.get("class") or [] if c in TOP_LEVEL), "book"),
            "source_url": f"{page_url}#{sec_id}" if sec is not book else page_url,
        }
        fname = f"{idx:02d}-{re.sub(r'[^a-z0-9-]+', '-', sec_id.lower()).strip('-')[:100]}.md"
        (gdir / fname).write_text(front_matter(meta) + body, encoding="utf-8")
        chapters.append((fname, number, title))

    readme = [f"# {guide_title}", ""]
    if description:
        readme += [f"_{description}_", ""]
    if abstract_text:
        readme += [abstract_text, ""]
    readme += [f"Source: {page_url}", "", "## Contents", ""]
    for fname, number, title in chapters:
        label = f"{number}. {title}" if number else title
        readme.append(f"- [{label}]({fname})")
    (gdir / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    return {"slug": slug, "title": guide_title, "description": description, "files": len(chapters)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--product", default="red_hat_satellite")
    ap.add_argument("--product-name", default="Red Hat Satellite")
    ap.add_argument("--version", default="6.19")
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--cache", type=Path, default=Path(".cache"))
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between network requests")
    ap.add_argument("--only", nargs="*", help="convert only these guide slugs")
    args = ap.parse_args()

    landing = f"{BASE}/en/documentation/{args.product}/{args.version}"
    slugs = guide_slugs(fetch(landing, args.cache, args.delay), args.product, args.version)
    if args.only:
        slugs = [s for s in slugs if s in args.only]
    if not slugs:
        sys.exit(f"no guides found at {landing}")
    print(f"{len(slugs)} guides")

    guides = []
    for slug in slugs:
        print(f"- {slug}")
        guides.append(convert_guide(slug, args, args.cache, args.out))

    index = [f"# {args.product_name} {args.version} documentation", "",
             f"Converted from {landing}", "", "| Guide | Files | Description |", "|---|---|---|"]
    for g in guides:
        index.append(f"| [{g['title']}]({g['slug']}/README.md) | {g['files']} | {g['description']} |")
    (args.out / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    print(f"done: {sum(g['files'] for g in guides)} files in {args.out}")


if __name__ == "__main__":
    main()
