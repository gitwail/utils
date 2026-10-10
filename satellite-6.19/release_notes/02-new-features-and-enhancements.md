---
title: "New features and enhancements"
product: "Red Hat Satellite"
version: "6.19"
guide: "release_notes"
guide_title: "Release notes"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#new-features-and-enhancements"
---
# Chapter 2. New features and enhancements

Discover new capabilities and improvements introduced in Red Hat Satellite 6.19.

## 2.1. Host provisioning and management

Job templates can be cloned with Hammer CLI
:   With this update, you can clone job templates on the command line by using the new `hammer job-template clone` sub-command. This is a CLI equivalent to the `POST /api/job_templates/:id/clone` API call. This enhancement streamlines workflows and aligns CLI capabilities with API functionality.

    [Jira:SAT-34616](https://redhat.atlassian.net/browse/SAT-34616)

Cloned templates track the original template ID
:   This update stores the original template reference in the new `cloned_from` metadata field. The source template is also displayed in the Web UI and as output from the `hammer template info --id My_host_id`, `hammer report-template info --id My_host_id`, and `hammer job-template info --id My_host_id` commands. This enhancement improves template management and traceability.

    [Jira:SAT-18489](https://redhat.atlassian.net/browse/SAT-18489)

SSH certificates are supported for remote execution
:   You can configure your Capsules to use SSH certificates signed by your trusted certificate authority (CA) during a remote execution connection. By enabling this feature, you can avoid the default Trust on First Use (TOFU) model, and benefit from centralized trust management and revocation capabilities. For more information, see [Configuring Capsule and hosts to authenticate with SSH certificates during remote execution](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-capsule-and-hosts-to-authenticate-with-ssh-certificates-during-remote-execution) in *Managing hosts*.

    [Jira:SAT-28038](https://redhat.atlassian.net/browse/SAT-28038)

VMs with Libvirt compute resource can be provisioned on RHEL 10 hypervisors
:   With this update, you can create and provision virtual machines by using the Libvirt compute resource on Red Hat Enterprise Linux 10 hypervisors.

    [Jira:SAT-40266](https://redhat.atlassian.net/browse/SAT-40266)

Port 80 is not required for global registration
:   With this update, host registration uses HTTPS for the `/unattended/built` endpoint. This means that registration no longer requires port 80 and it is not possible to use port 80 during host registration.

    [Jira:SAT-41516](https://redhat.atlassian.net/browse/SAT-41516)

Reports and **Host - Details** can include hardware and cloud billing facts
:   With this update, you can incorporate cloud billing facts for AWS, Microsoft Azure, and Google Cloud, and the hardware model into the **Host - Installed Products** report template and **Host - Details** pages. As a result, you can segment your systems based on billing sources and hardware.

    [Jira:SAT-39060](https://redhat.atlassian.net/browse/SAT-39060)

## 2.2. Red Hat Lightspeed

Enhanced role-based access control for Red Hat Lightspeed in Satellite
:   The following new user permissions are available to control user access to RHEL hosts Recommendations and Common Vulnerabilities and Exposures (CVE) data:

    - `edit_advisor`
    - `view_advisor`
    - `edit_vulnerability`
    - `view_vulnerability`

    Additionally, this update adds the `ForemanRhCloud Read Only` built-in role, which includes the new viewing permissions. The `ForemanRHCloud` built-in role now includes the new viewing and editing permissions.

    For more information, see [Monitoring hosts by using Red Hat Lightspeed in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#monitoring-hosts-by-using-red-hat-lightspeed-in-satellite) in *Managing hosts*.

    Jira:SAT-40466[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#ftn.PrivateTicketFootnote)

Enhanced control over vulnerability analysis on hosts
:   With this update, you can disable vulnerability analysis on selected hosts, controlling which hosts are included in vulnerability reporting. This functionality is available from the All Hosts page and Host Details page.

    For more information, see [Disabling vulnerability analysis on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#disabling-vulnerability-analysis-on-hosts) in *Managing hosts*.

    [Jira:SAT-40203](https://redhat.atlassian.net/browse/SAT-40203)

## 2.3. Model Context Protocol

Patch hosts and incrementally update, publish, and promote content views by using MCP
:   With this update, you can patch hosts registered with your Satellite by using natural language instructions through the Model Context Protocol (MCP). You can use your AI application connected to the MCP server for Satellite to apply errata to hosts, incrementally update, publish, and promote actions on content views. This improvement streamlines patch management, minimizing the requirement for manual work and multiple steps.

    For more information, see the following updated documentation:

    - [Installing errata on hosts by using MCP](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#installing-errata-on-hosts-by-using-mcp).
    - [Adding errata to an incremental content view by using MCP](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-errata-to-an-incremental-content-view-by-using-mcp).
    - [Publishing and promoting a content view by using MCP](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#publishing-and-promoting-a-content-view-by-using-mcp).

    Jira:SAT-40970[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#ftn.PrivateTicketFootnote)

## 2.4. Web UI

**Compact table mode** available in Satellite web UI to reduce table padding
:   With this update, the **Compact table mode** setting is available for viewing tables in Satellite web UI. With **Compact table mode** enabled, Satellite web UI shows table rows with less space between items. As a result, you can view more data on the screen at once.

    To enable **Compact table mode** in the Satellite web UI, click the user menu in the top bar and select **My Account**. Under the **UI Preferences** tab, select **Compact table mode**.

    [Jira:SAT-32173](https://redhat.atlassian.net/browse/SAT-32173)

**Container Image Tags** page is redesigned
:   The **Container Image Tags** page in the Satellite web UI is enhanced for improved usability and easier navigation when managing and viewing container content in Satellite. The enhancements include displaying more details about container content and improved filtering. As a result, the redesigned page provides a single location to view all information related to container image tags and their associated metadata in Satellite.

    To view the page, navigate to **Content** > **Content types** > **Container image tags**.

    [Jira:SAT-23851](https://redhat.atlassian.net/browse/SAT-23851)

**All Hosts** page improvements
:   This update adjusts the **All Hosts** page for easier management of host collections and system purpose. Among other improvements, you can more efficiently make changes for multiple hosts.

    [Jira:SAT-35463](https://redhat.atlassian.net/browse/SAT-35463)

## 2.5. Installation and upgrade

Leapp host upgrades support target version selection
:   When upgrading hosts to the next major Red Hat Enterprise Linux release, you can now specify a particular target version for Leapp pre-upgrade checks and upgrades. This enhancement provides more control and flexibility in host upgrades. For more information, see [Upgrading hosts to next major Enterprise Linux release](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Upgrading_Hosts_to_Next_Major_Release_managing-hosts).

    [Jira:SAT-38080](https://redhat.atlassian.net/browse/SAT-38080)

## 2.6. Content management

Satellite transitions to OpenVox 8
:   Satellite is transitioning to OpenVox 8 packages for Puppet management for Satellite Server, Capsule Server, and clients. The implementation of OpenVox reduces operational risk and ensures security continuity. To install these packages on the clients, enable the **Red Hat Satellite Client 6 OpenVox** repository for the Red Hat Enterprise Linux version your clients use. For more information, see [Upgrade Puppet agent 7 to OpenVox agent 8](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/upgrading_connected_red_hat_satellite_to_6.19/index#upgrade-puppet-agent-7-to-openvox-agent-8) in *Upgrading connected Red Hat Satellite to 6.19* and [OpenVox versions supported for integration with Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#openvox-versions-supported-for-integration-with-satellite) in *Managing configurations by using Puppet integration*.

    Jira:SAT-31648[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#ftn.PrivateTicketFootnote)

Making transient packages on image mode hosts persistent
:   If you use Satellite to manage image mode hosts with transient packages, you can generate a new Containerfile install command to persist transient packages in your container image. By placing the command in the Containerfile, you can build a new container image that includes the necessary packages. You can then upgrade your image mode host to the new image, incorporating the packages into future builds.

    For more information, see [Persisting transient packages in your image](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#persisting-transient-packages-in-your-image) in *Managing content*.

    [Jira:SAT-30671](https://redhat.atlassian.net/browse/SAT-30671)

Tracking transient packages on image mode hosts
:   Satellite provides options for viewing the persistence mode of packages on an image mode host:

    - On the host details page in the Satellite web UI, navigate to **Content** > **Packages**. Persistence mode is displayed in the **Persistence** column.
    - From the command line, execute the `hammer host package list --host-id My_Host_ID --fields ALL` command. Persistence mode is included in the output.

    Note that information about package persistence is not yet available in Satellite. The data will be provided by a future version of the Subscription Manager service.

    [Jira:SAT-36790](https://redhat.atlassian.net/browse/SAT-36790)

Enhanced support for multiple CV environments in hosts and activation keys in web UI
:   Previously, Satellite web UI could only display information about hosts and activation keys with multiple content view (CV) environments assigned. With this update, you can also assign and manage multiple CV environments for hosts and activation keys from the web UI.

    For more information, see [Managing content view environments](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-view-environments) in *Managing content*.

    Note that with this release, the option to manage multiple CV environments in hosts and activation keys is enabled by default.

    [Jira:SAT-26055](https://redhat.atlassian.net/browse/SAT-26055)

## 2.7. Documentation

Source for documentation links in Satellite web UI can be configured for RHOKP
:   With this update, the **Red Hat documentation server URL** setting is available in the Satellite web UI. You can use the setting to provide the URL of your instance of the Red Hat Offline Knowledge Portal (RHOKP). When the RHOKP URL is provided, documentation links in the Satellite web UI point to the RHOKP instance rather than the default `docs.redhat.com` site.

    To view the **Red Hat documentation server URL** setting in the Satellite web UI, navigate to **Administer > Settings**. The setting is located on the **General** tab.

    [Jira:SAT-31701](https://redhat.atlassian.net/browse/SAT-31701)

Guidelines on expense management for your subscriptions
:   Your procurement team can review the new documentation on managing expenses for your Red Hat subscriptions. For more information, see [Expense management for Red Hat subscriptions](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#expense-management-for-red-hat-subscriptions) in *Overview, concepts, and deployment considerations*.

    Jira:SAT-36021[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#ftn.PrivateTicketFootnote)
