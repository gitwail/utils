---
title: "host-collection"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "43"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-host-collection"
---
# Chapter 43. host-collection

Manipulate host collections

**Usage**

```
# hammer host-collection [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 43.1. host-collection add-host

Add host to the host collection

**Usage**

```
# hammer host-collection add-host [OPTIONS]
```

**Options**

- `--host-ids LIST` – Array of host ids
- `--hosts LIST`
- `--id NUMBER` – Id of the host collection
- `--name VALUE` – Host collection name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 43.2. host-collection copy

Copy a host collection

**Usage**

```
# hammer host-collection copy [OPTIONS]
```

**Options**

- `--id NUMBER` – ID of the host collection
- `--name VALUE` – New host collection name
- `--new-name VALUE` – New host collection name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 43.3. host-collection create

Create a host collection

**Usage**

```
# hammer host-collection create [OPTIONS]
```

**Options**

- `--description VALUE`
- `--host-ids LIST` – List of host ids to replace the hosts in host collection
- `--hosts LIST`
- `--max-hosts NUMBER` – Maximum number of hosts in the host collection
- `--name VALUE` – Host Collection name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--unlimited-hosts` – Set hosts max to unlimited
- `-h`, `--help` – Print help

## 43.4. host-collection delete

Destroy a host collection

**Usage**

```
# hammer host-collection <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – Id of the host collection
- `--name VALUE` – Host collection name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 43.5. host-collection erratum

Manage errata on your host collections. These commands are no longer available. Use the remote execution equivalent

**Usage**

```
# hammer host-collection erratum [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 43.5.1. host-collection erratum install

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_errata_install`. Specify the host collection with the --search-query parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

**Usage**

```
# hammer host-collection erratum install [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_errata_install`. Specify the host collection with the `--search-query` parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

Unfortunately the server does not support such operation.

## 43.6. host-collection hosts

List all hosts

**Usage**

```
# hammer host-collection hosts [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE` – Host Collection ID
- `--include ENUM` – Array of extra information types to include Possible value(s): `parameters`, `all_parameters`
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id VALUE` ID of puppet environment
- `--location VALUE` – Set the current location context for the request
- `--location-id VALUE` – ID of location
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Host Collection Name
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – ID of organization
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
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
| Security | x |  |  |
| Bugfix | x |  |  |
| Enhancement | x |  |  |

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

## 43.7. host-collection info

Show a host collection

**Usage**

```
# hammer host-collection <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Id of the host collection
- `--name VALUE` – Host collection name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Limit | x | x |  |
| Description | x | x |  |
| Total hosts | x | x |  |

## 43.8. host-collection list

List host collections

**Usage**

```
# hammer host-collection <list|index> [OPTIONS]
```

**Options**

- `--activation-key VALUE` – Activation key name to search by
- `--activation-key-id VALUE` – Activation key identifier
- `--available-for VALUE` – Interpret specified object to return only Host Collections that can be associated with specified object. The value `host` is supported.
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host VALUE` – Host name
- `--host-id NUMBER` – Filter products by host id
- `--name VALUE` – Host collection name to filter by
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Limit | x | x |  |
| Description | x | x |  |

**Search and order fields**

- `host` – string
- `name` – string
- `organization_id` – integer

## 43.9. host-collection package

Manage packages on your host collections. These commands are no longer available. Use the remote execution equivalent

**Usage**

```
# hammer host-collection package [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 43.9.1. host-collection package install

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_package_install`. Specify the host collection with the --search-query parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

**Usage**

```
# hammer host-collection package install [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_package_install`. Specify the host collection with the `--search-query` parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

Unfortunately the server does not support such operation.

### 43.9.2. host-collection package remove

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_package_remove`. Specify the host collection with the --search-query parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

**Usage**

```
# hammer host-collection package remove [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_package_remove`. Specify the host collection with the `--search-query` parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

Unfortunately the server does not support such operation.

### 43.9.3. host-collection package update

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_package_update`. Specify the host collection with the --search-query parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

**Usage**

```
# hammer host-collection package update [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_package_update`. Specify the host collection with the `--search-query` parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

Unfortunately the server does not support such operation.

## 43.10. host-collection package-group

Manage package-groups on your host collections. These commands are no longer available. Use the remote execution equivalent

**Usage**

```
# hammer host-collection package-group [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 43.10.1. host-collection package-group install

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_group_install`. Specify the host collection with the --search-query parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

**Usage**

```
# hammer host-collection package-group install [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_group_install`. Specify the host collection with the `--search-query` parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

Unfortunately the server does not support such operation.

### 43.10.2. host-collection package-group remove

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_group_remove`. Specify the host collection with the --search-query parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

**Usage**

```
# hammer host-collection package-group remove [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_group_remove`. Specify the host collection with the `--search-query` parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

Unfortunately the server does not support such operation.

### 43.10.3. host-collection package-group update

Not supported. Use the remote execution equivalent `hammer job-invocation create --feature katello_group_update`. Specify the host collection with the --search-query parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

**Usage**

```
# hammer host-collection package-group update [OPTIONS]
```

**Options**

- `-h`, `--help` – Unsupported Operation - Use the remote execution equivalent `` hammer job-invocation create `--feature `` katello_group_update`. Specify the host collection with the `--search-query` parameter, e.g. `--search-query "host_collection = MyCollection"` or `--search-query "host_collection_id=6"`

Unfortunately the server does not support such operation.

## 43.11. host-collection remove-host

Remove hosts from the host collection

**Usage**

```
# hammer host-collection remove-host [OPTIONS]
```

**Options**

- `--host-ids LIST` – Array of host ids
- `--hosts LIST`
- `--id NUMBER` – Id of the host collection
- `--name VALUE` – Host collection name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 43.12. host-collection update

Update a host collection

**Usage**

```
# hammer host-collection update [OPTIONS]
```

**Options**

- `--description VALUE`
- `--host-ids LIST` – List of host ids to replace the hosts in host collection
- `--hosts LIST`
- `--id NUMBER` – Id of the host collection
- `--max-hosts NUMBER` – Maximum number of hosts in the host collection
- `--name VALUE` – Host Collection name
- `--new-name VALUE` – Host Collection name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--unlimited-hosts` – Set hosts max to unlimited
- `-h`, `--help` – Print help
