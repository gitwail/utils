---
title: "user"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "92"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-user"
---
# Chapter 92. user

Manipulate users

**Usage**

```
# hammer user [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 92.1. user access-token

Managing personal access tokens

**Usage**

```
# hammer user access-token [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 92.1.1. user access-token create

Create a Personal Access Token for a user

**Usage**

```
# hammer user access-token create [OPTIONS]
```

**Options**

- `--expires-at VALUE` – Expiry Date
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

### 92.1.2. user access-token info

Show a Personal Access Token for a user

**Usage**

```
# hammer user access-token <info|show> [OPTIONS]
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
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Active | x | x |  |
| Expires at | x | x |  |
| Created at | x | x |  |
| Last used at | x | x |  |

### 92.1.3. user access-token list

List all Personal Access Tokens for a user

**Usage**

```
# hammer user access-token <list|index> [OPTIONS]
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
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Active | x | x |  |
| Expires at | x | x |  |

**Search and order fields**

- `id` – integer
- `name` – string
- `user_id` – integer

### 92.1.4. user access-token revoke

Revoke a Personal Access Token for a user

**Usage**

```
# hammer user access-token revoke [OPTIONS]
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
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

## 92.2. user add-role

Assign a user role

**Usage**

```
# hammer user add-role [OPTIONS]
```

**Options**

- `--id VALUE`
- `--login VALUE` – User`s login to search by
- `--role VALUE` – User role name
- `--role-id NUMBER`
- `-h`, `--help` – Print help

## 92.3. user create

Create a user

**Usage**

```
# hammer user create [OPTIONS]
```

**Options**

- `--admin BOOLEAN` – Is an admin account
- `--ask-password BOOLEAN`
- `--auth-source VALUE` – Name to search by
- `--auth-source-id NUMBER`
- `--default-location VALUE` – Default location name
- `--default-location-id NUMBER`
- `--default-organization VALUE` – Default organization name
- `--default-organization-id NUMBER`
- `--description VALUE`
- `--disabled BOOLEAN`
- `--firstname VALUE`
- `--lastname VALUE`
- `--locale ENUM` – User`s preferred locale Possible value(s): `ca`, `cs_CZ`, `de`, `en`, `en_GB`, `es`, `fr`, `it`, `ja`, `ka`, `ko`, `pl`, `pt_BR`, `ru`, `zh_CN`, `zh_TW`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--login VALUE`
- `--mail VALUE`
- `--mail-enabled BOOLEAN` – Enable user`s email
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--password VALUE` – Required unless user is in an external authentication source
- `--role-ids LIST`
- `--roles LIST`
- `--timezone ENUM` – User`s timezone Possible value(s): `International Date Line West`, `American Samoa`, `Midway Island`, `Hawaii`, `Alaska`, `Pacific Time (US & Canada)`, `Tijuana`, `Arizona`, `Mazatlan`, `Mountain Time (US & Canada)`, `Central America`, `Central Time (US & Canada)`, `Chihuahua`, `Guadalajara`, `Mexico City`, `Monterrey`, `Saskatchewan`, `Bogota`, `Eastern Time (US & Canada)`, `Indiana (East)`, `Lima`, `Quito`, `Atlantic Time (Canada)`, `Caracas`, `Georgetown`, `La Paz`, `Puerto Rico`, `Santiago`, `Newfoundland`, `Brasilia`, `Buenos Aires`, `Montevideo`, `Greenland`, `Mid-Atlantic`, `Azores`, `Cape Verde Is.`, `Casablanca`, `Dublin`, `Edinburgh`, `Lisbon`, `London`, `Monrovia`, `UTC`, `Amsterdam`, `Belgrade`, `Berlin`, `Bern`, `Bratislava`, `Brussels`, `Budapest`, `Copenhagen`, `Ljubljana`, `Madrid`, `Paris`, `Prague`, `Rome`, `Sarajevo`, `Skopje`, `Stockholm`, `Vienna`, `Warsaw`, `West Central Africa`, `Zagreb`, `Zurich`, `Athens`, `Bucharest`, `Cairo`, `Harare`, `Helsinki`, `Jerusalem`, `Kaliningrad`, `Kyiv`, `Pretoria`, `Riga`, `Sofia`, `Tallinn`, `Vilnius`, `Baghdad`, `Istanbul`, `Kuwait`, `Minsk`, `Moscow`, `Nairobi`, `Riyadh`, `St. Petersburg`, `Volgograd`, `Tehran`, `Abu Dhabi`, `Baku`, `Muscat`, `Samara`, `Tbilisi`, `Yerevan`, `Kabul`, `Almaty`, `Ekaterinburg`, `Islamabad`, `Karachi`, `Tashkent`, `Chennai`, `Kolkata`, `Mumbai`, `New Delhi`, `Sri Jayawardenepura`, `Kathmandu`, `Astana`, `Dhaka`, `Urumqi`, `Rangoon`, `Bangkok`, `Hanoi`, `Jakarta`, `Krasnoyarsk`, `Novosibirsk`, `Beijing`, `Chongqing`, `Hong Kong`, `Irkutsk`, `Kuala Lumpur`, `Perth`, `Singapore`, `Taipei`, `Ulaanbaatar`, `Osaka`, `Sapporo`, `Seoul`, `Tokyo`, `Yakutsk`, `Adelaide`, `Darwin`, `Brisbane`, `Canberra`, `Guam`, `Hobart`, `Melbourne`, `Port Moresby`, `Sydney`, `Vladivostok`, `Magadan`, `New Caledonia`, `Solomon Is.`, `Srednekolymsk`, `Auckland`, `Fiji`, `Kamchatka`, `Marshall Is.`, `Wellington`, `Chatham Is.`, `` Nuku`alofa ``, `Samoa`, `Tokelau Is.`
- `--ui-compact-mode BOOLEAN` – Use compact UI
- `-h`, `--help` – Print help

