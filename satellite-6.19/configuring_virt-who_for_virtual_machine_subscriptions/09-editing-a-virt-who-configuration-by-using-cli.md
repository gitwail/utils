---
title: "Editing a virt-who configuration by using Hammer CLI"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_virt-who_for_virtual_machine_subscriptions"
guide_title: "Configuring virt-who for virtual machine subscriptions"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt-who_for_virtual_machine_subscriptions/index#editing-a-virt-who-configuration-by-using-cli"
---
# Chapter 9. Editing a virt-who configuration by using Hammer CLI

Edit your virt-who configuration by using Hammer CLI to update settings such as reporting intervals, hypervisor credentials, and filtering options. This ensures accurate virtual machine reporting and proper subscription management.

**Procedure**

1. Update the virt-who configuration:

   ```
   $ hammer virt-who-config update \
   --name My_virt-who_Configuration \
   --new-name My_new_virt-who_Configuration \
   --interval 1440
   ```
2. Deploy the modified virt-who configuration.
