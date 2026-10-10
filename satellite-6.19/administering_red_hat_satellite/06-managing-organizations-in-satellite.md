---
title: "Managing organizations in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-organizations-in-satellite"
---
# Chapter 6. Managing organizations in Satellite

Organizations divide Satellite resources into logical groups based on ownership, purpose, content, security level, or other divisions. Use organizations to manage and isolate resources and users within a single Satellite deployment.

## 6.1. Examples of using organizations in Satellite

You can use organizations to structure your content and host management based on your business needs, whether you run a small business, a large company with multiple business units, or manage hosts for external customers.

Single Organization
:   Using a single organization is well suited for a small business with a simple system administration chain.

    In this case, you create a single organization for the business and assign content to it. You can also use the **Default Organization** for this purpose.

Multiple Organizations
:   Using multiple organizations is well suited for a large company that owns several smaller business units. For example, a company with separate system administration and software development groups.

    In this case, you create one organization for the company and then an organization for each of the business units it owns. You then assign content to each organization based on its needs.

External Organizations
:   Using external organizations is well suited for a company that manages external systems for other organizations. For example, a company offering cloud computing and web hosting resources to customers.

    In this case, you create an organization for the company’s own system infrastructure and then an organization for each external business. You then assign content to each organization where necessary.

## 6.2. Creating an organization by using Satellite web UI

Create an organization by using the Satellite web UI. You can use the organization to assign hosts and resources to the organization.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Organizations**.
2. Click **New Organization**.
3. In the **Name** field, enter a name for the organization.
4. In the **Label** field, enter a unique identifier for the organization. This is used for creating and mapping certain assets, such as directories for content storage. Use letters, numbers, underscores, and dashes, but no spaces.
5. Optional: In the **Description** field, enter a description for the organization.
6. Click **Submit**.
7. If you have hosts with no organization assigned, select the hosts that you want to add to the organization, then click **Proceed to Edit**.
8. In the **Edit** page, assign the infrastructure resources that you want to add to the organization. This includes networking resources, installation media, Kickstart templates, and other parameters. You can return to this page at any time by navigating to **Administer** > **Organizations** and then selecting an organization to edit.
9. Click **Submit**.

## 6.3. Creating an organization by using Hammer CLI

Create an organization by using Hammer CLI. You can use the organization to assign hosts and resources to the organization.

**Procedure**

1. Create an organization:

   ```
   $ hammer organization create \
   --name "My_Organization" \
   --label "My_Organization_Label" \
   --description "My_Organization_Description"
   ```
2. Optional: To edit an organization, enter the `hammer organization update` command. For example, you can assign a compute resource to the organization:

   ```
   $ hammer organization update \
   --name "My_Organization" \
   --compute-resource-ids 1
   ```

## 6.4. Creating an organization debug certificate

Generate a debug certificate for an organization to access repository content or troubleshoot content delivery without full Satellite authentication.

> **Note**
>
> Debug Certificates are automatically generated for provisioning template downloads if they do not already exist in the organization for which they are being downloaded.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Organizations**.
2. Select an organization that you want to generate a debug certificate for.
3. Click **Generate and Download**.
4. Save the certificate file in a secure location.

## 6.5. Browsing repository content using an organization debug certificate

Browse the repository content of an organization in a web browser or with curl after you generate a debug certificate for that organization.

**Prerequisites**

- You have created and downloaded an organization debug certificate. For more information, see [Section 6.4, “Creating an organization debug certificate”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Creating_an_Organization_Debug_Certificate_admin "6.4. Creating an organization debug certificate").

**Procedure**

1. Split the private and public keys from the certificate into two files.

   1. Open the X.509 certificate, for example, for the default organization:

      ```
      $ vi 'Default Organization-key-cert.pem'
      ```
   2. Copy the contents of the file from `-----BEGIN RSA PRIVATE KEY-----` to `-----END RSA PRIVATE KEY-----`, into a `key.pem` file.
   3. Copy the contents of the file from `-----BEGIN CERTIFICATE-----` to `-----END CERTIFICATE-----`, into a `cert.pem` file.
2. To use the organization debug certificate with a browser, you must first convert the X.509 certificate to a format your browser supports and then import the certificate. For example, for Mozilla Firefox users:

   1. Convert the certificate into the PKCS12 format using the following command:

      ```
      $ openssl pkcs12 -keypbe PBE-SHA1-3DES -certpbe PBE-SHA1-3DES -export -in cert.pem -inkey key.pem -out My_Organization_Label.pfx -name My_Organization
      ```
   2. In the Mozilla Firefox browser, navigate to **Edit** > **Settings** > **Privacy & Security**.
   3. Select **View Certificates** and click the **Your Certificates** tab.
   4. Click **Import** and select the `.pfx` file to load.
   5. Enter the following URL in the address bar to browse the accessible paths for all the repositories and check their contents:

      ```
      https://satellite.example.com/pulp/content/
      ```
3. To use the organization debug certificate with CURL:

   ```
   $ curl \
   --cert cert.pem \
   --key key.pem \
   https://satellite.example.com/pulp/content/My_Organization_Label/Library/content/dist/rhel/server/7/7Server/x86_64/os/
   ```

   Ensure that the paths to `cert.pem` and `key.pem` are the correct absolute paths otherwise the command fails silently. Pulp uses the organization label, therefore, you must enter the organization label into the URL.

## 6.6. Deleting an organization by using Satellite web UI

You can delete an organization from the Satellite web UI if you no longer need it for resource management.

> **Important**
>
> Do not delete **Default Organization** created during installation because the default organization is a placeholder for any unassociated hosts in your Satellite environment. There must be at least one organization in the environment at any given time.

**Procedure**

1. If there are any lifecycle environments or host groups associated with the organization you are about to delete, remove them by navigating to **Administer** > **Organizations** and clicking the relevant organization.
2. In the Satellite web UI, navigate to **Administer** > **Organizations**.
3. From the list to the right of the name of the organization you want to delete, select **Delete**.
4. Click **OK** to delete the organization.

## 6.7. Deleting an organization by using Hammer CLI

You can delete an organization by using Hammer CLI if you no longer need it for resource management.

> **Important**
>
> Do not delete **Default Organization** created during installation because the default organization is a placeholder for any unassociated hosts in your Satellite environment. There must be at least one organization in the environment at any given time.

**Procedure**

1. If there are any lifecycle environments or host groups associated with the organization you are about to delete, remove them by navigating to **Administer** > **Organizations** and clicking the relevant organization.
2. View all organizations:

   ```
   $ hammer organization list
   ```

   From the output, note the ID of the organization that you want to delete.
3. Delete an organization:

   ```
   $ hammer organization delete --id My_Organization_ID
   ```
