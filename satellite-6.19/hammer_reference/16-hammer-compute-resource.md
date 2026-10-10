---
title: "compute-resource"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "16"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-compute-resource"
---
# Chapter 16. compute-resource

Manipulate compute resources

**Usage**

```
# hammer compute-resource [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 16.1. compute-resource associate-vms

Associate VMs to Hosts

**Usage**

```
# hammer compute-resource associate-vms [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--vm-id VALUE` – Associate a specific VM
- `-h`, `--help` – Print help

## 16.2. compute-resource clusters

List available clusters for a compute resource

**Usage**

```
# hammer compute-resource clusters [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Datacenter | x | x |  |
| Hosts | x | x |  |
| Cluster path | x | x |  |

## 16.3. compute-resource create

Create a compute resource

**Usage**

```
# hammer compute-resource create [OPTIONS]
```

**Options**

- `--app-ident VALUE` – Client ID for AzureRm
- `--caching-enabled BOOLEAN` – Enable caching, for VMware only
- `--cloud VALUE` – Cloud
- `--datacenter VALUE` – For VMware Datacenter
- `--description VALUE`
- `--display-type ENUM` – For Libvirt only Possible value(s): `VNC`, `SPICE`
- `--domain VALUE` – For Red Hat OpenStack Platform (v3) only
- `--email VALUE` – Deprecated, email is automatically loaded from the JSON file. For GCE only
- `--key-path VALUE` – Certificate path, for GCE only
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--password VALUE` – Password for EC2, VMware, Red Hat OpenStack Platform. Secret key for EC2
- `--project VALUE` – Deprecated, project is automatically loaded from the JSON file. For GCE only
- `--project-domain-id VALUE` – For Red Hat OpenStack Platform (v3) only
- `--project-domain-name VALUE` – For Red Hat OpenStack Platform (v3) only
- `--provider VALUE` – Providers include Libvirt, EC2, Vmware, Openstack, AzureRm, GCE
- `--region VALUE` – For AzureRm eg. `eastus` and for EC2 only. Use `us-gov-west-1` for EC2 GovCloud region
- `--secret-key VALUE` – Client Secret for AzureRm
- `--server VALUE` – For VMware
- `--set-console-password BOOLEAN` For Libvirt and VMware only
- `--sub-id VALUE` – Subscription ID for AzureRm
- `--tenant VALUE` – For Red Hat OpenStack Platform and AzureRm only
- `--url VALUE` – URL for Libvirt and Red Hat OpenStack Platform
- `--user VALUE` – Username for EC2, VMware, Red Hat OpenStack Platform. Access Key for EC2.
- `--zone VALUE` – Zone, for GCE only
- `-h`, `--help` – Print help

## 16.4. compute-resource delete

Delete a compute resource

**Usage**

```
# hammer compute-resource <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 16.5. compute-resource flavors

List available flavors for a compute resource

**Usage**

```
# hammer compute-resource flavors [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

## 16.6. compute-resource folders

List available folders for a compute resource

**Usage**

```
# hammer compute-resource folders [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Parent | x | x |  |
| Datacenter | x | x |  |
| Path | x | x |  |
| Type | x | x |  |

## 16.7. compute-resource image

View and manage compute resource’s images

**Usage**

```
# hammer compute-resource image [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 16.7.1. compute-resource image available

Show images available for addition

**Usage**

```
# hammer compute-resource image available [OPTIONS]
```

**Options**

- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
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
| Name | x | x | x |
| Uuid | x | x |  |

### 16.7.2. compute-resource image create

Create an image

**Usage**

```
# hammer compute-resource image create [OPTIONS]
```

**Options**

- `--architecture VALUE` – Architecture name
- `--architecture-id VALUE` – ID of architecture
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE`
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – ID of operating system
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--password VALUE`
- `--user-data BOOLEAN` – Whether or not the image supports user data
- `--username VALUE`
- `--uuid VALUE` – Template ID in the compute resource
- `-h`, `--help` – Print help

### 16.7.3. compute-resource image delete

Delete an image

**Usage**

```
# hammer compute-resource image <delete|destroy> [OPTIONS]
```

**Options**

- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 16.7.4. compute-resource image info

Show an image

**Usage**

```
# hammer compute-resource image <info|show> [OPTIONS]
```

**Options**

- `--architecture VALUE` – Architecture name
- `--architecture-id VALUE` – ID of architecture
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE` – ID of compute resource
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – ID of operating system
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Operating system | x | x |  |
| Username | x | x |  |
| Uuid | x | x |  |
| User data | x | x |  |
| Architecture | x | x |  |
| Iam role | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

### 16.7.5. compute-resource image list

List all images for a compute resource

**Usage**

```
# hammer compute-resource image <list|index> [OPTIONS]
```

**Options**

- `--architecture VALUE` – Architecture name
- `--architecture-id VALUE` – ID of architecture
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE` – ID of compute resource
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – ID of operating system
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
| Operating system | x | x |  |
| Username | x | x |  |
| Uuid | x | x |  |
| User data | x | x |  |

**Search and order fields**

- `architecture` – integer
- `compute_resource` – string
- `id` – integer
- `name` – string
- `operatingsystem` – integer
- `user_data` – Values: true, false
- `username` – string

### 16.7.6. compute-resource image update

Update an image

**Usage**

```
# hammer compute-resource image update [OPTIONS]
```

**Options**

