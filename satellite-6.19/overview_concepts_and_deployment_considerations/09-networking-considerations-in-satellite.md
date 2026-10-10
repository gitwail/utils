---
title: "Networking considerations in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#networking-considerations-in-satellite"
---
# Chapter 9. Networking considerations in Satellite

For the components of Satellite architecture to communicate, the required network ports must be open to enable incoming and outgoing traffic between the components.

## 9.1. Capsule networking

The communication between Satellite Server and hosts registered to a Capsule Server is routed through that Capsule Server. Capsule Server also provides Satellite services to hosts.

In a topology with hosts connecting to a Capsule Server, Capsule Server provides a single endpoint for all host network communications so that in remote network segments, only firewall ports to the Capsule Server itself must be open. Hosts do not need direct access to Satellite Server.

**Figure 9.1. Satellite topology with hosts connecting to a Capsule**

[Image: Red Hat Satellite topology with a host](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/7e5677a9367e0faa4dd211607cf9689c/topology-isolated-satellite.png)

In a topology with hosts connecting directly to Satellite Server, hosts need direct network access to Satellite Server. This applies to all Capsule Servers because they are hosts of Satellite Server.

**Figure 9.2. Satellite topology with hosts connecting directly to Satellite Server**

[Image: Red Hat Satellite topology with a direct host](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/3e38f445a95fddcdffa406133dc9363d/topology-direct-satellite.png)

## 9.2. Satellite Server port and firewall requirements

The following tables indicate the destination port and the direction of incoming and outgoing traffic for Satellite Server.

Table 9.1. Satellite Server incoming traffic

| Destination Port | Protocol | Service | Source | Required For | Description |
| --- | --- | --- | --- | --- | --- |
| 53 | TCP and UDP | DNS | DNS Servers and clients | Name resolution | DNS (optional) |
| 67 | UDP | DHCP | Client | Dynamic IP | DHCP (optional) |
| 69 | UDP | TFTP | Client | TFTP Server (optional) |  |
| 443 | TCP | HTTPS | Capsule | Red Hat Satellite API | Communication from Capsule |
| 443, 80 | TCP | HTTPS, HTTP | Client | Global Registration | Registering hosts to Satellite    Port 443 is required for sending installed packages and traces, registration initiation, and uploading facts.    Port 80 notifies Satellite on the `/unattended/built` endpoint that registration has finished |
| 443 | TCP | HTTPS | Red Hat Satellite | Content Mirroring | Management |
| 443 | TCP | HTTPS | Red Hat Satellite | Capsule API | Smart Proxy functionality |
| 443, 80 | TCP | HTTPS, HTTP | Capsule | Content Retrieval | Content |
| 443, 80 | TCP | HTTPS, HTTP | Client | Content Retrieval | Content |
| 1883 | TCP | MQTT | Client | Pull based REX (optional) | Hosts for REX job notification (optional) |
| 5910 – 5930 | TCP | HTTPS | Browsers | Compute Resource’s virtual console |  |
| 8000 | TCP | HTTP | Client | Provisioning templates | Template retrieval for client installers, iPXE or UEFI HTTP Boot |
| 8000 | TCP | HTTPS | Client | PXE Boot | Installation |
| 8140 | TCP | HTTPS | Client | OpenVox agent | Client updates (optional) |
| 9090 | TCP | HTTPS | Red Hat Satellite | Capsule API | Smart Proxy functionality |
| 9090 | TCP | HTTPS | Client | OpenSCAP | Configure Client (if the OpenSCAP plugin is installed) |
| 9090 | TCP | HTTPS | Discovered Node | Discovery | Host discovery and provisioning (if the discovery plugin is installed) |
| 9090 | TCP | HTTPS | Client | Pull based REX (optional) | Hosts for REX job notification (optional) |

Table 9.2. Satellite Server outgoing traffic

| Destination Port | Protocol | Service | Destination | Required For | Description |
| --- | --- | --- | --- | --- | --- |
|  | ICMP | ping | Client | DHCP | Free IP checking (optional) |
| 7 | TCP | echo | Client | DHCP | Free IP checking (optional) |
| 22 | TCP | SSH | Target host | Remote execution | Run jobs |
| 22, 16514 | TCP | SSH SSH/TLS | Compute Resource | Satellite originated communications, for compute resources in libvirt |  |
| 53 | TCP and UDP | DNS | DNS Servers on the internet | DNS Server | Resolve DNS records (optional) |
| 53 | TCP and UDP | DNS | DNS Server | Capsule DNS | Validation of DNS conflicts (optional) |
| 53 | TCP and UDP | DNS | DNS Server | Orchestration | Validation of DNS conflicts |
| 68 | UDP | DHCP | Client | Dynamic IP | DHCP (optional) |
| 80 | TCP | HTTP | Remote repository | Content Sync | Remote repositories |
| 389, 636 | TCP | LDAP, LDAPS | External LDAP Server | LDAP | LDAP authentication, necessary only if external authentication is enabled. The port can be customized if `LDAPAuthSource` is defined |
| 443 | TCP | HTTPS | Amazon EC2, Azure, Google Compute Engine | Compute resources | Virtual machine interactions (query/create/destroy) (optional) |
| 443 | TCP | HTTPS | *.akamaiedge.net | CDN for the Red Hat Container Registry | Pulling container images to install Red Hat Lightspeed in Satellite (optional) |
| 443 | TCP | HTTPS | Capsule | Content mirroring | Initiation |
| 443 | TCP | HTTPS | Infoblox DHCP Server | DHCP management | When using Infoblox for DHCP, management of the DHCP leases (optional) |
| 623 |  |  | Client | Power management | BMC On/Off/Cycle/Status |
| 5000 | TCP | HTTPS | OpenStack Compute Resource | Compute resources | Virtual machine interactions (query/create/destroy) (optional) |
| 5900 – 5930 | TCP | SSL/TLS | Hypervisor | noVNC console | Launch noVNC console |
| 7911 | TCP | DHCP, OMAPI | DHCP Server | DHCP | The DHCP target is configured using `--foreman-proxy-dhcp-server` and defaults to localhost    ISC and `remote_isc` use a configurable port that defaults to 7911 and uses OMAPI |
| 8443 | TCP | HTTPS | Client | Discovery | Capsule sends reboot command to the discovered host (optional) |
| 9090 | TCP | HTTPS | Capsule | Capsule API | Management of Capsules |

