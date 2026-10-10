---
title: "subnet"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "85"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-subnet"
---
# Chapter 85. subnet

Manipulate subnets

**Usage**

```
# hammer subnet [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 85.1. subnet create

Create a subnet

**Usage**

```
# hammer subnet create [OPTIONS]
```

**Options**

- `--bmc VALUE` – BMC Proxy to use within this subnet
- `--bmc-id NUMBER` – BMC Capsule ID to use within this subnet
- `--boot-mode ENUM` – Default boot mode for interfaces assigned to this subnet. Possible value(s): `Static`, `DHCP`
- `--description VALUE` – Subnet description
- `--dhcp VALUE` – DHCP Proxy to use within this subnet
- `--dhcp-id NUMBER` – DHCP Capsule ID to use within this subnet
- `--discovery-id NUMBER` – ID of Discovery Capsule to use within this subnet for managing connection to discovered hosts
- `--dns VALUE` – DNS Proxy to use within this subnet
- `--dns-id NUMBER` – DNS Capsule ID to use within this subnet
- `--dns-primary VALUE` – Primary DNS for this subnet
- `--dns-secondary VALUE` – Secondary DNS for this subnet
- `--domain-ids LIST` – Domains in which this subnet is part
- `--domains LIST`
- `--externalipam-group VALUE` – External IPAM group - only relevant when IPAM is set to external
- `--externalipam-id NUMBER` – External IPAM Capsule ID to use within this subnet
- `--from VALUE` – Starting IP Address for IP auto suggestion
- `--gateway VALUE` – Subnet gateway
- `--httpboot-id NUMBER` – HTTPBoot Capsule ID to use within this subnet
- `--ipam ENUM` – IP Address auto suggestion mode for this subnet. Possible value(s): `DHCP`, `Internal DB`, `Random DB`, `EUI-64`, `External IPAM`, `None`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--mask VALUE` – Netmask for this subnet
- `--mtu NUMBER` – MTU for this subnet
- `--name VALUE` – Subnet name
- `--network VALUE` – Subnet network
- `--network-type ENUM` – Type or protocol, IPv4 or IPv6, defaults to IPv4 Possible value(s): `IPv4`, `IPv6`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--prefix VALUE` – Network prefix in CIDR notation (e.g. 64) for this subnet
- `--remote-execution-proxy-ids LIST` List of Capsule IDs to be used for remote execution
- `--template-id NUMBER` – Template HTTP proxy ID to use within this subnet
- `--tftp VALUE` – TFTP Proxy to use within this subnet
- `--tftp-id NUMBER` – TFTP Capsule ID to use within this subnet
- `--to VALUE` – Ending IP Address for IP auto suggestion
- `--vlanid VALUE` – VLAN ID for this subnet
- `-h`, `--help` – Print help

## 85.2. subnet delete

Delete a subnet

**Usage**

```
# hammer subnet <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – Subnet numeric identifier
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Subnet name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 85.3. subnet delete-parameter

Delete parameter for a subnet

**Usage**

```
# hammer subnet delete-parameter [OPTIONS]
```

**Options**

- `--name VALUE` – Parameter name
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER`
- `-h`, `--help` – Print help

## 85.4. subnet info

Show a subnet

**Usage**

```
# hammer subnet <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Subnet name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--show-hidden-parameters BOOLEAN` Display hidden parameter values
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Description | x | x |  |
| Protocol | x | x |  |
| Priority | x | x |  |
| Network addr | x | x |  |
| Network prefix | x | x |  |
| Network mask | x | x |  |
| Gateway addr | x | x |  |
| Primary dns | x | x |  |
| Secondary dns | x | x |  |
| Smart proxies/dns | x | x |  |
| Smart proxies/tftp | x | x |  |
| Smart proxies/dhcp | x | x |  |
| Remote execution proxies/id | x | x |  |
| Remote execution proxies/name | x | x |  |
| Ipam | x | x |  |
| Start of ip range | x | x |  |
| End of ip range | x | x |  |
| Vlan id | x | x |  |
| Mtu | x | x |  |
| Boot mode | x | x |  |
| Domains/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Parameters/ | x | x |  |

