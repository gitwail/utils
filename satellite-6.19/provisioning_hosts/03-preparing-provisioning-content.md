---
title: "Preparing provisioning content"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-provisioning-content"
---
# Chapter 3. Preparing provisioning content

You have to configure provisioning content that will be used for installation of the operating system on the provisioned host.

**Additional resources**

- [*Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#)

## 3.1. Preparing a synchronized Kickstart repository

You can use synchronized Kickstart repositories as the source of the operating system during host provisioning.

**Prerequisites**

- **BaseOS** and **AppStream Kickstart** are enabled before provisioning.

**Procedure**

1. Add the synchronized Kickstart repository that you want to use to the existing content view, or create a new content view and add the Kickstart repository.

   For Red Hat Enterprise Linux 8, ensure that you add both **Red Hat Enterprise Linux 8 for x86_64 - AppStream Kickstart x86_64 8** and **Red Hat Enterprise Linux 8 for x86_64 - BaseOS Kickstart x86_64 8** repositories.

   If you use a disconnected environment, you must import the Kickstart repositories from your Red Hat Enterprise Linux binary DVD.
2. Publish a new version of the content view where the Kickstart repository is added and promote it to a required lifecycle environment.
3. When you create a host, in the **Operating System** tab, for **Media Selection**, select the **Synced Content** checkbox.

**Verification**

- View the Kickstart tree:

  ```
  $ hammer medium list --organization "My_Organization"
  ```

**Additional resources**

- [Managing content views and content view environments](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-views-and-content-view-environments)

## 3.2. Adding installation media to Satellite by using Satellite web UI

You can add installation media as package sources to install a base operating system from an external repository. You can add installation media to install third-party content. Content to provision Red Hat Enterprise Linux hosts is delivered through Kickstart repositories.

You can view installation media by navigating to **Hosts** > **Provisioning Setup** > **Installation Media**.

Installation media must be in the format of an operating system installation tree and must be accessible from the machine hosting the installer through an HTTP URL.

By default, Satellite includes installation media for some official Linux distributions. Note that some of those installation media are targeted for a specific version of an operating system. For example **CentOS mirror (7.x)** must be used for CentOS 7 or earlier, and **CentOS mirror (8.x)** must be used for CentOS 8 or later.

If you want to improve download performance when using installation media to install operating systems on multiple hosts, you must modify the **Path** of the installation medium to point to the closest mirror or a local copy.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Provisioning Setup** > **Installation Media**.
2. Click **Create Medium**.
3. In the **Name** field, enter a name to represent the installation media entry.
4. In the **Path** enter the URL that contains the installation tree. You can use following variables in the path to represent multiple different system architectures and versions:

   - `$arch` – The system architecture.
   - `$version` – The operating system version.
   - `$major` – The operating system major version.
   - `$minor` – The operating system minor version.

     Example HTTP path:

     ```
     http://download.example.com/centos/$version/Server/$arch/os/
     ```
5. From the **Operating system family** list, select the distribution or family of the installation medium. For example, CentOS and Fedora are in the `Red Hat` family.
6. Click the **Organizations** and **Locations** tabs, to change the provisioning context. Satellite Server adds the installation medium to the set provisioning context.
7. Click **Submit** to save your installation medium.

## 3.3. Adding installation media to Satellite by using Hammer CLI

You can add installation media as package sources to install a base operating system from an external repository. You can add installation media to install third-party content. Content to provision Red Hat Enterprise Linux hosts is delivered through Kickstart repositories.

You can view installation media by navigating to **Hosts** > **Provisioning Setup** > **Installation Media**.

Installation media must be in the format of an operating system installation tree and must be accessible from the machine hosting the installer through an HTTP URL.

By default, Satellite includes installation media for some official Linux distributions. Note that some of those installation media are targeted for a specific version of an operating system. For example **CentOS mirror (7.x)** must be used for CentOS 7 or earlier, and **CentOS mirror (8.x)** must be used for CentOS 8 or later.

If you want to improve download performance when using installation media to install operating systems on multiple hosts, you must modify the **Path** of the installation medium to point to the closest mirror or a local copy.

**Procedure**

- Create an installation medium:

  ```
  $ hammer medium create \
  --locations "My_Location" \
  --name "My_Operating_System" \
  --organizations "My_Organization" \
  --os-family "Redhat" \
  --path "http://download.example.com/centos/$version/Server/$arch/os/"
  ```

## 3.4. Configuring Satellite to provision from a Red Hat Image Builder image

You can use the RHEL web console integration to access Red Hat Image Builder and build images for host provisioning.

**Additional resources**

- [Host management and monitoring by using the RHEL web console in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#host-management-and-monitoring-by-using-cockpit)

### 3.4.1. Provisioning from a Red Hat Image Builder image on Capsule

You can upload a Red Hat Image Builder image to Satellite and use this image to provision hosts by using network boot.

When you provision from a Red Hat Image Builder image, Anaconda installer partitions disks, downloads and mounts the image, and copies files over to a host.

**Prerequisites**

- An existing TAR image created by using Red Hat Image Builder in the RHEL web console. Ensure that your blueprint to build the image includes the [required packages](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#packages-required-in-a-builder-image "3.4.3. Packages required in a Red Hat Image Builder image").
- If you want to use Capsule Server URL, then the referenced lifecycle environment, such as Library, must be synchronized to that Capsule Server. For more information, see [Adding lifecycle environments to Capsule Servers](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#adding-lifecycle-environments-by-using-web-ui) in *Installing Capsule Server*.

**Procedure**

1. On Satellite, create a custom product, add a custom file type repository to this product, and upload the image to the repository. For more information, see [Importing an ISO image by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-an-iso-image-by-using-web-ui) in *Managing content*.
2. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
3. Select the host group that you want to use.
4. Click the **Parameters** tab, and then click **Add Parameter**.
5. Create a parameter named `kickstart_liveimg` with type **string** and set the value to the full URL of the image location or the file name of the image inside a published content view, for example:

   - Full URL: `https://capsule.example.com/pulp/content/My_Organization_Label/Library/custom/My_Product_Label/My_Repository_Label/My_Image_Name.tar`
   - Image file name: `My_Image_Name.tar`

     You can use the image file name only if the host is subscribed to a single content view and lifecycle environment, and the `kt_activation_keys` parameter is defined for the host. The content view must be published.

     If a content source is assigned to the host, Satellite will use the content source Capsule of the host. If a content source is not assigned, Satellite will use Satellite Server.
6. Click **Submit** to save your changes.

**Additional resources**

- [Chapter 8, *Using network boot to provision hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#using-network-boot-to-provision-hosts "Chapter 8. Using network boot to provision hosts")

### 3.4.2. Provisioning from a Red Hat Image Builder image on an HTTP server

You can upload a Red Hat Image Builder image to an HTTP server and use this image to provision hosts by using network boot.

When you provision from a Red Hat Image Builder image, Anaconda installer partitions disks, downloads and mounts the image, and copies files over to a host.

**Prerequisites**

- An existing TAR image created by using Red Hat Image Builder in the RHEL web console. Ensure that your blueprint to build the image includes the [required packages](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#packages-required-in-a-builder-image "3.4.3. Packages required in a Red Hat Image Builder image").

**Procedure**

1. Copy the image to an existing HTTP server that your hosts can reach.
2. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
3. Select the host group that you want to use.
4. Click the **Parameters** tab, and then click **Add Parameter**.
5. Create a parameter named `kickstart_liveimg` with type **string** and set the value to the URL of the image location, such as `https://webserver.example.com/path/My_Image_Name.tar`.
6. Click **Submit** to save your changes.

**Additional resources**

- [Chapter 8, *Using network boot to provision hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#using-network-boot-to-provision-hosts "Chapter 8. Using network boot to provision hosts")

### 3.4.3. Packages required in a Red Hat Image Builder image

For the use in Satellite, the Red Hat Image Builder image must contain the following minimum of packages:

- `NetworkManager`
- `authselect`
- `chrony`
- `dnf`
- `dracut`
- `efibootmgr`
- `firewalld`
- `grub2`
- `grub2-efi`
- `grub2-tools-extra`
- `insights-client` – required only if you plan to use Red Hat Lightspeed reporting
- `iproute`
- `iputils`
- `kernel`
- `kernel-core`
- `lvm2`
- `subscription-manager`
- `wget`
