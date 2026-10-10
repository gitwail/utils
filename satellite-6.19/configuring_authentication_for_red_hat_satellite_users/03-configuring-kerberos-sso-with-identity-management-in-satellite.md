---
title: "Configuring Kerberos SSO with Identity Management in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_authentication_for_red_hat_satellite_users"
guide_title: "Configuring authentication for Red Hat Satellite users"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-kerberos-sso-with-Identity_Management-in-satellite"
---
# Chapter 3. Configuring Kerberos SSO with Identity Management in Satellite

Identity Management is an open-source identity management solution that provides centralized authentication, authorization, and account management services. You can integrate Satellite with your existing Identity Management server to enable Identity Management users to authenticate to Satellite.

With your Identity Management server configured as an external identity provider, users defined in Identity Management can log in to Satellite with their Identity Management credentials. If cross-forest trust is configured between Identity Management and Active Directory, Active Directory users can also log in to Satellite.

Identity Management users can log in using the following methods:

- Username and password
- Kerberos single sign-on

When cross-forest trust is configured between Identity Management and Active Directory, Active Directory users can log in to Satellite with their user principal name (UPN) and password.

## 3.1. Enrolling Satellite Server in your Identity Management domain

Create a host entry for your Satellite Server system in the Identity Management LDAP and configure the system to be a client in your Identity Management domain.

**Prerequisites**

- An existing Identity Management server
- Identity Management user account with privileges to enroll new Identity Management hosts

**Procedure**

