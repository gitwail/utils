---
title: "Storing content on an NFS share"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "B"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#storing-content-on-an-nfs-share"
---
# Appendix B. Storing content on an NFS share

When local disk space on your Satellite Server is insufficient for content storage, you can mount an NFS share at `/var/lib/pulp` to store synchronized content remotely.

> **Important**
>
> Use high-bandwidth, low-latency storage for the `/var/lib/pulp` file system. Red Hat Satellite has many I/O-intensive operations. Therefore, high-latency, low-bandwidth storage might have issues with performance degradation.

**Procedure**

1. Create the NFS share. This example uses a share at `nfs.example.com:/Satellite/pulp`. Ensure this share provides the appropriate permissions to Satellite Server and its `apache` user.
2. Stop Satellite services on your Satellite Server:

   ```
   # satellite-maintain service stop
   ```
3. Install the `nfs-utils` package on your Satellite Server:

   ```
   # satellite-maintain packages install nfs-utils
   ```
4. Copy the existing contents of `/var/lib/pulp` to the NFS share.

   1. Mount the NFS share at a temporary location:

      ```
      # mkdir /mnt/temp
      # mount -o rw nfs.example.com:/Satellite/pulp /mnt/temp
      ```
   2. Copy the existing contents of `/var/lib/pulp` to the temporary location:

      ```
      # cp -r /var/lib/pulp/* /mnt/temp/.
      ```
   3. Set the permissions for all files on the share to use the `pulp` user.
   4. Unmount the temporary storage location:

      ```
      # umount /mnt/temp
      ```
5. Remove the existing contents of `/var/lib/pulp`:

   ```
   # rm -rf /var/lib/pulp/*
   ```
6. Edit the `/etc/fstab` file and add the following line:

   ```
   nfs.example.com:/Satellite/pulp    /var/lib/pulp   nfs    rw,hard,intr,context="system_u:object_r:pulpcore_var_lib_t:s0"
   ```

   This makes the mount persistent across system reboots. Ensure to include the SELinux context.
7. Enable the mount:

   ```
   # mount -a
   ```
8. Verify the NFS share provides the content:

   1. Confirm the NFS share mounts to `/var/lib/pulp`:

      ```
      # df
      Filesystem                         1K-blocks     Used Available Use% Mounted on
      ...
      nfs.example.com:/Satellite/pulp 309506048 58632800 235128224  20% /var/lib/pulp
      ...
      ```
   2. Confirm the content exists at the mount on `/var/lib/pulp`:

      ```
      # ls /var/lib/pulp
      ```
9. Start Satellite services on your Satellite Server:

   ```
   # satellite-maintain service start
   ```

**Verification**

- Run content synchronization to ensure the NFS share works as expected. For more information, see [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc").
