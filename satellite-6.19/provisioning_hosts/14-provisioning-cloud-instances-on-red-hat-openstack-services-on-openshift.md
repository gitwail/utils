---
title: "Provisioning cloud instances on Red Hat OpenStack Services on OpenShift"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "14"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-cloud-instances-on-red-hat-openstack-services-on-openshift"
---
# Chapter 14. Provisioning cloud instances on Red Hat OpenStack Services on OpenShift

You can use Satellite to create cloud instances and control their power management states through the Red Hat OpenStack Services on OpenShift REST API. Red Hat OpenStack Services on OpenShift is an Infrastructure-as-a-Service (IaaS) platform for building private or public clouds.

## 14.1. Prerequisites for Red Hat OpenStack Services on OpenShift provisioning

Before you can provision cloud instances on Red Hat OpenStack Services on OpenShift, ensure that your environment meets the following requirements.

- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.
- A Capsule Server managing a network in your Red Hat OpenStack Services on OpenShift environment. For more information, see [Chapter 2, *Preparing networking for host management*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management "Chapter 2. Preparing networking for host management").
- An image added to Red Hat OpenStack Services on OpenShift Image Storage (glance) service for image-based provisioning. For more information, see the [Red Hat OpenStack Services on OpenShift *Instances and Images Guide*](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/16.0/html/instances_and_images_guide/index).

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

## 14.2. Adding a Red Hat OpenStack Services on OpenShift connection to Satellite Server by using Satellite web UI

You can add Red Hat OpenStack Services on OpenShift as a compute resource to Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Click **Create Compute Resource**.
3. In the **Name** field, enter a name for the new compute resource.
4. From the **Provider** list, select **RHEL OpenStack Platform**.
5. Optional: In the **Description** field, enter a description for the compute resource.
6. In the **URL** field, enter the URL for the OpenStack Authentication keystone service’s API at the `tokens` resource, such as `http://openstack.example.com:5000/v2.0/tokens` or `http://openstack.example.com:5000/v3/auth/tokens`.
7. In the **Username** and **Password** fields, enter the user authentication for Satellite to access the environment.
8. Optional: In the **Project (Tenant) name** field, enter the name of your tenant (v2) or project (v3) for Satellite Server to manage.
9. In the **User domain** field, enter the user domain for v3 authentication.
10. In the **Project domain name** field, enter the project domain name for v3 authentication.
11. In the **Project domain ID** field, enter the project domain ID for v3 authentication.
12. Optional: Select **Allow external network as main network** to use external networks as primary networks for hosts.
13. Optional: Click **Test Connection** to verify that Satellite can connect to your compute resource.
14. Click the **Locations** and **Organizations** tabs and verify that the location and organization that you want to use are set to your current context. Add any additional contexts that you want to these tabs.
15. Click **Submit** to save the Red Hat OpenStack Services on OpenShift connection.

## 14.3. Adding a Red Hat OpenStack Services on OpenShift connection to Satellite Server by using Hammer CLI

You can add Red Hat OpenStack Services on OpenShift as a compute resource to Satellite.

**Procedure**

- Create a compute resource for Red Hat OpenStack Services on OpenShift:

  ```
  $ hammer compute-resource create --name "My_OpenStack" \
  --provider "OpenStack" \
  --description "My OpenStack environment at openstack.example.com" \
  --url "http://openstack.example.com:5000/v3/auth/tokens" \
  --user "My_Username" --password "My_Password" \
  --tenant "My_Openstack" --domain "My_User_Domain" \
  --project-domain-id "My_Project_Domain_ID" \
  --project-domain-name "My_Project_Domain_Name" \
  --locations "New York" --organizations "My_Organization"
  ```

## 14.4. Adding Red Hat OpenStack Services on OpenShift images to Satellite by using Satellite web UI

To create hosts using image-based provisioning, you must add information about the image, such as access details and the image location, to your Satellite Server.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Click the name of the Red Hat OpenStack Services on OpenShift connection.
3. Click **Create Image**.
4. In the **Name** field, enter a name for the image.
5. From the **Operating System** list, select the base operating system of the image.
6. From the **Architecture** list, select the operating system architecture.
7. In the **Username** field, enter the SSH user name for image access. This is normally the `root` user.
8. In the **Password** field, enter the SSH password for image access.
9. From the **Image** list, select an image from the Red Hat OpenStack Services on OpenShift compute resource.
10. Optional: Select the **User Data** checkbox if the image supports user data input, such as `cloud-init` data.
11. Click **Submit** to save the image details.

## 14.5. Adding Red Hat OpenStack Services on OpenShift images to Satellite by using Hammer CLI

To create hosts using image-based provisioning, you must add information about the image, such as access details and the image location, to your Satellite Server.

**Procedure**

