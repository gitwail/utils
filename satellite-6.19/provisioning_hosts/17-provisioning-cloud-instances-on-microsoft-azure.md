---
title: "Provisioning cloud instances on Microsoft Azure"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "17"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-cloud-instances-on-microsoft-azure"
---
# Chapter 17. Provisioning cloud instances on Microsoft Azure

You can create virtual machines and control their power management states on Microsoft Azure by using image-based provisioning. You can provision from Marketplace images, custom images, and shared image galleries.

## 17.1. Prerequisites for Microsoft Azure provisioning

Before you can provision cloud instances on Microsoft Azure, ensure that your environment meets the following requirements.

- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.
- Ensure that you have the correct permissions to create an Azure Active Directory application. For more information, see [Check Azure AD permissions](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal#required-permissions) in the *Microsoft identity platform (Azure Active Directory for developers)* documentation.
- You must create and configure an Azure Active Directory application and service principle to obtain Application or *client* ID, Directory or *tenant* ID, and Client Secret. For more information, see [Use the portal to create an Azure AD application and service principal that can access resources](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal) in the *Microsoft identity platform (Azure Active Directory for developers)* documentation.
- Optional: If you want to use Puppet with Azure hosts, navigate to **Administer** > **Settings** > **Puppet** and enable the `Use UUID for certificates` setting to configure Puppet to use consistent Puppet certificate IDs.
- Based on your needs, associate a `finish` or `user_data` provisioning template with the operating system you want to use. For more information about provisioning templates, see [Provisioning Templates](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-templates).
- Optional: If you want the virtual machine to use a static private IP address, create a subnet in Satellite with the **Network Address** field matching the Azure subnet address.
- Before creating Red Hat Enterprise Linux BYOS images, you must accept the image terms either in the Azure CLI or Portal so that the image can be used to create and manage virtual machines for your subscription.

**Additional resources**

- [Azure Resource Manager documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/)

## 17.2. Adding a Microsoft Azure connection by using Satellite web UI

Add Microsoft Azure as a compute resource to provision and manage hosts on Azure. Note that you must add a separate compute resource for each Microsoft Azure region that you want to use.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Click **Create Compute Resource**.
3. In the **Name** field, enter a name for the compute resource.
4. From the **Provider** list, select **Azure Resource Manager**.
5. Optional: In the **Description** field, enter a description for the resource.
6. By default, the **Cloud** is set to Public/Standard. Azure Government Cloud supports the following regions:

   - US Government
   - China
   - Germany
7. In the **Client ID** field, enter your Application or *client* ID.
8. In the **Client Secret** field, enter your client secret.
9. In the **Subscription ID** field, enter your subscription ID.
10. In the **Tenant ID** field, enter your Directory or *tenant* ID.
11. Click **Load Regions**. This tests if your connection to Azure Resource Manager is successful and loads the regions available in your subscription.
12. From the **Azure Region** list, select the Azure region to use.
13. Click **Submit**.

## 17.3. Adding a Microsoft Azure connection to Satellite Server by using Hammer CLI

Add Microsoft Azure as a compute resource to provision and manage hosts on Azure. Note that you must add a separate compute resource for each Microsoft Azure region that you want to use.

**Procedure**

- Add an Azure compute resource to Satellite:

  ```
  $ hammer compute-resource create \
  --app-ident My_Client_ID \
  --name My_Compute_Resource_Name \
  --provider azurerm \
  --region "My_Region" \
  --secret-key My_Client_Secret \
  --sub-id My_Subscription_ID \
  --tenant My_Tenant_ID
  ```

  Note that the value for the `--region` option must be in lowercase and must not contain special characters.

  > **Important**
  >
  > If you are using Azure Government Cloud then you must pass in the `--cloud` parameter. The values for the `cloud` parameter are:
  >
  > | Name of Azure Government Cloud | Value for hammer --cloud |
  > | --- | --- |
  > | US Government | azureusgovernment |
  > | China | azurechina |
  > | Germany | azuregermancloud |

## 17.4. Adding Microsoft Azure images to Satellite by using Satellite web UI

To create hosts using image-based provisioning, you must add information about the image, such as access details and the image location, to your Satellite Server.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Click the name of the Microsoft Azure connection.
3. Click **Create Image**.
4. In the **Name** field, enter a name for the image.
5. From the **Operating System** list, select the base operating system of the image.
6. From the **Architecture** list, select the operating system architecture.
7. In the **Username** field, enter the SSH user name for image access. You cannot use the `root` user.
8. Optional: In the **Password** field, enter a password to authenticate with.
9. In the **Azure Image Name** field, enter an image name in the format `prefix://UUID`.

   - For a custom image, use the prefix `custom`. For example, **custom://image-name**.
   - For a shared gallery image, use the prefix `gallery`. For example, **gallery://Templates/image-name**.
   - For public and RHEL Bring Your Own Subscription (BYOS) images, use the prefix `marketplace`. For example, **marketplace://OpenLogicCentOS:7.5:latest**.

     For more information, see [Find Linux VM images in the Azure Marketplace with the Azure CLI](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage).
10. Optional: Select the **User Data** checkbox if the image supports user data input, such as `cloud-init` data.
11. Click **Submit** to save the image details.

## 17.5. Adding Microsoft Azure images to Satellite by using Hammer CLI

To create hosts using image-based provisioning, you must add information about the image, such as access details and the image location, to your Satellite Server.

**Procedure**

- Create the image: Note that the username that you enter for the image must be the same that you use when you create a host with this image. The `--password` option is optional when creating an image. You cannot use the `root` user.

  ```
  $ hammer compute-resource image create \
  --name Azure_image_name \
  --compute-resource azure_cr_name \
  --uuid 'marketplace://RedHat:RHEL:7-RAW:latest' \
  --username 'azure_username' \
  --user-data no
  ```

## 17.6. Adding Microsoft Azure details to a compute profile by using Satellite web UI

You can create custom compute profiles to bundle Microsoft Azure hardware settings, for example, CPU cores, memory, and storage details. When you create a host on Microsoft Azure using this compute profile, these settings are automatically populated.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Profiles**.
2. In the Compute Profiles window, click the name of an existing compute profile, or click **Create Compute Profile**, enter a **Name**, and click **Submit**.
3. Click the name of the Azure compute resource.
4. From the **Resource group** list, select the resource group to provision to.
5. From the **VM Size** list, select a size of a virtual machine to provision.
6. From the **Platform** list, select **Linux**.
7. In the **Username** field, enter a user name to authenticate with. Note that the username that you enter for compute profile must be the same that you use when creating an image.
8. To authenticate the user, use one of the following options:

   - To authenticate using a password, enter a password in the **Password** field.
   - To authenticate using an SSH key, enter an SSH key in the **SSH Key** field.
9. Optional: If you want the virtual machine to use a premium virtual machine disk, select the **Premium OS Disk** checkbox.
10. From the **OS Disk Caching** list, select the disc caching setting.
11. Optional: In the **Custom Script Command** field, enter commands to perform on the virtual machine when the virtual machine is provisioned.
12. Optional: If you want to run custom scripts when provisioning finishes, in the **Comma separated file URIs** field, enter comma-separated file URIs of scripts to use. The scripts must contain `sudo` at the beginning because Red Hat Satellite downloads files to the `/var/lib/waagent/custom-script/download/0/` directory on the host and scripts require sudo privileges to be executed.
13. Optional: You can add a **NVIDIA Driver** by selecting the **NVIDIA driver / CUDA** checkbox. For more information, refer to the following Microsoft Azure documentation:

    - [NVIDIA GPU Driver Extension for Linux](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/hpccompute-gpu-linux)
    - [NVIDIA GPU Driver Extension for Windows](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/hpccompute-gpu-windows)
14. Optional: If you want to create an additional volume on the VM, click the **Add Volume** button, enter the **Size** in GB and select the **Data Disk Caching** method.

    - Note that the maximum number of these disks depends on the VM Size selected. For more information on Microsoft Azure VM storage requirements, see the [Microsoft Azure documentation](https://docs.microsoft.com/en-us/azure/virtual-machines).
15. Click **Add Interface**.

    > **Important**
    >
    > The maximum number of interfaces depends on the VM Size selected. For more information, see the Microsoft Azure documentation link above.
16. From the **Azure Subnet** list, select the Azure subnet to provision to.
17. From the **Public IP** list, select the public IP setting.
18. Optional: If you want the virtual machine to use a static private IP, select the **Static Private IP** checkbox.
19. Click **Submit**.

## 17.7. Adding Microsoft Azure details to a compute profile by using Hammer CLI

You can create custom compute profiles to bundle Microsoft Azure hardware settings, for example, CPU cores, memory, and storage details. When you create a host on Microsoft Azure using this compute profile, these settings are automatically populated.

**Procedure**

1. Create a compute profile to use with Microsoft Azure:

   ```
   $ hammer compute-profile create --name compute_profile_name
   ```
2. Add Microsoft Azure details to the compute profile. With the `username` setting, enter the SSH user name for image access. Note that the username that you enter for compute profile must be the same that you use when creating an image.

   ```
   $ hammer compute-profile values create \
   --compute-attributes="resource_group=resource_group,vm_size=Standard_B1s,username=azure_user,password=azure_password,platform=Linux,script_command=touch /var/tmp/text.txt" \
   --compute-profile "compute_profile_name" \
   --compute-resource azure_cr_name \
   --interface="compute_public_ip=Dynamic,compute_network=mysubnetID,compute_private_ip=false" \
   --volume="disk_size_gb=5,data_disk_caching=None"
   ```

   Optional: If you want to run scripts on the virtual machine after provisioning, specify the following settings:

   - To enter the script directly, with the `script_command` setting, enter a command to be executed on the provisioned virtual machine.
   - To run a script from a URI, with the `script_uris` setting, enter comma-separated file URIs of scripts to use. The scripts must contain `sudo` at the beginning because Red Hat Satellite downloads files to the `/var/lib/waagent/custom-script/download/0/` directory on the host and therefore scripts require sudo privileges to be executed.

## 17.8. Creating image-based hosts on Microsoft Azure by using Satellite web UI

In Satellite, you can use Microsoft Azure provisioning to create hosts from an existing image. The new host entry triggers the Microsoft Azure server to create the instance using the pre-existing image as a basis for the new volume.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. From the **Deploy on** list, select the Microsoft Azure connection.
7. From the **Compute Profile** list, select a profile to use to automatically populate virtual machine settings.
8. From the **Lifecycle Environment** list, select the environment.
9. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
10. Verify that the fields are populated with values. Note in particular:

    - Satellite automatically assigns an IP address for the new host.
    - Ensure that the **MAC address** field is blank. Microsoft Azure assigns a MAC address to the host during provisioning.
    - The **Name** from the **Host** tab becomes the **DNS name**.
    - The **Azure Subnet** field is populated with the required Azure subnet.
    - Optional: If you want to use a static private IP address, from the **IPv4 Subnet** list select the Satellite subnet with the **Network Address** field matching the Azure subnet address. In the **IPv4 Address** field, enter an IPv4 address within the range of your Azure subnet.
    - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
11. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

    For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
12. Click the **Operating System** tab, and confirm that all fields automatically contain values.
13. For **Provisioning Method**, ensure **Image Based** is selected.
14. From the **Image** list, select the Microsoft Azure image that you want to use for provisioning.
15. In the **Root Password** field, enter the root password to authenticate with.
16. Click **Resolve** in **Provisioning templates** to check the new host can identify the right provisioning templates to use.
17. Click the **Virtual Machine** tab and confirm that these settings are populated with details from the host group and compute profile. Modify these settings to suit your needs.
18. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
19. Click **Submit** to save the host entry.

## 17.9. Creating image-based hosts on Microsoft Azure by using Hammer CLI

In Satellite, you can use Microsoft Azure provisioning to create hosts from an existing image. The new host entry triggers the Microsoft Azure server to create the instance using the pre-existing image as a basis for the new volume.

For more information about additional host creation parameters for this compute resource, enter the `hammer host create --help` command.

**Procedure**

- Create the host with the `hammer host create` command and include `--provision-method image`. Replace the values in the following example with the appropriate values for your environment.

  ```
  $ hammer host create \
  --architecture x86_64 \
  --compute-profile "My_Compute_Profile" \
  --compute-resource "My_Compute_Resource" \
  --domain "My_Domain" \
  --image "My_Azure_Image" \
  --location "My_Location" \
  --name "My_Host_Name" \
  --operatingsystem "My_Operating_System" \
  --organization "My_Organization" \
  --provision-method "image"
  ```

## 17.10. Deleting a virtual machine on Microsoft Azure

You can delete virtual machines (VMs) running on Microsoft Azure from within Satellite.

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select your Microsoft Azure provider.
3. On the **Virtual Machines** tab, click **Delete** from the **Actions** menu. This deletes the virtual machine from the Microsoft Azure compute resource while retaining any associated hosts within Satellite. If you want to delete the orphaned host, navigate to **Hosts** > **All Hosts** and delete the host manually.
