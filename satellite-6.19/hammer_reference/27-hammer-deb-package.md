---
title: "deb-package"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "27"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-deb-package"
---
# Chapter 27. deb-package

Manipulate deb packages

**Usage**

```
# hammer deb-package [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 27.1. deb-package info

Show a deb package

**Usage**

```
# hammer deb-package <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – A deb package identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository identifier
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Pulp id | x | x |  |
| Uuid | x | x |  |
| Name | x | x | x |
| Version | x | x |  |
| Checksum | x | x |  |
| Architecture | x | x |  |
| Nav | x | x |  |
| Nva | x | x |  |
| Filename | x | x |  |
| Available host count | x | x |  |
| Applicable host count | x | x |  |
| Description | x | x |  |

## 27.2. deb-package list

List deb packages

**Usage**

```
# hammer deb-package <list|index> [OPTIONS]
```

**Options**

- `--available-for VALUE` – Return deb packages that can be added to the specified object. Only the value `content_view_version` is supported.
- `--content-view VALUE` – Content view name to search by
- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` – Content View Filter identifier. Use to filter by ID
- `--content-view-id NUMBER` – Content view numeric identifier
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` – Content View Version identifier
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – Host id to list applicable deb packages for
- `--ids LIST` – Deb package identifiers to filter content by
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` – Environment identifier
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--packages-restrict-applicable BOOLEAN` Return deb packages that are applicable to one or more hosts (defaults to true if host_id is specified)
- `--packages-restrict-latest BOOLEAN` – Return only the latest version of each package
- `--packages-restrict-upgradable BOOLEAN` Return deb packages that are upgradable on one or more hosts
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository identifier
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Filename | x | x |
