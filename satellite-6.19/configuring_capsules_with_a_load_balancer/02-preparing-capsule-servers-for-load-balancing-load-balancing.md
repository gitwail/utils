---
title: "Preparing Capsule Servers for load balancing"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#preparing-capsule-servers-for-load-balancing_load-balancing"
---
# Chapter 2. Preparing Capsule Servers for load balancing

Before you can configure load balancing in your Satellite environment, you must install a new Capsule Server. This is the Capsule Server that you will later configure for load balancing.

> **Important**
>
> Satellite does not support configuring existing Capsule Servers for load balancing. You must create a new Capsule Server for this purpose.

## 2.1. Registering Capsule Server

Register the base operating system to Satellite Server to access Capsule Server installation packages.

### 2.1.1. Prerequisites for registering Capsule Server to Satellite Server

Your environment must meet the following requirements before you can register your Capsule Server to your Satellite Server.

- Prerequisites for Red Hat subscription manifest:

  - On Satellite Server, a manifest must be installed and it must contain the appropriate repositories for the organization you want Capsule to belong to.
  - The manifest must contain repositories for the base operating system on which you want to install Capsule, as well as any clients that you want to connect to Capsule.
  - The repositories must be synchronized.

    For more information on manifests and repositories, see [Managing Red Hat Subscriptions](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Red_Hat_Subscriptions_content-management) in *Managing content*.
- Prerequisites for HTTP proxy and network:

  - The Satellite Server base operating system must be able to resolve the host name of the Capsule base operating system and vice versa.
  - Ensure HTTPS connection using client certificate authentication is possible between Capsule Server and Satellite Server. HTTP proxies between Capsule Server and Satellite Server are not supported.
  - You must configure the host and network-based firewalls accordingly. For more information, see [Opening required ports in *Installing Capsule Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#opening-required-ports).

### 2.1.2. Registering a host to Satellite by using Satellite web UI

You can register hosts with Satellite using the host registration feature in the Satellite web UI. For more information, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Register Host**.
2. From the **Activation Keys** list, select the activation keys to assign to your host.
3. Click **Generate** to create the registration command.
4. Click on the *files* icon to copy the command to your clipboard.
5. Connect to your host using SSH and run the registration command.
6. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

### 2.1.3. Registering a host to Satellite by using Hammer CLI

You can register hosts with Satellite using the host registration feature in Hammer CLI. For more information, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.

**Procedure**

1. Generate the host registration command:

   ```
   $ hammer host-registration generate-command \
   --activation-keys "My_Activation_Key"
   ```

   If your hosts do not trust the SSL certificate of Satellite Server, you can disable SSL validation by adding the `--insecure` flag to the registration command.

   ```
   $ hammer host-registration generate-command \
   --activation-keys "My_Activation_Key" \
   --insecure true
   ```
2. Connect to your host using SSH and run the registration command.
3. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

### 2.1.4. Registering a host to Satellite by using Satellite API

You can register hosts with Satellite using the host registration feature in the Satellite API. For more information, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.

**Procedure**

1. Generate the host registration command using the Satellite API:

   ```
   # curl -X POST https://satellite.example.com/api/registration_commands \
   --user "My_User_Name" \
   -H 'Content-Type: application/json' \
   -d '{ "registration_command": { "activation_keys": ["My_Activation_Key_1, My_Activation_Key_2"] }}'
   ```

   If your hosts do not trust the SSL certificate of Satellite Server, you can disable SSL validation by adding the `--insecure` flag to the registration command.

   ```
   # curl -X POST https://satellite.example.com/api/registration_commands \
   --user "My_User_Name" \
   -H 'Content-Type: application/json' \
   -d '{ "registration_command": { "activation_keys": ["My_Activation_Key_1, My_Activation_Key_2"], "insecure": true }}'
   ```

   Use an activation key to simplify specifying the environments. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.

   To enter a password as a command line argument, use `username:password` syntax. Keep in mind this can save the password in the shell history. Alternatively, you can use a temporary personal access token instead of a password. To generate a token in the Satellite web UI, navigate to **My Account** > **Personal Access Tokens**.
2. Connect to your host using SSH and run the registration command.
3. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

## 2.2. Configuring repositories

Configure repositories to install your Capsule Server.

**Procedure**

1. Disable all repositories:

   ```
   # subscription-manager repos --disable "*"
   ```
2. Enable the following repositories:

   ```
   # subscription-manager repos \
   --enable=rhel-9-for-x86_64-baseos-rpms \
   --enable=rhel-9-for-x86_64-appstream-rpms \
   --enable=satellite-capsule-6.19-for-rhel-9-x86_64-rpms \
   --enable=satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```

**Verification**

- Verify that the required repositories are enabled:

  ```
  # dnf repolist enabled
  ```

## 2.3. Installing Capsule packages

Install Capsule Server packages to set up the core software components needed for Capsule functionality.

**Procedure**

1. Upgrade all packages:

   ```
   # dnf upgrade
   ```
2. Install the packages:

   ```
   # dnf install satellite-capsule
   ```
