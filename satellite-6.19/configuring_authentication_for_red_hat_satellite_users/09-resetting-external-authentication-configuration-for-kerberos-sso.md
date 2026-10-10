---
title: "Resetting external authentication configuration for Kerberos SSO"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_authentication_for_red_hat_satellite_users"
guide_title: "Configuring authentication for Red Hat Satellite users"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#resetting-external-authentication-configuration-for-kerberos-sso"
---
# Chapter 9. Resetting external authentication configuration for Kerberos SSO

You can disable external authentication with Identity Management or Active Directory (AD) by resetting the configuration for the `IPA` authentication type. This prevents user accounts defined in the external authentication source from accessing Satellite.

> **Important**
>
> Resetting external authentication prevents users from accessing Satellite with Kerberos single sign-on (SSO). However, some configuration files, such as configuration files for the System Security Services Daemon (SSSD), will remain modified because Satellite does not have access to the previous state of these files.

**Procedure**

- Reset the external authentication configuration to the default state:

  - To disable access to Satellite web UI:

    ```
    # satellite-installer --reset-foreman-ipa-authentication
    ```
  - To disable access to Satellite web UI, Satellite API, and Hammer CLI:

    ```
    # satellite-installer --reset-foreman-ipa-authentication-api
    ```

**Verification**

- Display the value for the `foreman-ipa-authentication` and `foreman-ipa-authentication-api` configuration options:

  ```
  # satellite-installer --help | grep foreman-ipa-authentication
  ```

  The expected value for disabled external authentication is `false`.
