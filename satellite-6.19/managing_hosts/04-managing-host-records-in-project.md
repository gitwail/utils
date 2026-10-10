---
title: "Managing host records in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#managing-host-records-in-project"
---
# Chapter 4. Managing host records in Satellite

You can add a host record by cloning an existing host and choose whether Satellite manages it. You can remove the record from Satellite Server when the system is decommissioned or re-registered elsewhere.

## 4.1. Cloning hosts in Satellite

You can clone an existing host in Satellite to create a new host with the same configuration, then change the name and network settings.

> **Note**
>
> Unlike cloning, creating a host is part of the host provisioning process. There are multiple provisioning methods and each requires different configuration of Satellite and Capsules. For more information, see [*Provisioning hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#).

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. In the **Actions** menu, click **Clone**.
3. On the **Host** tab, ensure to provide a **Name** different from the original host.
4. On the **Interfaces** tab, ensure to provide a different IP address.
5. Click **Submit** to clone the host.

## 4.2. Changing the managed status of a host

Hosts provisioned by Satellite are Managed by default. When a host is set to Managed, you can configure additional host parameters from Satellite Server.

Additional host parameters that you can configure for your hosts are listed on the **Operating System** tab. If you change any settings on the **Operating System** tab, they will not take effect until you set the host to build and reboot it.

If you need to obtain reports about configuration management on systems using an operating system not supported by Satellite, set the host to Unmanaged.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of the host you want to modify.
3. Click **Edit**.
4. Click **Manage host** or **Unmanage host** to change the host’s status.
5. Click **Submit**.

## 4.3. Removing a host from Satellite by using Satellite web UI

You can remove a host from Satellite from the Satellite web UI when you decommission the host or no longer need to manage it. The host is permanently deleted from the Satellite database.

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select the hosts that you want to remove.
3. From the options menu, select **Delete**.
4. Select the checkbox **I understand that this action cannot be undone**.
5. Click **Delete** to remove the host from Satellite permanently.

## 4.4. Removing a host from Satellite by using Hammer CLI

You can remove a host from Satellite by using Hammer CLI when you decommission the host or no longer need to manage it. The host is permanently deleted from the Satellite database.

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

**Procedure**

- Delete your host from Satellite:

  ```
  $ hammer host delete \
  --id My_Host_ID \
  --location-id My_Location_ID \
  --organization-id My_Organization_ID
  ```

  Alternatively, you can use `--name My_Host_Name` instead of `--id My_Host_ID`.
