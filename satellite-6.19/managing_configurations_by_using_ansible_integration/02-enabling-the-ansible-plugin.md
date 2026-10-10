---
title: "Enabling the Ansible plugin"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_ansible_integration"
guide_title: "Managing configurations by using Ansible integration"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#enabling-the-ansible-plugin"
---
# Chapter 2. Enabling the Ansible plugin

Before you can use Ansible for configuration management in Satellite, enable Ansible integration in Satellite and on all Capsule Servers that you want to use to run Ansible roles on hosts.

**Procedure**

- On all Capsule Servers that you want to use to run Ansible roles on hosts, enable the Ansible plugin:

  ```
  # satellite-installer --enable-foreman-proxy-plugin-ansible
  ```
