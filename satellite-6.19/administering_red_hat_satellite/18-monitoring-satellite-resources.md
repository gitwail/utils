---
title: "Monitoring Satellite resources"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "18"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#monitoring-satellite-resources"
---
# Chapter 18. Monitoring Satellite resources

You can use Satellite web UI to monitor your Satellite environment and hosts. This includes details of hosts, such as configuration or compliance, and information about content and Capsules.

## 18.1. Using the Red Hat Satellite content dashboard

The Red Hat Satellite content dashboard contains various widgets. Use the dashboard to get a quick overview of the resources currently in use in Satellite.

In the Satellite web UI, navigate to **Monitor** > **Dashboard** to access the content dashboard. The dashboard can be rearranged by clicking on a widget and dragging it to a different position. The following widgets are available:

**Host Configuration Status**
:   An overview of the configuration states and the number of hosts associated with it during the last reporting interval. The following table shows the descriptions of the possible configuration states.

    Table 18.1. Host configuration states

    | Icon | State | Description |
    | --- | --- | --- |
    | [Image: host state config okay](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Administering_Red_Hat_Satellite-en-US/images/f3750aff74bb4fd738bd2fb0616397d6/host-state-config-okay.png) | **Hosts that had performed modifications without error** | Host that successfully performed modifications during the last reporting interval. |
    | [Image: host state config error](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Administering_Red_Hat_Satellite-en-US/images/b463ee593ffcf0847b53d10e28a1c303/host-state-config-error.png) | **Hosts in error state** | Hosts on which an error was detected during the last reporting interval. |
    | [Image: host state config report](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Administering_Red_Hat_Satellite-en-US/images/550ba146c57251a00dfd10e9737aa13a/host-state-config-report.png) | **Good host reports in the last 35 minutes** | Hosts without error that did not perform any modifications in the last 35 minutes. |
    | [Image: host state config pending](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Administering_Red_Hat_Satellite-en-US/images/18622573aa5659eeac62a835ee2c3f65/host-state-config-pending.png) | **Hosts that had pending changes** | Hosts on which some resources would be applied but Puppet was configured to run in the `noop` mode. |
    | [Image: host state config outofsync](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Administering_Red_Hat_Satellite-en-US/images/ef3f9ea7cf9f2aecd989fb547b151115/host-state-config-outofsync.png) | **Out of sync hosts** | Hosts that were not synchronized and the report was not received during the last reporting interval. |
    | [Image: host state config noreport](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Administering_Red_Hat_Satellite-en-US/images/6b059438b7fa009fd8ba7a122c87fdf9/host-state-config-noreport.png) | **Hosts with no reports** | Hosts for which no reports were collected during the last reporting interval. |
    | [Image: host state config noalert](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Administering_Red_Hat_Satellite-en-US/images/426ff6b84104d3ad425d664c3d40fb8e/host-state-config-noalert.png) | **Hosts with alerts disabled** | Hosts which are not being monitored. |

    Click the particular configuration status to view hosts associated with it.

**Host Configuration Chart**
:   A pie chart shows the proportion of the configuration status and the percentage of all hosts associated with it.

**Latest Events**
:   A list of messages produced by hosts including administration information, product changes, and any errors.

    Monitor this section for global notifications sent to all users and to detect any unusual activity or errors.

**Run Distribution (last 30 minutes)**
:   A graph shows the distribution of the running OpenVox agents during the last puppet interval which is 30 minutes by default. In this case, each column represents several reports received from clients during 3 minutes.

**New Hosts**
:   A list of the recently created hosts. Click the host for more details.

**Task Status**
:   A summary of all current tasks, grouped by their state and result. Click the number to see the list of corresponding tasks.

**Latest Warning/Error Tasks**
:   A list of the latest tasks that have been stopped due to a warning or error. Click a task to see more details.

**Discovered Hosts**
:   A list of all bare-metal hosts detected on the provisioning network by the Discovery plugin.

**Latest Errata**
:   A list of all errata available for hosts registered to Satellite.

**Content Views**
:   A list of all content views in Satellite and their publish status.

**Sync Overview**
:   An overview of all products or repositories enabled in Satellite and their synchronization status. All products that are in the queue for synchronization, are unsynchronized or have been previously synchronized are listed in this section.

