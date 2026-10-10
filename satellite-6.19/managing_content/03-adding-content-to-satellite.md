---
title: "Adding content to Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite"
---
# Chapter 3. Adding content to Satellite

Start adding content to Satellite by organizing products and repositories, securing upstream connections, and synchronizing or uploading packages for your hosts.

## 3.1. Products and repositories in Satellite

Products group related repositories in Satellite. Each repository stores packages or other content that you synchronize from upstream or upload directly.

Both Red Hat content and custom content in Satellite have similarities:

- The relationship between a product and its repositories is the same and the repositories still require synchronization.
- Custom products require a subscription for hosts to access, similar to subscriptions to Red Hat products. Satellite creates a subscription for each custom product you create.

Red Hat content is already organized into products. For example, Red Hat Enterprise Linux Server is a *product* in Satellite. The repositories for that product consist of different versions, architectures, and add-ons. For Red Hat repositories, products are created automatically after enabling the repository.

Other content can be organized into custom products however you want. For example, you might create an EPEL (Extra Packages for Enterprise Linux) Product and add an "EPEL 7 x86_64" repository to it.

**Additional resources**

- [*Packaging and distributing software* in Red Hat Enterprise Linux 10 documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/packaging_and_distributing_software/index)
- [Section 3.3, “Enabling Red Hat repositories by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-web-ui "3.3. Enabling Red Hat repositories by using Satellite web UI")

## 3.2. Best practices for products and repositories

Follow these recommendations when you organize products and repositories in Satellite to simplify content views and avoid synchronization issues.

