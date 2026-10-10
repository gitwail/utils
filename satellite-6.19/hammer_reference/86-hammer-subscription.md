---
title: "subscription"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "86"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-subscription"
---
# Chapter 86. subscription

Manipulate subscriptions

**Usage**

```
# hammer subscription [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 86.1. subscription delete-manifest

Delete manifest from Red Hat provider

**Usage**

```
# hammer subscription delete-manifest [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization id
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 86.2. subscription list

List organization subscriptions

**Usage**

```
# hammer subscription <list|index> [OPTIONS]
```

**Options**

- `--activation-key VALUE` – Activation key name to search by
- `--activation-key-id VALUE` – Activation key ID
- `--available-for VALUE` – Object to show subscriptions available for, either `host` or `activation_key`
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id VALUE` – Id of a host
- `--match-host BOOLEAN` – Ignore subscriptions that are unavailable to the specified host
- `--match-installed BOOLEAN` – Return subscriptions that match installed products of the specified host
- `--name VALUE` – Name of the subscription
- `--no-overlap BOOLEAN` – Return subscriptions which do not overlap with a currently-attached subscription
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Uuid | x | x |
| Name | x | x |
| Type | x | x |
| Contract | x | x |
| Account | x | x |
| Support | x | x |
| Start date | x | x |
| End date | x | x |
| Quantity | x | x |
| Consumed | x | x |
| Product host count | x | x |

## 86.3. subscription manifest-history

obtain manifest history for subscriptions

**Usage**

```
# hammer subscription manifest-history [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Status | x | x |
| Status message | x | x |
| Time | x | x |

## 86.4. subscription refresh-manifest

Refresh previously imported manifest for Red Hat provider

**Usage**

```
# hammer subscription refresh-manifest [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization id
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 86.5. subscription upload

Upload a subscription manifest

**Usage**

```
# hammer subscription upload [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--file FILE` – Subscription manifest file
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization id
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help
