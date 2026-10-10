---
title: "sync-plan"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "87"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-sync-plan"
---
# Chapter 87. sync-plan

Manipulate sync plans

**Usage**

```
# hammer sync-plan [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 87.1. sync-plan create

Create a sync plan

**Usage**

```
# hammer sync-plan create [OPTIONS]
```

**Options**

- `--cron-expression VALUE` – Set this when interval is custom cron
- `--description VALUE` – Sync plan description
- `--enabled BOOLEAN` – Enables or disables synchronization
- `--interval VALUE` – How often synchronization should run
- `--name VALUE` – Sync plan name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--sync-date DATETIME` – Start date and time for the sync plan.Time is optional, if kept blank current system time will be considered
- `-h`, `--help` – Print help

## 87.2. sync-plan delete

Destroy a sync plan

**Usage**

```
# hammer sync-plan <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – Sync plan numeric identifier
- `--name VALUE` – Sync plan name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 87.3. sync-plan info

Show a sync plan

**Usage**

```
# hammer sync-plan <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Sync plan numeric identifier
- `--name VALUE` – Sync plan name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Start date | x | x |  |
| Interval | x | x |  |
| Enabled | x | x |  |
| Cron expression | x | x |  |
| Recurring logic id | x | x |  |
| Description | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |
| Next sync | x | x |  |
| Products/id | x | x |  |
| Products/name | x | x |  |

## 87.4. sync-plan list

List sync plans

**Usage**

```
# hammer sync-plan <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--interval ENUM` – Filter by interval Possible value(s): `hourly`, `daily`, `weekly`, `custom cron`
- `--name VALUE` – Filter by name
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--sync-date VALUE` – Filter by sync date
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Start date | x | x |  |
| Interval | x | x |  |
| Enabled | x | x |  |
| Cron expression | x | x |  |
| Recurring logic id | x | x |  |

**Search and order fields**

- `enabled` – Values: true, false
- `interval` – string
- `name` – string
- `organization_id` – integer

## 87.5. sync-plan update

Update a sync plan

**Usage**

```
# hammer sync-plan update [OPTIONS]
```

**Options**

- `--cron-expression VALUE` – Add custom cron logic for sync plan
- `--description VALUE` – Sync plan description
- `--enabled BOOLEAN` – Enables or disables synchronization
- `--id NUMBER` – Sync plan numeric identifier
- `--interval VALUE` – How often synchronization should run
- `--name VALUE` – Sync plan name
- `--new-name VALUE` – Sync plan name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--sync-date DATETIME` – Start date and time of the synchronization
- `-h`, `--help` – Print help
