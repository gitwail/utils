---
title: "domain"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "32"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-domain"
---
# Chapter 32. domain

Manipulate domains

**Usage**

```
# hammer domain [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 32.1. domain create

Create a domain

**Usage**

```
# hammer domain create [OPTIONS]
```

**Options**

- `--description VALUE` – Full name describing the domain
- `--dns VALUE` – Name of DNS proxy to use within this domain
- `--dns-id NUMBER` – DNS Capsule ID to use within this domain
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – The full DNS domain name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `-h`, `--help` – Print help

## 32.2. domain delete

Delete a domain

**Usage**

```
# hammer domain <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Domain name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 32.3. domain delete-parameter

Delete parameter for a domain

**Usage**

```
# hammer domain delete-parameter [OPTIONS]
```

**Options**

- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Numerical ID or domain name
- `--name VALUE` – Parameter name
- `-h`, `--help` – Print help

## 32.4. domain info

Show a domain

**Usage**

```
# hammer domain <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – Numerical ID or domain name
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Domain name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--show-hidden-parameters BOOLEAN` Display hidden parameter values
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Description | x | x |  |
| Dns id | x | x |  |
| Subnets/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Parameters/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 32.5. domain list

List of domains

**Usage**

```
# hammer domain <list|index> [OPTIONS]
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
- `--subnet VALUE` – Subnet name
- `--subnet-id VALUE` – ID of subnet
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

**Search and order fields**

- `fullname` – string
- `id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
- `params` – string

## 32.6. domain set-parameter

Create or update parameter for a domain

**Usage**

```
# hammer domain set-parameter [OPTIONS]
```

**Options**

- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Numerical ID or domain name
- `--hidden-value BOOLEAN` – Should the value be hidden
- `--name VALUE` – Parameter name
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json` Default: "string"
- `--value VALUE` – Parameter value
- `-h`, `--help` – Print help

## 32.7. domain update

Update a domain

**Usage**

```
# hammer domain update [OPTIONS]
```

**Options**

- `--description VALUE` – Full name describing the domain
- `--dns VALUE` – Name of DNS proxy to use within this domain
- `--dns-id NUMBER` – DNS Capsule ID to use within this domain
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – The full DNS domain name
- `--new-name VALUE` – The full DNS domain name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `-h`, `--help` – Print help
