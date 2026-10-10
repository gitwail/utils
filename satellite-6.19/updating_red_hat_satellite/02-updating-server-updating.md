---
title: "Updating Satellite Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "updating_red_hat_satellite"
guide_title: "Updating Red Hat Satellite"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/updating_red_hat_satellite/index#Updating_Server_updating"
---
# Chapter 2. Updating Satellite Server

Update your connected Satellite Server to the next patch version. You can follow this process to update the underlying operating system between minor release versions. For information to update a disconnected Satellite setup, see [Chapter 3, *Updating a disconnected Satellite Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/updating_red_hat_satellite/index#Updating-Disconnected-satellite_updating "Chapter 3. Updating a disconnected Satellite Server").

If you use the Red Hat Lightspeed in Satellite, the following process updates Red Hat Lightspeed in Satellite to the latest version. The `satellite-maintain` tool pulls the new container images of the Red Hat Lightspeed in Satellite automatically.

**Prerequisites**

- Back up your Satellite Server. For more information, see [Backing Up Satellite Server and Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin) in *Administering Red Hat Satellite*.

> **Warning**
>
> Note that the satellite-installer is executed during an upgrade or update. Any files managed by satellite-installer are overwritten. Check if you have any manual changes that would be overwritten by satellite-installer. You can use the `--noop` option with the satellite-installer to test for changes. For more information, see the Red Hat Knowledgebase solution [How to use the noop option to check for changes in Satellite config files during an upgrade.](https://access.redhat.com/solutions/3351311)

**Procedure**

1. Ensure the Satellite Maintenance repository is enabled:

   ```
   # subscription-manager repos --enable \
   satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```
2. Use the health check option to determine if the system is ready for update. On first use of this command, `satellite-maintain` prompts you to enter the hammer admin user credentials and saves them in the `/etc/foreman-maintain/foreman-maintain-hammer.yml` file.

   ```
   # satellite-maintain update check
   ```

   Review the results and address any highlighted error conditions before performing the update.
3. Because of the lengthy update time, use a utility such as `tmux` to suspend and reattach a communication session. You can then check the update progress without staying connected to the command shell continuously.

   If you lose connection to the command shell where the update command is running, you can see the logged messages in the `/var/log/foreman-installer/satellite.log` file to check if the process completed successfully.
4. Perform the update:

   ```
   # satellite-maintain update run
   ```
5. If the `satellite-maintain` command told you to reboot, then reboot the system:

   ```
   # reboot
   ```

**Additional resources**

- [Restoring Satellite Server or Capsule Server from a Backup](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Restoring_from_a_Full_Backup_admin)
