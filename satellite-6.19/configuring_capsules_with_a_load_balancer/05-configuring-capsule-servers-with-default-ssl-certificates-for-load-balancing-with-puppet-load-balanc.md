---
title: "Configuring Capsule Servers with default SSL certificates for load balancing (with Puppet)"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#configuring-capsule-servers-with-default-ssl-certificates-for-load-balancing-with-puppet_load-balancing"
---
# Chapter 5. Configuring Capsule Servers with default SSL certificates for load balancing (with Puppet)

If you use Puppet in your Satellite setup, you can configure one or more Capsule Servers that use default SSL certificates for load balancing.

To do this, you configure Puppet certificate signing on one of your Capsule Servers. Then, you configure each remaining Puppet Capsule used for load balancing to use the certificates. The first Capsule Server will generate and sign Puppet certificates for the remaining Capsules configured for load balancing.

## 5.1. Configuring Capsule Server with default SSL certificates to generate and sign Puppet certificates

On the Capsule Server that will generate Puppet certificates for all other load-balancing Capsule Servers, configure Puppet certificate generation and signing.

**Prerequisites**

- Prepare a new Capsule Server to use for load balancing. See [Chapter 2, *Preparing Capsule Servers for load balancing*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#preparing-capsule-servers-for-load-balancing_load-balancing "Chapter 2. Preparing Capsule Servers for load balancing").
- Review [Section 1.2, “Services and features supported in a load-balanced setup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#services-and-features-supported-in-a-load-balanced-setup_load-balancing "1.2. Services and features supported in a load-balanced setup").

**Procedure**

1. On Satellite Server, generate Katello certificates for the system where you configure Capsule Server to generate and sign Puppet certificates:

   ```
   # capsule-certs-generate \
   --certs-tar "/root/capsule-ca.example.com-certs.tar" \
   --foreman-proxy-cname loadbalancer.example.com \
   --foreman-proxy-fqdn capsule-ca.example.com
   ```

   Retain a copy of the example `satellite-installer` command that is output by the `capsule-certs-generate` command for installing Capsule Server certificate.
2. Copy the certificate archive file from Satellite Server to Capsule Server:

   ```
   # scp /root/capsule-ca.example.com-certs.tar root@capsule-ca.example.com:capsule-ca.example.com-certs.tar
   ```
3. Append the following options to the `satellite-installer` command that you obtain from the output of the `capsule-certs-generate` command:

   ```
   --certs-cname "loadbalancer.example.com" \
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
   --certs-tar-file "capsule-ca.example.com-certs.tar" \
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
5. On Capsule Server that is the Puppet Certificate Authority, stop the OpenVox server:

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

## 5.2. Configuring remaining Capsule Servers with default SSL certificates for load balancing

On each load-balancing Capsule Server, excluding the Capsule Server configured to sign Puppet certificates, configure the system to use Puppet certificates.

**Procedure**

1. On Satellite Server, generate Katello certificates for Capsule Server:

   ```
   # capsule-certs-generate \
   --certs-tar "/root/capsule.example.com-certs.tar" \
   --foreman-proxy-cname loadbalancer.example.com \
   --foreman-proxy-fqdn capsule.example.com
   ```

   Retain a copy of the example `satellite-installer` command that is output by the `capsule-certs-generate` command for installing Capsule Server certificate.
2. Copy the certificate archive file from Satellite Server to Capsule Server:

   ```
   # scp /root/capsule.example.com-certs.tar root@capsule.example.com:/root/capsule.example.com-certs.tar
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

## 5.3. Managing Puppet limitations with load balancing in Satellite

If you use Puppet, Puppet certificate signing is assigned to the first Capsule that you configure. If the first Capsule is down, hosts cannot obtain Puppet content.

Puppet Certificate Authority (CA) management does not support certificate signing in a load-balanced setup. Puppet CA stores certificate information, such as the serial number counter and CRL, on the file system. Multiple writer processes that attempt to use the same data can corrupt it.

To manage this Puppet limitation, complete the following steps:

1. Configure Puppet certificate signing on one Capsule Server, typically the first system where you configure Capsule Server for load balancing.
2. Configure the clients to send CA requests to port 8141 on a load balancer.
3. Configure a load balancer to redirect CA requests from port 8141 to port 8140 on the system where you configure Capsule Server to sign Puppet certificates.

To troubleshoot issues, reproduce the issue on each Capsule, bypassing the load balancer. This solution does not use Pacemaker or other similar HA tools to maintain one state across all Capsules.
