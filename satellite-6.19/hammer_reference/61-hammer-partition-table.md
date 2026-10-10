---
title: "partition-table"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "61"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-partition-table"
---
# Chapter 61. partition-table

Manipulate partition tables

**Usage**

```
# hammer partition-table [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 61.1. partition-table add-operatingsystem

Associate an operating system

**Usage**

```
# hammer partition-table add-operatingsystem [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Partition table name
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 61.2. partition-table create

Create a partition table

**Usage**

```
# hammer partition-table create [OPTIONS]
```

**Options**

- `--audit-comment VALUE`
- `--description VALUE`
- `--file FILE` – Path to a file that contains the partition layout
- `--host-ids LIST` – Array of host IDs to associate with the partition table
- `--hostgroup-ids LIST` – Array of host group IDs to associate with the partition table
- `--hostgroup-titles LIST`
- `--hostgroups LIST`
- `--hosts LIST`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--locked BOOLEAN` – Whether or not the template is locked for editing
- `--name VALUE`
- `--operatingsystem-ids LIST` – Array of operating system IDs to associate with the partition table
- `--operatingsystems LIST`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--os-family VALUE`
- `--snippet BOOLEAN`
- `-h`, `--help` – Print help

## 61.3. partition-table delete

Delete a partition table

**Usage**

```
# hammer partition-table <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Partition table name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 61.4. partition-table dump

View partition table content

**Usage**

```
# hammer partition-table dump [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Partition table name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

|  |
| --- |
| FIELDS |

## 61.5. partition-table export

Export a partition template to ERB

**Usage**

```
# hammer partition-table export [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Partition table name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--path VALUE` – Path to directory where downloaded content will be saved
- `-h`, `--help` – Print help

## 61.6. partition-table import

Import a partition table

**Usage**

```
# hammer partition-table import [OPTIONS]
```

**Options**

- `--associate ENUM` – Determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata Possible value(s): `new`, `always`, `never`
- `--default BOOLEAN` – Makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default)
- `--file FILE` – Path to a file that contains the template content including metadata
- `--force BOOLEAN` – Use if you want update locked templates
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--lock BOOLEAN` – Lock imported templates (false by default)
- `--name VALUE` – Template name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `-h`, `--help` – Print help

## 61.7. partition-table info

Show a partition table

**Usage**

```
# hammer partition-table <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Partition table name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Os family | x | x |  |
| Description | x | x |  |
| Locked | x | x |  |
| Operating systems/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |

## 61.8. partition-table list

List all partition tables

**Usage**

```
# hammer partition-table <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Scope by locations
- `--location-title VALUE` – Set the current location context for the request
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – ID of operating system
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Scope by organizations
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
| Os family | x | x |  |

**Search and order fields**

- `default` – Values: true, false
- `family` – string
- `id` – integer
- `layout` – text
- `location` – string
- `location_id` – integer
- `locked` – Values: true, false
- `name` – string
- `organization` – string
- `organization_id` – integer
- `snippet` – Values: true, false
- `template` – text
- `vendor` – string

## 61.9. partition-table remove-operatingsystem

Disassociate an operating system

**Usage**

```
# hammer partition-table remove-operatingsystem [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Partition table name
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 61.10. partition-table update

Update a partition table

**Usage**

```
# hammer partition-table update [OPTIONS]
```

**Options**

- `--audit-comment VALUE`
- `--description VALUE`
- `--file FILE` – Path to a file that contains the partition layout
- `--host-ids LIST` – Array of host IDs to associate with the partition table
- `--hostgroup-ids LIST` – Array of host group IDs to associate with the partition table
- `--hostgroup-titles LIST`
- `--hostgroups LIST`
- `--hosts LIST`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--locked BOOLEAN` – Whether or not the template is locked for editing
- `--name VALUE`
- `--new-name VALUE`
- `--operatingsystem-ids LIST` – Array of operating system IDs to associate with the partition table
- `--operatingsystems LIST`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--os-family VALUE`
- `--snippet BOOLEAN`
- `-h`, `--help` – Print help
