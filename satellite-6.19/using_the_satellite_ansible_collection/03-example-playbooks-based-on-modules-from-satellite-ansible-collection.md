---
title: "Example playbooks based on modules from Satellite Ansible Collection"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_ansible_collection"
guide_title: "Using the Satellite Ansible Collection"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#example-playbooks-based-on-modules-from-satellite-ansible-collection"
---
# Chapter 3. Example playbooks based on modules from Satellite Ansible Collection

These examples show how to create playbooks that use Satellite Ansible Collection modules to automate tasks against the Satellite API.

All playbooks based on modules from Satellite Ansible Collection must include parameters detailing how to connect to the Satellite API. The following examples use Ansible vault and module defaults group to provide these parameters, and they authenticate using a username and password.

## 3.1. Help resources for example playbooks from Satellite Ansible Collection

You can use the following resources when you create example playbooks based on Satellite Ansible Collection modules.

- [Chapter 2, *Creating a playbook with modules from Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#creating-a-playbook-with-modules-from-satellite-ansible-collection "Chapter 2. Creating a playbook with modules from Satellite Ansible Collection")
- Use the `ansible-doc --list redhat.satellite` command to display the Satellite Ansible modules installed on your system.
- See [Red Hat Ansible Automation Platform](https://console.redhat.com/ansible/automation-hub/repo/published/redhat/satellite/docs) for a complete list of Satellite Ansible modules and other related information.

## 3.2. Playbook example: Enable repositories and create a content view

This is an example playbook for enabling repositories and creating a content view.

This example playbook uses the following modules:

- `redhat.satellite.repository_set`
- `redhat.satellite.content_view`

The playbook ensures RHEL 9 repositories are enabled and a content view that contains these repositories exists.

Before you run this playbook, ensure that you have uploaded a manifest and can access the Red Hat CDN.

```
- name: Ensure RHEL 9 repositories are enabled and a content view exists
  hosts: localhost
  vars_files:
    - My_Vault.yml
  module_defaults:
    group/redhat.satellite.satellite:
      username: "{{ My_Username }}"
      password: "{{ My_Password }}"
      server_url: "{{ My_Server_URL }}"
  tasks:
    - name: Ensure RHEL 9 BaseOS repositories are enabled
      redhat.satellite.repository_set:
        name: "Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)"
        organization: "Default Organization"
        product: "Red Hat Enterprise Linux for x86_64"
        repositories:
        - releasever: "9"
        state: enabled
    - name: Ensure RHEL 9 AppStream repositories are enabled
      redhat.satellite.repository_set:
        name: "Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)"
        organization: "Default Organization"
        product: "Red Hat Enterprise Linux for x86_64"
        repositories:
        - releasever: "9"
        state: enabled
    - name: Ensure a content view for RHEL 9 repositories exists
      redhat.satellite.content_view:
        name: "RHEL 9 content view"
        organization: "Default Organization"
        repositories:
          - name: "Red Hat Enterprise Linux 9 for x86_64 - BaseOS RPMs 9"
            product: "Red Hat Enterprise Linux for x86_64"
          - name: "Red Hat Enterprise Linux 9 for x86_64 - AppStream RPMs 9"
            product: "Red Hat Enterprise Linux for x86_64"
```

For more information, see the Ansible module documentation with the following commands:

- `ansible-doc redhat.satellite.repository_sync`
- `ansible-doc redhat.satellite.content_view`

## 3.3. Playbook example: Synchronize repositories and publish a content view

This is an example playbook for synchronizing repositories and publishing a content view.

This example playbook uses the following modules:

- `redhat.satellite.repository_sync`
- `redhat.satellite.content_view_version`

The playbook synchronizes repositories and publishes the content view that includes them.

Before you run this playbook, ensure that you have enabled the required repositories and created a content view. For an example playbook that ensures this, see [Section 3.2, “Playbook example: Enable repositories and create a content view”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#playbook-example-enable-repositories-and-create-a-content-view "3.2. Playbook example: Enable repositories and create a content view").

```
- name: Ensure Red Hat Enterprise Linux 9 repositories are synced and content view is published
  hosts: localhost
  vars_files:
    - My_Vault.yml
  module_defaults:
    group/redhat.satellite.satellite:
      username: "{{ My_Username }}"
      password: "{{ My_Password }}"
      server_url: "{{ My_Server_URL }}"
  tasks:
    - name: Sync Red Hat Enterprise Linux repositories
      redhat.satellite.repository_sync:
        product: "Red Hat Enterprise Linux for x86_64"
        organization: "Default Organization"
    - name: Publish Red Hat Enterprise Linux 9 content view
      redhat.satellite.content_view_version:
        content_view: "Red Hat Enterprise Linux 9 content view"
        organization: "Default Organization"
```

For more information, see the Ansible module documentation with the following commands:

- `ansible-doc redhat.satellite.repository_sync`
- `ansible-doc redhat.satellite.content_view_version`
