---
title: "Supported usage and versions of Satellite components"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#Supported-Usage-and-Versions-of-Project-Components_planning"
---
# Chapter 7. Supported usage and versions of Satellite components

Satellite supports the following use cases, architectures, and versions.

## 7.1. Supported usage of Satellite components

Usage of all Red Hat Satellite components is supported within the context of Red Hat Satellite only as described below.

Red Hat Enterprise Linux Server
:   Each Red Hat Satellite subscription includes one supported instance of Red Hat Enterprise Linux Server. Reserve this instance solely for the purpose of running Red Hat Satellite.

    Not supported: Using the operating system included with Satellite to run other daemons, applications, or services within your environment.

Foreman
:   You can extend Foreman with plugins packaged with Red Hat Satellite. See [Satellite 6 Component Versions](https://access.redhat.com/articles/1343683) in Red Hat Knowledgebase for information about supported Foreman plugins.

    Not supported: Extending Foreman with plugins in the *Red Hat Satellite Optional* repository.

    Red Hat Satellite also includes components, configuration, and functionality to provision and configure operating systems other than Red Hat Enterprise Linux. While these features are included, Red Hat supports their usage only for Red Hat Enterprise Linux.

Pulp
:   Interact with Pulp only by using the Satellite web UI, CLI, and API.

    Not supported: Direct modification or interaction with the Pulp local API or database. This can cause irreparable damage to the Red Hat Satellite databases.

Candlepin
:   Interact with Candlepin only by using the Satellite web UI, CLI, and API.

    Not supported: Direct interaction with Candlepin, its local API, or database. This can cause irreparable damage to the Red Hat Satellite databases.

Embedded Tomcat Application Server
:   Interact with the embedded Tomcat application server only by using the Satellite web UI, API, and database.

    Not supported: Direct interaction with the embedded Tomcat application server local API or database.

Puppet
:   When you run the Satellite installation program, you can install and configure OpenVox servers as part of Capsule Servers. A Puppet module, running on the OpenVox server on your Satellite Server or any Capsule Server, is also supported by Red Hat.

**Additional resources**

- [How does Red Hat support scripting frameworks in Red Hat Knowledgebase](https://access.redhat.com/articles/369183)
- [Red Hat Satellite Product Life Cycle](https://access.redhat.com/support/policy/updates/satellite)

## 7.2. Supported client architectures for content management

You can use the following combinations of major versions of Red Hat Enterprise Linux and hardware architectures for registering and managing hosts with Satellite. The Red Hat Satellite Client 6 repositories are also available for these combinations.

Table 7.1. Content management support

| Platform | Architectures |
| --- | --- |
| Red Hat Enterprise Linux 10 | x86_64, ppc64le, s390x, aarch64 |
| Red Hat Enterprise Linux 9 | x86_64, ppc64le, s390x, aarch64 |
| Red Hat Enterprise Linux 8 | x86_64, ppc64le, s390x |
| Red Hat Enterprise Linux 7 | x86_64, ppc64 (BE), ppc64le, aarch64, s390x |

## 7.3. Supported client architectures for host provisioning

You can use the following combinations of major versions of Red Hat Enterprise Linux and hardware architectures for host provisioning with Satellite.

Table 7.2. Host provisioning support

| Platform | Architectures |
| --- | --- |
| Red Hat Enterprise Linux 10 | x86_64 |
| Red Hat Enterprise Linux 9 | x86_64 |
| Red Hat Enterprise Linux 8 | x86_64 |
| Red Hat Enterprise Linux 7 | x86_64 |

## 7.4. Supported client architectures for configuration management

You can use the following combinations of major versions of Red Hat Enterprise Linux and hardware architectures for configuration management with Satellite.

Table 7.3. Configuration management support

| Platform | Architectures |
| --- | --- |
| Red Hat Enterprise Linux 10 | x86_64 |
| Red Hat Enterprise Linux 9 | x86_64 |
| Red Hat Enterprise Linux 8 | x86_64, aarch64 |
