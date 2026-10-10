---
title: "Provisioning virtual machines on KVM"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "11"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-virtual-machines-on-kvm"
---
# Chapter 11. Provisioning virtual machines on KVM

You can provision hosts and control virtualization functions by using the `libvirt` API on the KVM hypervisor.

Only Virtual Machines created through Satellite can be managed. Virtual Machines with other than directory storage pool types are unsupported.

You can use KVM provisioning to create hosts over a network connection or from an existing image.

Before you provision virtual machines on KVM, ensure that your environment meets the following requirements:

- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.
- A Capsule Server managing a network on the KVM server. Ensure no other DHCP services run on this network to avoid conflicts with Capsule Server.
- A Red Hat Enterprise Linux server running KVM virtualization tools (libvirt daemon).
- An existing virtual machine image if you want to use image-based provisioning. Ensure that this image exists in a storage pool on the KVM host. The `default` storage pool is usually located in `/var/lib/libvirt/images`. Only directory pool storage types can be managed through Satellite.
- Optional: The examples in these procedures use the root user for KVM. If you want to use a non-root user on the KVM server, you must add the user to the `libvirt` group on the KVM server:

  ```
  # usermod -a -G libvirt non_root_user
  ```
- Ensure the provisioning user has the required permissions to provision hosts.

**Additional resources**

