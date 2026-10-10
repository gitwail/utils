---
title: "Backing up Satellite Server and Capsule Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "11"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin"
---
# Chapter 11. Backing up Satellite Server and Capsule Server

You can back up your Satellite deployment to ensure the continuity of your Red Hat Satellite deployment and associated data in case a disaster occurs. If your deployment uses custom configurations, you must consider how to handle these custom configurations when you plan your backup and disaster recovery policy.

## 11.1. Planning Satellite Server and Capsule Server backup

Backing up your Satellite Server or Capsule Server requires you to plan scheduling, storage, and security so you avoid disruption and protect sensitive data.

### 11.1.1. Available backup methods

Choose an offline or online backup method based on how long you can keep Satellite services unavailable and how much time you can allocate for the backup.

Offline backup
:   All Satellite services are shut down during an offline backup.

    For more details, read help information for the offline backup:

    ```
    # satellite-maintain backup offline --help
    ```

Online backup
:   Only Satellite services that affect the consistency of the backup, including all background workers, are shut down while the backup process is running. Online backups check for consistency and require more time than offline backups.

    For more details, read help information for the online backup:

    ```
    # satellite-maintain backup online --help
    ```

### 11.1.2. Best practices for backing up Satellite Server and Capsule Servers

Apply these recommendations when scheduling and storing backups so you protect sensitive data and avoid conflicts with other administrators.

- Red Hat recommends backing up Satellite to a separate storage device on a separate system. The `satellite-maintain backup` command creates a backup of your Satellite Server or Capsule Server and all associated data.
- Satellite services are unavailable during the backup. Coordinate with other administrators to ensure no conflicting tasks run during the backup window.

  > **Warning**
  >
  > Request other users of Satellite Server or Capsule Server to save any changes and warn them that Satellite services are unavailable for the duration of the backup. Ensure no other tasks are scheduled for the same time as the backup.

  You can schedule a backup by using `cron`.

  > **Note**
  >
  > During offline backups, the services are inactive and Satellite is in a maintenance mode. A firewall rejects traffic from outside on port 443 to ensure there are no modifications triggered.
- Encrypt or move the backup to a secure location to minimize the risk of damage or unauthorized access to the hosts. A backup has sensitive information from the `/root/ssl-build` directory. For example, it can have hostnames, SSH keys, request files and SSL certificates.

### 11.1.3. Directories created during backups

Satellite organizes backups in time-stamped subdirectories, which helps you identify and select the correct backup when restoring your system.

The `satellite-maintain backup` command creates a time-stamped subdirectory in the backup directory that you specify. The `satellite-maintain backup` command does not overwrite backups, therefore you must select the correct directory or subdirectory when restoring from a backup or an incremental backup. The `satellite-maintain backup` command stops and restarts services as required.

When you run the `satellite-maintain backup offline` command, the following default backup directories are created:

- `satellite-backup` on Satellite
- `foreman-proxy-backup` on Capsule

If you want to set a custom directory name, add the `--preserve-directory` option and add a directory name. The backup is then stored in the directory you provide in the command line. If you use the `--preserve-directory` option, no data is removed if the backup fails.

### 11.1.4. Estimating the size of a backup

Estimate how much disk space a Satellite backup requires so you can ensure enough storage is available and avoid backup failures.

A full backup requires space to store the following data:

- Uncompressed Satellite database and configuration files
- Compressed Satellite database and configuration files
- An extra 20% of the total estimated space to ensure a reliable backup

Compression occurs after the archives are created to decrease the time when Satellite services are unavailable.

> **Note**
>
> Backups do not include container images for Red Hat Lightspeed in Satellite.

**Procedure**

1. Estimate the size of uncompressed directories containing Satellite database and configuration files:

   ```
   # du -sh /var/lib/pgsql/data /var/lib/pulp
   100G    /var/lib/pgsql/data
   100G	/var/lib/pulp

   # du -csh /var/lib/tftpboot /etc /root/ssl-build \
   /var/www/html/pub /opt/puppetlabs
   16M   /var/lib/tftpboot
   37M   /etc
   900K  /root/ssl-build
   100K  /var/www/html/pub
   2M    /opt/puppetlabs
   942M  total
   ```
2. Calculate how much space is required to store the compressed data.

   The following table describes the compression ratio of all data items included in the backup:

   Table 11.1. Backup data compression ratio

   | Data type | Directory | Ratio | Example results |
   | --- | --- | --- | --- |
   | PostgreSQL database files | `/var/lib/pgsql/data` | 80 – 85% | 100 GB → 20 GB |
   | Pulp RPM files | `/var/lib/pulp` | (not compressed) | 100 GB |
   | Configuration files | `/var/lib/tftpboot`    `/etc`    `/root/ssl-build`    `/var/www/html/pub`    `/opt/puppetlabs` | 85% | 942 MB → 141 MB |

   In this example, the compressed backup data occupies 120 GB in total.
3. To calculate the amount of available space you require to store a backup, calculate the sum of the estimated values of compressed and uncompressed backup data, and add an extra 20% to ensure a reliable backup.

   This example requires 201 GB plus 120 GB for the uncompressed and compressed backup data, 321 GB in total. With 64 GB of extra space, 385 GB must be allocated for the backup location.

## 11.2. Performing a full backup of Satellite Server or Capsule Server

Run a full offline backup on Satellite Server or Capsule Server to capture all Satellite content and configuration. A full backup is useful when you want to prepare for a future restore from scratch.

**Prerequisites**

