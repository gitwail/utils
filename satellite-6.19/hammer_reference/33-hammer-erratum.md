---
title: "erratum"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "33"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-erratum"
---
# Chapter 33. erratum

Manipulate errata

**Usage**

```
# hammer erratum [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 33.1. erratum info

Show an erratum

**Usage**

```
# hammer erratum info [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – An erratum identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository identifier
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Title | x | x |
| Version | x | x |
| Description | x | x |
| Status | x | x |
| Id | x | x |
| Errata id | x | x |
| Reboot suggested | x | x |
| Updated | x | x |
| Issued | x | x |
| Release | x | x |
| Solution | x | x |
| Packages | x | x |
| Module streams/name | x | x |
| Module streams/stream | x | x |
| Module streams/packages | x | x |

## 33.2. erratum list

List errata

**Usage**

```
# hammer erratum <list|index> [OPTIONS]
```

**Options**

- `--available-for VALUE` – Return errata that can be added to the specified object. The values `content_view_version` and `content_view_filter are supported.
- `--content-view VALUE` – Content view name to search by
- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` – Content View Filter identifier. Use to filter by ID
- `--content-view-id NUMBER` – Content view numeric identifier
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` – Content View Version identifier
- `--cve VALUE` – CVE identifier
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--errata-restrict-applicable BOOLEAN` Return errata that are applicable to one or more hosts (defaults to true if host_id is specified)
- `--errata-restrict-installable BOOLEAN` Return errata that are upgradable on one or more hosts
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – Host id to list applicable errata for
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

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Errata id | x | x |
| Type | x | x |
| Title | x | x |
| Issued | x | x |
| Updated | x | x |

**Search and order fields**

- `bug` – string
- `cve` – string
- `db_id` – integer
- `errata_id` – string
- `errata_type` – string
- `id` – string
- `issued` – date
- `modular` – Values: true, false
- `package` – string
- `package_name` – string
- `reboot_suggested` – boolean
- `repository` – string
- `severity` – string
- `synopsis` – string
- `title` – string
- `type` – Values: security, bugfix, enhancement, other
- `updated` – date
