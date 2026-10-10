---
title: "hostgroup"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "45"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-hostgroup"
---
# Chapter 45. hostgroup

Manipulate hostgroups

**Usage**

```
# hammer hostgroup [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 45.1. hostgroup ansible-roles

Manage Ansible roles on a hostgroup

**Usage**

```
# hammer hostgroup ansible-roles [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 45.1.1. hostgroup ansible-roles add

Associate an Ansible role

**Usage**

```
# hammer hostgroup ansible-roles add [OPTIONS]
```

**Options**

- `--ansible-role VALUE` – Name to search by
- `--ansible-role-id NUMBER`
- `--force` – Associate the Ansible role even if it already is associated indirectly
- `--id VALUE`
- `--name VALUE` – Hostgroup name
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

### 45.1.2. hostgroup ansible-roles assign

Assigns Ansible roles to a hostgroup

**Usage**

```
# hammer hostgroup ansible-roles assign [OPTIONS]
```

**Options**

- `--ansible-role-ids LIST` – Ansible roles to assign to a hostgroup
- `--ansible-roles LIST`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Hostgroup name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

### 45.1.3. hostgroup ansible-roles list

List all Ansible roles for a hostgroup

**Usage**

```
# hammer hostgroup ansible-roles <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Hostgroup name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Imported at | x | x |  |
| Inherited | x | x |  |
| Directly assigned | x | x |  |

### 45.1.4. hostgroup ansible-roles play

Runs all Ansible roles on a hostgroup

**Usage**

```
# hammer hostgroup ansible-roles play [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Hostgroup name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

### 45.1.5. hostgroup ansible-roles remove

Disassociate an Ansible role

**Usage**

```
# hammer hostgroup ansible-roles remove [OPTIONS]
```

**Options**

- `--ansible-role VALUE` – Name to search by
- `--ansible-role-id NUMBER`
- `--id VALUE`
- `--name VALUE` – Hostgroup name
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

## 45.2. hostgroup create

Create a host group

**Usage**

```
# hammer hostgroup create [OPTIONS]
```

**Options**

- `--ansible-role-ids LIST` – IDs of associated ansible roles
- `--ansible-roles LIST`
- `--architecture VALUE` – Architecture name
- `--architecture-id NUMBER` – Architecture ID
- `--ask-root-password BOOLEAN`
- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id NUMBER` – Compute profile ID
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id NUMBER` – Compute resource ID
- `--config-group-ids LIST` – IDs of associated config groups
- `--config-groups LIST`
- `--content-source VALUE` – Content Source name
- `--content-source-id NUMBER` – Content source ID
- `--content-view VALUE` – Name to search by
- `--content-view-id NUMBER` – Content view ID
- `--description VALUE` – Host group description
- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Domain ID
- `--group-parameters-attributes SCHEMA` Array of parameters
- `--kickstart-repository VALUE` – Kickstart repository name
- `--kickstart-repository-id NUMBER` – Kickstart repository ID
- `--lifecycle-environment VALUE` – Name to search by
- `--lifecycle-environment-id NUMBER` – Lifecycle environment ID
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--medium VALUE` – Medium name
- `--medium-id NUMBER` – Media ID
- `--name VALUE` – Name of the host group
- `--openscap-proxy-id NUMBER` – ID of OpenSCAP Capsule
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – Operating system ID
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--parent VALUE` – Name of parent hostgroup
- `--parent-id NUMBER` – Parent ID of the host group
- `--parent-title VALUE` – Title of parent hostgroup
- `--partition-table VALUE` – Partition table name
- `--partition-table-id NUMBER` – Partition table ID
- `--puppet-ca-proxy VALUE` – Name of Puppet CA proxy
- `--puppet-ca-proxy-id NUMBER` – Puppet CA Capsule ID
- `--puppet-class-ids LIST` – List of Puppet class ids
- `--puppet-classes LIST`
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` – ID of associated Puppet environment
- `--puppet-proxy VALUE` – Name of Puppet proxy
- `--puppet-proxy-id NUMBER` – Puppet Capsule ID
- `--pxe-loader ENUM` – DHCP filename option (Grub2/PXELinux by default) Possible value(s): `None`, `PXELinux BIOS`, `PXELinux UEFI`, `Grub2 BIOS`, `Grub2 ELF`, `Grub2 UEFI`, `Grub2 UEFI SecureBoot`, `Grub2 UEFI HTTP`, `Grub2 UEFI HTTPS`, `Grub2 UEFI HTTPS SecureBoot`, `iPXE Embedded`, `iPXE UEFI HTTP`, `iPXE Chain BIOS`, `iPXE Chain UEFI`
- `--query-organization VALUE` – Organization name to search by
- `--query-organization-id VALUE` – Organization ID to search by
- `--query-organization-label VALUE` – Organization label to search by
- `--realm VALUE` – Name to search by
- `--realm-id NUMBER` – Realm ID
- `--root-password VALUE` – Root password
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER` – Subnet ID
- `--subnet6 VALUE` – Subnet IPv6 name
- `--subnet6-id NUMBER` – Subnet IPv6 ID
- `-h`, `--help` – Print help

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--group-parameters-attributes` "**name**=<string>,**value**=<string>,parameter_type=[string|boolean|integer|real|array|hash|yaml|json],hidden_value=[true|false|1|0], …​ "

## 45.3. hostgroup delete

Delete a host group

**Usage**

```
# hammer hostgroup <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Hostgroup name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

