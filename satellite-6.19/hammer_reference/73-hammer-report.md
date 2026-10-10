---
title: "report"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "73"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-report"
---
# Chapter 73. report

Browse and read reports

**Usage**

```
# hammer report [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 73.1. report delete

Delete a report

**Usage**

```
# hammer report <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 73.2. report info

Show a report

**Usage**

```
# hammer report <info|show> [OPTIONS]
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
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Host | x | x |  |
| Reported at | x | x |  |
| Origin | x | x |  |
| Report status/applied | x | x |  |
| Report status/restarted | x | x |  |
| Report status/failed | x | x |  |
| Report status/restart failures | x | x |  |
| Report status/skipped | x | x |  |
| Report status/pending | x | x |  |
| Report metrics/config retrieval | x | x |  |
| Report metrics/exec | x | x |  |
| Report metrics/file | x | x |  |
| Report metrics/package | x | x |  |
| Report metrics/service | x | x |  |
| Report metrics/user | x | x |  |
| Report metrics/yumrepo | x | x |  |
| Report metrics/filebucket | x | x |  |
| Report metrics/cron | x | x |  |
| Report metrics/total | x | x |  |
| Logs/resource | x | x |  |
| Logs/message | x | x |  |

## 73.3. report list

List all reports

**Usage**

```
# hammer report <list|index> [OPTIONS]
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

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Host | x | x |  |
| Last report | x | x |  |
| Origin | x | x |  |
| Applied | x | x |  |
| Restarted | x | x |  |
| Failed | x | x |  |
| Restart failures | x | x |  |
| Skipped | x | x |  |
| Pending | x | x |  |

**Search and order fields**

- `applied` – integer
- `eventful` – Values: true, false
- `failed` – integer
- `failed_restarts` – integer
- `host` – string
- `host_id` – integer
- `host_owner_id` – integer
- `hostgroup` – string
- `hostgroup_fullname` – string
- `hostgroup_title` – string
- `id` – integer
- `last_report` – datetime
- `location` – string
- `log` – text
- `organization` – string
- `origin` – string
- `pending` – integer
- `reported` – datetime
- `resource` – text
- `restarted` – integer
- `skipped` – integer

**Search and order fields**

- `applied` – integer
- `eventful` – Values: true, false
- `failed` – integer
- `failed_restarts` – integer
- `host` – string
- `host_id` – integer
- `host_owner_id` – integer
- `hostgroup` – string
- `hostgroup_fullname` – string
- `hostgroup_title` – string
- `id` – integer
- `last_report` – datetime
- `location` – string
- `log` – text
- `organization` – string
- `origin` – string
- `pending` – integer
- `reported` – datetime
- `resource` – text
- `restarted` – integer
- `skipped` – integer
