---
title: "Preparing for Satellite upgrade"
product: "Red Hat Satellite"
version: "6.19"
guide: "upgrading_disconnected_red_hat_satellite_to_6.19"
guide_title: "Upgrading disconnected Red Hat Satellite to 6.19"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_disconnected_red_hat_satellite_to_6.19/index#preparing-for-satellite-upgrade"
---
# Chapter 2. Preparing for Satellite upgrade

Review the following available upgrade paths and planning considerations before upgrading your current Red Hat Satellite installation to Red Hat Satellite 6.19.

## 2.1. Upgrade path overview

You can upgrade from Red Hat Satellite 6.18 to Red Hat Satellite 6.19.

The upgrade process includes the following high-level steps:

1. Ensuring that your Satellite Servers and Capsule Servers are running on Satellite 6.18.
2. Upgrading your Satellite Server:

   1. Upgrading your Satellite Server to 6.19.
   2. Synchronizing the new 6.19 repositories.
3. Upgrading your Capsule Servers to 6.19.

You can upgrade your Capsules separately over multiple maintenance windows because versions 6.18 and 6.17 remain compatible with your upgraded Satellite Server 6.19. Upgrading Capsules separately can be useful in the following situations:

- If you want to have several smaller outage windows instead of one larger window.
- If several teams in your organization manage Capsules across different locations.
- If you use a load-balanced configuration, you can upgrade one load-balanced Capsule and keep other load-balanced Capsules at one version lower. This allows you to upgrade all Capsules one after another without any outage.

Capsules at version 6.18 and 6.17 retain all of their previous functionality. New functionality added in the 6.19 release is available only after you upgrade your Capsules to 6.19.

## 2.2. Planning Satellite upgrade

Upgrading to Satellite 6.19 affects your entire Satellite infrastructure. Plan carefully before proceeding.

- Read the Red Hat Satellite 6.19 [Release notes](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#).

  > **Important**
  >
  > If you use Flatpak content in your environment, be aware that upgrading to Satellite 6.19 will prevent your hosts from consuming Flatpak content from Satellite.
- Consider whether any of your integrations need updating. Some Satellite API endpoints, Hammer CLI commands, and modules from the Satellite Ansible Collection can differ between versions of Satellite. For information about changes in these tools, see the Red Hat Satellite 6.19 Release notes.
- If you use Puppet to manage your host configuration, ensure your Puppet modules are compatible with OpenVox 8, which uses Ruby 3.2.
- Optional: You can test the upgrade on a clone of your Satellite Server. After you successfully test the upgrade on the clone, you can repeat the upgrade on your primary Satellite Server and discard the clone. Alternately, you can promote the clone to your primary Satellite Server and discard the previous primary Satellite Server.
- You can upgrade to Satellite 6.19 from any Satellite 6.18 patch version.
- The upgrade process shuts down Satellite services. Ensure to plan for the required downtime. The upgrade process duration varies depending on your hardware configuration, network speed, and the amount of data on the server:

  - On average installations, upgrading Satellite Server takes up to 30 minutes and upgrading a single Capsule Server takes up to 10 minutes.
  - On very large installations, upgrading Satellite Server can take up to 1 – 2 hours and upgrading a single Capsule Server can take up to 15 – 30 minutes.

**Additional resources**

- [Release notes](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#)
- [Cloning Satellite Server in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#cloning-satellite-server)

## 2.3. Following the progress of the upgrade

Using a utility such as `tmux` helps follow the progress of the upgrade without the need to maintain a continuous shell session.

Because of the lengthy upgrade time, use a utility such as `tmux` to suspend and reattach a communication session. You can then check the upgrade progress without staying connected to the command shell continuously.

If you lose connection to the command shell where the upgrade command is running, you can see the logs in `/var/log/foreman-installer/satellite.log` to check if the process completed successfully.

For more information about using `tmux`, see the `tmux(1)` man page on your system.
