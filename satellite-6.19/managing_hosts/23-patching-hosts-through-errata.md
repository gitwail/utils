---
title: "Patching hosts through errata"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "23"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#patching-hosts-through-errata"
---
# Chapter 23. Patching hosts through errata

Hosts receive security and bugfix updates through errata. Review applicable and installable errata, generate status reports, install updates, and run custom code before or after installation.

**Additional resources**

- [Making errata available through content views in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#making-errata-available-through-content-views)
- [Section 18.10.5, “Installing errata on hosts in a host collection”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#installing-errata-on-hosts-in-a-host-collection "18.10.5. Installing errata on hosts in a host collection")

## 23.1. Prerequisites for installing errata on hosts

Installing errata on hosts requires synchronized repositories, installable errata in the content view environments, registered hosts, and remote execution configuration.

- Repositories on Satellite Server are synchronized with the latest errata available from Red Hat.
- The host is registered to one or more content view environments.
- The host is configured for remote execution.
- Errata are **installable**.

  Applicable errata have updates for packages on hosts, but you can only install errata included in the content view environments of the host. If errata are applicable but not installable, the content view must be incrementally updated and promoted to the lifecycle environment of the host.

**Additional resources**

- [Synchronizing repositories ad hoc in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc)
- [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration")
- [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs")
- [Making errata available through content views in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#making-errata-available-through-content-views)

## 23.2. Viewing errata by applicable and installable

You can view errata by applicable or installable status to see which updates affect your hosts and which are ready to install.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the host name.
3. Click the **Overview** tab. Under the Errata card, there are two types of Errata.
4. Click **Applicable** to view errata that apply to a package installed on your host.
5. Click **Installable** to view applicable errata that are available in the content view environments of the host.
6. Click the link with number of errata under each type to see the list of all available errata of that type.
7. Click **security advisories**, **bug fixes**, or **enhancements** under each type to view only the respective type of errata.

## 23.3. Generating a report for installable and applicable errata

You can generate a report of installable or applicable errata on hosts to review update status across your environment before installing errata on hosts.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Reports** > **Report Templates**.
2. Click **Generate** for the **Host – Applicable Errata** template.
3. Optional: To schedule a report, click the **calendar** icon to the right of the **Generate at** field and choose the date and time you want for the generated report.
4. Optional: To send a report to an e-mail address, select the **Send report via e-mail** checkbox, and in the **Deliver to e-mail addresses** field, enter the required e-mail address.
5. Optional: Select another **Output format** for the report file. The default is CSV.
6. Optional: To limit the report only to hosts found by the search query, click on **Hosts filter** and search from the available list of hosts. For a report on all available hosts, leave **Hosts filter** empty.
7. Optional: To limit the report only to errata found by the search query, click on **Errata filter** and search from the available list of errata. For a report on all available errata, leave **Errata filter** empty.
8. From the **Installability** list, select one of these options:

   - **Applicable** to show all applicable errata.
   - **Installable** to limit the report exclusively to errata that are accessible in the content view environments of your host that may be installed.
9. Click **Generate**. Your browser automatically downloads the report file after Satellite creates it. If you have selected the **Send report via e-mail** option, the report is sent to your e-mail address.

## 23.4. Filter errata by type and severity

You can filter errata by type or severity to focus on security updates, bug fixes, or enhancements when planning or applying errata.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select your host.
3. On the **Contents** tab, **Errata** lists the errata associated with the selected host.
4. Click **Type** to filter errata by type.
5. You can filter to display errata of type Security, Bugfix, or Enhancement
6. Click **Severity** to filter by severity.
7. You can filter to display errata of severity N/A, Low, Moderate, Important, or Critical.
8. To deselect your choice, return to the list of options and click the selected option again.

   You can also use the **Errata** card on the host page to pre-filter errata for type before display.

## 23.5. Installing errata on hosts by using Satellite web UI

You can use the Satellite web UI to review and install installable errata on hosts so that security and bugfix updates are installed on selected hosts.

**Prerequisites**

- Requirements for errata installation on hosts are met. For more information, see [Section 23.1, “Prerequisites for installing errata on hosts”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#prerequisites-for-installing-errata-on-hosts "23.1. Prerequisites for installing errata on hosts").

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Content Types** > **Errata**.
2. Click the name of an erratum you want to install.
3. On the to **Content Hosts** tab, select all hosts that you want to install errata on.
4. Click **Apply to Hosts** and click **Confirm**.

**Verification**

1. In the Satellite web UI, navigate to **Monitor** > **Jobs**.
2. Select the most recent `Install errata` job.
3. Verify that the remote execution to install errata on all selected hosts succeeded.

## 23.6. Installing errata on hosts by using CLI

You can use Hammer CLI to review and install installable errata on hosts so that security and bugfix updates are installed on selected hosts.

**Prerequisites**

- Requirements for errata installation on hosts are met. For more information, see [Section 23.1, “Prerequisites for installing errata on hosts”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#prerequisites-for-installing-errata-on-hosts "23.1. Prerequisites for installing errata on hosts").

**Procedure**

1. List all errata:

   ```
   $ hammer erratum list --organization "My_Organization"
   ```

   You can limit the output to applicable by adding `--errata-restrict-applicable` or to installable errata by adding `--errata-restrict-installable`.
2. Optional: View information of an erratum:

   ```
   $ hammer erratum info --id My_Erratum_ID
   ```
3. Install errata on your hosts.

   You can use `Remote Execution`:

   ```
   $ hammer job-invocation create \
   --feature katello_errata_install \
   --inputs errata=My_Erratum_ID_1,My_Erratum_ID_2 \
   --search-query "name = host.example.com"
   ```

   If you want to install errata on all hosts in a host collection, use `"host_collection = My_Host_Collection_Name"` as the search query. If you want to install a specific erratum on all hosts, use `"applicable_errata = My_Erratum_ID"` as the search query.

   You can use a Bash script that installs an erratum on each host for which this erratum is available:

   ```shell-session
   for HOST in hammer --csv --csv-separator "|" host list --search "applicable_errata = My_Erratum_ID" --organization "My_Organization" | tail -n+2 | awk -F "|" '{ print $2 }' ;
   do
     echo "== Installing on $HOST ==" ; hammer job-invocation create --feature katello_errata_install --search-query "name = $HOST" --inputs errata=My_Erratum_ID_1,My_Erratum_ID_2 ;
   done
   ```

   This command identifies all hosts with *My_Erratum_ID* as an applicable erratum and then installs the erratum on each host.

**Verification**

1. Locate the task ID of your errata installation in task listing:

   ```
   $ hammer task list
   ```
2. Inspect the state of the selected task:

   ```
   $ hammer task progress --id My_Task_ID
   ```

**Additional resources**

- [Working efficiently with Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui)

## 23.7. Installing errata on hosts by using MCP

You can use your AI application to install installable errata on hosts through natural language prompts that create remote execution jobs in Satellite.

> **Warning**
>
> Review the output generated by AI before using it in production.

> **Important**
>
> The MCP server for Satellite is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

- Requirements for errata installation on hosts are met. For more information, see [Section 23.1, “Prerequisites for installing errata on hosts”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#prerequisites-for-installing-errata-on-hosts "23.1. Prerequisites for installing errata on hosts").
- The MCP server for Satellite is deployed and configured to allow remote execution jobs for errata installation. For more information, see [Deploying the MCP server for Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#deploying-the-mcp-server-for-satellite) in *Managing hosts*.

**Procedure**

1. Allow the MCP server to trigger remote execution jobs for errata installation:

   ```
   $ podman run --interactive --tty --publish 127.0.0.1:8080:8080 \
     --volume Path_to_My_CA_Bundle:/app/ca.pem:ro,Z \
     registry.redhat.io/satellite/foreman-mcp-server-rhel9:6.18 \
     --foreman-url https://satellite.example.com \
     --allowed-rex-features katello_errata_install,katello_errata_install_by_search
   ```

   For more information, see [Deploying the MCP server for Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#deploying-the-mcp-server-for-satellite) in *Managing hosts*.
2. Type a prompt in your AI application to list any host with outstanding errata.

   ```
   Show a list of hosts that require patching on my Satellite.
   ```

   ```
   Categorize the list into hosts that require security patches and hosts that require bug fix patches.
   ```
3. The MCP server returns a list of hosts with installable errata to the AI application. Review the information.
4. The Satellite MCP server provides a prompt named `Apply Errata to Hosts`, which you can use to install errata on the hosts. Refer to the documentation of your AI application to find more about how to use MCP server prompts. Review all the steps that the AI application performs.

## 23.8. Running custom code while installing errata by using Satellite web UI

Create custom snippets to run code before or after errata installation when you need to prepare hosts or verify updates.

**Prerequisites**

- The job template that installs errata must conditionally include custom snippets ending in `custom pre` or `custom post`.

  You can view job templates in use under **Administer** > **Remote Execution Features**.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Job Templates**.
2. Click **Create Template**.
3. In the **Name** field, enter a name for your custom snippet. The name must start with the name of a template that supports custom snippets:

   - Append `custom pre` to the name of a template to run code before installing errata on hosts.
   - Append `custom post` to the name of a template to run code after installing errata on hosts.

   For example, if your template is called `Install Errata - Katello Ansible Default`, name your template `Install Errata - Katello Ansible Default custom pre` or `Install Errata - Katello Ansible Default custom post`.
4. On the **Type** tab, select **Snippet**.
5. Click **Submit** to create your custom snippet.

## 23.9. Running custom code while installing errata by using Hammer CLI

Create custom snippets that run code before or after errata installation when you need to prepare hosts or verify updates.

**Prerequisites**

- The job template that installs errata must conditionally include custom snippets ending in `custom pre` or `custom post`.

  You can view job templates in use under **Administer** > **Remote Execution Features**.

**Procedure**

1. Create a plain text file that contains your custom snippet.
2. Upload the snippet file to Satellite Server:

   ```
   $ hammer template create \
   --file "~/My_Snippet" \
   --locations "My_Location" \
   --name "My_Template_Name_custom_pre" \ --organizations "_My_Organization" \
   --type snippet
   ```

   The name must start with the name of a template that supports custom snippets:  **Append `custom pre` to the name of a template to run code before installing errata on hosts.**  Append `custom post` to the name of a template to run code after installing errata on hosts.

   For example, if your template is called `Install Errata - Katello Ansible Default`, name your snippet `Install Errata - Katello Ansible Default custom pre` or `Install Errata - Katello Ansible Default custom post`.
