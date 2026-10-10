---
title: "Security settings for provisioning"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#security-settings-for-provisioning"
---
# Chapter 6. Security settings for provisioning

Configure global security settings to secure your provisioning environment. You can set default encrypted root passwords for newly provisioned hosts, configure security token validity, and provision FIPS-compliant hosts.

**Additional resources**

- [Provisioning settings in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#host-provisioning-settings)

## 6.1. Configuring the security token validity duration

You can change the validity duration of the unique security token that Satellite generates for provisioning. By default, the token is valid for 360 minutes, and the host must reboot within this time frame.

If the token expires, you receive a 404 error and the operating system installer download fails.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**, and click the **Provisioning** tab.
2. Find the **Token duration** option and click the edit icon and edit the duration, or enter `0` to disable token generation. If token generation is disabled, an attacker can spoof client IP address and download kickstart from Satellite Server, including the encrypted root password.

## 6.2. Setting a default encrypted root password for hosts

If you do not want to set a plain text default root password for the hosts that you provision, you can use a default encrypted password.

The default root password can be inherited by a host group and consequentially by hosts in that group.

If you change the password and reprovision the hosts in the group that inherits the password, the password will be overwritten on the hosts.

**Procedure**

1. Generate an encrypted password:

   ```
   $ python3 -c 'import crypt,getpass;pw=getpass.getpass(); print(crypt.crypt(pw)) if (pw==getpass.getpass("Confirm: ")) else exit()'
   ```

   Copy the password for later use.
2. In the Satellite web UI, navigate to **Administer** > **Settings**.
3. On the **Settings** page, select the **Provisioning** tab.
4. In the **Name** column, navigate to **Root password**, and click **Click to edit**.
5. Paste the encrypted password, and click **Save**.

## 6.3. Provisioning FIPS-compliant hosts

You can provision hosts that comply with the National Institute of Standards and Technology’s Security Requirements for Cryptographic Modules standard, reference number FIPS 140-2, referred to here as FIPS.

### 6.3.1. Changing the provisioning password hashing algorithm

To provision FIPS-compliant hosts, you must first set the password hashing algorithm that you use in provisioning to SHA256. This configuration setting must be applied for each operating system you want to deploy as FIPS-compliant.

**Procedure**

1. Get a list of operating systems:

   ```
   $ hammer os list
   ```
2. Update each the password hash value of your operating system:

   ```
   $ hammer os update \
   --password-hash SHA256
   --title "My_Operating_System"
   ```

   Note that you cannot use a comma-separated list of values.

### 6.3.2. Setting the FIPS-enabled parameter

To provision a FIPS-compliant host, you must create a host group and set the host group parameter `fips_enabled` to `true`. If this is not set to `true`, or is absent, the FIPS-specific changes do not apply to the system.

You can set this parameter when you provision a host or for a host group.

**Procedure**

- Set the parameter when provisioning a host through a host group:

  ```
  $ hammer hostgroup set-parameter \
  --hostgroup "My_Host_Group" \
  --name fips_enabled \
  --value "true"
  ```

  For more information, see the output of the command `hammer hostgroup set-parameter --help`.

### 6.3.3. Verifying FIPS mode is enabled

To verify these FIPS compliance changes have been successful, you must provision a host and check its configuration.

**Procedure**

1. Log in to the host as `root` or with an admin-level account.
2. Enter the following command:

   ```
   $ cat /proc/sys/crypto/fips_enabled
   ```

   A value of `1` confirms that FIPS mode is enabled.
