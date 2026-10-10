---
title: "Cloning Satellite Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#cloning-satellite-server"
---
# Chapter 1. Cloning Satellite Server

You can clone your Satellite Server to create instances to test upgrades and migration of instances to a different machine or operating system. This is an optional step to provide more flexibility during the upgrade or migration.

> **Note**
>
> You cannot use the Satellite clone tool on Capsule Servers. To create a clone of a Capsule Server, you must first backup the existing Capsule Server, restore it on the target server, and then reconfigure Capsule Server.

## 1.1. Cloning process overview

The cloning process involves backing up your source server, transferring it to a target server, and reconfiguring it to operate in the new environment.

The source server is the old server that you want to clone. The target server is the new server that you copy files to and clone the source server to.

Cloning Satellite Server consists of the following high-level steps:

1. Back up the source server.
2. Clone the source server to the target server.
3. Power off the source server.
4. Update the network configuration on the target server to match the IP address of the target server with its new host name.
5. Test the new target server.

Note that because of the high volume of data that you must copy and transfer as part of the cloning process, it can take a significant amount of time to complete.

> **Note**
>
> If you create a new instance of the Satellite Server, decommission the old instances after restoring the backup. Cloned instances are not supposed to run in parallel in a production environment.

## 1.2. Prerequisites for cloning

Ensure that your environment meets the following prerequisites before you can clone your Satellite Server.

Ensure that the target server complies with all the required specifications for a Satellite Server:

- The target server is a minimal install of Red Hat Enterprise Linux 9. Do not install Red Hat Enterprise Linux 9 software groups or third-party applications.
- You have a Satellite subscription for the target server.

Before you begin cloning, ensure the following conditions exist:

- The target server is on an isolated network. This prevents the cloned Satellite Server from accidentally communicating with the source Satellite Server, Capsule Servers, and hosts.
- The target server has at least the same storage capacity as the source server.
- If you have any customized configurations on your source server that are not managed by the `satellite-installer` tool or Satellite backup process, you must manually back up these files.

## 1.3. Preparing the source server for cloning

To prepare the source Satellite Server for cloning, perform a backup of the Satellite data. Depending on the size of your Pulp data, you might need to transfer Pulp data to the target server manually.

> **Note**
>
> While you can clone Satellite Server without Pulp data, you must transfer the Pulp data afterwards to achieve a fully working environment. If the target server does not include Pulp data, it is not a fully working Satellite.

**Procedure**

1. Determine the size of the Pulp data:

   ```
   # du -sh /var/lib/pulp/
   ```
2. If you have a large amount of Pulp data, perform a backup without Pulp data and transfer it to the target server manually. Choose this option if you have more than 500 GB of Pulp data, or if you use a slow storage system, such as NFS, and have more than 100 GB of Pulp data.

   1. Perform a backup with PostgreSQL databases active excluding the Pulp data:

      ```
      # satellite-maintain backup offline --skip-pulp-content \
      --assumeyes /var/backup
      ```
   2. Stop and disable Satellite services:

      ```
      # satellite-maintain service stop
      # satellite-maintain service disable
      ```
   3. Copy the Pulp data to the target server:

      ```
      # rsync --archive --partial --progress --compress \
      /var/lib/pulp/ target_server.example.com:/var/lib/pulp/
      ```
3. If you have less than 500 GB of Pulp data, perform a backup with PostgreSQL databases active including the Pulp data.

   ```
   # satellite-maintain backup offline --assumeyes /var/backup
   ```
4. Stop and disable Satellite services:

   ```
   # satellite-maintain service stop
   # satellite-maintain service disable
   ```

## 1.4. Cloning to the target server

To clone a Satellite Server, you must prepare the target server with backup files, register it with Red Hat, install the cloning tool, and run the restoration process.

**Procedure**

1. Place the backup files from the source Satellite in the `/backup/` folder on the target server. You can either mount the shared storage or copy the backup files to the `/backup/` folder on the target server.
2. Power off the source server.
3. Prepare the target server for cloning:

   1. Register your instance to the Red Hat Customer Portal and enable only the required repositories:

      ```
      # subscription-manager register
      # subscription-manager repos --disable=*
      # subscription-manager repos --enable=rhel-9-for-x86_64-appstream-rpms \
      --enable=rhel-9-for-x86_64-baseos-rpms \
      --enable=satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
      ```
   2. Install the `satellite-clone` package:

      ```
      # dnf install satellite-clone
      ```

      After you install the `satellite-clone` tool, you can adjust any configuration to suit your own deployment in the `/etc/satellite-clone/satellite-clone-vars.yml` file. For example, the `satellite-clone` tool defaults to using `/backup/` as the backup folder. If your backup is located in a different folder, update the `backup_dir` variable in the `/etc/satellite-clone/satellite-clone-vars.yml` file.
4. Run the `satellite-clone` tool on the target server:

   ```
   # satellite-clone
   ```

## 1.5. Performing post-cloning tasks

To complete the cloning, perform the following tasks to ensure your new Satellite Server is fully functional and the source server is decommissioned.

**Procedure**

1. Log in to the Satellite web UI, with the username `admin` and the password `changeme`. Update the admin password to secure credentials.
2. Reconfigure provisioning services on the target server:

   1. Reconfigure DHCP, DNS, TFTP, and remote execution services. The cloning process disables these services on the target Satellite Server to avoid conflict with the source Satellite Server.
   2. Reconfigure and enable DHCP, DNS, and TFTP in the Satellite web UI. For more information, see [Integrating provisioning infrastructure services](https://docs.theforeman.org/3.18/Integrating_Provisioning_Infrastructure_Services/index-satellite.html#).
3. In the Satellite web UI, refresh subscriptions:

   1. Ensure that the correct organization is selected.
   2. Navigate to **Content** > **Subscriptions**.
   3. Click **Manage Manifest**.
   4. Click **Refresh** and then click **Close** to return to the list of subscriptions.
   5. Verify that the available subscriptions are correct.
4. Follow the instructions in the `/usr/share/satellite-clone/logs/reassociate_capsules.txt` file to restore the associations between Capsules and their lifecycle environments.
5. Update your network configuration, for example, DNS, to match the IP address of the target server with its new host name. The `satellite-clone` tool changes the host name to the source server’s host name. If you want to change the host name to something different, you can use the `satellite-change-hostname` tool. For more information, see [Renaming Satellite Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#renaming-satellite_admin) in *Administering Red Hat Satellite*.
6. If the source server uses the `virt-who` daemon, install and configure it on the target server. Copy all the `virt-who` configuration files in the `/etc/virt-who.d/` directory from the source server to the same directory on the target server. For more information, see [*Configuring virt-who for virtual machine subscriptions*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt_who_for_virtual_machine_subscriptions/index#).
7. Decommission the source server.
