---
title: "Making errata available through content views"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "13"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#making-errata-available-through-content-views"
---
# Chapter 13. Making errata available through content views

Use content views to manage how errata reach your hosts. Inspect synchronized advisories, filter what is published, and create incremental updates when errata are applicable but not yet installable.

There are three types of advisories, listed in order of importance:

Security Advisory
:   Describes fixed security issues found in the package. The severity of the issue can be Low, Moderate, Important, or Critical.

Bug Fix Advisory
:   Describes bug fixes for the package.

Product Enhancement Advisory
:   Describes enhancements and new features added to the package.

Errata are labeled according to the most important advisory type they contain. Therefore, errata labeled as **Product Enhancement Advisory** can contain only enhancement updates, while **Bug Fix Advisory** errata can contain both bug fixes and enhancements, and **Security Advisory** can contain all three types.

As a part of quality control and release process, Red Hat provides customers with updates for each release of official Red Hat RPMs. Red Hat compiles groups of related packages into an erratum along with an advisory that provides a description of the update.

Red Hat Satellite imports this errata information when synchronizing repositories from the Red Hat Content Delivery Network (CDN).

In Red Hat Satellite, there are two keywords that describe the relationship of an erratum to hosts:

Applicable
:   An erratum that applies to one or more hosts, which means it has updates for packages present on the host. Although these errata apply to hosts, until their state changes to **Installable**, the errata are not ready to be installed. Publish incremental content views to make applicable errata installable. Installable errata are always applicable.

Installable
:   An erratum that applies to one or more hosts and is ready to be installed on the host. Installable errata are available to a host from its associated content view environments, but are not yet installed.

**Additional resources**

