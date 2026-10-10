---
title: "architecture"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-architecture"
---
# Chapter 7. architecture

Manipulate architectures

**Usage**

```
# hammer architecture [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 7.1. architecture add-operatingsystem

Associate an operating system

**Usage**

```
# hammer architecture add-operatingsystem [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Architecture name
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 7.2. architecture create

Create an architecture

**Usage**

```
# hammer architecture create [OPTIONS]
```

**Options**

- `--name VALUE`
- `--operatingsystem-ids LIST` – Operating system IDs
- `--operatingsystems LIST`
- `-h`, `--help` – Print help

## 7.3. architecture delete

Delete an architecture

**Usage**

```
# hammer architecture <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Architecture name
- `-h`, `--help` – Print help

## 7.4. architecture info

Show an architecture

**Usage**

```
# hammer architecture <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--name VALUE` – Architecture name
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Operating systems/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 7.5. architecture list

List all architectures

**Usage**

```
# hammer architecture <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – ID of operating system
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

- `id` – integer
- `name` – string

## 7.6. architecture remove-operatingsystem

Disassociate an operating system

**Usage**

```
# hammer architecture remove-operatingsystem [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Architecture name
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 7.7. architecture update

Update an architecture

**Usage**

```
# hammer architecture update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE`
- `--new-name VALUE`
- `--operatingsystem-ids LIST` – Operating system IDs
- `--operatingsystems LIST`
- `-h`, `--help` – Print help