**Host Collections**
:   A list of all host collections in Satellite and their status, including the number of hosts in each host collection.

**Virt-who Configuration Status**
:   An overview of the status of reports received from the `virt-who` daemon running on hosts in the environment. The following table shows the possible states.

    Table 18.2. virt-who configuration states

    | State | Description |
    | --- | --- |
    | **No Reports** | No report has been received because either an error occurred during the virt-who configuration deployment, or the configuration has not been deployed yet, or virt-who cannot connect to Satellite during the scheduled interval. |
    | **No Change** | No report has been received because hypervisor did not detect any changes on the virtual machines, or virt-who failed to upload the reports during the scheduled interval. If you added a virtual machine but the configuration is in the **No Change** state, check that virt-who is running. |
    | **OK** | The report has been received without any errors during the scheduled interval. |
    | **Total Configurations** | A total number of virt-who configurations. |

    Click the configuration status to see all configurations in this state.

    The widget also lists the three latest configurations in the **No Change** state under **Latest Configurations Without Change**.

**Latest Compliance Reports**
:   A list of the latest compliance reports. Each compliance report shows several rules passed (P), failed (F), or othered (O). Click the host for the detailed compliance report. Click the policy for more details on that policy.

**Compliance Reports Breakdown**
:   A pie chart shows the distribution of compliance reports according to their status.

**Red Hat Lightspeed Actions**
:   Red Hat Lightspeed is a tool embedded in Satellite that checks the environment and suggests actions you can take. The actions are divided into 4 categories: Availability, Stability, Performance, and Security.

**Red Hat Lightspeed Risk Summary**
:   A table shows the distribution of the actions according to the risk levels. Risk level represents how critical the action is and how likely it is to cause an actual issue. The possible risk levels are: Low, Medium, High, and Critical.

## 18.2. Satellite task management

You can monitor and manage all planned or performed tasks, such as repositories synchronized, errata applied, and content views published. This is useful to track progress, troubleshoot issues, or adjust timeout settings for low bandwidth or high latency environments.

Reviewing the log
:   To review the log, in the Satellite web UI, navigate to **Monitor** > **Satellite Tasks** > **Tasks**.

    In the Task window, you can search for specific tasks, view their status, details, and elapsed time since they started. You can also cancel and resume one or more tasks.

The tasks are managed using the Dynflow engine. Remote tasks have a timeout which can be adjusted as needed.

Adjusting timeout settings
:   1. In the Satellite web UI, navigate to **Administer** > **Settings**.
    2. Enter *%_timeout* in the search box and click **Search**. The search should return four settings, including a description.
    3. In the **Value** column, click the icon next to a number to edit it.
    4. Enter the desired value in seconds, and click **Save**.

       > **Note**
       >
       > Adjusting the *%_finish_timeout* values might help in case of low bandwidth. Adjusting the *%_accept_timeout* values might help in case of high latency.

When a task is initialized, any back-end service that will be used in the task, such as Candlepin or Pulp, will be checked for correct functioning. If the check fails, you will receive an error similar to the following one:

```
There was an issue with the backend service candlepin: Connection refused – connect(2).
```

If the back-end service checking feature turns out to be causing any trouble, it can be disabled as follows.

Disabling checking for services
:   1. In the Satellite web UI, navigate to **Administer** > **Settings**.
    2. Enter *check_services_before_actions* in the search box and click **Search**.
    3. In the **Value** column, click the icon to edit the value.
    4. From the drop-down menu, select **false**.
    5. Click **Save**.

## 18.3. Configuring RSS notifications

You can configure custom RSS feed notifications to receive event alerts from your preferred sources, such as project blogs or internal news feeds, instead of the default notification sources.

To view Satellite event notification alerts, click the **Notifications** icon in the upper right of the screen.

