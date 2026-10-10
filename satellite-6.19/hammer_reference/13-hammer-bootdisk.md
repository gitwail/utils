---
title: "bootdisk"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "13"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-bootdisk"
---
# Chapter 13. bootdisk

Download boot disks

**Usage**

```
# hammer bootdisk [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 13.1. bootdisk generic

Download generic image

**Usage**

```
# hammer bootdisk generic [OPTIONS]
```

**Options**

- `--file VALUE` – File or device to write image to
- `--force` – Force writing to existing destination (device etc.)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--sudo` – Use sudo to write to device
- `-h`, `--help` – Print help

## 13.2. bootdisk host

Download host image

**Usage**

```
# hammer bootdisk host [OPTIONS]
```

**Options**

- `--file VALUE` – File or device to write image to
- `--force` – Force writing to existing destination (device etc.)
- `--full BOOLEAN` – True for full, false for basic reusable image
- `--host VALUE` – Host name
- `--host-id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--sudo` – Use sudo to write to device
- `-h`, `--help` – Print help

## 13.3. bootdisk subnet

Download subnet generic image

**Usage**

```
# hammer bootdisk subnet [OPTIONS]
```

**Options**

- `--file VALUE` – File or device to write image to
- `--force` – Force writing to existing destination (device etc.)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--subnet VALUE` – Subnet name
- `--subnet-id VALUE`
- `--sudo` – Use sudo to write to device
- `-h`, `--help` – Print help
