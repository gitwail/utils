---
title: "Preparing networking for host management"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management"
---
# Chapter 2. Preparing networking for host management

You must configure network services on your Capsules based on the provisioning type.

New hosts must have access to either your Satellite Server or any Capsule Server. If your hosts are on isolated networks and cannot connect to Satellite Server directly, you must provision your hosts from Capsule Servers. Provisioning by using Capsule Servers can save on network bandwidth.

Configuring Capsules has two basic requirements:

1. Configuring network services. This includes:

   - Content delivery services
   - Network services (DHCP, DNS, and TFTP)
   - Puppet configuration
2. Defining network resource data in Satellite Server to help configure network interfaces on new hosts.

The following instructions have similar applications to configuring Capsule Servers managing a specific network.

**Additional resources**

- [Integrating provisioning infrastructure services](https://docs.theforeman.org/3.18/Integrating_Provisioning_Infrastructure_Services/index-satellite.html#)

## 2.1. Facts and NIC filtering

Facts describe aspects such as total memory, operating system version, or architecture as reported by the host. You can find facts in **Monitor** > **Facts** and search hosts through facts or use facts in templates.

Satellite collects facts from multiple sources:

- `subscription manager`
- `ansible`
- `puppet`

Satellite is an inventory system for hosts and network interfaces. For hypervisors or container hosts, adding thousands of interfaces per host and updating the inventory every few minutes is inadequate. For each individual NIC reported, Satellite creates a NIC entry and those entries are never removed from the database. Parsing all the facts and comparing all records in the database makes Satellite extremely slow and unusable. To optimize the performance of various actions, most importantly fact import, you can use the options available on the **Facts** tab under **Administer** > **Settings**.

## 2.2. Optimizing performance by removing NICs from database

You can improve performance by filtering network interface card (NIC) connections from the database. If you name the virtual interfaces differently, you can update this filter to use it according to your requirements.

By default, these options are set for most common hypervisors.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings** and select the **Facts** tab.
2. To filter out all interfaces starting with specific names, for example, `blu`, add `blu*` to the `Ignore interfaces with matching identifier` option.
3. To prevent databases from storing facts related to interfaces starting with specific names, for example, `blu`, add `blu*` to the `Exclude pattern for facts stored in Satellite` option.

   By default, it contains the same list as the `Ignore interfaces with matching identifier` option. You can override it based on the your requirements. This filters out facts completely without storing them.
4. To remove facts from the database, enter the following command:

   ```
   # foreman-rake facts:clean
   ```

   This command removes all facts matching with the filter added in **Administer** > **Settings** > **Facts** > the `Exclude pattern for facts stored in Satellite` option.
5. To remove interfaces from the database, enter the following command:

   ```
   # foreman-rake interfaces:clean
   ```

   This command removes all interfaces matching with the filter added in **Administer** > **Settings** > **Facts** > the `Ignore interfaces with matching identifier` option.

## 2.3. Resources for network-based provisioning

You must set up and configure networking resources to provision hosts over a network.

The following networking resources are required:

Domain
:   You must assign every host that is managed by Satellite to a domain. Using the domain, Satellite can manage A, AAAA, and PTR records. Even if you do not want Satellite to manage your DNS servers, you still must create and associate at least one domain. Domains are included in the naming conventions Satellite hosts, for example, a host with the name `test123` in the `example.com` domain has the fully qualified domain name `test123.example.com`.

Subnet
:   You must assign every host managed by Satellite to a subnet. Using subnets, Satellite can then manage IPv4 reservations. If there are no reservation integrations, you still must create and associate at least one subnet. When you manage a subnet in Satellite, you cannot create DHCP records for that subnet outside of Satellite. In Satellite, you can use IP Address Management (IPAM) to manage IP addresses with one of the following options:

    - **DHCP**: DHCP Capsule manages the assignment of IP addresses by finding the next available IP address starting from the first address of the range and skipping all addresses that are reserved. Before assigning an IP address, Capsule sends an ICMP and TCP pings to check whether the IP address is in use. Note that if a host is powered off, or has a firewall configured to disable connections, Satellite makes a false assumption that the IP address is available. This check does not work for hosts that are turned off, therefore, the **DHCP** option can only be used with subnets that Satellite controls and that do not have any hosts created externally.

      The Capsule DHCP module retains the offered IP addresses for a short period of time to prevent collisions during concurrent access, so some IP addresses in the IP range might remain temporarily unused.
    - **Internal DB**: Satellite finds the next available IP address from the Subnet range by excluding all IP addresses from the Satellite database in sequence. The primary source of data is the database, not DHCP reservations. This IPAM is not safe when multiple hosts are being created in parallel; in that case, use **DHCP** or **Random DB** IPAM instead.
    - **Random DB**: Satellite finds the next available IP address from the Subnet range by excluding all IP addresses from the Satellite database randomly. The primary source of data is the database, not DHCP reservations. This IPAM is safe to use with concurrent host creation as IP addresses are returned in random order, minimizing the chance of a conflict.
    - **EUI-64**: Extended Unique Identifier (EUI) 64bit IPv6 address generation, as per RFC2373, is obtained through the 48-bit MAC address.
    - **External IPAM**: Delegates IPAM to an external system through Capsule feature. Satellite currently does not ship with any external IPAM implementations, but several plugins are in development.
    - **None**: IP address for each host must be entered manually.

      Options DHCP, Internal DB and Random DB can lead to DHCP conflicts on subnets with records created externally. These subnets must be under exclusive Satellite control.

DHCP Ranges
:   You can define the same DHCP range in Satellite Server for both discovered and provisioned systems, but use a separate range for each service within the same subnet.

### 2.3.1. Options in managed DHCPv4

When Satellite manages the DHCP service and can update the DHCP configuration, Satellite sets the `next-server` and `filename` DHCP options.

`next-server`
:   The `next-server` option provides the IP address of the TFTP server to boot from. This option is not set by default and must be set for each TFTP Capsule. You can use the `satellite-installer` command with the `--foreman-proxy-tftp-servername` argument to set the TFTP server in the `/etc/foreman-proxy/settings.d/tftp.yml` file:

    ```
    # satellite-installer --foreman-proxy-tftp-servername 1.2.3.4
    ```

    Each TFTP Capsule then reports this setting through the API and Satellite can retrieve the configuration information when it creates the DHCP record.

    When the PXE loader is set to `none`, Satellite does not populate the `next-server` option into the DHCP record.

    If the `next-server` option remains undefined, Satellite calls the Capsule API to retrieve the server name as specified by the `--foreman-proxy-tftp-servername` argument in a `satellite-installer` run. If the Capsule API call does not return a server name, Satellite uses the hostname of the Capsule.

`filename`
:   The `filename` option contains the full path to the file that downloads and executes during provisioning. The PXE loader that you select for the host or host group defines which `filename` option to use. When the PXE loader is set to `none`, Satellite does not populate the `filename` option into the DHCP record. Depending on the PXE loader option, the `filename` changes as follows:

    | PXE loader option | filename entry | Notes |
    | --- | --- | --- |
    | PXELinux BIOS | `pxelinux.0` |  |
    | PXELinux UEFI | `pxelinux.efi` |  |
    | iPXE Chain BIOS | `undionly.kpxe` |  |
    | PXEGrub2 UEFI | `grub2/grubx64.efi` | x64 can differ depending on architecture |
    | iPXE UEFI HTTP | `http://capsule.example.com:8000/httpboot/ipxe-x64.efi` | Requires the `httpboot` feature and renders the `filename` as a full URL where *capsule.example.com* is a known host name of Capsule in Satellite. |
    | Grub2 UEFI HTTP | `http://capsule.example.com:8000/httpboot/grub2/grubx64.efi` | Requires the `httpboot` feature and renders the `filename` as a full URL where *capsule.example.com* is a known host name of Capsule in Satellite. |

### 2.3.2. Options in unmanaged DHCPv6

To provision hosts over TFTP in an IPv6-only network, configure the DHCP server to respond with the `bootfile-url` DHCP option. Satellite cannot manage the DHCPv6 service, therefore, you have to configure your DHCP server manually.

`bootfile-url`
:   The URL value of this option has to point to a file on TFTP Capsule that is a first-stage boot loader, such as `pxelinux.0`. Example configuration:

    ```
       "option-data": [
          {
             "name": "bootfile-url",
             "data": "tftp://2001:db8:1::1/pxelinux.0"
          }
       ],
    ```

## 2.4. Prerequisites for image-based provisioning

Before you deploy pre-built cloud instances or virtual machines, DNS and TFTP must be configured so that hosts across multiple subnets or domains can locate and retrieve image installation content. The requirements depend on the boot configuration method.

Post-boot configuration method
:   Images that use the `finish` post-boot configuration scripts require a managed DHCP server, for example, your Satellite Server or Capsule Servers. The host must be created with a subnet associated with a DHCP Capsule, and the IP address of the host must be a valid IP address from the DHCP range.

    It is possible to use an external DHCP service, but IP addresses must be entered manually. The SSH credentials corresponding to the configuration in the image must be configured in Satellite to enable the post-boot configuration to be made.

    When you troubleshoot a virtual machine booted from an image that depends on post-configuration scripts, verify the following:

    - The host has a subnet assigned in Satellite Server.
    - The subnet has a DHCP Capsule assigned in Satellite Server.
    - The host has a valid IP address assigned in Satellite Server.
    - The IP address acquired by the virtual machine by using DHCP matches the address configured in Satellite Server.
    - The virtual machine created from an image responds to SSH requests.
    - The virtual machine created from an image authorizes the user and password, over SSH, which is associated with the image being deployed.
    - Satellite Server has access to the virtual machine via SSH keys. This is required for the virtual machine to receive post-configuration scripts from Satellite Server.

Pre-boot initialization configuration method
:   Images that use the `cloud-init` scripts require a DHCP server to avoid having to include the IP address in the image. A managed DHCP Capsule is preferred. The image must have the `cloud-init` service configured to start when the system boots and fetch a script or configuration data to use in completing the configuration.

    When you troubleshoot a virtual machine booted from an image that depends on initialization scripts included in the image, verify the following:

    - There is a DHCP server on the subnet.
    - The virtual machine has the `cloud-init` service installed and enabled.

    For information about the differing levels of support for `finish` and `cloud-init` scripts in virtual-machine images, see the Red Hat Knowledgebase Solution [What are the supported compute resources for the finish and cloud-init scripts](https://access.redhat.com/solutions/2987171) on the Red Hat Customer Portal.

### 2.4.1. Multiple subnets or domains using installer

The `satellite-installer` options allow only for a single DHCP subnet or DNS domain. One way to define more than one subnet is by using a custom configuration file.

For every additional subnet or domain, create an entry in `/etc/foreman-installer/custom-hiera.yaml` file:

```
dhcp::pools:
 isolated.lan:
   network: 192.168.99.0
   mask: 255.255.255.0
   gateway: 192.168.99.1
   range: 192.168.99.5 192.168.99.49

dns::zones:
  # creates @ SOA $::fqdn root.example.com.
  # creates $::fqdn A $::ipaddress
  example.com: {}

  # creates @ SOA test.example.net. hostmaster.example.com.
  # creates test.example.net A 192.0.2.100
  example.net:
    soa: test.example.net
    soaip: 192.0.2.100
    contact: hostmaster.example.com.

  # creates @ SOA $::fqdn root.example.org.
  # does NOT create an A record
  example.org:
    reverse: true

  # creates @ SOA $::fqdn hostmaster.example.com.
  2.0.192.in-addr.arpa:
    reverse: true
    contact: hostmaster.example.com.
```

Execute `satellite-installer` to perform the changes and verify that the `/etc/dhcp/dhcpd.conf` contains appropriate entries. Subnets must be then defined in Satellite database.

### 2.4.2. DNS options for network configuration

You can use the following options of `satellite-installer` to configure DNS.

--foreman-proxy-dns
:   Enables the DNS feature. You can set this option to `true` or `false`.

--foreman-proxy-dns-provider
:   Selects the provider to be used.

--foreman-proxy-dns-managed
:   Let the installer manage ISC BIND. This is only relevant when using the `nsupdate` and `nsupdate_gss` providers. You can set this option to `true` or `false`.

--foreman-proxy-dns-forwarders
:   Sets the DNS forwarders. Only used when ISC BIND is managed by the installer. Set this to your DNS recursors.

--foreman-proxy-dns-interface
:   Sets the interface to listen for DNS requests. Only used when ISC BIND is managed by the installer. Set this to `eth1`.

--foreman-proxy-dns-reverse
:   The DNS reverse zone name. Only used when ISC BIND is managed by the installer.

--foreman-proxy-dns-server
:   Sets the address of the DNS server. Only used by the `nsupdate`, `nsupdate_gss`, and `infoblox` providers.

--foreman-proxy-dns-zone
:   Sets the DNS zone name. Only used when ISC BIND is managed by the installer.

Run `satellite-installer --help` to view more options related to DNS and other Capsule services.

### 2.4.3. TFTP options for network configuration

You can use the following options of `satellite-installer` to configure TFTP.

--foreman-proxy-tftp
:   Enables TFTP service. You can set this option to `true` or `false`.

--foreman-proxy-tftp-managed
:   Enables Foreman to manage the TFTP service. You can set this option to `true` or `false`.

--foreman-proxy-tftp-servername
:   Sets the TFTP server to use. Ensure that you use Capsule’s IP address.

Run `satellite-installer --help` to view more options related to TFTP and other Capsule services.

## 2.5. Adding a domain to Satellite Server by using Satellite web UI

Satellite Server defines domain names for each host on the network. Satellite Server must have information about the domain and Capsule Server responsible for domain name assignment.

**Prerequisites**

- The selected domain name is available. Satellite Server might already have the relevant domain created as part of Satellite Server installation. Switch the context to `Any Organization` and `Any Location` then check the domain list to see if it exists.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Domains** and click **Create Domain**.
2. In the **DNS Domain** field, enter the full DNS domain name.
3. In the **Fullname** field, enter the plain text name of the domain.
4. Click the **Parameters** tab and configure any domain level parameters to apply to hosts attached to this domain. For example, user defined Boolean or string parameters to use in templates.
5. Click **Add Parameter** and fill in the **Name** and **Value** fields.
6. Click the **Locations** tab, and add the location where the domain resides.
7. Click the **Organizations** tab, and add the organization that the domain belongs to.
8. Click **Submit** to save the changes.

## 2.6. Adding a domain to Satellite Server by using Hammer CLI

Satellite Server defines domain names for each host on the network. Satellite Server must have information about the domain and Capsule Server responsible for domain name assignment.

**Prerequisites**

- The selected domain name is available. Satellite Server might already have the relevant domain created as part of Satellite Server installation. Switch the context to `Any Organization` and `Any Location` then check the domain list to see if it exists.

**Procedure**

- Use the `hammer domain create` command to create a domain:

  ```
  $ hammer domain create \
  --description "My_Domain" \
  --dns-id My_DNS_Capsule_ID \
  --locations "My_Location" \
  --name "my-domain.tld" \
  --organizations "My_Organization"
  ```

## 2.7. Adding a subnet to Satellite Server by using Satellite web UI

You must add information for each of your subnets to Satellite Server because Satellite configures interfaces for new hosts. To configure interfaces, Satellite Server must have all the information about the network that connects these interfaces.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
2. In the Subnets window, click **Create Subnet**.
3. In the **Name** field, enter a name for the subnet.
4. In the **Description** field, enter a description for the subnet.
5. In the **Network address** field, enter the network address for the subnet.
6. In the **Network prefix** field, enter the network prefix for the subnet.
7. In the **Network mask** field, enter the network mask for the subnet.
8. In the **Gateway address** field, enter the external gateway for the subnet.
9. In the **Primary DNS server** field, enter a primary DNS for the subnet.
10. In the **Secondary DNS server**, enter a secondary DNS for the subnet.
11. From the **IPAM** list, select the method that you want to use for IP address management (IPAM). For more information about IPAM, see [Section 2.3, “Resources for network-based provisioning”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#resources-for-network-based-provisioning "2.3. Resources for network-based provisioning").
12. Enter the information for the IPAM method that you select. Click the **Remote Execution** tab and select the Capsule that controls the remote execution.
13. Click the **Domains** tab and select the domains that apply to this subnet.
14. Click the **Capsules** tab and select the Capsule that applies to each service in the subnet, including DHCP, TFTP, and reverse DNS services.
15. Click the **Parameters** tab and configure any subnet level parameters to apply to hosts attached to this subnet. For example, user defined Boolean or string parameters to use in templates.
16. Click the **Locations** tab and select the locations that use this Capsule.
17. Click the **Organizations** tab and select the organizations that use this Capsule.
18. Click **Submit** to save the subnet information.

## 2.8. Adding a subnet to Satellite Server by using Hammer CLI

You must add information for each of your subnets to Satellite Server because Satellite configures interfaces for new hosts. To configure interfaces, Satellite Server must have all the information about the network that connects these interfaces.

**Procedure**

- Create a subnet:

  ```
  $ hammer subnet create \
  --boot-mode "DHCP" \
  --description "My_Description" \
  --dhcp-id My_DHCP_Capsule_ID \
  --dns-id My_DNS_Capsule_ID \
  --dns-primary "192.168.140.2" \
  --dns-secondary "8.8.8.8" \
  --domains "my-domain.tld" \ --from "192.168.140.111" \ --gateway "192.168.140.1" \ --ipam "DHCP" \ --locations "_My_Location" \
  --mask "255.255.255.0" \
  --name "My_Network" \
  --network "192.168.140.0" \
  --organizations "My_Organization" \
  --tftp-id My_TFTP_Capsule_ID \
  --to "192.168.140.250"
  ```

## 2.9. Troubleshooting DNS problems

DNS problems might prevent hosts from being provisioned because they cannot correctly resolve Satellite Server or Capsule Server hostnames required to download installation content or configuration files.

DNS server configuration considerations
:   During the DNS record creation, Satellite performs conflict DNS lookups to verify that the host name is not in active use. This check runs against one of the following DNS servers:

    - The system-wide resolver if **Administer** > **Settings** > **Query local nameservers** is set to **true**.
    - The nameservers that are defined in the subnet associated with the host.
    - The authoritative NS-Records that are queried from the SOA from the domain name associated with the host.

    If you experience timeouts during DNS conflict resolution, check the following settings:

    - The subnet nameservers must be reachable from Satellite Server.
    - The domain name must have a Start of Authority (SOA) record available from Satellite Server.
    - The system resolver in the `/etc/resolv.conf` file must have a valid and working configuration.
