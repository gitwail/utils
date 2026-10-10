---
title: "content-view"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "23"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-content-view"
---
# Chapter 23. content-view

Manipulate content views

**Usage**

```
# hammer content-view [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 23.1. content-view add-repository

Associate a resource

**Usage**

```
# hammer content-view add-repository [OPTIONS]
```

**Options**

- `--id VALUE` – Content view numeric identifier
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository ID
- `-h`, `--help` – Print help

## 23.2. content-view add-version

Add a content view version to a composite view

**Usage**

```
# hammer content-view add-version [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view id to search by
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` Content view version identifier
- `--id VALUE` – Content view numeric identifier
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 23.3. content-view copy

Copy a content view

**Usage**

```
# hammer content-view copy [OPTIONS]
```

**Options**

- `--id NUMBER` – Content view numeric identifier
- `--name VALUE` – Content view name to search by
- `--new-name VALUE` – New content view name
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 23.4. content-view create

Create a content view

**Usage**

```
# hammer content-view create [OPTIONS]
```

**Options**

- `--auto-publish BOOLEAN` – Enable/Disable auto publish of composite view
- `--component-ids LIST` – List of component content view version ids for composite views
- `--composite` – Create a composite content view
- `--description VALUE` – Description for the content view
- `--import-only` – Designate this Content View for importing from upstream servers only.
- `--label VALUE` – Content view label
- `--lifecycle-environment-ids LIST` List of lifecycle environments for rolling content views
- `--lifecycle-environments LIST`
- `--name VALUE` – Name of the content view
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--repository-ids LIST` – List of repository ids
- `--rolling` – Create a rolling content view
- `--solve-dependencies BOOLEAN` – Solve RPM dependencies by default on Content View publish, defaults to false
- `-h`, `--help` – Print help

## 23.5. content-view delete

Delete a content view

**Usage**

```
# hammer content-view delete [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Content view numeric identifier
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 23.6. content-view info

Show a content view

**Usage**

```
# hammer content-view <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Content view numeric identifier
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Label | x | x |  |
| Composite | x | x |  |
| Rolling | x | x |  |
| Description | x | x |  |
| Content host count | x | x |  |
| Solve dependencies | x | x |  |
| Organization | x | x |  |
| Yum repositories/id | x | x |  |
| Yum repositories/name | x | x |  |
| Yum repositories/label | x | x |  |
| File repositories/id | x | x |  |
| File repositories/name | x | x |  |
| File repositories/label | x | x |  |
| Container image repositories/id | x | x |  |
| Container image repositories/name | x | x |  |
| Container image repositories/label | x | x |  |
| Ostree repositories/id | x | x |  |
| Ostree repositories/name | x | x |  |
| Ostree repositories/label | x | x |  |
| Ansible repositories/id | x | x |  |
| Ansible repositories/name | x | x |  |
| Ansible repositories/label | x | x |  |
| File repositories/id | x | x |  |
| File repositories/name | x | x |  |
| File repositories/label | x | x |  |
| Debian repositories/id | x | x |  |
| Debian repositories/name | x | x |  |
| Debian repositories/label | x | x |  |
| Python repositories/id | x | x |  |
| Python repositories/name | x | x |  |
| Python repositories/label | x | x |  |
| Lifecycle environments/id | x | x |  |
| Lifecycle environments/name | x | x |  |
| Versions/id | x | x |  |
| Versions/version | x | x |  |
| Versions/published | x | x |  |
| Components/id | x | x |  |
| Components/name | x | x |  |
| Components/latest version | x | x |  |
| Components/not yet published | x | x |  |
| Components/always update to the latest | x | x |  |
| Activation keys/ | x | x |  |

## 23.7. content-view list

List content views

**Usage**

```
# hammer content-view <list|index> [OPTIONS]
```

**Options**

- `--composite BOOLEAN` – Filter only composite content views
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--include-generated BOOLEAN` – Include content views generated by imports/exports. Defaults to false
- `--label VALUE` – Label of the content view
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Environment identifier
- `--name VALUE` – Name of the content view
- `--noncomposite BOOLEAN` – Filter out composite content views
- `--nondefault BOOLEAN` – Filter out default content views
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--without LIST` – Do not include this array of content views
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Content view id | x | x | x |
| Name | x | x | x |
| Label | x | x |  |
| Composite | x | x |  |
| Rolling | x | x |  |
| Last published | x | x |  |
| Repository ids | x | x |  |

**Search and order fields**

- `composite` – Values: true, false
- `content_views` – string
- `default` – boolean
- `generated_for` – integer
- `label` – string
- `name` – string
- `organization_id` – integer
- `rolling` – Values: true, false

## 23.8. content-view publish

Publish a content view

**Usage**

