---
title: "Synchronizing template repositories"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "17"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#synchronizing-template-repositories"
---
# Chapter 17. Synchronizing template repositories

You can synchronize repositories of job templates, provisioning templates, report templates, and partition table templates between Satellite Server and a version control system or local directory. You can use the Template Sync plugin to export and import templates.

## 17.1. Synchronizing templates with an existing repository

If you store templates in a repository under a version control system, you can synchronize the templates between your Satellite Server and the repository.

In this procedure, a Git repository is used for demonstration purposes.

**Procedure**

1. If you want to use HTTPS to connect to the repository and you use a self-signed certificate authority (CA) on your Git server:

   1. Create a new directory under the `/usr/share/foreman/` directory to store the Git configuration for the certificate:

      ```
      # mkdir --parents /usr/share/foreman/.config/git
      ```
   2. Create a file named `config` in the new directory:

      ```
      # touch /usr/share/foreman/.config/git/config
      ```
   3. Allow the `foreman` user access to the `.config` directory:

      ```
      # chown --recursive foreman /usr/share/foreman/.config
      ```
   4. Update the Git global configuration for the `foreman` user with the path to your self-signed CA certificate:

      ```
      # sudo --user foreman git config --global http.sslCAPath Path_To_CA_Certificate
      ```
2. If you want to use SSH to connect to the repository:

   1. Create an SSH key pair if you do not already have it. Do not specify a passphrase.

      ```
      # sudo --user foreman ssh-keygen
      ```
   2. Configure your version control server with the public key from your Satellite, which resides in `/usr/share/foreman/.ssh/id_rsa.pub`.
   3. Accept the Git SSH host key as the `foreman` user:

      ```
      # sudo --user foreman ssh git.example.com
      ```
3. In the Satellite web UI, provide details for your Git repository:

   1. Navigate to **Administer** > **Settings**.
   2. Click the **Template Sync** tab.
   3. Change the **Branch** setting to define the target branch of the repository.
   4. Change the **Repo** setting to define the repository URL.
   5. If you want to use an HTTP proxy to connect to the repository, change the **HTTP proxy policy** setting to `Global default HTTP proxy` or `Custom HTTP proxy`.

**Next steps**

- Import templates from your repository or export templates to your repository.

## 17.2. Synchronizing templates with a local directory

If you store templates in a local directory that is tracked under a version control system, you can synchronize the templates between your Satellite Server and the local directory.

**Prerequisites**

- Each template must contain the location and organization that the template belongs to. This applies to all template types. Before you import a template, ensure that you add the following section to the template:

  ```
  <%#
  kind: provision
  name: My_Provisioning_Template
  oses:
  - My_first_Operating_System
  - My_second_Operating_System
  locations:
  - My_first_Location
  - My_second_Location
  organizations:
  - My_first_Organization
  - My_second_Organization
  %>
  ```

**Procedure**

1. On your Satellite Server, in `/var/lib/foreman`, create a directory for storing templates:

   ```
   # mkdir /var/lib/foreman/My_Templates_Dir
   ```

   > **Note**
   >
   > You can place your templates to a custom directory outside `/var/lib/foreman`, but you have to ensure that the `Foreman` service can read its contents. The directory must have the correct file permissions and the `foreman_lib_t` SELinux label.
2. Change the owner of the new templates directory to the `foreman` user:

   ```
   # chown foreman /var/lib/foreman/My_Templates_Dir
   ```
3. Change the **Repo** setting on the **Template Sync** tab to match the `/var/lib/foreman/My_Templates_Dir/` directory.

## 17.3. Importing templates by using Satellite web UI

You can import templates from a repository of your choice from the Satellite web UI. You can use different protocols to point to your repository, for example `/tmp/dir`, `git://example.com`, `https://example.com`, and `ssh://example.com`.

> **Note**
>
> The templates provided by Satellite are locked and you cannot import them by default. To overwrite this behavior, change the `Force import` setting in the **Template Sync** menu to `yes` or add the `force` parameter `-d '{ "force": "true" }'` to the import command.

**Prerequisites**

