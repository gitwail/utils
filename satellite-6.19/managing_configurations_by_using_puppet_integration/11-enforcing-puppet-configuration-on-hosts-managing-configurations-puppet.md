---
title: "Enforcing Puppet configuration on hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "11"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#enforcing-puppet-configuration-on-hosts_managing-configurations-puppet"
---
# Chapter 11. Enforcing Puppet configuration on hosts

You can enforce configuration from Satellite either manually on demand or automatically in configurable intervals.

## 11.1. Running Puppet once using SSH

Assign the job template to the *Run Puppet Once* feature to apply Puppet configuration on selected hosts immediately without waiting for the next scheduled run.

**Procedure**

1. Edit remote execution settings on Satellite:

   1. In the Satellite web UI, navigate to **Administer** > **Remote Execution Features**.
   2. Select the `puppet_run_host` remote execution feature.
   3. Assign the `Puppet Run Once – Script Default` job template.
2. To run Puppet on hosts, execute a remote job and select category `Puppet` and template `Puppet Run Once - Script Default`. Alternatively, click **Run Puppet Once** in the **Schedule Remote Job** drop down menu on the host details page.

## 11.2. Configuring Puppet intervals of automatic enforcement

Tune enforcement frequency and reporting by configuring intervals of automatic enforcement for Puppet.

Satellite considers hosts to be out of sync if the last Puppet report is older than the combined values of `outofsync_interval` and `puppet_interval` set in minutes.

Default values for automatic enforcement are as follows:

- The OpenVox agent on your hosts runs every 30 minutes
- The `puppet_interval` value is 35 minutes
- The global `outofsync_interval` value is 30 minutes

**Procedure**

1. Set the interval when the OpenVox agent runs and sends reports to Satellite:

   1. Connect to your host using SSH.
   2. Add the OpenVox agent run interval to `/etc/puppetlabs/puppet/puppet.conf`, for example, `runinterval = 1h`:
2. Set the global out-of-sync interval:

   1. In the Satellite web UI, navigate to **Administer** > **Settings**.
   2. On the **General** tab, edit **Out of sync interval**. Set a duration, in minutes, after which hosts are considered to be out of sync.
3. Set the Puppet out-of-sync interval:

   1. In the Satellite web UI, navigate to **Administer** > **Settings**.
   2. Select the **Config Management** tab.
   3. In the **Puppet interval** field, set the value to the duration, in minutes, after which hosts reporting using Puppet are considered to be out of sync.

**Example 11.1. Example automatic enforcement values**

The effective time after which hosts are considered out of sync is the sum of `outofsync_interval` and `puppet_interval`. For example, setting the global `outofsync_interval` to 30 and the `puppet_interval` to 60 results in a total of 90 minutes after which the host status changes to `out of sync`.

## 11.3. Overriding out-of-sync interval for a host group

You can override the out-of-sync interval for a host group from the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. Select a host group.
3. On the **Parameters** tab, click **Add Parameter**.
4. In the **Name** field, enter `outofsync_interval`.
5. From the **Type** dropdown menu, select `integer`.
6. In the **Value** field, enter the new interval in minutes.
7. Click **Submit**.

## 11.4. Overriding out-of-sync interval for an individual host

You can override the out-of-sync interval for an individual host from the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click **Edit** for a selected host.
3. On the **Parameters** tab, click **Add Parameter**.
4. In the **Name** field, enter `outofsync_interval`.
5. From the **Type** dropdown menu, select `integer`.
6. In the **Value** field, enter the new interval in minutes.
7. Click **Submit**.
