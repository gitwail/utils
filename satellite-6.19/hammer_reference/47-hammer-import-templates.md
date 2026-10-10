---
title: "import-templates"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "47"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-import-templates"
---
# Chapter 47. import-templates

Import templates from a git repo or a directory on the server

**Usage**

```
# hammer import-templates [OPTIONS]
```

**Options**

- `--associate ENUM` – Associate to OS`s, Locations & Organizations. Options are: always, new or never. Possible value(s): `always`, `new`, `never`
- `--branch VALUE` – Branch in Git repo.
- `--dirname VALUE` – Directory within Git repo containing the templates.
- `--filter VALUE` – Export templates with names matching this regex (case-insensitive; snippets are not filtered).
- `--force BOOLEAN` – Update templates that are locked
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – ID of an HTTP proxy to use for template sync. Use this parameter together with `` http_proxy_policy`:`selected ``
- `--http-proxy-policy ENUM` – HTTP proxy policy for template sync. Use only when synchronizing templates through the HTTP or the HTTPS protocol. If you choose `selected`, provide the `http_proxy_id` parameter. Possible value(s): `global`, `none`, `selected`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--lock ENUM` – Lock imported templates Possible value(s): `lock`, `keep_lock_new`, `keep`, `unlock`, `true`, `false`, `0`, `1`
- `--negate BOOLEAN` – Negate the prefix (for purging).
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--prefix VALUE` – The string all imported templates should begin with.
- `--repo VALUE` – Override the default repo from settings.
- `--verbose BOOLEAN` – Show template diff in response
- `-h`, `--help` – Print help
