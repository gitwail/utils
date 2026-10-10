---
title: "Configuring Capsule Servers with custom SSL certificates for load balancing (with Puppet)"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#configuring-capsule-servers-with-custom-ssl-certificates-for-load-balancing-with-puppet_load-balancing"
---
# Chapter 6. Configuring Capsule Servers with custom SSL certificates for load balancing (with Puppet)

You can configure one or more Capsule Servers that use custom SSL certificates for load balancing.

## 6.1. Creating a custom SSL certificate for Capsule Server

On each Capsule Server you want to configure for load balancing, create a configuration file for the Certificate Signing Request and include the load balancer and Capsule Server as Subject Alternative Names (SAN).

**Procedure**

1. To store all the source certificate files, create a directory that is accessible only to the `root` user:

   ```
   # mkdir /root/capsule_cert
   ```
2. Create a private key with which to sign the certificate signing request (CSR). The private key must be unencrypted:

   ```
   # openssl genrsa -out /root/capsule_cert/capsule_cert_key.pem 4096
   ```

   If you already have a private key, skip this step.
3. Optional: Verify that the key is unencrypted:

   ```
   # openssl pkey -noout -in /root/capsule_cert/capsule_cert_key.pem
   ```

   If the command does not ask for a password, the key is unencrypted. If your private key is password-protected, remove the password.
