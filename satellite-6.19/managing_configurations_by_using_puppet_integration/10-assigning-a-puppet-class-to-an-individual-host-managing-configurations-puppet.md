---
title: "Assigning a Puppet class to an individual host"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#assigning-a-puppet-class-to-an-individual-host_managing-configurations-puppet"
---
# Chapter 10. Assigning a Puppet class to an individual host

Assigning a Puppet class to an individual host enables you to apply a specific configuration to that host, overriding any settings inherited from its host group. This is useful for custom configurations that you want to apply to a single host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Locate the host you want to add the `ntp` Puppet class to and click **Edit**.
3. Select the **Puppet ENC** tab and look for the ntp class.
4. Click the **+** symbol next to `ntp` to add the *ntp submodule* to the list of *included classes*.
5. Click **Submit** to save your changes.

   > **Tip**
   >
   > If the *Puppet classes* tab of an individual host is empty, check if it is assigned to the proper Puppet environment.

**Verification**

1. Verify the Puppet configuration.

   1. Navigate to **Hosts** > **All Hosts** and select the host.
   2. From the top overflow menu, select **Legacy UI**.
   3. Under **Details**, click **Puppet YAML**. This produces output similar as follows:

      ```yaml
      ---
      parameters:
        // shortened YAML output
      classes:
        ntp:
          servers: '["0.de.pool.ntp.org","1.de.pool.ntp.org","2.de.pool.ntp.org","3.de.pool.ntp.org"]'
      environment: production
      ...
      ```
2. Verify the ntp configuration.

   Connect to your host using SSH and check the content of `/etc/ntp.conf`.

   This example assumes your host is running *CentOS 7*. Other operating systems may store the ntp config file in a different path.

   > **Tip**
   >
   > You can rerun the OpenVox agent on your host:
   >
   > ```
   > # puppet agent -t
   > ```
3. Check which ntp servers are used for clock synchronization:

   ```
   # cat /etc/ntp.conf
   ```

   This returns output similar as follows:

   ```
   # ntp.conf: Managed by puppet.
   server 0.de.pool.ntp.org
   server 1.de.pool.ntp.org
   server 2.de.pool.ntp.org
   server 3.de.pool.ntp.org
   ```

   You now have a working ntp module which you can add to a host or group of hosts to roll out your ntp configuration automatically.
