---
title: "scap-content"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "79"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-scap-content"
---
# Chapter 79. scap-content

Manipulate SCAP contents

**Usage**

```
# hammer scap-content [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 79.1. scap-content bulk-upload

Upload scap contents in bulk

**Usage**

```
# hammer scap-content bulk-upload [OPTIONS]
```

**Options**

- `--directory VALUE` – Directory to upload when using “directory” upload type
- `--files LIST` – File paths to upload when using “files” upload type
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--type ENUM` – Type of the upload Possible value(s): `files`, `directory`, `default`
- `-h`, `--help` – Print help

## 79.2. scap-content create

Create SCAP content

**Usage**

```
# hammer scap-content create [OPTIONS]
```

**Options**

- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--locations LIST`
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organizations LIST`
- `--original-filename VALUE` – Original file name of the XML file
- `--scap-file FILE` – SCAP content file
- `--title VALUE` – SCAP content name
- `-h`, `--help` – Print help

## 79.3. scap-content delete

Deletes an SCAP content

**Usage**

```
# hammer scap-content <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--title VALUE` – SCAP content title
- `-h`, `--help` – Print help

## 79.4. scap-content download

Download an SCAP content as XML

**Usage**

```
# hammer scap-content download [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--path VALUE` – Path to directory where downloaded file will be saved
- `--title VALUE` – SCAP content title
- `-h`, `--help` – Print help

## 79.5. scap-content info

Show an SCAP content

**Usage**

```
# hammer scap-content <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--title VALUE` – SCAP content title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Title | x | x | x |
| Digest | x | x |  |
| Created at | x | x |  |
| Original filename | x | x |  |
| Scap content profiles/id | x | x |  |
| Scap content profiles/profile id | x | x |  |
| Scap content profiles/title | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |

## 79.6. scap-content list

List SCAP contents

**Usage**

```
# hammer scap-content <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Title | x | x | x |
| Digest | x | x |  |

**Search and order fields**

- `created_at` – datetime
- `filename` – string
- `location` – string
- `location_id` – integer
- `organization` – string
- `organization_id` – integer
- `title` – string

## 79.7. scap-content update

Update an SCAP content

**Usage**

```
# hammer scap-content update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--locations LIST`
- `--new-title VALUE` – SCAP content name
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organizations LIST`
- `--original-filename VALUE` – Original file name of the XML file
- `--scap-file FILE` – SCAP content file
- `--title VALUE` – SCAP content name
- `-h`, `--help` – Print help
