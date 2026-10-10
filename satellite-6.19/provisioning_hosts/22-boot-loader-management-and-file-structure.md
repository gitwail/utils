---
title: "Boot loader management and file structure"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "E"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#boot-loader-management-and-file-structure"
---
# Appendix E. Boot loader management and file structure

Satellite manages and serves boot loader binaries through Capsule, which provides the network boot services used during automated host provisioning. You can use PXE boot for BIOS and UEFI firmware.

During a network-based installation, Capsule coordinates the following services:

DHCP
:   Assigns IP addresses and provides the boot loader filename and server information.

TFTP
:   Delivers boot loaders such as PXELinux, Grub2, or iPXE binaries to clients. TFTP also serves the following resources:

    1. Configuration files for boot loaders
    2. Kernels and `initramdisk`

HTTP(S)
:   Serves boot loaders and installation files through the HTTPBoot module of your Capsule. HTTP(S) also serves the following resources:

    1. Configuration files for bootloaders
    2. Kernels & initramdisk
    3. Installation config files (Kickstart)
    4. Repository content
    5. Communication between Host <> Smart Proxy <> Foreman

When a host begins a network boot, it retrieves the appropriate boot loader (for example, `pxelinux.0`, `grubx64.efi`, or `ipxe.efi`) according to the **PXE Loader** option in Satellite. The boot loader then loads Satellite-generated configuration files that define which kernel and initrd to boot, initiating the operating system installation process.

The **Capsule** manages the distribution of these boot loader binaries and their configuration files. All boot loaders are stored on Capsule under the TFTP root directory (`/var/lib/tftpboot/`), which is also shared by the HTTPBoot service.

The Capsule also generates a directory for each provisioned host and names the directory with the host MAC address. In these directories, the Capsule creates symlinks to the boot files and configuration files, for example:

```
├── host-config
│   └── 00-aa-aa-99-99-04
│       └── grub2
│           ├── boot.efi -> ../../../grub2/grubx64.efi
│           ├── boot-sb.efi -> ../../../grub2/shimx64.efi
│           ├── grub.cfg-00:aa:aa:99:99:04 -> ../../../grub2/grub.cfg-00:aa:aa:99:99:04
│           ├── grub.cfg-01-00-aa-aa-99-99-04 -> ../../../grub2/grub.cfg-01-00-aa-aa-99-99-04
│           ├── grubx64.efi -> ../../../grub2/grubx64.efi
│           └── shimx64.efi -> ../../../grub2/shimx64.efi
```

This is useful for placing your own boot loader binaries in the `bootloader_universe` directory and use them instead of the default ones provided in `/var/lib/tftpboot/boot`. This is useful, for example, when you provision ARM hosts, for which Red Hat Satellite does not provide boot loaders.

By default, boot loader binaries are placed directly under service-specific directories such as `grub2/`, for example, `/var/lib/tftpboot/grub2/grubx64.efi`.

If the **bootloader-universe** structure is enabled, boot loaders are instead organized into a hierarchy based on type, architecture, and operating system version.

> **Note**
>
> The TFTP root directory is configured in `/etc/foreman-proxy/settings.d/tftp.yml` under the `:tftproot` parameter. The default path is `/var/lib/tftpboot/`.
>
> The directory used by **Grub2 UEFI HTTP** and **iPXE HTTP** for file delivery is defined in `/etc/foreman-proxy/settings.d/httpboot.yml` under the `:root_dir` parameter. The default path is also `/var/lib/tftpboot/`.
>
> This document uses the default paths. If your environment uses a different path, replace the default paths with your custom paths.

## E.1. Boot loader types in Satellite

You can use multiple types of PXE boot loaders during network provisioning, depending on firmware type, protocol, and boot environment.

In Satellite, you can configure a **PXE Loader** for each host. The PXE Loader determines which boot loader binary the host retrieves during network boot and how it communicates with the Capsule (via TFTP or HTTP). Select a PXE Loader based on whether the host uses **BIOS**, **UEFI**, **Secure Boot**, or **HTTP Boot**.

Table E.1. PXE loader types and boot protocols