```
# hammer content-view publish [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--description VALUE` – Description for the new published content view version
- `--id NUMBER` – Content view identifier
- `--is-force-promote BOOLEAN` – Force content view promotion and bypass lifecycle environment restriction
- `--lifecycle-environment-ids LIST` Identifiers for Lifecycle Environment
- `--lifecycle-environments LIST`
- `--major NUMBER` – Override the major version number
- `--minor NUMBER` – Override the minor version number
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--publish-only-if-needed BOOLEAN` Check audited changes and proceed only if content or filters have changed since last publish
- `--repos-units SCHEMA` – Specify the list of units in each repo
- `-h`, `--help` – Print help

Following parameters accept format defined by its schema (bold are required; <> contains acceptable type; [] contains acceptable value):

- `--repos-units` – "**label**=<string>,**rpm_filenames**=<array>, …​ "

## 23.9. content-view purge

Delete old versions of a content view

**Usage**

```
# hammer content-view purge [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--count NUMBER` – (deprecated) Number of versions to keep
- `--id VALUE` – Content View numeric identifier
- `--name VALUE` – Content View name
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--versions-to-keep NUMBER` – Number of unused versions to keep Default: 3
- `-h`, `--help` – Print help

## 23.10. content-view remove

Remove versions and/or environments from a content view and reassign systems and keys

**Usage**

```
# hammer content-view remove [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view-version-ids LIST` Content view version identifiers to be deleted
- `--content-view-versions LIST`
- `--destroy-content-view BOOLEAN` – Delete the content view with all the versions and environments
- `--environment-ids LIST` – (--environment-ids is deprecated: Use `--lifecycle-environment-ids` instead)
- `--environments LIST` – (--environments is deprecated: Use `--lifecycle-environments` instead)
- `--id NUMBER` – Content view numeric identifier
- `--key-content-view-id NUMBER` – Content view to reassign orphaned activation keys to
- `--key-environment-id NUMBER` – Environment to reassign orphaned activation keys to
- `--lifecycle-environment-ids LIST` Environment numeric identifiers to be removed
- `--lifecycle-environments LIST`
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--system-content-view-id NUMBER` Content view to reassign orphaned systems to
- `--system-environment-id NUMBER` – Environment to reassign orphaned systems to
- `-h`, `--help` – Print help

## 23.11. content-view remove-from-environment

Remove a content view from an environment

**Usage**

```
# hammer content-view remove-from-environment [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--id NUMBER` – Content view numeric identifier
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Environment numeric identifier
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 23.12. content-view remove-repository

Disassociate a resource

**Usage**

```
# hammer content-view remove-repository [OPTIONS]
```

**Options**

- `--id VALUE` – Content view numeric identifier
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Repository ID
- `-h`, `--help` – Print help

## 23.13. content-view remove-version

Remove a content view version from a composite view

**Usage**

```
# hammer content-view remove-version [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` Content view version identifier
- `--id VALUE` – Content view numeric identifier
- `--name VALUE` – Content view name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 23.14. content-view update

Update a content view

**Usage**

```
# hammer content-view update [OPTIONS]
```

**Options**

- `--auto-publish BOOLEAN` – Enable/Disable auto publish of composite view
- `--component-ids LIST` – List of component content view version ids for composite views
- `--description VALUE` – Description for the content view
- `--id NUMBER` – Content view identifier
- `--import-only BOOLEAN` – Designate this Content View for importing from upstream servers only. Defaults to false
- `--lifecycle-environment-ids LIST` List of lifecycle environments for rolling content views
- `--lifecycle-environments LIST`
- `--name VALUE` – New name for the content view
- `--new-name VALUE` – New name for the content view
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--repository-ids LIST` – List of repository ids
- `--solve-dependencies BOOLEAN` – Solve RPM dependencies by default on Content View publish, defaults to false
- `-h`, `--help` – Print help

## 23.15. content-view version

View and manage content view versions

**Usage**

```
# hammer content-view version [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 23.15.1. content-view version delete

Remove content view version

**Usage**

```
# hammer content-view version delete [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--id NUMBER` – Content view version identifier
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` ID of the environment
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--version VALUE` – Content view version number
- `-h`, `--help` – Print help

### 23.15.2. content-view version incremental-update

Perform an Incremental Update on one or more Content View Versions

**Usage**

```
# hammer content-view version incremental-update [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` – Content View Version Ids to perform an incremental update on. May contain composites as well as one or more components to update.
- `--deb-ids LIST` – Deb Package ids to copy into the new versions
- `--debs LIST`
- `--description VALUE` – The description for the new generated Content View Versions
- `--errata-ids LIST` – Errata ids to copy into the new versions
- `--host-ids LIST` – IDs of hosts to update
- `--lifecycle-environment-ids LIST` – List of lifecycle environment IDs to update the content view version in
- `--lifecycle-environments LIST` – List of lifecycle environment names to update the content view version in
- `--organization VALUE` – Organization name for resolving lifecycle environment names
- `--organization-id VALUE` – Organization id for resolving lifecycle environment names
- `--package-ids LIST` – Package ids to copy into the new versions
- `--packages LIST`
- `--propagate-all-composites BOOLEAN` If true, will publish a new composite version using any specified content_view_version_id that has been promoted to a lifecycle environment
- `--resolve-dependencies BOOLEAN` – If true, when adding the specified errata or packages, any needed dependencies will be copied as well. Defaults to true
- `--update-all-hosts BOOLEAN` – Update all editable and applicable hosts within the specified Content View and Lifecycle Environments
- `-h`, `--help` – Print help

