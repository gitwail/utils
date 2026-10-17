---
title: "Converting virtual machines from other hypervisors to KVM with virt-v2v in RHEL 7, RHEL 8, RHEL 9, and RHEL 10"
source: https://access.redhat.com/articles/1351473
---

# Converting virtual machines from other hypervisors to KVM with virt-v2v in RHEL 7, RHEL 8, RHEL 9, and RHEL 10

The *virt-v2v* tool converts virtual machines (VMs) from foreign hypervisors, including their disk images and metadata, for use with Red Hat Enterprise Linux with KVM managed by *libvirt* and Red Hat OpenStack Platform. *virt-v2v* can convert Red Hat Enterprise Linux and Windows VMs running on Xen and VMware ESXi environments.

This article provides an overview of VM conversions and links to procedures for specific types of conversions.

*virt-v2v* is included in Red Hat Migration Toolkit for Virtualization, Red Hat Enterprise Linux 7 (RHEL 7), Red Hat Enterprise Linux 8 (RHEL 8), Red Hat Enterprise Linux 9 (RHEL 9), Red Hat Enterprise Linux 10 (RHEL 10). In RHEL, it is installed with the virt-v2v package. In Red Hat Enterprise Linux 7, *virt-v2v* is also available from the Red Hat OpenStack Platform channel.

**Important**: virt-v2v is currently only supported on the AMD64 and Intel 64 architecture, also known as x86\_64. All other architectures, including IBM Z, IBM POWER, and 64-bit ARM are not supported for v2v conversion.

In addition, RHEL 9 and later introduces the virt-v2v-in-place tool, which is installed as a part of the virt-v2v package. However, virt-v2v-in-place is only supported as a part of the [Migration Toolkit for Virtualization (MTV)](https://access.redhat.com/products/migration-toolkit-virtualization), and Red Hat heavily discourages using the tool on RHEL.

## Supported conversions

### Supported guest operating systems for conversions

Only virtual machines running specific guest operating systems can be converted by *virt-v2v* to run on KVM. This also differs when using *virt-v2v* on RHEL 7, on RHEL 8, and on RHEL 9:

| Guest OS | RHEL 7 host | RHEL 8 host | RHEL 9 host | RHEL 10 host |
| --- | --- | --- | --- | --- |
| Red Hat Enterprise Linux 5 | Supported | Not supported | Not supported | Not supported |
| Red Hat Enterprise Linux 6 | Supported | Supported | Not supported | Not supported |
| Red Hat Enterprise Linux 7 | Supported | Supported | Supported | Supported |
| Red Hat Enterprise Linux 8 | Not supported | Supported | Supported | Supported |
| Red Hat Enterprise Linux 9 | Not supported | Not supported | Supported | Supported |
| Red Hat Enterprise Linux 10 | Not supported | Not supported | Not supported | Supported |
| SUSE Linux Enterprise Server 11, SP4 and later | Not supported [1] | Not supported [1] | Not supported [1] | Not supported [1] |
| SUSE Linux Enterprise Server 12 | Not supported [1] | Not supported [1] | Not supported [1] | Not supported [1] |
| SUSE Linux Enterprise Server 15 | Not supported [1] | Not supported [1] | Not supported [1] | Not supported [1] |
| Windows 8 | Supported | Not supported | Not supported | Not supported |
| Windows 8.1 | Supported | Not supported | Not supported | Not supported |
| Windows 10 | Supported | Supported | Supported | Supported |
| Windows 11 | Not supported | Supported | Supported | Supported |
| Windows Server 2008 | Supported | Not supported | Not supported | Not supported |
| Windows Server 2008 R2 | Supported | Not supported | Not supported | Not supported |
| Windows Server 2012 | Supported | Not supported | Not supported | Not supported |
| Windows Server 2012 R2 | Supported | Not supported | Not supported | Not supported |
| Windows Server 2016 | Supported | Supported | Supported | Supported |
| Windows Server 2019 | Supported | Supported | Supported | Supported |
| Windows Server 2022 | Not supported | Supported | Supported | Supported |
| Windows Server 2025 | Not supported | Supported | Supported | Supported |
| Debian [2] | Technology Preview in RHEL 7.4 and later | Technology Preview | Technology Preview | Technology Preview |
| Ubuntu [2] | Technology Preview in RHEL 7.4 and later | Technology Preview | Technology Preview | Technology Preview |

[1] SUSE Enterprise Linux guests are validated to run on RHEL hosts. However, SUSE Linux uses the *btrfs* file system by default, which is unsupported by RHEL. Therefore, converting a SUSE system that use *btrfs* is not possible with *virt-v2v*.

In addition, VMs that use X graphics and a SUSE Linux Enterprise Server 11 operating system should be re-adjusted after the conversion for the graphics to work properly. To do so, use the *sax2* distribution tool in the guest OS after the migration is finished.

[2] As a Technology Preview, converting Debian and Ubuntu VMs is not supported. In addition, This conversion currently has the following known issues:

- *virt-v2v* cannot change the default kernel in the GRUB2 configuration, and the kernel configured in the VM is not changed during the conversion, even if a more optimal version of the kernel is available on the VM.
- After converting a linux virtual machine to KVM, the name of the VM's network interface may change, and thus requires manual configuration.

**Note:** *virt-v2v* conversions of any operating system not listed above may in some cases work, but are not supported by Red Hat.

### Supported hypervisors for conversion

Conversions from the following hypervisors are supported:

- Red Hat Enterprise Linux 5 Xen (Fully supported in RHEL 7 and 8, deprecated in RHEL 9, removed in RHEL 10)
- VMware vSphere ESX(i) - versions 7.0 and 8.0

**Note:** *virt-v2v* conversions from any hypervisor not listed above may in some cases work, but are not supported by Red Hat.

### Other considerations for V2V conversion support

Virtual machines that use the UEFI firmware are currently supported for conversion only to the following KVM hypervisors:

- RHEL 7, RHEL 8, and RHEL 9
- Red Hat OpenStack Platform

Note, however, that these features are supported when using the [Migration Toolkit for Virtualization](https://access.redhat.com/products/migration-toolkits-virtualization/).

## How to perform the V2V conversion?

The specific steps for preparing and performing the v2v conversion can differ based on the VM's guest OS and original hypervisor. For details about specific conversions, see one of the following:

- [Converting a VMware vCenter Linux virtual machine to KVM](https://access.redhat.com/articles/1353223)
- [Converting a VMware vCenter Windows machine to KVM](https://access.redhat.com/articles/1353463)
- [Converting a Linux machine on a Xen hypervisor to KVM](https://access.redhat.com/articles/1353783)
- [Export a virtual machine from VMware as an OVA file, and import it into KVM](https://access.redhat.com/articles/1351963)

## Related Links

For information on converting a virtual machine to run on Red Hat OpenStack Platform, see [Converting VMware virtual machines to import to Red Hat OpenStack Platform](https://access.redhat.com/articles/1247463).

For information on converting a physical machine from another hypervisor with *virt-v2v* and *virt-p2v*, see [Converting physical machines to KVM virtual machines using virt-p2v in RHEL7](https://access.redhat.com/articles/2702281).
