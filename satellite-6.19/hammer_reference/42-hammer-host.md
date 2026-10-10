---
title: "host"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "42"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-host"
---
# Chapter 42. host

Manipulate hosts

**Usage**

```
# hammer host [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 42.1. host ansible-roles

Manage Ansible roles on a host

**Usage**

```
# hammer host ansible-roles [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.1.1. host ansible-roles add

Associate an Ansible role

**Usage**

```
# hammer host ansible-roles add [OPTIONS]
```

**Options**

- `--ansible-role VALUE` – Name to search by
- `--ansible-role-id NUMBER`
- `--force` – Associate the Ansible role even if it already is associated indirectly
- `--id VALUE`
- `--name VALUE` – Host name
- `-h`, `--help` – Print help

### 42.1.2. host ansible-roles assign

Assigns Ansible roles to a host

**Usage**

```
# hammer host ansible-roles assign [OPTIONS]
```

**Options**

- `--ansible-role-ids LIST` – Ansible roles to assign to a host
- `--ansible-roles LIST`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 42.1.3. host ansible-roles list

List all Ansible roles for a host

**Usage**

```
# hammer host ansible-roles <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
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
| Inherited | x | x |  |
| Directly assigned | x | x |  |

### 42.1.4. host ansible-roles play

Runs all Ansible roles on a host

**Usage**

```
# hammer host ansible-roles play [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 42.1.5. host ansible-roles remove

Disassociate an Ansible role

**Usage**

```
# hammer host ansible-roles remove [OPTIONS]
```

**Options**

- `--ansible-role VALUE` – Name to search by
- `--ansible-role-id NUMBER`
- `--id VALUE`
- `--name VALUE` – Host name
- `-h`, `--help` – Print help

## 42.2. host boot

Boot host from specified device

**Usage**

```
# hammer host boot [OPTIONS]
```

**Options**

- `--device VALUE` – Boot device, valid devices are disk, cdrom, pxe, bios
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.3. host bootc

Manage bootc images on your hosts

**Usage**

```
# hammer host bootc [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.3.1. host bootc images

List booted bootc container images for hosts

**Usage**

```
# hammer host bootc images [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Running image | x | x |
| Running image digest | x | x |
| Host count | x | x |

## 42.4. host config-reports

List all reports

**Usage**

