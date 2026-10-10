---
title: "Updating Capsule Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "updating_red_hat_satellite"
guide_title: "Updating Red Hat Satellite"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/updating_red_hat_satellite/index#Updating-Smart-Proxy_updating"
---
# Chapter 4. Updating Capsule Server

Update Capsule Servers to the next patch version.

**Procedure**

1. Synchronize the `satellite-capsule-6.19-for-rhel-9-x86_64-rpms` repository in the Satellite Server.
2. Publish and promote a new version of the content view with which the Capsule is registered.
3. Ensure that the Satellite Maintenance repository is enabled:

   ```
   # subscription-manager repos --enable \
   satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```
4. Use the health check option to determine if the system is ready for update:

   ```
   # satellite-maintain update check
   ```

   Review the results and address any highlighted error conditions before performing the update.
5. Because of the lengthy update time, use a utility such as `tmux` to suspend and reattach a communication session. You can then check the update progress without staying connected to the command shell continuously.

   If you lose connection to the command shell where the update command is running, you can see the logged messages in the `/var/log/foreman-installer/capsule.log` file to check if the process completed successfully.
6. Perform the update:

   ```
   # satellite-maintain update run
   ```
7. If the `satellite-maintain` command told you to reboot, then reboot the system:

   ```
   # reboot
   ```
