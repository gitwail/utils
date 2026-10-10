---
title: "Using boot disks to provision hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#using-boot-disks-to-provision-hosts"
---
# Chapter 9. Using boot disks to provision hosts

In environments without PXE boot or network boot, you can provision hosts by generating a boot disk ISO. The host uses the ISO to boot installation media, connect to Capsule, and install the operating system.

## 9.1. Boot disk workflow

You can use Satellite to perform boot disk-based host provisioning as an alternative to network booting methods.

Using a boot disk to provision a host involves the following steps:

1. Create a host entry in Satellite.
2. Generate a boot disk ISO image.
3. Boot your host from the ISO image.
4. The host connects to Templates Capsule and starts installing the operating system.
5. When the installation completes, the host registers to Satellite Server by using an activation key, performs necessary configuration, and installs management tools from the **Red Hat Satellite Client 6** repository.

## 9.2. Boot disk types

You can perform boot disk-based provisioning if your your network does not provide a DHCP service.

You can generate the following types of boot disks:

Full host image
:   A boot disk ISO that contains the installer kernel and initial RAM disk image for a specific host. The boot loader on this image chainloads the installer directly from the image. This image is useful if the host fails to chainload from Satellite Server or Capsule Server correctly. The provisioning template still downloads from Satellite Server.

    This image is based on SYSLINUX and GRUB2 and works with most network cards.

    This image contains a provisioning security token, therefore the generated image has a limited lifespan.

Subnet image
:   A boot disk ISO that is not associated with a specific host. You can use this image if you have an environment with multiple subnets, where hosts do not have access to Satellite Server but can access Capsule in the particular subnet. You can use this image to boot multiple hosts on the same subnet. The boot loader on this image chainloads the installer from the TFTP Capsule of the host.

    The ISO sends the MAC address of the host to Capsule, which matches the MAC address against the host entry. The image does not store IP address details and requires access to a DHCP server on the network to bootstrap. This image is generic to all hosts with a provisioning NIC on the same subnet.

    This image is based on iPXE boot firmware. Only a limited number of network cards is supported.

**Additional resources**

- [Section 6.1, “Configuring the security token validity duration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#configuring-the-security-token-validity-duration "6.1. Configuring the security token validity duration")
- [Supported hardware drivers at ipxe.org](https://ipxe.org/appnote/hardware_drivers)

## 9.3. Generating a full host boot disk by using Satellite web UI

Generate a boot disk ISO that contains the installer kernel and initial RAM disk for a specific host.

**Prerequisites**

- An activation key must be available for your host. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server and enabled in the activation key you use. For more information, see [Adding content to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite) in *Managing content*.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
7. Verify that the fields are populated with values. Note in particular:

   - Satellite automatically assigns an IP address for the new host.
   - The **Name** from the **Host** tab becomes the **DNS name**.
   - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
8. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

   For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
9. Click the **Operating System** tab. Verify that all fields contain correct values.
10. Click **Resolve** in **Provisioning Templates** to check the new host can identify the right provisioning templates to use.

    For more information about associating provisioning templates, see [Section 5.10, “Associating templates with operating systems by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#associating-templates-with-operating-systems-by-using-web-ui "5.10. Associating templates with operating systems by using Satellite web UI").
11. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
12. Click **Submit** to save the host details. This creates a host entry and the host details page appears.
13. Download the boot disk from Satellite Server. On the host details page, open the options menu and select **Full host '*My_Host_Name*' image**.

## 9.4. Generating a full host boot disk by using Hammer CLI

Generate a boot disk ISO that contains the installer kernel and initial RAM disk for a specific host.

**Prerequisites**

- An activation key must be available for your host. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server and enabled in the activation key you use. For more information, see [Adding content to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite) in *Managing content*.

**Procedure**

1. Create a host:

   ```
   $ hammer host create \
   --build true \
   --enabled true \
   --hostgroup "My_Host_Group" \
   --location "My_Location" \
   --mac "My_MAC_Address" \
   --managed true \
   --name "My_Host_Name" \
   --organization "My_Organization"
   ```
2. Configure the network interface of your host:

   ```
   $ hammer host interface update \
   --host "My_Host_Name" \
   --managed true \
   --primary true \
   --provision true
   ```
3. Download the **Full host image** boot disk from Satellite Server:

   ```
   $ hammer bootdisk host \
   --full true \
   --host My_Host_Name
   ```

## 9.5. Generating a subnet boot disk by using Satellite web UI

Generate a boot disk ISO not associated with a specific host that chainloads the installer from TFTP Capsule for a subnet.

**Prerequisites**

- Ensure that the `ipxe-bootimgs` package is installed on your Capsule.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
2. Click the dropdown menu in the **Actions** column of the required subnet.
3. Select **Subnet generic image**.

## 9.6. Generating a subnet boot disk by using Hammer CLI

Generate a boot disk ISO not associated with a specific host that chainloads the installer from TFTP Capsule for a subnet.

**Prerequisites**

- Ensure that the `ipxe-bootimgs` package is installed on your Capsule.

**Procedure**

- Generate the **Subnet image** boot disk:

  ```
  $ hammer bootdisk subnet --subnet My_Subnet_Name
  ```
