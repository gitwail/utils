---
title: "template"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "90"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-template"
---
# Chapter 90. template

Manipulate provisioning templates

**Usage**

```
# hammer template [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 90.1. template add-operatingsystem

Associate an operating system

**Usage**

```
# hammer template add-operatingsystem [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 90.2. template build-pxe-default

Update the default PXE menu on all configured TFTP servers

**Usage**

```
# hammer template build-pxe-default [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 90.3. template clone

Clone a provision template

**Usage**

```
# hammer template clone [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Template name
- `--new-name VALUE` – Template name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 90.4. template combination

Manage template combinations

**Usage**

```
# hammer template combination [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 90.4.1. template combination create

Add a template combination

**Usage**

```
# hammer template combination create [OPTIONS]
```

**Options**

- `--environment VALUE` – Name to search by
- `--environment-id NUMBER` – Environment id
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id VALUE` ID of config template
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` – ID of associated Puppet environment
- `-h`, `--help` – Print help

### 90.4.2. template combination delete

Delete a template combination

**Usage**

```
# hammer template combination <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 90.4.3. template combination info

Show template combination

**Usage**

```
# hammer template combination <info|show> [OPTIONS]
```

**Options**

- `--environment VALUE` – Name to search by
- `--environment-id VALUE` – ID of Puppet environment
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id VALUE` ID of config template
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` – ID of associated Puppet environment
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Provisioning template id | x | x |  |
| Provisioning template name | x | x |  |
| Hostgroup id | x | x |  |
| Hostgroup name | x | x |  |
| Puppet environment | x | x |  |
| Puppet environment id | x | x |  |
| Puppet environment name | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

### 90.4.4. template combination list

List template combination

**Usage**

```
# hammer template combination <list|index> [OPTIONS]
```

**Options**

- `--environment VALUE` – Name to search by
- `--environment-id VALUE` – ID of Puppet environment
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id VALUE` ID of config template
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Provisioning template | x | x |  |
| Hostgroup | x | x |  |
| Puppet environment | x | x |  |

### 90.4.5. template combination update

Update template combination

**Usage**

```
# hammer template combination update [OPTIONS]
```

**Options**

- `--environment VALUE` – Name to search by
- `--environment-id NUMBER` – Environment id
- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id VALUE` – ID of host group
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id VALUE` ID of config template
- `--puppet-environment VALUE` – Name of associated Puppet environment
- `--puppet-environment-id NUMBER` – ID of associated Puppet environment
- `-h`, `--help` – Print help

## 90.5. template create

Create a provisioning template

**Usage**

```
# hammer template create [OPTIONS]
```

**Options**

- `--audit-comment VALUE`
- `--description VALUE`
- `--file FILE` – Path to a file that contains the template
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--locked BOOLEAN` – Whether or not the template is locked for editing
- `--name VALUE` – Template name
- `--operatingsystem-ids LIST` – Array of operating system IDs to associate with the template
- `--operatingsystems LIST`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--type VALUE` – Template type. Eg. snippet, script, provision
- `-h`, `--help` – Print help

## 90.6. template delete

Delete a provisioning template

**Usage**

```
# hammer template <delete|destroy> [OPTIONS]
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

## 90.7. template dump

View provisioning template content

**Usage**

```
# hammer template dump [OPTIONS]
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

## 90.8. template export

Export a provisioning template to ERB

**Usage**

```
# hammer template export [OPTIONS]
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

## 90.9. template import

Import a provisioning template

**Usage**

```
# hammer template import [OPTIONS]
```

**Options**

- `--associate ENUM` – Determines when the template should associate objects based on metadata, new means only when new template is being created, always means both for new and existing template which is only being updated, never ignores metadata Possible value(s): `new`, `always`, `never`
- `--default BOOLEAN` – Makes the template default meaning it will be automatically associated with newly created organizations and locations (false by default)
- `--file FILE` – Path to a file that contains the template content including metadata
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

## 90.10. template info

Show provisioning template details

**Usage**

```
# hammer template <info|show> [OPTIONS]
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
| Type | x | x |  |
| Description | x | x |  |
| Locked | x | x |  |
| Cloned from id | x | x |  |
| Operating systems/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Template combinations/hostgroup name | x | x |  |
| Template combinations/environment name | x | x |  |

## 90.11. template kinds

List available provisioning template kinds

**Usage**

```
# hammer template kinds [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Name | x | x | x |

## 90.12. template list

List provisioning templates

**Usage**

```
# hammer template <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Scope by locations
- `--location-title VALUE` – Set the current location context for the request
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER` – ID of operating system
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
| Type | x | x |  |

**Search and order fields**

- `default_template` – Values: true, false
- `environment` – string
- `hostgroup` – string
- `id` – integer
- `kind` – string
- `location` – string
- `location_id` – integer
- `locked` – Values: true, false
- `name` – string
- `operatingsystem` – string
- `organization` – string
- `organization_id` – integer
- `snippet` – Values: true, false
- `supported` – Values: true, false
- `template` – text
- `vendor` – string

## 90.13. template remove-operatingsystem

Disassociate an operating system

**Usage**

```
# hammer template remove-operatingsystem [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Name to search by
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 90.14. template update

Update a provisioning template

**Usage**

```
# hammer template update [OPTIONS]
```

**Options**

- `--audit-comment VALUE`
- `--description VALUE`
- `--file FILE` – Path to a file that contains the template
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--locked BOOLEAN` – Whether or not the template is locked for editing
- `--name VALUE` – Template name
- `--new-name VALUE` – Template name
- `--operatingsystem-ids LIST` – Array of operating system IDs to associate with the template
- `--operatingsystems LIST`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--type VALUE` – Template type. Eg. snippet, script, provision
- `-h`, `--help` – Print help
