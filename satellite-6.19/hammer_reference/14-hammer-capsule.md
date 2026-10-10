---
title: "capsule"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "14"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-capsule"
---
# Chapter 14. capsule

Manipulate capsule

**Usage**

```
# hammer capsule [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 14.1. capsule content

Manage the capsule content

**Usage**

```
# hammer capsule content [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 14.1.1. capsule content add-lifecycle-environment

Add lifecycle environments to the Capsule

**Usage**

```
# hammer capsule content add-lifecycle-environment [OPTIONS]
```

**Options**

- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--id NUMBER` – Id of the Capsule
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Id of the lifecycle environment
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name
- `--organization-id VALUE` – Organization ID
- `-h`, `--help` – Print help

### 14.1.2. capsule content available-lifecycle-environments

List the lifecycle environments not attached to the Capsule

**Usage**

```
# hammer capsule content available-lifecycle-environments [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Id of the Capsule
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Id of the organization to limit environments on
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Organization | x | x |  |

### 14.1.3. capsule content cancel-synchronization

Cancel running Capsule synchronization

**Usage**

```
# hammer capsule content cancel-synchronization [OPTIONS]
```

**Options**

- `--id NUMBER` – Id of the Capsule
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

### 14.1.4. capsule content info

Get current Capsule synchronization status

**Usage**

```
# hammer capsule content info [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Id of the Capsule
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Id of the organization to get the status for
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Lifecycle environments/name | x | x |
| Lifecycle environments/organization | x | x |
| Lifecycle environments/content views/name | x | x |
| Lifecycle environments/content views/composite | x | x |
| Lifecycle environments/content views/rolling | x | x |
| Lifecycle environments/content views/last published | x | x |
| Lifecycle environments/content views/repositories/repository id | x | x |
| Lifecycle environments/content views/repositories/repository name | x | x |
| Lifecycle environments/content views/repositories/content counts/warning | x | x |
| Lifecycle environments/content views/repositories/content counts/packages | x | x |
| Lifecycle environments/content views/repositories/content counts/srpms | x | x |
| Lifecycle environments/content views/repositories/content counts/module streams | x | x |
| Lifecycle environments/content views/repositories/content counts/package groups | x | x |
| Lifecycle environments/content views/repositories/content counts/errata | x | x |
| Lifecycle environments/content views/repositories/content counts/debian packages | x | x |
| Lifecycle environments/content views/repositories/content counts/container tags | x | x |
| Lifecycle environments/content views/repositories/content counts/container ma…​ | x | x |
| Lifecycle environments/content views/repositories/content counts/container ma…​ | x | x |
| Lifecycle environments/content views/repositories/content counts/files | x | x |
| Lifecycle environments/content views/repositories/content counts/ansible coll…​ | x | x |
| Lifecycle environments/content views/repositories/content counts/ostree refs | x | x |
| Lifecycle environments/content views/repositories/content counts/python packages | x | x |

### 14.1.5. capsule content lifecycle-environments

List the lifecycle environments attached to the Capsule

**Usage**

```
# hammer capsule content lifecycle-environments [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Id of the Capsule
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Id of the organization to limit environments on
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Organization | x | x |  |

### 14.1.6. capsule content reclaim-space

Reclaim space from all On Demand repositories on a Capsule

**Usage**

```
# hammer capsule content reclaim-space [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Id of the Capsule
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

### 14.1.7. capsule content remove-lifecycle-environment

Remove lifecycle environments from the Capsule

**Usage**

```
# hammer capsule content remove-lifecycle-environment [OPTIONS]
```

**Options**

- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--id NUMBER` – Id of the Capsule
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Id of the lifecycle environment
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name
- `--organization-id VALUE` – Organization ID
- `-h`, `--help` – Print help

### 14.1.8. capsule content synchronization-status

Get current Capsule synchronization status

**Usage**

