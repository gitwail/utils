---
title: "Overview"
product: "Red Hat Satellite"
version: "6.19"
guide: "release_notes"
guide_title: "Release notes"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#assembly_overview"
---
# Chapter 1. Overview

Release notes include links to the original tickets. Private tickets have no links and instead feature the following footnote[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#ftn.PrivateTicketFootnote).

## 1.1. Advisories

You can view [all advisories](https://access.redhat.com/errata-search/?q=&p=1&sort=portal_publication_date+desc&rows=10&portal_product=Red%5C+Hat%5C+Satellite&portal_product_version=6.19), including security and bug fixes, for major and minor versions of this release on the Red Hat Customer Portal.

## 1.2. Major changes in Red Hat Satellite 6.19

Red Hat Satellite 6.19 introduces the following major changes:

- Red Hat Lightspeed vulnerability service in Satellite (previously a Technology Preview feature) is fully supported. Additionally, the feature receives enhancements, such as improved role-based access control and control over vulnerability analysis on hosts ([Section 2.2, “Red Hat Lightspeed”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#new-features-and-enhancements-red-hat-lightspeed "2.2. Red Hat Lightspeed")).
- Satellite provides Puppet functionality through OpenVox packages ([SAT-31648](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#Jira-SAT-31648)).
- Transient packages on image mode hosts are now tracked ([SAT-30671](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#Jira-SAT-30671), [SAT-36790](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#Jira-SAT-36790)).
- SSH certificates are supported for remote execution ([SAT-28038](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#Jira-SAT-28038)).
- Multiple content view (CV) environments in hosts and activation keys (previously a Technology Preview feature) are fully supported. Additionally, support for multiple CV environments in hosts and activation keys in the Web UI is enhanced ([SAT-26055](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#Jira-SAT-26055)).
- Satellite MCP server (Technology Preview) can be granted write permissions, with which it can incrementally update, publish, and promote content views ([SAT-40970](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#Jira-SAT-40970)).
- The OpenShift Virtualization plugin (Technology Preview) benefits from improved stability and usability ([SAT-41368](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#Jira-SAT-41368)).

For a complete list of changes in this release, see the following sections.

## 1.3. Red Hat Satellite

With Red Hat Satellite, you can deploy, configure, and maintain your systems across physical, virtual, and cloud environments. Red Hat Satellite provides provisioning, remote management and monitoring of multiple Red Hat Enterprise Linux deployments with a single, centralized tool.

- *Red Hat Satellite Server* synchronizes content from the Red Hat Customer Portal and other sources. It provides detailed lifecycle management, user and group role-based access control, integrated subscription management, and advanced GUI, CLI, and API access.
- *Red Hat Satellite Capsule Server* mirrors content from the Red Hat Satellite Server and distributes it to different geographical locations. Host systems pull content and configurations from the Capsule Server in their location instead of the central Satellite Server. The Capsule Server also provides localized services such as Puppet server, DHCP, DNS, or TFTP, assisting in scaling Red Hat Satellite as the number of managed systems in your environment grows.

## 1.4. Additional resources

- [Red Hat Satellite product life cycle](https://access.redhat.com/support/policy/updates/satellite?extIdCarryOver=true&sc_cid=7013a000002q6eLAAQ) describes the time period for each major version and its level of maintenance.
- [Satellite 6 component versions](https://access.redhat.com/articles/1343683) describes upstream core components, Foreman plugins, and integrated projects.
- [*Overview, concepts, and deployment considerations*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#) describes Red Hat Satellite concepts, components, tools, and deployment planning.
- [Supported usage and versions of Satellite components](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Supported-Usage-and-Versions-of-Project-Components_planning) in *Overview, concepts, and deployment considerations* describes supported client architectures for content management, host provisioning, and configuration management.

---

[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#PrivateTicketFootnote)
This ticket does not have a link because it is private.
