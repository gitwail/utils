---
title: "package"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "59"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-package"
---
# Chapter 59. package

Manipulate packages

**Usage**

```
# hammer package [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 59.1. package info

Show a package

**Usage**

```
# hammer package <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – A package identifier
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
| Architecture | x | x |  |
| Epoch | x | x |  |
| Release | x | x |  |
| Author | x | x |  |
| Filename | x | x |  |
| Source rpm | x | x |  |
| Nvrea | x | x |  |
| Build host | x | x |  |
| Available host count | x | x |  |
| Applicable host count | x | x |  |
| Children | x | x |  |
| Vendor | x | x |  |
| License | x | x |  |
| Relative path | x | x |  |
| Description | x | x |  |
| Summary | x | x |  |
| Url | x | x |  |
| Build time | x | x |  |
| Group | x | x |  |
| Requires | x | x |  |
| Provides | x | x |  |
| Files | x | x |  |
| Size | x | x |  |
| Modular | x | x |  |

## 59.2. package list

List packages

**Usage**

```
# hammer package <list|index> [OPTIONS]
```

**Options**

- `--available-for VALUE` – Return packages that can be added to the specified object. Only the value `content_view_version` is supported.
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
- `--host-id NUMBER` – Host id to list applicable packages for
- `--ids LIST` – Package identifiers to filter content by
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` – Environment identifier
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--packages-restrict-applicable BOOLEAN` Return packages that are applicable to one or more hosts (defaults to true if host_id is specified)
- `--packages-restrict-latest BOOLEAN` – Return only the latest version of each package
- `--packages-restrict-upgradable BOOLEAN` Return packages that are upgradable on one or more hosts
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
| Source rpm | x | x |
