---
title: "Updating a disconnected Satellite Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "updating_red_hat_satellite"
guide_title: "Updating Red Hat Satellite"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/updating_red_hat_satellite/index#Updating-Disconnected-satellite_updating"
---
# Chapter 3. Updating a disconnected Satellite Server

You can update your air-gapped Satellite to the next patch version by creating a local repository using exported content from a connected Satellite Server.

You export synchronized repositories from the connected Satellite Server, create local repositories on your air-gapped Satellite Server, and update your air-gapped Satellite Server. This process also updates the base operating system on your air-gapped Satellite Server when a new minor version is available.

> **Important**
>
> Back up your disconnected Satellite Server before updating it.

**Additional resources**

- [Backing Up Satellite Server and Capsule Server in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin)

## 3.1. Exporting repositories from the connected Satellite Server

Export the required repositories on the connected Satellite Server to transfer to the disconnected Satellite Server.

**Procedure**

1. Synchronize the following repositories on your connected Satellite Server:

   - `rhel-9-for-x86_64-baseos-rpms`
   - `rhel-9-for-x86_64-appstream-rpms`
   - `satellite-6.19-for-rhel-9-x86_64-rpms`
   - `satellite-maintenance-6.19-for-rhel-9-x86_64-rpms`

   Ensure to set the download policy to **Immediate** for each repository.
2. List the repositories to identify their IDs:

   ```
   $ hammer repository list \
   --organization-label My_Organization_Label
   ```
3. Export each repository in the syncable format:

   ```
   $ hammer content-export complete repository \
   --format syncable \
   --id My_Repository_ID
   ```
4. Transfer the exported directories to your disconnected Satellite Server.

## 3.2. Preparing repositories on the disconnected Satellite Server

Create local repositories on your disconnected Satellite Server.

**Prerequisites**

- You have transferred the exported directories to your disconnected Satellite Server.

**Procedure**

1. Locate the transferred exported directories.
2. Create the `/etc/yum.repos.d/update.repo` file and update the `baseurl` values to point to the local file system:

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
   enabled=1
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

## 3.3. Performing the update of the disconnected Satellite Server

Evaluate that the system is ready for update and perform the update of the disconnected Satellite Server. Your Satellite Server does not require internet access to perform the update.

**Prerequisites**

- You have prepared the required repositories on the disconnected Satellite Server.

**Procedure**

1. Evaluate that the system is ready for update:

   ```
   # satellite-maintain update check --whitelist="repositories-validate,repositories-setup"
   ```

   The first time you run this command, `satellite-maintain` prompts you to enter the Hammer admin user credentials and saves them to `/etc/foreman-maintain/foreman-maintain-hammer.yml`.
2. Review the results and resolve any errors before proceeding with the update.
3. Due to the lengthy update time, use a utility such as `tmux` to suspend and resume the session as needed. By using such utility, you can monitor progress without maintaining a continuous connection to the command shell.

   If you lose connection to the command shell where the update command is running, check the `/var/log/foreman-installer/satellite.log` file to confirm whether the process completed successfully.
4. Perform the update:

   ```
   # satellite-maintain update run --whitelist="repositories-validate,repositories-setup"
   ```
5. If the `satellite-maintain` command told you to reboot, then reboot the system:

   ```
   # reboot
   ```

**Additional resources**

- [Restoring Satellite Server or Capsule Server from a backup](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Restoring_from_a_Full_Backup_admin)
