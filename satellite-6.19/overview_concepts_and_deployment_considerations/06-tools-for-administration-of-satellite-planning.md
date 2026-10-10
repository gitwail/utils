---
title: "Tools for administration of Red Hat Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Tools-for-Administration-of-Satellite_planning"
---
# Chapter 6. Tools for administration of Red Hat Satellite

You can use multiple tools to manage Red Hat Satellite.

## 6.1. Satellite web UI overview

You can manage and monitor your Satellite infrastructure from a browser with the Satellite web UI. Satellite supports recent versions of the Mozilla Firefox and Google Chrome browsers.

The Satellite web UI and command-line interface support English, French, Japanese, Korean, and Simplified Chinese.

[Image: Screenshot of dashboard in Satellite web UI](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Overview_concepts_and_deployment_considerations-en-US/images/6b607236175494f3f8b583601726a9b9/web-ui-overview-satellite.png)

## 6.2. Hammer CLI overview

You can configure and manage your Satellite Server with CLI commands by using Hammer.

Using Hammer has the following benefits:

- Create shell scripts based on Hammer commands for basic task automation.
- Redirect output from Hammer to other tools.
- Use the `--debug` option with Hammer to test responses to API calls before applying the API calls in a script. For example: `hammer --debug organization list`.

To issue Hammer commands, a user must have access to your Satellite Server.

> **Note**
>
> To ensure a user-friendly and intuitive experience, the Satellite web UI takes priority when developing new functionality. Therefore, some features that are available in the Satellite web UI might not yet be available for Hammer.

In the background, each Hammer command first establishes a binding to the API, then sends a request. This can have performance implications when executing a large number of Hammer commands in sequence. In contrast, scripts that use API commands communicate directly with the Satellite API and they establish the binding only once.

**Additional resources**

- [*Using the Hammer CLI tool*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#)

## 6.3. Satellite API overview

You can write custom scripts and external applications that access the Satellite API over HTTP with the Representational State Transfer (REST) API provided by Satellite Server.

Using the REST API has the following benefits:

- Configure any programming language, framework, or system with support for HTTP protocol to use the API.
- Create client applications that require minimal knowledge of the Satellite infrastructure because users discover many details at runtime.
- Adopt the resource-based REST model for intuitively managing a virtualization platform.

Scripts based on API commands communicate directly with the Satellite API, which makes them faster than scripts based on Hammer commands or Ansible Playbooks relying on modules within redhat.satellite.

> **Important**
>
> API commands differ between versions of Satellite. When you prepare to upgrade Satellite Server, update all the scripts that contain Satellite API commands.

**Additional resources**

- [*Using the Satellite REST API*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#)

## 6.4. MCP server overview

Satellite provides a Model Context Protocol (MCP) server so that you can query and manage your Satellite inventory from MCP-compatible AI applications by using natural language.

You deploy the MCP server from a container image that Red Hat provides and connect it to the AI application that runs your MCP client. The MCP server accesses Satellite with your credentials, so your MCP client cannot obtain data that you do not have permission to access.

By default, the MCP server is read-only. You can query your inventory and generate reports from it, for example, a report of all subnets and the hosts that are assigned to them.

When you start the MCP server, you can also grant it permissions to change your Satellite. For example, you can start remote execution jobs on your hosts, and publish and promote content views.

**Additional resources**

- [Connecting AI applications to the MCP server for Satellite in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#connecting-ai-applications-to-the-mcp-server-for-satellite)

## 6.5. Remote execution in Red Hat Satellite

With remote execution, you can run jobs on hosts from Capsules by using shell scripts or Ansible roles and playbooks.

Use remote execution for the following benefits in Satellite:

- Run jobs on multiple hosts at once.
- Use variables in your commands for more granular control over the jobs you run.
- Use host facts and parameters to populate the variable values.
- Specify custom values for templates when you run the command.

Communication for remote execution occurs through Capsule Server, which means that Satellite Server does not require direct access to the target host, and can scale to manage many hosts.

To use remote execution, you must define a job template. A job template is a command that you want to apply to remote hosts. You can execute a job template multiple times.

Satellite uses ERB syntax job templates.

By default, Satellite includes several job templates for shell scripts and Ansible.

**Additional resources**

- [Template writing reference in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts)
- [Configuring and setting up remote jobs in *Managing configurations by using Ansible integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#configuring-and-setting-up-remote-jobs)

## 6.6. Automating Satellite management with Satellite Ansible Collection

Satellite Ansible Collection is a set of Ansible modules that interact with the Satellite API. You can use these modules to automate many aspects of Satellite administration.

**Additional resources**

- [Managing configurations by using Ansible integration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#)
- [*Using the Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#)

## 6.7. Kickstart workflow

You can automate the installation process of a Satellite Server or Capsule Server by creating a Kickstart file that contains all the information that is required for the installation.

When you run a Red Hat Satellite Kickstart script, the script performs the following actions:

1. It specifies the installation location of a Satellite Server or a Capsule Server.
2. It installs the predefined packages.
3. It installs Subscription Manager.
4. It uses Activation Keys to subscribe the hosts to Red Hat Satellite.
5. It installs Puppet, and configures a `puppet.conf` file to indicate the Red Hat Satellite or Capsule instance.
6. It enables Puppet to run and request a certificate.
7. It runs user defined snippets.

**Additional resources**

- [Automated installation workflow in *Automatically installing RHEL 9*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/automatically_installing_rhel/automated-installation-workflow_rhel-installer)
