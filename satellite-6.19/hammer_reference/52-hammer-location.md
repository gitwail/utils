---
title: "location"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "52"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-location"
---
# Chapter 52. location

Manipulate locations

**Usage**

```
# hammer location [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 52.1. location add-compute-resource

Associate a compute resource

**Usage**

```
# hammer location add-compute-resource [OPTIONS]
```

**Options**

- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id NUMBER`
- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.2. location add-domain

Associate a domain

**Usage**

```
# hammer location add-domain [OPTIONS]
```

**Options**

- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Numerical ID or domain name
- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.3. location add-hostgroup

Associate a hostgroup

**Usage**

```
# hammer location add-hostgroup [OPTIONS]
```

**Options**

- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER`
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.4. location add-medium

Associate a medium

**Usage**

```
# hammer location add-medium [OPTIONS]
```

**Options**

- `--id VALUE`
- `--medium VALUE` – Medium name
- `--medium-id NUMBER`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.5. location add-organization

Associate an organization

**Usage**

```
# hammer location add-organization [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Organization ID
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.6. location add-provisioning-template

Associate provisioning templates

**Usage**

```
# hammer location add-provisioning-template [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id NUMBER`
- `--provisioning-template-ids LIST` – List of provisioning template ids
- `--provisioning-template-search VALUE` Provisioning template name regex to search, all matching templates will be associated
- `--provisioning-templates LIST` – List of provisioning template names
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.7. location add-smart-proxy

Associate a smart proxy

**Usage**

```
# hammer location add-smart-proxy [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--smart-proxy VALUE` – Name to search by
- `--smart-proxy-id NUMBER`
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.8. location add-subnet

Associate a subnet

**Usage**

```
# hammer location add-subnet [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER`
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.9. location add-user

Associate an user

**Usage**

```
# hammer location add-user [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `--user VALUE` – User`s login to search by
- `--user-id NUMBER`
- `-h`, `--help` – Print help

## 52.10. location create

Create a location

**Usage**

```
# hammer location create [OPTIONS]
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
- `--media LIST`
- `--medium-ids LIST` – Medium IDs
- `--name VALUE`
- `--organization-ids LIST` – Associated organization IDs
- `--parent-id NUMBER` – Parent ID
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

## 52.11. location delete

Delete a location

**Usage**

```
# hammer location <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE` – Location numeric id to search by
- `--name VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 52.12. location delete-parameter

Delete parameter for a location

**Usage**

```
# hammer location delete-parameter [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER`
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Parameter name
- `-h`, `--help` – Print help

## 52.13. location info

Show a location

**Usage**

```
# hammer location <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE` – Location numeric id to search by
- `--name VALUE` – Set the current organization context for the request
- `--show-hidden-parameters BOOLEAN` Display hidden parameter values
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
| Organizations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 52.14. location list

List all locations

**Usage**

```
# hammer location <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Title | x | x | x |
| Name | x | x | x |
| Description | x | x |  |

**Search and order fields**

- `description` – text
- `id` – integer
- `location_id` – integer
- `name` – string
- `title` – string

## 52.15. location remove-compute-resource

Disassociate a compute resource

**Usage**

```
# hammer location remove-compute-resource [OPTIONS]
```

**Options**

- `--compute-resource VALUE` – Compute resource name
- `--compute-resource-id NUMBER`
- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.16. location remove-domain

Disassociate a domain

**Usage**

```
# hammer location remove-domain [OPTIONS]
```

**Options**

- `--domain VALUE` – Domain name
- `--domain-id NUMBER` – Numerical ID or domain name
- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.17. location remove-hostgroup

Disassociate a hostgroup

**Usage**

```
# hammer location remove-hostgroup [OPTIONS]
```

**Options**

- `--hostgroup VALUE` – Hostgroup name
- `--hostgroup-id NUMBER`
- `--hostgroup-title VALUE` – Hostgroup title
- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.18. location remove-medium

Disassociate a medium

**Usage**

```
# hammer location remove-medium [OPTIONS]
```

**Options**

- `--id VALUE`
- `--medium VALUE` – Medium name
- `--medium-id NUMBER`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.19. location remove-organization

Disassociate an organization

**Usage**

```
# hammer location remove-organization [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Organization ID
- `--organization-title VALUE` – Set the current organization context for the request
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.20. location remove-provisioning-template

Disassociate provisioning templates

**Usage**

```
# hammer location remove-provisioning-template [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--provisioning-template VALUE` – Name to search by
- `--provisioning-template-id NUMBER`
- `--provisioning-template-ids LIST` – List of provisioning template ids
- `--provisioning-template-search VALUE` Provisioning template name regex to search, all matching templates will be disassociated
- `--provisioning-templates LIST` – List of provisioning template names
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.21. location remove-smart-proxy

Disassociate a smart proxy

**Usage**

```
# hammer location remove-smart-proxy [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--smart-proxy VALUE` – Name to search by
- `--smart-proxy-id NUMBER`
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.22. location remove-subnet

Disassociate a subnet

**Usage**

```
# hammer location remove-subnet [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--subnet VALUE` – Subnet name
- `--subnet-id NUMBER`
- `--title VALUE` – Set the current location context for the request
- `-h`, `--help` – Print help

## 52.23. location remove-user

Disassociate an user

**Usage**

```
# hammer location remove-user [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Set the current location context for the request
- `--title VALUE` – Set the current location context for the request
- `--user VALUE` – User`s login to search by
- `--user-id NUMBER`
- `-h`, `--help` – Print help

## 52.24. location set-parameter

Create or update parameter for a location

**Usage**

```
# hammer location set-parameter [OPTIONS]
```

**Options**

- `--hidden-value BOOLEAN` – Should the value be hidden
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER`
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Parameter name
- `--parameter-type ENUM` – Type of the parameter Possible value(s): `string`, `boolean`, `integer`, `real`, `array`, `hash`, `yaml`, `json` Default: "string"
- `--value VALUE` – Parameter value
- `-h`, `--help` – Print help

## 52.25. location update

Update a location

**Usage**

```
# hammer location update [OPTIONS]
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
- `--id VALUE` – Location numeric id to search by
- `--ignore-types LIST` – List of resources types that will be automatically associated
- `--media LIST`
- `--medium-ids LIST` – Medium IDs
- `--name VALUE`
- `--new-name VALUE`
- `--organization-ids LIST` – Associated organization IDs
- `--parent-id NUMBER` – Parent ID
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
- `--title VALUE` – Set the current location context for the request
- `--user-ids LIST` – User IDs
- `--users LIST`
- `-h`, `--help` – Print help
