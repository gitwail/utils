---
title: "Recovering corrupted content"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#recovering-corrupted-content"
---
# Chapter 10. Recovering corrupted content

Resynchronize corrupted repositories on Satellite Server, verify checksums on Capsule Servers, and republish repository or content view metadata when the repository metadata no longer matches stored content.

**Additional resources**

- [Section 4.5, “Advanced synchronization options”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#advanced-synchronization-options "4.5. Advanced synchronization options")

## 10.1. Recovering a corrupted repository by using Satellite web UI

Recover a corrupted repository with optimized or complete advanced sync, and optionally verify content checksums to confirm packages match upstream sources.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select the product containing the corrupted repository.
3. Select the name of a repository you want to synchronize.
4. To perform optimized sync or complete sync, select **Advanced Sync** from the **Select Action** menu.
5. Select the required option and click **Sync**.
6. Optional: To verify the checksum for a Yum repository, click **Verify Content Checksum** from the **Select Action** menu.

**Additional resources**

- [Section 4.5, “Advanced synchronization options”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#advanced-synchronization-options "4.5. Advanced synchronization options")

## 10.2. Recovering a corrupted repository by using Hammer CLI

Recover a corrupted repository by using optimized sync, complete sync, or validate-content synchronization when packages or metadata no longer match expected content.

**Procedure**

1. Obtain a list of repository IDs:

   ```
   $ hammer repository list \
   --organization "My_Organization"
   ```
2. Synchronize a corrupted repository using the necessary option:

   - For the optimized synchronization:

     ```
     $ hammer repository synchronize \
     --id My_ID
     ```
   - For the complete synchronization:

     ```
     $ hammer repository synchronize \
     --id My_ID \
     --skip-metadata-check true
     ```
   - For validating content of a Yum repository:

     ```
     $ hammer repository synchronize \
     --id My_ID \
     --validate-contents true
     ```

**Additional resources**

- [Section 4.5, “Advanced synchronization options”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#advanced-synchronization-options "4.5. Advanced synchronization options")

## 10.3. Recovering corrupted content on a Capsule Server by using Satellite web UI

Verify checksums for a lifecycle environment or content view on your Capsule Server when hosts cannot consume content and you need to repair corrupted files on the Capsule Server.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
2. Select your Capsule Server.
3. Recover corrupted content on your Capsule Server.

   - To repair content in a lifecycle environment, click the options menu icon next to your lifecycle environment and select **Verify Content Checksum**.
   - To repair content in a content view, click the options menu icon next to your content view and select **Verify Content Checksum**.

**Verification**

1. In the Satellite web UI, navigate to **Monitor** > **Satellite Tasks** > **Tasks**.
2. Search for `Verify checksum for content`.
3. Verify that the task completed successfully.

## 10.4. Recovering corrupted content on a Capsule Server by using CLI

Verify checksums on your Capsule Server for a repository, content view, lifecycle environment, or all Capsule Server content when hosts cannot consume synchronized packages.

**Prerequisites**

- The lifecycle environment, content view, or repository that you want to repair is available on the Capsule Server.

**Procedure**

1. Display a list of all Capsules:

   ```
   $ hammer capsule list
   ```

   Note the ID of your Capsule Server.
2. Recover corrupted content on your Capsule Server:

   - Repair content in a content view:

     ```
     $ hammer capsule content verify-checksum \
     --content-view-id My_Content_View_ID \
     --id My_Capsule_Server_ID \
     --organization-id My_Organization_ID
     ```
   - Repair content in a lifecycle environment:

     ```
     $ hammer capsule content verify-checksum \
     --id My_Capsule_Server_ID \
     --lifecycle-environment-id My_Lifecycle_Environment_ID \
     --organization-id My_Organization_ID
     ```
   - Repair content in a repository:

     ```
     $ hammer capsule content verify-checksum \
     --id My_Capsule_Server_ID \
     --organization-id My_Organization_ID \
     --repository-id My_Repository_ID
     ```
   - Repair all content on your Capsule Server:

     ```
     $ hammer capsule content verify-checksum \
     --id My_Capsule_Server_ID
     ```

**Verification**

- Verify that the task completed successfully:

  ```
  $ hammer task list --search "Verify checksum for content"
  ```

## 10.5. Republishing repository metadata by using Satellite web UI

Republish repository metadata when published metadata does not match repository contents.

> **Warning**
>
> Red Hat recommends a complete repository sync or publishing a new content view version to repair broken metadata instead.

**Prerequisites**

- The mirroring policy of the repository is not set to **Complete Mirroring**. For more information, see [Section 6.6, “Mirroring policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Mirroring_Policies_Overview_content-management "6.6. Mirroring policies overview").

  This action is not available for repositories that use the **Complete Mirroring** policy because the metadata is copied verbatim from the upstream source of the repository.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select the product that includes the repository for which you want to republish metadata.
3. On the **Repositories** tab, select a repository.
4. To republish metadata for the repository, click **Republish Repository Metadata** from the **Select Action** menu.

## 10.6. Republishing repository metadata by using CLI

Republish repository metadata when published metadata does not match repository contents.

> **Warning**
>
> Red Hat recommends a complete repository sync or publishing a new content view version to repair broken metadata in favor of republishing repository metadata.

**Prerequisites**

- The mirroring policy of the repository is not set to **Complete Mirroring**. For more information, see [Section 6.6, “Mirroring policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Mirroring_Policies_Overview_content-management "6.6. Mirroring policies overview").

  This action is not available for repositories that use the **Complete Mirroring** policy because the metadata is copied verbatim from the upstream source of the repository.

**Procedure**

- Republish metadata for your repository:

  ```
  $ hammer repository verify-checksum \
  --name "My_Repository_Name" \
  --organization-id My_Organization_ID \
  --product "My_Product_Name"
  ```

**Verification**

- Verify that the task completed successfully:

  ```
  $ hammer task list --search "Metadata generate repository"
  ```

## 10.7. Republishing content view metadata by using Satellite web UI

Republish content view version metadata when hosts report checksum mismatches. Satellite can regenerate metadata for repositories that do not use complete mirroring.

Republishing regenerates metadata for all repositories in the content view version that do not adhere to the **Complete Mirroring** policy.

**Prerequisites**

- The content view version includes repositories that do not use the **Complete Mirroring** policy.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Select a content view.
3. On the **Versions** tab, select a content view version.
4. To republish metadata for the content view version, click **Republish repository metadata** from the options icon.

## 10.8. Republishing content view metadata by using CLI

Republish content view version metadata when hosts report checksum mismatches. Satellite can regenerate metadata for repositories that do not use complete mirroring.

Republishing regenerates metadata for all repositories in the content view version that do not adhere to the **Complete Mirroring** policy.

**Prerequisites**

- The content view version includes repositories that do not use the **Complete Mirroring** policy.

**Procedure**

- Republish metadata for your content view version:

  ```
  $ hammer content-view version verify-checksum --id My_Content_View_Version_ID
  ```

**Verification**

- Verify that the task completed successfully:

  ```
  $ hammer task list --search "Verify checksum of repositories in"
  ```