By default, the Notifications area displays RSS feed events published in the [Red Hat Satellite Blog](https://access.redhat.com/blogs/1169563).

The feed is refreshed every 12 hours and the Notifications area is updated whenever new events become available.

You can configure the RSS feed notifications by changing the URL feed. The supported feed format is RSS 2.0 and Atom. For an example of the RSS 2.0 feed structure, see the [Red Hat Satellite Blog feed](https://access.redhat.com/blogs/1169563/feed). For an example of the Atom feed structure, see the [Foreman blog feed](https://theforeman.org/feed.xml).

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings** and select the **Notifications** tab.
2. In the RSS URL row, click the edit icon in the **Value** column and type the required URL.
3. In the RSS enable row, click the edit icon in the **Value** column to enable or disable this feature.

## 18.4. Monitoring Satellite Server

Audit records list the changes made by all users on Satellite. You can use this information for maintenance and troubleshooting.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Audits** to view the audit records.
2. Obtain a list of all audit attributes:

   ```
   # foreman-rake audits:list_attributes
   ```

## 18.5. Monitoring Capsule Server

In the Satellite web UI, you can find various information about Capsule Server and its services. This information is useful to maintain Capsule Server and troubleshoot any issues.

### 18.5.1. Viewing general Capsule information

You can view general information about your Capsules in the Satellite web UI, such as their status, enabled features, and managed hosts, to verify configuration or troubleshoot connectivity issues.

In the Satellite web UI, navigate to **Infrastructure** > **Capsules** to view a table of Capsule Servers registered to Satellite Server. The information contained in the table answers the following questions:

**Is Capsule Server running?**
:   This is indicated by a green icon in the **Status** column. A red icon indicates an inactive Capsule, use the `service foreman-proxy restart` command on Capsule Server to activate it.

**What services are enabled on Capsule Server?**
:   In the **Features** column, you can verify if, for example, your Capsule provides a DHCP service or acts as a Pulp mirror. Capsule features can be enabled during installation or configured in addition. For more information, see [Installing Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#).

**What organizations and locations is Capsule Server assigned to?**
:   A Capsule Server can be assigned to multiple organizations and locations, but only Capsules belonging to the currently selected organization are displayed. To list all Capsules, select **Any Organization** from the context menu in the top left corner.

    After changing the Capsule configuration, select **Refresh** from the drop-down menu in the **Actions** column to ensure the Capsule table is up to date.

    Click the Capsule name to view further details. At the **Overview** tab, you can find the same information as in the Capsule table. In addition, you can answer to the following questions:

**Which hosts are managed by Capsule Server?**
:   The number of associated hosts is displayed next to the **Hosts managed** label. Click the number to view the details of associated hosts.

**How much storage space is available on Capsule Server?**
:   The amount of storage space occupied by the Pulp content in `/var/lib/pulp` is displayed. Also the remaining storage space available on the Capsule can be ascertained.

### 18.5.2. Monitoring Capsule services

You can view the status and configuration details of Capsule services in Satellite web UI. This helps you verify that your Capsule services are running correctly and troubleshoot any issues.

**Procedure**

- In the Satellite web UI, navigate to **Infrastructure** > **Capsules** and click the name of the selected Capsule.

  - At the **Services** tab, you can find basic information on Capsule services, such as the list of DNS domains, or the number of Pulp workers.

    The appearance of the page depends on what services are enabled on Capsule Server. Services providing more detailed status information can have dedicated tabs at the Capsule page. For more information, see [Section 18.5.3, “Monitoring Puppet on Capsule”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#monitoring-puppet-on-capsule "18.5.3. Monitoring Puppet on Capsule").

### 18.5.3. Monitoring Puppet on Capsule

You can monitor Puppet activity and certificate management for each Capsule.

> **Note**
>
> The **Puppet** and **Puppet CA** tabs are available only if you have Puppet enabled in your Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
2. Click the name of your Capsule.

   - At the **Puppet** tab you can find the following:

     - A summary of Puppet events, an overview of latest Puppet runs, and the synchronization status of associated hosts at the **General** sub-tab.
     - A list of Puppet environments at the **Environments** sub-tab.
   - At the **Puppet CA** tab you can find the following:

     - A certificate status overview and the number of autosign entries at the **General** sub-tab.
     - A table of CA certificates associated with the Capsule at the **Certificates** sub-tab. Here you can inspect the certificate expiry data, or cancel the certificate by clicking **Revoke**.
     - A list of autosign entries at the **Autosign entries** sub-tab. Here you can create an entry by clicking **New** or delete one by clicking **Delete**.

**Additional resources**

- [Enabling Puppet integration with Satellite in *Managing configurations by using Puppet integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#enabling-puppet-integration-with-satellite)
