---
title: "Configuring and setting up remote jobs"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "19"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs"
---
# Chapter 19. Configuring and setting up remote jobs

Red Hat Satellite supports remote execution of commands on hosts. Using remote execution, you can perform various tasks on multiple hosts simultaneously.

## 19.1. Remote execution overview

With remote execution in Satellite, you can run commands on hosts from Capsules by using shell scripts or Ansible. Multiple transport modes and job providers are available so that you can pick the one that fits your environment.

### 19.1.1. Remote execution in Red Hat Satellite

With remote execution, you can run jobs on hosts from Capsules by using shell scripts or Ansible roles and playbooks.

Use remote execution for the following benefits in Satellite:

- Run jobs on multiple hosts at once.
- Use variables in your commands for more granular control over the jobs you run.
- Use host facts and parameters to populate the variable values.
- Specify custom values for templates when you run the command.

Communication for remote execution occurs through Capsule Server, which means that Satellite Server does not require direct access to the target host, and can scale to manage many hosts.

To use remote execution, you must define a job template. A job template is a command that you want to apply to remote hosts. You can execute a job template multiple times.

Satellite uses ERB syntax job templates.

By default, Satellite includes several job templates for shell scripts and Ansible.

**Additional resources**

- [Appendix B, *Template writing reference*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts "Appendix B. Template writing reference")
- [Section 19.6.6, “Customizing job templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#customizing-job-templates "19.6.6. Customizing job templates")

### 19.1.2. Remote execution workflow

When you run a remote job on hosts, Satellite uses various strategies to select a remote execution Capsule for each host to balance the load across available Capsules. Knowing how Satellite selects a Capsule helps you configure subnets and proxy assignments so remote jobs use the proxy you intend, and recognize why a job ran on a particular proxy.

For custom Ansible roles that you create, or roles that you download, you must install the package containing the roles on your Capsule Server. Before you can use Ansible roles, you must import the roles into Satellite from the Capsule where they are installed.

Satellite searches only for Capsules that have the remote execution feature enabled.

1. Satellite finds the host’s interfaces that have the **Remote execution** checkbox selected.
2. Satellite finds the subnets of these interfaces.
3. Satellite finds remote execution Capsules assigned to these subnets.
4. From this set of Capsules, Satellite selects the Capsule that has the least number of running jobs. By doing this, Satellite ensures that the jobs load is balanced between remote execution Capsules.

If you have enabled **Prefer registered through Capsule for remote execution**, Satellite runs the REX job by using the Capsule to which the host is registered.

By default, **Prefer registered through Capsule for remote execution** is set to **No**. To enable it, in the Satellite web UI, navigate to **Administer** > **Settings**, and on the **Content** tab, set `Prefer registered through Capsule for remote execution` to **Yes**. This ensures that Satellite performs REX jobs on hosts by the Capsule to which they are registered to.

If Satellite does not find a remote execution Capsule at this stage, and if the **Fallback to Any Capsule** setting is enabled, Satellite adds another set of Capsules to select the remote execution Capsule from. Satellite selects the most lightly loaded Capsule from the following types of Capsules that are assigned to the host:

- DHCP, DNS and TFTP Capsules assigned to the host’s subnets
- DNS Capsule assigned to the host’s domain
- Realm Capsule assigned to the host’s realm
- Puppet server Capsule
- Puppet CA Capsule
- OpenSCAP Capsule

If Satellite does not find a remote execution Capsule at this stage, and if the **Enable Global Capsule** setting is enabled, Satellite selects the most lightly loaded remote execution Capsule from the set of all Capsules in the host’s organization and location to execute a remote job.

### 19.1.3. Transport modes for remote execution

You can configure Satellite to use push-based (SSH) or pull-based (MQTT) transport for remote job execution. Each Capsule uses one mode. Choose push for slightly better scalability in larger deployments or pull if your organization restricts the ports needed for SSH.

Push-based transport
:   On Capsules in `ssh` mode, remote execution uses the SSH service to transport job details. This is the default transport mode. The SSH service must be enabled and active on the target hosts. The remote execution Capsule must have access to the SSH port on the target hosts. Unless you have a different setting, the standard SSH port is 22.

    This transport mode supports both Script and Ansible providers.

Pull-based transport
:   On Capsules in `pull-mqtt` mode, remote execution uses Message Queueing Telemetry Transport (MQTT) to initiate the job execution it receives from Satellite Server. The host subscribes to the MQTT broker on Capsule for job notifications by using the `yggdrasil` pull client. After the host receives a notification from the MQTT broker, it pulls job details from Capsule over HTTPS, runs the job, and reports results back to Capsule.

    This transport mode supports the Script provider only.

    To use the `pull-mqtt` mode, you must enable it on Capsule Server and configure the pull client on hosts.

> **Note**
>
> If your Capsule already uses the `pull-mqtt` mode and you want to switch back to the `ssh` mode, run this `satellite-installer` command:
>
> ```
> # satellite-installer --foreman-proxy-plugin-remote-execution-script-mode ssh
> ```

## 19.2. Getting started with remote execution

To run your first remote job, ensure that your user account has the required permissions and your hosts are configured to run remote jobs.

### 19.2.1. Permissions for remote execution

You can control which roles can run which jobs within your infrastructure, including which hosts they can target.

The remote execution feature provides two built-in roles:

- **Remote Execution Manager**: Can access all remote execution features and functionality.
- **Remote Execution User**: Can only run jobs.

You can clone the **Remote Execution User** role and customize its filter for increased granularity. If you adjust the filter with the `view_job_templates` permission on a customized role, you can only see and trigger jobs based on matching job templates. You can use the `view_hosts` and `view_smart_proxies` permissions to limit which hosts or Capsules are visible to the role.

The `execute_template_invocation` permission is a special permission that is checked immediately before execution of a job begins. This permission defines which job template you can run on a particular host. This allows for even more granularity when specifying permissions.

You can run remote execution jobs against Red Hat Satellite and Capsule registered as hosts to Red Hat Satellite with the `execute_jobs_on_infrastructure_hosts` permission. Standard **Manager** and **Site Manager** roles have this permission by default. If you use either the **Manager** or **Site Manager** role, or if you use a custom role with the `execute_jobs_on_infrastructure_hosts` permission, you can execute remote jobs against registered Red Hat Satellite and Capsule hosts.

The following example shows filters for the `execute_template_invocation` permission:

```
name = Reboot and host.name = staging.example.com
name = Reboot and host.name ~ *.staging.example.com
name = "Restart service" and host_group.name = webservers
```

Use the first line in this example to apply the **Reboot** template to one selected host. Use the second line to define a pool of hosts with names ending with `.staging.example.com`. Use the third line to bind the template with a host group.

> **Note**
>
> Permissions assigned to users with these roles can change over time. If you have already scheduled some jobs to run in the future, and the permissions change, this can result in execution failure because permissions are checked immediately before job execution.

**Additional resources**

- [Creating and managing roles in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#creating-and-managing-roles)

### 19.2.2. Configuring a host to use the pull client

For Capsules configured to use `pull-mqtt` mode, hosts can subscribe to remote jobs using the remote execution pull client. This does not use SSH and hosts do not require opening up any incoming firewall ports.

**Prerequisites**

- You have registered the host to Satellite.
- The Capsule through which the host is registered is configured to use `pull-mqtt` mode. For more information, see [Configuring pull-based transport for remote execution](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-pull-based-transport-for-remote-execution_capsule) in *Installing Capsule Server*.
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server, available in the content view environments of the host, and enabled for the host. For more information, see [Changing the repository sets status for a host in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Changing_the_Repository_Sets_Status_for-a-Host-in_satellite_content-management) in *Managing content*.
- The AppStream repository for the operating system version of the host is synchronized on Satellite Server, available in the content view and the lifecycle environment of the host, and enabled for the host. For more information, see [Changing the repository sets status for a host in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Changing_the_Repository_Sets_Status_for-a-Host-in_satellite_content-management) in *Managing content*.
- The host can communicate with its Capsule over MQTT using port `1883`.
- The host can communicate with its Capsule over HTTPS using port `9090`.

**Procedure**

- Install the `katello-pull-transport-migrate` package on your host:

  - On Red Hat Enterprise Linux 10, Red Hat Enterprise Linux 9, and Red Hat Enterprise Linux 8 hosts:

    ```
    # dnf install katello-pull-transport-migrate
    ```
  - On Red Hat Enterprise Linux 7 hosts:

    ```
    # yum install katello-pull-transport-migrate
    ```

**Verification**

1. Determine which version of the `yggdrasil` package is installed on the host:

   ```
   $ rpm --query yggdrasil
   ```
2. Check the status of the Yggdrasil services:

   - If your host has `yggdrasil` version 0.4.z or later installed:

     ```
     # systemctl status yggdrasil com.redhat.Yggdrasil1.Worker1.foreman
     ```
   - If your host has `yggdrasil` version 0.2.z or earlier installed:

     ```
     # systemctl status yggdrasild
     ```

If the services are running, you have successfully configured the host to use the pull client.

### 19.2.3. Distributing SSH keys for remote execution

For Capsules in `ssh` mode, remote execution connections are authenticated using SSH. The public SSH key from Capsule must be distributed to its attached hosts that you want to manage. Satellite distributes SSH keys for the remote execution feature to the hosts provisioned from Satellite by default.

**Prerequisites**

- The SSH service is enabled and running on the hosts.
- Any network or host-based firewalls are configured to enable access to port 22.
- If the hosts are running on Amazon Web Services, enable password authentication. For more information, see [New User Accounts](https://aws.amazon.com/premiumsupport/knowledge-center/new-user-accounts-linux-instance).

**Procedure**

- Use one of the following methods to distribute the public SSH key from Capsule to target hosts:

  - [Section 19.3.8, “Distributing SSH keys for remote execution manually”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#distributing-ssh-keys-for-remote-execution-manually_managing-hosts "19.3.8. Distributing SSH keys for remote execution manually").
  - [Section 19.3.10, “Using the Satellite API to obtain SSH keys for remote execution”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Using_the_satellite_API_to_Obtain_SSH_Keys_for_Remote_Execution_managing-hosts "19.3.10. Using the Satellite API to obtain SSH keys for remote execution").
  - [Section 19.3.11, “Configuring a Kickstart template to distribute SSH keys during provisioning”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Configuring_a_Kickstart_Template_to_Distribute_SSH_Keys_During_Provisioning_managing-hosts "19.3.11. Configuring a Kickstart template to distribute SSH keys during provisioning").
  - For new Satellite hosts, you can deploy SSH keys to Satellite hosts during registration using the global registration template. For more information, see [Registering hosts by using global registration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration) in *Managing hosts*.

### 19.2.4. Executing a remote job by using Satellite web UI

You can execute a job that is based on a job template against one or more hosts from the Satellite web UI.

> **Note**
>
> Ansible jobs run in batches on multiple hosts, so you cannot cancel a job running on a specific host. A job completes only after the Ansible Playbook runs on all hosts in the batch.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Jobs** and click **Run job**.
2. Select the **Job category** and the **Job template** you want to use, then click **Next**.
3. Select hosts on which you want to run the job. If you do not select any hosts, the job will run on all hosts you can see in the current context.

   > **Note**
   >
   > If you want to select a host group and all of its subgroups, it is not sufficient to select the host group as the job would only run on hosts directly in that group and not on hosts in subgroups. Instead, you must either select the host group and all of its subgroups or use this search query:
   >
   > ```
   > hostgroup_fullname ~ "My_Host_Group*"
   > ```
   >
   > Replace *My_Host_Group* with the name of the top-level host group.
4. If required, provide inputs for the job template. Different templates have different inputs and some templates do not have any inputs. After entering all the required inputs, click **Next**.
5. Optional: To configure advanced settings for the job, fill in the **Advanced fields**. To learn more about advanced settings, see [Section 19.7.1, “Advanced settings in the job wizard”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#advanced-settings-in-the-job-wizard_managing-hosts "19.7.1. Advanced settings in the job wizard").
6. Click **Next**.
7. Schedule time for the job.

   - To execute the job immediately, keep the pre-selected **Immediate execution**.
   - To execute the job in future time, select **Future execution**.
   - To execute the job on regular basis, select **Recurring execution**.
8. Optional: If you selected future or recurring execution, select the **Query type**, otherwise click **Next**.

   - **Static query** means that job executes on the exact list of hosts that you provided.
   - **Dynamic query** means that the list of hosts is evaluated just before the job is executed. If you entered the list of hosts based on some filter, the results can be different from when you first used that filter.

   Click **Next** after you have selected the query type.
9. Optional: If you selected future or recurring execution, provide additional details:

   - For **Future execution**, enter the **Starts at** date and time. You also have the option to select the **Starts before** date and time. If the job cannot start before that time, it will be canceled.
   - For **Recurring execution**, select the start date and time, frequency, and the condition for ending the recurring job. You can choose the recurrence to never end, end at a certain time, or end after a given number of repetitions. You can also add **Purpose** - a special label for tracking the job. There can only be one active job with a given purpose at a time.

   Click **Next** after you have entered the required information.
10. Review job details. You have the option to return to any part of the job wizard and edit the information.
11. Click **Submit** to schedule the job for execution.

### 19.2.5. Executing a remote job by using Hammer CLI

You can execute a job that is based on a job template against one or more hosts.

> **Note**
>
> Ansible jobs run in batches on multiple hosts, so you cannot cancel a job running on a specific host. A job completes only after the Ansible Playbook runs on all hosts in the batch.

For more information about creating, monitoring, or canceling remote jobs with Hammer CLI, enter `hammer job-template --help` and `hammer job-invocation --help`.

**Procedure**

1. Enter the following command on Satellite:

   ```
   $ hammer settings set \
   --name remote_execution_global_proxy \
   --value false
   ```
2. Find the ID of the job template you want to use:

   ```
   $ hammer job-template list
   ```
3. Show the template details to see parameters required by your template:

   ```
   $ hammer job-template info --id My_Template_ID
   ```
4. Execute a remote job with custom parameters:

   ```
   $ hammer job-invocation create \
   --inputs My_Key_1="My_Value_1",My_Key_2="My_Value_2",... \
   --job-template "My_Template_Name" \
   --search-query "My_Search_Query"
   ```

   Replace `My_Search_Query` with the filter expression that defines hosts, for example `"name ~ My_Pattern"`.

## 19.3. Configuring remote execution

You can configure remote execution in several ways to control how remote jobs run on your hosts. This helps you configure the remote execution process to run in a way that fits your needs.

### 19.3.1. Configuring the fallback to any Capsule remote execution setting by using Satellite web UI

You can enable the **Fallback to Any Capsule** setting so that Satellite can use other Capsules assigned to hosts when no remote execution Capsule is found for the host subnets. This is useful for hosts with no subnets or when their subnets use Capsules without remote execution enabled.

If the **Fallback to Any Capsule** setting is enabled, Satellite adds another set of Capsules to select the remote execution Capsule from. Satellite also selects the most lightly loaded Capsule from the set of all Capsules assigned to the host, such as the following:

- DHCP, DNS and TFTP Capsules assigned to the subnets of the hosts
- DNS Capsule assigned to the host domain
- Realm Capsule assigned to the host realm
- Puppet server Capsule
- Puppet CA Capsule
- OpenSCAP Capsule

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Click **Remote Execution**.
3. Configure the **Fallback to Any Capsule** setting.

### 19.3.2. Configuring the fallback to any Capsule remote execution setting by using Hammer CLI

You can enable the **Fallback to Any Capsule** setting so that Satellite can use other Capsules assigned to hosts when no remote execution Capsule is found for the host subnets. This is useful for hosts with no subnets or when their subnets use Capsules without remote execution enabled.

If the **Fallback to Any Capsule** setting is enabled, Satellite adds another set of Capsules to select the remote execution Capsule from. Satellite also selects the most lightly loaded Capsule from the set of all Capsules assigned to the host, such as the following:

- DHCP, DNS and TFTP Capsules assigned to the host’s subnets
- DNS Capsule assigned to the host’s domain
- Realm Capsule assigned to the host’s realm
- Puppet server Capsule
- Puppet CA Capsule
- OpenSCAP Capsule

**Procedure**

- Configure the **Fallback to Any Capsule** setting:

  ```
  $ hammer settings set \
  --name remote_execution_fallback_proxy \
  --value true
  ```

### 19.3.3. Configuring the global Capsule remote execution setting by using Satellite web UI

You can enable the **Enable Global Capsule** setting so that Satellite can use any remote execution Capsule in the organization and location of the host when none is found for the subnets of the host. You can disable it to limit job execution to Capsules assigned to the subnets of the host only.

If the **Enable Global Capsule** setting is enabled, Satellite adds another set of Capsules to select the remote execution Capsule from. Satellite also selects the most lightly loaded remote execution Capsule from the set of all Capsules in the host’s organization and location to execute a remote job.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Click **Remote Execution**.
3. Configure the **Enable Global Capsule** setting.

### 19.3.4. Configuring the global Capsule remote execution setting by using Hammer CLI

You can enable the **Enable Global Capsule** setting so that Satellite can use any remote execution Capsule in the organization and location of the host when none is found for the subnets of the host. You can disable it to limit job execution to Capsules assigned to the subnets of the host only.

If the **Enable Global Capsule** setting is enabled, Satellite adds another set of Capsules to select the remote execution Capsule from. Satellite also selects the most lightly loaded remote execution Capsule from the set of all Capsules in the host’s organization and location to execute a remote job.

**Procedure**

- Enter the `hammer settings set` command on Satellite to configure the `Enable Global Capsule` setting. To set the value to `true`, enter the following command:

  ```
  $ hammer settings set \
  --name remote_execution_global_proxy \
  --value true
  ```

### 19.3.5. Setting an alternative directory for remote execution jobs in push mode

By default, Satellite uses the `/var/tmp` directory on hosts for remote execution jobs in push mode. You can use `satellite-installer` to set an alternative directory for executing remote execution jobs in push mode.

If the `/var/tmp/` directory on your host is mounted with the `noexec` flag, Satellite cannot execute remote execution job scripts in this directory.

**Procedure**

1. On your host, create a new directory:

   ```
   # mkdir /My_Remote_Working_Directory
   ```
2. Copy the SELinux context from the default `/var/tmp` directory:

   ```
   # chcon --reference=/var/tmp /My_Remote_Working_Directory
   ```
3. Configure your Satellite Server or Capsule Server to use the new directory:

   ```
   # satellite-installer \
   --foreman-proxy-plugin-remote-execution-script-remote-working-dir /My_Remote_Working_Directory
   ```

### 19.3.6. Setting an alternative directory for remote execution jobs in pull mode

By default, Satellite uses the `/run` directory on hosts for remote execution jobs in pull mode. You can use the Yggdrasil service to set an alternative directory for executing remote execution jobs in pull mode.

If the `/run/` directory on your host is mounted with the `noexec` flag, Satellite cannot execute remote execution job scripts in this directory.

**Prerequisite**

- Determine which version of the `yggdrasil` package is installed on the host:

  ```
  $ rpm --query yggdrasil
  ```

**Procedure**

1. Create a new directory:

   ```
   # mkdir /My_Remote_Working_Directory
   ```
2. Access the Yggdrasil service configuration:

   - If your host has `yggdrasil` version 0.4.z or later installed:

     ```
     # systemctl edit com.redhat.Yggdrasil1.Worker1.foreman
     ```
   - If your host has `yggdrasil` version 0.2.z or earlier installed:

     ```
     # systemctl edit yggdrasild
     ```
3. Specify the alternative directory by adding the following line to the configuration:

   ```
   Environment=FOREMAN_YGG_WORKER_WORKDIR=/My_Remote_Working_Directory
   ```
4. Restart the Yggdrasil services:

   - If your host has `yggdrasil` version 0.4.z or later installed:

     ```
     # systemctl restart yggdrasil com.redhat.Yggdrasil1.Worker1.foreman
     ```
   - If your host has `yggdrasil` version 0.2.z or earlier installed:

     ```
     # systemctl restart yggdrasild
     ```

### 19.3.7. Altering the privilege elevation method

By default, push-based remote execution uses `sudo` to switch from the SSH user to the effective user that executes the script on your host. You can globally configure an alternative method in your Satellite settings.

> **Note**
>
> If the SSH user and effective user for push-based transport are non-root users, ensure the `acl` package is installed on the host and the remote execution working directory is mounted on a filesystem that supports ACLs.

**Prerequisites**

- Your user account has a role assigned that grants the `view_settings` and `edit_settings` permissions.
- If you use `dzdo` for Ansible jobs, the `community.general` Ansible collection must be installed. This collection contains the required **dzdo** become plugin. For more information, see [Installing collections](https://docs.ansible.com/ansible/latest/collections_guide/collections_installing.html) in *Ansible documentation*.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Select the **Remote Execution** tab.
3. Click the value of the **Effective User Method** setting.
4. Select the new value.
5. Click **Submit**.

### 19.3.8. Distributing SSH keys for remote execution manually

You can distribute SSH keys for remote execution manually.

**Procedure**

- Copy the SSH pub key from your Capsule to your target host:

  ```
  # ssh-copy-id -i ~foreman-proxy/.ssh/id_rsa_foreman_proxy.pub root@client.example.com
  ```

  Repeat this step for each target host you want to manage.

**Verification**

- On your Capsule, confirm that the key was successfully copied to the target host:

  ```
  # ssh -i ~foreman-proxy/.ssh/id_rsa_foreman_proxy root@client.example.com
  ```

### 19.3.9. Adding a passphrase to SSH key used for remote execution

By default, Capsule uses a non-passphrase protected SSH key to execute remote jobs on hosts. You can protect the SSH key with a passphrase by following this procedure.

**Procedure**

- On your Satellite Server or Capsule Server, use `ssh-keygen` to add a passphrase to your SSH key:

  ```
  # ssh-keygen -p -f ~foreman-proxy/.ssh/id_rsa_foreman_proxy
  ```

**Next steps**

- Users now must use a passphrase when running remote execution jobs on hosts.

### 19.3.10. Using the Satellite API to obtain SSH keys for remote execution

You can obtain the Satellite SSH key from Capsule and add it to the `authorized_keys` on the host so that remote execution jobs can run on the host using SSH. Use this when you cannot use the standard distribution method, for example in automated or scripted setups.

Perform these steps on each target host where you want to run remote execution jobs.

**Procedure**

1. On the target host, create the `~/.ssh` directory to store the SSH key:

   ```
   # mkdir ~/.ssh
   ```
2. Download the SSH key from Capsule:

   ```
   # curl https://capsule.example.com:9090/ssh/pubkey >> ~/.ssh/authorized_keys
   ```
3. Configure permissions for the `~/.ssh` directory:

   ```
   # chmod 700 ~/.ssh
   ```
4. Configure permissions for the `authorized_keys` file:

   ```
   # chmod 600 ~/.ssh/authorized_keys
   ```

### 19.3.11. Configuring a Kickstart template to distribute SSH keys during provisioning

You can add a `remote_execution_ssh_keys` snippet to your custom Kickstart template to deploy SSH keys to hosts during provisioning. Kickstart templates that Satellite ships include this snippet by default. Satellite copies the SSH key for remote execution to the systems during provisioning.

**Procedure**

- To include the public key in newly-provisioned hosts, add the following snippet to the Kickstart template that you use:

  ```
  <%= snippet 'remote_execution_ssh_keys' %>
  ```

## 19.4. Configuring Capsule and hosts to authenticate with SSH certificates during remote execution

By default, Satellite follows the Trust on First Use (TOFU) model when establishing a remote execution connection. You can reconfigure your Capsule to use SSH certificates instead. SSH certificates are signed by a Certificate Authority (CA), which allows centralized trust management and revocation capabilities.

You can configure SSH certificate authentication in the following ways. You can configure one or both of these authentication methods depending on your security requirements:

Using user certificates
:   When your Capsule connects to hosts, it presents a signed certificate. Hosts trust the CA that signed the certificate, eliminating the need to distribute individual SSH public keys to each host.

Using host certificates
:   When your Capsule connects to hosts, the hosts present signed certificates. Capsule verifies that it is connecting to legitimate hosts, helping prevent man-in-the-middle attacks.

If you configure Capsule to use SSH certificates, the configuration will apply to running Ansible jobs as well.

### 19.4.1. Enabling SSH certificate authentication on Capsule

You can configure Capsule to present an SSH certificate signed by a Certificate Authority (CA) to hosts instead of a plain SSH public key.

> **Warning**
>
> After enabling this feature, SSH certificate authentication works on all newly registered or provisioned hosts. Existing hosts will continue to trust plain SSH keys of your Capsule until you configure those hosts to trust the CA. To configure existing hosts to accept the SSH certificate from your Capsule, complete [Section 19.4.4, “Configuring registered hosts to accept an SSH certificate from Capsule”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-registered-hosts-to-accept-ssh-certificate-from-capsule "19.4.4. Configuring registered hosts to accept an SSH certificate from Capsule").

**Prerequisites**

- You have a CA for signing SSH certificates.

**Procedure**

1. On the Capsule Server, locate the SSH key pair that Capsule uses for remote execution. You can find the private key location in `/etc/foreman-proxy/settings.d/remote_execution_ssh.yml` under the `:ssh_identity_key_file:` setting. By default, the location is `/var/lib/foreman-proxy/ssh/id_rsa_foreman_proxy`.
2. If the CA is on a different server than your Capsule Server, copy the public key file of the Capsule to the CA server.
3. Sign the Capsule SSH public key with your CA.

   > **Note**
   >
   > The `ssh-keygen` command creates the certificate file with the name `My_Capsule_Private_Key-cert.pub`. Do not change the name of the file. By default, the created SSH certificate is named `id_rsa_foreman_proxy-cert.pub`.
4. If the CA is on a different server than your Capsule Server, ensure the Capsule Server has the SSH certificate and the CA public key file:

   1. Copy the created SSH certificate file back to the Capsule Server into the same directory as the original SSH key pair.
   2. Copy the CA public key file to the Capsule Server.

      > **Note**
      >
      > By default, the `foreman-proxy` user has read access to the CA public key file. Do not store the file in non-standard directories so that the `foreman-proxy` user can read the file. Red Hat recommends storing the file in the `/etc/ssh/` directory.
5. Enable SSH certificate authentication on your Capsule:

   ```
   # satellite-installer \
   --foreman-proxy-plugin-remote-execution-script-ssh-user-ca-public-key-file My_CA_Public_Key_File_Path
   ```

**Verification**

1. Run a remote execution job on a host through your Capsule with SSH certificate authentication enabled.
2. On the host, view the `sshd` logs:

   ```
   # journalctl -u sshd
   ```
3. Find the log message that confirms that the SSH certificate was used for authentication:

   ```
   Accepted publickey for <SSH USER> from <IP> port 22 ssh2: RSA-CERT ID foreman-proxy CA RSA
   ```

### 19.4.2. Disabling SSH certificate authentication on Capsule

If you disable SSH certificate authentication on Capsule, you will revert to plain SSH key pair authentication.

**Procedure**

1. Distribute your Capsule SSH keys to the hosts that use your Capsule for remote execution. For more information, see [Section 19.2.3, “Distributing SSH keys for remote execution”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Distributing_SSH_Keys_for_Remote_Execution_managing-hosts "19.2.3. Distributing SSH keys for remote execution").
2. Delete the SSH certificate file of the Capsule. By default, the path of this file is `/var/lib/foreman-proxy/ssh/id_rsa_foreman_proxy-cert.pub`.
3. Disable the SSH certificate authentication:

   ```
   # satellite-installer \
   --reset-foreman-proxy-plugin-remote-execution-script-ssh-user-ca-public-key-file
   ```

### 19.4.3. Rotating Capsule SSH certificate

You can rotate the SSH certificate used by Capsule for remote execution by generating a new SSH key pair and having it signed by your configured CA. For example, this is useful if the SSH certificate used by Capsule for remote execution is no longer valid.

**Prerequisites**

- You have SSH certificate authentication enabled on Capsule.
- You have a configured CA for signing SSH certificates.

**Procedure**

1. On the Capsule Server, locate the directory that Capsule uses for remote execution by checking where the configured Capsule SSH private key is stored. You can find the location of the SSH private key in `/etc/foreman-proxy/settings.d/remote_execution_ssh.yml` under the `:ssh_identity_key_file:` setting. By default, the directory is `/var/lib/foreman-proxy/ssh/`.
2. On the Capsule Server, generate a new SSH key pair in the directory:

   ```
   # ssh-keygen -f My_Capsule_SSH_Directory/My_New_SSH_Key
   ```
3. Set the correct ownership for the new key files:

   ```
   # chown foreman-proxy:foreman-proxy My_Capsule_SSH_Directory/My_New_SSH_Key*
   ```
4. If the CA is on a different server than your Capsule Server, copy the new public key file to the CA server.
5. Sign the new SSH public key with your CA.
6. If the CA is on a different server than your Capsule Server, copy the created SSH certificate file back to the Capsule Server into the Capsule SSH directory.
7. Set the correct ownership for the certificate file:

   ```
   # chown foreman-proxy:foreman-proxy My_Capsule_SSH_Directory/My_New_SSH_Key-cert.pub
   ```
8. Configure Capsule to use the new SSH key:

   ```
   # satellite-installer \
   --foreman-proxy-plugin-remote-execution-script-ssh-identity-file My_Capsule_SSH_Directory/My_New_SSH_Key
   ```

   > **Note**
   >
   > If you created the new SSH key pair with the same name as the old one and thus replaced the old key pair, you do not need to update your Capsule configuration with satellite-installer.
9. Optional: Remove the old SSH key files from the Capsule SSH directory.

**Verification**

1. Run a remote execution job on a host through your Capsule with SSH certificate authentication enabled.
2. On the host, view the `sshd` logs:

   ```
   # journalctl -u sshd
   ```
3. Find the log message that confirms that the SSH certificate was used for authentication:

   ```
   Accepted publickey for <SSH USER> from <IP> port 22 ssh2: RSA-CERT ID foreman-proxy CA RSA
   ```

### 19.4.4. Configuring registered hosts to accept an SSH certificate from Capsule

After you enable SSH certificate authentication on your Capsule, you can configure hosts to accept SSH certificates from your Capsule. This ensures the hosts will no longer accept plain SSH keys during a remote execution connection.

You can use remote execution to apply these changes.

Perform these steps on each host that uses your Capsule for remote execution and was registered before you enabled SSH certificate authentication on your Capsule.

**Prerequisites**

- You have a Certificate Authority (CA) for signing SSH certificates.

**Procedure**

1. Copy the CA public key file to the host.
2. Ensure that the `/etc/ssh/sshd_config.d/` directory exists:

   ```
   # mkdir --parents /etc/ssh/sshd_config.d/
   ```
3. Configure the `sshd` service to trust the CA:

   ```
   # echo 'TrustedUserCAKeys My_CA_Public_Key_File_Path' > /etc/ssh/sshd_config.d/60-foreman-user-ca.conf
   ```
4. Set the correct SELinux context for the created file:

   ```
   # restorecon /etc/ssh/sshd_config.d/60-foreman-user-ca.conf
   ```
5. Restart the `sshd` service:

   ```
   # systemctl restart sshd
   ```
6. Remove existing SSH keys of the Capsule from the `authorized_keys` file of your SSH user. By default, the SSH user is root and the SSH keys are associated with the `foreman-proxy` user:

   ```
   # sed -i '/foreman-proxy/d' ~/.ssh/authorized_keys
   ```

   > **Note**
   >
   > This command might not work if you configured custom SSH keys on your Capsule. In that case, manually edit the `authorized_keys` file.

### 19.4.5. Enabling SSH host certificate verification on Capsule

Your Capsule can use SSH host certificates to verify the identity of hosts. In this configuration, Capsule verifies that hosts present valid certificates signed by a trusted Certificate Authority (CA) during SSH connections. Your Capsule can trust host certificates signed by multiple CAs.

> **Important**
>
> After you enable host certificate verification on Capsule, all hosts that use this Capsule for remote execution can authenticate only if they are configured to use host certificates.

**Prerequisites**

- You have a CA for signing SSH host certificates.

**Procedure**

1. On each host that uses this Capsule for remote execution, prepare the SSH certificate for the host:

   1. Copy one of the public key files of the host to the CA server. The public keys are located in `/etc/ssh/`.
   2. Sign the public key with your CA to create an SSH host certificate. Use the `-h` option when generating the SSH host certificate with `ssh-keygen`.

      > **Important**
      >
      > The `ssh-keygen` command creates the certificate file with the name `My_Host_Private_SSH_Key-cert.pub`. Do not change the name of the file.
   3. Copy the SSH certificate file back to the host. The location must be the same as the location of the private key.
   4. Configure the host to use the certificate:

      ```
      # mkdir --parents /etc/ssh/sshd_config.d/
      # echo 'HostCertificate My_Host_SSH_Certificate_Path' > /etc/ssh/sshd_config.d/60-host-cert.conf
      # restorecon -R /etc/ssh/
      ```

      > **Note**
      >
      > If the host SSH public key you used for the certificate is not one of the default keys (`/etc/ssh/ssh_host_ecdsa_key.pub`, `/etc/ssh/ssh_host_ed25519_key.pub`, or `/etc/ssh/ssh_host_rsa_key.pub`), also add the host key configuration:
      >
      > ```
      > # echo 'HostKey My_Host_Private_SSH_Key_Path' >> /etc/ssh/sshd_config.d/60-host-cert.conf
      > ```
   5. Restart the `sshd` service:

      ```
      # systemctl restart sshd
      ```
2. On the Capsule, configure host certificate verification:

   1. If the host CA is not located on the Capsule Server, copy the host CA public key file to your Capsule Server. If you have multiple host CAs, place all of their public keys in a single file, with each key on a separate line.
   2. Enable host certificate verification:

      ```
      # satellite-installer \
      --foreman-proxy-plugin-remote-execution-script-ssh-host-ca-public-keys-file My_Host_CA_Public_Keys_File_Path
      ```

**Verification**

- Run a remote execution job on a host that is not configured with a host certificate signed by a trusted CA. The attempt results in an authentication failure.

### 19.4.6. Disabling SSH host certificate verification on Capsule

If you disable SSH host certificate verification on Capsule, you will revert to the Trust On First Use (TOFU) model.

**Procedure**

- On Capsule, disable SSH host certificate verification:

  ```
  # satellite-installer \
  --reset-foreman-proxy-plugin-remote-execution-script-ssh-host-ca-public-keys-file
  ```

## 19.5. Tuning authentication and performance for remote execution

Satellite supports advanced authentication methods and performance tuning for remote execution. You can configure Kerberos-based authentication and control job execution rates on Capsules.

### 19.5.1. Configuring a keytab for Kerberos ticket granting tickets

You can configure Satellite to use a keytab so that it obtains Kerberos ticket-granting tickets (TGTs) automatically for remote execution. This avoids manually retrieving tickets and enables remote jobs to use Kerberos authentication.

**Procedure**

1. Find the ID of the `foreman-proxy` user:

   ```
   # id -u foreman-proxy
   ```
2. Modify the `umask` value so that new files have the permissions `600`:

   ```
   # umask 077
   ```
3. Create the directory for the keytab:

   ```
   # mkdir -p "/var/kerberos/krb5/user/My_User_ID"
   ```
4. Create a keytab or copy an existing keytab to the directory:

   ```
   # cp My_Client.keytab /var/kerberos/krb5/user/My_User_ID/client.keytab
   ```
5. Change the directory owner to the `foreman-proxy` user:

   ```
   # chown -R foreman-proxy:foreman-proxy "/var/kerberos/krb5/user/My_User_ID"
   ```
6. Ensure that the keytab file is read-only:

   ```
   # chmod -wx "/var/kerberos/krb5/user/My_User_ID/client.keytab"
   ```
7. Restore the SELinux context:

   ```
   # restorecon -RvF /var/kerberos/krb5
   ```

### 19.5.2. Configuring Kerberos authentication for remote execution

You can use Kerberos authentication to establish an SSH connection for remote execution on Satellite hosts.

**Prerequisites**

- Satellite Server is enrolled on the Kerberos server.
- The Satellite target host is enrolled on the Kerberos server.
- A Kerberos user account for remote execution is configured and initialized.
- The `foreman-proxy` user on Satellite has a valid Kerberos ticket-granting ticket (TGT).

**Procedure**

1. Enable Kerberos authentication for remote execution:

   ```
   # satellite-installer --foreman-proxy-plugin-remote-execution-script-ssh-kerberos-auth true
   ```
2. To edit the default user for remote execution, in the Satellite web UI, navigate to **Administer** > **Settings** and click the **Remote Execution** tab. In the **SSH User** row, edit the second column and add the user name for the Kerberos account.
3. Navigate to **remote_execution_effective_user** and edit the second column to add the user name for the Kerberos account.

**Verification**

- To confirm that Kerberos authentication is ready to use, run a remote job on the host. For more information, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").

### 19.5.3. Setting the job rate limit on Capsule

You can limit the maximum number of active jobs on a Capsule at a time to prevent performance spikes.

The job is active from the time Capsule first tries to notify the host about the job until the job is finished on the host.

The job rate limit only applies to mqtt based jobs.

> **Note**
>
> The optimal maximum number of active jobs depends on the computing resources of your Capsule Server. By default, the maximum number of active jobs is unlimited.

**Procedure**

- Set the maximum number of active jobs using `satellite-installer`:

  ```
  # satellite-installer \
  --foreman-proxy-plugin-remote-execution-script-mqtt-rate-limit MAX_JOBS_NUMBER
  ```

  For example:

  ```
  # satellite-installer \
  --foreman-proxy-plugin-remote-execution-script-mqtt-rate-limit 200
  ```

## 19.6. Customizing remote jobs

You can customize remote jobs in Satellite to fit your needs. For example, you can create and customize job templates or you can import Ansible playbooks to use in your remote jobs.

### 19.6.1. Creating a job template by using Satellite web UI

You can create a job template from the Satellite web UI to define a reusable script or Ansible task that you can run on hosts via remote execution.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Job templates**.
2. Click **New Job Template**.
3. Click the **Template** tab, and in the **Name** field, enter a unique name for your job template.
4. Select **Default** to make the template available for all organizations and locations.
5. Create the template directly in the template editor or upload it from a text file by clicking **Import**.
6. Optional: In the **Audit Comment** field, add information about the change.
7. Click the **Job** tab, and in the **Job category** field, enter your own category or select from the default categories.
8. Optional: In the **Description Format** field, enter a description template. For example, `Install package %{package_name}`. You can also use `%{template_name}` and `%{job_category}` in your template.
9. From the **Provider Type** list, select **SSH** for shell scripts and **Ansible** for Ansible tasks or playbooks.
10. Optional: In the **Timeout to kill** field, enter a timeout value to terminate the job if it does not complete.
11. Optional: Click **Add Input** to define an input parameter. Parameters are requested when executing the job and do not have to be defined in the template. For examples, see the **Help** tab.
12. Optional: Click **Foreign input set** to include other templates in this job.
13. Optional: In the **Effective user** area, configure a user if the command cannot use the default `remote_execution_effective_user` setting.
14. Optional: If this template is a snippet to be included in other templates, click the **Type** tab and select **Snippet**.
15. Optional: If you use the Ansible provider, click the **Ansible** tab.

    1. Select **Enable Ansible Callback** to allow hosts to send facts, which are used to create configuration reports, back to Satellite after a job finishes.
    2. Select **Enable Ansible Check Mode** to run jobs based on the template in Ansible check mode, which executes Ansible playbooks without making changes to hosts.
16. Click the **Location** tab and add the locations where you want to use the template.
17. Click the **Organizations** tab and add the organizations where you want to use the template.
18. Click **Submit** to save your changes.

**Additional resources**

- [Template writing reference](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts)
- [Job template examples and extensions in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Job_Template_Examples_and_Extensions_managing-hosts)

### 19.6.2. Creating a job template by using Hammer CLI

You can create a job template by using Hammer CLI to define a reusable script or Ansible task that you can run on hosts via remote execution.

**Procedure**

- Create a job template using a template-definition file:

  ```
  $ hammer job-template create \
  --file "Path_to_My_Template_File" \
  --job-category "My_Category_Name" \
  --name "My_Template_Name" \
  --provider-type SSH
  ```

**Additional resources**

- [Template writing reference](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts)
- [Job template examples and extensions in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Job_Template_Examples_and_Extensions_managing-hosts)

### 19.6.3. Importing an Ansible Playbook by name

You can import Ansible Playbooks by name to Satellite from collections installed on Capsule. Satellite creates a job template from each playbook so you can run it on hosts via remote execution without writing the template manually.

When you import an Ansible Playbook, Satellite creates a job template from the imported playbook and places the template in the `Ansible Playbook - Imported` job category. If you have a custom collection, place it in `/etc/ansible/collections/ansible_collections/My_Namespace/My_Collection`.

**Prerequisites**

- Ansible plugin is enabled.
- Your Satellite account has a role that grants the `import_ansible_playbooks` permission.

**Procedure**

1. Fetch the available Ansible Playbooks by using the following API request:

   ```
   $ curl \
   --header 'Content-Type: application/json' \
   --request GET \
   https://satellite.example.com/ansible/api/v2/ansible_playbooks/fetch?proxy_id=My_Capsule_ID
   ```
2. Select the Ansible Playbook you want to import and note its name.
3. Import the Ansible Playbook by its name:

   ```
   $ curl \
   --data '{ "playbook_names": ["My_Playbook_Name"] }' \
   --header 'Content-Type: application/json' \
   --request PUT \
   https://satellite.example.com/ansible/api/v2/ansible_playbooks/sync?proxy_id=My_Capsule_ID
   ```

   You get a notification in the Satellite web UI after the import completes.

**Next steps**

- You can run the playbook by executing a remote job from the created job template. For more information, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").

### 19.6.4. Importing all available Ansible Playbooks

When Ansible collections on your Capsule hold playbooks you want to run from Satellite, you can import all available Ansible Playbooks to Satellite in one step.

When you import an Ansible Playbook, Satellite creates job templates from the imported playbooks and places the templates in the `Ansible Playbook - Imported` job category. If you have a custom collection, place it in `/etc/ansible/collections/ansible_collections/My_Namespace/My_Collection`.

**Prerequisites**

- Ansible plugin is enabled.
- Your Satellite account has a role that grants the `import_ansible_playbooks` permission.

**Procedure**

- Import the Ansible Playbooks by using the following API request:

  ```
  # curl -X PUT -H 'Content-Type: application/json' https://satellite.example.com/ansible/api/v2/ansible_playbooks/sync?proxy_id=My_Capsule_ID
  ```

  You get a notification in the Satellite web UI after the import completes.

**Next steps**

- You can run the playbooks by executing a remote job from the created job templates. For more information, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").

### 19.6.5. Running an Ansible Playbook from Satellite

You can run an Ansible Playbook on a host or host group by executing a remote job in Satellite.

> **Important**
>
> When you execute an Ansible Playbook on multiple hosts, Satellite renders the playbook for all hosts in the batch, but only uses the rendered playbook of the first host to execute it on all hosts in the batch. Therefore, you cannot modify the behavior of the playbook per host by using a host parameter in the template control flow constructs. Host parameters are translated into Ansible variables, so you can use them to control the behavior in native Ansible constructs. For more information, see [BZ#2282275](https://bugzilla.redhat.com/show_bug.cgi?id=2282275).

**Prerequisites**

- Ansible plugin in Satellite is enabled.
- Remote job execution is configured. For more information, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").
- You have an Ansible Playbook ready to use.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Jobs**.
2. Click **Run Job**.
3. In **Job category**, select `Ansible Playbook`.
4. In **Job template**, select `Ansible - Run playbook`.
5. Click **Next**.
6. Select the hosts on which you want to run the playbook.
7. In the **playbook** field, paste the content of your Ansible Playbook.
8. Follow the wizard to complete setting the remote job. For more information, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").
9. Click **Submit** to run the Ansible Playbook on your hosts.

**Example 19.1. Example Ansible Playbook to access host parameters**

You can use host parameters from Satellite in Ansible Playbooks.

```yaml
---
- name: "Ansible Playbook to access host parameters"
  hosts: all
  tasks:
    - name: "View a host parameter"
      ansible.builtin.debug:
        msg: "{{ hostvars[inventory_hostname]['My_Host_Parameter'] }}"
...
```

Ansible will access the host parameter and show its value. If you set the host parameter to an ERB template, for example, `<%= @host.capabilities.include?(:snapshots) %>`, Satellite will render it and provide the result to Ansible. Ansible receives only the rendered value, not the ERB template itself.

For more information, see [Appendix D, *Host parameter hierarchy*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#host-parameter-hierarchy "Appendix D. Host parameter hierarchy").

**Additional resources**

- [Section 19.6.3, “Importing an Ansible Playbook by name”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#importing-an-ansible-playbook-by-name_managing-hosts "19.6.3. Importing an Ansible Playbook by name")
- [Section 19.6.4, “Importing all available Ansible Playbooks”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#importing-all-available-ansible-playbooks_managing-hosts "19.6.4. Importing all available Ansible Playbooks")

### 19.6.6. Customizing job templates

Satellite provides default job templates that you can use for executing jobs. Default job templates are locked for editing but you can clone them and edit the clone.

Job templates use the Embedded Ruby (ERB) syntax. Ansible job templates use YAML syntax.

At run time, job templates can accept parameter variables that you define for a host. Note that only the parameters visible on the **Parameters** tab at the host’s edit page can be used as input parameters for job templates.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Job templates**.
2. To clone a template, in the **Actions** column, select **Clone**.
3. Enter a unique name for the clone and click **Submit** to save the changes.
4. In the list of job templates, click the cloned template to start editing it.

   > **Note**
   >
   > An Ansible template must begin with `---`. You can embed an Ansible Playbook YAML file into the job template body. You can also add ERB syntax to customize your YAML Ansible template.

**Additional resources**

- [Template Writing Reference in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts)
- [Synchronizing template repositories in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#synchronizing-template-repositories)

### 19.6.7. Changing the associated template

You can change the associated template to customize remote execution workflows.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Remote Execution Features**.
2. Select the remote execution feature of which you want to change the associated template.
3. In the **Job Template** menu, select a different job template.

   > **Important**
   >
   > Changing the default job templates might break existing Satellite workflows. Evaluate carefully why you want to change the default job template.
   >
   > Cloned templates do not receive updates from Red Hat when upgrading Satellite.
4. Click **Submit**.

### 19.6.8. Scheduling a recurring Ansible job for a host

You can schedule a recurring Ansible job to run on a host at a set interval. This is useful for regular tasks such as compliance checks, patching, or configuration drift remediation.

**Prerequisites**

- Your user account has the `view_foreman_tasks`, `view_job_invocations`, and `view_recurring_logics` permissions.
- At least one Ansible role is assigned to your host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select your host.
3. On the **Ansible** tab, select **Jobs**.
4. Click **Schedule recurring job**.
5. In the **Repeat** list, select the interval.
6. In the **Start time** field, enter the start time of the recurring job.
7. In the **Start date** field, enter the start date of the recurring job.
8. Click **Submit**.

### 19.6.9. Scheduling a recurring Ansible job for a host group

You can schedule a recurring Ansible job to run on a host group at a set interval. This is useful for regular tasks such as compliance checks, patching, or configuration drift remediation across all hosts that are assigned to this host group.

**Prerequisites**

- At least one Ansible role is assigned to your host group.
- At least one host is assigned to your host group.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. In the **Actions** column, select **Configure Ansible Job** for the host group you want to schedule an Ansible roles run for.
3. Click **Schedule recurring job**.
4. In the **Repeat** list, select the interval.
5. In the **Start time** field, enter the start time of the recurring job.
6. In the **Start date** field, enter the start date of the recurring job.
7. Click **Submit**.

### 19.6.10. Using Ansible provider for package and errata actions

By default, Satellite is configured to use the Script provider templates for remote execution jobs. If you prefer using Ansible job templates for your remote jobs, you can configure Satellite to use them by default for remote execution features associated with them.

> **Note**
>
> Remember that Ansible job templates only work when remote execution is configured for `ssh` mode.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Remote Execution Features**.
2. Find each feature whose name contains `by_search`.
3. Change the job template for these features from `Katello Script Default` to `Katello Ansible Default`.
4. Click **Submit**.

   Satellite now uses Ansible provider templates for remote execution jobs by which you can perform package and errata actions. This applies to job invocations from the Satellite web UI as well as by using `hammer job-invocation create` with the same remote execution features that you have changed.

## 19.7. Remote execution reference

Remote execution in Satellite provides advanced configuration options and extended scheduling capabilities for running jobs on hosts.

### 19.7.1. Advanced settings in the job wizard

Some job templates require you to enter advanced settings. Some of the advanced settings are only visible to certain job templates. Below is the list of general advanced settings.

SSH user
:   A user to be used for connecting to the host through SSH.

Effective user
:   A user to be used for executing the job. By default it is the SSH user. If it differs from the SSH user, su or sudo, depending on your settings, is used to switch the accounts.

    - If you set an effective user in the advanced settings, Ansible sets `ansible_become_user` to your input value and `ansible_become` to `true`. This means that if you use the parameters `become: true` and `become_user: My_User` within a playbook, these will be overwritten by Satellite.
    - If your *SSH user* and *effective user* are identical, Satellite does not overwrite the `become_user`. Therefore, you can set a custom `become_user` in your Ansible Playbook.

Description
:   A description template for the job.

Timeout to kill
:   Time in seconds from the start of the job after which the job should be killed if it is not finished already.

Time to pickup
:   Time in seconds after which the job is canceled if it is not picked up by a client. This setting only applies to hosts using `pull-mqtt` transport.

Password
:   Is used if SSH authentication method is a password instead of the SSH key.

Private key passphrase
:   Is used if SSH keys are protected by a passphrase.

Effective user password
:   Is used if effective user is different from the ssh user.

Concurrency level
:   Defines the maximum number of tasks executed at once. This can prevent overload of system resources in a case of executing the job on a large number of hosts.

    If you set the concurrency level to two or higher, remote execution jobs on hosts are executed concurrently. For example, you can patch multiple hosts at the same time.

    A concurrency level of one is identical to running remote execution jobs sequentially. For example, if you run HTTP servers behind a load balancer, you can set the concurrency level to one to update or configure them one at a time to ensure that there is always a host up and running.

    A high number of concurrent tasks may overload Capsules. If you have many hosts registered to Capsules, batching prevents overloading your Capsules. By default, **Allow Capsule batch tasks** is set to `Yes`. You can control the number of tasks your Capsule receives at once from starting a remote execution job by setting the batch size. By default, **Capsule tasks batch size** is set to `100`. You can find both settings under **Administer** > **Settings** on the **Tasks** tab.

Execution ordering
:   Determines the order in which the job is executed on hosts. It can be alphabetical or randomized.

### 19.7.2. Extended cron line syntax in remote jobs

When scheduling a cron job with remote execution, you can use an extended cron line to specify the cadence of the job. Extended cron syntax adds patterns on top of the standard five-field cron line when you schedule remote execution jobs.

The standard cron line has five fields: minute, hour, day of the month, month, and day of the week. For example, `0 5 * * *` means every day at 5 AM.

Extended syntax supports the following patterns:

`#` to specify a concrete weekday in a month
:   For example:

    - `0 0 * * mon#1` specifies first Monday of the month
    - `0 0 * * fri#3,fri#4` specifies third and fourth Fridays of the month
    - `0 7 * * fri#-1` specifies the last Friday of the month at 07:00
    - `0 7 * * fri#L` also specifies the last Friday of the month at 07:00
    - `0 23 * * mon#2,tue` specifies the second Monday of the month and every Tuesday, at 23:00

`%` to specify every n-th day of the month
:   For example:

    - `9 0 * * sun%2` specifies every other Sunday at 00:09
    - `0 0 * * sun%2+1` specifies every odd Sunday
    - `9 0 * * sun%2,tue%3` specifies every other Sunday and every third Tuesday

`&` to specify that the day of month must match day of week
:   For example:

    - `0 0 30 * 1&` specifies the 30th day of the month, but only if it is Monday

### 19.7.3. Troubleshooting remote jobs failing due to hostname resolution errors

If remote execution jobs fail on your host due to `Could not resolve hostname: Name or service not known`, disable **Ignore interfaces facts for provisioning**.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select your host.
3. Click **Edit**.
4. On the **Interfaces** tab, check if the host has an IP address. If the host has no IP address, continue with this procedure.
5. Navigate to **Administer** > **Settings**.
6. On the **Facts** tab, set **Ignore interfaces facts for provisioning** to `No`. This ensures that an IP address is assigned to the host during registration.