```
# hammer host config-reports [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – Host id
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
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
| Host | x | x |  |
| Last report | x | x |  |
| Origin | x | x |  |
| Applied | x | x |  |
| Restarted | x | x |  |
| Failed | x | x |  |
| Restart failures | x | x |  |
| Skipped | x | x |  |
| Pending | x | x |  |

**Search and order fields**

- `applied` – integer
- `eventful` – Values: true, false
- `failed` – integer
- `failed_restarts` – integer
- `host` – string
- `host_id` – integer
- `host_owner_id` – integer
- `hostgroup` – string
- `hostgroup_fullname` – string
- `hostgroup_title` – string
- `id` – integer
- `last_report` – datetime
- `location` – string
- `log` – text
- `organization` – string
- `origin` – string
- `pending` – integer
- `reported` – datetime
- `resource` – text
- `restarted` – integer
- `skipped` – integer

## 42.5. host create

Create a host

**Usage**

```
# hammer host create [OPTIONS]
```

**Options**

- `--ansible-role-ids LIST` – IDs of associated ansible roles
- `--ansible-roles LIST`
- `--architecture VALUE` – Architecture name
- `--architecture-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--ask-root-password BOOLEAN`
- `--build BOOLEAN`
- `--comment VALUE` – Additional information about this host
- `--compute-attributes KEY_VALUE_LIST` – Compute resource attributes
- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id NUMBER`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id NUMBER` – Nil means host is bare metal
- `--config-group-ids LIST` – IDs of associated config groups
- `--config-groups LIST`
- `--content-source VALUE` – Content Source name
- `--content-source-id NUMBER` – Id of the Capsule from which the host consumes content.
- `--content-view VALUE` – Name to search by
- `--content-view-environment-ids LIST` – Array of content view environment ids to be associated with the host. Ignored if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-environments LIST` – Comma-separated list of content view environment labels to be associated with the host, in the format of `lifecycle_environment_label/content_view_label`. Ignored if content_view_environment_ids is specified, or if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-id NUMBER` – Id of the single content view to be associated with the host.
- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--enabled BOOLEAN` – Include this host within Satellite reporting
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER` – ID of the host group. Note: Changing the host group will re-apply attributes inherited from the new host group, unless you explicitly override them again in the update request
- `--hostgroup-title VALUE` – Hostgroup title
- `--hypervisor-guest-uuids LIST` – List of hypervisor guest uuids
- `--image VALUE` – Name to search by
- `--image-id NUMBER`
- `--installed-products-attributes SCHEMA` List of products installed on the host
- `--interface KEY_VALUE_LIST` – Interface parameters Can be specified multiple times.
- `--ip VALUE` – Not required if using a subnet with DHCP Capsule
- `--kickstart-repository VALUE` – Kickstart repository name
- `--kickstart-repository-id NUMBER` – Repository Id associated with the kickstart repo used for provisioning
- `--lifecycle-environment VALUE` – Name to search by
- `--lifecycle-environment-id NUMBER` – Id of the single lifecycle environment to be associated with the host.
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mac VALUE` – Required for managed host that is bare metal, not required if it`s a virtual machine
- `--managed BOOLEAN` – True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not
- `--medium VALUE` – Medium name
- `--medium-id VALUE` – Required if not imaged based provisioning and host is managed and value is not inherited from host group
- `--model VALUE` – Model name
- `--model-id NUMBER`
- `--name VALUE`
- `--openscap-proxy-id NUMBER` – ID of OpenSCAP Capsule
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--overwrite BOOLEAN` – Default: "true"
- `--owner VALUE` – Login of the owner
- `--owner-id VALUE` – ID of the owner
- `--owner-type ENUM` – Host`s owner type Possible value(s): `User`, `Usergroup`
- `--parameters KEY_VALUE_LIST` – Replaces with new host parameters
- `--partition-table VALUE` – Partition table name
- `--partition-table-id NUMBER` – Required if host is managed and custom partition has not been defined
- `--product VALUE` – Name to search by
- `--product-id NUMBER` – Product id as listed from a host`s installed products, this is not the same product id as the products api returns
- `--progress-report-id VALUE` – UUID to track orchestration tasks status, GET /api/orchestration/:UUID/tasks
- `--provision-method ENUM` – The method used to provision the host. Possible value(s): `build`, `image`, `bootdisk`
- `--puppet-ca-proxy VALUE` – Name of Puppet CA proxy
- `--puppet-ca-proxy-id NUMBER` – Puppet CA Capsule ID
- `--puppet-class-ids LIST` – List of Puppet class ids
- `--puppet-classes LIST`
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` – ID of associated Puppet environment
- `--puppet-proxy VALUE` – Name of Puppet proxy
- `--puppet-proxy-id NUMBER` – Puppet Capsule ID
- `--purpose-role VALUE` – Sets the system purpose usage
- `--purpose-usage VALUE` – Sets the system purpose usage
- `--pxe-loader ENUM` – DHCP filename option (Grub2/PXELinux by default) Possible value(s): `None`, `PXELinux BIOS`, `PXELinux UEFI`, `Grub2 BIOS`, `Grub2 ELF`, `Grub2 UEFI`, `Grub2 UEFI SecureBoot`, `Grub2 UEFI HTTP`, `Grub2 UEFI HTTPS`, `Grub2 UEFI HTTPS SecureBoot`, `iPXE Embedded`, `iPXE UEFI HTTP`, `iPXE Chain BIOS`, `iPXE Chain UEFI`
- `--realm VALUE` – Name to search by
- `--realm-id NUMBER`
- `--release-version VALUE` – Release version for this Host to use (7Server, 7.1, etc)
- `--root-password VALUE` – Required if host is managed and value is not inherited from host group or default password in settings
- `--service-level VALUE` – Service level
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--typed-parameters SCHEMA` – Replaces with new host parameters (with type support)
- `--volume KEY_VALUE_LIST` – Volume parameters Can be specified multiple times.
- `-h`, `--help` – Print help

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--typed-parameters` "**name**=<string>,**value**=<string>,parameter_type=[string|boolean|integer|real|array|hash|yaml|json],hidden_value=[true|false|1|0], …​ "
- `--installed-products-attributes` "product_id=<string>,product_name=<string>,arch=<string>,version=<string>, …​ "

Available keys for `--interface:` mac ip type Possible values: interface, bmc, bond, bridge name subnet_id domain_id identifier managed true/false primary true/false, each managed hosts needs to have one primary interface. provision true/false virtual true/false

For virtual=true: tag VLAN tag, this attribute has precedence over the subnet VLAN ID. Only for virtual interfaces. attached_to Identifier of the interface to which this interface belongs, e.g. eth1.

For type=bond: mode Possible values: balance-rr, active-backup, balance-xor, broadcast, 802.3ad, balance-tlb, balance-alb attached_devices Identifiers of slave interfaces, e.g. [eth1,eth2] bond_options

For type=bmc: provider always IPMI username password

**Provider-specific options**

Bold attributes are required.

EC2:

- `--volume`:
- `--interface`:
- `--compute-attributes`:

  - `availability_zone` –
  - `flavor_id` –
  - `groups` –
  - `security_group_ids` –
  - `managed_ip` –

Libvirt:

- `--volume`:

  - `pool_name` – One of available storage pools
  - `capacity` – String value, e.g. 10G
  - `allocation` – Initial allocation, e.g. 0G
  - `format_type` – Possible values: raw, qcow2
- `--interface`:

  - `compute_type` – Possible values: bridge, network
  - `compute_bridge` – Name of interface according to type
  - `compute_model` – Possible values: virtio, rtl8139, ne2k_pci, pcnet, e1000
  - `compute_network` – Libvirt instance network, e.g. default
- `--compute-attributes`:

  - `cpus` – Number of CPUs
  - `memory` – String, amount of memory, value in bytes
  - `boot_order` – Device names to specify the boot order
  - `firmware` – automatic/bios/uefi/uefi_secure_boot (UEFI with Secure Boot enabled)
  - `start` – Boolean (expressed as 0 or 1), whether to start the machine or not

OpenStack:

- `--volume`:
- `--interface`:
- `--compute-attributes`:

  - `availability_zone` –
  - `boot_from_volume` –
  - `flavor_ref` –
  - `image_ref` –
  - `tenant_id` –
  - `security_groups` –
  - `network` –

VMware:

- `--volume`:

  - `name` –
  - `storage_pod` – Storage Pod ID from VMware
  - `datastore` – Datastore ID from VMware
  - `mode` – persistent/independent_persistent/independent_nonpersistent
  - `size_gb` – Integer number, volume size in GB
  - `thin` – true/false
  - `eager_zero` – true/false
  - `controller_key` – Associated controller key
- `--interface`:

  - `compute_type` – Type of the network adapter, for example one of: VirtualVmxnet3, VirtualE1000, See documentation center for your version of vSphere to find more details about available adapter types: <https://www.vmware.com/support/pubs/>
  - `compute_network` – Network ID or Network Name from VMware
- `--compute-attributes`:

  - `cluster` – Cluster ID from VMware
  - `corespersocket` – Number of cores per socket (applicable to hardware versions < 10 only)
  - `cpus` – CPU count
  - `memory_mb` – Integer number, amount of memory in MB
  - `path` – Path to folder
  - `resource_pool` – Resource Pool ID from VMware
  - `firmware` – automatic/bios/uefi/uefi_secure_boot (UEFI with Secure Boot enabled)
  - `guest_id` – Guest OS ID form VMware
  - `hardware_version` – Hardware version ID from VMware
  - `memoryHotAddEnabled` – Must be a 1 or 0, lets you add memory resources while the machine is on
  - `cpuHotAddEnabled` – Must be a 1 or 0, lets you add CPU resources while the machine is on
  - `add_cdrom` – Must be a 1 or 0, Add a CD-ROM drive to the virtual machine
  - `annotation` – Annotation Notes
  - `scsi_controllers` – List with SCSI controllers definitions

    - `type` – ID of the controller type from VMware
    - `key` – Key of the controller (e.g. 1000)
  - `nvme_controllers` – List with NVME controllers definitions

    - `type` – ID of the controller type from VMware
    - `key` – Key of the controller (e.g. 2000)
  - `boot_order` – Device names to specify the boot order
  - `virtual_tpm` – Must be a 1 or 0, Enable virtual TPM. Only compatible with EFI firmware.
  - `start` – Must be a 1 or 0, whether to start the machine or not

AzureRM:

- `--volume`:

  - `disk_size_gb` – Volume Size in GB (integer value)
  - `data_disk_caching` – Data Disk Caching (None, ReadOnly, ReadWrite)
- `--interface`:

  - `compute_network` – Select one of available Azure Subnets, must be an ID
  - `compute_public_ip` – Public IP (None, Static, Dynamic)
  - `compute_private_ip` – Static Private IP (expressed as true or false)
- `--compute-attributes`:

  - `resource_group` – Existing Azure Resource Group of user
  - `vm_size` – VM Size, eg. Standard_A0 etc.
  - `username` – The Admin username
  - `password` – The Admin password
  - `platform` – OS type eg. Linux
  - `ssh_key_data` – SSH key for passwordless authentication
  - `os_disk_caching` – OS disk caching
  - `premium_os_disk` – Premium OS Disk, Boolean as 0 or 1
  - `script_command` – Custom Script Command
  - `script_uris` – Comma seperated file URIs

GCE:

- `--volume`:

  - `size_gb` – Volume size in GB, integer value
- `--interface`:
- `--compute-attributes`:

  - `machine_type` –
  - `network` –
  - `associate_external_ip` –

## 42.6. host deb-package

Manage deb packages on your hosts

**Usage**

```
# hammer host deb-package [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.6.1. host deb-package list

