---
title: "auth-source"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "11"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-auth-source"
---
# Chapter 11. auth-source

Manipulate auth sources

**Usage**

```
# hammer auth-source [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 11.1. auth-source external

Manage external auth sources

**Usage**

```
# hammer auth-source external [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 11.1.1. auth-source external info

Show an external authentication source

**Usage**

```
# hammer auth-source external <info|show> [OPTIONS]
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
| Locations/ | x | x |  |
| Organizations/ | x | x |  |

### 11.1.2. auth-source external list

List external authentication sources

**Usage**

```
# hammer auth-source external <list|index> [OPTIONS]
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

### 11.1.3. auth-source external update

Update organization and location for Auth Source

**Usage**

```
# hammer auth-source external update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE`
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `-h`, `--help` – Print help

## 11.2. auth-source ldap

Manage LDAP auth sources

**Usage**

```
# hammer auth-source ldap [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 11.2.1. auth-source ldap create

Create an LDAP authentication source

**Usage**

```
# hammer auth-source ldap create [OPTIONS]
```

**Options**

- `--account VALUE`
- `--account-password VALUE` – Required if onthefly_register is true
- `--attr-firstname VALUE` – Required if onthefly_register is true
- `--attr-lastname VALUE` – Required if onthefly_register is true
- `--attr-login VALUE` – Required if onthefly_register is true
- `--attr-mail VALUE` – Required if onthefly_register is true
- `--attr-photo VALUE`
- `--base-dn VALUE`
- `--groups-base VALUE` – Groups base DN
- `--host VALUE` – The hostname of the LDAP server
- `--ldap-filter VALUE` – LDAP filter
- `--ldap-group-membership ENUM` Type of group membership to use, applicable only when server_type is posix, free_ipa or netiq. Option rfc4519 is only applicable when server_type is posix. Possible value(s): `posix`, `rfc4519`, `nis_netgroups`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE`
- `--onthefly-register BOOLEAN`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--port NUMBER` – Defaults to 389
- `--server-type ENUM` – Type of the LDAP server Possible value(s): `free_ipa`, `active_directory`, `posix`, `netiq`
- `--tls BOOLEAN`
- `--use-netgroups BOOLEAN` – Use NIS netgroups instead of posix groups, applicable only when server_type is posix or free_ipa. Deprecated in favor of ldap_group_membership = nis_netgroups
- `--usergroup-sync BOOLEAN` – Sync external user groups on login
- `-h`, `--help` – Print help

### 11.2.2. auth-source ldap delete

Delete an LDAP authentication source

**Usage**

```
# hammer auth-source ldap <delete|destroy> [OPTIONS]
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

### 11.2.3. auth-source ldap info

Show an LDAP authentication source

**Usage**

```
# hammer auth-source ldap <info|show> [OPTIONS]
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

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Server/id | x | x |
| Server/name | x | x |
| Server/server | x | x |
| Server/ldaps | x | x |
| Server/port | x | x |
| Server/server type | x | x |
| Account/account username | x | x |
| Account/base dn | x | x |
| Account/groups base dn | x | x |
| Account/use netgroups | x | x |
| Account/ldap group membership | x | x |
| Account/ldap filter | x | x |
| Account/automatically create accounts? | x | x |
| Account/usergroup sync | x | x |
| Attribute mappings/login name attribute | x | x |
| Attribute mappings/first name attribute | x | x |
| Attribute mappings/last name attribute | x | x |
| Attribute mappings/email address attribute | x | x |
| Attribute mappings/photo attribute | x | x |
| Locations/ | x | x |
| Organizations/ | x | x |

### 11.2.4. auth-source ldap list

List all LDAP authentication sources

**Usage**

```
# hammer auth-source ldap <list|index> [OPTIONS]
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
| Server | x | x |  |
| Port | x | x |  |
| Ldaps? | x | x |  |

**Search and order fields**

- `id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer

### 11.2.5. auth-source ldap update

Update an LDAP authentication source

**Usage**

```
# hammer auth-source ldap update [OPTIONS]
```

**Options**

- `--account VALUE`
- `--account-password VALUE` – Required if onthefly_register is true
- `--attr-firstname VALUE` – Required if onthefly_register is true
- `--attr-lastname VALUE` – Required if onthefly_register is true
- `--attr-login VALUE` – Required if onthefly_register is true
- `--attr-mail VALUE` – Required if onthefly_register is true
- `--attr-photo VALUE`
- `--base-dn VALUE`
- `--groups-base VALUE` – Groups base DN
- `--host VALUE` – The hostname of the LDAP server
- `--id VALUE`
- `--ldap-filter VALUE` – LDAP filter
- `--ldap-group-membership ENUM` Type of group membership to use, applicable only when server_type is posix, free_ipa or netiq. Option rfc4519 is only applicable when server_type is posix. Possible value(s): `posix`, `rfc4519`, `nis_netgroups`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE`
- `--new-name VALUE`
- `--onthefly-register BOOLEAN`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--port NUMBER` – Defaults to 389
- `--server-type ENUM` – Type of the LDAP server Possible value(s): `free_ipa`, `active_directory`, `posix`, `netiq`
- `--tls BOOLEAN`
- `--use-netgroups BOOLEAN` – Use NIS netgroups instead of posix groups, applicable only when server_type is posix or free_ipa. Deprecated in favor of ldap_group_membership = nis_netgroups
- `--usergroup-sync BOOLEAN` – Sync external user groups on login
- `-h`, `--help` – Print help

## 11.3. auth-source list

List all auth sources

**Usage**

```
# hammer auth-source <list|index> [OPTIONS]
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
| Type of auth source | x | x |  |

**Search and order fields**

- `id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
