---
title: "Configuring TFTP integration"
product: "Red Hat Satellite"
version: "6.19"
guide: "integrating_provisioning_infrastructure_services"
guide_title: "Integrating provisioning infrastructure services"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#configuring-tftp-integration"
---
# Chapter 3. Configuring TFTP integration

You can integrate TFTP with Satellite to perform unattended installations by booting the operating system’s setup over the network.

## 3.1. Enabling the installer-managed TFTP service

Instead of using a TFTP server, you can enable the installer-managed TFTP service to perform unattended installations with low maintenance. With installer-managed TFTP, Satellite fully manages the service and its files.

**Procedure**

- Configure your Satellite Server or Capsule Server as the TFTP server:

  ```
  # satellite-installer \
  --foreman-proxy-tftp true \
  --foreman-proxy-tftp-managed true
  ```

## 3.2. Integrating a generic TFTP server

If you have a TFTP server in your network, you can integrate this service into your Satellite to continue using your existing TFTP server. With this type of integration, Satellite uses the Network File System (NFS) protocol to access the root directory of the TFTP service.

> **Note**
>
> If you prefer a low maintenance solution that also manages files on the TFTP server, use the installer-managed TFTP service.

### 3.2.1. Configuring Satellite Server for use with tftp

After you have prepared the TFTP server, integrate it into your Satellite Server or Capsule Server.

**Prerequisites**

- You shared the `/exports/var/lib/tftpboot` on the TFTP server with NFS.

**Procedure**

1. Create the directory into which you later mount the NFS share:

   ```
   # mkdir -p /mnt/nfs/var/lib/tftpboot
   ```
2. Edit the `/etc/fstab` file, and add entry for the NFS share to mount them automatically when the system boots:

   ```
   tftp_server_fqdn:/exports/var/lib/tftpboot  /mnt/nfs/var/lib/tftpboot  nfs  rw,vers=3,auto,nosharecache,context="system_u:object_r:tftpdir_rw_t:s0"  0 0
   ```
3. Mount the NFS share:

   ```
   # mount /mnt/nfs/var/lib/tftpboot/
   ```
4. Configure Satellite Server or Capsule Server to use the TFTP server:

   ```
   # satellite-installer \
   --foreman-proxy-tftp true \
   --foreman-proxy-managed false \
   --foreman-proxy-tftp-root /mnt/nfs/var/lib/tftpboot \
   --foreman-proxy-tftp-servername tftp_server_fqdn
   ```
5. For each affected Capsule, update the configuration of that Capsule in the Satellite web UI. For more information, see [Section 3.3, “Associating the TFTP service with a subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-tftp-service-with-a-subnet "3.3. Associating the TFTP service with a subnet").

## 3.3. Associating the TFTP service with a subnet

After you configured or changed the TFTP provider, you must update the configuration of each affected Capsule in the Satellite web UI.

**Prerequisites**

- You configured a TFTP server.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
2. Select the subnet name.
3. On the **Capsules** tab, select the Capsule for TFTP.
4. Click **Submit**.

## 3.4. Disabling TFTP for integration

If you want to manually manage a TFTP service and not integrate it into Satellite, you must prevent Satellite from maintaining this service on the operating system and disable orchestration to avoid errors.

> **Note**
>
> Disabling TFTP in Satellite does not remove the related backend service on the operating system.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
2. For each subnet that is associated with the TFTP Capsule:

   1. Select the subnet.
   2. On the **Capsules** tab, clear the **TFTP Capsule** field.
   3. Click **Submit**.
3. On Satellite Server, enter:

   ```
   # satellite-installer --foreman-proxy-tftp false
   ```

   > **Note**
   >
   > Satellite does not perform orchestration when a Capsule is not set for a given subnet. When you disable Capsule associations, orchestration commands for existing hosts can fail if the expected records and configuration files are not present.