- Each template must contain the location and organization that the template belongs to. This applies to all template types.
- Before you import a template, ensure that you add the following section to the template:

  ```
  <%#
  kind: provision
  name: My_Provisioning_Template
  oses:
  - My_first_Operating_System
  - My_second_Operating_System
  locations:
  - My_first_Location
  - My_second_Location
  organizations:
  - My_first_Organization
  - My_second_Organization
  %>
  ```

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Sync Templates**.
2. Click **Import**.
3. Each field is populated with values configured in **Administer** > **Settings** > **Template Sync**. Change the values as required for the templates you want to import. For more information about each field, see [Section F.3, “Template sync settings”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#template_sync_settings_admin "F.3. Template sync settings").
4. Click **Submit**.

   The Satellite web UI displays the status of the import. The status is not persistent; if you leave the status page, you cannot return to it.

## 17.4. Importing templates by using Hammer CLI

You can import templates from a repository of your choice by using Hammer CLI. You can use different protocols to point to your repository, for example `/tmp/dir`, `git://example.com`, `https://example.com`, and `ssh://example.com`.

> **Note**
>
> The templates provided by Satellite are locked and you cannot import them by default. To overwrite this behavior, change the `Force import` setting in the **Template Sync** menu to `yes` or add the `force` parameter `-d '{ "force": "true" }'` to the import command.

**Prerequisites**

- Each template must contain the location and organization that the template belongs to. This applies to all template types.
- Before you import a template, ensure that you add the following section to the template:

  ```
  <%#
  kind: provision
  name: My_Provisioning_Template
  oses:
  - My_first_Operating_System
  - My_second_Operating_System
  locations:
  - My_first_Location
  - My_second_Location
  organizations:
  - My_first_Organization
  - My_second_Organization
  %>
  ```

**Procedure**

- Import a template from a repository:

  ```
  $ hammer import-templates \
  --branch "My_Branch" \
  --filter '.*Template Name$' \
  --organization "My_Organization" \
  --prefix "[Custom Index] " \
  --repo "https://git.example.com/path/to/repository"
  ```

  For better indexing and management of your templates, use `--prefix` to set a category for your templates. To select certain templates from a large repository, use `--filter` to define the title of the templates that you want to import. For example `--filter '.*Ansible Default$'` imports various Ansible Default templates.

## 17.5. Importing templates by using Satellite API

You can import templates from a repository of your choice by using Satellite API. You can use different protocols to point to your repository, for example `/tmp/dir`, `git://example.com`, `https://example.com`, and `ssh://example.com`.

> **Note**
>
> The templates provided by Satellite are locked and you cannot import them by default. To overwrite this behavior, change the `Force import` setting in the **Template Sync** menu to `yes` or add the `force` parameter `-d '{ "force": "true" }'` to the import command.

**Prerequisites**

- Each template must contain the location and organization that the template belongs to. This applies to all template types.
- Before you import a template, ensure that you add the following section to the template:

  ```
  <%#
  kind: provision
  name: My_Provisioning_Template
  oses:
  - My_first_Operating_System
  - My_second_Operating_System
  locations:
  - My_first_Location
  - My_second_Location
  organizations:
  - My_first_Organization
  - My_second_Organization
  %>
  ```

**Procedure**

- Send a `POST` request to `api/v2/templates/import`:

  ```
  $ curl \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request POST \
  --user "My_User_Name:My_Password" \
  https://satellite.example.com/api/v2/templates/import
  ```

  If the import is successful, you receive `{"message":"Success"}`.

## 17.6. Importing templates using Ansible

You can import templates from a repository of your choice. You can use different protocols to point to your repository, for example `/tmp/dir`, `git://example.com`, `https://example.com`, and `ssh://example.com`.

**Procedure**

- Use the `redhat.satellite.templates_import` module.

**Additional resources**

- [redhat.satellite.templates_import module – Sync Templates from a repository](https://console.redhat.com/ansible/automation-hub/repo/published/redhat/satellite/content/module/templates_import/)

## 17.7. Exporting templates by using Satellite web UI

You can export templates to an existing repository from the Satellite web UI. This is useful for backing up customized templates and keeping them synchronized with your version control system.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Templates** > **Sync Templates**.
2. Click **Export**.
3. Each field is populated with values configured in **Administer** > **Settings** > **Template Sync**. Change the values as required for the templates you want to export. For more information about each field, see [Section F.3, “Template sync settings”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#template_sync_settings_admin "F.3. Template sync settings").
4. Click **Submit**.

   The Satellite web UI displays the status of the export. The status is not persistent; if you leave the status page, you cannot return to it.

## 17.8. Exporting templates by using Hammer CLI

You can export templates to an existing repository by using Hammer CLI. This is useful for backing up customized templates and keeping them synchronized with your version control system.

**Procedure**

- Export all templates to a repository:

  ```
  $ hammer export-templates \
  --organization "My_Organization" \
  --repo "https://git.example.com/path/to/repository"
  ```

  > **Note**
  >
  > This command clones the repository, makes changes in a commit, and pushes back to the repository. You can use the `--branch "My_Branch"` option to export the templates to a specific branch.

## 17.9. Exporting templates by using Satellite API

You can export templates to an existing repository by using Satellite API. This is useful for backing up customized templates and keeping them synchronized with your version control system.

**Procedure**

1. Send a `POST` request to `api/v2/templates/export`:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request POST \
   --user "My_User_Name:My_Password" \
   https://satellite.example.com/api/v2/templates/export
   ```

   If the export is successful, you receive `{"message":"Success"}`.

   > **Note**
   >
   > You can override default API settings by specifying them in the request with the `-d` parameter. The following example exports templates to the `git.example.com/templates` repository:
   >
   > ```
   > $ curl \
   > --data "{\"repo\":\"git.example.com/templates\"}" \
   > --header "Accept: application/json" \
   > --header "Content-Type: application/json" \
   > --request POST \
   > --user "My_User_Name:My_Password" \
   > https://satellite.example.com/api/v2/templates/export
   > ```
