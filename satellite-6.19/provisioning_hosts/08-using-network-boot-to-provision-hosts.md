---
title: "Using network boot to provision hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#using-network-boot-to-provision-hosts"
---
# Chapter 8. Using network boot to provision hosts

You can provision hosts by booting over a network, where Satellite Server or Capsule Server provides the operating system installation content. After installing the system on the host, the host registers to Satellite for initial configuration.

BIOS and UEFI interfaces
:   Both BIOS and UEFI interfaces work as interpreters between the operating system and firmware of a computer, initializing hardware components and starting the operating system at boot time. With Satellite, you can perform both BIOS and UEFI based PXE provisioning. For UEFI interfaces with an HTTP boot client, you can also perform UEFI HTTP provisioning.

UEFI Secure Boot
:   Red Hat Satellite supports host provisioning with UEFI Secure Boot. By default, you can provision the same RHEL version as your Satellite Server on Secure Boot enabled hosts. To provision other versions of Red Hat Enterprise Linux, you have to provide signed shim and GRUB2 binaries of those RHEL versions.

Bonded network interfaces
:   You can configure a bonded interface that Satellite will use during the installation process, for example, to download installation content. After provisioning completes, the provisioned system can also use the bonded interface.

    > **Important**
    >
    > Satellite cannot PXE boot a bonded interface that requires configuration on a network switch as well as on your host.
    >
    > After your host loads the kernel of an installer or the kernel of an operating system, bonding works as expected. Therefore, you can use a boot disk to work around PXE boot limitations when your bonded interface requires configuration on both a switch and your host.

## 8.1. Network boot provisioning workflow

The Satellite provisioning process follows a basic PXE workflow. It might be useful to understand how Satellite coordinates network services and content delivery to install the system for troubleshooting, locating provisioning failures, and ensuring a successful host provisioning.

The provisioning process follows a basic PXE workflow:

1. You create a host and select a domain and subnet. Satellite requests an available IP address from the DHCP Capsule Server that is associated with the subnet or from the PostgreSQL database in Satellite. Satellite loads this IP address into the **IP address** field in the Create Host window. When you complete all the options for the new host, submit the new host request.
2. Depending on the configuration specifications of the host and its domain and subnet, Satellite creates the following settings:

   - A DHCP record on Capsule Server that is associated with the subnet.
   - A forward DNS record on Capsule Server that is associated with the domain.
   - A reverse DNS record on the DNS Capsule Server that is associated with the subnet.
   - PXELinux, Grub2, and iPXE configuration files for the host in the TFTP Capsule Server that is associated with the subnet.
   - A Puppet certificate on the associated OpenVox server.
   - A realm on the associated identity server.
3. The host is configured to boot from the network as the first device and HDD as the second device.
4. The new host requests a DHCP reservation from the DHCP server.
5. The DHCP server responds to the reservation request and returns TFTP `next-server` and `filename` options.
6. The host requests the boot loader and menu from the TFTP server according to the PXELoader setting.
7. A boot loader is returned over TFTP.
8. The boot loader fetches configuration for the host through its provisioning interface MAC address.
9. The boot loader fetches the operating system installer kernel, init RAM disk, and boot parameters.
10. The installer requests the provisioning template from Satellite.
11. Satellite renders the provision template and returns the result to the host.
12. The installer performs installation of the operating system.

    - The installer registers the host to Satellite by using Subscription Manager.
    - The installer notifies Satellite of a successful build in the `postinstall` script.
13. The PXE configuration files revert to a local boot template.
14. The host reboots.
15. The new host requests a DHCP reservation from the DHCP server.
16. The DHCP server responds to the reservation request and returns TFTP `next-server` and `filename` options.
17. The host requests the boot loader and menu from the TFTP server according to the PXELoader setting.
18. A boot loader is returned over TFTP.
19. The boot loader fetches the configuration for the host through its provision interface MAC address.
20. The boot loader initiates boot from the local drive.
21. If you configured the host to use Puppet classes, the host uses the modules to configure itself.

The fully provisioned host performs the following workflow:

