---
title: "Managing Red Hat subscriptions"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Red_Hat_Subscriptions_content-management"
---
# Chapter 2. Managing Red Hat subscriptions

You can import content from the Red Hat Content Delivery Network (CDN) into Red Hat Satellite by using a Red Hat subscription manifest. Manage your subscription allocations to ensure each organization can access and download Red Hat repositories.

A Red Hat subscription manifest contains the information about the subscriptions purchased from Red Hat. Satellite uses the information in the manifest to access the Red Hat CDN and find what repositories are available for the associated subscription.

You must have a Red Hat subscription manifest containing a subscription allocation for each organization in Satellite. All subscription information is available on the Red Hat Hybrid Cloud Console.

Subscription allocations and organizations
:   You can manage more than one organization if you have more than one subscription allocation. Satellite requires a single allocation for each organization configured in Satellite Server. The advantage of this is that each organization maintains separate subscriptions so that you can support multiple organizations, each with their own Red Hat accounts.

Future-dated subscriptions
:   You can use future-dated subscriptions in a subscription manifest. When you add future-dated subscriptions to your manifest before the expiry date of the existing subscriptions, you can have uninterrupted access to repositories.

Subscriptions service
:   The Subscriptions service on the Red Hat Hybrid Cloud Console helps you track and manage Red Hat subscription usage across connected and disconnected systems. It collects usage data, displays trends in a centralized dashboard, and supports historical analysis for planning and compliance.

**Additional resources**

