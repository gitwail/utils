---
title: "Deployment path for Red Hat Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "11"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#deployment-path_planning"
---
# Chapter 11. Deployment path for Red Hat Satellite

During installation and initial configuration of Satellite, you can customize your deployment to fit your specific needs and operational environment. By customizing each stage of the deployment process, you can choose deployment options that meet the requirements of your organization.

## 11.1. Installing a Satellite Server

Installing an instance of Satellite Server on a dedicated server is the first step to a working Satellite infrastructure.

You can install a Satellite Server in a connected or disconnected setup:

- Connected deployment is suitable for networked environments where your Satellite Server is connected to the Red Hat CDN.
- Disconnected deployment is suitable for high-security environments where direct internet access is restricted or prohibited.

In the disconnected setup, your Satellite Server uses Inter-Satellite Synchronization (ISS) to obtain content from another, connected Satellite Server. Although a disconnected Satellite Server is isolated from Red Hat CDN, you can still provision hosts with the latest security updates, errata, packages, and other content.

**Additional resources**

- [*Installing Satellite Server in a connected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#)
- [*Installing Satellite Server in a disconnected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#)

### 11.1.1. Configuring Satellite Server with external database

A default Satellite Server installation includes installing PostgreSQL databases on the server. However, you can configure your Satellite Server to use external databases instead. Moving to external databases distributes the workload and can reduce overall Satellite memory usage.

> **Note**
>
> Red Hat does not provide support or tools for external database maintenance. If you deploy Satellite with external databases, you will need to support and maintain the external databases yourself.

Consider using external databases if you plan to use your Satellite deployment for the following scenarios:

- Frequent remote execution tasks. This requires a high volume of records in PostgreSQL and generates heavy database workloads.
- High disk I/O workloads from frequent repository synchronization or content view publishing. This requires Satellite to create a record in PostgreSQL for each job.
- High volume of hosts.
- High volume of synchronized content.

**Additional resources**

- [Using external databases with Satellite in *Installing Satellite Server in a connected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#using-external-databases)
- [Using external databases with Satellite in *Installing Satellite Server in a disconnected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#using-external-databases)
- [Preparing Satellite for using external databases in *Installing Satellite Server in a connected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#preparing-for-using-external-databases_satellite)
- [Preparing Satellite for using external databases in *Installing Satellite Server in a disconnected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#preparing-for-using-external-databases_satellite)

## 11.2. Configuring external authentication in Satellite

The authentication methods you can configure depend on the authentication source you are using. If the native authentication features provided by Satellite are not sufficient for your use case, use this information to decide which external authentication provider best suits your requirements.

Red Hat Satellite includes native support for authentication with a username and password. If you require additional methods of authentication, configure your Satellite Server to use an external authentication source.

Table 11.1. External authentication sources supported by Satellite and the authentication features they provide

|  | Username and password | Single sign-on (SSO) | One-time password (OTP) | Time-based one-time password (TOTP) |
| --- | --- | --- | --- | --- |
| **Active Directory (direct integration)** | Yes | Yes | No | No |
| **Identity Management** | Yes (Linux and Active Directory users) | Yes (Linux users only) | No | No |
| **Red Hat Single Sign-On** | Yes | Yes | Yes | Yes |
| **LDAP** | Yes | No | No | No |

**Additional resources**

- [*Configuring authentication for Red Hat Satellite users*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#)

## 11.3. Planning organization and location context

Context in Satellite consists of organizations and locations. You can associate most resources, for example hosts, subnets, and domains, with at least one organization and location context.

Organizations and locations enable you to arrange Satellite resources into logically structured groups. For example, you can create groups based on ownership, purpose, content, or security level. You can create and manage multiple organizations through Red Hat Satellite, then divide and assign your Red Hat subscriptions to each individual organization.

Organizations
:   Organizations can represent different business units, departments, or teams, such as *Finance*, *Marketing*, or *Web Development*. Each organization requires a separate Red Hat subscription manifest.

    By creating organizations, you can create logical containers to isolate and manage their configurations separately according to their specific requirements.

Locations
:   Locations can represent physical locations, such as countries or cities.

    By creating locations, you can define geographical sites where hosts are located. For example, this is useful in environments with multiple data centers.

    You can use locations to map the network infrastructure to prevent incorrect host placement or configuration. While you cannot assign a subnet, domain, or compute resources directly to a Capsule Server, you can assign them to a location.

    Unlike organizations, locations can have a hierarchical structure. Resources and users can generally only access resources within their own context, which makes configuring organizations and locations an integral part of access management in Satellite.

Satellite Server defines all locations and organizations. Each Capsule Server synchronizes content and handles configuration of hosts in a different location.

Your Satellite Server retains the management function, while the content and configuration is synchronized between your Satellite Server and Capsule Servers assigned to certain locations.

> **Important**
>
> If you use host groups to bundle provisioning and configuration information, avoid mismatching resources from mutually exclusive contexts. For example, setting a subnet from one organization or location and a compute resource from a different organization or location creates an invalid host group.

**Example 11.1. Example of using organizations and locations in Satellite**

The structure of a multi-national company includes the Finance, Marketing, and Sales departments. The company operates across United States, United Kingdom, and Japan.

The system administrator creates the following organizations on their Satellite Server:

- Finance
- Marketing
- Sales

Additionally, the administrator creates the following locations on their Satellite Server:

- United States
- United Kingdom
- Japan

The administrator can define a nested location hierarchy to divide the United States location into additional locations based on specific cities:

- Boston
- Phoenix
- San Francisco

**Additional resources**

- [Chapter 12, *Common deployment scenarios*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#common-deployment-scenarios "Chapter 12. Common deployment scenarios")
- [Managing organizations in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-organizations-in-satellite)
- [Managing locations in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-locations-in-satellite)

## 11.4. Installing Capsule Servers

By installing Capsule Servers, you extend the reach and scalability of your Satellite deployment. You register each Capsule Server to Satellite Server and configure it to provide the required services within your Satellite deployment.

You can install a Capsule Server in each of your geographic locations. By assigning a Capsule to each location, you decrease the load on Satellite Server, increase redundancy, and reduce bandwidth usage.

> **Note**
>
> The maximum number of Capsule Servers that Satellite Server can support has no fixed limit. It was tested that a Satellite Server can support 17 Capsule Servers with 2 vCPUs.

Decide what services you want to enable on each Capsule Server. You can configure the DNS, DHCP, and TFTP services on one of your Capsule Servers or you can use an external server to provide these services to your Capsule Servers.

**Additional resources**

- [*Installing Capsule Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#)
- [Capsule configuration tuning in *Tuning performance of Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/tuning_performance_of_red_hat_satellite/index#Smart_Proxy_Configuration_Tuning_performance-tuning)

## 11.5. Adding a Red Hat subscription to Satellite

A Red Hat subscription manifest is a set of encrypted files that contains your subscription information. Adding a Red Hat subscription ensures you can use Red Hat content in your Satellite deployment.

Satellite Server uses information from the Red Hat subscription manifest to access the Red Hat CDN and find what repositories are available for the associated subscription.

> **Warning**
>
> Deleting a subscription manifest removes all the subscriptions attached to running hosts and activation keys.

**Additional resources**

- [Managing Red Hat subscriptions in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Red_Hat_Subscriptions_content-management)
- [*Creating and managing manifests for a connected Satellite Server*](https://docs.redhat.com/en/documentation//subscription_central/1-latest/html/creating_and_managing_manifests_for_a_connected_satellite_server/index)

## 11.6. Defining your content library

To ensure that your Satellite Server can manage software and provide it to your hosts, you must create repositories and synchronize them.

Your Satellite content library can include the following types of content:

Red Hat content
:   The Red Hat subscription manifest determines what Red Hat repositories your Satellite Server can access. Red Hat content is already organized into products.

    For example, Red Hat Enterprise Linux Server is a product in Satellite. The repositories for the Red Hat Enterprise Linux Server product consist of different versions, architectures, and add-ons. When you enable a Red Hat repository, Satellite automatically creates an associated product.

Other sources of content
:   To distribute content from custom sources, you must create products and repositories manually. You can organize other content into custom products however you want.

    For example, you can create an EPEL (Extra Packages for Enterprise Linux) product and add an "EPEL 9 x86_64" repository to it.

Creating repositories allows you to choose the specific software required for your environment. By creating only the necessary repositories, you avoid downloading unnecessary content.

Synchronizing repositories downloads the content from Red Hat CDN or another source to your Satellite Server. The synchronized content is stored on your Satellite Server, eliminating the need for hosts to access the repositories. You can synchronize repositories manually, or you can create a sync plan to ensure synchronization runs on a regular basis.

**Additional resources**

- [Adding content to Satellite in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite)

## 11.7. Defining content access strategies for hosts

When defining your content lifecycle in Satellite, you can use content views and lifecycle environments to define which hosts can access which content and content versions.

By default, Satellite includes the *Default Organization View* content view and the *Library* lifecycle environment.

Default Organization View
:   The *Default Organization View* is the default content view in Satellite that contains all the content that is synchronized to Satellite. After you update your content, such as by adding or removing a repository, the update is immediately reflected in *Default Organization View*.

Library
:   The *Library* lifecycle environment is the default lifecycle environment in Satellite. Every newly published content view version is automatically published to the Library lifecycle environment. You can also promote specific content view versions to the Library lifecycle environment if needed.

In smaller deployments or when you do not require content versioning and environment promotion, you can associate a host to the *Library* environment under the *Default Organization View* without configuring additional lifecycle environments.

**Additional resources**

- [Content access control for Satellite hosts in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-access-control-for-hosts)
- [Managing application lifecycles in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Application_Lifecycles_content-management)
- [Managing content views and content view environments in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-views-and-content-view-environments)
- [Chapter 12, *Common deployment scenarios*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#common-deployment-scenarios "Chapter 12. Common deployment scenarios")

## 11.8. Defining role-based access control policies

You can define role-based access control policies to manage access to Satellite resources. A role-based access control policy is a set of rules that defines which users can access which resources and what actions they can perform on those resources.

### 11.8.1. Roles in Satellite

Users in Satellite can have one or more roles assigned. These roles are associated with permissions that enable users to perform specified administrative actions in Satellite. Permission filters define the actions allowed for a certain resource type.

Satellite provides a set of predefined roles with permissions sufficient for standard tasks. You can also configure custom roles.

> **Note**
>
> One of the predefined roles is the **Default role**. Satellite assigns the **Default role** to every user in the system. By default, the **Default role** grants only a limited set of permissions. Be aware that if you add a permission to the **Default role**, every Satellite users will gain that permission. Assigning a different role to a user does not remove the **Default role** from the user.

The following types of roles are commonly defined within various Satellite deployments:

Roles related to applications or parts of infrastructure
:   For example, roles for owners of Red Hat Enterprise Linux as the operating system as opposed to roles for owners of application servers and database servers.

Roles related to a particular stage of the software lifecycle
:   For example, roles divided among the development, testing, and production phases, where each phase has one or more owners.

Roles related to specific tasks
:   For example, you can create a role for security managers and a role for license managers, depending on the specific tasks users need to be able to perform within your organization.

**Additional resources**

- [Managing users and roles in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Managing_Users_and_Roles_admin)

### 11.8.2. Best practices for role-based access control in Satellite

When implementing role-based access control in Satellite, consider the following guidelines for optimal results.

- Define the expected tasks and responsibilities: Define the subset of the Satellite infrastructure that you want the role to access as well as actions permitted on this subset. Think of the responsibilities of the role and how it differs from other roles.
- Use predefined roles whenever possible: Satellite provides several sample roles that you can use. Copying and editing an existing role can be a good start for creating a custom role.
- Adopt a granular approach to user role management: Define roles with specific and well-scoped permissions. Note that each user can have multiple roles assigned and that permissions from these roles are cumulative.
- Add permissions gradually and test the results: When creating a custom role, start with a limited set of permissions and add permissions one by one, while testing continuously. Ensure to test your custom role to verify that it works as intended.
- Consider areas of interest and granting read-only access: Even though a role has a limited area of responsibility, it might need a wider set of permissions. Therefore, you can grant the role a read-only access to parts of Satellite infrastructure that influence its area of responsibility.

## 11.9. Configuring provisioning

After your basic Satellite infrastructure is in place, you can start configuring provisioning to ensure that Satellite can seamlessly create, configure, and manage hosts.

The provisioning process depends on whether you want to provision bare-metal hosts, virtual machines, or cloud instances, but it includes defining installation media, configuring provisioning templates, and other tasks. If you are provisioning virtual machines or cloud instances, you must also integrate your compute provider with Satellite by connecting the provider as a compute resource to Satellite.

The following Satellite features support automating the provisioning of your hosts:

- Provisioning templates enable you to define the way Satellite installs an operating system on your hosts.
- The Discovery service enables you to detect unknown hosts and virtual machines on the provisioning network.
- Host groups enable you to standardize provisioning of host configurations.

**Additional resources**

- [*Provisioning hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#)

## 11.10. Overview of recommended disaster recovery plans

Choose a disaster recovery plan that best helps ensure the continuity of Satellite services in your deployment.

Snapshots of virtualized Satellite Server
:   How do I back up?
    :   Virtualize your Satellite Server and use the hypervisor tools to take virtual machine snapshots of the server. This method is suitable if you can run Satellite in a virtual machine.

    How will I recover in case of a disruptive event?
    :   To recover Satellite services, restore a virtual machine snapshot.

    Disadvantages and expected impact
    :   Expect some amount of data inconsistency after recovery, based on how old your last snapshot is. You will lose data changes that have occurred since the snapshot you are using to recover was taken.

Active and passive Satellite Server, with external storage
:   How do I back up?
    :   Store the following critical data on network attached storage: content in `/var/lib/pulp` and database in `/var/lib/pgsql`. Replicate this storage into a different data center. Attach the storage to a Satellite Server that is a clone of the primary Satellite Server but runs passively.

    How will I recover in case of a disruptive event?
    :   To recover Satellite services, switch DNS records of the active Satellite Server with the passive Satellite Server. This ensures that the passive server becomes the active server. All hosts remain connected without configuration updates.

    Disadvantages and expected impact
    :   If the network attached storage is replicated to another location, expect some amount of data inconsistency after recovery based on the synchronization interval.

Active and passive Satellite Server, with backup and restore
:   How do I back up?
    :   Ensure periodic backups of your Satellite Server. Copy this backup to a passive Satellite Server and restore it on the passive server.

    How will I recover in case of a disruptive event?
    :   To recover Satellite services, switch DNS records of the active Satellite Server with the passive Satellite Server. This ensures that the passive server becomes the active server. All hosts remain connected without configuration updates.

    Disadvantages and expected impact
    :   Expect some amount of data inconsistency after recovery, based on how often you took and restored backups and on how long it takes to complete the restore process.

Dual active Satellite Server
:   How do I back up?
    :   Operate an active, independent Satellite Server per data center. Hosts from each data center are registered to the Satellite Server in that data center. Then configure automation to ensure recovery in case of a disruptive event. For example, you can periodically run a health check and if the health check discovers that the current Satellite Server a host is registered to does not resolve, the host is re-registered to the other Satellite Server.

        To minimize downtime, you can automate the recovery in various ways. For example, you can use the Satellite Ansible collection. For more information, see [*Using the Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#).

    How will I recover in case of a disruptive event?
    :   To recover Satellite services, re-register all hosts to the Satellite Server in the other data center.

    Disadvantages and expected impact
    :   You must ensure that content synchronization and content view creation are synchronized to create the same content view in each Satellite and prevent content drift. Content drift occurs when available content deviates from the intended state defined by a content view. If you fail to prevent content drift, expect inconsistency in the content that is available to hosts.

**Additional resources**

- [Preparing for disaster recovery and recovering from data loss in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#preparing-for-disaster-recovery-and-recovering-from-data-loss)
- [Backing up Satellite Server and Capsule Server in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin)
- [Configuring and setting up remote jobs in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs)

## 11.11. Subscriptions tracking configuration

For successful tracking of your subscriptions usage, you have to perform the following configuration tasks.

In both connected and disconnected scenarios, perform the following task:

- Set the system purpose for hosts in Satellite.

In the connected scenarios, also perform the following tasks:

- If you use a hypervisor with virtual machines, configure virt-who on Satellite Server.
- Configure inventory upload in Satellite and install the Insights client on hosts.
- Activate the Subscriptions service in the Red Hat Hybrid Cloud Console if needed.

**Additional resources**

- [Editing the system purpose of a host by using Satellite web UI in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#editing-the-system-purpose-of-a-host-by-using-web-ui)
- [Monitoring hosts by using Red Hat Lightspeed in Red Hat Hybrid Cloud Console in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#monitoring-hosts-by-using-red-hat-lightspeed-in-cloud)
- [Activating and opening the subscriptions service in *Getting Started with the Subscriptions Service*](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_the_subscriptions_service)
- [Chapter 4, *Expense management for Red Hat subscriptions*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#expense-management-for-red-hat-subscriptions "Chapter 4. Expense management for Red Hat subscriptions")
- [*Configuring virt-who for virtual machine subscriptions*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt_who_for_virtual_machine_subscriptions/index#)
- [Monitoring hosts by using Red Hat Lightspeed in Red Hat Hybrid Cloud Console in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#monitoring-hosts-by-using-red-hat-lightspeed-in-cloud)
- [Activating and opening the subscriptions service in *Getting Started with the Subscriptions Service*](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_the_subscriptions_service)

## 11.12. Additional deployment tasks

Satellite offers a range of additional capabilities that you can use to further enhance your Satellite deployment.

Remote execution commands on hosts
:   With remote execution, you can perform various tasks on multiple hosts simultaneously. Satellite supports the following modes of transport for remote execution: pull-based mode (over MQTT/HTTPS) and push-based mode (over SSH).

    For more information, see [Configuring and setting up remote jobs](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs) in *Managing hosts*.

Automating tasks with a configuration management tool
:   By integrating Satellite with a configuration management tool, you can automate repetitive tasks and ensure consistent configuration of your hosts.

    For more information on using Ansible with Satellite, see [*Managing configurations by using Ansible integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#).

    You can use Puppet to configure hosts. For more information on using Puppet with Satellite, see [*Managing configurations by using Puppet integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#).

Security management with OpenSCAP
:   With OpenSCAP, you can manage compliance policies and run security compliance scans on your hosts. After the scan completes, a compliance report is uploaded to your Satellite Server.

    For more information, see [*Managing security compliance*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#).

Load balancing
:   With load balancing configured on your Capsule Servers, you can improve performance on Capsule Servers while also improving performance and stability for host connections to Satellite.

    For more information, see [*Configuring Capsules with a load balancer*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#).

Incident management with Red Hat Lightspeed
:   With Red Hat Lightspeed enabled on your Satellite Server, you can identify key risks to stability, security, and performance.

    For more information, see [Performing additional configuration on Satellite Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#performing-additional-configuration-on-server_satellite) in *Installing Satellite Server in a connected network environment*.
