---
title: "Importing Puppet classes and environments into Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#Importing_Puppet_Classes_and_Environments_managing-configurations-puppet"
---
# Chapter 5. Importing Puppet classes and environments into Satellite

Import Puppet classes and environments from the installed Puppet modules to Satellite Server or any attached Capsule Server before you assign any of the classes to hosts.

**Prerequisites**

- Ensure to select **Any Organization** and **Any Location** as context, otherwise the import might fail.
- Before you run an import of Puppet modules into Satellite, the environment must already exist as the folder `/etc/puppetlabs/code/environments/example_environment` on the OpenVox server and contain installed Puppet modules.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Puppet ENC** > **Classes** or **Configure** > **Puppet ENC** > **Environments**.
2. Click **Import** in the upper right corner and select which Capsule you want to import modules from. You may typically choose between your Satellite Server or any attached Capsule Server.
3. Select the Puppet environments to import using checkboxes on the left.
4. Click **Update** to import the Puppet environments and classes to Satellite.
5. The import should result in a notification as follows:

   ```
   Successfully updated environments and Puppet classes from the on-disk Puppet installation
   ```
