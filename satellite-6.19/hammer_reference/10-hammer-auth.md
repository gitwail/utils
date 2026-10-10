---
title: "auth"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-auth"
---
# Chapter 10. auth

Foreman connection login/logout

**Usage**

```
# hammer auth [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 10.1. auth login

Set credentials

**Usage**

```
# hammer auth login [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

### 10.1.1. auth login basic

provide username and password

**Usage**

```
# hammer auth login basic [OPTIONS]
```

**Options**

- `-h`, `--help` – Print help
- `-p`, `--password VALUE` – Password to access the remote system
- `-u`, `--username VALUE` – Username to access the remote system

### 10.1.2. auth login basic-external

Authenticate against external source (IPA/PAM) with credentials

**Usage**

```
# hammer auth login basic-external [OPTIONS]
```

**Options**

- `-h`, `--help` – Print help
- `-p`, `--password VALUE` – Password to access the remote system
- `-u`, `--username VALUE` – Username to access the remote system

### 10.1.3. auth login negotiate

negotiate the login credentials from the auth ticket (Kerberos)

**Usage**

```
# hammer auth login negotiate [OPTIONS]
```

**Options**

- `-h`, `--help` – Print help

### 10.1.4. auth login oauth

supports for both with/without 2fa

**Usage**

```
# hammer auth login oauth [OPTIONS]
```

**Options**

- `-a`, `--oidc-authorization-endpoint VALUE` Openidc provider URL which issues authentication code (two factor only)
- `-c`, `--oidc-client-id VALUE` – Client id used in the Openidc provider
- `-f`, `--two-factor` – Authenticate with two factor
- `-h`, `--help` – Print help
- `-p`, `--password VALUE` – Password to access the remote system
- `-r`, `--oidc-redirect-uri VALUE` – Redirect URI for the authentication code grant flow
- `-t`, `--oidc-token-endpoint VALUE` – Openidc provider URL which issues access token
- `-u`, `--username VALUE` – Username to access the remote system

## 10.2. auth logout

Wipe your credentials

**Usage**

```
# hammer auth logout [OPTIONS]
```

**Options**

- `-h`, `--help` – Print help

## 10.3. auth status

Information about current connections

**Usage**

```
# hammer auth status [OPTIONS]
```

**Options**

- `-h`, `--help` – Print help
