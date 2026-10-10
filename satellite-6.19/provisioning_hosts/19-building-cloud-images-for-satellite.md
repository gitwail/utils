---
title: "Building cloud images for Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "B"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#building-cloud-images-for-satellite"
---
# Appendix B. Building cloud images for Satellite

You can create a cloud image from a working system and use it to provision cloud instances.

Repeat the procedures for every image that you want to provision with Satellite. Move the image to the location where you want to store it for future use.

## B.1. Preconfigured Red Hat Enterprise Linux KVM guest images

You can use preconfigured Red Hat Enterprise Linux KVM guest QCOW2 images to provision cloud instances.

Select a preconfigured Red Hat Enterprise Linux KVM guest QCOW2 image:

- [Latest RHEL 9 KVM Guest Image](https://access.redhat.com/downloads/content/479/ver=/rhel---9/9.0/x86_64/product-software)
- [Latest RHEL 8 KVM Guest Image](https://access.redhat.com/downloads/content/479/ver=/rhel---8/8.0/x86_64/product-software)

These images contain `cloud-init`. To function properly, they must use ec2-compatible metadata services for provisioning an SSH key.

> **Note**
>
> For the KVM guest images:
>
> - The `root` account in the image is disabled, but `sudo` access is granted to a special user named `cloud-user`.
> - There is no `root` password set for this image. The `root` password is locked in `/etc/shadow` by placing `!!` in the second field.

If you want to create custom Red Hat Enterprise Linux images, see [*Composing a customized Red Hat Enterprise Linux 9 Image*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/composing_a_customized_rhel_system_image/index) or [*Composing a customized Red Hat Enterprise Linux 8 Image*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/composing_a_customized_rhel_system_image/index).

## B.2. Host requirements for custom Red Hat Enterprise Linux images

Before you create an image, you need to manually install and configure a Red Hat Enterprise Linux image on a dedicated host.

Ensure that your environment meets the following requirements: * Use a Linux host machine to create an image. This example uses Red Hat Enterprise Linux 7 Workstation. * Use `virt-manager` on your workstation to complete this procedure. If you create the image on a remote server, connect to the server from your workstation with `virt-manager`. * A Red Hat Enterprise Linux 7 ISO file (see [Red Hat Enterprise Linux 7.4 Binary DVD](https://access.redhat.com/downloads/content/69/ver=/rhel---7/7.4/x86_64/product-software)).

For more information about installing your Red Hat Enterprise Linux Workstation, see the [*Red Hat Enterprise Linux 7 Installation Guide*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html-single/installation_guide/index).

Before you can create custom images, install the following packages:

- Install `libvirt`, `qemu-kvm`, and graphical tools:

  ```
  # yum install virt-manager virt-viewer libvirt qemu-kvm
  ```
- Install the following command line tools:

  ```
  # yum install virt-install libguestfs-tools-c
  ```

> **Note**
>
> In the following procedures, enter all commands with the `[root@host]#` prompt on the workstation that hosts the `libvirt` environment.

## B.3. Supported clients in registration

You can register hosts with supported operating systems and architectures.

The hosts can use the following operating systems:

- Red Hat Enterprise Linux 10, 9, and 8
- Red Hat Enterprise Linux 7 with the [ELS Add-On](https://www.redhat.com/en/resources/els-datasheet)

The hosts can use the following architectures:

- AMD and Intel 64-bit architectures
- The 64-bit ARM architecture
- IBM Power Systems, Little Endian
- 64-bit IBM Z architectures

## B.4. Configuring a host for registration

Configure your host for registration to Satellite Server or Capsule Server. You can use a configuration management tool to configure multiple hosts at once.

**Prerequisites**

- The host must be using a supported operating system. For more information, see [Section B.3, “Supported clients in registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#supported-clients-in-registration_provisioning "B.3. Supported clients in registration").
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

## B.5. Registering a host by using Satellite web UI

You can register a host by using the Satellite web UI with registration templates. This also enables you to set up various integration features and host tools during the registration process.

**Prerequisites**

- Your Satellite account has the **Register hosts** role assigned or a role with equivalent permissions.
- Root privileges are available on the host that you want to register.
- Either `curl` or `wget` is installed on the host that you want to register.
- Your host is configured for registration. For more information, see [Section B.4, “Configuring a host for registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Configuring_a_Host_for_Registration_provisioning "B.4. Configuring a host for registration").
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

## B.6. Registering a host by using Hammer CLI

You can register a host by using Hammer CLI with registration templates. This also enables you to set up various integration features and host tools during the registration process.

**Prerequisites**

- Your Satellite account has the **Register hosts** role assigned or a role with equivalent permissions.
- Root privileges are available on the host that you want to register.
- Either `curl` or `wget` is installed on the host that you want to register.
- Your host is configured for registration. For more information, see [Section B.4, “Configuring a host for registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Configuring_a_Host_for_Registration_provisioning "B.4. Configuring a host for registration").
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

## B.7. Registering a host by using Satellite API

You can register a host by using Satellite API with registration templates. This also enables you to set up various integration features and host tools during the registration process.

**Prerequisites**

- Your Satellite account has the **Register hosts** role assigned or a role with equivalent permissions.
- Root privileges are available on the host that you want to register.
- Either `curl` or `wget` is installed on the host that you want to register.
- Your host is configured for registration. For more information, see [Section B.4, “Configuring a host for registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#Configuring_a_Host_for_Registration_provisioning "B.4. Configuring a host for registration").
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

## B.8. Registering a host by using Ansible

You can register a host with an Ansible playbook by using registration templates and set up various integration features and host tools during the registration process.

**Procedure**

- Use the `redhat.satellite.registration_command` module.

  For more information, see the Ansible module documentation with `ansible-doc redhat.satellite.registration_command`.

**Verification**

- If your activation key was supposed to enable repositories, check the `/etc/yum.repos.d/redhat.repo` file and verify that the repositories have been enabled.

## B.9. Configuring OpenVox agent on a host manually

On hosts that are already registered to Satellite, you can install and configure the OpenVox agent manually. A configured OpenVox agent is required on the host for Puppet integration with your Satellite.

**Prerequisites**

- Puppet must be enabled in your Satellite. For more information, see [*Managing configurations by using Puppet integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#).
- The host must have a Puppet environment assigned to it.
- Red Hat Satellite Client 6 OpenVox repository is synchronized on Satellite Server, available in the content view and the lifecycle environment of the host, and enabled for the host.

  Choose from the following repositories, based on the operating system version and the architecture of the host you are registering:

  - satellite-client-openvox-for-rhel-10-aarch64-rpms
  - satellite-client-openvox-for-rhel-10-x86_64-rpms
  - satellite-client-openvox-for-rhel-9-aarch64-rpms
  - satellite-client-openvox-for-rhel-9-x86_64-rpms
  - satellite-client-openvox-for-rhel-8-aarch64-rpms
  - satellite-client-openvox-for-rhel-8-x86_64-rpms

**Procedure**

1. Log in to the host as the `root` user.
2. Install the OpenVox agent package:

   - On hosts running Red Hat Enterprise Linux 8 and later:

     ```
     # dnf install openvox-agent
     ```
   - On hosts running Red Hat Enterprise Linux 7:

     ```
     # yum install openvox-agent
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

## B.10. Completing the Red Hat Enterprise Linux 7 image

To ensure that VMs deployed from your image are treated as clean and unique instances that can be successfully registered and managed by Satellite, prepare your pre-built Red Hat Enterprise Linux 7 image for cloud or virtual machine deployment and subsequent management by Satellite.

**Procedure**

1. Update the system:

   ```
   # yum update
   ```
2. Install the `cloud-init` packages:

   ```
   # yum install cloud-utils-growpart cloud-init
   ```
3. Open the `/etc/cloud/cloud.cfg` configuration file:

   ```
   # vi /etc/cloud/cloud.cfg
   ```
4. Under the heading `cloud_init_modules`, add:

   ```
   - resolv-conf
   ```

   The `resolv-conf` option automatically configures the `resolv.conf` when an instance boots for the first time. This file contains information related to the instance such as `nameservers`, `domain` and other options.
5. Open the `/etc/sysconfig/network` file:

   ```
   # vi /etc/sysconfig/network
   ```
6. Add the following line to avoid problems accessing the EC2 metadata service:

   ```
   NOZEROCONF=yes
   ```
7. Un-register the virtual machine so that the resulting image does not contain the same subscription details for every instance cloned based on it:

   ```
   # subscription-manager repos --disable=*
   # subscription-manager unregister
   ```
8. Power off the instance:

   ```
   # poweroff
   ```
9. On your Red Hat Enterprise Linux Workstation, connect to the terminal as the root user and navigate to the `/var/lib/libvirt/images/` directory:

   ```
   # cd /var/lib/libvirt/images/
   ```
10. Reset and clean the image using the `virt-sysprep` command so it can be used to create instances without issues:

    ```
    # virt-sysprep -d rhel7
    ```
11. Reduce image size using the `virt-sparsify` command. This command converts any free space within the disk image back to free space within the host:

    ```
    # virt-sparsify --compress rhel7.qcow2 rhel7-cloud.qcow2
    ```

    This creates a new `rhel7-cloud.qcow2` file in the location where you enter the command.
