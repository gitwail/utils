---
title: "Configuring Kerberos SSO for Active Directory users in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_authentication_for_red_hat_satellite_users"
guide_title: "Configuring authentication for Red Hat Satellite users"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-kerberos-sso-for-active-directory-users-in-project_authentication"
---
# Chapter 6. Configuring Kerberos SSO for Active Directory users in Satellite

If the base system of your Satellite Server is connected directly to Active Directory (AD), you can configure AD as an external authentication source for Satellite. Direct AD integration means that a Linux system is joined directly to the AD domain where the identity is stored.

AD users can log in using the following methods:

- Username and password
- Kerberos single sign-on

## 6.1. Joining the Satellite Server system to an AD domain

The base system of your Satellite Server must be joined to an Active Directory (AD) domain before you can configure the AD authentication source on your Satellite Server. Use the System Security Services Daemon (SSSD) and Samba services to join the base system to the AD domain.

**Procedure**

1. Install the following packages on Satellite Server:

   ```
   # satellite-maintain packages install adcli krb5-workstation oddjob-mkhomedir oddjob realmd samba-winbind-clients samba-winbind samba-common-tools samba-winbind-krb5-locator sssd
   ```
2. Join the system to the AD domain, specifying the required software:

   ```
   # realm join AD.EXAMPLE.COM --membership-software=samba --client-software=sssd
   ```

**Additional resources**

- [Connecting RHEL systems directly to AD using Samba Winbind](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/integrating_rhel_systems_directly_with_windows_active_directory/index#connecting-rhel-systems-directly-to-ad-using-samba-winbind_integrating-rhel-systems-directly-with-active-directory)

## 6.2. Configuring the Active Directory authentication source on Satellite Server

Enable Active Directory (AD) users to access Satellite by configuring the corresponding authentication provider on your Satellite Server.

**Procedure**

1. Define AD realm configuration in a location where Satellite expects it:

   1. Create a directory named `/etc/ipa/`:

      ```
      # mkdir /etc/ipa/
      ```
   2. Create the `/etc/ipa/default.conf` file with the following contents to configure the Kerberos realm for the AD domain:

      ```
      [global]
      realm = AD.EXAMPLE.COM
      ```
2. Configure the Apache keytab for Kerberos connections:

   1. Update the `/etc/samba/smb.conf` file with the following settings to configure how Samba interacts with AD:

      ```
      [global]
      workgroup = AD.EXAMPLE
      realm = AD.EXAMPLE.COM
      kerberos method = system keytab
      security = ads
      ```
   2. Add the Kerberos service principal to the keytab file at `/etc/httpd/conf/http.keytab`:

      ```
      # KRB5_KTNAME=FILE:/etc/httpd/conf/http.keytab net ads keytab create HTTP -U Administrator -s /etc/samba/smb.conf
      ```

      > **Note**
      >
      > The `net ads keytab create` command was introduced in Samba version 4.21.1. If your system uses an earlier version of Samba, use the `net ads keytab add` command.
3. Configure the System Security Services Daemon (SSSD) on your Satellite Server:

   1. Configure the AD access control provider to evaluate and enforce Group Policy Object (GPO) access control rules for the `foreman` PAM service. In the `[domain/ad.example.com]` section of your `/etc/sssd/sssd.conf` file, set the `ad_gpo_access_control` and `ad_gpo_map_service` options as follows:

      ```
      [domain/ad.example.com]
      ad_gpo_access_control = enforcing
      ad_gpo_map_service = +foreman
      ```

      For more information on GPOs, see [How SSSD interprets GPO access control rules](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/integrating_rhel_systems_directly_with_windows_active_directory/managing-direct-connections-to-ad_integrating-rhel-systems-directly-with-active-directory#how-sssd-interprets-gpo-access-control-rules_applying-group-policy-object-access-control-in-rhel) in *Integrating RHEL systems directly with Windows Active Directory (RHEL 9)*.
   2. If your Satellite Server runs in an IPv6-only network and also runs on RHEL 9.6 and earlier or RHEL 10.0, set the `lookup_family_order` option in the `[domain/ad.example.com]` section of the `/etc/sssd/sssd.conf` file:

      ```
      [domain/ad.example.com]
      lookup_family_order = ipv6_only
      ```

      If the DNS name of the AD server can be translated to both an IPv4 and IPv6 address but the IPv4 address is not accessible, SSSD requires `lookup_family_order` to translate the DNS name correctly. Without the option, AD users are unable to use `kinit` to authenticate to Satellite.
   3. Restart SSSD:

      ```
      # systemctl restart sssd
      ```
4. Enable the authentication source:

   ```
   # satellite-installer --foreman-ipa-authentication true
   ```

**Verification**

- To verify that AD users can log in to Satellite by entering their credentials, log in to Satellite web UI at https://satellite.example.com. Enter the user name in the user principal name (UPN) format, for example: `ad_user@AD.EXAMPLE.COM`.
- To verify that AD users can authenticate by using Kerberos single sign-on:

  - Obtain a Kerberos ticket-granting ticket (TGT) on behalf of an AD user:

    ```
    $ kinit ad_user@AD.EXAMPLE.COM
    ```
  - Verify user authentication by using your TGT:

    ```
    $ curl \
    --negotiate \
    --user : \
    https://satellite.example.com/users/extlogin
    ```

    If external authentication is configured correctly, the `curl` command redirects you to `https://satellite.example.com/hosts`:

    ```
    <html><body>You are being <a href="satellite.example.com/hosts">redirected</a>.</body></html>
    ```

**Troubleshooting**

- Connecting to the AD LDAP can sometimes fail with an error such as the following appearing in the logs:

  ```
  Authentication failed with status code: {
    "error": { "message": "ERF77-7629 [Foreman::LdapException]: Error while connecting to 'server.com' LDAP server at 'ldap.example.com' during authentication ([Net::LDAP::Error]: Connection reset by peer - SSL_connect)" } }
  ```

  If you see this error, verify which cipher is used for the connection:

  ```
  # openssl s_client -connect ldap.example.com:636
  ```

  If the `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384` cipher is used, disable it on either the Satellite Server side or on the AD side. The `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384` cipher is known to cause incompatibilities.

  For more information, see the Red Hat Knowledgebase solution [API calls to Red Hat Satellite 6 fail intermittently on LDAP authentication](https://access.redhat.com/solutions/4870221).

**Additional resources**

- [Configuring Firefox to use Kerberos for single sign-on in *Red Hat Enterprise Linux 9 Configuring authentication and authorization in RHEL*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_authentication_and_authorization_in_rhel/configuring_applications_for_sso#Configuring_Firefox_to_use_Kerberos_for_SSO)
- [Chapter 9, *Resetting external authentication configuration for Kerberos SSO*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#resetting-external-authentication-configuration-for-kerberos-sso "Chapter 9. Resetting external authentication configuration for Kerberos SSO")
