---
title: "Discovering hosts on a network"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#discovering-hosts-on-a-network"
---
# Chapter 10. Discovering hosts on a network

You can detect networked hosts not in your inventory by booting them into the Discovery image. The hosts relay hardware information to Satellite Server without manually entering MAC addresses.

## 10.1. Prerequisites for using Discovery

Before you start using Discovery, ensure that your environment meets the following requirements.

Ensure that your environment meets the following requirements:

- Ensure that the DHCP range of all subnets that you plan to use for Discovery does not overlap with the DHCP lease pool configured for the managed DHCP service. The DHCP range is set in the Satellite web UI, whereas the lease pool range is set by using the `satellite-installer` command.

  For example, in the 10.1.0.0/16 network range, you can allocate the following IP address blocks:

  - 10.1.0.0 to 10.1.127.255 for leases.
  - 10.1.128.0 to 10.1.255.254 for reservations.
- For provisioning of discovered hosts using `kexec` or automatic reboot as well as reboot of discovered hosts through Satellite web UI, ensure that the host and network-based firewalls are configured to allow communication from your Discovery Capsule to the discovered host on TCP port 8443.
- Ensure the host or virtual machine being discovered has at least 1200 MB of memory. Insufficient memory can cause various random kernel panic errors because the Discovery image is extracted in memory.

## 10.2. Installing the Discovery service

The Discovery service is enabled by default on Satellite Server. Additionally, you can enable the Discovery service on any Capsule Servers that provide the TFTP service.

The Discovery service requires a Discovery image, which is provided with Red Hat Satellite. The Discovery image uses a minimal operating system that is booted on hosts to acquire initial hardware information and check in with Satellite.

The Foreman Discovery image provided with Satellite is based on Red Hat Enterprise Linux 9.

**Procedure**

1. Install `foreman-discovery-image` on Satellite Server:

   ```
   # satellite-maintain packages install foreman-discovery-image
   ```

   The `foreman-discovery-image` package installs the Discovery ISO to the `/usr/share/foreman-discovery-image/` directory. The package also extracts the PXE boot image to the `/var/lib/tftpboot/boot/fdi-image/` directory.
2. On every Capsule Server you want to use as Discovery Capsule, install the Discovery plugin:

   ```
   # satellite-installer \
   --enable-foreman-proxy-plugin-discovery
   ```
3. On every Capsule Server you want to use as Discovery Capsule, install `foreman-discovery-image` on Capsule Server:

   ```
   # satellite-maintain packages install foreman-discovery-image
   ```

   The package extracts the PXE boot image to the `/var/lib/tftpboot/boot/fdi-image/` directory.
4. Configure the Discovery Capsule for the subnet with discoverable hosts:

   1. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
   2. Select a subnet.
   3. On the **Capsules** tab, select the Discovery Capsule that you want to use.

   Perform this for each subnet that you want to use.

## 10.3. Discovery in PXE mode

Satellite provides PXE-based Discovery that uses DHCP and TFTP services. Discovered hosts queued for installation reboot and provision through PXE.

**Figure 10.1. Discovery workflow in PXE mode**

[Image: Discovery workflow in PXE mode](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Provisioning_hosts-en-US/images/b6724589afbae38e49e3c0ada31f137d/discovery-pxe-mode-satellite.png)

### 10.3.1. Setting Discovery as the default PXE boot option

Set the Discovery service as the default service that boots for hosts that are not present in your current Satellite inventory.

When you start an unknown host in PXE mode, Satellite Server or Capsule Server provides a boot menu with a default boot option. The boot menu has two basic options: `local` and `discovery`. The default setting of the global PXE templates is to select `local` to boot the host from the local hard drive. Change the setting to select `discovery` to boot from the Discovery image.

**Prerequisites**

- Your Satellite account has the `view_settings`, `edit_settings`, and `view_provisioning_templates` permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. On the **Provisioning** tab, enter `discovery` in the **Default PXE global template entry** field.
3. Navigate to **Hosts** > **Templates** > **Provisioning Templates**.
4. Click **Build PXE Default**.

   The boot menus are built as the following files:

   - `/var/lib/tftpboot/pxelinux.cfg/default`
   - `/var/lib/tftpboot/grub2/grub.cfg`

   Satellite propagates the default boot menus to all TFTP Capsules.

