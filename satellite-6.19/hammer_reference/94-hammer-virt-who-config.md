---
title: "virt-who-config"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "94"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-virt-who-config"
---
# Chapter 94. virt-who-config

Manage Virt Who configurations

**Usage**

```
# hammer virt-who-config [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 94.1. virt-who-config create

Create a virt-who configuration

**Usage**

```
# hammer virt-who-config create [OPTIONS]
```

**Options**

- `--ahv-internal-debug BOOLEAN` Option Enable debugging output is required to enable AHV internal debug. It provides extra AHV debug information when both options are enabled
- `--blacklist VALUE` – Hypervisor blacklist, applicable only when filtering mode is set to 2. Wildcards and regular expressions are supported, multiple records must be separated by comma.
- `--debug BOOLEAN` – Enable debugging output
- `--exclude-host-parents VALUE` Applicable only for esx provider type. Hosts which parent (usually ComputeResource) name is specified in comma-separated list in this option will NOT be reported. Wildcards and regular expressions are supported, multiple records must be separated by comma. Put the value into the double-quotes if it contains special characters like comma. All new line characters will be removed in resulting configuration file, white spaces are removed from beginning and end.
- `--filter-host-parents VALUE` – Applicable only for esx provider type. Only hosts which parent (usually ComputeResource) name is specified in comma-separated list in this option will be reported. Wildcards and regular expressions are supported, multiple records must be separated by comma. Put the value into the double-quotes if it contains special characters like comma. All new line characters will be removed in resulting configuration file, white spaces are removed from beginning and end.
- `--filtering-mode ENUM` – Hypervisor filtering mode Possible value(s): `none`, `whitelist`, `blacklist`
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – HTTP proxy that should be used for communication between the server on which virt-who is running and the hypervisors and virtualization managers.
- `--hypervisor-id ENUM` – Specifies how the hypervisor will be identified. Possible value(s): `hostname`, `uuid`, `hwuuid`
- `--hypervisor-password VALUE` – Hypervisor password, required for all hypervisor types except for libvirt/OpenShift Virtualization.
- `--hypervisor-server VALUE` – Fully qualified host name or IP address of the hypervisor
- `--hypervisor-type ENUM` – Hypervisor type Possible value(s): `esx`, `hyperv`, `libvirt`, `kubevirt`, `ahv`
- `--hypervisor-username VALUE` – Account name by which virt-who is to connect to the hypervisor.
- `--interval ENUM` – Configuration interval in minutes Possible value(s): `60`, `120`, `240`, `480`, `720`, `1440`, `2880`, `4320`
- `--kubeconfig-path VALUE` – Configuration file containing details about how to connect to the cluster and authentication details.
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Configuration name
- `--no-proxy VALUE` – Ignore Proxy. A comma-separated list of hostnames or domains or ip addresses to ignore Capsule settings for. Optionally this may be set to * to bypass proxy settings for all hostnames domains or ip addresses.
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--prism-flavor ENUM` – Select the Prism flavor you are connecting to Possible value(s): `central`, `element`
- `--satellite-url VALUE` – Satellite server FQDN
- `--whitelist VALUE` – Hypervisor whitelist, applicable only when filtering mode is set to 1. Wildcards and regular expressions are supported, multiple records must be separated by comma.
- `-h`, `--help` – Print help

## 94.2. virt-who-config delete

Delete a virt-who configuration

**Usage**

```
# hammer virt-who-config <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – Configuration numeric identifier
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 94.3. virt-who-config deploy

Download and execute script for the specified virt-who configuration

**Usage**

```
# hammer virt-who-config deploy [OPTIONS]
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

## 94.4. virt-who-config fetch

Renders a deploy script for the specified virt-who configuration

**Usage**

