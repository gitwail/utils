---
title: "hammer"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer"
---
# Chapter 2. hammer

**Usage**

```
# hammer [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `--[no-]use-defaults` – Enable/disable stored defaults. Enabled by default
- `--autocomplete VALUE` – Get list of possible endings
- `--csv` – Output as CSV (same as `--output=csv)`
- `--csv-separator VALUE` – Character to separate the values
- `--fetch-ca-cert VALUE` – Fetch CA certificate from server and exit
- `--interactive BOOLEAN` – Explicitly turn interactive mode on/off
- `--no-headers` – Hide headers from output
- `--output ENUM` – Set output format Possible value(s): `base`, `table`, `silent`, `csv`, `yaml`, `json`
- `--output-file VALUE` – Path to custom output file
- `--show-ids` – Show ids of associated resources
- `--ssl-ca-file VALUE` – Configure the file containing the CA certificates
- `--ssl-ca-path VALUE` – Configure the directory containing the CA certificates
- `--ssl-client-cert VALUE` – Configure the client`s public certificate
- `--ssl-client-key VALUE` – Configure the client`s private key
- `--ssl-with-basic-auth` – Use standard authentication in addition to client certificate authentication
- `--verify-ssl BOOLEAN` – Configure SSL verification of remote system
- `--version` – Show version
- `-c`, `--config VALUE` – Path to custom config file
- `-d`, `--debug` – Show debugging output
- `-h`, `--help` – Print help
- `-p`, `--password VALUE` – Password to access the remote system
- `-q`, `--quiet` – Completely silent
- `-r`, `--reload-cache` – Force reload of Apipie cache
- `-s`, `--server VALUE` – Remote system address
- `-u`, `--username VALUE` – Username to access the remote system
- `-v`, `--[no-]verbose` – Be verbose (or not). True by default
