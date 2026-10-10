---
title: "Synchronizing content between Satellite Servers"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "11"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Synchronizing_Content_Between_Servers_content-management"
---
# Chapter 11. Synchronizing content between Satellite Servers

In multi-server Satellite deployments, use Inter-Satellite Synchronization to deliver content from upstream to downstream Satellite Servers over a network or through export and import, including the Library environment, content view versions, and individual repositories.

## 11.1. Inter-Satellite Synchronization configurations

Depending on network connectivity between upstream and downstream Satellite Servers, you can synchronize content over HTTPS with network sync or by exporting and importing content when servers are air gapped.

There are two possible ISS configurations of Satellite, depending on how you deployed your infrastructure:

ISS Network Sync
:   If your upstream server can communicate with the downstream server over a network, you can synchronize content over HTTPS.

    Configure your Satellite to synchronize content over a network.

ISS Export Sync
:   If your upstream and downstream servers are air gapped, you can synchronize content by using export and import.

    Configure your Satellite to synchronize content by using export and import.

**Additional resources**

- [Inter-Satellite Synchronization scenarios in *Overview, concepts, and deployment considerations*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#inter-satellite-synchronization-scenarios)
- [Hammer content export fails with "Path '/the/path' is not an allowed export path" in the *Red Hat Knowledgebase*](https://access.redhat.com/solutions/7013903)

## 11.2. Synchronizing a custom repository

To synchronize custom repositories over a network, configure the repositories on the downstream Satellite Server to synchronize from published URLs on the upstream server. Red Hat repositories do not require this configuration.

**Procedure**

1. On the connected Satellite Server, perform the following steps:

   1. In the Satellite web UI, navigate to **Content** > **Products**.
   2. Click on the custom product.
   3. Click on the custom repository.
   4. Copy the **Published At:** URL.
2. On the disconnected Satellite Server, perform the following steps:

   1. Download the `katello-server-ca.crt` file from the connected Satellite Server:

      ```
      # curl http://satellite.example.com/pub/katello-server-ca.crt
      ```
   2. Create an SSL Content Credential with the contents of `katello-server-ca.crt`. For more information on creating an SSL Content Credential, see [Section 3.5.1, “Importing custom SSL certificates by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-web-ui "3.5.1. Importing custom SSL certificates by using Satellite web UI").
   3. In the Satellite web UI, navigate to **Content** > **Products**.
   4. Create your custom product with the following:

      - **Upstream URL**: Paste the link that you copied earlier.
      - **SSL CA Cert**: Select the SSL certificate that was transferred from your connected Satellite Server.

   For more information on creating a custom product, see [Section 3.6.1, “Creating a custom product by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-product-by-using-web-ui "3.6.1. Creating a custom product by using Satellite web UI").

## 11.3. Content synchronization by using export and import

Export content from an upstream Satellite Server and import it into a downstream server when network connectivity is limited or air gapped. Choose an approach based on what content you need to synchronize.

> **Note**
>
> Synchronizing content by using export and import requires the same major version of Satellite on both the downstream and upstream Satellite Servers.
>
> When you are unable to match upstream and downstream Satellite versions, you can use:
>
> - Syncable exports and imports.
> - Inter-Satellite Synchronization (ISS) with your upstream Satellite connected to the internet and your downstream Satellite connected to the upstream Satellite.

### 11.3.1. Using an upstream Satellite Server as a content store

Export Library content from an upstream Satellite Server that serves as a content store and import it on the downstream server that manages content for isolated infrastructure.

**Procedure**

1. On the upstream Satellite Server, perform the following steps:

   1. Ensure that repositories are using the **Immediate** download policy in one of the following ways:

      1. For existing repositories using **On Demand**, change their download policy on the repository details page to **Immediate**.
      2. For new repositories, ensure that the **Default Red Hat Repository download policy** setting is set to **Immediate** before enabling Red Hat repositories, and that the **Default download policy** is set to **Immediate** for custom repositories.
   2. Enable the content that you want to synchronize.

      If you want to sync custom content, first create a custom product and then synchronize repositories.
   3. Synchronize the enabled content:

      1. On the first export, perform a `complete` Library export so that all the synchronized content is exported. This generates content archives that you can later import into one or more downstream Satellite Servers.
      2. Export all future updates on the upstream Satellite Server incrementally. This generates leaner content archives that contain only a recent set of updates. For example, if you enable and synchronize a new repository, the next exported content archive contains content only from the newly enabled repository.
2. On the downstream Satellite Server, perform the following steps:

   1. Bring the content exported from the upstream Satellite Server over to the hard disk.
   2. Place it inside a directory under `/var/lib/pulp/imports/`.
   3. Import the content to an organization.

      You can then manage content using content views or lifecycle environments as you require.

**Additional resources**

- [Section 3.3, “Enabling Red Hat repositories by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-web-ui "3.3. Enabling Red Hat repositories by using Satellite web UI")
- [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview")
- [Section 3.6.1, “Creating a custom product by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-product-by-using-web-ui "3.6.1. Creating a custom product by using Satellite web UI")
- [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc")
- [Section 11.4.1, “Exporting the Library environment”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Exporting_the_Library_Environment_content-management "11.4.1. Exporting the Library environment")
- [Section 11.4.3, “Exporting the Library environment incrementally”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#exporting-the-library-environment-incrementally_content-management "11.4.3. Exporting the Library environment incrementally")
- [Section 11.5.2, “Importing into the Library environment”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Importing_into_the_Library_Environment_content-management "11.5.2. Importing into the Library environment")

### 11.3.2. Using an upstream Satellite Server to synchronize content view versions

Curate updates on the upstream Satellite Server into content views and lifecycle environments, then export promoted content and import it on the downstream server that manages isolated infrastructure.

**Procedure**

1. On the upstream Satellite Server, perform the following steps:

   1. Ensure that repositories are using the **Immediate** download policy in one of the following ways:

      1. For existing repositories using **On Demand**, change their download policy on the repository details page to **Immediate**.
      2. For new repositories, ensure that the **Default Red Hat Repository download policy** setting is set to **Immediate** before enabling Red Hat repositories, and that the **Default download policy** is set to **Immediate** for custom repositories.
   2. Enable the content that you want to synchronize.

      If you want to sync custom content, first create a custom product and then synchronize repositories.
   3. Synchronize the enabled content:

      1. For the first export, perform a `complete` version export on the content view version that you want to export. This generates content archives that you can import into one or more downstream Satellite Servers.
      2. Export all future updates in the connected Satellite Servers incrementally. This generates leaner content archives that contain changes only from the recent set of updates. For example, if your content view has a new repository, this exported content archive contains only the latest changes.
      3. When you have new content, republish the content views that include this content before exporting the increment. This creates a new content view version with the appropriate content to export.
2. On the downstream Satellite Server, perform the following steps:

   1. Bring the content exported from the upstream Satellite Server over to the hard disk.
   2. Place it inside a directory under `/var/lib/pulp/imports/`.
   3. Import the content to the organization that you want. This will create a content view version from the exported content archives and then import content appropriately.

**Additional resources**

- [Section 3.3, “Enabling Red Hat repositories by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-web-ui "3.3. Enabling Red Hat repositories by using Satellite web UI")
- [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview")
- [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc")
- [Section 3.6.1, “Creating a custom product by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-product-by-using-web-ui "3.6.1. Creating a custom product by using Satellite web UI")
- [Chapter 9, *Managing content views and content view environments*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-views-and-content-view-environments "Chapter 9. Managing content views and content view environments")
- [Section 11.4.6, “Exporting a content view version incrementally”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Exporting_a_Content_View_Version_Incrementally_content-management "11.4.6. Exporting a content view version incrementally")
- [Section 11.4.4, “Exporting a content view version”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Exporting_a_Content_View_Version_content-management "11.4.4. Exporting a content view version")
- [Section 11.5.4, “Importing a content view version”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Importing_a_Content_View_Version_content-management "11.5.4. Importing a content view version")

### 11.3.3. Synchronizing a single repository

Export a single repository from the upstream Satellite Server and import it on the downstream server when you need to synchronize only specific content between air-gapped servers.

**Procedure**

1. On the upstream Satellite Server, perform the following steps:

   1. Ensure that the repository is using the **Immediate** download policy in one of the following ways:

      1. For existing repositories using **On Demand**, change their download policy on the repository details page to **Immediate**.
      2. For new repositories, ensure that the **Default Red Hat Repository download policy** setting is set to **Immediate** before enabling Red Hat repositories, and that the **Default download policy** is set to **Immediate** for custom repositories.
   2. Enable the content that you want to synchronize.

      If you want to sync custom content, first create a custom product and then synchronize product repositories.
   3. Synchronize the enabled content:
   4. On the first export, perform a `complete` repository export so that all the synchronized content is exported. This generates content archives that you can later import into one or more downstream Satellite Servers.
   5. Export all future updates on the upstream Satellite Server incrementally. This generates leaner content archives that contain only a recent set of updates.
2. On the downstream Satellite Server, perform the following steps:

   1. Bring the content exported from the upstream Satellite Server over to the hard disk.
   2. Place it inside a directory under `/var/lib/pulp/imports/`.
   3. Import the content to an organization.

      You can then manage content using content views or lifecycle environments as you require.

**Additional resources**

- [Section 3.3, “Enabling Red Hat repositories by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-web-ui "3.3. Enabling Red Hat repositories by using Satellite web UI")
- [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview")
- [Section 3.6.1, “Creating a custom product by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-product-by-using-web-ui "3.6.1. Creating a custom product by using Satellite web UI")
- [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc")
- [Section 11.4.7, “Exporting a repository”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Exporting_a_Repository_content-management "11.4.7. Exporting a repository")
- [Section 11.4.9, “Exporting a repository incrementally”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#exporting-a-repository-incrementally "11.4.9. Exporting a repository incrementally")
- [Section 11.5.6, “Importing a repository”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Importing_a_Repository_content-management "11.5.6. Importing a repository")

## 11.4. Exporting content from Satellite Server

When synchronizing content by using export and import, export the Library environment, content view versions, or individual repositories from the upstream Satellite Server.

### 11.4.1. Exporting the Library environment

You can export all Library content for an organization to an archive file and recreate the same repositories on another Satellite Server or organization.

The exported archive file contains the following data:

- A JSON file containing content view version metadata.
- An archive file containing all the repositories from the Library environment of the organization.

You can export the following content from Satellite Server:

- Ansible collections
- Docker content
- Custom file type content
- Kickstart repositories
- Yum content

**Prerequisites**

- The export directory has enough free storage space to accommodate the export.
- The `/var/lib/pulp/exports/` directory has enough free storage space equivalent to the size of the repositories being exported for temporary files created during the export process.
- Download policy is set to **Immediate** for all repositories within the Library lifecycle environment you export. For more information, see [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview").
- Products that you export are synchronized to the required date.
- The user exporting the content has the *Content Exporter* role.

**Procedure**

1. Export the Library environment for your organization:

   ```
   $ hammer content-export complete library --organization="My_Organization"
   ```

   In many cases the exported archive might be several gigabytes in size. You might want to split it into chunks of a smaller size. You can use the `--chunk-size-gb` option to split the export into smaller chunks, for example `--chunk-size-gb=2` to split the archive into 2 GB chunks.
2. A new content view **Export-Library** is created in the organization. This content view contains all the repositories belonging to this organization. A new version of this content view is published and exported automatically.

**Verification**

- Verify that the archive containing the exported version of a content view is located in the export directory:

  ```
  # ls -lh /var/lib/pulp/exports/My_Organization/Export-Library/1.0/2021-03-02T03-35-24-00-00/
  ```

  You need all three files, the `tar.gz` archive file, the `toc.json` file, and the `metadata.json` file, to import the content successfully.

### 11.4.2. Exporting the Library environment in the syncable format

You can export content in the Library environment of an organization to a syncable format that you can use to create your custom CDN and synchronize the content from the custom CDN over HTTP/HTTPS.

You can then serve the generated content on a local web server and synchronize it on the importing Satellite Server or in another Satellite Server organization.

You can use the generated content to create the same repository in another Satellite Server or in another Satellite Server organization by using content import. On import of the exported archive, a regular content view is created or updated on your importing Satellite Server. For more information, see [Section 11.5.4, “Importing a content view version”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Importing_a_Content_View_Version_content-management "11.5.4. Importing a content view version").

You can export the following content types in the syncable format from Satellite Server:

- Custom file type content
- Kickstart repositories
- Yum content

You cannot export Ansible collections or Docker content in the syncable format.

The export contains directories with the packages, **listing** files, and metadata of the repository in Yum format that can be used to synchronize in the importing Satellite Server.

**Prerequisites**

- Download policy is set to **Immediate** for all repositories within the Library lifecycle environment you export. For more information, see [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview").
- Products that you export are synchronized to the required date.
- The user exporting the content has the *Content Exporter* role.

**Procedure**

1. Use the organization name or ID to export:

   ```
   $ hammer content-export complete library \
   --organization="My_Organization" \
   --format=syncable
   ```
2. Optional: Verify that the exported content is located in the export directory:

   ```
   # du -sh /var/lib/pulp/exports/My_Organization/Export-My_Repository/1.0/2021-03-02T03-35-24-00-00
   ```

### 11.4.3. Exporting the Library environment incrementally

You can export only Library content that changed since the last export to reduce archive size and system resource usage when full Library exports are too large.

Exporting Library content can be a very expensive operation in terms of system resources. Organizations that have multiple Red Hat Enterprise Linux trees can occupy several gigabytes of space on Satellite Server.

In such cases, you can create an incremental export which contains only pieces of content that have changed since the last export. Incremental exports typically result in smaller archive files than the full exports.

You can export the following content from Satellite Server:

- Ansible collections
- Docker content
- Custom file type content
- Kickstart repositories
- Yum content

The example below shows incremental export of all repositories in the organization’s Library.

**Procedure**

1. Create an incremental export:

   ```
   $ hammer content-export incremental library \
   --organization="My_Organization"
   ```

   If you want to create a syncable export, add `--format=syncable`. By default, Satellite creates an importable export.

**Next steps**

- Optional: View the exported data:

  ```
  # find /var/lib/pulp/exports/My_Organization/Export-Library/
  ```

### 11.4.4. Exporting a content view version

You can export a content view version to an archive file and recreate the same version on another Satellite Server. Satellite exports composite content views as regular content views.

The composite nature is not retained. On importing the exported archive, a regular content view is created or updated on your downstream Satellite Server.

The exported archive file contains the following data:

- A JSON file containing content view version metadata
- An archive file containing all the repositories included into the content view version

You can export the following content from Satellite Server:

- Ansible collections
- Docker content
- Custom file type content
- Kickstart repositories
- Yum content

Satellite does not export content view definitions and metadata such as package filters.

**Prerequisites**

- The export directory has enough free storage space to accommodate the export.
- The `/var/lib/pulp/exports/` directory has enough free storage space equivalent to the size of the repositories being exported for temporary files created during the export process.
- Download policy is set to **Immediate** for all repositories within the content view version you export. For more information, see [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview").
- Products that you export are synchronized to the required date.
- The user exporting the content has the *Content Exporter* role.

**Procedure**

1. List versions of the content view that are available for export:

   ```
   $ hammer content-view version list \
   --content-view="My_Content_View" \
   --organization="My_Organization"
   ```

   Note the version number that you want to export. In the following example, the version number is `1.0`.
2. Export the content view version:

   ```
   $ hammer content-export complete version \
   --content-view="Content_View_Name" \
   --version=1.0 \
   --organization="My_Organization"
   ```

   In many cases, the exported archive might be several gigabytes in size. You might want to split it into smaller chunks of a smaller size. You can use the `--chunk-size-gb` option to export the content view version into smaller chunks, for example `--chunk-size-gb=2` to split the archives into 2 GB chunks.

**Verification**

1. Verify that the archive containing the exported version of a content view is located in the export directory:

   ```
   # ls -lh /var/lib/pulp/exports/My_Organization/Content_View_Name/1.0/2021-02-25T18-59-26-00-00/
   ```

   You require all three files, the `tar.gz` archive file, the `toc.json` file, and the `metadata.json` file, to import the content successfully.

### 11.4.5. Exporting a content view version in the syncable format

You can export a content view version in syncable format to serve from a custom CDN over HTTP/HTTPS or import on a matching Satellite version.

After you have exported the content view, you can do either of the following:

- Synchronize the content from your custom CDN over HTTP/HTTPS.
- Import the content using `hammer content-import`. Note that this requires both the Export and Import servers to run Satellite 6.19.

You can import Syncable Format exports directly by using the `hammer content-import` command. This is the recommended method for consuming syncable exports.

Alternatively, you can serve the generated content using a local web server on the importing Satellite Server or in another Satellite Server organization:

- Copy the generated content to an HTTP/HTTPS web server that is accessible to importing Satellite Server.
- Update your CDN configuration to **Custom CDN**.
- Set the CDN URL to point to the web server.
- Optional: Set an SSL/TLS CA Credential if the web server requires it.
- Enable the repository.
- Synchronize the repository.

The export contains directories with the packages, **listing** files, and metadata of the repository in Yum format that can be used to synchronize in the importing Satellite Server.

You can export the following content types in the syncable format from Satellite Server:

- Custom file type content
- Kickstart repositories
- Yum content

You cannot export Ansible collections or Docker content in the syncable format.

**Prerequisites**

- Download policy is set to **Immediate** for all repositories within the content view you export. For more information, see [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview").
- Products that you export are synchronized to the required date.
- The user exporting the content has the *Content Exporter* role.

**Procedure**

1. List versions of the content view that are available for export:

   ```
   $ hammer content-view version list \
   --content-view="My_Content_View_Name" \
   --organization="My_Organization"
   ```

   Note the version number that you want to export. In the following example, the version number is `1.0`.
2. Export the content view version in a syncable format:

   ```
   $ hammer content-export complete version \
   --content-view="My_Content_View_Name" \
   --version=1.0 \
   --organization="My_Organization" \
   --format=syncable
   ```

**Verification**

- Verify that the exported content is located in the export directory:

  ```
  # ls -lh /var/lib/pulp/exports/My_Organization/My_Content_View_Name/1.0/2021-02-25T18-59-26-00-00/
  ```

### 11.4.6. Exporting a content view version incrementally

You can export only the content that changed in a content view version since the last export to reduce archive size when full exports are too resource-intensive.

Exporting complete content view versions can be a very expensive operation in terms of system resources. Content view versions that have multiple Red Hat Enterprise Linux trees can occupy several gigabytes of space on Satellite Server.

In such cases, you can create an incremental export which contains only pieces of content that have changed since the last export. Incremental exports typically result in smaller archive files than the full exports.

You can export the following content from Satellite Server:

- Ansible collections
- Docker content
- Custom file type content
- Kickstart repositories
- Yum content

**Procedure**

1. Create an incremental export:

   ```
   $ hammer content-export incremental version \
   --content-view="My_Content_View" \
   --organization="My_Organization" \
   --version="My_Content_View_Version"
   ```

   If you want to create a syncable export, add `--format=syncable`. By default, Satellite creates an importable export.

**Next steps**

- Optional: View the exported content view:

  ```
  # find /var/lib/pulp/exports/My_Organization/My_Exported_Content_View/My_Content_View_Version/
  ```
- You can import your exported content view version into Satellite Server. For more information, see [Section 11.5.4, “Importing a content view version”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Importing_a_Content_View_Version_content-management "11.5.4. Importing a content view version").

### 11.4.7. Exporting a repository

You can export a repository from the Library environment to an archive file and recreate the same repository on another Satellite Server or organization.

You can export the following content from Satellite Server:

- Ansible collections
- Docker content
- Custom file type content
- Kickstart repositories
- Yum content

The export contains the following data:

- Two JSON files containing repository metadata.
- One or more archive files containing the contents of the repository from the Library environment of the organization.

You need all the files, `tar.gz`, `toc.json` and `metadata.json`, to be able to import.

**Prerequisites**

- The export directory has enough free storage space to accommodate the export.
- The `/var/lib/pulp/exports/` directory has enough free storage space equivalent to the size of the repository that you export.
- Download policy is set to **Immediate** for the repository you export. For more information, see [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview").
- Products that you export are synchronized to the required date.
- The user exporting the content has the *Content Exporter* role.

**Procedure**

1. Export a repository:

   ```
   $ hammer content-export complete repository \
   --name="My_Repository" \
   --product="My_Product" \
   --organization="My_Organization"
   ```

   > **Note**
   >
   > The size of the exported archive depends on the number and size of the packages within the repository. If you want to split the exported archive into chunks, export your repository using the `--chunk-size-gb` argument to limit the size by an integer value in gigabytes, for example `--chunk-size-gb=2`.
2. Optional: Verify that the exported archive is located in the export directory:

   ```
   # ls -lh /var/lib/pulp/exports/My_Organization/Export-My_Repository/1.0/2022-09-02T03-35-24-00-00/
   ```

### 11.4.8. Exporting a repository in the syncable format

You can export the content of a repository in the Library environment of an organization to a syncable format that you can use to create your custom CDN and synchronize the content from the custom CDN over HTTP/HTTPS.

You can import Syncable Format exports directly by using the `hammer content-import` command. This is the recommended method for consuming syncable exports.

Alternatively, you can serve the generated content using a local web server on the importing Satellite Server or in another Satellite Server organization:

- Copy the generated content to an HTTP/HTTPS web server that is accessible to importing Satellite Server.
- Update your CDN configuration to **Custom CDN**.
- Set the CDN URL to point to the web server.
- Optional: Set an SSL/TLS CA Credential if the web server requires it.
- Enable the repository.
- Synchronize the repository.

The export contains directories with the packages, **listing** files, and metadata of the repository in Yum format that can be used to synchronize in the importing Satellite Server.

You can export the following content types in the syncable format from Satellite Server:

- Custom file type content
- Kickstart repositories
- Yum content

You cannot export Ansible collections or Docker content in the syncable format.

**Prerequisites**

- Download policy is set to **Immediate** for the repository you export. For more information, see [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview").
- The user exporting the content has the *Content Exporter* role.

**Procedure**

1. Export a repository using the repository name or ID:

   ```
   $ hammer content-export complete repository \
   --organization="My_Organization" \
   --product="My_Product" \
   --name="My_Repository" \
   --format=syncable
   ```
2. Optional: Verify that the exported content is located in the export directory:

   ```
   # du -sh /var/lib/pulp/exports/My_Organization/Export-My_Repository/1.0/2021-03-02T03-35-24-00-00
   ```

### 11.4.9. Exporting a repository incrementally

You can export only repository content that changed since the previous export to reduce archive size when full repository exports are too large.

Exporting a repository can be a very expensive operation in terms of system resources. A typical Red Hat Enterprise Linux tree may occupy several gigabytes of space on Satellite Server.

In such cases, you can use **Incremental Export** to export only pieces of content that changed since the previous export. Incremental exports typically result in smaller archive files than the full exports.

You can export the following content from Satellite Server:

- Ansible collections
- Docker content
- Custom file type content
- Kickstart repositories
- Yum content

The example below shows incremental export of a repository in the Library lifecycle environment.

**Procedure**

1. Create an incremental export:

   ```
   $ hammer content-export incremental repository \
   --name="My_Repository" \
   --organization="My_Organization" \
   --product="My_Product"
   ```
2. Optional: View the exported data:

   ```
   # ls -lh /var/lib/pulp/exports/My_Organization/Export-My_Repository/3.0/2021-03-02T03-35-24-00-00/
   total 172K
   -rw-r--r--. 1 pulp pulp  20M Mar  2 04:22 export-436882d8-de5a-48e9-a30a-17169318f908-20210302_0422.tar.gz
   -rw-r--r--. 1 pulp pulp  333 Mar  2 04:22 export-436882d8-de5a-48e9-a30a-17169318f908-20210302_0422-toc.json
   -rw-r--r--. 1 root root  492 Mar  2 04:22 metadata.json
   ```

### 11.4.10. Exporting a repository incrementally in the syncable format

You can export only changed repository content in the syncable format to reduce transfer size when serving content from a custom CDN over HTTP/HTTPS.

Exporting a repository can be a very expensive operation in terms of system resources. A typical Red Hat Enterprise Linux tree may occupy several gigabytes of space on Satellite Server.

In such cases, you can use **Incremental Export** to export only pieces of content that changed since the previous export. Incremental exports typically result in smaller archive files than full exports.

You can export the following content types in the syncable format from Satellite Server:

- Custom file type content
- Kickstart repositories
- Yum content

You cannot export Ansible collections or Docker content in the syncable format.

The procedure below shows an incremental export of a repository in the Library lifecycle environment.

**Procedure**

1. Create an incremental export:

   ```
   $ hammer content-export incremental repository \
   --format=syncable \
   --name="My_Repository" \
   --organization="My_Organization" \
   --product="My_Product"
   ```
2. Optional: View the exported data:

   ```
   # find /var/lib/pulp/exports/Default_Organization/My_Product/2.0/2023-03-09T10-55-48-05-00/ -name "*.rpm"
   ```

### 11.4.11. Keeping track of your exports

Query and manage export records on the upstream Satellite Server to organize incremental exports and track which content was exported to specific downstream servers.

**Procedure**

1. Optional: Track the destinations of content exports. Use the `--destination-server` argument during export to indicate the target server. This option is available for all `content-export` operations.

   For example, specify the destination server when exporting a content view version:

   ```
   $ hammer content-export complete version \
   --content-view="My_Content_View_Name" \
   --destination-server=My_Downstream_Server_1 \
   --organization="My_Organization" \
   --version=1.0
   ```
2. Query export records by listing the exports:

   ```
   $ hammer content-export list \
   --organization="My_Organization"
   ```

## 11.5. Importing exported content

When synchronizing content by using export and import, import exported content into the downstream Satellite Server Library environment, content view versions, or individual repositories.

### 11.5.1. Importing exports in the syncable format

Import syncable exports from an allowed import path on your downstream Satellite Server into the Library environment.

**Prerequisites**

- The syncable exports must be located in one of your `ALLOWED_IMPORT_PATHS` as specified in `/etc/pulp/settings.py`. By default, this includes `/var/lib/pulp/imports/`.
- The importing organization must be configured to synchronize content through exports. For more information, see [Configuring Satellite Server to synchronize content through exports by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#configuring-project-server-to-synchronize-content-through-exports-by-using-web-ui) in *Installing Satellite Server in a disconnected network environment*.

**Procedure**

- Import the syncable exports into the Library environment of your organization:

  ```
  $ hammer content-import library \
  --organization="My_Organization" \
  --path="My_Path_To_Syncable_Export"
  ```

### 11.5.2. Importing into the Library environment

You can import exported Library content into the Library environment of an organization on a downstream Satellite Server.

**Prerequisites**

- The exported files must be in a directory under `/var/lib/pulp/imports`.
- The importing organization must be configured to synchronize content through exports. For more information, see [Configuring Satellite Server to synchronize content through exports by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#configuring-project-server-to-synchronize-content-through-exports-by-using-web-ui) in *Installing Satellite Server in a disconnected network environment*.
- If there are any Red Hat repositories in the exported content, the subscription manifest of the importing organization must contain subscriptions for the products contained within the export.
- The user importing the content has the *Content Importer* role.

**Procedure**

1. Copy the exported files to a subdirectory of `/var/lib/pulp/imports` on Satellite Server where you want to import.
2. Set the ownership of the import directory and its contents to `pulp:pulp`.

   ```
   # chown -R pulp:pulp /var/lib/pulp/imports/2021-03-02T03-35-24-00-00/
   ```
3. Verify that the ownership is set correctly:

   ```
   # ls -lh /var/lib/pulp/imports/2021-03-02T03-35-24-00-00
   total 68M
   -rw-r--r--. 1 pulp pulp 68M Mar  2 04:29 export-1e25417c-6d09-49d4-b9a5-23df4db3d52a-20210302_0335.tar.gz
   -rw-r--r--. 1 pulp pulp 333 Mar  2 04:29 export-1e25417c-6d09-49d4-b9a5-23df4db3d52a-20210302_0335-toc.json
   -rw-r--r--. 1 pulp pulp 443 Mar  2 04:29 metadata.json
   ```
4. Identify the Organization that you want to import into.
5. Import the Library content to Satellite Server:

   ```
   $ hammer content-import library \
   --organization="My_Organization" \
   --path=/var/lib/pulp/imports/2021-03-02T03-35-24-00-00/
   ```

   You must specify the absolute path as in the example: `/var/lib/pulp/imports/2021-03-02T03-35-24-00-00/`. Relative paths do not work.
6. Verify that you imported the Library content by checking the contents of the product and repositories. A new content view called `Import-Library` is created in the target organization. This content view is used to facilitate the Library content import.

   By default, this content view is not shown in the Satellite web UI. `Import-Library` is not meant to be assigned directly to hosts. Instead, assign your hosts to `Default Organization View` or another content view as you would normally.

   The importing Satellite Server extracts the `/var/lib/pulp/imports` directory to `/var/lib/pulp/`.
7. Delete the import files after a successful import:

   ```
   # rm -fr /var/lib/pulp/imports/2021-03-02T03-35-24-00-00/
   ```

### 11.5.3. Importing into the Library environment from a web server

You can import exported Library content directly from a web server into the Library environment on a downstream Satellite Server when exports are in syncable format.

**Prerequisites**

- The exported files must be in the syncable format.
- The exported files must be accessible through HTTP/HTTPS.
- If there are any Red Hat repositories in the exported content, the subscription manifest of the importing organization must contain subscriptions for the products contained within the export.
- The user importing the content has the *Content Importer* role.

**Procedure**

1. Identify the Organization that you want to import into.
2. To import the Library content to Satellite Server, enter the following command:

   ```
   $ hammer content-import library \
   --organization="My_Organization" \
   --path=http://server.example.com/pub/exports/2021-02-25T21-15-22-00-00/
   ```

   A new content view called `Import-Library` is created in the target organization. This content view is used to facilitate the Library content import.

   By default, this content view is not shown in the Satellite web UI. `Import-Library` is not meant to be assigned directly to hosts. Instead, assign your hosts to `Default Organization View` or another content view.

### 11.5.4. Importing a content view version

You can import an exported content view version to recreate the same content in an organization on a downstream Satellite Server.

When you import a content view version, it has the same major and minor version numbers and contains the same repositories with the same packages and errata. Custom repositories, products and content views are automatically created if they do not exist in the importing organization.

**Prerequisites**

- The exported files must be in a directory under `/var/lib/pulp/imports`.
- The importing organization must be configured to synchronize content through exports. For more information, see [Configuring Satellite Server to synchronize content through exports by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#configuring-project-server-to-synchronize-content-through-exports-by-using-web-ui) in *Installing Satellite Server in a disconnected network environment*.
- If there are any Red Hat repositories in the exported content, the subscription manifest of the importing organization must contain subscriptions for the products contained within the export.
- The user importing the content view version has the *Content Importer* role.

**Procedure**

1. Copy the exported files to a subdirectory of `/var/lib/pulp/imports` on Satellite Server where you want to import.
2. Set the ownership of the import directory and its contents to `pulp:pulp`:

   ```
   # chown -R pulp:pulp /var/lib/pulp/imports/2021-02-25T21-15-22-00-00/
   ```
3. Verify that the ownership is set correctly:

   ```
   # ls -lh /var/lib/pulp/imports/2021-02-25T21-15-22-00-00/
   ```
4. Import the content view version to Satellite Server:

   ```
   $ hammer content-import version \
   --organization=My_Organization \
   --path=/var/lib/pulp/imports/2021-02-25T21-15-22-00-00/
   ```

   You must specify the absolute path as in the example: `/var/lib/pulp/imports/2021-02-25T21-15-22-00-00/`. Relative paths do not work.
5. Verify that you imported the content view version successfully by listing the content view versions for your organization:

   ```
   $ hammer content-view version list \
   --organization-id=My_Organization_ID
   ```

   The importing Satellite Server extracts the `/var/lib/pulp/imports` directory to `/var/lib/pulp/`.
6. Delete the import files after a successful import:

   ```
   # rm -fr /var/lib/pulp/imports/2021-02-25T21-15-22-00-00/
   ```

### 11.5.5. Importing a content view version from a web server

You can import an exported content view version directly from a web server when the export is in syncable format and accessible over HTTP/HTTPS.

When you import a content view version, it has the same major and minor version numbers and contains the same repositories with the same packages and errata. Custom repositories, products, and content views are automatically created if they do not exist in the importing organization.

**Prerequisites**

- The exported files must be in a syncable format.
- The exported files must be accessible through HTTP/HTTPS.
- If there are any Red Hat repositories in the exported content, the importing organization’s manifest must contain subscriptions for the products contained within the export.
- The user importing the content view version must have the *Content Importer* role.

**Procedure**

- Import the content view version into Satellite Server:

  ```
  $ hammer content-import version \
  --organization=My_Organization \
  --path=http://server.example.com/pub/exports/2021-02-25T21-15-22-00-00/
  ```

### 11.5.6. Importing a repository

You can import an exported repository into an organization on a downstream Satellite Server to match content from the upstream server.

**Prerequisites**

- The exported files must be in a directory under `/var/lib/pulp/imports/`.
- The importing organization must be configured to synchronize content through exports. For more information, see [Configuring Satellite Server to synchronize content through exports by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#configuring-project-server-to-synchronize-content-through-exports-by-using-web-ui) in *Installing Satellite Server in a disconnected network environment*.
- If the export contains any Red Hat repositories, the subscription manifest of the importing organization must contain subscriptions for the products contained within the export.
- The user importing the content has the *Content Importer* role.

**Procedure**

1. Copy the exported files to a subdirectory of `/var/lib/pulp/imports` on Satellite Server where you want to import.
2. Set the ownership of the import directory and its contents to `pulp:pulp`:

   ```
   # chown -R pulp:pulp /var/lib/pulp/imports/2021-03-02T03-35-24-00-00/
   ```
3. Verify that the ownership is set correctly:

   ```
   # ls -lh /var/lib/pulp/imports/2021-03-02T03-35-24-00-00
   total 68M
   -rw-r--r--. 1 pulp pulp 68M Mar  2 04:29 export-1e25417c-6d09-49d4-b9a5-23df4db3d52a-20210302_0335.tar.gz
   -rw-r--r--. 1 pulp pulp 333 Mar  2 04:29 export-1e25417c-6d09-49d4-b9a5-23df4db3d52a-20210302_0335-toc.json
   -rw-r--r--. 1 pulp pulp 443 Mar  2 04:29 metadata.json
   ```
4. Identify the Organization that you want to import into.
5. Import the repository content into Satellite Server:

   ```
   $ hammer content-import repository \
   --organization="My_Organization" \
   --path=/var/lib/pulp/imports/2021-03-02T03-35-24-00-00/
   ```

   You must specify the absolute path as in the example: `/var/lib/pulp/imports/2021-03-02T03-35-24-00-00`. Relative paths do not work.
6. Verify that you imported the repository by checking the contents of the product and repository. The importing Satellite Server extracts the `/var/lib/pulp/imports` directory to `/var/lib/pulp/`.
7. Delete the import files after a successful import:

   ```
   # rm -fr /var/lib/pulp/imports/2021-03-02T03-35-24-00-00/
   ```

### 11.5.7. Importing a repository from a web server

You can import an exported repository directly from a web server when the export is in syncable format and accessible over HTTP/HTTPS.

**Prerequisites**

- The exported files must be in a syncable format.
- The exported files must be accessible through HTTP/HTTPS.
- If the export contains any Red Hat repositories, the subscription manifest of the importing organization must contain subscriptions for the products contained within the export.
- The user importing the content has the *Content Importer* role.

**Procedure**

1. Select the organization into which you want to import.
2. Import the repository to Satellite Server:

   ```
   $ hammer content-import repository \
   --organization="My_Organization" \
   --path=http://server.example.com/pub/exports/2021-02-25T21-15-22-00-00/
   ```

## 11.6. Hammer CLI cheat sheet for exporting and importing content

Use these Hammer CLI commands as a quick reference when exporting and importing content between Satellite Servers.

Table 11.1. Export

| Intent | Command |
| --- | --- |
| Fully export an Organization’s Library | `hammer content-export complete library --organization="My_Organization"` |
| Incrementally export an Organization’s Library (assuming you have exported something previously) | `hammer content-export incremental library --organization="My_Organization"` |
| Fully export a content view version | `hammer content-export complete version --content-view="My_Content_View" --version=1.0 --organization="My_Organization"` |
| Export a content view version promoted to the Dev Environment | `hammer content-export complete version --content-view="My_Content_View" --organization="My_Organization" --lifecycle-environment="Dev"` |
| Export a content view in smaller chunks (2-GB slabs) | `hammer content-export complete version --content-view="My_Content_View" --version=1.0 --organization="My_Organization" --chunk-size-gb=2` |
| Incrementally export a content view version (assuming you have exported something previously) | `hammer content-export incremental version --content-view="My_Content_View" --version=2.0 --organization="My_Organization"` |
| Fully export a Repository | `hammer content-export complete repository --product="My_Product" --name="My_Repository" --organization="My_Organization"` |
| Incrementally export a Repository (assuming you have exported something previously) | `hammer content-export incremental repository --product="My_Product" --name="My_Repository" --organization="My_Organization"` |
| List exports | `hammer content-export list --content-view="My_Content_View" --organization="My_Organization"` |

Table 11.2. Import

| Intent | Command |
| --- | --- |
| Import into an Organization’s Library | `hammer content-import library --organization="My_Organization" --path="/var/lib/pulp/imports/My_Exported_Library_Dir"` |
| Import to a content view version | `hammer content-import version --organization="My_Organization" --path="/var/lib/pulp/imports/My_Exported_Version_Dir"` |
| Import a Repository | `hammer content-import repository --organization="My_Organization" --path="/var/lib/pulp/imports/My_Exported_Repo_Dir"` |
