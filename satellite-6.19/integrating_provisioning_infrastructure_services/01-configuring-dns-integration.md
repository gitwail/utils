---
title: "Configuring DNS integration"
product: "Red Hat Satellite"
version: "6.19"
guide: "integrating_provisioning_infrastructure_services"
guide_title: "Integrating provisioning infrastructure services"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#configuring-dns-integration"
---
# Chapter 1. Configuring DNS integration

You can integrate DNS with Satellite to automate the creation and management of DNS records when provisioning, modifying, and decommissioning hosts. This helps to ensure a consistent and error-free network configuration.

## 1.1. DNS service providers

You can use DNS providers to integrate Satellite with your existing DNS infrastructure or deploy a new one.

Capsule supports the following DNS providers:

`dns_nsupdate`
:   Dynamic DNS updates on an RFC 2136-compatible DNS server by using the `nsupdate` utility.

`dns_nsupdate_gss`
:   Dynamic DNS updates on an RFC 2136-compatible DNS server by using the `nsupdate` utility with Generic Security Service algorithm for Transaction Signature (GSS-TSIG) authentication.

`dns_infoblox`
:   Dynamic DNS updates on an Infoblox DNS server.

**Additional resources**

- [RFC 2136 - Dynamic Updates in the Domain Name System](https://datatracker.ietf.org/doc/html/rfc2136)
- [Section 1.2, “Enabling the installer-managed DNS service”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#enabling-the-installer-managed-dns-service "1.2. Enabling the installer-managed DNS service")
- [Section 1.3, “Integrating a local self-managed DNS service”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-a-local-self-managed-dns-service "1.3. Integrating a local self-managed DNS service")
- [Section 1.4, “Integrating a generic RFC 2136-compatible remote DNS server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-a-generic-rfc-2136-compatible-remote-dns-server "1.4. Integrating a generic RFC 2136-compatible remote DNS server")
- [Section 1.5, “Integrating Identity Management DNS with TSIG authentication”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-idm-dns-with-tsig-authentication "1.5. Integrating Identity Management DNS with TSIG authentication")
- [Section 1.6, “Integrating Identity Management DNS with GSS-TSIG authentication”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-idm-dns-update-with-gss-tsig-authentication "1.6. Integrating Identity Management DNS with GSS-TSIG authentication")
- [Section 1.7, “Integrating Infoblox DNS”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-infoblox-dns "1.7. Integrating Infoblox DNS")

## 1.2. Enabling the installer-managed DNS service

If you do not have a DNS server available in your network, you can use the installer-managed DNS service. This feature enables you to provide a DNS service with low maintenance overhead.

**Procedure**

1. Configure Satellite or Capsule as DNS server:

   ```
   # satellite-installer \
   --foreman-proxy-dns true \
   --foreman-proxy-dns-provider nsupdate \
   --foreman-proxy-dns-managed true \
   --reset-foreman-proxy-dns-server
   ```
2. For each affected Capsule, update the configuration of that Capsule in the Satellite web UI. For more information, see [Section 1.8, “Associating the DNS service with a domain and subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-dns-service-with-a-domain-and-subnet "1.8. Associating the DNS service with a domain and subnet").

## 1.3. Integrating a local self-managed DNS service

To bypass the limitations of the installer-managed DNS service, you can convert it to a self-managed DNS server that offers full configurability and supports multiple forward DNS zones.

**Prerequisites**

- You installed and configured a DNS service on the Satellite Server or Capsule Server host.
- The DNS service supports [RFC 2136](https://datatracker.ietf.org/doc/html/rfc2136)-compatible updates

**Procedure**

1. Set the local, self-managed DNS service on your Satellite Server or Capsule Server:

   ```
   # satellite-installer \
   --foreman-proxy-dns true \
   --foreman-proxy-dns-provider nsupdate \
   --foreman-proxy-dns-managed false \
   --foreman-proxy-dns-server "127.0.0.1"
   ```
2. For each affected Capsule, update the configuration of that Capsule in the Satellite web UI. For more information, see [Section 1.8, “Associating the DNS service with a domain and subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-dns-service-with-a-domain-and-subnet "1.8. Associating the DNS service with a domain and subnet").

## 1.4. Integrating a generic RFC 2136-compatible remote DNS server

If you have a DNS service in your network and it supports RFC 2136-compatible dynamic updates, you can integrate this service into your Satellite Server. The integration enables you to continue using your existing DNS server, and Satellite manages DNS records for hosts during their life cycle.

With this type of integration, Satellite uses a transaction signature (TSIG) key to authenticate to the DNS server and the `nsupdate` utility to manage DNS records.

**Prerequisites**

- The remote DNS service is configured and can be queried.
- The remote DNS service supports RFC 2136-compatible dynamic updates
- The Remote Name Daemon Control (RNDC) key file to connect to the remote DNS server is placed in `/etc/foreman-proxy/rndc.key` on your Satellite Server or Capsule Server.

**Procedure**

1. Update the permissions on `/etc/foreman-proxy/rndc.key` to enable members of the `foreman-proxy` group to read this file:

   ```
   # chown -v root:foreman-proxy /etc/foreman-proxy/rndc.key
   # chmod -v 640 /etc/foreman-proxy/rndc.key
   ```
2. Restore the SELinux context on `/etc/foreman-proxy/rndc.key`:

   ```
   # restorecon -v /etc/foreman-proxy/rndc.key
   ```
3. Optional: Verify if you can use the key file to manually manage DNS entries:

   1. Create a test DNS entry. For example, host `test.example.com` with an `A` record of `192.168.25.20` on the DNS server at `192.168.25.1`.

      ```
      # echo -e "server 192.168.25.1\n \
      update add test.example.com 3600 IN A 192.168.25.20\n \
      send\n" | nsupdate -k /etc/foreman-proxy/rndc.key
      ```
   2. Verify that you can query the new DNS entry:

      ```
      # host test.example.com 192.168.25.1
      ```

      Example output:

      ```
      Using domain server:
      Name: 192.168.25.1
      Address: 192.168.25.1#53
      Aliases:

      test.example.com has address 192.168.25.20
      ```
   3. If resolved successfully, remove the test DNS entry:

      ```
      # echo -e "server 192.168.25.1\n \
      update delete test.example.com 3600 IN A 192.168.25.20\n \
      send\n" | nsupdate -k /etc/foreman-proxy/rndc.key
      ```
   4. Confirm that the DNS entry was removed:

      ```
      # host test.example.com 192.168.25.1
      ```

      If the command returns `Host test.example.com not found: 3(NXDOMAIN)`, the record was successfully deleted.
4. Configure Satellite Server or Capsule Server to use the DNS server:

   ```
   # satellite-installer \
   --foreman-proxy-dns true \
   --foreman-proxy-dns-provider nsupdate \
   --foreman-proxy-dns-managed false \
   --foreman-proxy-dns-server "dns_server_ip_address" \
   --foreman-proxy-keyfile /etc/foreman-proxy/rndc.key
   ```
5. For the affected Capsule, update the configuration of that Capsule in the Satellite web UI. For more information, see [Section 1.8, “Associating the DNS service with a domain and subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-dns-service-with-a-domain-and-subnet "1.8. Associating the DNS service with a domain and subnet").

## 1.5. Integrating Identity Management DNS with TSIG authentication

If you use Identity Management to centrally manage hosts in your domain, you can integrate the Identity Management DNS service into Satellite Server. The integration enables you to continue using your existing Identity Management DNS service, and Satellite manages DNS records for hosts during their life cycle.

If Satellite Server or Capsule Server is not a member of a Identity Management domain, use a transaction signature (TSIG) key to authenticate to the DNS server. This method provides a lower security and an increased key management effort compared to dynamic updates with generic security service transaction signature (GSS-TSIG) authentication. For more information, see [Section 1.6, “Integrating Identity Management DNS with GSS-TSIG authentication”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-idm-dns-update-with-gss-tsig-authentication "1.6. Integrating Identity Management DNS with GSS-TSIG authentication").

**Prerequisites**

- The Identity Management server is deployed and functional.
- The firewall on the Identity Management server allows access to the required ports. See [Port requirements for Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/installing_identity_management/preparing-the-system-for-ipa-server-installation_installing-identity-management#port-requirements-for-idm_preparing-the-system-for-ipa-server-installation) in the *Red Hat Enterprise Linux 9 Installing Identity Management guide*.
- You have `root` access on the Identity Management server.

**Procedure**

1. Perform the following steps on the Identity Management Server:

   1. Insert the following settings at the top of the `/etc/named.conf` file:

      ```
      include "/etc/rndc.key";
      controls {
          inet Identity Management_server_ip_address port 953 allow { Satellite_ip_address; } keys { "rndc-key"; };
      };
      ```
   2. Reload the `named` service:

      ```
      # systemctl reload named
      ```
2. In the Identity Management web UI:

   1. Navigate to **Network Services** > **DNS** > **DNS Zones**
   2. Click the name of the zone.
   3. Open the **Settings** tab.
   4. Enter in the **BIND update policy** field:

      ```
      grant "rndc-key" zonesub ANY;
      ```
   5. Set **Dynamic update** to **True**.
   6. Click **Update** to save the changes.
3. Configure dynamic DNS updates in Satellite Server or Capsule Server. For more information, see [Section 1.4, “Integrating a generic RFC 2136-compatible remote DNS server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#integrating-a-generic-rfc-2136-compatible-remote-dns-server "1.4. Integrating a generic RFC 2136-compatible remote DNS server").

## 1.6. Integrating Identity Management DNS with GSS-TSIG authentication

If you use Identity Management to centrally manage hosts in your domain, you can integrate the Identity Management DNS service into Satellite Server. The integration enables you to continue using your existing Identity Management DNS service, and Satellite manages DNS records for hosts during their life cycle.

If Satellite Server or Capsule Server is a member of a Identity Management domain, use generic security service transaction signature (GSS-TSIG) authentication. This method provides an increased security and a low key management effort compared to TSIG authentication.

### 1.6.1. Configuring Identity Management to use with Satellite Server

Before you can integrate an existing Identity Management DNS server, you must prepare the Identity Management environment. The preparation work enables Satellite Server to use generic security service transaction signature (GSS-TSIG) authentication to update DNS entries.

**Prerequisites**

- The Identity Management domain is deployed and functional.
- Identity Management is configured with its integrated DNS service.
- The firewall on the Identity Management servers allow access to the required ports. For more information, see [Port requirements for IdM](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux//9/html/installing_identity_management/preparing-the-system-for-ipa-server-installation_installing-identity-management#port-requirements-for-idm_preparing-the-system-for-ipa-server-installation) in *Red Hat Enterprise Linux 9 Installing Identity Management*.

**Procedure**

1. On a host that is a member of the Identity Management domain, obtain a Kerberos ticket for the `admin` user:

   ```
   # kinit admin
   ```
2. Create a new Kerberos principal Satellite Server to be used for authentication on the Identity Management server:

   ```
   # ipa service-add capsule/satellite.example.com
   ```
3. Optional: Add a forward DNS zone:

   ```
   # ipa dnszone-add example.com
   ```
4. Display the BIND update policy of the forward zone:

   ```
   # ipa dnszone-show example.com --all | \
   grep "BIND update policy"
   ```

   Example output:

   ```
   BIND update policy: grant EXAMPLE.COM krb5-self * A; grant EXAMPLE.COM krb5-self * AAAA; grant EXAMPLE.COM krb5-self * SSHFP;
   ```

   Note the value of the setting.
5. Update the forward zone settings:

   ```
   # ipa dnszone-mod example.com \
   --dynamic-update=TRUE \
   --allow-sync-ptr=TRUE \
   --update-policy="<existing_policy> grant smartproxy\047foreman.example.com@EXAMPLE.COM wildcard * ANY;"
   ```

   This command modifies the zone settings as follows:

   - Dynamic zone updates are enabled.
   - Identity Management updates the corresponding PTR record in the reverse DNS zone if an A or AAAA record is updated in the forward zone.
   - The Kerberos principal created in an earlier step is authorized to modify any type of any data record. Note that you must append this setting to the existing value.
6. Optional: Add a reverse DNS zone:

   ```
   # ipa dnszone-add 0.168.192.in-addr.arpa
   ```
7. Display the BIND update policy of the reverse zone:

   ```
   # ipa dnszone-show 0.168.192.in-addr.arpa --all | \
   grep "BIND update policy"
   ```

   Example output:

   ```
   BIND update policy: grant EXAMPLE.COM krb5-subdomain 0.168.192.in-addr.arpa. PTR;
   ```

   Note the value of the setting.
8. Update the reverse zone settings:

   ```
   # ipa dnszone-mod 0.168.192.in-addr.arpa \
   --dynamic-update=TRUE \
   --update-policy="<existing_policy> grant smartproxy\047foreman.example.com@EXAMPLE.COM wildcard * ANY;"
   ```

   Note that you must append the update policy to the existing value.

### 1.6.2. Configuring Capsules for use with Identity Management

After you have prepared the Identity Management DNS server as described in [Section 1.6.1, “Configuring Identity Management to use with Satellite Server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#configuring-freeipa-to-use-with-satellite-server "1.6.1. Configuring Identity Management to use with Satellite Server"), integrate the DNS server into your Satellite Server or Capsule Server.

**Prerequisites**

- You set the DNS search domain of the host to the Identity Management DNS domain.
- You know the Kerberos principal the host should use to authenticate to the Identity Management DNS server, for example, `capsule/satellite.example.com`.

**Procedure**

1. If your Satellite Server or Capsule Server is not yet a member of the Identity Management domain:

   1. Install the `ipa-client` package:

      ```
      # satellite-maintain packages install ipa-client
      ```
   2. Install the Identity Management client:

      ```
      # ipa-client-install
      ```

      Follow the on-screen prompts.
2. Obtain a Kerberos ticket for the `admin` user:

   ```
   # kinit admin
   ```
3. Remove the `/etc/foreman-proxy/dns.keytab` file:

   ```
   # rm --force /etc/foreman-proxy/dns.keytab
   ```
4. Obtain a Kerberos keytab file for your Capsule and store it in the `/etc/foreman-proxy/dns.keytab` file:

   ```
   # ipa-getkeytab -p capsule/satellite.example.com@EXAMPLE.COM \
   -k /etc/foreman-proxy/dns.keytab
   ```

   > **Important**
   >
   > When adding a keytab to a standby system with the same host name as the original system in service, pass the `-r` option to the `ipa-getkeytab` command to prevent generating new credentials and rendering the credentials on the original system invalid.
5. Set the owner and group of `/etc/foreman-proxy/dns.keytab` to `foreman-proxy`:

   ```
   # chown foreman-proxy:foreman-proxy /etc/foreman-proxy/dns.keytab
   ```
6. Verify that the `/etc/foreman-proxy/dns.keytab` file is valid:

   1. Use the file to obtain a Kerberos ticket:

      ```
      # kinit -kt /etc/foreman-proxy/dns.keytab \
      capsule/satellite.example.com@EXAMPLE.COM
      ```
   2. Display the Kerberos ticket:

      ```
      # klist
      ```

      Example output:

      ```
      Ticket cache: KCM:0:50473
      Default principal: smartproxy/satellite.example.com@EXAMPLE.COM

      Valid starting       Expires              Service principal
      05/20/2025 12:12:35  05/21/2025 11:54:31  krbtgt/EXAMPLE.COM@EXAMPLE.COM
      ```
7. Configure Satellite Server or Capsule Server to connect to the Identity Management DNS service:

   ```
   # satellite-installer \
   --foreman-proxy-dns true \
   --foreman-proxy-dns-provider nsupdate_gss \
   --foreman-proxy-dns-managed false \
   --foreman-proxy-dns-server "idm-server.example.com" \
   --foreman-proxy-dns-tsig-keytab /etc/foreman-proxy/dns.keytab \
   --foreman-proxy-dns-tsig-principal "capsule/satellite.example.com@EXAMPLE.COM"
   ```
8. For each affected Capsule, update the configuration of that Capsule in the Satellite web UI. For more information, see [Section 1.8, “Associating the DNS service with a domain and subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-dns-service-with-a-domain-and-subnet "1.8. Associating the DNS service with a domain and subnet").

## 1.7. Integrating Infoblox DNS

If you have an Infoblox appliance in your network, you can integrate this service into Satellite Server and Capsule Server by using the Infoblox Web API (WAPI) With the integration, you can use your existing DNS server, and Satellite manages DNS records for hosts during their life cycle.

> **Note**
>
> Integrating Infoblox DNS has the following limitations:
>
> - You can manage DNS entries only in a single view, and you cannot edit the view after you create it.
> - Satellite Server uses the standard HTTPS web API to communicate with Infoblox. By default, it communicates only with a single node. If you require high availability, configure this feature in Infoblox.
> - You cannot integrate the Satellite IP address management (IPAM) feature into Infoblox.

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
4. Configure Satellite Server or Capsule Server to connect to the Infoblox DNS service:

   ```
   # satellite-installer \
   --foreman-proxy-dns true \
   --foreman-proxy-dns-provider infoblox \
   --enable-foreman-proxy-plugin-dns-infoblox \
   --foreman-proxy-plugin-dns-infoblox-dns-server infoblox.example.com \
   --foreman-proxy-plugin-dns-infoblox-username admin \
   --foreman-proxy-plugin-dns-infoblox-password password \
   --foreman-proxy-plugin-dns-infoblox-dns-view view_name
   ```

   Omit the `--foreman-proxy-plugin-dns-infoblox-dns-view` option if you use the `default` view in Infoblox DNS.
5. For each affected Capsule, update the configuration of that Capsule in the Satellite web UI. For more information, see [Section 1.8, “Associating the DNS service with a domain and subnet”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/integrating_provisioning_infrastructure_services/index#associating-the-dns-service-with-a-domain-and-subnet "1.8. Associating the DNS service with a domain and subnet").

## 1.8. Associating the DNS service with a domain and subnet

After you configured or changed the DNS provider, you must update the configuration of each affected Capsule in the Satellite web UI.

**Prerequisites**

- You configured a DNS provider.

**Procedure**

1. Configure the domain:

   1. In the Satellite web UI, navigate to **Infrastructure** > **Domains**.
   2. Select the domain name.
   3. On the **Domain** tab, ensure **DNS Capsule** is set to the Capsule where the subnet is connected.
2. Configure the subnet:

   1. Navigate to **Infrastructure** > **Subnets**.
   2. Select the subnet name.
   3. On the **Domains** tab, select the domains that are valid on the subnet.
   4. In the **Capsules** tab, ensure **Reverse DNS Capsule** is set to the Capsule where the subnet is connected.
   5. Click **Submit**.

## 1.9. Disabling DNS for integration

If you want to manually manage a DNS service and not integrate it into Satellite Server, you must prevent Satellite from maintaining this service on the operating system and disable orchestration to avoid errors.

> **Note**
>
> Disabling DNS in Satellite does not remove the related backend service on the operating system.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Subnets**.
2. For each subnet that is associated with the DNS Capsule:

   1. Select the subnet.
   2. On the **Capsules** tab, clear the **Reverse DNS Capsule** field.
   3. Click **Submit**.
3. Navigate to **Infrastructure** > **Domains**.
4. For each domain that is associated with the DNS Capsule:

   1. Select the domain.
   2. Clear the **DNS Capsule** field.
   3. Click **Submit**.
5. On Satellite Server, enter:

   ```
   # satellite-installer --foreman-proxy-dns false
   ```

   > **Note**
   >
   > Satellite does not perform orchestration when a Capsule is not set for a given subnet and domain. When you disable Capsule associations, orchestration commands for existing hosts can fail if the expected records and configuration files are not present.
