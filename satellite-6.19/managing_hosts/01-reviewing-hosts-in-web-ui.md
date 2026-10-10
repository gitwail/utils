---
title: "Reviewing hosts in Satellite web UI"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#reviewing-hosts-in-web-ui"
---
# Chapter 1. Reviewing hosts in Satellite web UI

You can review hosts in the Satellite web UI to see them in one place and select the columns you need for daily work. When Red Hat Enterprise Linux lifecycle data is available, check it in the same views to plan patches and track compliance.

## 1.1. Browsing hosts in Satellite web UI

In the Satellite web UI, you can browse all hosts recognized by Satellite, grouped by type.

The following host types are available when browsing hosts in the Satellite web UI:

- **All Hosts** – a list of all hosts recognized by Satellite.
- **Discovered Hosts** – a list of bare-metal hosts detected on the provisioning network by the Discovery plugin.
- **Host Collections** – a list of user-defined collections of hosts used for bulk actions such as errata installation.

**Procedure**

1. Search for a host: Type in the **Search** field, and use an asterisk (*) to perform a partial string search. For example, if searching for a host named `server.example.com`, click the **All Hosts** page and type `server*` in the **Search** field. Alternatively, `*ver*` will also find the host `server.example.com`.

   > **Warning**
   >
   > Satellite Server is listed as a host itself even if it is not self-registered. Do not delete Satellite Server from the list of hosts.
2. Navigate between hosts: Click **⇄** next to the hostname. This displays a list of hosts in alphabetical order with a pagination arrow and a search bar to find the host you are looking for.

## 1.2. Selecting host columns

You can select what columns you want to see in the host table on the **Hosts** > **All Hosts** page.

> **Note**
>
> It is not possible to deselect the **Name** column. The **Name** column serves as a primary identification method of the host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click **Manage columns**.
3. Select columns that you want to display. You can select individual columns or column categories. Selecting or deselecting a category selects or deselects all columns in that category.

   > **Note**
   >
   > Some columns are included in more than one category, but you can display a column of a specific type only once. By selecting or deselecting a specific column, you select or deselect all instances of that column.

**Verification**

- You can now see the selected columns in the host table.

## 1.3. Lifecycle status of RHEL hosts

With Satellite, you can monitor the lifecycle status of your hosts by displaying upcoming End of Support (EOS) events. This is useful so that you can quickly identify which hosts require an update or action to maintain support.

Satellite provides multiple mechanisms to display information about upcoming EOS events for your Red Hat Enterprise Linux hosts:

- Notification banner
- A column on the Hosts index page
- Alert on the Hosts index page for each host that runs Red Hat Enterprise Linux with an upcoming EOS event in a year as well as when support has ended
- Ability to **Search** for hosts by EOS on the Hosts index page
- **Host status** card on the host details page

For any hosts that are not running Red Hat Enterprise Linux, Satellite displays **Unknown** in the **RHEL Lifecycle status** and **Last report** columns.

When either the end of maintenance support or the end of extended lifecycle support approaches in a year, you will see a notification banner in the Satellite web UI if you have hosts with that Red Hat Enterprise Linux version. The notification provides information about the Red Hat Enterprise Linux version, the number of hosts running that version in your environment, the lifecycle support, and the expiration date. Along with other information, the Red Hat Enterprise Linux lifecycle column is visible in the notification.

## 1.4. Displaying RHEL lifecycle status

You can display the status of the end of support (EOS) for your Red Hat Enterprise Linux hosts in the table on the Hosts index page.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click **Manage columns**.
3. Select the **Content** column to expand it.
4. Select **RHEL Lifecycle status**.
5. Click **Save** to generate a new column that displays the Red Hat Enterprise Linux lifecycle status.
6. Optional: You can use the **Search** field to search hosts by `rhel_lifecycle_status`. It can have one of the following values:

   - `full_support`
   - `maintenance_support`
   - `approaching_end_of_maintenance`
   - `extended_support`
   - `approaching_end_of_support`
   - `support_ended`

## 1.5. Host global status overview

You can use the host global status in Satellite to see at a glance whether a host is OK, needs attention (Warning), or has errors. The status appears on the Hosts Overview page and helps you prioritize which hosts to investigate.

The host global status can have one of three possible values: **OK**, **Warning**, or **Error**. You can find global status on the Hosts Overview page. The status displays a small icon next to the host name and has a color that corresponds with the status. Hovering over the icon renders a tooltip with sub-status information to quickly find out more details. To view the global status for a host, in the Satellite web UI, navigate to **Hosts** > **All Hosts**.

OK
:   No errors were reported by any sub-status. This status is highlighted with the color green.

Warning
:   While no error was detected, some sub-status raised a warning. For example, there are no configuration management reports for the host even though the host is configured to send reports. It is a good practice to investigate any warnings to ensure that your deployment remains healthy. This status is highlighted with the color yellow.

