---
title: "Configuring Satellite for Red Hat Lightspeed analytics"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "14"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#configuring-satellite-for-red-hat-lightspeed-analytics"
---
# Chapter 14. Configuring Satellite for Red Hat Lightspeed analytics

You can configure Satellite to connect to Red Hat Lightspeed hosted in the Red Hat Hybrid Cloud Console or to local Red Hat Lightspeed in Satellite so your hosts receive suggestions for improvement.

## 14.1. Red Hat Lightspeed overview

Red Hat Lightspeed is a set of analytical services by Red Hat for hosts running Red Hat Enterprise Linux. Red Hat Lightspeed services analyze host data and provide suggestions for host improvements.

Red Hat Lightspeed services
:   Red Hat Lightspeed services include:

    - Advisor, which provides recommendations for host improvements.
    - Vulnerability, which provides reports on vulnerabilities found on your hosts.
    - Compliance, which provides reports on compliance with regulatory requirements.

    Red Hat Lightspeed services hosted in the Red Hat Hybrid Cloud Console are not limited to the listed services.

    Table 14.1. Availability of Red Hat Lightspeed services

    | Service | Hosted Red Hat Lightspeed | Red Hat Lightspeed in Satellite |
    | --- | --- | --- |
    | Advisor | Available | Available |
    | Vulnerability | Available | Available |
    | Compliance | Available | - |

Hosted Red Hat Lightspeed
:   When you use Red Hat Lightspeed hosted in the Red Hat Hybrid Cloud Console, the Insights client on your hosts collects data and Satellite forwards it to the hosted Red Hat Lightspeed services for analysis.

    If you use Red Hat Lightspeed in the Red Hat Hybrid Cloud Console:

    - You can use Red Hat Lightspeed services online in the Red Hat Hybrid Cloud Console.
    - The Insights client collects data of your hosts and Satellite forwards the data to the Red Hat Hybrid Cloud Console to calculate recommendations.
    - You can view and remediate those recommendations both in the Satellite web UI and in the Red Hat Hybrid Cloud Console.
    - Satellite uploads host inventory reports to the Red Hat Hybrid Cloud Console.
    - You have control over how much information is included in those reports.
    - You cannot use local Red Hat Lightspeed in Satellite.

Red Hat Lightspeed in Satellite
:   When you use Red Hat Lightspeed in Satellite, the Red Hat Lightspeed services run locally on your Satellite Server without connecting to the Red Hat Hybrid Cloud Console. The Insights client on your hosts collects data and Satellite forwards it to the local Red Hat Lightspeed services for analysis.

    If you use Red Hat Lightspeed in Satellite:

    - The Red Hat Lightspeed services run locally on your Satellite Server.
    - Satellite only communicates with the locally running services of Red Hat Lightspeed in Satellite.
    - Satellite does not send any reports to the Red Hat Hybrid Cloud Console.
    - Satellite does not forward any data through the Insights client to the Red Hat Hybrid Cloud Console.
    - You cannot use any of the hosted services on the Red Hat Hybrid Cloud Console.

**Additional resources**

