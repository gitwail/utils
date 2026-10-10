---
title: "Using custom SSL certificate for hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#using-custom-ssl-certificate-for-hosts_managing-hosts"
---
# Chapter 8. Using custom SSL certificate for hosts

You can use custom SSL certificate on your hosts to enable encrypted communications between Satellite Server, Capsule Server, and hosts. Before deploying it to your hosts, ensure that you have configured the custom SSL certificate to your Satellite Server.

## 8.1. Deploying a custom SSL certificate to hosts

After you configure Satellite to use a custom SSL certificate, you must deploy the certificate to hosts registered to Satellite.

> **Important**
>
> The `katello-ca-consumer` RPM package and `katello-rhsm-consumer` script is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Use refreshing the self-signed CA certificate on hosts instead.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

**Procedure**

- Update the SSL certificate on each host:

  ```
  # dnf install http://satellite.example.com/pub/katello-ca-consumer-latest.noarch.rpm
  ```

**Additional resources**

- [Refreshing the self-signed CA certificate on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#refreshing-the-self-signed-ca-certificate-on-hosts)

## 8.2. Resetting custom SSL certificate to default self-signed certificate on hosts

To reset the custom SSL certificate on your hosts to default self-signed certificate, you must re-register your hosts through **Global Registration**.

**Additional resources**

- [Section 6.2, “Registering hosts by using global registration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration "6.2. Registering hosts by using global registration")
- [Resetting custom SSL certificate to default self-signed certificate on Satellite Server in *Installing Satellite Server in a connected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#resetting-custom-ssl-certificate-to-default-self-signed-certificate-on-satellite_satellite)
- [Resetting custom SSL certificate to default self-signed certificate on Capsule Server in *Installing Capsule Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#resetting-custom-ssl-certificate-to-default-self-signed-certificate-on-capsule_capsule)
