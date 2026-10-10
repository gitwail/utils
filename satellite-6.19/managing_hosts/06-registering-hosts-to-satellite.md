---
title: "Registering hosts to Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite"
---
# Chapter 6. Registering hosts to Satellite

Before you can use Satellite to manage hosts that have not been provisioned through Satellite, you must register them. You can register hosts through Satellite Server or Capsule Server.

## 6.1. Supported clients in registration

You can register hosts with supported operating systems and architectures.

The hosts can use the following operating systems:

- Red Hat Enterprise Linux 10, 9, and 8
- Red Hat Enterprise Linux 7 with the [ELS Add-On](https://www.redhat.com/en/resources/els-datasheet)
- You can register the following hosts for converting to RHEL:

  - CentOS Linux 7
  - Oracle Linux 7 and 8

The hosts can use the following architectures:

- AMD and Intel 64-bit architectures
- The 64-bit ARM architecture
- IBM Power Systems, Little Endian
- 64-bit IBM Z architectures

## 6.2. Registering hosts by using global registration

You can register hosts to Satellite by generating a `curl` or `wget` registration command on Satellite and running this command on multiple hosts.

Global registration uses two provisioning templates: **Global Registration** template and **Linux host_init_config default** template. That gives you complete control over the host registration process.

With this registration method, you can modify the initial configuration templates to enable additional features. For example, you can deploy Satellite SSH keys to hosts to enable remote execution jobs, configure hosts with Red Hat Lightspeed, or install the OpenVox agent on hosts to enable configuration management with Puppet.

### 6.2.1. Global parameters for registration

**Additional resources**

You can configure the following global parameters for registration.

You can view the parameters in the Satellite web UI by navigating to **Configure** > **Global Parameters**.

- The `host_registration_insights` parameter is used in the `insights` snippet. If the parameter is set to `true`, the registration installs and enables the Red Hat Lightspeed client on the host. If the parameter is set to `false`, Satellite prevents the installation and registration of the Red Hat Lightspeed client. The default value is `true`. When overriding the parameter value, set the parameter type to `boolean`.
- The `host_registration_insights_inventory` parameter controls Inventory uploads. If the parameter is set to `true`, the host is included in the Red Hat Lightspeed Inventory report uploaded to the Red Hat Hybrid Cloud Console. If the parameter is set to `false`, the host is excluded from the Red Hat Lightspeed Inventory report upload. To upload inventory data without registering the host with the Red Hat Lightspeed client, set the `host_registration_insights` parameter to `false` and set the `host_registration_insights_inventory` to `true`.
- The `host_packages` parameter is for installing packages on the host.
- The `host_registration_remote_execution` parameter is used in the `remote_execution_ssh_keys` snippet. If it is set to `true`, the registration enables remote execution on the host. The default value is `true`.
- The `remote_execution_ssh_keys`, `remote_execution_ssh_user`, `remote_execution_create_user`, and `remote_execution_effective_user_method` parameters are used in the `remote_execution_ssh_keys` snippet. For more details, see the snippet.

You can navigate to snippets in the Satellite web UI through **Hosts** > **Templates** > **Provisioning Templates**.

**Additional resources**

- [Configuring OpenVox agent on a host during registration in *Managing configurations by using Puppet integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#configuring-openvox-agent-on-a-host-during-registration)

### 6.2.2. Configuring a host for registration

Configure your host for registration to Satellite Server or Capsule Server. You can use a configuration management tool to configure multiple hosts at once.

**Prerequisites**

- The host must be using a supported operating system. For more information, see [Section 6.1, “Supported clients in registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#supported-clients-in-registration_managing-hosts "6.1. Supported clients in registration").
- The system clock on your Satellite Server and any Capsule Servers must be synchronized across the network. If the system clock is not synchronized, SSL certificate verification might fail. For example, you can use the Chrony suite for timekeeping.

**Procedure**

1. Enable and start a time-synchronization tool on your host. The host must be synchronized with the same NTP server as Satellite Server and any Capsule Servers.

   ```
   # systemctl enable --now chronyd
   ```
2. Deploy the SSL CA file on your host so that the host can make a secured registration call.

   1. Find where Satellite stores the SSL CA file by navigating to **Administer** > **Settings** > **Authentication** and locating the value of the **SSL CA file** setting.
   2. Transfer the SSL CA file to your host securely, for example by using `scp`.
   3. Login to your host by using SSH.
   4. Copy the certificate to the truststore:

      ```
      # cp My_SSL_CA_file.pem /etc/pki/ca-trust/source/anchors/
      ```
   5. Update the truststore:

      ```
      # update-ca-trust
      ```

### 6.2.3. Registering a host by using Satellite web UI

You can register a host by using the Satellite web UI with registration templates. This also enables you to set up various integration features and host tools during the registration process.

**Prerequisites**

- Your Satellite account has the **Register hosts** role assigned or a role with equivalent permissions.
- Root privileges are available on the host that you want to register.
- Either `curl` or `wget` is installed on the host that you want to register.
- Your host is configured for registration. For more information, see [Section 6.2.2, “Configuring a host for registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Configuring_a_Host_for_Registration_managing-hosts "6.2.2. Configuring a host for registration").
- An activation key must be available for your host. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.
- Optional: If you want to register your host to Red Hat Lightspeed, the **BaseOS** and **AppStream** RPM repositories must be synchronized and made available in the activation key that you use. For example, for RHEL 8 hosts, `rhel-8-for-x86_64-baseos-rpms` and `rhel-8-for-x86_64-appstream-rpms` repositories are required. This is required to install the `insights-client` package on your host.
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server and enabled in the activation key you use. For more information, see [Adding content to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite) in *Managing content*. This repository is required for the remote execution pull client, OpenVox agent, Tracer, and other tools.
- If you want to use Capsule Servers instead of your Satellite Server, ensure that you have configured your Capsule Servers accordingly.

  > **Important**
  >
  > It is essential to add your Capsule Server to the list of trusted proxies on Satellite Server!

  For more information, see [Configuring Capsule Server for host registration and provisioning](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-capsule-server-for-host-registration-and-provisioning) in *Installing Capsule Server*.
- If your Satellite Server or Capsule Server is behind an HTTP proxy, Subscription Manager on your host is configured to use the HTTP proxy for connection. For more information, see [How to access Red Hat Subscription Manager (RHSM) through a firewall or proxy](https://access.redhat.com/solutions/65300) in the *Red Hat Knowledgebase*.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Register Host**.
2. Enter the details for how you want the registered host to be configured.

   - If you select a host group from the **Host Group** list, the following fields inherit their values from the host group:

     - **Operating system**
     - **Activation Keys**
     - **Lifecycle environment**
   - A Capsule behind a load balancer takes precedence over the Capsule selected in the Satellite web UI as the content source of the host.
3. On the **General** tab, in the **Activation Keys** field, enter one or more activation keys to assign to your host.
4. Specify any other registration details that you require. The available settings include the following:

   - On the **General** tab, in the **Capsule** field, you can select the Capsule to register your host through. A Capsule behind a load balancer takes precedence over a Capsule selected in the Satellite web UI as the content source of the host.
   - On the **General** tab, in the **Download utility** field, you can select `wget` if you want to register your host by using a `wget` command. By default, Satellite generates a `curl` command.
   - On the **General** tab, you can select the **Insecure** option to make the first call insecure. During this first call, your host downloads the CA file from Satellite. Your host will use this CA file to connect to Satellite with all future calls making them secure.

     Red Hat recommends that you avoid insecure calls.

     If an attacker, located in the network between Satellite and your host, fetches the CA file from the first insecure call, the attacker will be able to access the content of the API calls to and from your host and the JSON Web Tokens (JWT). Therefore, if you have chosen to deploy SSH keys during registration, the attacker will be able to access your host using the SSH key.
   - On the **Advanced** tab, in the **Repositories** field, you can list repositories to be added before the registration is performed. You do not have to specify repositories if you provide them in an activation key.
   - On the **Advanced** tab, you can configure remote execution, Red Hat Lightspeed, and packages to be installed.
   - On the **Advanced** tab, in the **Token lifetime (hours)** field, you can change the validity duration of the JSON Web Token (JWT) that Satellite uses for authentication. The duration of this token defines how long the generated registration command works.

     Note that Satellite applies the permissions of the user who generates the registration command to authorization of your host. If the user loses or gains additional permissions, the permissions of the JWT change too. Therefore, do not delete, block, or change permissions of the user during the token duration.

     The scope of the JWTs is limited to the registration endpoints only and cannot be used anywhere else.
   - On the **Advanced** tab, you can enable container and Flatpak registry access without a username or password by selecting the **Set up container registry certs** checkbox. Using certificate-based authentication also enforces lifecycle management of container and Flatpak content for the host.
5. Click **Generate** to generate a registration command.
6. Run the registration command as `root` on the host that you want to register. After registration completes, any Ansible roles assigned to a host group you specified when configuring the registration template will run on the host.

**Verification**

- If your activation key was supposed to enable repositories, check the `/etc/yum.repos.d/redhat.repo` file and verify that the repositories have been enabled.

**Next steps**

- To set up monitoring of outdated services and applications using Tracer, see [Configuring Tracer on a host](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-tracer-on-a-host_managing-hosts) in *Managing hosts*.

**Additional resources**

- [Section 6.2.10, “Registration command customization”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registration-command-customization "6.2.10. Registration command customization")

### 6.2.4. Registering a host by using Hammer CLI

You can register a host by using Hammer CLI with registration templates. This also enables you to set up various integration features and host tools during the registration process.

**Prerequisites**

- Your Satellite account has the **Register hosts** role assigned or a role with equivalent permissions.
- Root privileges are available on the host that you want to register.
- Either `curl` or `wget` is installed on the host that you want to register.
- Your host is configured for registration. For more information, see [Section 6.2.2, “Configuring a host for registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Configuring_a_Host_for_Registration_managing-hosts "6.2.2. Configuring a host for registration").
- An activation key must be available for your host. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.
- Optional: If you want to register your host to Red Hat Lightspeed, the **BaseOS** and **AppStream** RPM repositories must be synchronized and made available in the activation key that you use. For example, for RHEL 8 hosts, `rhel-8-for-x86_64-baseos-rpms` and `rhel-8-for-x86_64-appstream-rpms` repositories are required. This is required to install the `insights-client` package on your host.
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server and enabled in the activation key you use. For more information, see [Adding content to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite) in *Managing content*. This repository is required for the remote execution pull client, OpenVox agent, Tracer, and other tools.
- If you want to use Capsule Servers instead of your Satellite Server, ensure that you have configured your Capsule Servers accordingly.

  > **Important**
  >
  > It is essential to add your Capsule Server to the list of trusted proxies on Satellite Server!

  For more information, see [Configuring Capsule Server for host registration and provisioning](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-capsule-server-for-host-registration-and-provisioning) in *Installing Capsule Server*.
- If your Satellite Server or Capsule Server is behind an HTTP proxy, Subscription Manager on your host is configured to use the HTTP proxy for connection. For more information, see [How to access Red Hat Subscription Manager (RHSM) through a firewall or proxy](https://access.redhat.com/solutions/65300) in the *Red Hat Knowledgebase*.

**Procedure**

1. Use the `hammer host-registration generate-command` to generate the registration command to register your host.
2. On your host that you want to register, run the registration command as `root`.

   For more information, see the Hammer CLI help with `hammer host-registration generate-command --help`.

**Verification**

- If your activation key was supposed to enable repositories, check the `/etc/yum.repos.d/redhat.repo` file and verify that the repositories have been enabled.

**Next steps**

- To set up monitoring of outdated services and applications using Tracer, see [Configuring Tracer on a host](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-tracer-on-a-host_managing-hosts) in *Managing hosts*.

**Additional resources**

- [Section 6.2.10, “Registration command customization”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registration-command-customization "6.2.10. Registration command customization")

### 6.2.5. Registering a host by using Satellite API

You can register a host by using Satellite API with registration templates. This also enables you to set up various integration features and host tools during the registration process.

**Prerequisites**

- Your Satellite account has the **Register hosts** role assigned or a role with equivalent permissions.
- Root privileges are available on the host that you want to register.
- Either `curl` or `wget` is installed on the host that you want to register.
- Your host is configured for registration. For more information, see [Section 6.2.2, “Configuring a host for registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Configuring_a_Host_for_Registration_managing-hosts "6.2.2. Configuring a host for registration").
- An activation key must be available for your host. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.
- Optional: If you want to register your host to Red Hat Lightspeed, the **BaseOS** and **AppStream** RPM repositories must be synchronized and made available in the activation key that you use. For example, for RHEL 8 hosts, `rhel-8-for-x86_64-baseos-rpms` and `rhel-8-for-x86_64-appstream-rpms` repositories are required. This is required to install the `insights-client` package on your host.
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server and enabled in the activation key you use. For more information, see [Adding content to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite) in *Managing content*. This repository is required for the remote execution pull client, OpenVox agent, Tracer, and other tools.
- If you want to use Capsule Servers instead of your Satellite Server, ensure that you have configured your Capsule Servers accordingly.

  > **Important**
  >
  > It is essential to add your Capsule Server to the list of trusted proxies on Satellite Server!

  For more information, see [Configuring Capsule Server for host registration and provisioning](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-capsule-server-for-host-registration-and-provisioning) in *Installing Capsule Server*.
- If your Satellite Server or Capsule Server is behind an HTTP proxy, Subscription Manager on your host is configured to use the HTTP proxy for connection. For more information, see [How to access Red Hat Subscription Manager (RHSM) through a firewall or proxy](https://access.redhat.com/solutions/65300) in the *Red Hat Knowledgebase*.

**Procedure**

- Use the POST `/api/registration_commands` resource.

**Verification**

- If your activation key was supposed to enable repositories, check the `/etc/yum.repos.d/redhat.repo` file and verify that the repositories have been enabled.

**Next steps**

- To set up monitoring of outdated services and applications using Tracer, see [Configuring Tracer on a host](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-tracer-on-a-host_managing-hosts) in *Managing hosts*.

**Additional resources**

- [Section 6.2.10, “Registration command customization”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registration-command-customization "6.2.10. Registration command customization")

### 6.2.6. Registering a host by using Ansible

You can register a host with an Ansible playbook by using registration templates and set up various integration features and host tools during the registration process.

**Procedure**

- Use the `redhat.satellite.registration_command` module.

  For more information, see the Ansible module documentation with `ansible-doc redhat.satellite.registration_command`.

**Verification**

- If your activation key was supposed to enable repositories, check the `/etc/yum.repos.d/redhat.repo` file and verify that the repositories have been enabled.

**Additional resources**

- [Section 6.2.10, “Registration command customization”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registration-command-customization "6.2.10. Registration command customization")

### 6.2.7. Running custom code during host registration

You can customize the registration process by creating snippets with pre-defined names.

The `Global Registration` template includes these snippets automatically. Therefore, you do not have to edit the template.

To add custom steps to registration, create one or both of the following snippets:

`before_registration`
:   This snippet is loaded and executed by the `Global Registration` template before registering your host to Satellite.

`after_registration`
:   This snippet is loaded and executed by the `Global Registration` template after registering your host to Satellite.

Ensure you name the snippets precisely. Otherwise, the `Global Registration` template cannot load them.

**Prerequisites**

- Your Satellite account has a role that grants the permissions `view_provisioning_templates`, `create_provisioning_templates`, `assign_organizations`, and `assign_locations`.
- You have selected a particular organization and location context.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Click **Create Template**.
3. In the **Name** field, enter the name of the required snippet: `before_registration` or `after_registration`.
4. In the template editor, create your snippet.
5. On the **Type** tab, select **Snippet**.
6. On the **Locations** tab, assign the snippet to required locations.
7. On the **Organizations** tab, assign the snippet to required organizations.
8. Click **Submit**.

**Additional resources**

- [Appendix B, *Template writing reference*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts "Appendix B. Template writing reference")

### 6.2.8. Customizing the registration templates

You can customize the registration process by editing the provisioning templates.

Note that all default templates in Satellite are locked. If you want to customize the registration templates, you must clone the default templates and edit the clones.

> **Note**
>
> Red Hat only provides support for the original unedited templates. Customized templates do not receive updates released by Red Hat.

The registration process uses the following provisioning templates:

- The **Global Registration** template contains steps for registering hosts to Satellite. This template renders when hosts access the `/register` Satellite API endpoint.
- The **Linux host_init_config default** template contains steps for initial configuration of hosts after they are registered.

**Procedure**

1. Navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Search for the template you want to edit.
3. In the row of the required template, click **Clone**.
4. Edit the template as needed. For more information, see [Appendix B, *Template writing reference*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts "Appendix B. Template writing reference").
5. Click **Submit**.
6. Navigate to **Administer** > **Settings** > **Provisioning**.
7. Change the following settings as needed:

   - Point the **Default Global registration template** setting to your custom global registration template,
   - Point the **Default 'Host initial configuration' template** setting to your custom initial configuration template.

### 6.2.9. Running Ansible roles during host registration

You can run Ansible roles when you are registering a host to Satellite.

**Prerequisites**

- The required Ansible roles have been imported from your Capsule to Satellite. For more information, see [Importing Ansible roles and variables](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#Importing_Ansible_Roles_and_Variables_ansible) in *Managing configurations by using Ansible integration*.

**Procedure**

1. Create a host group with Ansible roles. For more information, see [Chapter 5, *Working with host groups*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Working_with_Host_Groups_managing-hosts "Chapter 5. Working with host groups").
2. Register the host by using the host group with assigned Ansible roles. For more information, see [Section 6.2.3, “Registering a host by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-a-host-by-using-web-ui "6.2.3. Registering a host by using Satellite web UI") or [Section 6.2.4, “Registering a host by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-a-host-by-using-cli "6.2.4. Registering a host by using Hammer CLI").

### 6.2.10. Registration command customization

Satellite generates registration commands with ID-based search parameters. Customize URL parameters to search organizations, locations, host groups, and operating systems by title, using URL-encoded values.

You can use the following URL parameters to search resources by title:

Organization
:   URL fragment example: `organization=My%20Organization` or `organization=My+Organization`

Location
:   URL fragment example: `location=My%20Location` or `location=My+Location`

Host group
:   If a host group is nested, include the parent group separated with the slash character (`/`).

    URL fragment example: `hostgroup=Parent%20Group%2FMy%20Host%20Group`

Operating system
:   URL fragment example: `operatingsystem=My%20Operating%20System` or `operatingsystem=My+Operating+System`

The parameter values must be URL encoded.

## 6.3. Invalidating registration tokens

When you generate a registration command in global host registration, Satellite also generates a unique JSON Web Token (JWT) that is used to authorize the registration call from a host to Satellite Server. If needed, you can invalidate a previously issued JWT.

A JWT is bound to the user that generated the registration command.

Users can configure a custom validity duration for the JWT. If the validity duration is too long or if the JWT has been compromised, the JWT poses a security concern. To mitigate this concern, the Satellite administrator or users with adequate permissions can invalidate existing JWTs.

You can also temporarily disable registration tokens by disabling a user. When you reenable the user, the user will be able to continue using their registration tokens.

### 6.3.1. Invalidating your own JWTs by using Satellite web UI

You can invalidate all registration JSON Web Tokens of the current user from the Satellite web UI.

**Procedure**

1. In the Satellite web UI, click the user menu in the top bar and select **My Account**.
2. Select the **Registration Tokens** tab.
3. Click **Invalidate JWTs**.
4. In the confirmation window, click **Confirm**.

**Verification**

- The Satellite web UI displays the following message: `Successfully invalidated registration tokens.`

### 6.3.2. Invalidating your own JWTs by using Hammer CLI

You can invalidate all registration JSON Web Tokens of the current user by using Hammer CLI.

**Procedure**

- Invalidate all your registration tokens:

  ```
  $ hammer user registration-token invalidate --user-id My_User_ID
  ```

### 6.3.3. Invalidating your own JWTs by using Satellite API

You can invalidate all registration JSON Web Tokens of the current user by using Satellite API.

**Procedure**

- Use the `DELETE /api/users/:user_id/registration_tokens` resource.

  For more information, see the full API reference at `https://satellite.example.com/apidoc/v2.html`.

### 6.3.4. Invalidating JWTs of other users by using Satellite web UI

You can invalidate all registration JSON Web Tokens of one or more users from the Satellite web UI.

**Prerequisites**

- Your Satellite user has a role that grants the `edit_users` permissions. For Satellite web UI, you also require the `view_users` permission.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. In the row of the user whose registration tokens you want to invalidate, from the actions menu, select **Invalidate JWTs**.
3. In the confirmation window, click **Confirm**.

**Verification**

- The Satellite web UI displays the following message: `Successfully invalidated registration tokens for the user.`

**Additional resources**

- [Working efficiently with Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui)

### 6.3.5. Invalidating JWTs of other users by using Hammer CLI

You can invalidate all registration JSON Web Tokens of one or more users by using Hammer CLI.

**Prerequisites**

- Your Satellite user has a role that grants the `edit_users` permissions. For Satellite web UI, you also require the `view_users` permission.

**Procedure**

- Invalidate all registration tokens of a single user:

  ```
  $ hammer user registration-token invalidate --user-id User_ID
  ```
- Invalidate all registration tokens of multiple users:

  ```
  $ hammer user registration-token invalidate-multiple --search "My_Search_Query"
  ```

**Additional resources**

- [Working efficiently with Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui)

### 6.3.6. Invalidating JWTs of other users by using API

You can invalidate all registration JSON Web Tokens of one or more users by using Satellite API.

**Prerequisites**

- Your Satellite user has a role that grants the `edit_users` permissions. For Satellite web UI, you also require the `view_users` permission.

**Procedure**

- Invalidate all registration tokens of a single user by using the `DELETE /api/users/:user_id/registration_tokens` resource.
- Invalidate all registration tokens of multiple users by using the `DELETE /api/registration_tokens?search=url-encoded-search-query` resource.

**Additional resources**

- [Working efficiently with Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui)

### 6.3.7. Invalidating JWTs of all users

You can invalidate all registration JSON Web Tokens of all users at once in the Satellite web UI.

**Prerequisites**

- Your Satellite user has a role that grants the `view_users` and `edit_users` permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. Click **Invalidate JWTs for all users**.
3. In the confirmation window, click **Confirm**.

**Verification**

- The Satellite web UI displays the following message: `Successfully invalidated registration tokens for all users.`

## 6.4. Registering hosts by using the bootstrap script

You can use the bootstrap script to automate content registration and Puppet configuration.

> **Important**
>
> The bootstrap script is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Use global registration instead.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

You can use the bootstrap script to register new hosts, or to migrate existing hosts from RHN, SAM, RHSM, or another Red Hat Satellite instance.

The `katello-client-bootstrap` package is installed by default on Satellite Server’s base operating system. The `bootstrap.py` script is installed in the `/var/www/html/pub/` directory to make it available to hosts at `satellite.example.com/pub/bootstrap.py`. The script includes documentation in the `/usr/share/doc/katello-client-bootstrap-version/README.md` file.

To use the bootstrap script, you must install it on the host. As the script is only required once, and only for the `root` user, you can place it in `/root` or `/usr/local/sbin` and remove it after use. This procedure uses `/root`.

> **Important**
>
> Reverse proxying on Capsules is disabled by default for security reasons. Therefore, the bootstrap script does not work if you register hosts through Capsule. Red Hat recommends using global registration to register hosts instead.

**Additional resources**

- [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration")

### 6.4.1. Running the bootstrap script on the host

Download `bootstrap.py` on the host, run it with options for your organization and host group, approve the Puppet certificate when prompted, and verify the host in the Satellite web UI.

**Prerequisites**

- You have a Satellite user with the permissions required to run the bootstrap script. The examples in this procedure specify the `admin` user. If this is not acceptable to your security policy, create a new role with the minimum permissions required and add it to the user that will run the script.
- You have an activation key for your hosts with the Red Hat Satellite Client 6 repository enabled. For information on configuring activation keys, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.
- You have created a host group. For more information about creating host groups, see [Chapter 5, *Working with host groups*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Working_with_Host_Groups_managing-hosts "Chapter 5. Working with host groups").

**Procedure**

1. Log in to the host as the `root` user.
2. Download the script:

   ```
   # curl -O http://satellite.example.com/pub/bootstrap.py
   ```
3. Make the script executable:

   ```
   # chmod +x bootstrap.py
   ```
4. Confirm that the script is executable by viewing the help text:

   - On Red Hat Enterprise Linux 8:

     ```
     # /usr/libexec/platform-python bootstrap.py -h
     ```
   - On other Red Hat Enterprise Linux versions:

     ```
     # ./bootstrap.py -h
     ```
5. Enter the bootstrap command with values suitable for your environment.

   For the `--server` option, specify the FQDN of Satellite Server or a Capsule Server. For the `--location`, `--organization`, and `--hostgroup` options, use quoted names, not labels, as arguments to the options. For advanced use cases, see [Section 6.4.5, “Advanced bootstrap script configuration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Advanced_Bootstrap_Script_Configuration_managing-hosts "6.4.5. Advanced bootstrap script configuration").

   - On Red Hat Enterprise Linux 8, enter the following command:

     ```
     # /usr/libexec/platform-python bootstrap.py \
     --login=admin \
     --server satellite.example.com \
     --location="My_Location" \
     --organization="My_Organization" \
     --hostgroup="My_Host_Group" \
     --activationkey="My_Activation_Key"
     ```
   - On Red Hat Enterprise Linux 7, enter the following command:

     ```
     # ./bootstrap.py --login=admin \
     --server satellite.example.com \
     --location="My_Location" \
     --organization="My_Organization" \
     --hostgroup="My_Host_Group" \
     --activationkey="My_Activation_Key"
     ```
6. Enter the password of the Satellite user you specified with the `--login` option.

   The script sends notices of progress to **stdout**.
7. When prompted by the script, approve the host’s Puppet certificate. In the Satellite web UI, navigate to **Infrastructure** > **Capsules** and find the Satellite or Capsule Server you specified with the `--server` option.
8. From the list in the **Actions** column, select **Certificates**.
9. In the **Actions** column, click **Sign** to approve the host’s Puppet certificate.
10. Return to the host to see the remainder of the bootstrap process completing.
11. In the Satellite web UI, navigate to **Hosts** > **All Hosts** and ensure that the host is connected to the correct host group.
12. Optional: After the host registration is complete, remove the script:

    ```
    # rm bootstrap.py
    ```

### 6.4.2. Creating a Puppet environment for bootstrap registration

If a host group is associated with a Puppet environment created inside a `Production` environment, Puppet fails to retrieve the Puppet CA certificate while registering a host from that host group. You must create a suitable Puppet environment to be associated with a host group.

**Procedure**

1. Manually create a directory:

   ```
   # mkdir /etc/puppetlabs/code/environments/example_environment
   ```
2. In the Satellite web UI, navigate to **Configure** > **Puppet ENC** > **Environments**.
3. Click **Import environment from**.
4. Select your Capsule.
5. Choose the created directory and click **Update**.

### 6.4.3. Setting permissions for the bootstrap script by using Satellite web UI

You can configure a Satellite user with the permissions required to run the bootstrap script from the Satellite web UI. This allows the user to register hosts with the script without granting full administrative access.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. Select an existing user by clicking the required **Username**. A new pane opens with tabs to modify information about the selected user. Alternatively, create a new user specifically for the purpose of running this script.
3. Click the **Roles** tab.
4. Select **Edit hosts** and **Viewer** from the **Roles** list.

   > **Important**
   >
   > The **Edit hosts** role allows the user to edit and delete hosts as well as being able to add hosts. If this is not acceptable to your security policy, create a new role with the following permissions and assign it to the user:
   >
   > - `view_organizations`
   > - `view_locations`
   > - `view_domains`
   > - `view_hostgroups`
   > - `view_hosts`
   > - `view_architectures`
   > - `view_ptables`
   > - `view_operatingsystems`
   > - `create_hosts`
5. Click **Submit**.

### 6.4.4. Setting permissions for the bootstrap script by using Hammer CLI

You can configure a Satellite user with the permissions required to run the bootstrap script by using Hammer CLI. This allows the user to register hosts with the script without granting full administrative access.

**Procedure**

1. Create a role with the minimum permissions required by the bootstrap script. This example creates a role with the name *Bootstrap*:

   ```
   $ ROLE='Bootstrap'
   $ hammer role create --name "$ROLE"
   $ hammer filter create --role "$ROLE" --permissions view_organizations
   $ hammer filter create --role "$ROLE" --permissions view_locations
   $ hammer filter create --role "$ROLE" --permissions view_domains
   $ hammer filter create --role "$ROLE" --permissions view_hostgroups
   $ hammer filter create --role "$ROLE" --permissions view_hosts
   $ hammer filter create --role "$ROLE" --permissions view_architectures
   $ hammer filter create --role "$ROLE" --permissions view_ptables
   $ hammer filter create --role "$ROLE" --permissions view_operatingsystems
   $ hammer filter create --role "$ROLE" --permissions create_hosts
   ```
2. Assign the new role to an existing user:

   ```
   $ hammer user add-role --id user_id --role Bootstrap
   ```

   Alternatively, you can create a new user and assign this new role to them. For more information on creating users with Hammer, see [Managing users and roles](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Managing_Users_and_Roles_admin) in *Administering Red Hat Satellite*.

### 6.4.5. Advanced bootstrap script configuration

Use these advanced bootstrap script examples to register or migrate hosts with custom options and minimum required permissions.

> **Warning**
>
> These examples specify the `admin` Satellite user. If this is not acceptable to your security policy, create a new role with the minimum permissions required by the bootstrap script.

### 6.4.6. Migrating a host from one Satellite to another Satellite

Use the script with `--force` to remove the `katello-ca-consumer-*` packages from the old Satellite and install the `katello-ca-consumer-*` packages on the new Satellite.

> **Important**
>
> The `katello-ca-consumer` RPM package and `katello-rhsm-consumer` script is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Use global registration instead.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --force
  ```
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # bootstrap.py --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --force
  ```

**Additional resources**

- [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration")

### 6.4.7. Migrating a host from Red Hat Network (RHN) or Satellite 5 to Satellite

You can migrate a host from Red Hat Network (RHN) or Satellite 5 to Satellite by using the bootstrap script.

The bootstrap script detects the presence of `/etc/syconfig/rhn/systemid` and a valid connection to RHN as an indicator that the system is registered to a legacy platform. The script then calls `rhn-classic-migrate-to-rhsm` to migrate the system from RHN. By default, the script does not delete the system’s legacy profile due to auditing reasons. To remove the legacy profile, use `--legacy-purge`, and use `--legacy-login` to supply a user account that has appropriate permissions to remove a profile.

Enter the user account password when prompted.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --legacy-purge \
  --legacy-login rhn-user
  ```
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # bootstrap.py --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --legacy-purge \
  --legacy-login rhn-user
  ```

### 6.4.8. Registering a host to Satellite without Puppet

By default, the bootstrap script configures the host for content management and configuration management. If you have an existing configuration management system and do not want to install Puppet on the host, use `--skip-puppet`.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --skip-puppet
  ```
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # bootstrap.py --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --skip-puppet
  ```

### 6.4.9. Registering a host to Satellite for content management only

To register a system as a host, and omit the provisioning and configuration management functions, use `--skip-foreman`.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --server satellite.example.com \
  --organization="My_Organization" \
  --activationkey="My_Activation_Key" \
  --skip-foreman
  ```
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # bootstrap.py --server satellite.example.com \
  --organization="My_Organization" \
  --activationkey="My_Activation_Key" \
  --skip-foreman
  ```

### 6.4.10. Changing the method the bootstrap script uses to download the consumer RPM

By default, the bootstrap script uses HTTP to download the consumer RPM from `http://satellite.example.com/pub/katello-ca-consumer-latest.noarch.rpm`. In some environments, you might want to allow HTTPS only between the host and Satellite. Use `--download-method` to change the download method from HTTP to HTTPS.

> **Important**
>
> The `katello-ca-consumer` RPM package and `katello-rhsm-consumer` script is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Use global registration instead.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --download-method https
  ```
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # bootstrap.py --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --download-method https
  ```

**Additional resources**

- [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration")

### 6.4.11. Providing the host’s IP address to Satellite

On hosts with multiple interfaces or multiple IP addresses on one interface, you might need to override the auto-detection of the IP address and provide a specific IP address to Satellite. Use `--ip`.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --ip 192.x.x.x
  ```
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # bootstrap.py --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --ip 192.x.x.x
  ```

### 6.4.12. Enabling remote execution on the host

Use `--rex` and `--rex-user` to enable remote execution and add the required SSH keys for the specified user.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --rex \
  --rex-user root
  ```
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # bootstrap.py --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --rex \
  --rex-user root
  ```

### 6.4.13. Creating a domain for a host during registration

To create a host record, the DNS domain of a host needs to exist in Satellite prior to running the script. If the domain does not exist, add it using `--add-domain`.

**Procedure**

- On Red Hat Enterprise Linux 8, enter the following command:

  ```
  # /usr/libexec/platform-python bootstrap.py \
  --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --add-domain
  ```
- On Red Hat Enterprise Linux 7, enter the following command:

  ```
  # bootstrap.py --login=admin \
  --server satellite.example.com \
  --location="My_Location" \
  --organization="My_Organization" \
  --hostgroup="My_Host_Group" \
  --activationkey="My_Activation_Key" \
  --add-domain
  ```

### 6.4.14. Providing an alternative FQDN for the host

If the host name of the host is not an FQDN, or is not RFC-compliant (containing a character such as an underscore), the script will fail at the host name validation stage. If you cannot update the host to use an FQDN that is accepted by Satellite, you can use the bootstrap script to specify an alternative FQDN.

**Procedure**

1. Set `create_new_host_when_facts_are_uploaded` and `create_new_host_when_report_is_uploaded` to false using Hammer:

   ```
   $ hammer settings set \
   --name create_new_host_when_facts_are_uploaded \
   --value false
   $ hammer settings set \
   --name create_new_host_when_report_is_uploaded \
   --value false
   ```
2. Use `--fqdn` to specify the FQDN that will be reported to Satellite:

   - On Red Hat Enterprise Linux 8, enter the following command:

     ```
     # /usr/libexec/platform-python bootstrap.py --login=admin \
     --server satellite.example.com \
     --location="My_Location" \
     --organization="My_Organization" \
     --hostgroup="My_Host_Group" \
     --activationkey="My_Activation_Key" \
     --fqdn node100.example.com
     ```
   - On Red Hat Enterprise Linux 7, enter the following command:

     ```
     # bootstrap.py --login=admin \
     --server satellite.example.com \
     --location="My_Location" \
     --organization="My_Organization" \
     --hostgroup="My_Host_Group" \
     --activationkey="My_Activation_Key" \
     --fqdn node100.example.com
     ```

## 6.5. Katello CA consumer RPM and RHSM consumer script

The `katello-ca-consumer` RPM package and `katello-rhsm-consumer` script were previously available to register hosts to Satellite.

> **Important**
>
> The `katello-ca-consumer` RPM package and `katello-rhsm-consumer` script is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Use global registration instead.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

When using the Katello CA Consumer for host registration, you download and install the consumer RPM from `satellite.example.com/pub/katello-ca-consumer-latest.noarch.rpm` on the host and then run `subscription-manager`.

**Additional resources**

- [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration")