Error
:   Some sub-status reports a failure. For example, a run contains some failed resources. This status is highlighted with the color red.

**Additional resources**

- [Working efficiently with Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui)

## 1.6. Host sub-status overview

You can use host sub-statuses in Satellite to see the status of specific areas of a host, such as configuration, build, or content. Sub-statuses feed into the global host status and help you pinpoint what needs attention.

To view the sub-statuses of a host, in the Satellite web UI, navigate to **Hosts** > **All Hosts** and click on the host whose full status you want to inspect. You can view the global host status next to the name of the host and the host sub-statuses on the **Host status** card.

Each sub-status has its own set of possible values that are mapped to the three global status values. With any change of a sub-status, the global status is recalculated and the result is determined by the statuses of all sub-statuses.

The following sub-statuses are available in Satellite:

Configuration
:   This sub-status is only relevant if Satellite uses a configuration management system like Ansible, Puppet, or Salt.

    Possible values:

    | Label | Global host status |
    | --- | --- |
    | Alerts disabled | OK |
    | Active | OK |
    | Pending | OK |
    | No changes | OK |
    | No reports | OK / Warning |
    | Out of sync | Warning |
    | Error | Error |

    Additional information about the values of this sub-status:

    - **Active**: During the last configuration, some resources were applied.
    - **Pending**: During the last configuration, some resources would be applied but your configuration management integration was configured to run in `noop` mode.
    - **No changes**: During the last configuration, nothing changed.
    - **No reports**: This can be both a **Warning** or **OK** status. When there are no reports but the host uses an associated Capsule for configuration management or the `always_show_configuration_status` setting is set to `true`, it maps to **Warning**. Otherwise it maps to **OK**.
    - **Error**: This indicates an error during configuration. For example, a configuration run failed to install a package.
    - **Out of sync**: A configuration report was not received within the expected interval, based on the `outofsync_interval` setting. Reports are identified by an origin and can have different intervals based upon it.

Build
:   This sub-status is only relevant for hosts provisioned from Satellite or hosts registered through global registration.

    Possible values:

    | Label | Global host status | Number value |
    | --- | --- | --- |
    | Installed | OK | 0 |
    | Pending installation | OK | 1 |
    | Token expired | Error | 2 |
    | Installation error | Error | 3 |

Compliance
:   Indicates if the host is compliant with OpenSCAP policies.

    Possible values:

    | Label | Global host status | Number value |
    | --- | --- | --- |
    | Compliant | OK | 0 |
    | Inconclusive | Warning | 1 |
    | At least one incompliant | Error | 2 |

Execution
:   Status of the last completed remote execution job.

    Possible values:

    | Label | Global host status | Number value |
    | --- | --- | --- |
    | Last execution succeeded / No execution finished yet | OK | 0 |
    | Last execution failed | Error | 1 |
    | Unknown execution status | OK | 2 or 3 |
    | Last execution cancelled | OK | 4 |

Inventory
:   Indicates if the host is synchronized to Red Hat Hybrid Cloud Console. Satellite Server performs the synchronization itself but only uploads basic information to Red Hat Hybrid Cloud Console.

    Possible values:

    | Label | Global host status | Number value |
    | --- | --- | --- |
    | Host was not uploaded to your RH cloud inventory | Warning | 0 |
    | Successfully uploaded to your RH cloud inventory | OK | 1 |

Insights
:   Indicates if the host is synchronized to Red Hat Hybrid Cloud Console. This synchronization is performed by the host. The host uploads more information than the Satellite Server.

    Possible values:

    | Label | Global host status | Number value |
    | --- | --- | --- |
    | Reporting | OK | 0 |
    | Not reporting | Error | 1 |

Errata
:   Indicates if Errata is available on the host.

    Possible values:

    | Label | Global host status | Number value |
    | --- | --- | --- |
    | Up to date | OK | 0 |
    | Unknown | Warning | 1 |
    | Needed errata | Error | 2 |
    | Needed security errata | Error | 3 |

RHEL Lifecycle
:   Indicates the current state of the Red Hat Enterprise Linux operating system installed on the host.

    Possible values:

    | Label | Global host status | Number value |
    | --- | --- | --- |
    | Unknown | OK | 0 |
    | Full support | OK | 1 |
    | Maintenance support | OK | 2 |
    | Approaching end of maintenance support | Warning | 3 |
    | Extended support | OK | 4 |
    | Approaching end of support | Warning | 5 |
    | Support ended | Error | 6 |

Traces
:   Indicates if the host needs a reboot or a process restart.

    Possible values:

    | Label | Global host status | Number value |
    | --- | --- | --- |
    | Unknown | Warning | -1 |
    | Up to date | OK | 0 |
    | Required process restart | Error | 1 |
    | Required reboot | Error | 2 |

**Additional resources**

- [Working efficiently with Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui)