## 9.3. Capsule port and firewall requirements

The following tables indicate the destination port and the direction of incoming and outgoing traffic for Capsule Servers.

> **Note**
>
> ICMP to Port 7 UDP and TCP must not be rejected, but can be dropped. The DHCP Capsule sends an ECHO REQUEST to the Client network to verify that an IP address is free. A response prevents IP addresses from being allocated.

Table 9.3. Capsule incoming traffic

| Destination Port | Protocol | Service | Source | Required For | Description |
| --- | --- | --- | --- | --- | --- |
| 53 | TCP and UDP | DNS | DNS Servers and clients | Name resolution | DNS (optional) |
| 67 | UDP | DHCP | Client | Dynamic IP | DHCP (optional) |
| 69 | UDP | TFTP | Client | TFTP Server (optional) |  |
| 443, 80 | TCP | HTTPS, HTTP | Client | Content Retrieval | Content |
| 443, 80 | TCP | HTTPS, HTTP | Client | Host registration | Capsule CA RPM installation |
| 443 | TCP | HTTPS | Red Hat Satellite | Content Mirroring | Management |
| 443 | TCP | HTTPS | Red Hat Satellite | Capsule API | Smart Proxy functionality |
| 443 | TCP | HTTPS | Client | Host registration | Initiation    Uploading facts    Sending installed packages and traces |
| 1883 | TCP | MQTT | Client | Pull based REX (optional) | Hosts for REX job notification (optional) |
| 8000 | TCP | HTTP | Client | Provisioning templates | Template retrieval for client installers, iPXE or UEFI HTTP Boot |
| 8000 | TCP | HTTP | Client | PXE Boot | Installation |
| 8140 | TCP | HTTPS | Client | OpenVox agent | Client updates (optional) |
| 8443 | TCP | HTTPS | Client | Host registration | Deprecated and only needed for Client hosts deployed before upgrades |
| 9090 | TCP | HTTPS | Red Hat Satellite | Capsule API | Capsule functionality |
| 9090 | TCP | HTTPS | Client | Register Endpoint | Client registration with Capsule Servers |
| 9090 | TCP | HTTPS | Client | OpenSCAP | Configure Client (if the OpenSCAP plugin is installed) |
| 9090 | TCP | HTTPS | Discovered Node | Discovery | Host discovery and provisioning (if the discovery plugin is installed) |
| 9090 | TCP | HTTPS | Client | Pull based REX (optional) | Hosts for REX job notification (optional) |

Table 9.4. Capsule outgoing traffic

| Destination Port | Protocol | Service | Destination | Required For | Description |
| --- | --- | --- | --- | --- | --- |
|  | ICMP | ping | Client | DHCP | Free IP checking (optional) |
| 7 | TCP | echo | Client | DHCP | Free IP checking (optional) |
| 22 | TCP | SSH | Target host | Remote execution | Run jobs |
| 53 | TCP and UDP | DNS | DNS Servers on the internet | DNS Server | Resolve DNS records (optional) |
| 53 | TCP and UDP | DNS | DNS Server | Capsule DNS | Validation of DNS conflicts (optional) |
| 68 | UDP | DHCP | Client | Dynamic IP | DHCP (optional) |
| 443 | TCP | HTTPS | Satellite | Capsule | Capsule    Configuration management    Template retrieval    OpenSCAP    Remote Execution result upload |
| 443 | TCP | HTTPS | Red Hat Portal | SOS report | Assisting support cases (optional) |
| 443 | TCP | HTTPS | Satellite | Content | Sync |
| 443 | TCP | HTTPS | Satellite | Client communication | Forward requests from Client to Satellite |
| 443 | TCP | HTTPS | Infoblox DHCP Server | DHCP management | When using Infoblox for DHCP, management of the DHCP leases (optional) |
| 623 |  |  | Client | Power management | BMC On/Off/Cycle/Status |
| 7911 | TCP | DHCP, OMAPI | DHCP Server | DHCP | The DHCP target is configured using `--foreman-proxy-dhcp-server` and defaults to localhost    ISC and `remote_isc` use a configurable port that defaults to 7911 and uses OMAPI |
| 8443 | TCP | HTTPS | Client | Discovery | Capsule sends reboot command to the discovered host (optional) |
