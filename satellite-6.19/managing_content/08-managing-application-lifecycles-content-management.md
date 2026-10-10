---
title: "Managing application lifecycles"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Application_Lifecycles_content-management"
---
# Chapter 8. Managing application lifecycles

Lifecycle environments in Satellite separate content into ordered stages from development to production and link content views, hosts, and Capsule Server synchronization. You can create environment paths to stage applications and promote content views to deliver new versions to hosts.

## 8.1. Introduction to application lifecycle

The *application lifecycle* organizes how hosts and software appear at each stage of delivery. In Satellite, each stage is a lifecycle environment backed by a content view that selects repositories and packages for hosts registered to that stage.

The application lifecycle defines how a particular system and its software look at a particular stage. For example, an application lifecycle might be simple; you might only have a development stage and production stage. In this case the application lifecycle might look like this:

- Development
- Production

However, a more complex application lifecycle might have further stages, such as a phase for testing or a beta release. This adds extra stages to the application lifecycle:

- Development
- Testing
- Beta Release
- Production

Satellite provides methods to customize each application lifecycle stage so that it suits your specifications.

Each stage in the application lifecycle is called an *environment* in Satellite. Each environment uses a specific collection of content. Satellite defines these content collections as a content view. Each content view acts as a filter where you can define what repositories, and packages to include in a particular environment. This provides a method for you to define specific sets of content to designate to each environment.

For example, an email server might only require a simple application lifecycle where you have a production-level server for real-world use and a test server for trying out the latest mail server packages. When the test server passes the initial phase, you can set the production-level server to use the new packages.

Another example is a development lifecycle for a software product. To develop a new piece of software in a development environment, test it in a quality assurance environment, pre-release as a beta, then release the software as a production-level application.

**Figure 8.1. Satellite application lifecycle**

