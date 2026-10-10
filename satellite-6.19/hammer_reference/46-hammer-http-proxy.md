---
title: "http-proxy"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "46"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-http-proxy"
---
# Chapter 46. http-proxy

Manipulate http proxies

**Usage**

```
# hammer http-proxy [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 46.1. http-proxy create

Create an HTTP proxy

**Usage**

```
# hammer http-proxy create [OPTIONS]
```

**Options**

- `--content-default-http-proxy BOOLEAN` Set this HTTP proxy as the default content HTTP proxy
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – The HTTP proxy name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--password VALUE` – Password used to authenticate with the HTTP proxy
- `--url VALUE` – URL of the HTTP proxy
- `--username VALUE` – Username used to authenticate with the HTTP proxy
- `-h`, `--help` – Print help

## 46.2. http-proxy delete

Delete an HTTP proxy

**Usage**

```
# hammer http-proxy <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 46.3. http-proxy info

Show an HTTP proxy

**Usage**

```
# hammer http-proxy <info|show> [OPTIONS]
```

**Options**

- `--content-default-http-proxy BOOLEAN` Set this HTTP proxy as the default content HTTP proxy
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – Identifier of the HTTP proxy
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Username | x | x |  |
| Url | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |

## 46.4. http-proxy list

List of HTTP proxies

**Usage**

```
# hammer http-proxy <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Scope by locations
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Scope by organizations
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

**Search and order fields**

- `id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
- `url` – string

## 46.5. http-proxy update

Update an HTTP proxy

**Usage**

```
# hammer http-proxy update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – The HTTP proxy name
- `--new-name VALUE` – The HTTP proxy name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--password VALUE` – Password used to authenticate with the HTTP proxy
- `--url VALUE` – URL of the HTTP proxy
- `--username VALUE` – Username used to authenticate with the HTTP proxy
- `-h`, `--help` – Print help
