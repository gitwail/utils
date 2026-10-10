---
title: "Preparing for disaster recovery and recovering from data loss"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#preparing-for-disaster-recovery-and-recovering-from-data-loss"
---
# Chapter 4. Preparing for disaster recovery and recovering from data loss

Red Hat recommends preparing a disaster recovery plan to ensure the continuity of Satellite services in case of a disruptive event. These guidelines help ensure that you will be able to restore your Satellite deployment to an operational state after an incident.

## 4.1. Overview of recommended disaster recovery plans

Choose a disaster recovery plan that best helps ensure the continuity of Satellite services in your deployment.

Snapshots of virtualized Satellite Server
:   How do I back up?
    :   Virtualize your Satellite Server and use the hypervisor tools to take virtual machine snapshots of the server. This method is suitable if you can run Satellite in a virtual machine.

    How will I recover in case of a disruptive event?
    :   To recover Satellite services, restore a virtual machine snapshot.

    Disadvantages and expected impact
    :   Expect some amount of data inconsistency after recovery, based on how old your last snapshot is. You will lose data changes that have occurred since the snapshot you are using to recover was taken.

Active and passive Satellite Server, with external storage
:   How do I back up?
    :   Store the following critical data on network attached storage: content in `/var/lib/pulp` and database in `/var/lib/pgsql`. Replicate this storage into a different data center. Attach the storage to a Satellite Server that is a clone of the primary Satellite Server but runs passively.

    How will I recover in case of a disruptive event?
    :   To recover Satellite services, switch DNS records of the active Satellite Server with the passive Satellite Server. This ensures that the passive server becomes the active server. All hosts remain connected without configuration updates.

    Disadvantages and expected impact
    :   If the network attached storage is replicated to another location, expect some amount of data inconsistency after recovery based on the synchronization interval.

Active and passive Satellite Server, with backup and restore
:   How do I back up?
    :   Ensure periodic backups of your Satellite Server. Copy this backup to a passive Satellite Server and restore it on the passive server.

    How will I recover in case of a disruptive event?
    :   To recover Satellite services, switch DNS records of the active Satellite Server with the passive Satellite Server. This ensures that the passive server becomes the active server. All hosts remain connected without configuration updates.

    Disadvantages and expected impact
    :   Expect some amount of data inconsistency after recovery, based on how often you took and restored backups and on how long it takes to complete the restore process.