1. The host is configured to boot from the network as the first device and HDD as the second device.
2. The new host requests a DHCP reservation from the DHCP server.
3. The DHCP server responds to the reservation request and returns TFTP `next-server` and `filename` options.
4. The host requests the boot loader and menu from the TFTP server according to the PXELoader setting.
5. A boot loader is returned over TFTP.
6. The boot loader fetches the configuration settings for the host through its provisioning interface MAC address.
7. For BIOS hosts:

   - The boot loader returns non-bootable device so BIOS skips to the next device (boot from HDD).
8. For EFI hosts:

   - The boot loader finds Grub2 on a ESP partition and chainboots it.
9. If the host is unknown to Satellite, a default boot loader configuration is provided. When Discovery service is enabled, it boots into discovery, otherwise it boots from HDD.

This workflow differs depending on custom options. For example:

Discovery
:   If you use the discovery service, Satellite automatically detects the MAC address of the new host and restarts the host after you submit a request. Note that TCP port 8443 must be reachable by the Capsule to which the host is attached for Satellite to restart the host.

PXE-less Provisioning
:   After you submit a new host request, you must boot the specific host with the boot disk that you download from Satellite and transfer by using an external storage device.

Compute Resources
:   Satellite creates the virtual machine and retrieves the MAC address and stores the MAC address in Satellite. If you use image-based provisioning, the host does not follow the standard PXE boot and operating system installation. The compute resource creates a copy of the image for the host to use. Depending on image settings in Satellite, seed data can be passed in for initial configuration, for example by using `cloud-init`. Satellite can connect to the host by using SSH and execute a template to finish the customization.

## 8.2. Prerequisites for network-boot provisioning

Before you can perform network-based host provisioning, ensure that your environment meets the following requirements.

The requirements for network-boot provisioning include:

- Provisioning infrastructure services (DNS, DHCP, TFTP) are integrated with Satellite and configured.
- A bare-metal machine or a blank virtual machine. The provisioned machine must appear on the same network as your provisioning infrastructure services.

  You can integrate a compute resource with Satellite and let the compute resource create virtual machines through this integration. You can also provision virtual machines from unintegrated infrastructure as you would bare-metal machines.
- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.

**Additional resources**

