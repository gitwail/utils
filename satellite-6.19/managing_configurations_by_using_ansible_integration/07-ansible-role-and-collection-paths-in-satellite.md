---
title: "Ansible role and collection paths in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_ansible_integration"
guide_title: "Managing configurations by using Ansible integration"
chapter_number: "A"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#ansible-role-and-collection-paths-in-satellite"
---
# Appendix A. Ansible role and collection paths in Satellite

Satellite imports and runs Ansible roles and collections from specific system paths. System-installed roles and collections are located in `/usr/share/ansible`, while custom roles and collections should be placed in `/etc/ansible`.

Satellite imports and runs Ansible roles from the following paths:

- `/etc/ansible/roles`
- `/usr/share/ansible/roles`
- `/etc/ansible/collections`
- `/usr/share/ansible/collections`

Roles and collections from installed packages are placed under `/usr/share/ansible`. If you want to add custom roles or collections, place them under `/etc/ansible`.

Note that Red Hat provides support only for Ansible roles and collections obtained from Red Hat.

**Additional resources**

- [Synchronizing Ansible Collections in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-ansible-collections)
- [Consuming content from an Ansible Collection Repository in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#consuming-content-from-an-ansible-collection-repository)
