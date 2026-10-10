---
title: "repository-set"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "76"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-repository-set"
---
# Chapter 76. repository-set

Manipulate repository sets on the server

**Usage**

```
# hammer repository-set [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 76.1. repository-set available-repositories

Get list of available repositories for the repository set

**Usage**

```
# hammer repository-set available-repositories [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – ID of the repository set
- `--name VALUE` – Repository set name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – ID of a product to list repository sets from
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Name | x | x | x |
| Arch | x | x |  |
| Release | x | x |  |
| Registry name | x | x |  |
| Enabled | x | x |  |

## 76.2. repository-set disable

Disable a repository from the set

**Usage**

```
# hammer repository-set disable [OPTIONS]
```

**Options**

- `--basearch VALUE` – Basearch to disable
- `--id NUMBER` – ID of the repository set to disable
- `--name VALUE` – Repository set name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – ID of the product containing the repository set
- `--releasever VALUE` – Releasever to disable
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – ID of the repository within the set to disable
- `-h`, `--help` – Print help

## 76.3. repository-set enable

Enable a repository from the set

**Usage**

```
# hammer repository-set enable [OPTIONS]
```

**Options**

- `--basearch VALUE` – Basearch to enable
- `--id NUMBER` – ID of the repository set to enable
- `--name VALUE` – Repository set name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – ID of the product containing the repository set
- `--releasever VALUE` – Releasever to enable
- `-h`, `--help` – Print help

## 76.4. repository-set info

Get info about a repository set

**Usage**

```
# hammer repository-set <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – ID of the repository set
- `--name VALUE` – Repository set name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – ID of a product to list repository sets from
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Type | x | x |  |
| Url | x | x |  |
| Gpg key | x | x |  |
| Label | x | x |  |
| Enabled repositories/id | x | x |  |
| Enabled repositories/name | x | x |  |

## 76.5. repository-set list

List repository sets.

**Usage**

```
# hammer repository-set <list|index> [OPTIONS]
```

**Options**

- `--activation-key VALUE` – Activation key name to search by
- `--activation-key-id NUMBER` – Activation key identifier
- `--content-access-mode-all BOOLEAN` Get all content available, not just that provided by subscriptions.
- `--content-access-mode-env BOOLEAN` Limit content to just that available in the host`s or activation key`s content view version and lifecycle environment.
- `--enabled BOOLEAN` – If true, only return repository sets that have been enabled. Defaults to false
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – Id of the host
- `--name VALUE` – Repository set name to search on
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – ID of a product to list repository sets from
- `--repository-type ENUM` – Limit content to Red Hat / custom Possible value(s): `redhat`, `custom`
- `--search VALUE` – Search string
- `--status ENUM` – Limit content to enabled / disabled / overridden Possible value(s): `enabled`, `disabled`, `overridden`
- `--with-active-subscription BOOLEAN` If true, only return repository sets that are associated with an active subscriptions
- `--with-custom BOOLEAN` – If true, return custom repository sets along with redhat repos. Will be ignored if repository_type is supplied.
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Type | x | x |  |
| Name | x | x | x |

**Search and order fields**

- `content_label` – string
- `content_type` – string
- `enabled_by_default` – Values: true, false
- `label` – string
- `name` – string
- `path` – string
- `product` – string
- `product_id` – integer
- `product_name` – string
- `redhat` – Values: true, false
