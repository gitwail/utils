---
title: "Configuring an LDAP server as an external identity provider for Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_authentication_for_red_hat_satellite_users"
guide_title: "Configuring authentication for Red Hat Satellite users"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-an-ldap-server-as-an-external-identity-provider-for-project_authentication"
---
# Chapter 7. Configuring an LDAP server as an external identity provider for Satellite

Lightweight Directory Access Protocol (LDAP) is a set of open protocols used to access centrally stored information over a network. With Satellite, you can use one or multiple LDAP directories for external authentication.

## 7.1. Configuring TLS for secure LDAP

If Satellite uses TLS to establish a secure LDAP connection (LDAPS), you must obtain the CA certificates of your LDAP server and add them to the trusted CA list on the base operating system of your Satellite Server.

**Prerequisite**

- If your LDAP server uses a certificate chain with intermediate certificate authorities, the trusted CA list must contain all root and intermediate certificates.

**Procedure**

1. Obtain the CA certificate from the LDAP Server:

   1. If you use Active Directory Certificate Services, export the Enterprise PKI CA Certificate using the Base64 encoded X.509 format. See [How to configure Active Directory authentication with `TLS` on Satellite](https://access.redhat.com/solutions/1498773) for information on creating and exporting a CA certificate from an Active Directory server.
   2. Download the LDAP server certificate to a temporary location on the Satellite Server, such as `/tmp/example.crt`. You will remove the certificate when finished.

      The filename extensions `.cer` and `.crt` are only conventions and can refer to DER binary or PEM ASCII format certificates.
2. Add the LDAP server certificate to the system truststore:

   1. Import the certificate:

      ```
      # cp /tmp/example.crt /etc/pki/ca-trust/source/anchors
      ```
   2. Update the certificate authority truststore:

      ```
      # update-ca-trust extract
      ```
3. Delete the downloaded LDAP certificate from the temporary location on your Satellite Server.
4. Restart Satellite services:

   ```
   # satellite-maintain service restart
   ```

**Additional resources**

- [Using shared system certificates in *Red Hat Enterprise Linux 9 Securing networks*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/securing_networks/using-shared-system-certificates_securing-networks)

## 7.2. Configuring Satellite to use LDAP

Configure an LDAP authentication source to enable users to log in to Satellite with their existing LDAP credentials.

> **Note**
>
> While you can configure the LDAP server integrated with Identity Management as an external authentication source, Identity Management users will not be able to log in by using single sign-on. Instead, consider configuring Identity Management as an external identity provider. For more information, see [Chapter 3, *Configuring Kerberos SSO with Identity Management in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-kerberos-sso-with-Identity_Management-in-satellite "Chapter 3. Configuring Kerberos SSO with Identity Management in Satellite").

> **Important**
>
> Users cannot use both Identity Management and LDAP as an authentication method. After a user authenticates by using one of these methods, they cannot use the other method.
>
> To change the authentication method for a user, remove the automatically created user from Satellite.

**Prerequisites**

- Your LDAP server complies with the [RFC 2307](https://datatracker.ietf.org/doc/html/rfc2307) schema.
- Your user account has the following permissions:

  - `view_authenticators`, `create_authenticators`, `edit_authenticators`
  - `view_locations`, `assign_locations`
  - `view_organizations`, `assign_organizations`

**Procedure**

1. On your Satellite Server, enable the Network Information System (NIS) service so that SELinux does not block outgoing LDAP connections:

   ```
   # setsebool -P nis_enabled on
   ```
2. In the Satellite web UI, navigate to **Administer** > **Authentication Sources**.
3. From the **LDAP** menu, select **Create**.
4. On the **LDAP server** tab, enter the details of your LDAP server.

   For TLS encrypted connections, select **LDAPS** to enable encryption.
5. On the **Account** tab, enter the account information and domain name details. For more information, see the following sections:

   - [Section 7.3, “Example settings for LDAP connections”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#Example_Settings_for_LDAP_Connections_authentication "7.3. Example settings for LDAP connections")
   - [Section 7.4, “Example LDAP filters”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#Example_LDAP_Filters_authentication "7.4. Example LDAP filters")
6. On the **Attribute mappings** tab, map LDAP attributes to Satellite attributes.
7. On the **Locations** tab, select the locations you want Satellite to assign to users created from the LDAP authentication source. These locations are available to users after they log in for the first time.
8. On the **Organizations** tab, select the organizations you want Satellite to assign to users created from the LDAP authentication source. These locations are available to users after they log in for the first time.
9. Click **Submit**.

**Next steps**

- If you did not select **Automatically Create Accounts In Satellite** on the **Account** tab, create user accounts manually. For more information, see [Managing users and roles](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Managing_Users_and_Roles_admin) in *Administering Red Hat Satellite*.
- If you selected **Automatically Create Accounts In Satellite**, LDAP users can now log in to Satellite using their LDAP accounts and passwords.
- After users log in for the first time, the Satellite administrator must assign roles to them manually. For more information about assigning appropriate roles to user accounts, see [Assigning roles to a user by using Hammer CLI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#assigning-roles-to-a-user-by-using-cli) in *Administering Red Hat Satellite*.

## 7.3. Example settings for LDAP connections

Examples of settings for LDAP connections show how you can configure the necessary LDAP fields for user accounts from various external authentication sources.

**Example 7.1. Example settings for Active Directory LDAP connections**

This example uses a dedicated service account called *redhat* that has bind, read, and search permissions on the user and group entries.

- **Account Username**: DOMAIN\redhat
- **Account password**: P@ssword
- **Base DN**: DC=example,DC=COM
- **Login name attribute**: userPrincipalName
- **First name attribute**: givenName
- **Last name attribute**: sn
- **Email address attribute**: mail
- **Photo attribute**: thumbnailPhoto

The `userPrincipalName` attribute allows the use of whitespace in usernames. The `sAMAccountName` attribute, which provides backwards compatibility with legacy Microsoft systems, does not allow the use of whitespace in usernames.

**Example 7.2. Example settings for Identity Management LDAP connections**

This example uses a dedicated service account called *redhat* that has bind, read, and search permissions on the user and group entries.

- **Account Username**: uid=redhat,cn=users,cn=accounts,dc=example,dc=com
- **Base DN**: dc=example,dc=com
- **Groups Base DN**: cn=groups,cn=accounts,dc=example,dc=com
- **Login name attribute**: uid
- **First name attribute**: givenName
- **Last name attribute**: sn
- **Email address attribute**: mail

**Example 7.3. Example settings for POSIX LDAP connections**

This example uses a dedicated service account called *redhat* that has bind, read, and search permissions on the user and group entries.

- **Account Username**: uid=redhat,ou=users,dc=example,dc=com
- **Base DN**: dc=example,dc=com
- **Groups Base DN**: cn=employee,ou=userclass,dc=example,dc=com
- **Login name attribute**: uid
- **First name attribute**: givenName
- **Last name attribute**: sn
- **Email address attribute**: mail

## 7.4. Example LDAP filters

Examples of LDAP filters show how you can set up appropriate search filters for connecting your LDAP server as an external authentication source for Satellite.

**Example 7.4. Example LDAP filters for allowing specific users to login**

You are using the following LDAP directory structure:

```
DC=Domain,DC=Example
   |
   |----- CN=Users
         |
         |----- CN=Group1
         |----- CN=Group2
         |----- CN=User1
         |----- CN=User2
         |----- CN=User3
```

Group membership is defined as follows:

- `Group1` includes users `User1` and `User3`
- `Group2` includes users `User2` and `User3`

For example, you can define the following search filters:

| Search result (users) | Filter |
| --- | --- |
| User1 | (distinguishedName=cn=User1,cn=Users,dc=domain,dc=example) |
| User1, User3 | (memberOf=cn=Group1,cn=Users,dc=domain,dc=example) |
| User2, User3 | (memberOf=cn=Group2,cn=Users,dc=domain,dc=example) |
| User1, User2, User3 | (|(memberOf=cn=Group1,cn=Users,dc=domain,dc=example)(memberOf=cn=Group2,cn=Users,dc=domain,dc=example)) |
| User1, User2, User3 | (memberOf:1.2.840.113556.1.4.1941:=cn=Users,dc=domain,dc=example) |

Because group `Users` is a nested group that contains groups `Group1` and `Group2`, the filter must include `memberOf:1.2.840.113556.1.4.1941:=` before the nested group name. This enables you to filter all users from the nested group.
