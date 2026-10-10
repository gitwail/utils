---
title: "content-view component"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "24"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-content-view-component"
---
# Chapter 24. content-view component

View and manage components

**Usage**

```
# hammer content-view component [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 24.1. content-view component add

Add components to the content view

**Usage**

```
# hammer content-view component add [OPTIONS]
```

**Options**

- `--component-content-view VALUE` – Content View name of the component who`s latest version is desired
- `--component-content-view-id VALUE` – Content View identifier of the component who`s latest version is desired
- `--component-content-view-version VALUE` – Content View Version number of the component. Either use this or
- `--component-content-view-version-id` option
- `--component-content-view-version-id VALUE` Content View Version identifier of the component
- `--composite-content-view VALUE` – Name of the composite content view
- `--composite-content-view-id NUMBER` – Composite content view identifier
- `--latest` – Select the latest version of the components content view is desired
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 24.2. content-view component list

List components attached to this content view

**Usage**

```
# hammer content-view component <list|index> [OPTIONS]
```

**Options**

- `--composite-content-view VALUE` – Name of the composite content view
- `--composite-content-view-id NUMBER` Composite content view identifier
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Content view id | x | x |  |
| Name | x | x |  |
| Version | x | x |  |
| Component id | x | x | x |
| Current version | x | x |  |
| Version id | x | x |  |

## 24.3. content-view component remove

Remove components from the content view

**Usage**

```
# hammer content-view component remove [OPTIONS]
```

**Options**

- `--component-content-view-ids VALUE` Array of component content view identfiers to remove. Comma separated list of values
- `--component-content-views VALUE` – Array of component content view names to remove. Comma separated list of values
- `--component-ids LIST` – Array of content view component IDs to remove. Identifier of the component association
- `--composite-content-view VALUE` – Name of the composite content view
- `--composite-content-view-id NUMBER` Composite content view identifier
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help

## 24.4. content-view component update

Update a component associated with the content view

**Usage**

```
# hammer content-view component update [OPTIONS]
```

**Options**

- `--component-content-view VALUE` – Content View name of the component who`s latest version is desired
- `--component-content-view-id VALUE` – Content View identifier of the component who`s latest version is desired
- `--component-content-view-version VALUE` – Content View Version number of the component. Either use this or
- `--component-content-view-version-id` option
- `--component-content-view-version-id VALUE` Content View Version identifier of the component
- `--composite-content-view VALUE` – Name of the composite content view
- `--composite-content-view-id NUMBER` – Composite content view identifier
- `--id NUMBER` – Content view component ID. Identifier of the component association
- `--latest` – Select the latest version of the components content view is desired
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `-h`, `--help` – Print help
