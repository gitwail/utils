---
title: "Planning Satellite Server installation"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_disconnected_network_environment"
guide_title: "Installing Satellite Server in a disconnected network environment"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#planning-satellite-server-installation_satellite"
---
# Chapter 1. Planning Satellite Server installation

Before installing Satellite Server, review the operating system requirements, system requirements, storage requirements, and network requirements to ensure your environment meets the specifications.

## 1.1. Operating system requirements

Ensure that your operating system and installation method meet the necessary requirements before you install Satellite.

The following operating system is supported for deploying Satellite:

- Red Hat Enterprise Linux 9 (x86_64)

You can install the operating system from a disc, local ISO image, Kickstart, or any other method that Red Hat supports.

Red Hat Satellite Server is supported on the latest version of Red Hat Enterprise Linux 9 available at the time of installation. Previous versions of Red Hat Enterprise Linux including EUS or z-stream are not supported.

Red Hat Satellite Server requires a Red Hat Enterprise Linux installation with the `@Base` package group with no other package-set modifications, and without third-party configurations or software not directly necessary for the direct operation of the server. This restriction includes hardening and other non-Red Hat security software. If you require such software in your infrastructure, install and verify a complete working Satellite Server first, then create a backup of the system before adding any non-Red Hat software.

## 1.2. System requirements

System requirements for Satellite Server include minimum CPU, RAM, storage, hostname format, SELinux configuration, and time synchronization to ensure proper installation and operation.

