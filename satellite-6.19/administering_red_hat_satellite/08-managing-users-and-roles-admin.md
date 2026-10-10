---
title: "Managing users and roles"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Managing_Users_and_Roles_admin"
---
# Chapter 8. Managing users and roles

Satellite users represent individuals who access your Satellite and are scoped to organizations and locations. You assign roles to users to control which actions they can perform in your environment.

## 8.1. Managing Satellite users

As an administrator, you can create, modify and remove Satellite users. You can also configure access permissions for a user or a group of users by assigning them different roles.

### 8.1.1. Creating a user by using Satellite web UI

Create user accounts from the Satellite web UI to grant individuals access to your Satellite environment.

Users are strictly confined to their assigned organizations and locations. Users can only access and assign resources within the organizations and locations they belong to.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. Click **Create User**.
3. Enter the account details for the new user.
4. Click **Submit** to create the user.

   The user account details that you can specify include the following:

   - On the **User** tab, select an authentication source from the **Authorized by** list:

     - **INTERNAL**: to manage the user inside Satellite Server.
     - **EXTERNAL**: to manage the user with external authentication. For more information, see [*Configuring authentication for Red Hat Satellite users*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#).
   - On the **Organizations** tab, select organizations for the user. Select the default organization from the **Default on login** list. Satellite uses this organization for the user after login.
   - On the **Locations** tab, select locations for the user. Select the default location from the **Default on login** list. Satellite uses this location for the user after login.

### 8.1.2. Creating a user by using Hammer CLI

Create user accounts by using Hammer CLI to grant individuals access to your Satellite environment.

Users are strictly confined to their assigned organizations and locations. Users can only access and assign resources within the organizations and locations they belong to.

**Procedure**

- Create a user:

  ```
  $ hammer user create \
  --auth-source-id My_Authentication_Source \
  --login My_User_Name \
  --mail My_User_Mail \
  --organization-ids My_Organization_ID_1,My_Organization_ID_2 \
  --location-ids My_Location_ID_1,My_Location_ID_2 \
  --password My_User_Password
  ```

  Append `--auth-source-id 1` so that the user is authenticated internally. Run `hammer auth-source list` to get a list of authentication sources. Add the `--admin` option to grant administrator privileges to the user.

  You can modify the user details later by using the `hammer user update` command.

### 8.1.3. Assigning roles to a user by using Satellite web UI

Assign roles to a user in the Satellite web UI to control which permissions and resources they can access in your environment.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. Click the **username** of the user to be assigned one or more roles.

   > **Note**
   >
   > If a user account is not listed, check that you are currently viewing the correct organization. To list all the users in Satellite, click **Default Organization** and then **Any Organization**.
3. Click the **Locations** tab, and select a location if none is assigned.
4. Click the **Organizations** tab, and check that an organization is assigned.
5. Click the **Roles** tab to display the list of available roles.
6. Select the roles to assign from the **Roles** list.

   To grant all the available permissions, select the **Administrator** checkbox.
7. Click **Submit**.

   To view the roles assigned to a user, click the **Roles** tab; the assigned roles are listed under **Selected items**. To remove an assigned role, click the role name in **Selected items**.

### 8.1.4. Assigning roles to a user by using Hammer CLI

Assign roles to a user with Hammer CLI to grant the permissions they need to perform tasks in Satellite.

**Procedure**

- Assign roles to a user:

  ```
  $ hammer user add-role \
  --id My_User_ID \
  --role My_Role_Name
  ```

### 8.1.5. Impersonating a different user account

As an administrator, you can impersonate another user by logging on to the Satellite web UI as that user. Impersonating another user is useful for testing and troubleshooting purposes because you can access exactly what the impersonated user can access in the system, including the same menus.

Audits are created to record the actions that the administrator performs while impersonating another user. However, all actions that an administrator performs while impersonating another user are recorded as having been performed by the impersonated user.

**Prerequisites**

- You are logged on to the Satellite web UI as a user with administrator privileges for Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. To the right of the user that you want to impersonate, from the list in the **Actions** column, select **Impersonate**.

   When you want to stop the impersonation session, in the upper right of the main menu, click the impersonation icon.

### 8.1.6. Creating an API-only user

You can create a user account that can interact only with the Satellite API. This is useful for service accounts or integrations that must not use the Satellite web UI.

**Prerequisites**

- You have created a user and assigned roles to them. Note that this user must be authorized internally. For more information, see [Chapter 8, *Managing users and roles*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Managing_Users_and_Roles_admin "Chapter 8. Managing users and roles").

**Procedure**

1. Log in to your Satellite as admin.
2. Navigate to **Administer** > **Users** and select a user.
3. On the **User** tab, set a password. Do not save or communicate this password with others. You can create pseudo-random strings on your console:

   ```
   # openssl rand -hex 32
   ```
4. Create a Personal Access Token for the user. For more information, see [Section 8.3.1, “Creating a Personal Access Token”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#creating-a-personal-access-token_admin "8.3.1. Creating a Personal Access Token").

## 8.2. Managing SSH keys

Add SSH keys to user accounts so Satellite can deploy those keys during host provisioning.

**Additional resources**

- [Deploying SSH keys during provisioning in *Provisioning hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#deploying-ssh-keys-during-provisioning)
- [Using secure communications between two systems with OpenSSH in *Red Hat Enterprise Linux 9 Configuring basic system settings*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_basic_system_settings/index#assembly_using-secure-communications-between-two-systems-with-openssh_configuring-basic-system-settings)

### 8.2.1. Managing SSH keys for a user by using Satellite web UI

Add or remove SSH keys for a user in the Satellite web UI to control which keys Satellite deploys during provisioning.

**Prerequisites**

- You are logged in to the Satellite web UI as an Admin user of Red Hat Satellite or a user with the `create_ssh_key` permission enabled for adding SSH key and `destroy_ssh_key` permission for removing a key.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. From the **Username** column, click on the username of the required user.
3. Click on the **SSH Keys** tab.

   - To Add SSH key

     1. Prepare the content of the public SSH key in a clipboard.
     2. Click **Add SSH Key**.
     3. In the **Key** field, paste the public SSH key content from the clipboard.
     4. In the **Name** field, enter a name for the SSH key.
     5. Click **Submit**.
   - To Remove SSH key

     1. Click **Delete** on the row of the SSH key to be deleted.
     2. Click **OK** in the confirmation prompt.

### 8.2.2. Managing SSH keys for a user by using Hammer CLI

Add or remove SSH keys for a user with Hammer CLI to manage which keys Satellite deploys during provisioning.

**Prerequisites**

- You are logged in to the Satellite web UI as an Admin user of Red Hat Satellite or a user with the `create_ssh_key` permission enabled for adding SSH key and `destroy_ssh_key` permission for removing a key.

**Procedure**

1. To add an SSH key to a user, you must specify either the path to the public SSH key file, or the content of the public SSH key copied to the clipboard:

   - If you have the public SSH key file, enter the following command:

     ```
     $ hammer user ssh-keys add \
     --user-id user_id \
     --name key_name \
     --key-file ~/.ssh/id_rsa.pub
     ```
   - If you have the content of the public SSH key, enter the following command:

     ```
     $ hammer user ssh-keys add \
     --user-id user_id \
     --name key_name \
     --key ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNtYAAABBBHHS2KmNyIYa27Qaa7EHp+2l99ucGStx4P77e03ZvE3yVRJEFikpoP3MJtYYfIe8k 1/46MTIZo9CPTX4CYUHeN8= host@user
     ```
2. To delete an SSH key from a user, enter the following command:

   ```
   $ hammer user ssh-keys delete --id key_id --user-id user_id
   ```
3. To view an SSH key attached to a user, enter the following command:

   ```
   $ hammer user ssh-keys info --id key_id --user-id user_id
   ```
4. To list SSH keys attached to a user, enter the following command:

   ```
   $ hammer user ssh-keys list --user-id user_id
   ```

## 8.3. Managing Personal Access Tokens

Personal Access Tokens allow you to authenticate API requests without using your password. You can set an expiration date for your Personal Access Token and you can revoke it if you decide it should expire before the expiration date.

### 8.3.1. Creating a Personal Access Token

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

### 8.3.2. Revoking a Personal Access Token

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

## 8.4. Creating and managing user groups

You can manage permissions of several users at once by organizing them into user groups. User groups themselves can be further grouped to create a hierarchy of permissions.

With Satellite, you can assign permissions to groups of users. You can also create user groups as collections of other user groups. If you use an external authentication source, you can map Satellite user groups to external user groups.

User groups are defined in an organizational context, meaning that you must select an organization before you can access user groups.

**Additional resources**

- [Managing external user groups in *Configuring authentication for Red Hat Satellite users*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#managing-external-user-groups)

### 8.4.1. Creating a user group by using Satellite web UI

Create a user group in the Satellite web UI and define which roles the group will have.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **User Groups**.
2. Click **Create User group**.
3. On the **User Group** tab, specify the name of the new user group and select group members:

   - Select the previously created user groups from the **User Groups** list.
   - Select users from the **Users** list.
4. On the **Roles** tab, select the roles you want to assign to the user group. Alternatively, select the **Admin** checkbox to assign all available permissions.
5. Click **Submit**.

### 8.4.2. Creating a user group by using Hammer CLI

Create a user group by using Hammer CLI and define which roles the group will have.

**Procedure**

- Create a user group:

  ```
  $ hammer user-group create \
  --name My_User_Group_Name \
  --role-ids My_Role_ID_1,My_Role_ID_2 \
  --user-ids My_User_ID_1,My_User_ID_2
  ```

### 8.4.3. Removing a user group

Remove a user group from Satellite when you no longer need it or when you want to reorganize how permissions are assigned.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **User Groups**.
2. Click **Delete** to the right of the user group you want to delete.
3. Click **Confirm** to delete the user group.
