---
title: "Applying Ansible definitions to hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_ansible_integration"
guide_title: "Managing configurations by using Ansible integration"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#applying-ansible-definitions-to-hosts"
---
# Chapter 4. Applying Ansible definitions to hosts

When a host has one or more Ansible roles assigned to it, Satellite can run the roles on the host to apply and enforce the configuration state that the roles define.

## 4.1. Running Ansible roles on a host

Run Ansible roles on a host through the Satellite web UI to apply the assigned configuration immediately. This helps you verify and enforce the intended state of the host.

**Prerequisites**

- The public SSH key from Capsule is available on the host. For more information, see [Distributing SSH keys for remote execution](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Distributing_SSH_Keys_for_Remote_Execution_managing-hosts) in *Managing hosts*.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the host on which you want to run the assigned Ansible roles.
3. From the **Schedule a job** menu, select **Run Ansible roles**.

**Verification**

- You can view the status of your Ansible job by navigating to **Monitor** > **Jobs**.

## 4.2. Running Ansible roles on a host group

When a host group has one or more Ansible roles assigned to it, Satellite can run the roles on all hosts in the host group at once to apply and enforce the configuration state that the roles define.

**Prerequisites**

- The public SSH key from Capsule is available on the hosts in the host group. For more information, see [Distributing SSH keys for remote execution](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Distributing_SSH_Keys_for_Remote_Execution_managing-hosts) in *Managing hosts*.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. From the list in the **Actions** column for the host group, select **Run all Ansible roles**.
3. You can view the status of your Ansible job on the **Run Ansible roles** page. Click **Rerun** to rerun a job.

## 4.3. Configuring a host to run Ansible roles in check mode

Run Ansible roles in check mode through the Satellite web UI to preview changes before applying them. This helps you reduce risk when validating role behavior on a host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click **Edit** for the host you want to enable check mode for.
3. In the **Parameters** tab, ensure that the host has a parameter named `ansible_roles_check_mode` with type `boolean` set to `true`.
4. Click **Submit**.
