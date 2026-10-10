---
title: "Installing standalone Hammer"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#installing-standalone-hammer"
---
# Chapter 2. Installing standalone Hammer

You can install Hammer on a host running RHEL that has no Satellite Server installed, and use it to connect from the host to a remote Satellite.

**Prerequisites**

- Ensure that you register the host to Satellite Server or Capsule Server.
- Ensure that the following repositories are enabled and synchronized on Satellite Server:

  - rhel-9-for-x86_64-baseos-rpms
  - rhel-9-for-x86_64-appstream-rpms
  - satellite-utils-6.19-for-rhel-9-x86_64-rpms

**Procedure**

1. Enable the required repositories on the host.
2. Install Hammer CLI:

   ```
   # dnf install satellite-cli
   ```
3. Set the `:host:` entry in the `/etc/hammer/cli.modules.d/foreman.yml` file to the Satellite URL:

   ```
   :host: 'https://satellite.example.com'
   ```

**Additional resources**

- [Enabling custom repositories on hosts in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#enabling-custom-repositories-on-hosts)
- [Synchronizing repositories ad hoc in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc)
- [Registering hosts by using global registration in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration)