- [Explaining Red Hat errata](https://access.redhat.com/articles/explaining_redhat_errata)
- [Patching hosts through errata in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#patching-hosts-through-errata)

## 13.1. Best practices for errata

Apply these recommendations when managing errata so you patch security issues in a frozen set of content without unnecessarily updating unaffected packages.

- Use errata to add patches for security issues to a frozen set of content without unnecessarily updating other unaffected packages.
- Automate errata management by using a Hammer script or an [Ansible Playbook](https://theforeman.github.io/foreman-ansible-modules/develop/index.html).
- Check the host details page to compare errata between the current content view environments and the Library content view environment, which contains the latest synchronized packages.

  You can only apply errata included in the content view version of the lifecycle of your host. You can view applicable errata as a recommendation to create an incremental content view to provide errata to hosts. For more information, see [Section 13.7, “Adding errata to an incremental content view by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-errata-to-an-incremental-content-view-by-using-web-ui "13.7. Adding errata to an incremental content view by using Satellite web UI").

## 13.2. Errata email notifications

Configure email notifications in Satellite to receive summaries of applicable and installable errata, alerts after repository synchronization, and updates when content views are promoted.

**Additional resources**

- [Configuring email notification preferences in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Configuring_Email_Notification_Preferences_admin)

## 13.3. Inspecting available errata by using Satellite web UI

View and filter available errata to find applicable or installable updates and review advisory metadata before promoting content or patching hosts.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Content Types** > **Errata** to view the list of available errata.
2. Use the filtering tools at the top of the page to limit the number of displayed errata:

   - Select the repository to be inspected from the list. **All Repositories** is selected by default.
   - The **Applicable** checkbox is selected by default to view only applicable errata in the selected repository. Select the **Installable** checkbox to view only errata marked as installable.
   - To search the table of errata, type the query in the **Search** field in the form of:

     ```
     parameter operator value
     ```

     Automatic suggestion works as you type. You can also combine queries with the use of **and** and **or** operators. For example, to display only security advisories related to the **kernel** package, type:

     ```
     type = security and package_name = kernel
     ```

     Press **Enter** to start the search.
3. Click the **Errata ID** of the erratum you want to inspect:

   - The **Details** tab contains the description of the updated package as well as documentation of important fixes and enhancements provided by the update.
   - On the **Content Hosts** tab, you can install installable errata on selected hosts.
   - The **Repositories** tab lists repositories that already contain the erratum. You can filter repositories by the environment and content view, and search for them by the repository name.

**Additional resources**

- [Section 13.11, “Parameters available for errata search”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Parameters_Available_for_Errata_Search_content-management "13.11. Parameters available for errata search")
- [Supported operators for granular search in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Supported_Operators_for_Granular_Search_admin)

## 13.4. Inspecting available errata by using Hammer CLI

View and filter available errata to find applicable or installable updates and review advisory metadata before promoting content or patching hosts.

**Procedure**

- View errata that are available for all organizations:

  ```
  $ hammer erratum list
  ```
- View details of a specific erratum:

  ```
  $ hammer erratum info --id erratum_ID
  ```
- Search errata by entering the query with the `--search` option. For the list of parameters available for search, see [Section 13.11, “Parameters available for errata search”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Parameters_Available_for_Errata_Search_content-management "13.11. Parameters available for errata search"). For example, search for applicable errata for the selected product that contains the specified bugs ordered so that the security errata are displayed on top:

  ```
  $ hammer erratum list \
  --product-id 7 \
  --search "bug = 1213000 or bug = 1207972" \
  --errata-restrict-applicable 1 \
  --order "type desc"
  ```

## 13.5. Creating a content view filter for errata by using Satellite web UI

Control which errata are published with a content view, so you can keep production systems at a known patch level while testing newer updates separately.

You can use content filters to limit errata by ID, date range, or type such as security, bug fix, or enhancement updates. For example, exclude errata after a certain date in production while you test compatibility of newer packages in a separate lifecycle environment.

**Prerequisites**

- You have created a content view with the repositories that contain the required errata. For more information, see [Section 9.2.3, “Creating a content view by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-content-view-by-using-web-ui "9.2.3. Creating a content view by using Satellite web UI").

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Select a content view that you want to use for applying errata.
3. On the **Filters** tab, click **Create Filter**.
4. In the **Name** field, enter `Errata Filter`.
5. From the **Content Type** list, select **Errata – by date range**.
6. Select **Exclude filter**.
7. Optional: In the **Description** field, enter `Exclude errata items from YYYY-MM-DD`.
8. Click **Create filter**.
9. For **Errata Type**, select the checkboxes of errata types you want to exclude. For example, select the **Enhancement** and **Bugfix** checkboxes and clear the **Security** checkbox to exclude enhancement and bugfix errata after certain date, but include all the security errata.
10. For **Date Type**, select one of two checkboxes:

    - **Updated from** for the date of the last update of the erratum.
    - **Issued from** for the issued date of the erratum.
11. Select the **Start Date** to exclude all errata on or after the selected date.
12. Leave the **End Date** field blank.
13. Click **Save**.
14. Click **Publish New Version** to publish the resulting repository.
15. Enter `Adding errata filter` in the **Description** field.
16. Click **Save**.

    When the content view completes publication, notice the **Content** column reports a reduced number of packages and errata from the initial repository. This means the filter successfully excluded the all non-security errata from the last year.
17. Click the **Versions** tab.
18. Click **Promote** to the right of the published version.
19. Select the environments you want to promote the content view version to.
20. In the **Description** field, enter the description for promoting.
21. Click **Promote Version** to promote this content view version across the required environments.

## 13.6. Creating a content view filter for errata by using CLI

Control which errata are published with a content view, so you can keep production systems at a known patch level while testing newer updates separately.

**Procedure**

1. Create a filter for the errata:

   ```
   $ hammer content-view filter create \
   --content-view "My_Content_View" \
   --description "Exclude errata items from the YYYY-MM-DD" \
   --name "My_Filter_Name" \
   --organization "My_Organization" \
   --type "erratum"
   ```
2. Create a filter rule to exclude all errata on or after a *Start Date*:

   ```
   $ hammer content-view filter rule create \
   --content-view "My_Content_View" \
   --content-view-filter="My_Content_View_Filter" \
   --organization "My_Organization" \
   --start-date "YYYY-MM-DD" \
   --types=security,enhancement,bugfix
   ```
3. Publish the content view:

   ```
   $ hammer content-view publish \
   --name "My_Content_View" \
   --organization "My_Organization"
   ```
4. Promote the content view to the lifecycle environment so that the included errata are available to that lifecycle environment:

   ```
   $ hammer content-view version promote \
   --content-view "My_Content_View" \
   --organization "My_Organization" \
   --to-lifecycle-environment "My_Lifecycle_Environment"
   ```

## 13.7. Adding errata to an incremental content view by using Satellite web UI

Create an incremental content view version when errata are applicable but not installable, so you can publish the updates and make them available to hosts.

> **Important**
>
> If your content view version is old, you might encounter incompatibilities when incrementally adding enhancement errata. This is because enhancements are typically designed for the most current software in a repository.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Content Types** > **Errata**.
2. From the **Errata** list, click the name of the errata that you want to apply.
3. Select the hosts that you want to apply the errata to, and click **Apply to Hosts**. This creates the incremental update to the content view.
4. If you want to apply the errata to the host, select the **Apply Errata to Content Hosts immediately after publishing** checkbox.
5. Click **Confirm** to apply the errata.

**Additional resources**

- [Section 13.10, “Dependency resolution limitations for incremental errata updates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#dependency-resolution-limitations-for-incremental-errata-updates "13.10. Dependency resolution limitations for incremental errata updates")

## 13.8. Adding errata to an incremental content view by using Hammer CLI

Create an incremental content view version when errata are applicable but not installable, so you can publish the updates and make them available to hosts.

> **Important**
>
> If your content view version is old, you might encounter incompatibilities when incrementally adding enhancement errata. This is because enhancements are typically designed for the most current software in a repository.

**Procedure**

1. List the errata and its corresponding IDs:

   ```
   $ hammer erratum list
   ```
2. List the different content-view versions and the corresponding IDs:

   ```
   $ hammer content-view version list
   ```
3. Apply a single erratum to content-view version. You can add more IDs in a comma-separated list.

   ```
   $ hammer content-view version incremental-update \
   --content-view-version-id My_Content_View_Version_ID \
   --errata-ids My_Erratum_ID_1,My_Erratum_ID_2
   ```

**Additional resources**

- [Section 13.10, “Dependency resolution limitations for incremental errata updates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#dependency-resolution-limitations-for-incremental-errata-updates "13.10. Dependency resolution limitations for incremental errata updates")

## 13.9. Adding errata to an incremental content view by using MCP

Use your AI application with the MCP server to create an incremental content view update when errata are applicable but not yet installable on your hosts.

> **Warning**
>
> Review the output generated by AI before using it in production.

> **Important**
>
> The MCP server for Satellite is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Procedure**

1. Allow the MCP server to trigger content view actions:

   ```
   $ podman run --interactive --tty --publish 127.0.0.1:8080:8080 \
     --volume Path_to_My_CA_Bundle:/app/ca.pem:ro,Z \
     registry.redhat.io/satellite/foreman-mcp-server-rhel9:6.18 \
     --foreman-url https://satellite.example.com \
     --allowed-cv-actions "incremental_update"
   ```

   For more information, see [Deploying the MCP server for Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#deploying-the-mcp-server-for-satellite) in *Managing hosts*.
2. Type a prompt in your AI application to list applicable errata:

   ```
   Show a list of applicable errata on my Satellite.
   ```
3. The MCP server will return a list of applicable errata to the AI application. Review the information.
4. The Satellite MCP server provides a prompt named `Add Errata to Content Views`, which you can use to perform an incremental update of a content view. Refer to the documentation of your AI application to find more about how to use MCP server prompts. Review all the steps that the AI application performs.

**Additional resources**

- [Section 13.10, “Dependency resolution limitations for incremental errata updates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#dependency-resolution-limitations-for-incremental-errata-updates "13.10. Dependency resolution limitations for incremental errata updates")

## 13.10. Dependency resolution limitations for incremental errata updates

Incremental content view updates can resolve some package dependencies, but Satellite may still pull newer dependency versions that conflict with packages already in the repository.

When a repository update becomes available with a new dependency, Satellite retrieves the newest version of the package to solve the dependency, even if there are older versions available in the existing repository package. This can create further dependency resolution problems when installing packages.

**Example 13.1. Dependency resolution limitation**

A repository on your client has the package `example_repository-1.0` with the dependency `example_repository-libs-1.0`. The repository also has another package `example_tools-1.0`.

A security erratum becomes available with the package `example_tools-1.1`. The `example_tools-1.1` package requires the `example_repository-libs-1.1` package as a dependency.

After an incremental content view update, the `example_tools-1.1`, `example_tools-1.0`, and `example_repository-libs-1.1` are now in the repository. The repository also has the packages `example_repository-1.0` and `example_repository-libs-1.0`. Note that the incremental update to the content view did not add the package `example_repository-1.1`. Because you can install all these packages by using `dnf`, no potential problem is detected. However, when the client installs the `example_tools-1.1` package, a dependency resolution problem occurs because both `example_repository-libs-1.0` and `example_repository-libs-1.1` cannot be installed.

There is currently no workaround for this problem. The larger the time frame, and minor *Y* releases between the base set of packages and the errata being applied, the higher the chance of a problem with dependency resolution.

## 13.11. Parameters available for errata search

Use these parameters to search and filter errata by advisory ID, CVE, package name, severity, type, and issue or update date.

| Parameter | Description | Example |
| --- | --- | --- |
| bug | Search by the Bugzilla number. | *bug = 1172165* |
| cve | Search by the CVE number. | *cve = CVE-2015-0235* |
| id | Search by the errata ID. The auto-suggest system displays a list of available IDs as you type. | *id = RHBA-2014:2004* |
| issued | Search by the issue date. You can specify the exact date, like "Feb16,2015", or use keywords, for example "Yesterday", or "1 hour ago". The time range can be specified with the use of the "<" and ">" operators. | *issued < "Jan 12,2015"* |
| package | Search by the full package build name. The auto-suggest system displays a list of available packages as you type. | *package = glib2-2.22.5-6.el6.i686* |
| package_name | Search by the package name. The auto-suggest system displays a list of available packages as you type. | *package_name = glib2* |
| severity | Search by the severity of the issue fixed by the security update. Specify *Critical*, *Important*, or *Moderate*. | *severity = Critical* |
| title | Search by the advisory title. | *title ~ openssl* |
| type | Search by the advisory type. Specify *security*, *bugfix*, or *enhancement*. | *type = bugfix* |
| updated | Search by the date of the last update. You can use the same formats as with the `issued` parameter. | *updated = "6 days ago"* |
