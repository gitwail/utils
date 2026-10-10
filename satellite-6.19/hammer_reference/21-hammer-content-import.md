---
title: "content-import"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "21"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-content-import"
---
# Chapter 21. content-import

Import content from an upstream archive.

**Usage**

```
# hammer content-import [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 21.1. content-import library

Imports a content archive to an organization’s library lifecycle environment

**Usage**

```
# hammer content-import library [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--metadata-file VALUE` – Location of the metadata.json file. This is not required if the metadata.json file is already in the archive directory.
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--path VALUE` – Directory containing the exported Content View Version
- `-h`, `--help` – Print help

## 21.2. content-import list

View content view import histories

**Usage**

```
# hammer content-import <list|index> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` Content view version identifier
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--id NUMBER` – Content view version import history identifier
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--type ENUM` – Import Types Possible value(s): `complete`, `incremental`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Path | x | x |  |
| Type | x | x |  |
| Content view version | x | x |  |
| Content view version id | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

**Search and order fields**

- `content_view_id` – integer
- `content_view_version_id` – integer
- `id` – integer
- `type` – string

## 21.3. content-import repository

Imports a repository

**Usage**

```
# hammer content-import repository [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--metadata-file VALUE` – Location of the metadata.json file. This is not required if the metadata.json file is already in the archive directory.
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--path VALUE` – Directory containing the exported Content View Version
- `-h`, `--help` – Print help

## 21.4. content-import version

Imports a content archive to a content view version

**Usage**

```
# hammer content-import version [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--metadata-file VALUE` – Location of the metadata.json file. This is not required if the metadata.json file is already in the archive directory.
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--path VALUE` – Directory containing the exported Content View Version
- `-h`, `--help` – Print help
