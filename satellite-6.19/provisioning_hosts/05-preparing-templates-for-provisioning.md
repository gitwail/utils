---
title: "Preparing templates for provisioning"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-templates-for-provisioning"
---
# Chapter 5. Preparing templates for provisioning

You can customize the provisioning process without editing the default provisioning templates. You can define host parameters and add custom steps by creating custom `pre` or `post` snippets.

Satellite provides the following default template types:

- Provisioning templates
- Partition tables

You can use the default templates or create custom templates.

Thanks to partition tables implemented as templates, you can create custom, even dynamic, partition tables.

When you do not edit the default templates, maintenance is easier and you get the benefit of updates to the templates from Red Hat.

## 5.1. Provisioning templates

A provisioning template defines the way Satellite Server installs an operating system on a host.

Red Hat Satellite includes many template examples. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates** to view them. You can create a template or clone a template and edit the clone. For help with templates, navigate to **Hosts** > **Templates** > **Provisioning Templates** > **Create Template** > **Help**.

Templates supported by Red Hat are indicated by a Red Hat icon.

To hide unsupported templates, in the Satellite web UI navigate to **Administer** > **Settings**. On the **Provisioning** tab, set the value of **Show unsupported provisioning templates** to `false` and click **Submit**. You can also filter out the supported templates by making the following query "supported = true".

If you clone a supported template, the cloned template will be unsupported.

Templates accept the Embedded Ruby (ERB) syntax.

You can download provisioning templates. Before you can download the template, you must create a debug certificate.

You can synchronize templates between Satellite Server and a Git repository or a local directory.

To view the history of changes applied to a template, navigate to **Hosts** > **Templates** > **Provisioning Templates**, select one of the templates, and click **History**. Click **Revert** to override the content with the previous version. You can also revert to an earlier change. Click **Show Diff** to see information about a specific change:

- The **Template Diff** tab displays changes in the body of a provisioning template.
- The **Details** tab displays changes in the template description.
- The **History** tab displays the user who made a change to the template and date of the change.

**Additional resources**

