---
title: "Consuming custom file type content on hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "22"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#consuming-custom-file-type-content-on-hosts"
---
# Chapter 22. Consuming custom file type content on hosts

After you upload or synchronize files to Satellite, you can download files to hosts from a custom file type repository. You can download the files over HTTP or HTTPS, which depends on the repository settings.

**Additional resources**

- [Managing custom file type content in Satellite in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-custom-file-type-content-in-satellite)

## 22.1. Downloading files to a host from a custom file type repository by using Satellite web UI

You can download files to a host over HTTPS and optionally over HTTP if the **Unprotected** option for the repository is selected. Use Satellite web UI to find the download URL of the custom file type repository.

**Prerequisites**

- You have a custom file type repository. For more information, see [Creating a custom file type repository by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-file-type-repository-by-using-web-ui) in *Managing content*.
- You know the name of the file you want to download.
- To download the files over HTTPS, your host has the following certificates:

  - The `katello-server-ca.crt` certificate. For more information, see [Importing the Katello root CA certificate by using browser](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#importing-the-katello-root-ca-certificate-by-using-browser) in *Configuring authentication for Red Hat Satellite users*.
  - An Organization Debug Certificate. For more information, see [Creating an Organization Debug Certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Creating_an_Organization_Debug_Certificate_admin) in *Administering Red Hat Satellite*.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select a custom product by name.
3. Select a file type repository by name.
4. Ensure to select the **Unprotected** checkbox to access the repository published through HTTP.
5. Copy the **Published At** URL.
6. On your client, download the file from Satellite Server:

   - For HTTPS:

     ```
     # curl \
     --cacert ./_katello-server-ca.crt \
     --cert ./_My_Organization_key-cert.pem \
     --remote-name \
     https://satellite.example.com/pulp/content/My_Organization_Label/Library/custom/My_Product_Label/My_Repository_Label/My_File
     ```
   - For HTTP:

     ```
     # curl \
     --remote-name \
     http://satellite.example.com/pulp/content/My_Organization_Label/Library/custom/My_Product_Label/My_Repository_Label/My_File
     ```

## 22.2. Downloading files to a host from a custom file type repository by using Hammer CLI

You can download files to a host over HTTPS and optionally over HTTP if the **Unprotected** option for the repository is selected. Use Hammer CLI to find the download URL of the custom file type repository.

**Prerequisites**

- You have a custom file type repository. For more information, see [Creating a custom file type repository by using Hammer CLI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-file-type-repository-by-using-cli) in *Managing content*.
- You know the name of the file you want to download.
- To download the files over HTTPS, your host has the following certificates:

  - The `katello-server-ca.crt` certificate. For more information, see [Importing the Katello root CA certificate by using command line](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#importing-the-katello-root-ca-certificate-by-using-command-line) in *Configuring authentication for Red Hat Satellite users*.
  - An Organization Debug Certificate. For more information, see [Creating an Organization Debug Certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Creating_an_Organization_Debug_Certificate_admin) in *Administering Red Hat Satellite*.

**Procedure**

1. List the file type repositories:

   ```
   $ hammer repository list --content-type file
   ```
2. Display the repository information.

   ```
   $ hammer repository info \
   --name "My_Files" \
   --organization-id My_Organization_ID \
   --product "My_File_Product"
   ```

   If **Unprotected** is enabled, the output is similar to this:

   ```
   Publish Via HTTP: yes
   Published At:       https://satellite.example.com/pulp/content/My_Organization_Label/Library/custom/My_File_Product_Label/My_Files_Label/
   ```

   If **Unprotected** is not enabled, the output is similar to this:

   ```
   Publish Via HTTP: no
   Published At:       https://satellite.example.com/pulp/content/My_Organization_Label/Library/custom/My_File_Product_Label/My_Files_Label/
   ```
3. On your client, download the file from Satellite Server:

   - For HTTPS:

     ```
     # curl \
     --cacert ./_katello-server-ca.crt \
     --cert ./_My_Organization_key-cert.pem \
     --remote-name \
     https://satellite.example.com/pulp/content/My_Organization_Label/Library/custom/My_Product_Label/My_Repository_Label/My_File
     ```
   - For HTTP:

     ```
     # curl \
     --remote-name \
     http://satellite.example.com/pulp/content/My_Organization_Label/Library/custom/My_Product_Label/My_Repository_Label/My_File
     ```
