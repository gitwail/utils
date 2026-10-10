---
title: "job-template"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "50"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-job-template"
---
# Chapter 50. job-template

Manage job templates

**Usage**

```
# hammer job-template [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 50.1. job-template clone

Clone a job template

**Usage**

```
# hammer job-template clone [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--new-name VALUE` – Name for the cloned template
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 50.2. job-template create

Create a job template

**Usage**

```
# hammer job-template create [OPTIONS]
```

**Options**

- `--ansible-callback-enabled BOOLEAN` Enable the callback plugin for this template
- `--ansible-check-mode BOOLEAN` – Enable Ansible Check Mode for this template
- `--audit-comment VALUE`
- `--current-user BOOLEAN` – Whether the current user login should be used as the effective user
- `--description VALUE`
- `--description-format VALUE` – This template is used to generate the description. Input values can be used using the syntax %{package}. You may also include the job category and template name using %{job_category} and %{template_name}.
- `--file FILE` – Path to a file that contains the template
- `--job-category VALUE` – Job category
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--locked BOOLEAN` – Whether or not the template is locked for editing
- `--name VALUE` – Template name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--overridable BOOLEAN` – Whether it should be allowed to override the effective user from the invocation form.
- `--provider-type ENUM` – Provider type Possible value(s): `SSH`, `script`, `Ansible`
- `--snippet BOOLEAN`
- `--value VALUE` – What user should be used to run the script (using sudo-like mechanisms)
- `-h`, `--help` – Print help

## 50.3. job-template delete

Delete a job template

**Usage**

```
# hammer job-template <delete|destroy> [OPTIONS]
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

## 50.4. job-template dump

View job template content

**Usage**

```
# hammer job-template dump [OPTIONS]
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

## 50.5. job-template export

Export a template including all metadata

**Usage**

```
# hammer job-template export [OPTIONS]
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

## 50.6. job-template import

Import a job template from ERB

**Usage**

```
# hammer job-template import [OPTIONS]
```

**Options**

- `--associate ENUM` – Determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata Possible value(s): `new`, `always`, `never`
- `--default BOOLEAN` – Makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default)
- `--file FILE` – Path to a file that contains the template - must include ERB metadata
- `--force BOOLEAN` – Use if you want update locked templates
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--lock BOOLEAN` – Lock imported templates (false by default)
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--overwrite BOOLEAN` – Overwrite template if it already exists
- `-h`, `--help` – Print help

## 50.7. job-template info

Show job template details

**Usage**

```
# hammer job-template <info|show> [OPTIONS]
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
| Job category | x | x |  |
| Provider | x | x |  |
| Type | x | x |  |
| Ansible callback enabled | x | x |  |
| Ansible check mode enabled | x | x |  |
| Description | x | x |  |
| Cloned from id | x | x |  |
| Inputs | x | x |  |
| Locked | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |

## 50.8. job-template list

List job templates

**Usage**

```
# hammer job-template <list|index> [OPTIONS]
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
| Job category | x | x |  |
| Provider | x | x |  |
| Type | x | x |  |

## 50.9. job-template update

Update a job template

**Usage**

```
# hammer job-template update [OPTIONS]
```

**Options**

- `--ansible-callback-enabled BOOLEAN` Enable the callback plugin for this template
- `--ansible-check-mode BOOLEAN` – Enable Ansible Check Mode for this template
- `--audit-comment VALUE`
- `--current-user BOOLEAN` – Whether the current user login should be used as the effective user
- `--description VALUE`
- `--description-format VALUE` – This template is used to generate the description. Input values can be used using the syntax %{package}. You may also include the job category and template name using %{job_category} and %{template_name}.
- `--file FILE` – Path to a file that contains the template
- `--id VALUE`
- `--job-category VALUE` – Job category
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--locked BOOLEAN` – Whether or not the template is locked for editing
- `--name VALUE` – Template name
- `--new-name VALUE` – Template name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--overridable BOOLEAN` – Whether it should be allowed to override the effective user from the invocation form.
- `--provider-type ENUM` – Provider type Possible value(s): `SSH`, `script`, `Ansible`
- `--snippet BOOLEAN`
- `--value VALUE` – What user should be used to run the script (using sudo-like mechanisms)
- `-h`, `--help` – Print help
