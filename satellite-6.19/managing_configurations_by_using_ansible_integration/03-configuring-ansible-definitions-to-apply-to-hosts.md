---
title: "Configuring Ansible definitions to apply to hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_ansible_integration"
guide_title: "Managing configurations by using Ansible integration"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#configuring-ansible-definitions-to-apply-to-hosts"
---
# Chapter 3. Configuring Ansible definitions to apply to hosts

Configure and organize Ansible definitions in Satellite to control which configurations are available for your hosts. Keeping definitions organized helps you apply consistent changes across your hosts.

## 3.1. Adding Red Hat Enterprise Linux System Roles

Red Hat Enterprise Linux System Roles is a configuration interface to remotely manage Red Hat Enterprise Linux servers. You can use Red Hat Enterprise Linux System Roles to add Ansible roles in Satellite.

Support levels for some of the Red Hat Enterprise Linux System Roles might be in Technology Preview. For up-to-date information about support levels and general information about Red Hat Enterprise Linux System Roles, see [Red Hat Enterprise Linux System Roles](https://access.redhat.com/articles/3050101).

Before subscribing to the Extras or AppStream channels, see [Red Hat Enterprise Linux Extras Product Lifecycle](https://access.redhat.com/support/policy/updates/extras) or [Red Hat Enterprise Linux Application Streams Life Cycle](https://access.redhat.com/support/policy/updates/rhel-app-streams-life-cycle).

**Procedure**

1. Ensure that the following repository is enabled:

   - On Red Hat Enterprise Linux 10, 9, or 8, ensure that the **AppStream** repository is enabled:

     ```
     # subscription-manager repos --enable=rhel-10-for-x86_64-appstream-rpms
     # subscription-manager repos --enable=rhel-9-for-x86_64-appstream-rpms
     # subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms
     ```

     You must enable an AppStream repository that is designated for your architecture. For more information, see [RHEL 8 repositories](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/upgrading_from_rhel_7_to_rhel_8/appendix_rhel-8-repositories_upgrading-from-rhel-7-to-rhel-8).
   - On Red Hat Enterprise Linux 7, ensure that the **Extras** repository is enabled:

     ```
     # subscription-manager repos --enable=rhel-7-server-extras-rpms
     ```
2. Install the `rhel-system-roles` package:

   ```
   # satellite-maintain packages install rhel-system-roles
   ```

   The `rhel-system-roles` package downloads to `/usr/share/ansible/roles/`. You can view and make any modifications that you want to the files before you import.
3. In the Satellite web UI, navigate to **Configure** > **Ansible** > **Roles**.
4. Click the Capsule that contains the roles that you want to import.
5. From the list of Ansible roles, select the checkbox of the roles you want to import, and then click **Update**.

   You can now assign Ansible roles to hosts or host groups. For more information, see [Section 3.5, “Assigning Ansible roles to an existing host”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#Assigning_Ansible_Roles_to_an_Existing_Host_ansible "3.5. Assigning Ansible roles to an existing host").

   You can also add the modules contained in these roles to your Ansible Playbooks by adding them to Ansible Job Templates. You must include the `hosts:all` line in the job template. For more information, see [Red Hat Enterprise Linux (RHEL) System Roles](https://access.redhat.com/articles/3050101).

## 3.2. Importing Ansible roles and variables

You can import Ansible roles and variables from the Ansible paths on Satellite Server or Capsule Servers that have Ansible enabled.

**Procedure**

1. Place the roles and variables in the appropriate Ansible paths on all Capsules from where you want to use the roles. For more information, see [Appendix A, *Ansible role and collection paths in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#ansible-role-and-collection-paths-in-satellite "Appendix A. Ansible role and collection paths in Satellite").

   If you want to use custom or third party Ansible roles, ensure to configure an external version control system to synchronize roles between Satellite Server and Capsule Servers.
2. In the Satellite web UI, navigate to **Configure** > **Ansible** > **Roles**.
3. Click **Import** to select the Capsule from which you want to import.
4. Select the roles that you want to import.
5. Click **Submit**.

**Additional resources**

- [Synchronizing Ansible Collections in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-ansible-collections)
- [Consuming content from an Ansible Collection repository in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#consuming-content-from-an-ansible-collection-repository)

## 3.3. Overriding Ansible variables in Satellite

You can use Satellite to override Ansible variables for roles imported into Satellite. This helps you customize the behavior of imported roles to fit your specific needs.

> **Note**
>
> If you use an Ansible role to run a task as a user that is not the `Effective User`, there is a strict order of precedence for overriding Ansible variables. To ensure the variable that you override follows the correct order of precedence, see [Variable precedence: Where should I put a variable?](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#ansible-variable-precedence).

**Prerequisites**

- Ansible variables are available in Satellite. For more information, see [Section 3.2, “Importing Ansible roles and variables”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#Importing_Ansible_Roles_and_Variables_ansible "3.2. Importing Ansible roles and variables")
- To use overridden Ansible variables, your user account has a role that allows viewing the attributes that are matched against hosts.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Ansible** > **Variables**.
2. Select the Ansible variable that you want to override and manage with Satellite.
3. In the **Default Behavior** area, select the **Override** checkbox.
4. In the **Parameter Type** field, select the value type for validation such as **string** or **boolean**. The types **array** and **hash** have further options for handling upon a variable match. For more information, see [the *Prioritize Attribute Order* area](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#prioritize-order) below.
5. In the **Default Value** field, enter the default value that you want to use if there is no match for the variable.
6. Optional: If you do not want to display the value of the variable as plain text in the Satellite web UI, select the **Hidden Value** checkbox to display the content of the variable as asterisks. This is useful for sensitive values such as passwords or secret tokens.
7. Optional: Expand the **Optional Input Validator** area and specify conditions that will be used to validate concrete values of the variable:

   - Select **Required** if you want to enforce users to fill in this variable.
   - In the **Validator Type** field, select how the value will be validated:

     - `list` – The value will be validated against an enumeration of allowed values.
     - `regex` – The value will be validated against a regular expression pattern.
8. Optional: In the **Prioritize Attribute Order** area, specify the order of priority to match an override with a host by host attributes. Order at the top takes higher precedence. The first match wins.

   You can combine multiple attributes into a single matcher key using a comma as the AND operation. For example, the matcher key of `hostgroup, environment` would expect matchers such as `hostgroup = "web servers"` AND `environment = production`.

   If you use the parameter type **array** or **hash**, you can further set:

   - **Merge Overrides** – Merges members of the arrays/hashes instead of replacing the whole array or hash. If the hashes contain the same key, the value is overwritten by the value of the host.
   - **Merge Default** – Adds the default value to the array or hash.
   - **Avoid Duplicates** – Ensures that the values in the array or hash are unique.
9. Optional: Expand the **Specify Matchers** area and specify criteria for selecting hosts on which the variable overrides.
10. To save the override settings, click **Submit**.
11. To use the Ansible variable, add the variable as a parameter to your host or host group, or add the variable as a global parameter:

    1. To add the variable to a host:

       1. In the Satellite web UI, navigate to **Hosts** > **All Hosts** and select the host that you want to use.
       2. Click the **Ansible** tab, and in the **Variables** area, click the pencil icon to edit the value of the variable.
       3. Click the tick icon to accept the value of the changed variable or the cross icon to cancel the change.
    2. To add the variable to a host group:

       1. In the Satellite web UI, navigate to **Configure** > **Host Groups**, and select the host group that you want to use.
       2. Click the **Parameters** tab, and in the **Host Group Parameters** area, click **Add Parameter**.
       3. In the **Name** field, add the Ansible variable name.
       4. From the **Type** list, select the type of the variable for validation.
       5. In the **Value** field, enter the value for the variable.
    3. To add the variable as a global parameter:

       1. In the Satellite web UI, navigate to **Configure** > **Global Parameters**, and click **Create Parameter**.
       2. In the **Name** field, add the Ansible variable name.
       3. From the **Type** list, select the type of the variable for validation.
       4. In the **Value** field, enter the value for the variable.
       5. Optional: If you do not want to display the Ansible variable in plain text, select the **Hidden Values** checkbox to display the content of the variable as asterisks in the Satellite web UI.

## 3.4. Assigning Ansible roles to a host group

You can assign a previously imported Ansible role to a host group. This enables Satellite to apply the configuration defined by the role when you provision a new host by using the host group.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. Click the host group name to which you want to assign an Ansible role.
3. On the **Ansible Roles** tab, select the role that you want to add from the **Available Ansible Roles** list.
4. Click the **+** icon to add the role to the host group. You can add more than one role.
5. Click **Submit**.

## 3.5. Assigning Ansible roles to an existing host

You can assign a previously imported Ansible role to an existing host. This enables Satellite to apply the configuration defined by the role when you run the Ansible roles on the host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the host and click **Edit**.
3. On the **Ansible Roles** tab, select the role that you want to add from the **Available Ansible Roles** list.
4. Click the **+** icon to add the role to the host. You can add more than one role.
5. Click **Submit**.
6. Optional: On the **Parameters** tab, click **Add Parameter** to add any parameter variables that you want to pass to job templates at run time. This includes all Ansible Playbook parameters and host parameters that you want to associate with the host. To use a parameter variable with an Ansible job template, you must add a **Host Parameter**.

## 3.6. Changing the order of Ansible roles

Change the order of Ansible roles on a host to control how role tasks are applied. This helps prevent dependency and precedence issues during configuration runs.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select a host.
3. Select the **Ansible Roles** tab.
4. In the **Assigned Ansible Roles** area, you can change the order of the roles by dragging and dropping the roles into the preferred position.
5. Click **Submit** to save the order of the Ansible roles.

## 3.7. Removing Ansible roles from a host

Remove Ansible roles from a host to stop applying configurations to the host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the host and click **Edit**.
3. Select the **Ansible Roles** tab.
4. In the **Assigned Ansible Roles** area, click the **-** icon to remove the role from the host. Repeat to remove more roles.
5. Click **Submit**.
