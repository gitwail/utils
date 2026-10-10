---
title: "content-credentials"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "19"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-content-credentials"
---
# Chapter 19. content-credentials

Manipulate content credentials on the server

**Usage**

```
# hammer content-credentials [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 19.1. content-credentials create

Create a Content Credential

**Usage**

```
# hammer content-credentials create [OPTIONS]
```

**Options**

- `--content-type VALUE` – Type of content: “cert”, “gpg_key”
- `--name VALUE` – Name of the Content Credential
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization identifier
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--path FILE` – Key file
- `-h`, `--help` – Print help

## 19.2. content-credentials delete

Destroy a Content Credential

**Usage**

```
# hammer content-credentials <delete|destroy> [OPTIONS]
```

**Options**

- `--id NUMBER` – Content Credential ID
- `--name VALUE` – Name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `-h`, `--help` – Print help

## 19.3. content-credentials info

Show a Content Credential

**Usage**

```
# hammer content-credentials <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Content Credential numeric identifier
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
| Organization | x | x |  |
| Repositories/id | x | x |  |
| Repositories/name | x | x |  |
| Repositories/content type | x | x |  |
| Repositories/product | x | x |  |
| Content | x | x |  |

## 19.4. content-credentials list

List Content Credentials

**Usage**

```
# hammer content-credentials <list|index> [OPTIONS]
```

**Options**

- `--content-type VALUE` – Type of content
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--name VALUE` – Name of the Content Credential
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
| Content type | x | x |  |

## 19.5. content-credentials update

Update a Content Credential

**Usage**

```
# hammer content-credentials update [OPTIONS]
```

**Options**

- `--content-type VALUE` – Type of content: “cert”, “gpg_key”
- `--id NUMBER` – Content Credential ID
- `--name VALUE` – Name of the Content Credential
- `--new-name VALUE` – Name of the Content Credential
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--path FILE` – Key file
- `-h`, `--help` – Print help
