---
title: "Preparing your environment for Satellite Server installation"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_disconnected_network_environment"
guide_title: "Installing Satellite Server in a disconnected network environment"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#preparing-your-environment-for-satellite-server-installation"
---
# Chapter 2. Preparing your environment for Satellite Server installation

Prepare your environment for Satellite Server installation by opening required network ports, verifying DNS resolution, and configuring repositories.

## 2.1. Opening required ports

Open the required network ports to enable communication between Satellite components across your infrastructure, including firewall configurations for both host-based and network-based firewalls.

> **Note**
>
> Some cloud solutions must be specifically configured to allow communications between machines because they isolate machines similarly to network-based firewalls. If you use an application-based firewall, ensure that the application-based firewall permits all applications that are listed in the tables and known to your firewall. If possible, disable the application checking and allow open port communication based on the protocol.

**Procedure**

1. Open the ports for clients on Satellite Server:

   ```
   # firewall-cmd \
   --add-port="8000/tcp" \
   --add-port="9090/tcp"
   ```
2. Allow access to services on Satellite Server:

   ```
   # firewall-cmd \
   --add-service=dns \
   --add-service=dhcp \
   --add-service=tftp \
   --add-service=http \
   --add-service=https \
   --add-service=puppetmaster
   ```
3. Make the changes persistent:

   ```
   # firewall-cmd --runtime-to-permanent
   ```

**Verification**

- View all firewall zones and allowed services:

  ```
  # firewall-cmd --list-all
  ```

**Additional resources**

- [Networking considerations in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#networking-considerations-in-satellite)
- [Using and configuring firewalld in *Red Hat Enterprise Linux 9 Configuring firewalls and packet filters*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_firewalls_and_packet_filters/using-and-configuring-firewalld_firewall-packet-filters)

## 2.2. Verifying DNS resolution

Verify the full forward and reverse DNS resolution using a fully-qualified domain name to prevent issues while installing Satellite.

**Procedure**

1. Ensure that the host name and local host resolve correctly:

   ```
   # ping -c1 localhost
   # ping -c1 `hostname -f` # my_system.domain.com
   ```

   Successful name resolution results in output similar to the following:

   ```
   # ping -c1 localhost
   PING localhost (127.0.0.1) 56(84) bytes of data.
   64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.043 ms

   --- localhost ping statistics ---
   1 packets transmitted, 1 received, 0% packet loss, time 0ms
   rtt min/avg/max/mdev = 0.043/0.043/0.043/0.000 ms

   # ping -c1 `hostname -f`
   PING hostname.gateway (XX.XX.XX.XX) 56(84) bytes of data.
   64 bytes from hostname.gateway (XX.XX.XX.XX): icmp_seq=1 ttl=64 time=0.019 ms

   --- localhost.gateway ping statistics ---
   1 packets transmitted, 1 received, 0% packet loss, time 0ms
   rtt min/avg/max/mdev = 0.019/0.019/0.019/0.000 ms
   ```
2. To avoid discrepancies with static and transient host names, set all the host names on the system by entering the following command:

   ```
   # hostnamectl set-hostname name
   ```

   > **Warning**
   >
   > Name resolution is critical to the operation of Satellite. If Satellite cannot properly resolve its fully qualified domain name, tasks such as content management, subscription management, and provisioning will fail.

**Additional resources**

- [Changing a hostname using hostnamectl in *Red Hat Enterprise Linux 9 Configuring and managing networking*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_networking/index#proc_changing-a-hostname-using-hostnamectl_assembly_changing-a-hostname)

## 2.3. Preparing Satellite for using external databases

By default, the Satellite installation process includes installing a PostgreSQL database on the same host as Satellite Server. However, in certain Satellite deployments, using external databases instead of the default local databases can help with the server load or have other benefits.

**Prerequisites**

- You have considered whether using an external database is beneficial for your use case. For more information, see [PostgreSQL as an external database considerations](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#postgresql-as-an-external-database-considerations_admin) in *Administering Red Hat Satellite*.

**Procedure**

- Install PostgreSQL on an external database host you prepared. For more information, see [Installing PostgreSQL as an external database](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#installing-postgresql-as-an-external-database) in *Administering Red Hat Satellite*.

**Next steps**

- To set up an external database when installing Satellite, see [Section 3.6, “Configuring Satellite Server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#configuring-satellite-server "3.6. Configuring Satellite Server").

**Additional resources**

- [Migrating an existing Satellite deployment to an external database in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Migrating_from_Internal_Databases_to_External_Databases_admin)
