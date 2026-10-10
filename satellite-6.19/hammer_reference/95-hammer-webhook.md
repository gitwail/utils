---
title: "webhook"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "95"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-webhook"
---
# Chapter 95. webhook

Manage webhooks

**Usage**

```
# hammer webhook [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 95.1. webhook create

Create a Webhook

**Usage**

```
# hammer webhook create [OPTIONS]
```

**Options**

- `--enabled BOOLEAN`
- `--event ENUM` – Possible value(s): `actions.katello.capsule_content.sync_failed`, `actions.katello.capsule_content.sync_succeeded`, `actions.katello.content_view.promote_failed`, `actions.katello.content_view.promote_succeeded`, `actions.katello.content_view.publish_failed`, `actions.katello.content_view.publish_succeeded`, `actions.katello.repository.sync_failed`, `actions.katello.repository.sync_succeeded`, `actions.remote_execution.run_host_job_ansible_configure_cloud_connector_failed`, `actions.remote_execution.run_host_job_ansible_configure_cloud_connector_succeeded`, `actions.remote_execution.run_host_job_ansible_enable_web_console_failed`, `actions.remote_execution.run_host_job_ansible_enable_web_console_succeeded`, `actions.remote_execution.run_host_job_ansible_run_capsule_update_failed`, `actions.remote_execution.run_host_job_ansible_run_capsule_update_succeeded`, `actions.remote_execution.run_host_job_ansible_run_capsule_upgrade_failed`, `actions.remote_execution.run_host_job_ansible_run_capsule_upgrade_succeeded`, `actions.remote_execution.run_host_job_ansible_run_host_failed`, `actions.remote_execution.run_host_job_ansible_run_host_succeeded`, `actions.remote_execution.run_host_job_ansible_run_openscap_remediation_failed`, `actions.remote_execution.run_host_job_ansible_run_openscap_remediation_succeeded`, `actions.remote_execution.run_host_job_ansible_run_playbook_failed`, `actions.remote_execution.run_host_job_ansible_run_playbook_succeeded`, `actions.remote_execution.run_host_job_failed`, `actions.remote_execution.run_host_job_foreman_openscap_run_scans_failed`, `actions.remote_execution.run_host_job_foreman_openscap_run_scans_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_action_failed`, `actions.remote_execution.run_host_job_katello_bootc_action_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_rollback_failed`, `actions.remote_execution.run_host_job_katello_bootc_rollback_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_status_failed`, `actions.remote_execution.run_host_job_katello_bootc_status_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_switch_failed`, `actions.remote_execution.run_host_job_katello_bootc_switch_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_upgrade_failed`, `actions.remote_execution.run_host_job_katello_bootc_upgrade_succeeded`, `actions.remote_execution.run_host_job_katello_change_content_source_failed`, `actions.remote_execution.run_host_job_katello_change_content_source_succeeded`, `actions.remote_execution.run_host_job_katello_errata_install_by_search_failed`, `actions.remote_execution.run_host_job_katello_errata_install_by_search_succeeded`, `actions.remote_execution.run_host_job_katello_errata_install_failed`, `actions.remote_execution.run_host_job_katello_errata_install_succeeded`, `actions.remote_execution.run_host_job_katello_group_install_failed`, `actions.remote_execution.run_host_job_katello_group_install_succeeded`, `actions.remote_execution.run_host_job_katello_group_remove_failed`, `actions.remote_execution.run_host_job_katello_group_remove_succeeded`, `actions.remote_execution.run_host_job_katello_group_update_failed`, `actions.remote_execution.run_host_job_katello_group_update_succeeded`, `actions.remote_execution.run_host_job_katello_host_tracer_resolve_failed`, `actions.remote_execution.run_host_job_katello_host_tracer_resolve_succeeded`, `actions.remote_execution.run_host_job_katello_module_stream_action_failed`, `actions.remote_execution.run_host_job_katello_module_stream_action_succeeded`, `actions.remote_execution.run_host_job_katello_package_install_by_search_failed`, `actions.remote_execution.run_host_job_katello_package_install_by_search_succeeded`, `actions.remote_execution.run_host_job_katello_package_install_failed`, `actions.remote_execution.run_host_job_katello_package_install_succeeded`, `actions.remote_execution.run_host_job_katello_package_remove_failed`, `actions.remote_execution.run_host_job_katello_package_remove_succeeded`, `actions.remote_execution.run_host_job_katello_package_update_failed`, `actions.remote_execution.run_host_job_katello_package_update_succeeded`, `actions.remote_execution.run_host_job_katello_packages_remove_by_search_failed`, `actions.remote_execution.run_host_job_katello_packages_remove_by_search_succeeded`, `actions.remote_execution.run_host_job_katello_packages_update_by_search_failed`, `actions.remote_execution.run_host_job_katello_packages_update_by_search_succeeded`, `actions.remote_execution.run_host_job_katello_service_restart_failed`, `actions.remote_execution.run_host_job_katello_service_restart_succeeded`, `actions.remote_execution.run_host_job_katello_upload_profile_failed`, `actions.remote_execution.run_host_job_katello_upload_profile_succeeded`, `actions.remote_execution.run_host_job_leapp_preupgrade_failed`, `actions.remote_execution.run_host_job_leapp_preupgrade_succeeded`, `actions.remote_execution.run_host_job_leapp_remediation_plan_failed`, `actions.remote_execution.run_host_job_leapp_remediation_plan_succeeded`, `actions.remote_execution.run_host_job_leapp_upgrade_failed`, `actions.remote_execution.run_host_job_leapp_upgrade_succeeded`, `actions.remote_execution.run_host_job_puppet_run_host_failed`, `actions.remote_execution.run_host_job_puppet_run_host_succeeded`, `actions.remote_execution.run_host_job_rh_cloud_connector_run_playbook_failed`, `actions.remote_execution.run_host_job_rh_cloud_connector_run_playbook_succeeded`, `actions.remote_execution.run_host_job_rh_cloud_remediate_hosts_failed`, `actions.remote_execution.run_host_job_rh_cloud_remediate_hosts_succeeded`, `actions.remote_execution.run_host_job_run_script_failed`, `actions.remote_execution.run_host_job_run_script_succeeded`, `actions.remote_execution.run_host_job_script_run_openscap_remediation_failed`, `actions.remote_execution.run_host_job_script_run_openscap_remediation_succeeded`, `actions.remote_execution.run_host_job_succeeded`, `actions.remote_execution.run_hosts_job_ansible_configure_cloud_connector_failed`, `actions.remote_execution.run_hosts_job_ansible_configure_cloud_connector_running`, `actions.remote_execution.run_hosts_job_ansible_configure_cloud_connector_succeeded`, `actions.remote_execution.run_hosts_job_ansible_enable_web_console_failed`, `actions.remote_execution.run_hosts_job_ansible_enable_web_console_running`, `actions.remote_execution.run_hosts_job_ansible_enable_web_console_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_update_failed`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_update_running`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_update_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_upgrade_failed`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_upgrade_running`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_upgrade_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_host_failed`, `actions.remote_execution.run_hosts_job_ansible_run_host_running`, `actions.remote_execution.run_hosts_job_ansible_run_host_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_openscap_remediation_failed`, `actions.remote_execution.run_hosts_job_ansible_run_openscap_remediation_running`, `actions.remote_execution.run_hosts_job_ansible_run_openscap_remediation_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_playbook_failed`, `actions.remote_execution.run_hosts_job_ansible_run_playbook_running`, `actions.remote_execution.run_hosts_job_ansible_run_playbook_succeeded`, `actions.remote_execution.run_hosts_job_failed`, `actions.remote_execution.run_hosts_job_foreman_openscap_run_scans_failed`, `actions.remote_execution.run_hosts_job_foreman_openscap_run_scans_running`, `actions.remote_execution.run_hosts_job_foreman_openscap_run_scans_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_action_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_action_running`, `actions.remote_execution.run_hosts_job_katello_bootc_action_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_rollback_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_rollback_running`, `actions.remote_execution.run_hosts_job_katello_bootc_rollback_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_status_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_status_running`, `actions.remote_execution.run_hosts_job_katello_bootc_status_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_switch_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_switch_running`, `actions.remote_execution.run_hosts_job_katello_bootc_switch_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_upgrade_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_upgrade_running`, `actions.remote_execution.run_hosts_job_katello_bootc_upgrade_succeeded`, `actions.remote_execution.run_hosts_job_katello_change_content_source_failed`, `actions.remote_execution.run_hosts_job_katello_change_content_source_running`, `actions.remote_execution.run_hosts_job_katello_change_content_source_succeeded`, `actions.remote_execution.run_hosts_job_katello_errata_install_by_search_failed`, `actions.remote_execution.run_hosts_job_katello_errata_install_by_search_running`, `actions.remote_execution.run_hosts_job_katello_errata_install_by_search_succeeded`, `actions.remote_execution.run_hosts_job_katello_errata_install_failed`, `actions.remote_execution.run_hosts_job_katello_errata_install_running`, `actions.remote_execution.run_hosts_job_katello_errata_install_succeeded`, `actions.remote_execution.run_hosts_job_katello_group_install_failed`, `actions.remote_execution.run_hosts_job_katello_group_install_running`, `actions.remote_execution.run_hosts_job_katello_group_install_succeeded`, `actions.remote_execution.run_hosts_job_katello_group_remove_failed`, `actions.remote_execution.run_hosts_job_katello_group_remove_running`, `actions.remote_execution.run_hosts_job_katello_group_remove_succeeded`, `actions.remote_execution.run_hosts_job_katello_group_update_failed`, `actions.remote_execution.run_hosts_job_katello_group_update_running`, `actions.remote_execution.run_hosts_job_katello_group_update_succeeded`, `actions.remote_execution.run_hosts_job_katello_host_tracer_resolve_failed`, `actions.remote_execution.run_hosts_job_katello_host_tracer_resolve_running`, `actions.remote_execution.run_hosts_job_katello_host_tracer_resolve_succeeded`, `actions.remote_execution.run_hosts_job_katello_module_stream_action_failed`, `actions.remote_execution.run_hosts_job_katello_module_stream_action_running`, `actions.remote_execution.run_hosts_job_katello_module_stream_action_succeeded`, `actions.remote_execution.run_hosts_job_katello_package_install_by_search_failed`, `actions.remote_execution.run_hosts_job_katello_package_install_by_search_running`, `actions.remote_execution.run_hosts_job_katello_package_install_by_search_succeeded`, `actions.remote_execution.run_hosts_job_katello_package_install_failed`, `actions.remote_execution.run_hosts_job_katello_package_install_running`, `actions.remote_execution.run_hosts_job_katello_package_install_succeeded`, `actions.remote_execution.run_hosts_job_katello_package_remove_failed`, `actions.remote_execution.run_hosts_job_katello_package_remove_running`, `actions.remote_execution.run_hosts_job_katello_package_remove_succeeded`, `actions.remote_execution.run_hosts_job_katello_package_update_failed`, `actions.remote_execution.run_hosts_job_katello_package_update_running`, `actions.remote_execution.run_hosts_job_katello_package_update_succeeded`, `actions.remote_execution.run_hosts_job_katello_packages_remove_by_search_failed`, `actions.remote_execution.run_hosts_job_katello_packages_remove_by_search_running`, `actions.remote_execution.run_hosts_job_katello_packages_remove_by_search_succeeded`, `actions.remote_execution.run_hosts_job_katello_packages_update_by_search_failed`, `actions.remote_execution.run_hosts_job_katello_packages_update_by_search_running`, `actions.remote_execution.run_hosts_job_katello_packages_update_by_search_succeeded`, `actions.remote_execution.run_hosts_job_katello_service_restart_failed`, `actions.remote_execution.run_hosts_job_katello_service_restart_running`, `actions.remote_execution.run_hosts_job_katello_service_restart_succeeded`, `actions.remote_execution.run_hosts_job_katello_upload_profile_failed`, `actions.remote_execution.run_hosts_job_katello_upload_profile_running`, `actions.remote_execution.run_hosts_job_katello_upload_profile_succeeded`, `actions.remote_execution.run_hosts_job_leapp_preupgrade_failed`, `actions.remote_execution.run_hosts_job_leapp_preupgrade_running`, `actions.remote_execution.run_hosts_job_leapp_preupgrade_succeeded`, `actions.remote_execution.run_hosts_job_leapp_remediation_plan_failed`, `actions.remote_execution.run_hosts_job_leapp_remediation_plan_running`, `actions.remote_execution.run_hosts_job_leapp_remediation_plan_succeeded`, `actions.remote_execution.run_hosts_job_leapp_upgrade_failed`, `actions.remote_execution.run_hosts_job_leapp_upgrade_running`, `actions.remote_execution.run_hosts_job_leapp_upgrade_succeeded`, `actions.remote_execution.run_hosts_job_puppet_run_host_failed`, `actions.remote_execution.run_hosts_job_puppet_run_host_running`, `actions.remote_execution.run_hosts_job_puppet_run_host_succeeded`, `actions.remote_execution.run_hosts_job_rh_cloud_connector_run_playbook_failed`, `actions.remote_execution.run_hosts_job_rh_cloud_connector_run_playbook_running`, `actions.remote_execution.run_hosts_job_rh_cloud_connector_run_playbook_succeeded`, `actions.remote_execution.run_hosts_job_rh_cloud_remediate_hosts_failed`, `actions.remote_execution.run_hosts_job_rh_cloud_remediate_hosts_running`, `actions.remote_execution.run_hosts_job_rh_cloud_remediate_hosts_succeeded`, `actions.remote_execution.run_hosts_job_run_script_failed`, `actions.remote_execution.run_hosts_job_run_script_running`, `actions.remote_execution.run_hosts_job_run_script_succeeded`, `actions.remote_execution.run_hosts_job_running`, `actions.remote_execution.run_hosts_job_script_run_openscap_remediation_failed`, `actions.remote_execution.run_hosts_job_script_run_openscap_remediation_running`, `actions.remote_execution.run_hosts_job_script_run_openscap_remediation_succeeded`, `actions.remote_execution.run_hosts_job_succeeded`, `ansible_role_created`, `ansible_role_destroyed`, `ansible_role_updated`, `ansible_variable_created`, `ansible_variable_destroyed`, `ansible_variable_updated`, `build_entered`, `build_exited`, `config_report_created`, `config_report_destroyed`, `config_report_updated`, `content_view_created`, `content_view_destroyed`, `content_view_updated`, `create_rss_notifications_performed`, `domain_created`, `domain_destroyed`, `domain_updated`, `host_created`, `host_destroyed`, `host_facts_updated`, `host_updated`, `hostgroup_created`, `hostgroup_destroyed`, `hostgroup_updated`, `model_created`, `model_destroyed`, `model_updated`, `status_changed`, `stored_values_cleanup_performed`, `subnet_created`, `subnet_destroyed`, `subnet_updated`, `template_render_performed`, `user_created`, `user_destroyed`, `user_updated`
- `--http-content-type VALUE`
- `--http-headers KEY_VALUE_LIST`
- `--http-method ENUM` – Possible value(s): `POST`, `GET`, `PUT`, `DELETE`, `PATCH`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--password VALUE`
- `--proxy-authorization BOOLEAN` Authorize with Satellite client certificate and validate Capsule CA from Settings
- `--ssl-ca-certs FILE` – File containing X509 Certification Authorities concatenated in PEM format
- `--target-url VALUE`
- `--user VALUE`
- `--verify-ssl BOOLEAN`
- `--webhook-template VALUE` – Name to search by
- `--webhook-template-id VALUE`
- `-h`, `--help` – Print help

