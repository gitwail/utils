---
title: "host-registration"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "44"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-host-registration"
---
# Chapter 44. host-registration

Host Registration

**Usage**

```
# hammer host-registration [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 44.1. host-registration generate-command

Generate global registration command

**Usage**

```
# hammer host-registration generate-command [OPTIONS]
```

**Options**

- `--activation-key VALUE` – Activation key for subscription-manager client, required for CentOS and Red Hat Enterprise Linux. For multiple keys use `activation_keys` param instead.
- `--activation-keys LIST` – Activation keys for subscription-manager client, required for CentOS and Red Hat Enterprise Linux. Required only if host group has no activation keys or if you do not provide a host group.
- `--download-utility ENUM` – The download utility to use during host registration Possible value(s): `curl`, `wget`
- `--force BOOLEAN` – Clear any previous registration and run subscription-manager with –force.
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER` – ID of the Host group to register the host in
- `--hostgroup-title VALUE` – Hostgroup title
- `--ignore-subman-errors BOOLEAN` – Ignore subscription-manager errors for `subscription-manager register` command
- `--insecure BOOLEAN` – Enable insecure argument for the initial curl/wget
- `--jwt-expiration NUMBER` – Expiration of the authorization token (in hours), 0 means `unlimited`.
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – ID of the Operating System to register the host in. Operating system must have a `host_init_config` template assigned
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--packages VALUE` – Packages to install on the host when registered. Can be set by `host_packages` parameter, example: `pkg1 pkg2`
- `--remote-execution-interface VALUE` – Identifier of the Host interface for Remote execution
- `--repo VALUE` – DEPRECATED, use the `repo_data` param instead.
- `--repo-data SCHEMA` – Array with repository URL and corresponding GPG key URL
- `--repo-gpg-key-url VALUE` – DEPRECATED, use the `repo_data` param instead.
- `--setup-container-registry-certs BOOLEAN` Use container certificates for container registry authentication. If it is set to true, container registry certificates will be installed on the host
- `--setup-insights BOOLEAN` – Set `host_registration_insights` parameter for the host. If it is set to true, Red Hat Lightspeed client will be installed and registered on Red Hat family operating systems
- `--setup-remote-execution BOOLEAN` – Set `host_registration_remote_execution` parameter for the host. If it is set to true, SSH keys will be installed on the host
- `--setup-remote-execution-pull BOOLEAN` – Set `host_registration_remote_execution_pull` parameter for the host. If it is set to true, pull provider client will be deployed on the host
- `--smart-proxy VALUE` – Name to search by
- `--smart-proxy-id NUMBER` – ID of the Capsule. This Capsule must have enabled both the `Templates` and `Registration` features
- `--update-packages BOOLEAN` – Update all packages on the host
- `-h`, `--help` – Print help

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--repo-data` – "repo=<string>,repo_gpg_key_url=<string>, …​ "
