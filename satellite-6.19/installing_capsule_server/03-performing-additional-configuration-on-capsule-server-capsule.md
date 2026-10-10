---
title: "Performing additional configuration on Capsule Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_capsule_server"
guide_title: "Installing Capsule Server"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#performing-additional-configuration-on-capsule-server_capsule"
---
# Chapter 3. Performing additional configuration on Capsule Server

If you plan to register hosts to Capsule Servers, configure your Capsule Servers to provide remote execution, lifecycle environments, and power management functionalities.

## 3.1. Configuring Capsule Server for host registration and provisioning

Configure Capsule Server to register and provision hosts through your Capsule Server instead of your Satellite Server.

**Procedure**

- On Satellite Server, add the Capsule to the list of trusted proxies.

  This is required for Satellite to recognize hosts' IP addresses forwarded over the `X-Forwarded-For` HTTP header set by Capsule. For security reasons, Satellite recognizes this HTTP header only from localhost by default. You can enter trusted proxies as valid IPv4 or IPv6 addresses of Capsules, or network ranges.

  > **Warning**
  >
  > Do not use a network range that is too broad because that might cause a security risk.

  Enter the following command. Note that the command overwrites the list that is currently stored in Satellite. Therefore, if you have set any trusted proxies previously, you must include them in the command as well:

  ```
  # satellite-installer \
  --foreman-trusted-proxies "127.0.0.1/8" \
  --foreman-trusted-proxies "::1" \
  --foreman-trusted-proxies "My_IP_address" \
  --foreman-trusted-proxies "My_IP_range"
  ```

  The localhost entries are required, do not omit them.

**Verification**

1. List the current trusted proxies using the full help of Satellite installer:

   ```
   # satellite-installer --full-help | grep -A 2 "trusted-proxies"
   ```
2. The current listing contains all trusted proxies you require.

## 3.2. Configuring pull-based transport for remote execution

By default, remote execution uses push-based SSH as the transport mechanism for the Script provider. If your infrastructure prohibits outgoing connections from Capsule Server to hosts, you can use remote execution with pull-based transport instead, because the host initiates the connection to Capsule Server. The use of pull-based transport is not limited to those infrastructures.

The pull-based transport comprises `pull-mqtt` mode on Capsules in combination with a pull client running on hosts.

> **Note**
>
> The `pull-mqtt` mode works only with the Script provider. Ansible and other providers will continue to use their default transport settings.

The mode is configured per Capsule Server. Some Capsule Servers can be configured to use `pull-mqtt` mode while others use SSH. If this is the case, it is possible that one remote job on a given host will use the pull client and the next job on the same host will use SSH. If you want to avoid this scenario, configure all Capsule Servers to use the same mode.

**Procedure**

1. Enable the pull-based transport on your Capsule Server:

   ```
   # satellite-installer --foreman-proxy-plugin-remote-execution-script-mode pull-mqtt
   ```
2. Configure the firewall to allow the MQTT service on port 1883:

   ```
   # firewall-cmd --add-service=mqtt
   ```
3. Make the changes persistent:

   ```
   # firewall-cmd --runtime-to-permanent
   ```
4. In `pull-mqtt` mode, hosts subscribe for job notifications to either your Satellite Server or any Capsule Server through which they are registered. Ensure that Satellite Server sends remote execution jobs to that same Satellite Server or Capsule Server:

   ```
   $ hammer settings set \
   --name remote_execution_prefer_registered_through_proxy \
   --value true
   ```

**Next steps**

