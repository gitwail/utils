---
title: "config-group"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "17"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-config-group"
---
# Chapter 17. config-group

Manage Foreman config groups

**Usage**

```
# hammer config-group [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 17.1. config-group create

Create a config group

**Usage**

```
# hammer config-group create [OPTIONS]
```

**Options**

- `--name VALUE`
- `--puppet-class-ids LIST`
- `--puppet-classes LIST`
- `-h`, `--help` – Print help

## 17.2. config-group delete

Delete a config group

**Usage**

```
# hammer config-group <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

## 17.3. config-group info

Show a config group

**Usage**

```
# hammer config-group <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Puppetclasses/ | x | x |  |

## 17.4. config-group list

List of config groups

**Usage**

```
# hammer config-group <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
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

- `name` – string
- `puppetclass` – string

## 17.5. config-group update

Update a config group

**Usage**

```
# hammer config-group update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE`
- `--new-name VALUE`
- `--puppet-class-ids LIST`
- `--puppet-classes LIST`
- `-h`, `--help` – Print help
