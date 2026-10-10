---
title: "recurring-logic"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "71"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-recurring-logic"
---
# Chapter 71. recurring-logic

Recurring logic related actions

**Usage**

```
# hammer recurring-logic [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 71.1. recurring-logic cancel

Cancel recurring logic

**Usage**

```
# hammer recurring-logic cancel [OPTIONS]
```

**Options**

- `--id VALUE` – ID of the recurring logic
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 71.2. recurring-logic delete

Delete all recuring logics filtered by the arguments

**Usage**

```
# hammer recurring-logic delete [OPTIONS]
```

**Options**

- `--cancelled` – Only delete cancelled recurring logics
- `--finished` – Only delete finished recurring logics
- `-h`, `--help` – Print help

## 71.3. recurring-logic info

Show recurring logic details

**Usage**

```
# hammer recurring-logic <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – ID of the recurring logic
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Cron line | x | x |
| Action | x | x |
| Last occurrence | x | x |
| Next occurrence | x | x |
| Task count | x | x |
| Action | x | x |
| Last occurrence | x | x |
| Next occurrence | x | x |
| Iteration | x | x |
| Iteration limit | x | x |
| Iteration limit | x | x |
| Repeat until | x | x |
| State | x | x |
| Purpose | x | x |

## 71.4. recurring-logic list

List recurring logics

**Usage**

```
# hammer recurring-logic <list|index> [OPTIONS]
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

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Cron line | x | x |
| Task count | x | x |
| Action | x | x |
| Last occurrence | x | x |
| Next occurrence | x | x |
| Iteration | x | x |
| Iteration limit | x | x |
| End time | x | x |
| State | x | x |
| Purpose | x | x |
