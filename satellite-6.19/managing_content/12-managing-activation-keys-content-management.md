---
title: "Managing activation keys"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "12"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management"
---
# Chapter 12. Managing activation keys

Activation keys automate host configuration during registration to Satellite by assigning content view environments, enabling repositories, and defining system purpose. Create and configure your activation keys to scale consistent content access across many hosts.

You can use activation keys during host registration to improve the speed, simplicity and consistency of the process. Note that activation keys are used only when hosts are registered. If changes are made to an activation key, it is applicable only to hosts that are registered with the amended activation key in the future. The changes are not made to existing hosts.

Activation keys can define the following properties for hosts:

- Available products and repositories
- Content view environments
- Host collection membership
- System purpose

  Content view conflicts between host creation and registration
  :   When you provision a host, Satellite uses provisioning templates and other content from the content view that you set in the host group or host settings. When the host is registered, the content view environments from the activation key overwrite the original content view from the host group or host settings. Then Satellite uses the content view environments from the activation key for every future task, for example, rebuilding a host.

      When you rebuild a host, ensure that you set the content view that you want to use in the activation key and not in the host group or host settings.

  Using multiple activation keys with a host
  :   A host can be associated with multiple activation keys that are combined to define the host settings. In case of conflicting settings, the last specified activation key takes precedence. You can specify the order of precedence by setting a host group parameter as follows:

      ```
      $ hammer hostgroup set-parameter \
      --hostgroup "My_Host_Group" \
      --name "My_Activation_Key" \
      --value "name_of_first_key", "name_of_second_key", ...
      ```

## 12.1. Best practices for activation keys

Plan dedicated activation keys per use case, use descriptive names, and automate key management with Hammer or Ansible to keep host content modular and consistent.

