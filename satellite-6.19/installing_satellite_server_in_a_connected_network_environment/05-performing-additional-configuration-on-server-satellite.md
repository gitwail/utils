---
title: "Performing additional configuration on Satellite Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_connected_network_environment"
guide_title: "Installing Satellite Server in a connected network environment"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#performing-additional-configuration-on-server_satellite"
---
# Chapter 5. Performing additional configuration on Satellite Server

You can enable additional features on Satellite Server, such as Red Hat Lightspeed integration, pull-based transport for remote execution, or the usage of HTTP proxies. While you can configure these features after the initial setup, you can also configure many of them during the installation by using the corresponding `satellite-installer` options.

## 5.1. Configuring Satellite Server as Red Hat Lightspeed client

You can use Red Hat Lightspeed to diagnose systems and downtime related to security exploits, performance degradation, and stability failures. You can use the dashboard to quickly identify key risks to stability, security, and performance. You can sort by category, view details of the impact and resolution, and then determine what systems are affected.

Note that you do not require a Red Hat Lightspeed entitlement in your subscription manifest.

To maintain your Satellite Server, and improve your ability to monitor and diagnose problems you might have with Satellite, install the `insights-client` tool on Satellite Server and register Satellite Server with Red Hat Lightspeed.

**Procedure**

1. Register Satellite Server with Red Hat Lightspeed:

   ```
   # satellite-installer --register-with-insights
   ```
2. Optional: You can change the default schedule for running `insights-client` by updating the system systemd settings and the `insights-client.timer` file on your Satellite Server.

**Verification**

- Check that the system is registered with Red Hat Lightspeed:

  ```
  # insights-client --status
  ```

**Next steps**

- If you want to unregister the system from Red Hat Lightspeed:

  ```
  # insights-client --unregister
  ```

**Additional resources**

