---
title: "Assigning a Puppet class to a host group"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#assigning-a-puppet-class-to-a-host-group_managing-configurations-puppet"
---
# Chapter 9. Assigning a Puppet class to a host group

Use a host group to assign the *ntp* Puppet class to multiple hosts at once. Every host you deploy based on this host group has this Puppet class installed.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. Create or edit a host group.
3. On the **Host Group** tab, set the following:

   1. The **Lifecycle Environment** describes the stage in which certain versions of content are available to hosts.
   2. The **Content View** is comprised of products and allows for version control of content repositories.
   3. The **Environment** allows you to supply a group of hosts with their own dedicated configuration.
4. Navigate to the **Puppet ENC** tab.
5. Add the Puppet class to the *Included Classes* or to the *Included Config Groups* if a Puppet config group is configured.
6. Click **Submit** to save the changes.
