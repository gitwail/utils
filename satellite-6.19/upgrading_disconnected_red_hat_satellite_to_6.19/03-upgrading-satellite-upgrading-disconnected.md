---
title: "Upgrading Red Hat Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "upgrading_disconnected_red_hat_satellite_to_6.19"
guide_title: "Upgrading disconnected Red Hat Satellite to 6.19"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_disconnected_red_hat_satellite_to_6.19/index#Upgrading_satellite_upgrading-disconnected"
---
# Chapter 3. Upgrading Red Hat Satellite

Upgrading Satellite includes upgrading your Satellite Server, synchronizing the required repositories, and upgrading Capsule Servers.

## 3.1. Upgrading container images of Red Hat Lightspeed in Satellite

If you have Red Hat Lightspeed in Satellite enabled on your Satellite Server, prepare the container images of Red Hat Lightspeed in Satellite for Satellite 6.19 and load them on the disconnected server before running the upgrade.

**Prerequisites**

- Red Hat Lightspeed in Satellite is enabled on your disconnected Satellite Server.
- You know which method you used for the initial installation of Red Hat Lightspeed in Satellite: the ISO image method or the export and import method.

**Procedure**

- If you used the ISO image method for the initial installation of Red Hat Lightspeed in Satellite, update the Red Hat Lightspeed in Satellite container images from the ISO image for 6.19:

  1. Download and mount the Satellite installation ISO. For more information, see [Installing the Satellite packages from the offline repositories](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#installing-from-the-offline-repositories_upgrading-disconnected) in *Installing Satellite Server in a disconnected network environment*.
  2. Set up the local repositories for disconnected environments. For more information, see [Installing the Satellite packages from the offline repositories](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#installing-from-the-offline-repositories_upgrading-disconnected) in *Installing Satellite Server in a disconnected network environment*.
  3. Run the container setup script from the mounted ISO to load the Red Hat Lightspeed in Satellite images for 6.19:

     ```
     # /media/sat6/setup_containers
     ```
- If you used the export and import method for the initial installation of Red Hat Lightspeed in Satellite, update the Red Hat Lightspeed in Satellite container images from the exported archive files:

  1. On a connected system, log in to the container registry:

     ```
     $ skopeo login --username My_Username --password My_Password registry.redhat.io
     ```
  2. On the connected system, export the container images. Save the following script to a file and run it on the connected system to export the Red Hat Lightspeed in Satellite container images for 6.19:

     ```
     #!/bin/bash

     images=(
       "satellite/iop-ingress-rhel9:6.19"
       "satellite/iop-advisor-frontend-rhel9:6.19"
       "satellite/iop-host-inventory-rhel9:6.19"
       "satellite/iop-vmaas-rhel9:6.19"
       "satellite/iop-remediations-rhel9:6.19"
       "satellite/iop-vulnerability-frontend-rhel9:6.19"
       "satellite/iop-host-inventory-frontend-rhel9:6.19"
       "satellite/iop-advisor-backend-rhel9:6.19"
       "satellite/iop-puptoo-rhel9:6.19"
       "satellite/iop-yuptoo-rhel9:6.19"
       "satellite/iop-insights-engine-rhel9:6.19"
       "satellite/iop-vulnerability-engine-rhel9:6.19"
       "satellite/iop-gateway-rhel9:6.19"
       "amq-streams/kafka-39-rhel9:2.9.1-1"
     )

     for image in "${images[@]}"; do
       name=$(basename "${image}" | cut -d: -f1)
       image_url="registry.redhat.io/${image}"
       echo "Processing ${image}..."
       # Pull the image
       skopeo copy docker://${image_url} containers-storage:${image_url}
       # Copy image to archive
       skopeo copy containers-storage:${image_url} oci-archive:/tmp/${name}.tar
     done
     ```
  3. Transfer the archive files from `/tmp/` on the connected server to the `/tmp/` directory on the disconnected Satellite Server.
  4. On the disconnected Satellite Server, import the container images. Save the following script to a file and run it on the disconnected Satellite Server to import the Red Hat Lightspeed in Satellite container images for 6.19:

     ```
     #!/bin/bash

     images=(
       "satellite/iop-ingress-rhel9:6.19"
       "satellite/iop-advisor-frontend-rhel9:6.19"
       "satellite/iop-host-inventory-rhel9:6.19"
       "satellite/iop-vmaas-rhel9:6.19"
       "satellite/iop-remediations-rhel9:6.19"
       "satellite/iop-vulnerability-frontend-rhel9:6.19"
       "satellite/iop-host-inventory-frontend-rhel9:6.19"
       "satellite/iop-advisor-backend-rhel9:6.19"
       "satellite/iop-puptoo-rhel9:6.19"
       "satellite/iop-yuptoo-rhel9:6.19"
       "satellite/iop-insights-engine-rhel9:6.19"
       "satellite/iop-vulnerability-engine-rhel9:6.19"
       "satellite/iop-gateway-rhel9:6.19"
       "amq-streams/kafka-39-rhel9:2.9.1-1"
     )

     for image in "${images[@]}"; do
       name=$(basename "${image}" | cut -d: -f1)
       image_url="registry.redhat.io/${image}"
       echo "Processing ${image}..."
       # Import the image
       skopeo copy oci-archive:/tmp/${name}.tar containers-storage:${image_url}
     done
     ```

## 3.2. Upgrading a disconnected Satellite Server

Upgrading a Satellite Server that is not connected to the Red Hat Content Delivery Network includes backing up the server, configuring the server with the latest ISO files, and running the upgrade.

> **Warning**
>
> Note that the satellite-installer is executed during an upgrade or update. Any files managed by satellite-installer are overwritten. Check if you have any manual changes that would be overwritten by satellite-installer. You can use the `--noop` option with the satellite-installer to test for changes. For more information, see the Red Hat Knowledgebase solution [How to use the noop option to check for changes in Satellite config files during an upgrade.](https://access.redhat.com/solutions/3351311)

**Prerequisites**

- Ensure that all your Satellite Servers are on the same Satellite version.
- If you have made manual edits to you DNS or DHCP configuration in the `/etc/zones.conf` or `/etc/dhcp/dhcpd.conf` files, ensure DNS and DHCP configuration management is disabled:

  ```
  # satellite-installer \
  --foreman-proxy-dhcp-managed false \
  --foreman-proxy-dns-managed false
  ```

  This prevents the upgrade process from overwriting your DNS and DHCP configuration.

**Procedure**

1. Create a backup of your Satellite Server:

   1. Stop all Satellite services:

      ```
      # satellite-maintain service stop
      ```
   2. Take a snapshot or create a backup:

      - On a virtual machine, take a snapshot.
      - On a physical machine, create a backup.
   3. Start all Satellite services:

      ```
      # satellite-maintain service start
      ```
2. Remove old repositories:

   ```
   # rm /etc/yum.repos.d/*
   ```
3. Export the required repositories from your connected Satellite Server to your disconnected Satellite Server:

   1. Ensure that your connected server synchronizes the following repositories with the download policy set to **Immediate**:

      - `rhel-9-for-x86_64-baseos-rpms`
      - `rhel-9-for-x86_64-appstream-rpms`
      - `satellite-6.19-for-rhel-9-x86_64-rpms`
      - `satellite-maintenance-6.19-for-rhel-9-x86_64-rpms`
   2. List the repositories to identify their IDs:

      ```
      $ hammer repository list \
      --organization-label My_Organization_Label
      ```
   3. Export each repository in the syncable format by using its repository ID:

      ```
      $ hammer content-export complete repository \
      --format syncable \
      --id My_Repository_ID
      ```
   4. Copy the exported directories to the disconnected Satellite Server.
4. On the disconnected server, enable access to the exported content by configuring a repository:

   1. Locate the copied directories from the syncable export.
   2. Create the `/etc/yum.repos.d/upgrade.repo` file and update the `baseurl` directive to point to that location:

      ```
      [rhel-9-for-x86_64-baseos-rpms]
      name=Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)
      enabled=1
      metadata_expire=-1
      gpgcheck=0
      baseurl=file:///BaseOS_Export_Location/content/dist/rhel9/9/x86_64/baseos/os

      [rhel-9-for-x86_64-appstream-rpms]
      name=Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)
      enabled=1
      metadata_expire=-1
      gpgcheck=0
      baseurl=file:///AppStream_Export_Location/content/dist/rhel9/9/x86_64/appstream/os

      [satellite-6.19-for-rhel-9-x86_64-rpms]
      name=Red Hat Satellite 6.19 for RHEL 9 Server RPMs x86_64
      enabled=0
      metadata_expire=-1
      gpgcheck=0
      baseurl=file:///Satellite_Export_Location/content/dist/layered/rhel9/x86_64/satellite/6.19/os/

      [satellite-maintenance-6.19-for-rhel-9-x86_64-rpms]
      name=Red Hat Satellite Maintenance 6.19 for RHEL 9 Server RPMs x86_64
      enabled=1
      metadata_expire=-1
      gpgcheck=0
      baseurl=file:///Satellite_Maintenance_Export_Location/content/dist/layered/rhel9/x86_64/sat-maintenance/6.19/os/
      ```

      Keep the `satellite-6.19-for-rhel-9-x86_64-rpms` repository disabled.
5. Upgrade the `satellite-maintain` utility to its latest version:

   ```
   # satellite-maintain self-upgrade --maintenance-repo-label=satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```
6. Check whether your system is ready for Satellite upgrade:

   ```
   # satellite-maintain upgrade check --whitelist="repositories-validate,repositories-setup"
   ```

   Review the results and address any highlighted error conditions before performing the upgrade.

   > **Note**
   >
   > The `satellite-maintain upgrade check` might prompt you for the Hammer admin user credentials. It applies changes to the `/etc/foreman-maintain/foreman-maintain-hammer.yml` file.
7. Edit the `/etc/yum.repos.d/upgrade.repo` file and enable the `satellite-6.19-for-rhel-9-x86_64-rpms` repository:

   ```
   [satellite-6.19-for-rhel-9-x86_64-rpms]
   name=Red Hat Satellite 6.19 for RHEL 9 Server RPMs x86_64
   enabled=1
   metadata_expire=-1
   gpgcheck=0
   baseurl=file:///Satellite_Export_Location/content/dist/layered/rhel9/x86_64/satellite/6.19/os/
   ```
8. Run the Satellite Server upgrade command. Because of the lengthy upgrade time, consider using a utility such as `tmux`. For more information, see [Section 2.3, “Following the progress of the upgrade”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_disconnected_red_hat_satellite_to_6.19/index#following_the_progress_of_the_upgrade_upgrading-disconnected "2.3. Following the progress of the upgrade").

   ```
   # satellite-maintain upgrade run --whitelist="repositories-validate,repositories-setup"
   ```

   If the script fails due to missing or outdated packages, you must download and install these separately. For more information, see [Resolving Package Dependency Errors](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#resolving-package-dependency-errors_satellite) in *Installing Satellite Server in a disconnected network environment*.
9. If the `satellite-maintain` command told you to reboot, then reboot the system:

   ```
   # reboot
   ```
10. If you have the OpenSCAP plugin installed, but do not have the default OpenSCAP content available, enter the following command.

    ```
    # foreman-rake foreman_openscap:bulk_upload:default
    ```
11. In the Satellite web UI, navigate to **Configure** > **Discovery Rules**. Associate selected organizations and locations with Discovery rules.
12. Perform the following post-upgrade tasks to ensure your environment is adjusted to any changes applied during the upgrade.

    1. If you use Red Hat Lightspeed in Satellite, update the Common Vulnerabilities and Exposures (CVE) vulnerability mapping file:

       - On a connected system, download the latest `cvemap.xml` file from the Red Hat Customer Portal:

         ```
         $ curl \
         --output /var/www/html/pub/cvemap.xml \
         https://security.access.redhat.com/data/meta/v1/cvemap.xml
         ```
       - Transfer `cvemap.xml` to the disconnected Satellite Server you are upgrading, and place it in `/var/lib/foreman/`.

         Satellite detects the new file and publishes it to the internal Red Hat Lightspeed in Satellite services.
    2. Verify whether the default templates changed during the upgrade. Update any custom templates that you created by cloning a default template to reflect these changes.

       > **Note**
       >
       > Use custom provisioning snippets to execute custom code before or after the provisioning process instead of cloning default templates. You can avoid recreating cloned templates if you use custom provisioning snippets. For more information about configuring custom provisioning snippets, see [Running custom code during host provisioning by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#running-custom-code-during-host-provisioning-by-using-web-ui) in *Provisioning hosts*.
    3. If your Satellite shows any discovered hosts, reboot them:

       1. In the Satellite web UI, navigate to **Hosts** > **Discovered hosts**.
       2. Select **Any Organization** to display all discovered hosts.
       3. Reboot all discovered hosts.

## 3.3. Synchronizing the new repositories

You must enable and synchronize the new 6.19 repositories before you can upgrade Capsule Servers and Satellite clients.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Red Hat Repositories**.
2. Enable the following repositories:

   - Repositories required to upgrade Capsule Servers:

     - **Red Hat Satellite Capsule 6.19 (for RHEL 9 x86_64) (RPMs)**
     - **Red Hat Satellite Maintenance 6.19 (for RHEL 9 x86_64) (RPMs)**
     - **Red Hat Enterprise Linux 9 (for x86_64 – BaseOS) (RPMs)**
     - **Red Hat Enterprise Linux 9 (for x86_64 – AppStream) (RPMs)**
   - Repositories required to upgrade Satellite clients:

     - **Red Hat Satellite Client 6** for each Red Hat Enterprise Linux version your clients are using
     - If you use Puppet to manage host configurations, **Red Hat Satellite Client 6 OpenVox** for each Red Hat Enterprise Linux version your clients are using
3. In the Satellite web UI, navigate to **Content** > **Sync Status**.
4. Synchronize the following repositories:

   - All repositories for version 6.19
   - **Red Hat Satellite Client 6** repositories for each Red Hat Enterprise Linux version your clients are using
5. If you use Puppet to manage host configurations, manually update the content views for your hosts. Add the **Red Hat Satellite Client 6 OpenVox** repository for the Red Hat Enterprise Linux version your clients are using to the content views and publish and promote a new version of the content views.

**Troubleshooting**

- Refresh the Red Hat subscription manifest to resolve issues with synchronizing repositories. In the Satellite web UI, navigate to **Content** > **Subscriptions** > **Manage Manifest** > **Refresh**.

  > **Warning**
  >
  > Do not delete the manifest from the Customer Portal or in the Satellite web UI. Deleting your manifest removes all the entitlements of your hosts.

**Additional resources**

- [Importing content in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#)

## 3.4. Upgrading Capsule Servers

After upgrading your Satellite Server and synchronizing the required repositories, you can upgrade your Capsule Servers.

> **Note**
>
> You can use the **Capsule Upgrade Playbook** job template to upgrade Capsule Servers remotely. For more information about running remote jobs based on templates, see [Configuring and setting up remote jobs](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs) in *Managing hosts*.

**Prerequisites**

- The base system of the Capsule is registered to the newly upgraded Satellite Server.
- Ensure that you synchronize the required repositories on Satellite Server. For more information, see [Section 3.3, “Synchronizing the new repositories”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_disconnected_red_hat_satellite_to_6.19/index#synchronizing_the_new_repositories_upgrading-disconnected "3.3. Synchronizing the new repositories").
- If the Capsule Server is registered to a content view, add the Capsule 6.19 repositories to the content view. Publish and promote a new version of the content view. For more information, see [Managing content views and content view environments](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-views-and-content-view-environments) in *Managing content*.

**Procedure**

1. Create a backup of your Capsule Server. The backup can be a virtual machine (VM) snapshot or a regular full backup. For more information, see [Backing up Satellite Server and Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin) in *Administering Red Hat Satellite*.
2. Ensure that the Satellite Maintenance repository is enabled:

   ```
   # subscription-manager repos \
    --enable satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```
3. Upgrade the `satellite-maintain` utility on the Capsule Server to its latest version:

   ```
   # satellite-maintain self-upgrade
   ```
4. Determine whether Capsule Server is ready for the upgrade:

   ```
   # satellite-maintain upgrade check
   ```

   Review the results and address any highlighted error conditions before performing the upgrade.
5. Run the Satellite upgrade command. Because of the lengthy upgrade time, consider using a utility such as `tmux`. For more information, see [Section 2.3, “Following the progress of the upgrade”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_disconnected_red_hat_satellite_to_6.19/index#following_the_progress_of_the_upgrade_upgrading-disconnected "2.3. Following the progress of the upgrade").

   ```
   # satellite-maintain upgrade run
   ```
6. If the `satellite-maintain` command told you to reboot, then reboot the system:

   ```
   # reboot
   ```

## 3.5. Upgrading the external database operating system

If your Satellite uses an external database, you can upgrade the database from RHEL 8 to RHEL 9. You can upgrade the operating system while upgrading Satellite from 6.18 to 6.19.

**Prerequisites**

- A host running Red Hat Enterprise Linux 9 for PostgreSQL server. For more information, see [Preparing Satellite for using external databases](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#preparing-for-using-external-databases_satellite).

**Procedure**

1. Create a backup of your existing external database.
2. Restore the backup on the new Red Hat Enterprise Linux 9 server.
3. Verify that Satellite can reach the new database:

   ```
   # PGPASSWORD='My_Foreman_Database_Password' psql -h postgres.example.com -p 5432 -U foreman -d foreman -c "SELECT 1 as ping"
   ```
4. If your Satellite Server can reach the new database server by using the old name, you do not need to make any further changes. Otherwise, reconfigure Satellite to use the new name:

   ```
   # satellite-installer \
   --foreman-db-host newpostgres.example.com \
   --katello-candlepin-db-host newpostgres.example.com \
   --foreman-proxy-content-pulpcore-postgresql-host newpostgres.example.com
   ```

## 3.6. Refreshing clients of Red Hat Lightspeed in Satellite

If you use Red Hat Lightspeed in Satellite, you must refresh Red Hat Lightspeed in Satellite registration of your hosts to keep using services of Red Hat Lightspeed in Satellite after upgrading Satellite Server.

**Prerequisites**

- You have root access on your hosts.

**Procedure**

- On your hosts, refresh `insights-client` registration:

  ```
  # insights-client --register --force
  ```

  You can use remote execution to run this command on your hosts.

**Additional resources**

- [Executing a remote job by using Satellite web UI in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#executing-a-remote-job-by-using-web-ui)
- [Executing a remote job by using Hammer CLI in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#executing-a-remote-job-by-using-cli)

## 3.7. Upgrading Puppet agent 7 to OpenVox agent 8

If you use Puppet to configure hosts, you can upgrade Puppet agent 7 to OpenVox agent 8.

Puppet agent 7 remains compatible with OpenVox in Satellite as a legacy alternative, but Red Hat recommends to upgrade to OpenVox agent 8. For more information, see [OpenVox versions supported for integration with Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#openvox-versions-supported-for-integration-with-satellite) in *Managing configurations by using Puppet integration*.

**Prerequisites**

- **Red Hat Satellite Client 6 OpenVox** repository is enabled on the host.

**Procedure**

- On your hosts, upgrade the `puppet-agent` agent package to `openvox-agent`:

  ```
  # dnf upgrade puppet-agent
  ```

  You can also use remote execution to upgrade the package on multiple hosts. For more information, see [Upgrading a package](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Upgrading_a_package_managing-hosts) in *Managing hosts*.