- Your backup location must have sufficient available disk space to store the backup. For more information, see [Section 11.1.4, “Estimating the size of a backup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Estimating_the_Size_of_a_Backup_admin "11.1.4. Estimating the size of a backup").
- To enable Satellite to save the backup to an NFS share, the `root` user of your Satellite Server or Capsule Server must be able to write to the NFS share. NFS export options such as `root_squash` and `all_squash` are known to prevent this. For more information, see [Red Hat Enterprise Linux *Configuring and using network files services*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_using_network_file_services/deploying-an-nfs-server_configuring-and-using-network-file-services) and [Red Hat Enterprise Linux *Securing network services*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/securing_networks/securing-network-services_securing-networks#export-options-for-securing-an-nfs-server_securing-the-nfs-service).

> **Warning**
>
> Request other users of Satellite Server or Capsule Server to save any changes and warn them that Satellite services are unavailable for the duration of the backup. Ensure no other tasks are scheduled for the same time as the backup.

**Procedure**

1. Back up your Satellite Server:

   ```
   # satellite-maintain backup offline /var/satellite-backup
   ```
2. Back up your Capsule Server:

   ```
   # satellite-maintain backup offline /var/foreman-proxy-backup
   ```

## 11.3. Performing a backup without Pulp content

Run an offline backup that excludes the contents of the Pulp directory. A backup without Pulp content is useful for debugging purposes and is only intended to provide access to configuration files without backing up the Pulp database.

> **Warning**
>
> Do not use a backup without Pulp content to restore your Satellite Server or Capsule Server for production use cases.

**Prerequisites**

- Your backup location must have sufficient available disk space to store the backup. For more information, see [Section 11.1.4, “Estimating the size of a backup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Estimating_the_Size_of_a_Backup_admin "11.1.4. Estimating the size of a backup").

**Procedure**

- Back up your Satellite Server without Pulp content:

  ```
  # satellite-maintain backup offline --skip-pulp-content /var/backup_directory
  ```

## 11.4. Performing an incremental backup

Run an incremental backup to perform an offline backup that captures any changes since a previous full backup. Incremental backups use less time and storage than a full offline backup.

To perform incremental backups, you must perform a full backup as a reference to create the first incremental backup of a sequence. Keep the most recent full backup and a complete sequence of incremental backups to restore from.

**Prerequisites**

- Your backup location must have sufficient available disk space to store the backup. For more information, see [Section 11.1.4, “Estimating the size of a backup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Estimating_the_Size_of_a_Backup_admin "11.1.4. Estimating the size of a backup").

**Procedure**

1. Perform a full offline backup. For more information, see [Section 11.2, “Performing a full backup of Satellite Server or Capsule Server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Performing_a_Full_Backup_admin "11.2. Performing a full backup of Satellite Server or Capsule Server").
2. Create a directory within your backup directory to store the first incremental backup:

   ```
   # satellite-maintain backup offline --incremental /var/backup_directory/full_backup /var/backup_directory
   ```
3. Create the second incremental backup by including the path to the first incremental backup to indicate the starting point for the next increment. This creates a directory for the second incremental backup in your backup directory:

   ```
   # satellite-maintain backup offline --incremental /var/backup_directory/first_incremental_backup /var/backup_directory
   ```
4. Optional: If you want to point to a different version of the backup, and make a series of increments with that version of the backup as the starting point, you can do this at any time. For example, if you want to make a new incremental backup from the full backup rather than the first or second incremental backup, point to the full backup directory:

   ```
   # satellite-maintain backup offline --incremental /var/backup_directory/full_backup /var/backup_directory
   ```

## 11.5. Example of a weekly full backup followed by daily incremental backups

The following script performs a full backup on a Sunday followed by incremental backups for each of the following days. A new subdirectory is created for each day that an incremental backup is performed. The script requires a daily cron job.

```bash
#!/bin/bash -e
PATH=/sbin:/bin:/usr/sbin:/usr/bin
DESTINATION=/var/backup_directory
if [[ $(date +%w) == 0 ]]; then
  satellite-maintain backup offline --assumeyes $DESTINATION
else
  LAST=$(ls -td -- $DESTINATION/*/ | head -n 1)
  satellite-maintain backup offline --assumeyes --incremental "$LAST" $DESTINATION
fi
exit 0
```

Note that the `satellite-maintain backup` command requires `/sbin` and `/usr/sbin` directories to be in `PATH` and the `--assumeyes` option is used to skip the confirmation prompt.

## 11.6. Performing an online backup

Run an online backup to create a Satellite backup while keeping most services running. This is useful when you need to maintain system availability during backup operations.

When you perform an online backup, most Satellite services remain running and usable. Background workers are shut down to ensure consistent backups. Operations that require background workers remain in pending state. The backup process ensures that the Pulp data (`/var/lib/pulp`) is not altered during the backup. Any changes to the Pulp data during the backup will result in restart of the backup process, taking additional time.

**Prerequisites**

- Your backup location must have sufficient available disk space to store the backup. For more information, see [Section 11.1.4, “Estimating the size of a backup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Estimating_the_Size_of_a_Backup_admin "11.1.4. Estimating the size of a backup").

**Procedure**

- Perform an online backup on your Satellite Server:

  ```
  # satellite-maintain backup online /var/backup_directory
  ```

## 11.7. Creating a conventional backup

You can use conventional backup methods to back up your Satellite Server or Capsule Server. Unlike Satellite backup methods, conventional backup methods require you to stop Satellite services.

**Procedure**

1. When creating a snapshot or conventional backup, stop all Satellite services:

   ```
   # satellite-maintain service stop
   ```
2. Create the snapshot or conventional backup. For more information, see [Recovering and restoring a system in *Red Hat Enterprise Linux 9 Configuring basic system settings*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_basic_system_settings/index#assembly_recovering-and-restoring-a-system_configuring-basic-system-settings).
3. Start Satellite services after creating a snapshot or conventional backup:

   ```
   # satellite-maintain service start
   ```