Dual active Satellite Server
:   How do I back up?
    :   Operate an active, independent Satellite Server per data center. Hosts from each data center are registered to the Satellite Server in that data center. Then configure automation to ensure recovery in case of a disruptive event. For example, you can periodically run a health check and if the health check discovers that the current Satellite Server a host is registered to does not resolve, the host is re-registered to the other Satellite Server.

        To minimize downtime, you can automate the recovery in various ways. For example, you can use the Satellite Ansible collection. For more information, see [*Using the Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#).

    How will I recover in case of a disruptive event?
    :   To recover Satellite services, re-register all hosts to the Satellite Server in the other data center.

    Disadvantages and expected impact
    :   You must ensure that content synchronization and content view creation are synchronized to create the same content view in each Satellite and prevent content drift. Content drift occurs when available content deviates from the intended state defined by a content view. If you fail to prevent content drift, expect inconsistency in the content that is available to hosts.

## 4.2. Disaster recovery by virtualizing your Satellite Server

If you virtualize your Satellite Server and ensure that you take regular snapshots of the virtual machine (VM), you can respond to various disaster scenarios by restoring your Satellite deployment from one of your snapshots.

> **Note**
>
> The details for how to implement this scenario depend on your choice of a virtualization platform. Due to the variety of different hypervisors and their capabilities, Red Hat does not provide detailed instructions for any specific virtualization platform.

### 4.2.1. Preparing for disaster recovery by virtualizing your Satellite Server

Implement a reliable process for regularly taking VM snapshots of your virtualized Satellite Server and for backing up your snapshots for long-term storage.

**Prerequisites**

- You have reviewed [Section 4.1, “Overview of recommended disaster recovery plans”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#overview-of-recommended-disaster-recovery-plans "4.1. Overview of recommended disaster recovery plans") and determined that this disaster recovery plan works for you.
- Your Satellite Server is deployed as a VM.

**Procedure**

1. Define a schedule for taking periodic snapshots of your virtualized Satellite Server. Consider your tolerance for potential data loss: Taking snapshots frequently will result in smaller amounts of data loss in case of a disaster. However, creating a snapshot takes time, and the snapshots also require storage space.
2. Define your snapshot retention policy. Consider how many snapshots you want to store: Regularly removing outdated snapshots helps optimize storage usage.
3. Using your hypervisor, schedule periodic snapshots of your Satellite Server.
4. Schedule periodic backups of the snapshots to prevent data loss in case of hypervisor failure.

   > **Note**
   >
   > While snapshots provide quick recovery points, backing up your snapshots gives you the ability for long-term storage and provides extra safety in case of a disaster on the side of your hypervisor.
5. If you are using an external database that runs on a different machine than your Satellite Server, create snapshots and backups on the same schedule as your Satellite Server.

**Verification**

1. Verify that your hypervisor takes the snapshots according to the schedule that you defined.
2. Use the latest snapshot of your Satellite Server and restore it in an isolated environment.
3. To verify that you will be able to restore Satellite services in case of a disaster, assess the functionality of the test Satellite Server. For more information, see [Section 4.2.3, “Retrieving the status of services by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#retrieving-the-status-of-services-by-using-cli_dr-virt "4.2.3. Retrieving the status of services by using Hammer CLI").
4. Perform these verification checks regularly.

### 4.2.2. Recovering from disaster by restoring a VM snapshot of Satellite Server

In case of a disaster, use a virtual machine (VM) snapshot of your Satellite Server to restore Satellite services.

> **Important**
>
> Ensure that the hostname of your Satellite Server does not change during recovery. The IP address can change.

**Procedure**

1. Identify the snapshot from which you want to recover.
2. Use hypervisor tools to restore from the selected snapshot.
3. If you are using an external database that runs on a different machine than your Satellite Server, ensure that you restore the database from a snapshot taken at the same time as or before the Satellite Server snapshot.
4. Update DNS records so that the Satellite Server hostname resolves to the new IP address. This redirects traffic from the old server to the new server and you will not need to re-register your hosts.

**Verification**

- Assess the functionality of your restored Satellite Server. For more information, see [Section 4.2.3, “Retrieving the status of services by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#retrieving-the-status-of-services-by-using-cli_dr-virt "4.2.3. Retrieving the status of services by using Hammer CLI").

### 4.2.3. Retrieving the status of services by using Hammer CLI

Satellite uses a set of back-end services. When troubleshooting, you can check the status of Satellite services by using Hammer CLI.

**Procedure**

- Get information from the database and Satellite services:

  ```
  $ hammer ping
  ```
- Check the status of the services running in systemd:

  ```
  # satellite-maintain service status
  ```

  Run `satellite-maintain service --help` for more information.
- Perform a health check:

  ```
  $ satellite-maintain health check
  ```

  Run `satellite-maintain health --help` for more information.

## 4.3. Disaster recovery for active and passive Satellite Server with external storage

To prepare for disaster recovery, you can configure two Satellite Servers and store critical data externally on shared storage. The primary server is active while the secondary server remains passive. If the primary server fails, the shared storage is attached to your secondary server, which turns the secondary server into your new primary server.

### 4.3.1. Preparing for disaster recovery with active and passive Satellite Server with external storage

Create your passive Satellite Server as a clone of your active Satellite Server. Ensure that the `/var/lib/pulp` and `/var/lib/pgsql` directories on your shared storage are available to both servers.

**Prerequisites**

- You have reviewed [Section 4.1, “Overview of recommended disaster recovery plans”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#overview-of-recommended-disaster-recovery-plans "4.1. Overview of recommended disaster recovery plans") and determined that this disaster recovery plan works for you.
- Your shared storage meets the requirements for holding the contents of `/var/lib/pulp` and `/var/lib/pgsql`. For more information, see [Storage requirements](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#storage-requirements_satellite) in *Installing Satellite Server in a connected network environment*.
- You have configured your Satellite Server to use external databases. For more information, see [Migrating from internal Satellite databases to external databases](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Migrating_from_Internal_Databases_to_External_Databases_admin) in *Installing Satellite Server in a connected network environment*.

**Procedure**

1. Replicate the `/var/lib/pulp` and `/var/lib/pgsql` directories from the active Satellite Server to your shared storage.
2. Clone your active Satellite Server. For more information, see [Chapter 1, *Cloning Satellite Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#cloning-satellite-server "Chapter 1. Cloning Satellite Server").
3. Keep the source server powered on. Power off the new server.

   The source server remains your active primary server, while the new server becomes the passive secondary server.
4. Determine how you want to attach the database content on the shared storage to your passive server:

   - If you mount the storage directly on both your active and passive server, the servers will always see the same, up-to-date content.
   - If you mount the storage only on your active server, the passive server will access the data only if it takes over as the active server.

**Verification**

Perform this test in an isolated staging environment:

1. Mimic a full outage on the active server. To make sure the active server is inaccessible, you can turn the machine off, halt the virtual machine (VM) if your server runs on a VM, or isolate the machine by using a firewall.
2. Switch DNS records of the active server with the DNS records of the passive server.
3. Verify that your passive server can access the data stored on your shared storage.
4. Assess the functionality of the test Satellite Server. For more information, see [Section 4.3.3, “Retrieving the status of services by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#retrieving-the-status-of-services-by-using-cli_dr-storage "4.3.3. Retrieving the status of services by using Hammer CLI").
5. Perform these verification checks regularly.

**Additional resources**

- [Mounting file systems on demand in *Red Hat Enterprise Linux 9 Managing file systems*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_file_systems/index#mounting-file-systems-on-demand_managing-file-systems)

### 4.3.2. Recovering from disaster with active and passive server with external storage

If your active Satellite Server fails, detach it from the shared storage and make sure your passive server can access the data stored on the shared storage. This turns the passive server into your new active server.

**Procedure**

1. Verify that the failed active server is powered off or fully detached from the shared storage. This ensures that the failed server cannot keep writing to the shared storage.
2. Switch DNS records of the active server with the DNS records of the passive server. This ensures that hosts remain connected and you do not need to re-register them.
3. If your shared storage was mounted on both your active and passive servers, your passive server can already access the data.
4. If your shared storage was mounted only on your active server, re-mount it on your passive server.
5. Assess the functionality of your new active Satellite Server. For more information, see [Section 4.3.3, “Retrieving the status of services by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#retrieving-the-status-of-services-by-using-cli_dr-storage "4.3.3. Retrieving the status of services by using Hammer CLI").

### 4.3.3. Retrieving the status of services by using Hammer CLI

Satellite uses a set of back-end services. When troubleshooting, you can check the status of Satellite services by using Hammer CLI.

**Procedure**

- Get information from the database and Satellite services:

  ```
  $ hammer ping
  ```
- Check the status of the services running in systemd:

  ```
  # satellite-maintain service status
  ```

  Run `satellite-maintain service --help` for more information.
- Perform a health check:

  ```
  $ satellite-maintain health check
  ```

  Run `satellite-maintain health --help` for more information.

## 4.4. Disaster recovery for active and passive Satellite Server with backup and restore

To prepare for disaster recovery, you can configure two Satellite Servers: an active primary server and a passive secondary server. You configure periodic backups of the primary server. If the primary server fails, you can restore a backup on the secondary server to turn it into your new primary server.

### 4.4.1. Preparing for disaster recovery with active and passive Satellite Server and backup and restore

Create your passive Satellite Server by restoring a backup of your active Satellite Server. Configure periodic backups of the active server.

**Prerequisites**

- You have reviewed [Section 4.1, “Overview of recommended disaster recovery plans”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#overview-of-recommended-disaster-recovery-plans "4.1. Overview of recommended disaster recovery plans") and determined that this disaster recovery plan works for you.
- You have a Satellite Server installed.

**Procedure**

1. Define a schedule for periodic offline backups of your active Satellite Server. Consider your tolerance for potential data loss and your storage options: Taking backups frequently will result in smaller amounts of data loss in case of a disaster, but backups require a significant amount of storage space. For information about the size of Satellite backups, see [Section 11.1.4, “Estimating the size of a backup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Estimating_the_Size_of_a_Backup_admin "11.1.4. Estimating the size of a backup").

   You can combine full backups with incremental backups. For an example of a `cron` job that ensures regular backups, see [Section 4.4.4, “Example of a weekly full backup followed by daily incremental backups”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Example_of_a_Weekly_Full_Backup_Followed_by_Daily_Incremental_Backups_dr-backup-restore "4.4.4. Example of a weekly full backup followed by daily incremental backups").
2. Schedule periodic offline backups of your active Satellite Server to be taken according to the schedule you defined. For information about performing backups, see [Chapter 11, *Backing up Satellite Server and Capsule Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin "Chapter 11. Backing up Satellite Server and Capsule Server").
3. Ensure that the backup directories are encrypted and regularly synchronized to a secure location. By default, Satellite stores the backups in the `/var/satellite-backup` directory.

   > **Important**
   >
   > Satellite Server backups contain sensitive information from the `/root/ssl-build` directory. For example, they can contain hostnames, ssh keys, request files, and SSL certificates. Encrypting or moving the backups to a secure location helps minimize the risk of damage or unauthorized access to the hosts.
4. Restore the most recent backup on a system that will serve as your passive Satellite Server. For information about restoring backups, see [Chapter 12, *Restoring Satellite Server or Capsule Server from a backup*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#restoring-satellite-server-or-capsule-from-a-backup_admin "Chapter 12. Restoring Satellite Server or Capsule Server from a backup").
5. Optional: Automate backup restoration to keep the passive server periodically updated with the latest backup. A regularly restored passive server helps reduce switchover time if the active server fails.

   Consider how often you want the backups to be restored: More frequent updates reduce potential data loss but increase infrastructure and automation costs.
6. Power off the passive server. Keep the active server powered on.
7. Define your backup retention policy. Consider how many backups you want to store: Regularly removing outdated backups helps optimize storage usage.

**Verification**

1. Verify that Satellite takes backups according to the schedule you defined.
2. Perform further testing steps in an isolated staging environment:

   1. Mimic a full outage on the active server. To make sure the active server is inaccessible, you can turn the machine off, halt the virtual machine (VM) if your server runs on a VM, or isolate the machine by using a firewall.
   2. Switch DNS records of the active server with the DNS records of the passive server.
   3. Assess the functionality of the test Satellite Server. For more information, see [Section 4.4.3, “Retrieving the status of services by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#retrieving-the-status-of-services-by-using-cli_dr-backup-restore "4.4.3. Retrieving the status of services by using Hammer CLI").
   4. Perform these verification checks regularly.

### 4.4.2. Recovering from disaster with active and passive server and backup and restore

If your active Satellite Server fails, activate your passive secondary server.

**Procedure**

1. Verify that the failed active server is powered off and that backups are no longer being synchronized to your passive server.
2. Switch DNS records of the active server with the DNS records of the passive server. This ensures that hosts remain connected and you do not need to re-register them.
3. Assess the functionality of your new active Satellite Server. For more information, see [Section 4.4.3, “Retrieving the status of services by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#retrieving-the-status-of-services-by-using-cli_dr-backup-restore "4.4.3. Retrieving the status of services by using Hammer CLI").

### 4.4.3. Retrieving the status of services by using Hammer CLI

Satellite uses a set of back-end services. When troubleshooting, you can check the status of Satellite services by using Hammer CLI.

**Procedure**

- Get information from the database and Satellite services:

  ```
  $ hammer ping
  ```
- Check the status of the services running in systemd:

  ```
  # satellite-maintain service status
  ```

  Run `satellite-maintain service --help` for more information.
- Perform a health check:

  ```
  $ satellite-maintain health check
  ```

  Run `satellite-maintain health --help` for more information.

### 4.4.4. Example of a weekly full backup followed by daily incremental backups

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

## 4.5. Disaster recovery with two active Satellite Servers

To prepare for disaster recovery, you can configure two Satellite Servers and operate each server in a different data center. If one of the servers fails, you can re-register all hosts from the failed server to the other server.

### 4.5.1. Preparing for disaster recovery with two active Satellite Servers

Create a second Satellite Server by restoring a backup of your first Satellite Server. Configure both servers to operate independently in their respective data centers, but ensure that their content does not drift apart over time.

> **Note**
>
> Ansible playbooks can help you automate failover, re-registration, and synchronization. For more information, see [*Using the Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#).

**Prerequisites**

- You have reviewed [Section 4.1, “Overview of recommended disaster recovery plans”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#overview-of-recommended-disaster-recovery-plans "4.1. Overview of recommended disaster recovery plans") and determined that this disaster recovery plan works for you.
- You have a Satellite Server installed.

**Procedure**

1. Back up your Satellite Server. For more information, see [Chapter 11, *Backing up Satellite Server and Capsule Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin "Chapter 11. Backing up Satellite Server and Capsule Server").
2. Restore the backup on a system that will serve as your other Satellite Server. For more information, see [Chapter 12, *Restoring Satellite Server or Capsule Server from a backup*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#restoring-satellite-server-or-capsule-from-a-backup_admin "Chapter 12. Restoring Satellite Server or Capsule Server from a backup").

   > **Note**
   >
   > Each server must have a distinct hostname and IP address. This enables you to re-register hosts if one of the servers fails.
3. Ensure that content on your servers remains consistent:

   - If you want both servers to manage content synchronization and content view creation, follow these guidelines to prevent content drift:

     - Regularly synchronize repositories on both servers. You can use the following Ansible modules to automate repository synchronization: `redhat.satellite.repository_sync` and `redhat.satellite.sync_plan`.
     - Ensure that content views on both servers match.
   - If you want one server to manage content synchronization and content view creation, use one of these features to prevent content drift:

     - If your disaster recovery site has network access to your primary site, use Inter-Satellite Synchronization (ISS) to ensure your disaster recovery server synchronizes its content from the primary server.
     - If your disaster recovery site does not have network access to your primary site, synchronize content by using export and import.
   - If you want one server to manage only content view creation but not content synchronization, you can configure the other server or multiple other servers to import content views from the first server but synchronize content from repositories.
4. Register hosts to your servers so that each server manages hosts in its respective data center. For example, register all hosts in *My_Data_Center_1* to one Satellite Server and all hosts in *My_Data_Center_2* to the other Satellite Server.
5. Automate running the `satellite-maintain health check` command on both servers. The health check verifies whether the servers remain fully operational.

**Verification**

Perform this test in an isolated staging environment:

1. Mimic a full outage on one of your servers. To verify that the server is inaccessible, you can turn the machine off, halt the virtual machine (VM) if your server runs on a VM, or isolate the machine by using a firewall.
2. Verify that your `satellite-maintain health check` automation reported an error.
3. Re-register all hosts from the inaccessible server to the accessible server.
4. Verify that hosts have been properly re-registered to the accessible server.
5. Perform these verification checks regularly.

**Additional resources**

- [Synchronizing repositories ad hoc in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc)
- [Synchronizing content between Satellite Servers in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Synchronizing_Content_Between_Servers_content-management)

### 4.5.2. Recovering from disaster with two active Satellite Servers

If the health checks implemented in [Section 4.5.1, “Preparing for disaster recovery with two active Satellite Servers”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#preparing-for-disaster-recovery-with-two-active-project-servers "4.5.1. Preparing for disaster recovery with two active Satellite Servers") report an issue on one of your Satellite Servers, it might mean that the server has failed. If the server is down, you must re-register hosts to the other server.

> **Note**
>
> Ansible playbooks can help you automate failover, re-registration, and synchronization. For more information, see [*Using the Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#).

**Procedure**

1. Verify the status of the server:

   ```
   $ satellite-maintain health check
   ```
2. If `satellite-maintain health check` reported a problem, ensure that the server is powered off.
3. Re-register all hosts from the data center managed by the failed server to the other, functional server.

**Verification**

- Verify that hosts have been properly re-registered.
