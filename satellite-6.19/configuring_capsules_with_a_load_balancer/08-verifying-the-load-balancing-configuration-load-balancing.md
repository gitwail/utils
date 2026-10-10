---
title: "Verifying the load balancing configuration"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#Verifying_the_Load_Balancing_Configuration_load-balancing"
---
# Chapter 8. Verifying the load balancing configuration

Verify the load balancing configuration for each Capsule Server to ensure content and registration keep working when one server is unavailable.

**Procedure**

1. Shut down the base operating system for your Capsule Server.
2. Verify that content or subscription management features are available on clients registered to this Capsule. For example, enter the `subscription-manager refresh` command on a client.
3. Restart the base operating system for your Capsule Server.
