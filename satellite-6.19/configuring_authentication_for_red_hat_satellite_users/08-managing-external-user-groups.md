---
title: "Managing external user groups"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_authentication_for_red_hat_satellite_users"
guide_title: "Configuring authentication for Red Hat Satellite users"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#managing-external-user-groups"
---
# Chapter 8. Managing external user groups

When using external authentication sources, such as Identity Management or Active Directory, you can configure group membership to control user access and permissions in Satellite. You might need to take extra configuration steps to manage group membership for user accounts defined in external authentication sources.

> **Note**
>
> External user groups based on Identity Management or AD are refreshed only when a group member logs in to Satellite. It is not possible to alter user membership of external user groups in the Satellite web UI, such changes are overwritten on the next group refresh.

## 8.1. Associating external users with user groups

Satellite does not associate external users with their user group automatically. To associate these external users with their user group, you must create the user group on your Satellite Server.

When you create a Satellite user group with the same name as in the external source, members of the external user group automatically become members of the Satellite user group and receive the associated permissions. The configuration of external user groups depends on the type of external authentication.

To assign additional permissions to an external user, add this user to an internal user group that has no external mapping specified. Then assign the required roles to this group.

**Prerequisites**

- If you use an LDAP server, configure Satellite to use LDAP authentication. For more information, see [Chapter 7, *Configuring an LDAP server as an external identity provider for Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#configuring-an-ldap-server-as-an-external-identity-provider-for-project_authentication "Chapter 7. Configuring an LDAP server as an external identity provider for Satellite").

  When using external user groups from an LDAP source, you cannot use the `$login` variable as a substitute for the account user name. You must use either an anonymous or dedicated service user.
- If you use a Identity Management or AD server, configure Satellite to use Identity Management or AD authentication. For more information, see [*Configuring authentication for Red Hat Satellite users*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#).
- Ensure that at least one external user authenticates for the first time.
- Retain a copy of the external group names you want to use. You can find the group membership of external users:

  ```
  # id username
  ```

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **User Groups**, and click **Create User Group**.
2. Specify the name of the new user group. Do not select any users to avoid adding users automatically when you refresh the external user group.
3. Click the **Roles** tab and select the roles you want to assign to the user group. Alternatively, select the **Administrator** checkbox to assign all available permissions.
4. Click the **External groups** tab, then click **Add external user group**, and select an authentication source from the **Auth source** drop-down menu.

   Specify the exact name of the external group in the **Name** field.
5. Click **Submit**.

## 8.2. Refreshing external user groups for LDAP using CLI

You can refresh external user groups manually. This is useful if you want to immediately update membership changes from your LDAP source.

To set the LDAP source to synchronize user group membership automatically on user login, in the **Auth Source** page, select the **Usergroup Sync** option. If this option is not selected, LDAP user groups are refreshed automatically through a scheduled cron job synchronizing the LDAP Authentication source every 30 minutes by default.

If the user groups in the LDAP Authentication source change in the lapse of time between scheduled tasks, the user can be assigned to incorrect external user groups. This is corrected automatically when the scheduled task runs.

**Procedure**

- On your Satellite Server, refresh your LDAP source:

  ```
  # foreman-rake ldap:refresh_usergroups
  ```

## 8.3. Refreshing external user groups for LDAP using Satellite web UI

You can refresh external user groups manually. This is useful if you want to immediately update membership changes from your LDAP source.

To set the LDAP source to synchronize user group membership automatically on user login, in the **Auth Source** page, select the **Usergroup Sync** option. If this option is not selected, LDAP user groups are refreshed automatically through a scheduled cron job synchronizing the LDAP Authentication source every 30 minutes by default.

If the user groups in the LDAP Authentication source change in the lapse of time between scheduled tasks, the user can be assigned to incorrect external user groups. This is corrected automatically when the scheduled task runs.

Use this procedure to refresh the LDAP source manually.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Usergroups** and select a user group.
2. On the **External Groups** tab, click **Refresh** to the right of the required user group.
