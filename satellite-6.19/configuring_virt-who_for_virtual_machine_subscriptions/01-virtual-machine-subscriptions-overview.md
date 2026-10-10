---
title: "Virt-who and virtual machine subscriptions"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_virt-who_for_virtual_machine_subscriptions"
guide_title: "Configuring virt-who for virtual machine subscriptions"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt-who_for_virtual_machine_subscriptions/index#virtual-machine-subscriptions-overview"
---
# Chapter 1. Virt-who and virtual machine subscriptions

Virtual machines (VMs) require host-based Red Hat Enterprise Linux subscriptions instead of physical subscriptions. Many host-based subscriptions include entitlements for unlimited VMs.

virt-who queries the virtualization platform and reports hypervisor and VM information to Satellite. You can view your subscription usage by using the Subscriptions service on the Red Hat Hybrid Cloud Console.

You can configure virt-who for the following virtualization platforms:

- Red Hat Enterprise Linux Virtualization (KVM)
- VMware vSphere
- Nutanix AHV
- Microsoft Hyper-V
- Red Hat OpenStack Services on OpenShift
- OpenShift Virtualization

> **Important**
>
> The OpenShift Virtualization hypervisor is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

## 1.1. virt-who configuration overview

You configure virt-who by creating a virt-who configuration on Satellite Server. Then, you deploy the configuration on a target host such as a hypervisor or a dedicated Red Hat Enterprise Linux server.

Preparing your environment
:   - Import a subscription manifest that includes a host-based subscription into Satellite Server.
    - Register the target host to Satellite Server.
    - Create a read-only user for virt-who on the target host.

Virt-who configuration and deployment
:   1. Create a virt-who configuration on Satellite Server.
    2. Deploy the virt-who configuration on the target host.

Additional configuration
:   - Set the system purpose attributes of the host to improve the accuracy of the subscriptions service data. For more information, see [Editing the system purpose of a host](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Editing_the_System_Purpose_of_a_Host_managing-hosts) in *Managing hosts*.

      You can set the system purpose attributes when you configure activation keys for the host. For more information, see [Managing activation keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.
    - In a connected environment, configure the Satellite inventory upload plugin to upload your inventory to Red Hat Hybrid Cloud Console. For more information, see [Getting Started with the Subscriptions Service](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_the_subscriptions_service).
    - Associate the virtual machines with Satellite. For more information, see [Associating a virtual machine with Satellite from a hypervisor](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Associating_a_Virtual_Machine_from_a_Hypervisor_managing-hosts) in *Managing hosts*.

## 1.2. Checking for subscriptions that require virt-who

Identify which subscriptions require virt-who configuration to ensure accurate virtual machine reporting and maintain subscription compliance. This helps you avoid subscription violations and optimize license usage for virtualized environments.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Subscriptions**.
2. Check the **Requires Virt-Who** column of the subscriptions list. If a tick is displayed, you must configure virt-who to use that subscription.
