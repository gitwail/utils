---
title: "Converting hosts to Red Hat Enterprise Linux"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "12"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#converting-hosts-to-rhel"
---
# Chapter 12. Converting hosts to Red Hat Enterprise Linux

You can convert Red Hat Enterprise Linux derivative distributions, such as CentOS or Oracle Linux, to supported Red Hat Enterprise Linux on a host while retaining installed applications and configurations. This helps you move your hosts to Red Hat Enterprise Linux without a full reinstall.

## 12.1. Overview of the conversion process

You can use the Convert2RHEL utilities in Satellite to convert CentOS or Oracle Linux hosts to Red Hat Enterprise Linux. The process replaces packages with Red Hat Enterprise Linux equivalents while retaining applications and configurations.

The conversion process is similar to a minor release upgrade of Red Hat Enterprise Linux in which every RPM package on the system is replaced. Third-party packages and non-Red Hat packages that are not available in Red Hat Enterprise Linux are retained.

The Convert2RHEL utility removes unnecessary packages such as logos or packages known to cause issues during the conversion. The utility replaces the `CentOS-release` or `Oracle-release` package with the `rhel-release` package, and all packages signed by CentOS or Oracle with their Red Hat equivalents. The utility also subscribes the host to Red Hat Subscription Management.

The duration of the conversion process depends on the number of packages that have to be replaced, network speed, storage speed, and similar factors.

These following conversions are supported by Red Hat:

- CentOS Linux 7 to Red Hat Enterprise Linux 7
- Oracle Linux 7 to Red Hat Enterprise Linux 7
- Oracle Linux 8 to Red Hat Enterprise Linux 8

If you convert to a RHEL version that is in the Extended Life Phase and you do not plan to upgrade your host to a fully supported RHEL version, Red Hat recommends using an Extended Life Cycle Support (ELS) Add-On subscription during the conversion. Note that the conversion and the subsequent upgrade without an ELS subscription come with a limited support scope.

**Additional resources**

