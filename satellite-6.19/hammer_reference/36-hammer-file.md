---
title: "file"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "36"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-file"
---
# Chapter 36. file

Manipulate files

**Usage**

```
# hammer file [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 36.1. file info

Show a file

**Usage**

```
# hammer file <info|show> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` Content view version identifier
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – A file identifier
- `--name VALUE` – File name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository identifier
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x |  |
| Name | x | x | x |
| Path | x | x |  |
| Uuid | x | x |  |
| Checksum | x | x |  |

## 36.2. file list

List files

**Usage**

```
# hammer file <list|index> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` – Content view filter identifier
- `--content-view-filter-rule VALUE` – Name to search by
- `--content-view-filter-rule-id NUMBER` Content view filter rule identifier
- `--content-view-id NUMBER` – Content view numeric identifier
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` – Content view version identifier
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--ids LIST` – Ids to filter content by
- `--include-filter-ids BOOLEAN` – Includes associated content view filter ids in response
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` – Environment identifier
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository identifier
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x |  |
| Name | x | x | x |
| Path | x | x |  |
