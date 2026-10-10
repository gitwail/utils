---
title: "Common deployment scenarios"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "12"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#common-deployment-scenarios"
---
# Chapter 12. Common deployment scenarios

This section provides a brief overview of common deployment scenarios for Red Hat Satellite. Note that many variations and combinations of the following layouts are possible.

## 12.1. Single location with segregated subnets

If your infrastructure requires multiple isolated networks in one geographic location, you can create segregated subnets and manage them with a single Capsule.

Your infrastructure might require multiple isolated subnets even if Red Hat Satellite is deployed in a single geographic location. This can be achieved for example by deploying multiple Capsule Servers with DHCP and DNS services, but the recommended way is to create segregated subnets using a single Capsule. This Capsule is then used to manage hosts and compute resources in those segregated networks to ensure they only have to access the Capsule for provisioning, configuration, errata, and general management.

## 12.2. Multiple locations

Create at least one Capsule Server per geographic location to save bandwidth by having hosts obtain content locally. Only your Capsule Server synchronizes content from remote repositories, making your provisioning infrastructure more reliable and easier to configure.

Red Hat recommends to create at least one Capsule Server per geographic location. This practice can save bandwidth since hosts obtain content from a local Capsule Server. Synchronization of content from remote repositories is done only by the Capsule, not by each host in a location. In addition, this layout makes the provisioning infrastructure more reliable and easier to configure.

[Image: Content flow in Red Hat Satellite](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/cdd570403c72645373219722627c83e0/system-architecture-satellite.png)

## 12.3. Content view scenarios

You can organize content views and lifecycle environments to match your workflow, from simple single-environment setups to complex application-specific paths that enable individual release cycles and testing before production deployment.

The following section provides general scenarios for deploying content views as well as lifecycle environments.

The default lifecycle environment called **Library** gathers content from all connected sources. It is not recommended to associate hosts directly with the Library as it prevents any testing of content before making it available to hosts. Instead, create a lifecycle environment path that suits your content workflow. The following scenarios are common:

- **A single lifecycle environment** – content from Library is promoted directly to the production stage. This approach limits the complexity but still allows for testing the content within the Library before making it available to hosts.

  [Image: A single lifecycle environment](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/cbdb8f1001072ed394a55669bdd3fc32/lifecycle-path-basic-satellite.png)
- **A single lifecycle environment path** – both operating system and applications content is promoted through the same path. The path can consist of several stages, which enables thorough testing but requires additional effort. For example, you can use the **Development**, **QA**, and **Production** stages.

  [Image: A single lifecycle environment path](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/24a8e14aa5084fd0cbd95a17a2106245/lifecycle-path-simple-satellite.png)
- **Application specific lifecycle environment paths** – each application has a separate path, which allows for individual application release cycles. You can associate specific compute resources with application lifecycle stages to facilitate testing. However, this scenario increases the maintenance complexity.

  [Image: Application specific lifecycle environment paths](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/c7a66a9de74bf887a2705f5e55178637/lifecycle-path-diverged-satellite.png)

The following content view scenarios are common:

- **All in one content view** – a content view that contains all necessary content for the majority of your hosts. Reducing the number of content views is an advantage in deployments with constrained resources (time, storage space) or with uniform host types. However, this scenario limits the content view capabilities such as time based snapshots or intelligent filtering. Any change in content sources affects a proportion of hosts.
- **Host specific content view** – a dedicated content view for each host type. This approach can be useful in deployments with a small number of host types (up to 30). However, it prevents sharing content across host types as well as separation based on criteria other than the host type, for example, between operating system and applications. With critical updates every content view has to be updated, which increases maintenance efforts.
- **Host specific composite content view** – a dedicated combination of content views for each host type. This approach enables separating host specific and shared content, for example you can have dedicated content views for the operating system and application content. By using a composite, you can manage your operating system and applications separately and at different frequencies.
- **Component based content view** – a dedicated content view for a specific application. For example a database content view can be included into several composite content views. This approach allows for greater standardization but it leads to an increased number of content views.

The optimal solution depends on the nature of your host environment. Avoid creating a large number of content views, but keep in mind that the size of a content view affects the speed of related operations (publishing, promoting). Also make sure that when creating a subset of packages for the content view, all dependencies are included as well. Note that Kickstart repositories should not be added to content views, as they are used for host provisioning only.

## 12.4. Satellite Server with multiple manifests

You can use many Red Hat Network subscription manifests in one Satellite Server to manage systems from different Red Hat Network accounts or entities. This allows you to assign subscriptions to separate organizations and manage those organizations independently.

