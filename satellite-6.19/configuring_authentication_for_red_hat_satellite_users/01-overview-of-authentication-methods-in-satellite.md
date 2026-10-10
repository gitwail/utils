---
title: "Overview of authentication methods in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_authentication_for_red_hat_satellite_users"
guide_title: "Configuring authentication for Red Hat Satellite users"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#overview-of-authentication-methods-in-satellite"
---
# Chapter 1. Overview of authentication methods in Satellite

The authentication methods you can configure depend on the authentication source you are using. If the native authentication features provided by Satellite are not sufficient for your use case, use this information to decide which external authentication provider best suits your requirements.

Red Hat Satellite includes native support for authentication with a username and password. If you require additional methods of authentication, configure your Satellite Server to use an external authentication source.

Table 1.1. External authentication sources supported by Satellite and the authentication features they provide

|  | Username and password | Single sign-on (SSO) | One-time password (OTP) | Time-based one-time password (TOTP) | Additional details |
| --- | --- | --- | --- | --- | --- |
| **Active Directory (direct integration)** | Yes | Yes | No | No | [Chapter 6, *Configuring Kerberos SSO for Active Directory users in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-kerberos-sso-for-active-directory-users-in-project_authentication "Chapter 6. Configuring Kerberos SSO for Active Directory users in Satellite") |
| **Identity Management** | Yes (Linux and Active Directory users) | Yes (Linux users only) | No | No | [Chapter 3, *Configuring Kerberos SSO with Identity Management in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-kerberos-sso-with-Identity_Management-in-satellite "Chapter 3. Configuring Kerberos SSO with Identity Management in Satellite") |
| **Red Hat build of Keycloak** | Yes | Yes | Yes | Yes | [Chapter 5, *Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-sso-and-2fa-with-keycloak-in-project_keycloak-quarkus "Chapter 5. Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite") |
| **Red Hat Single Sign-On** | Yes | Yes | Yes | Yes | [Chapter 4, *Configuring SSO and 2FA with Red Hat Single Sign-On in Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-sso-and-2fa-with-keycloak-wildfly-in-project_keycloak-wildfly "Chapter 4. Configuring SSO and 2FA with Red Hat Single Sign-On in Satellite") |
| **LDAP** | Yes | No | No | No | [Chapter 7, *Configuring an LDAP server as an external identity provider for Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-an-ldap-server-as-an-external-identity-provider-for-project_authentication "Chapter 7. Configuring an LDAP server as an external identity provider for Satellite") |