## 45.4. hostgroup delete-parameter

Delete parameter for a hostgroup

**Usage**

```
# hammer hostgroup delete-parameter [OPTIONS]
```

**Options**

- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER`
- `--hostgroup-title VALUE` – Hostgroup title
- `--name VALUE` – Parameter name
- `-h`, `--help` – Print help

## 45.5. hostgroup info

Show a host group

**Usage**

```
# hammer hostgroup <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Hostgroup name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--show-hidden-parameters BOOLEAN` Display hidden parameter values
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Title | x | x | x |
| Model | x | x |  |
| Description | x | x |  |
| Parent | x | x |  |
| Compute profile | x | x |  |
| Compute resource | x | x |  |
| Puppet environment | x | x |  |
| Puppet ca proxy | x | x |  |
| Puppet master proxy | x | x |  |
| Puppetclasses/ | x | x |  |
| Network/subnet ipv4 | x | x |  |
| Network/subnet ipv6 | x | x |  |
| Network/realm | x | x |  |
| Network/domain | x | x |  |
| Operating system/architecture | x | x |  |
| Operating system/operating system | x | x |  |
| Operating system/medium | x | x |  |
| Operating system/partition table | x | x |  |
| Operating system/pxe loader | x | x |  |
| Parameters/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Openscap proxy | x | x |  |
| Content view/id | x | x |  |
| Content view/name | x | x |  |
| Lifecycle environment/id | x | x |  |
| Lifecycle environment/name | x | x |  |
| Content source/id | x | x |  |
| Content source/name | x | x |  |
| Kickstart repository/id | x | x |  |
| Kickstart repository/name | x | x |  |

## 45.6. hostgroup list

List all host groups

**Usage**

```
# hammer hostgroup <list|index> [OPTIONS]
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
- `--puppetclass VALUE` – Name to search by
- `--puppetclass-id VALUE` – ID of Puppetclass
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Title | x | x | x |
| Operating system | x | x |  |
| Puppet environment | x | x |  |
| Model | x | x |  |

**Search and order fields**

- `ansible_role` – string
- `architecture` – string
- `host` – string
- `id` – integer
- `label` – string
- `location` – string
- `location_id` – integer
- `medium` – string
- `name` – string
- `organization` – string
- `organization_id` – integer
- `os` – string
- `os_description` – string
- `os_id` – integer
- `os_major` – string
- `os_minor` – string
- `os_title` – string
- `params` – string
- `template` – string
- `title` – string

## 45.7. hostgroup puppet-classes

List all Puppet classes

**Usage**

```
# hammer hostgroup puppet-classes [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
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

**Search and order fields**

- `config_group` – string
- `environment` – string
- `host` – string
- `hostgroup` – string
- `key` – string
- `location` – string
- `name` – string
- `organization` – string

## 45.8. hostgroup rebuild-config

Rebuild orchestration config

**Usage**

```
# hammer hostgroup rebuild-config [OPTIONS]
```

**Options**

- `--children-hosts BOOLEAN` – Operate on child hostgroup hosts
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Hostgroup name
- `--only LIST` – Limit rebuild steps, valid steps are DHCP, DNS, TFTP, Content_Host_Status, Refresh_Content_Host_Status
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

