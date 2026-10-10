---
title: "ansible"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-ansible"
---
# Chapter 6. ansible

Manage foreman ansible

**Usage**

```
# hammer ansible [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 6.1. ansible inventory

Ansible Inventory

**Usage**

```
# hammer ansible inventory [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 6.1.1. ansible inventory hostgroups

Show Ansible inventory for hostgroups

**Usage**

```
# hammer ansible inventory hostgroups [OPTIONS]
```

**Options**

- `--as-json` – Full response as json
- `--hostgroup-ids LIST` – IDs of hostgroups included in inventory
- `--hostgroup-titles LIST`
- `--hostgroups LIST`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 6.1.2. ansible inventory hosts

Show Ansible inventory for hosts

**Usage**

```
# hammer ansible inventory hosts [OPTIONS]
```

**Options**

- `--as-json` – Full response as json
- `--host-ids LIST` – IDs of hosts included in inventory
- `--hosts LIST`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 6.1.3. ansible inventory schedule

Schedule generating of Ansible Inventory report

**Usage**

```
# hammer ansible inventory schedule [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--report-format ENUM` – Report format, defaults to `json` Possible value(s): `csv`, `json`, `yaml`, `html`
- `-h`, `--help` – Print help

## 6.2. ansible roles

Manage ansible roles

**Usage**

```
# hammer ansible roles [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 6.2.1. ansible roles delete

Deletes Ansible role

**Usage**

```
# hammer ansible roles <delete|destroy> [OPTIONS]
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

### 6.2.2. ansible roles fetch

Fetch Ansible roles available to be synced

**Usage**

```
# hammer ansible roles fetch [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--proxy-id VALUE` – Capsule to fetch from
- `-h`, `--help` – Print help

### 6.2.3. ansible roles import

DEPRECATED: Import Ansible roles. Use sync instead

**Usage**

```
# hammer ansible roles import [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--proxy-id VALUE` – Capsule to import from
- `--role-names LIST` – Ansible role names to be imported
- `-h`, `--help` – Print help

### 6.2.4. ansible roles info

Show role

**Usage**

```
# hammer ansible roles <info|show> [OPTIONS]
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
| Imported at | x | x |  |

### 6.2.5. ansible roles list

List Ansible roles

**Usage**

```
# hammer ansible roles <list|index> [OPTIONS]
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
| Name | x | x | x |
| Imported at | x | x |  |

**Search and order fields**

- `host` – string
- `host_id` – integer
- `hostgroup` – string
- `hostgroup_id` – integer
- `id` – integer
- `name` – string
- `updated_at` – datetime

### 6.2.6. ansible roles obsolete

DEPRECATED: Obsolete Ansible roles. Use sync instead

**Usage**

```
# hammer ansible roles obsolete [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--proxy-id VALUE` – Capsule to import from
- `-h`, `--help` – Print help

### 6.2.7. ansible roles play-hostgroups

Runs all Ansible roles on hostgroups

**Usage**

```
# hammer ansible roles play-hostgroups [OPTIONS]
```

**Options**

- `--hostgroup-ids LIST` – IDs of hostgroups to play roles on
- `--hostgroup-titles LIST`
- `--hostgroups LIST`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 6.2.8. ansible roles play-hosts

Runs all Ansible roles on hosts

**Usage**

```
# hammer ansible roles play-hosts [OPTIONS]
```

**Options**

- `--host-ids LIST` – IDs of hosts to play roles on
- `--hosts LIST`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 6.2.9. ansible roles sync

Sync Ansible roles

**Usage**

```
# hammer ansible roles sync [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--proxy-id VALUE` – Capsule to sync from
- `--role-names LIST` – Ansible role names to be synced
- `-h`, `--help` – Print help

## 6.3. ansible variables

Manage ansible variables

**Usage**

```
# hammer ansible variables [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 6.3.1. ansible variables add-matcher

Create an override value for a specific ansible variable

**Usage**

```
# hammer ansible variables add-matcher [OPTIONS]
```

**Options**

- `--ansible-variable VALUE` – Name to search by
- `--ansible-variable-id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--match VALUE` – Override match
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--value VALUE` – Override value, required if omit is false
- `-h`, `--help` – Print help

### 6.3.2. ansible variables create

Create Ansible variable

**Usage**