## 92.4. user delete

Delete a user

**Usage**

```
# hammer user <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--login VALUE` – User`s login to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 92.5. user info

Show a user

**Usage**

```
# hammer user <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--login VALUE` – User`s login to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Login | x | x | x |
| Name | x | x |  |
| Email | x | x |  |
| Admin | x | x |  |
| Disabled | x | x |  |
| Last login | x | x |  |
| Authorized by | x | x |  |
| Email enabled | x | x |  |
| Effective admin | x | x |  |
| Locale | x | x |  |
| Timezone | x | x |  |
| Description | x | x |  |
| Default organization | x | x |  |
| Default location | x | x |  |
| Roles/ | x | x |  |
| User groups/usergroup | x | x |  |
| User groups/id | x | x |  |
| User groups/roles/ | x | x |  |
| Inherited user groups/usergroup | x | x |  |
| Inherited user groups/id | x | x |  |
| Inherited user groups/roles/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 92.6. user list

List all users

**Usage**

```
# hammer user <list|index> [OPTIONS]
```

**Options**

- `--auth-source-ldap VALUE` – Name to search by
- `--auth-source-ldap-id VALUE` – ID of LDAP authentication source
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
- `--role VALUE` – User role name
- `--role-id VALUE` – ID of role
- `--search VALUE` – Filter results
- `--user-group VALUE` – Name to search by
- `--user-group-id VALUE` – ID of user group
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Login | x | x | x |
| Name | x | x |  |
| Email | x | x |  |
| Admin | x | x |  |
| Disabled | x | x |  |
| Last login | x | x |  |
| Authorized by | x | x |  |

**Search and order fields**

- `admin` – Values: true, false
- `auth_source` – string
- `auth_source_type` – string
- `description` – text
- `disabled` – Values: true, false
- `firstname` – string
- `id` – integer
- `last_login_on` – datetime
- `lastname` – string
- `location` – string
- `location_id` – integer
- `login` – string
- `mail` – string
- `organization` – string
- `organization_id` – integer
- `role` – string
- `role_id` – integer
- `usergroup` – string

## 92.7. user mail-notification

Managing personal mail notifications

**Usage**

```
# hammer user mail-notification [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 92.7.1. user mail-notification add

Add an email notification for a user

**Usage**

```
# hammer user mail-notification add [OPTIONS]
```

**Options**

- `--interval VALUE` – Mail notification interval option, e.g. Daily, Weekly or Monthly. Required for summary notification
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mail-notification VALUE` – Name to search by
- `--mail-notification-id NUMBER`
- `--mail-query VALUE` – Relevant only for audit summary notification
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--subscription VALUE` – Mail notification subscription option, e.g. Subscribe, Subscribe to my hosts or Subscribe to all hosts. Required for host built and config error state
- `--user VALUE` – User`s login to search by
- `--user-id VALUE`
- `-h`, `--help` – Print help

### 92.7.2. user mail-notification list

List all email notifications for a user

