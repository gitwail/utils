---
title: "export-templates"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "34"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-export-templates"
---
# Chapter 34. export-templates

Export templates to a git repo or a directory on the server

**Usage**

```
# hammer export-templates [OPTIONS]
```

**Options**

- `--branch VALUE` – Branch in Git repo.
- `--commit-msg VALUE` – Custom commit message for templates export
- `--dirname VALUE` – Directory within Git repo containing the templates.
- `--filter VALUE` – Export templates with names matching this regex (case-insensitive; snippets are not filtered).
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – ID of an HTTP proxy to use for template sync. Use this parameter together with `` http_proxy_policy`:`selected ``
- `--http-proxy-policy ENUM` – HTTP proxy policy for template sync. Use only when synchronizing templates through the HTTP or the HTTPS protocol. If you choose `selected`, provide the `http_proxy_id` parameter. Possible value(s): `global`, `none`, `selected`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--metadata-export-mode ENUM` – Specify how to handle metadata Possible value(s): `refresh`, `keep`, `remove`
- `--negate BOOLEAN` – Negate the prefix (for purging).
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--repo VALUE` – Override the default repo from settings.
- `--verbose BOOLEAN` – Be verbose
- `-h`, `--help` – Print help
