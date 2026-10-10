---
title: "Configuring network interfaces"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-network-interfaces"
---
# Chapter 10. Configuring network interfaces

Satellite supports specifying multiple network interfaces for a single host. This lets you add physical, virtual, bonded, bridge, or BMC interfaces as needed for your network layout.

## 10.1. Configuring a physical interface

You can configure a physical network interface for a host to set the MAC address, device identifier, and network or DNS settings.

**Procedure**

1. Navigate to the **Add Interface** form:

   1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
   2. Click **Edit** next to the host you want to edit.
   3. On the **Interfaces** tab, click **Add Interface**.
2. Specify the general interface settings:

   1. Ensure **Interface** is selected as the type.
   2. Specify a **MAC address**. This setting is required.
   3. Specify the **Device Identifier**, for example `eth0`.
3. Configure network and DNS settings:

   1. Specify the **DNS name** associated with the host’s IP address.
   2. Select a domain from the **Domain** list.
   3. Select a subnet in the **IPv4 Subnet** or **IPv6 Subnet** list.
   4. Specify the **IPv4 address** or **IPv6 address**.

      > **Note**
      >
      > Managed interfaces with an assigned DHCP Capsule Server require this setting for creating a DHCP lease. DHCP-enabled managed interfaces are automatically provided with a suggested IP address.
4. Specify interface management options:

   1. Select whether the interface is **Managed**.
   2. Select whether this is the **Primary** interface for the host.
   3. Select whether this is the **Provision** interface for the host.
   4. Select whether to use the interface for **Remote execution**.
5. Click **OK** to save the interface configuration.
6. Click **Submit** to apply the changes to the host.

## 10.2. Configuring a virtual interface

You can configure a virtual interface for a host as a VLAN or an alias. Use a VLAN to connect to separate network segments on one physical interface, or use an alias to add another IP address to an existing interface.

- A VLAN interface allows the host to connect to separate network segments using a single physical interface.
- An alias interface is an additional IP address attached to an existing interface. An alias interface automatically inherits a MAC address from the interface it is attached to; therefore, you can create an alias without specifying a MAC address. The interface must be specified in a subnet with boot mode set to `static`.

> **Note**
>
> Virtual interfaces currently require a MAC address of a physical device. Therefore, the configuration of these interfaces works only on bare-metal hosts.

**Procedure**

1. Navigate to the **Add Interface** form:

   1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
   2. Click **Edit** next to the host you want to edit.
   3. On the **Interfaces** tab, click **Add Interface**.
2. Specify the general interface settings:

   1. Ensure **Interface** is selected as the type.
   2. If the virtual interface is managed, specify a **MAC address**.
   3. Specify ID in the **Device Identifier** field.

      - For a VLAN, use the `eth1.10` format.
      - For an alias, use the `eth1:10` format.
3. Configure a virtual NIC:

   1. Select the **Virtual NIC** checkbox.
   2. Optionally, specify a VLAN **Tag**.
   3. Specify the identifier of the physical interface to which the virtual interface is **Attached to**, for example `eth1`. This setting is required.
4. Click **OK** to save the interface configuration.
5. Click **Submit** to apply the changes to the host.

## 10.3. Configuring a bonded interface by using Satellite web UI

You can combine multiple physical interfaces by configuring a bonded interface for the host. Network interface card (NIC) bonding binds multiple interfaces into one logical interface that appears as a single device with one MAC address. Bonding increases bandwidth and provides redundancy by making two or more NICs act as one.

> **Note**
>
> Bonded interfaces currently require a MAC address of a physical device. Therefore, the configuration of these interfaces works only on bare-metal hosts.

**Procedure**

1. Navigate to the **Add Interface** form:

   1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
   2. Click **Edit** next to the host you want to edit.
   3. On the **Interfaces** tab, click **Add Interface**.
