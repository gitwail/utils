---
title: "Major Satellite components"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Major-Satellite-Components_planning"
---
# Chapter 5. Major Satellite components

A typical Satellite deployment consists of the following components: a Satellite Server, Capsule Servers, and hosts that receive content and configuration from Satellite Server and Capsule Servers.

## 5.1. Satellite Server overview

Satellite Server is the central component of a Satellite deployment.

A typical Satellite deployment includes one Satellite Server on which you perform the following operations:

- Content lifecycle management
- Configuration of Capsule Servers
- Configuration of hosts
- Host provisioning
- Patch management
- Subscription management

Satellite Server delegates content distribution, host provisioning, and communication to Capsule Servers. Satellite Server itself also includes a Capsule.

Satellite Server also contains a fine-grained authentication system. You can grant Satellite users permissions to access precisely the parts of the infrastructure for which they are responsible.

**Additional resources**

- [Managing users and roles in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Managing_Users_and_Roles_admin)

## 5.2. Capsule overview

With Capsule Servers, you can extend the reach and scalability of your Satellite deployment. Capsule Servers provide the following functionalities in a Red Hat Satellite deployment:

- Running localized services to discover, provision, control, and configure hosts.
- Mirroring content from Satellite Server to establish content sources in various geographical or logical locations. By registering a host to a Capsule Server, you can configure this host to receive content and configuration from the Capsule in their location instead of from the central Satellite Server.

By using content views, you can specify the exact subset of content that Capsule Server makes available to hosts.

## 5.3. Overview of hosts in Satellite

A host is any Linux client that Red Hat Satellite manages. Hosts can be physical or virtual.

You can deploy virtual hosts on any platform supported by Red Hat Satellite, such as Amazon EC2, Google Compute Engine, KVM, libvirt, Microsoft Azure, OpenStack, Rackspace Cloud Services, or VMware vSphere.

With Satellite, you can manage hosts at scale, including monitoring, provisioning, remote execution, subscription management, content management, and configuration management. You can also group hosts by using features such as host groups and host collections.

## 5.4. List of key open source components of Satellite

Satellite consists of several open source projects integrated with each other, such as the following:

Foreman
:   Foreman is a lifecycle management application for physical and virtual systems. It helps manage hosts throughout their lifecycle, from provisioning and configuration to orchestration and monitoring.

Katello
:   Katello is a plugin of Foreman that extends Foreman capabilities with additional features for content, subscription, and repository management. Katello enables Satellite to subscribe to Red Hat repositories and to download content.

Candlepin
:   Candlepin is a service for subscription management.

Pulp
:   Pulp is a service for repository and content management.

**Additional resources**

- [Satellite 6 Component Versions](https://access.redhat.com/articles/1343683)

## 5.5. Capsule features

Capsule Servers provide local host management services and can mirror content from Satellite Server.

To mirror content from Satellite Server, Capsule Servers provide the following functionalities:

Repository synchronization
:   Capsule Servers pull content for selected lifecycle environments from Satellite Server and make this content available to the hosts they manage.

Content delivery
:   Hosts configured to use Capsule Server download content from that Capsule rather than from Satellite Server.

Host action delivery
:   Capsule Server executes scheduled actions on hosts.

Red Hat Subscription Management (RHSM) proxy
:   Hosts are registered to their associated Capsule Servers rather than to the central Satellite Server or the Red Hat Customer Portal.

You can use Capsule to run the following services for infrastructure and host management:

DHCP
:   Capsule can manage a DHCP server, including integration with an existing solution, such as ISC DHCP servers, Active Directory, and Libvirt instances.

DNS
:   Capsule can manage a DNS server, including integration with an existing solution, such as ISC BIND and Active Directory.

TFTP
:   Capsule can integrate with any UNIX-based TFTP server.

Realm
:   Capsule can manage Kerberos realms or domains so that hosts can join them automatically during provisioning. Capsule can integrate with an existing infrastructure, including Identity Management and Active Directory.

Puppet server
:   Capsule can act as a configuration management server by running an OpenVox server.

Puppet Certificate Authority
:   Capsule can integrate with the Puppet certificate authority (CA) to provide certificates to hosts.

Baseboard Management Controller (BMC)
:   Capsule can provide power management for hosts by using the Intelligent Platform Management Interface (IPMI) or Redfish standards.

Provisioning template proxy
:   Capsule can serve provisioning templates to hosts.

OpenSCAP
:   Capsule can perform security compliance scans on hosts.

Remote Execution (REX)
:   Capsule can run remote job execution on hosts.

You can configure a Capsule Server for a specific limited purpose by enabling only selected features on that Capsule. Common configurations include the following:

Infrastructure Capsules: DNS + DHCP + TFTP
:   Capsules with these services provide infrastructure services for hosts and have all necessary services for provisioning new hosts.

Content Capsules: Pulp
:   Capsules with this service provide content synchronized from Satellite Server to hosts.

Configuration Capsules: Pulp + Puppet + PuppetCA
:   Capsules with these services provide content and run configuration services for hosts.

Capsules with DNS + DHCP + TFTP + Pulp + Puppet + PuppetCA
:   Capsules with these services provide a full set of Capsule features. By configuring a Capsule with all these features, you can isolate hosts assigned to that Capsule by providing a single point of connection for the hosts.
