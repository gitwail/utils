---
title: "Optimizing content synchronization and storage"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#optimizing-content-synchronization-and-storage"
---
# Chapter 6. Optimizing content synchronization and storage

Use download and mirroring policies, sync concurrency limits, and package retention to balance local storage, bandwidth, and upstream alignment on Satellite Server and Capsule Servers. Configure defaults for new repositories or adjust individual repositories as needed.

## 6.1. Download policies overview

Download policies control when Satellite stores RPM packages during synchronization versus fetching them on request from Capsules or hosts.

Satellite Server has the following policies:

Immediate
:   Satellite Server downloads all metadata and packages during synchronization.

On Demand
:   Satellite Server downloads only the metadata during synchronization. Satellite Server only fetches and stores packages on the file system when Capsules or directly connected clients request them. This setting has no effect if you set a corresponding repository on a Capsule to **Immediate** because Satellite Server is forced to download all the packages.

The **On Demand** policy acts as a *Lazy Synchronization* feature because they save time synchronizing content. The lazy synchronization feature must be used only for Yum repositories. You can add the packages to content views and promote to lifecycle environments as normal.

Capsule Server has the following policies:

Immediate
:   Capsule Server downloads all metadata and packages during synchronization. Do not use this setting if the corresponding repository on Satellite Server is set to **On Demand** as Satellite Server is forced to download all the packages.

On Demand
:   Capsule Server only downloads the metadata during synchronization. Capsule Server fetches and stores packages only on the file system when directly connected clients request them. When you use an **On Demand** download policy, content is downloaded from Satellite Server if it is not available on Capsule Server.

Inherit
:   Capsule Server inherits the download policy for the repository from the corresponding repository on Satellite Server.

Streamed
:   Streamed download policy for Capsules permits Capsules to avoid caching any content. When content is requested from the Capsule, it functions as a proxy and requests the content directly from the Satellite.

You can configure the global default download policies in **Content** settings.

## 6.2. Updating the default download policy by using Satellite web UI

Set the default download policy so new repositories inherit immediate or on-demand behavior without updating existing repositories.

Depending on whether it is a Red Hat or non-Red Hat custom repository, Satellite uses separate settings. Changing the default value does not change the setting in existing repositories, but only the default setting for new repositories.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Click the **Content** tab.
3. Change the default download policy depending on your requirements:

   - To change the default download policy for a Red Hat repository, change the value of the **Default Red Hat Repository download policy** setting.
   - To change the default download policy for a custom repository, change the value of the **Default Custom Repository download policy** setting.

## 6.3. Updating the default download policy by using Hammer CLI

Set the default download policy so new repositories inherit immediate or on-demand behavior without updating existing repositories.

Depending on whether it is a Red Hat or non-Red Hat custom repository, Satellite uses separate settings. Changing the default value does not change the setting in existing repositories, but only the default setting for new repositories.

**Procedure**

- To change the default download policy for Red Hat repositories to one of `immediate` or `on_demand`, enter the following command:

  ```
  $ hammer settings set \
  --name default_redhat_download_policy \
  --value immediate
  ```
- To change the default download policy for a non-Red Hat custom repository to one of `immediate` or `on_demand`, enter the following command:

  ```
  $ hammer settings set \
  --name default_download_policy \
  --value immediate
  ```

## 6.4. Updating the download policy for a repository by using Satellite web UI

Change the download policy for an existing repository when you need immediate full downloads or on-demand storage.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select the required product name.
3. On the **Repositories** tab, click the required repository name, locate the **Download Policy** field, and click the edit icon.
4. From the list, select the required download policy and then click **Save**.

## 6.5. Updating the download policy for a repository by using Hammer CLI

Update the download policy for a specific repository when you need immediate full downloads or on-demand lazy synchronization for that repository.

**Procedure**

1. List the repositories for an organization:

   ```
   $ hammer repository list \
   --organization-label My_Organization_Label
   ```
2. Change the download policy for a repository to `immediate` or `on_demand`:

   ```
   $ hammer repository update \
   --download-policy immediate \
   --name "My_Repository" \
   --organization-label My_Organization_Label \
   --product "My_Product"
   ```

## 6.6. Mirroring policies overview

Mirroring policies control whether synchronized repositories add only new content, mirror repodata, or fully mirror upstream changes including deletions. Use them to match upstream behavior and storage needs for each repository.

Satellite Server has the following mirroring policies:

Additive
:   Neither the content nor the repodata is mirrored. Thus, only new content added since the last synchronization is added to the local repository and nothing is removed.

Content Only
:   Mirrors only content and not the repodata. Some repositories do not support metadata mirroring, in such cases you can set the mirroring policy to content only to only mirror the content.

Complete Mirroring
:   Mirrors content as well as repodata. This is the fastest method. This mirroring policy is only available for Yum content.

    > **Warning**
    >
    > Avoid republishing metadata for repositories with Complete Mirror mirroring policy. This also applies to content views containing repositories with the Complete Mirror mirroring policy.