### 10.3.2. Performing Discovery in PXE mode

Discovery in PXE mode uses the Discovery PXE boot images and runs unattended.

**Prerequisites**

- You have installed the Discovery service and image. For more information, see [Section 10.2, “Installing the Discovery service”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Installing_the_Discovery_Service_provisioning "10.2. Installing the Discovery service").
- You have set Discovery as the default booting option. For more information, see [Section 10.3.1, “Setting Discovery as the default PXE boot option”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#setting-discovery-as-the-default-PXE-boot-option_provisioning "10.3.1. Setting Discovery as the default PXE boot option").

**Procedure**

- Power on or reboot your host. After a few minutes, the Discovery image completes booting and the host displays a status screen.

**Verification**

- Satellite web UI displays a notification about a new discovered host.

**Next steps**

- In the Satellite web UI, navigate to **Hosts** > **Discovered Hosts** and view the newly discovered host. For more information about provisioning discovered hosts, see [Section 10.6, “Creating hosts from discovered hosts by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-hosts-from-discovered-hosts-by-using-web-ui "10.6. Creating hosts from discovered hosts by using Satellite web UI").

### 10.3.3. Customizing the Discovery PXE boot

You can add specific configuration information as kernel parameters into the boot process of hosts during automatic hardware detection. This is useful, for example, to direct the host to connect to specific Capsules or to provide additional network configuration.

Satellite builds PXE boot menus from the following global provisioning templates:

- `PXELinux global default` for BIOS provisioning.
- `PXEGrub2 global default` for UEFI provisioning.

The PXE boot menus are available on Satellite Server and Capsules that have TFTP enabled.

The Discovery menu item uses a Linux kernel for the operating system and passes kernel parameters to configure the Discovery service. You can customize the passed kernel parameters by changing the following snippets:

`pxelinux_discovery`
:   This snippet is included in the `PXELinux global default` template.

    This snippet renders the Discovery boot menu option. The `KERNEL` and `APPEND` options boot the Discovery kernel and initial RAM disk. The `APPEND` option contains kernel parameters.

`pxegrub2_discovery`
:   This snippet is included in the `PXEGrub2 global default` template.

    This snippet renders the Discovery GRUB2 menu entry. The `common` variable contains kernel parameters.

For information about the kernel parameters, see [Section 10.11, “Kernel parameters for Discovery customization”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#kernel-parameters-for-discovery-customization_provisioning "10.11. Kernel parameters for Discovery customization").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Clone and edit the snippet you want to customize. For more information, see [Section 5.5, “Cloning provisioning templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#cloning-provisioning-templates "5.5. Cloning provisioning templates").
3. Clone and edit the template that contains the original snippet. Include your custom snippet instead of the original snippet. For more information, see [Section 5.5, “Cloning provisioning templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#cloning-provisioning-templates "5.5. Cloning provisioning templates").
4. Navigate to **Administer** > **Settings**.
5. Click the **Provisioning** tab.
6. In the appropriate **Global default PXE\** template* setting, select your custom template.
7. Navigate to **Hosts** > **Templates** > **Provisioning Templates**.
8. Click **Build PXE Default**. This refreshes the default PXE boot menus on Satellite Server and any TFTP Capsules.

### 10.3.4. Host Discovery from multiple Capsule Servers

Satellite deploys the same template to all TFTP Capsules and there is no variable or macro available to render the host name of Capsule. The hard-coded `proxy.url` does not work with two or more TFTP Capsules.

As a workaround, every time you click **Build PXE Defaults**, edit the configuration file in the TFTP directory on all Capsule Servers by using SSH, or use a common DNS alias for appropriate subnets. To use Capsule Server to proxy the Discovery steps, edit `/var/lib/tftpboot/pxelinux.cfg/default` or `/var/lib/tftpboot/grub2/grub.cfg`, and change the URL to the Capsule Server FQDN you want to use.

## 10.4. Discovery in PXE-less mode

In environments without DHCP and TFTP, you can use PXE-less Discovery by using a Discovery ISO. Discovered hosts queued for installation reload the kernel with an operating system installer without rebooting.

> **Important**
>
> Discovery `kexec` is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

You might experience the following problems:

- The console might freeze during the process.
- On some hardware, you might experience graphical hardware problems.

**Figure 10.2. Discovery workflow in PXE-less mode**

[Image: Discovery workflow in PXE-less mode](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Provisioning_hosts-en-US/images/7690a24bfcb6fd0ea5f849897fe9fe97/discovery-pxeless-mode-satellite.png)

### 10.4.1. Performing Discovery in PXE-less mode

Discovery in PXE-less mode uses the Discovery ISO and requires you to attend to the process.

**Prerequisites**

- You have installed the Foreman Discovery image. For more information, see [Section 10.2, “Installing the Discovery service”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Installing_the_Discovery_Service_provisioning "10.2. Installing the Discovery service").

**Procedure**

1. Copy the Discovery ISO to a CD, DVD, or a USB flash drive. For example, to copy to a USB drive at `/dev/sdb`:

   ```
   # dd bs=4M \
   if=/usr/share/foreman-discovery-image/foreman-discovery-image-version.iso \
   of=/dev/sdb
   ```
2. Insert the Discovery boot media into a host, start the host, and boot from the media.
3. The Discovery image displays options for either **Manual network setup** or **Discovery with DHCP**:

   - **Manual network setup**:

     1. On the **Primary interface** screen, select the primary network interface that connects to Satellite Server or Capsule Server. Optionally, enter a **VLAN ID**. Hit **Select** to continue.
     2. On the **Network configuration** screen, enter the **Address**, **Gateway**, and **DNS**. Hit **Next** to continue.
   - **Discovery with DHCP**:

     1. On the **Primary interface** screen, select the primary network interface that connects to Satellite Server or Capsule Server. Optionally, enter a **VLAN ID**. Hit **Select** to continue.
     2. The Discovery image attempts to automatically configure the network interface by using a DHCP server, such as one that a Capsule Server provides.
4. On the **Credentials** screen, enter the following options:

   - In the **Server URL** field, enter the URL of Satellite Server or Discovery Capsule Server. If you refer to a Capsule Server, include the Capsule port number.
   - In the **Connection type** field, select the connection type: `Server` for Satellite Server or `Foreman Proxy` for Capsule Server.

   Hit **Next** to continue.
5. Optional: On the **Custom facts** screen, enter custom facts for the Facter tool to relay back to Satellite Server. Enter a name and value for each custom fact you need.
6. Hit **Confirm** to proceed.

**Verification**

- Satellite web UI displays a notification about a new discovered host.

**Next steps**

- In the Satellite web UI, navigate to **Hosts** > **Discovered Hosts** and view the newly discovered host. For more information about provisioning discovered hosts, see [Section 10.6, “Creating hosts from discovered hosts by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-hosts-from-discovered-hosts-by-using-web-ui "10.6. Creating hosts from discovered hosts by using Satellite web UI").

### 10.4.2. Customizing the Discovery ISO

You can create a customized Discovery ISO to automate the image configuration process after booting. The Discovery image uses a Linux kernel for the operating system, which passes kernel parameters to configure the Discovery service.

Satellite Server provides the `discovery-remaster` tool in the `foreman-discovery-image` package. By using this tool, remaster the image to include custom kernel parameters.

**Procedure**

1. Run the `discovery-remaster` tool. Enter the kernel parameters as a single string. For example:

   ```
   # discovery-remaster ~/iso/foreman-discovery-image-version.iso \
   "fdi.pxip=192.168.140.20/24 \
   fdi.pxgw=192.168.140.1 \
   fdi.pxdns=192.168.140.2 \
   proxy.url=https://satellite.example.com:9090 \
   proxy.type=proxy \
   fdi.pxfactname1=My_Custom_Hostname \
   fdi.pxfactvalue1=My_Host \
   fdi.pxmac=52:54:00:be:8e:8c fdi.pxauto=1"
   ```

   For more information about kernel parameters, see [Section 10.11, “Kernel parameters for Discovery customization”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#kernel-parameters-for-discovery-customization_provisioning "10.11. Kernel parameters for Discovery customization").
2. Copy the new ISO to either a CD, DVD, or a USB stick. For example, to copy to a USB stick at `/dev/sdb`:

   ```
   # dd bs=4M \
   if=/usr/share/foreman-discovery-image/foreman-discovery-image-version.iso \
   of=/dev/sdb
   ```

**Next steps**

- Insert the Discovery boot medium into a bare-metal host, start the host, and boot from the medium.

  For more information about provisioning discovered hosts, see [Section 10.6, “Creating hosts from discovered hosts by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-hosts-from-discovered-hosts-by-using-web-ui "10.6. Creating hosts from discovered hosts by using Satellite web UI").

## 10.5. Automatic contexts for discovered hosts

Satellite Server automatically assigns an organization and location to discovered hosts automatically.

Satellite Server assigns organizations and locations to discovered hosts according to the following sequence of rules:

1. If a discovered host uses a subnet defined in Satellite, the host uses the first organization and location associated with the subnet.
2. If the default location and organization is configured in global settings, the discovered hosts are placed in this organization and location. To configure these settings, navigate to **Administer** > **Settings** > **Discovery** and select values for the **Discovery organization** and **Discovery location** settings. Ensure that the subnet of discovered host also belongs to the selected organization and location, otherwise Satellite refuses to set it for security reasons.
3. If none of the previous conditions is met, Satellite assigns the first organization and location ordered by name.

You can change the organization or location manually by using the bulk actions on the **Discovered Hosts** page. Select the discovered hosts to modify and, from the **Select Action** menu, select **Assign Organization** or **Assign Location**.

## 10.6. Creating hosts from discovered hosts by using Satellite web UI

Provisioning discovered hosts follows a provisioning process that is similar to PXE provisioning. The main difference is that instead of manually entering the host’s MAC address, you can select the host to provision from the list of discovered hosts.

**Prerequisites**

- Configure a domain and subnet on Satellite. For more information about networking requirements, see [Chapter 2, *Preparing networking for host management*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management "Chapter 2. Preparing networking for host management").
- You have one or more discovered hosts in your Satellite inventory.
- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.
- You have associated a `Discovery kexec`-kind template and `provisioning`-kind template with the operating system. For more information, see [Section 5.10, “Associating templates with operating systems by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#associating-templates-with-operating-systems-by-using-web-ui "5.10. Associating templates with operating systems by using Satellite web UI").

For information about the security tokens, see [Section 6.1, “Configuring the security token validity duration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#configuring-the-security-token-validity-duration "6.1. Configuring the security token validity duration").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Discovered hosts**.
2. Select the host you want to provision and click **Provision** to the right of the list.
3. Select one of the following options:

   - To provision a host from a host group, select a host group, organization, and location, and then click **Create Host**.
   - To provision a host with further customization, click **Customize Host** and enter the additional details you want to specify for the new host.
4. Verify that the fields are populated with values. Note in particular:

   - The **Name** from the **Host** tab becomes the **DNS name**.
   - Satellite Server automatically assigns an IP address for the new host.
   - Satellite Server automatically populates the MAC address from the Discovery results.
5. Ensure that Satellite Server automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
6. Click the **Operating System** tab, and verify that all fields contain values. Confirm each aspect of the operating system.
7. In **Provisioning templates**, click **Resolve** to check if the new host can identify the correct provisioning templates. The host must resolve to the following provisioning templates:

   - **Discovery kexec**: `Discovery Red Hat kexec`
   - **Provisioning template**: `Kickstart default`
8. Click **Submit** to save the host details.

   When the host provisioning is complete, the discovered host moves to **Hosts** > **All Hosts**.

## 10.7. Creating hosts from discovered hosts by using Hammer CLI

Provisioning discovered hosts follows a provisioning process that is similar to PXE provisioning. The main difference is that instead of manually entering the host’s MAC address, you can select the host to provision from the list of discovered hosts.

**Prerequisites**

- Configure a domain and subnet on Satellite. For more information about networking requirements, see [Chapter 2, *Preparing networking for host management*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management "Chapter 2. Preparing networking for host management").
- You have one or more discovered hosts in your Satellite inventory.
- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.
- You have associated a `Discovery kexec`-kind template and `provisioning`-kind template with the operating system. For more information, see [Section 5.11, “Associating templates with operating systems by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#associating-templates-with-operating-systems-by-using-cli "5.11. Associating templates with operating systems by using Hammer CLI").

For information about the security tokens, see [Section 6.1, “Configuring the security token validity duration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#configuring-the-security-token-validity-duration "6.1. Configuring the security token validity duration").

**Procedure**

1. Identify the discovered host to provision:

   ```
   $ hammer discovery list
   ```
2. Select the host and provision it by using a host group. Set a new host name with the `--new-name` option:

   ```
   $ hammer discovery provision \
   --build true \
   --enabled true \
   --hostgroup "My_Host_Group" \
   --location "My_Location" \
   --managed true \
   --name "My_Host_Name" \
   --new-name "My_New_Host_Name" \
   --organization "My_Organization"
   ```

   This removes the host from the discovered host listing and creates a host entry with the provisioning settings. The Discovery image automatically reboots the host to PXE or initiates kernel execution. The host detects the DHCP service and starts installing the operating system. The rest of the process is identical to the normal PXE workflow. For more information, see [Section 8.6, “Creating hosts with PXE boot provisioning by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-hosts-with-pxe-boot-provisioning-by-using-cli "8.6. Creating hosts with PXE boot provisioning by using Hammer CLI").

## 10.8. Creating Discovery rules by using Satellite web UI

You can automate provisioning of discovered hosts by creating Discovery rules that assign hosts to host groups based on hardware attributes. For example, you can automatically provision hosts with a large number of CPU cores as hypervisors and hosts with large disks as storage servers.

> **Note**
>
> Auto provisioning does not currently allow configuring network interface cards (NICs). All systems are being provisioned with the NIC configuration that was detected during Discovery. However, you can set the NIC in the `kickstart` scriptlet, by using a script, or by using configuration management at a later stage.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Discovery rules**, and select **Create Rule**.
2. In the **Name** field, enter a name for the rule.
3. In the **Search** field, enter the rules to determine whether to provision a host. This field provides suggestions for values you enter and allows operators for multiple rules. For example: `cpu_count > 8`.
4. From the **Host Group** list, select the host group to use as a template for this host.
5. In the **Hostname** field, enter the pattern to determine host names for multiple hosts. This uses the same ERB syntax that provisioning templates use. The host name can use the `@host` attribute for host-specific values and the `rand` macro for a random number or the `sequence_hostgroup_param_next` macro for incrementing the value. For more information about provisioning templates, see [Section 5.1, “Provisioning templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-templates "5.1. Provisioning templates") and the API documentation.

   - `myhost-<%= sequence_hostgroup_param_next("EL7/MyHostgroup", 10, "discovery_host") %>`
   - `myhost-<%= rand(99999) %>`
   - `abc-<%= @host.facts['bios_vendor'] %>-<%= rand(99999) %>`
   - `xyz-<%= @host.hostgroup.name %>`
   - `srv-<%= @host.discovery_rule.name %>`
   - `server-<%= @host.ip.gsub('.','-') + '-' + @host.hostgroup.subnet.name %>`

     When creating host name patterns, ensure that the resulting host names are unique, do not start with numbers, and do not contain underscores or dots. A good approach is to use unique information provided by Facter, such as the MAC address, BIOS, or serial ID.
6. In the **Hosts limit** field, enter the maximum number of hosts that you can provision with the rule. Enter `0` for unlimited.
7. In the **Priority** field, enter a number to set the precedence the rule has over other rules. Rules with lower values have a higher priority.
8. From the **Enabled** list, select whether you want to enable the rule.
9. To set a different provisioning context for the rule, click the **Organizations** and **Locations** tabs and select the contexts you want to use.
10. Click **Submit** to save your rule.
11. In the Satellite web UI, navigate to **Hosts** > **Discovered Host** and select one of the following two options:

    - From the **Discovered hosts** list on the right, select **Auto-Provision** to automatically provisions a single host.
    - On the upper right of the window, click **Auto-Provision All** to automatically provisions all hosts.

## 10.9. Creating Discovery rules by using Hammer CLI

You can automate provisioning of discovered hosts by creating Discovery rules that assign hosts to host groups based on hardware attributes. For example, you can automatically provision hosts with a large number of CPU cores as hypervisors and hosts with large disks as storage servers.

> **Note**
>
> Auto provisioning does not currently allow configuring network interface cards (NICs). All systems are being provisioned with the NIC configuration that was detected during Discovery. However, you can set the NIC in the `kickstart` scriptlet, by using a script, or by using configuration management at a later stage.

**Procedure**

1. Create a Discovery rule:

   ```
   $ hammer discovery-rule create \
   --enabled true \
   --hostgroup "My_Host_Group" \
   --hostname "hypervisor-<%= rand(99999) %>" \
   --hosts-limit 5 \
   --name "My_Hypervisor" \
   --priority 5 \
   --search "cpu_count  > 8"
   ```
2. Automatically provision a host with the `hammer discovery auto-provision` command:

   ```
   $ hammer discovery auto-provision --name "macabcdef123456"
   ```

## 10.10. Extending the Discovery image

You can extend the Satellite Discovery image with custom facts, software, or device drivers. You can also provide a compressed archive file containing extra code for the image to use.

**Procedure**

1. Create the following directory structure:

   ```
   .
   ├── autostart.d
   │   └── 01_zip.sh
   ├── bin
   │   └── ntpdate
   ├── facts
   │   └── test.rb
   └── lib
       ├── libcrypto.so.1.0.0
       └── ruby
           └── test.rb
   ```

   - The `autostart.d` directory contains scripts that are executed in POSIX order by the Discovery kernel when it starts but before the host is registered to Satellite.
   - The `bin` directory is added to the `$PATH` variable; you can place binary files in this directory and use them in the `autostart` scripts.
   - The `facts` directory is added to the `FACTERLIB` variable so that custom facts can be configured and sent to Satellite.
   - The `lib` directory is added to the `LD_LIBRARY_PATH` variable and `lib/ruby` is added to the `RUBYLIB` variable, so that binary files in `/bin` can be executed correctly.
2. After creating the directory structure, create a `.zip` file archive:

   ```
   # zip -r my_extension.zip .
   ```
3. Inform the Discovery kernel of the extensions it must use. Place your zip files on your TFTP server with the Discovery image and customize the Discovery PXE boot with the `fdi.zips` parameter where the paths are relative to the TFTP root.

   For example, if you have two archives at `$TFTP/zip1.zip` and `$TFTP/boot/zip2.zip`, use the following syntax:

   ```
   fdi.zips=zip1.zip,boot/zip2.zip
   ```

   For more information, see [Section 10.3.3, “Customizing the Discovery PXE boot”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Customizing_the_Discovery_PXE_Boot_provisioning "10.3.3. Customizing the Discovery PXE boot").

   You can append new directives and options to the existing environment variables (`PATH`, `LD_LIBRARY_PATH`, `RUBYLIB` and `FACTERLIB`). If you want to specify the path explicitly in your scripts, the `.zip` file contents are extracted to the `/opt/extension` directory on the image.

   You can create multiple `.zip` files but be aware that they are extracted to the same location on the Discovery image. Files extracted from in later `.zip` files overwrite earlier versions if they contain the same file name.

## 10.11. Kernel parameters for Discovery customization

Discovery uses a Linux kernel for the operating system and passes kernel parameters to configure the Discovery service.

These kernel parameters include the following entries:

fdi.cachefacts
:   Number of fact uploads without caching. By default, Satellite does not cache any uploaded facts.

fdi.countdown
:   Number of seconds to wait until the text-user interface is refreshed after the initial discovery attempt. This value defaults to 45 seconds. Increase this value if the status page reports the IP address as `N/A`.

fdi.dhcp_timeout
:   NetworkManager DHCP timeout. The default value is 300 seconds.

fdi.dns_nameserver
:   Nameserver to use for DNS SRV record.

fdi.dns_ndots
:   `ndots` option to use for DNS SRV record.

fdi.dns_search
:   Search domain to use for DNS SRV record.

fdi.initnet
:   By default, the image initializes all network interfaces (value `all`). When this setting is set to `bootif`, only the network interface it was network-booted from will be initialized.

fdi.ipv4.method
:   By default, NetworkManager IPv4 method setting is set to `auto`. This option overrides it, set it to `ignore` to disable the IPv4 stack. This option works only in DHCP mode.

fdi.ipv6.method
:   By default, NetworkManager IPv6 method setting is set to `auto`. This option overrides it, set it to `ignore` to disable the IPv6 stack. This option only works in DHCP mode.

fdi.ipwait
:   Duration in seconds to wait for IP to be available in HTTP proxy SSL cert start. By default, Satellite waits for 120 seconds.

fdi.nmwait
:   `nmcli -wait` option for NetworkManager. By default, `nmcli` waits for 120 seconds.

fdi.proxy_cert_days
:   Number of days the self-signed HTTPS cert is valid for. By default, the certificate is valid for 999 days.

fdi.pxauto
:   To set automatic or semi-automatic mode. If set to 0, the image uses semi-automatic mode, which allows you to confirm your choices through a set of dialog options. If set to 1, the image uses automatic mode and proceeds without any confirmation.

fdi.pxfactname1, fdi.pxfactname2 …​ fdi.pxfactnameN
:   Use to specify custom fact names.

fdi.pxfactvalue1, fdi.pxfactvalue2 …​ fdi.pxfactvalueN
:   The values for each custom fact. Each value corresponds to a fact name. For example, `fdi.pxfactvalue1` sets the value for the fact named with `fdi.pxfactname1`.

fdi.pxip, fdi.pxgw, fdi.pxdns
:   Manually configures IP address (`fdi.pxip`), the gateway (`fdi.pxgw`), and the DNS (`fdi.pxdns`) for the primary network interface. If you omit these parameters, the image uses DHCP to configure the network interface. You can add multiple DNS entries in a comma-separated [[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#ftn.idm140520013446224) list, for example `fdi.pxdns=192.168.1.1,192.168.200.1`.

fdi.pxmac
:   The MAC address of the primary interface in the format of `AA:BB:CC:DD:EE:FF`. This is the interface you aim to use for communicating with Capsule Server. In automated mode, the first NIC (using network identifiers in alphabetical order) with a link is used. In semi-automated mode, a screen appears and requests you to select the correct interface.

fdi.rootpw
:   By default, the `root` account is locked. Use this option to set a root password. You can enter both clear and encrypted passwords.

fdi.ssh
:   By default, the SSH service is disabled. Set this to `1` or `true` to enable SSH access.

fdi.uploadsleep
:   Duration in seconds between facter runs. By default, facter runs every 30 seconds.

fdi.vlan.primary
:   VLAN tagging ID to set for the primary interface. If you want to use tagged VLAN provisioning and you want the Discovery service to send a discovery request, add the following parameter to the Discovery snippet:

    ```
    fdi.vlan.primary=My_VLAN_ID
    ```

fdi.zips
:   Filenames with extensions to be downloaded and started during boot. For more information, see [Section 10.10, “Extending the Discovery image”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Extending_the_Discovery_Image_provisioning "10.10. Extending the Discovery image").

fdi.zipserver
:   TFTP server to use to download extensions from. For more information, see [Section 10.10, “Extending the Discovery image”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Extending_the_Discovery_Image_provisioning "10.10. Extending the Discovery image").

net.ifnames and biosdevname
:   Because network interface names are not expected to always be the same [between major versions](https://access.redhat.com/solutions/5984311) of Red Hat Enterprise Linux, hosts can be created with incorrect network configurations. You can disable the new naming scheme by a kernel command line parameter:

    - For Dell servers, use the `biosdevname=1` parameter.
    - For other hardware or virtual machines, use the `net.ifnames=1` parameter.

proxy.type
:   The proxy type. By default, this parameter is set to `foreman`, where communication goes directly to Satellite Server. Set this parameter to `proxy` if you point to Capsule in `proxy.url`.

proxy.url
:   The URL of the server providing the Discovery service. By default, this parameter contains the `foreman_server_url` macro as its argument. This macro resolves to the full URL of Satellite Server. There is no macro for a Capsule URL. You have to set a Capsule explicitly. For example:

    ```
    proxy.url=https://capsule.example.com:9090 proxy.type=proxy
    ```

    You can use an IP address or FQDN in this parameter. Add a SSL port number if you point to Capsule.

---

[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#idm140520013446224)
NetworkManager expects `;` as a list separator but currently also accepts `,`. For more information, see `man nm-settings-keyfile`

## 10.12. Troubleshooting Discovery failures

If a machine is not listed in the Satellite web UI in **Hosts** > **Discovered Hosts**, it means that Discovery has failed. Inspect the following configuration areas to help isolate the problem:

Inspecting prerequisites
:   - Ensure that your Satellite and hosts meet the requirements. For more information, see [Section 10.1, “Prerequisites for using Discovery”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#prerequisites-for-using-discovery_provisioning "10.1. Prerequisites for using Discovery").

Inspecting problems on Satellite
:   - Ensure you have set Discovery for booting and built the PXE boot configuration files. For more information, see [Section 10.3.1, “Setting Discovery as the default PXE boot option”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#setting-discovery-as-the-default-PXE-boot-option_provisioning "10.3.1. Setting Discovery as the default PXE boot option").
    - Verify that these configuration files are present on your TFTP Capsule and have `discovery` set as the default boot option:

      - `/var/lib/tftpboot/pxelinux.cfg/default`
      - `/var/lib/tftpboot/grub2/grub.cfg`
    - Verify that the values of the `proxy.url` and `proxy.type` options in the PXE Discovery snippet you are using. The default snippets are named `pxelinux_discovery` or `pxegrub2_discovery`.

Inspecting problems with networking
:   - Ensure adequate network connectivity between hosts, Capsule Server, and Satellite Server.
    - Ensure that the DHCP server provides IP addresses to the booted Discovery image correctly.
    - Ensure that DNS is working correctly for the discovered hosts or use an IP address in the `proxy.url` option in the PXE Discovery snippet included in the PXE template you are using.

Inspecting problems on the host
:   - If the host boots into the Discovery image but Discovery is not successful, enable the root account and SSH access on the Discovery image. You can enable SSH and set the root password by using the following Discovery kernel options:

      ```
      fdi.ssh=1 fdi.rootpw=My_Password
      ```
    - Using TTY2 or higher, log in to a Discovery-booted host to review system logs. For example, these logs are useful for troubleshooting:

`discover-host`
:   Initial facts upload

`foreman-discovery`
:   Facts refresh, reboot remote commands

`nm-prepare`
:   Boot script which pre-configures NetworkManager

`NetworkManager`
:   Networking information

    - For gathering important system facts, use the `discovery-debug` command on the Discovery-booted host. It prints out system logs, network configuration, list of facts, and other information on the standard output. You can redirect this output to a file and copy it with the `scp` command for further investigation.

**Additional resources**

- [Section 10.3.3, “Customizing the Discovery PXE boot”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Customizing_the_Discovery_PXE_Boot_provisioning "10.3.3. Customizing the Discovery PXE boot")
- [Section 10.4.2, “Customizing the Discovery ISO”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#customizing-the-discovery-iso_provisioning "10.4.2. Customizing the Discovery ISO")
