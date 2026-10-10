---
title: "report-template"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "74"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-report-template"
---
# Chapter 74. report-template

Manipulate report templates

**Usage**

```
# hammer report-template [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 74.1. report-template clone

Clone a template

**Usage**

```
# hammer report-template clone [OPTIONS]
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

## 74.2. report-template create

Create a report template

**Usage**

```
# hammer report-template create [OPTIONS]
```

**Options**

- `--audit-comment VALUE`
- `--default BOOLEAN` – Whether or not the template is added automatically to new organizations and locations
- `--description VALUE`
- `--file FILE` – Path to a file that contains the report template content
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
- `-h`, `--help` – Print help
- `-i`, `--interactive` – Open empty template in an $EDITOR. Upload the result

## 74.3. report-template delete

Delete a report template

**Usage**

```
# hammer report-template <delete|destroy> [OPTIONS]
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

## 74.4. report-template dump

View report content

**Usage**

```
# hammer report-template dump [OPTIONS]
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

## 74.5. report-template export

Export a report template to ERB

**Usage**

```
# hammer report-template export [OPTIONS]
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

## 74.6. report-template generate

Generate report

**Usage**

```
# hammer report-template generate [OPTIONS]
```

**Options**

- `--gzip BOOLEAN` – Compress the report uzing gzip
- `--id VALUE`
- `--inputs KEY_VALUE_LIST` – Specify inputs
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--path VALUE` – Path to directory where downloaded content will be saved
- `--report-format ENUM` – Report format, defaults to `csv` Possible value(s): `csv`, `json`, `yaml`, `html`
- `-h`, `--help` – Print help

## 74.7. report-template import

Import a report template

**Usage**

```
# hammer report-template import [OPTIONS]
```

**Options**

- `--associate ENUM` – Determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata Possible value(s): `new`, `always`, `never`
- `--default BOOLEAN` – Makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default)
- `--file FILE` – Path to a file that contains the report template content including metadata
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

## 74.8. report-template info

Show a report template

**Usage**

```
# hammer report-template <info|show> [OPTIONS]
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
| Cloned from id | x | x |  |
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

## 74.9. report-template list

List all report templates

**Usage**

```
# hammer report-template <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
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

**Search and order fields**

- `default` – Values: true, false
- `id` – integer
- `location` – string
- `location_id` – integer
- `locked` – Values: true, false
- `name` – string
- `organization` – string
- `organization_id` – integer
- `snippet` – Values: true, false
- `template` – text

## 74.10. report-template report-data

Downloads a generated report

**Usage**

```
# hammer report-template report-data [OPTIONS]
```

**Options**

- `--id VALUE`
- `--job-id VALUE` – ID assigned to generating job by the schedule command
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--path VALUE` – Path to directory where downloaded content will be saved
- `-h`, `--help` – Print help

## 74.11. report-template schedule

Schedule generating of a report

**Usage**

```
# hammer report-template schedule [OPTIONS]
```

**Options**

- `--generate-at VALUE` – UTC time to generate report at
- `--gzip BOOLEAN` – Compress the report using gzip
- `--id VALUE`
- `--inputs KEY_VALUE_LIST` – Specify inputs
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--mail-to VALUE` – If set, scheduled report will be delivered via e-mail. Use `,` to separate multiple email addresses.
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--path VALUE` – Path to directory where downloaded content will be saved. Only usable if wait is specified
- `--report-format ENUM` – Report format, defaults to `csv` Possible value(s): `csv`, `json`, `yaml`, `html`
- `--wait` – Turns a command to be active, wait for the result and download it right away
- `-h`, `--help` – Print help

## 74.12. report-template update

Update a report template

**Usage**

```
# hammer report-template update [OPTIONS]
```

**Options**

- `--audit-comment VALUE`
- `--default BOOLEAN` – Whether or not the template is added automatically to new organizations and locations
- `--description VALUE`
- `--file FILE` – Path to a file that contains the report template content
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
- `-h`, `--help` – Print help
- `-i`, `--interactive` – Dump existing template and open it in an $EDITOR. Update with the result
