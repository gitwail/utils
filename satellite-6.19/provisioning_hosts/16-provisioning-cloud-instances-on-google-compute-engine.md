---
title: "Provisioning cloud instances on Google Compute Engine"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "16"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-cloud-instances-on-google-compute-engine"
---
# Chapter 16. Provisioning cloud instances on Google Compute Engine

You can create and manage virtual machines on Google Compute Engine (GCE) by using Satellite.

You can only use golden images supported by Red Hat with Satellite for creating GCE hosts.

## 16.1. Prerequisites for Google Compute Engine provisioning

Before you can provision cloud instances on Google Compute Engine (GCE), ensure that your environment meets the following requirements.

- Configure a domain and subnet on Satellite. For more information about networking requirements, see [Chapter 2, *Preparing networking for host management*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management "Chapter 2. Preparing networking for host management").
- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.
- In your GCE project, configure a service account with the necessary IAM Compute role. For more information, see [Compute Engine IAM roles](https://cloud.google.com/compute/docs/access/iam) in the GCE documentation.
- In your GCE project-wise metadata, set the `enable-oslogin` to `FALSE`. For more information, see [Enabling or disabling OS Login](https://cloud.google.com/compute/docs/instances/managing-instance-access#enable_oslogin) in the GCE documentation.
- Optional: If you want to use Puppet with GCE hosts, navigate to **Administer** > **Settings** > **Puppet** and enable the `Use UUID for certificates` setting to configure Puppet to use consistent Puppet certificate IDs.
- Based on your needs, associate a `finish` or `user_data` provisioning template with the operating system you want to use. For more information, see [Provisioning Templates](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-templates) in *Provisioning hosts*.

## 16.2. Adding a GCE connection to Satellite Server by using Satellite web UI

Add Google Compute Engine (GCE) as a compute resource to provision and manage hosts on GCE.

**Procedure**

1. In GCE, generate a service account key in JSON format. For more information, see [Create and manage service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) in the GCE documentation.
2. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources** and click **Create Compute Resource**.
3. In the **Name** field, enter a name for the compute resource.
4. From the **Provider** list, select **Google**.
5. Optional: In the **Description** field, enter a description for the resource.
6. In the **JSON key** field, click **Choose File** and locate your service account key for upload from your local machine.
7. Click **Load Zones** to populate the list of zones from your GCE environment.
8. From the **Zone** list, select the GCE zone to use.
9. Click **Submit**.

## 16.3. Adding a GCE connection to Satellite Server by using Hammer CLI

Add Google Compute Engine (GCE) as a compute resource to provision and manage hosts on GCE.

**Procedure**

1. In GCE, generate a service account key in JSON format. For more information, see [Create and manage service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) in the GCE documentation.
2. Use the `hammer compute-resource create` command to add a GCE compute resource to Satellite:

   ```
   # hammer compute-resource create \
   --key-path "My_GCE_Key.json" \
   --name "My_GCE_Compute_Resource" \
   --provider "gce" \
   --zone "My_Zone"
   ```

## 16.4. Adding Google Compute Engine images to Satellite by using Satellite web UI

To create hosts using image-based provisioning, you must add information about the image, such as access details and the image location, to your Satellite Server.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Click the name of the Google Compute Engine connection.
3. Click **Create Image**.
4. In the **Name** field, enter a name for the image.
5. From the **Operating System** list, select the base operating system of the image.
6. From the **Architecture** list, select the operating system architecture.
7. In the **Username** field, enter the SSH user name for image access. Specify a user other than `root`, because the `root` user cannot connect to a GCE instance using SSH keys. The username must begin with a letter and consist of lowercase letters and numbers.
8. From the **Image** list, select an image from the Google Compute Engine compute resource.
9. Optional: Select the **User Data** checkbox if the image supports user data input, such as `cloud-init` data.
10. Click **Submit** to save the image details.

## 16.5. Adding Google Compute Engine images to Satellite by using Hammer CLI

To create hosts using image-based provisioning, you must add information about the image, such as access details and the image location, to your Satellite Server.

**Procedure**

- Create the image: With the `--username` option, specify a user other than `root`, because the `root` user cannot connect to a GCE instance using SSH keys. The username must begin with a letter and consist of lowercase letters and numbers.

  ```
  $ hammer compute-resource image create \
  --name 'gce_image_name' \
  --compute-resource 'gce_cr' \
  --operatingsystem-id 1 \
  --architecture-id 1 \
  --uuid '3780108136525169178' \
  --username 'admin'
  ```

## 16.6. Adding GCE details to a compute profile by using Satellite web UI

You can add Google Compute Engine (GCE) hardware settings to a compute profile. When you create a host on GCE using this compute profile, these settings are automatically populated.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Profiles**.
2. In the Compute Profiles window, click the name of an existing compute profile, or click **Create Compute Profile**, enter a **Name**, and click **Submit**.
3. Click the name of the GCE compute resource.
4. From the **Machine Type** list, select the machine type to use for provisioning.
5. From the **Image** list, select the image to use for provisioning.
6. From the **Network** list, select the GCE network to use for provisioning.
7. Optional: Select the **Associate Ephemeral External IP** checkbox to assign a dynamic ephemeral IP address that Satellite uses to communicate with the host. This public IP address changes when you reboot the host. If you need a permanent IP address, reserve a static public IP address on GCE and attach it to the host.
8. In the **Size (GB)** field, enter the size of the storage to create on the host.
9. Click **Submit** to save the compute profile.

## 16.7. Adding GCE details to a compute profile by using Hammer CLI

You can add Google Compute Engine (GCE) hardware settings to a compute profile. When you create a host on GCE using this compute profile, these settings are automatically populated.

**Procedure**

1. Create a compute profile to use with the GCE compute resource:

   ```
   $ hammer compute-profile create --name My_GCE_Compute_Profile
   ```
2. Add GCE details to the compute profile:

   ```
   $ hammer compute-profile values create \
   --compute-attributes "machine_type=f1-micro,associate_external_ip=true,network=default" \
   --compute-profile "My_GCE_Compute_Profile" \
   --compute-resource "My_GCE_Compute_Resource" \
   --volume "size_gb=20"
   ```

## 16.8. Creating image-based hosts on Google Compute Engine by using Satellite web UI

In Satellite, you can use Google Compute Engine provisioning to create hosts from an existing image. The new host entry triggers the Google Compute Engine server to create the instance using the pre-existing image as a basis for the new volume.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. From the **Deploy on** list, select the Google Compute Engine connection.
7. From the **Compute Profile** list, select a profile to use to automatically populate virtual machine settings.
8. From the **Lifecycle Environment** list, select the environment.
9. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
10. Verify that the fields are populated with values. Note in particular:

    - Satellite automatically assigns an IP address for the new host.
    - Ensure that the **MAC address** field is blank. Google Compute Engine assigns a MAC address to the host during provisioning.
    - The **Name** from the **Host** tab becomes the **DNS name**.
    - The **Domain** field is populated with the required domain.
    - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
11. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

    For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
12. Click the **Operating System** tab, and confirm that all fields automatically contain values.
13. Click **Resolve** in **Provisioning templates** to check the new host can identify the right provisioning templates to use.
14. Click the **Virtual Machine** tab and confirm that these settings are populated with details from the host group and compute profile. Modify these settings to suit your needs.
15. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
16. Click **Submit** to save the host entry.

## 16.9. Creating image-based hosts on Google Compute Engine by using Hammer CLI

In Satellite, you can use Google Compute Engine provisioning to create hosts from an existing image. The new host entry triggers the Google Compute Engine server to create the instance using the pre-existing image as a basis for the new volume.

For more information about additional host creation parameters for this compute resource, enter the `hammer host create --help` command.

**Procedure**

- Create the host with the `hammer host create` command and include `--provision-method image`. Replace the values in the following example with the appropriate values for your environment.

  ```
  $ hammer host create \
  --architecture x86_64 \
  --compute-profile "My_Compute_Profile" \
  --compute-resource "My_Compute_Resource" \
  --image "My_GCE_Image" \
  --interface "type=interface,domain_id=1,managed=true,primary=true,provision=true" \
  --location "My_Location" \
  --name "My_Host_Name" \
  --operatingsystem "My_Operating_System" \
  --organization "My_Organization" \
  --provision-method "image" \
  --puppet-ca-proxy-id My_Puppet_CA_Proxy_ID \
  --puppet-environment-id My_Puppet_Environment_ID \
  --puppet-proxy-id My_Puppet_Proxy_ID \
  --root-password "My_Root_Password"
  ```

## 16.10. Deleting a virtual machine on Google Compute Engine

You can delete virtual machines (VMs) running on Google Compute Engine from within Satellite.

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select your Google Compute Engine provider.
3. On the **Virtual Machines** tab, click **Delete** from the **Actions** menu. This deletes the virtual machine from the Google Compute Engine compute resource while retaining any associated hosts within Satellite. If you want to delete the orphaned host, navigate to **Hosts** > **All Hosts** and delete the host manually.
