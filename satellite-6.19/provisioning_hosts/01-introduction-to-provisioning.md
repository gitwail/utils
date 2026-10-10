---
title: "Introduction to provisioning"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#introduction-to-provisioning"
---
# Chapter 1. Introduction to provisioning

Provisioning is a process that starts with a blank machine and ends with a fully configured, ready-to-use operating system. Using Red Hat Satellite, you can define and automate fine-grained provisioning for a large number of hosts.

## 1.1. Provisioning methods in Satellite

With Red Hat Satellite, you can provision hosts by using the following provisioning methods.

Network based
:   You can use this method with hosts that are capable of PXE booting or UEFI HTTP booting.

    You must configure the necessary network booting services, such as DHCP or TFTP. When you create a host entry, you select a PXE loader that can configure DHCP options for network booting if Capsule is set up to configure the DHCP service automatically.

    This method uses the Anaconda operating system installer and template-generated Kickstart script for installation automation downloaded from Satellite.

    Network based with PXE Discovery
    :   You can create host entries by discovering hosts on a network. The discovery process uses the Discovery image to boot the host and report its hardware details to Satellite. You can automate provisioning of discovered hosts by creating Discovery rules.

PXE-less Discovery with kexec
:   You can use this method with hosts that do not support network boot.

    You must configure DHCP for host discovery.

    This method uses the Discovery image ISO to boot the host and report its hardware details to Satellite. Using kernel execute (kexec), the Discovery image runs the installer downloaded from Satellite.

> **Important**
>
> Kernel execute is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Boot disk based
:   You can use this method with hosts that do not support network boot or when you do not have the option of configuring network booting services, such as DHCP.

    This method supplies the booting capability but the rest of the provisioning process still downloads the installer and template-generated files from Satellite to automate the installation.

Image based
:   You can use this method with virtual machines or cloud instances.

    This method uses a virtual image template or a cloud image from a compute resource to provision the operating system. Satellite can customize the image by running either a pre-boot or post-boot configuration script generated from a provisioning template.

## 1.2. Provisioning hardware types

With Red Hat Satellite, you can provision hosts of the following hardware types.

Bare-metal hosts
:   Satellite provisions bare-metal hosts primarily by using network boot and MAC address identification. When provisioning bare-metal hosts with Satellite, you can do the following:

    - Create host entries and specify the MAC address of the host to provision.
    - Boot blank hosts to the Satellite Discovery service, which creates a pool of hosts that are ready to be provisioned.
    - Boot and provision PXE-less hosts by using boot disks.

Virtual machines
:   Satellite connects to virtualization infrastructure services, such as VMware. You can instruct Satellite to use a particular hardware profile by defining a compute profile. When provisioning virtual machines with Satellite, you can do the following:

    - Select which hardware profile to use.
    - Provision virtual machines from virtual image templates.
    - Use the same provisioning methods that you use to provision bare-metal hosts.

Cloud instances
:   Satellite connects to private and public cloud providers to provision instances of hosts from images stored in the cloud environment. You can instruct Satellite to use a particular hardware profile by defining a compute profile.

## 1.3. Supported client platforms in provisioning

You can provision supported operating systems on hosts with supported architectures.

The hosts can use the following operating systems:

- Red Hat Enterprise Linux 10, 9, and 8
- Red Hat Enterprise Linux 7 with the [ELS Add-On](https://www.redhat.com/en/resources/els-datasheet)

The hosts can use the following architectures:

- AMD and Intel 64-bit architectures
- The 64-bit ARM architecture
- IBM Power Systems, Little Endian
- 64-bit IBM Z architectures

## 1.4. Supported cloud providers

You can connect the following cloud providers as compute resources to Satellite:

- Red Hat OpenStack Services on OpenShift
- Amazon EC2
- Google Compute Engine
- Microsoft Azure

**Additional resources**

- [Chapter 14, *Provisioning cloud instances on Red Hat OpenStack Services on OpenShift*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-cloud-instances-on-red-hat-openstack-services-on-openshift "Chapter 14. Provisioning cloud instances on Red Hat OpenStack Services on OpenShift")
- [Chapter 15, *Provisioning cloud instances on Amazon EC2*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-cloud-instances-on-amazon-ec2 "Chapter 15. Provisioning cloud instances on Amazon EC2")
- [Chapter 16, *Provisioning cloud instances on Google Compute Engine*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-cloud-instances-on-google-compute-engine "Chapter 16. Provisioning cloud instances on Google Compute Engine")
- [Chapter 17, *Provisioning cloud instances on Microsoft Azure*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-cloud-instances-on-microsoft-azure "Chapter 17. Provisioning cloud instances on Microsoft Azure")

## 1.5. Supported virtualization infrastructures

You can connect the following virtualization infrastructures as compute resources to Satellite:

- KVM (libvirt)
- VMware
- OpenShift Virtualization

**Additional resources**

- [Chapter 11, *Provisioning virtual machines on KVM*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-virtual-machines-on-kvm "Chapter 11. Provisioning virtual machines on KVM")
- [Chapter 12, *Provisioning virtual machines in VMware*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-virtual-machines-in-vmware "Chapter 12. Provisioning virtual machines in VMware")
- [Chapter 13, *Provisioning virtual machines on OpenShift Virtualization*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-virtual-machines-on-openshift-virtualization "Chapter 13. Provisioning virtual machines on OpenShift Virtualization")