If you plan to have more than one Red Hat Network account, or if you want to manage systems belonging to another entity that is also a Red Hat Network account holder, then you and the other account holder can assign subscriptions, as required, to manifests. A customer that does not have a Satellite subscription can create a Subscription Asset Manager manifest, which can be used with Satellite, if they have other valid subscriptions. You can then use the multiple manifests in one Satellite Server to manage multiple organizations.

If you must manage systems but do not have access to the subscriptions for the RPMs, you must use Red Hat Enterprise Linux Satellite Add-On.

The following diagram shows two Red Hat Network account holders, who want their systems to be managed by the same Satellite installation. In this scenario, Example Corporation 1 can allocate any subset of their 60 subscriptions, in this example they have allocated 30, to a manifest. This can be imported into the Satellite as a distinct Organization. This allows system administrators the ability to manage Example Corporation 1’s systems using Satellite completely independently of Example Corporation 2’s organizations (R&D, Operations, and Engineering).

**Figure 12.1. Satellite Server with multiple manifests**

[Image: Satellite Server with multiple manifests](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/49f8aed74acd3f56bde5d625ef009c60/server-multiple-manifests-satellite.png)

When creating a Red Hat subscription manifest:

- Add the subscription for Satellite Server to the manifest if planning a disconnected or self-registered Satellite Server. This is not necessary for a connected Satellite Server that is subscribed using the Subscription Manager utility on the base system.
- Add subscriptions for all Capsule Servers you want to create.
- Add subscriptions for all Red Hat products you want to manage with Satellite.
- Note the date when the subscriptions are due to expire and plan for their renewal before the expiry date.
- Create one manifest per organization. You can use multiple manifests and they can be from different Red Hat subscriptions.

Red Hat Satellite allows the use of future-dated subscriptions in the manifest. This enables uninterrupted access to repositories when future-dated subscriptions are added to a manifest before the expiry date of existing subscriptions.

Note that the Red Hat subscription manifest can be modified and reloaded to Satellite Server in case of any changes in your infrastructure, or when adding more subscriptions. Manifests should not be deleted. If you delete the manifest from the Red Hat Customer Portal or in the Satellite web UI it will unregister all of your hosts.

**Additional resources**