```
# hammer virt-who-config fetch [OPTIONS]
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
- `-o`, `--output VALUE` – File where the script will be written

## 94.5. virt-who-config info

Show a virt-who configuration

**Usage**

```
# hammer virt-who-config <info|show> [OPTIONS]
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
| General information/id | x | x |
| General information/name | x | x |
| General information/hypervisor type | x | x |
| General information/hypervisor server | x | x |
| General information/hypervisor username | x | x |
| General information/configuration file | x | x |
| General information/ahv prism flavor | x | x |
| General information/enable ahv debug | x | x |
| General information/status | x | x |
| Schedule/interval | x | x |
| Schedule/last report at | x | x |
| Connection/satellite server | x | x |
| Connection/hypervisor id | x | x |
| Connection/filtering | x | x |
| Connection/excluded hosts | x | x |
| Connection/filtered hosts | x | x |
| Connection/filter host parents | x | x |
| Connection/exclude host parents | x | x |
| Connection/debug mode | x | x |
| Connection/ignore proxy | x | x |
| Http proxy/http proxy id | x | x |
| Http proxy/http proxy name | x | x |
| Http proxy/http proxy url | x | x |
| Locations/ | x | x |
| Organizations/ | x | x |

## 94.6. virt-who-config list

List of virt-who configurations

**Usage**

```
# hammer virt-who-config <list|index> [OPTIONS]
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
| Interval | x | x |  |
| Status | x | x |  |
| Last report at | x | x |  |

## 94.7. virt-who-config update

Update a virt-who configuration

**Usage**

```
# hammer virt-who-config update [OPTIONS]
```

**Options**

- `--ahv-internal-debug BOOLEAN` Option Enable debugging output is required to enable AHV internal debug. It provides extra AHV debug information when both options are enabled
- `--blacklist VALUE` – Hypervisor blacklist, applicable only when filtering mode is set to 2. Wildcards and regular expressions are supported, multiple records must be separated by comma.
- `--debug BOOLEAN` – Enable debugging output
- `--exclude-host-parents VALUE` Applicable only for esx provider type. Hosts which parent (usually ComputeResource) name is specified in comma-separated list in this option will NOT be reported. Wildcards and regular expressions are supported, multiple records must be separated by comma. Put the value into the double-quotes if it contains special characters like comma. All new line characters will be removed in resulting configuration file, white spaces are removed from beginning and end.
- `--filter-host-parents VALUE` – Applicable only for esx provider type. Only hosts which parent (usually ComputeResource) name is specified in comma-separated list in this option will be reported. Wildcards and regular expressions are supported, multiple records must be separated by comma. Put the value into the double-quotes if it contains special characters like comma. All new line characters will be removed in resulting configuration file, white spaces are removed from beginning and end.
- `--filtering-mode ENUM` – Hypervisor filtering mode Possible value(s): `none`, `whitelist`, `blacklist`
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – HTTP proxy that should be used for communication between the server on which virt-who is running and the hypervisors and virtualization managers.
- `--hypervisor-id ENUM` – Specifies how the hypervisor will be identified. Possible value(s): `hostname`, `uuid`, `hwuuid`
- `--hypervisor-password VALUE` – Hypervisor password, required for all hypervisor types except for libvirt/OpenShift Virtualization.
- `--hypervisor-server VALUE` – Fully qualified host name or IP address of the hypervisor
- `--hypervisor-type ENUM` – Hypervisor type Possible value(s): `esx`, `hyperv`, `libvirt`, `kubevirt`, `ahv`
- `--hypervisor-username VALUE` – Account name by which virt-who is to connect to the hypervisor.
- `--id NUMBER` – Configuration numeric identifier
- `--interval ENUM` – Configuration interval in minutes Possible value(s): `60`, `120`, `240`, `480`, `720`, `1440`, `2880`, `4320`
- `--kubeconfig-path VALUE` – Configuration file containing details about how to connect to the cluster and authentication details.
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Configuration name
- `--new-name VALUE` – Configuration name
- `--no-proxy VALUE` – Ignore Proxy. A comma-separated list of hostnames or domains or ip addresses to ignore Capsule settings for. Optionally this may be set to * to bypass proxy settings for all hostnames domains or ip addresses.
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--prism-flavor ENUM` – Select the Prism flavor you are connecting to Possible value(s): `central`, `element`
- `--satellite-url VALUE` – Satellite server FQDN
- `--whitelist VALUE` – Hypervisor whitelist, applicable only when filtering mode is set to 1. Wildcards and regular expressions are supported, multiple records must be separated by comma.
- `-h`, `--help` – Print help
