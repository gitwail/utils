---
title: "Provisioning requirements in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "13"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#provisioning-requirements-in-satellite"
---
# Chapter 13. Provisioning requirements in Satellite

An important feature of Red Hat Satellite is unattended provisioning of hosts. To achieve this, Red Hat Satellite uses DNS and DHCP infrastructures, PXE booting, TFTP, and Kickstart. Use this chapter to understand the working principle of these concepts.

## 13.1. PXE booting in Satellite

Preboot execution environment (PXE) provides the ability to boot a system over a network. Instead of using local hard drives or a CD-ROM, PXE uses DHCP to provide host with standard information about the network, to discover a TFTP server, and to download a boot image.

PXE sequence
:   1. The host boots the PXE image if no other bootable image is found.
    2. A NIC of the host sends a broadcast request to the DHCP server.
    3. The DHCP server receives the request and sends standard information about the network: IP address, subnet mask, gateway, DNS, the location of a TFTP server, and a boot image.
    4. The host obtains the boot loader `image/pxelinux.0` and the configuration file `pxelinux.cfg/00:MA:CA:AD:D` from the TFTP server.
    5. The host configuration specifies the location of a kernel image, `initrd` and Kickstart.
    6. The host downloads the files and installs the image.

PXE booting requirements
:   - Network requirements:

      - Optional: If the host and the DHCP server are separated by a router, configure the DHCP relay agent and point to the DHCP server.
    - Client requirements:

      - Ensure that all the network-based firewalls are configured to allow clients on the subnet to access the Capsule.
      - Ensure that your client has access to the DHCP and TFTP servers.
    - Satellite requirements:

      - Ensure that both Satellite Server and Capsule have DNS configured and are able to resolve provisioned host names.
      - Ensure that the UDP ports 67 and 68 are accessible by the client to enable the client to receive a DHCP offer with the boot options.
      - Ensure that the UDP port 69 is accessible by the client so that the client can access the TFTP server on the Capsule.
      - Ensure that the TCP port 80 is accessible by the client to allow the client to download files and Kickstart templates from the Capsule.
      - Ensure that the host provisioning interface subnet has a DHCP Capsule set.
      - Ensure that the host provisioning interface subnet has a TFTP Capsule set.
      - Ensure that the host provisioning interface subnet has a Templates Capsule set.
      - Ensure that DHCP with the correct subnet is enabled using the Satellite installer.
      - Enable TFTP using the Satellite installer.

**Additional resources**

- [Network boot provisioning workflow in *Provisioning hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#network-boot-provisioning-workflow)
- [How to set-up/configure a PXE Server in the Red Hat Knowledgebase](https://access.redhat.com/solutions/163253)
- [Chapter 9, *Networking considerations in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#networking-considerations-in-satellite "Chapter 9. Networking considerations in Satellite")

## 13.2. HTTP booting in Satellite

You can use HTTP booting to boot networked systems over HTTP. Requirements differ depending on whether DHCP is managed or unmanaged.

HTTP booting requirements with managed DHCP
:   - Client requirements:

      - All the network-based firewalls are configured to allow clients on the subnet to access the Capsule. For more information, see [Chapter 9, *Networking considerations in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#networking-considerations-in-satellite "Chapter 9. Networking considerations in Satellite").
      - Your client has access to the DHCP and DNS servers.
      - Your client has access to the HTTP UEFI Boot Capsule.
    - Network requirements:

      - Optional: If the host and the DHCP server are separated by a router, configure the DHCP relay agent and point to the DHCP server.
    - Satellite requirements:

      > **Note**
      >
      > Although TFTP protocol is not used for HTTP UEFI Booting, Satellite uses TFTP Capsule API to deploy boot loader configuration.

      - Both Satellite Server and Capsule have DNS configured and are able to resolve provisioned host names.
      - The UDP ports 67 and 68 are accessible by the client so that the client can send and receive a DHCP request and offer.
      - Ensure that the TCP port 8000 is open for the client to download the boot loader and Kickstart templates from the Capsule.
      - The TCP port 9090 is open for the client to download the boot loader from the Capsule using the HTTPS protocol.
      - The subnet that functions as the host’s provisioning interface has a DHCP Capsule, an HTTP Boot Capsule, a TFTP Capsule, and a Templates Capsule

HTTP booting requirements with unmanaged DHCP
:   - Client requirements:

      - HTTP UEFI Boot URL must be set to one of:

        - `http://capsule.example.com:8000`
        - `https://capsule.example.com:9090`
      - Ensure that your client has access to the DHCP and DNS servers.
      - Ensure that your client has access to the HTTP UEFI Boot Capsule.
      - Ensure that all the network-based firewalls are configured to allow clients on the subnet to access the Capsule. For more information, see [Chapter 9, *Networking considerations in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#networking-considerations-in-satellite "Chapter 9. Networking considerations in Satellite").
    - Network requirements:

      - An unmanaged DHCP server available for clients.
      - An unmanaged DNS server available for clients. In case DNS is not available, use IP address to configure clients.
    - Satellite requirements:

      > **Note**
      >
      > Although TFTP protocol is not used for HTTP UEFI Booting, Satellite uses TFTP Capsule API to deploy boot loader configuration.

      - Ensure that both Satellite Server and Capsule have DNS configured and are able to resolve provisioned host names.
      - Ensure that the UDP ports 67 and 68 are accessible by the client so that the client can send and receive a DHCP request and offer.
      - Ensure that the TCP port 8000 is open for the client to download boot loader and Kickstart templates from the Capsule.
      - Ensure that the TCP port 9090 is open for the client to download the boot loader from the Capsule through HTTPS.
      - Ensure that the host provisioning interface subnet has an HTTP Boot Capsule set.
      - Ensure that the host provisioning interface subnet has a TFTP Capsule set.
      - Ensure that the host provisioning interface subnet has a Templates Capsule set.