- [Satellite Add-On](https://www.redhat.com/en/technologies/management/satellite)

## 12.5. Host group structures

You can organize host groups by using flat, lifecycle environment-based, application-based, or location-based structures to simplify maintenance of host settings and match your workflow. Nested groups inherit parameters from parent groups.

The fact that host groups can be nested to inherit parameters from each other allows for designing host group hierarchies that fit particular workflows. A well planned host group structure can help to simplify the maintenance of host settings. This section outlines four approaches to organizing host groups.

**Figure 12.2. Host group structuring examples**

[Image: Host group structuring examples](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/53c9e37fa1385bf4f35d6794c6b6789c/host-group-structures-satellite.png)

Flat structure
:   The advantage of a flat structure is limited complexity, as inheritance is avoided. In a deployment with few host types, this scenario is the best option. However, without inheritance there is a risk of high duplication of settings between host groups.

Lifecycle environment based structure
:   In this hierarchy, the first host group level is reserved for parameters specific to a lifecycle environment. The second level contains operating system related definitions, and the third level contains application specific settings. Such structure is useful in scenarios where responsibilities are divided among lifecycle environments. For example, if there is a dedicated owner for the **Development**, **QA**, and **Production** lifecycle stages.

Application based structure
:   This hierarchy is based on roles of hosts in a specific application. For example, it enables defining network settings for groups of back-end and front-end servers. The selected characteristics of hosts are segregated, which supports Puppet-focused management of complex configurations. However, the content views can only be assigned to host groups at the bottom level of this hierarchy.

Location based structure
:   In this hierarchy, the distribution of locations is aligned with the host group structure. In a scenario where the location or Capsule Server topology determines many other attributes, this approach is the best option. However, this structure complicates sharing parameters across locations, therefore in complex environments with a large number of applications, the number of host group changes required for each configuration change increases significantly.

## 12.6. Inter-Satellite Synchronization scenarios

You can use Inter-Satellite Synchronization to synchronize content between Satellite Servers, including air-gapped servers. In these scenarios, you copy selected content views or all Library content from an upstream server to downstream servers over a network or through physical export.

Red Hat Satellite uses Inter-Satellite Synchronization (ISS) to synchronize content between two Satellite Servers including those that are air gapped.

You can use ISS in cases such as:

- If you want to copy some but not all content from your Satellite Server to other Satellite Servers. For example, you have content views that your IT department consumes from Satellite Server, and you want to copy content from those content views to other Satellite Servers.
- If you want to copy all Library content from your Satellite Server to other Satellite Servers. For example, you have products and repositories that your IT department consumes from Satellite Server in the Library, and you want to copy all products and repositories in that organization to other Satellite Servers.

> **Note**
>
> You cannot use ISS to synchronize content from Satellite Server to Capsule Server. Capsule Server supports synchronization natively.

There are different ways of using ISS. The way you can use depends on your multi-server setup that can fall to one of the following scenarios.

In a disconnected scenario, there is the following setup:

- The upstream Satellite Server is connected to the internet. This server consumes content from the Red Hat Content Delivery Network (CDN) or custom sources.
- The downstream Satellite Server is completely isolated from all external networks.
- The downstream Satellite Server can communicate with a connected upstream Satellite Server over an internal network.

**Figure 12.3. Satellite ISS disconnected scenario**

[Image: Satellite ISS disconnected scenario](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/f6363cbd6a5ef19b97ce0c1723a3bd86/iss-disconnected-satellite.png)

You can configure your downstream Satellite Server to synchronize content from the upstream Satellite Server over the network.

In an air-gapped scenario, there is the following setup:

- The upstream Satellite Server is connected to the internet. This server consumes content from the Red Hat CDN or custom sources.
- The downstream Satellite Server is completely isolated from all external networks.
- The downstream Satellite Server does not have a network connection to a connected upstream Satellite Server.

**Figure 12.4. Satellite ISS air-gapped scenario**

[Image: Satellite ISS air-gapped scenario](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/409f4b6b5fe180eb82320fa032a37fb0/iss-airgapped-satellite.png)

The only way for an air-gapped downstream Satellite Server to receive content updates is by exporting payload from the upstream Satellite Server, bringing it physically to the downstream Satellite Server, and importing the payload.

You can configure your downstream Satellite Server to synchronize content by using exports.

**Additional resources**

- [Synchronizing Content Between Satellite Servers in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Synchronizing_Content_Between_Servers_content-management)

## 12.7. Deploying Satellite on AWS

You can deploy Satellite Server, Capsule Servers, and hosts in Amazon Web Services (AWS) using various configurations. Options range from simple single-region setups to multi-region deployments with VPN connections or direct connections between on-premises and cloud environments.

You can run Satellite Server, Capsule Servers, and hosts in your Amazon Web Services (AWS) environment. You can deploy Satellite on Amazon Web Services (AWS) in several scenarios.

One-region setup
:   This is the least complex configuration of Satellite in AWS. Deploy both Satellite Server and the hosts residing within the same region and within the Virtual Private Cloud (VPC) You can also use a different availability zone.

    **Figure 12.5. One-region setup**

    [Image: One-region setup](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/1c0a5c30c9f4c1d264661230a36308d0/aws-one-region-setup-satellite.png)

Connecting on-premises and AWS region
:   Create a VPN connection between the on-premises location and the AWS region where your Capsule Server is located. It is also possible to use the external host name of Satellite Server when you register the instance that runs Capsule.

    **Figure 12.6. Site-to-site VPN connection between the AWS region and the on-premises data center**

    [Image: Site-to-site VPN connection between the AWS region and the on-premises data center](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/d56e4f979ca5f3c450918be7f37ea335/aws-combined-vpn-satellite.png)

    **Figure 12.7. Direct connection using the external DNS host name**

    [Image: Direct connection using the external DNS host name](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/dc209fe0d8c931359c85c24599346415/aws-combined-direct-satellite.png)

Connecting different regions
:   Create a site-to-site VPN connection between different regions so that you can use the internal DNS host name when you register the instance that runs Capsule to Satellite Server. If you do not establish a site-to-site VPN connection, use the external DNS host name when you register the instance that runs Capsule to Satellite Server.

    > **Note**
    >
    > Most public cloud providers do not charge for data being transferred into a region or between availability zones within a single region. However, they charge for data leaving the region to the internet.

    **Figure 12.8. Site-to-site VPN connection between AWS regions**

    [Image: Site-to-site VPN connection between AWS regions](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/293e45843c99da0e0795ae9eef18d388/aws-multi-region-vpn-satellite.png)

    **Figure 12.9. Direct connection using the external DNS host name**

    [Image: Direct connection using the external DNS host name](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/32e1ffbc2768041673a404f4444e78ae/aws-multi-region-direct-satellite.png)
