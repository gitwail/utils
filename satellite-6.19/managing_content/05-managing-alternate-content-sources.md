---
title: "Managing alternate content sources"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-alternate-content-sources"
---
# Chapter 5. Managing alternate content sources

You can accelerate content synchronization for your Satellite Server and Capsule Servers by creating alternate content sources. Use an alternate content source on your local filesystem or nearby network to download content faster while still receiving metadata from the upstream source.

An alternate content source (ACS) defines an alternate path to download content during synchronization. The content itself is downloaded from the ACS, while the metadata is downloaded from the Satellite Server or the upstream URL, depending on the configuration. You can use ACS to accelerate synchronization if the content is located on the local filesystem or on a nearby network. You can set up ACS for Satellite Server and Capsule Servers.

You must refresh the alternate content source after creation or after making any changes. A weekly cron job refreshes all alternate content sources. You can also refresh the alternate content sources manually by using the Satellite web UI or Hammer CLI. Alternate content sources associated with your Satellite Server, or Capsule Servers attached to multiple organizations, affect all organizations.

There are the following types of alternate content sources:

Custom
:   Custom alternate content sources download the content from any upstream repository on the network or filesystem.

Simplified
:   Simplified alternate content sources copy the upstream repository information from your Satellite Server for the selected products. Simplified alternate content sources are ideal for situations where the connection from your Capsule Server to the upstream repository is faster than to your Satellite Server. Selecting the Red Hat products when creating a simplified alternate content source will download the content to the Capsule Servers from the Red Hat CDN.

RHUI
:   RHUI alternate content sources download content from a Red Hat Update Infrastructure (RHUI) server. Satellite web UI provides examples to help you find the network paths and to import authentication credentials. The RHUI alternate content source must be RHUI version 4 or greater and use the default installation configuration. For example, AWS RHUI is unsupported because it uses an installation scenario with unique authentication requirements.

## 5.1. Creating a custom alternate content source by using Satellite web UI

You can create a custom alternate content source (ACS) to accelerate content synchronization by downloading from your local network or filesystem instead of remote upstream servers.

**Prerequisites**

- If the repository requires SSL authentication, the SSL certificate and key must be imported into Satellite. For more information, see [Importing custom SSL certificates by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-web-ui) in *Managing content*.
- You have the base URL and subpaths of your alternate content source. For example, if your base URL is `https://server.example.com` and your subpaths are `red-hat-enterprise-linux-9/` and `red-hat-enterprise-linux-8/`, then Satellite will search `https://server.example.com/red-hat-enterprise-linux-9/` and `https://server.example.com/red-hat-enterprise-linux-8/`.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Alternate Content Sources**.
2. Click **Add source**.
3. Set the **Source type** to **Custom**.
4. Select the **Content type** from the drop-down list.
5. In the **Name** field, enter a name for your custom ACS.
6. Optional: In the **Description** field, provide a description for the ACS.
7. Select Capsules to which you want to synchronize content from your alternate content source.
8. If you require synchronizing content through the HTTP proxy of your Capsules, select **Use HTTP proxies**.
9. In the **Base URL** field, enter the base URL of the alternate content source.
10. In the **Subpaths** field, provide a comma-separated list of subpaths.
11. If your alternate content source requires authentication, select the **Manual authentication** or **Content credentials**.
12. If SSL verification is required, enable **Verify SSL** and select the SSL CA certificate.
13. Click **Add**.
14. Navigate to **Content** > **Alternate Content Sources**.
15. Open the options menu next to the newly created alternate content source and click **Refresh**.

**Verification**

1. In the Satellite web UI, navigate to **Monitor** > **Satellite Tasks** > **Tasks**.
2. Search for `Refresh Alternate Content Source`.
3. Verify that the task finished successfully.

## 5.2. Creating a custom alternate content source by using Hammer CLI

You can create a custom alternate content source (ACS) to accelerate content synchronization by downloading from your local network or filesystem instead of remote upstream servers.

**Prerequisites**

- If the repository requires SSL authentication, the SSL certificate and key must be imported into Satellite. For more information, see [Importing custom SSL certificates by using Hammer CLI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-cli) in *Managing content*.
- You have the base URL and subpaths of your alternate content source. For example, if your base URL is `https://server.example.com` and your subpaths are `red-hat-enterprise-linux-9/` and `red-hat-enterprise-linux-8/`, then Satellite will search `https://server.example.com/red-hat-enterprise-linux-9/` and `https://server.example.com/red-hat-enterprise-linux-8/`.

**Procedure**

