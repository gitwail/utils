---
title: "webhook-template"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "96"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-webhook-template"
---
# Chapter 96. webhook-template

Manipulate webhook templates

**Usage**

```
# hammer webhook-template [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 96.1. webhook-template clone

Clone a template

**Usage**

```
# hammer webhook-template clone [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Template name
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 96.2. webhook-template create

Create a webhook template

**Usage**

```
# hammer webhook-template create [OPTIONS]
```

**Options**

- `--audit-comment VALUE`
- `--default BOOLEAN` – Whether or not the template is added automatically to new organizations and locations
- `--description VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--locked BOOLEAN` – Whether or not the template is locked for editing
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--snippet BOOLEAN`
- `--template VALUE`
- `-h`, `--help` – Print help

## 96.3. webhook-template delete

Delete a webhook template

**Usage**

```
# hammer webhook-template <delete|destroy> [OPTIONS]
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

## 96.4. webhook-template dump

View webhook template content

**Usage**

```
# hammer webhook-template dump [OPTIONS]
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

|  |
| --- |
| FIELDS |

## 96.5. webhook-template export

Export a webhook template to ERB

**Usage**

```
# hammer webhook-template export [OPTIONS]
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
- `--path VALUE` – Path to directory where downloaded content will be saved
- `-h`, `--help` – Print help

## 96.6. webhook-template import

Import a webhook template

**Usage**

```
# hammer webhook-template import [OPTIONS]
```

**Options**

- `--associate ENUM` – Determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata Possible value(s): `new`, `always`, `never`
- `--default BOOLEAN` – Makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default)
- `--file FILE` – Path to a file that contains the webhook template content including metadata
- `--force BOOLEAN` – Use if you want update locked templates
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--lock BOOLEAN` – Lock imported templates (false by default)
- `--name VALUE` – Template name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `-h`, `--help` – Print help

## 96.7. webhook-template info

Show webhook template details

**Usage**

```
# hammer webhook-template <info|show> [OPTIONS]
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
| Description | x | x |  |
| Locked | x | x |  |
| Default | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Template inputs/id | x | x |  |
| Template inputs/name | x | x |  |
| Template inputs/description | x | x |  |
| Template inputs/required | x | x |  |
| Template inputs/options | x | x |  |

## 96.8. webhook-template list

List webhook templates

**Usage**

```
# hammer webhook-template <list|index> [OPTIONS]
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

**Search and order fields**

- `default` – Values: true, false
- `location` – string
- `location_id` – integer
- `locked` – Values: true, false
- `name` – string
- `organization` – string
- `organization_id` – integer
- `snippet` – Values: true, false
- `template` – text

## 96.9. webhook-template update

Update a webhook template

**Usage**

```
# hammer webhook-template update [OPTIONS]
```

**Options**

- `--audit-comment VALUE`
- `--default BOOLEAN` – Whether or not the template is added automatically to new organizations and locations
- `--description VALUE`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--locked BOOLEAN` – Whether or not the template is locked for editing
- `--name VALUE`
- `--new-name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--snippet BOOLEAN`
- `--template VALUE`
- `-h`, `--help` – Print help