- Create the image: Use the `--uuid` field to store the full path of the image location on the Red Hat OpenStack Services on OpenShift server.

  ```
  $ hammer compute-resource image create \
  --name "OpenStack Image" \
  --compute-resource "My_OpenStack_Platform"
  --operatingsystem "RedHat version" \
  --architecture "x86_64" \
  --username root \
  --user-data true \
  --uuid "/path/to/OpenstackImage.qcow2"
  ```

## 14.6. Adding Red Hat OpenStack Services on OpenShift details to a compute profile by using Satellite web UI

You can automatically populate settings when provisioning hosts within your Red Hat OpenStack Services on OpenShift environment by adding Red Hat OpenStack Services on OpenShift hardware settings to a compute profile.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Profiles**.
2. In the Compute Profiles window, click the name of an existing compute profile, or click **Create Compute Profile**, enter a **Name**, and click **Submit**.
3. Click the name of the Red Hat OpenStack Services on OpenShift compute resource.
4. From the **Flavor** list, select the hardware profile on Red Hat OpenStack Services on OpenShift to use for the host.
5. From the **Availability zone** list, select the target cluster to use within the Red Hat OpenStack Services on OpenShift environment.
6. From the **Image** list, select the image to use for image-based provisioning.
7. From the **Tenant** list, select the tenant or project for the Red Hat OpenStack Services on OpenShift instance.
8. From the **Security Group** list, select the cloud-based access rules for ports and IP addresses.
9. From the **Internal network**, select the private networks for the host to join.
10. From the **Floating IP network**, select the external networks for the host to join and assign a floating IP address.
11. From the **Boot from volume**, select whether a volume is created from the image. If not selected, the instance boots the image directly.
12. In the **New boot volume size (GB)** field, enter the size, in GB, of the new boot volume.
13. Click **Submit** to save the compute profile.

## 14.7. Adding Red Hat OpenStack Services on OpenShift details to a compute profile by using Hammer CLI

You can automatically populate settings when provisioning hosts within your Red Hat OpenStack Services on OpenShift environment by adding Red Hat OpenStack Services on OpenShift hardware settings to a compute profile.

**Procedure**

- Set Red Hat OpenStack Services on OpenShift details to a compute profile:

  ```
  $ hammer compute-profile values create
  --compute-resource "My_Laptop" \
  --compute-profile "My_Compute_Profile" \
  --compute-attributes "availability_zone=My_Zone,image_ref=My_Image,flavor_ref=m1.small,tenant_id=openstack,security_groups=default,network=My_Network,boot_from_volume=false"
  ```

## 14.8. Creating image-based hosts on Red Hat OpenStack Services on OpenShift by using Satellite web UI

In Satellite, you can use Red Hat OpenStack Services on OpenShift provisioning to create hosts from an existing image. The new host entry triggers the Red Hat OpenStack Services on OpenShift server to create the instance using the pre-existing image as a basis for the new volume.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. From the **Deploy on** list, select the Red Hat OpenStack Services on OpenShift connection.
7. From the **Compute Profile** list, select a profile to use to automatically populate virtual machine settings.
8. From the **Lifecycle Environment** list, select the environment.
9. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
10. Verify that the fields are populated with values. Note in particular:

    - Satellite automatically assigns an IP address for the new host.
    - Ensure that the **MAC address** field is blank. Red Hat OpenStack Services on OpenShift assigns a MAC address to the host during provisioning.
    - The **Name** from the **Host** tab becomes the **DNS name**.
    - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
11. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

    For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
12. Click the **Operating System** tab, and confirm that all fields automatically contain values.
13. If you want to change the image that populates automatically from your compute profile, from the **Images** list, select a different image to base the new host’s root volume on.
14. Click **Resolve** in **Provisioning templates** to check the new host can identify the right provisioning templates to use.
15. Click the **Virtual Machine** tab and confirm that these settings are populated with details from the host group and compute profile. Modify these settings to suit your needs.
16. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
17. Click **Submit** to save the host entry.

## 14.9. Creating image-based hosts on Red Hat OpenStack Services on OpenShift by using Hammer CLI

In Satellite, you can use Red Hat OpenStack Services on OpenShift provisioning to create hosts from an existing image. The new host entry triggers the Red Hat OpenStack Services on OpenShift server to create the instance using the pre-existing image as a basis for the new volume.

For more information about additional host creation parameters for this compute resource, enter the `hammer host create --help` command.

**Procedure**

- Create the host with the `hammer host create` command and include `--provision-method image`. Replace the values in the following example with the appropriate values for your environment.

  ```
  $ hammer host create \
  --compute-attributes="flavor_ref=m1.small,tenant_id=openstack,security_groups=default,network=mynetwork" \
  --compute-resource "My_OpenStack_Platform" \
  --enabled true \
  --hostgroup "My_Host_Group" \
  --image "My_OpenStack_Image" \
  --interface "managed=true,primary=true,provision=true" \
  --location "My_Location" \
  --managed true \
  --name "My_Host_Name" \
  --organization "My_Organization" \
  --provision-method image
  ```
