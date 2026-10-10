---
title: "Renewing certificates"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "16"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#renewing-certificates"
---
# Chapter 16. Renewing certificates

You can renew the CA certificate on Satellite Server or the custom SSL certificate on Satellite Server as well as on Capsule Server.

## 16.1. Planning for self-signed CA certificate renewal

If you need to update the Certification Authority (CA) certificate on your Satellite Server, add the new CA certificate and use a temporary dual CA certificate file to retain the HTTPS connections to your Satellite Server during the renewal.

**Procedure**

1. Add the new SSL certificate to the CA certificate file on Satellite Server and keep the old SSL certificate.
2. Renew the certificates on Satellite Server and any Capsule Servers.
3. Deploy the dual CA certificate on hosts.
4. Remove the old certificate from the CA certificates file on Satellite Server, so the CA certificate file contains only the new SSL certificate.
5. Renew the certificates on Satellite Server and any Capsule Servers.
6. Deploy the new CA certificate on hosts.

**Additional resources**

- [Refreshing the self-signed CA certificate on hosts in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#refreshing-the-self-signed-ca-certificate-on-hosts)

## 16.2. Renewing a custom SSL certificate on Satellite Server

You can deploy a renewed custom SSL certificate on Satellite Server to replace an expiring certificate and maintain trusted access to the Satellite web UI and API.

**Prerequisites**

- You have created a new Certificate Signing Request (CSR) and sent it to the Certificate Authority to sign the certificate. Refer to the [Configuring Satellite Server with a custom SSL certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#configuring-satellite-server-with-a-custom-ssl-certificate) guide before creating a new CSR because the Server certificate must have X.509 v3 `Key Usage` and `Extended Key Usage` extensions with required values. In return, you will receive the Satellite Server certificate and CA bundle.

**Procedure**

- Deploy the renewed CA certificates to Satellite Server:

  ```
  # satellite-installer --scenario satellite \
  --certs-server-cert "/root/satellite_cert/satellite_cert.pem" \
  --certs-server-key "/root/satellite_cert/satellite_cert_key.pem" \
  --certs-server-ca-cert "/root/satellite_cert/ca_cert_bundle.pem" \
  --certs-update-server \
  --certs-update-server-ca
  ```

  > **Important**
  >
  > Do not delete the certificate files after you deploy the certificate. They are required when upgrading Satellite Server.

**Verification**

1. Access the Satellite web UI from your local machine. For example, `https://satellite.example.com`.
2. In your browser, view the certificate details to verify the deployed certificate.

**Next steps**

- If you have changed the CA certificate on Satellite Server, refresh the CA certificate on your hosts. For more information, see [Refreshing the self-signed CA certificate on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#refreshing-the-self-signed-ca-certificate-on-hosts) in *Managing hosts*.

## 16.3. Renewing a custom SSL certificate on Capsule Server

You can deploy a renewed custom SSL certificate on each Capsule Server before it expires to maintain secure communication with Satellite Server. Run a unique `satellite-installer` command on each server because the output of `capsule-certs-generate` cannot be reused.

**Prerequisites**

- You have created a new Certificate Signing Request and sent it to the Certificate Authority to sign the certificate. Refer to the [Configuring Satellite Server with a custom SSL certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#configuring-satellite-server-with-a-custom-ssl-certificate) guide before creating a new CSR because the Satellite Server certificate must have X.509 v3 `Key Usage` and `Extended Key Usage` extensions with required values. In return, you will receive the Capsule Server certificate and CA bundle.

**Procedure**

1. On your Satellite Server, generate the certificate archive file for your Capsule Server:

   ```
   # capsule-certs-generate \
   --certs-tar "/root/My_Certificates/capsule.example.com-certs.tar" \
   --certs-update-server \
   --foreman-proxy-fqdn "capsule.example.com" \
   --server-ca-cert "/root/My_Certificates/ca_cert_bundle.pem" \
   --server-cert "/root/My_Certificates/capsule_cert.pem" \
   --server-key "/root/My_Certificates/capsule_cert_key.pem"
   ```
2. On your Satellite Server, copy the certificate archive file to your Capsule Server:

   ```
   # scp /root/My_Certificates/capsule.example.com-certs.tar user@capsule.example.com:
   ```

   You can move the copied file to the applicable path if required.
3. Retain a copy of the `satellite-installer` command that the `capsule-certs-generate` command returns for deploying the certificate to your Capsule Server.
4. Deploy the certificate on your Capsule Server using the `satellite-installer` command returned by the `capsule-certs-generate` command:

   ```
   # satellite-installer --scenario capsule \
   --certs-tar-file "/root/My_Certificates/capsule.example.com-certs.tar" \
   --certs-update-server \
   --foreman-proxy-foreman-base-url "https://satellite.example.com"
   ```

   > **Important**
   >
   > Do not delete the certificate archive file on the Capsule Server after you deploy the certificate. They are required when upgrading Capsule Server.

**Next steps**

- If you have changed the CA certificate on Satellite Server, refresh the CA certificate on your hosts. For more information, see [Refreshing the self-signed CA certificate on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#refreshing-the-self-signed-ca-certificate-on-hosts) in *Managing hosts*.
