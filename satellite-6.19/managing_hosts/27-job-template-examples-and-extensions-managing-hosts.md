---
title: "Job template examples and extensions"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "C"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Job_Template_Examples_and_Extensions_managing-hosts"
---
# Appendix C. Job template examples and extensions

You can use these examples to modify, customize, and extend job templates for tasks such as restoring SELinux context, combining templates, or adding power actions.

## C.1. Customizing job templates

When creating a job template, you can include an existing template in the template editor field. This way you can combine templates, or create more specific templates from the general ones.

The following template combines default templates to install and start the **nginx** service on clients:

```
<%= render_template 'Package Action - Script Default', :action => 'install', :package => 'nginx' %>
<%= render_template 'Service Action - Script Default', :action => 'start', :service_name => 'nginx' %>
```

The above template specifies parameter values for the rendered template directly. It is also possible to use the **input()** method to allow users to define input for the rendered template on job execution. For example, you can use the following syntax:

```
<%= render_template 'Package Action - Script Default', :action => 'install', :package => input("package") %>
```

With the above template, you have to import the parameter definition from the rendered template. To do so, navigate to the **Jobs** tab, click **Add Foreign Input Set**, and select the rendered template from the **Target template** list. You can import all parameters or specify a comma separated list.

## C.2. Creating a job template to restore SELinux context

This example shows how to create a template called **Run Command - restorecon** that restores the default **SELinux** context for all files in the selected directory on target hosts.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Job templates**.
2. Click **New Job Template**.
3. Enter **Run Command - restorecon** in the **Name** field. Select **Default** to make the template available to all organizations. Add the following text to the template editor:

   ```
   restorecon -RvF <%= input("directory") %>
   ```

   The `<%= input("directory") %>` string is replaced by a user-defined directory during job invocation.
4. On the **Job** tab, set **Job category** to `Commands`.
5. Click **Add Input** to allow job customization. Enter `directory` to the **Name** field. The input name must match the value specified in the template editor.
6. Click **Required** so that the command cannot be executed without the user specified parameter.
7. Select **User input** from the **Input type** list. Enter a description to be shown during job invocation, for example `Target directory for restorecon`.
8. Click **Submit**. For more information, see [Section C.4, “Executing a restorecon template on multiple hosts”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Executing_a_restorecon_Template_on_Multiple_Hosts_managing-hosts "C.4. Executing a restorecon template on multiple hosts").

## C.3. Rendering a restorecon template

This example shows how to create a template derived from the **Run command - restorecon** template created in [Section C.2, “Creating a job template to restore SELinux context”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#creating-a-job-template-to-restore-selinux-context "C.2. Creating a job template to restore SELinux context").

This template does not require user input on job execution, it will restore the SELinux context in all files under the `/home/` directory on target hosts.

**Procedure**

- Create a new template as described in [Section 19.6.6, “Customizing job templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#customizing-job-templates "19.6.6. Customizing job templates"), and specify the following string in the template editor:

  ```
  <%= render_template("Run Command - restorecon", :directory => "/home") %>
  ```

## C.4. Executing a restorecon template on multiple hosts

This example shows how to run a job based on the template created in [Section C.2, “Creating a job template to restore SELinux context”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#creating-a-job-template-to-restore-selinux-context "C.2. Creating a job template to restore SELinux context") on multiple hosts. The job restores the SELinux context in all files under the `/home/` directory.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Jobs** and click **Run job**.
2. Select **Commands** as **Job category** and **Run Command – restorecon** as **Job template** and click **Next**.
3. Select the hosts on which you want to run the job. If you do not select any hosts, the job will run on all hosts you can see in the current context.
4. In the **directory** field, provide a directory, for example `/home`, and click **Next**.
5. Optional: To configure advanced settings for the job, fill in the **Advanced fields**. To learn more about advanced settings, see [Section 19.7.1, “Advanced settings in the job wizard”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#advanced-settings-in-the-job-wizard_managing-hosts "19.7.1. Advanced settings in the job wizard"). When you are done entering the advanced settings or if it is not required, click **Next**.
6. Schedule time for the job.

   - To execute the job immediately, keep the pre-selected **Immediate execution**.
   - To execute the job in future time, select **Future execution**.
   - To execute the job on regular basis, select **Recurring execution**.
7. Optional: If you selected future or recurring execution, select the **Query type**, otherwise click **Next**.

   - **Static query** means that the job executes on the exact list of hosts that you provided.
   - **Dynamic query** means that the list of hosts is evaluated just before the job is executed. If you entered the list of hosts based on some filter, the results can be different from when you first used that filter.

     Click **Next** after you have selected the query type.
8. Optional: If you selected future or recurring execution, provide additional details:

   - For **Future execution**, enter the **Starts at** date and time. You also have the option to select the **Starts before** date and time. If the job cannot start before that time, it will be canceled.
   - For **Recurring execution**, select the start date and time, frequency, and condition for ending the recurring job. You can choose the recurrence to never end, end at a certain time, or end after a given number of repetitions. You can also add **Purpose** - a special label for tracking the job. There can only be one active job with a given purpose at a time.

     Click **Next** after you have entered the required information.
9. Review job details. You have the option to return to any part of the job wizard and edit the information.
10. Click **Submit** to schedule the job for execution.

## C.5. Including power actions in templates

This example shows how to set up a job template for performing power actions, such as reboot. This procedure prevents Satellite from interpreting the disconnect exception upon reboot as an error, and consequently, remote execution of the job works correctly.

**Procedure**

- Create a new template as described in [Section 19.6.6, “Customizing job templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#customizing-job-templates "19.6.6. Customizing job templates"), and specify the following string in the template editor:

  ```
  <%= render_template("Power Action - Script Default", :action => "restart") %>
  ```
