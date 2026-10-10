---
title: "Upgrading Red Hat Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "upgrading_connected_red_hat_satellite_to_6.19"
guide_title: "Upgrading connected Red Hat Satellite to 6.19"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_connected_red_hat_satellite_to_6.19/index#Upgrading_satellite_upgrading-connected"
---
# Chapter 2. Upgrading Red Hat Satellite

Upgrading Satellite includes upgrading your Satellite Server, synchronizing the required repositories, and upgrading Capsule Servers.

## 2.1. Upgrading your Satellite Server

Upgrading a connected Satellite Server includes backing up the server, updating the system and Satellite configuration, and performing the upgrade.

> **Warning**
>
> Note that the satellite-installer is executed during an upgrade or update. Any files managed by satellite-installer are overwritten. Check if you have any manual changes that would be overwritten by satellite-installer. You can use the `--noop` option with the satellite-installer to test for changes. For more information, see the Red Hat Knowledgebase solution [How to use the noop option to check for changes in Satellite config files during an upgrade.](https://access.redhat.com/solutions/3351311)

If you use Red Hat Lightspeed in Satellite, the following process upgrades Red Hat Lightspeed in Satellite. The `satellite-maintain` tool pulls the container images of Red Hat Lightspeed in Satellite automatically.

**Prerequisites**

- If you made manual edits to your DNS or DHCP configuration in the `/etc/zones.conf` or `/etc/dhcp/dhcpd.conf` files, ensure DNS and DHCP configuration management is disabled:

  ```
  # satellite-installer \
  --foreman-proxy-dhcp-managed false \
  --foreman-proxy-dns-managed false
  ```

  This prevents the upgrade process from overwriting your DNS and DHCP configuration.
- If you use Red Hat Lightspeed advisor service in Satellite in your environment, ensure you are logged in to `registry.redhat.io` so that the latest container images can be downloaded:

  ```
  # podman login --authfile /etc/foreman/registry-auth.json registry.redhat.io
  ```

**Procedure**

1. Create a backup of your Satellite Server. The backup can be a virtual machine (VM) snapshot or a regular full backup. For more information, see [Backing up Satellite Server and Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin) in *Administering Red Hat Satellite*.
2. Ensure that the Satellite Maintenance repository is enabled:

   ```
   # subscription-manager repos --enable \
   satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```
3. Upgrade the satellite-maintain utility to its latest version:

   ```
   # satellite-maintain self-upgrade
   ```
4. Determine whether your system is ready for Satellite upgrade:

   ```
   # satellite-maintain upgrade check
   ```

   Review the results and address any highlighted error conditions before performing the upgrade.

   > **Note**
   >
   > The `satellite-maintain upgrade check` might prompt you for the Hammer admin user credentials. These changes are applied to the `/etc/foreman-maintain/foreman-maintain-hammer.yml` file.
5. Run the Satellite Server upgrade command. Because of the lengthy upgrade time, consider using a utility such as `tmux`. For more information, see [Section 1.3, “Following the progress of the upgrade”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_connected_red_hat_satellite_to_6.19/index#following_the_progress_of_the_upgrade_upgrading-connected "1.3. Following the progress of the upgrade").

   ```
   # satellite-maintain upgrade run
   ```
6. If the `satellite-maintain` command told you to reboot, then reboot the system:

   ```
   # reboot
   ```
7. Perform the following post-upgrade tasks to ensure your environment is adjusted to any changes applied during the upgrade.

   1. Verify whether the default templates changed during the upgrade. Update any custom templates that you created by cloning a default template to reflect these changes.

      > **Note**
      >
      > Use custom provisioning snippets to execute custom code before or after the provisioning process instead of cloning default templates. You can avoid recreating cloned templates if you use custom provisioning snippets. For more information about configuring custom provisioning snippets, see [Running custom code during host provisioning by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#running-custom-code-during-host-provisioning-by-using-web-ui) in *Provisioning hosts*.
   2. If your Satellite shows any discovered hosts, reboot them:

      1. In the Satellite web UI, navigate to **Hosts** > **Discovered hosts**.
      2. Select **Any Organization** to display all discovered hosts.
      3. Reboot all discovered hosts.

## 2.2. Synchronizing the new repositories

You must enable and synchronize the new 6.19 repositories before you can upgrade Capsule Servers and Satellite clients.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Red Hat Repositories**.
2. Enable the following repositories:

   - Repositories required to upgrade Capsule Servers:

     - **Red Hat Satellite Capsule 6.19 (for RHEL 9 x86_64) (RPMs)**
     - **Red Hat Satellite Maintenance 6.19 (for RHEL 9 x86_64) (RPMs)**
     - **Red Hat Enterprise Linux 9 (for x86_64 – BaseOS) (RPMs)**
     - **Red Hat Enterprise Linux 9 (for x86_64 – AppStream) (RPMs)**
   - Repositories required to upgrade Satellite clients:

     - **Red Hat Satellite Client 6** for each Red Hat Enterprise Linux version your clients are using
     - If you use Puppet to manage host configurations, **Red Hat Satellite Client 6 OpenVox** for each Red Hat Enterprise Linux version your clients are using
3. In the Satellite web UI, navigate to **Content** > **Sync Status**.
4. Synchronize the following repositories:

   - All repositories for version 6.19
   - **Red Hat Satellite Client 6** repositories for each Red Hat Enterprise Linux version your clients are using
5. If you use Puppet to manage host configurations, manually update the content views for your hosts. Add the **Red Hat Satellite Client 6 OpenVox** repository for the Red Hat Enterprise Linux version your clients are using to the content views and publish and promote a new version of the content views.

**Troubleshooting**

- Refresh the Red Hat subscription manifest to resolve issues with synchronizing repositories. In the Satellite web UI, navigate to **Content** > **Subscriptions** > **Manage Manifest** > **Refresh**.

  > **Warning**
  >
  > Do not delete the manifest from the Customer Portal or in the Satellite web UI. Deleting your manifest removes all the entitlements of your hosts.

**Additional resources**

- [Importing content in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#)

## 2.3. Upgrading Capsule Servers

After upgrading your Satellite Server and synchronizing the required repositories, you can upgrade your Capsule Servers.

> **Note**
>
> You can use the **Capsule Upgrade Playbook** job template to upgrade Capsule Servers remotely. For more information about running remote jobs based on templates, see [Configuring and setting up remote jobs](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs) in *Managing hosts*.

**Prerequisites**

- The base system of the Capsule is registered to the newly upgraded Satellite Server.
- Ensure that you synchronize the required repositories on Satellite Server. For more information, see [Section 2.2, “Synchronizing the new repositories”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_connected_red_hat_satellite_to_6.19/index#synchronizing_the_new_repositories_upgrading-connected "2.2. Synchronizing the new repositories").
- If the Capsule Server is registered to a content view, add the Capsule 6.19 repositories to the content view. Publish and promote a new version of the content view. For more information, see [Managing content views and content view environments](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-views-and-content-view-environments) in *Managing content*.

**Procedure**

1. Create a backup of your Capsule Server. The backup can be a virtual machine (VM) snapshot or a regular full backup. For more information, see [Backing up Satellite Server and Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin) in *Administering Red Hat Satellite*.
2. Ensure that the Satellite Maintenance repository is enabled:

   ```
   # subscription-manager repos \
    --enable satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```
3. Upgrade the `satellite-maintain` utility on the Capsule Server to its latest version:

   ```
   # satellite-maintain self-upgrade
   ```
4. Determine whether Capsule Server is ready for the upgrade:

   ```
   # satellite-maintain upgrade check
   ```

   Review the results and address any highlighted error conditions before performing the upgrade.
5. Run the Satellite upgrade command. Because of the lengthy upgrade time, consider using a utility such as `tmux`. For more information, see [Section 1.3, “Following the progress of the upgrade”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_connected_red_hat_satellite_to_6.19/index#following_the_progress_of_the_upgrade_upgrading-connected "1.3. Following the progress of the upgrade").

   ```
   # satellite-maintain upgrade run
   ```
6. If the `satellite-maintain` command told you to reboot, then reboot the system:

   ```
   # reboot
   ```

## 2.4. Upgrading the external database operating system

If your Satellite uses an external database, you can upgrade the database from RHEL 8 to RHEL 9. You can upgrade the operating system while upgrading Satellite from 6.18 to 6.19.

**Prerequisites**

- A host running Red Hat Enterprise Linux 9 for PostgreSQL server. For more information, see [Preparing Satellite for using external databases](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#preparing-for-using-external-databases_satellite).

**Procedure**

1. Create a backup of your existing external database.
2. Restore the backup on the new Red Hat Enterprise Linux 9 server.
3. Verify that Satellite can reach the new database:

   ```
   # PGPASSWORD='My_Foreman_Database_Password' psql -h postgres.example.com -p 5432 -U foreman -d foreman -c "SELECT 1 as ping"
   ```
4. If your Satellite Server can reach the new database server by using the old name, you do not need to make any further changes. Otherwise, reconfigure Satellite to use the new name:

   ```
   # satellite-installer \
   --foreman-db-host newpostgres.example.com \
   --katello-candlepin-db-host newpostgres.example.com \
   --foreman-proxy-content-pulpcore-postgresql-host newpostgres.example.com
   ```

## 2.5. Refreshing clients of Red Hat Lightspeed in Satellite

If you use Red Hat Lightspeed in Satellite, you must refresh Red Hat Lightspeed in Satellite registration of your hosts to keep using services of Red Hat Lightspeed in Satellite after upgrading Satellite Server.

**Prerequisites**

- You have root access on your hosts.

**Procedure**

- On your hosts, refresh `insights-client` registration:

  ```
  # insights-client --register --force
  ```

  You can use remote execution to run this command on your hosts.

**Additional resources**

- [Executing a remote job by using Satellite web UI in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#executing-a-remote-job-by-using-web-ui)
- [Executing a remote job by using Hammer CLI in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#executing-a-remote-job-by-using-cli)

## 2.6. Upgrading Puppet agent 7 to OpenVox agent 8

If you use Puppet to configure hosts, you can upgrade Puppet agent 7 to OpenVox agent 8.

Puppet agent 7 remains compatible with OpenVox in Satellite as a legacy alternative, but Red Hat recommends to upgrade to OpenVox agent 8. For more information, see [OpenVox versions supported for integration with Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#openvox-versions-supported-for-integration-with-satellite) in *Managing configurations by using Puppet integration*.

**Prerequisites**

- **Red Hat Satellite Client 6 OpenVox** repository is enabled on the host.

**Procedure**

- On your hosts, upgrade the `puppet-agent` agent package to `openvox-agent`:

  ```
  # dnf upgrade puppet-agent
  ```

  You can also use remote execution to upgrade the package on multiple hosts. For more information, see [Upgrading a package](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Upgrading_a_package_managing-hosts) in *Managing hosts*.
