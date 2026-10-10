---
title: "Managing host placement and associations"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#managing-host-placement-and-associations"
---
# Chapter 2. Managing host placement and associations

Hosts in Satellite define your infrastructure and are part of an organization and location to form logically structured groups. You can associate existing virtual machines to Satellite to actively manage them through Satellite.

## 2.1. Associating a virtual machine with Satellite from a hypervisor

Associate virtual machines (VMs) on a hypervisor with Satellite to manage them from a central location.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select a compute resource.
3. On the **Virtual Machines** tab, click **Associate VMs** to associate all VMs or select **Associate VM** from the **Actions** menu to associate a single VM.

## 2.2. Disassociating a VM from Satellite without removing it from a hypervisor

You can disassociate a virtual machine (VM) from Satellite if you no longer want to manage it. This does not delete the VM from its hypervisor.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the hosts that you want to disassociate.
3. From the options menu, select **Disassociate hosts**.
4. Click **Disassociate**.

## 2.3. Assigning a host to a specific organization

You can assign a host to a different organization so that the host is managed under the content, permissions, and settings of that organization.

> **Note**
>
> If your host is already registered with a different organization, you must first unregister the host before assigning it to a new organization. To unregister the host, run `subscription-manager unregister` on the host. After you assign the host to a new organization, you can re-register the host.

**Prerequisites**

- Your user account has the `assign_organizations` permission.
- You belong to the organization that you want to assign to the host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the checkbox of the host you want to change.
3. From the options menu, select **Change associations** > **Organization**. A new option window opens.
4. Select the organization that you want to assign your host to. Select **Fix on mismatch**.

   > **Note**
   >
   > A mismatch happens if there is a resource associated with a host, such as a domain or subnet, and at the same time not associated with the organization you want to assign the host to. The option **Fix on mismatch** will add such a resource to the organization, and is therefore the recommended choice. The option **Fail on mismatch** will always result in an error message. For example, reassigning a host from one organization to another will fail, even if there is no actual mismatch in settings.
5. Click **Change organization**.

**Additional resources**

- [Managing organizations in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-organizations-in-satellite)

## 2.4. Assigning a host to a specific location

You can assign a host to a different location so that the host is managed under the subnets, domains, and settings of that location.

**Prerequisites**

- Your user account has the `assign_locations` permission.
- You belong to the location that you want to assign to the host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the checkbox of the host you want to change.
3. From the options menu, select **Change associations** > **Location**. A new option window opens.
4. Select the location that you want for your host. Select the checkbox **Fix on mismatch**.

   > **Note**
   >
   > A mismatch happens if there is a resource associated with a host, such as a domain or subnet, and at the same time not associated with the location you want to assign the host to. The option **Fix on mismatch** will add such a resource to the location, and is therefore the recommended choice. The option **Fail on mismatch** will always result in an error message. For example, reassigning a host from one location to another will fail, even if there is no actual mismatch in settings.
5. Click **Change location**.

**Additional resources**

- [Managing locations in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-locations-in-satellite)

## 2.5. Changing the content view environments of a host

You can change the content view environments of a host when you need to alter which content the host can consume from Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host you want to modify.
3. On the **Content view environment** card, click the options icon and select **Edit content view environments**.
4. Select the environment.
5. Select the content view.
6. Click **Save**.
