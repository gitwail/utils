---
title: "Introduction to content management"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Introduction_to_Content_Management_content-management"
---
# Chapter 1. Introduction to content management

You can manage the software lifecycle for your Red Hat Enterprise Linux hosts by organizing various types of content from various sources. Manage subscription information, base operating systems, middleware services, and end-user applications to maintain reliable and up-to-date host environments.

## 1.1. Content management capabilities in Red Hat Satellite

Understand how Red Hat Satellite groups subscription-related work and repository content so you can plan imports, lifecycle environments, and host access.

Red Hat Satellite provides the following management capabilities:

Subscription management
:   This provides organizations with a method to manage their Red Hat subscription information.

Content management
:   This provides organizations with a method to store Red Hat content and organize it in various ways. In the context of Satellite, *content* is defined as the software installed on hosts.

## 1.2. Content types in Red Hat Satellite

You can import and manage various content types, such as packages and ISO images, in Red Hat Satellite. Organize both Red Hat and custom content into products to streamline your software distribution.

For example, Satellite supports the following content types:

RPM packages
:   Import RPM packages from repositories related to your Red Hat subscriptions. Satellite Server downloads the RPM packages from the Red Hat Content Delivery Network and stores them locally. You can use these repositories and their RPM packages in content views.

Kickstart trees
:   Import the Kickstart trees to provision a host. New systems access these Kickstart trees over a network to use as base content for their installation. Red Hat Satellite contains predefined Kickstart templates. You can also create your own Kickstart templates.

ISO and KVM images
:   Download and manage media for installation and provisioning. For example, Satellite downloads, stores, and manages ISO images and guest images for specific Red Hat Enterprise Linux and non-Red Hat operating systems.

Custom file type
:   Manage custom content for any type of file you require, such as SSL certificates, ISO images, and OVAL files.
