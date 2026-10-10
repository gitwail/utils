---
title: "Performing additional configuration on Satellite Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_disconnected_network_environment"
guide_title: "Installing Satellite Server in a disconnected network environment"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#performing-additional-configuration-on-server_satellite"
---
# Chapter 5. Performing additional configuration on Satellite Server

You can enable additional features on Satellite Server, such as Red Hat Lightspeed integration or pull-based transport for remote execution. While you can configure these features after the initial setup, you can also configure many of them during the installation by using the corresponding `satellite-installer` options.

## 5.1. Installing and configuring Red Hat Lightspeed in Satellite

Red Hat Lightspeed in Satellite analyzes system health and configuration by applying predefined rules to a small set of local data, such as installed packages, running services, and configuration settings. When you install Red Hat Lightspeed in Satellite locally, you can generate Red Hat Lightspeed recommendations without sending system data to Red Hat services.

> **Important**
>
> - With Red Hat Lightspeed in Satellite enabled, you cannot use the hosted Red Hat Lightspeed services for hosts registered to your Satellite. Enabling Red Hat Lightspeed in Satellite prevents you from using any Red Hat Hybrid Cloud Console services on hosts registered to Satellite.
> - If you install Satellite with external databases, you cannot enable Red Hat Lightspeed in Satellite. Enabling Red Hat Lightspeed in Satellite prevents you from using external databases.
> - Podman must be configured to use the netavark network backend.

Red Hat Lightspeed in Satellite follows the standard lifecycle policy for Red Hat Satellite. To update Red Hat Lightspeed in Satellite, follow the standard update instructions for Satellite.

**Additional resources**

