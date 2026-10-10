---
title: "Configuration management with Ansible in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_ansible_integration"
guide_title: "Managing configurations by using Ansible integration"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#configuration-management-with-ansible-in-satellite"
---
# Chapter 1. Configuration management with Ansible in Satellite

By using Ansible as a configuration management tool in Satellite, you can define the desired state of your hosts and maintain it over time. Satellite combines Ansible features with recurring job runs and centralized orchestration, which helps you manage host configurations consistently.

## 1.1. High-level steps for configuration management with Ansible

You use Ansible roles to define the desired state of the hosts registered to Satellite. Running the roles enforces the configuration.

Configuration management with Ansible involves the following high-level steps:

1. Import Ansible roles into Satellite.
2. Assign specific roles to a host or host group.
3. Optional: Override Ansible variables per host or host group in Satellite.
4. Run the roles on the host or host group.

As a result, your hosts maintain a consistent configuration over time. The Ansible roles become a part of their definition.

> **Note**
>
> Running an Ansible role on a host triggers a remote execution job in the background but the use case is different. The typical use case for a remote execution job is to run an ad-hoc task or orchestration. The typical use case for configuration management by using Ansible and Ansible roles is long-term state management.

**Additional resources**

- [Configuring and setting up remote jobs in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs)

## 1.2. Ansible versions supported for integration with Satellite

Satellite repositories include `ansible-core` as a packaged dependency, which determines the version supported for integration with Satellite.

Satellite repositories include `ansible-core` as a packaged dependency for Ansible integration with Satellite Server and Capsule Servers. The supported version of Ansible is `ansible-core` 2.16.