- [Section 14.3, “Data control settings for hosted Red Hat Lightspeed”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#data-control-settings-for-hosted-red-hat-lightspeed "14.3. Data control settings for hosted Red Hat Lightspeed")
- [Red Hat Hybrid Cloud Console](https://console.redhat.com)
- [Red Hat Lightspeed dashboard](https://console.redhat.com/insights/dashboard)
- [Red Hat Lightspeed documentation](https://docs.redhat.com/en/documentation/red_hat_lightspeed/)

## 14.2. Enabling hosted Red Hat Lightspeed

Enable the integration between Satellite and hosted Red Hat Lightspeed in the Red Hat Hybrid Cloud Console to upload host inventory and receive cloud-based recommendations for your hosts.

### 14.2.1. Adding Satellite Server SSH key to authorized keys

To run remote execution jobs on Satellite Server itself, add the Satellite Server SSH key to authorized keys on your Satellite Server.

**Prerequisites**

- You can access your Satellite Server by using SSH as root.

**Procedure**

1. If the `~root/.ssh/authorized_keys` file does not exist, create it with restrictive ownership and permissions:

   1. If the `~root/.ssh` directory does not exist, create it:

      ```
      # mkdir ~root/.ssh
      ```
   2. Ensure that the directory is owned by the `root` user:

      ```
      # chown root:root ~root/.ssh
      ```
   3. Ensure that the directory is accessible only to the `root` user:

      ```
      # chmod 700 ~root/.ssh
      ```
   4. Create the `authorized_keys` file:

      ```
      # touch ~root/.ssh/authorized_keys
      ```
   5. Ensure that the `authorized_keys` file is owned by the `root` user:

      ```
      # chown root:root ~root/.ssh/authorized_keys
      ```
   6. Ensure that the `authorized_keys` file is accessible only to the `root` user:

      ```
      # chmod 600 ~root/.ssh/authorized_keys
      ```
2. Add the SSH key of the `foreman-proxy` user to the `authorized_keys` file:

   ```
   # cat ~foreman-proxy/.ssh/id_rsa_foreman_proxy.pub >>~root/.ssh/authorized_keys
   ```

### 14.2.2. Configuring Satellite Server for cloud connection

You can configure Satellite Server to connect to the Red Hat Hybrid Cloud Console by using remote execution. This enables inventory upload and cloud-based features such as Red Hat Lightspeed for your hosts.

**Prerequisites**

- Satellite Server must be registered with Red Hat Subscription Management. You can verify the status by running `subscription-manager status`.
- You have added the SSH key to authorized keys on your Satellite Server. For more information, see [Section 14.2.1, “Adding Satellite Server SSH key to authorized keys”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#adding-satellite-server-ssh-key-to-authorized-keys "14.2.1. Adding Satellite Server SSH key to authorized keys").
- Your Satellite account has a role that grants the `execute_jobs_on_infrastructure_hosts` permission.

  Note that this permission is not included in the default **Remote Execution User** role.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Inventory Upload**.
2. Click **Configure cloud connector**.
3. Click **Confirm**.

**Verification**

1. In the Satellite web UI, navigate to **Monitor** > **Satellite Tasks** > **Tasks**.
2. Find the job with the name `Remote action: Configure cloud connector`.
3. Verify that the job completed successfully.

**Next steps**

- Install the Insights client on hosts. For more information, see [Monitoring hosts by using Red Hat Lightspeed in Red Hat Hybrid Cloud Console in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#monitoring-hosts-by-using-red-hat-lightspeed-in-cloud).

## 14.3. Data control settings for hosted Red Hat Lightspeed

You can configure how Satellite handles the data collected from hosts before uploading it to the Red Hat Hybrid Cloud Console and how Satellite handles hosts in the Red Hat Hybrid Cloud Console that are no longer managed by Satellite.

### 14.3.1. Minimizing collected data

Use minimal data collection to limit host data sent to Red Hat while keeping the Subscriptions service active. Other Red Hat Lightspeed services are disabled because they require installed package data.

You can use minimal reporting to limit the amount of system data sent to the Subscriptions service, which remains active. Other Red Hat Lightspeed services are disabled because they require installed package data, which minimal reports do not include. Reports are still processed daily during the midnight synchronization cycle.

Minimal reports also exclude hostnames, IP addresses, and installed packages. Therefore, obfuscation and exclusion settings do not apply.

If you switch to **Analytics data collection**, Satellite enables the following settings by default:

- Obfuscate host names
- Obfuscate host ipv4 addresses
- Exclude installed packages

Review and adjust these settings to control what data Satellite shares.

**Example 14.1. Example of data collected in a minimal report**

```
{
  "report_slice_id": "de92044d-9d77-4895-83c4-a476f5020519",
  "hosts": [
    {
      "account": "123456789",
      "subscription_manager_id": "9fc621b9-08c3-4085-a749-bfed38c3052e",
      "insights_id": "9fc621b9-08c3-4085-a749-bfed38c3052e",
      "bios_uuid": "203F234F-58C7-4237-8DDF-A17A2838A66C",
      "bios_vendor": "SeaBIOS",
      "bios_version": "1.16.1-1.el9",
      "arch": "x86_64",
      "infrastructure_type": "virtual",
      "system_profile": {
        "installed_products": [
          {
            "name": "Red Hat Enterprise Linux for x86_64",
            "id": "479"
          }
        ],
        "cores_per_socket": 1,
        "system_memory_bytes": 3836579840,
        "number_of_cpus": 1,
        "number_of_sockets": 1
      },
      "cpu_socket(s)": "1"
    }
  ]
}
```

**Prerequisites**

- Your user account has a role that grants the `edit_settings` permission.
- Existing data in Red Hat Lightspeed Inventory has been deleted before switching to minimal reporting. To remove existing data of a system, navigate to **Inventory** > **Systems** in the Red Hat Hybrid Cloud Console, select the system, and click **Delete**.
- You have selected an organization and location.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Inventory Upload**.
2. Select the **Minimal data collection** setting from the dropdown menu under **Settings**.
3. When you select this option, Satellite also updates the corresponding setting on the **Red Hat Lightspeed** tab under **Administer** > **Settings**.
4. Click the **Generate and upload report** button to create a new inventory report and send it to the Red Hat Hybrid Cloud Console.

### 14.3.2. Obfuscating hostnames and IP addresses

You can configure Satellite to obfuscate hostnames and IP addresses when uploading host data to Red Hat Lightspeed. Obfuscation ensures that sensitive identifying information is not exposed.

When obfuscation settings are enabled, Satellite obfuscates hostnames and IP addresses. If obfuscation settings are enabled and the host has its own `insights-client` obfuscation settings, Satellite honors the host settings. If obfuscation settings are disabled, Satellite does not obfuscate hostnames or IP addresses unless the client has obfuscation enabled in `insights-client`.

By default, Satellite applies global obfuscation settings unless an `insights-client` on the host overrides the settings with its own configuration.

> **Note**
>
> Obfuscation only works when **Minimal data collection** is disabled. If **Minimal data collection** is enabled, hostnames and IP addresses are not included in reports, making obfuscation unnecessary and inactive.

**Prerequisites**

- Your hosts have `insights-client` installed and configured.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Inventory Upload**.
2. Enable the **Obfuscate host names** setting to obfuscate host names sent to the Red Hat Hybrid Cloud Console.
3. Enable the **Obfuscate host ipv4 addresses** setting to obfuscate IPv4 addresses sent to the Red Hat Hybrid Cloud Console.

**Verification**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Inventory Upload**.
2. In the **Organization** dropdown menu, select the organization that uploaded the host data.
3. Click **Generate report** to create a fresh report with obfuscated data.
4. Click **Download report** to download the host inventory report.
5. Verify that the hostname is `randomhostname.example.com` and the IP address is obfuscated.

**Next steps**

- Click **Generate and upload report** to create and upload a new report with obfuscated data to the Red Hat Hybrid Cloud Console.

### 14.3.3. Removing hosts from the Red Hat Lightspeed Inventory

When hosts are removed from Satellite, they can also be removed from the inventory of Red Hat Lightspeed, either automatically or manually. You can configure automatic removal of hosts from the Red Hat Lightspeed Inventory during Red Hat Hybrid Cloud Console synchronization with Satellite that occurs daily by default.

If you leave the setting disabled, you can still remove the bulk of hosts from the Inventory manually.

If **Automatic mismatch deletion** is enabled, Satellite removes any hosts from the Red Hat Hybrid Cloud Console that are not registered in Satellite. Enable this setting only when all hosts are registered through Satellite. If any hosts are registered through other Satellite instances or directly to the Red Hat Hybrid Cloud Console, Satellite deletes them.

> **Note**
>
> Automatic mismatch deletion runs once a day as a scheduled task. After removing hosts from Satellite, hosts are deleted from the Red Hat Hybrid Cloud Console inventory during the next scheduled sync. Clicking **Sync all inventory status** updates the status of hosts but does not trigger immediate deletion.

**Prerequisites**

- Your Satellite account has a role that grants the `view_foreman_rh_cloud` and `edit_settings` permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Inventory Upload**.
2. Enable the **Automatic mismatch deletion** setting.

## 14.4. Migrating from hosted to in-Satellite Red Hat Lightspeed

Migrate from hosted Red Hat Lightspeed to Red Hat Lightspeed in Satellite when you need local analysis on your Satellite Server without sending host data to the Red Hat Hybrid Cloud Console.

**Procedure**

1. Log in to the Red Hat container registry:

   ```
   # podman login --authfile /etc/foreman/registry-auth.json registry.redhat.io
   ```

   This command creates the `/etc/foreman/registry-auth.json` file.
2. On Satellite Server, enable Red Hat Lightspeed in Satellite:

   - If Red Hat Lightspeed in Satellite was previously enabled:

     ```
     # satellite-installer --iop-ensure present
     ```
   - If Red Hat Lightspeed in Satellite was not previously enabled:

     ```
     # satellite-installer --enable-iop
     ```
3. On your hosts, re-register the Insights client:

   ```
   # insights-client --register
   ```

   You can use remote execution to run this command on your hosts.

**Verification**

1. Verify that the **Red Hat Lightspeed** submenu in the Satellite web UI no longer shows the **Inventory Upload** menu item and shows the **Vulnerability** menu item.
2. Verify that the same recommendations appear for your hosts as before.

**Additional resources**

- [Configuring and setting up remote jobs in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs)

## 14.5. Migrating from in-Satellite to hosted Red Hat Lightspeed

Migrate from Red Hat Lightspeed in Satellite to hosted Red Hat Lightspeed when you want cloud-based analytics and access to the full set of Red Hat Lightspeed services on the Red Hat Hybrid Cloud Console.

**Prerequisites**

- Red Hat Lightspeed in Satellite is enabled on your Satellite Server.
- Your Satellite Server can access the [Red Hat Hybrid Cloud Console](https://console.redhat.com).

**Procedure**

1. On Satellite Server, disable Red Hat Lightspeed in Satellite:

   ```
   # satellite-installer --iop-ensure absent
   ```
2. Reconfigure the cloud connector on Satellite Server. For more information, see [Section 14.2.2, “Configuring Satellite Server for cloud connection”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#configuring-satellite-server-for-cloud-connection "14.2.2. Configuring Satellite Server for cloud connection").
3. On your hosts, re-register the Insights client:

   ```
   # insights-client --register
   ```

   You can use remote execution to run this command on your hosts.

**Verification**

1. Verify that the **Red Hat Lightspeed** submenu in the Satellite web UI no longer shows the **Vulnerability** menu item and shows the **Inventory Upload** menu item.
2. Verify that the same recommendations appear for your hosts as before.
3. Verify that, on the **Inventory Upload** page, the **Sync all inventory status** button is present.

**Additional resources**

- [Configuring and setting up remote jobs in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs)
