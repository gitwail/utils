---
title: "Managing packages in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "20"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#managing-packages-in-satellite"
---
# Chapter 20. Managing packages in Satellite

You can use Satellite to install, upgrade, and remove packages and to enable or disable repositories on hosts. Package actions use remote execution so you can manage software on hosts from a central place.

## 20.1. Enabling and disabling repositories on hosts

You can enable or disable repositories on a host from the Satellite web UI to control which package sources the host can use. This affects which packages are available for installation or upgrade on the host.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**,
2. Select a host.
3. On the **Content** tab, click the **Repository sets** tab.
4. Open the options menu and select **Override to disabled** or **Override to enabled** to disable or enable repositories on hosts.

## 20.2. Viewing upgradeable packages by using Satellite web UI

You can use Satellite web UI to view upgradeable packages. This can help you identify and prioritize updating hosts.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select your host.
3. On the **Content** tab, select the **Packages** tab.
4. Select **Upgradable** from the **Status** list.

   By default, Satellite shows all installed packages.

**Next steps**

- You can use remote execution to upgrade packages on your host. For more information, see [Section 19.2.4, “Executing a remote job by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#executing-a-remote-job-by-using-web-ui "19.2.4. Executing a remote job by using Satellite web UI").

## 20.3. Viewing upgradeable packages by using Hammer CLI

You can use Hammer CLI to view upgradeable packages. This can help you identify and prioritize updating hosts.

**Procedure**

1. Optional: Get the ID of your host:

   ```
   $ hammer host list --fields Id,Name
   ```
2. Get a list of upgradeable packages of your host:

   ```
   $ hammer host package list --status upgradable --host-id My_Host_ID
   ```

**Next steps**

- You can use Hammer CLI to upgrade packages on your host:

  ```
  $ hammer job-invocation create --feature katello_package_update --search-query "id = My_Host_ID" --inputs "package=My_Package_Name"
  ```

  For more information, see [Using the Hammer CLI tool](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#).

## 20.4. Installing packages on a host

You can review and install packages on a host from the Satellite web UI so that the host has the software it needs. Available packages depend on the content view environments assigned to the host.

**Prerequisites**

- The host is assigned to one or more content view environments.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select a host.
3. On the **Content** tab, click the **Packages** tab.
4. From the options icon next to the upgrade button, click **Install packages**.
5. In the **Install packages** window, select the package or packages that you want to install on the host.
6. Click **Install**. The Satellite web UI shows a notification for the remote execution job.

## 20.5. Upgrading packages on a host

You can upgrade packages on a host in bulk from the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select a host.
3. On the **Content** tab, click the **Packages** tab.
4. Select **Upgradable** from the **Status** list.
5. In the **Upgradable to** column, select the package version that you want to upgrade to.
6. Select the packages you want to upgrade.
7. Click **Upgrade**. The Satellite web UI shows a notification for the remote execution job.

## 20.6. Removing packages from a host

You can remove packages from a host from the Satellite web UI to uninstall software or resolve dependency conflicts.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select a host.
3. On the **Content** tab, click the **Packages** tab.
4. Click the options icon for the package you want to remove.
5. Select **Remove**. The Satellite web UI shows a notification for the remote execution job.

## 20.7. Managing packages on a host by using API

You can install, upgrade, or remove packages on a host by using the Satellite API for automation, scripts, or integration with other tools.

The example below uses the `katello_package_install` action to install a package. You can also use package actions `katello_package_upgrade` to upgrade or `katello_package_remove` to remove packages.

**Procedure**

1. Specify the API request body in the JSON format. For example:

   ```
   {
     "job_invocation" : {
       "concurrency_control" : {
         "concurrency_level" : 100
       },
       "feature" : "katello_package_install",
       "inputs" : {
         "package" : "nano vim"
       },
       "scheduling" : {
         "start_at" : "2023-09-21T19:00:00+00:00",
         "start_before" : "2023-09-23T00:00:00+00:00"
       },
       "search_query" : "*",
       "ssh" : {
         "effective_user" : "My_Username",
         "effective_user_password" : "My_Password"
       },
       "targeting_type" : "dynamic_query"
     }
   }
   ```

   The example uses the following notable values:

   "job_invocation"
   :   Specifies the object which contains the API request.

   "concurrency_level"
   :   Optional. Limits the number of hosts on which the job is run concurrently.

   "feature"
   :   Specifies the action to be performed. Use `"katello_package_install"` to install a package, `"katello_package_upgrade"` to upgrade a package, or `"katello_package_remove"` to remove a package.

   "package"
   :   Specifies the packages on which the action is performed. Separate multiple packages with a whitespace.

   "scheduling"
   :   Optional. Specifies time boundaries for when to start the package action.

       - You can specify one or both boundaries in the ISO 8601 format.
       - The action is canceled if it is not possible to perform the package action by this time.
       - If you omit time, it defaults to 00:00:00.
       - If you omit time zone, it defaults to UTC.

   "search_query"
   :   Specifies the search query that selects the hosts on which you want to perform the package action.

   "ssh"
   :   Optional. Specifies the credentials of an SSH user, if you want to perform the package action as that user.

   "dynamic_query"
   :   Optional. If you supplied the `"scheduling"` object, you can make the search query be evaluated when the job runs by specifying the `"targeting_type/dynamic_query"` field.

       - This is useful if you expect the query to produce a different result at the time of the job run.
       - If you omit this field, it defaults to `"static_query"`.
2. Send a `POST` request with the created body to the `/api/job_invocations` endpoint of your Satellite Server and see a formatted response. For example:

   ```
   $ curl https://satellite.example.com/api/job_invocations \
   -H "content-type: application/json" \
   -X POST \
   -d @Path_To_My_API_Request_Body \
   -u My_Username:My_Password \
   | python3 -m json.tool
   ```

**Verification**

- In the Satellite web UI, navigate to **Monitor** > **Jobs** and see the report of the scheduled or completed remote execution job to perform the package action on the selected hosts.

## 20.8. Best practices for host patching

Follow these guidelines when you patch hosts in Satellite so errata reporting stays accurate, updates go through supported tools, and bulk patching actions run reliably.

- Registering hosts to Satellite requires Red Hat Satellite Client 6, which contains the `katello-host-tools` package and its dependencies. For more information, see [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration").
- Use the Satellite web UI to install, upgrade, and remove packages from hosts. You can update hosts with job templates using SSH and Ansible.
- Apply errata on hosts using the Satellite web UI. When patching packages on hosts using the default package manager, Satellite receives a list of packages and repositories to recalculate applicable errata and available updates.
- Modify or replace job templates to add custom steps. This allows you to run commands or execute scripts on hosts.
- When running bulk actions on hosts, bundle them by major operating system version, especially when upgrading packages.
- Select **via remote execution – customize first** to define the time when patches are applied to hosts when performing bulk actions.
- You cannot apply errata to packages that are not part of the repositories on Satellite and the assigned content view environments.
- Modifications to installed packages using `rpm` or `dpkg` are sent to Satellite with the next run of `apt`, `yum`, or `zypper`.