**Usage**

```
# hammer user mail-notification <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x |  |
| Name | x | x | x |
| Description | x | x |  |
| Interval | x | x |  |
| Mail query | x | x |  |

### 92.7.3. user mail-notification remove

Remove an email notification for a user

**Usage**

```
# hammer user mail-notification remove [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mail-notification VALUE` – Name to search by
- `--mail-notification-id NUMBER`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE`
- `-h`, `--help` – Print help

### 92.7.4. user mail-notification update

Update an email notification for a user

**Usage**

```
# hammer user mail-notification update [OPTIONS]
```

**Options**

- `--interval VALUE` – Mail notification interval option, e.g. Daily, Weekly or Monthly. Required for summary notification
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mail-notification VALUE` – Name to search by
- `--mail-notification-id NUMBER`
- `--mail-query VALUE` – Relevant only for audit summary notification
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--subscription VALUE` – Mail notification subscription option, e.g. Subscribe, Subscribe to my hosts or Subscribe to all hosts. Required for host built and config error state
- `--user VALUE` – User`s login to search by
- `--user-id VALUE`
- `-h`, `--help` – Print help

## 92.8. user registration-tokens

Managing registration tokens

**Usage**

```
# hammer user registration-tokens [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 92.8.1. user registration-tokens invalidate

Invalidate all registration tokens for a specific user

**Usage**

```
# hammer user registration-tokens invalidate [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

### 92.8.2. user registration-tokens invalidate-multiple

Invalidate all registration tokens for multiple users

**Usage**

```
# hammer user registration-tokens invalidate-multiple [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--search VALUE` – Search query that selects users for which registration tokens will be invalidated. Search query example: id ^ (2, 4, 6)
- `-h`, `--help` – Print help

## 92.9. user remove-role

Remove a user role

**Usage**

```
# hammer user remove-role [OPTIONS]
```

**Options**

- `--id VALUE`
- `--login VALUE` – User`s login to search by
- `--role VALUE` – User role name
- `--role-id NUMBER`
- `-h`, `--help` – Print help

## 92.10. user ssh-keys

Managing User SSH Keys.

**Usage**

```
# hammer user ssh-keys [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 92.10.1. user ssh-keys add

Add an SSH key for a user

**Usage**

```
# hammer user ssh-keys add [OPTIONS]
```

**Options**

- `--key VALUE` – Public SSH key
- `--key-file FILE` – Path to a SSH public key
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

### 92.10.2. user ssh-keys delete

Delete an SSH key for a user

**Usage**

```
# hammer user ssh-keys <delete|destroy> [OPTIONS]
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
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

### 92.10.3. user ssh-keys info

Show an SSH key from a user

**Usage**

```
# hammer user ssh-keys <info|show> [OPTIONS]
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
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Fingerprint | x | x |  |
| Length | x | x |  |
| Created at | x | x |  |
| Public key | x | x |  |

### 92.10.4. user ssh-keys list

List all SSH keys for a user

**Usage**

```
# hammer user ssh-keys <list|index> [OPTIONS]
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
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Fingerprint | x | x |  |
| Length | x | x |  |
| Created at | x | x |  |

**Search and order fields**

- `id` – integer
- `name` – string
- `user_id` – integer

## 92.11. user table-preference

Managing table preferences

**Usage**

```
# hammer user table-preference [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 92.11.1. user table-preference create

Creates a table preference for a given table

**Usage**

```
# hammer user table-preference create [OPTIONS]
```

**Options**

- `--columns LIST` – List of user selected columns
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name of the table
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

### 92.11.2. user table-preference delete

Delete a table preference for a given table

**Usage**

```
# hammer user table-preference <delete|destroy> [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name of the table
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

### 92.11.3. user table-preference info

Table preference details of a given table

**Usage**

```
# hammer user table-preference <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name of the table
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x |  |
| Columns | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

### 92.11.4. user table-preference list

List of table preferences for a user

**Usage**

```
# hammer user table-preference <list|index> [OPTIONS]
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
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x |  |
| Columns | x | x |  |

### 92.11.5. user table-preference update

Updates a table preference for a given table

**Usage**

```
# hammer user table-preference update [OPTIONS]
```

**Options**

- `--columns LIST` – List of user selected columns
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name of the table
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id VALUE` – ID of the user
- `-h`, `--help` – Print help

## 92.12. user update

Update a user

**Usage**

```
# hammer user update [OPTIONS]
```

