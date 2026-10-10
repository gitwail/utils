---
title: "Configuring DHCP integration"
product: "Red Hat Satellite"
version: "6.19"
guide: "integrating_provisioning_infrastructure_services"
guide_title: "Integrating provisioning infrastructure services"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#configuring-dhcp-integration"
---
# Chapter 2. Configuring DHCP integration

You can integrate DHCP with Satellite to automatically manage IP leases and boot configurations on a DHCP server during the provisioning of hosts. This helps to simplify the automated provisioning of hosts.

## 2.1. DHCP service providers

You can use DHCP providers to integrate Satellite with your existing DHCP infrastructure or deploy a new one.

Capsule supports the following DHCP providers:

`dhcp_isc`
:   Managing IP leases on an ISC DHCP server by using the Object Management Application Programming Interface (OMAPI).

`dhcp_remote_isc`
:   Managing IP leases on a remote ISC dhcpd server by using OMAPI. This provider requires that you share the leases over the network, for example, with NFS.

`dhcp_infoblox`
:   Managing IP leases on an Infoblox DHCP server.

**Additional resources**

- [Section 2.2, “Enabling the installer-managed DHCP service”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#enabling-the-installer-managed-dhcp-service "2.2. Enabling the installer-managed DHCP service")
- [Section 2.3, “Integrating a remote ISC DHCP server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-a-remote-isc-dhcp-server "2.3. Integrating a remote ISC DHCP server")
- [Section 2.4, “Integrating Infoblox DHCP”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-infoblox-dhcp "2.4. Integrating Infoblox DHCP")

## 2.2. Enabling the installer-managed DHCP service

If you do not have a DHCP server available in your network, you can use the installer-managed DHCP service. Therefore, you can run a DHCP service with a lower maintenance overhead.

**Prerequisites**

- You know the following network information:

  - The range of IP addresses the DHCP should manage
  - The IP address of the default gateway in the subnet
  - The IP addresses of the name servers for the subnet

**Procedure**

1. Configure Satellite Server or Capsule Server as DHCP server:

   ```
   # satellite-installer \
   --foreman-proxy-dhcp true \
   --foreman-proxy-dhcp-provider isc \
   --foreman-proxy-dhcp-managed true \
   --foreman-proxy-dhcp-range "192.0.2.100 192.0.2.150" \
   --foreman-proxy-dhcp-gateway 192.0.2.1 \
   --foreman-proxy-dhcp-nameservers 192.0.2.2,192.0.2.3
   ```
2. For each affected Capsule, update the configuration of that Capsule in the Satellite web UI. See [Section 2.5, “Associating the DHCP service with a subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-dhcp-service-with-a-subnet "2.5. Associating the DHCP service with a subnet").
3. Optional: Secure the `dhcpd` API on the Capsule by using an Object Management Application Programming Interface (OMAPI) key:

   1. Install the required package:

      ```
      # satellite-maintain packages install bind-utils
      ```
   2. Generate an OMAPI key:

      ```
      # tsig-keygen -a Algorithm_Name My_Key_Name
      ```

      Use the following values in the command:

      `Algorithm_Name`
      :   Specifies the algorithm to be used to generate the key. You can use any of the values specified in the `tsig-keygen(8)` man page on your system. The default algorithm is HMAC-SHA256.

      `My_Key_Name`
      :   Specifies the name of the OMAPI key. The default name is `tsig-key`.

      The command outputs key information in the following format:

      ```
      key "My_Key_Name" {
      	algorithm Algorithm_Name;
      	secret "Key_Secret";
      };
      ```
4. Add the information about the key from the command output to the Capsule configuration:

   ```
   # satellite-installer \
   --foreman-proxy-dhcp-key-name "My_Key_Name" \
   --foreman-proxy-dhcp-key-algorithm "Algorithm_Name" \
   --foreman-proxy-dhcp-key-secret "Key_Secret"
   ```

   If you use the default algorithm, which is HMAC-SHA256, you can omit the algorithm line from the configuration.

## 2.3. Integrating a remote ISC DHCP server

If you have an ISC DHCP server in your network, but not on the same host as your Satellite Server, you can integrate this service into your Satellite Server.

With the remote ISC DHCP server integration, you can continue using your existing DHCP server, and Satellite manages IP leases and boot configurations on the DHCP server during the provisioning of hosts. Satellite uses an Object Management Application Programming Interface (OMAPI) key to update leases and the Network File System (NFS) protocol to access the ISC DHCP server configuration files and lease database.

### 2.3.1. Enabling OMAPI authentication in ISC DHCP

The integration of an existing remote ISC DHCP service requires that you enable the Object Management Application Programming Interface (OMAPI) in the DHCP service. Satellite uses OMAPI to remotely manage DHCP server objects.

**Prerequisites**

- The ISC DHCP service is deployed and functional.
- The firewall on the DHCP server allows access to the DHCP service (port 67/UDP).

**Procedure**

1. Create a security token:

   ```
   # tsig-keygen -a Algorithm_Name My_Key_Name
   ```

   Use the following values in the command:

   `Algorithm_Name`
   :   Specifies the algorithm to be used to generate the key. You can use any of the values specified in the `tsig-keygen(8)` man page on your system. The default algorithm is HMAC-SHA256.

   `My_Key_Name`
   :   Specifies the name of the OMAPI key. The default name is `tsig-key`.

   The command outputs key information in the following format:

   ```
   key "My_Key_Name" {
   	algorithm Algorithm_Name;
   	secret "Key_Secret";
   };
   ```
2. Edit the `/etc/dhcp/dhcpd.conf` file, and append the following settings:

   ```
   key "My_Key_Name" {
   	algorithm Algorithm_Name;
   	secret "Key_Secret";
   };
   omapi-port 7911;
   omapi-key My_Key_Name;
   ```

   The settings specified in the example include the following:

   `key "My_Key_Name"`
   :   Defines the key, its algorithm and encrypted password. Use the output of the `tsig-keygen` command for this directive.

   `omapi-port 7911`
   :   Enables the OMAPI protocol in ISC DHCP and defines the port of the protocol.

   `omapi-key My_Key_Name`
   :   Defines the name of the key the OMAPI interface uses. The name must match the one you specified in the `tsig-keygen` command.
3. Restart the `dhcpd` service:

   ```
   # systemctl restart dhcpd
   ```
4. Open the OMAPI port in the `firewalld` service:

   ```
   # firewall-cmd --add-port=7911/tcp
   ```
5. Make the changes persistent:

   ```
   # firewall-cmd --runtime-to-permanent
   ```

### 2.3.2. Sharing the DHCP configuration files and lease database over NFS

To integrate a remote ISC DHCP server, you must share its configuration and lease database over the Network File System (NFS). Afterwards, Satellite can access configuration settings, such as subnet definitions, and lease information that is not available over the ISC DHCP Object Management Application Programming Interface (OMAPI).

For example, you can use the NFS service.

**Prerequisites**

- The ISC DHCP service is deployed and functional.

**Procedure**

1. On Satellite Server, determine both the UID and the primary GID of the `foreman-proxy` user:

   ```
   # id -u foreman-proxy
   # id -g foreman-proxy
   ```

   You require these IDs in the next steps.
2. On the DHCP server, share the configuration of the DHCP service and lease database over NFS:

   1. Create the `foreman-proxy` group with the same group ID as on the Satellite Server:

      ```
      # groupadd -g My_User_ID foreman-proxy
      ```
   2. Create the `foreman-proxy` user with the same user ID and primary group ID as on the Satellite Server:

      ```
      # useradd -u My_User_ID -g My_Group_ID -s /sbin/nologin foreman-proxy
      ```
   3. Ensure that members of the `foreman-proxy` group can access the configuration file of the DHCP service:

      ```
      # chgrp -R foreman-proxy /etc/dhcp/
      # chmod g+rx /etc/dhcp/
      # chmod g+r /etc/dhcp/dhcpd.conf
      ```
   4. Install the `nfs-server` package:

      ```
      # dnf install nfs-utils
      ```
   5. Edit the `/etc/exports` file, and append share entries for the `/etc/dhcp/` and `/var/lib/dhcpd/` directories:

      ```
      /etc/dhcp        satellite.example.com(ro)
      /var/lib/dhcpd   satellite.example.com(ro)
      ```

      Share the directories in read-only mode and only with the Satellite Server or Capsule Server.
   6. Enable and start the NFS server service:

      ```
      # systemctl enable --now nfs-server
      ```
   7. Open the NFSv4 port in the `firewalld` service:

      ```
      # firewall-cmd --add-service=nfs
      ```
   8. Make the changes persistent:

      ```
      # firewall-cmd --runtime-to-permanent
      ```

**Next steps**

- By default, the NFS protocol is unencrypted. If you require an encrypted connection, configure NFS over TLS or Kerberos authentication after you completed this procedure. For more information, see [Configuring an NFS server with TLS support](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_using_network_file_services/deploying-an-nfs-server_configuring-and-using-network-file-services#configuring-an-nfs-server-with-tls-support_deploying-an-nfs-server) and [Setting up an NFS server with Kerberos in a Red Hat Enterprise Linux Identity Management domain](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_using_network_file_services/deploying-an-nfs-server_configuring-and-using-network-file-services#setting-up-an-nfs-server-with-kerberos-in-a-red-hat-identity-management-domain_deploying-an-nfs-server) in *Red Hat Enterprise Linux 9 Configuring and using network file services*.

### 2.3.3. Configuring Satellite Server or Capsule Server for use with ISC DHCP

After you have prepared the DHCP server, integrate the ISC DHCP server into your Satellite Server or Capsule Server.

**Prerequisites**

- You enabled Object Management Application Programming Interface (OMAPI) authentication in ISC DHCP. For more information, see [Section 2.3.1, “Enabling OMAPI authentication in ISC DHCP”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#enabling-omapi-authentication-in-isc-dhcp "2.3.1. Enabling OMAPI authentication in ISC DHCP").
- You shared the DHCP configuration and lease database over NFS. For more information, see [Section 2.3.2, “Sharing the DHCP configuration files and lease database over NFS”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#sharing-the-dhcp-configuration-files-and-lease-database-over-nfs "2.3.2. Sharing the DHCP configuration files and lease database over NFS").

**Procedure**

1. Install the required package:

   ```
   # satellite-maintain packages install nfs-utils
   ```
2. Create the directories into which you later mount the NFS shares:

   ```
   # mkdir -p \
   /srv/nfs/etc/dhcp \
   /srv/nfs/var/lib/dhcpd
   ```
3. Edit the `/etc/fstab` file, and add entries for the NFS shares to mount them automatically when the system boots:

   ```
   dhcp_server_fqdn:/etc/dhcp       /srv/nfs/etc/dhcp       nfs  ro,auto,context="system_u:object_r:dhcp_etc_t:s0"     0 0
   dhcp_server_fqdn:/var/lib/dhcpd  /srv/nfs/var/lib/dhcpd  nfs  ro,auto,context="system_u:object_r:dhcpd_state_t:s0"  0 0
   ```
4. Reload `systemd` so that this service uses the updated `/etc/fstab` file:

   ```
   # systemctl daemon-reload
   ```
5. Mount the NFS shares:

   ```
   # mount /srv/nfs/etc/dhcp/
   # mount /srv/nfs/var/lib/dhcpd/
   ```
6. Verify that the `foreman-proxy` user can access the files on the NFS server. For example:

   1. Display the first 5 lines of the `/srv/nfs/etc/dhcp/dhcpd.conf` file:

      ```
      $ su - foreman-proxy -c 'head -5 /srv/nfs/etc/dhcp/dhcpd.conf'
      ```
   2. Display the first 5 lines of the `/srv/nfs/var/lib/dhcpd/dhcpd.leases` file:

      ```
      $ su - foreman-proxy -c 'head -5 /srv/nfs/var/lib/dhcpd/dhcpd.leases'
      ```
7. Configure Satellite Server or Capsule Server to use the DHCP server:

   ```
   # satellite-installer \
   --foreman-proxy-dhcp true \
   --foreman-proxy-dhcp-provider remote_isc \
   --enable-foreman-proxy-plugin-dhcp-remote-isc \
   --foreman-proxy-dhcp-server dhcp_server_fqdn \
   --foreman-proxy-plugin-dhcp-remote-isc-dhcp-config /srv/nfs/etc/dhcp/dhcpd.conf \
   --foreman-proxy-plugin-dhcp-remote-isc-dhcp-leases /srv/nfs/var/lib/dhcpd/dhcpd.leases \
   --foreman-proxy-plugin-dhcp-remote-isc-key-name omapi_key \
   --foreman-proxy-plugin-dhcp-remote-isc-key-secret key_secret \
   --foreman-proxy-plugin-dhcp-remote-isc-omapi-port 7911
   ```
8. For each affected Capsule, update the configuration of that Capsule in the Satellite web UI. For more information, see [Section 2.5, “Associating the DHCP service with a subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-dhcp-service-with-a-subnet "2.5. Associating the DHCP service with a subnet").

## 2.4. Integrating Infoblox DHCP

If you have an Infoblox appliance in your network, you can integrate this service into Satellite Server and Capsule Server by using the Infoblox Web API (WAPI). With the integration, you can use your existing DHCP server, and Satellite manages IP leases and boot configurations on the DHCP server during the provisioning of hosts.

> **Note**
>
> Integrating Infoblox DHCP has the following limitations:
>
> - You can manage DHCP entries only in a single network and view, and you cannot edit the view after you create it.
> - Satellite Server uses the standard HTTPS web API to communicate with Infoblox. By default, it communicates only with a single node. If you require high availability, configure this feature in Infoblox.

**Prerequisites**

- You have an Infoblox account with the roles `DHCP Admin` and `DNS Admin`.
- The Infoblox roles have permissions or belong to an admin group that permits the accounts to perform tasks through the Infoblox API.

**Procedure**

1. Download the certificate from the Infoblox server, and store it in the `/etc/pki/ca-trust/source/anchors/infoblox.crt` file:

   ```
   # openssl s_client -showcerts -connect infoblox.example.com:443 </dev/null | \
   openssl x509 -text >/etc/pki/ca-trust/source/anchors/infoblox.crt
   ```

   The hostname must match the one for the Infoblox application in the X.509 certificate.
2. Add the Infoblox certificate to the system truststore:

   ```
   # update-ca-trust extract
   ```
3. Test the CA certificate by using it in a query to the Infoblox API:

   ```
   # curl -u admin:password https://infoblox.example.com/wapi/v2.0/network
   ```

   Example of a positive response:

   ```
   [
       {
           "_ref": "network/ZG5zLm5ldHdvcmskMTkyLjE2OC4yMDIuMC8yNC8w:infoblox.example.com/24/default",
           "network": "192.168.202.0/24",
           "network_view": "default"
       }
   ]
   ```
4. Configure Satellite Server or Capsule Server to connect to the Infoblox DHCP service:

   ```
   # satellite-installer \
   --foreman-proxy-dhcp true \
   --foreman-proxy-dhcp-provider infoblox \
   --enable-foreman-proxy-plugin-dhcp-infoblox \
   --foreman-proxy-dhcp-server infoblox.example.com \
   --foreman-proxy-plugin-dhcp-infoblox-username admin \
   --foreman-proxy-plugin-dhcp-infoblox-password password \
   --foreman-proxy-plugin-dhcp-infoblox-record-type fixedaddress \
   --foreman-proxy-plugin-dhcp-infoblox-dns-view default \
   --foreman-proxy-plugin-dhcp-infoblox-network-view default
   ```

   > **Note**
   >
   > If you want to use the DHCP and DNS Infoblox modules together, configure the DHCP Infoblox module with the `fixedaddress` record type only. The `host` record type is not supported in this scenario because it causes conflicts and you cannot rename hosts in Satellite.
5. For each affected Capsule, update the configuration of that Capsule in the Satellite web UI. For more information, see [Section 2.5, “Associating the DHCP service with a subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-dhcp-service-with-a-subnet "2.5. Associating the DHCP service with a subnet").

## 2.5. Associating the DHCP service with a subnet

After you configured or changed the DHCP provider, you must update the configuration of each affected Capsule in the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
2. Select the subnet name.
3. On the **Subnet** tab, set **IPAM** to **DHCP**.
4. On the **Capsule** tab, set **DHCP Proxy** to your Capsule.
5. Click **Submit**.

## 2.6. Disabling Capsule DHCP pinging

You can disable DHCP IP address validation on Capsule to reduce network traffic or avoid triggering network security alerts.

By default, A DHCP Capsule performs ICMP ping and TCP echo connection attempts to validate whether an IP address is free. This happens for hosts in subnets that have the IPAM configured as DHCP.

**Procedure**

- On your Capsule, disable DHCP IP address pinging:

  ```
  # satellite-installer --foreman-proxy-dhcp-ping-free-ip false
  ```

## 2.7. Disabling DHCP for integration

If you want to manually manage a DHCP service and not integrate it into Satellite Server, you must prevent Satellite from maintaining this service on the operating system and disable orchestration to avoid errors.

> **Note**
>
> Disabling DHCP in Satellite does not remove the related backend service on the operating system.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
2. For each subnet that is associated with the DHCP Capsule:

   1. Select the subnet.
   2. On the **Capsules** tab, clear the **DHCP Capsule** field.
   3. Click **Submit**.
3. On Satellite Server and Capsule Server, enter:

   ```
   # satellite-installer --foreman-proxy-dhcp false
   ```

   > **Note**
   >
   > Satellite does not perform orchestration when a Capsule is not set for a given subnet. When you disable Capsule associations, orchestration commands for existing hosts can fail if the expected records and configuration files are not present.

## 2.8. Troubleshooting DHCP problems

Satellite can manage an ISC DHCP server on Satellite Server or Capsule Servers. Satellite can list, create, and delete DHCP reservations and leases.

However, you might encounter the following problems:

Out of sync DHCP records
:   When an error occurs during DHCP orchestration, DHCP records in the Satellite database and the DHCP server might not match. To fix this, you must add missing DHCP records from the Satellite database to the DHCP server and then remove unwanted records from the DHCP server as per the following steps:

    1. Preview the DHCP records that are going to be added to the DHCP server:

       ```
       # foreman-rake orchestration:dhcp:add_missing subnet_name=NAME
       ```
    2. If you are satisfied by the preview changes in the previous step, apply them by entering the above command with the `perform=1` argument:

       ```
       # foreman-rake orchestration:dhcp:add_missing subnet_name=NAME perform=1
       ```
    3. To keep DHCP records in Satellite and in the DHCP server synchronized, you can remove unwanted DHCP records from the DHCP server. Note that Satellite assumes that all managed DHCP servers do not contain third-party records, therefore, this step might delete those unexpected records. Preview what records are going to be removed from the DHCP server:

       ```
       # foreman-rake orchestration:dhcp:remove_offending subnet_name=NAME
       ```
    4. If you are satisfied by the preview changes in the previous step, apply them by entering the above command with the `perform=1` argument:

       ```
       # foreman-rake orchestration:dhcp:remove_offending subnet_name=NAME perform=1
       ```

PXE loader option change
:   When the PXE loader option is changed for an existing host, this causes a DHCP conflict. The only workaround is to overwrite the DHCP entry.

Incorrect permissions on DHCP files
:   An operating system update can update the `dhcpd` package. This causes the permissions of important directories and files to reset so that the DHCP Capsule cannot read the required information.

    For more information, see [DHCP error while provisioning host from Satellite server Error ERF12-6899 ProxyAPI::ProxyException: Unable to set DHCP entry RestClient::ResourceNotFound 404 Resource Not Found](https://access.redhat.com/solutions/2952061) on Red Hat Knowledgebase.

Changing the DHCP Capsule entry
:   Satellite manages DHCP records only for hosts that are assigned to subnets with a DHCP Capsule set. If you create a host and then clear or change the DHCP Capsule, when you attempt to delete the host, the action fails.

    If you create a host without setting the DHCP Capsule and then try to set the DHCP Capsule, this causes DHCP conflicts.

Deleted hosts entries in the `dhcpd.leases` file
:   Any changes to a DHCP lease are appended to the end of the `dhcpd.leases` file. Because entries are appended to the file, it is possible that two or more entries of the same lease can exist in the `dhcpd.leases` file at the same time. When there are two or more entries of the same lease, the last entry in the file takes precedence. Group, subgroup and host declarations in the lease file are processed in the same manner. If a lease is deleted, `{ deleted; }` is appended to the declaration.