## 85.5. subnet list

List of subnets

**Usage**

```
# hammer subnet <list|index> [OPTIONS]
```

**Options**

- `--domain VALUE` – Domain name
- `--domain-id VALUE` – ID of domain
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
| Network addr | x | x |  |
| Network prefix | x | x |  |
| Network mask | x | x |  |
| Vlan id | x | x |  |
| Boot mode | x | x |  |
| Gateway address | x | x |  |

**Search and order fields**

- `boot_mode` – string
- `dns_primary` – string
- `dns_secondary` – string
- `domain` – string
- `gateway` – string
- `id` – integer
- `ipam` – string
- `location` – string
- `location_id` – integer
- `mask` – string
- `mtu` – integer
- `name` – text
- `network` – string
- `nic_delay` – integer
- `organization` – string
- `organization_id` – integer
- `params` – string
- `type` – string
- `vlanid` – integer

## 85.6. subnet set-parameter

Create or update parameter for a subnet

**Usage**

```
# hammer subnet set-parameter [OPTIONS]
```

**Options**

- `--hidden-value BOOLEAN` – Should the value be hidden
- `--name VALUE` – Parameter name
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json` Default: "string"
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER`
- `--value VALUE` – Parameter value
- `-h`, `--help` – Print help

## 85.7. subnet update

Update a subnet

**Usage**

```
# hammer subnet update [OPTIONS]
```

**Options**

- `--bmc VALUE` – BMC Proxy to use within this subnet
- `--bmc-id NUMBER` – BMC Capsule ID to use within this subnet
- `--boot-mode ENUM` – Default boot mode for interfaces assigned to this subnet. Possible value(s): `Static`, `DHCP`
- `--description VALUE` – Subnet description
- `--dhcp VALUE` – DHCP Proxy to use within this subnet
- `--dhcp-id NUMBER` – DHCP Capsule ID to use within this subnet
- `--discovery-id NUMBER` – ID of Discovery Capsule to use within this subnet for managing connection to discovered hosts
- `--dns VALUE` – DNS Proxy to use within this subnet
- `--dns-id NUMBER` – DNS Capsule ID to use within this subnet
- `--dns-primary VALUE` – Primary DNS for this subnet
- `--dns-secondary VALUE` – Secondary DNS for this subnet
- `--domain-ids LIST` – Domains in which this subnet is part
- `--domains LIST`
- `--externalipam-group VALUE` – External IPAM group - only relevant when IPAM is set to external
- `--externalipam-id NUMBER` – External IPAM Capsule ID to use within this subnet
- `--from VALUE` – Starting IP Address for IP auto suggestion
- `--gateway VALUE` – Subnet gateway
- `--httpboot-id NUMBER` – HTTPBoot Capsule ID to use within this subnet
- `--id NUMBER` – Subnet numeric identifier
- `--ipam ENUM` – IP Address auto suggestion mode for this subnet. Possible value(s): `DHCP`, `Internal DB`, `Random DB`, `EUI-64`, `External IPAM`, `None`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--mask VALUE` – Netmask for this subnet
- `--mtu NUMBER` – MTU for this subnet
- `--name VALUE` – Subnet name
- `--network VALUE` – Subnet network
- `--network-type ENUM` – Type or protocol, IPv4 or IPv6, defaults to IPv4 Possible value(s): `IPv4`, `IPv6`
- `--new-name VALUE` – Subnet name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--prefix VALUE` – Network prefix in CIDR notation (e.g. 64) for this subnet
- `--remote-execution-proxy-ids LIST` List of Capsule IDs to be used for remote execution
- `--template-id NUMBER` – Template HTTP proxy ID to use within this subnet
- `--tftp VALUE` – TFTP Proxy to use within this subnet
- `--tftp-id NUMBER` – TFTP Capsule ID to use within this subnet
- `--to VALUE` – Ending IP Address for IP auto suggestion
- `--vlanid VALUE` – VLAN ID for this subnet
- `-h`, `--help` – Print help
