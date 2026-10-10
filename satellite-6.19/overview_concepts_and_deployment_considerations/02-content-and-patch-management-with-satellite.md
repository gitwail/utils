---
title: "Content and patch management with Red Hat Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#content-and-patch-management-with-satellite"
---
# Chapter 2. Content and patch management with Red Hat Satellite

With Red Hat Satellite, you can provide content and apply patches to hosts systematically in all lifecycle stages.

## 2.1. Content flow in Red Hat Satellite

Content flow in Red Hat Satellite involves management and distribution of content from external sources to hosts.

Content in Satellite flows from *external content sources* to *Satellite Server*. *Capsule Servers* mirror the content from Satellite Server to *hosts*.

External content sources
:   You can configure many content sources with Satellite. The supported content sources include the Red Hat Customer Portal, custom Yum repositories, Git repositories, Ansible collections, container registries, SCAP repositories, or internal data stores of your organization.

**Satellite Server**
:   On your Satellite Server, you plan and manage the content lifecycle.

**Capsule Servers**
:   By creating Capsule Servers, you can establish content sources in various locations based on your needs. For example, you can establish a content source for each geographical location or multiple content sources for a data center with separate networks.

**Hosts**
:   By assigning a host system to a Capsule Server or directly to your Satellite Server, you ensure the host receives the content they provide. Hosts can be physical or virtual.

[Image: Content flow in Red Hat Satellite](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/cdd570403c72645373219722627c83e0/system-architecture-satellite.png)

**Additional resources**

- [Chapter 5, *Major Satellite components*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Major-Satellite-Components_planning "Chapter 5. Major Satellite components")
- [Managing Red Hat subscriptions in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Red_Hat_Subscriptions_content-management)

## 2.2. Content views in Red Hat Satellite

A content view is a deliberately curated subset of content that your hosts can access. By creating a content view, you can define the software versions used by a particular environment or Capsule Server.

Each content view creates a set of repositories across each environment. Your Satellite Server stores and manages these repositories. For example, you can create content views in the following ways:

- A content view with older package versions for a production environment and another content view with newer package versions for a *Development* environment.
- A content view with a package repository required by an operating system and another content view with a package repository required by an application.
- A composite content view for a modular approach to managing content views. For example, you can use one content view for content for managing an operating system and another content view for content for managing an application. By creating a composite content view that combines both content views, you create a new repository that merges the repositories from each of the content views. However, the repositories for the content views still exist and you can keep managing them separately as well.

  Default Organization View
  :   A *Default Organization View* is an application-controlled content view for all content that is synchronized to Satellite. You can register a host to the *Library* environment on Satellite to consume the *Default Organization View* without configuring content views and lifecycle environments.

  Promoting a content view across environments
  :   When you promote a content view from one environment to the next environment in the application lifecycle, Satellite updates the repository and publishes the packages.

**Example 2.1. Promoting a package from *Development* to *Testing***

The repositories for *Testing* and *Production* contain the `my-software-1.0-0.noarch.rpm` package:

|  | Development | Testing | Production |
| --- | --- | --- | --- |
| Version of the content view | Version 2 | Version 1 | Version 1 |
| Contents of the content view | *my-software*-1.1-0.noarch.rpm | *my-software*-1.0-0.noarch.rpm | *my-software*-1.0-0.noarch.rpm |

If you promote Version 2 of the content view from *Development* to *Testing*, the repository for *Testing* updates to contain the `my-software-1.1-0.noarch.rpm` package:

|  | Development | Testing | Production |
| --- | --- | --- | --- |
| Version of the content view | Version 2 | **Version 2** | Version 1 |
| Contents of the content view | *my-software*-1.1-0.noarch.rpm | ***my-software*-1.1-0.noarch.rpm** | *my-software*-1.0-0.noarch.rpm |

This ensures hosts are designated to a specific environment but receive updates when that environment uses a new version of the content view.

**Additional resources**

- [Managing content views and content view environments in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-views-and-content-view-environments)

## 2.3. Lifecycle environments and environment paths

Application lifecycles are divided into lifecycle environments which represent each stage of the application lifecycle. By linking lifecycle environments, you create an environment path.

You can promote content along the environment path to the next lifecycle environment when required. When you promote a content view from one environment to the next environment in the application lifecycle, Satellite updates the repository and publishes the packages. For example, if development ends on a particular version of an application, you can promote this version to the testing environment and start development on the next version.

**Figure 2.1. An environment path containing four environments**

[Image: An environment path containing four environments](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/b97e048dbc07c162427b31b140c5e345/lifecycle-satellite.png)

## 2.4. Content types in Red Hat Satellite

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
