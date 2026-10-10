---
title: "flatpak-remote"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "38"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-flatpak-remote"
---
# Chapter 38. flatpak-remote

Manipulate flatpak remotes

**Usage**

```
# hammer flatpak-remote [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 38.1. flatpak-remote create

Create a flatpak remote

**Usage**

```
# hammer flatpak-remote create [OPTIONS]
```

**Options**

- `--description VALUE` – Description of the flatpak remote
- `--name VALUE` – Name
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--token VALUE` – Token/password for the flatpak remote
- `--url VALUE` – Base URL of the flatpak registry index, ex: flatpaks.redhat.io/rhel/ , registry.fedoraproject.org/.
- `--username VALUE` – Username for the flatpak remote
- `-h`, `--help` – Print help

## 38.2. flatpak-remote delete

Delete a flatpak remote

**Usage**

```
# hammer flatpak-remote <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – Flatpak remote numeric identifier
- `--name VALUE` – Flatpak remote name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 38.3. flatpak-remote info

Show a flatpak remote

**Usage**

```
# hammer flatpak-remote <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Flatpak remote numeric identifier
- `--name VALUE` – Flatpak remote name to search by
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
| Description | x | x |  |
| Flatpak index url | x | x |  |
| Username | x | x |  |
| Registry url | x | x |  |
| Organization/id | x | x |  |
| Organization/name | x | x |  |
| Organization/label | x | x |  |

## 38.4. flatpak-remote list

List flatpak remotes

**Usage**

```
# hammer flatpak-remote <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--name VALUE` – Name of the flatpak remote
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Url | x | x |  |
| Description | x | x |  |
| Username | x | x |  |
| Registry url | x | x |  |

**Search and order fields**

- `name` – string
- `organization_id` – integer
- `registry_url` – string
- `url` – string

## 38.5. flatpak-remote remote-repository

View and manage flatpak remote repositories

**Usage**

```
# hammer flatpak-remote remote-repository [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 38.5.1. flatpak-remote remote-repository info

Show a flatpak remote repository

**Usage**

```
# hammer flatpak-remote remote-repository <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--flatpak-remote VALUE` – Flatpak remote name to search by
- `--flatpak-remote-id NUMBER`
- `--id NUMBER` – Flatpak remote repository numeric identifier
- `--manifests BOOLEAN` – Include manifests
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Label | x | x |  |
| Flatpak remote id | x | x |  |
| Flatpak remote name | x | x |  |
| Flatpak remote url | x | x |  |
| Manifests/manifest name | x | x |  |
| Manifests/manifest digest | x | x |  |
| Manifests/manifest tags | x | x |  |

### 38.5.2. flatpak-remote remote-repository list

List flatpak remote repositories

**Usage**

```
# hammer flatpak-remote remote-repository <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--flatpak-remote VALUE` – Flatpak remote name to search by
- `--flatpak-remote-id NUMBER` – ID of flatpak remote to show repositories of
- `--full-result BOOLEAN` – Whether or not to show all results
- `--label VALUE` – Label of the flatpak remote
- `--name VALUE` – Name of the flatpak remote repository
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
| Label | x | x |  |

**Search and order fields**

- `flatpak_remote_id` – integer
- `id` – integer
- `label` – string
- `name` – string

### 38.5.3. flatpak-remote remote-repository mirror

Mirror a flatpak remote repository

**Usage**

```
# hammer flatpak-remote remote-repository mirror [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--dependency-ids LIST` – Array of dependency repository IDs to mirror along with the main repository
- `--flatpak-remote VALUE` – Flatpak remote name to search by
- `--flatpak-remote-id NUMBER`
- `--id NUMBER` – Flatpak remote repository numeric identifier
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product ID to mirror the remote repository to
- `--product-name VALUE` – Name of the product to mirror the remote repository to
- `-h`, `--help` – Print help

## 38.6. flatpak-remote scan

Scan a flatpak remote

**Usage**

```
# hammer flatpak-remote scan [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Flatpak remote numeric identifier
- `--name VALUE` – Flatpak remote name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 38.7. flatpak-remote update

Update a flatpak remote

**Usage**

```
# hammer flatpak-remote update [OPTIONS]
```

**Options**

- `--description VALUE` – Description of the flatpak remote
- `--id NUMBER` – Flatpak remote numeric identifier
- `--name VALUE` – Name
- `--new-name VALUE` – Name
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--token VALUE` – Token/password for the flatpak remote
- `--url VALUE` – Base URL of the flatpak registry index, ex: flatpaks.redhat.io/rhel/ , registry.fedoraproject.org/.
- `--username VALUE` – Username for the flatpak remote
- `-h`, `--help` – Print help
