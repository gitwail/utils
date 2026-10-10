---
title: "Removed features"
product: "Red Hat Satellite"
version: "6.19"
guide: "release_notes"
guide_title: "Release notes"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#removed-features"
---
# Chapter 5. Removed features

The following functionalities are removed in Red Hat Satellite 6.19.

## 5.1. Server administration

Legacy Content Host Details page and related API endpoints are removed
:   The legacy Content Host Details page is removed. The `auto_attach` parameter is removed from the following endpoints:

    - `PUT /activation_keys/:id`
    - `POST /activation_keys`
    - `POST /activation_keys/:id/copy`

    The following API endpoints are removed entirely:

    - `PUT /activation_keys/:id/add_subscriptions`
    - `PUT /activation_keys/:id/remove_subscriptions`
    - `PUT /hosts/:host_id/subscriptions/auto_attach`
    - `PUT /hosts/:host_id/subscriptions/add_subscriptions`
    - `PUT /hosts/:host_id/subscriptions/remove_subscriptions`
    - `PUT /hosts/bulk/remove_subscriptions`
    - `PUT /hosts/bulk/add_subscriptions`
    - `PUT /hosts/bulk/auto_attach`

    Check that your automation does not use any of the removed endpoints.

    Jira:SAT-21227[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#ftn.PrivateTicketFootnote)

## 5.2. Host provisioning and management

GRUB Legacy is removed from provisioning
:   GRUB Legacy, also known as GRUB version 1, is removed from provisioning. GRUB 1 was used in RHEL versions prior to RHEL 7. Current distributions use GRUB 2 and are not affected by the deprecation. Systems that were upgraded from an older version might contain obsolete GRUB 1 files and templates.

    [Jira:SAT-38784](https://redhat.atlassian.net/browse/SAT-38784)

Content Host UI and package group actions in the web UI are removed
:   The Content Host UI is removed. This includes all pages under **Hosts** > **Content Hosts**. As an alternative, use the new UI at **Hosts** > **All Hosts**.

    Package group actions in the web UI are removed. As an alternative, use the **Run Command** remote execution job template.

    [Jira:SAT-37927](https://redhat.atlassian.net/browse/SAT-37927)

## 5.3. Users and roles

Overriding organizations and locations on the filter level is no longer available
:   You can no longer specify organizations and locations when editing a permission filter. Filters now always inherit the organizations and locations set at the role level. The web UI form for editing a filter no longer includes the **Override** and **Unlimited** checkboxes. You can still add a search to the filter as long as the selected resource type supports granular filtering.

    [Jira:SAT-28731](https://redhat.atlassian.net/browse/SAT-28731), [Jira:SAT-28820](https://redhat.atlassian.net/browse/SAT-28820)
