---
title: "insights"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "48"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-insights"
---
# Chapter 48. insights

Manage Insights related operations

**Usage**

```
# hammer insights [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 48.1. insights cloud-connector

Manage cloud connector setup

**Usage**

```
# hammer insights cloud-connector [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 48.1.1. insights cloud-connector enable

Enable cloud connector

**Usage**

```
# hammer insights cloud-connector enable [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 48.2. insights inventory

Manage inventory related operations

**Usage**

```
# hammer insights inventory [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 48.2.1. insights inventory download-report

Download the last generated report

**Usage**

```
# hammer insights inventory download-report [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--path VALUE` – Path to download report.
- `--path VALUE` – Path to directory where downloaded content will be saved
- `-h`, `--help` – Print help

### 48.2.2. insights inventory generate-report

Start new report generation

**Usage**

```
# hammer insights inventory generate-report [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--no-upload` – Generate the report, but do not upload
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

### 48.2.3. insights inventory sync

Start inventory status sync

**Usage**

```
# hammer insights inventory sync [OPTIONS]
```

**Options**

- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help
