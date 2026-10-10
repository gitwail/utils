---
title: "product"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "66"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-product"
---
# Chapter 66. product

Manipulate products

**Usage**

```
# hammer product [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 66.1. product create

Create a product

**Usage**

```
# hammer product create [OPTIONS]
```

**Options**

- `--description VALUE` – Product description
- `--gpg-key-id NUMBER` – Identifier of the GPG key
- `--label VALUE`
- `--name VALUE` – Product name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – ID of the organization
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--ssl-ca-cert-id NUMBER` – Idenifier of the SSL CA Cert
- `--ssl-client-cert-id NUMBER` – Identifier of the SSL Client Cert
- `--ssl-client-key-id NUMBER` – Identifier of the SSL Client Key
- `--sync-plan VALUE` – Sync plan name to search by
- `--sync-plan-id NUMBER` – Plan numeric identifier
- `-h`, `--help` – Print help

## 66.2. product delete

Destroy a product

**Usage**

```
# hammer product <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – Product numeric identifier
- `--name VALUE` – Product name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 66.3. product info

Show a product

**Usage**

```
# hammer product <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Product numeric identifier
- `--name VALUE` – Product name to search by
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
| Label | x | x |  |
| Description | x | x |  |
| Sync state (all) | x | x |  |
| Sync state (last) | x | x |  |
| Sync plan id | x | x |  |
| Gpg/gpg key id | x | x |  |
| Gpg/gpg key | x | x |  |
| Organization | x | x |  |
| Readonly | x | x |  |
| Deletable | x | x |  |
| Content/repo name | x | x |  |
| Content/url | x | x |  |
| Content/content type | x | x |  |

## 66.4. product list

List products

**Usage**

```
# hammer product <list|index> [OPTIONS]
```

**Options**

- `--available-for VALUE` – Interpret specified object to return only Products that can be associated with specified object. Only `sync_plan` is supported.
- `--custom BOOLEAN` – Return custom products only
- `--enabled BOOLEAN` – Return enabled products only
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--include-available-content BOOLEAN` Whether to include available content attribute in results
- `--name VALUE` – Filter products by name
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Filter products by organization
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--redhat-only BOOLEAN` – Return Red Hat (non-custom) products only
- `--search VALUE` – Search string
- `--subscription VALUE` – Subscription name to search by
- `--subscription-id NUMBER` – Filter products by subscription
- `--sync-plan VALUE` – Sync plan name to search by
- `--sync-plan-id NUMBER` – Filter products by sync plan id
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Description | x | x |  |
| Organization | x | x |  |
| Repositories | x | x |  |
| Sync state | x | x |  |

**Search and order fields**

- `description` – text
- `label` – string
- `name` – string
- `organization_id` – integer
- `redhat` – Values: true, false

## 66.5. product remove-sync-plan

Delete assignment sync plan and product

**Usage**

```
# hammer product remove-sync-plan [OPTIONS]
```

**Options**

- `--description VALUE` – Product description
- `--gpg-key-id NUMBER` – Identifier of the GPG key
- `--id NUMBER` – Product numeric identifier
- `--name VALUE` – Product name
- `--new-name VALUE` – Product name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--ssl-ca-cert-id NUMBER` – Idenifier of the SSL CA Cert
- `--ssl-client-cert-id NUMBER` – Identifier of the SSL Client Cert
- `--ssl-client-key-id NUMBER` – Identifier of the SSL Client Key
- `-h`, `--help` – Print help

## 66.6. product set-sync-plan

Assign sync plan to product

**Usage**

```
# hammer product set-sync-plan [OPTIONS]
```

**Options**

- `--id NUMBER` – Product numeric identifier
- `--name VALUE` – Product name to search by
- `--new-name VALUE` – Product name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--ssl-ca-cert-id NUMBER` – Idenifier of the SSL CA Cert
- `--ssl-client-cert-id NUMBER` – Identifier of the SSL Client Cert
- `--ssl-client-key-id NUMBER` – Identifier of the SSL Client Key
- `--sync-plan VALUE` – Sync plan name to search by
- `--sync-plan-id NUMBER` – Plan numeric identifier
- `-h`, `--help` – Print help

## 66.7. product synchronize

Sync all repositories for a product

**Usage**

```
# hammer product synchronize [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Product ID
- `--name VALUE` – Product name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 66.8. product update

Updates a product

**Usage**

```
# hammer product update [OPTIONS]
```

**Options**

- `--description VALUE` – Product description
- `--gpg-key-id NUMBER` – Identifier of the GPG key
- `--id NUMBER` – Product numeric identifier
- `--name VALUE` – Product name
- `--new-name VALUE` – Product name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--ssl-ca-cert-id NUMBER` – Idenifier of the SSL CA Cert
- `--ssl-client-cert-id NUMBER` – Identifier of the SSL Client Cert
- `--ssl-client-key-id NUMBER` – Identifier of the SSL Client Key
- `--sync-plan VALUE` – Sync plan name to search by
- `--sync-plan-id NUMBER` – Plan numeric identifier
- `-h`, `--help` – Print help

## 66.9. product update-proxy

Updates an HTTP Proxy for a product

**Usage**

```
# hammer product update-proxy [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – HTTP proxy identifier to associated
- `--http-proxy-policy ENUM` – Policy for HTTP proxy for content sync Possible value(s): `global_default_http_proxy`, `none`, `use_selected_http_proxy`
- `--ids LIST` – List of product ids
- `-h`, `--help` – Print help

## 66.10. product verify-checksum

Verify checksum for one or more products

**Usage**

```
# hammer product verify-checksum [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--ids LIST` – List of product ids
- `-h`, `--help` – Print help
