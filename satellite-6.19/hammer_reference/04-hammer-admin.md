---
title: "admin"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-admin"
---
# Chapter 4. admin

Administrative server-side tasks

**Usage**

```
# hammer admin [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 4.1. admin logging

Logging verbosity level setup

**Usage**

```
# hammer admin logging [OPTIONS]
```

**Options**

- `--no-backup` – Skip configuration backups creation.
- `--prefix VALUE` – Operate on prefixed environment (e.g. chroot).
- `-a`, `--all` – Apply to all components.
- `-c`, `--components LIST` – Components to apply, use `--list` to get them.
- `-d`, `--level-debug` – Increase verbosity level to debug.
- `-h`, `--help` – Print help
- `-l`, `--list` – List available components.
- `-n`, `--dry-run` – Do not apply specified changes.
- `-p`, `--level-production` – Decrease verbosity level to standard.
