---
title: "organization"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "57"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-organization"
---
# Chapter 57. organization

Manipulate organizations

**Usage**

```
# hammer organization [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 57.1. organization add-compute-resource

Associate a compute resource

**Usage**

```
# hammer organization add-compute-resource [OPTIONS]
```

**Options**

- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id NUMBER`
- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.2. organization add-domain

Associate a domain

**Usage**

```
# hammer organization add-domain [OPTIONS]
```

**Options**

- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Numerical ID or domain name
- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.3. organization add-hostgroup

Associate a hostgroup

**Usage**

```
# hammer organization add-hostgroup [OPTIONS]
```

**Options**

- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER`
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.4. organization add-location

Associate a location

**Usage**

```
# hammer organization add-location [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER`
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.5. organization add-medium

Associate a medium

**Usage**

```
# hammer organization add-medium [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--medium VALUE` – Medium name
- `--medium-id NUMBER`
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.6. organization add-provisioning-template

Associate provisioning templates

**Usage**

```
# hammer organization add-provisioning-template [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id NUMBER`
- `--provisioning-template-ids LIST` – List of provisioning template ids
- `--provisioning-template-search VALUE` Provisioning template name regex to search, all matching templates will be associated
- `--provisioning-templates LIST` – List of provisioning template names
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.7. organization add-smart-proxy

Associate a smart proxy

**Usage**

```
# hammer organization add-smart-proxy [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--smart-proxy VALUE` – Name to search by
- `--smart-proxy-id NUMBER`
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.8. organization add-subnet

Associate a subnet

**Usage**

```
# hammer organization add-subnet [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER`
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.9. organization add-user

Associate an user

**Usage**

```
# hammer organization add-user [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id NUMBER`
- `-h`, `--help` – Print help

## 57.10. organization configure-cdn

Update the CDN configuration

**Usage**

```
# hammer organization configure-cdn [OPTIONS]
```

**Options**

- `--custom-cdn-auth-enabled BOOLEAN` – If product certificates should be used to authenticate to a custom CDN.
- `--id VALUE` – ID of the Organization
- `--label VALUE` – Organization label to search by
- `--name VALUE` – Organization name to search by
- `--password VALUE` – Password for authentication. Relevant only for `upstream_server` type.
- `--ssl-ca-credential-id NUMBER` – Content Credential to use for SSL CA. Relevant only for `upstream_server` type.
- `--title VALUE` – Organization title
- `--type VALUE` – CDN configuration type. One of redhat_cdn, network_sync, export_sync, custom_cdn.
- `--upstream-content-view-label VALUE` – Upstream Content View Label, default: Default_Organization_View. Relevant only for `upstream_server` type.
- `--upstream-lifecycle-environment-label VALUE` Upstream Lifecycle Environment, default: Library. Relevant only for `upstream_server` type.
- `--upstream-organization-label VALUE` – Upstream organization to sync CDN content from. Relevant only for `upstream_server` type.
- `--url VALUE` – Upstream Satellite server to sync CDN content from. Relevant only for `upstream_server` type.
- `--username VALUE` – Username for authentication. Relevant only for `upstream_server` type.
- `-h`, `--help` – Print help

## 57.11. organization create

Create organization

**Usage**

```
# hammer organization create [OPTIONS]
```

**Options**

- `--compute-resource-ids LIST` – Compute resource IDs
- `--compute-resources LIST`
- `--description VALUE`
- `--domain-ids LIST` – Domain IDs
- `--domains LIST`
- `--environment-ids LIST` – Environment IDs
- `--environments LIST`
- `--hostgroup-ids LIST` – Host group IDs
- `--hostgroup-titles LIST`
- `--hostgroups LIST`
- `--ignore-types LIST` – List of resources types that will be automatically associated
- `--label VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – Associated location IDs
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--media LIST`
- `--medium-ids LIST` – Medium IDs
- `--name VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Set the current organization context for the request
- `--partition-table-ids LIST` – Partition template IDs
- `--partition-tables LIST`
- `--provisioning-template-ids LIST` Provisioning template IDs
- `--provisioning-templates LIST`
- `--puppet-environment-ids LIST` – IDs of associated Puppet environment
- `--puppet-environments VALUE` – Names of associated Puppet environment
- `--realm-ids LIST` – Realm IDs
- `--realms LIST`
- `--smart-proxies LIST`
- `--smart-proxy-ids LIST` – Capsule IDs
- `--subnet-ids LIST` – Subnet IDs
- `--subnets LIST`
- `--user-ids LIST` – User IDs
- `--users LIST`
- `-h`, `--help` – Print help

## 57.12. organization delete

Delete an organization

**Usage**

```
# hammer organization <delete|destroy> [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id VALUE`
- `--label VALUE` – Organization label to search by
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Set the current organization context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.13. organization delete-parameter

Delete parameter for an organization

**Usage**

```
# hammer organization delete-parameter [OPTIONS]
```

**Options**

- `--name VALUE` – Parameter name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Organization ID
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.14. organization info

Show organization

**Usage**

