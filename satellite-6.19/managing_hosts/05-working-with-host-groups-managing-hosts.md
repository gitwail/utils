---
title: "Working with host groups"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Working_with_Host_Groups_managing-hosts"
---
# Chapter 5. Working with host groups

To reduce repeated configuration when you manage many similar hosts, you can use host groups in Satellite as templates for shared host settings and apply them to many similar hosts. You can also nest host groups so child groups inherit from a parent and add specifics only where needed.

## 5.1. Host groups overview

You can use host groups in Satellite as templates for common host settings. Define the settings once and apply them to multiple hosts instead of configuring each host individually.

With host groups, you can define many settings for hosts, such as lifecycle environment, content view, or Ansible roles that are available to the hosts. Instead of defining the settings individually for each host, you can use host groups to define common settings once and apply them to multiple hosts.

You can create nested host groups.

> **Important**
>
> When you change the settings of an existing host group, the new settings do not propagate to the hosts assigned to the host group. Only Puppet class settings get updated on hosts after you change them in the host group.

## 5.2. Nested host groups

You can create a hierarchy of host groups so that child host groups inherit and override settings from parent host groups.

Aim to have one base level host group that represents all hosts in your organization and provides general settings, and then nested groups that provide specific settings.

Satellite applies host settings in the following order when nesting host groups:

- Host settings take priority over host group settings.
- Nested host group settings take priority over parent host group settings.

**Example 5.1. Nested host group hierarchy**

You create a top-level host group named **Base** and two nested host groups named **Webserver** and **Storage**. The nested host groups are associated with multiple hosts. You also create host `custom.example.com` that is not associated with any host group.

You define the operating system on the top-level host group (**Base**) and Ansible roles on the nested host groups (**Webservers** and **Storage**).

| Top-level host group | Nested host group | Hosts | Settings inherited from host groups |
| --- | --- | --- | --- |
| **Base**    This host group applies the `Red Hat Enterprise Linux 9.5` operating system setting. | **Webservers**    This host group applies the `linux-system-roles.selinux` Ansible role. | **webserver1.example.com** | Hosts use the following settings:   - `Red Hat Enterprise Linux 9.5` defined by host group **Base** - `linux-system-roles.selinux` defined by host group **Webservers** |
| **webserver2.example.com** |
| **Storage**    This host group applies the `linux-system-roles.postfix` Ansible role. | **storage1.example.com** | Hosts use the following settings:   - `Red Hat Enterprise Linux 9.5` defined by host group **Base** - `linux-system-roles.postfix` defined by host group **Storage** |
| **storage2.example.com** |
| [No host group] | | **custom.example.com** | No settings inherited from host groups. |

**Example 5.2. Nested host group settings**

You create a top-level host group named **Base** and two nested host groups named **Webserver** and **Storage**. You also create host `custom.example.com` that is associated with the top-level host group **Base**, but no nested host group.

You define different values for the operating system and Ansible role settings on the top-level host group (**Base**) and nested host groups (**Webserver** and **Storage**).

| Top-level host group | Nested host group | Host | Settings inherited from host groups |
| --- | --- | --- | --- |
| **Base**    This host group applies these settings:   - The `Red Hat Enterprise Linux 9.5` operating system - The `linux-system-roles.selinux` Ansible role | **Webservers**    This host group applies these settings:   - The `Red Hat Enterprise Linux 9.6` operating system - No Ansible role | **webserver1.example.com** | Hosts use the following settings:   - The `Red Hat Enterprise Linux 9.6` operating system from host group **Webservers** - The `linux-system-roles.selinux` Ansible role from host group **Base** |
| **webserver2.example.com** |
| **Storage**    This host group applies these settings:   - No operating system - The `linux-system-roles.postfix` Ansible role | **storage1.example.com** | Hosts use the following settings:   - The `Red Hat Enterprise Linux 9.5` operating system from host group **Base** - The `linux-system-roles.postfix` Ansible role from host group **Storage** |
| **storage2.example.com** |
| [No nested host group] | **custom.example.com** | Host uses the following settings:   - The `Red Hat Enterprise Linux 9.5` operating system from host group **Base** - The `linux-system-roles.selinux` Ansible role from host group **Base** |

