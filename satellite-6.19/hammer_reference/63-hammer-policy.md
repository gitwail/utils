---
title: "policy"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "63"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-policy"
---
# Chapter 63. policy

Manipulate policies

**Usage**

```
# hammer policy [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 63.1. policy create

Create a Policy

**Usage**

```
# hammer policy create [OPTIONS]
```

**Options**

- `--cron-line VALUE` – Policy schedule cron line (only if period == “custom”)
- `--day-of-month NUMBER` – Policy schedule day of month (only if period == “monthly”)
- `--deploy-by ENUM` – How the policy should be deployed Possible value(s): `puppet`, `ansible`, `manual`
- `--description VALUE` – Policy description
- `--host-ids LIST` – Apply policy to hosts
- `--hostgroup-ids LIST` – Apply policy to host groups
- `--hostgroups LIST`
- `--hosts LIST`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--locations LIST`
- `--name VALUE` – Policy name
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organizations LIST`
- `--period VALUE` – Policy schedule period (weekly, monthly, custom)
- `--scap-content VALUE` – SCAP content title
- `--scap-content-id NUMBER` – Policy SCAP content ID
- `--scap-content-profile VALUE` – Name to search by
- `--scap-content-profile-id NUMBER` – Policy SCAP content profile ID
- `--tailoring-file VALUE` – Tailoring file name
- `--tailoring-file-id NUMBER` – Tailoring file ID
- `--tailoring-file-profile-id NUMBER` Tailoring file profile ID
- `--weekday VALUE` – Policy schedule weekday (only if period == “weekly”)
- `-h`, `--help` – Print help

## 63.2. policy delete

Delete a Policy

**Usage**

```
# hammer policy <delete|destroy> [OPTIONS]
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

## 63.3. policy hosts

List all hosts

**Usage**

```
# hammer policy hosts [OPTIONS]
```

**Options**

