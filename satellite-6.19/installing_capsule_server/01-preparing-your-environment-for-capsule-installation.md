---
title: "Preparing your environment for Capsule installation"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_capsule_server"
guide_title: "Installing Capsule Server"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#preparing-your-environment-for-capsule-installation"
---
# Chapter 1. Preparing your environment for Capsule installation

For a successful installation and operation of Capsule Server, ensure your environment meets the operating system requirements, system requirements, storage requirements, and network port configurations.

## 1.1. Operating system requirements

Ensure that your operating system and installation method meet the necessary requirements before you install Satellite.

The following operating system is supported for deploying Satellite:

- Red Hat Enterprise Linux 9 (x86_64)

You can install the operating system from a disc, local ISO image, Kickstart, or any other method that Red Hat supports.

Red Hat Capsule Server is supported on the latest version of Red Hat Enterprise Linux 9 available at the time of installation. Previous versions of Red Hat Enterprise Linux including EUS or z-stream are not supported.

Red Hat Capsule Server requires a Red Hat Enterprise Linux installation with the `@Base` package group with no other package-set modifications, and without third-party configurations or software not directly necessary for the direct operation of the server. This restriction includes hardening and other non-Red Hat security software. If you require such software in your infrastructure, install and verify a complete working Capsule Server first, then create a backup of the system before adding any non-Red Hat software.

Do not register Capsule Server to the Red Hat Content Delivery Network (CDN).

## 1.2. System requirements

System requirements for Capsule Server include minimum CPU, RAM, storage, hostname format, SELinux configuration, and time synchronization to ensure proper installation and operation.

