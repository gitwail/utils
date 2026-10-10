---
title: "Technology Preview features"
product: "Red Hat Satellite"
version: "6.19"
guide: "release_notes"
guide_title: "Release notes"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#technology-preview-features"
---
# Chapter 3. Technology Preview features

Explore Technology Preview features available in Red Hat Satellite 6.19.

For information on Red Hat scope of support for Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

## 3.1. Model Context Protocol

MCP server is available for Satellite (Technology Preview)
:   Satellite provides a container image that you can use to run a Model Context Protocol (MCP) server locally. The MCP server for Satellite is designed for advanced reporting and data analysis that leverages AI capabilities. You can use it to generate dynamic and comprehensive reports from your Satellite inventory. With the container image provided with Satellite 6.19, you can also use MCP to patch hosts and incrementally update, publish, and promote content views. For more information on this update, see [Jira:SAT-40970](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#Jira-SAT-40970).

    For more information on MCP for Satellite, see [Connecting AI applications to the MCP server for Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.18/html-single/managing_hosts/index#connecting-ai-applications-to-the-mcp-server-for-satellite).

    [Jira:SAT-35530](https://redhat.atlassian.net/browse/SAT-35530)

## 3.2. Host provisioning and management

OpenShift Virtualization plugin (Technology Preview)
:   You can provision virtual machines by using the OpenShift Virtualization plugin. For more information, see [Provisioning hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Provisioning_Virtual_Machines_Kubevirt_kubevirt-provisioning).

    Jira:SAT-18663[[1]](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#ftn.PrivateTicketFootnote)

Red Hat OpenShift Virtualization compute resource enhancements
:   This update introduces many fixes and improvements for the Red Hat OpenShift Virtualization compute resource, which is a Technology Preview feature. This improves the stability and usability of this feature.

    [Jira:SAT-41368](https://redhat.atlassian.net/browse/SAT-41368)

Kernel execution template (Technology Preview)
:   You can use the kernel execution (`kexec`) provisioning template for PXE-less boot methods. For more information, see [Discovery in PXE-less mode](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#discovery-in-pxeless-mode).

    [Jira:SAT-21012](https://redhat.atlassian.net/browse/SAT-21012)
