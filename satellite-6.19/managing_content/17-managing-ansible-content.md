---
title: "Managing Ansible content"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "17"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-ansible-content"
---
# Chapter 17. Managing Ansible content

Managing Ansible content in Satellite includes importing Ansible collections from different sources, synchronizing them, and distributing them to your hosts. This enables maintaining consistent automation across your infrastructure.

**Additional resources**

- [Managing configurations by using Ansible integration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#)

## 17.1. Synchronizing Ansible Collections

On Satellite, you can synchronize your Ansible Collections from Private Automation Hub, `console.redhat.com`, and other Satellite instances to centrally manage and distribute automation content across your infrastructure. Ansible Collections will appear on Satellite as a new repository type in the Satellite web UI menu under **Content** after the sync.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select the required product name.
3. In the **Products** window, select the name of a product that you want to create a repository for.
4. Click the **Repositories** tab, and then click **New Repository**.
5. In the **Name** field, enter a name for the repository.

   The **Label** field is populated automatically based on the name.
6. From the **Type** list, select **ansible collection**.
7. In the **Upstream URL** field, enter the URL for the upstream collections repository.

   The URL can be any Ansible Galaxy endpoint. For example, `https://console.redhat.com/api/automation-hub/`.
8. Optional: In the **Requirements.yml** field, you can specify the list of collections you want to sync from the endpoint and their versions.

   If you do not specify a list of collections, Satellite synchronizes all Ansible collections from the endpoint.

   ```yaml
   ---
   collections:
   - name: my_namespace.my_collection
     version: 1.2.3
   ```

   For more information, see [Installing roles and collections from the same requirements.yml file](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-roles-and-collections-from-the-same-requirements-yml-file) in the *Galaxy User Guide*.
9. Optional: Deselect **Sync Dependencies** if you do not want Satellite to resolve and synchronize dependencies. By default, Satellite synchronizes all required dependencies.
10. Authenticate:

    - To sync Ansible collections from **Private Automation Hub**:

      1. Navigate to [Connect to Hub](https://console.redhat.com/ansible/automation-hub/token). Click **Load token**.
      2. Enter the token in the **Auth Token** field in the Satellite web UI.
    - To sync Ansible collections from `console.redhat.com`:

      1. Navigate to [Connect to Hub](https://console.redhat.com/ansible/automation-hub/token). Click **Load token**.
      2. Enter the authentication token in the **Auth Token** field in the Satellite web UI.
      3. Copy the SSO URL from the SSO URL section.
      4. Enter the SSO URL in the **Auth URL** field in the Satellite web UI.
    - To sync Ansible collections from Satellite, leave both authentication fields blank.
11. Click **Save**.
12. Navigate to the Ansible Collections repository.
13. From the **Select Action** menu, select **Sync Now**.

**Additional resources**

- [Connect to Hub](https://console.redhat.com/ansible/automation-hub/token)

## 17.2. Consuming content from an Ansible Collection repository

Configure hosts to consume content from an Ansible Collection repository on Satellite Server or Capsule Server to ensure consistent automation content across your infrastructure. You can configure the Ansible Galaxy client to use your Satellite Server or Capsule Server as a Galaxy server.

**Prerequisites**

- You have synchronized an Ansible Collection to a Satellite repository.
- The `ansible-core` package is installed on the host. This package is available in AppStream repositories.

**Procedure**

1. On the host, configure the `ansible-galaxy` client to use Satellite Server or Capsule Server as the Galaxy server. Add the required sections to an `ansible.cfg` file, for example:

   ```
   [galaxy]
   server_list = My_Library_Server, My_Promoted_CV_Server

   [galaxy_server.My_Library_Server]
   url = https://server.example.com/pulp_ansible/galaxy/My_Organization_Label/Library/custom/My_Product_Label/My_Repository_Label/api/

   [galaxy_server.My_Promoted_CV_Server]
   url = https://server.example.com/pulp_ansible/galaxy/My_Organization_Label/My_Lifecycle_Environment_Label/My_Content_View_Label/custom/My_Product_Label/My_Repository_Label/api/
   ```

   Replace `server.example.com` with the fully qualified domain name of your Satellite Server or Capsule Server.
2. Install an Ansible Collection from your Galaxy server. For example:

   ```
   # ansible-galaxy collection install My_Namespace.My_Collection \
   --server My_Library_Server
   ```

**Additional resources**

- [Configuring the ansible-galaxy client in the *Ansible Collections Guide*](https://docs.ansible.com/projects/ansible/latest/collections_guide/collections_installing.html#configuring-the-ansible-galaxy-client)
- [The configuration file in the *Ansible Reference Appendix*](https://docs.ansible.com/projects/ansible/latest/reference_appendices/config.html#the-configuration-file)
