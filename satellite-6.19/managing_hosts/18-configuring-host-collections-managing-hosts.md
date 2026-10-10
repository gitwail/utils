---
title: "Configuring host collections"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "18"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Configuring_Host_Collections_managing-hosts"
---
# Chapter 18. Configuring host collections

To group hosts and perform the same action on them at once, you can use host collections. Available actions include managing packages, applying errata, or assigning content view environments. Group hosts in a way that suits your workflow, such as by function, department, or business unit.

You can assign host collections to activation keys to ensure that newly provisioned or registered hosts become automatically part of your host collection during the registration to Satellite.

## 18.1. Creating a host collection by using Satellite web UI

You can create a host collection from the Satellite web UI to group hosts and perform bulk actions such as package updates or errata installation.

**Prerequisites**

- Your user account has a role that grants the `create_host_collections` permission.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Host Collections**.
2. Click **New Host Collection**.
3. Add the **Name** of the host collection.
4. Clear **Unlimited Hosts**, and enter the desired maximum number of hosts in the **Limit** field.
5. Add the **Description** of the host collection.
6. Click **Save**.

## 18.2. Creating a host collection by using Hammer CLI

You can create a host collection by using Hammer CLI to group hosts and perform bulk actions such as package updates or errata installation.

**Procedure**

- Create a host collection:

  ```
  $ hammer host-collection create \
  --name "My_Host_Collection" \
  --organization "My_Organization"
  ```

## 18.3. Cloning a host collection

You can clone a host collection to create a new collection with the same settings and membership, then adjust it as needed.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Host Collections**.
2. On the left hand panel, click the host collection you want to clone.
3. Click **Copy Collection**.
4. Specify a name for the cloned collection.
5. Click **Create**.

## 18.4. Removing a host collection

You can remove a host collection from Satellite when you no longer need that grouping. The hosts in the collection are not deleted.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Host Collections**.
2. Select the host collection that you want to remove.
3. Under **Select Action**, click **Remove**.
4. Click **Delete** to remove the host collection.

## 18.5. Adding a host to a host collection by using Satellite web UI

You can add a host to a host collection from the Satellite web UI.

Note that if you add a host to a host collection, the Satellite auditing system does not log the change.

**Prerequisites**

