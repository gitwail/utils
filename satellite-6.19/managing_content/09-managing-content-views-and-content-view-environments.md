---
title: "Managing content views and content view environments"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-views-and-content-view-environments"
---
# Chapter 9. Managing content views and content view environments

Use content views to curate the content that hosts consume. You can create and promote content views, configure filters, work with rolling and composite views, manage versions, and assign content view environments to hosts.

## 9.1. Workflow for creating content views

Follow this sequence to add repositories, optionally refine content with filters and dependency resolution, publish and promote the content view, and attach hosts.

The general workflow for creating content views for filtering and creating snapshots is as follows:

1. Create a content view.
2. Add one or more repositories that you want to the content view.
3. Optional: Create one or more filters to refine the content of the content view.
4. Optional: Resolve any package dependencies for a content view.
5. Publish the content view.
6. Optional: Promote the content view to another environment.
7. Attach the host to the content view.

   If a repository is not associated with the content view, the file `/etc/yum.repos.d/redhat.repo` remains empty and hosts registered to it cannot receive updates.

Hosts can only be associated with a single content view. To associate a host with multiple content views, create a composite content view.

**Additional resources**

- [Section 9.3.2, “Content filter examples”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Content_Filter_Examples_content-management "9.3.2. Content filter examples")
- [Section 9.4, “Dependency solving for content views”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#dependency-solving-for-content-views "9.4. Dependency solving for content views")
- [Section 9.2.10, “Promoting a content view by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#promoting-a-content-view-by-using-web-ui "9.2.10. Promoting a content view by using Satellite web UI")
- [Section 9.6.2, “Creating a composite content view by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-composite-content-view-by-using-web-ui "9.6.2. Creating a composite content view by using Satellite web UI")

## 9.2. Managing content views

Red Hat Satellite uses content views to allow your hosts access to a deliberately curated subset of content. To do this, you must define which repositories to use and then apply certain filters to the content.

### 9.2.1. Content views in Red Hat Satellite

A content view is a deliberately curated subset of content that your hosts can access. By creating a content view, you can define the software versions used by a particular environment or Capsule Server.

Each content view creates a set of repositories across each environment. Your Satellite Server stores and manages these repositories. For example, you can create content views in the following ways:

- A content view with older package versions for a production environment and another content view with newer package versions for a *Development* environment.
- A content view with a package repository required by an operating system and another content view with a package repository required by an application.
- A composite content view for a modular approach to managing content views. For example, you can use one content view for content for managing an operating system and another content view for content for managing an application. By creating a composite content view that combines both content views, you create a new repository that merges the repositories from each of the content views. However, the repositories for the content views still exist and you can keep managing them separately as well.

  Default Organization View
  :   A *Default Organization View* is an application-controlled content view for all content that is synchronized to Satellite. You can register a host to the *Library* environment on Satellite to consume the *Default Organization View* without configuring content views and lifecycle environments.

  Promoting a content view across environments
  :   When you promote a content view from one environment to the next environment in the application lifecycle, Satellite updates the repository and publishes the packages.

**Example 9.1. Promoting a package from *Development* to *Testing***

The repositories for *Testing* and *Production* contain the `my-software-1.0-0.noarch.rpm` package:

|  | Development | Testing | Production |
| --- | --- | --- | --- |
| Version of the content view | Version 2 | Version 1 | Version 1 |
| Contents of the content view | *my-software*-1.1-0.noarch.rpm | *my-software*-1.0-0.noarch.rpm | *my-software*-1.0-0.noarch.rpm |

If you promote Version 2 of the content view from *Development* to *Testing*, the repository for *Testing* updates to contain the `my-software-1.1-0.noarch.rpm` package:

|  | Development | Testing | Production |
| --- | --- | --- | --- |
| Version of the content view | Version 2 | **Version 2** | Version 1 |
| Contents of the content view | *my-software*-1.1-0.noarch.rpm | ***my-software*-1.1-0.noarch.rpm** | *my-software*-1.0-0.noarch.rpm |

This ensures hosts are designated to a specific environment but receive updates when that environment uses a new version of the content view.

### 9.2.2. Best practices for content views

Red Hat recommends you apply these practices when you plan, publish, and maintain content views to reduce administrative overhead and keep host content consistent.

- Content views that bundle content, such as Red Hat Enterprise Linux and additional software like `Apache-2.4` or `PostgreSQL-16.2`, are easier to maintain. Content views that are too small require more maintenance.
- If you require daily updated content, use the content view `Default Organization View`, which contains the latest synchronized content from all repositories and is available in the Library lifecycle environment.
- If you require daily updated content for hosts registered to a specific Capsule Server, use rolling content views and assign them to a lifecycle environment other than **Library**.
- To give hosts access to content from multiple content views, such as when you update one content view weekly and another monthly, you have two options:

  - Assign multiple content view environments to hosts. For more information, see [Section 9.8.4, “Assigning content view environments to hosts in bulk”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#assigning-content-view-environments-to-hosts-in-bulk "9.8.4. Assigning content view environments to hosts in bulk").
  - Assign composite content views to hosts.

  For more information, see [Section 9.9, “Comparison of content view environments and composite content views”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#comparison-of-content-view-environments-and-composite-content-views "9.9. Comparison of content view environments and composite content views").
- If you use composite content views, first publish the content views and then publish the composite content views. The more content views you bundle into composite content views, the more effort is needed to change or update content.
- Setting a lifecycle environment for content views is unnecessary if they are solely bundled to a composite content view.
- Automate creating and publishing composite content views and lifecycle environments by using a Hammer script or an [Ansible Playbook](https://theforeman.github.io/foreman-ansible-modules/develop/index.html). Use cron jobs, systemd timers, or recurring logics for more visibility.
- Add the changes and date to the description of each published content view or composite content view version. The most recent activity, such as moving content to a new lifecycle environment, is displayed by date in the Satellite web UI, regardless of the latest changes to the content itself.
- Publishing a new content view or composite content view creates a new major version. Incremental errata updates increment the minor version. Note that you cannot change or reset this counter.

### 9.2.3. Creating a content view by using Satellite web UI

Create a content view to define which repositories and content your hosts can access through lifecycle environments.

While you can stipulate whether you want to resolve any package dependencies on a content view by content view basis, you might want to change the default Satellite settings to enable or disable package resolution for all content views. For more information, see [Section 9.4, “Dependency solving for content views”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#dependency-solving-for-content-views "9.4. Dependency solving for content views").

**Prerequisites**

- At least one repository is available in your organization.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Click **Create content view**.
3. In the **Name** field, enter a name for the view. Satellite automatically completes the **Label** field from the name you enter.
4. In the **Description** field, enter a description of the view.
5. In the **Type** field, select a **Content view** or a **Composite content view**.
6. Optional: If you want to solve dependencies automatically every time you publish this content view, select the **Solve dependencies** checkbox. Dependency solving slows the publishing time and might ignore any content view filters you use. This can also cause errors when resolving dependencies for errata.
7. Click **Create content view**.
8. On the **Repositories** tab, select the repository from the **Type** list that you want to add to your content view, select the checkbox next to the available repositories you want to add, then click **Add repositories**.
9. Click **Publish new version** and in the **Description** field, enter information about the version to log changes.
10. Optional: Enable a promotion path by clicking **Promote** and select one or more lifecycle environments to promote the new version to.
11. Click **Next**.
12. On the **Review details** page, review the environments you are trying to publish.
13. Click **Finish**.

**Next steps**

- To register a host to your content view, see [Registering hosts by using global registration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration) in *Managing hosts*.

### 9.2.4. Creating a content view by using Hammer CLI

Create a content view to define which repositories and content your hosts can access through lifecycle environments.

While you can stipulate whether you want to resolve any package dependencies on a content view by content view basis, you might want to change the default Satellite settings to enable or disable package resolution for all content views. For more information, see [Section 9.4, “Dependency solving for content views”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#dependency-solving-for-content-views "9.4. Dependency solving for content views").

**Prerequisites**

- At least one repository is available in your organization.

**Procedure**

1. Obtain a list of repository IDs:

   ```
   $ hammer repository list --organization "My_Organization"
   ```
2. Create the content view and add repositories:

   ```
   $ hammer content-view create \
   --description "My_Content_View" \
   --name "My_Content_View" \
   --organization "My_Organization" \
   --repository-ids My_Repository_ID_1,My_Repository_ID_2
   ```
3. Optional: Add another repository to your content view:

   ```
   $ hammer content-view add-repository \
   --name "My_Content_View" \
   --organization "My_Organization" \
   --repository-id My_Repository_ID_3
   ```
4. Publish the content view:

   ```
   $ hammer content-view publish \
   --description "My_Content_View" \
   --name "My_Content_View" \
   --organization "My_Organization"
   ```

   Satellite Server creates the new version of the view and publishes it to the Library environment.

### 9.2.5. Copying a content view by using Satellite web UI

Copy an existing content view to create a content view based on its repositories and filters without reconfiguring them from scratch.

> **Note**
>
> A copied content view does not have the same history as the original content view. Version 1 of the copied content view begins at the last version of the original content view. As a result, you cannot promote an older version of a content view from the copied content view.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Select the content view you want to copy.
3. Open the options menu and click **Copy**.
4. In the **Name** field, enter a name for the new content view and click **Copy content view**.

**Verification**

- The copied content view appears on the **Content views** page.

### 9.2.6. Copying a content view by using Hammer CLI

Copy an existing content view to create a content view based on its repositories and filters without reconfiguring them from scratch.

> **Note**
>
> A copied content view does not have the same history as the original content view. Version 1 of the copied content view begins at the last version of the original content view. As a result, you cannot promote an older version of a content view from the copied content view.

**Procedure**

- Copy the content view by using Hammer:

  ```
  $ hammer content-view copy \
  --name My_original_CV_name \
  --new-name My_new_CV_name
  ```

### 9.2.7. Synchronizing a content view to a Capsule Server

In the Satellite web UI, you can only synchronize all selected lifecycle environments simultaneously. If you need to synchronize smaller items, such as individual lifecycle environments, single content views, and single repositories, use the Hammer CLI.

**Prerequisites**

- The content view is published and promoted to a lifecycle environment that the Capsule Server synchronizes.

**Procedure**

- Synchronize a content view to your Capsule Server:

  ```
  $ hammer capsule content synchronize \
  --content-view "My_Content_View_Name" \
  --id My_Capsule_Server_ID
  ```

### 9.2.8. Viewing module streams by using Satellite web UI

View module streams in your content views to verify which modular Yum content is included before you publish or promote a content view.

**Prerequisites**

- The content view has at least one published version that includes modular repositories.

**Procedure**

1. In the Satellite web UI, **Content** > **Lifecycle** > **Content Views**.
2. Select your content view.
3. Click on a published version.
4. Click **Module Streams** to view the module streams that are available for the Content Types.
5. Use the **Search** field to search for specific modules.
6. To view the information about the module, click the module and its corresponding tabs to include **Details**, **Repositories**, **Profiles**, and **Artifacts**.

### 9.2.9. Viewing module streams by using Hammer CLI

View module streams in your content views to verify which modular Yum content is included before you publish or promote a content view.

**Prerequisites**

- Your organization includes repositories with module streams.

**Procedure**

1. List all organizations:

   ```
   $ hammer organization list
   ```
2. View all module streams for your organization:

   ```
   $ hammer module-stream list \
   --organization-id My_Organization_ID
   ```

### 9.2.10. Promoting a content view by using Satellite web UI

Promote a content view to the next lifecycle environment to make its published content available to hosts in that environment.

**Prerequisites**

- Your Satellite account has a role that grants the `promote_or_remove_content_views` and `promote_or_remove_content_views_to_environment` permissions.
- The content view has at least one published version.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Select the content view that you want to promote.
3. Select the version that you want to promote, click the options icon, and click **Promote**.
4. Select the environment where you want to promote the content view and click **Promote**.

**Next steps**

- To register a host to your content view, see [Registering hosts by using global registration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration) in *Managing hosts*.

### 9.2.11. Promoting a content view by using Hammer CLI

Promote a content view to the next lifecycle environment to make its published content available to hosts in that environment.

**Prerequisites**

- Your Satellite account has a role that grants the `promote_or_remove_content_views` and `promote_or_remove_content_views_to_environment` permissions.
- The content view has at least one published version.

**Procedure**

- Promote the content view to a lifecycle environment:

  ```
  $ hammer content-view version promote \
  --content-view "My_Content_View_Name" \
  --version 1 \
  --to-lifecycle-environment "My_Lifecycle_Environment_Name" \
  --organization "My_Organization"
  ```

  Repeat the command for each lifecycle environment to promote the content view to.

**Verification**

- Display information about your content view version to verify that it is promoted to the required lifecycle environment:

  ```
  $ hammer content-view version info --id My_Content_View_Version_ID
  ```

**Next steps**

- To register a host to your content view, see [Registering hosts by using global registration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration) in *Managing hosts*.

### 9.2.12. Publishing and promoting a content view by using MCP

You can use your AI application to publish and promote content views across different lifecycle environments.

> **Warning**
>
> Review the output generated by AI before using it in production.

> **Important**
>
> The MCP server for Satellite is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

- The MCP server for Satellite is deployed and configured to allow content view publish and promote actions. For more information, see [Deploying the MCP server for Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#deploying-the-mcp-server-for-satellite) in *Managing hosts*.

**Procedure**

1. Allow the MCP server to trigger content view publish and promote actions:

   ```
   $ podman run --interactive --tty --publish 127.0.0.1:8080:8080 \
     --volume Path_to_My_CA_Bundle:/app/ca.pem:ro,Z \
     registry.redhat.io/satellite/foreman-mcp-server-rhel9:6.18 \
     --foreman-url https://satellite.example.com \
     --allowed-cv-actions "publish,promote"
   ```

   For more information, see [Deploying the MCP server for Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#deploying-the-mcp-server-for-satellite) in *Managing hosts*.
2. Type a prompt in your AI application to list content views:

   ```
   Show a list of content views on my Satellite.
   ```
3. The MCP server will return a list of content views to the AI application. Review the information.
4. Type a prompt in your AI application to publish a new version of the content view or to promote the content view to an environment. Review all the steps that the AI application performs.

### 9.2.13. Promoting a content view to all environments in an organization

You can promote content views across all lifecycle environments within an organization by using the following Bash script.

**Prerequisites**

- Your Satellite account has a role that grants the `promote_or_remove_content_views` and `promote_or_remove_content_views_to_environment` permissions.
- The content view version that you want to promote is published.

**Procedure**

- Promote content views across all lifecycle environments within an organization:

  ```shell-session
  ORG="My_Organization"
  CVV_ID=My_Content_View_Version_ID

  for i in $(hammer --no-headers --csv lifecycle-environment list --organization $ORG | awk -F, {'print $1'} | sort -n)
  do
     hammer content-view version promote --organization $ORG --to-lifecycle-environment-id $i --id $CVV_ID
  done
  ```

## 9.3. Configuring content view filters

After you add repositories to a content view, you can refine what content hosts receive by configuring include and exclude filters and optional dependency resolution.

### 9.3.1. Content filter overview

Use content view filters to include or exclude specific Yum packages, errata, and other content types from a published view. Without filters, a content view includes all content from its selected repositories.

Filter types
:   There are two types of content filters:

    Table 9.1. Filter types

    | Filter Type | Description |
    | --- | --- |
    | **Include** | You start with no content, then select which content to add from the selected repositories. Use this filter to combine multiple content items. |
    | **Exclude** | You start with all content from selected repositories, then select which content to remove. Use this filter when you want to use most of a particular content repository while excluding certain packages. The filter uses all content in the repository except for the content you select. |

Include and Exclude filter combinations
:   If using a combination of Include and Exclude filters, publishing a content view triggers the include filters first, then the exclude filters. In this situation, select which content to include, then which content to exclude from the inclusive subset.

Content types
:   You can filter content based on the following content types:

    Table 9.2. Content types

    | Content Type | Description |
    | --- | --- |
    | **RPM** | Filter packages based on their name and version number. The **RPM** option filters non-modular RPM packages and errata. Source RPMs are not affected by this filter and will still be available in the content view. |
    | **Package Group** | Filter packages based on package groups. The list of package groups is based on the repositories added to the content view. |
    | **Erratum (by ID)** | Select which specific errata to add to the filter. The list of Errata is based on the repositories added to the content view. |
    | **Erratum (by Date and Type)** | Select a issued or updated date range and errata type (Bugfix, Enhancement, or Security) to add to the filter. |
    | **Module Streams** | Select whether to include or exclude specific module streams. The **Module Streams** option filters modular RPMs and errata, but does not filter non-modular content that is associated with the selected module stream. |
    | **Container Image Tag** | Select whether to include or exclude specific container image tags. |

### 9.3.2. Content filter examples

These examples show common content filter configurations for package groups, errata, and module streams that you can adapt when refining a content view.

> **Note**
>
> Filters can significantly increase the time to publish a content view. For example, if a content view publish task completes in a few minutes without filters, it can take 30 minutes after adding an exclude or include errata filter.

**Example 9.2. Include a package group**

Create a repository with the base Red Hat Enterprise Linux packages. This filter requires a Red Hat Enterprise Linux repository added to the content view.

**Filter:**

- **Inclusion Type:** Include
- **Content Type:** Package Group
- **Filter:** Select only the **Base** package group

**Example 9.3. Exclude errata**

Create a repository that excludes all errata, except for security updates, after a certain date. This is useful if you want to perform system updates on a regular basis with the exception of critical security updates, which must be applied immediately. This filter requires a Red Hat Enterprise Linux repository added to the content view.

**Filter:**

- **Inclusion Type:** Exclude
- **Content Type:** Erratum (by Date and Type)
- **Filter:** Select only the **Bugfix** and **Enhancement** errata types, and clear the **Security** errata type. Set the **Date Type** to **Updated On**. Set the **Start Date** to the date you want to restrict errata. Leave the **End Date** blank to ensure any new non-security errata is filtered.

**Example 9.4. Exclude errata and include a package group**

A combination of Example 1 and Example 2 where you only require the operating system packages and want to exclude recent bug fix and enhancement errata. This requires two filters attached to the same content view. The content view processes the Include filter first, then the Exclude filter.

**Filter 1:**

- **Inclusion Type:** Include
- **Content Type:** Package Group
- **Filter:** Select only the **Base** package group

**Filter 2:**

- **Inclusion Type:** Exclude
- **Content Type:** Erratum (by Date and Type)
- **Filter:** Select only the **Bugfix** and **Enhancement** errata types, and clear the **Security** errata type. Set the **Date Type** to **Updated On**. Set the **Start Date** to the date you want to restrict errata. Leave the **End Date** blank to ensure any new non-security errata is filtered.

**Example 9.5. Include a module stream**

Filter a specific module stream in a content view.

**Filter 1:**

- **Inclusion Type:** Include
- **Content Type:** Module Stream
- **Filter:** Select only the specific module stream that you want for the content view, for example **ant**, and click **Add Module Stream**.

**Filter 2:**

- **Inclusion Type:** Exclude
- **Content Type:** Package
- **Filter:** Add a rule to filter any non-modular packages that you want to exclude from the content view. If you do not filter the packages, the content view filter includes all non-modular packages associated with the module stream **ant**. Add a rule to exclude all `*` packages, or specify the package names that you want to exclude.

**Additional resources**

- ["How do content filters work in Satellite 6"](https://access.redhat.com/solutions/1564953)

### 9.3.3. Creating a content view filter by using Satellite web UI

Create content view filters to include or exclude specific packages, errata, and other content types from a content view. Package filters match content by name, version, and architecture.

For examples of how to build a filter, see [Section 9.3.2, “Content filter examples”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Content_Filter_Examples_content-management "9.3.2. Content filter examples").

**Prerequisites**

- You have created a content view with the repositories you want to filter. For more information, see [Section 9.2.3, “Creating a content view by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-content-view-by-using-web-ui "9.2.3. Creating a content view by using Satellite web UI").

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Select a content view.
3. On the **Filters** tab, click **Create filter**.
4. Enter a name.
5. From the **Content type** list, select a content type.
6. From the **Inclusion Type** list, select either **Include filter** or **Exclude filter**.
7. Optional: In the **Description** field, enter a description for the filter.
8. Click **Create filter** to create your content filter.
9. Click **Add RPM rule**.
10. Enter a *name*, *architecture*, and *version*.
11. Click **Add rule**.
12. Select if you want the filter to **Apply to subset of repositories** or **Apply to all repositories in the CV**.
13. Click **Publish new version** to publish the filtered content view.
14. Optional: In the **Description** field, enter a description of the changes.
15. Optional: Select **Promote** to promote your filtered content view to a lifecycle environment.
16. Click **Finish** to publish a new version of the content view.

### 9.3.4. Creating a content view filter by using CLI

You can use Hammer CLI to create content view filters to include or exclude specific content units like packages, errata, or container image tags.

**Prerequisites**

- You have created a content view with the repositories you want to filter. For more information, see [Section 9.2.4, “Creating a content view by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-content-view-by-using-cli "9.2.4. Creating a content view by using Hammer CLI").

**Procedure**

1. Add a filter to the content view. Use the `--inclusion false` option to set the filter to an Exclude filter:

   ```
   $ hammer content-view filter create \
   --name "Errata Filter" \
   --type erratum --content-view "Example_Content_View" \
   --description "My latest filter" \
   --inclusion false \
   --organization "My_Organization"
   ```
2. Add a rule to the filter:

   ```
   $ hammer content-view filter rule create \
   --content-view "Example_Content_View" \
   --content-view-filter "Errata Filter" \
   --start-date "YYYY-MM-DD" \
   --types enhancement,bugfix \
   --date-type updated \
   --organization "My_Organization"
   ```
3. Publish the content view:

   ```
   $ hammer content-view publish \
   --name "Example_Content_View" \
   --description "Adding errata filter" \
   --organization "My_Organization"
   ```
4. Promote the view across all environments:

   ```
   $ hammer content-view version promote \
   --content-view "Example_Content_View" \
   --version 1 \
   --to-lifecycle-environment "Development" \
   --organization "My_Organization"
   $ hammer content-view version promote \
   --content-view "Example_Content_View" \
   --version 1 \
   --to-lifecycle-environment "Testing" \
   --organization "My_Organization"
   $ hammer content-view version promote \
   --content-view "Example_Content_View" \
   --version 1 \
   --to-lifecycle-environment "Production" \
   --organization "My_Organization"
   ```

## 9.4. Dependency solving for content views

Satellite can add dependencies of packages in a content view to the dependent repository when publishing the content view. To configure this, you can enable *dependency solving*.

For example, dependency solving is useful when you incrementally add a single package to a content view version. You might need to enable dependency solving to install that package.

However, dependency solving is unnecessary in most situations. For example:

- When incrementally adding a security errata to a content view, dependency solving can cause significant delays to content view publication without major benefits.
- Packages from a newer erratum might have dependencies that are incompatible with packages from an older content view version. Incrementally adding the erratum by solving dependencies might result in the inclusion of unwanted packages. As an alternative, consider updating the content view.

> **Note**
>
> Dependency solving only considers packages within the repositories of the content view. It does not consider packages installed on clients. For example, if a content view includes only AppStream, dependency solving does not include dependent BaseOS content at publish time.

Dependency solving can lead to the following problems:

Significant delay in content view publication
:   Satellite examines every repository in a content view for dependencies. Therefore, publish time increases with more repositories.

    To mitigate this problem, use multiple content views with fewer repositories and combine them into composite content views.

Ignored content view filters on dependent packages
:   Satellite prioritizes resolving package dependencies over the rules in your filter.

    For example, if you create a filter for security purposes but enable dependency solving, Satellite can add packages that you might consider insecure.

    To mitigate this problem, carefully test filtering rules to determine the required dependencies. If dependency solving includes unwanted packages, manually identify the core basic dependencies that the extra packages and errata need.

**Example 9.6. Combining exclusion filters with dependency solving**

For example, you can recreate Red Hat Enterprise Linux 9.3 by using content view filters and include selected errata from a later Red Hat Enterprise Linux 9 minor release. To achieve this, you create filters to exclude most of the errata after the Red Hat Enterprise Linux 9.3 release date, except a few that you need. Then, you enable dependency solving.

In this situation, dependency solving might include more packages than expected. As a result, the host diverges from Red Hat Enterprise Linux 9.3 machines.

If you do not need the extra errata and packages, do not configure content view filtering. Instead, enable and use the Red Hat Enterprise Linux 9.3 repository on the **Content** > **Red Hat Repositories** page in the Satellite web UI.

**Example 9.7. Excluding packages sometimes makes dependency solving impossible for DNF**

If you create Red Hat Enterprise Linux 9.3 repositories with a few excluded packages, `dnf upgrade` can sometimes fail.

Do not enable dependency solving to resolve the problem. Instead, investigate the error from `dnf` and adjust the filters to stop excluding the missing dependency.

Else, dependency solving might cause the repository to diverge from Red Hat Enterprise Linux 9.3.

**Additional resources**

- [Section 13.10, “Dependency resolution limitations for incremental errata updates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#dependency-resolution-limitations-for-incremental-errata-updates "13.10. Dependency resolution limitations for incremental errata updates")

### 9.4.1. Enabling dependency solving for a content view

Enable dependency solving on a content view when you need Satellite to include package dependencies during publication, such as when adding a single package incrementally.

**Prerequisites**

- You have reviewed [Section 9.4, “Dependency solving for content views”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#dependency-solving-for-content-views "9.4. Dependency solving for content views") to determine whether dependency solving is appropriate for your content view.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. From the list of content views, select the required content view.
3. On the **Details** tab, toggle **Solve dependencies**.

## 9.5. Managing content view versions

Each time you publish a content view, Satellite creates a new version. You can compare versions to review changes, delete unused versions to reclaim storage, and distribute archived versions for debugging.

### 9.5.1. Comparing content view versions

Compare two content view versions to identify added, removed, or changed packages, errata, and other content between versions.

**Prerequisites**

- The content view has at least two published versions.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Select a content view whose versions you want to compare.
3. On the **Versions** tab, select the checkbox next to any two versions you want to compare.
4. Click **Compare**.

   The **Compare** screen has the pre-selected versions in the version dropdown menus and tabs for all content types found in either version. You can filter the results to show only the same, different, or all content types. You can compare different content view versions by selecting them from the dropdown menus.

### 9.5.2. Distributing archived content view versions

Enable distribution of archived content view versions when you need access to repositories from published versions that are not currently promoted, such as for debugging.

**Prerequisites**

- Your Satellite account has a role that grants the `view_settings` and `edit_settings` permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Click the **Content** tab.
3. Set the **Distribute archived content view versions** parameter to **Yes**.
4. Click **Submit**.

   This enables the repositories of content view versions without lifecycle environments to be distributed at `satellite.example.com/pulp/content/My_Organization/content_views/My_Content_View/My_Content_View_Version/`.

   > **Note**
   >
   > Older non-promoted content view versions are not distributed once the setting is enabled. Only new content view versions become distributed.

### 9.5.3. Deleting multiple content view versions by using Satellite web UI

Delete multiple content view versions at once to remove obsolete snapshots and free storage on Satellite Server.

**Prerequisites**

- Your Satellite account has a role that grants the `promote_or_remove_content_views` permission.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Select the content view you want to delete versions of.
3. On the **Versions** tab, select the checkbox of the version or versions you want to delete.
4. Open the options menu at the top of the list of content views.
5. Click **Delete** to open the deletion wizard that shows any affected environments.
6. If there are no affected environments, review the details and click **Delete**.
7. If there are any affected environments, reassign any hosts or activation keys before deletion.
8. Review the details of the actions.
9. Click **Delete**.

### 9.5.4. Deleting multiple content view versions by using Hammer CLI

You can delete multiple content view versions simultaneously by using Hammer CLI.

**Procedure**

1. List versions of your content view:

   ```
   $ hammer content-view info \
   --name "My_Content_View_Name" \
   --organization-id My_Organization_ID
   ```
2. Delete content view versions:

   ```
   $ hammer content-view remove \
   --content-view-version-ids My_Content_View_Version_ID_1,My_Content_View_Version_ID_2 \
   --id My_Content_View_ID
   ```

**Verification**

- Verify that Satellite deleted the content view versions:

  ```
  $ hammer content-view info \
  --name "My_Content_View_Name" \
  --organization-id My_Organization_ID
  ```

### 9.5.5. Deleting multiple content view versions by using Ansible

You can delete multiple content view versions simultaneously by using Satellite Ansible collection.

**Procedure**

- Use the `redhat.satellite.content_view_version` module.

  For more information, see the Ansible module documentation with `ansible-doc redhat.satellite.content_view_version`.

### 9.5.6. Purging content view versions by using Hammer CLI

You can purge excess numbers of content view versions on Satellite to limit disk space usage. By default, Satellite keeps every version of a content view. Removing content view versions is a tradeoff between disk space and possibly bandwidth during content synchronizations to Capsule Servers and the possibility to roll back to older content snapshots.

Satellite only considers deleting content view versions that are not part of any lifecycle environment.

**Procedure**

1. Optional: View your content view versions:

   ```
   $ hammer content-view info \
   --name "My_Content_View_Name" \
   --organization-id My_Organization_ID
   ```
2. Clean up content view versions:

   ```
   $ hammer content-view purge \
   --name "My_Content_View_Name" \
   --organization-id My_Organization_ID \
   --versions-to-keep My_Number_Of_Versions_To_Keep
   ```

**Verification**

- Verify that Satellite deleted the content view versions:

  ```
  $ hammer content-view info \
  --name "My_Content_View_Name" \
  --organization-id My_Organization_ID
  ```

**Additional resources**

- [Recovering from a full disk in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#recovering-from-a-full-disk)

## 9.6. Using composite content views

Use composite content views when you need to merge content from multiple content views for hosts to consume.

### 9.6.1. Composite content views overview

A composite content view combines repositories from several content views for hosts to consume content. Use it when hosts need content from multiple content views, such as an operating system and an application, managed separately.

**Example 9.8. Application that supports different database servers**

You want to develop an application that supports different database servers. The *example_application* appears as:

| *example_software* |
| --- |
| Application |
| Database |
| Operating System |

Example of four separate content views:

- Red Hat Enterprise Linux (Operating System)
- PostgreSQL (Database)
- MariaDB (Database)
- *example_software* (Application)

From the previous content views, you can create two composite content views.

Example composite content view for a PostgreSQL database:

| Composite content view 1 – *example_software* on PostgreSQL |
| --- |
| *example_software* (Application) |
| PostgreSQL (Database) |
| Red Hat Enterprise Linux (Operating System) |

Example composite content view for a MariaDB:

| Composite content view 2 – *example_software* on MariaDB |
| --- |
| *example_software* (Application) |
| MariaDB (Database) |
| Red Hat Enterprise Linux (Operating System) |

Each content view is then managed and published separately. When you create a version of the application, you publish a new version of the composite content views. You can also select the **Auto Publish** option when creating a composite content view, and then the composite content view is automatically republished when a content view it includes is republished.

Repository restrictions
:   Docker repositories cannot be included more than once in a composite content view. For example, if you attempt to include two content views that contain the same docker repository in a composite content view, Satellite Server reports an error.

### 9.6.2. Creating a composite content view by using Satellite web UI

Create a composite content view to combine repositories from multiple content views for your hosts to consume.

**Prerequisites**

- The content views that you want to combine are published.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Click **Create content view**.
3. In the **Create content view** window, enter a name for the view in the **Name** field. Red Hat Satellite automatically completes the **Label** field from the name you enter.
4. Optional: In the **Description** field, enter a description of the view.
5. On the **Type** tab, select **Composite content view**.
6. Optional: If you want to automatically publish a new version of the composite content view when a content view is republished, select the **Auto publish** checkbox.
7. Click **Create content view**.
8. On the **Content views** tab, select the content views that you want to add to the composite content view, and then click **Add content views**.
9. In the **Add content views** window, select the version of each content view.
10. Optional: If you want to automatically update the content view to the latest version, select the **Always update to latest version** checkbox.
11. Click **Add**, then click **Publish new version**.
12. Optional: In the **Description** field, enter a description of the content view.
13. In the **Publish** window, set the **Promote** switch, then select the lifecycle environment.
14. Click **Next**, then click **Finish**.

### 9.6.3. Creating a composite content view by using Hammer CLI

Create a composite content view to combine repositories from multiple content views for your hosts to consume.

**Prerequisites**

- The content views that you want to combine are published.

**Procedure**

1. Before you create the composite content views, list the version IDs for your existing content views:

   ```
   $ hammer content-view version list \
   --organization "My_Organization"
   ```
2. Create a new composite content view. When the `--auto-publish` option is set to `yes`, the composite content view is automatically republished when a content view it includes is republished:

   ```
   $ hammer content-view create \
   --composite \
   --auto-publish yes \
   --name "Example_Composite_Content_View" \
   --description "Example composite content view" \
   --organization "My_Organization"
   ```
3. Add a content view to the composite content view. You can identify content view, content view version, and Organization in the commands by either their ID or their name. To add multiple content views to the composite content view, repeat this step for every content view you want to include.

   - If you have the **Always update to latest version** option enabled for the content view:

     ```
     $ hammer content-view component add \
     --component-content-view-id Content_View_ID \
     --composite-content-view "Example_Composite_Content_View" \
     --latest \
     --organization "My_Organization"
     ```
   - If you have the **Always update to latest version** option disabled for the content view:

     ```
     $ hammer content-view component add \
     --component-content-view-id Content_View_ID \
     --composite-content-view "Example_Composite_Content_View" \
     --component-content-view-version-id Content_View_Version_ID \
     --organization "My_Organization"
     ```
4. Publish the composite content view:

   ```
   $ hammer content-view publish \
   --name "Example_Composite_Content_View" \
   --description "Initial version of composite content view" \
   --organization "My_Organization"
   ```
5. Promote the composite content view across all environments:

   ```
   $ hammer content-view version promote \
   --content-view "Example_Composite_Content_View" \
   --version 1 \
   --to-lifecycle-environment "Development" \
   --organization "My_Organization"
   $ hammer content-view version promote \
   --content-view "Example_Composite_Content_View" \
   --version 1 \
   --to-lifecycle-environment "Testing" \
   --organization "My_Organization"
   $ hammer content-view version promote \
   --content-view "Example_Composite_Content_View" \
   --version 1 \
   --to-lifecycle-environment "Production" \
   --organization "My_Organization"
   ```

## 9.7. Using rolling content views

Use rolling content views when you need hosts to consume the latest synchronized content without publishing and promoting new content view versions.

### 9.7.1. Rolling content views

A rolling content view is a curated subset of Library content that hosts can access without publishing or promoting new content view versions. Use it to provide a continuous stream of the latest synchronized content from one or more repositories.

When you synchronize repositories to Satellite, all rolling content views that contain them get automatically updated to include the latest changes. You do not have to publish and/or promote a rolling content view compared to content views or composite content views.

Instead, you can assign rolling content views to one or multiple lifecycle environments. By doing so, you can synchronize subsets of the Library content from Satellite Server to Capsule Servers that are configured to consume content from the assigned lifecycle environments.

### 9.7.2. Creating a rolling content view by using Satellite web UI

Create a rolling content view to give hosts continuous access to the latest synchronized content without publishing new content view versions.

**Prerequisites**

- At least one populated repository exists in your organization.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Click **Create content view**.
3. In the **Create content view** window, enter a name for the content view in the **Name** field. Satellite automatically completes the **Label** field from the name you enter.
4. Optional: In the **Description** field, enter a description of the content view.
5. On the **Type** tab, select **Rolling content view**.
6. Optional: In the **Lifecycle Environments** field, assign your rolling content view to your lifecycle environments.
7. Click **Create content view**.
8. Click **Show repositories**.
9. Select the repositories that you want to add to your rolling content view.
10. Click **Add repositories** to add all selected repositories to your rolling content view.

**Next steps**

- You cannot publish or promote your rolling content view. Instead, continue by adding it to your activation key. For more information, see [Section 12.2, “Creating an activation key by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui "12.2. Creating an activation key by using Satellite web UI").
- To register a host to your rolling content view, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.

### 9.7.3. Creating a rolling content view by using Hammer CLI

Create a rolling content view to give hosts continuous access to the latest synchronized content without publishing new content view versions.

**Prerequisites**

- At least one repository is synchronized to your organization.

**Procedure**

1. List all available lifecycle environments:

   ```
   $ hammer lifecycle-environment list \
   --fields id,name \
   --organization "My_Organization"
   ```
2. List all available repositories to identify IDs of repositories to add to your rolling content view:

   ```
   $ hammer repository list \
   --fields id,name,product \
   --organization "My_Organization"
   ```
3. Create your rolling content view:

   ```
   $ hammer content-view create \
   --lifecycle-environment-ids My_List_Of_Lifecycle_Environment_IDs \
   --name "My_Rolling_Content_View" \
   --organization "My_Organization" \
   --repository-ids My_List_Of_Repository_IDs \
   --rolling
   ```

**Next steps**

- You cannot publish or promote your rolling content view. Instead, continue by adding it to your activation key. For more information, see [Section 12.3, “Creating an activation key by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-cli "12.3. Creating an activation key by using Hammer CLI").
- To register a host to your rolling content view, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.

### 9.7.4. Assigning a rolling content view to lifecycle environments by using Satellite web UI

Assign a rolling content view to lifecycle environments to limit which Library content is synchronized to Capsule Servers.

To consume rolling content views, you must assign them to one or more lifecycle environments. By doing so, you expose a subset of Library content to those lifecycle environments. Red Hat does not recommend assigning a rolling content view to the Library environment itself because it creates duplicate content within Library. By using environments other than Library, you can synchronize your rolling content views from Satellite Server to any Capsule Servers that are configured to consume the relevant lifecycle environments without the need to synchronize all of Library to Capsule Servers.

**Prerequisites**

- A rolling content view exists in your organization.
- At least one lifecycle environment other than Library exists in your organization.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Content Views**.
2. Select your rolling content view.
3. Select the **Details** tab.
4. In the **Lifecycle Environments** field, assign your rolling content view to your lifecycle environments.
5. Click **Save Environments** to submit your changes to Satellite.

**Next steps**

- Synchronize lifecycle environments to Capsule Servers. For more information, see [Adding lifecycle environments to Capsule Servers by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-lifecycle-environments-by-using-web-ui) in *Managing content*.

### 9.7.5. Assigning a rolling content view to lifecycle environments by using Hammer CLI

Assign a rolling content view to lifecycle environments to limit which Library content is synchronized to Capsule Servers.

To consume rolling content views, you must assign them to one or more lifecycle environments. By doing so, you expose a subset of Library content to those lifecycle environments. Red Hat does not recommend assigning a rolling content view to the Library environment itself because it creates duplicate content within Library. By using environments other than Library, you can synchronize your rolling content views from Satellite Server to any Capsule Servers that are configured to consume the relevant lifecycle environments without the need to synchronize all of Library to Capsule Servers.

**Prerequisites**

- A rolling content view exists in your organization.
- At least one lifecycle environment other than Library exists in your organization.

**Procedure**

1. List all content views:

   ```
   $ hammer content-view list \
   --fields "content view id,name" \
   --organization "My_Organization"
   ```
2. Assign your rolling content view to lifecycle environments:

   ```
   $ hammer content-view update \
   --id My_Rolling_Content_View_ID \
   --lifecycle-environment-ids My_List_Of_Lifecycle_Environment_IDs \
   --organization "My_Organization"
   ```

   If you want to remove your rolling content view from all lifecycle environments, pass an empty list.

**Next steps**

- Synchronize lifecycle environments to Capsule Servers. For more information, see [Synchronizing a content view to a Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-a-content-view-to-a-capsule-server) in *Managing content*.

## 9.8. Managing content view environments

A content view environment combines a lifecycle environment and a content view into a single entity. You can assign hosts to content view environments, control multi-environment access, and set content view priority.

### 9.8.1. Content view environments overview

By default, you can assign multiple content view environments to hosts and activation keys. This is controlled by the **Allow multiple content views** setting.

Hosts registered with multiple activation keys handle content view environment assignments based on the order of activation keys and order of content view environments.

When you disable **Allow multiple content views**, multi-environment hosts remain assigned to multiple content view environments and retain access to all their content. Existing multi-environment activation keys remain associated with multiple content view environments, and both multi-environment hosts and activation keys remain visible in the Satellite web UI and accessible through the Hammer CLI. However, registration fails if you attempt to assign a host to multiple content view environments or use a multi-environment activation key during host registration. Assigning multiple content view environments to a host or activation key results in an error.

When you disable **Allow multiple content views**, you can still reassign a multi-environment host to a single content view environment. You can also reassign a multi-environment activation key to a single content view environment or remove all content view environments from the key.

**Additional resources**

- [Content management settings in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#content-management-settings)
- [Section 9.8.3, “Content view environment ordering and priority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environment-ordering-and-priority "9.8.3. Content view environment ordering and priority")

### 9.8.2. Content view environment categories

Satellite labels content view environments according to the lifecycle environment and content view they represent.

The content view environments available in your organization fall into the following categories:

Library environment
:   Satellite assigns the Library environment to represent the Library lifecycle environment and the **Default Organization View** content view. Satellite labels this environment as `Library`.

Unpromoted content views
:   For each content view that you publish but do not promote to a lifecycle environment, Satellite creates a content view environment. Satellite labels these environments using the format: `Library/<content_view_label>`.

Promoted content views
:   For each content view that you promote to a specific lifecycle environment, Satellite creates a corresponding content view environment. Satellite labels these environments using the format: `<lifecycle_environment_label>/<content_view_label>`.

### 9.8.3. Content view environment ordering and priority

The order of content view environments on a host or activation key determines which repository version the host uses when the same repository exists in multiple content view environments.

During host registration, an activation key assigns content view environments in the order they are stored.

A host pulls content from the first assigned content view environment that contains the repository. If `Library` is first in the list, it overrides other content view environments because it contains all repositories.

The order of the content view environments is critical when repository conflicts occur. A repository conflict occurs when multiple content view environments contain a repository with the same label. For example: A host assigned to the content view environments `Library/cv1, dev/cv1` uses the following configuration:

```
$ hammer host update \
--content-view-environments "Library/cv1,dev/cv1" \
--name "server.example.com" \
--organization-id My_Organization_ID
```

Both content view environments include the `satellite-client-6-for-rhel-9-x86_64-rpms` repository. Log in as a `root` user, then run `subscription-manager repos` to inspect the available repositories on the host. The output reflects the `Library/cv1` content view environment:

```
# subscription-manager repos
```

This results in the following output:

```
+----------------------------------------------------------+
    Available Repositories in /etc/yum.repos.d/redhat.repo
+----------------------------------------------------------+
Repo ID:   satellite-client-6-for-rhel-9-x86_64-rpms
Repo Name: Red Hat Satellite Client 6 for RHEL 9 x86_64 (RPMs)
Repo URL:  https://satellite.example.com/pulp/content/My_Organization/Library/cv1/content/dist/layered/rhel9/x86_64/My_Product/My_Repository_ID/os
Enabled:   0
```

> **Note**
>
> The `Repo URL` reflects the `Library/cv1` content view environment, meaning the system uses content from `Library/cv1` and ignores `dev/cv1`.

To change priority, reorder the content view environments. To prioritize `dev/cv1` over `Library/cv1`, update the host settings:

```
$ hammer host update \
--content-view-environments "dev/cv1,Library/cv1" \
--name "server.example.com" \
--organization-id My_Organization_ID
```

After reordering, inspecting the repositories again shows the `dev/cv1` content view environment:

```
# subscription-manager repos
```

This results in the following output:

```
+----------------------------------------------------------+
    Available Repositories in /etc/yum.repos.d/redhat.repo
+----------------------------------------------------------+
Repo ID:   satellite-client-6-for-rhel-9-x86_64-rpms
Repo Name: Red Hat Satellite Client 6 for RHEL 9 x86_64 (RPMs)
Repo URL:  https://satellite.example.com/pulp/content/My_Organization/dev/cv1/content/dist/layered/rhel9/x86_64/My_Product/My_Repository_ID/os
Enabled:   0
```

The `Repo URL` now reflects the `dev/cv1` content view environment, meaning the system uses content from `dev/cv1` and ignores `Library/cv1`.

### 9.8.4. Assigning content view environments to hosts in bulk

Assign content view environments to multiple hosts at once to provide the same content for those hosts.

**Prerequisites**

- If you want to assign multiple content view environments, the **Allow multiple content views** setting must be enabled. For more information, see [Section 9.8.1, “Content view environments overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environments-overview "9.8.1. Content view environments overview").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the hosts to which you want to assign content view environments.
3. Click the hosts table menu icon and select **Manage content** > **Content view environments**.
4. Edit the content view environments as needed.

   - Click **Remove** to remove a content view environment.
   - Click **Add content view environment** to assign an additional content view environment.
   - Drag and drop the content view environments to change their order.
5. Click **Save**.

**Additional resources**

- [Section 9.8.3, “Content view environment ordering and priority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environment-ordering-and-priority "9.8.3. Content view environment ordering and priority")

### 9.8.5. Assigning content view environments to a host by using Satellite web UI

Assign content view environments to a host to provide content access for that host.

**Prerequisites**

- If you want to assign multiple content view environments, the **Allow multiple content views** setting must be enabled. For more information, see [Section 9.8.1, “Content view environments overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environments-overview "9.8.1. Content view environments overview").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host to which you want to assign content view environments.
3. On the the **Content view environments** card, click **Assign content view environments**.
4. Edit the content view environments as needed.

   - Click **Remove** to remove a content view environment.
   - Click **Assign another content view environment** to assign another content view environment.
   - Drag and drop the content view environments to change their order.
5. Optional: Select **Update the host immediately via remote execution** to update the host immediately.
6. Click **Save**.

**Additional resources**

- [Section 9.8.3, “Content view environment ordering and priority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environment-ordering-and-priority "9.8.3. Content view environment ordering and priority")

### 9.8.6. Assigning content view environments to a host by using Hammer CLI

Assign content view environments to a host to provide content access for that host. Use Hammer CLI when you automate configuration.

To assign content view environments to a host, specify the entire list in order. There is no interface in Hammer or the API to add, remove, or insert individual content view environments. The current content view environments on the host are replaced with the new list you provide.

**Prerequisites**

- If you want to assign multiple content view environments, the **Allow multiple content views** setting must be enabled. For more information, see [Section 9.8.1, “Content view environments overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environments-overview "9.8.1. Content view environments overview").

**Procedure**

1. List available content view environments in your organization:

   ```
   $ hammer content-view-environment list --organization "My_Organization"
   ```

   Record the labels of the environments you want to assign to the host.
2. Assign the content view environments to the host:

   ```
   $ hammer host update \
   --content-view-environments="Library/along_cv,LCE_XYZ/CV1" \
   --name "server.example.com" \
   --organization-id My_Organization_ID
   ```

**Additional resources**

- [Section 9.8.3, “Content view environment ordering and priority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environment-ordering-and-priority "9.8.3. Content view environment ordering and priority")

### 9.8.7. Assigning content view environments to a host by using Subscription Manager

Assign content view environments to a host to provide content access for that host. Use Subscription Manager when you configure content access from the host rather than from Satellite.

**Prerequisites**

- If you want to assign multiple content view environments, the **Allow multiple content views** setting must be enabled in Satellite. For more information, see [Section 9.8.1, “Content view environments overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environments-overview "9.8.1. Content view environments overview").
- You have a Satellite username and password, which Subscription Manager requires to list available environments.

**Procedure**

1. List available content view environments:

   ```
   # subscription-manager environments --list
   ```

   Record the names of the environments you want to assign to the host.
2. Assign the content view environments to the host:

   ```
   # subscription-manager environments --set My_Content_View_Environment_1,My_Content_View_Environment_2
   ```

**Verification**

- List the assigned content view environments:

  ```
  # subscription-manager environments --list-enabled
  ```

**Additional resources**

- [Section 9.8.3, “Content view environment ordering and priority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environment-ordering-and-priority "9.8.3. Content view environment ordering and priority")

## 9.9. Comparison of content view environments and composite content views

Compare composite content views and content view environments to decide how hosts access content from more than one content view. The differences include access timing, conflict resolution, and version selection.

Composite content views provide an alternative method for granting hosts access to content from multiple content views. You can use composite content views, multiple content view environments, or a combination of both. The key differences between these methods include the following:

Access timing
:   Hosts assigned to composite content views gain access to the combined content only after you publish the composite content view. Hosts assigned to multiple content view environments immediately access the combined content from all assigned environments.

Conflict resolution
:   Composite content views resolve conflicts at the time of publishing by merging duplicate repositories. For hosts assigned to multiple content view environments, repository conflicts are resolved based on the order of content view environments.

Version selection
:   Composite content views allow you to select specific versions of a content view, including older versions. With multiple content view environments, the host receives the version of the content view that is currently promoted to the selected lifecycle environment.

Choose the approach that best suits your requirements based on these differences.

**Additional resources**

- [Section 9.8.3, “Content view environment ordering and priority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environment-ordering-and-priority "9.8.3. Content view environment ordering and priority")