4. Create the `/root/capsule_cert/openssl.cnf` configuration file for the CSR and include the following content:

   ```
   [ req ]
   req_extensions = v3_req
   distinguished_name = req_distinguished_name
   x509_extensions = usr_cert
   prompt = no

   [ req_distinguished_name ]
   commonName = capsule.example.com

   [ v3_req ]
   basicConstraints = CA:FALSE
   keyUsage = digitalSignature, keyEncipherment
   extendedKeyUsage = serverAuth, clientAuth
   subjectAltName = @alt_names

   [alt_names]
   DNS.1 = loadbalancer.example.com
   DNS.2 = capsule.example.com
   ```

   The options used in the configuration file include the following:

   `commonName`
   :   The certificate common name. It must match the FQDN of Capsule Server. Ensure to change this when running the command on each Capsule Server that you configure for load balancing. You can also set a wildcard value `*`.

   `[alt_names]`
   :   The alternative names for the load balancer and Capsule Server. Include the FQDN of the load balancer as `DNS.1` and the FQDN of Capsule Server as `DNS.2`.

       For more information about the `[ v3_req ]` parameters and their purpose, see [RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile](https://www.rfc-editor.org/rfc/rfc5280).
5. Optional: If you want to add Distinguished Name (DN) details to the CSR, add the following information to the `[ req_distinguished_name ]` section:

   ```
   [req_distinguished_name]
   CN = capsule.example.com
   countryName = My_Country_Name
   stateOrProvinceName = My_State_Or_Province_Name
   localityName = My_Locality_Name
   organizationName = My_Organization_Or_Company_Name
   organizationalUnitName = My_Organizational_Unit_Name
   ```

   The options used in the configuration file include the following:

   `countryName`
   :   The country represented by a two-letter code

   `stateOrProvinceName`
   :   Full name of the state or province

   `localityName`
   :   Full name of the locality (example: New York)

   `organizationalUnitName`
   :   Division responsible for the certificate (example: IT department)
6. Generate the CSR:

   ```
   # openssl req -new \
   -key /root/capsule_cert/capsule_cert_key.pem \
   -config /root/capsule_cert/openssl.cnf \
   -out /root/capsule_cert/capsule_cert_csr.pem
   ```

   The options used in the configuration file include the following:

   `-key`
   :   Path to the private key

   `-config`
   :   Path to the configuration file

   `-out`
   :   Path to the CSR to generate
7. Send the certificate signing request to the certificate authority (CA). The same CA must sign certificates for Satellite Server and Capsule Server.

   When you submit the request, specify the lifespan of the certificate. The method for sending the certificate request varies, so consult the CA for the preferred method. In response to the request, you can expect to receive a CA bundle and a signed certificate, in separate files.
8. Copy the Certificate Authority bundle and Capsule Server certificate file that you receive from the Certificate Authority, and Capsule Server private key to your Satellite Server.

## 6.2. Configuring Capsule Server with custom SSL certificates to generate and sign Puppet certificates

On the Capsule Server that will generate Puppet certificates for all other load-balancing Capsule Servers, configure Puppet certificate generation and signing.

**Prerequisites**

- Prepare a new Capsule Server to use for load balancing. See [Chapter 2, *Preparing Capsule Servers for load balancing*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#preparing-capsule-servers-for-load-balancing_load-balancing "Chapter 2. Preparing Capsule Servers for load balancing").
- Review [Section 1.2, “Services and features supported in a load-balanced setup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#services-and-features-supported-in-a-load-balanced-setup_load-balancing "1.2. Services and features supported in a load-balanced setup").

**Procedure**

1. On Satellite Server, enter the `capsule-certs-generate` command to generate Capsule certificates:

   ```
   # capsule-certs-generate \
   --certs-tar /root/capsule_cert/capsule-ca.tar \
   --foreman-proxy-cname loadbalancer.example.com \
   --foreman-proxy-fqdn capsule-ca.example.com \
   --server-ca-cert /root/capsule_cert/ca_cert_bundle.pem \
   --server-cert /root/capsule_cert/capsule-ca.pem \
   --server-key /root/capsule_cert/capsule-ca.pem
   ```

   Retain a copy of the example `satellite-installer` command from the output for installing Capsule Server certificates.
2. Copy the certificate archive file from Satellite Server to Capsule Server.
3. Append the following options to the `satellite-installer` command that you obtain from the output of the `capsule-certs-generate` command:

   ```
   --enable-foreman-proxy-plugin-remote-execution-script \
   --foreman-proxy-puppetca "true" \
   --puppet-ca-server "capsule-ca.example.com" \
   --puppet-dns-alt-names "loadbalancer.example.com" \
   --puppet-server-ca "true"
   ```
4. On Capsule Server, enter the `satellite-installer` command:

   ```
   # satellite-installer --scenario capsule \
   --certs-cname "loadbalancer.example.com" \
   --certs-tar-file "certs.tgz" \
   --enable-foreman-proxy-plugin-remote-execution-script \
   --enable-puppet \
   --foreman-proxy-foreman-base-url "https://satellite.example.com" \
   --foreman-proxy-oauth-consumer-key "oauth key" \
   --foreman-proxy-oauth-consumer-secret "oauth secret" \
   --foreman-proxy-puppetca "true" \
   --foreman-proxy-trusted-hosts "satellite.example.com" \
   --foreman-proxy-trusted-hosts "capsule-ca.example.com" \
   --puppet-ca-server "capsule-ca.example.com" \
   --puppet-dns-alt-names "loadbalancer.example.com" \
   --puppet-server true \
   --puppet-server-ca "true"
   ```
5. On Capsule Server that is the Puppetserver Certificate Authority, stop the OpenVox server:

   ```
   # systemctl stop puppetserver
   ```
6. Generate Puppet certificates for all other Capsule Servers that you configure for load balancing, except the system where you first configured Puppet certificate signing:

   ```
   # puppetserver ca generate \
   --ca-client \
   --certname capsule.example.com \
   --subject-alt-names loadbalancer.example.com
   ```

   This command creates the following files:

   - `/etc/puppetlabs/puppet/ssl/certs/capsule.example.com.pem`
   - `/etc/puppetlabs/puppet/ssl/private_keys/capsule.example.com.pem`
   - `/etc/puppetlabs/puppet/ssl/public_keys/capsule.example.com.pem`
   - `/etc/puppetlabs/puppetserver/ca/signed/capsule.example.com.pem`
7. Start the OpenVox server:

   ```
   # systemctl start puppetserver
   ```

## 6.3. Configuring remaining Capsule Servers with custom SSL certificates for load balancing

On each load-balancing Capsule Server, excluding the Capsule Server configured to sign Puppet certificates, configure the system to use Puppet certificates.

**Procedure**

1. On Satellite Server, enter the `capsule-certs-generate` command to generate Capsule certificates:

   ```
   # capsule-certs-generate \
   --certs-tar /root/capsule_cert/capsule.tar \
   --foreman-proxy-cname loadbalancer.example.com \
   --foreman-proxy-fqdn capsule.example.com \
   --server-ca-cert /root/capsule_cert/ca_cert_bundle.pem \
   --server-cert /root/capsule_cert/capsule.pem \
   --server-key /root/capsule_cert/capsule.pem
   ```

   Retain a copy of the example `satellite-installer` command from the output for installing Capsule Server certificates.
2. Copy the certificate archive file from Satellite Server to Capsule Server.

   ```
   # scp /root/capsule.example.com-certs.tar root@capsule.example.com:capsule.example.com-certs.tar
   ```
3. On Capsule Server, install the `puppetserver` package:

   ```
   # satellite-maintain packages install puppetserver
   ```
4. On Capsule Server, create directories for puppet certificates:

   ```
   # mkdir -p /etc/puppetlabs/puppet/ssl/certs/ \
   /etc/puppetlabs/puppet/ssl/private_keys/ \
   /etc/puppetlabs/puppet/ssl/public_keys/
   ```
5. On Capsule Server, copy the Puppet certificates for this Capsule Server from the system where you configure Capsule Server to sign Puppet certificates:

   ```
   # scp root@capsule-ca.example.com:/etc/puppetlabs/puppet/ssl/certs/capsule.example.com.pem /etc/puppetlabs/puppet/ssl/certs/capsule.example.com.pem
   # scp root@capsule-ca.example.com:/etc/puppetlabs/puppet/ssl/certs/ca.pem /etc/puppetlabs/puppet/ssl/certs/ca.pem
   # scp root@capsule-ca.example.com:/etc/puppetlabs/puppet/ssl/private_keys/capsule.example.com.pem /etc/puppetlabs/puppet/ssl/private_keys/capsule.example.com.pem
   # scp root@capsule-ca.example.com:/etc/puppetlabs/puppet/ssl/public_keys/capsule.example.com.pem /etc/puppetlabs/puppet/ssl/public_keys/capsule.example.com.pem
   ```
6. On Capsule Server, change the `/etc/puppetlabs/puppet/ssl/` directory ownership to user `puppet` and group `puppet`:

   ```
   # chown -R puppet:puppet /etc/puppetlabs/puppet/ssl/
   ```
7. On Capsule Server, set the SELinux context for the `/etc/puppetlabs/puppet/ssl/` directory:

   ```
   # restorecon -Rv /etc/puppetlabs/puppet/ssl/
   ```
8. Append the following options to the `satellite-installer` command that you obtain from the output of the `capsule-certs-generate` command:

   ```
   --certs-cname "loadbalancer.example.com" \
   --enable-foreman-proxy-plugin-remote-execution-script \
   --foreman-proxy-puppetca "false" \
   --puppet-ca-server "capsule-ca.example.com" \
   --puppet-dns-alt-names "loadbalancer.example.com" \
   --puppet-server-ca "false"
   ```
9. On Capsule Server, enter the `satellite-installer` command:

   ```
   # satellite-installer --scenario capsule \
   --certs-cname "loadbalancer.example.com" \
   --certs-tar-file "capsule.example.com-certs.tar" \
   --enable-foreman-proxy-plugin-remote-execution-script \
   --foreman-proxy-foreman-base-url "https://satellite.example.com" \
   --foreman-proxy-oauth-consumer-key "oauth key" \
   --foreman-proxy-oauth-consumer-secret "oauth secret" \
   --foreman-proxy-puppetca "false" \
   --foreman-proxy-trusted-hosts "satellite.example.com" \
   --foreman-proxy-trusted-hosts "capsule.example.com" \
   --puppet-ca-server "capsule-ca.example.com" \
   --puppet-dns-alt-names "loadbalancer.example.com" \
   --puppet-server-ca "false"
   ```

## 6.4. Managing Puppet limitations with load balancing in Satellite

If you use Puppet, Puppet certificate signing is assigned to the first Capsule that you configure. If the first Capsule is down, hosts cannot obtain Puppet content.

Puppet Certificate Authority (CA) management does not support certificate signing in a load-balanced setup. Puppet CA stores certificate information, such as the serial number counter and CRL, on the file system. Multiple writer processes that attempt to use the same data can corrupt it.

To manage this Puppet limitation, complete the following steps:

1. Configure Puppet certificate signing on one Capsule Server, typically the first system where you configure Capsule Server for load balancing.
2. Configure the clients to send CA requests to port 8141 on a load balancer.
3. Configure a load balancer to redirect CA requests from port 8141 to port 8140 on the system where you configure Capsule Server to sign Puppet certificates.

To troubleshoot issues, reproduce the issue on each Capsule, bypassing the load balancer. This solution does not use Pacemaker or other similar HA tools to maintain one state across all Capsules.
