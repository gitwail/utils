---
title: "proxy"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "67"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-proxy"
---
# Chapter 67. proxy

Manipulate smart proxies

**Usage**

```
# hammer proxy [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 67.1. proxy content

Manage the capsule content

**Usage**

```
# hammer proxy content [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 67.1.1. proxy content add-lifecycle-environment

Add lifecycle environments to the Capsule

**Usage**

```
# hammer proxy content add-lifecycle-environment [OPTIONS]
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

### 67.1.2. proxy content available-lifecycle-environments

List the lifecycle environments not attached to the Capsule

**Usage**

```
# hammer proxy content available-lifecycle-environments [OPTIONS]
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

### 67.1.3. proxy content cancel-synchronization

Cancel running Capsule synchronization

**Usage**

```
# hammer proxy content cancel-synchronization [OPTIONS]
```

**Options**

- `--id NUMBER` – Id of the Capsule
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

### 67.1.4. proxy content info

Get current Capsule synchronization status

**Usage**

```
# hammer proxy content info [OPTIONS]
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

### 67.1.5. proxy content lifecycle-environments

List the lifecycle environments attached to the Capsule

**Usage**

```
# hammer proxy content lifecycle-environments [OPTIONS]
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

### 67.1.6. proxy content reclaim-space

Reclaim space from all On Demand repositories on a Capsule

**Usage**

```
# hammer proxy content reclaim-space [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Id of the Capsule
- `--name VALUE` – Name to search by
- `-h`, `--help` – Print help

### 67.1.7. proxy content remove-lifecycle-environment

Remove lifecycle environments from the Capsule

**Usage**

```
# hammer proxy content remove-lifecycle-environment [OPTIONS]
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

### 67.1.8. proxy content synchronization-status

Get current Capsule synchronization status

**Usage**

```
# hammer proxy content synchronization-status [OPTIONS]
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

### 67.1.9. proxy content synchronize

Synchronize the content to the Capsule

**Usage**

```
# hammer proxy content synchronize [OPTIONS]
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

### 67.1.10. proxy content update-counts

Update content counts for the Capsule

**Usage**

```
# hammer proxy content update-counts [OPTIONS]
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

### 67.1.11. proxy content verify-checksum

Check for missing or corrupted artifacts, and attempt to redownload them.

**Usage**

```
# hammer proxy content verify-checksum [OPTIONS]
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

## 67.2. proxy create

Create a Capsule

**Usage**

```
# hammer proxy create [OPTIONS]
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

## 67.3. proxy delete

Delete a Capsule

**Usage**

```
# hammer proxy <delete|destroy> [OPTIONS]
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

## 67.4. proxy import-classes

Import Puppet classes from Puppet proxy

**Usage**

```
# hammer proxy import-classes [OPTIONS]
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

## 67.5. proxy import-subnets

Import subnets from Capsule

**Usage**

```
# hammer proxy import-subnets [OPTIONS]
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

## 67.6. proxy info

Show a Capsule

**Usage**

```
# hammer proxy <info|show> [OPTIONS]
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

## 67.7. proxy list

List all Capsules

**Usage**

```
# hammer proxy <list|index> [OPTIONS]
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

**Search and order fields**

- `feature` – string
- `id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
- `url` – string

## 67.8. proxy refresh-features

Refresh Capsule features

**Usage**

```
# hammer proxy refresh-features [OPTIONS]
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

## 67.9. proxy update

Update a Capsule

**Usage**

```
# hammer proxy update [OPTIONS]
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