## 95.2. webhook delete

Delete a Webhook

**Usage**

```
# hammer webhook <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 95.3. webhook info

Show Webhook details

**Usage**

```
# hammer webhook <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ADDITIONAL | ALL | DEFAULT | THIN |
| --- | --- | --- | --- | --- |
| Id |  | x | x | x |
| Name |  | x | x | x |
| Target url |  | x | x |  |
| Enabled |  | x | x |  |
| Event |  | x | x |  |
| Http method |  | x | x |  |
| Http content type |  | x | x |  |
| Webhook template |  | x | x |  |
| User |  | x | x |  |
| Verify ssl |  | x | x |  |
| Proxy authorization |  | x | x |  |
| X509 certification authorities | x | x |  |  |
| Http headers/ |  | x | x |  |
| Created at |  | x | x |  |
| Updated at |  | x | x |  |

## 95.4. webhook list

List Webhooks

**Usage**

```
# hammer webhook <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Target url | x | x |  |
| Enabled | x | x |  |

**Search and order fields**

- `enabled` – Values: true, false
- `name` – string
- `target_url` – string

## 95.5. webhook update

Update a Webhook

**Usage**

```
# hammer webhook update [OPTIONS]
```

**Options**

- `--enabled BOOLEAN`
- `--event ENUM` – Possible value(s): `actions.katello.capsule_content.sync_failed`, `actions.katello.capsule_content.sync_succeeded`, `actions.katello.content_view.promote_failed`, `actions.katello.content_view.promote_succeeded`, `actions.katello.content_view.publish_failed`, `actions.katello.content_view.publish_succeeded`, `actions.katello.repository.sync_failed`, `actions.katello.repository.sync_succeeded`, `actions.remote_execution.run_host_job_ansible_configure_cloud_connector_failed`, `actions.remote_execution.run_host_job_ansible_configure_cloud_connector_succeeded`, `actions.remote_execution.run_host_job_ansible_enable_web_console_failed`, `actions.remote_execution.run_host_job_ansible_enable_web_console_succeeded`, `actions.remote_execution.run_host_job_ansible_run_capsule_update_failed`, `actions.remote_execution.run_host_job_ansible_run_capsule_update_succeeded`, `actions.remote_execution.run_host_job_ansible_run_capsule_upgrade_failed`, `actions.remote_execution.run_host_job_ansible_run_capsule_upgrade_succeeded`, `actions.remote_execution.run_host_job_ansible_run_host_failed`, `actions.remote_execution.run_host_job_ansible_run_host_succeeded`, `actions.remote_execution.run_host_job_ansible_run_openscap_remediation_failed`, `actions.remote_execution.run_host_job_ansible_run_openscap_remediation_succeeded`, `actions.remote_execution.run_host_job_ansible_run_playbook_failed`, `actions.remote_execution.run_host_job_ansible_run_playbook_succeeded`, `actions.remote_execution.run_host_job_failed`, `actions.remote_execution.run_host_job_foreman_openscap_run_scans_failed`, `actions.remote_execution.run_host_job_foreman_openscap_run_scans_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_action_failed`, `actions.remote_execution.run_host_job_katello_bootc_action_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_rollback_failed`, `actions.remote_execution.run_host_job_katello_bootc_rollback_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_status_failed`, `actions.remote_execution.run_host_job_katello_bootc_status_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_switch_failed`, `actions.remote_execution.run_host_job_katello_bootc_switch_succeeded`, `actions.remote_execution.run_host_job_katello_bootc_upgrade_failed`, `actions.remote_execution.run_host_job_katello_bootc_upgrade_succeeded`, `actions.remote_execution.run_host_job_katello_change_content_source_failed`, `actions.remote_execution.run_host_job_katello_change_content_source_succeeded`, `actions.remote_execution.run_host_job_katello_errata_install_by_search_failed`, `actions.remote_execution.run_host_job_katello_errata_install_by_search_succeeded`, `actions.remote_execution.run_host_job_katello_errata_install_failed`, `actions.remote_execution.run_host_job_katello_errata_install_succeeded`, `actions.remote_execution.run_host_job_katello_group_install_failed`, `actions.remote_execution.run_host_job_katello_group_install_succeeded`, `actions.remote_execution.run_host_job_katello_group_remove_failed`, `actions.remote_execution.run_host_job_katello_group_remove_succeeded`, `actions.remote_execution.run_host_job_katello_group_update_failed`, `actions.remote_execution.run_host_job_katello_group_update_succeeded`, `actions.remote_execution.run_host_job_katello_host_tracer_resolve_failed`, `actions.remote_execution.run_host_job_katello_host_tracer_resolve_succeeded`, `actions.remote_execution.run_host_job_katello_module_stream_action_failed`, `actions.remote_execution.run_host_job_katello_module_stream_action_succeeded`, `actions.remote_execution.run_host_job_katello_package_install_by_search_failed`, `actions.remote_execution.run_host_job_katello_package_install_by_search_succeeded`, `actions.remote_execution.run_host_job_katello_package_install_failed`, `actions.remote_execution.run_host_job_katello_package_install_succeeded`, `actions.remote_execution.run_host_job_katello_package_remove_failed`, `actions.remote_execution.run_host_job_katello_package_remove_succeeded`, `actions.remote_execution.run_host_job_katello_package_update_failed`, `actions.remote_execution.run_host_job_katello_package_update_succeeded`, `actions.remote_execution.run_host_job_katello_packages_remove_by_search_failed`, `actions.remote_execution.run_host_job_katello_packages_remove_by_search_succeeded`, `actions.remote_execution.run_host_job_katello_packages_update_by_search_failed`, `actions.remote_execution.run_host_job_katello_packages_update_by_search_succeeded`, `actions.remote_execution.run_host_job_katello_service_restart_failed`, `actions.remote_execution.run_host_job_katello_service_restart_succeeded`, `actions.remote_execution.run_host_job_katello_upload_profile_failed`, `actions.remote_execution.run_host_job_katello_upload_profile_succeeded`, `actions.remote_execution.run_host_job_leapp_preupgrade_failed`, `actions.remote_execution.run_host_job_leapp_preupgrade_succeeded`, `actions.remote_execution.run_host_job_leapp_remediation_plan_failed`, `actions.remote_execution.run_host_job_leapp_remediation_plan_succeeded`, `actions.remote_execution.run_host_job_leapp_upgrade_failed`, `actions.remote_execution.run_host_job_leapp_upgrade_succeeded`, `actions.remote_execution.run_host_job_puppet_run_host_failed`, `actions.remote_execution.run_host_job_puppet_run_host_succeeded`, `actions.remote_execution.run_host_job_rh_cloud_connector_run_playbook_failed`, `actions.remote_execution.run_host_job_rh_cloud_connector_run_playbook_succeeded`, `actions.remote_execution.run_host_job_rh_cloud_remediate_hosts_failed`, `actions.remote_execution.run_host_job_rh_cloud_remediate_hosts_succeeded`, `actions.remote_execution.run_host_job_run_script_failed`, `actions.remote_execution.run_host_job_run_script_succeeded`, `actions.remote_execution.run_host_job_script_run_openscap_remediation_failed`, `actions.remote_execution.run_host_job_script_run_openscap_remediation_succeeded`, `actions.remote_execution.run_host_job_succeeded`, `actions.remote_execution.run_hosts_job_ansible_configure_cloud_connector_failed`, `actions.remote_execution.run_hosts_job_ansible_configure_cloud_connector_running`, `actions.remote_execution.run_hosts_job_ansible_configure_cloud_connector_succeeded`, `actions.remote_execution.run_hosts_job_ansible_enable_web_console_failed`, `actions.remote_execution.run_hosts_job_ansible_enable_web_console_running`, `actions.remote_execution.run_hosts_job_ansible_enable_web_console_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_update_failed`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_update_running`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_update_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_upgrade_failed`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_upgrade_running`, `actions.remote_execution.run_hosts_job_ansible_run_capsule_upgrade_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_host_failed`, `actions.remote_execution.run_hosts_job_ansible_run_host_running`, `actions.remote_execution.run_hosts_job_ansible_run_host_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_openscap_remediation_failed`, `actions.remote_execution.run_hosts_job_ansible_run_openscap_remediation_running`, `actions.remote_execution.run_hosts_job_ansible_run_openscap_remediation_succeeded`, `actions.remote_execution.run_hosts_job_ansible_run_playbook_failed`, `actions.remote_execution.run_hosts_job_ansible_run_playbook_running`, `actions.remote_execution.run_hosts_job_ansible_run_playbook_succeeded`, `actions.remote_execution.run_hosts_job_failed`, `actions.remote_execution.run_hosts_job_foreman_openscap_run_scans_failed`, `actions.remote_execution.run_hosts_job_foreman_openscap_run_scans_running`, `actions.remote_execution.run_hosts_job_foreman_openscap_run_scans_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_action_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_action_running`, `actions.remote_execution.run_hosts_job_katello_bootc_action_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_rollback_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_rollback_running`, `actions.remote_execution.run_hosts_job_katello_bootc_rollback_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_status_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_status_running`, `actions.remote_execution.run_hosts_job_katello_bootc_status_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_switch_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_switch_running`, `actions.remote_execution.run_hosts_job_katello_bootc_switch_succeeded`, `actions.remote_execution.run_hosts_job_katello_bootc_upgrade_failed`, `actions.remote_execution.run_hosts_job_katello_bootc_upgrade_running`, `actions.remote_execution.run_hosts_job_katello_bootc_upgrade_succeeded`, `actions.remote_execution.run_hosts_job_katello_change_content_source_failed`, `actions.remote_execution.run_hosts_job_katello_change_content_source_running`, `actions.remote_execution.run_hosts_job_katello_change_content_source_succeeded`, `actions.remote_execution.run_hosts_job_katello_errata_install_by_search_failed`, `actions.remote_execution.run_hosts_job_katello_errata_install_by_search_running`, `actions.remote_execution.run_hosts_job_katello_errata_install_by_search_succeeded`, `actions.remote_execution.run_hosts_job_katello_errata_install_failed`, `actions.remote_execution.run_hosts_job_katello_errata_install_running`, `actions.remote_execution.run_hosts_job_katello_errata_install_succeeded`, `actions.remote_execution.run_hosts_job_katello_group_install_failed`, `actions.remote_execution.run_hosts_job_katello_group_install_running`, `actions.remote_execution.run_hosts_job_katello_group_install_succeeded`, `actions.remote_execution.run_hosts_job_katello_group_remove_failed`, `actions.remote_execution.run_hosts_job_katello_group_remove_running`, `actions.remote_execution.run_hosts_job_katello_group_remove_succeeded`, `actions.remote_execution.run_hosts_job_katello_group_update_failed`, `actions.remote_execution.run_hosts_job_katello_group_update_running`, `actions.remote_execution.run_hosts_job_katello_group_update_succeeded`, `actions.remote_execution.run_hosts_job_katello_host_tracer_resolve_failed`, `actions.remote_execution.run_hosts_job_katello_host_tracer_resolve_running`, `actions.remote_execution.run_hosts_job_katello_host_tracer_resolve_succeeded`, `actions.remote_execution.run_hosts_job_katello_module_stream_action_failed`, `actions.remote_execution.run_hosts_job_katello_module_stream_action_running`, `actions.remote_execution.run_hosts_job_katello_module_stream_action_succeeded`, `actions.remote_execution.run_hosts_job_katello_package_install_by_search_failed`, `actions.remote_execution.run_hosts_job_katello_package_install_by_search_running`, `actions.remote_execution.run_hosts_job_katello_package_install_by_search_succeeded`, `actions.remote_execution.run_hosts_job_katello_package_install_failed`, `actions.remote_execution.run_hosts_job_katello_package_install_running`, `actions.remote_execution.run_hosts_job_katello_package_install_succeeded`, `actions.remote_execution.run_hosts_job_katello_package_remove_failed`, `actions.remote_execution.run_hosts_job_katello_package_remove_running`, `actions.remote_execution.run_hosts_job_katello_package_remove_succeeded`, `actions.remote_execution.run_hosts_job_katello_package_update_failed`, `actions.remote_execution.run_hosts_job_katello_package_update_running`, `actions.remote_execution.run_hosts_job_katello_package_update_succeeded`, `actions.remote_execution.run_hosts_job_katello_packages_remove_by_search_failed`, `actions.remote_execution.run_hosts_job_katello_packages_remove_by_search_running`, `actions.remote_execution.run_hosts_job_katello_packages_remove_by_search_succeeded`, `actions.remote_execution.run_hosts_job_katello_packages_update_by_search_failed`, `actions.remote_execution.run_hosts_job_katello_packages_update_by_search_running`, `actions.remote_execution.run_hosts_job_katello_packages_update_by_search_succeeded`, `actions.remote_execution.run_hosts_job_katello_service_restart_failed`, `actions.remote_execution.run_hosts_job_katello_service_restart_running`, `actions.remote_execution.run_hosts_job_katello_service_restart_succeeded`, `actions.remote_execution.run_hosts_job_katello_upload_profile_failed`, `actions.remote_execution.run_hosts_job_katello_upload_profile_running`, `actions.remote_execution.run_hosts_job_katello_upload_profile_succeeded`, `actions.remote_execution.run_hosts_job_leapp_preupgrade_failed`, `actions.remote_execution.run_hosts_job_leapp_preupgrade_running`, `actions.remote_execution.run_hosts_job_leapp_preupgrade_succeeded`, `actions.remote_execution.run_hosts_job_leapp_remediation_plan_failed`, `actions.remote_execution.run_hosts_job_leapp_remediation_plan_running`, `actions.remote_execution.run_hosts_job_leapp_remediation_plan_succeeded`, `actions.remote_execution.run_hosts_job_leapp_upgrade_failed`, `actions.remote_execution.run_hosts_job_leapp_upgrade_running`, `actions.remote_execution.run_hosts_job_leapp_upgrade_succeeded`, `actions.remote_execution.run_hosts_job_puppet_run_host_failed`, `actions.remote_execution.run_hosts_job_puppet_run_host_running`, `actions.remote_execution.run_hosts_job_puppet_run_host_succeeded`, `actions.remote_execution.run_hosts_job_rh_cloud_connector_run_playbook_failed`, `actions.remote_execution.run_hosts_job_rh_cloud_connector_run_playbook_running`, `actions.remote_execution.run_hosts_job_rh_cloud_connector_run_playbook_succeeded`, `actions.remote_execution.run_hosts_job_rh_cloud_remediate_hosts_failed`, `actions.remote_execution.run_hosts_job_rh_cloud_remediate_hosts_running`, `actions.remote_execution.run_hosts_job_rh_cloud_remediate_hosts_succeeded`, `actions.remote_execution.run_hosts_job_run_script_failed`, `actions.remote_execution.run_hosts_job_run_script_running`, `actions.remote_execution.run_hosts_job_run_script_succeeded`, `actions.remote_execution.run_hosts_job_running`, `actions.remote_execution.run_hosts_job_script_run_openscap_remediation_failed`, `actions.remote_execution.run_hosts_job_script_run_openscap_remediation_running`, `actions.remote_execution.run_hosts_job_script_run_openscap_remediation_succeeded`, `actions.remote_execution.run_hosts_job_succeeded`, `ansible_role_created`, `ansible_role_destroyed`, `ansible_role_updated`, `ansible_variable_created`, `ansible_variable_destroyed`, `ansible_variable_updated`, `build_entered`, `build_exited`, `config_report_created`, `config_report_destroyed`, `config_report_updated`, `content_view_created`, `content_view_destroyed`, `content_view_updated`, `create_rss_notifications_performed`, `domain_created`, `domain_destroyed`, `domain_updated`, `host_created`, `host_destroyed`, `host_facts_updated`, `host_updated`, `hostgroup_created`, `hostgroup_destroyed`, `hostgroup_updated`, `model_created`, `model_destroyed`, `model_updated`, `status_changed`, `stored_values_cleanup_performed`, `subnet_created`, `subnet_destroyed`, `subnet_updated`, `template_render_performed`, `user_created`, `user_destroyed`, `user_updated`
- `--http-content-type VALUE`
- `--http-headers KEY_VALUE_LIST`
- `--http-method ENUM` – Possible value(s): `POST`, `GET`, `PUT`, `DELETE`, `PATCH`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE`
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--password VALUE`
- `--proxy-authorization BOOLEAN` Authorize with Satellite client certificate and validate Capsule CA from Settings
- `--ssl-ca-certs FILE` – File containing X509 Certification Authorities concatenated in PEM format
- `--target-url VALUE`
- `--user VALUE`
- `--verify-ssl BOOLEAN`
- `--webhook-template VALUE` – Name to search by
- `--webhook-template-id VALUE`
- `-h`, `--help` – Print help