```
# hammer ansible variables create [OPTIONS]
```

**Options**

- `--ansible-role VALUE` – Name to search by
- `--ansible-role-id NUMBER` – Role ID
- `--avoid-duplicates BOOLEAN` – Remove duplicate values (only array type)
- `--default-value VALUE` – Default value of variable
- `--description VALUE` – Description of variable
- `--hidden-value BOOLEAN` – When enabled the parameter is hidden in the UI
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--merge-default BOOLEAN` – Include default value when merging all matching values
- `--merge-overrides BOOLEAN` – Merge all matching values (only array/hash type)
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--override BOOLEAN` – Whether to override variable or not
- `--override-value-order VALUE` The order in which values are resolved
- `--validator-rule VALUE` – Used to enforce certain values for the parameter values
- `--validator-type ENUM` – Types of validation values Possible value(s): `regexp`, `list`
- `--variable VALUE` – Name of variable
- `--variable-type ENUM` – Types of variable values Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json`
- `-h`, `--help` – Print help

### 6.3.3. ansible variables delete

Deletes Ansible variable

**Usage**

```
# hammer ansible variables <delete|destroy> [OPTIONS]
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

### 6.3.4. ansible variables import

DEPRECATED: Import Ansible variables. This will only import variables for already existing roles, it will not import any new roles

**Usage**

```
# hammer ansible variables import [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--proxy-id VALUE` – Capsule to import from
- `-h`, `--help` – Print help

### 6.3.5. ansible variables info

Show variable

**Usage**

```
# hammer ansible variables <info|show> [OPTIONS]
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
| Id | x | x |
| Variable | x | x |
| Default value | x | x |
| Type | x | x |
| Role | x | x |
| Role id | x | x |
| Description | x | x |
| Hidden value? | x | x |
| Validator/type | x | x |
| Validator/rule | x | x |
| Override values/override | x | x |
| Override values/merge overrides | x | x |
| Override values/merge default value | x | x |
| Override values/avoid duplicates | x | x |
| Override values/order | x | x |
| Override values/values/id | x | x |
| Override values/values/match | x | x |
| Override values/values/value | x | x |
| Created at | x | x |
| Updated at | x | x |

### 6.3.6. ansible variables list

List Ansible variables

**Usage**

```
# hammer ansible variables <list|index> [OPTIONS]
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

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Variable | x | x |
| Default value | x | x |
| Type | x | x |
| Role | x | x |
| Role id | x | x |

**Search and order fields**

- `ansible_role` – string
- `avoid_duplicates` – Values: true, false
- `imported` – Values: true, false
- `key` – string
- `merge_default` – Values: true, false
- `merge_overrides` – Values: true, false
- `name` – string
- `override` – Values: true, false
- `parameter` – string

### 6.3.7. ansible variables obsolete

DEPRECATED: Obsolete Ansible variables. This will only obsolete variables for already existing roles, it will not delete any old roles

**Usage**

```
# hammer ansible variables obsolete [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--proxy-id VALUE` – Capsule to import from
- `-h`, `--help` – Print help

### 6.3.8. ansible variables remove-matcher

Destroy an override value

**Usage**

```
# hammer ansible variables remove-matcher [OPTIONS]
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

### 6.3.9. ansible variables update

Updates Ansible variable

**Usage**

```
# hammer ansible variables update [OPTIONS]
```

**Options**

- `--ansible-role VALUE` – Name to search by
- `--ansible-role-id NUMBER` – Role ID
- `--avoid-duplicates BOOLEAN` – Remove duplicate values (only array type)
- `--default-value VALUE` – Default value of variable
- `--description VALUE` – Description of variable
- `--hidden-value BOOLEAN` – When enabled the parameter is hidden in the UI
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--merge-default BOOLEAN` – Include default value when merging all matching values
- `--merge-overrides BOOLEAN` – Merge all matching values (only array/hash type)
- `--name VALUE` – Name to search by
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--override BOOLEAN` – Whether to override variable or not
- `--override-value-order LIST` – The order in which values are resolved
- `--validator-rule VALUE` – Used to enforce certain values for the parameter values
- `--validator-type ENUM` – Types of validation values Possible value(s): `regexp`, `list`
- `--variable VALUE` – Name of variable
- `--variable-type ENUM` – Types of variable values Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json`
- `-h`, `--help` – Print help
