---
title: "Configuring email notifications"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Configuring_Email_Notifications_admin"
---
# Chapter 10. Configuring email notifications

Email notifications are created by Satellite Server periodically or after completion of certain events. The periodic notifications can be sent daily, weekly or monthly.

Users do not receive any email notifications by default. An administrator can configure users to receive notifications based on criteria such as the type of notification, and frequency.

> **Important**
>
> Satellite Server does not enable outgoing emails by default, therefore you must review your email configuration.

**Additional resources**

- [Configuring Satellite Server for Outgoing Emails in *Installing Satellite Server in a connected network environment*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#Configuring_Server_for_Outgoing_Emails_satellite)

## 10.1. Email notification types

You can configure Satellite to send email notifications for system events such as host builds, errata updates, content synchronization failures, and audit summaries to stay informed about important activities in your environment.

Audit summary
:   A summary of all activity audited by Satellite Server.

Capsule sync failure
:   A notification sent after Capsule synchronization fails.

Compliance policy summary
:   A summary of OpenSCAP policy reports and their results.

Content view promote failure
:   A notification sent after content view promotion fails.

Content view publish failure
:   A notification sent after content view publication fails.

Host built
:   A notification sent after a host is built.

Host errata advisory
:   A summary of applicable and installable errata for hosts managed by the user.

Promote errata
:   A notification sent only after a content view promotion. It contains a summary of errata applicable and installable to hosts registered to the promoted content view. This allows a user to monitor what updates have been applied to which hosts.

Repository sync failure
:   A notification sent after repository synchronization fails.

Sync errata
:   A notification sent only after synchronizing a repository. It contains a summary of new errata introduced by the synchronization.

For a complete list of email notification types, navigate to **Administer** > **Users** in the Satellite web UI, click the **Username** of the required user, and select the **Email Preferences** tab.

## 10.2. Configuring email notification preferences

You can configure Satellite to send email messages to individual users registered to Satellite. Satellite sends the email to the email address that has been added to the account, if present.

Users can edit the email address by clicking on their name in the top right of the Satellite web UI and selecting **My account**.

> **Note**
>
> If you want to send email notifications to a group email address instead of an individual email address, create a user account with the group email address and minimal Satellite permissions, then subscribe the user account to the desired notification types.

**Prerequisites**

- The user you are configuring to receive email notifications has a role with this permission: `view_mail_notifications`.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. Click the **Username** of the user you want to edit.
3. On the **User** tab, verify the value of the **Mail** field. Email notifications will be sent to the address in this field.
4. On the **Email Preferences** tab, select **Mail Enabled**.
5. Select the notifications you want the user to receive using the drop-down menus next to the notification types.

   > **Note**
   >
   > The **Audit Summary** notification can be filtered by entering the required query in the **Mail Query** text box.
6. Click **Submit**.

   The user will start receiving the notification emails.

## 10.3. Testing email delivery

To verify the delivery of emails, send a test email to a user. If the email gets delivered, the settings are correct.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Users**.
2. Click on the username.
3. On the **Email Preferences** tab, click **Test email**.

   A test email message is sent immediately to the user’s email address.

**Verification**

- If the email is delivered, the verification is complete.

**Troubleshooting**

- If the email is not delivered, perform the following diagnostic steps:

  1. Verify the user’s email address.
  2. Verify Satellite Server’s email configuration.
  3. Examine firewall and mail server logs.
  4. If your Satellite Server uses the Postfix service for email delivery, the test email might be held in the queue. To verify, enter the `mailq` command to list the current mail queue. If the test email is held in the queue, `mailq` displays the following message:

     ```
     postqueue: warning: Mail system is down -- accessing queue directly
     -Queue ID-  --Size-- ----Arrival Time---- -Sender/Recipient-------
     BE68482A783    1922 Thu Oct  3 05:13:36  satellite-noreply@example.com
     ```

     To fix the problem, start the Postfix service on your Satellite Server:

     ```
     # systemctl start postfix
     ```

## 10.4. Testing email notifications

To verify that users are correctly subscribed to notifications, trigger the notifications manually.

This triggers all notifications scheduled for the specified frequency for all subscribed users. If every subscribed user receives the notifications, the verification succeeds.

> **Note**
>
> Sending manually triggered notifications to individual users is currently not supported.

**Procedure**

- Trigger email notifications:

  ```
  # foreman-rake reports:_My_Frequency_
  ```

  Replace *My_Frequency* with one of the following:
- daily
- weekly
- monthly

## 10.5. Changing email notification settings for a host

You can enable or disable email notifications for a host to control whether its events trigger alerts. Satellite sends these notifications to the registered owner of the host.

You can configure Satellite to send email notifications either to an individual user or a user group. When set to a user group, all group members who are subscribed to the email type receive a message.

Receiving email notifications for a host can be useful, but also overwhelming if you are expecting to receive frequent errors, for example, because of a known issue or error you are working around.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**, locate the host that you want to view, and click **Edit** in the **Actions** column.
2. Go to the **Additional Information** tab. If the **Enabled** checkbox is checked, then email notifications are enabled on that host.
3. Optional: Toggle the checkbox to enable or disable the email notifications.

   > **Note**
   >
   > If you want to receive email notifications, ensure that you have an email address set in your user settings.
