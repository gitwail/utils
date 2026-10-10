---
title: "os"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "58"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-os"
---
# Chapter 58. os

Manipulate operating system

**Usage**

```
# hammer os [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 58.1. os add-architecture

Associate an architecture

**Usage**

```
# hammer os add-architecture [OPTIONS]
```

**Options**

- `--architecture VALUE` – Architecture name
- `--architecture-id NUMBER`
- `--id VALUE`
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

## 58.2. os add-provisioning-template

Associate provisioning templates

**Usage**

```
# hammer os add-provisioning-template [OPTIONS]
```

**Options**

- `--id VALUE`
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id NUMBER`
- `--provisioning-template-ids LIST` – List of provisioning template ids
- `--provisioning-template-search VALUE` Provisioning template name regex to search, all matching templates will be associated
- `--provisioning-templates LIST` – List of provisioning template names
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

## 58.3. os add-ptable

Associate a partition table

**Usage**

```
# hammer os add-ptable [OPTIONS]
```

**Options**

- `--id VALUE`
- `--partition-table VALUE` – Partition table name
- `--partition-table-id NUMBER`
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

## 58.4. os create

Create an operating system

**Usage**

```
# hammer os create [OPTIONS]
```

**Options**

- `--architecture-ids LIST` – IDs of associated architectures
- `--architectures LIST`
- `--description VALUE`
- `--family VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--major VALUE`
- `--media LIST`
- `--medium-ids LIST` – IDs of associated media
- `--minor VALUE`
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--os-parameters-attributes SCHEMA` Array of parameters
- `--partition-table-ids LIST` – IDs of associated partition tables
- `--partition-tables LIST`
- `--password-hash ENUM` – Root password hash function to use Possible value(s): `SHA512`, `SHA256`, `Base64`, `Base64-Windows`, `MD5`
- `--provisioning-template-ids LIST` IDs of associated provisioning templates
- `--provisioning-templates LIST`
- `--release-name VALUE`
- `-h`, `--help` – Print help

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--os-parameters-attributes` "**name**=<string>,**value**=<string>, …​ "

## 58.5. os delete

Delete an operating system

**Usage**

```
# hammer os <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

## 58.6. os delete-default-template

**Usage**

```
# hammer os delete-default-template [OPTIONS]
```

**Options**

- `--id VALUE` – Operatingsystem id
- `--type VALUE` – Type of the provisioning template
- `-h`, `--help` – Print help

## 58.7. os delete-parameter

Delete parameter for an operating system

**Usage**

```
# hammer os delete-parameter [OPTIONS]
```

**Options**

- `--name VALUE` – Parameter name
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 58.8. os info

Show an operating system

**Usage**

```
# hammer os <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--show-hidden-parameters BOOLEAN` Display hidden parameter values
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Title | x | x | x |
| Release name | x | x |  |
| Family | x | x |  |
| Name | x | x |  |
| Major version | x | x |  |
| Minor version | x | x |  |
| Partition tables/ | x | x |  |
| Default templates/ | x | x |  |
| Architectures/ | x | x |  |
| Installation media/ | x | x |  |
| Templates/ | x | x |  |
| Parameters/ | x | x |  |

## 58.9. os list

List all operating systems

**Usage**

```
# hammer os <list|index> [OPTIONS]
```

**Options**

- `--architecture VALUE` – Architecture name
- `--architecture-id VALUE` – ID of architecture
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--medium VALUE` – Medium name
- `--medium-id VALUE` – ID of medium
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--os-parameters-attributes SCHEMA` Array of parameters
- `--page NUMBER` – Page number, starting at 1
- `--partition-table VALUE` – Partition table name
- `--partition-table-id VALUE` – ID of partition table
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id VALUE` ID of template
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Title | x | x | x |
| Release name | x | x |  |
| Family | x | x |  |

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--os-parameters-attributes` "**name**=<string>,**value**=<string>, …​ "

**Search and order fields**

- `architecture` – string
- `description` – string
- `family` – string
- `id` – integer
- `major` – string
- `medium` – string
- `minor` – string
- `name` – string
- `params` – string
- `template` – string
- `title` – string

## 58.10. os remove-architecture

Disassociate an architecture

**Usage**

```
# hammer os remove-architecture [OPTIONS]
```

**Options**

- `--architecture VALUE` – Architecture name
- `--architecture-id NUMBER`
- `--id VALUE`
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

## 58.11. os remove-provisioning-template

Disassociate provisioning templates

**Usage**

```
# hammer os remove-provisioning-template [OPTIONS]
```

**Options**

- `--id VALUE`
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id NUMBER`
- `--provisioning-template-ids LIST` – List of provisioning template ids
- `--provisioning-template-search VALUE` Provisioning template name regex to search, all matching templates will be disassociated
- `--provisioning-templates LIST` – List of provisioning template names
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

## 58.12. os remove-ptable

Disassociate a partition table

**Usage**

```
# hammer os remove-ptable [OPTIONS]
```

**Options**

- `--id VALUE`
- `--partition-table VALUE` – Partition table name
- `--partition-table-id NUMBER`
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

## 58.13. os set-default-template

**Usage**

```
# hammer os set-default-template [OPTIONS]
```

**Options**

- `--id VALUE` – Operatingsystem id
- `--provisioning-template-id VALUE` Provisioning template id to be set
- `-h`, `--help` – Print help

## 58.14. os set-parameter

Create or update parameter for an operating system

**Usage**

```
# hammer os set-parameter [OPTIONS]
```

**Options**

- `--hidden-value BOOLEAN` – Should the value be hidden
- `--name VALUE` – Parameter name
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json` Default: "string"
- `--value VALUE` – Parameter value
- `-h`, `--help` – Print help

## 58.15. os update

Update an operating system

**Usage**

```
# hammer os update [OPTIONS]
```

**Options**

- `--architecture-ids LIST` – IDs of associated architectures
- `--architectures LIST`
- `--description VALUE`
- `--family VALUE`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--major VALUE`
- `--media LIST`
- `--medium-ids LIST` – IDs of associated media
- `--minor VALUE`
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--os-parameters-attributes SCHEMA` Array of parameters
- `--partition-table-ids LIST` – IDs of associated partition tables
- `--partition-tables LIST`
- `--password-hash ENUM` – Root password hash function to use Possible value(s): `SHA512`, `SHA256`, `Base64`, `Base64-Windows`, `MD5`
- `--provisioning-template-ids LIST` IDs of associated provisioning templates
- `--provisioning-templates LIST`
- `--release-name VALUE`
- `--title VALUE` – Operating system title
- `-h`, `--help` – Print help

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--os-parameters-attributes` "name=<string>,value=<string>, …​ "
