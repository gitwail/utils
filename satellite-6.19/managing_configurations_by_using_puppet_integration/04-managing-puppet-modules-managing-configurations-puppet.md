---
title: "Managing Puppet modules"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#managing-puppet-modules_managing-configurations-puppet"
---
# Chapter 4. Managing Puppet modules

Managing Puppet modules includes installing the modules from your preferred source and keeping them updated.

## 4.1. Installing a Puppet module on Satellite server

You can install a pre-built Puppet module from the Puppet Forge or a private Puppet module that is not available on the Puppet Forge by manually coping the module to your Satellite Server. The Puppet Forge is a repository that provides Puppet modules contributed by the community.

> **Note**
>
> Puppet modules flagged as *supported* are officially supported and tested by Puppet Inc.

**Procedure**

1. Navigate to [forge.puppet.com](https://forge.puppet.com/) and search for the Puppet module you want.
2. Choose how to install the Puppet module:

   - To install from the Puppet forge, install the Puppet module on your Satellite Server:

     ```
     # puppet module install My_Puppet_Module -i /etc/puppetlabs/code/environments/production/modules
     ```

     Use the `-i` parameter to specify the path and Puppet environment, for example `production`.

     Once the installation is completed, the output looks as follows:

     ```
     Notice: Preparing to install into /etc/puppetlabs/code/environments/production/modules ...
     Notice: Created target directory /etc/puppetlabs/code/environments/production/modules
     Notice: Downloading from https://forgeapi.puppet.com ...
     Notice: Installing -- do not interrupt ...
     /etc/puppetlabs/code/environments/production/modules
     |-| puppetlabs-ntp (v8.3.0)
       |-- puppetlabs-stdlib (v4.25.1) [/etc/puppetlabs/code/environments/production/modules]
     ```
   - To install manually, copy the module and its dependencies to Satellite Server:

     ```
     $ scp -r My_Puppet_Module root@satellite.example.com:/etc/puppetlabs/code/environments/production/modules/My_Puppet_Module
     ```

## 4.2. Updating a Puppet module on your Satellite Server

Regularly updating Puppet modules installed on your Satellite Server helps ensure they stay up-to-date with their source.

**Procedure**

1. Connect to your OpenVox server using SSH and find out where the Puppet modules are located:

   ```
   # puppet config print modulepath
   ```

   This returns output as follows:

   ```
   /etc/puppetlabs/code/environments/production/modules:/etc/puppetlabs/code/environments/common:/etc/puppetlabs/code/modules:/opt/puppetlabs/puppet/modules:/usr/share/puppet/modules
   ```
2. If the module is located in the path as displayed above, the following command updates a module:

   ```
   # puppet module upgrade module name
   ```