Satellite Server is fully supported on both physical systems and virtual machines that run on hypervisors that are supported to run Red Hat Enterprise Linux. For more information about certified hypervisors, see [Certified Guest Operating Systems in Red Hat OpenStack Platform, Red Hat Virtualization, Red Hat OpenShift Virtualization and Red Hat Enterprise Linux with KVM](https://access.redhat.com/articles/certified-hypervisors).

Follow these system requirements when installing Satellite Server:

- Install Satellite Server on a freshly provisioned system that serves no other function except to run Satellite Server. Do not use an existing system because the Satellite installer will affect the configuration of several components.
- Ensure you have administrative user (root) access to the system.
- Ensure the system meets the following requirements:

  - 4 CPU cores
  - 20 GB RAM or higher
  - 4 GB RAM of swap space or higher
  - A unique host name, which can contain lower-case letters, numbers, dots (.) and hyphens (-)
- If you use custom certificates, ensure that the Common Name (CN) of the custom certificate is a fully qualified domain name (FQDN). Satellite Server and Capsule Server do not support shortnames in the hostnames.
- Ensure SELinux is enabled, either in enforcing or permissive mode. Installation with disabled SELinux is not supported. For more information, see [Security considerations](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#security-considerations) in *Overview, concepts, and deployment considerations*.
- Ensure the system clock on the system is synchronized across the network. If the system clock is not synchronized, SSL certificate verification might fail. For example, you can use the Chrony suite for timekeeping. For more information, see [Configuring time synchronization](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/configuring-time-synchronization_configuring-basic-system-settings) in *Red Hat Enterprise Linux 9 Configuring basic system settings*
- If you are installing in an environment with air-gapped Satellite Servers, ensure that all your Satellite Servers are on the same Satellite version for ISS Export Sync to work. ISS Network Sync works across all Satellite versions that support it. For more information, see [Synchronizing Content Between Satellite Servers](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Synchronizing_Content_Between_Servers_content-management) in *Managing content*.
- Ensure the system uses the `UTF-8` encoding. If your territory is USA and your language is English, set `en_US.utf-8` as the system-wide locale settings. For more information about configuring system locale in Red Hat Enterprise Linux, see [Configuring the system locale](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_basic_system_settings/assembly_changing-basic-environment-settings_configuring-basic-system-settings#proc_configuring-the-system-locale_assembly_changing-basic-environment-settings) in *Red Hat Enterprise Linux 9 Configuring basic system settings*.
- If you use an external identity provider in your deployment, ensure the provider did not create the following user accounts on the system. These user accounts can cause conflicts with the local users that Satellite Server creates:

  - apache
  - foreman
  - foreman-proxy
  - postgres
  - pulp
  - puppet
  - redis
  - tomcat

## 1.3. Storage requirements

Your system must meet the following storage requirements before you can install Satellite Server.

Follow these storage requirements when installing Satellite Server:

- Ensure that the directories used by Satellite Server have sufficient disk space available:

  Table 1.1. Storage requirements for a Satellite Server installation

  | Directory | Installation Size | Runtime Size |
  | --- | --- | --- |
  | /var/log | 10 MB | 10 GB |
  | /var/lib/pgsql | 1 GB | 20 GB |
  | /usr | 10 GB | Not Applicable |
  | /opt/puppetlabs | 500 MB | Not Applicable |
  | /var/lib/pulp | 1 MB | 300 GB |
  | /var/lib/containers if using Red Hat Lightspeed in Satellite | 20 GB | 30 GB |

  These values are based on expected use case scenarios and can vary according to individual environments. The runtime size was measured with Red Hat Enterprise Linux 7, 8, and 9 repositories synchronized.
- If you mount the `/tmp` directory as a separate file system, use the `exec` mount option in the `/etc/fstab` file.

  If `/tmp` is already mounted with the `noexec` option, change the option to `exec` and remount the file system. This is a requirement for the `puppetserver` service to work.
- If you mount the `/var/lib/pulp` directory as an NFS share, specify the SELinux context of the `/var/lib/pulp` directory in the file system table. Add the following lines to `/etc/fstab`:

  ```
  nfs.example.com:/nfsshare  /var/lib/pulp  nfs  context="system_u:object_r:pulpcore_var_lib_t:s0"  1 2
  ```

  If the NFS share is already mounted, remount it using the above configuration and restore the SELinux context:

  ```
  # restorecon -R /var/lib/pulp
  ```
- Do not use symbolic links for `/var/lib/pulp/`.

**Additional resources**

- [Disk partitions in *Red Hat Enterprise Linux 9 Managing storage devices*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_storage_devices/disk-partitions_managing-storage-devices)

## 1.4. Best practices for optimizing storage

You can optimize your storage by following the storage best practices. These include using LVM for `/var`, high-bandwidth storage for critical directories, and appropriate file systems to improve I/O performance and scalability.

- The exact amount of storage you require for log messages depends on your installation and setup. You can manage the size of the log files by using **logrotate**.
- Consider mounting `/var` on LVM storage. This can help the system to scale because most Satellite Server data is stored in the `/var` directory.
- Use high-bandwidth, low-latency storage for the `/var/lib/pulp/` and `/var/lib/pgsql` directories. Using high latency, low-bandwidth storage causes performance degradation because Red Hat Satellite has many operations that are I/O intensive.
- Use a file system with low input-output latency. Do not use the GFS2 file system because the input-output latency is too high.

**Additional resources**

- [How to use logrotate utility to rotate log files](https://access.redhat.com/solutions/1294)
- [Logging and reporting problems in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Logging_and_Reporting_Problems_admin)

## 1.5. AWS Requirements

Installing and running Satellite Server and Capsule Servers on Amazon Web Services (AWS) has additional requirements to your environment.

Amazon Web Service requirements
:   - Use [Storage requirements](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#storage-requirements_satellite) in *Installing Satellite Server in a connected network environment* to understand and assign the correct storage to your AWS EBS volumes. See also an [AWS storage optimized instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/storage-optimized-instances.html) for further guidance.
    - Create EBS volumes for directories expected to contain larger amounts of data like `/var/lib/pulp` and ensure they are correctly mounted on start-up and before continuing the installation.
    - Optional: Store other data on a separate EBS volume.
    - If you want Satellite Server and Capsule Server to communicate using external DNS hostnames, open the required ports for communication in the AWS Security Group that is associated with the instance.

AWS permission requirements
:   - Create and access Red Hat Enterprise Linux images in AWS
    - Edit network access in AWS Security
    - Create EC2 instances and EBS volumes
    - Launch EC2 instances
    - Import and export of virtual machines in AWS
    - Usage of AWS Direct Connect

Satellite requirements
:   Ensure that your Amazon EC2 instance meets or exceeds requirements for Satellite:

    - For Satellite Server, see [Preparing your environment for Satellite Server installation](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#preparing-your-environment-for-satellite-server-installation) in *Installing Satellite Server in a connected network environment*.
    - For Capsule Servers, see [Preparing your environment for Capsule installation](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#preparing-your-environment-for-capsule-installation) in *Installing Capsule Server*.

Red Hat Cloud prerequisites
:   - Register with Red Hat Cloud Access.
    - Migrate any Red Hat subscriptions that you want to use.
    - Create an AWS instance and deploy a virtual machine running Red Hat Enterprise Linux to the instance. For more information about deploying Red Hat Enterprise Linux in AWS, see [How to Locate Red Hat Cloud Access Gold Images on AWS EC2](https://access.redhat.com/articles/2962171).
    - Ensure that your subscriptions are eligible for transfer to Red Hat Cloud. For more information, see [Red Hat Cloud Access Program Details](https://www.redhat.com/en/technologies/cloud-computing/cloud-access#program-details).

**Additional resources**

- [Amazon Elastic Compute Cloud Documentation](https://docs.aws.amazon.com/ec2/)
- [What is AWS Direct Connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
