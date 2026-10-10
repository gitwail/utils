---
title: "Configuration management with Puppet in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#configuration-management-with-puppet-in-satellite"
---
# Chapter 1. Configuration management with Puppet in Satellite

Puppet is a configuration management tool to automate host configurations across your infrastructure. You can use Puppet to consistently manage configurations of hosts registered to Satellite. Satellite uses OpenVox server as the Puppet-compatible central server for the integration.

## 1.1. How Puppet integrates with Satellite

Puppet uses a server-agent architecture. OpenVox server communicates with OpenVox agents on hosts registered to Satellite to manage the Puppet configuration of these hosts. Satellite components integrate with that architecture to provide configuration management capabilities in Satellite.

Puppet architecture in Satellite comprises the following components:

OpenVox server
:   OpenVox server is the central component that stores Puppet configuration definitions in Satellite. It runs on Satellite Server or Capsule Servers.

    > **Note**
    >
    > Puppet server is no longer supported for Puppet integration with Satellite. To integrate your Puppet infrastructure with Satellite, you need to use an OpenVox server instead. An OpenVox server is functionally equivalent to a Puppet server.

OpenVox agent
:   OpenVox agent is a service that communicates with an OpenVox server to manage the configuration of hosts. It runs on hosts registered to Satellite.

    > **Note**
    >
    > As a legacy alternative, Puppet agent also remains compatible with Satellite for Puppet integration. However, an OpenVox agent is the recommended agent for Puppet integration, and it is functionally equivalent to a Puppet agent. You cannot run both OpenVox agent and Puppet agent on the same host.

Puppet modules
:   A Puppet module is a collection of classes, manifests, resources, files, and templates. The Puppet modules work as components of host configuration definitions.

Puppet environments
:   Puppet environments are used to control versions of configuration definitions or to manage variants of the definitions, and to test the definitions before you deploy them on production. You can create multiple Puppet environments.

On each run, the OpenVox agent collects Puppet facts about the host and sends them to the OpenVox server. The OpenVox server forwards those facts to Satellite.

> **Note**
>
> To list Puppet facts on a host, run the `puppet facts` command.

Satellite acts as an external node classifier (ENC) for the OpenVox server. Based on the facts and other definitions Satellite receives from the OpenVox server, Satellite constructs the ENC answer to the OpenVox server.

Based on the ENC answer, the OpenVox server compiles a catalog for the host and sends it to the agent.

The agent evaluates the system state on the host. If the agent finds differences between the desired state defined in the catalog and the actual state, known as drifts, it enforces correction of the state of the host.

The agent reports correction results back to the OpenVox server. The OpenVox server receives correction results from the agent and reports them to Satellite.

If the Puppet modules you are using support the use of parameters, you can override parameters of the module by using Smart Class parameters in Satellite. In Satellite, you define the parameters as key-value pairs, which behave similar to host parameters or Ansible variables.

## 1.2. High-level steps for configuration management with Puppet

After you deploy an OpenVox agent on a host, use Satellite to manage Puppet modules, import classes, set parameter overrides, and assign classes to hosts so configuration is applied automatically or on demand.

Configuration management with Puppet involves the following high-level steps:

1. Managing Puppet modules on the OpenVox server by installing and updating them.
2. Importing Puppet classes and environments from Puppet modules into Satellite.
3. Optional: Creating config groups from Puppet classes.
4. Configuring overrides of Smart Class parameters on various levels.
5. Assigning Puppet classes or config groups to host groups or individual hosts.
6. Configuring intervals for runs of the OpenVox agent on hosts and for configuration enforcement runs of the OpenVox server.
7. Monitoring configuration management using reports in the Satellite web UI.
8. Configuring email notifications.

After assigning Puppet classes or config groups, Satellite runs configuration management automatically in the configured intervals to enforce Puppet configuration on your hosts, or you can initiate it manually on demand with the **Run Puppet Once** feature.

**Additional resources**

- [Monitoring Satellite resources in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#monitoring-satellite-resources)
- [Configuring email notification preferences in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Configuring_Email_Notification_Preferences_admin)
- [Section 11.1, “Running Puppet once using SSH”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#running-puppet-once-using-ssh_managing-configurations-puppet "11.1. Running Puppet once using SSH")

## 1.3. OpenVox versions supported for integration with Satellite

Before you begin with the Puppet integration, review which versions of the OpenVox server and OpenVox agent are supported for integration with Satellite.

OpenVox Server 8 is supported on Satellite Server and Capsule Servers.

> **Important**
>
> The Puppet modules you use must be compatible with the OpenVox Server version you run.

OpenVox Agent 8 is supported on hosts registered to Satellite.

Additionally, Puppet agent 7 remains compatible with OpenVox in Satellite as a legacy alternative. Hosts registered to Satellite that run Puppet agent 7 can still integrate with the OpenVox implementation in Satellite. However, Puppet agent 7 is end of life. Red Hat recommends to use OpenVox agent 8.
