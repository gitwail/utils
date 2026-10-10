---
title: "Managing packages on the base operating system of Satellite Server or Capsule Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "E"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Managing_Packages_on_the_Base_Operating_System_admin"
---
# Appendix E. Managing packages on the base operating system of Satellite Server or Capsule Server

Satellite provides the `satellite-maintain packages` command to install and update packages on the base operating system of your Satellite Server or Capsule Servers.

> **Warning**
>
> Installing and updating individual packages with `dnf` is locked by default and not supported. While Satellite provides the `satellite-maintain packages unlock` command to bypass the locking and enable package management with `dnf`, this can lead to configuration inconsistencies and compromise the stability of the system. Always use `satellite-maintain packages` to install and update packages.

After installing or updating a package on the base operating system, it is required to run `satellite-installer`. The `satellite-maintain packages` command automatically runs `satellite-installer` after you use it to install or update a package. Note that running `satellite-installer` might trigger service restarts if updating a package affected service configurations.

Table E.1. Overview of satellite-maintain packages subcommands

| Subcommand | Description |
| --- | --- |
| `satellite-maintain packages install My_Package` | Installs packages on Satellite Server or Capsule Server |
| `satellite-maintain packages check-update` | Checks for available package updates on Satellite Server or Capsule Server |
| `satellite-maintain packages update` | Updates all packages on Satellite Server or Capsule Server |
| `satellite-maintain packages update My_Package` | Updates specific packages on Satellite Server or Capsule Server |
| `satellite-maintain packages lock` | Enables package locking to ensure the stability of the base operating system by preventing users from managing packages with `dnf`. |
