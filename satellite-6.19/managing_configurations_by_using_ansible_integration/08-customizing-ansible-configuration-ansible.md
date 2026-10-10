---
title: "Customizing Ansible configuration"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_ansible_integration"
guide_title: "Managing configurations by using Ansible integration"
chapter_number: "B"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#customizing-ansible-configuration_ansible"
---
# Appendix B. Customizing Ansible configuration

Satellite manages essential Ansible configuration that is required for Ansible integration with Satellite. However, you can customize other Ansible configuration options as usual.

Satellite stores the essential Ansible configuration as environment variables in `/etc/foreman-proxy/ansible.env`. This file is managed by `satellite-installer`.

Ansible reads configuration from a configuration file and the environment provided by Capsule. If you need to customize Ansible configuration, you can do so in the system-wide `/etc/ansible/ansible.cfg` file or in the `/usr/share/foreman-proxy/.ansible.cfg` file in the home directory of the `foreman-proxy` user. Note that if you use `/usr/share/foreman-proxy/.ansible.cfg`, Ansible spawned by Satellite ignores configuration in `/etc/ansible/ansible.cfg`.

Note that environment variables take precedence over values in `ansible.cfg`, which ensures that the essential configuration required by Satellite is retained.

The following table lists the essential Ansible configuration options managed by Satellite.

Table B.1. Essential Ansible configuration

| Environment Variable | Config Key | Description |
| --- | --- | --- |
| ANSIBLE_CALLBACKS_ENABLED | callbacks_enabled | Enables callback to Satellite; equivalent to `callback_whitelist` for cross-version compatibility |
| ANSIBLE_CALLBACK_WHITELIST | callback_whitelist | Enables callback to Satellite; equivalent to `callbacks_enabled` for cross-version compatibility |
| ANSIBLE_COLLECTIONS_PATHS | collections_paths | List of paths to Ansible collections |
| ANSIBLE_HOST_KEY_CHECKING | host_key_checking | Disables checking of host keys during SSH connection |
| ANSIBLE_LOCAL_TEMP | local_tmp | Temporary directory on Capsule |
| ANSIBLE_ROLES_PATH | roles_path | List of paths to Ansible roles |
| ANSIBLE_SSH_ARGS | ssh_args | Arguments passed to SSH connection |

**Additional resources**

- [Ansible Configuration Settings](https://docs.ansible.com/ansible/latest/reference_appendices/config.html)
