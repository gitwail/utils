---
title: "Refreshing the self-signed CA certificate on hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#refreshing-the-self-signed-ca-certificate-on-hosts"
---
# Chapter 9. Refreshing the self-signed CA certificate on hosts

When you change the CA certificate on your Satellite Server, you must refresh the CA certificate on your hosts.

Ensure that you use a temporary dual CA certificate file for uninterrupted operation.

If you have already changed the CA certificate on Satellite Server without using the temporary dual CA certificate file, you must refresh the certificate on hosts manually because the scripted variant will not recognize Satellite Server.

> **Important**
>
> You only must redeploy the CA certificate if you use a self-signed CA certificate.

**Additional resources**

- [Planning for self-signed CA certificate renewal in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#planning-for-self-signed-ca-certificate-renewal)

## 9.1. Deploying the CA certificate on a host by using Script REX

You can use remote execution (REX) with the Script provider to deploy the CA certificate.

**Prerequisites**

- The host is registered to Satellite.

- Remote execution is enabled on the host.
- The CA certificate has been changed on Satellite Server. For more information, see [Planning for self-signed CA certificate renewal](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#planning-for-self-signed-ca-certificate-renewal) in *Administering Red Hat Satellite*.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Jobs**.
2. Click **Run Job**.
3. From the **Job category** list, select **Commands**.
4. From the **Job template** list, select **Download and run a script**.
5. Click **Next**.
6. Select hosts on which you want to execute the job.
7. In the **url** field, enter the following URL:

   ```
   https://satellite.example.com/unattended/public/foreman_ca_refresh
   ```

   You can use HTTP when the CA certificate is expired.
8. Optional: Click **Next** and configure advanced fields and scheduling as you require.
9. Click **Run on selected hosts**.

**Verification**

- If the host can access Satellite Server, the following command succeeds on your host:

  ```
  $ curl --head https://satellite.example.com
  ```
- If the host can access Capsule Server, the following command succeeds on your host:

  ```
  $ curl --head https://capsule.example.com:9090/features
  ```

**Additional resources**

- [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs")

## 9.2. Deploying the CA certificate on a host by using Ansible REX

You can use remote execution (REX) with the Ansible provider to deploy the CA certificate.

**Prerequisites**

- The host is registered to Satellite.

- Remote execution is enabled on the host.
- The CA certificate has been changed on Satellite Server. For more information, see [Planning for self-signed CA certificate renewal](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#planning-for-self-signed-ca-certificate-renewal) in *Administering Red Hat Satellite*.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Jobs**.
2. Click **Run Job**.
3. From the **Job category** list, select **Ansible Commands**.
4. From the **Job template** list, select **Download and execute a script**.
5. Click **Next**.
6. Select hosts on which you want to execute the job.
7. In the **url** field, enter the following URL:

   ```
   https://satellite.example.com/unattended/public/foreman_ca_refresh
   ```

   You can use HTTP when the CA certificate is expired.
8. Optional: Click **Next** and configure advanced fields and scheduling as you require.
9. Click **Run on selected hosts**.

**Verification**

- If the host can access Satellite Server, the following command succeeds on your host:

  ```
  $ curl --head https://satellite.example.com
  ```
- If the host can access Capsule Server, the following command succeeds on your host:

  ```
  $ curl --head https://capsule.example.com:9090/features
  ```

**Additional resources**

- [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs")

## 9.3. Deploying the CA certificate on a host manually

You can deploy the CA certificate on the host manually by rendering a public provisioning template, which provides the CA certificate.

**Prerequisites**

- You have root access on both your Satellite Server and your host.

**Procedure**

1. Download the certificate on your Satellite Server:

   ```
   # curl -o "satellite_ca_cert.crt" https://satellite.example.com/unattended/public/foreman_raw_ca
   ```
2. Transfer the CA certificate to your host securely, for example by using `scp`.
3. Login to your host by using SSH.
4. Copy the certificate to the Subscription Manager configuration directory:

   ```
   # cp -u satellite_ca_cert.crt /etc/rhsm/ca/katello-server-ca.pem
   ```
5. Copy the certificate to the truststore:

   ```
   # cp satellite_ca_cert.crt /etc/pki/ca-trust/source/anchors/
   ```
6. Update the truststore:

   ```
   # update-ca-trust
   ```

**Verification**

- If the host can access Satellite Server, the following command succeeds on your host:

  ```
  $ curl --head https://satellite.example.com
  ```
- If the host can access Capsule Server, the following command succeeds on your host:

  ```
  $ curl --head https://capsule.example.com:9090/features
  ```