### 23.15.3. content-view version info

Show content view version

**Usage**

```
# hammer content-view version <info|show> [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Content view version identifier
- `--include-applied-filters BOOLEAN` Whether or not to return filters applied to the content view version
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` ID of the environment
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--version VALUE` – Content view version number
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x |  |
| Version | x | x | x |
| Description | x | x |  |
| Content view id | x | x |  |
| Content view name | x | x |  |
| Content view label | x | x |  |
| Lifecycle environments/id | x | x |  |
| Lifecycle environments/name | x | x |  |
| Lifecycle environments/label | x | x |  |
| Repositories/id | x | x |  |
| Repositories/name | x | x |  |
| Repositories/label | x | x |  |
| Has applied filters | x | x |  |
| Applied filters/id | x | x |  |
| Applied filters/name | x | x |  |
| Applied filters/type | x | x |  |
| Applied filters/inclusion | x | x |  |
| Applied filters/original packages | x | x |  |
| Applied filters/original module streams | x | x |  |
| Applied filters/rules/id | x | x |  |
| Applied filters/rules/name | x | x |  |
| Applied filters/rules/uuid | x | x |  |
| Applied filters/rules/module stream id | x | x |  |
| Applied filters/rules/types/ | x | x |  |
| Applied filters/rules/architecture | x | x |  |
| Applied filters/rules/content view filter id | x | x |  |
| Applied filters/rules/errata id | x | x |  |
| Applied filters/rules/date type | x | x |  |
| Applied filters/rules/start date | x | x |  |
| Applied filters/rules/end date | x | x |  |
| Dependency solving | x | x |  |

### 23.15.4. content-view version list

List content view versions

**Usage**

```
# hammer content-view version <list|index> [OPTIONS]
```

**Options**

- `--composite-version-id NUMBER` – Filter versions that are components in the specified composite version
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view identifier
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--file-id NUMBER` – Filter content view versions that contain the file
- `--full-result BOOLEAN` – Whether or not to show all results
- `--include-applied-filters BOOLEAN` Whether or not to return filters applied to the content view version
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Filter versions by environment
- `--nondefault BOOLEAN` – Filter out default content views
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--triggered-by-id NUMBER` – Filter composite versions whose publish was triggered by the specified component version
- `--version VALUE` – Filter versions by version number
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x |  |
| Version | x | x | x |
| Description | x | x |  |
| Lifecycle environments | x | x |  |

**Search and order fields**

- `content_view_id` – integer
- `repository` – string
- `version` – string

### 23.15.5. content-view version promote

Promote a content view version

**Usage**

```
# hammer content-view version promote [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--description VALUE` – The description for the content view version promotion
- `--force` – Force content view promotion and bypass lifecycle environment restriction
- `--from-lifecycle-environment VALUE` – Environment name from where to promote its version from (if version is unknown)
- `--from-lifecycle-environment-id VALUE` Id of the environment from where to promote its version from (if version is unknown)
- `--id NUMBER` – Content view version identifier
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--to-lifecycle-environment VALUE` – Name of the target environment
- `--to-lifecycle-environment-id VALUE` – Id of the target environment
- `--version VALUE` – Content view version number
- `-h`, `--help` – Print help

### 23.15.6. content-view version republish-repositories

Forces a republish of the version’s repositories' metadata

**Usage**

```
# hammer content-view version republish-repositories [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--force BOOLEAN` – Force metadata regeneration to proceed. Dangerous operation when version has repositories with the `Complete Mirroring` mirroring policy
- `--id NUMBER` – Content view version identifier
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--version VALUE` – Content view version number
- `-h`, `--help` – Print help

### 23.15.7. content-view version update

Update a content view version

**Usage**

```
# hammer content-view version update [OPTIONS]
```

**Options**

- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--description VALUE` – The description for the content view version
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--id NUMBER` – Content view version identifier
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` ID of the environment
- `--new-version VALUE`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--version VALUE` – Content view version number
- `-h`, `--help` – Print help

### 23.15.8. content-view version verify-checksum

Verify checksum of repository contents in the content view version

**Usage**

```
# hammer content-view version verify-checksum [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Content view numeric identifier
- `--id NUMBER` – Content view version identifier
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--version VALUE` – Content view version number
- `-h`, `--help` – Print help
