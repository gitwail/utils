---
title: "Managing compliance policies"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_security_compliance"
guide_title: "Managing security compliance"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Managing_Compliance_Policies_security-compliance"
---
# Chapter 4. Managing compliance policies

A compliance policy is a scheduled audit that checks the specified hosts for compliance against a specific XCCDF profile from a SCAP content. Before you can deploy compliance policies to scan your hosts, you must define these policies on Satellite.

## 4.1. Configuring compliance policy deployment methods

Before you can start creating compliance policies, choose your preferred method of deploying compliance policies. Some of these methods require you to configure your Satellite Server to enable them.

### 4.1.1. Deployment options for compliance policies

With Satellite, multiple methods are available for compliance policy deployment.

You can use one of the following methods to deploy compliance policies:

Ansible deployment
:   You use an Ansible role to configure hosts for compliance scans.

Puppet deployment
:   You use a Puppet class and the OpenVox agent to configure hosts for compliance scans.

Manual deployment
:   You manually configure hosts for compliance scans.

    For the manual deployment method, no additional Satellite configuration is required.

**Additional resources**

- [How to set up OpenSCAP Policies using Manual Deployment option in the *Red Hat Knowledgebase*](https://access.redhat.com/solutions/6389101)

### 4.1.2. Configuring Satellite for Ansible compliance policy deployment

If you want to use Ansible to deploy compliance policies, configure Satellite for Ansible compliance policy deployment.

**Procedure**

1. Import the `theforeman.foreman_scap_client` Ansible role.

   For more information, see [*Managing configurations by using Ansible integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#).
2. Assign the created policy and the `theforeman.foreman_scap_client` Ansible role to a host or host group.
3. To trigger the deployment, run the Ansible role on the host or host group either manually, or set up a recurring job by using remote execution for regular policy updates.

   For more information, see [Configuring and setting up remote jobs](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs) in *Managing hosts*.

### 4.1.3. Configuring Satellite for Puppet compliance policy deployment

If you want to use Puppet to deploy compliance policies, configure Satellite for Puppet compliance policy deployment.

**Procedure**

1. Ensure Puppet is enabled.
2. Ensure the OpenVox agent is installed on hosts.
3. Import the Puppet environment that contains the `foreman_scap_client` Puppet module.

   For more information, see [*Managing configurations by using Puppet integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#).
4. Assign the created policy and the `foreman_scap_client` Puppet class to a host or host group.

   Puppet triggers the deployment on the next regular run or you can run Puppet manually. Puppet runs every 30 minutes by default.

## 4.2. Creating a compliance policy

By creating a compliance policy, you can define and plan your security compliance requirements, and ensure that your hosts remain compliant to your security policies.

**Prerequisites**

- You have configured Satellite for your selected [compliance policy deployment method](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#deployment-options-for-compliance-policies_security-compliance "4.1.1. Deployment options for compliance policies").
- You have available SCAP contents, and eventually tailoring files, in Satellite.

  - To verify what SCAP contents are available by using Satellite web UI, see [Section 3.1, “Listing available SCAP contents using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#listing-available-scap-contents-using-web-ui "3.1. Listing available SCAP contents using Satellite web UI").
  - To verify what SCAP contents are available by using CLI, see [Section 3.2, “Listing available SCAP contents using CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#listing-available-scap-contents-using-cli "3.2. Listing available SCAP contents using CLI").
  - To upload SCAP contents and tailoring files, see [Chapter 3, *Configuring SCAP contents for compliance policies in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#configuring-scap-contents-for-compliance-policies-in-satellite "Chapter 3. Configuring SCAP contents for compliance policies in Satellite").
- Your user account has a role assigned that has the `view_policies` and `create_policies` permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Compliance** > **Policies**.
2. Click **New Policy** or **New Compliance Policy**.
3. Select the deployment method: **Ansible**, **Puppet**, or **Manual**. Then click **Next**.
4. Enter a name for this policy, a description (optional), then click **Next**.
5. Select the **SCAP Content** and **XCCDF Profile** to be applied, then click **Next**.

   Note that Satellite does not detect whether the selected XCCDF profile contains any rules. An empty XCCDF profile, such as the `Default XCCDF Profile`, will return empty reports.
6. Optional: To customize the XCCDF profile, select a **Tailoring File** and a **XCCDF Profile in Tailoring File**, then click **Next**.
7. Specify the scheduled time when the policy is to be applied. Select **Weekly**, **Monthly**, or **Custom** from the **Period** list. The **Custom** option allows for greater flexibility in the policy’s schedule.

   - If you select **Weekly**, also select the desired day of the week from the **Weekday** list.
   - If you select **Monthly**, also specify the desired day of the month in the **Day of month** field.
   - If you select **Custom**, enter a valid Cron expression in the **Cron line** field.
8. Select the locations to which to apply the policy, then click **Next**.
9. Select the organizations to which to apply the policy, then click **Next**.
10. Optional: Select the host groups to which to assign the policy.
11. Click **Submit**.

## 4.3. Viewing a compliance policy

You can preview the rules which will be applied by specific OpenSCAP content and profile combination. This is useful when you plan policies.

**Prerequisites**

- Your user account has a role assigned that has the `view_policies` permission.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Compliance** > **Policies**.
2. In the **Actions** column of the required policy, click **Show Guide** or select it from the list.

## 4.4. Editing a compliance policy

You can change the attributes of a compliance policy by editing it in the Satellite web UI.

OpenVox agent applies an edited policy to the host on the next run. By default, this occurs every 30 minutes. If you use Ansible, you must run the Ansible role manually again or have configured a recurring remote execution job that runs the Ansible role on hosts.

**Prerequisites**

- Your user account has a role assigned that has the `view_policies` and `edit_policies` permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Compliance** > **Policies**.
2. Click the name of the required policy.
3. Edit the necessary attributes.
4. Click **Submit**.

## 4.5. Deleting a compliance policy

In the Satellite web UI, you can delete existing compliance policies. Deleting a compliance policy removes it from your Satellite Server.

**Prerequisites**

- Your user account has a role assigned that has the `view_policies` and `destroy_policies` permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Compliance** > **Policies**.
2. In the **Actions** column of the required policy, select **Delete** from the list.
3. Click **OK** in the confirmation message.