List deb packages installed on the host

**Usage**

```
# hammer host deb-package <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – ID of the host
- `--include-latest-upgradable BOOLEAN` Also include the latest upgradable package version for each host package
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--status VALUE` – Return only packages of a particular status (upgradable or up-to-date)
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Version | x | x |  |
| Arch | x | x |  |

**Search and order fields**

- `architecture` – string
- `id` – integer
- `name` – string
- `version` – string

## 42.7. host delete

Delete a host

**Usage**

```
# hammer host <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.8. host delete-parameter

Delete parameter for a host

**Usage**

```
# hammer host delete-parameter [OPTIONS]
```

**Options**

- `--host VALUE` – Host name
- `--host-id NUMBER`
- `--name VALUE` – Parameter name
- `-h`, `--help` – Print help

## 42.9. host disassociate

Disassociate a host

**Usage**

```
# hammer host disassociate [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.10. host enc-dump

Dump host’s ENC YAML

**Usage**

```
# hammer host enc-dump [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.11. host errata

Manage errata on your hosts

**Usage**

```
# hammer host errata [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.11.1. host errata apply

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_errata_install`.

**Usage**

```
# hammer host errata apply [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_errata_install`.

Unfortunately the server does not support such operation.

### 42.11.2. host errata info

Retrieve a single errata for a host

**Usage**

```
# hammer host errata info [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id NUMBER` – Host ID
- `--id VALUE` – Errata id of the erratum (RHSA-2012:108)
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Title | x | x |
| Version | x | x |
| Description | x | x |
| Status | x | x |
| Id | x | x |
| Errata id | x | x |
| Reboot suggested | x | x |
| Updated | x | x |
| Issued | x | x |
| Release | x | x |
| Solution | x | x |
| Packages | x | x |
| Module streams/name | x | x |
| Module streams/stream | x | x |
| Module streams/packages | x | x |

### 42.11.3. host errata list

List errata available for the content host

**Usage**

```
# hammer host errata list [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Calculate Applicable Errata based on a particular Content View
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – UUID of the content host
- `--include-applicable BOOLEAN` – Return errata that are applicable to this host. Defaults to false)
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Calculate Applicable Errata based on a particular Environment
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--severity VALUE` – Return only errata of a particular severity (None, Low, Moderate, Important, Critical)
- `--type VALUE` – Return only errata of a particular type (security, bugfix, enhancement, other)
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Erratum id | x | x |
| Type | x | x |
| Title | x | x |
| Installable | x | x |

### 42.11.4. host errata recalculate

Force regenerate applicability.

**Usage**

```
# hammer host errata recalculate [OPTIONS]
```

**Options**

- `--host VALUE` – Host name
- `--host-id NUMBER` – Host ID
- `-h`, `--help` – Print help

## 42.12. host facts

List all fact values

**Usage**

```
# hammer host facts [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
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

## 42.13. host info

Show a host

**Usage**

```
# hammer host <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--show-hidden-parameters BOOLEAN` Display hidden parameter values
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Uuid | x | x |  |
| Name | x | x | x |
| Organization | x | x |  |
| Location | x | x |  |
| Puppet environment | x | x |  |
| Puppet ca proxy | x | x |  |
| Puppet master proxy | x | x |  |
| Host group | x | x |  |
| Compute resource | x | x |  |
| Compute profile | x | x |  |
| Cert name | x | x |  |
| Token | x | x |  |
| Managed | x | x |  |
| Installed at | x | x |  |
| Last report | x | x |  |
| Uptime (seconds) | x | x |  |
| Status/global status | x | x |  |
| Status/build status | x | x |  |
| Network/ipv4 address | x | x |  |
| Network/ipv6 address | x | x |  |
| Network/mac | x | x |  |
| Network/subnet ipv4 | x | x |  |
| Network/subnet ipv6 | x | x |  |
| Network/domain | x | x |  |
| Network/service provider/sp name | x | x |  |
| Network/service provider/sp ip | x | x |  |
| Network/service provider/sp mac | x | x |  |
| Network/service provider/sp subnet | x | x |  |
| Network interfaces/id | x | x |  |
| Network interfaces/identifier | x | x |  |
| Network interfaces/type | x | x |  |
| Network interfaces/mac address | x | x |  |
| Network interfaces/ipv4 address | x | x |  |
| Network interfaces/ipv6 address | x | x |  |
| Network interfaces/fqdn | x | x |  |
| Operating system/architecture | x | x |  |
| Operating system/operating system | x | x |  |
| Operating system/build | x | x |  |
| Operating system/medium | x | x |  |
| Operating system/partition table | x | x |  |
| Operating system/pxe loader | x | x |  |
| Operating system/custom partition table | x | x |  |
| Operating system/image | x | x |  |
| Operating system/image file | x | x |  |
| Operating system/use image | x | x |  |
| Parameters/ | x | x |  |
| All parameters/ | x | x |  |
| Additional info/owner | x | x |  |
| Additional info/owner id | x | x |  |
| Additional info/owner type | x | x |  |
| Additional info/enabled | x | x |  |
| Additional info/model | x | x |  |
| Additional info/comment | x | x |  |
| Openscap proxy | x | x |  |
| Content information/content view environment labels | x | x |  |
| Content information/content view environments/content view/id | x |  |  |
| Content information/content view environments/content view/name | x |  |  |
| Content information/content view environments/content view/composite | x |  |  |
| Content information/content view environments/content view/rolling | x |  |  |
| Content information/content view environments/content view id | x | x |  |
| Content information/content view environments/content view name | x | x |  |
| Content information/content view environments/composite content view | x | x |  |
| Content information/content view environments/rolling content view | x | x |  |
| Content information/content view environments/lifecycle environment/id | x |  |  |
| Content information/content view environments/lifecycle environment/name | x |  |  |
| Content information/content view environments/lifecycle environment id | x | x |  |
| Content information/content view environments/lifecycle environment name | x | x |  |
| Content information/content view environments/label | x | x |  |
| Content information/content source/id | x | x |  |
| Content information/content source/name | x | x |  |
| Content information/kickstart repository/id | x | x |  |
| Content information/kickstart repository/name | x | x |  |
| Content information/applicable packages | x | x |  |
| Content information/upgradable packages | x | x |  |
| Content information/applicable errata/enhancement | x | x |  |
| Content information/applicable errata/bug fix | x | x |  |
| Content information/applicable errata/security | x | x |  |
| Subscription information/uuid | x | x |  |
| Subscription information/last checkin | x | x |  |
| Subscription information/release version | x | x |  |
| Subscription information/registered to | x | x |  |
| Subscription information/registered at | x | x |  |
| Subscription information/registered by activation keys/ | x | x |  |
| Subscription information/system purpose/service level | x | x |  |
| Subscription information/system purpose/purpose usage | x | x |  |
| Subscription information/system purpose/purpose role | x | x |  |
| Bootc image information/running image | x | x |  |
| Bootc image information/running image digest | x | x |  |
| Bootc image information/staged image | x | x |  |
| Bootc image information/staged image digest | x | x |  |
| Bootc image information/available image | x | x |  |
| Bootc image information/available image digest | x | x |  |
| Bootc image information/rollback image | x | x |  |
| Bootc image information/rollback image digest | x | x |  |
| Trace status | x | x |  |
| Host collections/id | x | x |  |
| Host collections/name | x | x |  |

