---
title: "Monitoring hosts by using Red Hat Lightspeed in Red Hat Hybrid Cloud Console"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "14"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#monitoring-hosts-by-using-red-hat-lightspeed-in-cloud"
---
# Chapter 14. Monitoring hosts by using Red Hat Lightspeed in Red Hat Hybrid Cloud Console

You can use the Red Hat Lightspeed advisor service in the Red Hat Hybrid Cloud Console to assess system health on hosts running Red Hat Enterprise Linux. You can use the Red Hat Lightspeed dashboard in the Red Hat Hybrid Cloud Console to quickly analyze recommendations for remediation, vulnerabilities, and more.

## 14.1. Prerequisites for using Red Hat Lightspeed in Red Hat Hybrid Cloud Console

Your environment must meet certain requirements before you can use Red Hat Lightspeed in the Red Hat Hybrid Cloud Console.

- You have configured hosted Red Hat Lightspeed on your Satellite Server, including data control settings.
- Install and configure the Insights client on hosts during host registration or provisioning.
- For hosts already registered to Satellite, install and configure the Insights client on your hosts by using an Ansible role.
- If you register your host to a new Satellite Server, reregister the host to Red Hat Lightspeed to avoid creating duplicate entries.
- You can change the schedule for running the Insights client by configuring `insights-client.timer` on a host.

**Additional resources**

- [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration")
- [Section 14.2, “Deploying Insights client on registered hosts”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#deploying-insights-client-on-registered-hosts_insights-in-cloud "14.2. Deploying Insights client on registered hosts")
- [Configuring Satellite for Red Hat Lightspeed analytics in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#configuring-satellite-for-red-hat-lightspeed-analytics)
- [Re-registering your system with Red Hat Lightspeed](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/client_configuration_guide_for_red_hat_lightspeed/assembly-client-configuring-insights-client#proc-reregistering-system-insights_insights-cg-configuring-client)
- [Changing the insights-client schedule in the *Client Configuration Guide for Red Hat Lightspeed*](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/client_configuration_guide_for_red_hat_lightspeed/assembly-client-changing-schedule)

## 14.2. Deploying Insights client on registered hosts

You can use the **RedHatInsights.insights-client** Ansible role to automate the installation of the Insights client on hosts and initiate the host data upload.

**Prerequisites**

- Remote execution with the Ansible provider is available.
- Ensure that the following repositories are enabled on your host:

  - On Red Hat Enterprise Linux 10: `rhel-10-for-x86_64-baseos-rpms` and `rhel-10-for-x86_64-appstream-rpms`
  - On Red Hat Enterprise Linux 9: `rhel-9-for-x86_64-baseos-rpms` and `rhel-9-for-x86_64-appstream-rpms`
  - On Red Hat Enterprise Linux 8: `rhel-8-for-x86_64-baseos-rpms` and `rhel-8-for-x86_64-appstream-rpms`
  - On Red Hat Enterprise Linux 7: `rhel-7-server-rpms`

**Procedure**

1. Add the **RedHatInsights.insights-client** role to the hosts.
2. To run the **RedHatInsights.insights-client** role on your host, navigate to **Hosts** > **All Hosts** and click the name of the host that you want to use.
3. On the host details page, expand the **Schedule a job** dropdown menu.
4. Click **Run Ansible roles**.

**Additional resources**

- [Running Ansible roles on a host in *Managing configurations by using Ansible integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#running-ansible-roles-on-a-host)

## 14.3. Synchronizing Red Hat Lightspeed recommendations for hosts

You can enable automatic synchronization of the recommendations from Red Hat Hybrid Cloud Console that occurs daily by default. If you leave the setting disabled, you can synchronize the recommendations manually.

**Procedure**

- To get the recommendations automatically:

  1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Recommendations**.
  2. Enable **Sync Automatically**.
- To get the recommendations manually:

  1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Recommendations**.
  2. From the options menu, select **Sync Recommendations**.

## 14.4. Examining recommendations for hosts

You can view Red Hat Lightspeed recommendations for Red Hat Enterprise Linux hosts in the Satellite web UI. Use the list to identify configuration issues and prioritize which issues to remediate.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Recommendations**.
2. From the menu next to the **Remediate** button, select **View in Red Hat Lightspeed** to navigate to the recommendations page in the Red Hat Hybrid Cloud Console.

**Additional resources**

- [Assessing RHEL configuration issues by using the Red Hat Lightspeed advisor service](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/assessing_rhel_configuration_issues_by_using_the_red_hat_lightspeed_advisor_service/index)

## 14.5. Remediating issues based on Red Hat Lightspeed recommendations

You can remediate issues on RHEL hosts based on Red Hat Lightspeed recommendations. You can only remediate recommendations that have an associated playbook.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Recommendations**.
2. Select the recommendations that you want to remediate.
3. Click **Remediate**.
4. In the **Remediation summary** window, you can select the **Resolutions** to apply if there are multiple options. Use the **Filter** field to search for specific keywords.
5. Click **Remediate**.

**Verification**

1. On the **Jobs** page, you can view the progress of your remediation.
2. Verify that the remediation job completed successfully.

## 14.6. Exclusion of hosts from Red Hat Lightspeed analytics

You can exclude hosts from Red Hat Lightspeed analytics by using host parameters.

`host_registration_insights`
:   Setting this parameter to `false` will prevent Satellite Server from forwarding data from the Insights client on hosts to Red Hat Lightspeed services. The Insights client will not be installed on newly registered hosts.

`host_registration_insights_inventory`
:   Setting this parameter to `false` will exclude the host from the Satellite host inventory that is uploaded to the Red Hat Hybrid Cloud Console.

    If you exclude a host that is already reported on the [Red Hat Hybrid Cloud Console](https://console.redhat.com/), it will be still removed automatically from the inventory. However, this process can take some time to complete.

You can set these parameters at any level. For more information, see [Appendix D, *Host parameter hierarchy*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#host-parameter-hierarchy "Appendix D. Host parameter hierarchy").

## 14.7. Troubleshooting Red Hat Lightspeed in Red Hat Hybrid Cloud Console

You can troubleshoot issues with Red Hat Lightspeed in the Red Hat Hybrid Cloud Console by checking logs and certificates.

To troubleshoot hosts monitoring, you can try the following approaches:

- You can find the logs in the `/var/log/foreman/production.log` file.
- If you have problems connecting to Red Hat Lightspeed, ensure that your certificates are up-to-date. Refresh your subscription manifest to update your certificates.
