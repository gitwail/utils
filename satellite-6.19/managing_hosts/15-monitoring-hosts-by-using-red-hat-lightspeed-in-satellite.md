---
title: "Monitoring hosts by using Red Hat Lightspeed in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "15"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#monitoring-hosts-by-using-red-hat-lightspeed-in-satellite"
---
# Chapter 15. Monitoring hosts by using Red Hat Lightspeed in Satellite

You can use local services of Red Hat Lightspeed in Satellite to assess system health on hosts running Red Hat Enterprise Linux without connecting to the Red Hat Hybrid Cloud Console. Red Hat Lightspeed in Satellite provides advisor recommendations and vulnerability reports.

## 15.1. Prerequisites for using Red Hat Lightspeed in Satellite

Your environment must meet certain requirements before you can use Red Hat Lightspeed in Satellite.

- You have configured Red Hat Lightspeed in Satellite on your Satellite Server.
- Install and configure the Insights client on hosts during host registration or provisioning.
- For hosts already registered to Satellite, install and configure the Insights client on your hosts by using an Ansible role.

**Additional resources**

- [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration")
- [Section 15.2, “Deploying Insights client on registered hosts”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#deploying-insights-client-on-registered-hosts_insights-in-satellite "15.2. Deploying Insights client on registered hosts")
- [Configuring Satellite for Red Hat Lightspeed analytics in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#configuring-satellite-for-red-hat-lightspeed-analytics)
- [Changing the insights-client schedule in the *Client Configuration Guide for Red Hat Lightspeed*](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/client_configuration_guide_for_red_hat_lightspeed/assembly-client-changing-schedule)

## 15.2. Deploying Insights client on registered hosts

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

## 15.3. Examining recommendations for hosts

You can view Red Hat Lightspeed recommendations for Red Hat Enterprise Linux hosts in the Satellite web UI. Use the list to identify configuration issues and prioritize which issues to remediate.

**Prerequisites**

- Your Satellite account has a role that grants the `view_foreman_rh_cloud`, `view_insights_hits`, and `view_advisor` permissions. You can get these permissions with the `ForemanRhCloud Read Only` built-in role.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Recommendations**.

   By default, Satellite web UI only displays recommendations enabled for the organization. To view disabled recommendations, update the recommendation filter to include disabled recommendations.
2. Click the arrow next to the recommendation to expand it.
3. Click the name of the recommendation to view full details and affected hosts.

   If the recommendation is disabled for the organization, you might see the reason for disablement and the date thereof under the **Recommendation is disabled** section.

   If the recommendation is disabled for any hosts, you can inspect the reason for disablement and the date thereof under the **Recommendation is disabled for some systems** section, by clicking **View systems**.

## 15.4. Remediating issues based on Red Hat Lightspeed recommendations

You can remediate issues on RHEL hosts based on Red Hat Lightspeed recommendations. You can only remediate recommendations that have an associated playbook.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Recommendations**.
2. Click the name of the recommendation to view the recommendation details.
3. Select the affected hosts that you want to remediate.
4. Click **Remediate**.
5. In the **Remediation summary** window, you can select the **Resolutions** to apply if there are multiple options. Use the **Filter** field to search for specific keywords.
6. Click **Remediate**.

**Verification**

1. On the **Jobs** page, you can view the progress of your remediation.
2. Verify that the remediation job completed successfully.

## 15.5. Disabling recommendations in Satellite

You can disable recommendations per organization or per host. Satellite does not show disabled recommendations in dashboards or reports.

**Prerequisites**

- Your Satellite account has a role that grants the following permissions: `view_foreman_rh_cloud`, `view_insights_hits`, `view_advisor`, and `edit_advisor`. You can get these permissions with the `ForemanRhCloud` built-in role.
- An organization and location are selected in the top bar of the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Recommendations**.
2. Disable the recommendation:

   - To disable the recommendation for an organization:

     1. Click the recommendation menu icon next to the recommendation you want to disable.
     2. Select **Disable recommendation**.
     3. Optional: Enter a justification for disabling the recommendation.
     4. Click **Save**.
   - To disable the recommendation for a host:

     1. Click the name of the recommendation to view affected hosts.
     2. Click the host menu icon next to the host for which you want to disable the recommendation.
     3. Select **Disable recommendation for system**.
     4. Optional: Enter a justification for disabling the recommendation.
     5. Click **Save**.

## 15.6. Enabling recommendations in Satellite

If you have previously disabled recommendations, you can re-enable them per organization or per host.

**Prerequisites**

- Your Satellite account has a role that grants the following permissions: `view_foreman_rh_cloud`, `view_insights_hits`, `view_advisor`, and `edit_advisor`. You can get these permissions with the `ForemanRhCloud` built-in role.
- An organization and location are selected in the top bar of the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Recommendations**.
2. Enable the recommendation:

   - To enable the recommendation for an organization:

     1. Filter recommendations to include disabled recommendations.
     2. Click the recommendation menu icon next to the recommendation you want to re-enable.
     3. Select **Enable recommendation**.
   - To enable the recommendation for a host:

     1. Click the name of the recommendation to view recommendation details.
     2. Under the **Recommendation is disabled for some systems** section, click **View systems**.
     3. Click **Enable** in the row next to the host for which you want to re-enable the recommendation.

## 15.7. Examining vulnerability of hosts

You can view Common Vulnerabilities and Exposures (CVE) from Red Hat Lightspeed vulnerability service in Satellite. You can examine how the CVEs affect your hosts.

**Prerequisites**

- You have installed Red Hat Lightspeed in Satellite.
- Your Satellite account has a role that grants the `view_foreman_rh_cloud`, `view_insights_hits`, and `view_vulnerability` permissions. You can get these permissions with the `ForemanRhCloud Read Only` built-in role.

**Procedure**

1. In the Satellite web UI, navigate to **Red Hat Lightspeed** > **Vulnerability**.
2. In the **CVE ID** column, click the ID of the vulnerability to see details.

## 15.8. Disabling vulnerability analysis on hosts

If you do not require vulnerability analysis for some hosts, you can disable it on those hosts.

**Prerequisites**

- You are using Red Hat Lightspeed in Satellite.
- Your Satellite account has a role that grants the following permissions: `view_foreman_rh_cloud`, `view_vulnerability`, and `edit_vulnerability`. You can get these permissions with the `ForemanRhCloud` built-in role.
- Your Satellite account has a role that grants the `view_hosts` permission. You can get this permission with the `View hosts` built-in role.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Disable vulnerability analysis.

   - To disable vulnerability analysis on hosts in bulk:

     1. Select the hosts for which you want to disable vulnerability analysis.
     2. Click the host table menu icon.
     3. Select **Manage vulnerability analysis** > **Disable**.
   - To disable vulnerability analysis on a single host:

     1. Click the host menu icon in the row of the host for which you want to disable vulnerability analysis.
     2. Select **Disable vulnerability analysis**.

**Verification**

- The **Total CVEs** column shows **Analysis disabled** for hosts with vulnerability analysis disabled. This column is hidden by default. You can show it by clicking **Manage columns** and selecting **Total CVEs**.

## 15.9. Enabling vulnerability analysis on hosts

If you have previously disabled vulnerability analysis on some hosts, you can re-enable it.

**Prerequisites**

- You are using Red Hat Lightspeed in Satellite.
- Your Satellite account has a role that grants the following permissions: `view_foreman_rh_cloud`, `view_vulnerability`, and `edit_vulnerability`. You can get these permissions with the `ForemanRhCloud` built-in role.
- Your Satellite account has a role that grants the `view_hosts` permission. You can get this permission with the `View hosts` built-in role.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Enable vulnerability analysis.

   - To enable vulnerability analysis on hosts in bulk:

     1. Select the hosts for which you want to enable vulnerability analysis.
     2. Click the host table menu icon.
     3. Select **Manage vulnerability analysis** > **Enable**.
   - To enable vulnerability analysis on a single host:

     1. Click the host menu icon in the row of the host for which you want to enable vulnerability analysis.
     2. Select **Enable vulnerability analysis**.

**Verification**

- The **Total CVEs** column shows a count of CVEs for hosts with vulnerability analysis enabled. This column is hidden by default. You can show it by clicking **Manage columns** and selecting **Total CVEs**.

## 15.10. Exclusion of hosts from Red Hat Lightspeed analytics

You can exclude hosts from Red Hat Lightspeed analytics by using a host parameter.

`host_registration_insights`
:   Setting this parameter to `false` will prevent Satellite Server from forwarding data from the Insights client on hosts to Red Hat Lightspeed services. The Insights client will not be installed on newly registered hosts.

You can set this parameter at any level. For more information, see [Appendix D, *Host parameter hierarchy*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#host-parameter-hierarchy "Appendix D. Host parameter hierarchy").

## 15.11. Troubleshooting Red Hat Lightspeed in Satellite

You can check the logs to troubleshoot issues with Red Hat Lightspeed in Satellite.

To troubleshoot hosts monitoring, you can find the logs in the `/var/log/foreman/production.log` file.