```
# hammer organization <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--label VALUE` – Organization label to search by
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Set the current organization context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Title | x | x | x |
| Name | x | x | x |
| Description | x | x |  |
| Parent | x | x |  |
| Users/ | x | x |  |
| Smart proxies/ | x | x |  |
| Subnets/ | x | x |  |
| Compute resources/ | x | x |  |
| Installation media/ | x | x |  |
| Templates/ | x | x |  |
| Partition tables/ | x | x |  |
| Domains/ | x | x |  |
| Realms/ | x | x |  |
| Environments/ | x | x |  |
| Hostgroups/ | x | x |  |
| Parameters/ | x | x |  |
| Locations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |
| Label | x | x | x |
| Description | x | x |  |
| Service levels | x | x |  |
| Cdn configuration/type | x | x |  |
| Cdn configuration/url | x | x |  |
| Cdn configuration/upstream organization | x | x |  |
| Cdn configuration/upstream lifecycle environment | x | x |  |
| Cdn configuration/upstream content view | x | x |  |
| Cdn configuration/username | x | x |  |
| Cdn configuration/ssl ca credential id | x | x |  |

## 57.15. organization list

List all organizations

**Usage**

```
# hammer organization <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--full-result BOOLEAN` – Whether or not to show all results
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--search VALUE` – Search string
- `--sort-by VALUE` – Field to sort the results on
- `--sort-order VALUE` – How to order the sorted results (e.g. ASC for ascending)
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Title | x | x | x |
| Name | x | x | x |
| Description | x | x |  |
| Label | x | x | x |

**Search and order fields**

- `description` – text
- `id` – integer
- `label` – string
- `name` – string
- `organization_id` – integer
- `title` – string

## 57.16. organization remove-compute-resource

Disassociate a compute resource

**Usage**

```
# hammer organization remove-compute-resource [OPTIONS]
```

**Options**

- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id NUMBER`
- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.17. organization remove-domain

Disassociate a domain

**Usage**

```
# hammer organization remove-domain [OPTIONS]
```

**Options**

- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Numerical ID or domain name
- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.18. organization remove-hostgroup

Disassociate a hostgroup

**Usage**

```
# hammer organization remove-hostgroup [OPTIONS]
```

**Options**

- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER`
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.19. organization remove-location

Disassociate a location

**Usage**

```
# hammer organization remove-location [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER`
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.20. organization remove-medium

Disassociate a medium

**Usage**

```
# hammer organization remove-medium [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--medium VALUE` – Medium name
- `--medium-id NUMBER`
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.21. organization remove-provisioning-template

Disassociate provisioning templates

**Usage**

```
# hammer organization remove-provisioning-template [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id NUMBER`
- `--provisioning-template-ids LIST` – List of provisioning template ids
- `--provisioning-template-search VALUE` Provisioning template name regex to search, all matching templates will be disassociated
- `--provisioning-templates LIST` – List of provisioning template names
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.22. organization remove-smart-proxy

Disassociate a smart proxy

**Usage**

```
# hammer organization remove-smart-proxy [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--smart-proxy VALUE` – Name to search by
- `--smart-proxy-id NUMBER`
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.23. organization remove-subnet

Disassociate a subnet

**Usage**

```
# hammer organization remove-subnet [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER`
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 57.24. organization remove-user

Disassociate an user

**Usage**

```
# hammer organization remove-user [OPTIONS]
```

**Options**

- `--id VALUE` – Organization ID
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `--user VALUE` – User`s login to search by
- `--user-id NUMBER`
- `-h`, `--help` – Print help

## 57.25. organization set-parameter

Create or update parameter for an organization

**Usage**

```
# hammer organization set-parameter [OPTIONS]
```

**Options**

- `--hidden-value BOOLEAN` – Should the value be hidden
- `--name VALUE` – Parameter name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Organization ID
- `--organization-title VALUE` – Set the current organization context for the request
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json` Default: "string"
- `--value VALUE` – Parameter value
- `-h`, `--help` – Print help

## 57.26. organization update

Update organization

**Usage**

```
# hammer organization update [OPTIONS]
```

**Options**

- `--compute-resource-ids LIST` – Compute resource IDs
- `--compute-resources LIST`
- `--description VALUE`
- `--domain-ids LIST` – Domain IDs
- `--domains LIST`
- `--environment-ids LIST` – Environment IDs
- `--environments LIST`
- `--hostgroup-ids LIST` – Host group IDs
- `--hostgroup-titles LIST`
- `--hostgroups LIST`
- `--id VALUE`
- `--ignore-types LIST` – List of resources types that will be automatically associated
- `--label VALUE` – Organization label to search by
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – Associated location IDs
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--media LIST`
- `--medium-ids LIST` – Medium IDs
- `--name VALUE`
- `--new-name VALUE`
- `--new-title VALUE`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Set the current organization context for the request
- `--partition-table-ids LIST` – Partition template IDs
- `--partition-tables LIST`
- `--provisioning-template-ids LIST` Provisioning template IDs
- `--provisioning-templates LIST`
- `--puppet-environment-ids LIST` – IDs of associated Puppet environment
- `--puppet-environments VALUE` – Names of associated Puppet environment
- `--realm-ids LIST` – Realm IDs
- `--realms LIST`
- `--redhat-repository-url VALUE` – Red Hat CDN URL
- `--smart-proxies LIST`
- `--smart-proxy-ids LIST` – Capsule IDs
- `--subnet-ids LIST` – Subnet IDs
- `--subnets LIST`
- `--title VALUE` – Set the current organization context for the request
- `--user-ids LIST` – User IDs
- `--users LIST`
- `-h`, `--help` – Print help