1. Create a custom alternate content source:

   ```
   $ hammer alternate-content-source create \
   --alternate-content-source-type custom \
   --base-url "https://local-repo.example.com:port" \
   --name "My_ACS_Name" \
   --smart-proxy-ids My_Capsule_ID_1,My_Capsule_ID_2 \
   --subpaths "My_Subpath_1/,_My_Subpath_2/," \ --verify-ssl _true
   ```
2. Refresh your alternate content source:

   ```
   $ hammer alternate-content-source refresh --name "My_ACS_Name"
   ```

**Verification**

- Verify that the task ran successfully:

  ```
  $ hammer task list --search "Refresh Alternate Content Source"
  ```

## 5.3. Creating a simplified alternate content source by using Satellite web UI

You can create a simplified alternate content source (ACS) when your Capsule Servers have faster connections to the upstream repository than to your Satellite Server. This accelerates synchronization by downloading content directly from the upstream source.

**Prerequisites**

- You have created the products that will use the alternate content source.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Alternate Content Sources**.
2. Click **Add source**.
3. Set the **Source type** to **Simplified**.
4. Select the **Content type** from the drop-down list.
5. In the **Name** field, enter a name for your simplified ACS.
6. Optional: In the **Description** field, provide a description for the ACS.
7. Select Capsules to which you want to synchronize content from your alternate content source.
8. If you require synchronizing content through the HTTP proxy of your Capsules, select **Use HTTP proxies**.
9. Select the products that should use the alternate content source.
10. Click **Add**.
11. Navigate to **Content** > **Alternate Content Sources**.
12. Open the options menu next to the newly created alternate content source and click **Refresh**.

**Verification**

1. In the Satellite web UI, navigate to **Monitor** > **Satellite Tasks** > **Tasks**.
2. Search for `Refresh Alternate Content Source`.
3. Verify that the task finished successfully.

## 5.4. Creating a simplified alternate content source by using Hammer CLI

You can create a simplified alternate content source (ACS) when your Capsule Servers have faster connections to the upstream repository than to your Satellite Server. This accelerates synchronization by downloading content directly from the upstream source.

**Prerequisites**

- You have created the products that will use the alternate content source.

**Procedure**

1. Create a simplified alternate content source:

   ```
   $ hammer alternate-content-source create \
   --alternate-content-source-type simplified \
   --content-type yum \
   --name "My_ACS_Name" \
   --product-ids My_Product_ID_1,My_Product_ID_2 \
   --smart-proxy-ids My_Capsule_ID_1,My_Capsule_ID_2
   ```

   Use `--content-type file` if you want to create a simplified ACS for a product with file-type repositories.
2. Refresh your alternate content source:

   ```
   $ hammer alternate-content-source refresh --name "My_ACS_Name"
   ```

**Verification**

- Verify that the task ran successfully:

  ```
  $ hammer task list --search "Refresh Alternate Content Source"
  ```

## 5.5. Synchronizing Capsule directly from Red Hat CDN by using Satellite web UI

You can configure your Capsule Servers to sync Red Hat content directly from the Red Hat CDN to reduce load on your Satellite Server and accelerate content synchronization.

**Prerequisites**

- The required Red Hat repositories are enabled in Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Alternate Content Sources**.
2. Click **Add source**.
3. Set the **Source type** as **Simplified**.
4. Set the **Content type** to **Yum**.
5. In the **Name** field, enter a name for the alternate content source.
6. Optional: In the **Description** field, provide a description for the alternate content source.
7. Select Capsules that you want to sync directly from Red Hat CDN.
8. If you require synchronizing content through the HTTP proxy of your Capsules, select **Use HTTP proxies**.
9. Select the Red Hat products that should be synced to the Capsule from Red Hat CDN.
10. Review details and click **Add**.
11. Navigate to **Content** > **Alternate Content Sources**, click the options icon next to the newly created alternate content source, and select **Refresh**.

## 5.6. Creating an RHUI alternate content source by using Satellite web UI

You can create an RHUI alternate content source (ACS) to synchronize content from your Red Hat Update Infrastructure (RHUI) server. Leverage your existing RHUI investment and accelerate content synchronization.

Satellite searches content paths that combine a base URL with subpaths. For example, if your base URL is `https://server.example.com` and your subpaths are `rhel10/` and `rhel9/`, then Satellite searches `https://server.example.com/rhel10/` and `https://server.example.com/rhel9/`.

**Prerequisites**