**Options**

- `--admin BOOLEAN` – Is an admin account
- `--ask-password BOOLEAN`
- `--auth-source VALUE` – Name to search by
- `--auth-source-id NUMBER`
- `--current-password VALUE` – Required when user want to change own password
- `--default-location VALUE` – Default location name
- `--default-location-id NUMBER`
- `--default-organization VALUE` – Default organization name
- `--default-organization-id NUMBER`
- `--description VALUE`
- `--disabled BOOLEAN`
- `--firstname VALUE`
- `--id VALUE`
- `--lastname VALUE`
- `--locale ENUM` – User`s preferred locale Possible value(s): `ca`, `cs_CZ`, `de`, `en`, `en_GB`, `es`, `fr`, `it`, `ja`, `ka`, `ko`, `pl`, `pt_BR`, `ru`, `zh_CN`, `zh_TW`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--login VALUE`
- `--mail VALUE`
- `--mail-enabled BOOLEAN` – Enable user`s email
- `--new-login VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--password VALUE` – Required unless user is in an external authentication source
- `--role-ids LIST`
- `--roles LIST`
- `--timezone ENUM` – User`s timezone Possible value(s): `International Date Line West`, `American Samoa`, `Midway Island`, `Hawaii`, `Alaska`, `Pacific Time (US & Canada)`, `Tijuana`, `Arizona`, `Mazatlan`, `Mountain Time (US & Canada)`, `Central America`, `Central Time (US & Canada)`, `Chihuahua`, `Guadalajara`, `Mexico City`, `Monterrey`, `Saskatchewan`, `Bogota`, `Eastern Time (US & Canada)`, `Indiana (East)`, `Lima`, `Quito`, `Atlantic Time (Canada)`, `Caracas`, `Georgetown`, `La Paz`, `Puerto Rico`, `Santiago`, `Newfoundland`, `Brasilia`, `Buenos Aires`, `Montevideo`, `Greenland`, `Mid-Atlantic`, `Azores`, `Cape Verde Is.`, `Casablanca`, `Dublin`, `Edinburgh`, `Lisbon`, `London`, `Monrovia`, `UTC`, `Amsterdam`, `Belgrade`, `Berlin`, `Bern`, `Bratislava`, `Brussels`, `Budapest`, `Copenhagen`, `Ljubljana`, `Madrid`, `Paris`, `Prague`, `Rome`, `Sarajevo`, `Skopje`, `Stockholm`, `Vienna`, `Warsaw`, `West Central Africa`, `Zagreb`, `Zurich`, `Athens`, `Bucharest`, `Cairo`, `Harare`, `Helsinki`, `Jerusalem`, `Kaliningrad`, `Kyiv`, `Pretoria`, `Riga`, `Sofia`, `Tallinn`, `Vilnius`, `Baghdad`, `Istanbul`, `Kuwait`, `Minsk`, `Moscow`, `Nairobi`, `Riyadh`, `St. Petersburg`, `Volgograd`, `Tehran`, `Abu Dhabi`, `Baku`, `Muscat`, `Samara`, `Tbilisi`, `Yerevan`, `Kabul`, `Almaty`, `Ekaterinburg`, `Islamabad`, `Karachi`, `Tashkent`, `Chennai`, `Kolkata`, `Mumbai`, `New Delhi`, `Sri Jayawardenepura`, `Kathmandu`, `Astana`, `Dhaka`, `Urumqi`, `Rangoon`, `Bangkok`, `Hanoi`, `Jakarta`, `Krasnoyarsk`, `Novosibirsk`, `Beijing`, `Chongqing`, `Hong Kong`, `Irkutsk`, `Kuala Lumpur`, `Perth`, `Singapore`, `Taipei`, `Ulaanbaatar`, `Osaka`, `Sapporo`, `Seoul`, `Tokyo`, `Yakutsk`, `Adelaide`, `Darwin`, `Brisbane`, `Canberra`, `Guam`, `Hobart`, `Melbourne`, `Port Moresby`, `Sydney`, `Vladivostok`, `Magadan`, `New Caledonia`, `Solomon Is.`, `Srednekolymsk`, `Auckland`, `Fiji`, `Kamchatka`, `Marshall Is.`, `Wellington`, `Chatham Is.`, `` Nuku`alofa ``, `Samoa`, `Tokelau Is.`
- `--ui-compact-mode BOOLEAN` – Use compact UI
- `-h`, `--help` – Print help
