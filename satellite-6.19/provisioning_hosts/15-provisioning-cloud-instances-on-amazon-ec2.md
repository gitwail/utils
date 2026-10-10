---
title: "Provisioning cloud instances on Amazon EC2"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "15"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-cloud-instances-on-amazon-ec2"
---
# Chapter 15. Provisioning cloud instances on Amazon EC2

You can use Satellite to create cloud instances and control their power management states through Amazon Elastic Compute Cloud (Amazon EC2) public API.

## 15.1. HTTP proxy for communication with Amazon EC2

If your Amazon EC2 requires an HTTP proxy to communicate with Satellite, you have to set up and select the HTTP proxy in Satellite. If you have configured an HTTP proxy for Satellite in **Administer** > **Settings**, it takes precedence over the HTTP proxy for your compute resource.

**Additional resources**

- [Adding an HTTP proxy in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-an-http-proxy-by-using-web-ui)

## 15.2. Adding an Amazon EC2 connection to Satellite Server by using Satellite web UI

Add Amazon EC2 as a compute resource to provision and manage hosts on EC2.

**Prerequisites**

- An AWS EC2 user performing this procedure needs the `AmazonEC2FullAccess` permissions. You can attach these permissions from AWS.
- Amazon Web Services uses time settings as part of the authentication process. Ensure that Satellite Server has an NTP service configured, for example, `ntpd` or `chronyd`.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources** and in the Compute Resources window, click **Create Compute Resource**.
2. In the **Name** field, enter a name to identify the Amazon EC2 compute resource.
3. From the **Provider** list, select **EC2**.
4. In the **Description** field, enter information that helps distinguish the resource for future use.
5. Optional: From the **HTTP proxy** list, select an HTTP proxy to connect to external API services. You must add HTTP proxies to Satellite before you can select an HTTP proxy from this list. For more information, see [Section 15.1, “HTTP proxy for communication with Amazon EC2”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#http-proxy-for-communication-with-amazon-ec2 "15.1. HTTP proxy for communication with Amazon EC2").
6. In the **Access Key** and **Secret Key** fields, enter the access keys for your Amazon EC2 account. For more information, see [Managing Access Keys for your AWS Account](http://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html) on the Amazon documentation website.
7. Optional: Click **Load Regions** to populate the **Regions** list.
8. From the **Region** list, select the Amazon EC2 region or data center to use.
9. Click the **Locations** tab and ensure that the location you want to use is selected, or add a different location.
10. Click the **Organizations** tab and ensure that the organization you want to use is selected, or add a different organization.
11. Click **Submit** to save the Amazon EC2 connection.
12. Select the new compute resource and then click the **SSH keys** tab, and click **Download** to save a copy of the SSH keys to use for SSH authentication. Until [BZ1793138](https://bugzilla.redhat.com/show_bug.cgi?id=1793138) is resolved, you can download a copy of the SSH keys only immediately after creating the Amazon EC2 compute resource. If you require SSH keys at a later stage, follow the procedure in [Section 15.11, “Connecting to an Amazon EC2 instance by using SSH”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#connecting-to-an-amazon-ec2-instance-by-using-ssh "15.11. Connecting to an Amazon EC2 instance by using SSH").

## 15.3. Adding an Amazon EC2 connection to Satellite Server by using Hammer CLI

Add Amazon EC2 as a compute resource to provision and manage hosts on EC2.

**Prerequisites**

- An AWS EC2 user performing this procedure needs the `AmazonEC2FullAccess` permissions. You can attach these permissions from AWS.
- Amazon Web Services uses time settings as part of the authentication process. Ensure that Satellite Server has an NTP service configured, for example, `ntpd` or `chronyd`.

**Procedure**

- Connect your Satellite Server to Amazon EC2:

  ```
  $ hammer compute-resource create \
  --description "Amazon EC2 Public Cloud" \
  --locations "My_Location" \
  --name "My_EC2_Compute_Resource" \
  --organizations "My_Organization" \
  --password "My_Secret_Key" \
  --provider "EC2" \
  --region "My_Region" \
  --user "My_User_Name"
  ```

## 15.4. Creating an image for Amazon EC2

You can create images for Amazon EC2 from within Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select your Amazon EC2 provider.
3. Click **Create Image**.

   - In the **Name** field, enter a meaningful and unique name for your EC2 image.
   - From the **Operating System** list, select an operating system to associate with the image.
   - From the **Architecture** list, select an architecture to associate with the image.
   - In the **Username** field, enter the username needed to SSH into the machine.
   - In the **Image ID** field, enter the image ID provided by Amazon or an operating system vendor.
   - Optional: Select the **User Data** check box to enable support for user data input.
   - Optional: Set an **Iam Role** for *Fog* to use when creating this image.
   - Click **Submit** to save your changes to Satellite.

## 15.5. Adding Amazon EC2 images to Satellite Server by using Satellite web UI

You must add Amazon EC2 image details to Satellite Server for image-based provisioning.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources** and select an Amazon EC2 connection.
2. Click the **Images** tab, and then click **Create Image**.
3. In the **Name** field, enter a name to identify the image for future use.
4. From the **Operating System** list, select the operating system that corresponds with the image you want to add.
5. From the **Architecture** list, select the operating system’s architecture.
6. In the **Username** field, enter the SSH user name for image access. This is normally the `root` user.
7. In the **Password** field, enter the SSH password for image access.
8. In the **Image ID** field, enter the Amazon Machine Image (AMI) ID for the image. This is usually in the following format: `ami-xxxxxxxx`.
9. Optional: Select the **User Data** checkbox if the images support user data input, such as `cloud-init` data. If you enable user data, the Finish scripts are automatically disabled. This also applies in reverse: if you enable the Finish scripts, this disables user data.
10. Optional: In the **IAM role** field, enter the Amazon security role used for creating the image.
11. Click **Submit** to save the image details.

## 15.6. Adding Amazon EC2 images to Satellite Server by using Hammer CLI

You must add Amazon EC2 image details to Satellite Server for image-based provisioning.

**Procedure**

- Create the image:

  ```
  $ hammer compute-resource image create \
  --architecture "My_Architecture" \
  --compute-resource "My_EC2_Compute_Resource" \
  --name "My_Amazon_EC2_Image" \
  --operatingsystem "My_Operating_System" \
  --user-data true \
  --username root \
  --uuid "ami-My_AMI_ID"
  ```

## 15.7. Adding Amazon EC2 details to a compute profile by using Satellite web UI

You can add hardware settings for instances on Amazon EC2 to a compute profile.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Profiles** and click the name of your profile, then click an EC2 connection.
2. From the **Flavor** list, select the hardware profile on EC2 to use for the host.
3. From the **Image** list, select the image to use for image-based provisioning.
4. From the **Availability zone** list, select the target cluster to use within the chosen EC2 region.
5. From the **Subnet** list, add the subnet for the EC2 instance. If you have a VPC for provisioning new hosts, use its subnet.
6. From the **Security Groups** list, select the cloud-based access rules for ports and IP addresses to apply to the host.
7. From the **Managed IP** list, select either a `Public` IP or a `Private` IP.
8. Click **Submit** to save the compute profile.

## 15.8. Adding Amazon EC2 details to a compute profile by using Hammer CLI

You can add hardware settings for instances on Amazon EC2 to a compute profile.

**Procedure**

- Add Amazon EC2 details to a compute profile:

  ```
  $ hammer compute-profile values create
  --compute-resource "My_Amazon_EC2_Compute_Resource" \ --compute-profile "_My_Compute_Profile" \
  --compute-attributes "flavor_id=1,availability_zone= My_Zone,subnet_id=1,security_group_ids=1,managed_ip=public_ip"
  ```

## 15.9. Creating image-based hosts on Amazon EC2 by using Satellite web UI

You can perform image-based host provisioning on Amazon EC2 through Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
2. In the **Name** field, enter a name for the host.
3. Optional: Click the **Organization** tab and change the organization context to match your requirement.
4. Optional: Click the **Location** tab and change the location context to match your requirement.
5. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
6. From the **Deploy on** list, select the EC2 connection.
7. From the **Compute Profile** list, select a profile to use to automatically populate virtual machine-based settings.
8. Click the **Interfaces** tab, and on the interface of the host, click **Edit**.
9. Verify that the fields are populated with values. Note in particular:

   - Satellite automatically assigns an IP address for the new host.
   - Ensure that the **MAC address** field is blank. Amazon EC2 assigns a MAC address to the host during provisioning.
   - The **Name** from the **Host** tab becomes the **DNS name**.
   - Ensure that Satellite automatically selects the **Managed**, **Primary**, and **Provision** options for the first interface on the host. If not, select them.
10. Click **OK** to save. To add another interface, click **Add Interface**. You can select only one interface for **Provision** and **Primary**.

    For more information about network interfaces, see [Configuring network interfaces](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces) in *Managing hosts*.
11. Click the **Operating System** tab and confirm that all fields are populated with values.
12. Click the **Virtual Machine** tab and confirm that all fields are populated with values.
13. On the **Parameters** tab, click **Add parameter**. Add a parameter named `kt_activation_keys`, select the **string** type, and enter the name of the activation key as the value. The activation key has to belong to the same organization as your host. You can also enter a comma-separated list of multiple activation keys.
14. Click **Submit** to save your changes.

    This new host entry triggers the Amazon EC2 server to create the instance, using the pre-existing image as a basis for the new volume.

## 15.10. Creating image-based hosts on Amazon EC2 by using Hammer CLI

You can perform image-based host provisioning on Amazon EC2 through Satellite.

For more information about additional host creation parameters for this compute resource, enter the `hammer host create --help` command.

**Procedure**

- Create the host with the `hammer host create` command and include `--provision-method image` to use image-based provisioning.

  ```
  $ hammer host create \
  --compute-attributes="flavor_id=m1.small,image_id=TestImage,availability_zones=us-east-1a,security_group_ids=Default,managed_ip=Public" \
  --compute-resource "My_EC2_Compute_Resource" \
  --enabled true \
  --hostgroup "My_Host_Group" \
  --image "My_Amazon_EC2_Image" \
  --interface "managed=true,primary=true,provision=true,subnet_id=EC2" \
  --location "My_Location" \
  --managed true \
  --name "My_Host_Name_" \
  --organization "My_Organization" \
  --provision-method image
  ```

  This new host entry triggers the Amazon EC2 server to create the instance, using the pre-existing image as a basis for the new volume.

## 15.11. Connecting to an Amazon EC2 instance by using SSH

You can connect remotely to Amazon EC2 instances that you provision through Satellite by using SSH. To authenticate, retrieve the private key associated with the compute resource from the `foreman` database.

**Procedure**

1. On your Satellite Server base system, locate the ID of the compute resource that you want to use:

   ```
   $ hammer compute-resource list
   ```
2. Connect to the `foreman` database as the user `postgres`:

   ```
   # su - postgres -c psql foreman
   ```
3. Select the secret from `key_pairs` where `compute_resource_id = 3`:

   ```
   # select secret from key_pairs where compute_resource_id = 3; secret
   ```
4. Copy the key from after `-----BEGIN RSA PRIVATE KEY-----` until `-----END RSA PRIVATE KEY-----`.
5. Create a `.pem` file and paste your key into the file:

   ```
   # vim Keyname.pem
   ```
6. Ensure that you restrict access to the `.pem` file:

   ```
   # chmod 600 Keyname.pem
   ```
7. To connect to the Amazon EC2 instance, enter the following command:

   ```
   ssh -i Keyname.pem   ec2-user@example.aws.com
   ```

## 15.12. Configuring a finish template for an Amazon Web Service EC2 environment

You can use Red Hat Satellite finish templates during the provisioning of Red Hat Enterprise Linux instances in an Amazon EC2 environment.

If you want to use a Finish template with SSH, Satellite must reside within the EC2 environment and in the correct security group. Satellite currently performs SSH finish provisioning directly, not using Capsule Server. If Satellite Server does not reside within EC2, the EC2 virtual machine reports an internal IP rather than the necessary external IP with which it can be reached.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. In the **Provisioning Templates** page, enter `Kickstart default finish` into the search field and click **Search**.
3. On the **Kickstart default finish** template, select **Clone**.
4. In the **Name** field, enter a unique name for the template.
5. In the template, prefix each command that requires root privileges with `sudo`, except for `subscription-manager register` and `yum` commands, or add the following line to run the entire template as the sudo user:

   ```
   sudo -s << EOS
   _Template_ _Body_
   EOS
   ```
6. Click the **Association** tab, and associate the template with a Red Hat Enterprise Linux operating system that you want to use.
7. Click the **Locations** tab, and add the the location where the host resides.
8. Click the **Organizations** tab, and add the organization that the host belongs to.
9. Make any additional customizations or changes that you require, then click **Submit** to save your template.
10. In the Satellite web UI, navigate to **Hosts** > **Operating systems** and select the operating system that you want for your host.
11. Click the **Templates** tab, and from the **Finish Template** list, select your finish template.
12. In the Satellite web UI, navigate to **Hosts** > **Create Host**.
13. In the **Name** field, enter a name for the host.
14. Optional: Click the **Organization** tab and change the organization context to match your requirement.
15. Optional: Click the **Location** tab and change the location context to match your requirement.
16. From the **Host Group** list, select a host group that you want to assign your host to. That host group will populate the form.
17. Click the **Parameters** tab and navigate to **Host parameters**.
18. In **Host parameters**, click **Add Parameter** two times to add two new parameter fields. Add the following parameters:

    1. In the **Name** field, enter `activation_keys`. In the corresponding **Value** field, enter your activation key.
    2. In the **Name** field, enter `remote_execution_ssh_user`. In the corresponding **Value** field, enter `ec2-user`.
19. Click **Submit** to save the changes.

## 15.13. Deleting a virtual machine on Amazon EC2

You can delete virtual machines (VMs) running on Amazon EC2 from within Satellite.

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**.
2. Select your Amazon EC2 provider.
3. On the **Virtual Machines** tab, click **Delete** from the **Actions** menu. This deletes the virtual machine from the Amazon EC2 compute resource while retaining any associated hosts within Satellite. If you want to delete the orphaned host, navigate to **Hosts** > **All Hosts** and delete the host manually.

## 15.14. More information about Amazon Web Services and Satellite

You can use the following external documentation to work with Amazon Web Services together with Satellite.

- [How to Locate Red Hat Cloud Access Gold Images on AWS EC2](https://access.redhat.com/articles/2962171)
- [Install the AWS Command Line Interface on Linux](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux.html) in the Amazon Web Services documentation
- [VM Import/Export](https://aws.amazon.com/ec2/vm-import/) in the Amazon Web Services documentation
