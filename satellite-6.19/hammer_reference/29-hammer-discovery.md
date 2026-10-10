---
title: "discovery"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "29"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-discovery"
---
# Chapter 29. discovery

Manipulate discovered hosts.

**Usage**

```
# hammer discovery [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 29.1. discovery auto-provision

Auto provision a host

**Usage**

```
# hammer discovery auto-provision [OPTIONS]
```

**Options**

- `--all` – Auto provision all discovered hosts
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 29.2. discovery delete

Delete a discovered host

**Usage**

```
# hammer discovery <delete|destroy> [OPTIONS]
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

## 29.3. discovery facts

List all fact values

**Usage**

```
# hammer discovery facts [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
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
| Fact | x | x |
| Value | x | x |

**Search and order fields**

- `fact` – string
- `fact_short_name` – string
- `facts` – string
- `host` – string
- `host.hostgroup` – string
- `host_id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
- `origin` – string
- `reported_at` – datetime
- `short_name` – string
- `type` – string
- `value` – string

## 29.4. discovery info

Show a discovered host

**Usage**

```
# hammer discovery <info|show> [OPTIONS]
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
| Mac | x | x |  |
| Cpus | x | x |  |
| Memory | x | x |  |
| Disk count | x | x |  |
| Disks size | x | x |  |
| Subnet | x | x |  |
| Last report | x | x |  |
| Ip | x | x |  |
| Model | x | x |  |
| Organization | x | x |  |
| Location | x | x |  |

## 29.5. discovery list

List all discovered hosts

**Usage**

```
# hammer discovery <list|index> [OPTIONS]
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
| Mac | x | x |  |
| Cpus | x | x |  |
| Memory | x | x |  |
| Disk count | x | x |  |
| Disks size | x | x |  |
| Subnet | x | x |  |
| Last report | x | x |  |

## 29.6. discovery provision

Provision a discovered host

**Usage**

```
# hammer discovery provision [OPTIONS]
```

**Options**

- `--architecture VALUE` – Architecture name
- `--architecture-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--ask-root-password BOOLEAN`
- `--build BOOLEAN`
- `--capabilities VALUE`
- `--config-group-ids LIST` – IDs of associated config groups
- `--config-groups LIST`
- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--enabled BOOLEAN`
- `--environment VALUE` – Environment name (--environment is deprecated: Use `--puppet-environment[-id]` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--puppet-environment[-id]` instead)
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER`
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE`
- `--image VALUE` – Name to search by
- `--image-id NUMBER`
- `--interface KEY_VALUE_LIST` – Interface parameters Can be specified multiple times.
- `--ip VALUE` – Not required if using a subnet with DHCP Capsule
- `--ip6 VALUE` – Not required if using an IPv6 subnet with DHCP Capsule
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mac VALUE` – Not required if it`s a virtual machine
- `--managed BOOLEAN`
- `--medium VALUE` – Medium name
- `--medium-id VALUE` – Required if not imaged based provisioning and host is managed and value is not inherited from host group
- `--model VALUE` – Model name
- `--model-id NUMBER`
- `--name VALUE`
- `--new-name VALUE`
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--overwrite BOOLEAN`
- `--owner-id NUMBER`
- `--owner-type ENUM` – Host`s owner type Possible value(s): `User`, `Usergroup`
- `--parameters KEY_VALUE_LIST` – Host parameters
- `--partition-table VALUE` – Partition table name
- `--partition-table-id NUMBER`
- `--progress-report-id VALUE` – UUID to track orchestration tasks status, GET /api/orchestration/:UUID/tasks
- `--provision-method ENUM` – Possible value(s): `build`, `image`
- `--puppet-ca-proxy VALUE` – Name of Puppet CA proxy
- `--puppet-ca-proxy-id NUMBER`
- `--puppet-class-ids LIST` – List of Puppet class ids
- `--puppet-classes LIST`
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` ID of associated Puppet environment
- `--puppet-proxy VALUE` – Name of Puppet proxy
- `--puppet-proxy-id NUMBER`
- `--pxe-loader ENUM` – DHCP filename option (Grub2 or PXELinux by default) Possible value(s): `None`, `PXELinux BIOS`, `PXELinux UEFI`, `Grub2 BIOS`, `Grub2 ELF`, `Grub2 UEFI`, `Grub2 UEFI SecureBoot`, `Grub2 UEFI HTTP`, `Grub2 UEFI HTTPS`, `Grub2 UEFI HTTPS SecureBoot`, `iPXE Embedded`, `iPXE UEFI HTTP`, `iPXE Chain BIOS`, `iPXE Chain UEFI`
- `--root-password VALUE`
- `--sp-subnet-id NUMBER`
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--subnet6-id NUMBER` – Required if host is managed, does not have IPv4 IP / Subnet, or the value is not inherited from the host group
- `-h`, `--help` – Print help

## 29.7. discovery reboot

Reboot a host

**Usage**

```
# hammer discovery reboot [OPTIONS]
```

**Options**

- `--all` – Reboot all discovered hosts
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 29.8. discovery refresh-facts

Refresh the facts of a host

**Usage**

```
# hammer discovery refresh-facts [OPTIONS]
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