- [Template Writing Reference in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts)
- [Creating an Organization Debug Certificate in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Creating_an_Organization_Debug_Certificate_admin)
- [Synchronizing template repositories in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#synchronizing-template-repositories)

## 5.2. Kinds of provisioning templates

Satellite provides templates for different host provisioning workflows. Choose a provisioning template type based on your compute resource and provisioning environment.

Provision
:   The main template for the provisioning process. For example, a Kickstart template. For more information about Kickstart syntax and commands, see the following resources:

    - [Automated installation workflow](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/automatically_installing_rhel/automated-installation-workflow_rhel-installer) in *Automatically installing RHEL 9*
    - [Automated installation workflow](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/automatically_installing_rhel/automated-installation-workflow_rhel-installer) in *Automatically installing RHEL 8*
    - [Kickstart Syntax Reference](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/installation_guide/sect-kickstart-syntax) in the *Red Hat Enterprise Linux 7 Installation Guide*

PXELinux and PXEGrub2
:   PXE-based templates that deploy to the template Capsule associated with a subnet to ensure that the host uses the installer with the correct kernel options. For BIOS provisioning, select **PXELinux** template. For UEFI provisioning, select **PXEGrub2**.

Finish
:   Post-configuration scripts to execute using an SSH connection when the main provisioning process completes. You can use Finish templates only for image-based provisioning in virtual or cloud environments that do not support user_data. Do not confuse an image with a foreman discovery ISO, which is sometimes called a Foreman discovery image. An image in this context is an install image in a virtualized environment for easy deployment.

    When a finish script successfully exits with the return code `0`, Red Hat Satellite treats the code as a success and the host exits the build mode.

    Note that there are a few finish scripts with a build mode that uses a *call back* HTTP call. These scripts are not used for image-based provisioning, but for post configuration of operating-system installations such as Debian, Ubuntu, and BSD. Red Hat does not support provisioning of operating systems other than Red Hat Enterprise Linux.

user_data
:   Post-configuration scripts for providers that accept custom data, also known as seed data. You can use the user_data template to provision virtual machines in cloud or virtualised environments only. This template does not require Satellite to be able to reach the host; the cloud or virtualization platform is responsible for delivering the data to the image.

    Ensure that the image that you want to provision has the software to read the data installed and set to start during boot. For example, `cloud-init`, which expects YAML input, or `ignition`, which expects JSON input.

cloud_init
:   Some environments, such as VMWare, either do not support custom data or have their own data format that limits what can be done during customization. In this case, you can configure a cloud-init client with the `foreman` plugin, which attempts to download the template directly from Satellite over HTTP or HTTPS. This technique can be used in any environment, preferably virtualized.

    Ensure that you meet the following requirements to use the `cloud_init` template:

    - Ensure that the image that you want to provision has the software to read the data installed and set to start during boot.
    - A provisioned host is able to reach Satellite from the IP address that matches the host’s provisioning interface IP.

      Note that cloud-init does not work behind NAT.

Bootdisk
:   Templates for PXE-less boot methods.

Kernel Execution (kexec)
:   Kernel execution templates for PXE-less boot methods.

    > **Note**
    >
    > Kernel Execution is a Technology Preview feature. Technology Preview features are not fully supported under Red Hat Subscription Service Level Agreements (SLAs), may not be functionally complete, and are not intended for production use. However, these features provide early access to upcoming product innovations, enabling customers to test functionality and provide feedback during the development process.

Script
:   An arbitrary script not used by default but useful for custom tasks.

ZTP
:   Zero Touch Provisioning templates.

POAP
:   PowerOn Auto Provisioning templates.

iPXE
:   Templates for `iPXE` or `gPXE` environments to use instead of PXELinux.

## 5.3. Creating provisioning templates by using Satellite web UI

Define how Satellite installs an operating system on a host by creating a provisioning template.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates** and click **Create Template**.
2. In the **Name** field, enter a name for the provisioning template.
3. Fill in the rest of the fields as required. The **Help** tab provides information about the template syntax and details the available functions, variables, and methods that can be called on different types of objects within the template.

## 5.4. Creating provisioning templates by using Hammer CLI

Define how Satellite installs an operating system on a host by creating a provisioning template.

**Procedure**

1. Before you create a template with the CLI, create a plain text file that contains the template. This example uses the `~/my-template` file.
2. Create the template using the `hammer template create` command and specify the type with the `--type` option:

   ```
   $ hammer template create \
   --file ~/my-template \
   --locations "My_Location" \
   --name "My_Provisioning_Template" \
   --organizations "My_Organization" \
   --type provision
   ```

## 5.5. Cloning provisioning templates

A provisioning template defines the way Satellite Server installs an operating system on a host. You can clone a template and then apply your changes to the clone without changing the original template.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Find the template that you want to use.
3. Click **Clone** to duplicate the template.
4. In the **Name** field, enter a name for the provisioning template.
5. Select the **Default** checkbox to set the template to associate automatically with new organizations or locations.
6. In the **Template editor** field, enter the body of the provisioning template. You can also use the **Template** file browser to upload a template file.
7. In the **Audit Comment** field, enter a summary of changes to the provisioning template for auditing purposes.
8. Click the **Type** tab and if your template is a snippet, select the **Snippet** checkbox. A snippet is not a standalone provisioning template, but a part of a provisioning template that can be inserted into other provisioning templates.
9. From the **Type** list, select the type of the template. For example, **Provisioning template**.
10. Click the **Association** tab and from the **Applicable Operating Systems** list, select the names of the operating systems that you want to associate with the provisioning template.
11. Optionally, click **Add combination** and select a host group from the **Host Group** list or an environment from the **Environment** list to associate provisioning template with the host groups and environments.
12. Click the **Organizations** and **Locations** tabs to add any additional contexts to the template.
13. Click **Submit** to save your provisioning template.

## 5.6. Running custom code during host provisioning by using Satellite web UI

You can run custom code before or after provisioning the host by creating a custom provisioning snippet.

**Prerequisites**

- Check your provisioning template to ensure that it supports the custom snippets you want to use.

  You can view all provisioning templates under **Hosts** > **Templates** > **Provisioning Templates**.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Click **Create Template**.
3. In the **Name** field, enter a name for your custom provisioning snippet. The name must start with the name of a provisioning template that supports including custom provisioning snippets:

   - Append `custom pre` to the name of a provisioning template to run code before provisioning a host.
   - Append `custom post` to the name of a provisioning template to run code after provisioning a host.
4. On the **Type** tab, select **Snippet**.
5. Click **Submit** to create your custom provisioning snippet.

## 5.7. Running custom code during host provisioning by using Hammer CLI

You can run custom code before or after provisioning the host by creating a custom provisioning snippet.

**Prerequisites**

- Check your provisioning template to ensure that it supports the custom snippets you want to use.

  You can view all provisioning templates under **Hosts** > **Templates** > **Provisioning Templates**.

**Procedure**

1. Create a plain text file that contains your custom snippet.
2. Create the template using `hammer`:

   ```
   $ hammer template create \
   --file "/path/to/My_Snippet" \
   --locations "My_Location" \
   --name "My_Template_Name_custom_pre" \ --organizations "_My_Organization" \
   --type snippet
   ```

## 5.8. Custom provisioning snippet example for Red Hat Enterprise Linux

You can use `custom post` snippets to call external APIs from within the provisioning template directly after provisioning a host.

**Example 5.1. `Kickstart default finish custom post` Example for Red Hat Enterprise Linux**

```
echo "Calling API to report successful host deployment"

yum install -y curl ca-certificates

curl -X POST \
-H "Content-Type: application/json" \
-d '{"name": "<%= @host.name %>", "operating_system": "<%= @host.operatingsystem.name %>", "status": "provisioned",}' \
"https://api.example.com/"
```

## 5.9. Deploying SSH keys during provisioning

You can deploy SSH keys during provisioning to establish secure, passwordless remote access to newly provisioned hosts.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Create a provisioning template, or clone and edit an existing template. For more information, see [Section 5.3, “Creating provisioning templates by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-provisioning-templates-by-using-web-ui "5.3. Creating provisioning templates by using Satellite web UI").
3. In the template, click the **Template** tab.
4. In the **Template editor** field, add the `create_users` snippet to the `%post` section:

   ```
   <%= snippet('create_users') %>
   ```
5. Select the **Default** checkbox.
6. Click the **Association** tab.
7. From the **Application Operating Systems** list, select an operating system.
8. Click **Submit** to save the provisioning template.
9. Create a host that is associated with the provisioning template or rebuild a host using the operating system associated with the modified template.

   The SSH keys of the **Owned by** user are added automatically when the `create_users` snippet is executed during the provisioning process. You can set **Owned by** to an individual user or a user group. If you set **Owned by** to a user group, the SSH keys of all users in the user group are added automatically.

**Additional resources**

- [Managing SSH keys for a user by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-ssh-keys-for-a-user-by-using-web-ui)

## 5.10. Associating templates with operating systems by using Satellite web UI

You can associate templates with operating systems in Satellite. The following example adds a provisioning template to an operating system entry.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Provisioning Templates**.
2. Select a provisioning template.
3. On the **Association** tab, select all applicable operating systems.
4. Click **Submit** to save your changes.

## 5.11. Associating templates with operating systems by using Hammer CLI

You can associate templates with operating systems in Satellite. The following example adds a provisioning template to an operating system entry.

**Procedure**

1. Optional: View all templates:

   ```
   $ hammer template list
   ```
2. Optional: View all operating systems:

   ```
   $ hammer os list
   ```
3. Associate a template with an operating system:

   ```
   $ hammer template add-operatingsystem \
   --id My_Template_ID \
   --operatingsystem-id My_Operating_System_ID
   ```

## 5.12. Creating partition tables by using Satellite web UI

You can create custom partition tables with your preferred partitioning scheme instead of the default tables in Satellite. To use them during provisioning, associate partition tables with operating systems.

Partition tables use ERB syntax similar to provisioning templates.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Partition Tables**.
2. Click **Create Partition Table**.
3. In the **Name** field, enter a name for the partition table.
4. Select the **Default** checkbox if you want to set the template to automatically associate with new organizations or locations.
5. Select the **Snippet** checkbox if you want to identify the template as a reusable snippet for other partition tables.
6. From the **Operating System Family** list, select the distribution or family of the partitioning layout. For example, Red Hat Enterprise Linux, CentOS, and Fedora are in the Red Hat family.
7. In the **Template editor** field, enter the layout for the disk partition.

   The format of the layout must match that for the intended operating system. For example, Red Hat Enterprise Linux requires a layout that matches a Kickstart file, such as:

   ```
   zerombr
   clearpart --all --initlabel
   autopart
   ```

   For more information, see [Section 5.15, “Dynamic partition example”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#dynamic-partition-example "5.15. Dynamic partition example").

   You can also use the file browser in the template editor to import the layout from a file.
8. In the **Audit Comment** field, add a summary of changes to the partition layout.
9. Click the **Organizations** and **Locations** tabs to add any other provisioning contexts that you want to associate with the partition table. Satellite adds the partition table to the current provisioning context.
10. Click **Submit** to save your partition table.

## 5.13. Creating partition tables by using Hammer CLI

You can create custom partition tables with your preferred partitioning scheme instead of the default tables in Satellite. To use them during provisioning, associate partition tables with operating systems.

Partition tables use ERB syntax similar to provisioning templates.

**Procedure**

1. Create a plain text file, such as `~/My_Partition_Table`, that contains the partition layout.

   The format of the layout must match that for the intended operating system. For example, Red Hat Enterprise Linux requires a layout that matches a Kickstart file, such as:

   ```
   zerombr
   clearpart --all --initlabel
   autopart
   ```

   For more information, see [Section 5.15, “Dynamic partition example”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#dynamic-partition-example "5.15. Dynamic partition example").
2. Create the installation medium:

   ```
   $ hammer partition-table create \
   --file "~/My_Partition_Table" \
   --locations "My_Location" \
   --name "My_Partition_Table" \
   --organizations "My_Organization" \
   --os-family "Redhat" \
   --snippet false
   ```

## 5.14. Associating partition tables with disk encryption

You can encrypt host disks by using Linux Unified Key Setup (LUKS) during provisioning to protect data at rest. Optionally, bind the disk to a Tang server through Clevis for decryption during boot.

Associate the partition table with your operating system entry. Then, you assign the partition table to your host group or select it manually during provisioning.

**Prerequisites**

- Your host has access to the `AppStream` repository to install `clevis` during provisioning.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Provisioning Setup** > **Operating Systems**.
2. Select your Red Hat Enterprise Linux entry.
3. On the **Partition Table** tab, associate `Kickstart default encrypted` with your operating system entry.
4. Create a host group that uses the `Kickstart default encrypted` partition table. For more information, see [Working with host groups](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Working_with_Host_Groups_managing-hosts) in *Managing hosts*.
5. Decrypt the disk of your host during boot time by using one of the following options:

   - LUKS encryption: Add the host parameter `disk_enc_passphrase` as type **string** and your cleartext passphrase of the LUKS container as the value.
   - Clevis and Tang: Add the host parameter `disk_enc_tang_servers` as type **array** and your list of Tang servers (example: `["1.2.3.4"]` or `["server.example.com", "5.6.7.8"]`).

     If you set `disk_enc_tang_servers`, do not set `disk_enc_passphrase` because the passphrase slot is removed from the LUKS container after provisioning.

## 5.15. Dynamic partition example

This example demonstrates dynamic partitioning in a Kickstart template that erases the disk, creates partitions automatically, and enlarges one partition to maximum size.

```
zerombr
clearpart --all --initlabel
autopart <%= host_param('autopart_options') %>
```

Dynamic partitioning is executed by the installation program. Therefore, you can write your own rules to specify how you want to partition disks according to runtime information from the node, for example, disk sizes, number of drives, vendor, or manufacturer.

If you want to provision servers and use dynamic partitioning, add the following example as a template. When the `#Dynamic` entry is included, the content of the template loads into a `%pre` shell scriplet and creates a `/tmp/diskpart.cfg` that is then included into the Kickstart partitioning section.

```
#Dynamic (do not remove this line)

MEMORY=$((`grep MemTotal: /proc/meminfo | sed 's/^MemTotal: *//'|sed 's/ .*//'` / 1024))
if [ "$MEMORY" -lt 2048 ]; then
    SWAP_MEMORY=$(($MEMORY * 2))
elif [ "$MEMORY" -lt 8192 ]; then
    SWAP_MEMORY=$MEMORY
elif [ "$MEMORY" -lt 65536 ]; then
    SWAP_MEMORY=$(($MEMORY / 2))
else
    SWAP_MEMORY=32768
fi

cat <<EOF > /tmp/diskpart.cfg
zerombr
clearpart --all --initlabel
part /boot --fstype ext4 --size 200 --asprimary
part swap --size "$SWAP_MEMORY"
part / --fstype ext4 --size 1024 --grow
EOF
```
