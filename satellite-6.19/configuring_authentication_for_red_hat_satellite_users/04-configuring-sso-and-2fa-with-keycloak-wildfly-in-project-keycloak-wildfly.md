---
title: "Configuring SSO and 2FA with Red Hat Single Sign-On in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_authentication_for_red_hat_satellite_users"
guide_title: "Configuring authentication for Red Hat Satellite users"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-sso-and-2fa-with-keycloak-wildfly-in-project_keycloak-wildfly"
---
# Chapter 4. Configuring SSO and 2FA with Red Hat Single Sign-On in Satellite

Red Hat Single Sign-On is an open source identity and access management solution that provides various authentication features. You can integrate Satellite Server with your existing Red Hat Single Sign-On server to delegate user authentication and authorization to Red Hat Single Sign-On.

> **Important**
>
> Configuring Satellite with Red Hat Single Sign-On is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

Red Hat Single Sign-On users can log in using the following login methods:

- User name and password in Satellite web UI
- User name and password in Hammer CLI

> **Note**
>
> Red Hat Single Sign-On users cannot use both Satellite web UI and Hammer CLI authentication in Satellite at the same time.

- Time-based one-time password (TOTP)

## 4.1. Prerequisites for configuring Satellite with Red Hat Single Sign-On authentication

Your Satellite Server and Red Hat Single Sign-On server must meet the following requirements before you configure Red Hat Single Sign-On authentication.

> **Note**
>
> The Red Hat Single Sign-On 7 product family has reached End of Full Support. Use Red Hat build of Keycloak instead in your Satellite deployments. For information about configuring Red Hat build of Keycloak authentication, see [Chapter 5, *Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-sso-and-2fa-with-keycloak-in-project_keycloak-quarkus "Chapter 5. Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite").
>
> For information about migrating from Red Hat Single Sign-On to Red Hat build of Keycloak, see [documentation for Red Hat build of Keycloak](https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0).

On your Satellite Server:

- Install the packages required for registering a Red Hat Single Sign-On client:

  ```
  # satellite-maintain packages install mod_auth_openidc keycloak-httpd-client-install python3-lxml
  ```

On the Red Hat Single Sign-On side, ensure you meet the following requirements:

- Your Red Hat Single Sign-On server uses HTTPS instead of HTTP.
- If the certificates or the CA are self-signed, they have been added to the end-user certificate truststore.
- Your Red Hat Single Sign-On account has administrative privileges.
- A realm is created on the Red Hat Single Sign-On server for Satellite user accounts, for example `Satellite_Realm`.
- User accounts have been imported or added to Red Hat Single Sign-On. For more information about importing or creating users, see the [*Red Hat Single Sign-On Server Administration Guide*](https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html/server_administration_guide/assembly-managing-users_server_administration_guide#proc-creating-user_server_administration_guide).

## 4.2. Registering Satellite as a client of Red Hat Single Sign-On

To allow Red Hat Single Sign-On users to authenticate to Satellite, you must register Satellite as a client of Red Hat Single Sign-On on your Satellite Server. This configuration requires selecting and configuring the authentication method: Satellite web UI access or Hammer CLI access.

Perform these steps on your Satellite Server.

**Procedure**

1. Choose the authentication method you want Red Hat Single Sign-On users to use when authenticating to Satellite:

   - If you want users to authenticate by using the Satellite web UI:

     1. Create a client for Satellite. Use `foreman-openidc` as the application name.

        ```
        # keycloak-httpd-client-install --app-name foreman-openidc \
        --keycloak-server-url "https://rhsso.example.com" \
        --keycloak-admin-username "admin" \
        --keycloak-realm "Satellite_Realm" \
        --keycloak-admin-realm master \
        --keycloak-auth-role root-admin \
        -t openidc -l /users/extlogin --force
        ```
     2. Configure Satellite to use Red Hat Single Sign-On as an authentication source for Satellite web UI:

        ```
        # satellite-installer --foreman-keycloak true \
        --foreman-keycloak-app-name "foreman-openidc" \
        --foreman-keycloak-realm "Satellite_Realm"
        ```
   - If you want users to authenticate by using the Hammer CLI:

     1. Create a client for Satellite. Use `hammer-openidc` as the application name.

        ```
        # keycloak-httpd-client-install --app-name hammer-openidc \
        --keycloak-server-url "https://rhsso.example.com" \
        --keycloak-admin-username "admin" \
        --keycloak-realm "Satellite_Realm" \
        --keycloak-admin-realm master \
        --keycloak-auth-role root-admin \
        -t openidc -l /users/extlogin --force
        ```
     2. Configure Satellite to use Red Hat Single Sign-On as an authentication source for Hammer CLI:

        ```
        # satellite-installer --foreman-keycloak true \
        --foreman-keycloak-app-name "hammer-openidc" \
        --foreman-keycloak-realm "Satellite_Realm"
        ```
2. Restart the `httpd` service:

   ```
   # systemctl restart httpd
   ```

## 4.3. Configuring the Satellite client in Red Hat Single Sign-On

On the Red Hat Single Sign-On side, you must configure the Satellite client with valid redirect URIs and mappers. This includes setting the appropriate client authentication mode, redirect URIs, and necessary mappers to support Satellite web UI or Hammer CLI authentication.

Perform these steps in the Red Hat Single Sign-On web UI.

**Procedure**

1. Go to the realm created for Satellite users. Navigate to **Clients** and click the Satellite client.
2. Configure access type:

   - If you are configuring a client that will provide Satellite web UI authentication, select **confidential** from the **Access Type** list.
   - If you are configuring a client that will provide Hammer CLI authentication, select **public** from the **Access Type** list.
3. Configure **Valid redirect URI** addresses:

   - If you are configuring a client that will provide Satellite web UI authentication:

     - You will see a pre-defined URI: `https://satellite.example.com/users/extlogin/redirect_uri`. Do not change or remove this URI.
     - Add another URI below the pre-defined URI: `https://satellite.example.com/users/extlogin`
   - If you are configuring a client that will provide Hammer CLI authentication:

     - You will see a pre-defined URI: `https://satellite.example.com/users/extlogin/redirect_uri`. Do not change or remove this URI.
     - Add another URI below the pre-defined URI: `urn:ietf:wg:oauth:2.0:oob`
4. Click **Save**.
5. On the **Mappers** tab, click **Create** to add an audience mapper.

   1. From the **Mapper Type** list, select **Audience**.
   2. From the **Included Client Audience** list, select the Satellite client.
6. Click **Save**.
7. On the **Mappers** tab, click **Create** to add a group mapper so that you can specify authorization in Satellite based on group membership.

   1. From the **Mapper Type** list, select **Group Membership**.
   2. In the **Token Claim Name** field, enter **groups**.
   3. Set the **Full group path** setting to `OFF`.
8. Click **Save**.

**Additional resources**

- [Red Hat Single Sign-On *Server Administration Guide*](https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html-single/server_administration_guide/index)

## 4.4. Configuring a Satellite client to provide Satellite web UI authentication with Red Hat Single Sign-On

If you are configuring a client that will provide Satellite web UI authentication to your Satellite deployment, delegate authentication to the Red Hat Single Sign-On server and add Red Hat Single Sign-On as an external authentication source in Satellite.

Perform these steps in the Satellite web UI.

**Prerequisites**

- Ensure that the **Access Type** setting in the Satellite client in the Red Hat Single Sign-On web UI is set to **confidential**. For more information, see [Section 4.3, “Configuring the Satellite client in Red Hat Single Sign-On”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-the-satellite-client-in-keycloak_keycloak-wildfly "4.3. Configuring the Satellite client in Red Hat Single Sign-On").

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. On the **Authentication** tab, configure the following settings:

   1. **Authorize login delegation**: Set to `Yes`.
   2. **Authorize login delegation auth source user autocreate**: Set to `External`.
   3. **Login delegation logout URL**: Set to `https://satellite.example.com/users/extlogout`.
   4. **OIDC Algorithm**: For example, set to `RS256`.
   5. **OIDC Audience**: Set to the client ID for Red Hat Single Sign-On.
   6. **OIDC Issuer**: Set to `https://rhsso.example.com/auth/realms/Satellite_Realm`.
   7. **OIDC JWKs URL**: Set to `https://rhsso.example.com/auth/realms/Satellite_Realm/protocol/openid-connect/certs`.
3. Navigate to **Administer** > **Authentication Sources**.

   1. From the **External** menu, select **Edit**.
   2. On the **Locations** tab, add the locations that you want to be able to use the Red Hat Single Sign-On authentication source.
   3. On the **Organizations** tab, add the organizations that you want to be able to use the Red Hat Single Sign-On authentication source.
   4. Click **Submit**.

## 4.5. Configuring a Satellite client to provide Hammer CLI authentication with Red Hat Single Sign-On

If you are configuring a client that will provide Hammer CLI authentication to your Satellite deployment, delegate authentication to the Red Hat Single Sign-On server and add Red Hat Single Sign-On as an external authentication source in Satellite.

Perform these steps on the Satellite client registered to Red Hat Single Sign-On.

**Prerequisites**

- Ensure that the **Access Type** setting in the Satellite client in the Red Hat Single Sign-On web UI is set to **public**. For more information, see [Section 4.3, “Configuring the Satellite client in Red Hat Single Sign-On”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-the-satellite-client-in-keycloak_keycloak-wildfly "4.3. Configuring the Satellite client in Red Hat Single Sign-On").
- Obtain the values to configure Satellite settings from the following URL: `https://rhsso.example.com/auth/realms/Satellite_Realm/.well-known/openid-configuration`. Replace *Satellite_Realm* with the name of the Red Hat Single Sign-On realm created for your Satellite server.

**Procedure**

1. Set the login delegation to `true` so that users can authenticate using the Open IDC protocol:

   ```
   $ hammer settings set --name authorize_login_delegation --value true
   ```
2. Set the login delegation logout URL:

   ```
   $ hammer settings set --name login_delegation_logout_url \
   --value https://satellite.example.com/users/extlogout
   ```
3. Set the algorithm for encoding: For example, to use the `RS256` algorithm:

   ```
   $ hammer settings set --name oidc_algorithm --value 'RS256'
   ```
4. Add the value for the Hammer client in the Open IDC audience:

   ```
   $ hammer settings set --name oidc_audience \
   --value "['satellite.example.com-hammer-openidc']"
   ```
5. Set the value for the Open IDC issuer:

   ```
   $ hammer settings set --name oidc_issuer \
   --value "https://rhsso.example.com/auth/realms/Satellite_Realm"
   ```
6. Set the value for Open IDC Java Web Token (JWT):

   ```
   $ hammer settings set --name oidc_jwks_url \
   --value "https://rhsso.example.com/auth/realms/Satellite_Realm/protocol/openid-connect/certs"
   ```
7. Retrieve the ID of the Red Hat Single Sign-On authentication source:

   ```
   $ hammer auth-source external list
   ```
8. Set the location and organization:

   ```
   $ hammer auth-source external update \
   --id My_Authentication_Source_ID \
   --location-ids My_Location_ID \
   --organization-ids My_Organization_ID
   ```

## 4.6. Configuring Satellite with Red Hat Single Sign-On for TOTP authentication

If you want users to authenticate with time-based one-time passwords (TOTP), configure an OTP policy for the Satellite realm in Red Hat Single Sign-On.

**Procedure**

1. In the Red Hat Single Sign-On web UI, navigate to the Satellite realm.
2. Navigate to **Authentication**.
3. On the **Policies** tab, click the **OTP Policy** tab. Ensure that the **Supported Applications** field includes FreeOTP or Google Authenticator.
4. Configure the OTP settings to suit your requirements.
5. On **Required Actions** tab, enable the **Set as default action** setting for the **Configure OTP** action.

**Additional resources**

- [Red Hat Single Sign-On Server Administration Guide](https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/24.0/html/server_administration_guide/configuring-authentication_server_administration_guide#configuring-authentication_server_administration_guide)
- [Red Hat build of Keycloak Server Administration Guide](https://docs.redhat.com/en/documentation/red_hat_single_sign-on/7.6/html-single/server_administration_guide/index#configuring-authentication_server_administration_guide)

## 4.7. Configuring group mapping for Red Hat Single Sign-On authentication

Optionally, to implement the role-based access control (RBAC), create a group in Satellite, assign a role to this group, and map an Red Hat Single Sign-On group to the Satellite group. Anyone in the given group in Red Hat Single Sign-On will log in under the corresponding Satellite group.

For example, you can configure users of the Satellite-admin user group defined in Active Directory to authenticate as users with administrator privileges on Satellite.

If you do not configure group mapping, every user will receive the *Default role* permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **User Groups**.
2. Click **Create User Group**.

   1. In the **Name** field, enter a name for the user group. Enter a name that is different from the Active Directory user group name.
   2. Do not add any users or user groups to the new group in Satellite web UI.
3. On the **Roles** tab, select **Administer**.
4. On the **External Groups** tab, click **Add external user group**.

   1. In the **Name** field, enter the name of the Active Directory group.
   2. From the **Auth Source** drop-down menu, select **EXTERNAL**.
5. Click **Submit**.

## 4.8. Logging in to Satellite configured with Red Hat Single Sign-On as an authentication source

With Red Hat Single Sign-On configured as an authentication source for Satellite, users defined in a Red Hat Single Sign-On realm can log in to Satellite Server. The available login methods depend on how you configured integration between Red Hat Single Sign-On and Satellite.

**Procedure**

1. To authenticate to the Satellite web UI, in your browser, go to `https://satellite.example.com` and enter your credentials.
2. To authenticate to the Satellite web UI by using Red Hat Single Sign-On TOTP:

   1. In your browser, log in to Satellite. Satellite redirects you to the Red Hat Single Sign-On login screen.
   2. Enter your username and password, and click **Log In**.
   3. On your first login attempt, Red Hat Single Sign-On requests you to configure your client by scanning the bar code and entering your PIN. Once authenticated, your browser redirects you back to Satellite and logs you in.
3. To authenticate to the Satellite CLI with Hammer:

   1. Ensure that Hammer is configured to enforce session usage in `~/.hammer/cli.modules.d/foreman.yml`:

      ```yaml
      :foreman:
        :use_sessions: true
      ```
   2. Initiate an authentication session with `hammer auth login oauth`:

      ```
      $ hammer auth login oauth \
      --oidc-token-endpoint 'https://rhsso.example.com/auth/realms/Satellite_realm/protocol/openid-connect/token' \
      --oidc-authorization-endpoint 'https://rhsso.example.com/auth' \
      --oidc-client-id 'satellite.example.com-hammer-openidc' \
      --oidc-redirect-uri urn:ietf:wg:oauth:2.0:oob
      ```
4. To authenticate to the Satellite CLI with Hammer by using Red Hat Single Sign-On TOTP:

   1. Ensure that Hammer is configured to enforce session usage in `~/.hammer/cli.modules.d/foreman.yml`:

      ```yaml
      :foreman:
        :use_sessions: true
      ```
   2. Initiate an authentication session by using `--two-factor` with `hammer auth login oauth`:

      ```
      $ hammer auth login oauth \
      --two-factor \
      --oidc-token-endpoint 'https://rhsso.example.com/auth/realms/Satellite_realm/protocol/openid-connect/token' \
      --oidc-authorization-endpoint 'https://rhsso.example.com/auth' \
      --oidc-client-id 'satellite.example.com-hammer-openidc' \
      --oidc-redirect-uri urn:ietf:wg:oauth:2.0:oob
      ```
   3. You will be prompted to enter a success code. To retrieve the success code, navigate to the URL that the command returns.
   4. Enter the success code in CLI.