## 6.7. Updating the default mirroring policy by using Satellite web UI

Set default mirroring policies for new custom repositories so they inherit additive, content-only, or complete mirroring without affecting existing repositories.

Depending on whether it is a Yum or non-Yum custom repository, Satellite uses separate settings. Only Yum repositories support the `mirror_complete` mirroring policy. Red Hat repositories use the `mirror_complete` policy by default and are not affected by these settings. Changing the default value does not change existing mirroring policy settings per repository. For more information on mirroring policies, see [Section 6.6, “Mirroring policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Mirroring_Policies_Overview_content-management "6.6. Mirroring policies overview").

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Click the **Content** tab.
3. Change the default mirroring policy depending on your requirements:

   - To change the default mirroring policy for a Yum custom repository, change the value of the **Default custom yum repository mirroring policy** setting.
   - To change the default mirroring policy for a non-Yum custom repository, change the value of the **Default custom non-yum repository mirroring policy** setting.

## 6.8. Updating the default mirroring policy by using Hammer CLI

Set default mirroring policies for new custom repositories so they inherit additive, content-only, or complete mirroring without affecting existing repositories.

Depending on whether it is a Yum or non-Yum custom repository, Satellite uses separate settings. Only Yum repositories support the `mirror_complete` mirroring policy. Red Hat repositories use the `mirror_complete` policy by default and are not affected by these settings. Changing the default value does not change existing mirroring policy settings per repository. For more information on mirroring policies, see [Section 6.6, “Mirroring policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Mirroring_Policies_Overview_content-management "6.6. Mirroring policies overview").

**Procedure**

- Change the default mirroring policy for a Yum custom repository to `additive`, `mirror_content_only`, or `mirror_complete`:

  ```
  $ hammer settings set \
  --name default_yum_mirroring_policy \
  --value mirror_complete
  ```
- Change the default mirroring policy for a non-Yum custom repository to `additive` or `mirror_content_only`:

  ```
  $ hammer settings set \
  --name default_non_yum_mirroring_policy \
  --value additive
  ```

## 6.9. Updating the mirroring policy for a repository by using Satellite web UI

Update the mirroring policy for an existing repository to control whether synchronization adds content only, mirrors repodata, or removes content deleted upstream.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select the product name.
3. On the **Repositories** tab, click the repository name, locate the **Mirroring Policy** field, and click the edit icon.
4. From the list, select a mirroring policy and click **Save**.

## 6.10. Updating the mirroring policy for a repository by using Hammer CLI

Update the mirroring policy for a specific repository to control whether synchronization adds content only, mirrors repodata, or removes content deleted upstream.

**Procedure**

1. List the repositories for an organization:

   ```
   $ hammer repository list \
   --organization-label My_Organization_Label
   ```
2. Change the mirroring policy for a repository to `additive`, `mirror_complete`, or `mirror_content_only`:

   ```
   $ hammer repository update \
   --id My_Repository_ID \
   --mirroring-policy mirror_complete
   ```

## 6.11. Limiting synchronization concurrency

Adjust per-repository download concurrency when sync jobs fail because upstream servers reject parallel requests, or raise the limit cautiously to improve sync performance.

Increasing the limit may improve performance, but can cause the upstream server to be overloaded or start rejecting requests. If you are seeing repository syncs fail due to the upstream servers rejecting requests, you may want to try lowering the limit.

**Procedure**

- Define a value for synchronization concurrency:

  ```
  $ hammer repository update \
  --download-concurrency 5 \
  --id Repository_ID \
  --organization "My_Organization"
  ```

## 6.12. Limiting growth of synchronized content by using Satellite web UI

Limit how many package versions Satellite keeps in the Library by setting an additive mirroring policy and a retain count, reducing disk growth from repeated synchronizations.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select your product.
3. On the **Repository** tab, select your repository.
4. Set the **Mirroring Policy** to `Additive`.
5. Define the number of retained package versions:

   - Set **Retain package versions** to `1` to only keep the latest synchronized package version on Satellite.
   - Set **Retain package versions** to `2` or higher to keep multiple package versions on Satellite.

**Additional resources**

- [Section 6.6, “Mirroring policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Mirroring_Policies_Overview_content-management "6.6. Mirroring policies overview")

## 6.13. Limiting growth of synchronized content by using Hammer CLI

Limit how many package versions Satellite keeps in the Library by setting an additive mirroring policy and a retain count, reducing disk growth from repeated synchronizations.

**Procedure**

- Configure your repository to retain a limited number of package versions in Satellite:

  ```
  $ hammer repository update \
  --id My_Repository_ID \
  --mirroring-policy additive \
  --retain-package-versions-count My_Package_Versions_Count
  ```

  - Set *My_Package_Versions_Count* to `1` to only keep the latest synchronized package version on Satellite.
  - Set *My_Package_Versions_Count* to `2` or higher to keep multiple package versions on Satellite.

**Additional resources**

- [Section 6.6, “Mirroring policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Mirroring_Policies_Overview_content-management "6.6. Mirroring policies overview")
