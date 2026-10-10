---
title: "Installing Satellite Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_connected_network_environment"
guide_title: "Installing Satellite Server in a connected network environment"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#installing-satellite-server"
---
# Chapter 3. Installing Satellite Server

Use the following procedures to install Satellite Server in a connected environment, perform the initial configuration, and import subscription manifests.

When you install Satellite Server from a connected network, you can obtain packages and receive updates directly from the Red Hat Content Delivery Network.

> **Note**
>
> You cannot register Satellite Server to itself.

## 3.1. Configuring the HTTP proxy to connect to Red Hat CDN

You can configure an HTTP proxy to connect to Red Hat CDN when your network requires proxy access for subscription management and content delivery.

**Prerequisites**

- Your network gateway and the HTTP proxy must allow access to the following hosts:

  | Host name | Port | Protocol |
  | --- | --- | --- |
  | subscription.rhsm.redhat.com | 443 | HTTPS |
  | cdn.redhat.com | 443 | HTTPS |
  | cert.console.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | api.access.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | cert-api.access.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | console.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | connect.cloud.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | *.akamaiedge.net (if using Red Hat Lightspeed in Satellite) | 443 | HTTPS |

**Procedure**

- On Satellite Server, complete the following details in the `/etc/rhsm/rhsm.conf` file:

  ```
  # an http proxy server to use (enter server FQDN)
  proxy_hostname = http-proxy.example.com

  # port for http proxy server
  proxy_port = 8080

  # user name for authenticating to an http proxy, if needed
  proxy_user =

  # password for basic http proxy auth, if needed
  proxy_password =
  ```

**Additional resources**