## 42.14. host interface

View and manage host’s network interfaces

**Usage**

```
# hammer host interface [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.14.1. host interface create

Create an interface on a host

**Usage**

```
# hammer host interface create [OPTIONS]
```

**Options**

- `--attached-devices LIST` – Identifiers of attached interfaces, e.g. `` [`eth1 ``, `eth2`]`. For bond interfaces those are the slaves. Only for bond and bridges interfaces.
- `--attached-to VALUE` – Identifier of the interface to which this interface belongs, e.g. eth1. Only for virtual interfaces.
- `--bond-options VALUE` – Space separated options, e.g. miimon=100. Only for bond interfaces.
- `--compute-attributes KEY_VALUE_LIST` Compute resource specific attributes
- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Satellite domain ID of interface. Required for primary interfaces on managed hosts.
- `--execution BOOLEAN` – Should this interface be used for remote execution?
- `--host VALUE` – Host name
- `--host-id VALUE` – ID or name of host
- `--identifier VALUE` – Device identifier, e.g. eth0 or eth1.1
- `--ip VALUE` – IPv4 address of interface
- `--ip6 VALUE` – IPv6 address of interface
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mac VALUE` – MAC address of interface. Required for managed interfaces on bare metal.
- `--managed BOOLEAN` – Should this interface be managed via DHCP and DNS Capsule and should it be configured during provisioning?
- `--mode ENUM` – Bond mode of the interface, e.g. balance-rr. Only for bond interfaces. Possible value(s): `balance-rr`, `active-backup`, `balance-xor`, `broadcast`, `802.3ad`, `balance-tlb`, `balance-alb`
- `--mtu NUMBER` – MTU, this attribute has precedence over the subnet MTU.
- `--name VALUE` – Interface`s DNS name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--password VALUE` – Only for BMC interfaces.
- `--primary` – Should this interface be used for constructing the FQDN of the host? Each managed hosts needs to have one primary interface
- `--provider ENUM` – Interface provider, e.g. IPMI. Only for BMC interfaces. Possible value(s): `IPMI`, `Redfish`, `SSH`
- `--provision` – Should this interface be used for TFTP of PXELinux (or SSH for image-based hosts)? Each managed hosts needs to have one provision interface
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER` – Satellite subnet ID of IPv4 interface
- `--subnet6-id NUMBER` – Satellite subnet ID of IPv6 interface
- `--tag VALUE` – VLAN tag, this attribute has precedence over the subnet VLAN ID. Only for virtual interfaces.
- `--type ENUM` – Interface type, e.g. bmc. Default is interface Possible value(s): `interface`, `bmc`, `bond`, `bridge`
- `--username VALUE` – Only for BMC interfaces.
- `--virtual BOOLEAN` – Alias or VLAN device
- `-h`, `--help` – Print help

### 42.14.2. host interface delete

Delete a host’s interface

**Usage**

```
# hammer host interface <delete|destroy> [OPTIONS]
```

**Options**

- `--host VALUE` – Host name
- `--host-id VALUE` – ID or name of host
- `--id VALUE` – ID of interface
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 42.14.3. host interface info

Show an interface for host

**Usage**

```
# hammer host interface <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id VALUE` – ID or name of host
- `--id VALUE` – ID or name of interface
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Identifier | x | x |  |
| Type | x | x |  |
| Mac address | x | x |  |
| Ip address | x | x |  |
| Dns name | x | x |  |
| Subnet | x | x |  |
| Domain | x | x |  |
| Managed | x | x |  |
| Primary | x | x |  |
| Provision | x | x |  |
| Virtual | x | x |  |
| Tag | x | x |  |
| Attached to | x | x |  |
| Bmc/username | x | x |  |
| Bmc/provider | x | x |  |
| Bond/mode | x | x |  |
| Bond/attached devices | x | x |  |
| Bond/bond options | x | x |  |
| Execution | x | x |  |

### 42.14.4. host interface list

List all interfaces for host

**Usage**

```
# hammer host interface <list|index> [OPTIONS]
```

**Options**

- `--domain VALUE` – Domain name
- `--domain-id VALUE` – ID or name of domain
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id VALUE` – ID or name of host
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--subnet VALUE` – Subnet name
- `--subnet-id VALUE` – ID or name of subnet
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Identifier | x | x |  |
| Type | x | x |  |
| Mac address | x | x |  |
| Ip address | x | x |  |
| Dns name | x | x |  |

### 42.14.5. host interface update

Update a host’s interface

**Usage**

```
# hammer host interface update [OPTIONS]
```

**Options**