## 5.3. Creating a host group by using Satellite web UI

You can create a host group from the Satellite web UI to use as a template for common host settings.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. Click **Create Host Group**.
3. If you have an existing host group that you want to inherit attributes from, you can select a host group from the **Parent** list. If you do not, leave this field blank.
4. Enter a **Name** for the new host group.
5. Enter any further information that you want future hosts to inherit.
6. Click the **Ansible Roles** tab, and from the **Ansible Roles** list, select one or more roles that you want to add to the host. Use the **arrow** icon to manage the roles that you add or remove.
7. Click the additional tabs and add any details that you want to attribute to the host group.

   > **Note**
   >
   > Puppet fails to retrieve the Puppet CA certificate while registering a host with a host group associated with a Puppet environment created inside a `Production` environment.
   >
   > To create a suitable Puppet environment to be associated with a host group, manually create a directory:
   >
   > ```
   > # mkdir /etc/puppetlabs/code/environments/example_environment
   > ```
8. Click **Submit** to save the host group.

## 5.4. Creating a host group by using Hammer CLI

You can create a host group by using Hammer CLI to use as a template for common host settings.

**Procedure**

- Create a host group:

  ```
  $ hammer hostgroup create \
  --architecture "My_Architecture" \
  --content-source-id My_Content_Source_ID \
  --content-view "My_Content_View" \
  --domain "My_Domain" \
  --lifecycle-environment "My_Lifecycle_Environment" \
  --locations "My_Location" \
  --medium-id My_Installation_Medium_ID \
  --name "My_Host_Group" \
  --operatingsystem "My_Operating_System" \
  --organizations "My_Organization" \
  --partition-table "My_Partition_Table" \
  --puppet-ca-proxy-id My_Puppet_CA_Proxy_ID \
  --puppet-environment "My_Puppet_Environment" \
  --puppet-proxy-id My_Puppet_Proxy_ID \
  --root-pass "My_Password" \
  --subnet "My_Subnet"
  ```

## 5.5. Creating a host group for each lifecycle environment

You can create a host group for the Library lifecycle environment and nested host groups for other lifecycle environments. This organizes hosts by lifecycle stage, for example Development, Testing, and Production.

**Procedure**

- To create a host group for each lifecycle environment, run the following Bash script:

  ```shell-session
  MAJOR="My_Major_Operating_System_Version"
  ARCH="My_Architecture"
  ORG="My_Organization"
  LOCATIONS="My_Location"
  PTABLE_NAME="My_Partition_Table"
  DOMAIN="My_Domain"

  hammer --output csv --no-headers lifecycle-environment list --organization "${ORG}" | cut -d ',' -f 2 | while read LC_ENV; do
    [[ ${LC_ENV} == "Library" ]] && continue

    hammer hostgroup create --name "rhel-${MAJOR}server-${ARCH}-${LC_ENV}" \
      --architecture "${ARCH}" \
      --partition-table "${PTABLE_NAME}" \
      --domain "${DOMAIN}" \
      --organizations "${ORG}" \
      --query-organization "${ORG}" \
      --locations "${LOCATIONS}" \
      --lifecycle-environment "${LC_ENV}"
  done
  ```

## 5.6. Adding a host to a host group

You can add a host to a host group from the Satellite web UI so that the host inherits the settings of the host group.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host you want to modify.
3. Click **Edit**.
4. Select the host group from the **Host Group** list.
5. Click **Submit**.

**Verification**

- The **Details** card under the **Overview** tab now shows the host group your host belongs to.

## 5.7. Changing the host group of a host

You can change the host group of a host so that the host inherits settings from the new host group.

> **Note**
>
> If you reprovision the host, the fresh values that the host group inherits from the new host group are applied.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host you want to modify.
3. Click **Edit**.
4. Select the new host group from the **Host Group** list.
5. Click **Submit**.

**Verification**

- The **Details** card under the **Overview** tab now shows the host group your host belongs to.
