---
title: "Installing Satellite Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_disconnected_network_environment"
guide_title: "Installing Satellite Server in a disconnected network environment"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#installing-satellite-server"
---
# Chapter 3. Installing Satellite Server

Use the following procedures to install Satellite Server in a disconnected environment, perform the initial configuration, and import subscription manifests.

When the intended host for Satellite Server is in a disconnected environment, you can install Satellite Server by using an external computer to download an ISO image of the packages, and copying the packages to the system you want to install Satellite Server on. This method is not recommended for any other situation as ISO images might not contain the latest updates, bug fixes, and functionality.

Before you continue, consider which manifests are relevant for your environment.

> **Note**
>
> You cannot register Satellite Server to itself.

## 3.1. Downloading the binary DVD images

Download the binary DVD images to create local installation repositories for installing Red Hat Satellite in disconnected environments.

**Procedure**

1. Go to [Red Hat Customer Portal](https://access.redhat.com/) and log in.
2. Click **DOWNLOADS**.
3. Select **Red Hat Enterprise Linux**.
4. Click **All Red Hat Enterprise Linux Downloads**.
5. Ensure that you have the correct product and version for your environment.

   - **Product Variant** is set to **Red Hat Enterprise Linux for x86_64**.
   - **Version** is set to the latest minor version of the product you plan to use as the base operating system.
   - **Architecture** is set to the 64 bit version.
6. On the **Product Software** tab, download the Binary DVD image for the latest **Red Hat Enterprise Linux for x86_64** version.
7. Click **DOWNLOADS** and select **Red Hat Satellite**.
8. Ensure that you have the correct product and version for your environment.

   - **Product Variant** is set to **Red Hat Satellite**.
   - **Version** is set to the latest minor version of the product you plan to use.
9. On the **Product Software** tab, download the Binary DVD image for the latest Red Hat Satellite version.
10. Copy the ISO files to `/var/tmp` on the Satellite base operating system or other accessible storage device.

    ```
    # scp localfile username@hostname:remotefile
    ```

## 3.2. Configuring the base operating system with offline repositories

Use this procedure to configure offline repositories for Red Hat Enterprise Linux 9 and Red Hat Satellite ISO images.

**Procedure**

1. Create a directory to serve as the mount point for the ISO file corresponding to the version of the base operating system.

   ```
   # mkdir /media/rhel
   ```
2. Mount the ISO image for Red Hat Enterprise Linux to the mount point.

   ```
   # mount -o loop rhel-DVD.iso /media/rhel
   ```
3. To copy the ISO file’s repository data file and change permissions, enter:

   ```
   # cp /media/rhel/media.repo /etc/yum.repos.d/rhel.repo
   # chmod u+w /etc/yum.repos.d/rhel.repo
   ```
4. Edit the repository data file and add the `baseurl` directive.

   ```
   [RHEL-BaseOS]
   name=Red Hat Enterprise Linux BaseOS
   mediaid=None
   metadata_expire=-1
   gpgcheck=0
   cost=500
   baseurl=file:///media/rhel/BaseOS/

   [RHEL-AppStream]
   name=Red Hat Enterprise Linux AppStream
   mediaid=None
   metadata_expire=-1
   gpgcheck=0
   cost=500
   baseurl=file:///media/rhel/AppStream/
   ```
5. Verify that the repository has been configured.

   ```
   # yum repolist
   ```
6. Create a directory to serve as the mount point for the ISO file of Satellite Server.

   ```
   # mkdir /media/sat6
   ```
7. Mount the ISO image for Satellite Server to the mount point.

   ```
   # mount -o loop sat6-DVD.iso /media/sat6
   ```

## 3.3. Installing the Satellite packages from the offline repositories

You can install the Satellite packages from the offline repositories by using locally mounted ISO images.

**Procedure**

1. Ensure that the ISO images for Red Hat Enterprise Linux Server and Red Hat Satellite are mounted:

   ```
   # findmnt -t iso9660
   ```
2. Import Red Hat GPG keys:

   ```
   # rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release
   ```
3. Update the base operating system with the Binary DVD image:

   ```
   # dnf upgrade
   ```
4. Change to the directory where the Satellite ISO is mounted:

   ```
   # cd /media/sat6/
   ```
5. Run the installation script in the mounted directory:

   ```
   # ./install_packages
   ```

   If you have successfully installed the Satellite packages, the following message is displayed: `Install is complete. Please run satellite-installer --scenario satellite`.

## 3.4. Resolving package dependency errors

If there are package dependency errors during installation of Satellite Server packages, you can resolve the errors by downloading and installing packages from Red Hat Customer Portal.

If you have successfully installed the Satellite packages, skip this procedure.

**Procedure**

1. Go to the [Red Hat Customer Portal](https://access.redhat.com/) and log in.
2. Click **DOWNLOADS**.
3. Click the product that contains the package that you want to download.
4. Ensure that you have the correct **Product Variant**, **Version**, and **Architecture** for your environment.
5. Click the **Packages** tab.
6. In the **Search** field, enter the name of the package.
7. Click the package.
8. From the **Version** list, select the version of the package.
9. At the bottom of the page, click **Download Now**.
10. Copy the package to the Satellite base operating system.
11. On Satellite Server, change to the directory where the package is located:

    ```
    # cd /path-to-package/
    ```
12. Install the package locally:

    ```
    # dnf install package_name
    ```
13. Change to the directory where the Satellite ISO is mounted:

    ```
    # cd /media/sat6/
    ```
14. Verify that you have resolved the package dependency errors by installing Satellite Server packages. If there are further package dependency errors, repeat this procedure.

    ```
    # ./install_packages
    ```

    If you have successfully installed the Satellite packages, the following message is displayed: `Install is complete. Please run satellite-installer --scenario satellite`.

**Additional resources**

- [How can I use the yum output to solve yum dependency errors?](https://access.redhat.com/solutions/262323)

## 3.5. Considerations for using the satellite-installer utility

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

## 3.6. Configuring Satellite Server

You can use the `satellite-installer` installation script to configure the Satellite Server with the default local database or an external PostgreSQL server. The command options override the corresponding default initial configuration options and are recorded in the Satellite answer file.

> **Note**
>
> By default, all configuration files configured by the installer are managed. When `satellite-installer` runs, it overwrites any manual changes to the managed files with the intended values. This means that running the installer on a broken system should restore it to working order, regardless of changes made. For more information on how to apply custom configuration on other services, see [Applying Custom Configuration to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#applying-custom-configuration_satellite).

**Prerequisites**

- If you want to use an external PostgreSQL database with your Satellite Server, you have prepared a PostgreSQL server with the required databases and user permissions. For more information, see [Section 2.3, “Preparing Satellite for using external databases”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#preparing-for-using-external-databases_satellite "2.3. Preparing Satellite for using external databases").

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
2. Unmount the ISO images:

   ```
   # umount /media/sat6
   # umount /media/rhel
   ```

## 3.7. Disabling subscription connection by using Satellite web UI

Disable subscription connection on your disconnected Satellite Server to avoid connecting to the Red Hat Portal. This will also prevent you from refreshing the manifest and updating upstream entitlements.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Click the **Content** tab.
3. Set the `Subscription Connection Enabled` value to `No`.

## 3.8. Disabling subscription connection by using Hammer CLI

Disable subscription connection on disconnected Satellite Server to avoid connecting to the Red Hat Portal. This will also prevent you from refreshing the manifest and updating upstream entitlements.

**Procedure**

- Enter the following command on Satellite Server:

  ```
  $ hammer settings set --name subscription_connection_enabled --value false
  ```

## 3.9. Importing Red Hat subscription manifests into Satellite

You can import a Red Hat subscription manifest into Satellite to provide subscription allocation to your organization in Satellite.

> **Note**
>
> Simple Content Access (SCA) is set on the organization, not the manifest. Importing a manifest does not change your organization’s Simple Content Access status.

Simple Content Access simplifies the subscription experience for administrators.

**Additional resources**

- [Subscription Management Administration Guide for Red Hat Enterprise Linux on the Red Hat Customer Portal](https://access.redhat.com/subscription_mgmt_guide_for_RHEL)

### 3.9.1. Obtaining a Red Hat subscription manifest

You can create and export a Red Hat subscription manifest to prepare subscriptions for import into Satellite.

**Procedure**

1. Export your Red Hat subscription manifest from the Red Hat Customer Portal. You will use the same manifest in [Section 5.4.4, “Configuring Satellite Server to synchronize content over a network by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#configuring-satellite-server-to-synchronize-content-over-a-network-by-using-web-ui "5.4.4. Configuring Satellite Server to synchronize content over a network by using Satellite web UI"). For more information, see [Creating and managing manifests for a disconnected Satellite Server](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/creating_and_managing_manifests_for_a_disconnected_satellite_server/index) in *Subscription Central*.
2. Disable subscription connection on your Satellite Server. For more information, see [Section 3.7, “Disabling subscription connection by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#disabling-subscription-connection-by-using-web-ui "3.7. Disabling subscription connection by using Satellite web UI").

### 3.9.2. Importing a Red Hat subscription manifest by using Satellite web UI

You can import a Red Hat subscription manifest into Satellite Server by using Satellite web UI. Import the manifest so that you can enable and synchronize Red Hat repositories in your organization.

**Prerequisites**

- You have a Red Hat subscription manifest file. For more information, see [Section 3.9.1, “Obtaining a Red Hat subscription manifest”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#obtaining-a-red-hat-subscription-manifest "3.9.1. Obtaining a Red Hat subscription manifest").

**Procedure**

1. In the Satellite web UI, ensure the context is set to the organization you want to use.
2. Navigate to **Content** > **Subscriptions**.
3. Click **Manage Manifest**.
4. In the **Manage Manifest** window, click **Choose File**.
5. Navigate to the location that contains the Red Hat subscription manifest file, then click **Open**.

**Next steps**

- You can now enable and synchronize Red Hat repositories. For more information, see [Adding content to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite) in *Managing content*.

### 3.9.3. Importing a Red Hat subscription manifest by using Hammer CLI

You can import a Red Hat subscription manifest into Satellite Server by using Hammer CLI. Import the manifest so that you can enable and synchronize Red Hat repositories in your organization.

**Prerequisites**

- You have a Red Hat subscription manifest file. For more information, see [Section 3.9.1, “Obtaining a Red Hat subscription manifest”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#obtaining-a-red-hat-subscription-manifest "3.9.1. Obtaining a Red Hat subscription manifest").

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

**Next steps**

- You can now enable and synchronize Red Hat repositories. For more information, see [Adding content to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite) in *Managing content*.
