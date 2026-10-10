---
title: "Glossary of terms used in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "B"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#glossary-of-terms-used-in-satellite_planning"
---
# Appendix B. Glossary of terms used in Satellite

This alphabetically ordered glossary provides an overview of Satellite related technical terms.

Activation key
:   Activation keys are used by [Subscription Manager](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Subscription-Manager) to register hosts to Satellite. They define content view and lifecycle environment associations, content overrides, system purpose attributes, and other parameters to be associated with a newly created host.

    They are associated to exactly one lifecycle environment and exactly one content view, though this may be a composite content view. You can use them on multiple machines and they behave like configuration information rather than traditional software license keys. You can also use multiple activation keys with a single host. When you register a host using an activation key, certain content from Satellite is provided to the host. The content that is made available depends on the content in the activation key’s content view and lifecycle environment, any content overrides present, any repository-level restrictions such as operating system or architecture, and system purpose attributes such as release version.

Ansible
:   Ansible is an agentless open-source automation engine. Ansible uses SSH to connect to hosts. It uses playbooks and roles to describe and bundle tasks. Within Satellite, you can use Ansible to configure hosts and perform [remote execution](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Remote-execution-REX).

    For more information about using Ansible to configure hosts, see [Managing configurations by using Ansible integration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#). For more information about automating Satellite using Ansible, see [*Using the Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#).

Answer file
:   A configuration file that defines settings for an installation scenario. Answer files are defined in the YAML format and stored in the `/etc/foreman-installer/scenarios.d/` directory. To see the default values for installation scenario parameters, use the `satellite-installer --full-help` command on your Satellite Server.

ARF report
:   Asset Reporting Format (ARF) reports are the result of OpenSCAP compliance scans on hosts which have a policy assigned. Summarizes the security compliance of hosts managed by Red Hat Satellite. They list compliance criteria and whether the scanned host has passed or failed.

Audits
:   Provide a report on changes made by a specific user. Audits can be viewed in the Satellite web UI under **Monitor** > **Audits**.

Baseboard management controller (BMC)
:   Enables remote power management of bare-metal hosts. In Satellite, you can create a BMC interface to manage selected hosts.

Boot disk
:   An ISO image used for PXE-less provisioning. This ISO enables the host to connect to Satellite Server, boot the installation media, and install the operating system. There are several kinds of boot disks: **host image**, **full host image**, **generic image**, and **subnet image**.

Capsule Server
:   Capsule Servers can provide DHCP, DNS, and TFTP services and act as an Ansible control node or OpenVox server in separate networks. They interact with Satellite Server in a client-server model. Satellite Server always comes bundled with an integrated Capsule.

    Capsule Servers are required in Satellite deployments that manage IT infrastructure spanning across multiple networks and useful for Satellite deployments across various geographical locations.

Catalog
:   A document that describes the desired system state for one specific host managed by Puppet. It lists all of the resources that need to be managed, as well as any dependencies between those resources. Catalogs are compiled by a OpenVox server from Puppet Manifests and data from OpenVox agents.

Candlepin
:   A service within Katello responsible for subscription management.

Compliance policy
:   Compliance policies refer to the application of SCAP content to hosts by using Satellite with its OpenSCAP plugin. You can create compliance policies by using the Satellite web UI, Hammer CLI, or API. A compliance policy requires the setting of a specific XCCDF profile from a SCAP content, optionally using a tailoring file. You can set up scheduled tasks on Satellite that check your hosts for compliance against SCAP content. When a compliance policy scan completes, the host sends an [ARF report](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#ARF_report) to Satellite.

Compute profile
:   Specifies default attributes for new virtual machines on a compute resource.

Compute resource
:   A compute resource is an external virtualization or cloud infrastructure that you can attach to Satellite. Satellite can provision, configure, and manage hosts within attached compute resources. Examples of compute resources include VMware or libvirt and cloud providers such as Microsoft Azure or Amazon EC2.

Configuration Management
:   Configuration management describes the task of configuring and maintaining hosts. In Satellite, you can use Ansible and Puppet to configure and maintain hosts with Satellite as a single source of infrastructure truth.

Container (Docker container)
:   An isolated application sandbox that contains all runtime dependencies required by an application. Satellite supports container provisioning on a dedicated compute resource.

Container image
:   A static snapshot of the container’s configuration. Satellite supports various methods of importing container images as well as distributing images to hosts through content views.

Content
:   A general term for everything Satellite distributes to hosts. Content includes software packages such as `.rpm` packages, errata, or Docker images. Content is synchronized into the Library and then promoted into lifecycle environments using content views so that they can be consumed by hosts.

Content delivery network (CDN)
:   The mechanism used to deliver Red Hat content to Satellite Server.

Content view
:   Content views are named and versioned collections of repositories. When you publish a content view, Satellite creates a new content view version. This content view version is a frozen snapshot of the current state of the repositories within the content view. Any subsequent changes to the underlying repositories will no longer affect the published content view version. Once a content view is published, it can be promoted through the lifecycle environment path, or modified using incremental upgrades.

Composite content view
:   Composite content views contain content views, which allows for a more modular approach to manage and version content. You can choose which version of each content view is used in a composite content view.

Discovered host
:   A bare-metal host detected on the provisioning network by the Discovery plugin.

Discovery image
:   Refers to the minimal operating system based on Red Hat Enterprise Linux that is PXE-booted on hosts to acquire initial hardware information and to communicate with Satellite Server before starting the provisioning process.

Discovery plugin
:   Enables automatic bare-metal discovery of unknown hosts on the provisioning network. The plugin consists of three components: services running on Satellite Server and Capsule Server, and the Discovery image running on host.

Discovery rule
:   A set of predefined provisioning rules which assigns a host group to discovered hosts and triggers provisioning automatically.

Docker tag
:   A mark used to differentiate container images, typically by the version of the application stored in the image. In the Satellite web UI, you can filter images by tag under **Content** > **Docker Tags**.

ERB
:   Embedded Ruby (ERB) is a template syntax used in provisioning and job templates.

Errata
:   Updated packages containing security fixes, bug fixes, and enhancements. In relationship to a host, erratum is **applicable** if it updates a package installed on the host and **installable** if it is present in the host’s content view (which means it is accessible for installation on the host).

External node classifier (ENC)
:   A construct that provides additional data for a server to use when configuring hosts. When Puppet obtains information about nodes from an external source instead of its own database, the external source is called External node classifier. If the Puppet plugin is installed, Red Hat Satellite can act as an External node classifier to OpenVox servers in a Satellite deployment.

Facter
:   A program that provides information (facts) about the system on which it is run; for example, Facter can report total memory, operating system version, architecture, and more. Puppet modules enable specific configurations based on host data gathered by Facter.

Facts
:   Host parameters such as total memory, operating system version, or architecture. Facts are reported by Facter and used by Puppet.

Foreman
:   Foreman is an open-source component to provision and manage hosts. Foreman is the core upstream component of Red Hat Satellite.

Full host image
:   A boot disk used for PXE-less provisioning of a specific host. The full host image contains an embedded Linux kernel and init RAM disk of the associated operating system installer.

Generic image
:   A boot disk for PXE-less provisioning that is not tied to a specific host. The generic image sends the MAC address of your host to Satellite Server, which matches it against the host entry.

Hammer
:   Hammer is a command-line interface tool for Satellite. You can execute Hammer commands from the command line or utilize it in scripts. You can use Hammer to automate certain recurring tasks as an alternative to Satellite Ansible collection or Satellite API.

Host
:   A host is a physical, virtual, or cloud instance registered to Satellite.

Host collection
:   A user defined group of one or more Hosts used for bulk actions such as errata installation.

Host group
:   A host group is a template to build hosts that holds shared parameters, such as subnet or lifecycle environment. It helps to unify configuration management in Ansible and Puppet by grouping hosts. You can nest host groups to create a hierarchical structure. For more information, see [Working with host groups](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Working_with_Host_Groups_managing-hosts) in *Managing hosts*.

Host image
:   A boot disk used for PXE-less provisioning of a specific host. The host image only contains the boot files necessary to access the installation media on Satellite Server.

Incremental upgrade (of a content view)
:   The act of creating a new (minor) content view version in a lifecycle environment. Incremental upgrades provide a way to make in-place modification of an already published content view. Useful for rapid updates, for example when applying security errata.

Installation Media
:   Installation media are sets of installation files used to install the base operating system during the provisioning process. An installation medium in Satellite represents the installation files for one or more operating systems, which must be accessible over the network, either through an URL or an NFS server location. It is usually either a mirror or a CD or DVD image.

    Every operating system depends on exactly one path of an installation medium, whereas installation media paths may serve different operating systems at the same time. You can use operating system parameters such as `$version`, `$major`, and `$minor` to parameterize the URL.

Job
:   A command executed remotely on a host from Satellite Server. Every job is defined in a job template.

Katello
:   Katello is an open-source plugin to perform content management and subscription handling. It depends on Pulp for content management, which fetches software from repositories and stores various versions of it. It also depends on Candlepin for host registration and managing subscription manifests. The Katello plugin is always installed on Satellite.

Lazy sync
:   The ability to change the default download policy of a repository from **Immediate** to **On Demand**. The **On Demand** setting saves storage space and synchronization time by only downloading the packages when requested by a host.

Location
:   A collection of default settings that represent a physical place. Location is a tag mostly used for geographical separation of hosts within Satellite. Examples include different cities or different data centers.

Library
:   A container for content from all synchronized repositories on Satellite Server. Libraries exist by default for each organization as the root of every lifecycle environment path and the source of content for every content view.

Lifecycle environment
:   A lifecycle environment represents a step in the lifecycle environment path. It defines the stage in which certain versions of content are available to hosts, such as *development*, *testing*, and *production*. This way, new versions of software can be developed and tested before being deployed in a *production* environment, thus reducing the risk of disruption by prematurely rolled out updates. Content moves through lifecycle environments by publishing and promoting content views.

Lifecycle environment path
:   A sequence of lifecycle environments through which content views are promoted. You can promote a content view through a typical promotion path, for example, from *development* to *test* to *production*. All lifecycle environment paths originate from the *Library* environment, which is always present by default.

Manifest (Red Hat subscription manifest)
:   A mechanism for transferring subscriptions from the Red Hat Customer Portal to Red Hat Satellite. Do not confuse with [Puppet manifest](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Puppet_manifest).

Migrating Satellite
:   The process of moving an existing Satellite installation to a new instance.

OpenSCAP
:   A project implementing security compliance auditing according to the Security Content Automation Protocol (SCAP). OpenSCAP is integrated in Satellite to provide compliance auditing for hosts.

Organization
:   An isolated collection of systems, content, and other functionality within Satellite. Organization is a tag used for organizational separation of hosts within Satellite. Examples include different teams or business units.

Parameter
:   Defines the behavior of Red Hat Satellite components during provisioning. Depending on the parameter scope, we distinguish between global, domain, host group, and host parameters. Depending on the parameter complexity, we distinguish between simple parameters (key-value pair) and smart parameters (conditional arguments, validation, overrides).

Parametrized class (smart class parameter)
:   A parameter created by importing a class from OpenVox server.

Patch and release management
:   Patch and release management describes the process of acquiring, managing, and installing patches and software updates to your infrastructure. Using Satellite, you can keep control of the package versions available to your hosts and deliver applicable errata.

Permission
:   Defines an action related to a selected part of Satellite infrastructure (resource type). Each resource type is associated with a set of permissions, for example the **Architecture** resource type has the following permissions: **view_architectures**, **create_architectures**, **edit_architectures**, and **destroy_architectures**. You can group permissions into roles and associate them with users or user groups.

Product
:   Products are named collections of one or more [repositories](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Repository). When you upload a Red Hat manifest, Satellite automatically groups Red Hat content within products.

Promote (a content view)
:   The act of moving a content view from one lifecycle environment to another. For more information, see [Promoting a content view](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#promoting-a-content-view-by-using-web-ui) in *Managing content*.

Provisioning
:   The provisioning of a host is the deployment of the base operating system on the host and registration of the host to Satellite. Optionally, the process continues with the supply of content and configuration. This process is ideally automated. Provisioned hosts run on [compute resources](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Compute_resource) or bare metal, never Satellite Server or Capsule Servers.

Provisioning template
:   Provisioning templates are templates that automate deployment of an operating system on hosts. Satellite contains provisioning templates for Red Hat Enterprise Linux.

Publish (a content view)
:   The act of making a content view version available in a lifecycle environment and usable by hosts.

Pulp
:   A service within Katello responsible for repository and content management.

Puppet
:   Puppet is a configuration management tool utilizing a declarative language in a server-client architecture. For more information about using Puppet to configure hosts, see [Managing configurations by using Puppet integration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#).

OpenVox agent
:   A service running on a host that applies configuration changes to that host.

Puppet environment
:   An isolated set of OpenVox agent nodes that can be associated with a specific set of Puppet Modules.

Puppet manifest
:   Refers to Puppet scripts, which are files with the **.pp** extension. The files contain code to define a set of necessary resources, such as packages, services, files, users and groups, and so on, using a set of key-value pairs for their attributes.

    Do not confuse with [Manifest (Red Hat subscription manifest)](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Manifest).

OpenVox server
:   A Capsule Server component that provides a Puppet catalog to hosts for execution by the OpenVox agent.

Puppet module
:   A self-contained bundle of code (Puppet Manifests) and data (facts) that you can use to manage resources such as users, files, and services.

PXE
:   PXE stands for *preboot execution environment* and is used to boot operating systems received from the network rather than a local disk. It requires a compatible network interface card (NIC) and relies on DHCP and TFTP.

Recurring logic
:   A job executed automatically according to a schedule. In the Satellite web UI, you can view those jobs under **Monitor** > **Recurring logics**.

Registry
:   An archive of container images. Satellite supports importing images from local and external registries. Satellite itself can act as an image registry for hosts. However, hosts cannot push changes back to the registry.

Remote execution (REX)
:   Remote execution is the process of using Satellite to run commands on registered hosts.

Repository
:   A repository is a single source and the smallest unit of content in Satellite. You can either synchronize a repository with a URL or manually upload content to Satellite. Satellite supports multiple content types. For more information, see [Content types in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Content_Types_in_Satellite_content-management) in *Managing content*. One or more repositories form a [product](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Product).

Resource type
:   Refers to a part of Satellite infrastructure, for example host, Capsule, or architecture. Used in permission filtering.

Role
:   Specifies a collection of permissions that are applied to a set of resources, such as hosts. Roles can be assigned to users and user groups. Satellite provides several predefined roles.

SCAP content
:   SCAP stands for Security Content Automation Protocol and refers to `.xml` files containing the configuration and security baseline against which hosts are checked. Satellite uses SCAP content in compliance policies.

Subnet image
:   A type of generic image for PXE-less provisioning that communicates through Capsule Server.

Subscription
:   An entitlement for receiving content and service from Red Hat.

Subscription Manager
:   Subscription Manager is a client application to register hosts to Satellite. `subscription-manager` uses [activation keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Activation_key) to consume content on hosts.

Synchronization
:   Synchronization describes the process of fetching content from external repositories into the Satellite Server.

Sync plan
:   Sync plans describe the scheduled synchronization of content from external content.

Tailoring files
:   Tailoring files specify a set of modifications to existing SCAP content. They adapt SCAP content to your particular needs without changing the original SCAP content itself.

Task
:   A background process executed on the Satellite or Capsule Server, such as repository synchronization or content view publishing. You can monitor the task status in the Satellite web UI under **Monitor** > **Satellite Tasks** > **Tasks**.

Updating Satellite
:   The process of advancing your Satellite Server and Capsule Server installations from one patch release to the next, for example Satellite 6.19.0 to Satellite 6.19.1.

Upgrading Satellite
:   The process of advancing your Satellite Server and Capsule Server installations from one minor release to the next, for example Satellite 6.18 to Satellite 6.19.

User group
:   A collection of roles which can be assigned to a collection of users.

User
:   Anyone registered to use Red Hat Satellite. Authentication and authorization is possible through built-in logic, through external resources (LDAP, Identity Management, or Active Directory), or with Kerberos.

Virtualization
:   Virtualization describes the process of running multiple operating systems with various applications on a single hardware host using hypervisors like VMware or libvirt. It facilitates scalability and cost savings. You can attach virtualization infrastructure as compute resources to Satellite.

virt-who
:   An agent for retrieving IDs of virtual machines from the hypervisor. When used with Satellite, virt-who reports those IDs to Satellite Server so that it can provide subscriptions for hosts provisioned on virtual machines.

XCCDF profiles
:   Extensible configuration checklist description format (XCCDF) profiles are a component of SCAP content. XCCDF is a language to write security checklists and benchmarks. An XCCDF file contains security configuration rules for lists of hosts.
