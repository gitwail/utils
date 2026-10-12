# utils

## Red Hat Satellite 6.19 documentation as Markdown

`satellite-6.19/` contains the full [Red Hat Satellite 6.19 documentation](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19)
converted to Markdown for use in a RAG pipeline:

- one directory per guide (26 guides), each with a `README.md` table of contents
- one file per chapter/appendix (`NN-<section-id>.md`), with YAML front matter:

```yaml
---
title: "Reviewing hosts in Satellite web UI"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#reviewing-hosts-in-web-ui"
---
```

Admonitions become blockquotes (`> **Note**`), code blocks are fenced with their language, and
all links (including cross-references) are absolute docs.redhat.com URLs. Images are replaced by
links. The "Providing feedback" preface and legal notice are dropped.

### Regenerate

Requires [uv](https://docs.astral.sh/uv/); dependencies are declared inline in the script.

```bash
uv run scripts/rh_docs_to_md.py --product red_hat_satellite --version 6.19 --out satellite-6.19
```

Raw HTML is cached in `.cache/` (gitignored); delete it to re-download. Use `--only <slug> ...`
to convert specific guides. The script should work for other docs.redhat.com products and versions
(`--product`, `--product-name`, `--version`).

## Confluence (Data Center / Server) to Markdown

`scripts/confluence_to_md.py` exports a Confluence space, or a single page with all its child pages,
to one Markdown file per page for RAG. It must run on a machine that can reach Confluence (for example
the company network or VPN).

1. Create a Personal Access Token in Confluence: avatar → **Settings** → **Personal Access Tokens** →
   **Create token** (read access is enough). If the menu is missing, ask IT whether PATs are enabled.
2. Run:

```bash
export CONFLUENCE_URL=https://confluence.example.com
export CONFLUENCE_PAT=...              # or CONFLUENCE_USER + CONFLUENCE_PASSWORD
uv run scripts/confluence_to_md.py --space LINUX --out confluence/LINUX --limit 5   # smoke test
uv run scripts/confluence_to_md.py --space LINUX --out confluence/LINUX             # full space
uv run scripts/confluence_to_md.py --page-id 123456 --out confluence/my-tree        # one page and its children
```

Instead of `export`, you can fill in the `.env` template (run `git update-index --skip-worktree .env`
first so your token is never committed) and run with `uv run --env-file .env ...`.
See [CONFLUENCE_ENV.md](CONFLUENCE_ENV.md) for where to get each variable.

Options: `--attachments` downloads embedded images to `_attachments/`, `--ca-bundle corp-ca.pem`
uses an internal TLS certificate authority, `--force` re-exports every page and `--delay` sets the
seconds between requests.

Output: one `<page_id>-<slug>.md` per page, each with front matter (`title`, `space`, `page_id`,
`ancestors`, `labels`, `version`, `last_modified`, `author`, `source_url`), plus a `README.md`
page tree and a `state.json`. Reruns download only pages whose version changed and delete files
for pages that were removed. Code, info/warning/note/tip, panel and expand macros are converted;
table-of-contents and child-page listing macros are dropped.

For RAG, chunk each file on `##` headings and keep `title` and `ancestors` with every chunk.

**The export is internal company data.** `confluence/` is gitignored, so don't commit it to this repo.
