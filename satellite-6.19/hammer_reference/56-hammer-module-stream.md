---
title: "module-stream"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "56"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-module-stream"
---
# Chapter 56. module-stream

View Module Streams

**Usage**

```
# hammer module-stream [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 56.1. module-stream info

Show a module stream

**Usage**

```
# hammer module-stream <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – A module stream identifier
- `--name VALUE` – Module stream name to search by
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
| Module stream name | x | x | x |
| Stream | x | x |  |
| Uuid | x | x |  |
| Version | x | x |  |
| Architecture | x | x |  |
| Context | x | x |  |
| Repositories/id | x | x |  |
| Repositories/name | x | x |  |
| Repositories/label | x | x |  |
| Artifacts/id | x | x |  |
| Artifacts/name | x | x |  |
| Profiles/id | x | x |  |
| Profiles/name | x | x |  |
| Profiles/rpms/id | x | x |  |
| Profiles/rpms/name | x | x |  |

## 56.2. module-stream list

List module streams

**Usage**

```
# hammer module-stream <list|index> [OPTIONS]
```

**Options**

- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` – Content view filter identifier
- `--content-view-filter-rule VALUE` – Name to search by
- `--content-view-filter-rule-id NUMBER` Content view filter rule identifier
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` – Content view version identifier
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host-ids LIST` – List of host id to list available module streams for
- `--hosts LIST`
- `--ids LIST` – Ids to filter content by
- `--include-filter-ids BOOLEAN` – Includes associated content view filter ids in response
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` – Environment identifier
- `--name-stream-only BOOLEAN` – Return name and stream information only)
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
| Module stream name | x | x | x |
| Stream | x | x |  |
| Uuid | x | x |  |
| Version | x | x |  |
| Architecture | x | x |  |
| Context | x | x |  |
