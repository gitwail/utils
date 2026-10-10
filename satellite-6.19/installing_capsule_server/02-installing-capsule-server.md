---
title: "Installing Capsule Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_capsule_server"
guide_title: "Installing Capsule Server"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#installing-capsule-server"
---
# Chapter 2. Installing Capsule Server

To install Capsule Server, register the server to Satellite Server, configure repositories, install packages, and set up SSL certificates to enable content management and remote execution capabilities in distributed environments.

## 2.1. Registering Capsule Server

Register the base operating system to Satellite Server to access Capsule Server installation packages.

### 2.1.1. Prerequisites for registering Capsule Server to Satellite Server

Your environment must meet the following requirements before you can register your Capsule Server to your Satellite Server.

- Prerequisites for Red Hat subscription manifest:

  - On Satellite Server, a manifest must be installed and it must contain the appropriate repositories for the organization you want Capsule to belong to.
  - The manifest must contain repositories for the base operating system on which you want to install Capsule, as well as any clients that you want to connect to Capsule.
  - The repositories must be synchronized.

    For more information on manifests and repositories, see [Managing Red Hat Subscriptions](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Red_Hat_Subscriptions_content-management) in *Managing content*.
- Prerequisites for HTTP proxy and network:

  - The Satellite Server base operating system must be able to resolve the host name of the Capsule base operating system and vice versa.
  - Ensure HTTPS connection using client certificate authentication is possible between Capsule Server and Satellite Server. HTTP proxies between Capsule Server and Satellite Server are not supported.
  - You must configure the host and network-based firewalls accordingly.

### 2.1.2. Registering a host to Satellite by using Satellite web UI

You can register hosts with Satellite using the host registration feature in the Satellite web UI. For more information, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Register Host**.
2. From the **Activation Keys** list, select the activation keys to assign to your host.
3. Click **Generate** to create the registration command.
4. Click on the *files* icon to copy the command to your clipboard.
5. Connect to your host using SSH and run the registration command.
6. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

### 2.1.3. Registering a host to Satellite by using Hammer CLI

You can register hosts with Satellite using the host registration feature in Hammer CLI. For more information, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.

**Procedure**

1. Generate the host registration command:

   ```
   $ hammer host-registration generate-command \
   --activation-keys "My_Activation_Key"
   ```

   If your hosts do not trust the SSL certificate of Satellite Server, you can disable SSL validation by adding the `--insecure` flag to the registration command.

   ```
   $ hammer host-registration generate-command \
   --activation-keys "My_Activation_Key" \
   --insecure true
   ```
2. Connect to your host using SSH and run the registration command.
3. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

### 2.1.4. Registering a host to Satellite by using Satellite API

You can register hosts with Satellite using the host registration feature in the Satellite API. For more information, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.

**Procedure**

1. Generate the host registration command using the Satellite API:

   ```
   # curl -X POST https://satellite.example.com/api/registration_commands \
   --user "My_User_Name" \
   -H 'Content-Type: application/json' \
   -d '{ "registration_command": { "activation_keys": ["My_Activation_Key_1, My_Activation_Key_2"] }}'
   ```

   If your hosts do not trust the SSL certificate of Satellite Server, you can disable SSL validation by adding the `--insecure` flag to the registration command.

   ```
   # curl -X POST https://satellite.example.com/api/registration_commands \
   --user "My_User_Name" \
   -H 'Content-Type: application/json' \
   -d '{ "registration_command": { "activation_keys": ["My_Activation_Key_1, My_Activation_Key_2"], "insecure": true }}'
   ```

   Use an activation key to simplify specifying the environments. For more information, see [Managing Activation Keys](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management) in *Managing content*.

   To enter a password as a command line argument, use `username:password` syntax. Keep in mind this can save the password in the shell history. Alternatively, you can use a temporary personal access token instead of a password. To generate a token in the Satellite web UI, navigate to **My Account** > **Personal Access Tokens**.
2. Connect to your host using SSH and run the registration command.
3. Check the `/etc/yum.repos.d/redhat.repo` file and ensure that the appropriate repositories have been enabled.

## 2.2. Configuring repositories

Configure repositories to install your Capsule Server.

**Procedure**

1. Disable all repositories:

   ```
   # subscription-manager repos --disable "*"
   ```
2. Enable the following repositories:

   ```
   # subscription-manager repos \
   --enable=rhel-9-for-x86_64-baseos-rpms \
   --enable=rhel-9-for-x86_64-appstream-rpms \
   --enable=satellite-capsule-6.19-for-rhel-9-x86_64-rpms \
   --enable=satellite-maintenance-6.19-for-rhel-9-x86_64-rpms
   ```

**Verification**

- Verify that the required repositories are enabled:

  ```
  # dnf repolist enabled
  ```

## 2.3. Installing Capsule packages

Install Capsule Server packages to set up the core software components needed for Capsule functionality.

**Procedure**

1. Upgrade all packages:

   ```
   # dnf upgrade
   ```
