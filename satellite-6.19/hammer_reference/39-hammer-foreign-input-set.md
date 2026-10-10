---
title: "foreign-input-set"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "39"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-foreign-input-set"
---
# Chapter 39. foreign-input-set

Manage foreign input sets

**Usage**

```
# hammer foreign-input-set [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 39.1. foreign-input-set create

Create a foreign input set

**Usage**

```
# hammer foreign-input-set create [OPTIONS]
```

**Options**

- `--description VALUE` – Input set description
- `--exclude VALUE` – A comma separated list of input names to be included from the foreign template.
- `--include VALUE` – A comma separated list of input names to be included from the foreign template.
- `--include-all BOOLEAN` – Include all inputs from the foreign template
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--target-template-id VALUE` – Target template ID
- `--template-id VALUE`
- `-h`, `--help` – Print help

## 39.2. foreign-input-set delete

Delete a foreign input set

**Usage**

```
# hammer foreign-input-set <delete|destroy> [OPTIONS]
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
- `--template-id VALUE`
- `-h`, `--help` – Print help

## 39.3. foreign-input-set info

Show foreign input set details

**Usage**

```
# hammer foreign-input-set <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--template-id VALUE`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Target template id | x | x |  |
| Target template name | x | x |  |
| Include all | x | x |  |
| Include | x | x |  |
| Exclude | x | x |  |

## 39.4. foreign-input-set list

List foreign input sets

**Usage**

```
# hammer foreign-input-set <list|index> [OPTIONS]
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
- `--template-id VALUE`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Target template id | x | x |
| Target template name | x | x |

## 39.5. foreign-input-set update

Update a foreign input set

**Usage**

```
# hammer foreign-input-set update [OPTIONS]
```

**Options**

- `--description VALUE` – Input set description
- `--exclude VALUE` – A comma separated list of input names to be included from the foreign template.
- `--id VALUE`
- `--include VALUE` – A comma separated list of input names to be included from the foreign template.
- `--include-all BOOLEAN` – Include all inputs from the foreign template
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--target-template-id VALUE` – Target template ID
- `--template-id VALUE`
- `-h`, `--help` – Print help
