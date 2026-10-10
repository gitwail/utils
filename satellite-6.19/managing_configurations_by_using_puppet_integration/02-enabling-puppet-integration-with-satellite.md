---
title: "Enabling Puppet integration with Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#enabling-puppet-integration-with-satellite"
---
# Chapter 2. Enabling Puppet integration with Satellite

Before you can use Puppet for configuration management in Satellite, you need to deploy an OpenVox server on Satellite Server or Capsule Servers and install the OpenVox agent on your hosts.

## 2.1. Installing OpenVox server on Satellite Server and Capsule Servers

Use the `satellite-installer` utility to install an OpenVox server on Satellite Server. Optionally, you can also install additional OpenVox servers on Capsule Servers.

**Procedure**

1. Install OpenVox server on Satellite Server:

   ```
   # satellite-installer \
   --enable-foreman-cli-puppet \
   --enable-foreman-plugin-puppet \
   --enable-puppet \
   --foreman-proxy-puppet true \
   --foreman-proxy-puppetca true \
   --puppet-server true
   ```
2. Optional: If you want manage configuration with Puppet on Capsule Servers, install OpenVox server on Capsule Servers:

   ```
   # satellite-installer \
   --enable-puppet \
   --foreman-proxy-puppet true \
   --foreman-proxy-puppetca true \
   --puppet-server true
   ```

## 2.2. Configuring OpenVox agent on a host during provisioning

If you prefer to install and configure the OpenVox agent on a host when provisioning the host through Satellite, add the `puppet_setup` snippet to your provisioning template. A configured OpenVox agent is required on the host for Puppet integration with your Satellite.

**Prerequisites**

- Red Hat Satellite Client 6 OpenVox repository is synchronized on Satellite Server and enabled in the activation key you use.

  Choose from the following repositories, based on the operating system version and the architecture of the host you are registering:

  - satellite-client-openvox-for-rhel-9-x86_64-rpms
  - satellite-client-openvox-for-rhel-8-aarch64-rpms
  - satellite-client-openvox-for-rhel-8-x86_64-rpms
- You have an activation key. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Select a provisioning template depending on your host provisioning method. For more information, see [Kinds of Provisioning Templates](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#kinds-of-provisioning-templates) in *Provisioning hosts*.
3. Ensure the `puppet_setup` snippet is included as follows:

   ```
   <%= snippet 'puppet_setup' %>
   ```

   Note that this snippet is already included in the templates shipped with Satellite, for example, in the `Kickstart default` template.
4. Enable the OpenVox agent using a host parameter in global parameters, a host group, or for a single host. Add a host parameter named `enable-puppet8`, select the **boolean** type, and set the value to `true`.
5. Set configuration for the OpenVox agent.

   - If you use an integrated OpenVox server, ensure that you select a Puppet Capsule, Puppet CA Capsule, and Puppet environment when you create a host.
   - If you use a non-integrated OpenVox server, either set the following host parameters in global parameters, or a host group, or when you create a host:

     - Add a host parameter named `puppet_server`, select the **string** type, and set the value to the hostname of your OpenVox server, such as `openvox.example.com`.
     - Optional: Add a host parameter named `puppet_ca_server`, select the **string** type, and set the value to the hostname of your Puppet CA server, such as `puppet-ca.example.com`. If `puppet_ca_server` is not set, the OpenVox agent will use the same server as `puppet_server`.
     - Optional: Add a host parameter named `puppet_environment`, select the **string** type, and set the value to the Puppet environment you want the host to use.
6. Ensure your host has access to the OpenVox agent packages from Satellite Server by using an appropriate activation key.

## 2.3. Configuring OpenVox agent on a host during registration

If you prefer to install and configure the OpenVox agent on a host when registering the host to Satellite, enable the OpenVox agent with host parameters in global parameters or a host group. A configured OpenVox agent is required on the host for Puppet integration with your Satellite.

**Prerequisites**

- Red Hat Satellite Client 6 OpenVox repository is synchronized on Satellite Server and enabled in the activation key you use:

  Choose from the following repositories, based on the operating system version and the architecture of the host you are registering:

  - satellite-client-openvox-for-rhel-9-x86_64-rpms
  - satellite-client-openvox-for-rhel-8-aarch64-rpms
  - satellite-client-openvox-for-rhel-8-x86_64-rpms
- You have an activation key. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Global Parameters** to add host parameters globally. Alternatively, you can navigate to **Configure** > **Host Groups** and edit or create a host group to add host parameters only to a host group.
2. Enable the OpenVox agent using a host parameter in global parameters or a host group. Add a host parameter named `enable-puppet8`, select the **boolean** type, and set the value to `true`.
3. Specify configuration for the OpenVox agent using the following host parameters in global parameters or a host group:

   - Add a host parameter named `puppet_server`, select the **string** type, and set the value to the hostname of your OpenVox server, such as `openvox.example.com`.
   - Optional: Add a host parameter named `puppet_ca_server`, select the **string** type, and set the value to the hostname of your Puppet CA server, such as `puppet-ca.example.com`. If `puppet_ca_server` is not set, the OpenVox agent will use the same server as `puppet_server`.
   - Optional: Add a host parameter named `puppet_environment`, select the **string** type, and set the value to the Puppet environment you want the host to use.

   Until the [BZ2177730](https://bugzilla.redhat.com/show_bug.cgi?id=2177730) is resolved, you must use host parameters to specify the OpenVox agent configuration even in integrated setups where the OpenVox server is a Capsule Server.
4. Navigate to **Hosts** > **Register Host** and register your host using an appropriate activation key. For more information, see [Registering hosts by using global registration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration) in *Managing hosts*.
5. Navigate to **Infrastructure** > **Capsules**.
6. From the list in the **Actions** column for the required Capsule Server, select **Certificates**.
7. Click **Sign** to the right of the required host to sign the SSL certificate for the OpenVox agent.

## 2.4. Configuring OpenVox agent on a host manually

On hosts that are already registered to Satellite, you can install and configure the OpenVox agent manually. A configured OpenVox agent is required on the host for Puppet integration with your Satellite.

**Prerequisites**

- The host must have a Puppet environment assigned to it.
- Red Hat Satellite Client 6 OpenVox repository is synchronized on Satellite Server, available in the content view and the lifecycle environment of the host, and enabled for the host.

  Choose from the following repositories, based on the operating system version and the architecture of the host you are registering:

  - satellite-client-openvox-for-rhel-9-x86_64-rpms
  - satellite-client-openvox-for-rhel-8-aarch64-rpms
  - satellite-client-openvox-for-rhel-8-x86_64-rpms

**Procedure**

1. Log in to the host as the `root` user.
2. Install the OpenVox agent package:

   ```
   # dnf install openvox-agent
   ```
3. Add the OpenVox agent to `PATH` in your current shell using the following script:

   ```
   . /etc/profile.d/puppet-agent.sh
   ```
4. Configure the OpenVox agent. Set the `environment` parameter to the name of the Puppet environment to which the host belongs:

   ```
   # puppet config set server satellite.example.com --section agent
   # puppet config set environment My_Puppet_Environment --section agent
   ```
5. Start the OpenVox agent service:

   ```
   # puppet resource service puppet ensure=running enable=true
   ```
6. Create a certificate for the host:

   ```
   # puppet ssl bootstrap
   ```
7. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
8. From the list in the **Actions** column for the required Capsule Server, select **Certificates**.
9. Click **Sign** to the right of the required host to sign the SSL certificate for the OpenVox agent.
10. On the host, run the OpenVox agent again:

    ```
    # puppet ssl bootstrap
    ```