- [Public CIDR Lists for Red Hat in the *Red Hat Knowledgebase*](https://access.redhat.com/articles/1525183)

## 3.2. Registering to Red Hat Subscription Management

Registering the host to Red Hat Subscription Management enables the host to subscribe to and consume content for any subscriptions available to the user. This includes content such as Red Hat Enterprise Linux and Red Hat Satellite.

**Procedure**

- Register your system with the Red Hat Content Delivery Network, entering your Customer Portal user name and password when prompted:

  ```
  # subscription-manager register
  ```

  The command displays output similar to the following:

  ```
  # subscription-manager register
  Username: user_name
  Password:
  The system has been registered with ID: 541084ff2-44cab-4eb1-9fa1-7683431bcf9a
  ```

## 3.3. Configuring repositories

Enable the necessary repositories on your Satellite host to access installation packages and dependencies.

**Procedure**

1. Disable all repositories:

   ```
   # subscription-manager repos --disable "*"
   ```
2. Enable the following repositories:

   ```
   # subscription-manager repos \
   --enable=rhel-9-for-x86_64-baseos-rpms \
   --enable=rhel-9-for-x86_64-appstream-rpms \
   --enable=satellite-6.19-for-rhel-9-x86_64-rpms \
   --enable=satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```

**Verification**

- Verify that the required repositories are enabled:

  ```
  # dnf repolist enabled
  ```

## 3.4. Considerations for using the satellite-installer utility

The satellite-installer utility is a collection of Puppet modules. Before using it to install Satellite Server, consider that installations can take tens of minutes and that repeated runs might overwrite manual configuration changes.

Installation duration
:   The installation process can take tens of minutes to complete. If you are connecting remotely to the system, use a utility such as `tmux` that allows suspending and reattaching a communication session so that you can check the installation progress in case you become disconnected from the remote system. If you lose connection to the shell where the installation command is running, see the log at `/var/log/foreman-installer/satellite.log` to determine if the process completed successfully.

Avoiding configuration overwrites
:   The Satellite installation script is based on Puppet, which means that if you run the installation script more than once, it might overwrite any manual configuration changes.

    To avoid this and determine which future changes apply, use the `--noop` argument when you run the installation script. This argument ensures that no actual changes are made. Potential changes are written to `/var/log/foreman-installer/satellite.log`.

    Files are always backed up and so you can revert any unwanted changes. For example, in the logs of `foreman-installer`, you can see an entry similar to the following about Filebucket:

    ```
    /Stage[main]/Dhcp/File[/etc/dhcp/dhcpd.conf]: Filebucketed /etc/dhcp/dhcpd.conf to puppet with sum 622d9820b8e764ab124367c68f5fa3a1
    ```

    You can restore the previous file as follows:

    ```
    # puppet filebucket -l \
    restore /etc/dhcp/dhcpd.conf 622d9820b8e764ab124367c68f5fa3a1
    ```

Installer help options
:   - Use the `satellite-installer --scenario satellite --help` command to display the most commonly used options and any default values.
    - Use the `satellite-installer --scenario satellite --full-help` command to display advanced options.

## 3.5. Installing Satellite Server packages

Ensure the packages required for Satellite Server installation are available on your system.

**Procedure**

1. Upgrade all packages:

   ```
   # dnf upgrade
   ```
2. Install the packages:

   ```
   # dnf install satellite
   ```

## 3.6. Configuring Satellite Server

You can use the `satellite-installer` installation script to configure the Satellite Server with the default local database or an external PostgreSQL server. The command options override the corresponding default initial configuration options and are recorded in the Satellite answer file.

> **Note**
>
> By default, all configuration files configured by the installer are managed. When `satellite-installer` runs, it overwrites any manual changes to the managed files with the intended values. This means that running the installer on a broken system should restore it to working order, regardless of changes made. For more information on how to apply custom configuration on other services, see [Applying Custom Configuration to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#applying-custom-configuration_satellite).

**Prerequisites**

- If you want to use an external PostgreSQL database with your Satellite Server, you have prepared a PostgreSQL server with the required databases and user permissions. For more information, see [Section 2.3, “Preparing Satellite for using external databases”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#preparing-for-using-external-databases_satellite "2.3. Preparing Satellite for using external databases").

**Procedure**

1. Depending on what type of database you want to use on your Satellite deployment, do one of the following:

   > **Note**
   >
   > Specify a meaningful value for the option: `--foreman-initial-organization`. This can be your company name. An internal label that matches the value is also created and cannot be changed afterwards. If you do not specify a value, an organization called **Default Organization** with the label **Default_Organization** is created. You can rename the organization name but not the label.

   - To install Satellite Server with the default local database, enter the following command with any additional options that you want to use:

     ```
     # satellite-installer --scenario satellite \
     --foreman-initial-organization "My_Organization" \
     --foreman-initial-location "My_Location" \
     --foreman-initial-admin-username admin_user_name \
     --foreman-initial-admin-password admin_password
     ```
   - To install Satellite Server with an external PostgreSQL server, enter the following command:

     ```
     # satellite-installer --scenario satellite \
     --foreman-initial-organization "My_Organization" \
     --foreman-initial-location "My_Location" \
     --foreman-initial-admin-username admin_user_name \
     --foreman-initial-admin-password admin_password \
     --katello-candlepin-manage-db false \
     --katello-candlepin-db-host postgres.example.com \
     --katello-candlepin-db-name candlepin \
     --katello-candlepin-db-user candlepin \
     --katello-candlepin-db-password Candlepin_Password \
     --foreman-proxy-content-pulpcore-manage-postgresql false \
     --foreman-proxy-content-pulpcore-postgresql-host postgres.example.com \
     --foreman-proxy-content-pulpcore-postgresql-db-name pulpcore \
     --foreman-proxy-content-pulpcore-postgresql-user pulp \
     --foreman-proxy-content-pulpcore-postgresql-password Pulpcore_Password \
     --foreman-db-manage false \
     --foreman-db-host postgres.example.com \
     --foreman-db-database foreman \
     --foreman-db-username foreman \
     --foreman-db-password Foreman_Password
     ```

     To also enable encrypted connections for these external databases, use the following command instead:

     ```
     # satellite-installer --scenario satellite \
     --foreman-initial-organization "My_Organization" \
     --foreman-initial-location "My_Location" \
     --foreman-initial-admin-username admin_user_name \
     --foreman-initial-admin-password admin_password \
     --katello-candlepin-manage-db false \
     --katello-candlepin-db-host postgres.example.com \
     --katello-candlepin-db-name candlepin \
     --katello-candlepin-db-user candlepin \
     --katello-candlepin-db-password Candlepin_Password \
     --katello-candlepin-db-ssl true \
     --katello-candlepin-db-ssl-ca My_CA_Certificate \
     --katello-candlepin-db-ssl-verify true \
     --foreman-proxy-content-pulpcore-manage-postgresql false \
     --foreman-proxy-content-pulpcore-postgresql-host postgres.example.com \
     --foreman-proxy-content-pulpcore-postgresql-db-name pulpcore \
     --foreman-proxy-content-pulpcore-postgresql-user pulp \
     --foreman-proxy-content-pulpcore-postgresql-password Pulpcore_Password \
     --foreman-proxy-content-pulpcore-postgresql-ssl true \
     --foreman-proxy-content-pulpcore-postgresql-ssl-root-ca My_CA_Certificate \
     --foreman-db-manage false \
     --foreman-db-host postgres.example.com \
     --foreman-db-database foreman \
     --foreman-db-username foreman \
     --foreman-db-password Foreman_Password \
     --foreman-db-root-cert My_CA_Certificate \
     --foreman-db-sslmode verify-full
     ```

   The script displays its progress and writes logs to `/var/log/foreman-installer/satellite.log`.

## 3.7. Importing Red Hat subscription manifests into Satellite

You can import a Red Hat subscription manifest into Satellite to provide subscription allocation to your organization in Satellite.

> **Note**
>
> Simple Content Access (SCA) is set on the organization, not the manifest. Importing a manifest does not change your organization’s Simple Content Access status.

Simple Content Access simplifies the subscription experience for administrators.

**Additional resources**

- [Subscription Management Administration Guide for Red Hat Enterprise Linux on the Red Hat Customer Portal](https://access.redhat.com/subscription_mgmt_guide_for_RHEL)

### 3.7.1. Obtaining a Red Hat subscription manifest

You can create and export a Red Hat subscription manifest to prepare subscriptions for import into Satellite.

**Procedure**

- Export your Red Hat subscription manifest from the Red Hat Hybrid Cloud Console. For more information, see [Creating and managing manifests for a connected Satellite Server](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/creating_and_managing_manifests_for_a_connected_satellite_server/index) in *Subscription Central*.

### 3.7.2. Importing a Red Hat subscription manifest by using Satellite web UI

You can import a Red Hat subscription manifest into Satellite Server by using Satellite web UI. Import the manifest so that you can enable and synchronize Red Hat repositories in your organization.

**Prerequisites**

- You have a Red Hat subscription manifest file. For more information, see [Section 3.7.1, “Obtaining a Red Hat subscription manifest”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#obtaining-a-red-hat-subscription-manifest "3.7.1. Obtaining a Red Hat subscription manifest").

**Procedure**

1. In the Satellite web UI, ensure the context is set to the organization you want to use.
2. Navigate to **Content** > **Subscriptions**.
3. Click **Manage Manifest**.
4. In the **Manage Manifest** window, click **Choose File**.
5. Navigate to the location that contains the Red Hat subscription manifest file, then click **Open**.

### 3.7.3. Importing a Red Hat subscription manifest by using Hammer CLI

You can import a Red Hat subscription manifest into Satellite Server by using Hammer CLI. Import the manifest so that you can enable and synchronize Red Hat repositories in your organization.

**Prerequisites**

- You have a Red Hat subscription manifest file. For more information, see [Section 3.7.1, “Obtaining a Red Hat subscription manifest”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#obtaining-a-red-hat-subscription-manifest "3.7.1. Obtaining a Red Hat subscription manifest").

**Procedure**

1. Copy the Red Hat subscription manifest file from your local machine to Satellite Server:

   ```
   $ scp ~/manifest_file.zip root@satellite.example.com:~/.
   ```
2. Log in to Satellite Server over SSH as the `root` user.
3. Import the Red Hat subscription manifest file:

   ```
   $ hammer subscription upload \
   --file ~/manifest_file.zip \
   --organization "My_Organization"
   ```
