---
title: "puppet-environment"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "69"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-puppet-environment"
---
# Chapter 69. puppet-environment

Manage Foreman Puppet environments

**Usage**

```
# hammer puppet-environment [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 69.1. puppet-environment create

Create an environment

**Usage**

```
# hammer puppet-environment create [OPTIONS]
```

**Options**

- `--location-ids LIST` – REPLACE locations with given ids
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE`
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-titles LIST`
- `--organizations LIST`
- `-h`, `--help` – Print help

## 69.2. puppet-environment delete

Delete an environment

**Usage**

```
# hammer puppet-environment <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Puppet environment name
- `-h`, `--help` – Print help

## 69.3. puppet-environment info

Show an environment

**Usage**

```
# hammer puppet-environment <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--name VALUE` – Puppet environment name
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Puppetclasses/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 69.4. puppet-environment list

List all environments

**Usage**

```
# hammer puppet-environment <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Scope by locations
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Scope by organizations
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--puppet-class VALUE` – Puppet class name
- `--puppet-class-id VALUE` – ID of Puppet class
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

**Search and order fields**

- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer

## 69.5. puppet-environment sc-params

List all smart class parameters

**Usage**

```
# hammer puppet-environment sc-params [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--puppet-environment VALUE` – Puppet environment name
- `--puppet-environment-id NUMBER`
- `--search VALUE` – Filter results
- `--show-hidden BOOLEAN` – Display hidden values
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Parameter | x | x |
| Default value | x | x |
| Override | x | x |
| Puppet class | x | x |
| Class id | x | x |

**Search and order fields**

- `avoid_duplicates` – Values: true, false
- `environment` – string
- `key` – string
- `merge_default` – Values: true, false
- `merge_overrides` – Values: true, false
- `override` – Values: true, false
- `parameter` – string
- `puppetclass` – string
- `puppetclass_name` – string

## 69.6. puppet-environment update

Update an environment

**Usage**

```
# hammer puppet-environment update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE`
- `--new-name VALUE`
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-titles LIST`
- `--organizations LIST`
- `-h`, `--help` – Print help