2. Install the packages:

   ```
   # dnf install satellite-capsule
   ```

## 2.4. Configuring Capsule Server with SSL certificates

Red Hat Satellite uses SSL certificates to enable encrypted communications between Satellite Server, Capsule Servers, and all hosts. Depending on the requirements of your organization, you must configure your Capsule Server with a default or custom certificate.

### 2.4.1. Configuring Capsule Server with a default SSL certificate

Use this section to configure Capsule Server with an SSL certificate that is signed by Satellite Server default Certificate Authority (CA).

**Prerequisites**

- Capsule Server is registered to Satellite Server. For more information, see [Section 2.1, “Registering Capsule Server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#registering-capsule-server "2.1. Registering Capsule Server").
- Capsule Server packages are installed. For more information, see [Section 2.3, “Installing Capsule packages”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#installing-capsule-packages "2.3. Installing Capsule packages").
- The required ports are open. For more information, see [Section 1.5, “Opening required ports”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#opening-required-ports "1.5. Opening required ports").

**Procedure**

1. On Satellite Server, to store all the source certificate files for your Capsule Server, create a directory that is accessible only to the `root` user, for example `/root/capsule_cert`:

   ```
   # mkdir /root/capsule_cert
   ```
2. On Satellite Server, generate the `/root/capsule_cert/capsule.example.com-certs.tar` certificate archive for your Capsule Server:

   ```
   # capsule-certs-generate \
   --foreman-proxy-fqdn capsule.example.com \
   --certs-tar /root/capsule_cert/capsule.example.com-certs.tar
   ```

   Retain a copy of the `satellite-installer` command that the `capsule-certs-generate` command returns for deploying the certificate to your Capsule Server.

   **Example output of `capsule-certs-generate`**

   ```
   output omitted
   satellite-installer --scenario capsule \
   --certs-tar-file "/root/capsule_cert/capsule.example.com-certs.tar" \
   --foreman-proxy-foreman-base-url "https://satellite.example.com" \
   --foreman-proxy-trusted-hosts "satellite.example.com" \
   --foreman-proxy-trusted-hosts "capsule.example.com" \
   --foreman-proxy-oauth-consumer-key "s97QxvUAgFNAQZNGg4F9zLq2biDsxM7f" \
   --foreman-proxy-oauth-consumer-secret "6bpzAdMpRAfYaVZtaepYetomgBVQ6ehY"
   ```
3. On Satellite Server, copy the certificate archive file to your Capsule Server:

   ```
   # scp /root/capsule_cert/capsule.example.com-certs.tar \
   root@capsule.example.com:/root/capsule.example.com-certs.tar
   ```
4. On Capsule Server, to deploy the certificate, enter the `satellite-installer` command that the `capsule-certs-generate` command returns.

   > **Important**
   >
   > Do not delete the certificate archive file after you deploy the certificate. It is required, for example, when upgrading Capsule Server.

#### 2.4.1.1. Configuring Capsule Server with a custom SSL certificate

If you configure Satellite Server to use a custom SSL certificate, you must also configure each of your Capsule Servers with a distinct custom SSL certificate.

#### 2.4.1.2. Creating a custom SSL certificate for Capsule Server

On Satellite Server, create a custom certificate for your Capsule Server. If you already have a custom SSL certificate for Capsule Server, skip this procedure.

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
   prompt = no

   [ req_distinguished_name ]
   commonName = capsule.example.com

   [ v3_req ]
   basicConstraints = CA:FALSE
   keyUsage = digitalSignature, keyEncipherment
   extendedKeyUsage = serverAuth, clientAuth
   subjectAltName = @alt_names

   [ alt_names ]
   DNS.1 = capsule.example.com
   ```

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

#### 2.4.1.3. Deploying a custom SSL certificate to Capsule Server

Use this procedure to configure your Capsule Server with a custom SSL certificate signed by a Certificate Authority.

The `satellite-installer` command, which the `capsule-certs-generate` command returns, is unique to each Capsule Server. Do not use the same command on more than one Capsule Server.

**Prerequisites**

- Satellite Server is configured with a custom certificate. For more information, see [Configuring Satellite Server with a custom SSL certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#configuring-satellite-server-with-a-custom-ssl-certificate) in *Installing Satellite Server in a connected network environment*.
- Capsule Server is registered to Satellite Server. For more information, see [Section 2.1, “Registering Capsule Server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#registering-capsule-server "2.1. Registering Capsule Server").
- Capsule Server packages are installed. For more information, see [Section 2.3, “Installing Capsule packages”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#installing-capsule-packages "2.3. Installing Capsule packages").
- The required ports are open. For more information, see [Section 1.5, “Opening required ports”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#opening-required-ports "1.5. Opening required ports").

**Procedure**

1. On your Satellite Server, generate a certificate bundle:

   ```
   # capsule-certs-generate \
   --foreman-proxy-fqdn capsule.example.com \
   --certs-tar ~/capsule.example.com-certs.tar \
   --server-cert /root/capsule_cert/capsule_cert.pem \
   --server-key /root/capsule_cert/capsule_cert_key.pem \
   --server-ca-cert /root/capsule_cert/ca_cert_bundle.pem
   ```

   The options specified in the command include the following:

   `--server-cert`
   :   Path to Capsule Server certificate file that is signed by a Certificate Authority

   `--server-key`
   :   Path to the private key that was used to sign Capsule Server certificate

   `--server-ca-cert`
   :   Path to the Certificate Authority bundle
2. Retain a copy of the `satellite-installer` command that the `capsule-certs-generate` command returns for deploying the certificate to your Capsule Server.

   **Example output of `capsule-certs-generate`**

   ```
   output omitted
   satellite-installer --scenario capsule \
   --certs-tar-file "/root/capsule.example.com-certs.tar" \
   --foreman-proxy-foreman-base-url "https://satellite.example.com" \
   --foreman-proxy-trusted-hosts "satellite.example.com" \
   --foreman-proxy-trusted-hosts "capsule.example.com" \
   --foreman-proxy-oauth-consumer-key "My_OAuth_Consumer_Key" \
   --foreman-proxy-oauth-consumer-secret "My_OAuth_Consumer_Secret"
   ```
3. On your Satellite Server, copy the certificate archive file to your Capsule Server:

   ```
   # scp ~/capsule.example.com-certs.tar \
   root@capsule.example.com:/root/capsule.example.com-certs.tar
   ```
4. On your Capsule Server, to deploy the certificate, enter the `satellite-installer` command that the `capsule-certs-generate` command returns.

   > **Important**
   >
   > Do not delete the certificate archive file after you deploy the certificate. It is required, for example, when upgrading Capsule Server.

#### 2.4.1.4. Deploying a custom SSL certificate to hosts

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
  # dnf install http://capsule.example.com/pub/katello-ca-consumer-latest.noarch.rpm
  ```

**Additional resources**

- [Refreshing the self-signed CA certificate on hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#refreshing-the-self-signed-ca-certificate-on-hosts)

## 2.5. Resetting custom SSL certificate to default self-signed certificate on Capsule Server

If you want to revert to the default certificate configuration, you can reset a custom SSL certificate to the default self-signed certificate on your Capsule Server by re-registering your Capsule Server to Satellite.

**Procedure**

- To reset the custom SSL certificate to default self-signed certificate on your Capsule Server, you must re-register your Capsule Server through **Global Registration**. For more information, see [Registering hosts by using global registration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration) in *Managing hosts*.

**Verification**

1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules** and select any Capsule Server.
2. On the **Overview** tab, click **Refresh features**.

**Additional resources**

- [Reset custom SSL certificate to default self-signed certificate on Satellite Server in *Installing Satellite Server in a connected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#resetting-custom-ssl-certificate-to-default-self-signed-certificate-on-satellite_satellite)
- [Reset custom SSL certificate to default self-signed certificate on hosts in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#resetting-custom-ssl-certificate-to-default-self-signed-certificate-on-hosts_managing-hosts)

## 2.6. Assigning organization and location to Capsule Server

Assign the correct organization and location to Capsule Server to properly manage your Capsule Server within your organizational structure.

> **Note**
>
> Assigning a Capsule to the same location as your Satellite Server with an embedded Capsule prevents Red Hat Lightspeed from uploading the Red Hat Lightspeed inventory. To enable the inventory upload, synchronize SSH keys for both Capsules.

**Prerequisites**

- Your user account has the `assign_organizations` and `assign_locations` permissions.
- You belong to the organization and location that you want to assign to the Capsule.

**Procedure**

1. Log into the Satellite web UI.
2. From the **Organization** list in the upper-left of the screen, select **Any Organization**.
3. From the **Location** list in the upper-left of the screen, select **Any Location**.
4. In the Satellite web UI, navigate to **Hosts** > **All Hosts** and select Capsule Server.
5. From the options menu, select **Change associations** > **Organization**.
6. Select the organization where you want to assign this Capsule.
7. Select **Fix on mismatch**.
8. Click **Change organization**.
9. From the options menu, select **Change associations** > **Location**.
10. Select the location where you want to assign this Capsule.
11. Select **Fix on mismatch**.
12. Click **Change location**.
13. In the Satellite web UI, navigate to **Administer** > **Organizations** and click the organization to which you have assigned Capsule.
14. Click **Capsules** tab and ensure that Capsule Server is listed under the **Selected items** list, then click **Submit**.
15. In the Satellite web UI, navigate to **Administer** > **Locations** and click the location to which you have assigned Capsule.
16. Click **Capsules** tab and ensure that Capsule Server is listed under the **Selected items** list, then click **Submit**.

**Verification**

Optionally, you can verify if Capsule Server is correctly listed in the Satellite web UI.

1. Select the organization from the **Organization** list.
2. Select the location from the **Location** list.
3. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
4. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