| PXE loader (UI label) | Category | Firmware | Protocol |
| --- | --- | --- | --- |
| None | None | - | - |
| PXELinux BIOS | PXELinux | BIOS | DHCP → TFTP |
| PXELinux UEFI | PXELinux | UEFI | DHCP → TFTP |
| Grub2 BIOS | PXEGrub2 (TFTP) | BIOS | DHCP → TFTP |
| Grub2 ELF | PXEGrub2 (TFTP) | BIOS | DHCP → TFTP |
| Grub2 UEFI | PXEGrub2 (TFTP) | UEFI | DHCP → TFTP |
| Grub2 UEFI SecureBoot | PXEGrub2 (TFTP) | UEFI | DHCP → TFTP |
| Grub2 UEFI HTTP | Grub2 (HTTP) | UEFI | DHCP → HTTP |
| Grub2 UEFI HTTPS | Grub2 (HTTPS) | UEFI | DHCP → HTTPS |
| Grub2 UEFI HTTPS SecureBoot | Grub2 (HTTPS) | UEFI | DHCP → HTTPS |
| iPXE Embedded | iPXE Direct (HTTP) | BIOS / UEFI | DHCP → HTTP |
| iPXE UEFI HTTP | iPXE Direct (HTTP) | UEFI | DHCP → HTTP |
| iPXE Chain BIOS | iPXE Chainload | BIOS | DHCP → TFTP → HTTP |
| iPXE Chain UEFI | iPXE Chainload | UEFI | DHCP → TFTP → HTTP |

Each type of PXE Loader categories delivers boot loaders and installation files during network provisioning. In Satellite, you can select from the following PXE Loader categories:

PXELinux
:   Syslinux-based loaders for BIOS and UEFI environments.

PXEGrub2 (TFTP)
:   Grub2-based loader supporting both BIOS and UEFI environments (including Secure Boot via `shim`).

Grub2 (HTTP/HTTPS)
:   Grub2-based UEFI boot loader fetched over HTTP or HTTPS using the Capsule’s HTTPBoot service.

iPXE Chainload
:   A two-stage boot process in which the client first downloads an iPXE binary (`undionly-ipxe.0` or `ipxe.efi`) via TFTP. When loaded, iPXE retrieves Satellite’s iPXE script and installation files over HTTP, enabling flexible configuration and network boot via HTTP.

iPXE Direct (HTTP)
:   Boots directly via embedded or firmware-level iPXE using only HTTP.

None
:   Satellite does not specify a boot loader.

Satellite automatically determines the correct boot loader filename for each host based on its **architecture** and the **PXE Loader** selected in the host settings. This mechanism ensures that the correct boot loader binary (such as `grubx64.efi` or `grubaa64.efi`) is selected automatically, without requiring administrators to manage architecture-specific filenames.

Table E.2. PXE loader to boot loader mapping

| PXE loader (UI label) | Boot loader file (template path) | Example (x86_64) |
| --- | --- | --- |
| None | - | - |
| PXELinux BIOS | `pxelinux.0` | `pxelinux.0` |
| PXELinux UEFI | `pxelinux.efi` | `pxelinux.efi` |
| Grub2 BIOS | `grubMy_Arch.0` | `grubx64.0` |
| Grub2 ELF | `grubMy_Arch.elf` | `grubx64.elf` |
| Grub2 UEFI | `grubMy_Arch.efi` | `grubx64.efi` |
| Grub2 UEFI SecureBoot | `shimMy_Arch.efi` | `shimx64.efi` |
| Grub2 UEFI HTTP | `grubMy_Arch.efi` (via HTTP) | `grubx64.efi` |
| Grub2 UEFI HTTPS | `grubMy_Arch.efi` (via HTTPS) | `grubx64.efi` |
| Grub2 UEFI HTTPS SecureBoot | `shimMy_Arch.efi` (via HTTPS) | `shimx64.efi` |
| iPXE Embedded | Rendered dynamically as `Satellite_url('iPXE')` | - |
| iPXE UEFI HTTP | `ipxe-My_Arch.efi` | `ipxe-x64.efi` |
| iPXE Chain BIOS | `undionly-ipxe.0` | `undionly-ipxe.0` |
| iPXE Chain UEFI | `ipxe.efi` | `ipxe.efi` |

Satellite automatically determines the correct boot loader filename for each host based on its architecture. For example, `x86_64` hosts use `grubx64.efi`, while `aarch64` hosts use `grubaa64.efi`.

Table E.3. Boot loader filenames by architecture

| Architecture (Web UI) | Example Filename | Internal Suffix (for reference) |
| --- | --- | --- |
| i386, i686, x86 | `grubia32.efi` | `ia32` |
| x86_64, amd64 | `grubx64.efi`, `shimx64.efi` | `x64` |
| aarch64, aa64 | `grubaa64.efi`, `shimaa64.efi` | `aa64` |
| ppc64, ppc64le | `grubppc64.efi` | `ppc64`, `ppc64le` |
| Other architectures (for example, riscv64, loongarch64) | `grubriscv64.efi` | normalized name |

