---
title: "Introduction to Hammer"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#introduction-to-hammer"
---
# Chapter 1. Introduction to Hammer

Hammer is a powerful command-line tool provided with Red Hat Satellite 6. You can use Hammer to configure and manage a Satellite Server either through CLI commands or automation in shell scripts. Hammer also provides an interactive shell.

**Additional resources**

- [Hammer reference](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#)

## 1.1. Hammer compared to Satellite web UI

Hammer provides faster interaction with Satellite than the Satellite web UI through shell features, scripting capabilities, and tool integration.

## 1.2. Satellite API compared to Hammer CLI

Hammer serves as a human-friendly interface to Satellite API. Use Hammer for interactive tasks and testing API calls, but use the API directly for better performance when executing many commands in scripts.

For example, to test responses to API calls before applying them in a script, use the `--debug` option to inspect API calls that Hammer issues: `hammer --debug organization list`.

In the background, each Hammer command first establishes a binding to the API, then sends a request. This can have performance implications when executing a large number of Hammer commands in sequence. In contrast, a script communicating directly with the API establishes the binding only once.

**Additional resources**

- [*Using the Satellite REST API*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#)
- [*Using the Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#)

## 1.3. Getting help with Hammer CLI

Use the `--help` flag with Hammer CLI commands to view the built-in help documentation.

View the full list of `hammer` options and subcommands by executing:

```
$ hammer --help
```

Use `--help` to inspect any subcommand, for example:

```
$ hammer organization --help
```

You can search the help output using `grep`, or redirect it to a text viewer, for example:

```
$ hammer | less
```