2. Select **Bond** from the **Type** list.
3. Specify the general interface settings:

   1. In the **Device Identifier** field, specify the interface ID in the `bond0` format .
   2. Specify a **MAC address**.
   3. If you are configuring a secondary interface, select **Managed**. Otherwise, Satellite does not apply the configuration.
4. Add the configuration specific to bonded interfaces:

   1. **Mode**: Select the bonding mode.
   2. **Attached devices**: Specify a comma-separated list of identifiers of attached devices. These can be physical interfaces or VLANs.
   3. **Bond options**: Specify a space-separated list of configuration options, for example `miimon=100`.
5. Click **OK** to save the interface configuration.
6. Click **Submit** to apply the changes to the host.

## 10.4. Configuring a bonded interface by using Hammer CLI

You can combine multiple physical interfaces by configuring a bonded interface for the host. Network interface card (NIC) bonding binds multiple interfaces into one logical interface that appears as a single device with one MAC address. Bonding increases bandwidth and provides redundancy by making two or more NICs act as one.

> **Note**
>
> Bonded interfaces currently require a MAC address of a physical device. Therefore, the configuration of these interfaces works only on bare-metal hosts.

**Procedure**

- Create a host with a bonded interface:

  ```
  $ hammer host create \
  --ask-root-password yes \
  --hostgroup My_Host_Group \
  --ip=My_IP_Address \
  --mac=My_MAC_Address \
  --managed true \
  --interface="identifier=My_NIC_1, mac=_My_MAC_Address_1, managed=true, type=Nic::Managed, domain_id=My_Domain_ID, subnet_id=My_Subnet_ID" \
  --interface="identifier=My_NIC_2, mac=My_MAC_Address_2, managed=true, type=Nic::Managed, domain_id=My_Domain_ID, subnet_id=My_Subnet_ID" \
  --interface="identifier=bondN, ip=My_IP_Address_2, type=Nic::Bond, mode=active-backup, attached_devices=[My_NIC_1,My_NIC_2], managed=true, domain_id=My_Domain_ID, subnet_id=My_Subnet_ID" \
  --location "My_Location" \
  --name "My_Host_Name" \
  --organization "My_Organization" \
  --subnet-id=My_Subnet_ID
  ```

  Replace `bondN` with `bond` and the ID of your device identifier, for example, `bond0`.

## 10.5. Configuring a bridge interface

You can configure a bridge interface for a host to forward traffic between networks. Use a bridge when you need to connect network segments or run virtual machines with external network access.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click **Edit** next to the host you want to edit.
3. On the **Interfaces** tab, click **Add Interface**.
4. Select **Bridge** from the **Type** list.
5. Specify a **MAC address**.
6. In the **Device Identifier** field, specify the interface ID in the `bridge0` format.
7. If you are configuring a secondary interface, select **Managed**.
8. In the **Attached devices** field, specify a comma-separated list of identifiers of attached devices. These can be physical or virtual Ethernet devices, bonds, or VLAN devices.
9. Click **OK** to save the interface configuration.
10. Click **Submit** to apply the changes to the host.

## 10.6. Bonding modes available in Satellite

The following bonding modes are available when managing network interfaces in Satellite.

| Bonding Mode | Description |
| --- | --- |
| balance-rr | Transmissions are received and sent sequentially on each bonded interface. |
| active-backup | Transmissions are received and sent through the first available bonded interface. Another bonded interface is only used if the active bonded interface fails. |
| balance-xor | Transmissions are based on the selected hash policy. In this mode, traffic destined for specific peers is always sent over the same interface. |
| broadcast | All transmissions are sent on all bonded interfaces. |
| 802.a3 | Creates aggregation groups that share the same settings. Transmits and receives on all interfaces in the active group. |
| balance-tlb | The outgoing traffic is distributed according to the current load on each bonded interface. |
| balance-alb | Receive load balancing is achieved through Address Resolution Protocol (ARP) negotiation. |

## 10.7. Configuring a baseboard management controller (BMC) interface

