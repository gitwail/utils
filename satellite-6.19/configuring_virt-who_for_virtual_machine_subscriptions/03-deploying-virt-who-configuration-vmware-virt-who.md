---
title: "Configuring virt-who for VMware vSphere"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_virt-who_for_virtual_machine_subscriptions"
guide_title: "Configuring virt-who for virtual machine subscriptions"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt-who_for_virtual_machine_subscriptions/index#deploying-virt-who-configuration_vmware-virt-who"
---
# Chapter 3. Configuring virt-who for VMware vSphere

Configure virt-who for VMware vSphere to enable Satellite to discover and manage subscriptions for your virtual machines. This ensures proper subscription entitlements are applied based on the relationship between virtual machines and their physical hosts.

## 3.1. Creating a virt-who configuration by using the Satellite web UI

You can create a virt-who configuration for VMware vSphere by using the Satellite web UI.

The virt-who configuration creates a `virt_who_reporter_1` user with the `Virt-who Reporter` role, which provides minimal permissions for virt-who reporting to Satellite Server. This user cannot be manually configured or used to log in to Satellite Server.

Local configuration values are stored in the `/etc/virt-who.d/conf_name.conf` file. These values apply only to the hypervisor.

Global configuration values are stored in the `/etc/sysconfig/virt-who` file These values, which include `Interval`, `Enable debugging output`, `HTTP Proxy`, and `Ignore Proxy`, apply to all virt-who configurations on the same server. Redeploying a virt-who configuration on the same server overwrites these values.

**Prerequisites**

