---
title: "task"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "89"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-task"
---
# Chapter 89. task

Tasks related actions.

**Usage**

```
# hammer task [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 89.1. task info

Show task details

**Usage**

```
# hammer task <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – UUID of the task
- `--location-id NUMBER` – Set the current location context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Action | x | x |
| State | x | x |
| Result | x | x |
| Started at | x | x |
| Ended at | x | x |
| Duration | x | x |
| Owner | x | x |
| Task errors | x | x |

## 89.2. task list

List tasks

**Usage**

```
# hammer task <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location-id NUMBER` – Set the current location context for the request
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization-id NUMBER` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--parent-task-id VALUE` – UUID of the task
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Action | x | x |
| State | x | x |
| Result | x | x |
| Started at | x | x |
| Ended at | x | x |
| Duration | x | x |
| Owner | x | x |
| Task errors | x | x |

## 89.3. task progress

Show the progress of the task

**Usage**

```
# hammer task progress [OPTIONS]
```

**Options**

- `--id VALUE` – UUID of the task
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 89.4. task resume

Resume all tasks paused in error state

**Usage**

```
# hammer task resume [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--search VALUE` – Resume tasks matching search string
- `--task-ids LIST` – Resume specific tasks by ID
- `--tasks LIST`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Total tasks found paused in error state | x | x |
| Total tasks resumed | x | x |
| Resumed tasks/task identifier | x | x |
| Resumed tasks/task action | x | x |
| Resumed tasks/task errors | x | x |
| Total tasks failed to resume | x | x |
| Failed tasks/task identifier | x | x |
| Failed tasks/task action | x | x |
| Failed tasks/task errors | x | x |
| Total tasks skipped | x | x |
| Skipped tasks/task identifier | x | x |
| Skipped tasks/task action | x | x |
| Skipped tasks/task errors | x | x |