- Use one content type per product and content view, for example, yum content only.
- Make file repositories available over HTTP. If you set **Protected** to true, you can only download content using a global debugging certificate.
- Automate the creation of multiple products and repositories by using a Hammer script or an [Ansible Playbook](https://theforeman.github.io/foreman-ansible-modules/develop/index.html).
- For Red Hat content, import your Red Hat manifest into Satellite. For more information, see [Chapter 2, *Managing Red Hat subscriptions*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Red_Hat_Subscriptions_content-management "Chapter 2. Managing Red Hat subscriptions").
- Avoid uploading content to repositories with an **Upstream URL**. Instead, create a repository to synchronize content and upload content to without setting an **Upstream URL**.

  If you upload content to a repository that already synchronizes another repository, the content might be overwritten, depending on the mirroring policy and content type.

## 3.3. Enabling Red Hat repositories by using Satellite web UI

Enable the Red Hat repositories that match the release and architecture of your hosts so Satellite can synchronize the content from the Red Hat CDN.

To select the repositories to synchronize, you must first identify the product that contains the repository, and then enable that repository based on the relevant release version and base architecture.

**Prerequisites**

- If outside network access requires usage of an HTTP proxy, a default HTTP proxy for your Satellite Server is configured. For more information, see [Adding a default HTTP proxy by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#adding-a-default-http-proxy-by-using-web-ui).
- Your Red Hat subscription manifest is imported to your organization and contains subscriptions. For more information, see [Section 2.2, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-red-hat-subscription-manifests-into-satellite "2.2. Importing Red Hat subscription manifests into Satellite").

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Red Hat Repositories**.
2. From the package type list, select the required package types, such as RPM or Kickstart.
3. To find repositories, either enter the repository name, or toggle the **Recommended Repositories** button to the on position to view a list of repositories that you require.
4. In the **Available Repositories** pane, click a repository to expand the repository set.
5. Click the **Enable** icon next to the base architecture and release version that you want.

**Next steps**

- [Chapter 4, *Synchronizing content to Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-content-to-satellite "Chapter 4. Synchronizing content to Satellite")

**Additional resources**

- [Appendix A, *Required Red Hat repositories*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#required-red-hat-repositories "Appendix A. Required Red Hat repositories")

## 3.4. Enabling Red Hat repositories by using Hammer CLI

Enable the Red Hat repositories that match the release and architecture of your hosts so Satellite can synchronize the content from the Red Hat CDN.

To select the repositories to synchronize, you must first identify the product that contains the repository, and then enable that repository based on the relevant release version and base architecture.

**Prerequisites**

- If outside network access requires usage of an HTTP proxy, a default HTTP proxy for your Satellite Server is configured. For more information, see [Adding a default HTTP proxy by using Hammer CLI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#adding-a-default-http-proxy-by-using-cli).
- Your Red Hat subscription manifest is imported to your organization and contains subscriptions. For more information, see [Section 2.2, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-red-hat-subscription-manifests-into-satellite "2.2. Importing Red Hat subscription manifests into Satellite").

**Procedure**

1. Search for your product:

   ```
   $ hammer product list --organization "My_Organization"
   ```
2. List the repository set for the product:

   ```
   $ hammer repository-set list \
   --product "Red Hat Enterprise Linux Server" \
   --organization "My_Organization"
   ```
3. Enable the repository using either the name or ID number. Include the release version, such as `7Server`, and base architecture, such as `x86_64`.

   ```
   $ hammer repository-set enable \
   --name "Red Hat Enterprise Linux 7 Server (RPMs)" \
   --releasever "7Server" \
   --basearch "x86_64" \
   --product "Red Hat Enterprise Linux Server" \
   --organization "My_Organization"
   ```

**Next steps**

- [Chapter 4, *Synchronizing content to Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-content-to-satellite "Chapter 4. Synchronizing content to Satellite")

**Additional resources**

- [Appendix A, *Required Red Hat repositories*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#required-red-hat-repositories "Appendix A. Required Red Hat repositories")

## 3.5. Authenticating and securing content with content credentials

Upstream content often uses HTTPS and signed metadata or packages. Import SSL certificates when upstream servers use custom or private certificate authorities so Satellite can connect securely. Import GPG keys so registered hosts can verify signatures on Yum content when they consume content from Satellite.

### 3.5.1. Importing custom SSL certificates by using Satellite web UI

Import SSL certificates and keys into content credentials before synchronizing custom content from upstream servers that use HTTPS or client authentication. This might include client certificates and keys or CA certificates.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Content Credentials**. In the Content Credentials window, click **Create Content Credential**.
2. In the **Name** field, enter a name for your SSL certificate.
3. From the **Type** list, select **SSL Certificate**.
4. In the **Content Credentials Content** field, paste your SSL certificate, or click **Browse** to upload your SSL certificate.
5. Click **Save**.

### 3.5.2. Importing custom SSL certificates by using Hammer CLI

Import SSL certificates and keys into content credentials before synchronizing custom content from upstream servers that use HTTPS or client authentication. This might include client certificates and keys or CA certificates.

**Procedure**

1. Copy the SSL certificate to your Satellite Server:

   ```
   $ scp My_SSL_Certificate root@satellite.example.com:~/.
   ```

   Or download the SSL certificate to your Satellite Server from an online source:

   ```
   $ wget -P ~ http://upstream-satellite.example.com/pub/katello-server-ca.crt
   ```
2. Upload the SSL Certificate to Satellite:

   ```
   $ hammer content-credential create \
   --content-type cert \
   --name "My_SSL_Certificate" \
   --organization "My_Organization" \
   --path ~/My_SSL_Certificate
   ```

### 3.5.3. Extracting GPG keys from RPM packages

Extract GPG public keys from vendor RPM packages without installing them when upstream repositories ship keys inside a release package.

**Prerequisites**

- You know the download URL for the RPM that ships the vendor GPG keys.

**Procedure**

1. Download the RPM to your local machine:

   ```
   $ wget http://www.example.com/9.5/example-9.5-2.noarch.rpm
   ```
2. Extract the RPM file without installing it:

   ```
   $ rpm2cpio example-9.5-2.noarch.rpm | cpio -idmv
   ```
3. Locate the GPG public key files under the extracted `etc/pki/rpm-gpg/` directory, for example `etc/pki/rpm-gpg/RPM-GPG-KEY-EXAMPLE-95`.

**Next steps**

- Use the extracted key file when you import a custom GPG key into Satellite. For more information, see [Section 3.5.4, “Importing a custom GPG key by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-a-custom-gpg-key-by-using-web-ui "3.5.4. Importing a custom GPG key by using Satellite web UI").

### 3.5.4. Importing a custom GPG key by using Satellite web UI

Import a vendor GPG key into Satellite so hosts validate signatures when they install signed custom content from authorized sources.

Red Hat content is already configured with the appropriate GPG key and thus GPG Key management of Red Hat repositories is not supported.

**Prerequisites**

- You have a copy of the GPG key used to sign the RPM content that you want to use and manage in Satellite. Most RPM distribution vendors provide their GPG Key on their website. You can also extract GPG key files from an RPM package. For more information, see [Section 3.5.3, “Extracting GPG keys from RPM packages”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#extracting-gpg-keys-from-rpm-packages "3.5.3. Extracting GPG keys from RPM packages").

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Content Credentials**.
2. Click **Create Content Credential**.
3. Enter the name of your repository and select **GPG Key** from the **Type** list.
4. Either paste the GPG key into the **Content Credential Contents** field, or click **Browse** and select the GPG key file that you want to import.

   If your custom repository contains content signed by multiple GPG keys, you must enter all required GPG keys in the **Content Credential Contents** field with new lines between each key, for example:

   ```
   -----BEGIN PGP PUBLIC KEY BLOCK-----

   mQINBFy/HE4BEADttv2TCPzVrre+aJ9f5QsR6oWZMm7N5Lwxjm5x5zA9BLiPPGFN
   4aTUR/g+K1S0aqCU+ZS3Rnxb+6fnBxD+COH9kMqXHi3M5UNzbp5WhCdUpISXjjpU
   XIFFWBPuBfyr/FKRknFH15P+9kLZLxCpVZZLsweLWCuw+JKCMmnA
   =F6VG
   -----END PGP PUBLIC KEY BLOCK-----

   -----BEGIN PGP PUBLIC KEY BLOCK-----

   mQINBFw467UBEACmREzDeK/kuScCmfJfHJa0Wgh/2fbJLLt3KSvsgDhORIptf+PP
   OTFDlKuLkJx99ZYG5xMnBG47C7ByoMec1j94YeXczuBbynOyyPlvduma/zf8oB9e
   Wl5GnzcLGAnUSRamfqGUWcyMMinHHIKIc1X1P4I=
   =WPpI
   -----END PGP PUBLIC KEY BLOCK-----
   ```
5. Click **Save**.

### 3.5.5. Importing a custom GPG key by using Hammer CLI

Import a vendor GPG key into Satellite so hosts validate signatures when they install signed custom content from authorized sources.

Red Hat content is already configured with the appropriate GPG key and thus GPG Key management of Red Hat repositories is not supported.

**Prerequisites**

- You have a copy of the GPG key used to sign the RPM content that you want to use and manage in Satellite. Most RPM distribution vendors provide their GPG Key on their website. You can also extract GPG key files from an RPM package. For more information, see [Section 3.5.3, “Extracting GPG keys from RPM packages”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#extracting-gpg-keys-from-rpm-packages "3.5.3. Extracting GPG keys from RPM packages").

**Procedure**

1. Copy the GPG key to your Satellite Server:

   ```
   $ scp ~/etc/pki/rpm-gpg/RPM-GPG-KEY-EXAMPLE-95 root@satellite.example.com:~/.
   ```
2. Upload the GPG key to Satellite:

   ```
   $ hammer content-credentials create \
   --content-type gpg_key \
   --name "My_GPG_Key" \
   --organization "My_Organization" \
   --path ~/RPM-GPG-KEY-EXAMPLE-95
   ```

## 3.6. Creating custom products

A product in Satellite groups related repositories. Create a custom product before you add custom repositories.

### 3.6.1. Creating a custom product by using Satellite web UI

Create a custom product to group repositories you add manually before you define custom repositories or upload packages.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**, click **Create Product**.
2. In the **Name** field, enter a name for the product. Satellite automatically completes the **Label** field based on what you have entered for **Name**.
3. Optional: From the **GPG Key** list, select the GPG key for the product.
4. Optional: From the **SSL CA Cert** list, select the SSL CA certificate for the product.
5. Optional: From the **SSL Client Cert** list, select the SSL client certificate for the product.
6. Optional: From the **SSL Client Key** list, select the SSL client key for the product.
7. Optional: From the **Sync Plan** list, select an existing sync plan or click **Create Sync Plan** and create a sync plan for your product requirements.
8. In the **Description** field, enter a description of the product.
9. Click **Save**.

### 3.6.2. Creating a custom product by using Hammer CLI

Create a custom product to group repositories you add manually before you define custom repositories or upload packages.

**Procedure**

- Create a product:

  ```
  $ hammer product create \
  --name "My_Name" \
  --organization-id My_Organization_ID
  ```

## 3.7. Creating custom repositories

Repositories hold synchronized or uploaded content for a product. Add repository definitions for custom Yum content, then synchronize or upload packages as required.

### 3.7.1. Adding custom RPM repositories by using Satellite web UI

Add custom RPM repositories from an upstream URL to distribute Yum content to your hosts. Use Repo Discovery to import multiple repositories from one source.

> **Note**
>
> Red Hat does not support the upstream RPMs directly from third-party sites. These RPMs are used to demonstrate the synchronization process. For any issues with these RPMs, contact the third-party developers.

The **Products** window in the Satellite web UI also provides a **Repo Discovery** function that finds all repositories from a URL and you can select which ones to add to your custom product. For example, you can use the **Repo Discovery** to search `https://download.postgresql.org/pub/repos/yum/16/redhat/` and list all repositories for different Red Hat Enterprise Linux versions and architectures. This helps you save time importing multiple repositories from a single source.

**Prerequisites**

- You have imported the GPG key that you want to use to verify signatures of the RPM packages. For more information, see [Section 3.5.4, “Importing a custom GPG key by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-a-custom-gpg-key-by-using-web-ui "3.5.4. Importing a custom GPG key by using Satellite web UI").

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products** and select the product that you want to use, and then click **New Repository**.
2. In the **Name** field, enter a name for the repository. Satellite automatically completes the **Label** field based on what you have entered for **Name**.
3. Optional: In the **Description** field, enter a description for the repository.
4. From the **Type** list, select `yum` as type of repository.
5. Optional: From the **Restrict to Architecture** list, select an architecture. If you want to make the repository available to all hosts regardless of the architecture, ensure to select **No restriction**.
6. Optional: From the **Restrict to OS Version** list, select the operating system version. If you want to make the repository available to all hosts regardless of the operating system version, ensure to select **No restriction**.
7. Optional: In the **Upstream URL** field, enter the URL of the external repository to use as a source. Satellite supports three protocols: `http://`, `https://`, and `file://`. If you are using a `file://` repository, you have to place it under `/var/lib/pulp/sync_imports/` directory.

   If you do not enter an upstream URL, you can manually upload packages.
8. Optional: Check the **Ignore SRPMs** checkbox to exclude source RPM packages from being synchronized to Satellite.
9. Optional: Check the **Ignore treeinfo** checkbox if you receive the error `Treeinfo file should have INI format`. All files related to Kickstart will be missing from the repository if `treeinfo` files are skipped.
10. Select the **Verify SSL** checkbox if you want to verify that the upstream repository’s SSL certificates are signed by a trusted CA.
11. Optional: In the **Upstream Username** field, enter the user name for the upstream repository if required for authentication. Clear this field if the repository does not require authentication.
12. Optional: In the **Upstream Password** field, enter the corresponding password for the upstream repository. Clear this field if the repository does not require authentication.
13. Optional: In the **Upstream Authentication Token** field, provide the token of the upstream repository user for authentication. Leave this field empty if the repository does not require authentication.
14. From the **Download Policy** list, select the type of synchronization Satellite Server performs. For more information, see [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview").
15. From the **Mirroring Policy** list, select the type of content synchronization Satellite Server performs. For more information, see [Section 6.6, “Mirroring policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Mirroring_Policies_Overview_content-management "6.6. Mirroring policies overview").
16. Optional: In the **Retain package versions** field, enter the number of versions you want to retain per package. This field is available only if you are using the additive download policy.
17. Optional: In the **HTTP Proxy Policy** field, select an HTTP proxy.
18. From the **Checksum** list, select the checksum type for the repository.
19. Optional: You can clear the **Unprotected** checkbox to require a subscription entitlement certificate for accessing this repository. By default, the repository is published through HTTP.
20. Optional: From the **GPG Key** list, select the GPG key for the product.
21. Optional: In the **SSL CA Cert** field, select the SSL CA Certificate for the repository.
22. Optional: In the **SSL Client cert** field, select the SSL Client Certificate for the repository.
23. Optional: In the **SSL Client Key** field, select the SSL Client Key for the repository.
24. Click **Save** to create the repository.

**Next steps**

- [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc")

### 3.7.2. Adding custom RPM repositories by using Hammer CLI

Add custom RPM repositories from an upstream URL to distribute Yum content to your hosts.

> **Note**
>
> Red Hat does not support the upstream RPMs directly from third-party sites. These RPMs are used to demonstrate the synchronization process. For any issues with these RPMs, contact the third-party developers.

**Prerequisites**

- You have imported the GPG key that you want to use to verify signatures of the RPM packages. For more information, see [Section 3.5.5, “Importing a custom GPG key by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-a-custom-gpg-key-by-using-cli "3.5.5. Importing a custom GPG key by using Hammer CLI").

**Procedure**

- Create a Yum repository:

  ```
  $ hammer repository create \
  --arch "My_Architecture" \
  --content-type "yum" \
  --gpg-key-id My_GPG_Key_ID \
  --name "My_Repository" \
  --organization "My_Organization" \
  --os-version "My_Operating_System_Version" \
  --product "My_Product" \
  --publish-via-http true \
  --url My_Upstream_URL
  ```

**Next steps**

- [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc")

## 3.8. Uploading content to custom repositories

You can upload content to custom repositories to distribute content that you cannot synchronize from an upstream URL.

### 3.8.1. Uploading content to a custom RPM repository by using Satellite web UI

You can upload individual RPM packages to a custom RPM repository to distribute Yum content that you cannot synchronize.

You must use Hammer CLI to upload source RPM packages. For more information, see [Section 3.8.2, “Uploading content to a custom RPM repository by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#uploading-content-to-a-custom-rpm-repository-by-using-cli "3.8.2. Uploading content to a custom RPM repository by using Hammer CLI").

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Click the name of the custom product.
3. In the **Repositories** tab, click the name of the custom RPM repository.
4. Under **Upload Package**, click **Browse…​** and select the RPM you want to upload.
5. Click **Upload**.

**Verification**

- To view all RPMs in this repository, click the number next to **Packages** under **Content Counts**.

**Troubleshooting**

- If the upload times out when uploading very large files on a slow network, raise the **Sync task timeout** setting value. In the Satellite web UI, navigate to **Administer** > **Settings**. The **Sync task timeout** setting is located on the **Tasks** tab.

**Next steps**

- Add your custom RPM repository to a content view. For more information, see [Section 9.2.3, “Creating a content view by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-content-view-by-using-web-ui "9.2.3. Creating a content view by using Satellite web UI").
- If your custom RPM is unprotected, hosts can consume its content by using the **Published At** URL.

  In the Default Organization View content view, the URL consists of your Capsule FQDN, `/pulp/content/`, your organization label, `/Library/custom/`, your product label, `/`, your repository label, and a trailing `/`, for example, `https://foreman.example.com/pulp/content/Example/Library/custom/my-software/my-app/`.

**Additional resources**

- [**Sync task timeout** description in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#background-tasks-settings)

### 3.8.2. Uploading content to a custom RPM repository by using Hammer CLI

You can upload individual RPM packages to a custom RPM repository to distribute Yum content that you cannot synchronize. Use Hammer CLI to upload source RPM packages.

**Procedure**

- Upload an RPM package:

  ```
  $ hammer repository upload-content \
  --id My_Repository_ID \
  --path /path/to/example-package.rpm
  ```
- Upload a source RPM package:

  ```
  $ hammer repository upload-content \
  --content-type srpm \
  --id My_Repository_ID \
  --path /path/to/example-package.src.rpm
  ```

**Verification**

- After the upload is complete, you can view information about a source RPM by using the commands `hammer srpm list` and `hammer srpm info --id srpm_ID`.

**Troubleshooting**

- If the upload times out when uploading very large files on a slow network, raise the **Sync task timeout** setting value:

  ```
  $ hammer settings set --name foreman_tasks_sync_task_timeout --value seconds
  ```

**Next steps**

- Add your custom RPM repository to a content view. For more information, see [Section 9.2.4, “Creating a content view by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-content-view-by-using-cli "9.2.4. Creating a content view by using Hammer CLI").
- If your custom RPM is unprotected, hosts can consume its content by using the **Published At** URL.

  In the Default Organization View content view, the URL consists of your Capsule FQDN, `/pulp/content/`, your organization label, `/Library/custom/`, your product label, `/`, your repository label, and a trailing `/`, for example, `https://foreman.example.com/pulp/content/Example/Library/custom/my-software/my-app/`.

**Additional resources**

- [**Sync task timeout** description in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#background-tasks-settings)

### 3.8.3. Uploading content to a custom file type repository by using Satellite web UI

If you cannot create a `PULP_MANIFEST` and synchronize your content from a local or remote repository to Satellite, you can manually upload content to a custom file type repository.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select a custom product by name.
3. Select a file type repository by name.
4. Click **Browse** to search and select the file you want to upload.
5. Click **Upload** to upload the selected file to Satellite Server.
6. Visit the URL where the repository is published to see the file.

**Additional resources**

- [Managing custom file type content in Satellite in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-custom-file-type-content-in-satellite)

### 3.8.4. Uploading content to a custom file type repository by using Hammer CLI

If you cannot create a `PULP_MANIFEST` and synchronize your content from a local or remote repository to Satellite, you can manually upload content to a custom file type repository.

**Procedure**

- Upload files to your custom file type repository:

  ```
  $ hammer repository upload-content \
  --id My_Repository_ID \
  --organization-id My_Organization_ID \
  --path My_Example_File
  ```

  The `--path` option can indicate a file, a directory of files, or a glob expression of files. Globs must be escaped by single or double quotes.

**Additional resources**

- [Managing custom file type content in Satellite in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-custom-file-type-content-in-satellite)
