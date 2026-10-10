---
title: "puppet-class"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "68"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-puppet-class"
---
# Chapter 68. puppet-class

Manage Foreman Puppet classes

**Usage**

```
# hammer puppet-class [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 68.1. puppet-class info

Show a Puppet class

**Usage**

```
# hammer puppet-class <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id VALUE` – ID of host
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE` – ID of Puppet class
- `--name VALUE` – Puppet class name
- `--puppet-environment VALUE` – Puppet environment name
- `--puppet-environment-id VALUE` ID of environment
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Smart class parameters/ | x | x |  |
| Hostgroups/ | x | x |  |
| Environments/ | x | x |  |
| Parameters/ | x | x |  |

## 68.2. puppet-class list

List all Puppet classes

**Usage**

```
# hammer puppet-class <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id VALUE` – ID of host
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--puppet-environment VALUE` – Puppet environment name
- `--puppet-environment-id VALUE` ID of environment
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

**Search and order fields**

- `config_group` – string
- `environment` – string
- `host` – string
- `hostgroup` – string
- `key` – string
- `location` – string
- `name` – string
- `organization` – string

## 68.3. puppet-class sc-params

List all smart class parameters

**Usage**

```
# hammer puppet-class sc-params [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--puppet-class VALUE` – Puppet class name
- `--puppet-class-id NUMBER`
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
