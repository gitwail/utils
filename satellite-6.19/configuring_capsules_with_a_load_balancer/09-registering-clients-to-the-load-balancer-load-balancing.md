---
title: "Registering clients to the load balancer"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#Registering_Clients_to_the_Load_Balancer_load-balancing"
---
# Chapter 9. Registering clients to the load balancer

To balance the load of network traffic from clients, you must register the clients to the load balancer.

To consume container content from a load balancer regardless of client registration, use the load balancer hostname with the container client of choice. For example, use `podman login loadbalancer.example.com` to log in.

## 9.1. Setting the load balancer for host registration

You can configure Satellite to register clients through a load balancer when using the host registration feature.

You will be able to register hosts to the load balancer instead of Capsule. The load balancer will decide through which Capsule to register the host at the time of request. Upon registration, the subscription manager on the host will be configured to manage content through the load balancer.

**Prerequisites**

- You configured SSL certificates on all Capsule Servers. For more information, see the following sections:

  - [Chapter 3, *Configuring Capsule Servers with default SSL certificates for load balancing*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#configuring-capsule-servers-with-default-ssl-certificates-for-load-balancing-without-puppet_load-balancing "Chapter 3. Configuring Capsule Servers with default SSL certificates for load balancing").
  - [Chapter 4, *Configuring Capsule Servers with custom SSL certificates for load balancing*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#configuring-capsule-servers-with-custom-ssl-certificates-for-load-balancing-without-puppet_load-balancing "Chapter 4. Configuring Capsule Servers with custom SSL certificates for load balancing").
  - [Chapter 5, *Configuring Capsule Servers with default SSL certificates for load balancing (with Puppet)*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#configuring-capsule-servers-with-default-ssl-certificates-for-load-balancing-with-puppet_load-balancing "Chapter 5. Configuring Capsule Servers with default SSL certificates for load balancing (with Puppet)").
  - [Chapter 6, *Configuring Capsule Servers with custom SSL certificates for load balancing (with Puppet)*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#configuring-capsule-servers-with-custom-ssl-certificates-for-load-balancing-with-puppet_load-balancing "Chapter 6. Configuring Capsule Servers with custom SSL certificates for load balancing (with Puppet)").
- You enabled Registration and Templates plugins on all Capsule Servers:

  ```
  # satellite-installer \
  --foreman-proxy-registration true \
  --foreman-proxy-templates true
  ```

**Procedure**

1. On all Capsule Servers, set the registration and template URLs using `satellite-installer`:

   ```
   # satellite-installer \
   --foreman-proxy-registration-url "https://loadbalancer.example.com:9090" \
   --foreman-proxy-template-url "http://loadbalancer.example.com:8000"
   ```
2. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
3. For each Capsule, click the dropdown menu in the **Actions** column and select **Refresh**.

## 9.2. Registering a host to the load balancer using Satellite web UI

After setting the load balancer for host registration, you can register a host to the load balancer.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Register Host**.
2. From the **Capsule** dropdown list, select your Capsule Server configured for load balancing.
3. Select **Force** to register a host that has been previously registered to a Capsule Server.
4. From the **Activation Keys** list, select the activation keys to assign to your host.
5. Click **Generate** to create the registration command.
6. Click on the *files* icon to copy the command to your clipboard.
7. Connect to your host using SSH and run the registration command.
8. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

## 9.3. Registering a host to the load balancer using CLI

After setting the load balancer for host registration, you can register a host to the load balancer.

**Procedure**

1. Generate the host registration command using the Hammer CLI:

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

   Include the `--smart-proxy-id My_Capsule_ID` option. You can use the ID of any Capsule Server that you configured for host registration load balancing. Satellite will apply the load balancer to the registration command automatically.

   Include the `--force` option to register a host that has been previously registered to a Capsule Server.
2. Connect to your host using SSH and run the registration command.
3. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

## 9.4. Registering a host to the load balancer using API

After setting the load balancer for host registration, you can register a host to a load-balanced Capsule.

**Procedure**

1. Generate the host registration command using the Satellite API:

   ```
   $ curl \
   --data '{ "registration_command": { "activation_keys": ["My_Activation_Key_1, My_Activation_Key_2"] }}' \
   --header 'Content-Type: application/json' \
   --request POST \
   --user "My_User_Name:My_Password" \
   https://satellite.example.com/api/registration_commands
   ```

   If your hosts do not trust the SSL certificate of Satellite Server, you can disable SSL validation by adding the `--insecure` flag to the registration command.

   ```
   $ curl \
   --data '{ "registration_command": { "activation_keys": ["My_Activation_Key_1, My_Activation_Key_2"], "insecure": true }}' \
   --header 'Content-Type: application/json' \
   --insecure \
   --request POST \
   --user "My_User_Name:My_Password" \
   https://satellite.example.com/api/registration_commands
   ```

   Use an activation key to simplify specifying the environments. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.

   Include `{ "smart_proxy_id": My_Capsule_ID }`. You can use the ID of any Capsule Server that you configured for host registration load balancing. Satellite will apply the load balancer to the registration command automatically.

   Include `{ "force": true }` to register a host that has been previously registered to a Capsule Server.

   To enter a password as a command line argument, use `username:password` syntax. Keep in mind this can save the password in the shell history. Alternatively, you can use a temporary personal access token instead of a password. To generate a token in the Satellite web UI, navigate to **My Account** > **Personal Access Tokens**.
2. Connect to your host using SSH and run the registration command.
3. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

## 9.5. (Deprecated) Registering clients using the bootstrap script

To register clients, enter the following command on the client. You must complete the registration procedure for each client.

**Prerequisites**

- Ensure that you install the bootstrap script on the client and change file permissions of the script to executable. For more information, see [Registering Hosts to Red Hat Satellite Using The Bootstrap Script](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Registering_Hosts_by_Using_the_Bootstrap_Script_managing-hosts) in *Managing hosts*.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --activationkey="My_Activation_Key" \
  --enablerepos=satellite-client-6-for-rhel-8-<arch>-rpms \
  --force \
  --hostgroup="My_Host_Group" \
  --location="My_Location" \
  --login=admin \
  --organization="My_Organization" \
  --puppet-ca-port 8141 \
  --server loadbalancer.example.com
  ```

  The options used in the command include the following:

  `enablerepos`
  :   Replace `<arch>` with the client architecture, for example `x86`.

  `--force`
  :   Include the `--force` option to register the client that has been previously registered to a standalone Capsule.

  `--puppet-ca-port`
  :   Include the `--puppet-ca-port 8141` option if you use Puppet.
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # python bootstrap.py --login=admin \
  --activationkey="My_Activation_Key" \
  --enablerepos=rhel-7-server-satellite-client-6-rpms \
  --force \
  --hostgroup="My_Host_Group" \
  --location="My_Location" \
  --organization="My_Organization" \
  --puppet-ca-port 8141 \
  --server loadbalancer.example.com
  ```

  The options used in the command include the following:

  `--force`
  :   Include the `--force` option to register the client that has been previously registered to a standalone Capsule.

  `--puppet-ca-port`
  :   Include the `--puppet-ca-port 8141` option if you use Puppet.

      The script prompts for the password corresponding to the Satellite user name you entered with the `--login` option.
