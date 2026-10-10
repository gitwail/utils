---
title: "Fixed issues"
product: "Red Hat Satellite"
version: "6.19"
guide: "release_notes"
guide_title: "Release notes"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#fixed-issues"
---
# Chapter 7. Fixed issues

Red Hat Satellite 6.19 fixes the following bugs that may have previously impacted Red Hat Satellite deployments.

## 7.1. Installation and upgrade

`Red Hat Lightspeed` no longer fails to enable when `Host.NetworkBackend` for Podman is set to `CNI`
:   Before this update, when `Host.NetworkBackend` for Podman was set to Container Network Interface (CNI on a Satellite Server, satellite-installer failed to enable `Red Hat Lightspeed`. The issue occured because the Red Hat Enterprise Linux 9.6 ISO provided a version of the `container-selinux` policy that older than 2.237.0. With this release, the error starting IoP container due to CNI network configuration is resolved.

    [Jira:SAT-39069](https://redhat.atlassian.net/browse/SAT-39069)

Validation no longer fails due to duplicate operating system entries
:   Before this update, Satellite duplicated operating system entries when uploading Puppet facts. As a consequence, uploading facts failed with a validation error, which also affected Leapp upgrades. This release improves how the fact parser handles operating system title uniqueness and prevents duplicate entries. As a result, Satellite correctly reuses existing operating system entries instead of trying to create new ones.

    [Jira:SAT-40641](https://redhat.atlassian.net/browse/SAT-40641)

## 7.2. Security and authentication

Proper session termination in certain API endpoints and enforced reauthentication
:   Before this update, API endpoints that call the `add_smart_proxy_filters` function bypassed user authentication. This was due to improper session termination logic introduced in Satellite 6.18. In addition, user sessions remained active beyond the period specified in the `idle_timeout` setting. This affected the API endpoints related to the following resources:

    - Organizations
    - Repositories
    - Config reports
    - Hosts

    As a consequence, removed and nonexistent users failed due to missing required permissions and not due to failed authentication. In addition, user sessions were not terminated and could access certain endpoints without reauthentication.

    With this release, user sessions no longer bypass authentication and are terminated correctly. As a result, users are forced to reauthenticate to access those resources.

    [Jira:SAT-38951](https://redhat.atlassian.net/browse/SAT-38951)

## 7.3. Content management

Capsules sync correctly after upgrading Satellite Server to 6.18
:   Previously, after upgrading Satellite Server from version 6.17 to version 6.18 while keeping Capsules at version 6.17, Capsule sync started failing. The 6.18.3 update fixes the problem, and 6.17 Capsules sync as expected after upgrading Satellite Server to 6.18.

    [Jira:SAT-41180](https://redhat.atlassian.net/browse/SAT-41180)

Capsule sync no longer fails due to a null value in UUID of a host
:   Before this update, when attempting to sync Capsule in certain setups with an improperly registered host, the sync failed due to a null value in the `uuid` column of the `hosts` database table. This update fixes the issue, and the host UUID is correctly set in the described setups.

    [Jira:SAT-39794](https://redhat.atlassian.net/browse/SAT-39794)

## 7.4. Host provisioning and management

Root password update added to `cloud-init` template for image-based deployment on VMware
:   Before this update, image-based deployment on VMware using Satellite set the root password to the password defined in the VM template, not the password defined in the Host settings during the build process. As a consequence, the root password remained unchanged from the VM template during image-based deployment. With this release, the root password update has been incorporated into the `cloud-init` template. Consequently, the root password changes correctly in accordance with the Host settings in `cloud-init` templates.

    [Jira:SAT-20584](https://redhat.atlassian.net/browse/SAT-20584)

Provisioning RHEL 9 hosts no longer creates unnecessary `localhost.localdomain` entries
:   Before this update, provisioning of RHEL 9 hosts with Foreman discovery image (FDI), PXE-less discovery, and static networking created an unnecessary `localhost.localdomain` entry due to a missing hostname update. With this release, Satellite sets the hostname to the static value before the Red Hat Subscription Manager call. As a result, setting the hostname prevents unnecessary `localhost.localdomain` creation.

    [Jira:SAT-39469](https://redhat.atlassian.net/browse/SAT-39469)

Firmware type in **Compute Profiles** and the **New Host** form no longer reverts to Automatic
:   Before this update, the selected firmware type could be reset to **Automatic** or shown incorrectly in the web UI. This release ensures that the firmware type keeps the correct value.

    [Jira:SAT-31447](https://redhat.atlassian.net/browse/SAT-31447)

Corrected power operations on hosts in Redfish BMC provider
:   Before this update, power operations were implemented in the Redfish provider of the baseboard management controller (BMC) as follows:

    - Cycle – implemented incorrectly
    - Reboot – not implemented
    - Reset – not implemented

    As a consequence, users experienced host shutdown instead of cycle and could not use host reboot or reset. This release fixes implementation of all three operations. As a result, BMC operations work correctly on the Redfish provider.

    [Jira:SAT-37871](https://redhat.atlassian.net/browse/SAT-37871)

Incomplete **Create host** form on OpenShift Virtualization no longer duplicates disks
:   Before this update, submitting a **Create host** form on an OpenShift Virtualization compute resource with a validation error, such as an empty required field, caused additional virtual disks to be added on the **Virtual machine** tab. This might also have caused host creation failures.

    This update fixes the issue. The disk configuration remains unchanged when validation fails, and prevents disk duplication.

    [Jira:SAT-42730](https://redhat.atlassian.net/browse/SAT-42730)

## 7.5. Users and roles

External users can now log in to Satellite without specifying an email address
:   Previously, external users, such as users defined in Identity Management or Active Directory, were unable to log in to Satellite without an email address. With this update, external users can log in to Satellite even when their user account does not include an email address. Note that if the `Mail Enabled` option is enabled for a user account in the Satellite web UI, the user is still prompted to enter an email address.

    [Jira:SAT-23437](https://redhat.atlassian.net/browse/SAT-23437)

## 7.6. Red Hat Lightspeed

`hammer ping` correctly lists Red Hat Lightspeed services in Satellite
:   Before this update, with Red Hat Lightspeed in Satellite enabled, the `hammer ping` command did not display the Advisor and Vulnerability services. Additionally, some web UI elements, such as the **Recommendations** tab on host details and the **Recommendations** list page behaved as in a non-Red Hat Lightspeed in Satellite setup.

    This update fixes the problem, and `hammer ping` correctly displays the Advisor and Vulnerability services.

    [Jira:SAT-39088](https://redhat.atlassian.net/browse/SAT-39088)

Tag generation works with `Any location`
:   Before this update, accessing the Recommendations or Vulnerabilities menu produced an error message when the location was set to `Any location`. As a consequence, users could not see a global view of all systems in **Recommendations** or **Vulnerabilities**. This update adds support for forwarding Insights Cloud UI requests when the session has no location selected. Tag generation works when the location is not set by using a wildcard location tag and relaxing host filtering on location. As a result, you can access the Recommendations or Vulnerabilities menu without selecting a location.

    [Jira:SAT-38683](https://redhat.atlassian.net/browse/SAT-38683)

"Sync all inventory status" no longer fails with Red Hat Lightspeed
:   Before this update, with Red Hat Lightspeed enabled, performing the **Sync all inventory status** operation on the **Inventory Upload** page could fail with an error similar to the following:

    ```
    Could not get task details: TypeError: Cannot read properties of undefined (reading 'sync')
    ```

    This update adds inventory synchronization in IOP mode, hides cloud-specific UI components that are not relevant in local Advisor Engine environments, and has fixed the issue. The **Inventory Upload** page and its controls are adjusted for environments that use Red Hat Lightspeed, and using **Sync all inventory status** no longer produces this error.

    [Jira:SAT-36556](https://redhat.atlassian.net/browse/SAT-36556)

Recommendations and Vulnerabilities no longer fail to switch hosts
:   Before this update, when switching between hosts by using the breadcrumb switcher on the host details page, the **Recommendations** and **Vulnerabilities** tabs did not update to reflect the newly selected host.

    With this update, this issue is fixed for cases where you switch between two registered hosts with Red Hat Lightspeed.

    However, if you switch from a host that is registered to Red Hat Lightspeed to a host that is not registered, you might still encounter a blank screen and loading spinner instead of being redirected to the **Overview** tab. To work around this problem, reload the page.

    [Jira:SAT-38703](https://redhat.atlassian.net/browse/SAT-38703)
