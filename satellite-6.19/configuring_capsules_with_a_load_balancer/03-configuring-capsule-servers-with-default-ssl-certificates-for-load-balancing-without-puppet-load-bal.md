---
title: "Configuring Capsule Servers with default SSL certificates for load balancing"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#configuring-capsule-servers-with-default-ssl-certificates-for-load-balancing-without-puppet_load-balancing"
---
# Chapter 3. Configuring Capsule Servers with default SSL certificates for load balancing

You can configure one or more Capsule Servers that use default SSL certificates for load balancing.

## 3.1. Configuring Capsule Server with default SSL certificates for load balancing without Puppet

On each Capsule Server that you want to configure for load balancing, install Katello certificates.

**Prerequisites**

- Prepare a new Capsule Server to use for load balancing. See [Chapter 2, *Preparing Capsule Servers for load balancing*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#preparing-capsule-servers-for-load-balancing_load-balancing "Chapter 2. Preparing Capsule Servers for load balancing").
- Review [Section 1.2, “Services and features supported in a load-balanced setup”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#services-and-features-supported-in-a-load-balanced-setup_load-balancing "1.2. Services and features supported in a load-balanced setup").

**Procedure**

1. On Satellite Server, generate Katello certificates for Capsule Server:

   ```
   # capsule-certs-generate \
   --certs-tar "/root/capsule.example.com-certs.tar" \
   --foreman-proxy-cname loadbalancer.example.com \
   --foreman-proxy-fqdn capsule.example.com
   ```

   Retain a copy of the example `satellite-installer` command that is output by the `capsule-certs-generate` command for installing Capsule Server certificate.
2. Copy the certificate archive file from Satellite Server to Capsule Server.

   ```
   # scp /root/capsule.example.com-certs.tar root@capsule.example.com:/root/capsule.example.com-certs.tar
   ```
3. Append the following options to the `satellite-installer` command that you obtain from the output of the `capsule-certs-generate` command:

   ```
   --certs-cname "loadbalancer.example.com" \
   --enable-foreman-proxy-plugin-remote-execution-script
   ```
4. On Capsule Server, enter the `satellite-installer` command:

   ```
   # satellite-installer --scenario capsule \
   --certs-cname "loadbalancer.example.com" \
   --certs-tar-file "capsule.example.com-certs.tar" \
   --enable-foreman-proxy-plugin-remote-execution-script \
   --foreman-proxy-foreman-base-url "https://satellite.example.com" \
   --foreman-proxy-oauth-consumer-key "oauth key" \
   --foreman-proxy-oauth-consumer-secret "oauth secret" \
   --foreman-proxy-trusted-hosts "satellite.example.com" \
   --foreman-proxy-trusted-hosts "capsule.example.com"
   ```