You can configure a baseboard management controller (BMC) interface for a host. A BMC lets you remotely monitor and manage the physical state of the machine and control host power from Satellite. This applies to bare-metal hosts that support BMC.

**Prerequisites**

- Power management is enabled on Satellite Server. For more information, see [Enabling power management on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#enabling-power-management-on-hosts_satellite) in *Installing Satellite Server in a connected network environment*.
- If you use Capsule Server instead of Satellite Server, power management must be enabled on your Capsule Server. For more information, see [Enabling power management on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#enabling-power-management-on-hosts_satellite) in *Installing Capsule Server*.
- You know the MAC address, IP address, and other details of the BMC interface on the host, and authentication credentials for that interface.

  > **Note**
  >
  > You only need the MAC address for the BMC interface if the BMC interface is managed, so that it can create a DHCP reservation.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Edit your host.
3. On the **Interfaces** tab, click **Add Interface**.
4. Select **BMC** from the **Type** list.
5. Specify the general interface settings:

   1. If the BMC is managed, specify a **MAC address**.
   2. Specify the **Device Identifier**.
6. Specify the configuration options specific to BMC interfaces:

   1. **Username** and **Password**: Specify any authentication credentials required by BMC.
   2. **Provider**: Specify the BMC provider.
7. Click **OK** to save the interface configuration.
8. Click **Submit** to apply the changes to the host.

## 10.8. Network interface configuration options

When adding a network interface, you need to specify several configuration options. The following lists provide information on the relevant options for the different types of interfaces.

Physical interface settings
:   **Device Identifier**
    :   The identifier is used to specify this physical interface when creating bonded interfaces, VLANs, and aliases.

    **DNS name**
    :   Satellite saves this name in the Capsule Server associated with the selected domain (the "DNS A" field) and Capsule Server associated with the selected subnet (the "DNS PTR" field). A single host can therefore have several DNS entries.

    **Domain**
    :   Specifies the domain associated with the network interface. To create and manage domains, navigate to **Infrastructure** > **Domains**.

    **Subnet**
    :   Specifies the subnet associated with the network interface. To create and manage subnets, navigate to **Infrastructure** > **Subnets**.

    **Managed** interface
    :   If the interface is managed, configuration is pulled from the associated Capsule Server during provisioning, and DNS and DHCP entries are created. If you use provisioning with installer automation, a configuration file is automatically created for the interface.

        > **Note**
        >
        > Additional interfaces have the **Managed** flag enabled by default, which means the new interface is configured automatically during provisioning by the DNS and DHCP Capsule Servers associated with the selected subnet. This requires a subnet with correctly configured DNS and DHCP Capsule Servers. If you use a Kickstart method for host provisioning, configuration files are automatically created for managed interfaces in the post-installation phase at `/etc/sysconfig/network-scripts/ifcfg-interface_id`.

    **Primary** interface
    :   The DNS name from the primary interface is used as the host portion of the FQDN.

    **Provision**
    :   Network boot uses the provisioning interface. For image-based provisioning, the script to complete the provisioning is executed through the provisioning interface.

Virtual interface settings
:   **Tag**
    :   You can set a VLAN tag to trunk a network segment from the physical network through to the virtual interface.

        - If you do not specify a tag, managed interfaces inherit the VLAN tag of the associated subnet.
        - User-specified entries from this field are not applied to alias interfaces.

Bonded interface settings
:   **Mode**
    :   The bonding mode defines a policy for fault tolerance and load balancing. See [Section 10.6, “Bonding modes available in Satellite”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#bonding-modes-available_managing-hosts "10.6. Bonding modes available in Satellite") for a brief description of each bonding mode.

For more information on configuration options for bonded interfaces, see [Configuring network bonding](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html-single/configuring_and_managing_networking/index#configuring-network-bonding_configuring-and-managing-networking) in *Red Hat Enterprise Linux 8 Configuring and Managing Networking*.
