---
title: "Provisioning virtual machines in VMware"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "12"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-virtual-machines-in-vmware"
---
# Chapter 12. Provisioning virtual machines in VMware

You can create and manage virtual machines on VMware vSphere by using Satellite. VMware vSphere is an enterprise-level virtualization platform.

## 12.1. Prerequisites for VMware provisioning

Before you can deploy virtual machines to VMware vSphere, ensure that your environment meets the following requirements.

The requirements for VMware vSphere provisioning include:

- A supported version of VMware vCenter Server. The following versions have been fully tested with Satellite:

  - vCenter Server 8.0
  - vCenter Server 7.0
- A Capsule Server managing a network on the vSphere environment. Ensure no other DHCP services run on this network to avoid conflicts with Capsule Server. For more information, see [Chapter 2, *Preparing networking for host management*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management "Chapter 2. Preparing networking for host management").
- An existing VMware template if you want to use image-based provisioning.
- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.

## 12.2. VMware user privileges

VMware vSphere requires an administration-like user for Satellite Server communication. For security, create a dedicated user with required privileges instead of using the `administrator` account.

In VMware vCenter Server version 8.0 or 7.0, set the following privileges:

- All Privileges → Datastore → Allocate Space, Browse datastore, Update Virtual Machine files, Low level file operations
- All Privileges → Network → Assign Network
- All Privileges → Resource → Assign virtual machine to resource pool
- All Privileges → Virtual Machine → Change Config (All)
- All Privileges → Virtual Machine → Interaction (All)
- All Privileges → Virtual Machine → Edit Inventory (All)
- All Privileges → Virtual Machine → Provisioning (All)
- All Privileges → Virtual Machine → Guest Operations (All)

If you want to create virtual machines with a Virtual Trusted Platform Module (TPM) for enhanced security, set the following privileges:

- All Privileges → Cryptographic operations → Clone, Encrypt, Encrypt new, Migrate, Register VM
- All Privileges → Cryptographic operations → Direct Access – required to open a console session

## 12.3. Adding a VMware connection to Satellite Server by using Satellite web UI

Add VMware vSphere as a compute resource to provision and manage hosts on VMware.

**Prerequisites**

