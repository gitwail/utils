---
title: "activation-key"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-activation-key"
---
# Chapter 3. activation-key

Manipulate activation keys

**Usage**

```
# hammer activation-key [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 3.1. activation-key add-host-collection

Associate a resource

**Usage**

```
# hammer activation-key add-host-collection [OPTIONS]
```

**Options**

- `--host-collection VALUE` – Host collection name to search by
- `--host-collection-id NUMBER` – Id of the host collection
- `--id VALUE` – ID of the activation key
- `--name VALUE` – Activation key name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 3.2. activation-key content-override

Override product content defaults

**Usage**

```
# hammer activation-key content-override [OPTIONS]
```

**Options**

- `--content-label VALUE` – Label of the content
- `--force` – Force the override. Required for overrides other than `enabled`
- `--id NUMBER` – ID of the activation key
- `--name VALUE` – Activation key name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--override-name VALUE` – Override parameter key or name. To enable or disable a repo select `enabled`. Default value: enabled Default: "enabled"
- `--remove` – Remove a content override
- `--value VALUE` – Override value. Note for repo enablement you can use a boolean value
- `-h`, `--help` – Print help

## 3.3. activation-key copy

Copy an activation key

**Usage**

```
# hammer activation-key copy [OPTIONS]
```

**Options**

- `--id NUMBER` – ID of the activation key
- `--name VALUE` – Activation key name to search by
- `--new-name VALUE` – Name of new activation key
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 3.4. activation-key create

Create an activation key

**Usage**

```
# hammer activation-key create [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-environment-ids LIST` Array of content view environment ids to be associated with the activation key. Ignored if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-environments LIST` – Comma-separated list of content view environment labels to be associated with the activation key, in the format of `lifecycle_environment_label/content_view_label`. Ignored if content_view_environment_ids is specified, or if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-id NUMBER` – Id of the single content view to be associated with the activation key.
- `--description VALUE` – Description
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` – Id of the single lifecycle environment to be associated with the activation key.
- `--max-hosts NUMBER` – Maximum number of registered content hosts
- `--name VALUE` – Name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--purpose-role VALUE` – Sets the system purpose usage
- `--purpose-usage VALUE` – Sets the system purpose usage
- `--release-version VALUE` – Content release version
- `--service-level VALUE` – Service level
- `--unlimited-hosts` – Set hosts max to unlimited
- `-h`, `--help` – Print help

## 3.5. activation-key delete

Destroy an activation key

**Usage**

```
# hammer activation-key <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – ID of the activation key
- `--name VALUE` – Activation key name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 3.6. activation-key host-collections

List associated host collections

**Usage**

```
# hammer activation-key host-collections [OPTIONS]
```

**Options**

- `--available-for VALUE` – Interpret specified object to return only Host Collections that can be associated with specified object. The value `host` is supported.
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--host-id NUMBER` – Filter products by host id
- `--id VALUE` – ID of activation key
- `--name VALUE` – Name of activation key
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--sort-by VALUE` – Field to sort the results on
- `--sort-order VALUE` – How to order the sorted results (e.g. ASC for ascending)
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |

## 3.7. activation-key info

Show an activation key

**Usage**

```
# hammer activation-key <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – ID of the activation key
- `--name VALUE` – Activation key name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--show-hosts BOOLEAN` – Show hosts associated to an activation key
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Name | x | x | x |
| Id | x | x | x |
| Description | x | x |  |
| Host limit | x | x |  |
| Multi content view environment | x | x |  |
| Release version | x | x |  |
| Content view environment labels | x | x |  |
| Organization/id | x | x |  |
| Organization/name | x | x |  |
| Content view environments/content view/id | x | x |  |
| Content view environments/content view/name | x | x |  |
| Content view environments/content view/version | x | x |  |
| Content view environments/content view/content view version id | x | x |  |
| Content view environments/content view/composite | x | x |  |
| Content view environments/content view/rolling | x | x |  |
| Content view environments/content view/content view environment id | x | x |  |
| Content view environments/lifecycle environment/id | x | x |  |
| Content view environments/lifecycle environment/name | x | x |  |
| Content view environments/label | x | x |  |
| Associated hosts/id | x | x |  |
| Associated hosts/name | x | x |  |
| Host collections/id | x | x |  |
| Host collections/name | x | x |  |
| Content overrides/content label | x | x |  |
| Content overrides/name | x | x |  |
| Content overrides/value | x | x |  |
| System purpose/service level | x | x |  |
| System purpose/purpose usage | x | x |  |
| System purpose/purpose role | x | x |  |

## 3.8. activation-key list

List activation keys

**Usage**

```
# hammer activation-key <list|index> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-environment-ids LIST` Array of content view environment ids associated with the activation key. Ignored if content_view_id and lifecycle_environment_id are specified.Requires allow_multiple_content_views setting to be on.
- `--content-view-environments LIST` – Comma-separated list of content view environment labels associated with the activation key, in the format of `lifecycle_environment_label/content_view_label`. Ignored if content_view_environment_ids is specified, or if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-id NUMBER` – Content view identifier
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` – Environment identifier
- `--name VALUE` – Activation key name to filter by
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
| Host limit | x | x |  |
| Content view environments | x | x |  |
| Multi content view environment | x | x |  |

**Search and order fields**

- `content_view` – string
- `content_view_id` – integer
- `description` – text
- `environment` – string
- `lifecycle_environment_id` – integer
- `name` – string
- `organization_id` – integer
- `role` – string
- `subscription_id` – string
- `subscription_name` – string
- `usage` – string

## 3.9. activation-key product-content

List associated products

**Usage**

```
# hammer activation-key product-content [OPTIONS]
```

**Options**

- `--content-access-mode-all BOOLEAN` Get all content available, not just that provided by subscriptions
- `--content-access-mode-env BOOLEAN` Limit content to just that available in the activation key`s content view version
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--id VALUE` – ID of the activation key
- `--name VALUE` – Activation key name to search by
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
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
| Type | x | x |  |
| Url | x | x |  |
| Gpg key | x | x |  |
| Label | x | x |  |
| Default enabled? | x | x |  |
| Override | x | x |  |

## 3.10. activation-key remove-host-collection

Disassociate a resource

**Usage**

```
# hammer activation-key remove-host-collection [OPTIONS]
```

**Options**

- `--host-collection VALUE` – Host collection name to search by
- `--host-collection-id NUMBER` – Id of the host collection
- `--id VALUE` – ID of the activation key
- `--name VALUE` – Activation key name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 3.11. activation-key update

Update an activation key

**Usage**

```
# hammer activation-key update [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-environment-ids LIST` Array of content view environment ids to be associated with the activation key. Ignored if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-environments LIST` – Comma-separated list of content view environment labels to be associated with the activation key, in the format of `lifecycle_environment_label/content_view_label`. Ignored if content_view_environment_ids is specified, or if content_view_id and lifecycle_environment_id are specified. Requires allow_multiple_content_views setting to be on.
- `--content-view-id NUMBER` – Id of the single content view to be associated with the activation key.
- `--description VALUE` – Description
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--id NUMBER` – ID of the activation key
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` – Id of the single lifecycle environment to be associated with the activation key.
- `--max-hosts NUMBER` – Maximum number of registered content hosts
- `--name VALUE` – Name
- `--new-name VALUE` – Name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--purpose-role VALUE` – Sets the system purpose usage
- `--purpose-usage VALUE` – Sets the system purpose usage
- `--release-version VALUE` – Content release version
- `--service-level VALUE` – Service level
- `--unlimited-hosts` – Set hosts max to unlimited
- `-h`, `--help` – Print help