For example, a host with architecture `aarch64` and PXE Loader set to `Grub2 UEFI` uses:

```
/var/lib/tftpboot/grub2/grubaa64.efi
```

This mechanism allows Satellite to select the correct boot loader automatically, without requiring users to manage architecture-specific filenames manually.

## E.2. PXELinux boot loaders

PXELinux is a Syslinux-based PXE boot loader used by Satellite for BIOS and UEFI systems. In Satellite, PXELinux enables hosts to boot into the OS installer automatically during provisioning.

When a host is set to **Build mode**, Satellite generates a host-specific configuration file and places it in the TFTP directory managed by the Capsule.

Table E.4. Default boot loader files

| Default path | Purpose | User action |
| --- | --- | --- |
| `/var/lib/tftpboot/pxelinux.0` | The main PXELinux boot loader binary. Installed automatically by the satellite-installer. | **Auto-installed by satellite-installer** |
| `/var/lib/tftpboot/pxelinux.cfg/` | Directory that contains configuration files generated by Satellite for each host (for example, 01-52-54-00-ab-cd-ef). | **Auto-created during Build mode** |
| `/var/lib/tftpboot/ldlinux.c32` | Support module required by PXELinux for menu and filesystem operations. | **Provide manually** |
| `/var/lib/tftpboot/menu.c32`, `/var/lib/tftpboot/chain.c32` | Optional Syslinux modules for displaying boot menus or chainloading. | **Provide manually** |

**Example E.1. PXELinux-related directory layout**

```
# tree /var/lib/tftpboot/
/var/lib/tftpboot/
 ├── pxelinux.0
 ├── ldlinux.c32
 ├── menu.c32
 ├── chain.c32
 └── pxelinux.cfg/
      ├── default
      └── 01-52-54-00-ab-cd-ef
```

> **Note**
>
> When a host is set to **Build mode**, Satellite automatically generates the configuration file under `pxelinux.cfg/` based on the host’s OS, architecture, and installation template. The Capsule’s TFTP service then serves both the PXELinux binary and its configuration file to the client during network boot.

## E.3. Grub2 UEFI boot loader and the bootloader-universe structure

**PXEGrub2** GRUB-based PXE boot loader supports BIOS and UEFI environments, as well as Secure Boot environments. The `bootloader-universe` directory structure organizes Grub2 binaries by OS and architecture.

PXEGrub2 is managed by the Capsule’s TFTP service, which provides PXE clients with the appropriate boot loader binaries and configuration files.

By using the `bootloader-universe` directory structure, Grub2-based UEFI boot loaders can be organized and managed by distribution, version, and architecture. This feature does not require explicit configuration. It is automatically enabled when the Capsule uses the `/var/lib/tftpboot/bootloader-universe/pxegrub2/` directory structure.

The `bootloader-universe` directory enables multiple operating system versions and architectures to coexist without conflicts.

When the Capsule recognizes the `/var/lib/tftpboot/bootloader-universe/pxegrub2/` structure, boot loaders are stored in an organized hierarchy by OS, version, and architecture.

Before placing boot loader binaries (`shimMy_Arch.efi`, `grubMy_Arch.efi`), you must manually create the corresponding directory hierarchy by using the `mkdir` command, for example, `# mkdir -p /var/lib/tftpboot/bootloader-universe/pxegrub2/My_Distribution/My_Version/My_Arch`.

Table E.5. Default bootloader-universe files

| Path | Purpose | User action |
| --- | --- | --- |
| `/var/lib/tftpboot/bootloader-universe/pxegrub2/My_Distribution/My_Version/My_Arch/` | Stores OS- and architecture-specific Grub2 binaries (shim*My_Arch*.efi, grub*My_Arch*.efi) and symbolic links (boot.efi, boot-sb.efi). Used for version-specific boot loader management within the `bootloader-universe` hierarchy. | **Create manually** |
| `/var/lib/tftpboot/bootloader-universe/pxegrub2/My_Distribution/default/My_Arch/` | Stores OS- and architecture-specific Grub2 binaries (`shimMy_Arch.efi`, `grubMy_Arch.efi`) and symbolic links (`boot.efi`, `boot-sb.efi`). Used as a fallback directory when a specific version is not available. | **Create manually** |
| `/var/lib/tftpboot/host-config/My_MAC_Address/grub2/` | Host-specific directory automatically created when a host enters **Build mode**. Contains symbolic links (`boot.efi`, `boot-sb.efi`) and a generated `grub.cfg`. | **Auto-created by Capsule** |

