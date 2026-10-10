---
title: "Provisioning management with Red Hat Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Provisioning-Management-with-Satellite_planning"
---
# Chapter 3. Provisioning management with Red Hat Satellite

With Red Hat Satellite, you can provision hosts on various compute resources with many provisioning methods from a unified interface.

## 3.1. Provisioning methods in Satellite

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