## 45.9. hostgroup sc-params

List all smart class parameters

**Usage**

```
# hammer hostgroup sc-params [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER`
- `--hostgroup-title VALUE` – Hostgroup title
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
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

## 45.10. hostgroup set-parameter

Create or update parameter for a hostgroup

**Usage**

```
# hammer hostgroup set-parameter [OPTIONS]
```

**Options**

- `--hidden-value BOOLEAN` – Should the value be hidden
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER`
- `--hostgroup-title VALUE` – Hostgroup title
- `--name VALUE` – Parameter name
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json` Default: "string"
- `--value VALUE` – Parameter value
- `-h`, `--help` – Print help

## 45.11. hostgroup update

Update a host group

**Usage**

```
# hammer hostgroup update [OPTIONS]
```

**Options**

- `--ansible-role-ids LIST` – IDs of associated ansible roles
- `--ansible-roles LIST`
- `--architecture VALUE` – Architecture name
- `--architecture-id NUMBER` – Architecture ID
- `--ask-root-password BOOLEAN`
- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id NUMBER` – Compute profile ID
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id NUMBER` – Compute resource ID
- `--config-group-ids LIST` – IDs of associated config groups
- `--config-groups LIST`
- `--content-source VALUE` – Content Source name
- `--content-source-id NUMBER` – Content source ID
- `--content-view VALUE` – Name to search by
- `--content-view-id NUMBER` – Content view ID
- `--description VALUE` – Host group description
- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Domain ID
- `--group-parameters-attributes SCHEMA` Array of parameters
- `--id VALUE`
- `--kickstart-repository VALUE` – Kickstart repository name
- `--kickstart-repository-id NUMBER` – Kickstart repository ID
- `--lifecycle-environment VALUE` – Name to search by
- `--lifecycle-environment-id NUMBER` – Lifecycle environment ID
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--medium VALUE` – Medium name
- `--medium-id NUMBER` – Media ID
- `--name VALUE` – Name of the host group
- `--new-name VALUE` – Name of the host group
- `--openscap-proxy-id NUMBER` – ID of OpenSCAP Capsule
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – Operating system ID
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--parent VALUE` – Name of parent hostgroup
- `--parent-id NUMBER` – Parent ID of the host group
- `--parent-title VALUE` – Title of parent hostgroup
- `--partition-table VALUE` – Partition table name
- `--partition-table-id NUMBER` – Partition table ID
- `--puppet-ca-proxy VALUE` – Name of Puppet CA proxy
- `--puppet-ca-proxy-id NUMBER` – Puppet CA Capsule ID
- `--puppet-class-ids LIST` – List of Puppet class ids
- `--puppet-classes LIST`
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` – ID of associated Puppet environment
- `--puppet-proxy VALUE` – Name of Puppet proxy
- `--puppet-proxy-id NUMBER` – Puppet Capsule ID
- `--pxe-loader ENUM` – DHCP filename option (Grub2/PXELinux by default) Possible value(s): `None`, `PXELinux BIOS`, `PXELinux UEFI`, `Grub2 BIOS`, `Grub2 ELF`, `Grub2 UEFI`, `Grub2 UEFI SecureBoot`, `Grub2 UEFI HTTP`, `Grub2 UEFI HTTPS`, `Grub2 UEFI HTTPS SecureBoot`, `iPXE Embedded`, `iPXE UEFI HTTP`, `iPXE Chain BIOS`, `iPXE Chain UEFI`
- `--query-organization VALUE` – Organization name to search by
- `--query-organization-id VALUE` – Organization ID to search by
- `--query-organization-label VALUE` – Organization label to search by
- `--realm VALUE` – Name to search by
- `--realm-id NUMBER` – Realm ID
- `--root-password VALUE` – Root password
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER` – Subnet ID
- `--subnet6 VALUE` – Subnet IPv6 name
- `--subnet6-id NUMBER` – Subnet IPv6 ID
- `--title VALUE` – Hostgroup title
- `-h`, `--help` – Print help

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--group-parameters-attributes` "name=<string>,value=<string>,parameter_type=[string|boolean|integer|real|array|hash|yaml|json],hidden_value=[true|false|1|0], …​ "