- Configure your hosts for the pull-based transport. For more information, see [Transport modes for remote execution](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#transport-modes-for-remote-execution_managing-hosts) in *Managing hosts*.

## 3.3. Adding lifecycle environments to Capsule Servers by using Satellite web UI

To distribute content through content-enabled Capsule Server, add lifecycle environments to your Capsule Server. Capsule Server synchronizes the right repositories from Satellite Server and provides that content to hosts.

Do not assign the *Library* lifecycle environment to your Capsule Server because it triggers an automated Capsule sync every time the CDN updates a repository. This might consume multiple system resources on Capsules, network bandwidth between Satellite and Capsules, and available disk space on Capsules.

You can add an environment from the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
2. Select your Capsule Server that you want to add a lifecycle to.
3. Click **Edit** and click the **Lifecycle Environments** tab.
4. From the left menu, select the lifecycle environments that you want to add to your Capsule Server and click **Submit**.
5. To synchronize the content to your Capsule Server, click the **Overview** tab and click **Synchronize**.
6. Select either **Optimized Sync** or **Complete Sync**.

   For definitions of each synchronization type, see [Advanced synchronization options](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#advanced-synchronization-options).

## 3.4. Adding lifecycle environments to Capsule Servers by using Hammer CLI

To distribute content through content-enabled Capsule Server, add lifecycle environments to your Capsule Server. Capsule Server synchronizes the right repositories from Satellite Server and provides that content to hosts.

Do not assign the *Library* lifecycle environment to your Capsule Server because it triggers an automated Capsule sync every time the CDN updates a repository. This might consume multiple system resources on Capsules, network bandwidth between Satellite and Capsules, and available disk space on Capsules.

You can add an environment by using Hammer CLI.

**Procedure**

1. To display a list of all Capsule Servers, on Satellite Server, enter the following command:

   ```
   $ hammer capsule list
   ```

   Note the Capsule ID of the Capsule to which you want to add a lifecycle.
2. Using the ID, verify the details of your Capsule:

   ```
   $ hammer capsule info \
   --id My_Capsule_ID
   ```
3. To view the lifecycle environments available for your Capsule Server, enter the following command and note the ID and the organization name:

   ```
   $ hammer capsule content available-lifecycle-environments \
   --id My_Capsule_ID
   ```
4. Add the lifecycle environment to your Capsule Server:

   ```
   $ hammer capsule content add-lifecycle-environment \
   --id My_Capsule_ID \
   --lifecycle-environment-id My_Lifecycle_Environment_ID \
   --organization "My_Organization"
   ```

   Repeat for each lifecycle environment you want to add to Capsule Server.
5. Synchronize the content from Satellite to Capsule.

   - To synchronize all content from your Satellite Server environment to Capsule Server, enter the following command:

     ```
     $ hammer capsule content synchronize \
     --id My_Capsule_ID
     ```
   - To synchronize a specific lifecycle environment from your Satellite Server to Capsule Server, enter the following command:

     ```
     $ hammer capsule content synchronize \
     --id My_Capsule_ID \
     --lifecycle-environment-id My_Lifecycle_Environment_ID
     ```
   - To synchronize all content from your Satellite Server to your Capsule Server without checking metadata:

     ```
     $ hammer capsule content synchronize \
     --id My_Capsule_ID \
     --skip-metadata-check true
     ```

     This equals selecting **Complete Sync** in the Satellite web UI.

## 3.5. Enabling power management on hosts

Enable the baseboard management controller (BMC) module on Capsule Server to perform remote power management tasks on hosts, including power cycling and monitoring power states.

Red Hat Satellite supports the following BMC providers:

- `freeipmi`
- `ipmitool`
- `redfish`

**Prerequisites**

- Your host has a network interface of the BMC type. Capsule Server uses this NIC to pass credentials to the host.

**Procedure**

1. Enable the BMC module and select the default provider:

   ```
   # satellite-installer \
   --foreman-proxy-bmc "true" \
   --foreman-proxy-bmc-default-provider "freeipmi"
   ```
2. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
3. Select the subnet of your host.
4. On the **Capsules** tab, select your Capsule Server as **BMC Capsule**.
5. Click **Submit**.

**Next steps**

- Configure a BMC interface on your host. For more information, see [Configuring a baseboard management controller (BMC) interface](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-a-baseboard-management-controller-interface) in *Managing hosts*.
