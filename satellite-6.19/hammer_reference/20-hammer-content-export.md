---
title: "content-export"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "20"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-content-export"
---
# Chapter 20. content-export

Prepare content for export to a disconnected Katello

**Usage**

```
# hammer content-export [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 20.1. content-export complete

Prepare content for a full export to a disconnected Katello

**Usage**

```
# hammer content-export complete [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 20.1.1. content-export complete library

Performs a full export of the organization’s library environment

**Usage**

```
# hammer content-export complete library [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--chunk-size-gb NUMBER` – Split the exported content into archives no greater than the specified size in gigabytes.
- `--destination-server VALUE` – Destination Server name
- `--fail-on-missing-content` – Fails if any of the repositories belonging to this organization are unexportable.
- `--format ENUM` – Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version and exported content needs to be one of yum, file, ansible_collection, docker, deb repositories. Possible value(s): `syncable`, `importable`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

### 20.1.2. content-export complete repository

Performs a full export of a repository

**Usage**

```
# hammer content-export complete repository [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--chunk-size-gb NUMBER` – Split the exported content into archives no greater than the specified size in gigabytes.
- `--format ENUM` – Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version and exported content needs to be one of yum, file, ansible_collection, docker, deb repositories. Possible value(s): `syncable`, `importable`
- `--id NUMBER` – Repository identifier
- `--name VALUE` – Filter repositories by name.
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `-h`, `--help` – Print help

### 20.1.3. content-export complete version

Performs a full export a content view version

**Usage**

```
# hammer content-export complete version [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--chunk-size-gb NUMBER` – Split the exported content into archives no greater than the specified size in gigabytes.
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--destination-server VALUE` – Destination Server name
- `--fail-on-missing-content` – Fails if any of the repositories belonging to this version are unexportable.
- `--format ENUM` – Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version and exported content needs to be one of yum, file, ansible_collection, docker, deb repositories. Possible value(s): `syncable`, `importable`
- `--id NUMBER` – Content view version identifier
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` ID of the environment
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--version VALUE` – Filter versions by version number.
- `-h`, `--help` – Print help

## 20.2. content-export generate-listing

Generates listing file on each directory of a syncable export. This command only needs to be used if the export was performed asynchronously or if the listing files were lost. Assumes the syncable export directory is accessible on disk

**Usage**

```
# hammer content-export generate-listing [OPTIONS]
```

**Options**

- `--id VALUE` – Generate listing files based on specified export history
- `--task-id VALUE` – Generate listing files for a syncable export task
- `-h`, `--help` – Print help

## 20.3. content-export generate-metadata

Writes export metadata to disk for use by the importing Katello. This command only needs to be used if the export was performed asynchronously or if the metadata was lost

**Usage**

```
# hammer content-export generate-metadata [OPTIONS]
```

**Options**

- `--id VALUE` – Generate metadata based on specified export history
- `--task-id VALUE` – Generate metadata based on output of the specified export task
- `-h`, `--help` – Print help

## 20.4. content-export incremental

Prepare content for an incremental export to a disconnected Katello

**Usage**

```
# hammer content-export incremental [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 20.4.1. content-export incremental library

Performs an incremental export of the organization’s library environment

**Usage**

```
# hammer content-export incremental library [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--chunk-size-gb NUMBER` – Split the exported content into archives no greater than the specified size in gigabytes.
- `--destination-server VALUE` – Destination Server name
- `--fail-on-missing-content` – Fails if any of the repositories belonging to this organization are unexportable.
- `--format ENUM` – Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version and exported content needs to be one of yum, file, ansible_collection, docker, deb repositories. Possible value(s): `syncable`, `importable`
- `--from-history-id NUMBER` – Export history identifier used for incremental export. If not provided the most recent export history will be used.
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

### 20.4.2. content-export incremental repository

Performs an incremental export of a repository

**Usage**

```
# hammer content-export incremental repository [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--chunk-size-gb NUMBER` – Split the exported content into archives no greater than the specified size in gigabytes.
- `--format ENUM` – Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version and exported content needs to be one of yum, file, ansible_collection, docker, deb repositories. Possible value(s): `syncable`, `importable`
- `--from-history-id NUMBER` – Export history identifier used for incremental export. If not provided the most recent export history will be used.
- `--id NUMBER` – Repository identifier
- `--name VALUE` – Filter repositories by name.
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `-h`, `--help` – Print help

### 20.4.3. content-export incremental version

Performs an incremental export of a content view version

**Usage**

```
# hammer content-export incremental version [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--chunk-size-gb NUMBER` – Split the exported content into archives no greater than the specified size in gigabytes.
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--destination-server VALUE` – Destination Server name
- `--fail-on-missing-content` – Fails if any of the repositories belonging to this version are unexportable.
- `--format ENUM` – Export formats.Choose syncable if the exported content needs to be in a yum format. This option is only available for yum, file repositories. Choose importable if the importing server uses the same version and exported content needs to be one of yum, file, ansible_collection, docker, deb repositories. Possible value(s): `syncable`, `importable`
- `--from-history-id NUMBER` – Export history identifier used for incremental export. If not provided the most recent export history will be used.
- `--id NUMBER` – Content view version identifier
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` ID of the environment
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--version VALUE` – Filter versions by version number.
- `-h`, `--help` – Print help

## 20.5. content-export list

View content view export histories

**Usage**

```
# hammer content-export <list|index> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` Content view version identifier
- `--destination-server VALUE` – Destination Server name
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--id NUMBER` – Content view version export history identifier
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--type ENUM` – Export Types Possible value(s): `complete`, `incremental`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Destination server | x | x |  |
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
