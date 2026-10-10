---
title: "Introduction to Satellite API"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_rest_api"
guide_title: "Using the Satellite REST API"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#introduction-to-satellite-api"
---
# Chapter 1. Introduction to Satellite API

With the Representational State Transfer (REST) API of Satellite, you can control your Satellite environment outside of the standard web interface. That way, you can integrate your Satellite with custom scripts or external applications over HTTP.

## 1.1. Overview of the Satellite API

Integrate with enterprise systems, automate repetitive tasks, and manage your infrastructure programmatically using the resource-based REST model of the Satellite API. You can use any HTTP client to interact with Satellite.

The benefits of using the REST API are:

- Broad client support – any programming language, framework, or system with support for HTTP protocol can use the API.
- Self-descriptive – client applications require minimal knowledge of the Red Hat Satellite infrastructure because a user discovers many details at runtime.
- Resource-based model – the resource-based REST model provides a natural way to manage a virtualization platform.

You can use the REST API to perform the following tasks:

- Integrate with enterprise IT systems.
- Integrate with third-party applications.
- Perform automated maintenance or error checking tasks.
- Automate repetitive tasks with scripts.

## 1.2. Satellite API compared to Hammer CLI

Hammer serves as a human-friendly interface to Satellite API. Use Hammer for interactive tasks and testing API calls, but use the API directly for better performance when executing many commands in scripts.

For example, to test responses to API calls before applying them in a script, use the `--debug` option to inspect API calls that Hammer issues: `hammer --debug organization list`.

In the background, each Hammer command first establishes a binding to the API, then sends a request. This can have performance implications when executing a large number of Hammer commands in sequence. In contrast, a script communicating directly with the API establishes the binding only once.

**Additional resources**

- [*Using the Hammer CLI tool*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#)
- [*Using the Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#)

## 1.3. Getting help with Satellite API

You can use the API reference on your Satellite Server to view information about API endpoints supported for Satellite API integrations.

View the full API reference on your Satellite Server at the following URL:

```
https://satellite.example.com/apidoc/
```

Replace *satellite.example.com* with the FQDN of your Satellite Server.