- [Red Hat Lightspeed](https://access.redhat.com/products/red-hat-lightspeed)
- [Registering your system with Red Hat Lightspeed](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/client_configuration_guide_for_red_hat_lightspeed/assembly-client-configuring-insights-client#proc-registering-system-insights_insights-cg-configuring-client)
- [Changing the insights-client schedule](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/client_configuration_guide_for_red_hat_lightspeed/assembly-client-changing-schedule)
- [Unregistering your system with Red Hat Lightspeed](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/client_configuration_guide_for_red_hat_lightspeed/assembly-client-configuring-insights-client#proc-unregistering-system-insights_insights-cg-configuring-client)
- [Configuring insights-client](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/client_configuration_guide_for_red_hat_lightspeed/assembly-client-configuring-insights-client)

## 5.2. Installing and configuring Red Hat Lightspeed in Satellite

Red Hat Lightspeed in Satellite analyzes system health and configuration by applying predefined rules to a small set of local data, such as installed packages, running services, and configuration settings. When you install Red Hat Lightspeed in Satellite locally, you can generate Red Hat Lightspeed recommendations without sending system data to Red Hat services.

> **Important**
>
> - With Red Hat Lightspeed in Satellite enabled, you cannot use the hosted Red Hat Lightspeed services for hosts registered to your Satellite. Enabling Red Hat Lightspeed in Satellite prevents you from using any Red Hat Hybrid Cloud Console services on hosts registered to Satellite.
> - If you install Satellite with external databases, you cannot enable Red Hat Lightspeed in Satellite. Enabling Red Hat Lightspeed in Satellite prevents you from using external databases.
> - Podman must be configured to use the netavark network backend.

Red Hat Lightspeed in Satellite follows the standard lifecycle policy for Red Hat Satellite. To update Red Hat Lightspeed in Satellite, follow the standard update instructions for Satellite.

**Additional resources**

- [How to switch to netavark network backend in Podman in the Red Hat Knowledgebase](https://access.redhat.com/solutions/7055981)

### 5.2.1. Configuring Podman to use an HTTP proxy

If your Satellite Server connects to the internet through an HTTP proxy, configure Podman for connections through the same HTTP proxy.

**Prerequisites**

- Podman is installed. For more information, see [Getting container tools](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/assembly_starting-with-containers_building-running-and-managing-containers#proc_getting-container-tools_assembly_starting-with-containers) in *Red Hat Enterprise Linux 9 Building, running, and managing containers*.

**Procedure**

- Edit the `/etc/containers/containers.conf` file to include the following directives:

  ```
  [engine]
  env = ["https_proxy=https://http-proxy.example.com:port"]

  [containers]
  http_proxy=false
  ```

### 5.2.2. Installing Red Hat Lightspeed in Satellite on a connected Satellite Server

You can pull the Red Hat Lightspeed in Satellite from the Red Hat container registry if your Satellite Server has access to the registry.

**Prerequisites**

- Ensure that the Satellite Server has access to the Red Hat container registry.
- Ensure that Podman is installed. For more information, see [Getting container tools](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/assembly_starting-with-containers_building-running-and-managing-containers#proc_getting-container-tools_assembly_starting-with-containers) in *Red Hat Enterprise Linux 9 Building, running, and managing containers*.
- Ensure that Podman is configured to use the netavark network backend. For more information, see [How to switch to netavark network backend in Podman in the Red Hat Knowledgebase](https://access.redhat.com/solutions/7055981).

**Procedure**

1. Log in to the Red Hat registry by using Podman:

   ```
   # podman login --authfile /etc/foreman/registry-auth.json registry.redhat.io
   ```

   This command creates the `/etc/foreman/registry-auth.json` file.
2. Enable the plugin:

   ```
   # satellite-installer --enable-iop
   ```
3. If you want to use the Red Hat Lightspeed vulnerability service in Satellite and your Satellite Server connects to `https://security.access.redhat.com` through an HTTP proxy, configure the `iop-cvemap-download` service to use the same HTTP proxy:

   1. Edit the `iop-cvemap-download` service:

      ```
      # systemctl edit iop-cvemap-download.service
      ```
   2. Input the following content:

      ```
      [Service]
      Environment = HTTPS_PROXY=http://http-proxy.example.com:port
      Environment = NO_PROXY=localhost
      ```

## 5.3. Importing the Red Hat Satellite Client 6 repository

The Red Hat Satellite Client 6 repository provides essential client integration tools, such as `katello-host-tools`, that enable communication between hosts and Satellite. To use these tools, you must enable and synchronize the repository on Satellite Server, then enable it on your hosts. These tools are required for features like remote execution, package management, and host reporting.

### 5.3.1. Enabling the Red Hat Satellite Client 6 repository

Enable the Red Hat Satellite Client 6 repository for every major version of Red Hat Enterprise Linux that you intend to run on your hosts. After enabling a Red Hat repository, Satellite creates a product for this repository automatically.

**Prerequisites**

- Ensure that a subscription manifest has been imported to your organization.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Red Hat Repositories**.
2. Ensure that the **RPM** repository type is selected.
3. In the search field, type `name = "Red Hat Satellite Client 6"` and press **Enter**. Optionally, enable the **Recommended Repositories** filter to limit the results.
4. Click the name of the required repository to expand the repository set.
5. For the required architecture, click the **+** icon to enable the repository.

**Additional resources**

- [Section 3.7, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#importing-red-hat-subscription-manifests-into-satellite "3.7. Importing Red Hat subscription manifests into Satellite")

### 5.3.2. Synchronizing the Red Hat Satellite Client 6 repository

Synchronize the Red Hat Satellite Client 6 repository to import the content to your Satellite Server.

**Prerequisites**

- You have enabled the Red Hat Satellite Client 6 repository.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Sync Status**.
2. Click the arrow next to the required product to view available repositories.
3. Select the repositories you want to synchronize.
4. Click **Synchronize Now**.

**Next steps**

- You can create a sync plan to update the content regularly.

**Additional resources**

- [Creating a sync plan by using Satellite web UI in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-sync-plan-by-using-web-ui)

## 5.4. Configuring pull-based transport for remote execution

By default, remote execution uses push-based SSH as the transport mechanism for the Script provider. If your infrastructure prohibits outgoing connections from Satellite Server to hosts, you can use remote execution with pull-based transport instead, because the host initiates the connection to Satellite Server. The use of pull-based transport is not limited to those infrastructures.

The pull-based transport comprises `pull-mqtt` mode on Capsules in combination with a pull client running on hosts.

> **Note**
>
> The `pull-mqtt` mode works only with the Script provider. Ansible and other providers will continue to use their default transport settings.

**Procedure**

1. Enable the pull-based transport on your Satellite Server:

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

## 5.5. Configuring Satellite for UEFI HTTP boot provisioning in an IPv6 network

Use this procedure to configure Satellite to provision hosts in an IPv6 network with UEFI HTTP Boot provisioning.

**Prerequisites**

- Ensure that your clients can access DHCP and HTTP servers.
- Ensure that the UDP ports 67 and 68 are accessible by clients so clients can send DHCP requests and receive DHCP offers.
- Ensure that the TCP port 8000 is open for clients to download files and Kickstart templates from Satellite and Capsules.
- Ensure that the host provisioning interface subnet has an HTTP Boot Capsule, and Templates Capsule set. For more information, see [Adding a subnet to Satellite Server by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#adding-a-subnet-to-satellite-server-by-using-web-ui) in *Provisioning hosts*.
- In the Satellite web UI, navigate to **Administer** > **Settings** > **Provisioning** and ensure that the **Token duration** setting is not set to **0**. Satellite cannot identify clients that are booting from the network by a remote IPv6 address because of unmanaged DHCPv6 service, therefore provisioning tokens must be enabled.

**Procedure**

1. You must disable DHCP management in the installer or not use it.
2. For all IPv6 subnets created in Satellite, set the **DHCP Capsule** to blank.
3. Optional: If the host and the DHCP server are separated by a router, configure the DHCP relay agent and point to the DHCP server.

## 5.6. Configuring Satellite Server to use an HTTP proxy

Configure Satellite Server to use an HTTP proxy if your environment uses an HTTP proxy to connect to the internet.

### 5.6.1. Adding a default HTTP proxy by using Satellite web UI

If your network uses an HTTP proxy, you can configure Satellite Server to use an HTTP proxy for requests to the Red Hat Content Delivery Network (CDN) or another content source. Use the FQDN instead of the IP address where possible to avoid losing connectivity because of network changes.

The following procedure configures an HTTP proxy only for downloading content for Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **HTTP Proxies**.
2. Click **New HTTP Proxy**.
3. In the **Name** field, enter the name for the HTTP proxy.
4. In the **Url** field, enter the URL of the HTTP proxy in the following format: `https://http-proxy.example.com:8080`.
5. Optional: If authentication is required, in the **Username** field, enter the username to authenticate with.
6. Optional: If authentication is required, in the **Password** field, enter the password to authenticate with.
7. To test connection to the proxy, click **Test Connection**.
8. Select the **Default content HTTP proxy** option to set the new HTTP proxy as default for content synchronization.
9. Click **Submit**.

### 5.6.2. Adding a default HTTP proxy by using Hammer CLI

If your network uses an HTTP proxy, you can configure Satellite Server to use an HTTP proxy for requests to the Red Hat Content Delivery Network (CDN) or another content source. Use the FQDN instead of the IP address where possible to avoid losing connectivity because of network changes.

The following procedure configures an HTTP proxy only for downloading content for Satellite.

**Procedure**

1. Verify that the `http_proxy`, `https_proxy`, and `no_proxy` variables are not set:

   ```
   # unset http_proxy https_proxy no_proxy
   ```
2. Add an HTTP proxy entry to Satellite and set the HTTP proxy as default for content synchronization:

   ```
   $ hammer http-proxy create \
   --name=My_HTTP_Proxy \
   --username=My_HTTP_Proxy_User_Name \
   --password=My_HTTP_Proxy_Password \
   --url http://http-proxy.example.com:8080 \
   --content-default-http-proxy true
   ```

### 5.6.3. Configuring SELinux to ensure access to Satellite on custom ports

SELinux ensures access of Red Hat Satellite and Subscription Manager only to specific ports. In the case of the HTTP cache, the TCP ports are 8080, 8118, 8123, and 10001 – 10010. If you use a port that does not have SELinux type `http_cache_port_t`, complete the following steps.

**Procedure**

1. On Satellite, to verify the ports that are permitted by SELinux for the HTTP cache, enter a command as follows:

   ```
   # semanage port -l | grep http_cache
   http_cache_port_t       tcp    8080, 8118, 8123, 10001-10010
   [output truncated]
   ```
2. To configure SELinux to permit a port for the HTTP cache, for example 8088, enter a command as follows:

   ```
   # semanage port -a -t http_cache_port_t -p tcp 8088
   ```

### 5.6.4. Using an HTTP proxy for all Satellite HTTP requests by using Satellite web UI

If your Satellite Server must remain behind a firewall that blocks HTTP and HTTPS, you can configure an HTTP proxy for communication with external systems, including compute resources, by using the Satellite web UI.

Note that if you are using compute resources for provisioning, and you want to use a different HTTP proxy with the compute resources, the HTTP proxy that you set for all Satellite communication takes precedence over the HTTP proxies that you set for compute resources.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. In the **HTTP(S) proxy** row, select the adjacent **Value** column and enter the proxy URL.
3. Click the tick icon to save your changes.

### 5.6.5. Using an HTTP proxy for all Satellite HTTP requests by using Hammer CLI

If your Satellite Server must remain behind a firewall that blocks HTTP and HTTPS, you can configure an HTTP proxy for communication with external systems, including compute resources, by using Hammer CLI.

Note that if you are using compute resources for provisioning, and you want to use a different HTTP proxy with the compute resources, the HTTP proxy that you set for all Satellite communication takes precedence over the HTTP proxies that you set for compute resources.

**Procedure**

- Use an HTTP proxy:

  ```
  $ hammer settings set --name=http_proxy --value=My_HTTP_Proxy_URL
  ```

### 5.6.6. Excluding hosts from receiving proxied requests by using Satellite web UI

If you use an HTTP proxy for all Satellite HTTP or HTTPS requests, you can prevent certain hosts from communicating through the HTTP proxy.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. In the **HTTP(S) proxy except hosts** row, select the adjacent **Value** column and enter the names of one or more hosts that you want to exclude from proxy requests.
3. Click the tick icon to save your changes.

### 5.6.7. Excluding hosts from receiving proxied requests by using Hammer CLI

If you use an HTTP proxy for all Satellite HTTP or HTTPS requests, you can prevent certain hosts from communicating through the HTTP proxy.

**Procedure**

- Enter the following command:

  ```
  $ hammer settings set --name=http_proxy_except_list --value=[hostname1.hostname2...]
  ```

### 5.6.8. Resetting the HTTP proxy by using Satellite web UI

If you want to reset the current HTTP proxy setting, unset the **Default HTTP Proxy** setting.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**, and click the **Content** tab.
2. Set the **Default HTTP Proxy** setting to **no global default**.

### 5.6.9. Resetting the HTTP proxy by using Hammer CLI

If you want to reset the current HTTP proxy setting, unset the **Default HTTP Proxy** setting.

**Procedure**

- Set the `content_default_http_proxy` setting to an empty string:

  ```
  $ hammer settings set --name=content_default_http_proxy --value=""
  ```

## 5.7. Enabling power management on hosts

Enable the baseboard management controller (BMC) module on Satellite Server to perform remote power management tasks on hosts, including power cycling and monitoring power states.

Red Hat Satellite supports the following BMC providers:

- `freeipmi`
- `ipmitool`
- `redfish`

**Prerequisites**

- Your host has a network interface of the BMC type. Satellite Server uses this NIC to pass credentials to the host.

**Procedure**

1. Enable the BMC module and select the default provider:

   ```
   # satellite-installer \
   --foreman-proxy-bmc "true" \
   --foreman-proxy-bmc-default-provider "freeipmi"
   ```
2. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
3. Select the subnet of your host.
4. On the **Capsules** tab, select your Satellite Server as **BMC Capsule**.
5. Click **Submit**.

**Next steps**

- Configure a BMC interface on your host. For more information, see [Configuring a baseboard management controller (BMC) interface](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-a-baseboard-management-controller-interface) in *Managing hosts*.

## 5.8. Configuring Satellite Server for outgoing emails

To send email messages from Satellite Server, you can use an SMTP server or the `sendmail` command.

> **Important**
>
> The `sendmail` command is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Use an SMTP service instead.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

> **Note**
>
> Some SMTP servers with anti-spam protection or greylisting features are known to cause problems. To set up outgoing email with such a service, install and configure an SMTP service on Satellite Server for relay or use the `sendmail` command.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Click the **Email** tab and set the configuration options to match your preferred delivery method. The changes have an immediate effect.

   - The following example shows the configuration options for using an SMTP server:

     Table 5.1. Using an SMTP server as a delivery method

     | Name | Example value | Additional information |
     | --- | --- | --- |
     | Delivery method | SMTP |  |
     | SMTP address | *smtp.example.com* |  |
     | SMTP authentication | login |  |
     | SMTP HELO/EHLO domain | *example.com* |  |
     | SMTP password | *password* | Use the login credentials for the SMTP server. |
     | SMTP port | 25 |  |
     | SMTP username | *user@example.com* | Use the login credentials for the SMTP server. |
   - The following example uses **gmail.com** as an SMTP server:

     Table 5.2. Using gmail.com as an SMTP server

     | Name | Example value | Additional information |
     | --- | --- | --- |
     | Delivery method | SMTP |  |
     | SMTP address | smtp.gmail.com |  |
     | SMTP authentication | plain |  |
     | SMTP HELO/EHLO domain | smtp.gmail.com |  |
     | SMTP enable StartTLS auto | Yes |  |
     | SMTP password | *app password* | Use the Google app password. For more information, see [Sign in with app passwords](https://support.google.com/mail/answer/185833) in *Google Help Center*. |
     | SMTP port | 587 |  |
     | SMTP username | *user*@gmail.com | Use the Google account name. |
   - The following example uses the `sendmail` command as a delivery method:

     Table 5.3. Using sendmail as a delivery method

     | Name | Example value | Additional information |
     | --- | --- | --- |
     | Delivery method | Sendmail |  |
     | Sendmail location | /usr/sbin/sendmail | For security reasons, both Sendmail location and Sendmail argument settings are read-only and can be only set in `/etc/foreman/settings.yaml`. Both settings currently cannot be set via `satellite-installer`. For more information see the **sendmail 1** man page. |
     | Sendmail arguments | -i |
3. To send email by using an SMTP server that uses TLS authentication, also perform one of the following steps:

   - Mark the CA certificate of the SMTP server as trusted. To do so, execute the following commands on Satellite Server:

     ```
     # cp mailca.crt /etc/pki/ca-trust/source/anchors/
     # update-ca-trust extract
     ```

     Where `mailca.crt` is the CA certificate of the SMTP server.
   - Alternatively, in the Satellite web UI, set the `SMTP enable StartTLS auto` option to `No`.
4. Click **Test email** to send a test message to the user’s email address to confirm the configuration is working. If a message fails to send, the Satellite web UI displays an error. See the log at `/var/log/foreman/production.log` for further details.

**Additional resources**

- [Configuring email notification preferences in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Configuring_Email_Notification_Preferences_admin)

## 5.9. Configuring Satellite to manage the lifecycle of a host registered to a Identity Management realm

As well as providing access to Satellite Server, hosts provisioned with Satellite can also be integrated with Identity Management realms. Red Hat Satellite has a realm feature that automatically manages the lifecycle of any system registered to a realm or domain provider.

Use this section to configure Satellite Server or Capsule Server for Identity Management realm support, then add hosts to the Identity Management realm group.

### 5.9.1. Installing and configuring Identity Management packages on Satellite Server or Capsule Server

To use Identity Management for provisioned hosts, complete the following steps to install and configure Identity Management packages on Satellite Server or Capsule Server:

**Procedure**

1. Install the `ipa-client` package on Satellite Server or Capsule Server:

   ```
   # satellite-maintain packages install ipa-client
   ```
2. Configure the server as a Identity Management client:

   ```
   # ipa-client-install
   ```
3. Create a realm proxy user, `realm-capsule`, and the relevant roles in Identity Management:

   ```
   # foreman-prepare-realm admin realm-capsule
   ```

   Note the principal name that returns and your Identity Management server configuration details because you require them for the following procedure.

### 5.9.2. Configuring Satellite Server or Capsule Server for Identity Management realm support

Complete the following procedure on your Satellite Server and every Capsule Server that you want to use.

**Procedure**

1. Copy the `/root/freeipa.keytab` file to any Capsule Server that you want to include in the same principal and realm:

   ```
   # scp /root/freeipa.keytab root@capsule.example.com:/etc/foreman-proxy/freeipa.keytab
   ```
2. On your Satellite Server, move the `/root/freeipa.keytab` file to the `/etc/foreman-proxy` directory:

   ```
   # mv /root/freeipa.keytab /etc/foreman-proxy
   ```
3. On your Satellite Server and Capsule Servers, set ownership to the `foreman-proxy` user and group:

   ```
   # chown foreman-proxy:foreman-proxy /etc/foreman-proxy/freeipa.keytab
   ```
4. Enter the following command on all Capsules that you want to include in the realm. If you use the integrated Capsule on Satellite, enter this command on Satellite Server:

   ```
   # satellite-installer --foreman-proxy-realm true \
   --foreman-proxy-realm-keytab /etc/foreman-proxy/freeipa.keytab \
   --foreman-proxy-realm-principal realm-capsule@EXAMPLE.COM \
   --foreman-proxy-realm-provider freeipa
   ```

   You can also use these options when you first configure the Satellite Server.
5. Ensure that the most updated versions of the ca-certificates package is installed and trust the Identity Management Certificate Authority:

   ```
   # cp /etc/ipa/ca.crt /etc/pki/ca-trust/source/anchors/ipa.crt
   # update-ca-trust extract
   ```
6. Optional: If you configure Identity Management on an existing Satellite Server or Capsule Server, complete the following steps to ensure that the configuration changes take effect:

   1. Restart the **foreman-proxy** service:

      ```
      # systemctl restart foreman-proxy
      ```
   2. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
   3. Locate the Capsule you have configured for Identity Management and from the list in the **Actions** column, select **Refresh**.

### 5.9.3. Creating a realm for the Identity Management-enabled Capsule

After you configure your Capsule with Identity Management, you must create a realm and add the Identity Management-configured Capsule to the realm.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Realms** and click **Create Realm**.
2. In the **Name** field, enter a name for the realm.
3. From the **Realm Type** list, select the type of realm.
4. From the **Realm Capsule** list, select Capsule Server where you have configured Identity Management.
5. Click the **Locations** tab and from the **Locations** list, select the location where you want to add the new realm.
6. Click the **Organizations** tab and from the **Organizations** list, select the organization where you want to add the new realm.
7. Click **Submit**.

### 5.9.4. Updating host groups with realm information

You must update any host groups that you want to use with the new realm information.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. Select the host group that you want to update.
3. Select the **Network** tab.
4. From the **Realm** list, select the realm you create as part of this procedure.
5. Click **Submit**.

### 5.9.5. Adding hosts to a Identity Management host group

Identity Management supports the ability to set up automatic membership rules based on a system’s attributes. Red Hat Satellite’s realm feature provides administrators with the ability to map the Red Hat Satellite host groups to the Identity Management parameter `userclass` which allow administrators to configure automembership.

When nested host groups are used, they are sent to the Identity Management server as they are displayed in the Red Hat Satellite User Interface. For example, `Parent/Child/Child`.

Satellite Server or Capsule Server sends updates to the Identity Management server, however automembership rules are only applied at initial registration.

**Procedure**

1. On the Identity Management server, create a host group:

   ```
   # ipa hostgroup-add hostgroup_name --desc=hostgroup_description
   ```
2. Create an `automembership` rule:

   ```
   # ipa automember-add --type=hostgroup hostgroup_name automember_rule
   ```

   Where you can use the following options:

   - `automember-add` flags the group as an automember group.
   - `--type=hostgroup` identifies that the target group is a host group, not a user group.
   - `automember_rule` adds the name you want to identify the automember rule by.
3. Define an automembership condition based on the `userclass` attribute:

   ```
   # ipa automember-add-condition --key=userclass --type=hostgroup --inclusive-regex=^webserver hostgroup_name
   ----------------------------------
   Added condition(s) to "hostgroup_name"
   ----------------------------------
   Automember Rule: automember_rule
   Inclusive Regex: userclass=^webserver
   ----------------------------
   Number of conditions added 1
   ----------------------------
   ```

   Where you can use the following options:

   - `automember-add-condition` adds regular expression conditions to identify group members.
   - `--key=userclass` specifies the key attribute as `userclass`.
   - `--type=hostgroup` identifies that the target group is a host group, not a user group.
   - `--inclusive-regex=` *^webserver* identifies matching values with a regular expression pattern.
   - *hostgroup_name* – identifies the target host group’s name.

     > **Note**
     >
     > When a system is added to Satellite Server’s *hostgroup_name* host group, it is added automatically to the Identity Management server’s "*hostgroup_name*" host group. Identity Management host groups allow for Host-Based Access Controls (HBAC), sudo policies and other Identity Management functions.

## 5.10. Configuring an alternate CNAME for Satellite

You can configure an alternate CNAME for Satellite. This might be useful if you want to deploy the Satellite web interface on a different domain name than the one that is used by client systems to connect to Satellite. You must plan the alternate CNAME configuration in advance prior to installing Capsules and registering hosts to Satellite to avoid redeploying new certificates to hosts.

### 5.10.1. Configuring Satellite with an alternate CNAME

Use this procedure to configure Satellite with an alternate CNAME. Note that the procedures for users of a default Satellite certificate and custom certificate differ.

**Procedure**

1. If you have installed Satellite with a default Satellite certificate and want to configure Satellite with an alternate CNAME, generate a new default Satellite SSL certificate with an additional CNAME on Satellite Server:

   ```
   # satellite-installer --certs-cname alternate_fqdn --certs-update-server
   ```
2. If you have not installed Satellite, you can add the `--certs-cname alternate_fqdn` option to the `satellite-installer` command to install Satellite with an alternate CNAME.
3. If you use Satellite with a custom certificate, when creating a custom certificate, include the alternate CNAME records to the custom certificate. For more information, see [Creating a Custom SSL Certificate for Satellite Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#creating-a-custom-ssl-certificate_satellite).

### 5.10.2. Configuring hosts to use an alternate Satellite CNAME for content management

If Satellite is configured with an alternate CNAME, you can configure hosts to use the alternate Satellite CNAME for content management. To do this, you must point hosts to the alternate Satellite CNAME prior to registering the hosts to Satellite. You can do this using the bootstrap script or manually.

Perform these steps on the hosts you want to configure.

**Procedure**

- If you want to configure the host with the bootstrap script, run the bootstrap script with the `--server My-Alternate-FQDN.example.com` option to register the host to the alternate Satellite CNAME:

  ```
  # ./bootstrap.py --server My-Alternate-FQDN.example.com
  ```
- If you want to configure the host manually, edit the `/etc/rhsm/rhsm.conf` file to update `hostname` and `baseurl` settings to point to the alternate host name, for example:

  ```
  [server]
  # Server hostname:
  hostname = My-Alternate-FQDN.example.com

  content omitted

  [rhsm]
  # Content base URL:
  baseurl=https://My-Alternate-FQDN.example.com/pulp/content/
  ```

**Next steps**

- Now you can register the host with the `subscription-manager`.

## 5.11. Configuring Satellite Server with a custom SSL certificate

By default, Red Hat Satellite uses a self-signed SSL certificate to enable encrypted communications between Satellite Server, Capsule Servers, and all hosts. If you cannot use a Satellite self-signed certificate, you can configure Satellite Server to use an SSL certificate signed by an external certificate authority (CA).

When you configure Red Hat Satellite with custom SSL certificates, you must fulfill the following requirements:

- You must use the privacy-enhanced mail (PEM) encoding for the SSL certificates.
- You must not use the same SSL certificate for both Satellite Server and Capsule Server.
- The same CA must sign certificates for Satellite Server and Capsule Server.
- An SSL certificate must not also be a CA certificate.
- An SSL certificate must include a subject alt name (SAN) entry that matches the common name (CN).
- An SSL certificate must be allowed for Key Encipherment using a Key Usage extension.
- An SSL certificate must not have a shortname as the CN.
- You must not set a passphrase for the private key.
- If you use a certificate signed by an intermediate CA, you must provide the full chain of certificates. Your certificate must start with the Root CA, contain one or more intermediate CAs, and end with your server certificate.

### 5.11.1. Creating a custom SSL certificate for Satellite Server

Use this procedure to create a custom SSL certificate for Satellite Server. If you already have a custom SSL certificate for Satellite Server, skip this procedure.

**Procedure**

1. To store all the source certificate files, create a directory that is accessible only to the `root` user:

   ```
   # mkdir /root/satellite_cert
   ```
2. Create a private key with which to sign the certificate signing request (CSR). The private key must be unencrypted:

   ```
   # openssl genrsa -out /root/satellite_cert/satellite_cert_key.pem 4096
   ```

   If you already have a private key, skip this step.
3. Optional: Verify that the key is unencrypted:

   ```
   # openssl pkey -noout -in /root/satellite_cert/satellite_cert_key.pem
   ```

   If the command does not ask for a password, the key is unencrypted. If your private key is password-protected, remove the password.
4. Create the `/root/satellite_cert/openssl.cnf` configuration file for the CSR and include the following content:

   ```
   [ req ]
   req_extensions = v3_req
   distinguished_name = req_distinguished_name
   prompt = no

   [ req_distinguished_name ]
   commonName = satellite.example.com

   [ v3_req ]
   basicConstraints = CA:FALSE
   keyUsage = digitalSignature, keyEncipherment
   extendedKeyUsage = serverAuth, clientAuth
   subjectAltName = @alt_names

   [ alt_names ]
   DNS.1 = satellite.example.com
   ```

   For more information about the `[ v3_req ]` parameters and their purpose, see [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://www.rfc-editor.org/rfc/rfc5280).
5. Optional: If you want to add Distinguished Name (DN) details to the CSR, add the following information to the `[ req_distinguished_name ]` section:

   ```
   [req_distinguished_name]
   CN = satellite.example.com
   countryName = My_Country_Name
   stateOrProvinceName = My_State_Or_Province_Name
   localityName = My_Locality_Name
   organizationName = My_Organization_Or_Company_Name
   organizationalUnitName = My_Organizational_Unit_Name
   ```

   The options used in the configuration file include the following:

   `countryName`
   :   The country represented by a two-letter code

   `stateOrProvinceName`
   :   Full name of the state or province

   `localityName`
   :   Full name of the locality (example: New York)

   `organizationalUnitName`
   :   Division responsible for the certificate (example: IT department)
6. Generate the CSR:

   ```
   # openssl req -new \
   -key /root/satellite_cert/satellite_cert_key.pem \
   -config /root/satellite_cert/openssl.cnf \
   -out /root/satellite_cert/satellite_cert_csr.pem
   ```

   The options used in the configuration file include the following:

   `-key`
   :   Path to the private key

   `-config`
   :   Path to the configuration file

   `-out`
   :   Path to the CSR to generate
7. Send the certificate signing request to the certificate authority (CA). The same CA must sign certificates for Satellite Server and Capsule Server.

   When you submit the request, specify the lifespan of the certificate. The method for sending the certificate request varies, so consult the CA for the preferred method. In response to the request, you can expect to receive a CA bundle and a signed certificate, in separate files.

### 5.11.2. Deploying a custom SSL certificate to Satellite Server

Use this procedure to configure your Satellite Server to use a custom SSL certificate signed by a Certificate Authority.

> **Important**
>
> Do not store the SSL certificates or .tar bundles in `/tmp` or `/var/tmp` directory. The operating system removes files from these directories periodically. As a result, `satellite-installer` fails to execute while enabling features or upgrading Satellite Server.

**Procedure**

- Update certificates on your Satellite Server:

  ```
  # satellite-installer \
  --certs-server-cert "/root/satellite_cert/satellite_cert.pem" \
  --certs-server-key "/root/satellite_cert/satellite_cert_key.pem" \
  --certs-server-ca-cert "/root/satellite_cert/ca_cert_bundle.pem" \
  --certs-update-server --certs-update-server-ca
  ```

  The options used in the command include the following:

  `--certs-server-cert`
  :   Path to Satellite Server certificate file that is signed by a Certificate Authority

  `--certs-server-key`
  :   Path to the private key that was used to sign Satellite Server certificate

  `--certs-server-ca-cert`
  :   Path to the Certificate Authority bundle

**Verification**

1. On a computer with network access to Satellite Server, navigate to the following URL: `https://satellite.example.com`.
2. In your browser, view the certificate details to verify the deployed certificate.

**Next steps**

- After you configure Satellite Server to use a custom SSL certificate, you must refresh the self-signed CA certificate on registered hosts. For more information, see [Refreshing the self-signed CA certificate on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#refreshing-the-self-signed-ca-certificate-on-hosts) in *Managing hosts*.

### 5.11.3. Deploying a custom SSL certificate to hosts

After you configure Satellite to use a custom SSL certificate, you must deploy the certificate to hosts registered to Satellite.

> **Important**
>
> The `katello-ca-consumer` RPM package and `katello-rhsm-consumer` script is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Use refreshing the self-signed CA certificate on hosts instead.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

**Procedure**

- Update the SSL certificate on each host:

  ```
  # dnf install http://satellite.example.com/pub/katello-ca-consumer-latest.noarch.rpm
  ```

**Additional resources**

- [Refreshing the self-signed CA certificate on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#refreshing-the-self-signed-ca-certificate-on-hosts)

### 5.11.4. Deploying a custom SSL certificate to Capsule Servers

If you have Capsule Servers registered to Satellite, configure them with custom SSL certificates.

**Procedure**

- Follow the procedure in [Configuring Capsule Server with a Custom SSL Certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-capsule-custom-server-certificate_capsule) in *Installing Capsule Server*.

## 5.12. Resetting custom SSL certificate to default self-signed certificate on Satellite Server

If you want to revert to the default configuration, you can reset a custom SSL certificate to the default self-signed certificate on your Satellite Server.

**Procedure**

- Reset the custom SSL certificate to default self-signed certificate:

  ```
  # satellite-installer --certs-reset
  ```

**Verification**

Verify that the following parameters in `/etc/foreman-installer/scenarios.d/satellite-answers.yaml` have no values:

- server_cert:
- server_key:
- server_cert_req:
- server_ca_cert:

**Additional resources**

- [Resetting custom SSL certificate to default self-signed certificate on Capsule Server in *Installing Capsule Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#resetting-custom-ssl-certificate-to-default-self-signed-certificate-on-capsule_capsule)
- [Resetting custom SSL certificate to default self-signed certificate on hosts in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#resetting-custom-ssl-certificate-to-default-self-signed-certificate-on-hosts_managing-hosts)