- `--architecture VALUE` – Architecture name
- `--architecture-id VALUE` – ID of architecture
- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id VALUE`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE`
- `--new-name VALUE`
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – ID of operating system
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--password VALUE`
- `--user-data BOOLEAN` – Whether or not the image supports user data
- `--username VALUE`
- `--uuid VALUE` – Template ID in the compute resource
- `-h`, `--help` – Print help

## 16.8. compute-resource images

List available images for a compute resource

**Usage**

```
# hammer compute-resource images [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Uuid | x | x |  |
| Name | x | x | x |
| Path | x | x |  |

## 16.9. compute-resource info

Show a compute resource

**Usage**

```
# hammer compute-resource <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Provider | x | x |  |
| Description | x | x |  |
| User | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 16.10. compute-resource list

List all compute resources

**Usage**

```
# hammer compute-resource <list|index> [OPTIONS]
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
| Provider | x | x |  |

**Search and order fields**

- `id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
- `type` – string

## 16.11. compute-resource networks

List available networks for a compute resource

**Usage**

```
# hammer compute-resource networks [OPTIONS]
```

**Options**

- `--cluster-id VALUE` – Cluster ID (Deprecated: Use `--cluster-name` instead)
- `--cluster-name VALUE` – Cluster name or path to search by
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Datacenter | x | x |  |
| Virtual switch | x | x |  |
| Vlan id | x | x |  |

## 16.12. compute-resource resource-pools

List resource pools for a compute resource cluster

**Usage**

```
# hammer compute-resource resource-pools [OPTIONS]
```

**Options**

- `--cluster-id VALUE` – Cluster ID (Deprecated: Use `--cluster-name` instead)
- `--cluster-name VALUE` – Cluster name or path to search by
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Cluster | x | x |  |
| Datacenter | x | x |  |

## 16.13. compute-resource security-groups

List available security groups for a compute resource

**Usage**

```
# hammer compute-resource security-groups [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

## 16.14. compute-resource storage-domains

List storage domains for a compute resource

**Usage**

```
# hammer compute-resource storage-domains [OPTIONS]
```

**Options**

- `--cluster-id VALUE` – Cluster ID (Deprecated: Use `--cluster-name` instead)
- `--cluster-name VALUE` – Cluster name or path to search by
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--storage-domain VALUE`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

## 16.15. compute-resource storage-pods

List storage pods for a compute resource

**Usage**

```
# hammer compute-resource storage-pods [OPTIONS]
```

**Options**

- `--cluster-id VALUE` – Cluster ID (Deprecated: Use `--cluster-name` instead)
- `--cluster-name VALUE` – Cluster name or path to search by
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--storage-pod VALUE`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Datacenter | x | x |  |

## 16.16. compute-resource update

Update a compute resource

**Usage**

```
# hammer compute-resource update [OPTIONS]
```

**Options**

- `--app-ident VALUE` – Client ID for AzureRm
- `--caching-enabled BOOLEAN` – Enable caching, for VMware only
- `--cloud VALUE` – Cloud
- `--datacenter VALUE` – For VMware Datacenter
- `--description VALUE`
- `--display-type ENUM` – For Libvirt only Possible value(s): `VNC`, `SPICE`
- `--domain VALUE` – For Red Hat OpenStack Platform (v3) only
- `--email VALUE` – Deprecated, email is automatically loaded from the JSON file. For GCE only
- `--id VALUE`
- `--key-path VALUE` – Certificate path, for GCE only
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – Compute resource name
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--password VALUE` – Password for EC2, VMware, Red Hat OpenStack Platform. Secret key for EC2
- `--project VALUE` – Deprecated, project is automatically loaded from the JSON file. For GCE only
- `--project-domain-id VALUE` – For Red Hat OpenStack Platform (v3) only
- `--project-domain-name VALUE` – For Red Hat OpenStack Platform (v3) only
- `--provider VALUE` – Providers include Libvirt, EC2, Vmware, Openstack, AzureRm, GCE
- `--region VALUE` – For AzureRm eg. `eastus` and for EC2 only. Use `us-gov-west-1` for EC2 GovCloud region
- `--secret-key VALUE` – Client Secret for AzureRm
- `--server VALUE` – For VMware
- `--set-console-password BOOLEAN` For Libvirt and VMware only
- `--sub-id VALUE` – Subscription ID for AzureRm
- `--tenant VALUE` – For Red Hat OpenStack Platform and AzureRm only
- `--url VALUE` – URL for Libvirt and Red Hat OpenStack Platform
- `--user VALUE` – Username for EC2, VMware, Red Hat OpenStack Platform. Access Key for EC2.
- `--zone VALUE` – Zone, for GCE only
- `-h`, `--help` – Print help

## 16.17. compute-resource virtual-machine

View and manage compute resource’s virtual machines

**Usage**

```
# hammer compute-resource virtual-machine [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 16.17.1. compute-resource virtual-machine delete

Delete a Virtual Machine

**Usage**

```
# hammer compute-resource virtual-machine <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--vm-id VALUE`
- `-h`, `--help` – Print help

### 16.17.2. compute-resource virtual-machine info

Show a virtual machine

**Usage**

```
# hammer compute-resource virtual-machine <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--vm-id VALUE`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

### 16.17.3. compute-resource virtual-machine power

Power a Virtual Machine

**Usage**

```
# hammer compute-resource virtual-machine power [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--vm-id VALUE`
- `-h`, `--help` – Print help

## 16.18. compute-resource virtual-machines

List available virtual machines for a compute resource

**Usage**

```
# hammer compute-resource virtual-machines [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Path | x | x |  |
| State | x | x |  |

## 16.19. compute-resource zones

List available zone for a compute resource

**Usage**

```
# hammer compute-resource zones [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Compute resource name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