Capsule Server is fully supported on both physical systems and virtual machines that run on hypervisors that are supported to run Red Hat Enterprise Linux. For more information about certified hypervisors, see [Certified Guest Operating Systems in Red Hat OpenStack Platform, Red Hat Virtualization, Red Hat OpenShift Virtualization and Red Hat Enterprise Linux with KVM](https://access.redhat.com/articles/certified-hypervisors).

Follow these system requirements when installing Capsule Server:

- Install Capsule Server on a freshly provisioned system that serves no other function except to run Capsule Server. Do not use an existing system because the Satellite installer will affect the configuration of several components.
- Ensure you have administrative user (root) access to the system.
- Ensure the system meets the following requirements:

  - 4 CPU cores
  - 12 GB or higher
  - 4 GB RAM of swap space or higher
  - A unique host name, which can contain lower-case letters, numbers, dots (.) and hyphens (-)
- If you use custom certificates, ensure that the Common Name (CN) of the custom certificate is a fully qualified domain name (FQDN). Satellite Server and Capsule Server do not support shortnames in the hostnames.
- Ensure SELinux is enabled, either in enforcing or permissive mode. Installation with disabled SELinux is not supported. For more information, see [Security considerations](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#security-considerations) in *Overview, concepts, and deployment considerations*.
- Ensure the system clock on the system is synchronized across the network. If the system clock is not synchronized, SSL certificate verification might fail. For example, you can use the Chrony suite for timekeeping. For more information, see [Configuring time synchronization](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/configuring-time-synchronization_configuring-basic-system-settings) in *Red Hat Enterprise Linux 9 Configuring basic system settings*
- Ensure the system uses the `UTF-8` encoding. If your territory is USA and your language is English, set `en_US.utf-8` as the system-wide locale settings. For more information about configuring system locale in Red Hat Enterprise Linux, see [Configuring the system locale](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_changing-basic-environment-settings_configuring-basic-system-settings#proc_configuring-the-system-locale_assembly_changing-basic-environment-settings) in *Red Hat Enterprise Linux 9 Configuring basic system settings*.
- If you use an external identity provider in your deployment, ensure the provider did not create the following user accounts on the system. These user accounts can cause conflicts with the local users that Capsule Server creates:

  - apache
  - foreman-proxy
  - postgres
  - pulp
  - puppet
  - redis

> **Warning**
>
> The version of Capsule must match the version of Satellite installed. For example, the Capsule version 6.19 cannot be registered with the Satellite version 6.18.

For more information on scaling your Capsule Servers, see [Capsule Server scalability considerations](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#capsule-server-scalability-considerations_capsule).

## 1.3. Capsule storage requirements

Ensure sufficient storage is allocated to the required directories for successful installation and operation of Capsule Server. Note that the values can vary according to individual environments.

The runtime size was measured with Red Hat Enterprise Linux 7, 8, and 9 repositories synchronized.

Table 1.1. Storage requirements for Capsule Server installation

| Directory | Installation Size | Runtime Size |
| --- | --- | --- |
| /var/lib/pulp | 1 MB | 300 GB |
| /var/lib/pgsql | 100 MB | 20 GB |
| /usr | 3 GB | Not Applicable |
| /opt/puppetlabs | 500 MB | Not Applicable |

The size of the PostgreSQL database on your Capsule Server can grow significantly with an increasing number of lifecycle environments, content views, or repositories that are synchronized from your Satellite Server. In the largest Satellite environments, the size of `/var/lib/pgsql` on Capsule Server can grow to double or triple the size of `/var/lib/pgsql` on your Satellite Server.

## 1.4. Best practices for optimizing storage

You can optimize your storage by following the storage best practices. These include using LVM for `/var`, high-bandwidth storage for critical directories, and appropriate file systems to improve I/O performance and scalability.

- The exact amount of storage you require for log messages depends on your installation and setup. You can manage the size of the log files by using **logrotate**.
- Consider mounting `/var` on LVM storage. This can help the system to scale because most Capsule Server data is stored in the `/var` directory.
- Use high-bandwidth, low-latency storage for the `/var/lib/pulp/` and `/var/lib/pgsql` directories. Using high latency, low-bandwidth storage causes performance degradation because Red Hat Satellite has many operations that are I/O intensive.
- Use a file system with low input-output latency. Do not use the GFS2 file system because the input-output latency is too high.

**Additional resources**

- [How to use logrotate utility to rotate log files](https://access.redhat.com/solutions/1294)
- [Logging and reporting problems in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Logging_and_Reporting_Problems_admin)

## 1.5. Opening required ports

Open the required network ports to enable communication between Satellite components across your infrastructure, including firewall configurations for both host-based and network-based firewalls.

> **Note**
>
> Some cloud solutions must be specifically configured to allow communications between machines because they isolate machines similarly to network-based firewalls. If you use an application-based firewall, ensure that the application-based firewall permits all applications that are listed in the tables and known to your firewall. If possible, disable the application checking and allow open port communication based on the protocol.

**Prerequisites**

- You have reviewed the [Capsule port and firewall requirements](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#capsule-port-and-firewall-requirements) in *Overview, concepts, and deployment considerations* and identified the ports required for your Satellite deployment.

**Procedure**

1. Open the ports for clients on Capsule Server:

   ```
   # firewall-cmd \
   --add-port="8000/tcp" \
   --add-port="9090/tcp"
   ```
2. Allow access to services on Capsule Server:

   ```
   # firewall-cmd \
   --add-service=dns \
   --add-service=dhcp \
   --add-service=tftp \
   --add-service=http \
   --add-service=https \
   --add-service=puppetmaster
   ```
3. Make the changes persistent:

   ```
   # firewall-cmd --runtime-to-permanent
   ```

**Verification**

- View all firewall zones and allowed services:

  ```
  # firewall-cmd --list-all
  ```

**Additional resources**

- [Networking considerations in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#networking-considerations-in-satellite)
- [Using and configuring firewalld in *Red Hat Enterprise Linux 9 Configuring firewalls and packet filters*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_firewalls_and_packet_filters/using-and-configuring-firewalld_firewall-packet-filters)
