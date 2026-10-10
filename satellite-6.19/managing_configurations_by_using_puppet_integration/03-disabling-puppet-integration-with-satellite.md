---
title: "Disabling Puppet integration with Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#disabling-puppet-integration-with-satellite"
---
# Chapter 3. Disabling Puppet integration with Satellite

Disable Puppet integration in Satellite when you no longer need configuration management or want to remove Puppet data from the database and server. Optionally remove all OpenVox server data, including environments, with the `--remove-all-data` argument.

> **Warning**
>
> If you disable Puppet with the `--remove-all-data` argument, you will not be able to re-enable Puppet afterwards. This is a known issue, see the [Bug 2087067](https://bugzilla.redhat.com/show_bug.cgi?id=2087067).

**Procedure**

1. If you have used OpenVox server on any Capsules, disable OpenVox server on all Capsules:

   ```
   # satellite-maintain plugin purge-puppet --remove-all-data
   ```
2. Disable OpenVox server on Satellite Server:

   ```
   # satellite-maintain plugin purge-puppet --remove-all-data
   ```
