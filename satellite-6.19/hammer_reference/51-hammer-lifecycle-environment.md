---
title: "lifecycle-environment"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "51"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-lifecycle-environment"
---
# Chapter 51. lifecycle-environment

Manipulate lifecycle_environments on the server

**Usage**

```
# hammer lifecycle-environment [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 51.1. lifecycle-environment create

Create an environment

**Usage**

```
# hammer lifecycle-environment create [OPTIONS]
```

**Options**

- `--description VALUE` – Description of the environment
- `--label VALUE` – Label of the environment
- `--name VALUE` – Name of the environment
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Name of organization
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--path-id NUMBER` – If you are adding an environment to an existing path after Library, pass the ID of the environment that is the current successor of Library in the path. It has to be the id of the old environment following library in this path.
- `--prior VALUE` – Name of the prior environment
- `--prior-id NUMBER` – ID of an environment that is prior to the new environment in the chain. It has to be either the ID of Library or the ID of an environment at the end of a chain.
- `--registry-name-pattern VALUE` – Pattern for container image names
- `--registry-unauthenticated-pull BOOLEAN` Allow unauthenticed pull of container images
- `-h`, `--help` – Print help

## 51.2. lifecycle-environment delete

Destroy an environment

**Usage**

```
# hammer lifecycle-environment <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – ID of the environment
- `--name VALUE` – Lifecycle environment name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 51.3. lifecycle-environment info

Show an environment

**Usage**

```
# hammer lifecycle-environment <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – ID of the environment
- `--name VALUE` – Lifecycle environment name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – ID of the organization
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Label | x | x |  |
| Description | x | x |  |
| Organization | x | x |  |
| Library | x | x |  |
| Prior lifecycle environment | x | x |  |
| Unauthenticated pull | x | x |  |
| Registry name pattern | x | x |  |

## 51.4. lifecycle-environment list

List environments in an organization

**Usage**

```
# hammer lifecycle-environment <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--label VALUE` – Filter only environments containing this label
- `--library BOOLEAN` – Set true if you want to see only library environments
- `--name VALUE` – Filter only environments containing this name
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
| Prior | x | x |  |

**Search and order fields**

- `id` – integer
- `label` – string
- `name` – string
- `organization_id` – integer

## 51.5. lifecycle-environment paths

List environment paths

**Usage**

```
# hammer lifecycle-environment paths [OPTIONS]
```

**Options**

- `--content-source-id NUMBER` – Show whether each lifecycle environment is associated with the given Capsule id.
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--permission-type VALUE` – The associated permission type. One of (readable | promotable) Default: readable
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Lifecycle path | x | x |

## 51.6. lifecycle-environment update

Update an environment

**Usage**

```
# hammer lifecycle-environment update [OPTIONS]
```

**Options**

- `--async BOOLEAN` – Do not wait for the update action to finish. Default: true
- `--description VALUE` – Description of the environment
- `--id NUMBER` – ID of the environment
- `--name VALUE` – Lifecycle environment name to search by
- `--new-name VALUE` – New name to be given to the environment
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Name of the organization
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--registry-name-pattern VALUE` – Pattern for container image names
- `--registry-unauthenticated-pull BOOLEAN` Allow unauthenticed pull of container images
- `-h`, `--help` – Print help