- A host must be registered to Red Hat Satellite to add it to a Host Collection. For more information about registering hosts, see [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host you want to modify.
3. In the **Host collections** card, open the options menu and select **Add host to collections**.
4. Select the host collection.
5. Click **Add**.

## 18.6. Adding a host to a host collection by using Hammer CLI

You can add a host to a host collection by using Hammer CLI.

Note that if you add a host to a host collection, the Satellite auditing system does not log the change.

**Prerequisites**

- A host must be registered to Red Hat Satellite to add it to a Host Collection. For more information about registering hosts, see [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration").

**Procedure**

- Add a host to your host collection:

  ```
  $ hammer host-collection add-host \
  --host-ids My_Host_ID \
  --id My_Host_Collection_ID
  ```

## 18.7. Adding hosts to a host collection in bulk by using Satellite web UI

You can add multiple hosts to a host collection at once from the Satellite web UI.

Note that if you add a host to a host collection, the Satellite auditing system does not log the change.

**Prerequisites**

- A host must be registered to Red Hat Satellite to add it to a host collection. For more information about registering hosts, see [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Host Collections**.
2. Select the host collection where the host should be added.
3. On the **Hosts** tab, select the **Add** subtab.
4. Select the hosts to be added from the table and click **Add Selected**.

## 18.8. Adding hosts to a host collection in bulk by using Hammer CLI

You can add multiple hosts to a host collection at once by using Hammer CLI.

Note that if you add a host to a host collection, the Satellite auditing system does not log the change.

**Prerequisites**

- A host must be registered to Red Hat Satellite to add it to a host collection. For more information about registering hosts, see [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration").

**Procedure**

- Add multiple hosts to a host collection:

  ```
  $ hammer host-collection add-host \
  --host-ids My_Host_ID_1,My_Host_ID_2 \
  --id My_Host_Collection_ID
  ```

## 18.9. Removing a host from a host collection

Remove hosts from a host collection to update membership without deleting the host from Satellite.

Note that if you remove a host from a host collection, the host collection record in the database is not modified so the Satellite auditing system does not log the change.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Host Collections**.
2. Choose the desired host collection.
3. On the **Hosts** tab, select the **List/Remove** subtab.
4. Select the hosts you want to remove from the host collection and click **Remove Selected**.

## 18.10. Managing host content with host collections

You can use host collections in Satellite to install packages, apply errata, or manage other content across all hosts in the collection.

### 18.10.1. Installing packages on hosts in a host collection

You can install packages on all hosts in a host collection in one action.

**Prerequisites**

- The packages or package groups you want to install should be available in one of the existing repositories or added before this procedure.
- Content should be promoted to the environment where the hosts are assigned.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Host Collections**.
2. Select the host collection on which you want to install the package.
3. On the **Collection Actions** tab, click **Package Installation, Removal, and Update**.
4. To update all packages, click **Update All Packages** to use the default method. Alternatively, select the drop-down icon to the right of the button to select a method to use. Selecting the **via remote execution – customize first** menu entry will take you to the **Job invocation** page where you can customize the action.
5. Select the **Package** or **Package Group** radio button as required.
6. In the field provided, specify the package or package group name. Then click:

   - **Install** – to install a new package using the default method. Alternatively, select the drop-down icon to the right of the button and select a method to use. Selecting the **via remote execution – customize first** menu entry will take you to the **Job invocation** page where you can customize the action.
   - **Update** – to update an existing package in the host collection using the default method. Alternatively, select the drop-down icon to the right of the button and select a method to use. Selecting the **via remote execution – customize first** menu entry will take you to the **Job invocation** page where you can customize the action.

### 18.10.2. Viewing installed packages

You can view the installed packages on a host to see what is present or to plan package or errata actions.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the name of the host.
3. On the **Content** tab, **Packages** displays a list of installed packages.
4. To see details of a package, select that package.

   - The **Details** tab displays details of the selected package.
   - The **Files** tab lists the files contained in the package.
   - The **Dependencies** tab lists the dependencies of the package.
   - The **Repositories** tab lists the repositories that contain the selected package.
5. You can filter these by **Library** or **Default organization**.

### 18.10.3. Upgrading a package

You can upgrade an installed package on a host to a newer version from the Satellite web UI to get bug fixes or new features.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts** and select the name of the host that contains the package you want to upgrade.
2. On the **Content** tab, select **Packages**.

   The **Status** column displays whether the package is upgradeable or Up-to date. You cannot update an up-to-date package.
3. From the list of packages, choose the package you want to upgrade and click the options icon at the end of the line.
4. Choose the **Apply via Remote Execution** to use Remote Execution, or **Apply via customized remote execution** if you want to customize the remote execution, for example, to set a time when it should be applied.
5. Click **Submit** to upgrade the package.

### 18.10.4. Removing a package from a host

To uninstall software or resolve dependency issues, you can remove a package from a host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the host containing the package you want to remove.
3. On the **Content** tab, select **Packages**.
4. Click the options icon at the end of the line for the package you want to remove, and click **Remove**.
5. Click **Submit**.

### 18.10.5. Installing errata on hosts in a host collection

You can install errata on all hosts in a host collection in one action using remote execution.

**Prerequisites**

- Requirements for errata installation on hosts are met. For more information, see [Section 23.1, “Prerequisites for installing errata on hosts”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#prerequisites-for-installing-errata-on-hosts "23.1. Prerequisites for installing errata on hosts").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Host Collections**.
2. Select the host collection where the errata should be installed.
3. On the **Collection Actions** tab, click **Errata Installation**.
4. Select the errata you want to install on the hosts in the collection and click **Install Selected** to use the default method. Alternatively, select the drop-down icon to the right of the button to select a method to use. Selecting the **via remote execution – customize first** menu entry takes you to the **Job invocation** page where you can customize the action.

**Additional resources**

- [Chapter 23, *Patching hosts through errata*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#patching-hosts-through-errata "Chapter 23. Patching hosts through errata")

### 18.10.6. Removing content from hosts in a host collection

Remove packages or package groups from hosts in a host collection to keep collection content in sync with your requirements.

**Procedure**

1. Click **Hosts** > **Host Collections**.
2. Click the host collection where the package should be removed.
3. On the **Collection Actions** tab, click **Package Installation, Removal, and Update**.
4. Select the **Package** or **Package Group** radio button as required.
5. In the field provided, specify the package or package group name.
6. Click **Remove** to remove the package or package group using the default method. Alternatively, select the drop-down icon to the right of the button and select a method to use. Selecting the **via remote execution - customize first** menu entry will take you to the **Job invocation** page where you can customize the action.

### 18.10.7. Changing the lifecycle environment or content view of a host collection

You can change the lifecycle environment or content view assigned to a host collection so that all hosts in the host collection consume content from the new lifecycle environment or content view.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Host Collection**.
2. Selection the host collection where the lifecycle environment or content view should be changed.
3. On the **Collection Actions** tab, click **Change assigned Lifecycle Environment or Content View**.
4. Select the lifecycle environment to be assigned to the host collection.
5. Select the required content view from the list.
6. Click **Assign**.

   > **Note**
   >
   > The changes take effect in approximately 4 hours. To make the changes take effect immediately, on the host, enter the following command:
   >
   > ```
   > # subscription-manager refresh
   > ```
   >
   > You can use remote execution to run this command on multiple hosts at the same time.
