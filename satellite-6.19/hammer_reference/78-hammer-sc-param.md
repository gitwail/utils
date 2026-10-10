---
title: "sc-param"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "78"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-sc-param"
---
# Chapter 78. sc-param

Manage Foreman Puppet smart class parameters

**Usage**

```
# hammer sc-param [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 78.1. sc-param add-matcher

Create an override value for a specific smart class parameter

**Usage**

```
# hammer sc-param add-matcher [OPTIONS]
```

**Options**

- `--match VALUE` – Override match
- `--omit BOOLEAN` – Satellite will not send this parameter in classification output
- `--puppet-class VALUE` – Puppet class name
- `--puppet-class-id NUMBER` – ID of Puppet class
- `--smart-class-parameter VALUE` – Smart class parameter name
- `--smart-class-parameter-id VALUE`
- `--value VALUE` – Override value, required if omit is false
- `-h`, `--help` – Print help

## 78.2. sc-param info

Show a smart class parameter

**Usage**

```
# hammer sc-param <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--name VALUE` – Smart class parameter name
- `--puppet-class VALUE` – Puppet class name
- `--puppet-class-id NUMBER` – ID of Puppet class
- `--show-hidden BOOLEAN` – Display hidden values
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Parameter | x | x |
| Default value | x | x |
| Override | x | x |
| Puppet class | x | x |
| Class id | x | x |
| Description | x | x |
| Type | x | x |
| Hidden value? | x | x |
| Omit | x | x |
| Required | x | x |
| Validator/type | x | x |
| Validator/rule | x | x |
| Override values/merge overrides | x | x |
| Override values/merge default value | x | x |
| Override values/avoid duplicates | x | x |
| Override values/order | x | x |
| Override values/values/id | x | x |
| Override values/values/match | x | x |
| Override values/values/value | x | x |
| Override values/values/omit | x | x |
| Environments/ | x | x |
| Created at | x | x |
| Updated at | x | x |

## 78.3. sc-param list

List all smart class parameters

**Usage**

```
# hammer sc-param <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id VALUE`
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE`
- `--hostgroup-title VALUE` – Hostgroup title
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--puppet-class VALUE` – Puppet class name
- `--puppet-class-id VALUE`
- `--puppet-environment VALUE` – Puppet environment name
- `--puppet-environment-id VALUE`
- `--search VALUE` – Filter results
- `--show-hidden BOOLEAN` – Display hidden values
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Parameter | x | x |
| Default value | x | x |
| Override | x | x |
| Puppet class | x | x |
| Class id | x | x |

**Search and order fields**

- `avoid_duplicates` – Values: true, false
- `environment` – string
- `key` – string
- `merge_default` – Values: true, false
- `merge_overrides` – Values: true, false
- `override` – Values: true, false
- `parameter` – string
- `puppetclass` – string
- `puppetclass_name` – string

## 78.4. sc-param remove-matcher

Delete an override value for a specific smart class parameter

**Usage**

```
# hammer sc-param remove-matcher [OPTIONS]
```

**Options**

- `--id VALUE`
- `--puppet-class VALUE` – Puppet class name
- `--puppet-class-id NUMBER` – ID of Puppet class
- `--smart-class-parameter VALUE` – Smart class parameter name
- `--smart-class-parameter-id VALUE`
- `-h`, `--help` – Print help

## 78.5. sc-param update

Update a smart class parameter

**Usage**

```
# hammer sc-param update [OPTIONS]
```

**Options**

- `--avoid-duplicates BOOLEAN` – Remove duplicate values (only array type)
- `--default-value VALUE` – Value to use when there is no match
- `--description VALUE` – Description of smart class
- `--hidden-value BOOLEAN` – When enabled the parameter is hidden in the UI
- `--id VALUE`
- `--merge-default BOOLEAN` – Include default value when merging all matching values
- `--merge-overrides BOOLEAN` – Merge all matching values (only array/hash type)
- `--name VALUE` – Smart class parameter name
- `--omit BOOLEAN` – Satellite will not send this parameter in classification output.Puppet will use the value defined in the Puppet manifest for this parameter
- `--override BOOLEAN` – Override this parameter
- `--override-value-order LIST` – The order in which values are resolved
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json`
- `--path VALUE` – The order in which values are resolved
- `--puppet-class VALUE` – Puppet class name
- `--puppet-class-id NUMBER` – ID of Puppet class
- `--required BOOLEAN` – This parameter is required
- `--validator-rule VALUE` – Used to enforce certain values for the parameter values
- `--validator-type ENUM` – Type of the validator Possible value(s): `regexp`, `list`, ``
- `-h`, `--help` – Print help
