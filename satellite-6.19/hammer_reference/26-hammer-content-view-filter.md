---
title: "content-view filter"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "26"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-content-view-filter"
---
# Chapter 26. content-view filter

View and manage filters

**Usage**

```
# hammer content-view filter [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 26.1. content-view filter add-repository

Associate a resource

**Usage**

```
# hammer content-view filter add-repository [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--id VALUE` – Filter identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository ID
- `-h`, `--help` – Print help

## 26.2. content-view filter create

create a filter for a content view

**Usage**

```
# hammer content-view filter create [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--description VALUE` – Description of the filter
- `--inclusion BOOLEAN` – Specifies if content should be included or excluded, default: inclusion=false
- `--name VALUE` – Name of the filter
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--original-module-streams BOOLEAN` Add all module streams without errata to the included/excluded list. (module stream filter only)
- `--original-packages BOOLEAN` – Add all packages without errata to the included/excluded list. (package filter only)
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--repositories LIST`
- `--repository-ids LIST` – List of repository ids
- `--type VALUE` – Type of filter (e.g. deb, rpm, package_group, erratum, erratum_id, erratum_date, docker, modulemd)
- `-h`, `--help` – Print help

## 26.3. content-view filter delete

delete a filter

**Usage**

```
# hammer content-view filter <delete|destroy> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--id NUMBER` – Filter identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 26.4. content-view filter info

show filter info

**Usage**

```
# hammer content-view filter <info|show> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Filter identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Filter id | x | x | x |
| Name | x | x | x |
| Type | x | x |  |
| Inclusion | x | x |  |
| Description | x | x |  |
| Repositories/id | x | x |  |
| Repositories/name | x | x |  |
| Repositories/label | x | x |  |
| Rules/id | x | x |  |
| Rules/name | x | x |  |
| Rules/version | x | x |  |
| Rules/minimum version | x | x |  |
| Rules/maximum version | x | x |  |
| Rules/errata id | x | x |  |
| Rules/start date | x | x |  |
| Rules/end date | x | x |  |
| Rules/types | x | x |  |
| Rules/module stream id | x | x |  |
| Rules/created | x | x |  |
| Rules/updated | x | x |  |

## 26.5. content-view filter list

list filters

**Usage**

```
# hammer content-view filter <list|index> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--name VALUE` – Filter content view filters by name
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--types LIST` – Types of filters
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Filter id | x | x | x |
| Name | x | x | x |
| Description | x | x |  |
| Type | x | x |  |
| Inclusion | x | x |  |

**Search and order fields**

- `content_type` – Values: rpm, deb, package_group, erratum, docker, modulemd
- `inclusion_type` – Values: include, exclude
- `name` – string

## 26.6. content-view filter remove-repository

Disassociate a resource

**Usage**

```
# hammer content-view filter remove-repository [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--id VALUE` – Filter identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository ID
- `-h`, `--help` – Print help

## 26.7. content-view filter rule

View and manage filter rules

**Usage**

```
# hammer content-view filter rule [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 26.7.1. content-view filter rule create

Create a filter rule. The parameters included should be based upon the filter type.

**Usage**

```
# hammer content-view filter rule create [OPTIONS]
```

**Options**

- `--allow-other-types BOOLEAN` – Erratum: allow types not matching a valid errata type
- `--architecture VALUE` – Package: architecture
- `--content-view VALUE` – Content view name to search by
- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` Filter identifier
- `--content-view-id NUMBER`
- `--date-type VALUE` – Erratum: search using the `Issued On` or `Updated On` column of the errata. Values are `issued`/`updated`
- `--end-date VALUE` – Erratum: end date (YYYY-MM-DD)
- `--errata-id VALUE` – Erratum: id
- `--errata-ids LIST` – Erratum: IDs or a select all object
- `--max-version VALUE` – Package: maximum version
- `--min-version VALUE` – Package: minimum version
- `--module-stream-ids LIST` – Module stream ids
- `--name LIST` – Deb, package, package group, or docker tag names
- `--names VALUE` – Package and package group names
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--start-date VALUE` – Erratum: start date (YYYY-MM-DD)
- `--types LIST` – Erratum: types (enhancement, bugfix, security)
- `--uuid VALUE` – Package group: uuid
- `--version VALUE` – Package: version
- `-h`, `--help` – Print help

### 26.7.2. content-view filter rule delete

Delete a filter rule

**Usage**

```
# hammer content-view filter rule <delete|destroy> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` Filter identifier
- `--content-view-id NUMBER`
- `--id NUMBER` – Rule identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

### 26.7.3. content-view filter rule info

Show filter rule info

**Usage**

```
# hammer content-view filter rule <info|show> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` Filter identifier
- `--content-view-id NUMBER`
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Rule identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Rule id | x | x | x |
| Filter id | x | x |  |
| Name | x | x | x |
| Version | x | x |  |
| Minimum version | x | x |  |
| Maximum version | x | x |  |
| Architecture | x | x |  |
| Errata id | x | x |  |
| Start date | x | x |  |
| End date | x | x |  |
| Date type | x | x |  |
| Types | x | x |  |
| Module stream id | x | x |  |
| Created | x | x |  |
| Updated | x | x |  |

### 26.7.4. content-view filter rule list

List filter rules

**Usage**

```
# hammer content-view filter rule <list|index> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` Filter identifier
- `--content-view-id NUMBER`
- `--errata-id VALUE` – Errata_id of the content view filter rule
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--name VALUE` – Name of the content view filter rule
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Rule id | x | x | x |
| Filter id | x | x |  |
| Name | x | x | x |
| Version | x | x |  |
| Minimum version | x | x |  |
| Maximum version | x | x |  |
| Architecture | x | x |  |
| Errata id | x | x |  |
| Start date | x | x |  |
| End date | x | x |  |
| Module stream id | x | x |  |

### 26.7.5. content-view filter rule update

Update a filter rule. The parameters included should be based upon the filter type.

**Usage**

```
# hammer content-view filter rule update [OPTIONS]
```

**Options**

- `--allow-other-types BOOLEAN` – Erratum: allow types not matching a valid errata type
- `--architecture VALUE` – Package: architecture
- `--content-view VALUE` – Content view name to search by
- `--content-view-filter VALUE` – Name to search by
- `--content-view-filter-id NUMBER` Filter identifier
- `--content-view-id NUMBER`
- `--end-date VALUE` – Erratum: end date (YYYY-MM-DD)
- `--errata-id VALUE` – Erratum: id
- `--id NUMBER` – Rule identifier
- `--max-version VALUE` – Package: maximum version
- `--min-version VALUE` – Package: minimum version
- `--name VALUE` – Package, package group, or docker tag: name
- `--new-name VALUE` – Package, package group, or docker tag: name
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--start-date VALUE` – Erratum: start date (YYYY-MM-DD)
- `--types LIST` – Erratum: types (enhancement, bugfix, security)
- `--version VALUE` – Package: version
- `-h`, `--help` – Print help

## 26.8. content-view filter update

update a filter

**Usage**

```
# hammer content-view filter update [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--description VALUE` – Description of the filter
- `--id NUMBER` – Filter identifier
- `--inclusion BOOLEAN` – Specifies if content should be included or excluded, default: inclusion=false
- `--name VALUE` – New name for the filter
- `--new-name VALUE` – New name for the filter
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--original-module-streams BOOLEAN` Add all module streams without errata to the included/excluded list. (module stream filter only)
- `--original-packages BOOLEAN` – Add all packages without errata to the included/excluded list. (package filter only)
- `--repositories LIST`
- `--repository-ids LIST` – List of repository ids
- `-h`, `--help` – Print help
