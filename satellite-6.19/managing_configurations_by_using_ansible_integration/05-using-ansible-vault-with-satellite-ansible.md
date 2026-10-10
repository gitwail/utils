---
title: "Using Ansible Vault with Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_ansible_integration"
guide_title: "Managing configurations by using Ansible integration"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#using-ansible-vault-with-satellite_ansible"
---
# Chapter 5. Using Ansible Vault with Satellite

You can encrypt sensitive Ansible data files using the Ansible Vault tool and configure Ansible to access the encrypted files using a password stored in a file.

**Procedure**

1. If you customized `/etc/ansible/ansible.cfg`, copy your configuration from `/etc/ansible/ansible.cfg` to `/usr/share/foreman-proxy/.ansible.cfg`.
2. Encrypt the sensitive file using the `ansible-vault` command:

   ```
   # ansible-vault encrypt /etc/ansible/roles/Role_Name/vars/main.yml
   ```

   Note that `ansible-vault` changes the file permissions to `600`.
3. Change the group and permissions of the encrypted file to ensure that the `foreman-proxy` user can read it:

   ```
   # chgrp foreman-proxy /etc/ansible/roles/Role_Name/vars/main.yml
   # chmod 0640 /etc/ansible/roles/Role_Name/vars/main.yml
   ```
4. Create the `/usr/share/foreman-proxy/.ansible_vault_password` file and enter the Vault password into it.
5. Change the user and permissions of the `.ansible_vault_password` file to ensure that only the `foreman-proxy` user can read it:

   ```
   # chown foreman-proxy:foreman-proxy /usr/share/foreman-proxy/.ansible_vault_password
   # chmod 0400 /usr/share/foreman-proxy/.ansible_vault_password
   ```
6. Add the path of the Vault password file to the `[defaults]` section in `/usr/share/foreman-proxy/.ansible.cfg`:

   ```
   [defaults]
   vault_password_file = /usr/share/foreman-proxy/.ansible_vault_password
   ```

   The path to the Vault password file must be absolute.
