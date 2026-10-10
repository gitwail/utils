---
title: "Accessing Red Hat Satellite from Satellite web UI"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_authentication_for_red_hat_satellite_users"
guide_title: "Configuring authentication for Red Hat Satellite users"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#accessing-satellite-from-web-ui"
---
# Chapter 2. Accessing Red Hat Satellite from Satellite web UI

After Red Hat Satellite has been installed and configured, you can use a browser to log in to the Satellite web UI.

## 2.1. Logging in to the Satellite web UI

The Satellite web UI is a browser-based user interface that you can use to manage and monitor your Satellite infrastructure. To access Satellite web UI, use your web browser to navigate to the Satellite web UI login page and enter your credentials.

**Prerequisites**

- Ensure that the Katello root CA certificate is installed in your browser. For more information, see [Section 2.2, “Importing the Katello root CA certificate by using browser”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#importing-the-katello-root-ca-certificate-by-using-browser "2.2. Importing the Katello root CA certificate by using browser").

**Procedure**

1. Access Satellite Server using a web browser pointed to the fully qualified domain name:

   ```
   https://satellite.example.com/
   ```
2. Enter the user name and password created during the configuration process. If a user was not created during the configuration process, the default user name is *admin*.

**Next steps**

- If you have problems logging in, you can reset the password. For more information, see [Section 2.4, “Resetting the administrative user password”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#Resetting_the_Administrative_User_Password_authentication "2.4. Resetting the administrative user password").

## 2.2. Importing the Katello root CA certificate by using browser

After the first login to Satellite web UI, you might see a warning that you are using the default self-signed certificate. To ensure a successful connection, locate the root CA certificate on Satellite and import it into your browser truststore.

**Prerequisites**

- Your Red Hat Satellite is installed and configured.

**Procedure**

1. Identify the fully qualified domain name of your Satellite Server:

   ```
   # hostname -f
   ```
2. Access the `pub` directory on your Satellite Server using a web browser pointed to the fully qualified domain name:

   ```
   https://satellite.example.com/pub
   ```
3. When you access Satellite for the first time, an untrusted connection warning displays in your web browser. Accept the self-signed certificate and add the Satellite URL as a security exception to override the settings. This procedure might differ depending on the browser being used. Ensure that the Satellite URL is valid before you accept the security exception.
4. Select `katello-server-ca.crt`.
5. Import the certificate into your browser as a certificate authority and trust it to identify websites.

## 2.3. Importing the Katello root CA certificate by using command line

After the first login to Satellite web UI, you might see a warning that you are using the default self-signed certificate. To ensure a successful connection, locate the root CA certificate on Satellite and import it into your browser truststore.

**Prerequisites**

- Your Red Hat Satellite is installed and configured.

**Procedure**

1. On your Satellite Server, copy the `katello-server-ca.crt` file to the machine you use to access the Satellite web UI:

   ```
   # scp /var/www/html/pub/katello-server-ca.crt username@hostname:remotefile
   ```
2. In the browser, import the `katello-server-ca.crt` certificate as a certificate authority and trust it to identify websites.

## 2.4. Resetting the administrative user password

You can reset the administrative password to randomly generated characters or set a new administrative password for a specific user. This might be useful when you forget the password, when the administrative user is deleted, or for assigning administrative privileges to a user.

**Procedure**

1. Log in to the base operating system where your Satellite Server is installed.
2. Reset the administrative user password:

   - To set a randomly generated administrative user password:

     ```
     # foreman-rake permissions:reset
     Reset to user: admin, password: qwJxBptxb7Gfcjj5
     ```
   - To set a new administrative user password:

     ```
     # foreman-rake permissions:reset username=My_User_Name password=My_New_Password
     ```

     Replace `My_User_Name` with the username of the user whose password you want to reset.

     > **Note**
     >
     > Be aware of the following behaviors:
     >
     > - If you enter a username that does not exist, the `foreman-rake` utility creates a new administrative user with the defined password.
     > - If you enter a username of a user without administrative privileges, that user gains administrative privileges.
     > - If you do not enter a username, the password resets for the `admin` user by default.
3. To use the new password with the Hammer CLI, add the password and username to the `~/.hammer/cli.modules.d/foreman.yml` file on your Satellite Server:

   ```
   # vi ~/.hammer/cli.modules.d/foreman.yml
   ```

**Verification**

- Use the new password to log in to the Satellite web UI.

## 2.5. Setting a custom message on the Satellite web UI login page

You can change the default text on the login page to a custom message you want your users to see every time they access the page. For example, your custom message might be a warning required by your company.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. Select the **General** tab.
3. Enter your custom message in the **Login page footer text** field.
4. Click **Submit**.

**Verification**

- Log out of the Satellite web UI and verify that the custom message is now displayed on the login page.