- [How to switch to netavark network backend in Podman in the Red Hat Knowledgebase](https://access.redhat.com/solutions/7055981)

### 5.1.1. Installing Red Hat Lightspeed in Satellite with the Satellite ISO image

You can use the Satellite installation ISO image to access the required container content.

**Prerequisites**

- `skopeo` is installed on your Satellite Server. For more information, see [Getting container tools](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/assembly_starting-with-containers_building-running-and-managing-containers#proc_getting-container-tools_assembly_starting-with-containers) in *Red Hat Enterprise Linux 9 Building, running, and managing containers*.
- Ensure that Podman is configured to use the netavark network backend. For more information, see [How to switch to netavark network backend in Podman in the Red Hat Knowledgebase](https://access.redhat.com/solutions/7055981).

**Procedure**

1. Download and mount the Satellite ISO image: For more information, see [Section 3.3, “Installing the Satellite packages from the offline repositories”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#installing-from-the-offline-repositories_satellite "3.3. Installing the Satellite packages from the offline repositories").
2. Set up the local repositories for disconnected environments. For more information, see [Section 3.3, “Installing the Satellite packages from the offline repositories”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#installing-from-the-offline-repositories_satellite "3.3. Installing the Satellite packages from the offline repositories").
3. Set up containers on your Satellite Server:

   ```
   # /media/sat6/setup_containers
   ```
4. Enable the plugin:

   ```
   # satellite-installer --enable-iop
   ```
5. Download and populate the Common Vulnerabilities and Exposures (CVE) mapping file:

   ```
   $ curl -o cvemap.xml https://security.access.redhat.com/data/meta/v1/cvemap.xml
   ```
6. Transfer the `cvemap.xml` file to your disconnected Satellite Server.
7. Copy the file to `/var/lib/foreman/`:

   ```
   # cp cvemap.xml /var/lib/foreman/
   ```

   Satellite detects the file and automatically publishes it to `/var/www/html/pub/iop/data/meta/v1/cvemap.xml`.

### 5.1.2. Installing Red Hat Lightspeed in Satellite by using export and import

You can transfer the container images from a connected system to a disconnected Satellite Server.

**Prerequisites**

- You have a connected system with access to the container registry.
- You have prepared a disconnected Satellite Server.
- Ensure that Podman is installed on both systems. For more information, see [Getting container tools](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/building_running_and_managing_containers/assembly_starting-with-containers_building-running-and-managing-containers#proc_getting-container-tools_assembly_starting-with-containers) in *Red Hat Enterprise Linux 9 Building, running, and managing containers*.
- Ensure that Podman on the disconnected Satellite Server is configured to use the netavark network backend. For more information, see [How to switch to netavark network backend in Podman in the Red Hat Knowledgebase](https://access.redhat.com/solutions/7055981).

**Procedure**

1. On the connected system, log in to the container registry:

   ```
   $ podman login --username My_Username --password My_Password registry.redhat.io
   ```
2. Export the container images. Save the following script to a file and execute it on the connected system:

   ```
   #!/bin/bash

   images=(
     "satellite/iop-ingress-rhel9:6.19"
     "satellite/iop-advisor-frontend-rhel9:6.19"
     "satellite/iop-host-inventory-rhel9:6.19"
     "satellite/iop-vmaas-rhel9:6.19"
     "satellite/iop-remediations-rhel9:6.19"
     "satellite/iop-vulnerability-frontend-rhel9:6.19"
     "satellite/iop-host-inventory-frontend-rhel9:6.19"
     "satellite/iop-advisor-backend-rhel9:6.19"
     "satellite/iop-puptoo-rhel9:6.19"
     "satellite/iop-yuptoo-rhel9:6.19"
     "satellite/iop-insights-engine-rhel9:6.19"
     "satellite/iop-vulnerability-engine-rhel9:6.19"
     "satellite/iop-gateway-rhel9:6.19"
     "amq-streams/kafka-39-rhel9:2.9.1-1"
   )

   for image in "${images[@]}"; do
     name=$(basename "${image}" | cut -d: -f1)
     image_url="registry.redhat.io/${image}"
     echo "Processing ${image}..."
     # Pull the image
     podman pull ${image_url}
     # Save image to archive
     podman save --output /tmp/${name}.tar ${image_url}
   done
   ```
3. Transfer the archive files to the disconnected Satellite Server. Place the archive files in the `/tmp` directory.
4. On the disconnected Satellite Server, import the container images. Save the following script to a file and execute it on the disconnected Satellite Server:

   ```
   #!/bin/bash

   images=(
     "satellite/iop-ingress-rhel9:6.19"
     "satellite/iop-advisor-frontend-rhel9:6.19"
     "satellite/iop-host-inventory-rhel9:6.19"
     "satellite/iop-vmaas-rhel9:6.19"
     "satellite/iop-remediations-rhel9:6.19"
     "satellite/iop-vulnerability-frontend-rhel9:6.19"
     "satellite/iop-host-inventory-frontend-rhel9:6.19"
     "satellite/iop-advisor-backend-rhel9:6.19"
     "satellite/iop-puptoo-rhel9:6.19"
     "satellite/iop-yuptoo-rhel9:6.19"
     "satellite/iop-insights-engine-rhel9:6.19"
     "satellite/iop-vulnerability-engine-rhel9:6.19"
     "satellite/iop-gateway-rhel9:6.19"
     "amq-streams/kafka-39-rhel9:2.9.1-1"
   )

   for image in "${images[@]}"; do
     name=$(basename "${image}" | cut -d: -f1)
     image_url="registry.redhat.io/${image}"
     echo "Processing ${image}..."
     # Import the image
     podman load --input /tmp/${name}.tar
   done
   ```
5. Enable the Red Hat Lightspeed in Satellite plugin:

   ```
   # satellite-installer --enable-iop
   ```

## 5.2. Configuring Satellite Server to consume content from a custom CDN by using Satellite web UI

Configure your Satellite Server to consume Red Hat repositories from a custom Content Delivery Network (CDN) server or web server instead of the Red Hat CDN. Satellite automatically recognizes which repositories from your subscription manifest are available on your CDN server.

**Prerequisites**

- You have a CDN server that provides Red Hat content and is accessible by Satellite Server.
- If your CDN server uses HTTPS, ensure you have uploaded the SSL certificate into Satellite. For more information, see [Importing Custom SSL Certificates](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-web-ui) in *Managing content*.
- You have uploaded a manifest to your organization.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Subscriptions**.
2. Click **Manage Manifest**.
3. Select the **CDN Configuration** tab.
4. Select the **Custom CDN** tab.
5. In the **URL** field, enter the URL of your CDN server from which you want Satellite Server to consume Red Hat repositories.
6. Optional: In the **SSL CA Content Credential**, select the SSL certificate of the CDN server.
7. Click **Update**.
8. Enable Red Hat repositories consumed from your internal CDN server.

## 5.3. Configuring Satellite Server to consume content from a custom CDN by using Hammer CLI

If you have an internal Content Delivery Network (CDN) or serve content on an accessible web server, you can configure your Satellite Server to consume Red Hat repositories from this CDN server instead of the Red Hat CDN. A CDN server can be any web server that mirrors repositories in the same directory structure as the Red Hat CDN.

You can configure the source of content for each organization. Satellite recognizes automatically which Red Hat repositories from the subscription manifest in your organization are available on your CDN server.

**Prerequisites**

- You have a CDN server that provides Red Hat content and is accessible by Satellite Server.
- If your CDN server uses HTTPS, ensure you have uploaded the SSL certificate into Satellite. For more information, see [Importing Custom SSL Certificates](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-web-ui) in *Managing content*.
- You have uploaded a manifest to your organization.

**Procedure**

1. Connect to your Satellite Server using SSH.
2. Set CDN configuration to your custom CDN server:

   ```
   $ hammer organization configure-cdn \
   --name="My_Organization" \
   --type=custom_cdn \
   --url https://my-cdn.example.com \
   --ssl-ca-credential-id "My_CDN_CA_Cert_ID"
   ```

## 5.4. Configuring Inter-Satellite Synchronization

Configure Inter-Satellite Synchronization on your disconnected Satellite Server to provide content in your disconnected network.

### 5.4.1. Inter-Satellite Synchronization configurations

Depending on network connectivity between upstream and downstream Satellite Servers, you can synchronize content over HTTPS with network sync or by exporting and importing content when servers are air gapped.

There are two possible ISS configurations of Satellite, depending on how you deployed your infrastructure:

ISS Network Sync
:   If your upstream server can communicate with the downstream server over a network, you can synchronize content over HTTPS.

    Configure your Satellite to synchronize content over a network.

ISS Export Sync
:   If your upstream and downstream servers are air gapped, you can synchronize content by using export and import.

    Configure your Satellite to synchronize content by using export and import.

**Additional resources**

- [Inter-Satellite Synchronization scenarios in *Overview, concepts, and deployment considerations*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#inter-satellite-synchronization-scenarios)
- [Hammer content export fails with "Path '/the/path' is not an allowed export path" in the *Red Hat Knowledgebase*](https://access.redhat.com/solutions/7013903)

### 5.4.2. Configuring Satellite Server to synchronize content through exports by using Satellite web UI

If you deployed your downstream Satellite Server as air gapped, configure your Satellite Server as such to avoid attempts to consume content from a network.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Subscriptions**.
2. Click **Manage Manifest**.
3. Switch to the **CDN Configuration** tab.
4. Select the **Export Sync** tab.
5. Click **Update**.

**Additional resources**

- [Content synchronization by using export and import in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-synchronization-by-using-export-and-import_content-management)

### 5.4.3. Configuring Satellite Server to synchronize content through exports by using Hammer CLI

If you deployed your downstream Satellite Server as air gapped, configure your Satellite Server as such to avoid attempts to consume content from a network.

**Procedure**

1. Log in to your Satellite Server by using SSH.
2. Set CDN configuration to sync by using exports:

   ```
   $ hammer organization configure-cdn \
   --name="My_Organization" \
   --type=export_sync
   ```

**Additional resources**

- [Content synchronization by using export and import in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-synchronization-by-using-export-and-import_content-management)

### 5.4.4. Configuring Satellite Server to synchronize content over a network by using Satellite web UI

To synchronize content over a network, configure your downstream Satellite Server to pull repositories from a connected upstream Satellite Server.

**Prerequisites**

- A network connection exists between the upstream Satellite Server and the downstream Satellite Server.
- You imported the same subscription manifest on both the upstream and downstream Satellite Server.
- On the upstream Satellite Server, you enabled the required repositories for the organization.
- The upstream user is an admin or has the following permissions:

  - `view_organizations`
  - `view_products`
  - `export_content`
  - `view_lifecycle_environments`
  - `view_content_views`
- On the downstream Satellite Server, you have imported the SSL certificate of the upstream Satellite Server using the contents of `http://upstream-satellite.example.com/pub/katello-server-ca.crt`.
- The downstream user is an admin or has the permissions to create product repositories and organizations.

**Procedure**

1. Navigate to **Content** > **Subscriptions**.
2. Click **Manage Manifest**.
3. Navigate to the **CDN Configuration** tab.
4. Select the **Network Sync** tab.
5. In the **URL** field, enter the address of the upstream Satellite Server.
6. In the **Username**, enter your username for upstream login.
7. In the **Password**, enter your password or personal access token for upstream login.
8. In the **Organization label** field, enter the label of the upstream organization.
9. Optional: In the **Lifecycle Environment Label** field, enter the label of the upstream lifecycle environment. Default is `Library`.
10. Optional: In the **Content view label** field, enter the label of the upstream content view. Default is `Default_Organization_View`.
11. From the **SSL CA Content Credential** menu, select a CA certificate used by the upstream Satellite Server.
12. Click **Update**.
13. In the Satellite web UI, navigate to **Content** > **Products**.
14. Select the product that contains the repositories that you want to synchronize.
15. From the **Select Action** menu, select **Sync Now** to synchronize all repositories within the product.

    You can also create a synchronization plan to ensure updates on a regular basis.

**Additional resources**

- [Section 3.9, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#importing-red-hat-subscription-manifests-into-satellite "3.9. Importing Red Hat subscription manifests into Satellite")
- [Enabling Red Hat repositories in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-web-ui)
- [Importing custom SSL certificates by using Satellite web UI in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-web-ui)
- [Creating a sync plan by using Satellite web UI in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-sync-plan-by-using-web-ui)

### 5.4.5. Configuring Satellite Server to synchronize content over a network by using Hammer CLI

To synchronize content over a network, configure your downstream Satellite Server to pull repositories from a connected upstream Satellite Server.

**Prerequisites**

- A network connection exists between the upstream Satellite Server and the downstream Satellite Server.
- You imported the same subscription manifest on both the upstream and downstream Satellite Server.
- On the upstream Satellite Server, you enabled the required repositories for the organization.
- The upstream user is an admin or has the following permissions:

  - `view_organizations`
  - `view_products`
  - `export_content`
  - `view_lifecycle_environments`
  - `view_content_views`
- On the downstream Satellite Server, you have imported the SSL certificate of the upstream Satellite Server using the contents of `http://upstream-satellite.example.com/pub/katello-server-ca.crt`.
- The downstream user is an admin or has the permissions to create product repositories and organizations.

**Procedure**

1. Connect to your downstream Satellite Server using SSH.
2. View information about the upstream CA certificate:

   ```
   $ hammer content-credential show \
   --name="My_Upstream_CA_Cert" \
   --organization="My_Downstream_Organization"
   ```

   Note the ID of the CA certificate for the next step.
3. Set CDN configuration to an upstream Satellite Server:

   ```
   $ hammer organization configure-cdn \
   --name="My_Downstream_Organization" \
   --type=network_sync \
   --url https://upstream-satellite.example.com \
   --username upstream_username --password upstream_password \
   --ssl-ca-credential-id "My_Upstream_CA_Cert_ID" \ --upstream-organization-label="_My_Upstream_Organization" \
   [--upstream-lifecycle-environment-label="My_Lifecycle_Environment"] \
   [--upstream-content-view-label="My_Content_View"]
   ```

   The default lifecycle environment label is `Library`. The default content view label is `Default_Organization_View`.

**Additional resources**

- [Section 3.9, “Importing Red Hat subscription manifests into Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#importing-red-hat-subscription-manifests-into-satellite "3.9. Importing Red Hat subscription manifests into Satellite")
- [Enabling Red Hat repositories in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-web-ui)
- [Importing custom SSL certificates by using Satellite web UI in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#importing-custom-ssl-certificates-by-using-web-ui)

## 5.5. Configuring pull-based transport for remote execution

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

## 5.6. Enabling power management on hosts

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

## 5.7. Configuring Satellite Server for outgoing emails

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

## 5.8. Configuring Satellite to manage the lifecycle of a host registered to a Identity Management realm

As well as providing access to Satellite Server, hosts provisioned with Satellite can also be integrated with Identity Management realms. Red Hat Satellite has a realm feature that automatically manages the lifecycle of any system registered to a realm or domain provider.

Use this section to configure Satellite Server or Capsule Server for Identity Management realm support, then add hosts to the Identity Management realm group.

### 5.8.1. Installing and configuring Identity Management packages on Satellite Server or Capsule Server

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

### 5.8.2. Configuring Satellite Server or Capsule Server for Identity Management realm support

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

### 5.8.3. Creating a realm for the Identity Management-enabled Capsule

After you configure your Capsule with Identity Management, you must create a realm and add the Identity Management-configured Capsule to the realm.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Realms** and click **Create Realm**.
2. In the **Name** field, enter a name for the realm.
3. From the **Realm Type** list, select the type of realm.
4. From the **Realm Capsule** list, select Capsule Server where you have configured Identity Management.
5. Click the **Locations** tab and from the **Locations** list, select the location where you want to add the new realm.
6. Click the **Organizations** tab and from the **Organizations** list, select the organization where you want to add the new realm.
7. Click **Submit**.

### 5.8.4. Updating host groups with realm information

You must update any host groups that you want to use with the new realm information.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. Select the host group that you want to update.
3. Select the **Network** tab.
4. From the **Realm** list, select the realm you create as part of this procedure.
5. Click **Submit**.

### 5.8.5. Adding hosts to a Identity Management host group

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

## 5.9. Configuring Satellite Server with a custom SSL certificate

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

### 5.9.1. Creating a custom SSL certificate for Satellite Server

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

### 5.9.2. Deploying a custom SSL certificate to Satellite Server

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

### 5.9.3. Deploying a custom SSL certificate to hosts

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

### 5.9.4. Deploying a custom SSL certificate to Capsule Servers

If you have Capsule Servers registered to Satellite, configure them with custom SSL certificates.

**Procedure**

- Follow the procedure in [Configuring Capsule Server with a Custom SSL Certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-capsule-custom-server-certificate_capsule) in *Installing Capsule Server*.
