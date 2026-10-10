---
title: "user-group"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "93"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-user-group"
---
# Chapter 93. user-group

Manage user groups

**Usage**

```
# hammer user-group [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 93.1. user-group add-role

Assign a user role

**Usage**

```
# hammer user-group add-role [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `--role VALUE` – User role name
- `--role-id NUMBER`
- `-h`, `--help` – Print help

## 93.2. user-group add-user

Associate an user

**Usage**

```
# hammer user-group add-user [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `--user VALUE` – User`s login to search by
- `--user-id NUMBER`
- `-h`, `--help` – Print help

## 93.3. user-group add-user-group

Associate an user group

**Usage**

```
# hammer user-group add-user-group [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `--user-group VALUE` – Name to search by
- `--user-group-id NUMBER`
- `-h`, `--help` – Print help

## 93.4. user-group create

Create a user group

**Usage**

```
# hammer user-group create [OPTIONS]
```

**Options**

- `--admin BOOLEAN` – Is an admin user group, can be modified by admins only
- `--name VALUE`
- `--role-ids LIST`
- `--roles LIST`
- `--user-group-ids LIST`
- `--user-groups LIST`
- `--user-ids LIST`
- `--users LIST`
- `-h`, `--help` – Print help

## 93.5. user-group delete

Delete a user group

**Usage**

```
# hammer user-group <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

## 93.6. user-group external

View and manage user group’s external user groups

**Usage**

```
# hammer user-group external [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 93.6.1. user-group external create

Create an external user group linked to a user group

**Usage**

```
# hammer user-group external create [OPTIONS]
```

**Options**

- `--auth-source VALUE` – Name to search by
- `--auth-source-id NUMBER` – ID of linked authentication source
- `--name VALUE` – External user group name
- `--user-group VALUE` – Name to search by
- `--user-group-id VALUE` – ID or name of user group
- `-h`, `--help` – Print help

### 93.6.2. user-group external delete

Delete an external user group

**Usage**

```
# hammer user-group external <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE` – ID or name external user group
- `--name VALUE` – Name to search by
- `--user-group VALUE` – Name to search by
- `--user-group-id VALUE` – ID or name of user group
- `-h`, `--help` – Print help

### 93.6.3. user-group external info

Show an external user group for user group

**Usage**

```
# hammer user-group external <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – ID or name of external user group
- `--name VALUE` – Name to search by
- `--user-group VALUE` – Name to search by
- `--user-group-id VALUE` – ID or name of user group
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Auth source | x | x |  |

### 93.6.4. user-group external list

List all external user groups for user group

**Usage**

```
# hammer user-group external <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--user-group VALUE` – Name to search by
- `--user-group-id VALUE` – ID or name of user group
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Auth source | x | x |  |

### 93.6.5. user-group external refresh

Refresh external user group

**Usage**

```
# hammer user-group external refresh [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – ID or name of external user group
- `--name VALUE` – Name to search by
- `--user-group VALUE` – Name to search by
- `--user-group-id VALUE` – ID or name of user group
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Name | x | x | x |
| Auth source | x | x |  |

### 93.6.6. user-group external update

Update external user group

**Usage**

```
# hammer user-group external update [OPTIONS]
```

**Options**

- `--auth-source VALUE` – Name to search by
- `--auth-source-id NUMBER` – ID of linked authentication source
- `--id VALUE` – ID or name of external user group
- `--name VALUE` – External user group name
- `--new-name VALUE` – External user group name
- `--user-group VALUE` – Name to search by
- `--user-group-id VALUE` – ID or name of user group
- `-h`, `--help` – Print help

## 93.7. user-group info

Show a user group

**Usage**

```
# hammer user-group <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Admin | x | x |  |
| Users/ | x | x |  |
| User groups/usergroup | x | x |  |
| User groups/id | x | x |  |
| User groups/roles/ | x | x |  |
| Inherited user groups/usergroup | x | x |  |
| Inherited user groups/id | x | x |  |
| Inherited user groups/roles/ | x | x |  |
| External user groups/ | x | x |  |
| Roles/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 93.8. user-group list

List all user groups

**Usage**

```
# hammer user-group <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Admin | x | x |  |

**Search and order fields**

- `id` – integer
- `name` – string
- `role` – string
- `role_id` – integer

## 93.9. user-group remove-role

Remove a user role

**Usage**

```
# hammer user-group remove-role [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `--role VALUE` – User role name
- `--role-id NUMBER`
- `-h`, `--help` – Print help

## 93.10. user-group remove-user

Disassociate an user

**Usage**

```
# hammer user-group remove-user [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `--user VALUE` – User`s login to search by
- `--user-id NUMBER`
- `-h`, `--help` – Print help

## 93.11. user-group remove-user-group

Disassociate an user group

**Usage**

```
# hammer user-group remove-user-group [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `--user-group VALUE` – Name to search by
- `--user-group-id NUMBER`
- `-h`, `--help` – Print help

## 93.12. user-group update

Update a user group

**Usage**

```
# hammer user-group update [OPTIONS]
```

**Options**

- `--admin BOOLEAN` – Is an admin user group, can be modified by admins only
- `--id VALUE`
- `--name VALUE`
- `--new-name VALUE`
- `--role-ids LIST`
- `--roles LIST`
- `--user-group-ids LIST`
- `--user-groups LIST`
- `--user-ids LIST`
- `--users LIST`
- `-h`, `--help` – Print help