- You have imported a subscription manifest that includes a host-based subscription into Satellite Server. For more information, see [Section 1.2, “Checking for subscriptions that require virt-who”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt-who_for_virtual_machine_subscriptions/index#checking-for-subscriptions-that-require-virt-who_virt-who-vm-subs "1.2. Checking for subscriptions that require virt-who").
- You have created a virt-who user with read-only access to all objects in the vCenter Data Center and a non-expiring password on the vCenter Server.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Virt-who Configurations**.
2. Click **Create Config**.
3. Complete the following fields:

   - **Name**: Configuration name.
   - **Hypervisor Type**: Select **VMware vSphere / vCenter (esx)**.
   - **Hypervisor Server**: FQDN or IP address.
   - **Hypervisor Username**: virt-who user name.
   - **Hypervisor Password**: virt-who user password. The password is encrypted when you deploy the configuration.
   - **Interval**: Virtual machine information reporting interval.
   - **Satellite Server FQDN**.
   - **Hypervisor ID**: Select **Hostname** or **UUID**.
4. Optional: **Filtering**. Select one of the following options for querying hypervisors:

   - **Unlimited** (default): All hypervisors are queried.
   - **Whitelist**: Specific hypervisors are included.

     - **Filter hosts**: Comma-separated list of included hypervisors.
     - **Filter host parents**: Comma-separated list of included cluster IDs.
   - **Blacklist**: Specific hypervisors are excluded.

     - **Exclude hosts**: Comma-separated list of excluded hypervisors.
     - **Exclude host parents**: Comma-separated list of excluded cluster IDs.

   In the Filtering fields, specify the host name or UUID according to the hypervisor ID you selected. Follow these guidelines for host names:

   - You can use wildcards, regular expressions, and special characters in the host name.
   - If you use regular expressions, you must escape the backslashes.
   - If you use special characters, you must enclose the host name in quotation marks.

   For more information, see [Using the "Filter Host Parents" and "Exclude Host Parents" Attributes with VMware Clusters](https://access.redhat.com/solutions/5696481) in the *Red Hat Knowledgebase*.
5. You can configure the following logging and proxy options:

   - **Enable debugging output**: Enables debug logging for virt-who.
   - **HTTP Proxy**. Example: `http://proxy.example.com:3128`.

     To use no proxy, leave this field blank; this has the same result as entering `*` in the **Ignore Proxy** field.
   - **Ignore Proxy**: Comma-separated list of host names, IP addresses, or domains to bypass existing proxy settings.
6. Click **Submit**.

## 3.2. Creating a virt-who configuration by using Hammer CLI

You can create a virt-who configuration for VMware vSphere by using Hammer CLI.

The virt-who configuration creates a `virt_who_reporter_1` user with the `Virt-who Reporter` role, which provides minimal permissions for virt-who reporting to Satellite Server. This user cannot be manually configured or used to log in to Satellite Server.

Local configuration values are stored in the `/etc/virt-who.d/conf_name.conf` file. These values apply only to the hypervisor.

Global configuration values are stored in the `/etc/sysconfig/virt-who` file These values, which include `Interval`, `Enable debugging output`, `HTTP Proxy`, and `Ignore Proxy`, apply to all virt-who configurations on the same server. Redeploying a virt-who configuration on the same server overwrites these values.

**Prerequisites**

- You have imported a subscription manifest that includes a host-based subscription into Satellite Server. For more information, see [Section 1.2, “Checking for subscriptions that require virt-who”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt-who_for_virtual_machine_subscriptions/index#checking-for-subscriptions-that-require-virt-who_virt-who-vm-subs "1.2. Checking for subscriptions that require virt-who").
- You have created a virt-who user with read-only access to all objects in the vCenter Data Center and a non-expiring password on the vCenter Server.

**Procedure**

- On Satellite Server, enter the `hammer virt-who-config create` command:

  ```
  $ hammer virt-who-config create \
  --name My_virt-who_Configuration \
  --organizations "My_Organization" \
  --interval 720 \
  --filtering-mode none \
  --hypervisor-id hostname \
  --hypervisor-type esx \
  --hypervisor-server vcenter.example.com \
  --hypervisor-username virt_who_user \
  --hypervisor-password <password>
  --satellite-url satellite.example.com
  ```

In this command, use the following options:

- In `--filtering-mode`, specify `none` for no filtering of hypervisors for virt-who queries. Specify `whitelist` or `blacklist` to include or exclude hypervisors for virt-who queries.
- In `--hypervisor-id`, specify `hostname`, `uuid`, or `hwuuid` for the hypervisor ID format.

  - You can use `uuid` to avoid duplication if you rename a hypervisor.
  - You can use `hwuuid` for configurations that apply to a virtualization manager instead of an individual hypervisor.

    > **Note**
    >
    > You cannot change `hwuuid` to another option after virt-who starts running because this might cause duplicate entries in Subscription Manager.
- In `--hypervisor-server`, specify the FQDN or IP address of the vCenter Server.
- In `--hypervisor-username`, specify the name of the virt-who user you created on the hypervisor.
- Optionally, in the `--proxy` option, specify the proxy address and port, for example, `--proxy '\http://proxy.example.com:3128'`.
- Optionally, in the `--interval` option, specify the virtual machine information reporting interval in minutes.

**Example 3.1. VMware vSphere virt-who configuration**

```
type=esx
hypervisor_id=hostname
owner=Default_Organization
env=Library
server=vcenter.example.com
username=username_vcenter@example.com
encrypted_password=$cr_password
rhsm_hostname=satellite.example.com
rhsm_username=virt_who_reporter_1
rhsm_encrypted_password=$user_password
rhsm_prefix=/rhsm
```

## 3.3. Deploying a virt-who configuration on Satellite Server

You deploy a virt-who configuration on Satellite Server to enable virtual machine subscription tracking. You download a virt-who configuration script from the Satellite web UI and then you run the script on Satellite Server.

Global configuration values apply to all virt-who configurations on this server and are overwritten if you deploy a new virt-who configuration.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Virt-who Configurations**.
2. Click a virt-who configuration.
3. Click the **Deploy** tab.
4. Under **Hammer command**, click **Copy to clipboard**.
5. Log in to Satellite Server, paste the Hammer command into your terminal, and then run the command.

## 3.4. Deploying a virt-who configuration on Capsule Server

You deploy a virt-who configuration on Capsule Server to enable virtual machine subscription tracking. You download a virt-who configuration script from the Satellite web UI and then you run the script on Capsule Server.

Global configuration values apply to all virt-who configurations on this server and are overwritten if you deploy a new virt-who configuration.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Virt-who Configurations**.
2. Click a virt-who configuration.
3. Click the **Deploy** tab.
4. Under **Configuration script**, click **Download the script**.
5. Copy the script from Satellite Server to Capsule Server:

   ```
   $ scp deploy_virt_who_config_1.sh root@capsule.example.com:
   ```
6. Log in to Capsule Server and make the script executable:

   ```
   $ chmod +x deploy_virt_who_config_1.sh
   ```
7. Run the script:

   ```
   $ sh deploy_virt_who_config_1.sh
   ```
8. After the deployment is complete, delete the script:

   ```
   $ rm deploy_virt_who_config_1.sh
   ```

## 3.5. Deploying a virt-who configuration on a dedicated Red Hat Enterprise Linux server

You deploy a virt-who configuration on a dedicated Red Hat Enterprise Linux server to enable virtual machine subscription tracking. You download a virt-who configuration script from the Satellite web UI and then you run the script on the Red Hat Enterprise Linux server.

The server can be physical or virtual.

Global configuration values apply to all virt-who configurations on this server and are overwritten if you deploy a new virt-who configuration.

**Prerequisites**

- You have registered the Red Hat Enterprise Linux server to Satellite Server. For more information, see [Registering hosts by using global registration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration) in *Managing hosts*.

**Procedure**

1. Log in to the Red Hat Enterprise Linux server.
2. Add a TCP port for communication between virt-who and Satellite Server to the runtime configuration:

   ```
   $ firewall-cmd --add-port="443/tcp"
   ```
3. Add a TCP port for communication between virt-who and Satellite Server to the permanent configuration:

   ```
   $ firewall-cmd --add-port="443/tcp" --permanent
   ```
4. In the Satellite web UI, navigate to **Infrastructure** > **Virt-who Configurations**.
5. Click a virt-who configuration.
6. Click the **Deploy** tab.
7. Under **Configuration script**, click **Download the script**.
8. Copy the script from Satellite Server to the Red Hat Enterprise Linux server:

   ```
   $ scp deploy_virt_who_config_1.sh root@server.example.com:
   ```
9. Log in to the Red Hat Enterprise Linux server and make the script executable:

   ```
   $ chmod +x deploy_virt_who_config_1.sh
   ```
10. Run the script:

    ```
    $ sh deploy_virt_who_config_1.sh
    ```
11. After the deployment is complete, delete the script:

    ```
    $ rm deploy_virt_who_config_1.sh
    ```
