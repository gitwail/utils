---
title: "Creating a playbook with modules from Satellite Ansible Collection"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_ansible_collection"
guide_title: "Using the Satellite Ansible Collection"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#creating-a-playbook-with-modules-from-satellite-ansible-collection"
---
# Chapter 2. Creating a playbook with modules from Satellite Ansible Collection

Ansible modules from the Satellite Ansible Collection must be able to communicate with the Satellite API over HTTPS. In your playbooks, include parameters specifying how to authenticate to enable the connection to API.

> **Important**
>
> Do not store sensitive credentials, such as username and password, directly in your playbooks or environment variables. The following examples use Ansible vault to manage sensitive data.

**Prerequisites**

- A user account in Satellite exists with permissions to perform the action defined in your playbook.
- You have access to one of the following types of authentication credentials for that user:

  - Username and password
  - Username and Personal Access Token
  - Kerberos ticket, if your Satellite Server is configured to use Identity Management as an external authentication source
- A system that you will execute your playbook against. The following examples use `localhost`.

  This system must be able to reach the Satellite API. You can choose from these options:

  - A system that can reach the Satellite API directly. You can use your Satellite Server, your Capsule Servers, or any other system in your environment.
  - A system without a direct connection to the Satellite API that uses an HTTP proxy to connect to Satellite.

**Procedure**

1. Store your sensitive variables in an encrypted file:

   1. Create an Ansible vault. For example, to create a vault named *My_Vault.yml*:

      ```
      $ ansible-vault create My_Vault.yml
      ```
   2. After the `ansible-vault create` command opens an editor, provide the required parameters in the *key*: *value* format.

      If you want to authenticate with Satellite username and password:

      ```
      My_Username: My_Admin_User_Account
      My_Password: My_Admin_Password
      My_Server_URL: https://satellite.example.com
      ```

      If you want to authenticate with Satellite username and Personal Access Token (PAT):

      ```
      My_Username: My_Admin_User_Account
      My_Password: My_PAT
      My_Server_URL: https://satellite.example.com
      ```

      If you want to authenticate with a Kerberos ticket:

      ```
      My_Server_URL: https://satellite.example.com
      ```
   3. If you use an HTTP proxy to reach the Satellite API, store it in the vault too:

      ```
      My_HTTP_Proxy: "http://proxy.example.com:8080"
      ```
   4. Save your changes and close the editor. Ansible encrypts the data in the vault.
2. Create a playbook file that references the vault file:

   > **Note**
   >
   > The following YAML snippets include the `module_defaults` keyword to pass vault variables as parameters to all modules from the redhat.satellite.satellite group that are used in the playbook. Module defaults groups simplify parameter management by enabling you to define common parameters to groups of modules rather than having to pass the parameters to each module individually.

   1. Provide details on how to authenticate to the Satellite API.

      If you are authenticating with Satellite username and password or PAT, map the `username`, `password`, and `server_url` parameters to the contents of *My_Vault.yml*:

      ```yaml
      - name: My Playbook
        hosts: localhost
        vars_files:
          - My_Vault.yml
        module_defaults:
          group/redhat.satellite.satellite:
            username: "{{ My_Username }}"
            password: "{{ My_Password }}"
            server_url: "{{ My_Server_URL }}"
        tasks:
      ```

      If you are authenticating with a Kerberos ticket, map the `server_url` parameter to the contents of *My_Vault.yml* and add `use_gssapi: true` to enable Kerberos authentication:

      ```yaml
      - name: My Playbook
        hosts: localhost
        vars_files:
          - My_Vault.yml
        module_defaults:
          group/redhat.satellite.satellite:
            server_url: "{{ My_Server_URL }}"
            use_gssapi: true
        tasks:
      ```
   2. If you need to use an HTTP proxy to reach the Satellite API, set the `https_proxy` environment variable:

      ```yaml
      - name: My Playbook
        hosts: localhost
        vars_files:
          - My_Vault.yml
        environment:
          https_proxy: "{{ My_HTTP_Proxy }}"
        module_defaults:
          group/redhat.satellite.satellite:
            username: "{{ My_Username }}"
            password: "{{ My_Password }}"
            server_url: "{{ My_Server_URL }}"
        tasks:
      ```
   3. In the `tasks:` section, define the tasks that you want your playbook to perform.
3. Validate the playbook syntax:

   ```
   $ ansible-playbook --syntax-check --ask-vault-pass My_Playbook.yml
   ```

   Note that this command only validates the syntax. It does not protect against a valid but incorrect configuration.
4. Run the playbook:

   ```
   $ ansible-playbook --ask-vault-pass My_Playbook.yml
   ```

**Example 2.1. Example Ansible playbook: Ensure that domain `new.example.com` exists in Satellite**

The `redhat.satellite.domain` module can create, update, and delete domains. This example playbook uses `redhat.satellite.domain` to ensure that a domain named `new.example.com` exists and is managed by Satellite. For additional examples, see [Chapter 3, *Example playbooks based on modules from Satellite Ansible Collection*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_ansible_collection/index#example-playbooks-based-on-modules-from-satellite-ansible-collection "Chapter 3. Example playbooks based on modules from Satellite Ansible Collection").

```
- name: Domain management
  hosts: localhost
  vars_files:
    - My_Vault.yml
  module_defaults:
    group/redhat.satellite.satellite:
      username: "{{ My_Username }}"
      password: "{{ My_Password }}"
      server_url: "{{ My_Server_URL }}"
  tasks:
    - name: Ensure domain new.example.com exists
      redhat.satellite.domain:
        name: new.example.com
```

The settings specified in the example playbook include the following:

`vars_files`
:   The name of the vault file that stores the variables `My_Username`, `My_Password`, and `My_Server_URL`.

`module_defaults`
:   The module defaults group that maps the variables from the vault file to the `username`, `password`, and `server_url` module parameters.

`name`
:   The name of the domain that you want to ensure exists in Satellite.

For more information, see the Ansible module documentation with `ansible-doc redhat.satellite.domain`.

**Additional resources**

- [Protecting sensitive data with Ansible vault](https://docs.ansible.com/ansible/latest/vault_guide/index.html)
- [Module defaults](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_module_defaults.html)
