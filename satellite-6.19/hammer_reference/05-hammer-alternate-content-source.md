---
title: "alternate-content-source"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-alternate-content-source"
---
# Chapter 5. alternate-content-source

Manipulate alternate content sources

**Usage**

```
# hammer alternate-content-source [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 5.1. alternate-content-source bulk

Modify alternate content sources in bulk

**Usage**

```
# hammer alternate-content-source bulk [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 5.1.1. alternate-content-source bulk destroy

Destroy alternate content sources

**Usage**

```
# hammer alternate-content-source bulk destroy [OPTIONS]
```

**Options**

- `--ids LIST` – List of alternate content source IDs
- `-h`, `--help` – Print help

### 5.1.2. alternate-content-source bulk refresh

Refresh alternate content sources

**Usage**

```
# hammer alternate-content-source bulk refresh [OPTIONS]
```

**Options**

- `--ids LIST` – List of alternate content source IDs
- `-h`, `--help` – Print help

### 5.1.3. alternate-content-source bulk refresh-all

Refresh all alternate content sources

**Usage**

```
# hammer alternate-content-source bulk refresh-all [OPTIONS]
```

**Options**

- `-h`, `--help` – Print help

## 5.2. alternate-content-source create

Create an alternate content source to download content from during repository syncing. Note: alternate content sources are global and affect ALL sync actions on their Capsules regardless of organization.

**Usage**

```
# hammer alternate-content-source create [OPTIONS]
```

**Options**

- `--alternate-content-source-type ENUM` The Alternate Content Source type Possible value(s): `custom`, `simplified`, `rhui`
- `--base-url VALUE` – Base URL for finding alternate content
- `--content-type ENUM` – The content type for the Alternate Content Source Possible value(s): `file`, `yum`
- `--description VALUE` – Description for the alternate content source
- `--name VALUE` – Name of the alternate content source
- `--product-ids LIST` – IDs of products to copy repository information from into a Simplified Alternate Content Source. Products must include at least one repository of the chosen content type.
- `--smart-proxies LIST`
- `--smart-proxy-ids LIST` – Ids of Capsules to associate
- `--smart-proxy-names LIST` – Names of Capsules to associate
- `--ssl-ca-cert-id NUMBER` – Identifier of the content credential containing the SSL CA Cert
- `--ssl-client-cert-id NUMBER` – Identifier of the content credential containing the SSL Client Cert
- `--ssl-client-key-id NUMBER` – Identifier of the content credential containing the SSL Client Key
- `--subpaths LIST` – Path suffixes for finding alternate content
- `--upstream-password VALUE` – Basic authentication password
- `--upstream-username VALUE` – Basic authentication username
- `--use-http-proxies BOOLEAN` – If the Capsules` assigned HTTP proxies should be used
- `--verify-ssl BOOLEAN` – If SSL should be verified for the upstream URL
- `-h`, `--help` – Print help

## 5.3. alternate-content-source delete

Destroy an alternate content source.

**Usage**

```
# hammer alternate-content-source <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – Alternate content source ID
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

## 5.4. alternate-content-source info

Show an alternate content source.

**Usage**

```
# hammer alternate-content-source <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Alternate content source ID
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Label | x | x |  |
| Description | x | x |  |
| Base url | x | x |  |
| Content type | x | x |  |
| Alternate content source type | x | x |  |
| Upstream username | x | x |  |
| Verify ssl | x | x |  |
| Ssl ca cert/id | x | x |  |
| Ssl ca cert/name | x | x |  |
| Ssl client cert/id | x | x |  |
| Ssl client cert/name | x | x |  |
| Ssl client key/id | x | x |  |
| Ssl client key/name | x | x |  |
| Subpaths/ | x | x |  |
| Products/id | x | x |  |
| Products/organization id | x | x |  |
| Products/name | x | x |  |
| Products/label | x | x |  |
| Smart proxies/id | x | x |  |
| Smart proxies/name | x | x |  |
| Smart proxies/url | x | x |  |
| Smart proxies/download policy | x | x |  |

## 5.5. alternate-content-source list

List alternate content sources.

**Usage**

```
# hammer alternate-content-source <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--name VALUE` – Name of the alternate content source
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Type | x | x |  |

**Search and order fields**

- `alternate_content_source_type` – string
- `base_url` – string
- `content_type` – string
- `description` – text
- `label` – string
- `name` – string
- `product_id` – integer
- `product_name` – string
- `smart_proxy_id` – integer
- `smart_proxy_name` – string
- `subpath` – string
- `upstream_username` – string

## 5.6. alternate-content-source refresh

Refresh an alternate content source. Refreshing, like repository syncing, is required before using an alternate content source.

**Usage**

```
# hammer alternate-content-source refresh [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Alternate content source ID
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

## 5.7. alternate-content-source update

Update an alternate content source.

**Usage**

```
# hammer alternate-content-source update [OPTIONS]
```

**Options**

- `--base-url VALUE` – Base URL for finding alternate content
- `--description VALUE` – Description for the alternate content source
- `--id NUMBER` – Alternate content source ID
- `--name VALUE` – Name of the alternate content source
- `--new-name VALUE` – Name of the alternate content source
- `--product-ids LIST` – IDs of products to copy repository information from into a Simplified Alternate Content Source. Products must include at least one repository of the chosen content type.
- `--products LIST`
- `--smart-proxies LIST`
- `--smart-proxy-ids LIST` – Ids of Capsules to associate
- `--smart-proxy-names LIST` – Names of Capsules to associate
- `--ssl-ca-cert-id NUMBER` – Identifier of the content credential containing the SSL CA Cert
- `--ssl-client-cert-id NUMBER` – Identifier of the content credential containing the SSL Client Cert
- `--ssl-client-key-id NUMBER` – Identifier of the content credential containing the SSL Client Key
- `--subpaths LIST` – Path suffixes for finding alternate content
- `--upstream-password VALUE` – Basic authentication password
- `--upstream-username VALUE` – Basic authentication username
- `--use-http-proxies BOOLEAN` – If the Capsules` assigned HTTP proxies should be used
- `--verify-ssl BOOLEAN` – If SSL should be verified for the upstream URL
- `-h`, `--help` – Print help