- `--attached-devices LIST` – Identifiers of attached interfaces, e.g. `` [`eth1 ``, `eth2`]`. For bond interfaces those are the slaves. Only for bond and bridges interfaces.
- `--attached-to VALUE` – Identifier of the interface to which this interface belongs, e.g. eth1. Only for virtual interfaces.
- `--bond-options VALUE` – Space separated options, e.g. miimon=100. Only for bond interfaces.
- `--compute-attributes KEY_VALUE_LIST` Compute resource specific attributes
- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Satellite domain ID of interface. Required for primary interfaces on managed hosts.
- `--execution BOOLEAN` – Should this interface be used for remote execution?
- `--host VALUE` – Host name
- `--host-id VALUE` – ID or name of host
- `--id VALUE` – ID of interface
- `--identifier VALUE` – Device identifier, e.g. eth0 or eth1.1
- `--ip VALUE` – IPv4 address of interface
- `--ip6 VALUE` – IPv6 address of interface
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mac VALUE` – MAC address of interface. Required for managed interfaces on bare metal.
- `--managed BOOLEAN` – Should this interface be managed via DHCP and DNS Capsule and should it be configured during provisioning?
- `--mode ENUM` – Bond mode of the interface, e.g. balance-rr. Only for bond interfaces. Possible value(s): `balance-rr`, `active-backup`, `balance-xor`, `broadcast`, `802.3ad`, `balance-tlb`, `balance-alb`
- `--mtu NUMBER` – MTU, this attribute has precedence over the subnet MTU.
- `--name VALUE` – Interface`s DNS name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--password VALUE` – Only for BMC interfaces.
- `--primary` – Should this interface be used for constructing the FQDN of the host? Each managed hosts needs to have one primary interface
- `--provider ENUM` – Interface provider, e.g. IPMI. Only for BMC interfaces. Possible value(s): `IPMI`, `Redfish`, `SSH`
- `--provision` – Should this interface be used for TFTP of PXELinux (or SSH for image-based hosts)? Each managed hosts needs to have one provision interface
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER` – Satellite subnet ID of IPv4 interface
- `--subnet6-id NUMBER` – Satellite subnet ID of IPv6 interface
- `--tag VALUE` – VLAN tag, this attribute has precedence over the subnet VLAN ID. Only for virtual interfaces.
- `--type ENUM` – Interface type, e.g. bmc. Default is interface Possible value(s): `interface`, `bmc`, `bond`, `bridge`
- `--username VALUE` – Only for BMC interfaces.
- `--virtual BOOLEAN` – Alias or VLAN device
- `-h`, `--help` – Print help

## 42.15. host list

List all hosts

**Usage**

```
# hammer host <list|index> [OPTIONS]
```

**Options**

- `--environment VALUE` – Name to search by
- `--environment-id VALUE` – ID of puppet environment
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
- `--location VALUE` – Set the current location context for the request
- `--location-id VALUE` – ID of location
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id VALUE` – ID of organization
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` ID of associated Puppet environment
- `--search VALUE` – Filter results
- `--thin BOOLEAN` – Only list ID and name of hosts
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Operating system | x | x |  |
| Host group | x | x |  |
| Ip | x | x |  |
| Mac | x | x |  |
| Global status | x | x |  |
| Organization | x |  |  |
| Location | x |  |  |
| Additional information | x |  |  |
| Content view environments | x | x |  |
| Multi content view environment | x | x |  |
| Security | x |  |  |
| Bugfix | x |  |  |
| Enhancement | x |  |  |
| Running image | x |  |  |
| Running image digest | x |  |  |
| Staged image | x |  |  |
| Staged image digest | x |  |  |
| Available image | x |  |  |
| Available image digest | x |  |  |
| Rollback image | x |  |  |
| Rollback image digest | x |  |  |
| Trace status | x | x |  |
| Last checkin | x | x |  |

**Search and order fields**

- `activation_key` – string
- `activation_key_id` – string
- `applicable_debs` – string
- `applicable_errata` – string
- `applicable_errata_issued` – date
- `applicable_rpms` – string
- `architecture` – string
- `boot_time`
- `bootc_available_digest` – string
- `bootc_available_image` – string
- `bootc_booted_digest` – string
- `bootc_booted_image` – string
- `bootc_rollback_digest` – string
- `bootc_rollback_image` – string
- `bootc_staged_digest` – string
- `bootc_staged_image` – string
- `build` – Values: true, false
- `build_status` – Values: built, pending, token_expired, build_failed
- `comment` – text
- `compute_resource` – string
- `compute_resource_id` – integer
- `configuration_status.applied` – integer
- `configuration_status.enabled` – Values: true, false
- `configuration_status.failed` – integer
- `configuration_status.failed_restarts` – integer
- `configuration_status.interesting` – Values: true, false
- `configuration_status.pending` – integer
- `configuration_status.restarted` – integer
- `configuration_status.skipped` – integer
- `content_source` – string
- `content_views` – string
- convert2rhel_through_foreman integer
- `created_at` – datetime
- `domain` – string
- `domain_id` – integer
- `errata_status` – Values: security_needed, errata_needed, updated, unknown
- `execution_status` – Values: ok, error
- `facts` – string
- `global_status` – Values: ok, warning, error
- `has_ip` – string
- has_ip6 string
- `has_mac` – string
- `hostgroup` – string
- `hostgroup_fullname` – string
- `hostgroup_id` – integer
- `hostgroup_name` – string
- `hostgroup_title` – string
- `hypervisor` – boolean
- `hypervisor_host` – string
- `id` – integer
- `image` – string
- `image_mode` – Values: true, false
- `infrastructure_facet.foreman` – Values: true, false
- `infrastructure_facet.smart_proxy_id`
- `insights_client_report_status` – Values: reporting, no_report
- `insights_inventory_sync_status` – Values: disconnect, sync
- `insights_recommendations_count` – integer
- `insights_uuid` – string
- `installable_errata` – string
- `installed_at` – datetime
- `ip` – string
- ip6 string
- `job_invocation.id` – string
- `job_invocation.result` – Values: cancelled, failed, pending, success
- `last_checkin` – datetime
- `last_report` – datetime
- `lifecycle_environments` – string
- `location` – string
- `location_id` – integer
- `mac` – string
- `managed` – Values: true, false
- `model` – string
- `name` – string
- `organization` – string
- `organization_id` – integer
- `origin` – string
- `os` – string
- `os_description` – string
- `os_id` – integer
- `os_major` – string
- `os_minor` – string
- `os_title` – string
- `owner` – string
- `owner_id` – integer
- `owner_type` – string
- `params` – string
- `params_name` – string
- `parent_hostgroup` – string
- `puppet_ca` – string
- `puppet_proxy_id` – integer
- `puppetmaster` – string
- `pxe_loader` – Values: PXELinux_BIOS, PXELinux_UEFI, Grub2_BIOS, Grub2_ELF, Grub2_UEFI, Grub2_UEFI_SecureBoot, Grub2_UEFI_HTTP, Grub2_UEFI_HTTPS, Grub2_UEFI_HTTPS_SecureBoot, iPXE_Embedded, iPXE_UEFI_HTTP, iPXE_Chain_BIOS, iPXE_Chain_UEFI
- `realm` – string
- `realm_id` – integer
- `registered_at` – datetime
- `registered_through` – string
- `release_version` – string
- `reported.aws_account_id`
- `reported.aws_instance_id`
- `reported.aws_region`
- `reported.azure_instance_id`
- `reported.azure_subscription_id`
- `reported.bios_release_date`
- `reported.bios_vendor`
- `reported.bios_version`
- `reported.boot_time`
- `reported.cloud_provider`
- `reported.cores`
- `reported.disks_total`
- `reported.gcp_instance_id`
- `reported.gcp_project_id`
- `reported.kernel_version`
- `reported.ram`
- `reported.sockets`
- `reported.virtual` – Values: true, false
- `repository` – string
- `repository_content_label` – string
- `rhel_lifecycle_status` – Values: full_support, maintenance_support, approaching_end_of_maintenance, extended_support, approaching_end_of_support, support_ended
- `role` – text
- `service_level` – string
- `smart_proxy` – string
- `status.applied` – integer
- `status.enabled` – Values: true, false
- `status.failed` – integer
- `status.failed_restarts` – integer
- `status.interesting` – Values: true, false
- `status.pending` – integer
- `status.restarted` – integer
- `status.skipped` – integer
- `subnet` – string
- `subnet.name` – text
- subnet6 string
- subnet6.name text
- `subscription_id` – string
- `subscription_name` – string
- `subscription_uuid` – string
- `trace_status` – Values: reboot_needed, process_restart_needed, updated
- `upgradable_debs` – string
- `upgradable_rpms` – string
- `usage` – text
- `user.firstname` – string
- `user.lastname` – string
- `user.login` – string
- `user.mail` – string
- `usergroup` – string
- `usergroup.name` – string
- `uuid` – string

## 42.16. host package

Manage packages on your hosts

**Usage**

```
# hammer host package [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.16.1. host package containerfile-install-command

Generate a Containerfile RUN command from transiently installed packages on image mode hosts

**Usage**

```
# hammer host package containerfile-install-command [OPTIONS]
```

**Options**

- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – ID of the host
- `--include-unknown-persistence BOOLEAN` Include packages with unknown persistence in addition to transient packages
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--sort-by VALUE` – Field to sort the results on
- `--sort-order VALUE` – How to order the sorted results (e.g. ASC for ascending)
- `-h`, `--help` – Print help

### 42.16.2. host package install

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_package_install`.

**Usage**

```
# hammer host package install [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_package_install`.

Unfortunately the server does not support such operation.

### 42.16.3. host package list

List packages installed on the host

**Usage**

```
# hammer host package <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – ID of the host
- `--include-latest-upgradable BOOLEAN` Also include the latest upgradable package version for each host package
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--persistence VALUE` – Return only packages of a particular persistence (transient, persistent, or nil)
- `--search VALUE` – Search string
- `--status VALUE` – Return only packages of a particular status (upgradable or up-to-date)
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Nvra | x | x |
| Persistence | x |  |

**Search and order fields**

- `arch` – string
- `epoch` – string
- `id` – integer
- `name` – string
- `nvra` – string
- `nvrea` – string
- `persistence` – Values: transient, persistent
- `release` – string
- `vendor` – string
- `version` – string

### 42.16.4. host package remove

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_package_remove`.

**Usage**

```
# hammer host package remove [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_package_remove`.

Unfortunately the server does not support such operation.

### 42.16.5. host package upgrade

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_package_update`.

**Usage**

```
# hammer host package upgrade [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_package_update`.

Unfortunately the server does not support such operation.

### 42.16.6. host package upgrade-all

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_package_update`.

**Usage**

```
# hammer host package upgrade-all [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_package_update`.

Unfortunately the server does not support such operation.

## 42.17. host package-group

Manage package-groups on your hosts. These commands are no longer available

Use the remote execution equivalent

**Usage**

```
# hammer host package-group [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.17.1. host package-group install

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_group_install`.

**Usage**

```
# hammer host package-group install [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_group_install`.

Unfortunately the server does not support such operation.

### 42.17.2. host package-group remove

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_group_remove`.

**Usage**

```
# hammer host package-group remove [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_group_remove`.

Unfortunately the server does not support such operation.

## 42.18. host policies-enc

View policies ENC for host

**Usage**

```
# hammer host policies-enc [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – The identifier of the host
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Profile id | x | x |
| Content path | x | x |
| Content download path | x | x |
| Tailoring path | x | x |
| Tailoring download path | x | x |
| Day of month | x | x |
| Hour | x | x |
| Minute | x | x |
| Month | x | x |
| Week | x | x |

## 42.19. host puppet-classes

List all Puppet classes

**Usage**

```
# hammer host puppet-classes [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id VALUE` – ID of host
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

## 42.20. host reboot

Reboot a host

**Usage**

```
# hammer host reboot [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.21. host rebuild-config

Rebuild orchestration related configurations for host

**Usage**

```
# hammer host rebuild-config [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--only LIST` – Limit rebuild steps, valid steps are DHCP, DNS, TFTP, Content_Host_Status, Refresh_Content_Host_Status
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.22. host reports

List all reports

**Usage**

```
# hammer host reports [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – Host id
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
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
| Host | x | x |  |
| Last report | x | x |  |
| Origin | x | x |  |
| Applied | x | x |  |
| Restarted | x | x |  |
| Failed | x | x |  |
| Restart failures | x | x |  |
| Skipped | x | x |  |
| Pending | x | x |  |

**Search and order fields**

- `applied` – integer
- `eventful` – Values: true, false
- `failed` – integer
- `failed_restarts` – integer
- `host` – string
- `host_id` – integer
- `host_owner_id` – integer
- `hostgroup` – string
- `hostgroup_fullname` – string
- `hostgroup_title` – string
- `id` – integer
- `last_report` – datetime
- `location` – string
- `log` – text
- `organization` – string
- `origin` – string
- `pending` – integer
- `reported` – datetime
- `resource` – text
- `restarted` – integer
- `skipped` – integer

## 42.23. host reset

Reset a host

**Usage**

```
# hammer host reset [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.24. host sc-params

List all smart class parameters

**Usage**

```
# hammer host sc-params [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id NUMBER`
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

## 42.25. host set-parameter

Create or append a parameter for a host

**Usage**

```
# hammer host set-parameter [OPTIONS]
```

**Options**

- `--hidden-value BOOLEAN` – Should the value be hidden
- `--host VALUE` – Host name
- `--host-id NUMBER`
- `--name VALUE` – Parameter name
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json` Default: "string"
- `--value VALUE` – Parameter value
- `-h`, `--help` – Print help

## 42.26. host start

Power a host on

**Usage**

```
# hammer host start [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.27. host status

Get status of host

**Usage**

```
# hammer host status [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--type ENUM` – Possible value(s): `global`, `build`, `configuration`, `compliance`, `execution`, `inventory`, `insights`, `errata`, `rhel_lifecycle`, `traces`
- `-h`, `--help` – Print help

## 42.28. host stop

Power a host off

**Usage**

```
# hammer host stop [OPTIONS]
```

**Options**

- `--force` – Force turning off a host
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 42.29. host subscription

Manage subscription information on your hosts

**Usage**

```
# hammer host subscription [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.29.1. host subscription content-override

Override product content defaults

**Usage**

```
# hammer host subscription content-override [OPTIONS]
```

**Options**

- `--content-label VALUE` – Label of the content
- `--enabled BOOLEAN` – Set true to override to enabled; Set false to override to disabled.`
- `--force` – Force the override. Required for overrides other than `enabled`
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id VALUE` – Id of the content host
- `--limit-to-env BOOLEAN` – Limit actions to content in the host`s environment.
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--override-name VALUE` – Override parameter key or name. To enable or disable a repo select `enabled`. Default value: enabled Default: "enabled"
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--remove` – Remove a content override
- `--search VALUE` – Search string
- `--sort-by VALUE` – Field to sort the results on
- `--sort-order VALUE` – How to order the sorted results (e.g. ASC for ascending)
- `--value VALUE` – Override value. Note for repo enablement you can use a boolean value
- `-h`, `--help` – Print help

### 42.29.2. host subscription enabled-repositories

Show repositories enabled on the host that are known to Katello

**Usage**

```
# hammer host subscription enabled-repositories [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id VALUE` – Id of host
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Label | x | x |  |
| Content type | x | x |  |
| Checksum | x | x |  |
| Content view id | x | x |  |
| Content view name | x | x |  |
| Content view version | x | x |  |
| Environment name | x | x |  |
| Product name | x | x |  |

### 42.29.3. host subscription product-content

List associated products

**Usage**

```
# hammer host subscription product-content [OPTIONS]
```

**Options**

- `--content-access-mode-all BOOLEAN` Get all content available, not just that provided by subscriptions
- `--content-access-mode-env BOOLEAN` Limit content to just that available in the host`s content view version
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id VALUE` – Id of the host
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Type | x | x |  |
| Url | x | x |  |
| Gpg key | x | x |  |
| Label | x | x |  |
| Default enabled? | x | x |  |
| Override | x | x |  |

### 42.29.4. host subscription register

Register a host with subscription and information

**Usage**

```
# hammer host subscription register [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content View ID
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--hypervisor-guest-uuids LIST` – UUIDs of the virtual guests from the host`s hypervisor
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Lifecycle Environment ID
- `--name VALUE` – Name of the host
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--release-version VALUE` – Release version of the content host
- `--service-level VALUE` – Service level, e.g. SELF-SUPPORT
- `--uuid VALUE` – UUID to use for registered host, random uuid is generated if not provided
- `-h`, `--help` – Print help

### 42.29.5. host subscription unregister

Unregister the host as a subscription consumer

**Usage**

```
# hammer host subscription unregister [OPTIONS]
```

**Options**

- `--host VALUE` – Host name
- `--host-id NUMBER` – Id of the host
- `-h`, `--help` – Print help

## 42.30. host traces

List traces on your hosts

**Usage**

```
# hammer host traces [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 42.30.1. host traces list

List services that need restarting on the host

**Usage**

```
# hammer host traces list [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--host VALUE` – Host name
- `--host-id NUMBER` – ID of the host
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Trace id | x | x |
| Application | x | x |
| Helper | x | x |
| Type | x | x |

### 42.30.2. host traces resolve

Resolve traces

**Usage**

```
# hammer host traces resolve [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--host VALUE` – Host name
- `--host-id NUMBER` – ID of the host
- `--trace-ids LIST` – Array of Trace IDs
- `-h`, `--help` – Print help

## 42.31. host update

Update a host

**Usage**

```
# hammer host update [OPTIONS]
```

**Options**

- `--ansible-role-ids LIST` – IDs of associated ansible roles
- `--ansible-roles LIST`
- `--architecture VALUE` – Architecture name
- `--architecture-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--ask-root-password BOOLEAN`
- `--build BOOLEAN`
- `--comment VALUE` – Additional information about this host
- `--compute-attributes KEY_VALUE_LIST` – Compute resource attributes
- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id NUMBER`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id NUMBER` – Nil means host is bare metal
- `--config-group-ids LIST` – IDs of associated config groups
- `--config-groups LIST`
- `--content-source VALUE` – Content Source name
- `--content-source-id NUMBER` – Id of the Capsule from which the host consumes content.
- `--content-view VALUE` – Name to search by
- `--content-view-environment-ids LIST` – Array of content view environment ids to be associated with the host. Ignored if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-environments LIST` – Comma-separated list of content view environment labels to be associated with the host, in the format of `lifecycle_environment_label/content_view_label`. Ignored if content_view_environment_ids is specified, or if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-id NUMBER` – Id of the single content view to be associated with the host.
- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--enabled BOOLEAN` – Include this host within Satellite reporting
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER` – ID of the host group. Note: Changing the host group will re-apply attributes inherited from the new host group, unless you explicitly override them again in the update request
- `--hostgroup-title VALUE` – Hostgroup title
- `--hypervisor-guest-uuids LIST` – List of hypervisor guest uuids
- `--id VALUE`
- `--image VALUE` – Name to search by
- `--image-id NUMBER`
- `--installed-products-attributes SCHEMA` List of products installed on the host
- `--interface KEY_VALUE_LIST` – Interface parameters Can be specified multiple times.
- `--ip VALUE` – Not required if using a subnet with DHCP Capsule
- `--kickstart-repository VALUE` – Kickstart repository name
- `--kickstart-repository-id NUMBER` – Repository Id associated with the kickstart repo used for provisioning
- `--lifecycle-environment VALUE` – Name to search by
- `--lifecycle-environment-id NUMBER` – Id of the single lifecycle environment to be associated with the host.
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mac VALUE` – Required for managed host that is bare metal, not required if it`s a virtual machine
- `--managed BOOLEAN` – True/False flag whether a host is managed or unmanaged. Note: this value also determines whether several parameters are required or not
- `--medium VALUE` – Medium name
- `--medium-id VALUE` – Required if not imaged based provisioning and host is managed and value is not inherited from host group
- `--model VALUE` – Model name
- `--model-id NUMBER`
- `--name VALUE`
- `--new-location VALUE` – Use to update associated location
- `--new-location-id NUMBER` – Use to update associated location
- `--new-location-title VALUE` – Use to update associated location
- `--new-name VALUE`
- `--new-organization VALUE` – Use to update associated organization
- `--new-organization-id NUMBER` – Use to update associated organization
- `--new-organization-title VALUE` – Use to update associated organization
- `--openscap-proxy-id NUMBER` – ID of OpenSCAP Capsule
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--overwrite BOOLEAN`
- `--owner VALUE` – Login of the owner
- `--owner-id VALUE` – ID of the owner
- `--owner-type ENUM` – Host`s owner type Possible value(s): `User`, `Usergroup`
- `--parameters KEY_VALUE_LIST` – Replaces with new host parameters
- `--partition-table VALUE` – Partition table name
- `--partition-table-id NUMBER` – Required if host is managed and custom partition has not been defined
- `--product VALUE` – Name to search by
- `--product-id NUMBER` – Product id as listed from a host`s installed products, this is not the same product id as the products api returns
- `--progress-report-id VALUE` – UUID to track orchestration tasks status, GET /api/orchestration/:UUID/tasks
- `--provision-method ENUM` – The method used to provision the host. Possible value(s): `build`, `image`, `bootdisk`
- `--puppet-ca-proxy VALUE` – Name of Puppet CA proxy
- `--puppet-ca-proxy-id NUMBER` – Puppet CA Capsule ID
- `--puppet-class-ids LIST` – List of Puppet class ids
- `--puppet-classes LIST`
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` – ID of associated Puppet environment
- `--puppet-proxy VALUE` – Name of Puppet proxy
- `--puppet-proxy-id NUMBER` – Puppet Capsule ID
- `--purpose-role VALUE` – Sets the system purpose usage
- `--purpose-usage VALUE` – Sets the system purpose usage
- `--pxe-loader ENUM` – DHCP filename option (Grub2/PXELinux by default) Possible value(s): `None`, `PXELinux BIOS`, `PXELinux UEFI`, `Grub2 BIOS`, `Grub2 ELF`, `Grub2 UEFI`, `Grub2 UEFI SecureBoot`, `Grub2 UEFI HTTP`, `Grub2 UEFI HTTPS`, `Grub2 UEFI HTTPS SecureBoot`, `iPXE Embedded`, `iPXE UEFI HTTP`, `iPXE Chain BIOS`, `iPXE Chain UEFI`
- `--realm VALUE` – Name to search by
- `--realm-id NUMBER`
- `--release-version VALUE` – Release version for this Host to use (7Server, 7.1, etc)
- `--root-password VALUE` – Required if host is managed and value is not inherited from host group or default password in settings
- `--service-level VALUE` – Service level
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER` – Required if host is managed and value is not inherited from host group
- `--typed-parameters SCHEMA` – Replaces with new host parameters (with type support)
- `--volume KEY_VALUE_LIST` – Volume parameters Can be specified multiple times.
- `-h`, `--help` – Print help

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--typed-parameters` "name=<string>,value=<string>,parameter_type=[string|boolean|integer|real|array|hash|yaml|json],hidden_value=[true|false|1|0], …​ "
- `--installed-products-attributes` "product_id=<string>,product_name=<string>,arch=<string>,version=<string>, …​ "

Available keys for `--interface:` mac ip type Possible values: interface, bmc, bond, bridge name subnet_id domain_id identifier managed true/false primary true/false, each managed hosts needs to have one primary interface. provision true/false virtual true/false

For virtual=true: tag VLAN tag, this attribute has precedence over the subnet VLAN ID. Only for virtual interfaces. attached_to Identifier of the interface to which this interface belongs, e.g. eth1.

For type=bond: mode Possible values: balance-rr, active-backup, balance-xor, broadcast, 802.3ad, balance-tlb, balance-alb attached_devices Identifiers of slave interfaces, e.g. [eth1,eth2] bond_options

For type=bmc: provider always IPMI username password

**Provider-specific options**

Bold attributes are required.

EC2:

- `--volume`:
- `--interface`:
- `--compute-attributes`:

  - `availability_zone` –
  - `flavor_id` –
  - `groups` –
  - `security_group_ids` –
  - `managed_ip` –

Libvirt:

- `--volume`:

  - `pool_name` – One of available storage pools
  - `capacity` – String value, e.g. 10G
  - `allocation` – Initial allocation, e.g. 0G
  - `format_type` – Possible values: raw, qcow2
- `--interface`:

  - `compute_type` – Possible values: bridge, network
  - `compute_bridge` – Name of interface according to type
  - `compute_model` – Possible values: virtio, rtl8139, ne2k_pci, pcnet, e1000
  - `compute_network` – Libvirt instance network, e.g. default
- `--compute-attributes`:

  - `cpus` – Number of CPUs
  - `memory` – String, amount of memory, value in bytes
  - `boot_order` – Device names to specify the boot order
  - `firmware` – automatic/bios/uefi/uefi_secure_boot (UEFI with Secure Boot enabled)
  - `start` – Boolean (expressed as 0 or 1), whether to start the machine or not

OpenStack:

- `--volume`:
- `--interface`:
- `--compute-attributes`:

  - `availability_zone` –
  - `boot_from_volume` –
  - `flavor_ref` –
  - `image_ref` –
  - `tenant_id` –
  - `security_groups` –
  - `network` –

VMware:

- `--volume`:

  - `name` –
  - `storage_pod` – Storage Pod ID from VMware
  - `datastore` – Datastore ID from VMware
  - `mode` – persistent/independent_persistent/independent_nonpersistent
  - `size_gb` – Integer number, volume size in GB
  - `thin` – true/false
  - `eager_zero` – true/false
  - `controller_key` – Associated controller key
- `--interface`:

  - `compute_type` – Type of the network adapter, for example one of: VirtualVmxnet3, VirtualE1000, See documentation center for your version of vSphere to find more details about available adapter types: <https://www.vmware.com/support/pubs/>
  - `compute_network` – Network ID or Network Name from VMware
- `--compute-attributes`:

  - `cluster` – Cluster ID from VMware
  - `corespersocket` – Number of cores per socket (applicable to hardware versions < 10 only)
  - `cpus` – CPU count
  - `memory_mb` – Integer number, amount of memory in MB
  - `path` – Path to folder
  - `resource_pool` – Resource Pool ID from VMware
  - `firmware` – automatic/bios/uefi/uefi_secure_boot (UEFI with Secure Boot enabled)
  - `guest_id` – Guest OS ID form VMware
  - `hardware_version` – Hardware version ID from VMware
  - `memoryHotAddEnabled` – Must be a 1 or 0, lets you add memory resources while the machine is on
  - `cpuHotAddEnabled` – Must be a 1 or 0, lets you add CPU resources while the machine is on
  - `add_cdrom` – Must be a 1 or 0, Add a CD-ROM drive to the virtual machine
  - `annotation` – Annotation Notes
  - `scsi_controllers` – List with SCSI controllers definitions

    - `type` – ID of the controller type from VMware
    - `key` – Key of the controller (e.g. 1000)
  - `nvme_controllers` – List with NVME controllers definitions

    - `type` – ID of the controller type from VMware
    - `key` – Key of the controller (e.g. 2000)
  - `boot_order` – Device names to specify the boot order
  - `virtual_tpm` – Must be a 1 or 0, Enable virtual TPM. Only compatible with EFI firmware.
  - `start` – Must be a 1 or 0, whether to start the machine or not

AzureRM:

- `--volume`:

  - `disk_size_gb` – Volume Size in GB (integer value)
  - `data_disk_caching` – Data Disk Caching (None, ReadOnly, ReadWrite)
- `--interface`:

  - `compute_network` – Select one of available Azure Subnets, must be an ID
  - `compute_public_ip` – Public IP (None, Static, Dynamic)
  - `compute_private_ip` – Static Private IP (expressed as true or false)
- `--compute-attributes`:

  - `resource_group` – Existing Azure Resource Group of user
  - `vm_size` – VM Size, eg. Standard_A0 etc.
  - `username` – The Admin username
  - `password` – The Admin password
  - `platform` – OS type eg. Linux
  - `ssh_key_data` – SSH key for passwordless authentication
  - `os_disk_caching` – OS disk caching
  - `premium_os_disk` – Premium OS Disk, Boolean as 0 or 1
  - `script_command` – Custom Script Command
  - `script_uris` – Comma seperated file URIs

GCE:

- `--volume`:

  - `size_gb` – Volume size in GB, integer value
- `--interface`:
- `--compute-attributes`:

  - `machine_type` –
  - `network` –
  - `associate_external_ip` –
