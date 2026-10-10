---
title: "Overview of load balancing in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#overview-of-load-balancing-in-project_load-balancing"
---
# Chapter 1. Overview of load balancing in Satellite

You can configure your Satellite environment to use a load balancer to distribute host requests across multiple Capsule Servers. This improves performance and keeps host connections working when one Capsule Server is unavailable.

## 1.1. Components of a load-balanced setup

When you configure your Satellite environment for load balancing, several components interact to distribute traffic and provide high availability.

A load-balanced setup in a Satellite environment consists of the following components:

- Satellite Server
- Two or more Capsule Servers
- A load balancer
- Multiple hosts

A host sends a request to the TCP load balancer. The load balancer receives the request and determines which Capsule Server will handle the request to ensure optimal performance and availability.

**Figure 1.1. Components of a load-balanced setup**

[Image: Components of a load-balanced setup](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Configuring_Capsules_with_a_load_balancer-en-US/images/55913b152c4641ed072e597b73ef483f/load-balancing-architecture-satellite.png)

## 1.2. Services and features supported in a load-balanced setup

A load balancer in Satellite distributes load only for selected services and features. The services listed below are supported for load balancing and will continue to work when one Capsule Server is unavailable.

The following services and features are supported for load balancing:

- Registering hosts
- Providing content to hosts
- Configuring hosts by using Puppet

Other Satellite services, such as provisioning, `virt-who`, or remote execution, go directly through the individual Capsules on which these services are running.

## 1.3. Additional maintenance required for load balancing

Configuring Capsules to use a load balancer results in a more complex environment and requires additional maintenance.

The following additional steps are required for load balancing:

- You must ensure that all Capsules have the same content. If you publish a content view version on Satellite, synchronize it to all Capsule Servers.
- You must upgrade each Capsule in sequence.