```
# hammer capsule content synchronization-status [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Id of the Capsule
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Id of the organization to get the status for
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Last sync | x | x |
| Status | x | x |
| Currently running sync tasks/task id | x | x |
| Currently running sync tasks/progress | x | x |
| Last failure/task id | x | x |
| Last failure/messages | x | x |

### 14.1.9. capsule content synchronize

Synchronize the content to the Capsule

**Usage**

```
# hammer capsule content synchronize [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Id of the content view to limit the synchronization on
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--id NUMBER` – Id of the Capsule
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Id of the environment to limit the synchronization on
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name
- `--organization-id VALUE` – Organization ID
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Id of the repository to limit the synchronization on
- `--skip-metadata-check BOOLEAN` – Skip metadata check on each repository on the Capsule
- `-h`, `--help` – Print help

### 14.1.10. capsule content update-counts

Update content counts for the Capsule

**Usage**

```
# hammer capsule content update-counts [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Id of the content view to limit the content counting on
- `--id NUMBER` – Id of the Capsule
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Id of the environment to limit the content counting on
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name
- `--organization-id VALUE` – Organization ID
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Id of the repository to limit the content counting on
- `-h`, `--help` – Print help

### 14.1.11. capsule content verify-checksum

Check for missing or corrupted artifacts, and attempt to redownload them.

**Usage**

```
# hammer capsule content verify-checksum [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – Id of the content view to limit verifying checksum on
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--id NUMBER` – Id of the Capsule
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` Id of the environment to limit verifying checksum on
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name
- `--organization-id VALUE` – Organization ID
- `--repository VALUE` – Repository name to search by
- `--repository-id NUMBER` – Id of the repository to limit verifying checksum on
- `-h`, `--help` – Print help

## 14.2. capsule create

Create a Capsule

**Usage**

```
# hammer capsule create [OPTIONS]
```

**Options**

- `--download-policy VALUE` – Download Policy of the capsule, must be one of on_demand, immediate, inherit, streamed
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – Id of the HTTP proxy to use with alternate content sources
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--url VALUE`
- `-h`, `--help` – Print help

## 14.3. capsule delete

Delete a Capsule

**Usage**

```
# hammer capsule <delete|destroy> [OPTIONS]
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

## 14.4. capsule import-classes

Import Puppet classes from Puppet proxy

**Usage**

```
# hammer capsule import-classes [OPTIONS]
```

**Options**

- `--dryrun` – Do not run the import
- `--except VALUE` – Optional comma-delimited stringcontaining either `new`, `updated`, or `obsolete`that is used to limit the imported Puppet classes
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--puppet-environment VALUE` – Puppet environment name
- `--puppet-environment-id VALUE`
- `-h`, `--help` – Print help

## 14.5. capsule import-subnets

Import subnets from Capsule

**Usage**

```
# hammer capsule import-subnets [OPTIONS]
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

## 14.6. capsule info

Show a Capsule

**Usage**

```
# hammer capsule <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--include-status BOOLEAN` – Flag to indicate whether to include status or not
- `--include-version BOOLEAN` – Flag to indicate whether to include version or not
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
| Status | x | x |  |
| Url | x | x |  |
| Features | x | x |  |
| Version | x | x |  |
| Host count | x | x |  |
| Features/name | x | x |  |
| Features/version | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 14.7. capsule list

List all Capsules

**Usage**

```
# hammer capsule <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--include-status BOOLEAN` – Flag to indicate whether to include status or not
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Scope by locations
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Scope by organizations
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
| Status | x | x |  |
| Url | x | x |  |
| Features | x | x |  |

**Search and order fields**

- `feature` – string
- `id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
- `url` – string

## 14.8. capsule refresh-features

Refresh Capsule features

**Usage**

```
# hammer capsule refresh-features [OPTIONS]
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

## 14.9. capsule update

Update a Capsule

**Usage**

```
# hammer capsule update [OPTIONS]
```

**Options**

- `--download-policy VALUE` – Download Policy of the capsule, must be one of on_demand, immediate, inherit, streamed
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – Id of the HTTP proxy to use with alternate content sources
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE`
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--url VALUE`
- `-h`, `--help` – Print help