- [Configuring Satellite Server to consume content from a custom CDN in *Installing Satellite Server in a disconnected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#configuring-satellite-server-to-consume-content-from-a-custom-cdn-by-using-web-ui)
- [How to register and subscribe a system offline to the Red Hat Customer Portal?](https://access.redhat.com/solutions/7065718)
- [Section 2.1, “Tracking subscription usage by using the Subscriptions service”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#tracking-subscription-usage-by-using-the-subscriptions-service "2.1. Tracking subscription usage by using the Subscriptions service")

## 2.1. Tracking subscription usage by using the Subscriptions service

You can configure your Satellite Server to report usage data to the Red Hat Hybrid Cloud Console. Track and manage your subscription usage to analyze historical trends for planning and compliance.

Connected Satellite
:   In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Inventory Upload** to configure the `foreman_rh_cloud` plugin and share inventory information with the Red Hat Hybrid Cloud Console. Ensure that the **Automatic Inventory Upload** setting is enabled. The plugin enables the subscriptions service to track usage information across connected systems.

    You can configure the plugin to omit data that is not needed for subscription tracking, such as host names and IP addresses.

Disconnected Satellite
:   Export usage data in one of the following ways:

    - Use the `foreman_rh_cloud` plugin to generate a report locally. You can download the report from the Satellite web UI. The report is in JSON format and is easily integrated for automated scripts or machine processing. You can generate this report by using CLI:

      ```
      # foreman-rake rh_cloud_inventory:report:generate
      ```
    - View product usage by running the **Host - Installed Products** report.

      Navigate to **Monitor** > **Reports** > **Report Templates**. You can select the format that you want for the report. YAML, JSON, HTML, and CSV formats are supported.

## 2.2. Importing Red Hat subscription manifests into Satellite

You can import a Red Hat subscription manifest into Satellite to provide subscription allocation to your organization in Satellite.

> **Note**
>
> Simple Content Access (SCA) is set on the organization, not the manifest. Importing a manifest does not change your organization’s Simple Content Access status.

Simple Content Access simplifies the subscription experience for administrators.

**Additional resources**

- [Subscription Management Administration Guide for Red Hat Enterprise Linux on the Red Hat Customer Portal](https://access.redhat.com/subscription_mgmt_guide_for_RHEL)

### 2.2.1. Obtaining a Red Hat subscription manifest

You can create and export a Red Hat subscription manifest to prepare subscriptions for import into Satellite.

**Procedure**

- If your Satellite is connected, use the Red Hat Hybrid Cloud Console to create and export the manifest. For more information, see [Creating and managing manifests for a connected Satellite Server](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/creating_and_managing_manifests_for_a_connected_satellite_server/index) in *Subscription Central*.

  This manifest does not yet contain any subscriptions. After you import the manifest into Satellite, add subscriptions to the manifest in Satellite.
- If your Satellite is disconnected, use the Red Hat Customer Portal to create and export the manifest. For more information, see [Creating and managing manifests for a disconnected Satellite Server](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/creating_and_managing_manifests_for_a_disconnected_satellite_server/index) in *Subscription Central*.

  This manifest already contains subscriptions.

### 2.2.2. Importing a Red Hat subscription manifest by using Satellite web UI

You can import a Red Hat subscription manifest into Satellite Server by using Satellite web UI. Import the manifest so that you can enable and synchronize Red Hat repositories in your organization.

**Prerequisites**

- You have a Red Hat subscription manifest file. For more information, see [Section 2.2.1, “Obtaining a Red Hat subscription manifest”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#obtaining-a-red-hat-subscription-manifest "2.2.1. Obtaining a Red Hat subscription manifest").

**Procedure**

1. In the Satellite web UI, ensure the context is set to the organization you want to use.
2. Navigate to **Content** > **Subscriptions**.
3. Click **Manage Manifest**.
4. In the **Manage Manifest** window, click **Choose File**.
5. Navigate to the location that contains the Red Hat subscription manifest file, then click **Open**.

**Next steps**

- If you use the manifest from the Red Hat Hybrid Cloud Console, add subscriptions to the manifest. For more information, see [Section 2.4, “Adding Red Hat subscriptions to subscription manifests”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Adding_Red_Hat_Subscriptions_to_Subscription_Manifests_content-management "2.4. Adding Red Hat subscriptions to subscription manifests").

### 2.2.3. Importing a Red Hat subscription manifest by using Hammer CLI

You can import a Red Hat subscription manifest into Satellite Server by using Hammer CLI. Import the manifest so that you can enable and synchronize Red Hat repositories in your organization.

**Prerequisites**

- You have a Red Hat subscription manifest file. For more information, see [Section 2.2.1, “Obtaining a Red Hat subscription manifest”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#obtaining-a-red-hat-subscription-manifest "2.2.1. Obtaining a Red Hat subscription manifest").

**Procedure**

1. Copy the Red Hat subscription manifest file from your local machine to Satellite Server:

   ```
   $ scp ~/manifest_file.zip root@satellite.example.com:~/.
   ```
2. Log in to Satellite Server over SSH as the `root` user.
3. Import the Red Hat subscription manifest file:

   ```
   $ hammer subscription upload \
   --file ~/manifest_file.zip \
   --organization "My_Organization"
   ```

**Next steps**

- If you use the manifest from the Red Hat Hybrid Cloud Console, add subscriptions to the manifest. For more information, see [Section 2.4, “Adding Red Hat subscriptions to subscription manifests”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Adding_Red_Hat_Subscriptions_to_Subscription_Manifests_content-management "2.4. Adding Red Hat subscriptions to subscription manifests").

## 2.3. Locating a Red Hat subscription

You can locate specific Red Hat subscriptions in your Satellite by filtering the results on the Subscriptions page to navigate a high volume of subscriptions.

**Prerequisites**

- A Red Hat subscription manifest is imported to Satellite. For more information, see [Section 2.2, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-red-hat-subscription-manifests-into-satellite "2.2. Importing Red Hat subscription manifests into Satellite").

**Procedure**

1. In the Satellite web UI, ensure the context is set to the organization you want to use.
2. In the Satellite web UI, navigate to **Content** > **Subscriptions**.
3. In the Subscriptions window, click the **Search** field to view the list of search criteria for building your search query.
4. Select search criteria to display further options.
5. When you have built your search query, click the search icon.

**Additional resources**

- [Working efficiently with Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui)

## 2.4. Adding Red Hat subscriptions to subscription manifests

You can add Red Hat subscriptions to your subscription manifest in Satellite to allocate entitlements to Red Hat content in your organization.

If you have exported a new subscription manifest from the Red Hat Hybrid Cloud Console, you have to populate the manifest with subscriptions. Such a manifest does not initially contain any subscriptions.

**Prerequisites**

- A Red Hat subscription manifest is imported to Satellite. For more information, see [Section 2.2, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-red-hat-subscription-manifests-into-satellite "2.2. Importing Red Hat subscription manifests into Satellite").

**Procedure**

1. In the Satellite web UI, ensure the context is set to the organization you want to use.
2. Navigate to **Content** > **Subscriptions**.
3. On the **Subscriptions** page, click **Add Subscriptions**.
4. On the row of each subscription you want to add, enter the quantity in the **Quantity to Allocate** column.
5. Click **Submit**.

## 2.5. Removing Red Hat subscriptions from subscription manifests

You can remove Red Hat subscriptions from manifests to adjust entitlement allocations or decommission Red Hat products from your organization.

> **Warning**
>
> Manifests must not be deleted. If you delete the manifest from the Red Hat Customer Portal or in the Satellite web UI, all of the entitlements for all of your hosts will be removed.

**Prerequisites**

- A Red Hat subscription manifest is imported to Satellite. For more information, see [Section 2.2, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-red-hat-subscription-manifests-into-satellite "2.2. Importing Red Hat subscription manifests into Satellite").

**Procedure**

1. In the Satellite web UI, ensure the context is set to the organization you want to use.
2. Navigate to **Content** > **Subscriptions**.
3. On the row of each subscription you want to remove, select the corresponding checkbox.
4. Click **Delete**, and then confirm deletion.

## 2.6. Updating and refreshing Red Hat subscription manifests

You can refresh your Red Hat subscription manifests to keep your subscription allocations up to date. Refresh your manifests after renewing, adjusting, or purchasing subscriptions to ensure accurate entitlements in your Satellite.

Every time you change a subscription allocation, you must refresh the manifest to reflect these changes. For example, you must refresh the manifest if you take any of the following actions:

- Renewing a subscription
- Adjusting subscription quantities
- Purchasing additional subscriptions

You can refresh the manifest directly in the Satellite web UI. Alternatively, you can import an updated manifest that contains the changes.

The Satellite web UI provides a notification before the subscription manifest expires.

**Prerequisites**

- A Red Hat subscription manifest is imported to Satellite. For more information, see [Section 2.2, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-red-hat-subscription-manifests-into-satellite "2.2. Importing Red Hat subscription manifests into Satellite").

**Procedure**

1. In the Satellite web UI, ensure the context is set to the organization you want to use.
2. Navigate to **Content** > **Subscriptions**.
3. On the **Subscriptions** page, click **Manage Manifest**.
4. In the **Manage Manifest** window, click **Refresh**.

**Additional resources**

- [How and when does a Red Hat Satellite manifest certificate expire?](https://access.redhat.com/solutions/11101)

## 2.7. Red Hat CDN structure

The Red Hat Content Delivery Network (CDN) is a geographically distributed series of static web servers providing Red Hat software. You can access this content directly through Subscription Manager or Satellite Server.

The Red Hat CDN is located at `cdn.redhat.com`. Satellite and Subscription Manager configure which content is accessible to your hosts based on your subscription entitlements. Satellite must authenticate to the Red Hat CDN by using X.509 certificate authentication. The certificate is part of a subscription manifest.

**Example 2.1. Directory structure of the Red Hat CDN**

```
$ tree -d -L 11
└── content
    ├── beta
    │   └── rhel
    │       └── server
    │           └── 7
    │               └── x86_64
    │                   └── sat-tools
    └── dist
        └── rhel
            └── server
                └── 7
                ├── 7.2
                │   └── x86_64
                │       └── kickstart
                └── 7Server
                    └── x86_64
                        └── os
```

- `content` – Root directory for the content.
- `beta` – Directory responsible for the lifecycle of the content. Common directories include `beta` (for Beta code), `dist` (for Production) and `eus` (For Extended Update Support) directories.
- `rhel` – Directory responsible for the product name. Usually `rhel` for Red Hat Enterprise Linux.
- `server` – Directory responsible for the type of the product. For Red Hat Enterprise Linux this might include `server`, `workstation`, and `computenode` directories.
- `7` – Directory responsible for the release version, such as `7`, `7.2` or `7Server`.
- `x86_64` – Directory responsible for the base architecture, such as `i386` or `x86_64`.
- `sat-tools` – Directory responsible for the repository name, such as `sat-tools`, `kickstart`, `rhscl`.

Some components have additional subdirectories which might vary.

This directory structure is also used in Red Hat subscription manifests.
