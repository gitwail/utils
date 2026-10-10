---
title: "Integrating Red Hat Satellite and Ansible Automation Platform"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_ansible_integration"
guide_title: "Managing configurations by using Ansible integration"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#Integrating_satellite_and_Ansible_Automation_Platform_ansible"
---
# Chapter 6. Integrating Red Hat Satellite and Ansible Automation Platform

You can integrate Red Hat Satellite and Ansible Automation Platform to use Satellite Server as a dynamic inventory source for Ansible Automation Platform. When provisioning new hosts from Satellite Server, you can use the provisioning callback function to trigger playbook runs from Ansible Automation Platform.

## 6.1. Adding Satellite Server to Ansible Automation Platform as a dynamic inventory item

To add Satellite Server to Ansible Automation Platform as a dynamic inventory item, you must create a credential for a Satellite Server user on Ansible Automation Platform, add an Ansible Automation Platform user to the credential, and then configure an inventory source.

**Prerequisites**

- If your Satellite deployment is large, for example, managing tens of thousands of hosts, using a non-admin user can negatively impact performance because of time penalties that accrue during authorization checks. For large deployments, consider using an admin user.
- For non-admin users, the `Ansible Tower Inventory Reader` role is assigned to your Satellite Server user. For more information about managing users, roles, and permission filters, see [Creating and managing roles](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#creating-and-managing-roles) in *Administering Red Hat Satellite*.
- Your Satellite Server and Ansible Automation Platform are hosted on the same network or subnet.

**Procedure**

1. In the Ansible Automation Platform web UI, create a credential for your Satellite. For more information about creating credentials, see [Creating new credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-create-credential) and [Red Hat Satellite 6 credential type](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#ref-controller-credential-satellite) in *Red Hat Ansible Automation Platform documentation*.

   Table 6.1. Satellite credentials

   | **Credential Type**: | **Red Hat Satellite 6** |
   | --- | --- |
   | **Satellite URL**: | https://*satellite.example.com* |
   | **Username**: | The username of the Satellite user with the integration role. |
   | **Password**: | The password of the Satellite user. |
2. Add an Ansible Automation Platform user to the new credential. For more information about adding a user to a credential, see [Adding new users and job templates to existing credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials#controller-credential-add-users-job-templates) in *Red Hat Ansible Automation Platform documentation*.
3. Add a new inventory. For more information, see [Add a new inventory](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-inventories#proc-controller-adding-new-inventory) in *Red Hat Ansible Automation Platform documentation*.

   In the new inventory, add Satellite Server as the inventory source, specifying the following inventory source options.

   Table 6.2. Inventory source options

   | **Source** | **Red Hat Satellite 6** |
   | --- | --- |
   | **Credential** | The credential you create for Satellite Server. |
   | **Overwrite** | Select |
   | **Overwrite Variables** | Select |
   | **Update on Launch** | Select |
   | **Cache Timeout** | *90* |
4. Ensure that you synchronize the source that you add.

## 6.2. Configuring provisioning callback for a host

When you create hosts in Satellite, you can use Ansible Automation Platform to run playbooks to configure your newly created hosts. This is called *provisioning callback* in Ansible Automation Platform.

The provisioning callback function triggers a playbook run from Ansible Automation Platform as part of the provisioning process. The playbook configures the host after the provisioning process.

In Satellite Server, the `Kickstart Default` and `Kickstart Default Finish` templates include three snippets:

1. `ansible_provisioning_callback`
2. `ansible_tower_callback_script`
3. `ansible_tower_callback_service`

You can add parameters to hosts or host groups to provide the credentials that these snippets can use to run Ansible Playbooks on your newly created hosts.

**Prerequisites**

- Satellite is added as a dynamic inventory in Ansible Automation Platform. For more information, see [Chapter 6, *Integrating Red Hat Satellite and Ansible Automation Platform*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#Integrating_satellite_and_Ansible_Automation_Platform_ansible "Chapter 6. Integrating Red Hat Satellite and Ansible Automation Platform").

**Procedure**

1. In the Ansible Automation Platform web UI, complete the following tasks:

   1. Create a machine credential for your new host. Ensure that you enter the same password in the credential that you plan to assign to the host that you create in Satellite. For more information, see [Managing user credentials](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-credentials) in *Red Hat Ansible Automation Platform documentation*.
   2. Create a project. For more information, see [Projects](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-projects) in *Red Hat Ansible Automation Platform documentation*.
   3. Add a job template to your project. In your job template, you must enable provisioning callbacks, generate the host configuration key, and note the *template_ID* of your job template. For more information, see [Job templates](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-job-templates) in *Red Hat Ansible Automation Platform documentation*.
2. In the Satellite web UI, navigate to **Configure** > **Host Group**.
3. Create a host group or edit an existing host group.
4. In the Host Group window, click the **Parameters** tab.
5. Click **Add Parameter**.
6. Enter the following information for each new parameter:

   Table 6.3. Host parameters

   | Name | Value | Description |
   | --- | --- | --- |
   | `ansible_tower_provisioning` | true | Enables Provisioning Callback. |
   | `ansible_tower_api_url` | *<https://aap.example.com/api/controller/v2>* | Defines the URL of your Ansible Automation Platform, including the required API path. For older versions of Ansible Automation Platform, use `/api/v2` instead of `/api/controller/v2`. If unsure, check the API endpoints of your instance to verify the correct path. |
   | `ansible_job_template_id` | *template_ID* | The ID of your provisioning template that you can find in the URL of the template: `/templates/job_template/5`. |
   | `ansible_host_config_key` | *config_KEY* | The host configuration key that your job template generates in Ansible Automation Platform. |
7. Click **Submit**.
8. Create a host using the host group.
9. On your new host, start the `ansible-callback` service:

   ```
   # systemctl start ansible-callback
   ```
10. On your new host, check the the status of the `ansible-callback` service:

    ```
    # systemctl status ansible-callback
    ```

    Provisioning callback is configured correctly if the command returns the following output:

    ```
    satellite.example.com systemd[1]: Started Provisioning callback to Ansible Automation Platform...
    ```

    > **Note**
    >
    > For manual provisioning callback, you can use the provisioning callback URL and the host configuration key from a host to call Ansible Automation Platform:
    >
    > ```
    > $ curl \
    > --data curl \
    > --data host_config_key=My_Host_Config_Key \
    > --show-error \
    > --silent \
    > https://aap.example.com/api/v2/job_templates/8/callback/
    > ```
    >
    > Ensure that you use `https` when you enter the provisioning callback URL.
    >
    > This triggers the playbook run specified in the template against the host.

**Additional resources**

- [Provisioning Callbacks in *Red Hat Ansible Automation Platform documentation*](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.5/html/using_automation_execution/controller-job-templates#controller-provisioning-callbacks)
