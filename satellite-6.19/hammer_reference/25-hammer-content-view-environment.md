---
title: "content-view-environment"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "25"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-content-view-environment"
---
# Chapter 25. content-view-environment

Manipulate content view environments

**Usage**

```
# hammer content-view-environment [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 25.1. content-view-environment list

List content view environments

**Usage**

```
# hammer content-view-environment <list|index> [OPTIONS]
```

**Options**

- `--activation-key VALUE` – Activation key name to search by
- `--activation-key-id NUMBER` – Activation key identifier
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – Host identifier
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Environment identifier
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Label | x | x |  |
| Lifecycle environment | x | x | x |
| Content view | x | x |  |
| Default | x | x |  |
| Hosts count | x | x |  |
| Activation keys count | x | x |  |
| Organization | x | x |  |
