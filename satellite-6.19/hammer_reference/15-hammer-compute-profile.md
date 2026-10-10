---
title: "compute-profile"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "15"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-compute-profile"
---
# Chapter 15. compute-profile

Manipulate compute profiles

**Usage**

```
# hammer compute-profile [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 15.1. compute-profile create

Create a compute profile

**Usage**

```
# hammer compute-profile create [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 15.2. compute-profile delete

Delete a compute profile

**Usage**

```
# hammer compute-profile <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute profile name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 15.3. compute-profile info

Show a compute profile

**Usage**

```
# hammer compute-profile <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute profile name
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
| Created at | x | x |  |
| Updated at | x | x |  |
| Compute attributes/id | x | x |  |
| Compute attributes/name | x | x |  |
| Compute attributes/compute resource | x | x |  |
| Compute attributes/vm attributes | x | x |  |

## 15.4. compute-profile list

List of compute profiles

**Usage**

```
# hammer compute-profile <list|index> [OPTIONS]
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

**Search and order fields**

- `id` – integer
- `name` – string

## 15.5. compute-profile update

Update a compute profile

**Usage**

```
# hammer compute-profile update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE`
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 15.6. compute-profile values

Create update and delete Compute profile values

**Usage**

```
# hammer compute-profile values [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 15.6.1. compute-profile values add-interface

Add interface for Compute Profile

**Usage**

```
# hammer compute-profile values add-interface [OPTIONS]
```

**Options**

- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id VALUE`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--interface KEY_VALUE_LIST` – Interface parameters, should be comma separated list of values
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Provider-specific options**

Bold attributes are required.

EC2:

- `--interface`:

Libvirt:

- `--interface`:

  - `compute_type` – Possible values: bridge, network
  - `compute_bridge` – Name of interface according to type
  - `compute_model` – Possible values: virtio, rtl8139, ne2k_pci, pcnet, e1000
  - `compute_network` – Libvirt instance network, e.g. default

OpenStack:

- `--interface`:

VMware:

- `--interface`:

  - `compute_type` – Type of the network adapter, for example one of: VirtualVmxnet3, VirtualE1000, See documentation center for your version of vSphere to find more details about available adapter types: <https://www.vmware.com/support/pubs/>
  - `compute_network` – Network ID or Network Name from VMware

AzureRM:

- `--interface`:

  - `compute_network` – Select one of available Azure Subnets, must be an ID
  - `compute_public_ip` – Public IP (None, Static, Dynamic)
  - `compute_private_ip` – Static Private IP (expressed as true or false)

GCE:

- `--interface`:

### 15.6.2. compute-profile values add-volume

Add volume for Compute Profile

**Usage**

```
# hammer compute-profile values add-volume [OPTIONS]
```

**Options**

- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id VALUE`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--volume KEY_VALUE_LIST` – Volume parameters, should be comma separated list of values
- `-h`, `--help` – Print help

**Provider-specific options**

Bold attributes are required.

EC2:

- `--volume`:

Libvirt:

- `--volume`:

  - `pool_name` – One of available storage pools
  - `capacity` – String value, e.g. 10G
  - `allocation` – Initial allocation, e.g. 0G
  - `format_type` – Possible values: raw, qcow2

OpenStack:

- `--volume`:

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

AzureRM:

- `--volume`:

  - `disk_size_gb` – Volume Size in GB (integer value)
  - `data_disk_caching` – Data Disk Caching (None, ReadOnly, ReadWrite)

GCE:

- `--volume`:

  - `size_gb` – Volume size in GB, integer value

### 15.6.3. compute-profile values create

Create compute profile set of values

**Usage**

```
# hammer compute-profile values create [OPTIONS]
```

**Options**

- `--compute-attributes KEY_VALUE_LIST` Compute resource attributes
- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id VALUE`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--interface KEY_VALUE_LIST` – Interface parameters, should be comma separated list of values Can be specified multiple times.
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--volume KEY_VALUE_LIST` – Volume parameters, should be comma separated list of values Can be specified multiple times.
- `-h`, `--help` – Print help

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

### 15.6.4. compute-profile values remove-interface

Remove compute profile interface

**Usage**

```
# hammer compute-profile values remove-interface [OPTIONS]
```

**Options**

- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id VALUE`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--interface-id NUMBER` – Interface id
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 15.6.5. compute-profile values remove-volume

Remove compute profile volume

**Usage**

```
# hammer compute-profile values remove-volume [OPTIONS]
```

**Options**

- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id VALUE`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--volume-id NUMBER` – Volume id
- `-h`, `--help` – Print help

### 15.6.6. compute-profile values update

Update compute profile values

**Usage**

```
# hammer compute-profile values update [OPTIONS]
```

**Options**

- `--compute-attributes KEY_VALUE_LIST` Compute resource attributes, should be comma separated list of values
- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id VALUE`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--interface KEY_VALUE_LIST` – Interface parameters, should be comma separated list of values Can be specified multiple times.
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--volume KEY_VALUE_LIST` – Volume parameters, should be comma separated list of values Can be specified multiple times.
- `-h`, `--help` – Print help

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

### 15.6.7. compute-profile values update-interface

Update compute profile interface

**Usage**

```
# hammer compute-profile values update-interface [OPTIONS]
```

**Options**

- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id VALUE`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--interface KEY_VALUE_LIST` – Interface parameters, should be comma separated list of values
- `--interface-id NUMBER` – Interface id
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Provider-specific options**

Bold attributes are required.

EC2:

- `--interface`:

Libvirt:

- `--interface`:

  - `compute_type` – Possible values: bridge, network
  - `compute_bridge` – Name of interface according to type
  - `compute_model` – Possible values: virtio, rtl8139, ne2k_pci, pcnet, e1000
  - `compute_network` – Libvirt instance network, e.g. default

OpenStack:

- `--interface`:

VMware:

- `--interface`:

  - `compute_type` – Type of the network adapter, for example one of: VirtualVmxnet3, VirtualE1000, See documentation center for your version of vSphere to find more details about available adapter types: <https://www.vmware.com/support/pubs/>
  - `compute_network` – Network ID or Network Name from VMware

AzureRM:

- `--interface`:

  - `compute_network` – Select one of available Azure Subnets, must be an ID
  - `compute_public_ip` – Public IP (None, Static, Dynamic)
  - `compute_private_ip` – Static Private IP (expressed as true or false)

GCE:

- `--interface`:

### 15.6.8. compute-profile values update-volume

Update compute profile volume

**Usage**

```
# hammer compute-profile values update-volume [OPTIONS]
```

**Options**

- `--compute-profile VALUE` – Compute profile name
- `--compute-profile-id VALUE`
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--volume KEY_VALUE_LIST` – Volume parameters, should be comma separated list of values
- `--volume-id NUMBER` – Volume id
- `-h`, `--help` – Print help

**Provider-specific options**

Bold attributes are required.

EC2:

- `--volume`:

Libvirt:

- `--volume`:

  - `pool_name` – One of available storage pools
  - `capacity` – String value, e.g. 10G
  - `allocation` – Initial allocation, e.g. 0G
  - `format_type` – Possible values: raw, qcow2

OpenStack:

- `--volume`:

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

AzureRM:

- `--volume`:

  - `disk_size_gb` – Volume Size in GB (integer value)
  - `data_disk_caching` – Data Disk Caching (None, ReadOnly, ReadWrite)

GCE:

- `--volume`:

  - `size_gb` – Volume size in GB, integer value
