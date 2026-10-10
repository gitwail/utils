---
title: "settings"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "81"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-settings"
---
# Chapter 81. settings

Change server settings

**Usage**

```
# hammer settings [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 81.1. settings info

Show a setting

**Usage**

```
# hammer settings <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--name VALUE` – Setting name
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Description | x | x |  |
| Category | x | x |  |
| Settings type | x | x |  |
| Value | x | x |  |

## 81.2. settings list

List all settings

**Usage**

```
# hammer settings <list|index> [OPTIONS]
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
| Full name | x | x |  |
| Value | x | x |  |
| Description | x | x |  |

**Search and order fields**

- `description`
- `id` – integer
- `name` – string

## 81.3. settings set

Update a setting

**Usage**

```
# hammer settings set [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Setting name
- `--value VALUE`
- `-h`, `--help` – Print help