- [Chapter 2, *Preparing networking for host management*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management "Chapter 2. Preparing networking for host management")
- [*Red Hat Enterprise Linux 8 Configuring and managing virtualization*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/configuring_and_managing_virtualization/index)
- [Appendix D, *Permissions required to provision hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#permissions-required-to-provision-hosts "Appendix D. Permissions required to provision hosts")

## 11.1. Configuring Satellite Server for KVM connections

Before adding the KVM connection, create an SSH key pair for the `foreman` user to ensure a secure connection between Satellite Server and KVM.

**Procedure**

1. On your Satellite Server, switch to the `foreman` user:

   ```
   # su foreman -s /bin/bash
   ```
2. Generate the key pair:

   ```
   $ ssh-keygen
   ```
3. Copy the public key to the KVM server:

   ```
   $ ssh-copy-id root@kvm.example.com
   ```
4. Exit the bash shell for the `foreman` user:

   ```
   $ exit
   ```
5. Install the `libvirt-client` package:

   ```
   # satellite-maintain packages install libvirt-client
   ```

**Verification**

- On your Satellite Server, test the connection to the KVM server:

  ```
  # su foreman -s /bin/bash -c 'virsh -c qemu+ssh://root@kvm.example.com/system list'
  ```

## 11.2. Adding a KVM connection to Satellite Server by using Satellite web UI

To provision and manage virtual machines on KVM (libvirt), add KVM as a compute resource to Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources** and click **Create Compute Resource**.
2. In the **Name** field, enter a name for the new compute resource.
3. From the **Provider** list, select **Libvirt**.
4. In the **Description** field, enter a description for the compute resource.
5. In the **URL** field, enter the connection URL to the KVM server. For example:

   ```
    qemu+ssh://root@kvm.example.com/system
   ```
6. From the **Display type** list, select either **VNC** or **Spice**.
7. Optional: To secure console access for new hosts with a randomly generated password, select the **Set a randomly generated password on the display connection** checkbox. You can retrieve the password for the VNC console to access the guest virtual machine console on your KVM server:

   ```
   # virsh edit your_VM_name
   <graphics type='vnc' port='-1' autoport='yes' listen='0.0.0.0' passwd='your_randomly_generated_password'>
   ```

   The password is randomly generated every time the console for the virtual machine is opened, for example, with virt-manager.
8. Click **Test Connection** to ensure that Satellite Server connects to the KVM server without fault.
9. Verify that the **Locations** and **Organizations** tabs are automatically set to your current context. If you want, add additional contexts to these tabs.
10. Click **Submit** to save the KVM connection.

## 11.3. Adding a KVM connection to Satellite Server by using Hammer CLI

To provision and manage virtual machines on KVM (libvirt), add KVM as a compute resource to Satellite.

**Procedure**

- Create a compute resource:

  ```
  $ hammer compute-resource create --name "My_KVM_Server" \
  --provider "Libvirt" --description "KVM server at kvm.example.com" \
  --url "qemu+ssh://root@kvm.example.com/system" --locations "New York" \
  --organizations "My_Organization"
  ```

## 11.4. Adding KVM images to Satellite by using Satellite web UI

To create hosts using image-based provisioning, you must add information about the image, such as access details and the image location, to your Satellite Server.

Note that you can manage only directory pool storage types through Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Click the name of the KVM connection.
3. Click **Create Image**.
4. In the **Name** field, enter a name for the image.
5. From the **Operating System** list, select the base operating system of the image.
6. From the **Architecture** list, select the operating system architecture.
7. In the **Username** field, enter the SSH user name for image access. This is normally the `root` user.
8. In the **Password** field, enter the SSH password for image access.
9. In the **Image path** field, enter the full path that points to the image on the KVM server. For example:

   ```
    /var/lib/libvirt/images/TestImage.qcow2
   ```
10. Optional: Select the **User Data** checkbox if the image supports user data input, such as `cloud-init` data.
11. Click **Submit** to save the image details.

## 11.5. Adding KVM images to Satellite by using Hammer CLI

To create hosts using image-based provisioning, you must add information about the image, such as access details and the image location, to your Satellite Server.

> **Note**
>
> You can manage only directory pool storage types through Satellite.

**Procedure**

- Create the image: Use the `--uuid` field to store the full path of the image location on the KVM server.

  ```
  $ hammer compute-resource image create \
  --name "KVM Image" \
  --compute-resource "My_KVM_Server"
  --operatingsystem "RedHat version" \
  --architecture "x86_64" \
  --username root \
  --user-data false \
  --uuid "/var/lib/libvirt/images/KVMimage.qcow2" \
  ```

## 11.6. Adding KVM details to a compute profile by using Satellite web UI

You can create standardized virtual machines more quickly and efficiently by adding KVM hardware settings to a compute profile. When you create a host on KVM using this compute profile, these settings are automatically populated.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Profiles**.
2. In the Compute Profiles window, click the name of an existing compute profile, or click **Create Compute Profile**, enter a **Name**, and click **Submit**.
3. Click the name of the KVM compute resource.
4. In the **CPUs** field, enter the number of CPUs to allocate to the new host.
5. In the **Memory** field, enter the amount of memory to allocate to the new host.
6. From the **Image** list, select the image to use if performing image-based provisioning.
7. From the **Network Interfaces** list, select the network parameters for the host’s network interface. You can create multiple network interfaces. However, at least one interface must point to a Capsule-managed network.
8. In the **Storage** area, enter the storage parameters for the host. You can create multiple volumes for the host.
9. Click **Submit** to save the settings to the compute profile.

## 11.7. Adding KVM details to a compute profile by using Hammer CLI

You can create standardized virtual machines more quickly and efficiently by adding KVM hardware settings to a compute profile. When you create a host on KVM using this compute profile, these settings are automatically populated.

**Procedure**

1. Create a compute profile:

   ```
   $ hammer compute-profile create --name "My_Libvirt_Compute_Profile"
   ```
2. Add values to your compute profile:

   ```
   $ hammer compute-profile values create \
   --compute-attributes "cpus=1,memory=1073741824" \
   --compute-profile "My_Libvirt_Compute_Profile" \
   --compute-resource "My_KVM_Server" \
   --interface "compute_type=network,compute_model=virtio,compute_network=examplenetwork" \
   --volume "pool_name=default,capacity=20G,format_type=qcow2"
   ```

## 11.8. Creating hosts on KVM by using Satellite web UI

In Satellite, you can use network or image-based provisioning to create hosts on KVM.

**Prerequisites**

- For network-based provisioning, if you use a virtual network on the KVM server for provisioning, select a network that does not provide DHCP assignments. This causes DHCP conflicts with Satellite Server when booting new hosts.
- If you want to create a host over a network connection, the new host must be able to access your Satellite Server or Capsule Servers on a KVM virtual network, so that the host has access to PXE provisioning services. This new host entry triggers the KVM server to create and start a virtual machine. If the virtual machine detects the defined Capsule Server through the virtual network, the virtual machine boots to PXE and begins to install the chosen operating system.
- If you want to create a host with an existing image, the new host entry triggers the KVM server to create the virtual machine using a pre-existing image as a basis for the new volume.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. From the **Deploy on** list, select the KVM connection.
7. From the **Compute Profile** list, select a profile to use to automatically populate virtual machine settings. The KVM-specific fields are populated with settings from your compute profile. Modify these settings if required.
8. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
9. Verify that the fields are populated with values. Note in particular:

   - Satellite automatically assigns an IP address for the new host.
   - Ensure that the **MAC address** field is blank. KVM assigns a MAC address to the host during provisioning.
   - The **Name** from the **Host** tab becomes the **DNS name**.
   - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
10. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

    For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
11. Click the **Operating System** tab, and confirm that all fields automatically contain values.
12. Select the **Provisioning Method** that you want to use:

    - For network-based provisioning, click **Network Based**.
    - For image-based provisioning, click **Image Based**.
13. Click **Resolve** in **Provisioning templates** to check the new host can identify the right provisioning templates to use.
14. Click the **Virtual Machine** tab and confirm that these settings are populated with details from the host group and compute profile. Modify these settings to suit your needs.

    If you want to provision a Secure Boot-enabled host, select **UEFI Secure Boot** in the **Firmware** field.
15. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
16. Click **Submit** to save the host entry.

## 11.9. Creating hosts on KVM by using Hammer CLI

In Satellite, you can use KVM provisioning to create hosts over a network connection or from an existing image.

For more information about additional host creation parameters for this compute resource, enter the `hammer host create --help` command.

**Prerequisites**

- For network-based provisioning, if you use a virtual network on the KVM server for provisioning, select a network that does not provide DHCP assignments. This causes DHCP conflicts with Satellite Server when booting new hosts.
- If you want to create a host over a network connection, the new host must be able to access your Satellite Server or Capsule Servers on a KVM virtual network, so that the host has access to PXE provisioning services. This new host entry triggers the KVM server to create and start a virtual machine. If the virtual machine detects the defined Capsule Server through the virtual network, the virtual machine boots to PXE and begins to install the chosen operating system.
- If you want to create a host with an existing image, the new host entry triggers the KVM server to create the virtual machine using a pre-existing image as a basis for the new volume.

**Procedure**

- Create a host by using one of the following methods:

  - To use network-based provisioning, create the host with the `hammer host create` command and include `--provision-method build`. Replace the values in the following example with the appropriate values for your environment.

    ```
    $ hammer host create \
    --build true \
    --compute-attributes="cpus=1,memory=1073741824" \
    --compute-resource "My_KVM_Server" \
    --enabled true \
    --hostgroup "My_Host_Group" \
    --interface "managed=true,primary=true,provision=true,compute_type=network,compute_network=examplenetwork" \
    --location "My_Location" \
    --managed true \
    --name "My_Host_Name" \
    --organization "My_Organization" \
    --provision-method "build" \
    --root-password "My_Password" \
    --volume="pool_name=default,capacity=20G,format_type=qcow2"
    ```
  - To use image-based provisioning, create the host with the `hammer host create` command and include `--provision-method image`. Replace the values in the following example with the appropriate values for your environment.

    ```
    $ hammer host create \
    --compute-attributes="cpus=1,memory=1073741824" \
    --compute-resource "My_KVM_Server" \
    --enabled true \
    --hostgroup "My_Host_Group" \
    --image "My_KVM_Image" \
    --interface "managed=true,primary=true,provision=true,compute_type=network,compute_network=examplenetwork" \
    --location "My_Location" \
    --managed true \
    --name "My_Host_Name" \
    --organization "My_Organization" \
    --provision-method "image" \
    --volume="pool_name=default,capacity=20G,format_type=qcow2"
    ```

## 11.10. Deleting a virtual machine on KVM

You can delete virtual machines (VMs) running on KVM from within Satellite.

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select your KVM provider.
3. On the **Virtual Machines** tab, click **Delete** from the **Actions** menu. This deletes the virtual machine from the KVM compute resource while retaining any associated hosts within Satellite. If you want to delete the orphaned host, navigate to **Hosts** > **All Hosts** and delete the host manually.