- [Integrating provisioning infrastructure services](https://docs.theforeman.org/3.18/Integrating_Provisioning_Infrastructure_Services/index-satellite.html#)
- [Chapter 2, *Preparing networking for host management*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management "Chapter 2. Preparing networking for host management")
- [Section 5.10, “Associating templates with operating systems by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#associating-templates-with-operating-systems-by-using-web-ui "5.10. Associating templates with operating systems by using Satellite web UI")
- [Chapter 10, *Discovering hosts on a network*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#discovering-hosts-on-a-network "Chapter 10. Discovering hosts on a network")
- [Section 6.1, “Configuring the security token validity duration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#configuring-the-security-token-validity-duration "6.1. Configuring the security token validity duration")

## 8.3. Required boot order for network boot

This requirement applies to physical and virtual machines that you want to provision in Red Hat Satellite.

Machines with BIOS interface
:   The first booting device: network

    The second booting device: hard drive

    When Satellite manages TFTP boot configuration files, hosts can be provisioned by rebooting.

Machines with UEFI interface
:   The first booting device: network

    Depending on the UEFI firmware type and configuration, the operating system installer configures the operating system boot loader as the first entry.

    You can reboot back into the installer by using the `efibootmgr` utility to switch back to booting from network.

## 8.4. Configuring Capsule to provision Red Hat Enterprise Linux by using UEFI

When provisioning, always use the boot loader version that is provided by the operating system that is being provisioned, not the one which Red Hat Satellite was deployed on.

This is especially important when using Secure Boot, which follows a chain of trust from the start of the host to the loading of Linux kernel modules. The first shim that is loaded determines which distribution can be booted or loaded by using a `kexec` system call until the next reboot.

You can provision the same RHEL version as your Satellite Server on hosts out of the box and you can skip this procedure. To provision other RHEL versions, you have to provide signed shim and GRUB2 binaries for those RHEL versions.

> **Important**
>
> You have to perform the following configuration steps on each TFTP Capsule for a subnet to provision hosts using UEFI on that subnet.

Red Hat Enterprise Linux supports Secure Boot on x86_64 architecture only.

**Prerequisites**

- Ensure that the `cpio` package is installed on your Capsule.

**Procedure**

1. Set the path for the shim and GRUB2 binaries for the operating system of your host:

   ```
   # BOOTLOADER_PATH="/var/lib/tftpboot/bootloader-universe/pxegrub2/redhat/default/x86_64"
   ```

   If you require specific versions of the shim and GRUB2 binaries for the version of the operating system of your host, replace `default` with the **Major** and **Minor** version of the operating system separated by a dot. If no **Minor** version is set, replace `default` with the **Major** version.

   Red Hat recommends to not use version-specific shim and GRUB2 binaries unless it is really necessary.
2. Create the directory to store the shim and GRUB2 binaries for the operating system of your host:

   ```
   # install -o foreman-proxy -g foreman-proxy -d $BOOTLOADER_PATH
   ```
3. Download the shim and GRUB2 packages for the operating system of your host. You can download the `grub2-efi-x64` and `shim-x64` packages from [Package browser](https://access.redhat.com/downloads/content/package-browser) on the Red Hat Customer Portal.
4. Extract the shim and GRUB2 binaries:

   ```
   # rpm2cpio /tmp/grub2-efi-x64.rpm | cpio -idv --directory /tmp
   # rpm2cpio /tmp/shim-x64.rpm | cpio -idv --directory /tmp
   ```
5. Make the shim and GRUB2 binaries available for host provisioning:

   ```
   # cp /tmp/boot/efi/EFI/redhat/grubx64.efi $BOOTLOADER_PATH/grubx64.efi
   # cp /tmp/boot/efi/EFI/redhat/shimx64.efi $BOOTLOADER_PATH/shimx64.efi
   # ln -sr $BOOTLOADER_PATH/grubx64.efi $BOOTLOADER_PATH/boot.efi
   # ln -sr $BOOTLOADER_PATH/shimx64.efi $BOOTLOADER_PATH/boot-sb.efi
   # chmod 644 $BOOTLOADER_PATH/grubx64.efi $BOOTLOADER_PATH/shimx64.efi
   ```

**Verification**

- Verify the contents of your boot loader directory:

  ```
  # tree /var/lib/tftpboot/bootloader-universe
  /var/lib/tftpboot/bootloader-universe
  └── pxegrub2
      └── redhat
          └── default
              └── x86_64
                  ├── boot.efi -> grubx64.efi
                  ├── boot-sb.efi -> shimx64.efi
                  ├── grubx64.efi
                  └── shimx64.efi
  ```

**Next steps**

- You can now provision Red Hat Enterprise Linux hosts by using the **Grub2 UEFI** and **Grub2 UEFI HTTPS** PXE loaders.
- You can now provision Secure Boot enabled Red Hat Enterprise Linux hosts by using the **Grub2 UEFI SecureBoot** PXE loader.

## 8.5. Creating hosts with PXE boot provisioning by using Satellite web UI

PXE boot provisioning is a method of unattended host provisioning that requires minimal interaction during the process.

You enter the host details on Satellite Server and boot your host. Satellite Server automatically manages the PXE configuration, organizes networking services, and provides the operating system and configuration for the host.

Create a host entry to add the host details. When you save the host entry, Satellite creates the relevant provisioning settings. This also includes creating the necessary directories and files for PXE booting. When you boot the host, the host requests a DHCP lease. The DHCP service responds with a lease which includes the location of the installation content. The host uses the installation content to install the operating system.

During the installation, the host registers to Satellite Server by using the activation key, installs the necessary host management tools from the Red Hat Satellite Client 6 repository, and performs initial configuration.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
7. Verify that the fields are populated with values. Note in particular:

   - Satellite automatically assigns an IP address for the new host.
   - In the **MAC address** field, enter a MAC address of the provisioning interface of the host. This ensures the identification of the host during the PXE boot process.
   - The **Name** from the **Host** tab becomes the **DNS name**.
   - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
8. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

   For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
9. Click the **Operating System** tab, and verify that all fields contain values. Confirm each aspect of the operating system.
10. Optional: Click **Resolve** in **Provisioning template** to check the new host can identify the right provisioning templates to use.

    For more information about provisioning templates, see [Section 5.1, “Provisioning templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-templates "5.1. Provisioning templates").
11. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
12. Click **Submit** to save the host details.

## 8.6. Creating hosts with PXE boot provisioning by using Hammer CLI

PXE boot provisioning is a method of unattended host provisioning that requires minimal interaction during the process.

You enter the host details on Satellite Server and boot your host. Satellite Server automatically manages the PXE configuration, organizes networking services, and provides the operating system and configuration for the host.

Create a host entry to add the host details. When you save the host entry, Satellite creates the relevant provisioning settings. This also includes creating the necessary directories and files for PXE booting. When you boot the host, the host requests a DHCP lease. The DHCP service responds with a lease which includes the location of the installation content. The host uses the installation content to install the operating system.

During the installation, the host registers to Satellite Server by using the activation key, installs the necessary host management tools from the Red Hat Satellite Client 6 repository, and performs initial configuration.

**Procedure**

1. Create the host:

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
2. Configure the network interface:

   ```
   $ hammer host interface update \
   --host "_My_Host_Name_" \
   --managed true \
   --primary true \
   --provision true
   ```

## 8.7. Configuring Capsule for UEFI HTTP booting

You can provision hosts from Satellite by using the UEFI HTTP Boot if the hosts have this capability. Configure your Capsule for UEFI HTTP booting.

**Prerequisites**

- Ensure that your environment meets the requirements for HTTP booting. For more information, see [HTTP booting in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#http-booting-in-satellite) in *Overview, concepts, and deployment considerations*.

**Procedure**

1. Ensure that Capsule is associated with the provisioning subnet. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
2. Click **Edit Subnet** > **Capsules**.
3. Select the Capsule for both **TFTP** and **HTTPBoot** options.
4. Click **OK** to save.

**Next steps**

- [Section 8.8, “Creating hosts with UEFI HTTP boot provisioning by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-hosts-with-uefi-http-boot-provisioning-by-using-web-ui "8.8. Creating hosts with UEFI HTTP boot provisioning by using Satellite web UI")

## 8.8. Creating hosts with UEFI HTTP boot provisioning by using Satellite web UI

You can provision hosts with UEFI HTTP boot to transfer files over HTTP. This improves reliability for large files, such as Live images, and reduces boot time compared to TFTP.

You enter the host details on Satellite Server and boot your host. Satellite Server automatically manages the HTTP boot configuration, organizes networking services, and provides the operating system and configuration for the host.

Create a host entry to add the host details. When you save the host entry, Satellite creates the relevant provisioning settings. This also includes creating the necessary directories and files for PXE booting. When you boot the host, the host requests a DHCP lease. The DHCP service responds with a lease which includes the location of the installation content. The host uses the installation content to install the operating system.

During the installation, the host registers to Satellite Server by using the activation key, installs the necessary host management tools from the Red Hat Satellite Client 6 repository, and performs initial configuration.

**Prerequisites**

- Your Capsule has been configured for UEFI HTTP booting. For more information, see [Section 8.7, “Configuring Capsule for UEFI HTTP booting”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#configuring-capsule-for-uefi-http-booting "8.7. Configuring Capsule for UEFI HTTP booting").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
7. Verify that the fields are populated with values. Note in particular:

   - Satellite automatically assigns an IP address for the new host.
   - In the **MAC address** field, enter a MAC address of the provisioning interface of the host. This ensures the identification of the host during the PXE boot process.
   - The **Name** from the **Host** tab becomes the **DNS name**.
   - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
8. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

   For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
9. Click the **Operating System** tab, and verify that all fields contain values. Confirm each aspect of the operating system.
10. From the **PXE Loader** list, select **Grub2 UEFI HTTP**.
11. Optional: Click **Resolve** in **Provisioning template** to check the new host can identify the right provisioning templates to use.

    For more information about provisioning templates, see [Section 5.1, “Provisioning templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-templates "5.1. Provisioning templates").
12. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
13. Click **Submit** to save the host details.

## 8.9. Creating hosts with UEFI HTTP boot provisioning by using Hammer CLI

You can provision hosts with UEFI HTTP boot to transfer files over HTTP. This improves reliability for large files, such as Live images, and reduces boot time compared to TFTP.

You enter the host details on Satellite Server and boot your host. Satellite Server automatically manages the HTTP boot configuration, organizes networking services, and provides the operating system and configuration for the host.

Create a host entry to add the host details. When you save the host entry, Satellite creates the relevant provisioning settings. This also includes creating the necessary directories and files for PXE booting. When you boot the host, the host requests a DHCP lease. The DHCP service responds with a lease which includes the location of the installation content. The host uses the installation content to install the operating system.

During the installation, the host registers to Satellite Server by using the activation key, installs the necessary host management tools from the Red Hat Satellite Client 6 repository, and performs initial configuration.

**Prerequisites**

- Your Capsule has been configured for UEFI HTTP booting. For more information, see [Section 8.7, “Configuring Capsule for UEFI HTTP booting”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#configuring-capsule-for-uefi-http-booting "8.7. Configuring Capsule for UEFI HTTP booting").

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
   --organization "My_Organization" \
   --pxe-loader "Grub2 UEFI HTTP"
   ```
2. Configure the network interface:

   ```
   $ hammer host interface update \
   --host "My_Host_Name" \
   --managed true \
   --primary true \
   --provision true
   ```

## 8.10. Using iPXE to reduce provisioning times

iPXE is an open-source network-boot firmware. It provides a full PXE implementation enhanced with additional features, such as booting from an HTTP server.

> **Important**
>
> The iPXE network boot is **deprecated** and will be removed in a future release.

You can use iPXE if the following restrictions prevent you from using PXE:

- A network with unmanaged DHCP servers.
- A PXE service that is unreachable because of, for example, a firewall restriction.
- A TFTP UDP-based protocol that is unreliable because of, for example, a low-bandwidth network.

Booting a virtual machine has the following workflow:

1. Virtual machine starts.
2. iPXE retrieves the network credentials, including an HTTP URL, by using DHCP.
3. iPXE loads the iPXE bootstrap template from Capsule.
4. iPXE loads the iPXE template with MAC as a URL parameter from Capsule.
5. iPXE loads the kernel and initial RAM disk of the installer.

Chainbooting iPXE has the following workflow:

1. Host powers on.
2. PXE driver retrieves the network credentials by using DHCP.
3. PXE driver retrieves the PXELinux firmware `pxelinux.0` by using TFTP.
4. PXELinux searches for the configuration file on the TFTP server.
5. PXELinux chainloads iPXE `ipxe.lkrn` or `undionly-ipxe.0`.
6. iPXE retrieves the network credentials, including an HTTP URL, by using DHCP again.
7. iPXE chainloads the iPXE template from your Templates Capsule.
8. iPXE loads the kernel and initial RAM disk of the installer.

**Additional resources**

- [ipxe.org](https://ipxe.org)

### 8.10.1. Prerequisites for using iPXE

Before you use iPXE to boot virtual machines, verify that your environment meets the following requirements.

You can use iPXE to boot virtual machines in the following cases:

- Your virtual machines run on a hypervisor that uses iPXE as primary firmware.
- Your virtual machines are in BIOS mode. In this case, you can configure PXELinux to chainboot iPXE and boot by using the HTTP protocol.

For booting virtual machines in UEFI mode by using HTTP, you can follow [Section 8.8, “Creating hosts with UEFI HTTP boot provisioning by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-hosts-with-uefi-http-boot-provisioning-by-using-web-ui "8.8. Creating hosts with UEFI HTTP boot provisioning by using Satellite web UI") instead.

Supportability
:   Red Hat does not officially support iPXE in Red Hat Satellite. For more information, see [Supported architectures and kickstart scenarios in Satellite 6](https://access.redhat.com/solutions/2674001) in the *Red Hat Knowledgebase*.

Host requirements
:   - The MAC address of the provisioning interface matches the host configuration.
    - The provisioning interface of the host has a valid DHCP reservation.
    - The NIC is capable of PXE booting. For more information, see [supported hardware on ipxe.org](https://ipxe.org/appnote/hardware_drivers) for a list of hardware drivers expected to work with an iPXE-based boot disk.
    - The NIC is compatible with iPXE.

### 8.10.2. Configuring iPXE environment

Configure an iPXE environment on all Capsules that you want to use for iPXE provisioning.

> **Important**
>
> In RHEL, security-related features of iPXE are not supported and the iPXE binary is built without security features. For this reason, you can only use HTTP but not HTTPS. For more information, see [Red Hat Enterprise Linux HTTPS support in iPXE](https://access.redhat.com/solutions/3483601).

**Prerequisites**

- If you want to use Capsule Servers instead of your Satellite Server, ensure that you have configured your Capsule Servers accordingly.

  > **Important**
  >
  > It is essential to add your Capsule Server to the list of trusted proxies on Satellite Server!

  For more information, see [Configuring Capsule Server for host registration and provisioning](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-capsule-server-for-host-registration-and-provisioning) in *Installing Capsule Server*.

**Procedure**

1. Enable the **TFTP** and **HTTPboot** services on your Capsule:

   ```
   # satellite-installer \
   --foreman-proxy-httpboot true \
   --foreman-proxy-tftp true
   ```
2. Install the `ipxe-bootimgs` package on your Capsule:

   ```
   # satellite-maintain packages install ipxe-bootimgs
   ```
3. Copy iPXE firmware to the TFTP directory.

   - Copy the iPXE firmware with the Linux kernel header:

     ```
     # cp /usr/share/ipxe/ipxe.lkrn /var/lib/tftpboot/
     ```
   - Copy the UNDI iPXE firmware:

     ```
     # cp /usr/share/ipxe/undionly.kpxe /var/lib/tftpboot/undionly-ipxe.0
     ```
4. Correct the SELinux file contexts:

   ```
   # restorecon -RvF /var/lib/tftpboot/
   ```
5. Set the HTTP URL.

   - If you want to use Satellite Server for booting, reconfigure your Satellite Server:

     ```
     # satellite-installer \
     --foreman-proxy-dhcp-ipxefilename "http://satellite.example.com/unattended/iPXE?bootstrap=1"
     ```
   - If you want to use Capsule Server for booting, reconfigure your Capsule Server:

     ```
     # satellite-installer --foreman-proxy-dhcp-ipxe-bootstrap true
     ```

### 8.10.3. Booting virtual machines

Some virtualization hypervisors use iPXE as primary firmware for PXE booting. If you use such a hypervisor, you can boot virtual machines without TFTP and PXELinux.

**Prerequisites**

- Your hypervisor must support iPXE. The following virtualization hypervisors support iPXE:

  - libvirt
- You have configured your iPXE environment. For more information, see [Section 8.10.2, “Configuring iPXE environment”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Configuring_iPXE_Environment_using-network-boot "8.10.2. Configuring iPXE environment").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Search for the `Kickstart default iPXE` template.
3. Click the name of the template.
4. Click the **Association** tab and select the operating systems that your host uses.
5. Click the **Locations** tab and add the location where the host resides.
6. Click the **Organizations** tab and add the organization that the host belongs to.
7. Click **Submit** to save the changes.
8. In the Satellite web UI, navigate to **Hosts** > **Operating systems** and select the operating system of your host.
9. Click the **Templates** tab.
10. From the **iPXE template** list, select the `Kickstart default iPXE` template.
11. Click **Submit** to save the changes.
12. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
13. In the **Hosts** page, select the host that you want to use.
14. Select the **Operating System** tab.
15. Set **PXE Loader** to `iPXE Embedded`.
16. Select the **Templates** tab.
17. In **Provisioning Templates**, click **Resolve** and verify that the **iPXE template** resolves to the required template.
18. Click **Submit** to save host settings.

**Additional resources**

- [Section 5.6, “Running custom code during host provisioning by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#running-custom-code-during-host-provisioning-by-using-web-ui "5.6. Running custom code during host provisioning by using Satellite web UI")

### 8.10.4. Chainbooting iPXE from PXELinux

You can set up iPXE to use a built-in driver for network communication (`ipxe.lkrn`) or Universal Network Device Interface (UNDI) (`undionly-ipxe.0`). You can choose to load either file depending on the networking hardware capabilities and iPXE driver availability.

UNDI is a minimalistic UDP/IP stack that implements TFTP client. However, UNDI cannot support other protocols like HTTP. To use HTTP with iPXE, use the iPXE build with built-in drivers (`ipxe.lkrn`).

**Prerequisites**

- You have configured your iPXE environment. For more information, see [Section 8.10.2, “Configuring iPXE environment”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Configuring_iPXE_Environment_using-network-boot "8.10.2. Configuring iPXE environment").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Search for the required PXELinux template:

   - `PXELinux chain iPXE` to use `ipxe.lkrn`
   - `PXELinux chain iPXE UNDI` to use `undionly-ipxe.0`
3. Click the name of the template you want to use.
4. Click the **Association** tab and select the operating systems that your host uses.
5. Click the **Locations** tab and add the location where the host resides.
6. Click the **Organizations** tab and add the organization that the host belongs to.
7. Click **Submit** to save the changes.
8. On the **Provisioning Templates** page, search for the required template:

   - For Debian hosts, search for `Preseed default iPXE` templates.
   - For Red Hat Enterprise Linux hosts, search for `Kickstart default iPXE` template.
   - For openSUSE/SUSE Linux Enterprise Server hosts, search for `Agama default iPXE` templates for SLES 16 or `AutoYaST default iPXE` for SLES 15 and SLES 12.
   - For Ubuntu hosts, search for `Preseed default iPXE Autoinstall` templates.
9. On the **Provisioning Templates** page, search for the `Kickstart default iPXE` template.
10. Click the name of the template.
11. Click the **Association** tab and associate the template with the operating system that your host uses.
12. Click the **Locations** tab and add the location where the host resides.
13. Click the **Organizations** tab and add the organization that the host belongs to.
14. Click **Submit** to save the changes.
15. In the Satellite web UI, navigate to **Hosts** > **Operating systems** and select the operating system of your host.
16. Click the **Templates** tab.
17. From the **PXELinux template** list, select the template you want to use.
18. From the **iPXE template** list, select the `Kickstart default iPXE` template.
19. Click **Submit** to save the changes.
20. In the Satellite web UI, navigate to **Configure** > **Host Groups**, and select the host group you want to configure.
21. Select the **Operating System** tab.
22. Select the **Architecture** and **Operating system**.
23. Set the **PXE Loader**:

    - Select `PXELinux BIOS` to chainboot iPXE (`ipxe.lkrn`) from PXELinux.
    - Select `iPXE Chain BIOS` to load `undionly-ipxe.0` directly.

**Additional resources**

- [Section 5.6, “Running custom code during host provisioning by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#running-custom-code-during-host-provisioning-by-using-web-ui "5.6. Running custom code during host provisioning by using Satellite web UI")

## 8.11. PXE loaders in Satellite

A PXE loader defines the `filename` DHCPv4 option to use during provisioning. Satellite deploys the required files to TFTP Capsule.

> **Note**
>
> Red Hat does not provide support for iPXE workflows.

Table 8.1. PXE loaders and DHCPv4 filenames

| PXE loader option | `filename` value | Use for |
| --- | --- | --- |
| **None** | No filename passed | Non-PXE booting, for example HTTP booting with iPXE or image-based provisioning |
| **PXELinux BIOS** | `pxelinux.0` | BIOS machines with PXE booting |
| **PXELinux UEFI** | `pxelinux.efi` | UEFI machines with PXE booting |
| **Grub2 BIOS** | `grub2/grubarch.0` | BIOS machines with PXE booting |
| **Grub2 UEFI** | `subdir/grub2/grubarch.efi` | UEFI machines with PXE boot using GRUB2 |
| **Grub2 UEFI SecureBoot** | `subdir/grub2/shimarch.efi` | SecureBoot-enabled UEFI machines with PXE booting |
| **Grub2 UEFI HTTP** | `http://capsule.example.com:8000/httpboot/subdir/grub2/grubarch.efi` | UEFI machines with HTTP booting |
| **Grub2 UEFI HTTPS** | `https://capsule.example.com:9090/httpboot/subdir/grub2/grubarch.efi` | UEFI machines with HTTP booting over HTTPS |
| **iPXE Embedded** | Satellite iPXE URL | Machines with iPXE embedded in their NIC firmware |
| **iPXE UEFI HTTP** | `http://capsule.example.com:8000/httpboot/ipxe-arch.efi` | UEFI machines with HTTP boot using iPXE implementation |
| **iPXE Chain BIOS** | `undionly-ipxe.0` | BIOS machines with PXE boot chainloading iPXE executable |
| **iPXE Chain UEFI** | `ipxe.efi` | UEFI machines with PXE boot chainloading iPXE executable |

**Additional resources**

- [Section 8.4, “Configuring Capsule to provision Red Hat Enterprise Linux by using UEFI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#configuring-capsule-to-provision-rhel-by-using-uefi "8.4. Configuring Capsule to provision Red Hat Enterprise Linux by using UEFI")
- [Supported architectures and provisioning scenarios](https://access.redhat.com/solutions/2674001)