**Example E.2. `bootloader-universe` directory layout**

```
# tree /var/lib/tftpboot/bootloader-universe/
/var/lib/tftpboot/bootloader-universe/
 ├── pxegrub2/
 │    ├── My_Distribution/My_Version/My_Arch/
 │    │    ├── shimx64.efi
 │    │    ├── grubx64.efi
 │    │    ├── boot.efi -> grubx64.efi
 │    │    └── boot-sb.efi -> shimx64.efi
 │    └── ubuntu/22.04/My_Arch/
 │         ├── shimx64.efi
 │         ├── grubx64.efi
 │         ├── boot.efi -> grubx64.efi
 │         └── boot-sb.efi -> shimx64.efi
 └── host-config/
      └── 52-54-00-ab-cd-ef/
           └── grub2/
                ├── boot.efi -> ../../../bootloader-universe/pxegrub2/My_Distribution/My_Version/My_Arch/boot.efi
                ├── boot-sb.efi -> ../../../bootloader-universe/pxegrub2/My_Distribution/My_Version/My_Arch/boot-sb.efi
                ├── grub.cfg
                ├── shimx64.efi -> ../../../bootloader-universe/pxegrub2/My_Distribution/My_Version/My_Arch/shimx64.efi
                └── grubx64.efi -> ../../../bootloader-universe/pxegrub2/My_Distribution/My_Version/My_Arch/grubx64.efi
```

In this structure, the following principles apply:

- `boot.efi` and `boot-sb.efi` are symbolic links to `grubMy_Arch.efi` and `shimMy_Arch.efi`, respectively. The Capsule automatically creates host-specific links to these files under `host-config/My_MAC_Address/grub2/`.
- In the Satellite web UI, the `My_Distribution` OS and distribution identifiers must not contain spaces.
- You must manually create `boot.efi` and `boot-sb.efi` symbolic links within each `My_Arch` directory, for example:

  ```
  $ ln -s grubx64.efi boot.efi
  $ ln -s shimx64.efi boot-sb.efi
  $ chmod 644 grubx64.efi shimx64.efi
  ```

  The `chmod` command ensures that TFTP and HTTPBoot clients can read these files.

In addition to the `bootloader-universe` layout, Satellite also supports the **Legacy layout** for backward compatibility.

If the `/var/lib/tftpboot/bootloader-universe/pxegrub2/` structure is not used, Satellite falls back to the legacy `/var/lib/tftpboot/grub2/` directory. Boot loaders are stored in a flat layout, but when a host enters **Build mode**, the Capsule creates a host-specific directory with the required configuration files and links.

Table E.6. Default legacy layout files

| Path | Purpose | User action |
| --- | --- | --- |
| `/var/lib/tftpboot/grub2/` | Default directory used when `bootloader-universe` is not enabled. Contains Grub2 UEFI boot loader binaries such as `grubx64.efi`, `shimx64.efi`, `grubaa64.efi`, and `shimaa64.efi`. | Place the appropriate boot loader binaries (`grubMy_Arch.efi`, `shimMy_Arch.efi`) in this directory. No subdirectory creation is required. |
| `/var/lib/tftpboot/host-config/My_MAC_Address/grub2/` | Host-specific directory automatically created when a host enters **Build mode**. Contains symbolic links (`boot.efi`, `boot-sb.efi`) and a generated `grub.cfg`. | **Auto-created by Capsule** |

**Example E.3. `tftpboot/grub2/` structure**

```
/var/lib/tftpboot/grub2/
 ├── grubx64.efi
 └── shimx64.efi
```

When a host enters **Build mode**, Capsule creates the following directory structure:

```
# tree /var/lib/tftpboot/
/var/lib/tftpboot/
 └── host-config/
      └── 52-54-00-ab-cd-ef/
           └── grub2/
                ├── boot.efi -> ../../../grub2/grubx64.efi
                ├── boot-sb.efi -> ../../../grub2/shimx64.efi
                ├── grub.cfg
                ├── grub.cfg-01-52-54-00-ab-cd-ef
                └── grub.cfg-52:54:00:ab:cd:ef
```

## E.4. HTTP-capable boot loaders

