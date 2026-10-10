---
title: "Deprecated features"
product: "Red Hat Satellite"
version: "6.19"
guide: "release_notes"
guide_title: "Release notes"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#deprecated-features"
---
# Chapter 4. Deprecated features

The following functionalities are deprecated in Red Hat Satellite 6.19.

Deprecated functionalities will likely not be supported in future releases of this product and are not recommended for new deployments. For the most recent list of deprecated functionality within a particular major release, refer to the latest version of release documentation.

The support status of deprecated functionality remains unchanged within Red Hat Satellite 6.19. For information about the length of support, see [Red Hat Enterprise Linux Life Cycle](https://access.redhat.com/support/policy/updates/errata) and [Red Hat Enterprise Linux Application Streams Life Cycle](https://access.redhat.com/support/policy/updates/rhel-app-streams-life-cycle).

Deprecated hardware components are not recommended for new deployments on the current or future releases. Hardware driver updates are limited to security and critical fixes only. Red Hat recommends replacing this hardware as soon as reasonably feasible.

A package can be deprecated and not recommended for further use. Under certain circumstances, a package can be removed from a product. Product documentation then identifies more recent packages that offer functionality similar, identical, or more advanced to the one deprecated, and provides further recommendations.

Hammer Admin is deprecated
:   The Hammer Admin plugin is deprecated. As an alternative, you can use the Satellite installer to manage your Satellite Server or Satellite Capsule Server.

    First deprecated in Satellite 6.19.

    [Jira:SAT-43244](https://redhat.atlassian.net/browse/SAT-43244)

API parameter deprecations
:   On hosts, the `content_view_id` and `lifecycle_environment_id` parameters are deprecated and will be removed in a future release. On the `POST /activation_keys` and `PUT /activation_keys/:id` activation keys, the `content_view_id`, `environment_id`, and environment parameters are deprecated and will be removed in a future release. Check any automations you may have to make sure they do not use API calls with these parameters.

    Use the `content_view_environment_ids` or `content_view_environments` parameters instead.

    First deprecated in Satellite 6.19.

    [Jira:SAT-42732](https://redhat.atlassian.net/browse/SAT-42732)

Legacy Job Invocations page is deprecated
:   The legacy **Job Invocations Details** page is deprecated and will be removed in a future version. The new job details page is displayed by default.

    First deprecated in Satellite 6.19.

    [Jira:SAT-43508](https://redhat.atlassian.net/browse/SAT-43508)

GRUB Legacy is deprecated in provisioning
:   GRUB Legacy, also known as GRUB version 1, is deprecated in provisioning and will be removed in a future release. GRUB 1 was used by end of life distributions such as RHEL 6. Current distributions use GRUB 2 and are not affected by the deprecation.

    First deprecated in Satellite 6.18.

    [Jira:SAT-39843](https://redhat.atlassian.net/browse/SAT-39843)

Puppet packages included in Satellite are deprecated
:   The `puppet-agent` and `puppetserver` packages, which are currently included in Satellite, are deprecated. In a future release, Satellite will stop providing these packages. Satellite will provide integration with OpenVox or Puppet packages that customers implement in their environment.

    First deprecated in Satellite 6.18.

    Jira:SAT-39110[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#ftn.PrivateTicketFootnote)

Sendmail is deprecated for delivering email
:   Delivering email by calling the `sendmail` binary on the system is deprecated and will be removed in a future version. As an alternative, use the SMTP mail delivery method. For more information, see [Configuring Satellite Server for outgoing emails](https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html/installing_satellite_server_in_a_connected_network_environment/performing-additional-configuration-on-server_satellite#Configuring_Server_for_Outgoing_Emails_satellite).

    First deprecated in Satellite 6.18.

    [Jira:SAT-38905](https://redhat.atlassian.net/browse/SAT-38905)

External authentication with Red Hat Single Sign-On is deprecated
:   Configuring Satellite with Red Hat Single Sign-On (RH SSO) as an external authentication source is deprecated. The RH SSO 7 product family reached End of Full Support. Instead of RH SSO, you can configure Red Hat build of Keycloak as an external authentication source for Satellite.

    To migrate from using RH SSO in your Satellite deployment, reconfigure the authentication source settings on your 6.17 Satellite Server to follow the requirements for Red Hat build of Keycloak. For more information, see [Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.17/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-sso-and-2fa-with-keycloak-in-project_keycloak-quarkus).

    For information on the current support policy for RH SSO, see [Red Hat Application Services Product Update and Support Policy](https://access.redhat.com/support/policy/updates/jboss_notes/).

    First deprecated in Satellite 6.17.

    [Jira:SAT-27644](https://redhat.atlassian.net/browse/SAT-27644)

Legacy remote execution job form in the Satellite web UI is deprecated
:   The option to use the legacy web UI form to run remote execution jobs is deprecated and will be removed in a future version. The new job invocation wizard will be the only available option. Note that the new job invocation wizard is the default method to run remote execution jobs in Satellite 6.13 and later versions.

    First deprecated in Satellite 6.17.

    [Jira:SAT-30410](https://redhat.atlassian.net/browse/SAT-30410)

iPXE firmware is deprecated
:   Using iPXE firmware for network-boot provisioning is deprecated. Instead, use HTTP booting for hosts in UEFI mode to reduce provisioning times. Note that iPXE firmware was never officially supported in Red Hat Satellite.

    First deprecated in Satellite 6.17

    [Jira:SAT-28823](https://redhat.atlassian.net/browse/SAT-28823)

`hammer host subscription attach` and `hammer host subscription auto-attach` commands are deprecated
:   The `hammer host subscription attach` and `hammer host subscription auto-attach` commands are deprecated. The commands are non-functional and do not result in attaching a subscription.

    First deprecated in Satellite 6.16

    Note: Entitlement-based subscription management was removed in Satellite 6.16.

    [Jira:SAT-28367](https://redhat.atlassian.net/browse/SAT-28367)

Asynchronous SSH remote execution mode is deprecated
:   The `async-ssh` remote execution mode is deprecated. If you have unstable connectivity between Capsules and managed hosts, use the pull mode instead. For more information about pull mode, see [Transport Modes for Remote Execution](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Transport_Modes_for_Remote_Execution_managing-hosts) in *Managing hosts*.

    First deprecated in Satellite 6.13.

    [Jira:SAT-16415](https://redhat.atlassian.net/browse/SAT-16415)

Package Group Actions is deprecated
:   The **Package Group Actions** option in the web UI is deprecated.

    First deprecated in Satellite 6.10.

    [Jira:SAT-27578](https://redhat.atlassian.net/browse/SAT-27578)

`katello-ca-consumer` package and `katello-rhsm-consumer` script are deprecated
:   The `katello-ca-consumer` package and `katello-rhsm-consumer` script are deprecated. You must use the global registration template to register a host.

    First deprecated in Satellite 6.9.

    [Jira:SAT-21372](https://redhat.atlassian.net/browse/SAT-21372)

Bootstrap.py host registration script is deprecated
:   The `bootstrap.py` script for registering a host to Satellite or Capsule is deprecated. It is replaced with the `curl` command created by using the global registration template.

    First deprecated in Satellite 6.9.

    [Jira:SAT-21137](https://redhat.atlassian.net/browse/SAT-21137)
