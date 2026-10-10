---
title: "Restoring Satellite Server or Capsule Server from a backup"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "12"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#restoring-satellite-server-or-capsule-from-a-backup_admin"
---
# Chapter 12. Restoring Satellite Server or Capsule Server from a backup

You can restore Satellite Server or Capsule Server from a backup to recover after failure or data loss. This process outlines how to restore the backup on the same server that generated the backup, and all data covered by the backup is deleted on the target system. If the original system is unavailable, provision a system with the same configuration settings and host name.

## 12.1. Restoring from a full backup

Restore Satellite Server or Capsule Server from a full backup return the system to the state at the time of the backup. When the restore process completes, all processes are online, and all databases and system configuration revert to the state at the time of the backup.

**Prerequisites**

- Your Satellite Server must have the same host name, configuration, and be the same minor version (X.Y) as the original system.
- The target directory must exist and be writable. The target directory is read from the configuration files contained within the backup archive.
- If the backed up system had FIPS enabled, the system on which you are restoring must also have FIPS enabled.

**Procedure**

1. Ensure that you have enough space to store the backup data on the base system of Satellite Server or Capsule Server as well as enough space after the restoration to contain all the data in the `/etc/` and `/var/` directories contained within the backup.

   To check the space used by a directory:

   ```
   # du -sh /var/backup_directory
   ```

   To check for free space:

   ```
   # df -h /var/backup_directory
   ```

   Add the `--total` option to get a total of the results from more than one directory.
2. Restore the correct SELinux contexts:

   ```
   # restorecon -Rv /
   ```
3. Choose the appropriate method to install Satellite or Capsule:

   - To install Satellite Server from a connected network, follow the procedures in [Installing Satellite Server in a connected network environment](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#).

     If you have used Red Hat Lightspeed in Satellite, enable it. For more information, see [Installing and configuring Red Hat Lightspeed in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#installing-and-configuring-red-hat-lightspeed-in-satellite).
   - To install Satellite Server from a disconnected network, follow the procedures in [Installing Satellite Server in a disconnected network environment](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#).

     If you have used Red Hat Lightspeed in Satellite, enable it. For more information, see [Installing and configuring Red Hat Lightspeed in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#installing-and-configuring-red-hat-lightspeed-in-satellite).
   - To install a Capsule Server, follow the procedures in [Installing Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#).
4. Copy the backup data to the local file system on Satellite Server. Use `/var/` or `/var/tmp/`.
5. Run the restoration script.

   ```
   # satellite-maintain restore /var/backup_directory
   ```

   Where *backup_directory* is the time-stamped directory or subdirectory containing the backed-up data.

   The restore process can take a long time to complete, because of the amount of data to copy.

**Next steps**

- If you create a new instance of Satellite Server or Capsule Server, decommission the old instance after restoring the backup. Cloned instances are not supposed to run in parallel in a production environment.

**Troubleshooting**

- Review the `/var/log/foreman/production.log` and `/var/log/messages` log files.

## 12.2. Restoring from incremental backups

Restore Satellite Server or Capsule Server from an incremental backup to return the system to the state at the time of the backup. When the restore process completes, all processes are online, and all databases and system configuration revert to the state at the time of the backup.

If you have multiple branches of incremental backups, select your full backup and each incremental backup for the *branch* you want to restore, in chronological order.

**Prerequisites**

- If the backed up system had FIPS enabled, the system on which you are restoring must also have FIPS enabled.

**Procedure**

1. Restore the last full backup using the instructions in [Section 12.1, “Restoring from a full backup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Restoring_from_a_Full_Backup_admin "12.1. Restoring from a full backup").
2. Remove the full backup data from the local file system on Satellite Server, for example, `/var/` or `/var/tmp/`.
3. Copy the incremental backup data to the local file system on Satellite Server, for example, `/var/` or `/var/tmp/`.
4. Restore the incremental backups in the same sequence that they are made:

   ```
   # satellite-maintain restore /var/backup_directory/FIRST_INCREMENTAL
   # satellite-maintain restore /var/backup_directory/SECOND_INCREMENTAL
   ```

**Next steps**

- If you create a new instance of Satellite Server or Capsule Server, decommission the old instance after restoring the backup. Cloned instances are not supposed to run in parallel in a production environment.

**Troubleshooting**

- Review the `/var/log/foreman/production.log` and `/var/log/messages` log files.

## 12.3. Restoring Capsule Server by using a virtual machine snapshot

Restore Capsule Server from a virtual machine snapshot to return the system to the state at the time of the snapshot. You can use virtual machine snapshots to back up and restore your Capsule Server for quick recovery after server failure or configuration issues.

**Prerequisites**

- If the backed up system had FIPS enabled, the system on which you are restoring must also have FIPS enabled.
- You have selected the relevant organization and location context of your Capsule Server, or chosen **Any Organization** and **Any Location**.

**Procedure**

1. If your Capsule Server is a virtual machine, include it in your backup strategy by using VM snapshots. Creating weekly snapshots that you can restore from is recommended.
2. After a failure, either restore your Capsule Server from a snapshot by using your hypervisor tools, or deploy a new Capsule Server and ensure that the host name is the same as before, and then install the Capsule certificates. You may still have them on Satellite Server, the package name ends in -certs.tar, alternately create new ones.
3. Follow the procedures in [Installing Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#) until you can confirm, in the Satellite web UI, that Capsule Server is connected to Satellite Server.
4. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
5. Select your Capsule Server.
6. On the **Overview** tab, click **Synchronize**.

   - Select **Optimized Sync** to synchronize content from your Satellite Server to your Capsule Server that bypasses unnecessary steps to speed up performance.
   - Select **Complete Sync** to perform a complete sync from your Satellite Server to your Capsule Server that synchronizes content even if the metadata has not changed.