- `--environment VALUE` – Name to search by
- `--environment-id VALUE` – ID of puppet environment
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE` – Policy Id
- `--include ENUM` – Array of extra information types to include Possible value(s): `parameters`, `all_parameters`
- `--location VALUE` – Set the current location context for the request
- `--location-id VALUE` – ID of location
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Policy name
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id VALUE` – ID of organization
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--search VALUE` – Filter results
- `--thin BOOLEAN` – Only list ID and name of hosts
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Operating system | x | x |  |
| Host group | x | x |  |
| Ip | x | x |  |
| Mac | x | x |  |
| Global status | x | x |  |
| Organization | x |  |  |
| Location | x |  |  |
| Additional information | x |  |  |
| Content view environments | x | x |  |
| Multi content view environment | x | x |  |
| Security | x |  |  |
| Bugfix | x |  |  |
| Enhancement | x |  |  |
| Running image | x |  |  |
| Running image digest | x |  |  |
| Staged image | x |  |  |
| Staged image digest | x |  |  |
| Available image | x |  |  |
| Available image digest | x |  |  |
| Rollback image | x |  |  |
| Rollback image digest | x |  |  |
| Trace status | x | x |  |
| Last checkin | x | x |  |

**Search and order fields**

- `activation_key` – string
- `activation_key_id` – string
- `applicable_debs` – string
- `applicable_errata` – string
- `applicable_errata_issued` – date
- `applicable_rpms` – string
- `architecture` – string
- `boot_time`
- `bootc_available_digest` – string
- `bootc_available_image` – string
- `bootc_booted_digest` – string
- `bootc_booted_image` – string
- `bootc_rollback_digest` – string
- `bootc_rollback_image` – string
- `bootc_staged_digest` – string
- `bootc_staged_image` – string
- `build` – Values: true, false
- `build_status` – Values: built, pending, token_expired, build_failed
- `comment` – text
- `compute_resource` – string
- `compute_resource_id` – integer
- `configuration_status.applied` – integer
- `configuration_status.enabled` – Values: true, false
- `configuration_status.failed` – integer
- `configuration_status.failed_restarts` – integer
- `configuration_status.interesting` – Values: true, false
- `configuration_status.pending` – integer
- `configuration_status.restarted` – integer
- `configuration_status.skipped` – integer
- `content_source` – string
- `content_views` – string
- convert2rhel_through_foreman integer
- `created_at` – datetime
- `domain` – string
- `domain_id` – integer
- `errata_status` – Values: security_needed, errata_needed, updated, unknown
- `execution_status` – Values: ok, error
- `facts` – string
- `global_status` – Values: ok, warning, error
- `has_ip` – string
- has_ip6 string
- `has_mac` – string
- `hostgroup` – string
- `hostgroup_fullname` – string
- `hostgroup_id` – integer
- `hostgroup_name` – string
- `hostgroup_title` – string
- `hypervisor` – boolean
- `hypervisor_host` – string
- `id` – integer
- `image` – string
- `image_mode` – Values: true, false
- `infrastructure_facet.foreman` – Values: true, false
- `infrastructure_facet.smart_proxy_id`
- `insights_client_report_status` – Values: reporting, no_report
- `insights_inventory_sync_status` – Values: disconnect, sync
- `insights_recommendations_count` – integer
- `insights_uuid` – string
- `installable_errata` – string
- `installed_at` – datetime
- `ip` – string
- ip6 string
- `job_invocation.id` – string
- `job_invocation.result` – Values: cancelled, failed, pending, success
- `last_checkin` – datetime
- `last_report` – datetime
- `lifecycle_environments` – string
- `location` – string
- `location_id` – integer
- `mac` – string
- `managed` – Values: true, false
- `model` – string
- `name` – string
- `organization` – string
- `organization_id` – integer
- `origin` – string
- `os` – string
- `os_description` – string
- `os_id` – integer
- `os_major` – string
- `os_minor` – string
- `os_title` – string
- `owner` – string
- `owner_id` – integer
- `owner_type` – string
- `params` – string
- `params_name` – string
- `parent_hostgroup` – string
- `puppet_ca` – string
- `puppet_proxy_id` – integer
- `puppetmaster` – string
- `pxe_loader` – Values: PXELinux_BIOS, PXELinux_UEFI, Grub2_BIOS, Grub2_ELF, Grub2_UEFI, Grub2_UEFI_SecureBoot, Grub2_UEFI_HTTP, Grub2_UEFI_HTTPS, Grub2_UEFI_HTTPS_SecureBoot, iPXE_Embedded, iPXE_UEFI_HTTP, iPXE_Chain_BIOS, iPXE_Chain_UEFI
- `realm` – string
- `realm_id` – integer
- `registered_at` – datetime
- `registered_through` – string
- `release_version` – string
- `reported.aws_account_id`
- `reported.aws_instance_id`
- `reported.aws_region`
- `reported.azure_instance_id`
- `reported.azure_subscription_id`
- `reported.bios_release_date`
- `reported.bios_vendor`
- `reported.bios_version`
- `reported.boot_time`
- `reported.cloud_provider`
- `reported.cores`
- `reported.disks_total`
- `reported.gcp_instance_id`
- `reported.gcp_project_id`
- `reported.kernel_version`
- `reported.ram`
- `reported.sockets`
- `reported.virtual` – Values: true, false
- `repository` – string
- `repository_content_label` – string
- `rhel_lifecycle_status` – Values: full_support, maintenance_support, approaching_end_of_maintenance, extended_support, approaching_end_of_support, support_ended
- `role` – text
- `service_level` – string
- `smart_proxy` – string
- `status.applied` – integer
- `status.enabled` – Values: true, false
- `status.failed` – integer
- `status.failed_restarts` – integer
- `status.interesting` – Values: true, false
- `status.pending` – integer
- `status.restarted` – integer
- `status.skipped` – integer
- `subnet` – string
- `subnet.name` – text
- subnet6 string
- subnet6.name text
- `subscription_id` – string
- `subscription_name` – string
- `subscription_uuid` – string
- `trace_status` – Values: reboot_needed, process_restart_needed, updated
- `upgradable_debs` – string
- `upgradable_rpms` – string
- `usage` – text
- `user.firstname` – string
- `user.lastname` – string
- `user.login` – string
- `user.mail` – string
- `usergroup` – string
- `usergroup.name` – string
- `uuid` – string

## 63.4. policy info

Show a Policy

**Usage**

```
# hammer policy <info|show> [OPTIONS]
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

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Created at | x | x |  |
| Period | x | x |  |
| Weekday | x | x |  |
| Day of month | x | x |  |
| Cron line | x | x |  |
| Scap content id | x | x |  |
| Scap content profile id | x | x |  |
| Tailoring file id | x | x |  |
| Tailoring file profile id | x | x |  |
| Deployment option | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Hostgroups/ | x | x |  |

## 63.5. policy list

List Policies

**Usage**

```
# hammer policy <list|index> [OPTIONS]
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
| Created at | x | x |  |

**Search and order fields**

- `content` – string
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
- `profile` – string
- `tailoring_file` – string
- `tailoring_file_profile` – string

## 63.6. policy update

Update a Policy

**Usage**

```
# hammer policy update [OPTIONS]
```

**Options**

- `--cron-line VALUE` – Policy schedule cron line (only if period == “custom”)
- `--day-of-month NUMBER` – Policy schedule day of month (only if period == “monthly”)
- `--deploy-by ENUM` – How the policy should be deployed Possible value(s): `puppet`, `ansible`, `manual`
- `--description VALUE` – Policy description
- `--host-ids LIST` – Apply policy to hosts
- `--hostgroup-ids LIST` – Apply policy to host groups
- `--hostgroups LIST`
- `--hosts LIST`
- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--locations LIST`
- `--name VALUE` – Policy name
- `--new-name VALUE` – Policy name
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organizations LIST`
- `--period VALUE` – Policy schedule period (weekly, monthly, custom)
- `--scap-content VALUE` – SCAP content title
- `--scap-content-id NUMBER` – Policy SCAP content ID
- `--scap-content-profile VALUE` – Name to search by
- `--scap-content-profile-id NUMBER` – Policy SCAP content profile ID
- `--tailoring-file VALUE` – Tailoring file name
- `--tailoring-file-id NUMBER` – Tailoring file ID
- `--tailoring-file-profile-id NUMBER` Tailoring file profile ID
- `--weekday VALUE` – Policy schedule weekday (only if period == “weekly”)
- `-h`, `--help` – Print help