- Ensure that the host and network-based firewalls are configured to allow communication from Satellite Server to vCenter on TCP port 443.
- Verify that Satellite Server and vCenter can resolve each other’s host names.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**, and in the Compute Resources window, click **Create Compute Resource**.
2. In the **Name** field, enter a name for the resource.
3. From the **Provider** list, select **VMware**.
4. In the **Description** field, enter a description for the resource.
5. In the **VCenter/Server** field, enter the IP address or host name of the vCenter server.
6. In the **User** field, enter the user name with permission to access the vCenter’s resources.
7. In the **Password** field, enter the password for the user.
8. Click **Load Datacenters** to populate the list of data centers from your VMware vSphere environment.
9. From the **Datacenter** list, select a specific data center to manage from this list.
10. In the **Fingerprint** field, ensure that this field is populated with the fingerprint from the data center.
11. From the **Display Type** list, select a console type, for example, **VNC** or **VMRC**. Note that VNC consoles are unsupported on VMware ESXi 6.5 and later.
12. Optional: In the **VNC Console Passwords** field, select the **Set a randomly generated password on the display connection** checkbox to secure console access for new hosts with a randomly generated password.
13. From the **Enable Caching** list, you can select whether to enable caching of compute resources. For more information, see [Section 12.17, “Caching of compute resources”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#caching-of-compute-resources "12.17. Caching of compute resources").
14. Click the **Locations** and **Organizations** tabs and verify that the values are automatically set to your current context. You can also add additional contexts.
15. Click **Submit** to save the connection.

## 12.4. Adding a VMware connection to Satellite Server by using Hammer CLI

Add VMware vSphere as a compute resource to provision and manage hosts on VMware.

**Prerequisites**

- Ensure that the host and network-based firewalls are configured to allow communication from Satellite Server to vCenter on TCP port 443.
- Verify that Satellite Server and vCenter can resolve each other’s host names.

**Procedure**

- Add a VMware connection to Satellite:

  ```
  $ hammer compute-resource create \
  --datacenter "My_Data_Center" \
  --description "vSphere server at vsphere.example.com" \
  --locations "My_Location" \
  --name "My_vSphere" \
  --organizations "My_Organization" \
  --password "My_Password" \
  --provider "Vmware" \
  --server "vsphere.example.com" \
  --user "My_User" \
  --uuid "My_Data_Center_UUID"
  ```

## 12.5. Adding VMware images to Satellite Server by using Satellite web UI

You must add VMware template details to Satellite Server for image-based provisioning.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select your VMware compute resource.
3. Click **Create Image**.
4. In the **Name** field, enter a name for the image.
5. From the **Operating System** list, select the base operating system of the image.
6. From the **Architecture** list, select the operating system architecture.
7. In the **Username** field, enter the SSH user name for image access. By default, this is set to `root`.
8. If your image supports user data input such as `cloud-init` data, click the **User data** checkbox.
9. Optional: In the **Password** field, enter the SSH password to access the image.
10. From the **Image** list, select an image from VMware.
11. Click **Submit** to save the image details.

## 12.6. Adding VMware images to Satellite Server by using Hammer CLI

You must add VMware template details to Satellite Server for image-based provisioning.

**Procedure**

- Create an image. Use the `--uuid` field to store the relative template path on the vSphere environment:

  ```
  $ hammer compute-resource image create \
  --architecture "My_Architecture" \
  --compute-resource "My_VMware"
  --name "My_Image" \
  --operatingsystem "My_Operating_System" \
  --username root \
  --uuid "My_UUID"
  ```

## 12.7. Adding VMware details to a compute profile by using Satellite web UI

You can predefine certain hardware settings for virtual machines on VMware vSphere. You achieve this through adding these hardware settings to a compute profile.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Profiles**.
2. Select a compute profile.
3. Select a VMware compute resource.
4. In the **CPUs** field, enter the number of CPUs to allocate to the host.
5. In the **Cores per socket** field, enter the number of cores to allocate to each CPU.
6. In the **Memory** field, enter the amount of memory in MiB to allocate to the host.
7. In the **Firmware** field, select the firmware type for the host. By default, this is set to **Automatic**. If you want to provision Secure Boot-enabled hosts, select **UEFI Secure Boot**.
8. In the **Cluster** list, select the name of the target host cluster on the VMware environment.
9. From the **Resource pool** list, select an available resource allocations for the host.
10. In the **Folder** list, select the folder to organize the host.
11. From the **Guest OS** list, select the operating system you want to use in VMware vSphere.
12. From the **Virtual H/W version** list, select the underlying VMware hardware abstraction to use for virtual machines.
13. If you want to add more memory while the virtual machine is powered on, select the **Memory hot add** checkbox.
14. If you want to add more CPUs while the virtual machine is powered on, select the **CPU hot add** checkbox.
15. If you want to add a CD-ROM drive, select the **CD-ROM drive** checkbox.
16. From the **Boot order** list, define the order in which the virtual machines tried to boot.
17. Optional: In the **Annotation Notes** field, enter an arbitrary description.
18. If you use image-based provisioning, select the image from the **Image** list.
19. From the **SCSI controller** list, select the disk access method for the host.
20. If you want to use eager zero thick provisioning, select the **Eager zero** checkbox. By default, the disk uses lazy zero thick provisioning.
21. Optional: Select **Virtual TPM** if you want to add a Virtual Trusted Platform Module for enhanced security. This is compatible with UEFI firmware only.
22. From the **Network Interfaces** list, select the network parameters for the host’s network interface. At least one interface must point to a Capsule-managed network.
23. Optional: Click **Add Interface** to create another network interfaces.
24. Click **Submit** to save the compute profile.

## 12.8. Adding VMware details to a compute profile by using Hammer CLI

You can predefine certain hardware settings for virtual machines on VMware vSphere. You achieve this through adding these hardware settings to a compute profile.

**Procedure**

1. Create a compute profile:

   ```
   $ hammer compute-profile create --name "My_Compute_Profile"
   ```
2. Set VMware details to a compute profile:

   ```
   $ hammer compute-profile values create \
   --compute-attributes "cpus=1,corespersocket=2,memory_mb=1024,cluster=MyCluster,path=MyVMs,virtual_tpm=true,start=true" \
   --compute-profile "My_Compute_Profile" \
   --compute-resource "My_VMware" \
   --interface "compute_type=VirtualE1000,compute_network=mynetwork \
   --volume "size_gb=20G,datastore=Data,name=myharddisk,thin=true"
   ```

## 12.9. Creating hosts on VMware by using Satellite web UI

In Satellite, you can use network or image-based provisioning to create hosts on VMware.

For network-based provisioning, you must create a host to access either Satellite Server or Capsule Servers on a VMware virtual network, so that the host has access to PXE provisioning services. The new host entry triggers the VMware to create the virtual machine. If the virtual machine detects the defined Capsule through the virtual network, the virtual machine boots to PXE and begins to install the chosen operating system.

**Prerequisites**

- For network-based provisioning, if you use a virtual network on the VMware server for provisioning, select a network that does not provide DHCP assignments. This causes DHCP conflicts with Satellite Server when booting new hosts.
- If you want to create a host over a network connection, the new host must be able to access your Satellite Server or Capsule Servers on a VMware virtual network, so that the host has access to PXE provisioning services. This new host entry triggers the VMware server to create and start a virtual machine. If the virtual machine detects the defined Capsule Server through the virtual network, the virtual machine boots to PXE and begins to install the chosen operating system.
- If you want to create a host with an existing image, the new host entry triggers the VMware server to create the virtual machine using a pre-existing image as a basis for the new volume.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. From the **Deploy on** list, select the VMware connection.
7. From the **Compute Profile** list, select a profile to use to automatically populate virtual machine settings. The VMware-specific fields are populated with settings from your compute profile. Modify these settings if required.
8. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
9. Verify that the fields are populated with values. Note in particular:

   - Satellite automatically assigns an IP address for the new host.
   - Ensure that the **MAC address** field is blank. VMware assigns a MAC address to the host during provisioning.
   - The **Name** from the **Host** tab becomes the **DNS name**.
   - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
10. In the interface window, review the VMware-specific fields that are populated with settings from our compute profile. Modify these settings to suit your needs.
11. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

    For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
12. Click the **Operating System** tab, and confirm that all fields automatically contain values.
13. Select the **Provisioning Method** that you want to use:

    - For network-based provisioning, click **Network Based**.
    - For image-based provisioning, click **Image Based**.
    - For boot disk-based provisioning, click **Boot disk based**.
14. Click **Resolve** in **Provisioning templates** to check the new host can identify the right provisioning templates to use.
15. Click the **Virtual Machine** tab and confirm that these settings are populated with details from the host group and compute profile. Modify these settings to suit your needs.

    If you want to provision a Secure Boot-enabled host, select **UEFI Secure Boot** in the **Firmware** field.
16. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
17. Click **Submit** to save the host entry.

## 12.10. Creating hosts on VMware by using Hammer CLI

In Satellite, you can use VMware provisioning to create hosts over a network connection or from an existing image.

For network-based provisioning, you must create a host to access either Satellite Server or Capsule Servers on a VMware vSphere virtual network, so that the host has access to PXE provisioning services. The new host entry triggers the VMware vSphere server to create the virtual machine. If the virtual machine detects the defined Capsule through the virtual network, the virtual machine boots to PXE and begins to install the chosen operating system. For more information about additional host creation parameters for this compute resource, enter the `hammer host create --help` command.

**Prerequisites**

- For network-based provisioning, if you use a virtual network on the VMware server for provisioning, select a network that does not provide DHCP assignments. This causes DHCP conflicts with Satellite Server when booting new hosts.
- If you want to create a host over a network connection, the new host must be able to access your Satellite Server or Capsule Servers on a VMware virtual network, so that the host has access to PXE provisioning services. This new host entry triggers the VMware server to create and start a virtual machine. If the virtual machine detects the defined Capsule Server through the virtual network, the virtual machine boots to PXE and begins to install the chosen operating system.
- If you want to create a host with an existing image, the new host entry triggers the VMware server to create the virtual machine using a pre-existing image as a basis for the new volume.

**Procedure**

- Create a host by using one of the following methods:

  - To use network-based provisioning, create the host with the `hammer host create` command and include `--provision-method build`. Replace the values in the following example with the appropriate values for your environment.

    ```
    $ hammer host create \
    --build true \
    --compute-attributes="cpus=1,corespersocket=2,memory_mb=1024,cluster=MyCluster,path=MyVMs,start=true" \
    --compute-resource "My_VMware" \
    --enabled true \
    --hostgroup "My_Host_Group" \
    --interface "managed=true,primary=true,provision=true,compute_type=VirtualE1000,compute_network=mynetwork" \
    --location "My_Location" \
    --managed true \
    --name "My_Host" \
    --organization "My_Organization" \
    --provision-method build \
    --volume="size_gb=20G,datastore=Data,name=myharddisk,thin=true"
    ```
  - To use image-based provisioning, create the host with the `hammer host create` command and include `--provision-method image`. Replace the values in the following example with the appropriate values for your environment.

    ```
    $ hammer host create \
    --compute-attributes="cpus=1,corespersocket=2,memory_mb=1024,cluster=MyCluster,path=MyVMs,start=true" \
    --compute-resource "My_VMware" \
    --enabled true \
    --hostgroup "My_Host_Group" \
    --image "My_VMware_Image" \
    --interface "managed=true,primary=true,provision=true,compute_type=VirtualE1000,compute_network=mynetwork" \
    --location "My_Location" \
    --managed true \
    --name "My_Host" \
    --organization "My_Organization" \
    --provision-method image \
    --volume="size_gb=20G,datastore=Data,name=myharddisk,thin=true"
    ```

## 12.11. VMware cloud-init provisioning overview

When you set up the compute resource and images for VMware provisioning in Satellite, the following sequence of provisioning events occurs.

VMware `cloud-init` performs the following provisioning sequence:

1. The user provisions one or more virtual machines using the Satellite web UI, API, or Hammer
2. Satellite calls the VMware vCenter to clone the virtual machine template
3. Satellite `userdata` provisioning template adds customized identity information
4. When provisioning completes, the `Cloud-init` provisioning template instructs the virtual machine to call back to Capsule when `cloud-init` runs
5. VMware vCenter clones the template to the virtual machine
6. VMware vCenter applies customization for the virtual machine’s identity, including the host name, IP, and DNS
7. The virtual machine builds, `cloud-init` is invoked and calls back Satellite on port `80`, which then redirects to `443`

**Figure 12.1. VMware cloud-init provisioning overview**

[Image: VMware cloud-init provisioning overview](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Provisioning_hosts-en-US/images/d35482be70ff604d3e48099f22f7b287/user-data-sequence-satellite.png)

## 12.12. Associating the userdata and cloud-init templates with the operating system

Before you can use VMware `cloud-init` and `userdata` templates for provisioning, you must associate these templates with your operating system.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Search for the **CloudInit default** template and click its name.
3. Click the **Association** tab.
4. Select all operating systems to which the template applies and click **Submit**.
5. Repeat the steps above for the **UserData open-vm-tools** template.
6. Navigate to **Hosts** > **Provisioning Setup** > **Operating Systems**.
7. Select the operating system that you want to use for provisioning.
8. Click the **Templates** tab.
9. From the **Cloud-init template** list, select **CloudInit default**.
10. From the **User data template** list, select **UserData open-vm-tools**.
11. Click **Submit** to save the changes.

## 12.13. Preparing an image to use the cloud-init template

To prepare an image, you must first configure the settings that you require on a virtual machine that you can then save as an image to use in Satellite.

**Procedure**

1. To use the `cloud-init` template for provisioning, you must configure a virtual machine so that `cloud-init` is installed, enabled, and configured to call back to Satellite Server.
2. For security purposes, you must install a CA certificate to use HTTPS for all communication. This procedure includes steps to clean the virtual machine so that no unwanted information transfers to the image you use for provisioning.
3. If you have an image with `cloud-init`, you must still follow this procedure to enable `cloud-init` to communicate with Satellite because `cloud-init` is disabled by default.

## 12.14. Using VMware cloud-init and userdata templates for provisioning

You can use VMware with the `Cloud-init` and `Userdata` templates to insert user data into the new virtual machine, to make further VMware customization, and to enable the VMware-hosted virtual machine to call back to Satellite.

You can use the same procedures to set up a VMware compute resource within Satellite, with a few modifications to the workflow.

**Prerequisites**

- The templates are associated with your operating system. For more information, see [Section 12.12, “Associating the userdata and cloud-init templates with the operating system”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#associating-the-userdata-and-cloud-init-templates-with-the-operating-system "12.12. Associating the userdata and cloud-init templates with the operating system").
- An image is prepared. For more information, see [Section 12.13, “Preparing an image to use the cloud-init template”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-an-image-to-use-the-cloud-init-template "12.13. Preparing an image to use the cloud-init template").
- Port and firewall settings are configured to open any necessary connections. Because of the `cloud-init` service, the virtual machine always calls back to Satellite even if you register the virtual machine to Capsule. For more information, see [Satellite Server port and firewall requirements](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#satellite-port-and-firewall-requirements) in *Overview, concepts, and deployment considerations* and [Capsule port and firewall requirements](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#capsule-port-and-firewall-requirements) in *Overview, concepts, and deployment considerations*.
- If you want to use Capsule Servers instead of your Satellite Server, ensure that you have configured your Capsule Servers accordingly.

  > **Important**
  >
  > It is essential to add your Capsule Server to the list of trusted proxies on Satellite Server!

  For more information, see [Configuring Capsule Server for host registration and provisioning](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-capsule-server-for-host-registration-and-provisioning) in *Installing Capsule Server*.
- You have backups of the following configuration files:

  - `/etc/cloud/cloud.cfg.d/01_network.cfg`
  - `/etc/cloud/cloud.cfg.d/10_datasource.cfg`
  - `/etc/cloud/cloud.cfg`

**Procedure**

1. On the virtual machine that you use to create the image, install the required packages:

   ```
   # dnf install cloud-init open-vm-tools perl-interpreter perl-File-Temp
   ```

   On Red Hat Enterprise Linux 9, you also require the `dbus-tools` package for network connectivity.
2. Disable network configuration by `cloud-init`:

   ```
   # cat << EOM > /etc/cloud/cloud.cfg.d/01_network.cfg
   network:
     config: disabled
   EOM
   ```
3. Configure `cloud-init` to fetch data from Satellite:

   ```
   # cat << EOM > /etc/cloud/cloud.cfg.d/10_datasource.cfg
   datasource_list: [NoCloud]
   datasource:
     NoCloud:
       seedfrom: https://satellite.example.com/userdata/
   EOM
   ```

   If you intend to provision through Capsule Server, use the URL of your Capsule Server in the `seedfrom` option, such as `https://capsule.example.com:9090/userdata/`.
4. Configure modules to use in `cloud-init`:

   ```
   # cat << EOM > /etc/cloud/cloud.cfg
   cloud_init_modules:
    - bootcmd
    - ssh

   cloud_config_modules:
    - set_passwords
    - runcmd

   cloud_final_modules:
    - scripts-per-once
    - scripts-per-boot
    - scripts-per-instance
    - scripts-user
    - phone-home

   system_info:
     distro: rhel
     paths:
       cloud_dir: /var/lib/cloud
       templates_dir: /etc/cloud/templates
     ssh_svcname: sshd
   EOM
   ```
5. Download the `katello-server-ca.crt` file from Satellite Server:

   ```
   # wget -O /etc/pki/ca-trust/source/anchors/cloud-init-ca.crt https://satellite.example.com/pub/katello-server-ca.crt
   ```

   If you intend to provision through Capsule Server, download the file from your Capsule Server, such as `https://capsule.example.com/pub/katello-server-ca.crt`.
6. Update the record of certificates:

   ```
   # update-ca-trust extract
   ```
7. Stop the `rsyslog` and `auditd` services:

   ```
   # systemctl stop rsyslog
   # systemctl stop auditd
   ```
8. Clean packages on the image:

   - On Red Hat Enterprise Linux 8 and later:

     ```
     # dnf remove --oldinstallonly
     ```
   - On Red Hat Enterprise Linux 7 and earlier:

     ```
     # package-cleanup --oldkernels --count=1
     # dnf clean all
     ```
9. Reduce logspace, remove old logs, and truncate logs:

   ```
   # logrotate -f /etc/logrotate.conf
   # rm -f /var/log/*-???????? /var/log/*.gz
   # rm -f /var/log/dmesg.old
   # rm -rf /var/log/anaconda
   # cat /dev/null > /var/log/audit/audit.log
   # cat /dev/null > /var/log/wtmp
   # cat /dev/null > /var/log/lastlog
   # cat /dev/null > /var/log/grubby
   ```
10. Remove `udev` hardware rules:

    ```
    # rm -f /etc/udev/rules.d/70*
    ```
11. Remove the `ifcfg` scripts related to existing network configurations:

    ```
    # rm -f /etc/sysconfig/network-scripts/ifcfg-ens*
    # rm -f /etc/sysconfig/network-scripts/ifcfg-eth*
    ```
12. Remove the SSH host keys:

    ```
    # rm -f /etc/ssh/ssh_host_*
    ```
13. Remove root user’s SSH history:

    ```
    # rm -rf ~root/.ssh/known_hosts
    ```
14. Remove root user’s shell history:

    ```
    # rm -f ~root/.bash_history
    # unset HISTFILE
    ```
15. Create an image from this virtual machine.
16. [Add your image to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#adding-vmware-images-to-server-by-using-cli_provisioning "12.6. Adding VMware images to Satellite Server by using Hammer CLI").

## 12.15. Deleting a virtual machine on VMware

You can delete virtual machines (VMs) running on VMware from within Satellite.

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select your VMware provider.
3. On the **Virtual Machines** tab, click **Delete** from the **Actions** menu. This deletes the virtual machine from the VMware compute resource while retaining any associated hosts within Satellite. If you want to delete the orphaned host, navigate to **Hosts** > **All Hosts** and delete the host manually.

## 12.16. Importing a virtual machine from VMware into Satellite

You can import existing virtual machines running on VMware into Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select your VMware compute resource.
3. On the **Virtual Machines** tab, click **Import as managed Host** or **Import as unmanaged Host** from the **Actions** menu. The following page looks identical to creating a host with the compute resource being already selected.
4. Click **Submit** to import the virtual machine into Satellite.

## 12.17. Caching of compute resources

Caching of compute resources speeds up rendering of VMware information.

### 12.17.1. Enabling caching of compute resources

You can enable and disable caching of compute resources in the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Click the **Edit** button to the right of the VMware server you want to update.
3. Select the **Enable caching** checkbox.

### 12.17.2. Refreshing the compute resources cache by using Satellite web UI

Refresh the cache of compute resources to update compute resources information.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select a VMware server you want to refresh the compute resources cache for and click **Refresh Cache**.

### 12.17.3. Refreshing the compute resources cache by using Hammer CLI

Refresh the cache of compute resources to update compute resources information.

**Procedure**

- Use this API call to refresh the compute resources cache:

  ```
  $ curl \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request PUT \
  --user "My_User_Name:My_Password" \
  https://satellite.example.com/api/compute_resources/compute_resource_id/refresh_cache
  ```

  Use `hammer compute-resource list` to determine the ID of the VMware server you want to refresh the compute resources cache for.
