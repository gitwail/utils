---
title: "Removing a virt-who configuration"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_virt-who_for_virtual_machine_subscriptions"
guide_title: "Configuring virt-who for virtual machine subscriptions"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt-who_for_virtual_machine_subscriptions/index#removing-an-existing-virt-who-configuration"
---
# Chapter 10. Removing a virt-who configuration

You can remove a virt-who configuration by deleting the configuration in the Satellite web UI and then by deleting the configuration file from the hypervisor or the virtualization manager.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Virt-who Configurations**.
2. Select **Delete** from the **Actions** column of the virt-who configuration.
3. On the hypervisor or virtualization manager, remove the configuration file by running the following command:

   ```
   $ rm /etc/virt-who.d/conf_name.conf
   ```
