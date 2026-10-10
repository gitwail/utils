---
title: "Installing and configuring the load balancer"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#installing-and-configuring-the-load-balancer"
---
# Chapter 7. Installing and configuring the load balancer

Red Hat provides general guidance for configuring an HAProxy load balancer using Red Hat Enterprise Linux 9. However, you can install any suitable load balancing software solution that supports TCP forwarding.

## 7.1. Installing the load balancer

The following example provides general guidance for configuring an HAProxy load balancer using Red Hat Enterprise Linux 9. However, you can install any suitable load balancing software solution that supports TCP forwarding.

**Procedure**

1. Install HAProxy:

   ```
   # dnf install haproxy
   ```
2. Install the following package that includes the `semanage` tool:

   ```
   # dnf install policycoreutils-python-utils
   ```
3. Configure SELinux to allow HAProxy to bind any port:

   ```
   # semanage boolean --modify --on haproxy_connect_any
   ```
4. Configure the load balancer to balance the network load for the ports as described in [Section 7.2, “Ports configuration for the load balancer”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#ports-configuration-for-the-load-balancer "7.2. Ports configuration for the load balancer").
5. Configure the load balancer to disable SSL offloading and allow client-side SSL certificates to pass through to back end servers. This is required because communication from clients to Capsule Servers depends on client-side SSL certificates.
6. Start and enable the HAProxy service:

   ```
   # systemctl enable --now haproxy
   ```

## 7.2. Ports configuration for the load balancer

You must ensure proper network configuration of the load balancer to enable it to balance the network load for the ports.

For example, to configure ports for HAProxy, edit the `/etc/haproxy/haproxy.cfg` file to correspond with the table.

Table 7.1. Ports configuration for the load balancer

| Service | Port | Mode | Balance Mode | Destination |
| --- | --- | --- | --- | --- |
| HTTP | 80 | TCP | roundrobin | port 80 on all Capsule Servers |
| HTTPS and RHSM | 443 | TCP | source | port 443 on all Capsule Servers |
| Anaconda for template retrieval | 8000 | TCP | roundrobin | port 8000 on all Capsule Servers |
| Puppet (*Optional*) | 8140 | TCP | roundrobin | port 8140 on all Capsule Servers |
| PuppetCA (*Optional*) | 8141 | TCP | roundrobin | port 8140 only on the system where you configure Capsule Server to sign Puppet certificates |
| Capsule HTTPS for Host Registration and optionally OpenSCAP | 9090 | TCP | roundrobin | port 9090 on all Capsule Servers |

**Additional resources**

- [Configuration example for haproxy.cfg for HAProxy load balancer with Satellite 6 in the *Red Hat Knowledgebase*](https://access.redhat.com/solutions/4062981)