[Image: Satellite application lifecycle](https://access.redhat.com/webassets/avalon/d/Red_Hat_Satellite-6.19-Managing_content-en-US/images/630edab3257dfa4d62c130d8ff311c3a/application-lifecycle-satellite.png)

## 8.2. Content promotion across the application lifecycle

In the application lifecycle chain, moving content from one environment to the next is called *promotion*. Promotion updates repositories of the target environment so hosts registered to that environment can use the new versions.

**Example 8.1. Content promotion across Satellite lifecycle environments**

Each environment contains a set of systems registered to Red Hat Satellite. These systems only have access to repositories relevant to their environment. When you promote packages from one environment to the next, the target environment’s repositories receive new package versions. As a result, each system in the target environment can update to the new package versions.

| Development | Testing | Production |
| --- | --- | --- |
| *example_software*-1.1-0.noarch.rpm | *example_software*-1.0-0.noarch.rpm | *example_software*-1.0-0.noarch.rpm |

After completing development on the patch, you promote the package to the Testing environment so the Quality Engineering team can review the patch. The application lifecycle then contains the following package versions in each environment:

| Development | Testing | Production |
| --- | --- | --- |
| *example_software*-1.1-0.noarch.rpm | ***example_software*-1.1-0.noarch.rpm** | *example_software*-1.0-0.noarch.rpm |

While the Quality Engineering team reviews the patch, the Development team starts work on *example_software* 2.0. This results in the following application lifecycle:

| Development | Testing | Production |
| --- | --- | --- |
| ***example_software*-2.0-0.noarch.rpm** | *example_software*-1.1-0.noarch.rpm | *example_software*-1.0-0.noarch.rpm |

The Quality Engineering team completes their review of the patch. Now *example_software* 1.1 is ready to release. You promote 1.1 to the *Production* environment:

| Development | Testing | Production |
| --- | --- | --- |
| *example_software*-2.0-0.noarch.rpm | *example_software*-1.1-0.noarch.rpm | ***example_software*-1.1-0.noarch.rpm** |

The Development team completes their work on *example_software* 2.0 and promotes it to the Testing environment:

| Development | Testing | Production |
| --- | --- | --- |
| *example_software*-2.0-0.noarch.rpm | ***example_software*-2.0-0.noarch.rpm** | *example_software*-1.1-0.noarch.rpm |

Finally, the Quality Engineering team reviews the package. After a successful review, promote the package to the *Production* environment:

| Development | Testing | Production |
| --- | --- | --- |
| *example_software*-2.0-0.noarch.rpm | *example_software*-2.0-0.noarch.rpm | ***example_software*-2.0-0.noarch.rpm** |

**Additional resources**

- [Section 9.2.10, “Promoting a content view by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#promoting-a-content-view-by-using-web-ui "9.2.10. Promoting a content view by using Satellite web UI")

## 8.3. Best practices for lifecycle environments

Design lifecycle environment paths, plan promotions, and configure Capsule Server content synchronization for predictable staging from development to production.

- Use multiple lifecycle environment paths to implement multiple sequential stages of content consumption. Each stage contains a defined set of content, for example in the *Production* lifecycle environment.
- Automate the creation of lifecycle environments by using a Hammer script or an [Ansible Playbook](https://theforeman.github.io/foreman-ansible-modules/develop/index.html).
- Default use case: Fixed stages in each lifecycle environment paths, for example *Development*, *Test*, and *Production*.

  - Promote content views to lifecycle environments, for example, from *Test* to *Production*. All hosts consuming this content view or composite content view are able to install packages from the *Production* lifecycle environment. Note that these packages are not installed or updated automatically.
  - If you encounter errors during patching hosts, attach the host to a previous version of the content view. This only affects the availability of packages but does not downgrade installed packages.
- Alternative use case: Using stages in lifecycle environments for fixed content, for example, quarterly updates, and only publishing new minor versions with incremental updates from errata.

  - When patching hosts, change the lifecycle environment from `2023-Q4` to `2024-Q1` using the Satellite web UI, Satellite API, Hammer CLI, or an activation key.
  - Advantage: You can directly see which software packages a hosts receives by looking at its lifecycle environment.
  - Disadvantage: Promoting content is less dynamic without clearly defined stages such as *Development*, *Test*, and *Production*.
- Use multiple lifecycle environment paths to define multiple stages for different environments, for example to decouple web server and database hosts.
- Capsule Servers use lifecycle environments to synchronize content. They synchronize content more efficiently if you split content into multiple lifecycle environment paths. If a specific Capsule Server only serves content for one operating system in a single lifecycle environment path, it only synchronizes required content.

## 8.4. Creating a lifecycle environment path by using Satellite web UI

Create a lifecycle environment path starting from the *Library* environment to stage content from development through release. Optionally chain additional environments for testing, beta, or production stages.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Lifecycle Environments**.
2. Click **New Environment Path** to start a new application lifecycle.
3. In the **Name** field, enter a name for your environment.
4. In the **Description** field, enter a description for your environment.
5. Click **Save**.
6. Optional: To add an environment to the environment path, click **Add New Environment**, complete the **Name** and **Description** fields, and select the prior environment from the **Prior Environment** list.

## 8.5. Creating a lifecycle environment path by using Hammer CLI

Create a lifecycle environment path starting from the *Library* environment to stage content from development through release. Optionally chain additional environments for testing, beta, or production stages.

**Procedure**

1. Create a lifecycle environment path by tying your first environment to Library:

   ```
   $ hammer lifecycle-environment create \
   --name "My First Lifecycle Environment" \
   --description "Environment Path Description" \
   --prior "Library" \
   --organization "My_Organization"
   ```
2. Optional: Add another environment to the environment path by tying it to the prior environment:

   ```
   $ hammer lifecycle-environment create \
   --name "My Second Lifecycle Environment" \
   --description "Environment Description" \
   --prior "My First Lifecycle Environment" \
   --organization "My_Organization"
   ```
3. View the chain of the lifecycle environment path:

   ```
   $ hammer lifecycle-environment paths --organization "My_Organization"
   ```

## 8.6. Adding lifecycle environments to Capsule Servers by using Satellite web UI

To distribute content through content-enabled Capsule Server, add lifecycle environments to your Capsule Server. Capsule Server synchronizes the right repositories from Satellite Server and provides that content to hosts.

Do not assign the *Library* lifecycle environment to your Capsule Server because it triggers an automated Capsule sync every time the CDN updates a repository. This might consume multiple system resources on Capsules, network bandwidth between Satellite and Capsules, and available disk space on Capsules.

You can add an environment from the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
2. Select your Capsule Server that you want to add a lifecycle to.
3. Click **Edit** and click the **Lifecycle Environments** tab.
4. From the left menu, select the lifecycle environments that you want to add to your Capsule Server and click **Submit**.
5. To synchronize the content to your Capsule Server, click the **Overview** tab and click **Synchronize**.
6. Select either **Optimized Sync** or **Complete Sync**.

   For definitions of each synchronization type, see [Advanced synchronization options](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#advanced-synchronization-options).

## 8.7. Adding lifecycle environments to Capsule Servers by using Hammer CLI

To distribute content through content-enabled Capsule Server, add lifecycle environments to your Capsule Server. Capsule Server synchronizes the right repositories from Satellite Server and provides that content to hosts.

Do not assign the *Library* lifecycle environment to your Capsule Server because it triggers an automated Capsule sync every time the CDN updates a repository. This might consume multiple system resources on Capsules, network bandwidth between Satellite and Capsules, and available disk space on Capsules.

You can add an environment by using Hammer CLI.

**Procedure**

1. To display a list of all Capsule Servers, on Satellite Server, enter the following command:

   ```
   $ hammer capsule list
   ```

   Note the Capsule ID of the Capsule to which you want to add a lifecycle.
2. Using the ID, verify the details of your Capsule:

   ```
   $ hammer capsule info \
   --id My_Capsule_ID
   ```
3. To view the lifecycle environments available for your Capsule Server, enter the following command and note the ID and the organization name:

   ```
   $ hammer capsule content available-lifecycle-environments \
   --id My_Capsule_ID
   ```
4. Add the lifecycle environment to your Capsule Server:

   ```
   $ hammer capsule content add-lifecycle-environment \
   --id My_Capsule_ID \
   --lifecycle-environment-id My_Lifecycle_Environment_ID \
   --organization "My_Organization"
   ```

   Repeat for each lifecycle environment you want to add to Capsule Server.
5. Synchronize the content from Satellite to Capsule.

   - To synchronize all content from your Satellite Server environment to Capsule Server, enter the following command:

     ```
     $ hammer capsule content synchronize \
     --id My_Capsule_ID
     ```
   - To synchronize a specific lifecycle environment from your Satellite Server to Capsule Server, enter the following command:

     ```
     $ hammer capsule content synchronize \
     --id My_Capsule_ID \
     --lifecycle-environment-id My_Lifecycle_Environment_ID
     ```
   - To synchronize all content from your Satellite Server to your Capsule Server without checking metadata:

     ```
     $ hammer capsule content synchronize \
     --id My_Capsule_ID \
     --skip-metadata-check true
     ```

     This equals selecting **Complete Sync** in the Satellite web UI.

## 8.8. Removing lifecycle environments from Satellite Server by using Satellite web UI

Remove a lifecycle environment from Satellite Server when it is empty and no longer needed so your content paths stay accurate and easier to manage.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle Environments**.
2. Click the name of the lifecycle environment that you want to remove, and then click **Remove Environment**.
3. Click **Remove** to remove the environment.

## 8.9. Removing lifecycle environments from Satellite Server by using Hammer CLI

Remove a lifecycle environment from Satellite Server when it is empty and no longer needed so your content paths stay accurate and easier to manage.

**Procedure**

1. List the lifecycle environments for your organization and note the name of the lifecycle environment you want to remove:

   ```
   $ hammer lifecycle-environment list \
   --organization "My_Organization"
   ```
2. Use the `hammer lifecycle-environment delete` command to remove an environment:

   ```
   $ hammer lifecycle-environment delete \
   --name "My_Environment" \
   --organization "My_Organization"
   ```

## 8.10. Removing lifecycle environments from Capsule Server by using Satellite web UI

Remove lifecycle environments from Capsule Server when they are obsolete or were added incorrectly, then resynchronize. That way, your Capsule Server only stores content your hosts still need.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
2. Select the Capsule Server that you want to remove a lifecycle from.
3. Click **Edit** and click the **Lifecycle Environments** tab.
4. From the right menu, select the lifecycle environments that you want to remove from Capsule Server, and then click **Submit**.
5. To synchronize content to your Capsule Server, click the **Overview** tab, and then click **Synchronize**.
6. Select either **Optimized Sync** or **Complete Sync**.

## 8.11. Removing lifecycle environments from Capsule Server by using Hammer CLI

Remove lifecycle environments from Capsule Server when they are obsolete or were added incorrectly, then resynchronize. That way, your Capsule Server only stores content your hosts still need.

**Procedure**

1. Get a list of Capsules:

   ```
   # hammer capsule list
   ```

   Note down the ID of your Capsule Server.
2. Optional: Verify the details of your Capsule Server:

   ```
   # hammer capsule info \
   --id My_Capsule_Server_ID
   ```
3. Optional: Verify the list of lifecycle environments currently attached to Capsule Server:

   ```
   # hammer capsule content lifecycle-environments \
   --id My_Capsule_Server_ID
   ```

   Note down the Environment ID.
4. Remove the lifecycle environment from Capsule Server:

   ```
   # hammer capsule content remove-lifecycle-environment \
   --id My_Capsule_Server_ID \
   --lifecycle-environment-id My_Lifecycle_Environment_ID
   ```

   Repeat this step for every lifecycle environment that you want to remove from Capsule Server.
5. Synchronize the content from Satellite Server to Capsule Server:

   ```
   # hammer capsule content synchronize \
   --id My_Capsule_Server_ID
   ```
