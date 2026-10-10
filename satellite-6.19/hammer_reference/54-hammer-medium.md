---
title: "medium"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "54"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-medium"
---
# Chapter 54. medium

Manipulate installation media

**Usage**

```
# hammer medium [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 54.1. medium add-operatingsystem

Associate an operating system

**Usage**

```
# hammer medium add-operatingsystem [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Medium name
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 54.2. medium create

Create a medium

**Usage**

```
# hammer medium create [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – Name of media
- `--operatingsystem-ids LIST`
- `--operatingsystems LIST`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--os-family VALUE` – Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Fcos, Freebsd, Gentoo, Junos, NXOS, Rancheros, Redhat, Rhcos, Solaris, Suse, VRP, Windows, Xenserver
- `--path VALUE` – The path to the medium, can be a URL or a valid NFS server (exclusive of the architecture).

For example mirror.centos.org/centos/$version/os/$arch where $arch will be substituted for the host`s actual OS architecture and $version, $major and $minor will be substituted for the version of the operating system.

Solaris and Debian media may also use $release. * `-h`, `--help` – Print help

## 54.3. medium delete

Delete a medium

**Usage**

```
# hammer medium <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Medium name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 54.4. medium info

Show a medium

**Usage**

```
# hammer medium <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Medium name
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Path | x | x |  |
| Os family | x | x |  |
| Operating systems/ | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |
| Created at | x | x |  |
| Updated at | x | x |  |

## 54.5. medium list

List all installation media

**Usage**

```
# hammer medium <list|index> [OPTIONS]
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
| Path | x | x |  |

**Search and order fields**

- `family` – string
- `id` – integer
- `location` – string
- `location_id` – integer
- `name` – string
- `organization` – string
- `organization_id` – integer
- `path` – string

## 54.6. medium remove-operatingsystem

Disassociate an operating system

**Usage**

```
# hammer medium remove-operatingsystem [OPTIONS]
```

**Options**

- `--id VALUE`
- `--name VALUE` – Medium name
- `--operatingsystem VALUE` – Operating system title
- `--operatingsystem-id NUMBER`
- `-h`, `--help` – Print help

## 54.7. medium update

Update a medium

**Usage**

```
# hammer medium update [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-ids LIST` – REPLACE locations with given ids
- `--location-title VALUE` – Set the current location context for the request
- `--location-titles LIST`
- `--locations LIST`
- `--name VALUE` – Name of media
- `--new-name VALUE` – Name of media
- `--operatingsystem-ids LIST`
- `--operatingsystems LIST`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-ids LIST` – REPLACE organizations with given ids.
- `--organization-title VALUE` – Set the current organization context for the request
- `--organization-titles LIST`
- `--organizations LIST`
- `--os-family VALUE` – Operating system family, available values: AIX, Altlinux, Archlinux, Coreos, Debian, Fcos, Freebsd, Gentoo, Junos, NXOS, Rancheros, Redhat, Rhcos, Solaris, Suse, VRP, Windows, Xenserver
- `--path VALUE` – The path to the medium, can be a URL or a valid NFS server (exclusive of the architecture).

For example mirror.centos.org/centos/$version/os/$arch where $arch will be substituted for the host`s actual OS architecture and $version, $major and $minor will be substituted for the version of the operating system.

Solaris and Debian media may also use $release. * `-h`, `--help` – Print help
