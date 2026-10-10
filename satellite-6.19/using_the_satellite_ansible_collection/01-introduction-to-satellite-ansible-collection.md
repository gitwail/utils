---
title: "Introduction to Satellite Ansible Collection"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_ansible_collection"
guide_title: "Using the Satellite Ansible Collection"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#introduction-to-satellite-ansible-collection"
---
# Chapter 1. Introduction to Satellite Ansible Collection

Satellite Ansible Collection provides a set of Ansible modules for managing Satellite. Using the modules, you can automate many aspects of Satellite management.

## 1.1. Installing the Satellite Ansible modules

Modules from the Satellite Ansible Collection are provided by the `ansible-collection-redhat-satellite` package. On your Satellite Server, the package is installed by default. If you want to execute your playbooks on a different system, you must first install the package that provides them.

> **Note**
>
> You can execute your playbooks on any system that can reach the Satellite API. This can also be your Satellite Server itself.

**Procedure**

- Install the `ansible-collection-redhat-satellite` package:

  ```
  # dnf install ansible-collection-redhat-satellite
  ```

**Verification**

- Display the list of Ansible modules that are now available on your system:

  ```
  # ansible-doc --list redhat.satellite
  ```

**Next steps**

- You can now use the installed Ansible modules to execute playbooks.

## 1.2. Getting help with Satellite Ansible Collection

You can use the built-in Ansible documentation to view information about modules. For example, you can use the built-in documentation to check for required parameters.

> **Note**
>
> To view the built-in documentation, Satellite Ansible Collection must be installed on your system. For more information, see [Section 1.1, “Installing the Satellite Ansible modules”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#Installing_the_Project_Ansible_Modules_ansible-collection "1.1. Installing the Satellite Ansible modules").

You can view the full built-in documentation for available modules with the following command:

```
# ansible-doc --list redhat.satellite
```

You can view the built-in documentation for a particular module with the following command:

```
# ansible-doc redhat.satellite.Module_Name
```

For example:

```
# ansible-doc redhat.satellite.location
```
