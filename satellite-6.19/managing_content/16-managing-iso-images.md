---
title: "Managing ISO images"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "16"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-iso-images"
---
# Chapter 16. Managing ISO images

You can use Satellite to store ISO images from the Red Hat Content Delivery Network or other sources for host provisioning and creating installation media. You can also upload other files, such as virtual machine images, and publish them in repositories.

## 16.1. Importing ISO images from Red Hat by using Satellite web UI

You can import ISO images for certain products from the Red Hat Content Delivery Network. The process is similar to enabling repositories for Yum content.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Red Hat Repositories**.
2. In the **Search** field, enter an image name, for example, `Red Hat Enterprise Linux 7 Server (ISOs)`.
3. In the Available Repositories window, expand **Red Hat Enterprise Linux 7 Server (ISOs)**.
4. For the **x86_64 7.2** entry, click the **Enable** icon to enable the repositories for the image.
5. In the Satellite web UI, navigate to **Content** > **Products** and click **Red Hat Enterprise Linux Server**.
6. Click the **Repositories** tab of the Red Hat Enterprise Linux Server window, and click **Red Hat Enterprise Linux 7 Server ISOs x86_64 7.2**.
7. In the upper right of the Red Hat Enterprise Linux 7 Server ISO images x86_64 7.2 window, click **Select Action** and select **Sync Now**.

**Next steps**

- To view the synchronization status, navigate to **Content** > **Sync Status** and expand **Red Hat Enterprise Linux Server**.

## 16.2. Importing ISO images from Red Hat by using Hammer CLI

You can import ISO images for certain products from the Red Hat Content Delivery Network. The process is similar to enabling repositories for Yum content.

**Procedure**

1. Locate the Red Hat Enterprise Linux Server product for `file` repositories:

   ```
   $ hammer repository-set list \
   --product "Red Hat Enterprise Linux Server" \
   --organization "My_Organization" | grep "file"
   ```
2. Enable the `file` repository for Red Hat Enterprise Linux 7.2 Server ISO:

   ```
   $ hammer repository-set enable \
   --product "Red Hat Enterprise Linux Server" \
   --name "Red Hat Enterprise Linux 7 Server (ISOs)" \
   --releasever 7.2 \
   --basearch x86_64 \
   --organization "My_Organization"
   ```
3. Locate the repository in the product:

   ```
   $ hammer repository list \
   --product "Red Hat Enterprise Linux Server" \
   --organization "My_Organization"
   ```
4. Synchronize the repository in the product:

   ```
   $ hammer repository synchronize \
   --name "Red Hat Enterprise Linux 7 Server ISOs x86_64 7.2" \
   --product "Red Hat Enterprise Linux Server" \
   --organization "My_Organization"
   ```

## 16.3. Importing an ISO image by using Satellite web UI

You can manually import an ISO image to Satellite Server by using Satellite web UI. However, if the file size is larger than 15 MB, you must use the Hammer CLI to upload it to a repository.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products** and click **Create Product**.
2. In the **Name** field, enter a name to identify the product. This name populates the **Label** field.
3. Optional: In the **GPG Key** field, enter a GPG Key for the product.
4. Optional: From the **Sync Plan** list, select a synchronization plan for the product.
5. Optional: In the **Description** field, enter a description of the product.
6. Click **Save**.
7. In the **Products** window, click the new product and then click **Create Repository**.
8. In the **Name** field, enter a name for the repository. This automatically populates the **Label** field.
9. From the **Type** list, select **file**.
10. In the **Upstream URL** field, enter the URL of the registry to use as a source. Add a corresponding user name and password in the **Upstream Username** and **Upstream Password** fields.
11. Click **Save**.
12. Select the new repository.
13. Navigate to **Upload File** and click **Browse**.
14. Select the `.iso` file and click **Upload**.

## 16.4. Importing an ISO image by using Hammer CLI

You can manually import an ISO image to Satellite Server by using Hammer CLI. You must use the Hammer CLI to upload files larger than 15 MB to a repository.

**Procedure**

1. Create the custom product:

   ```
   $ hammer product create \
   --name "My_ISOs" \
   --sync-plan "Example Plan" \
   --description "My_Product" \
   --organization "My_Organization"
   ```
2. Create the repository:

   ```
   $ hammer repository create \
   --name "My_ISOs" \
   --content-type "file" \
   --product "My_Product" \
   --organization "My_Organization"
   ```
3. Upload the ISO file to the repository:

   ```
   $ hammer repository upload-content \
   --path ~/bootdisk.iso \
   --id repo_ID \
   --organization "My_Organization"
   ```
