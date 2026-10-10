---
title: "defaults"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "28"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-defaults"
---
# Chapter 28. defaults

Defaults management

**Usage**

```
# hammer defaults [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 28.1. defaults add

Add a default parameter to config

**Usage**

```
# hammer defaults add [OPTIONS]
```

**Options**

- `--param-name VALUE` – The name of the default option (e.g. organization_id)
- `--param-value VALUE` – The value for the default option
- `--provider VALUE` – The name of the provider providing the value. For list available providers see `hammer defaults providers`
- `-h`, `--help` – Print help

## 28.2. defaults delete

Delete a default param

**Usage**

```
# hammer defaults delete [OPTIONS]
```

**Options**

- `--param-name VALUE` – The name of the default option
- `-h`, `--help` – Print help

## 28.3. defaults list

List all the default parameters

**Usage**

```
# hammer defaults list [OPTIONS]
```

**Options**

- `-h`, `--help` – Print help

## 28.4. defaults providers

List all the providers

**Usage**

```
# hammer defaults providers [OPTIONS]
```

**Options**

- `-h`, `--help` – Print help