- Create an activation key for each use case. This structures, modularizes, and simplifies content management on hosts.
- Use a naming convention for activation keys to indicate the content and lifecycle environment, for example, `red-hat-enterprise-linux-webserver`.
- Automate activation key management by using a Hammer script or an [Ansible Playbook](https://theforeman.github.io/foreman-ansible-modules/develop/index.html).

## 12.2. Creating an activation key by using Satellite web UI

Create an activation key and associate content view environments, system purpose, and repository overrides for host registration.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Activation Keys**.
2. Click **Create Activation Key**.
3. In the **Name** field, enter the name of the activation key.
4. If you want to set a limit, clear the **Unlimited hosts** checkbox, and in the **Limit** field, enter the maximum number of systems you can register with the activation key. If you want unlimited hosts to register with the activation key, ensure the **Unlimited Hosts** checkbox is selected.
5. Optional: In the **Description** field, enter a description for the activation key.
6. On the **Content view environments** card, click **Assign content view environments**.
7. Select a lifecycle environment.
8. Select a content view.
9. Optional: Click **Assign another content view environment** to assign additional content view environments to the activation key.
10. Optional: Drag and drop the content view environments to change the order of the content view environments.
11. Click **Save** to save the content view environments.
12. Click **Save** to save the activation key.
13. Optional: In the **System Purpose** section, you can configure the activation key to set system purpose attributes on hosts during registration. This helps determine which repositories are available on the host. It also helps with reporting in the Subscriptions service of the Red Hat Hybrid Cloud Console.
14. On the **Repository Sets** tab, override repositories to Enabled or Disabled as desired. For more information, see [Section 12.6, “Enabling and disabling repositories on activation key”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-and-disabling-repositories-on-activation-key_content-management "12.6. Enabling and disabling repositories on activation key").
15. Optional: On the **Host Collections** tab, click **Add** to view a list of available host collections. Select your host collection and click **Add Selected**. This ensures that hosts become part of your host collection during the host registration process.

## 12.3. Creating an activation key by using Hammer CLI

Create an activation key and associate content view environments, system purpose, and repository overrides for host registration.

**Procedure**

1. Create the activation key:

   ```
   $ hammer activation-key create \
   --name "My_Activation_Key" \
   --unlimited-hosts \
   --description "Example Stack in the Development Environment" \
   --content-view-environments "Development/Stack" \
   --organization "My_Organization"
   ```
2. Optional: Configure the activation key with system purpose attributes to set on hosts during registration. This helps determine which repositories are available on the host. It also helps with reporting in the Subscriptions service of the Red Hat Hybrid Cloud Console.

   ```
   $ hammer activation-key update \
   --organization "My_Organization" \
   --name "My_Activation_Key" \
   --service-level "Standard" \
   --purpose-usage "Development/Test" \
   --purpose-role "Red Hat Enterprise Linux Server"
   ```
3. List the product content associated with the activation key:

   ```
   $ hammer activation-key product-content \
   --content-access-mode-all true \
   --name "My_Activation_Key" \
   --organization "My_Organization"
   ```
4. Override the default auto-enable status for the Red Hat Satellite Client 6 repository:

   ```
   $ hammer activation-key content-override \
   --name "My_Activation_Key" \
   --content-label "My_Content_Label" \
   --value 1 \
   --organization "My_Organization"
   ```

   For a custom repository, the content label consists of your organization label, product label, and repository label split by underscores. For example, `Example_Satellite_Client_Red_Hat_Enterprise_Linux_9`. For content from Red Hat, the content label is taken from the Red Hat manifest. For example, `rhel-10-for-x86_64-baseos-rpms`.

   The default status is set to disabled.
5. Optional: Assign a host collection to your activation key:

   ```
   $ hammer activation-key add-host-collection \
   --host-collection-id My_Host_Collection_ID \ --id _My_Activation_Key_ID \ --organization-id _My_Organization_ID
   ```

   This ensures that hosts become part of your host collection during the host registration process.

## 12.4. Setting the service level by using Satellite web UI

Configure an activation key to set the default subscription service level that hosts inherit when they register with the activation key.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Activation Keys**.
2. Click the activation key name you want to edit.
3. Click the edit icon next to **Service Level**.
4. Select the required service level from the list. The list only contains service levels available to the activation key.
5. Click **Save**.

## 12.5. Setting the service level by using Hammer CLI

Configure an activation key to set the default subscription service level that hosts inherit when they register with the activation key.

**Procedure**

- Set the service level to Premium on your activation key:

  ```
  $ hammer activation-key update \
  --name "My_Activation_Key" \
  --organization "My_Organization" \
  --service-level premium
  ```

## 12.6. Enabling and disabling repositories on activation key

Override repository set status on an activation key to control which repositories are enabled when hosts register with the activation key.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Activation Keys**.
2. Select an activation key.
3. Select the **Repository Sets** tab.
4. Optional: Clear the **Limit to Environment** checkbox to view repositories that are available in the lifecycle environment of the activation key.
5. Optional: Use the **Repository type** dropdown menu to filter repositories by type.
6. Optional: Use the **Status** dropdown menu to filter repositories by status.
7. Select the desired repositories or click the **Select All** checkbox to select all repositories.
8. From the **Select Action** list, select **Override to Enabled**, **Override to Disabled**, or **Reset to Default**.

## 12.7. Activation keys and host registration

Use activation keys during provisioning or when registering existing Red Hat Enterprise Linux hosts to apply subscription and content settings automatically.

> **Note**
>
> The `Kickstart` provisioning templates in Satellite contain commands to register the host, using an activation key that is defined when creating a host.

You can use multiple activation keys when registering a host. For example, you can use one activation key to enable specific repositories and another to assign content view environments.

If there are conflicting settings in activation keys, the rightmost key takes precedence.

- Settings that conflict: **Service Level**, **Release Version**, **Environment**, **Content View**, and **Product Content**.
- Settings that do not conflict and the host gets the union of them: **Host Collections**.
- Settings that influence the behavior of the key itself and not the host configuration: **Content Host Limit**.

**Additional resources**

- [Registering hosts to Satellite in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite)

## 12.8. Multiple activation keys and content view environments

When you register a host with multiple activation keys, Satellite merges their settings and resolves conflicts by key order and the **Allow multiple content views** setting.

When multiple activation keys assign the same attributes, Satellite decides how to resolve conflicts. In general, the host receives the union of non-conflicting settings and the setting from the last activation key for conflicting settings.

Conflicting settings, where the setting from the last activation key wins, include:

- System purpose attributes
- Release version

Non-conflicting settings, where the host receives the union of them, include:

- Host collections

Activation key behavior regarding multiple content view environments depends on the **Allow multiple content views** setting. If you enable **Allow multiple content views**, content view environments are treated as non-conflicting. If you disable **Allow multiple content views**, content view environments are considered conflicting.

When you enable **Allow multiple content views** and register a host with multiple activation keys, the host receives all content view environments from each activation key, in the order they are passed.

**Example 12.1. Example with Allow multiple content views enabled**

Assuming that:

- Activation key `ak_multi` assigns content view environments `dev/cv2`, `dev/cv3`.
- Activation key `ak4` assigns content view environments `dev/cv4`.

A host registered with activation keys `ak_multi` and `ak4` receives content view environments `dev/cv2`, `dev/cv3`, and `dev/cv4`.

If the order is reversed, with `ak4` followed by `ak_multi`, the host receives content view environments `dev/cv4`, `dev/cv2`, and `dev/cv3`.

When you disable **Allow multiple content views** and register a host with multiple activation keys, the host receives the content view environments from the last activation key with any content view environments. If any of the activation keys is a multi-environment activation key, registration fails with an error, regardless of the order.

**Example 12.2. Example with Allow multiple content views disabled**

Assuming that:

- Activation key `ak_multi` assigns content view environments `dev/cv2`, `dev/cv3`.
- Activation key `ak4` assigns content view environment `dev/cv4`.
- Activation key `ak5` assigns content view environment `dev/cv5`.
- Activation key `ak_none` assigns no content view environments.

If you attempt to register a host with activation keys `ak_multi`, `ak4`, registration fails because `ak_multi` is a multi-environment activation key.

If you register a host with activation keys `ak4`, `ak5`, the host receives `dev/cv5`, as `ak5` is the last activation key with content view environments.

If you register a host with activation keys `ak4`, `ak5`, `ak_none`, the host receives `dev/cv5` because `ak5` is the last activation key with content view environments.

If you register a host with activation keys `ak5`, `ak4`, the host receives `dev/cv4`, as `ak4` is the last activation key with content view environments.

## 12.9. Assigning content view environments to an activation key by using Satellite web UI

Assign content view environments to an activation key so registered hosts receive content from the content view environments you specify, in the order you define.

**Prerequisites**

- If you want to assign multiple content view environments, the **Allow multiple content views** setting must be enabled. For more information, see [Section 9.8.1, “Content view environments overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environments-overview "9.8.1. Content view environments overview").
- You have created an activation key.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Activation Keys**.
2. Click the name of the activation key to which you want to assign content view environments.
3. On the the **Content view environments** card, click **Assign content view environments**.
4. Select a lifecycle environment.
5. Select a content view.
6. Optional: Click **Assign another content view environment** to assign additional content view environments to the activation key.
7. Optional: Drag and drop the content view environments to change the order of the content view environments.
8. Click **Save**.

**Verification**

- The **Details** tab of the activation key displays the assigned content view environments in order.

**Additional resources**

- [Section 12.8, “Multiple activation keys and content view environments”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#multiple-activation-keys-and-content-view-environments "12.8. Multiple activation keys and content view environments")

## 12.10. Assigning content view environments to an activation key by using Hammer CLI

Assign content view environments to an activation key so registered hosts receive content from the content view environments you specify, in the order you define.

**Prerequisites**

- If you want to assign multiple content view environments, the **Allow multiple content views** setting must be enabled. For more information, see [Section 9.8.1, “Content view environments overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-view-environments-overview "9.8.1. Content view environments overview").
- You have created an activation key.

**Procedure**

1. Display the available content view environments to obtain their labels or IDs:

   ```
   $ hammer content-view-environment list
   ```
2. Assign content view environments to an activation key:

   - By using their labels:

     ```
     $ hammer activation-key update \
     --id My_Activation_Key_ID \
     --organization-id My_Organization_ID \
     --content-view-environments "My_env1/My_cv1,My_env2/My_cv2"
     ```
   - By using their IDs:

     ```
     $ hammer activation-key update \
     --id My_Activation_Key_ID \
     --organization-id My_Organization_ID \
     --content-view-environment-ids [My_content_view_env_ID_1, My_content_view_env_ID_2]
     ```

**Additional resources**

- [Section 12.8, “Multiple activation keys and content view environments”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#multiple-activation-keys-and-content-view-environments "12.8. Multiple activation keys and content view environments")

## 12.11. Removing all content view environments from an activation key

Remove all content view environments from an activation key when you need to clear assignments before reconfiguring the activation key.

**Procedure**

- Remove all content view environments from the activation key by passing an empty array:

  ```
  $ hammer activation-key update \
  --content-view-environment-ids [] \
  --name My_Activation_Key \
  --organization-id My_Organization_ID
  ```
- Remove all content view environments from an activation key by passing an empty string:

  ```
  $ hammer activation-key update \
  --content-view-environments "" \
  --name My_Activation_Key \
  --organization-id My_Organization_ID
  ```
