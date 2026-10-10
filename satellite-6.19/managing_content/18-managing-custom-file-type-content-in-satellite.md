---
title: "Managing custom file type content in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "18"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-custom-file-type-content-in-satellite"
---
# Chapter 18. Managing custom file type content in Satellite

You can use custom file type repositories in custom products to store and distribute arbitrary files such as SSH keys, source code, or ISO images in Satellite.

You can upload files to the repository and synchronize files from an upstream Satellite Server. When you add files to a custom file type repository, you can use the normal Satellite management functions such as adding a specific version to a content view to provide version control and making the repository of files available on various Capsule Servers.

You can create a file type repository in Satellite Server only in a custom product, but there is flexibility in how you create the repository source. You can create an independent repository source in a directory on Satellite Server, or on a remote HTTP server, and then synchronize the contents of that directory into Satellite. This method is useful when you have multiple files to add to a Satellite repository.

**Additional resources**

- [Consuming custom file type content on hosts in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#consuming-custom-file-type-content-on-hosts)

## 18.1. Creating a local source for a custom file type repository

When you have multiple files to import, you can prepare a directory on Satellite Server as a local Pulp source. Then, synchronize files from this directory into a custom file type repository.

Configure a directory on the base system where Satellite is installed as the repository source. To create a file type repository in a directory on a remote server, see [Section 18.2, “Creating a remote source for a custom file type repository”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-remote-source-for-a-custom-file-type-repository "18.2. Creating a remote source for a custom file type repository").

**Procedure**

1. On your Satellite Server, install the Pulp Manifest package:

   ```
   # satellite-maintain packages install pulp-manifest
   ```

   Note that this command stops the Satellite service and re-runs `satellite-installer`. Alternatively, to prevent downtime caused by stopping the service, you can use the following:

   ```
   # satellite-maintain packages unlock
   # satellite-maintain packages install pulp-manifest
   # satellite-maintain packages lock
   ```
2. Create a directory that you want to use as the file type repository, such as:

   ```
   # mkdir -p /var/lib/pulp/local_repos/my_file_repo
   ```
3. Add the parent folder into allowed import paths:

   ```
   # satellite-installer --foreman-proxy-content-pulpcore-additional-import-paths /var/lib/pulp/local_repos
   ```
4. Add files to the directory or create a test file:

   ```
   # touch /var/lib/pulp/local_repos/my_file_repo/test.txt
   ```
5. Create the Pulp Manifest:

   ```
   # pulp-manifest /var/lib/pulp/local_repos/my_file_repo
   ```
6. Verify the manifest was created:

   ```
   # ls /var/lib/pulp/local_repos/my_file_repo
   PULP_MANIFEST test.txt
   ```

**Next steps**

- You can import your local source as a custom file type repository. Use the `file://` URL scheme and the name of the directory to specify an **Upstream URL**, such as `file:///var/lib/pulp/local_repos/my_file_repo`. For more information, see [Section 18.3, “Creating a custom file type repository by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-file-type-repository-by-using-web-ui "18.3. Creating a custom file type repository by using Satellite web UI").
- If you update the contents of your directory, re-run Pulp Manifest and sync the repository in Satellite. For more information, see [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc").

## 18.2. Creating a remote source for a custom file type repository

You can prepare a directory on a remote HTTP server as a Pulp source and synchronize files into a custom file type repository on Satellite Server.

Configure a directory on a remote server as the repository source. To create a file type repository in a directory on the base system where Satellite Server is installed, see [Section 18.1, “Creating a local source for a custom file type repository”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-local-source-for-a-custom-file-type-repository "18.1. Creating a local source for a custom file type repository").

**Prerequisites**

- You have a server running Red Hat Enterprise Linux 9 registered to your Satellite or the Red Hat CDN.
- Your server has an entitlement to the Red Hat Enterprise Linux Server and Red Hat Satellite repositories.
- You have installed an HTTP server. For more information about configuring a web server, see [Setting up the Apache HTTP web server](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/deploying_web_servers_and_reverse_proxies/setting-apache-http-server_deploying-web-servers-and-reverse-proxies) in Red Hat Enterprise Linux 9 *Deploying web servers and reverse proxies*.

**Procedure**

1. On your HTTP server, enable the required repositories:

   ```
   # subscription-manager repos \
   --enable=rhel-9-for-x86_64-appstream-rpms \
   --enable=rhel-9-for-x86_64-baseos-rpms \
   --enable=satellite-6.19-for-rhel-9-x86_64-rpms
   ```
2. Install the Pulp Manifest package:

   ```
   # dnf install pulp-manifest
   ```
3. Create a directory that you want to use as the file type repository in the HTTP server’s public folder:

   ```
   # mkdir /var/www/html/pub/my_file_repo
   ```
4. Add files to the directory or create a test file:

   ```
   # touch /var/www/html/pub/my_file_repo/test.txt
   ```
5. Create the Pulp Manifest:

   ```
   # pulp-manifest /var/www/html/pub/my_file_repo
   ```
6. Verify the manifest was created:

   ```
   # ls /var/www/html/pub/my_file_repo
   PULP_MANIFEST test.txt
   ```

**Next steps**

- You can import your remote source as a custom file type repository. Use the path to the directory to specify an **Upstream URL**, such as `http://server.example.com/my_file_repo`. For more information, see [Section 18.3, “Creating a custom file type repository by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-file-type-repository-by-using-web-ui "18.3. Creating a custom file type repository by using Satellite web UI").
- If you update the contents of your directory, re-run Pulp Manifest and sync the repository in Satellite. For more information, see [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc").

## 18.3. Creating a custom file type repository by using Satellite web UI

You can add a custom file type repository to an existing custom product. Select the `file` repository type and follow the same workflow as when you add other custom content.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select a product that you want to create a repository for.
3. On the **Repositories** tab, click **New Repository**.
4. In the **Name** field, enter a name for the repository. Satellite automatically completes the **Label** field based on the name.
5. Optional: In the **Description** field, enter a description for the repository.
6. From the **Type** list, select `file` as type of repository.
7. Optional: In the **Upstream URL** field, enter the URL of the upstream repository to use as a source. If you do not enter an upstream URL, you can manually upload packages. For more information, see [Section 3.8.3, “Uploading content to a custom file type repository by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#uploading-content-to-a-custom-file-repository-by-using-web-ui "3.8.3. Uploading content to a custom file type repository by using Satellite web UI").
8. Select **Verify SSL** to verify that the SSL certificates of the repository are signed by a trusted CA.
9. Optional: In the **Upstream Username** field, enter the user name for the upstream repository if required for authentication. Clear this field if the repository does not require authentication.
10. Optional: In the **Upstream Password** field, enter the corresponding password for the upstream repository. Clear this field if the repository does not require authentication.
11. Optional: In the **Upstream Authentication Token** field, provide the token of the upstream repository user for authentication. Leave this field empty if the repository does not require authentication.
12. From the **Download Policy** list, select the type of synchronization Satellite Server performs. For more information, see [Section 6.1, “Download policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Download_Policies_Overview_content-management "6.1. Download policies overview").
13. From the **Mirroring Policy** list, select the type of content synchronization Satellite Server performs. For more information, see [Section 6.6, “Mirroring policies overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Mirroring_Policies_Overview_content-management "6.6. Mirroring policies overview").
14. Optional: In the **HTTP Proxy Policy** field, select an HTTP proxy. By default, it uses the `Global Default` HTTP proxy.
15. Optional: You can clear the **Unprotected** checkbox to require a subscription entitlement certificate for accessing this repository. By default, the repository is published through HTTP.
16. Optional: In the **SSL CA Cert** field, select the SSL CA Certificate for the repository.
17. Optional: In the **SSL Client Cert** field, select the SSL Client Certificate for the repository.
18. Optional: In the **SSL Client Key** field, select the SSL Client Key for the repository.
19. Click **Save** to create the repository.

## 18.4. Creating a custom file type repository by using Hammer CLI

You can add a custom file type repository to an existing custom product. Select the `file` repository type and follow the same workflow as when you add other custom content.

**Procedure**

1. Create a custom product:

   ```
   $ hammer product create \
   --name "My_File_Product" \
   --organization-id My_Organization_ID \
   --sync-plan "My_Sync_Plan"
   ```

   Table 18.1. Optional parameters for the hammer product create command

   | **Option** | **Description** |
   | --- | --- |
   | `--gpg-key-id` *gpg_key_id* | GPG key numeric identifier |
   | `--sync-plan-id` *sync_plan_id* | Sync plan numeric identifier |
   | `--sync-plan` *sync_plan_name* | Sync plan name to search by |
2. Create a `file` type repository:

   ```
   $ hammer repository create \
   --content-type file \
   --name "My_Files" \
   --organization-id My_Organization_ID \
   --product "My_File_Product"
   ```

   Table 18.2. Optional parameters for the hammer repository create command

   | **Option** | **Description** |
   | --- | --- |
   | `--checksum-type` *sha_version* | Repository checksum (either `sha256`, `sha384`, or `sha512`) |
   | `--download-policy` *policy_name* | Download policy for repositories (either `immediate` or `on_demand`) |
   | `--gpg-key-id` *gpg_key_id* | GPG key numeric identifier |
   | `--gpg-key` *gpg_key_name* | Key name to search by |
   | `--mirror-on-sync` *boolean* | Must this repo be mirrored from the source, and stale packages removed, when synced? Set to `true` or `false`, `yes` or `no`, `1` or `0`. |
   | `--publish-via-http` *boolean* | Must this also be published using HTTP? Set to `true` or `false`, `yes` or `no`, `1` or `0`. |
   | `--upstream-password` *repository_password* | Password for the upstream repository user |
   | `--upstream-username` *repository_username* | Upstream repository user, if required for authentication |
   | `--url` *My_Repository_URL* | URL of the remote repository |
   | `--verify-ssl-on-sync` *boolean* | Verify that the upstream SSL certificates of the remote repository are signed by a trusted CA? Set to `true` or `false`, `yes` or `no`, `1` or `0`. |

**Next steps**

- If you set an upstream URL, you can synchronize content to Satellite. For more information, see [Section 4.2.2, “Synchronizing repositories by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-by-using-cli "4.2.2. Synchronizing repositories by using Hammer CLI").
- If you did not set an upstream URL, you can upload content to your custom file type. For more information, see [Section 3.8.4, “Uploading content to a custom file type repository by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#uploading-content-to-a-custom-file-repository-by-using-cli "3.8.4. Uploading content to a custom file type repository by using Hammer CLI").
