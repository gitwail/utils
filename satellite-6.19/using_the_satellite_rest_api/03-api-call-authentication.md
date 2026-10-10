---
title: "API call authentication"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_rest_api"
guide_title: "Using the Satellite REST API"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#api-call-authentication"
---
# Chapter 3. API call authentication

You must authenticate API calls to Satellite Server by using SSL certificates and valid user credentials, with options for HTTP basic authentication, SSL client certificates, or personal access tokens.

## 3.1. SSL authentication overview

Red Hat Satellite requires HTTPS for all API communications to provide encryption and identity verification. You can use either self-signed certificates or custom SSL certificates you configure.

Satellite 6.19 does not support non-SSL communications.

By default, Satellite Server uses a self-signed certificate. This certificate acts as both the server certificate to verify the encryption key and the certificate authority (CA) to trust the identity of Satellite Server.

**Additional resources**

- [Configuring Satellite Server with a custom SSL certificate in *Installing Satellite Server in a connected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#configuring-satellite-server-with-a-custom-ssl-certificate)
- [Configuring Satellite Server with a custom SSL certificate in *Installing Satellite Server in a disconnected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#configuring-satellite-server-with-a-custom-ssl-certificate)

## 3.2. Configuring SSL authentication

Configure SSL authentication to enable secure API requests to Satellite by installing and trusting the CA certificate.

**Procedure**

1. Obtain a certificate from your Satellite Server by using one of the following options:

   - If you plan to call the API from a remote server, download the CA certificate:

     ```
     $ curl \
     --output /etc/pki/ca-trust/source/anchors/satellite.example.com-katello-server-ca.crt \
     http://satellite.example.com/pub/katello-server-ca.crt
     ```
   - If you plan to call the API directly on your Satellite Server, copy the certificate to the `/etc/pki/ca-trust/source/anchors` directory:

     ```
     # cp /var/www/html/pub/katello-server-ca.crt /etc/pki/ca-trust/source/anchors/satellite.example.com-katello-server-ca.crt
     ```
2. Add the certificate to the list of trusted CAs:

   ```
   $ update-ca-trust extract
   ```

**Verification**

- Verify that your client trusts the Satellite SSL certificate by entering the API request without the `--cacert` option:

  ```
  $ curl \
  --request GET \
  --user My_User_Name:My_Password \
  https://satellite.example.com/api/v2/hosts
  ```

## 3.3. HTTP authentication overview

You must provide valid Satellite credentials to access the Satellite API.

The API uses HTTP Basic authentication to send encoded user credentials in the `Authorization` header. If a request does not include an appropriate `Authorization` header, the API returns a `401 Authorization Required` error.

> **Important**
>
> Basic authentication involves potentially sensitive information, for example, it sends passwords as plain text. The REST API requires HTTPS for transport-level encryption of plain text requests.

Some base64 libraries break encoded credentials into multiple lines and terminate each line with a newline character. This invalidates the header and causes a faulty request. The `Authorization` header requires the encoded credentials to be on a single line within the header.

**Additional resources**

- [RFC 2617 HTTP Authentication: Basic and Digest Access Authentication](http://tools.ietf.org/html/rfc2617)

## 3.4. Token authentication overview

You can use Personal Access Tokens to authenticate API requests instead of passwords. Additionally, you can manage your security by setting expiration dates or revoking tokens at any time.

### 3.4.1. Creating a Personal Access Token

Create a Personal Access Token to authenticate API requests without sharing your password.

**Prerequisites**

- Your user account has a role that grants the `create_personal_access_tokens` permission.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. Select a user for which you want to create a Personal Access Token.
3. On the **Personal Access Tokens** tab, click **Add Personal Access Token**.
4. Enter a **Name** for you Personal Access Token.
5. Optional: Select the **Expires** date to set an expiration date. If you do not set an expiration date, your Personal Access Token will never expire unless revoked.
6. Click Submit. You now have the Personal Access Token available to you on the **Personal Access Tokens** tab.

   > **Important**
   >
   > Ensure to store your Personal Access Token as you will not be able to access it again after you leave the page or create a new Personal Access Token. You can click **Copy to clipboard** to copy your Personal Access Token.

**Verification**

1. Make an API request to your Satellite Server and authenticate with your Personal Access Token:

   ```
   $ curl \
   --user My_Username:My_Personal_Access_Token \
   https://satellite.example.com/api/status
   ```
2. You should receive a response with status `200`, for example:

   ```
   {"satellite_version":"6.19.0","result":"ok","status":200,"version":"3.5.1.10","api_version":2}
   ```

   If you go back to **Personal Access Tokens** tab, you can see the updated **Last Used** time next to your Personal Access Token.

### 3.4.2. Revoking a Personal Access Token

Revoke a Personal Access Token before its expiration date when a token is compromised or no longer needed for API access.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. Select a user for which you want to revoke the Personal Access Token.
3. On the **Personal Access Tokens** tab, locate the Personal Access Token you want to revoke.
4. Click **Revoke** in the **Actions** column next to the Personal Access Token you want to revoke.

**Verification**

1. Make an API request to your Satellite Server and try to authenticate with the revoked Personal Access Token:

   ```
   $ curl \
   --user My_Username:My_Personal_Access_Token \
   https://satellite.example.com/api/status
   ```
2. You receive the following error message:

   ```
   {
     "error": {"message":"Unable to authenticate user My_Username"}
   }
   ```
