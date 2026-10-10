---
title: "Managing host content settings and system purpose"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#managing-host-content-settings-and-system-purpose"
---
# Chapter 3. Managing host content settings and system purpose

You can set which content source and repositories a host uses and choose module streams for software versions. You can configure system purpose so subscription usage on the host reflects its role and usage.

## 3.1. Editing the system purpose of a host by using Satellite web UI

You can edit the system purpose attributes for your Red Hat Enterprise Linux host from the Satellite web UI. Setting system purpose defines the intended use of the system on your network and improves reporting accuracy in the Subscriptions service of the Red Hat Hybrid Cloud Console.

**Prerequisites**

- The host that you want to edit must be registered with the subscription-manager.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host you want to modify.
3. On the **Overview** tab, click **Edit** on the **System purpose** card.
4. Select the system purpose attributes for your host.
5. Click **Save**.

**Additional resources**

- [Configuring System Purpose using the subscription-manager command-line tool in *Automatically installing RHEL 8*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/automatically_installing_rhel/proc_configuring-system-purpose-using-the-subscription-manager-command-line-tool_rhel-installer)

## 3.2. Editing the system purpose of a host by using Hammer CLI

You can edit the system purpose attributes for your Red Hat Enterprise Linux host by using Hammer CLI. Setting system purpose defines the intended use of the system on your network and improves reporting accuracy in the Subscriptions service of the Red Hat Hybrid Cloud Console.

**Prerequisites**

- The host that you want to edit must be registered with the subscription-manager.

**Procedure**

1. Log in to the host and edit the required system purpose attributes. For example, set the usage type to `Production` and the role to `Red Hat Enterprise Linux Server`. For the list of values, see [Configuring System Purpose using the subscription-manager command-line tool](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/automatically_installing_rhel/proc_configuring-system-purpose-using-the-subscription-manager-command-line-tool_rhel-installer) in *Automatically installing RHEL 8*.

   ```
   # subscription-manager syspurpose set usage 'Production'
   # subscription-manager syspurpose set role 'Red Hat Enterprise Linux Server'
   ```
2. Verify the system purpose attributes for this host:

   ```
   # subscription-manager syspurpose
   ```

**Additional resources**

- [Configuring System Purpose using the subscription-manager command-line tool in *Automatically installing RHEL 8*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/automatically_installing_rhel/proc_configuring-system-purpose-using-the-subscription-manager-command-line-tool_rhel-installer)

## 3.3. Editing the system purpose of multiple hosts

You can edit the system purpose attributes of multiple Red Hat Enterprise Linux hosts at once from the Satellite web UI. Setting system purpose defines the intended use of the systems on your network and improves reporting accuracy in the Subscriptions service of the Red Hat Hybrid Cloud Console.

**Prerequisites**

- The hosts that you want to edit must be registered with the subscription-manager.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the Red Hat Enterprise Linux hosts that you want to edit.
3. Click the main menu icon and select **Manage content** > **System purpose**.
4. Select the system purpose attributes that you want to assign to the selected hosts. You can select one of the following values:

   - A specific attribute to set an all selected hosts.
   - **No Change** to keep the attribute set on the selected hosts.
   - **(unset)** to clear the attribute on the selected hosts.
5. Click **Save**.

**Additional resources**

- [Configuring System Purpose using the subscription-manager command-line tool in *Automatically installing RHEL 8*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/automatically_installing_rhel/proc_configuring-system-purpose-using-the-subscription-manager-command-line-tool_rhel-installer)

## 3.4. Changing a module stream for a host

If you have a host running Red Hat Enterprise Linux 8, you can modify the module stream for the repositories you install. You can enable, disable, install, update, and remove module streams from your host in the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host you want to modify.
3. Click the **Content** tab, then click the **Module streams** tab.
4. Open the options menu next to the module and select the action you want to perform. You get a REX job notification once the remote execution job is complete.

## 3.5. Enabling custom repositories on hosts

You can enable custom repositories on a host from the Satellite web UI. This allows the host to install packages or consume other content from repositories you have added to Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts** and select a host.
2. Select the **Content** tab, then select **Repository sets**.
3. From the dropdown, you can filter the **Repository type** column to **Custom**.
4. Select the desired number of repositories or click the **Select All** checkbox to select all repositories.
5. Open the options menu, and select **Override to Enabled**.

## 3.6. Changing the content source of a host

You can change the content source of a host so that the host consumes content from a different Capsule. This helps you balance load or point the host to a closer or preferred content source.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host you want to modify.
3. Open the options menu next to the **Edit** button and select **Change content source**.
4. From the **Content source** list, select your Capsule that you want to use to provide software to your host.
5. In the **Content view environments** area, select the lifecycle environment and content view you want to use. Click **Assign another content view environment** to assign another content view environment. Drag and drop the content view environments to change their order.

   > **Note**
   >
   > Some lifecycle environments can be unavailable for selection if they are not synced on the selected content source. For more information, see [Adding lifecycle environments to Capsule Servers](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-lifecycle-environments-by-using-web-ui) in *Managing content*.
6. Click **Save**.
7. You can complete the content source change by using remote execution or manually.

   To update configuration on host using remote execution, click **Run job invocation**. For more information about running remote execution jobs, see [Configuring and setting up remote jobs](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs) in *Managing hosts*.

   To update the content source manually, execute the autogenerated commands from **Change content source** on the host.
