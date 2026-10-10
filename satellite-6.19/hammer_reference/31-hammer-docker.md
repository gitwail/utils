---
title: "docker"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "31"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-docker"
---
# Chapter 31. docker

Manipulate docker content

**Usage**

```
# hammer docker [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 31.1. docker manifest

Manage docker manifests

**Usage**

```
# hammer docker manifest [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 31.1.1. docker manifest info

Show a docker manifest

**Usage**

```
# hammer docker manifest <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – A docker manifest identifier
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
| Name | x | x | x |
| Schema version | x | x |  |
| Digest | x | x |  |
| Downloaded | x | x |  |
| Tags/name | x | x |  |

### 31.1.2. docker manifest list

List docker_manifests

**Usage**

```
# hammer docker manifest <list|index> [OPTIONS]
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
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
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
| Id | x | x | x |
| Name | x | x | x |
| Schema version | x | x |  |
| Digest | x | x |  |
| Downloaded | x | x |  |
| Tags | x | x |  |

## 31.2. docker tag

Manage docker tags

**Usage**

```
# hammer docker tag [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 31.2.1. docker tag info

Show a docker tag

**Usage**

```
# hammer docker tag <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – A docker tag identifier
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
| Tag | x | x | x |
| Repository id | x | x |  |
| Docker manifest id | x | x |  |
| Docker manifest name | x | x |  |

### 31.2.2. docker tag list

List docker_tags

**Usage**

```
# hammer docker tag <list|index> [OPTIONS]
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
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
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
| Id | x | x | x |
| Tag | x | x | x |
| Repository id | x | x |  |
