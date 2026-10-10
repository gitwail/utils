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