- [Extended Life Phase](https://access.redhat.com/support/policy/updates/errata#Extended_Life_Cycle_Phase)
- [RHEL Conversion Support Policy](https://access.redhat.com/support/policy/convert2rhel-support)
- [RHEL In-place upgrade Support Policy](https://access.redhat.com/support/policy/ipu-support)

## 12.2. Converting a host to Red Hat Enterprise Linux

You can convert a host to Red Hat Enterprise Linux by using the Convert2RHEL Ansible role and playbook in Satellite. The role prepares conversion data on Satellite Server, and the playbook runs the conversion on the host.

**Prerequisites**

- You have reviewed the [supported conversion paths](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html-single/converting_from_a_linux_distribution_to_rhel_using_the_convert2rhel_utility/index#con_supported-conversion-paths_converting-from-a-linux-distribution-to-rhel) in *Red Hat Enterprise Linux 8 Converting from a Linux distribution to RHEL using the Convert2RHEL utility*.
- A subscription manifest is uploaded to your Satellite with sufficient Red Hat Enterprise Linux entitlements allocated for the conversions you intend. Alternatively, you can use Ansible variables to tell the role to import the manifest from disk. The manifest must be imported to the organization to which you will register hosts for conversion.

  You can update your allocations and download the updated manifest from the [Red Hat Customer Portal](https://access.redhat.com). For more information, see [Exporting and downloading a manifest](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/creating_and_managing_manifests_for_a_connected_satellite_server/index#proc-exporting-downloading-manifest-satellite-connected) in *Creating and managing manifests for a connected Satellite Server*.
- Red Hat repositories are enabled and synchronized in Satellite for the minor Red Hat Enterprise Linux version to which you convert your hosts. For more information, see [Enabling Red Hat repositories by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-web-ui) and [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.

**Procedure**

1. Import the `redhat.satellite.convert2rhel` Ansible role and variables. For more information, see [Importing Ansible Roles and Variables](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#Importing_Ansible_Roles_and_Variables_ansible) in *Managing configurations by using Ansible integration*.
2. Configure Ansible variables for generation of conversion data. For more information, see [Section 12.3, “Ansible variables for conversion”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#ansible-variables-for-conversion_managing-hosts "12.3. Ansible variables for conversion").
3. Assign the `redhat.satellite.convert2rhel` role to the host that represents Satellite Server. For more information, see [Assigning Ansible Roles to an Existing Host](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#Assigning_Ansible_Roles_to_an_Existing_Host_ansible) in *Managing configurations by using Ansible integration*.
4. Run the Ansible role on Satellite Server. For more information, see [Running Ansible roles on a host](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#running-ansible-roles-on-a-host) in *Managing configurations by using Ansible integration*.

   The Ansible role generates data required for host conversion, that is, repositories, certificates, activation keys, and host groups. The role enables the `rhel-7-server-rpms` repository with the **7Server** release and **x86_64** architecture, or `rhel-8-for-x86_64-baseos-rpms` and `rhel-8-for-x86_64-appstream-rpms`, or both, depending on which variables you have set in the previous steps.
5. Register a host for conversion by using a generated host group.

   Use the global registration template to register and subscribe your host before the conversion. Select the host group that was generated for the conversion you intend, such as `CentOS 7 converting` if you convert the host from CentOS 7. For more information, see [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration").
6. Run the pre-conversion analysis on the host group to verify if your hosts are ready for the conversion. Execute a remote job with the following settings:

   - **Job category**: `Convert 2 RHEL`
   - **Job template**: `Convert2RHEL analyze`
   - If you want to use an Extended Lifecycle Support add-on subscription, set the **ELS** option to `yes`.

     For more information, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").

   Review pre-conversion analysis reports and resolve all issues that are blocking the conversion. Repeat this step until you resolve all blocking issues. For more information, see [Reviewing the pre-conversion analysis report](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html-single/converting_from_a_linux_distribution_to_rhel_using_the_convert2rhel_utility/index#reviewing-the-pre-conversion-analysis-report_converting-using-the-command-line) in *Red Hat Enterprise Linux 8 Converting from a Linux distribution to RHEL using the Convert2RHEL utility*.
7. Run the Convert2RHEL playbook on the host group. Execute a remote job with the following settings:

   - **Job category**: `Convert 2 RHEL`
   - **Job template**: `Convert to RHEL`
   - **Activation key**:

     - `convert2rhel_rhel7` if you convert to Red Hat Enterprise Linux 7
     - `convert2rhel_rhel8` if you convert to Red Hat Enterprise Linux 8
   - If you want to use an Extended Lifecycle Support add-on subscription, set the **ELS** option to `yes`.

   For more information, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").

**Additional resources**

- [How to perform an unsupported conversion from a RHEL-derived Linux distribution to RHEL in the *Red Hat Knowledgebase*](https://access.redhat.com/articles/2360841)

## 12.3. Ansible variables for conversion

Configure the required Ansible variables for the Convert2RHEL role before you run it to generate conversion data on Satellite Server. This reference lists the variables and their intended values.

Satellite imports most of the required Ansible variables from the `redhat.satellite.convert2rhel` role. However, some variables are not imported. These variables are marked with an asterisk `*` in the tables below. You must create those additional variables manually and assign them to the `redhat.satellite.convert2rhel` role.

Table 12.1. Required variables for conversion

| Name | Type | Intent and value |
| --- | --- | --- |
| `satellite_server_url` * | string | URL of your Satellite Server, such as `https://satellite.example.com` |
| `satellite_username` * | string | Your user name |
| `satellite_password` * | string | Your password |
| `satellite_organization` * | string | Name of your organization |
| `satellite_content_rhel_wait_for_syncs` * | boolean | Set to `false` if you do not want Satellite Server to wait until repository sync finishes before continuing with data generation. (default: `true`) |
| `satellite_validate_certs` * | boolean | Set to `true` if you want to enable certificate checks in Ansible. (default: `true`) |
| `satellite_convert2rhel_manage_subscription` | boolean | Set to `false` if you already have a manifest on your Satellite Server. If you upload a new manifest from disk, the current manifest will be overwritten. (default: `true`) |
| `satellite_content_rhel_enable_rhel7` * | boolean | Enables Red Hat Enterprise Linux 7 repositories. Set to `false` if you do not intend to convert hosts to Red Hat Enterprise Linux 7. (default: `true`) |
| `satellite_convert2rhel_enable_oracle7` | boolean | Set to `true` if you want to prepare conversion data for Oracle Linux 7. Otherwise, you must set the value to `false`. |
| `satellite_content_rhel_enable_rhel8` * | boolean | Enables Red Hat Enterprise Linux 8 repositories. Set to `false` if you do not intend to convert hosts to Red Hat Enterprise Linux 8. (default: `true`) |
| `satellite_convert2rhel_enable_oracle8` | boolean | Set to `true` if you want to prepare conversion data for Oracle Linux 8. Otherwise, you must set the value to `false`. |

Table 12.2. Optional variables for conversion

| Name | Type | Intent and value |
| --- | --- | --- |
| `satellite_manifest_path` * | string | Path to a manifest to upload from disk, such as `~/manifest.zip`. You must set this path if you upload a new manifest from disk using `satellite_convert2rhel_manage_subscription`. |
| `satellite_content_rhel_rhel8_releasever` * | string | Minor release version, such as `8.5`. Set this variable if the minor release version of your system differs from the latest Red Hat Enterprise Linux release to prevent conversion issues. (default: latest) |
