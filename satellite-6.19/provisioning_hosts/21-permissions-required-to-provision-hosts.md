---
title: "Permissions required to provision hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "D"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#permissions-required-to-provision-hosts"
---
# Appendix D. Permissions required to provision hosts

Grant these permissions to enable users to provision hosts without full administrator access.

| Resource name | Permissions | Additional details |
| --- | --- | --- |
| Activation Keys | `view_activation_keys` |  |
| Ansible role | `view_ansible_roles` | Required if Ansible is used. |
| Architecture | `view_architectures` |  |
| Compute profile | `view_compute_profiles` |  |
| Compute resource | `view_compute_resources`, `create_compute_resources`, `destroy_compute_resources`, `power_compute_resources` | Required to provision bare-metal hosts. |
| `view_compute_resources_vms`, `create_compute_resources_vms`, `destroy_compute_resources_vms`, `power_compute_resources_vms` | Required to provision virtual machines. |
| Content Views | `view_content_views` |  |
| Domain | `view_domains` |  |
| Environment | `view_environments` |  |
| Host | `view_hosts`, `create_hosts`, `edit_hosts`, `destroy_hosts`, `build_hosts`, `power_hosts`, `play_roles_on_host` |  |
| `view_discovered_hosts`, `submit_discovered_hosts`, `auto_provision_discovered_hosts`, `provision_discovered_hosts`, `edit_discovered_hosts`, `destroy_discovered_hosts` | Required if the Discovery service is enabled. |
| Hostgroup | `view_hostgroups`, `create_hostgroups`, `edit_hostgroups`, `play_roles_on_hostgroup` |  |
| Image | `view_images` |  |
| Lifecycle environment | `view_lifecycle_environments` |  |
| Location | `view_locations` |  |
| `assign_locations` | Required to assign locations to hosts or other resources. You can only assign locations that you belong to. |
| Medium | `view_media` |  |
| Operatingsystem | `view_operatingsystems` |  |
| Organization | `view_organizations` |  |
| `assign_organizations` | Required to assign organizations to hosts or other resources. You can only assign organizations that you belong to. |
| Parameter | `view_params`, `create_params`, `edit_params`, `destroy_params` |  |
| Product and Repositories | `view_products` |  |
| Provisioning template | `view_provisioning_templates` |  |
| Ptable | `view_ptables` |  |
| Capsule | `view_smart_proxies`, `view_smart_proxies_puppetca` |  |
| `view_openscap_proxies` | Required if the OpenSCAP plugin is enabled. |
| Subnet | `view_subnets` |  |

**Additional resources**

- [Creating a role by using Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#creating-a-role-by-using-web-ui)
- [Adding permissions to a role by using Satellite web UI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#adding-permissions-to-a-role-by-using-web-ui)
- [Assigning roles to a user by using Hammer CLI in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#assigning-roles-to-a-user-by-using-cli)
