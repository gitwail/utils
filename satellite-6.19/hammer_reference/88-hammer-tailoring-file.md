---
title: "tailoring-file"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "88"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-tailoring-file"
---
# Chapter 88. tailoring-file

Manipulate Tailoring files

**Usage**

```
# hammer tailoring-file [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 88.1. tailoring-file create

Create a Tailoring file

**Usage**

```
# hammer tailoring-file create [OPTIONS]
```

**Options**

- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--locations LIST`
- `--name VALUE` – Tailoring file name
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organizations LIST`
- `--original-filename VALUE` – Original file name of the XML file
- `--scap-file FILE` – Tailoring file content
- `-h`, `--help` – Print help

## 88.2. tailoring-file delete

Deletes a Tailoring file

**Usage**

```
# hammer tailoring-file <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 88.3. tailoring-file download

Download a Tailoring file as XML

**Usage**

```
# hammer tailoring-file download [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--name VALUE` – Tailoring file name
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--path VALUE` – Path to directory where downloaded file will be saved
- `-h`, `--help` – Print help

## 88.4. tailoring-file info

Show a Tailoring file

**Usage**

```
# hammer tailoring-file <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--name VALUE` – Tailoring file name
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Created at | x | x |  |
| Original filename | x | x |  |
| Tailoring file profiles/id | x | x |  |
| Tailoring file profiles/profile id | x | x |  |
| Tailoring file profiles/title | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |

## 88.5. tailoring-file list

List Tailoring files

**Usage**

```
# hammer tailoring-file <list|index> [OPTIONS]
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
| Name | x | x | x |

**Search and order fields**

- `created_at` – datetime
- `filename` – string
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer

## 88.6. tailoring-file update

Update a Tailoring file

**Usage**

```
# hammer tailoring-file update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--locations LIST`
- `--name VALUE` – Tailoring file name
- `--new-name VALUE` – Tailoring file name
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organizations LIST`
- `--original-filename VALUE` – Original file name of the XML file
- `--scap-file FILE` – Tailoring file content
- `-h`, `--help` – Print help
