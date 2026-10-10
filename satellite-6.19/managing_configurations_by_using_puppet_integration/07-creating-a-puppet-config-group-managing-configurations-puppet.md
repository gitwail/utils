---
title: "Creating a Puppet config group"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#creating-a-puppet-config-group_managing-configurations-puppet"
---
# Chapter 7. Creating a Puppet config group

A Puppet config group is a named list of Puppet classes that allows you to combine their capabilities and assign them to hosts at a click. This is equivalent to the concept of profiles in pure Puppet.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Puppet ENC** > **Config Groups**.
2. Click **Create Config Group**.
3. Select the classes you want to add to the config group.

   1. Choose a meaningful **Name** for the Puppet config group.
   2. Add selected Puppet classes to the **Included Classes** field.
4. Click **Submit** to save the changes.
