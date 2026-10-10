---
title: "global-parameter"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "41"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-global-parameter"
---
# Chapter 41. global-parameter

Manipulate global parameters

**Usage**

```
# hammer global-parameter [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 41.1. global-parameter delete

Delete a global parameter

**Usage**

```
# hammer global-parameter <delete|destroy> [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Common parameter name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 41.2. global-parameter list

List all global parameters

**Usage**

```
# hammer global-parameter <list|index> [OPTIONS]
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
- `--show-hidden BOOLEAN` – Display hidden values
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Name | x | x | x |
| Value | x | x |  |
| Type | x | x |  |

**Search and order fields**

- `domain_name` – string
- `host_group_name` – string
- `host_name` – string
- `id` – integer
- `key_type` – string
- `location_name` – string
- `name` – string
- `organization_name` – string
- `os_name` – string
- `parameter_type` – string
- `subnet_name` – text
- `type` – string
- `value` – text

## 41.3. global-parameter set

Set a global parameter

**Usage**

```
# hammer global-parameter set [OPTIONS]
```

**Options**

- `--hidden-value BOOLEAN` – Should the value be hidden
- `--name VALUE` – Parameter name
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json` Default: "string"
- `--value VALUE` – Parameter value
- `-h`, `--help` – Print help