Satellite supports HTTP-based boot methods including iPXE, iPXE chainloading, Grub2, and UEFI HTTP Boot. These methods use the HTTPBoot module of Capsule to deliver boot loaders and installation files.

Each method offers advantages depending on the firmware type and network environment.

The **HTTPBoot** feature exposes the same files that are available via TFTP, but over the HTTP or HTTPS protocol. This can improve boot reliability in environments where TFTP is blocked, unreliable, or slow.

The boot methods in Satellite use the following boot workflows:

iPXE chainloading (PXE to HTTP)
:   The boot process starts with a traditional PXE (TFTP) stage and then switches to HTTP for improved performance and flexibility. With this hybrid approach, existing PXE infrastructure can use HTTP for the later boot stages without requiring firmware-level HTTP support.

    iPXE chainloading uses the following workflow:

    1. The firmware downloads the appropriate iPXE loader via TFTP.

       - BIOS downloads `undionly-ipxe.0`.
       - UEFI downloads `ipxe.efi`.
    2. iPXE initializes the network and switches to HTTP, requesting an iPXE script such as `menu.ipxe`.

iPXE, Grub2, and UEFI HTTP(S) boot
:   UEFI firmware directly loads boot loaders by using HTTP or HTTPS without any TFTP step.

    iPXE, Grub2, and UEFI HTTP(S) Boot use the following workflow:

    1. UEFI firmware requests boot loader files from the Capsule via HTTP or HTTPS, for example, `ipxe-My_Architecture.efi`.
    2. Grub2 loads `grub.cfg` and starts the OS installer.

The Capsule’s **HTTPBoot** module and **TFTP** service share the same root directory. By default, this directory is `/var/lib/tftpboot/`.

```
URL path:   http://capsule.example.com/httpboot/
Filesystem: /var/lib/tftpboot/
```

This mapping means that the `/httpboot/` HTTP URL path directly corresponds to the local filesystem under `/var/lib/tftpboot/`. For example, a file located at `/var/lib/tftpboot/pxegrub2/grubx64.efi` is available over HTTP at `http://capsule.example.com/httpboot/pxegrub2/grubx64.efi`.

This shared structure simplifies management by ensuring that both PXE (TFTP) and HTTP clients use the same set of boot loader binaries and configuration files.

**Example E.4. iPXE and HTTPBoot-related directory layout**

```
# tree /var/lib/tftpboot/
/var/lib/tftpboot/
 ├── undionly-ipxe.0
 ├── ipxe.efi
 ├── ipxe-x64.efi
 └── grub2/
      ├── grubx64.efi
      └── shimx64.efi
```

Table E.7. Default boot loader files

| Default path | Purpose | User action |
| --- | --- | --- |
| `/var/lib/tftpboot/undionly-ipxe.0` | iPXE boot loader for **iPXE Chain BIOS**. Used in BIOS environments as the first-stage loader that transitions from TFTP-based PXE to HTTP-based iPXE boot. | **Place the `undionly-ipxe.0` binary in this directory.** |
| `/var/lib/tftpboot/ipxe.efi` | iPXE boot loader for **iPXE Chain UEFI**. Used in UEFI environments to chainload into iPXE for HTTP-capable provisioning. | **Place the `ipxe.efi` binary in this directory.** |
| `/var/lib/tftpboot/ipxe-x64.efi` | Architecture-specific iPXE binary for **iPXE UEFI HTTP** boot. Used for direct iPXE boot via HTTP without TFTP chainloading. | **Place the architecture-matched file, for example, `ipxe-x64.efi`, in this directory.** |
| `/var/lib/tftpboot/grub2/grubx64.efi` | Grub2 UEFI boot loader for **Grub2**, **UEFI HTTP**, or **HTTPS Boot**. Used to start UEFI installations via the Capsule’s HTTPBoot module. | **Place the corresponding architecture-specific file, for example, `grubx64.efi`, in this directory.** |
| `/var/lib/tftpboot/grub2/shimx64.efi` | Secure Boot shim loader for Grub2. Used when **Grub2 UEFI SecureBoot**, **Grub2**, or **UEFI HTTPS SecureBoot** is selected. | **Place the matching shim binary, for example, `shimx64.efi`, in this directory.** |

> **Note**
>
> Grub2 and UEFI HTTPS Boot relies on the Capsule’s HTTPS service to securely deliver the `boot.efi`, `shimx64.efi`, and similar boot loader binaries to UEFI clients. The configuration for this HTTPS service is defined in the Capsule’s main settings file `/etc/foreman-proxy/settings.yml`.
