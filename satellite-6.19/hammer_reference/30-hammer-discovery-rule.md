---
title: "discovery-rule"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "30"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-discovery-rule"
---
# Chapter 30. discovery-rule

Manipulate discovered rules.

**Usage**

```
# hammer discovery-rule [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 30.1. discovery-rule create

Create a discovery rule

**Usage**

```
# hammer discovery-rule create [OPTIONS]
```

**Options**

- `--enabled BOOLEAN` – Flag is used for temporary shutdown of rules
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER` – The hostgroup that is used to auto provision a host
- `--hostgroup-title VALUE` – Hostgroup title
- `--hostname VALUE` – Defines a pattern to assign human-readable hostnames to the matching hosts
- `--hosts-limit VALUE` – Enables to limit maximum amount of provisioned hosts per rule
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – Location ID for provisioned hosts
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – Represents rule name shown to the users
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – Organization ID for provisioned hosts
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--priority NUMBER` – Puts the rules in order, low numbers go first. Must be greater then zero
- `--search VALUE` – Query to match discovered hosts for the particular rule
- `-h`, `--help` – Print help

## 30.2. discovery-rule delete

Delete a rule

**Usage**

```
# hammer discovery-rule <delete|destroy> [OPTIONS]
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

## 30.3. discovery-rule info

Show a discovery rule

**Usage**

```
# hammer discovery-rule <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
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
| Priority | x | x |  |
| Search | x | x |  |
| Host group | x | x |  |
| Hosts limit | x | x |  |
| Enabled | x | x |  |
| Hostname template | x | x |  |
| Hosts/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |

## 30.4. discovery-rule list

List all discovery rules

**Usage**

```
# hammer discovery-rule <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort results
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--page VALUE` – Paginate results
- `--per-page VALUE` – Number of entries per request
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Priority | x | x |  |
| Search | x | x |  |
| Host group | x | x |  |
| Hosts limit | x | x |  |
| Enabled | x | x |  |

## 30.5. discovery-rule update

Update a rule

**Usage**

```
# hammer discovery-rule update [OPTIONS]
```

**Options**

- `--enabled BOOLEAN` – Flag is used for temporary shutdown of rules
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER` – The hostgroup that is used to auto provision a host
- `--hostgroup-title VALUE` – Hostgroup title
- `--hostname VALUE` – Defines a pattern to assign human-readable hostnames to the matching hosts
- `--hosts-limit VALUE` – Enables to limit maximum amount of provisioned hosts per rule
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – Location ID for provisioned hosts
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – Represents rule name shown to the users
- `--new-name VALUE` – Represents rule name shown to the users
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – Organization ID for provisioned hosts
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--priority NUMBER` – Puts the rules in order, low numbers go first. Must be greater then zero
- `--search VALUE` – Query to match discovered hosts for the particular rule
- `-h`, `--help` – Print help