- The client entitlement certificates for the required repositories are generated on the RHUA node. For more information, see [Creating a client entitlement certificate with the Red Hat Update Infrastructure Management Tool](https://docs.redhat.com/en/documentation/red_hat_update_infrastructure/4/html/configuring_and_managing_red_hat_update_infrastructure/assembly_cmg-creating-client-ent-cert-config-rpm_configuring-and-managing-red-hat-update-infrastructure#proc_cmg-creating-client-entitlement-certificate_assembly_cmg-creating-client-ent-cert-config-rpm) in *Configuring and Managing Red Hat Update Infrastructure 4*.
- The client entitlement certificates are imported into Satellite. For more information, see [Importing custom SSL certificates by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-web-ui) in *Managing content*.
- You have the base URL of the Red Hat Update Infrastructure CDS node.

**Procedure**

1. On your RHUA server, display details for the required repositories:

   ```
   # rhui-manager repo info --repo_id My_Repo_ID
   ```

   Record the relative paths from the command output to use as subpaths.
2. In the Satellite web UI, navigate to **Content** > **Alternate Content Sources**.
3. Click **Add source**.
4. Set the **Source type** to **RHUI**.
5. Generate RHUI certificates using the command provided in the Satellite web UI. Ensure that you pass the repo labels of the desired repositories.
6. In the **Name** field, enter a name for your RHUI ACS.
7. Optional: In the **Description** field, provide a description for the ACS.
8. Select Capsules to which you want to synchronize content from your alternate content source.
9. If you require synchronizing content through the HTTP proxy of your Capsules, select **Use HTTP proxies**.
10. In the **Base URL** field, enter the base URL of the Red Hat Update Infrastructure CDS node.
11. In the **Subpaths** field, provide a comma-separated list of subpaths.
12. If your alternate content source requires authentication, provide the **SSL client certificate** and **SSL client key**.
13. If SSL verification is required, enable **Verify SSL** and select the SSL CA certificate.
14. Click **Add**.
15. Navigate to **Content** > **Alternate Content Sources**.
16. Open the options menu next to the newly created alternate content source and click **Refresh**.

## 5.7. Creating an RHUI alternate content source by using Hammer CLI

You can create an RHUI alternate content source (ACS) to synchronize content from your Red Hat Update Infrastructure (RHUI) server. Leverage your existing RHUI investment and accelerate content synchronization.

Satellite searches content paths that combine a base URL with subpaths. For example, if your base URL is `https://server.example.com` and your subpaths are `rhel10/` and `rhel9/`, then Satellite searches `https://server.example.com/rhel10/` and `https://server.example.com/rhel9/`.

**Prerequisites**

- The client entitlement certificates for the required repositories are generated on the RHUA node. For more information, see [Creating a client entitlement certificate with the Red Hat Update Infrastructure Management Tool](https://docs.redhat.com/en/documentation/red_hat_update_infrastructure/4/html/configuring_and_managing_red_hat_update_infrastructure/assembly_cmg-creating-client-ent-cert-config-rpm_configuring-and-managing-red-hat-update-infrastructure#proc_cmg-creating-client-entitlement-certificate_assembly_cmg-creating-client-ent-cert-config-rpm) in *Configuring and Managing Red Hat Update Infrastructure 4*.
- The client entitlement certificates are imported into Satellite. For more information, see [Importing custom SSL certificates by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-web-ui) in *Managing content*.
- You have the base URL of the Red Hat Update Infrastructure CDS node.

**Procedure**

1. On your RHUA server, display details for the required repositories:

   ```
   # rhui-manager repo info --repo_id My_Repo_ID
   ```

   Record the relative paths from the command output to use as subpaths.
2. Create a RHUI alternate content source:

   ```
   $ hammer alternate-content-source create \
   --alternate-content-source-type rhui \
   --base-url "https://rhui-cds-node.example.com/pulp/content" \
   --name "My_ACS_Name" \
   --smart-proxy-ids My_Capsule_ID_1,My_Capsule_ID_2 \
   --ssl-client-cert-id My_SSL_Client_Certificate_ID \
   --ssl-client-key-id My_SSL_Client_Key_ID \
   --subpaths path/to/repo/1/,path/to/repo/2/ \
   --verify-ssl true
   ```
3. Refresh the alternate content source:

   ```
   $ hammer alternate-content-source refresh --name "My_ACS_Name"
   ```

**Verification**

- Verify that the task ran successfully:

  ```
  $ hammer task list --search "Refresh Alternate Content Source"
  ```

## 5.8. Permissions required to manage alternate content sources

User accounts must have a role that grants the following permissions to view and manage alternate content sources in Red Hat Satellite.

Permissions to view ACS
:   - `view_content_credentials`
    - `view_organizations`
    - `view_products`
    - `view_smart_proxies`

Permissions to manage ACS
:   - `create_alternate_content_sources`
    - `destroy_alternate_content_sources`
    - `edit_alternate_content_sources`
    - `view_alternate_content_sources`