1. On the Identity Management server:

   1. Create a host entry for the Satellite Server system.

      For more information, see [Red Hat Enterprise Linux 9 Managing IdM users, groups, hosts, and access control rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_idm_users_groups_hosts_and_access_control_rules).
   2. Create an entry for the HTTP service for Satellite Server. This enables access to the keytab file by creating a service principal for your Satellite Server.

      For more information on creating a service entry in Identity Management, see [Red Hat Enterprise Linux 9 Managing IdM users, groups, hosts, and access control rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/managing_idm_users_groups_hosts_and_access_control_rules/index#).
2. On your Satellite Server, configure the system as client in the Identity Management domain. This includes ensuring that the system meets the necessary prerequisites, installing the necessary packages, and running the `ipa-client-install` utility.

   For more information, see [Red Hat Enterprise Linux 9 Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux//9/html-single/installing_identity_management/index#assembly_installing-an-idm-client_installing-identity-management).

**Verification**

- On your Satellite Server, check that you are able to resolve a user defined on the Identity Management server. For example, to check the `admin` user that Identity Management creates by default:

  ```
  $ id admin
  ```

**Example 3.1. Enrolling a Satellite Server system as a Identity Management client from the command line by using a one-time password**

On the Identity Management server, a user named *admin* who has administrative privileges on the Identity Management server prepares a host entry for the Satellite Server system:

1. Authenticate as the Identity Management *admin* user:

   ```
   # kinit admin
   ```
2. Optional: Verify that you have authenticated successfully:

   ```
   # klist
   ```
3. Create a host entry from the command line. Specify that you want to use a random password for the enrollment.

   ```
   # ipa host-add --random satellite-server.example.com
   --------------------------------------------------
    Added host "satellite-server.example.com"
    --------------------------------------------------
     Host name: satellite-server.example.com
     Random password: W5YpARl=7M.n
     Password: True
     Keytab: False
     Managed by: idm-server.example.com
   ```
4. Enable access to the keytab file by creating a service principal for your Satellite Server:

   ```
   # ipa service-add HTTP/satellite-server.example.com
   ```

On the Satellite Server system, a user with Satellite administrative privileges enrolls the system into the Identity Management domain:

1. Install the Identity Management client packages:

   ```
   # satellite-maintain packages install ipa-client
   ```
2. Configure the Satellite Server system a client in Identity Management by using the random password produced by `ipa host-add` in a previous step:

   ```
   # ipa-client-install --password 'W5YpARl=7M.n'
   ```
3. Verify that you are able to resolve the Identity Management `admin` user from your Satellite Server:

   ```
   $ id admin
   ```

## 3.2. Configuring the Identity Management authentication source on Satellite Server

Connect your Satellite Server to your Identity Management domain by configuring Identity Management as an authentication provider on your Satellite Server.

> **Note**
>
> The Identity Management and Active Directory authentication sources are mutually exclusive. Running `satellite-installer --foreman-ipa-authentication` or `satellite-installer --foreman-ipa-authentication-api` overwrites any previously defined configuration for these authentication sources.

**Prerequisites**

- Satellite Server running on a system that is enrolled in the Identity Management domain.

**Procedure**

1. Enable access for your preferred login method:

   - To enable access to the Satellite web UI only:

     ```
     # satellite-installer \
     --foreman-ipa-authentication true
     ```
   - To enable access to the Satellite web UI and the Satellite API, including Hammer CLI:

     ```
     # satellite-installer \
     --foreman-ipa-authentication-api true \
     --foreman-ipa-authentication true
     ```

     > **Warning**
     >
     > Enabling access to both the Satellite web UI and the Satellite API poses a security risk. After the Identity Management user enters `kinit` to receive a Kerberos ticket-granting ticket (TGT), an attacker might obtain an API session. The attack is possible even if the user did not previously enter the Satellite login credentials anywhere, for example in the browser.
2. If your Satellite Server runs in an IPv6-only network and also runs on Red Hat Enterprise Linux 9.6 and earlier or Red Hat Enterprise Linux 10.0, set the `lookup_family_order` option in the `[domain/idm-server.example.com]` section of the `/etc/sssd/sssd.conf` file:

   ```
   [domain/idm-server.example.com]
   lookup_family_order = ipv6_only
   ```

   If the DNS name of the IdM server can be translated to both an IPv4 and IPv6 address but the IPv4 address is not accessible, SSSD requires `lookup_family_order` to translate the DNS name correctly. Without the option, IdM users are unable to use `kinit` to authenticate to Satellite.

**Verification**

- Log in to Satellite web UI by entering the credentials of a user defined in Identity Management.

**Additional resources**

- [Chapter 9, *Resetting external authentication configuration for Kerberos SSO*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#resetting-external-authentication-configuration-for-kerberos-sso "Chapter 9. Resetting external authentication configuration for Kerberos SSO")

## 3.3. Configuring host-based access control for Identity Management users logging in to Satellite

You can use host-based access control (HBAC) rules to manage access control within your Identity Management domain. In Identity Management, HBAC rules define which users can access which hosts and which services can be used to gain access.

For example, you can configure HBAC on the Identity Management server to limit access to Satellite Server only to selected users or user groups. By configuring a HBAC rule in the Identity Management domain, you can ensure Satellite does not create database entries for users who should not have access.

**Prerequisites**

- Identity Management user account with privileges to configure HBAC rules

**Procedure**

1. On the Identity Management server, configure HBAC control. For more information, see [*Red Hat Enterprise Linux 9 Managing IdM users, groups, hosts, and access control rules*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_idm_users_groups_hosts_and_access_control_rules/configuring-host-based-access-control-rules_managing-users-groups-hosts).

   1. Create a HBAC service for Satellite Server.
   2. Create a new HBAC rule to define the required access control. Add the following Identity Management entities to the HBAC rule:

      1. The HBAC service for Satellite Server
      2. The Satellite Server host
      3. The users or user groups to whom you want to grant access
   3. Make sure the default Identity Management `allow_all` rule is disabled. For information about how to disable `allow_all` without disrupting other services, see the [How to configure HBAC rules in IdM](https://access.redhat.com/solutions/67895) article on the Red Hat Customer Portal.
2. On your Satellite Server, load the host-based access control rules from Identity Management:

   ```
   # satellite-installer --foreman-pam-service foreman-prod
   ```

**Verification**

- Log in to the Satellite web UI as a user defined in Identity Management.

  - If the user is included in the HBAC rule, Satellite web UI will grant access.
  - If the user is not included in the HBAC rule, Satellite web UI will not grant access.

**Example 3.2. Configuring host-based access control to allow access to Satellite only for selected Identity Management users by using the command line**

On the Identity Management server, a user with administrative privileges configures a HBAC rule to allow selected users access to Satellite Server:

1. Authenticate as the user with privileges required to configure HBAC rules:

   ```
   $ kinit admin
   ```
2. Optional: Verify that you have authenticated successfully:

   ```
   $ klist
   ```
3. Create a new HBAC service named `satellite-prod`:

   ```
   $ ipa hbacsvc-add satellite-prod
   ```
4. Create a new HBAC rule:

   ```
   $ ipa hbacrule-add allow-satellite-prod
   ```
5. Add the following Identity Management entities to the HBAC rule:

   1. The `satellite-prod` HBAC service:

      ```
      $ ipa hbacrule-add-service allow-satellite-prod --hbacsvcs=satellite-prod
      ```
   2. The Satellite Server host:

      ```
      $ ipa hbacrule-add-host allow-satellite-prod --hosts=satellite.example.com
      ```
   3. The users or user groups to whom you want to grant access:

      ```
      $ ipa hbacrule-add-user allow-satellite-prod --user=ipa-user
      ```
6. Optional: Verify the status of the rule:

   ```
   $ ipa hbacrule-find satellite-prod
   $ ipa hbactest --user=ipa-user --host=satellite.example.com --service=satellite-prod
   ```
7. Disable the default `allow_all` rule:

```
$ ipa hbacrule-disable allow_all
```

On Satellite Server, a Satellite administrator re-runs `satellite-installer` to load the host-based access control rules from Identity Management:

```
# satellite-installer --foreman-pam-service foreman-prod
```

## 3.4. Configuring Hammer CLI to accept Identity Management credentials

To enable users to authenticate to the Hammer CLI by using their Identity Management credentials, update Hammer configuration.

**Prerequisites**

- You have enabled Identity Management access to the Satellite API. For more information, see [Section 3.2, “Configuring the Identity Management authentication source on Satellite Server”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-the-freeipa-authentication-source-on-satellite-server "3.2. Configuring the Identity Management authentication source on Satellite Server").

**Procedure**

- Open the `~/.hammer/cli.modules.d/foreman.yml` file on your Satellite Server and update the list of `foreman` parameters:

  - To enforce session usage, enable `:use_sessions:`:

    ```yaml
    :foreman:
      :use_sessions: true
    ```

    With this configuration, you will need to initiate an authentication session manually with `hammer auth login negotiate`.
  - Alternatively, to enforce session usage and also negotiate authentication by default:

    ```yaml
    :foreman:
      :default_auth_type: 'Negotiate_Auth'
      :use_sessions: true
    ```

    With this configuration, Hammer will negotiate authentication automatically when you enter the first `hammer` command.

## 3.5. Logging in to Hammer CLI with Identity Management credentials

Authenticate to the Satellite Hammer CLI with your Identity Management username and password.

**Prerequisites**

- You have configured Hammer CLI to accept Identity Management credentials. See [Section 3.4, “Configuring Hammer CLI to accept Identity Management credentials”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-hammer-cli-to-accept-Identity_Management-credentials_authentication "3.4. Configuring Hammer CLI to accept Identity Management credentials").

**Procedure**

1. Authenticate as a user defined in Identity Management to obtain a Kerberos ticket-granting ticket (TGT):

   ```
   $ kinit Identity_Management_user
   ```

   > **Warning**
   >
   > If you enabled access to the Satellite API and the Satellite web UI when you were configuring Identity Management as the authentication provider for Satellite, an attacker might now obtain an API session after the user receives the Kerberos TGT. The attack is possible even if the user did not previously enter the Satellite login credentials anywhere, for example in the browser.
2. If Hammer is not configured to negotiate authentication, initiate an authentication session manually:

   ```
   $ hammer auth login negotiate
   ```

   > **Note**
   >
   > If you destroy the active Kerberos ticket, for example with `kdestroy`, you will still be logged in to Hammer. To log out, enter `hammer auth logout`.

**Verification**

- Use any `hammer` command to check that the system does not ask you to authenticate. For example:

  ```
  $ hammer host list
  ```

## 3.6. Logging in to the Satellite web UI with Identity Management credentials in Mozilla Firefox

Users with valid Identity Management login credentials can log in to the Satellite web UI from the Mozilla Firefox browser.

Use the latest stable Mozilla Firefox browser.

**Prerequisites**

- You have Identity Management authentication configured in your Satellite environment. For more information, see [Chapter 3, *Configuring Kerberos SSO with Identity Management in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-kerberos-sso-with-Identity_Management-in-satellite "Chapter 3. Configuring Kerberos SSO with Identity Management in Satellite").
- The host on which you are using Mozilla Firefox is a client in the Identity Management domain.
- Your Mozilla Firefox is configured for Single Sign-On (SSO). For more information, see [Configuring Firefox to use Kerberos for single sign-on](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/configuring_applications_for_sso#Configuring_Firefox_to_use_Kerberos_for_SSO) in *Configuring authentication and authorization in Red Hat Enterprise Linux 9*.

**Procedure**

1. To log in with a Kerberos ticket granting ticket (TGT):

   1. Obtain the Kerberos TGT:

      ```
      $ kinit user
      Password for user@EXAMPLE.COM:
      ```
   2. In Mozilla Firefox, go to the URL of your Satellite Server.
   3. You are logged in automatically.
2. To log in with your username and password:

   1. In your browser address bar, enter the URL of your Satellite Server.
   2. Enter your username and password.

## 3.7. Logging in to the Satellite web UI with Identity Management credentials in Chrome

Users with valid Identity Management login credentials can log in to the Satellite web UI from the Chrome browser.

Use the latest stable Chrome browser.

**Prerequisites**

- You have Identity Management authentication configured in your Satellite environment. For more information, see [Chapter 3, *Configuring Kerberos SSO with Identity Management in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-kerberos-sso-with-Identity_Management-in-satellite "Chapter 3. Configuring Kerberos SSO with Identity Management in Satellite").
- The host on which you are using Chrome is a client in the Identity Management domain.
- Your Chrome browser is configured for Single Sign-On (SSO). For more information, see [Configuring the browser for Kerberos authentication](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/accessing_identity_management_services/index#configuring-the-browser-for-kerberos-authentication-login-web-ui-krb) in *Accessing Identity Management services in Red Hat Enterprise Linux 9*.

**Procedure**

1. To use Kerberos authentication to log in:

   1. Obtain the Kerberos ticket-granting ticket (TGT):

      ```
      $ kinit user
      Password for user@EXAMPLE.COM:
      ```
   2. In Chrome, go to the URL of your Satellite Server.
   3. You are logged in automatically.
2. To use username and password to log in:

   1. In your browser address bar, enter the URL of your Satellite Server.
   2. Enter your username and password.

## 3.8. Configuring a cross-forest trust between Identity Management and Active Directory for Satellite

If your Identity Management deployment includes a cross-forest trust with Active Directory (AD), you must configure host-based access control (HBAC) and the System Security Services Daemon (SSSD) before AD users can log in to Satellite.

**Prerequisites**

- An existing Identity Management server with a cross-forest trust with AD established. For more information, see [Red Hat Enterprise Linux 9 *Installing trust between IdM and AD*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/installing_trust_between_idm_and_ad).

**Procedure**

1. On your Identity Management server:

   1. Enable HBAC:

      1. Create an external group and add the AD group to it.
      2. Add the new external group to a POSIX group.
      3. Use the POSIX group in a HBAC rule.
2. On your Identity Management server and all replicas in your Identity Management topology, configure SSSD to transfer additional attributes of AD users:

   1. Add the AD user attributes to the *nss* and *domain* sections in `/etc/sssd/sssd.conf`. For example:

      ```
      [domain/EXAMPLE.com]
      ...
      krb5_store_password_if_offline = True
      ldap_user_extra_attrs=email:mail, lastname:sn, firstname:givenname

      [nss]
      user_attributes=+email, +firstname, +lastname

      [ifp]
      allowed_uids = ipaapi, root
      user_attributes=+email, +firstname, +lastname
      ```
   2. Clear the SSSD cache:

      1. Stop SSSD:

         ```
         # systemctl stop sssd
         ```
      2. Clear the cache:

         ```
         # sss_cache -E
         ```
      3. Start SSSD:

         ```
         # systemctl start sssd
         ```
   3. Verify the AD attributes value by using the `dbus-send` command on your Satellite Server and on your Identity Management server. Make sure that both outputs match.

      ```
      # dbus-send --print-reply --system --dest=org.freedesktop.sssd.infopipe /org/freedesktop/sssd/infopipe org.freedesktop.sssd.infopipe.GetUserAttr string:ad-user@ad-domain array:string:email,firstname,lastname
      ```
