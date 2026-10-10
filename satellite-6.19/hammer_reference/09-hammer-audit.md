---
title: "audit"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-audit"
---
# Chapter 9. audit

Search audit trails.

**Usage**

```
# hammer audit [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 9.1. audit info

Show an audit

**Usage**

```
# hammer audit <info|show> [OPTIONS]
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
| At | x | x |  |
| Ip | x | x |  |
| User | x | x |  |
| Action | x | x |  |
| Audit type | x | x |  |
| Audit record | x | x |  |
| Request uuid | x | x |  |
| Audited changes/attribute | x | x |  |
| Audited changes/value | x | x |  |
| Audited changes/old | x | x |  |
| Audited changes/new | x | x |  |

## 9.2. audit list

List all audits

**Usage**

```
# hammer audit <list|index> [OPTIONS]
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
| At | x | x |  |
| Ip | x | x |  |
| User | x | x |  |
| Action | x | x |  |
| Audit type | x | x |  |
| Audit record | x | x |  |
| Request uuid | x |  |  |

**Search and order fields**

- `location` – string
- `location_id` – integer
- `organization` – string
- `organization_id` – integer
