---
title: "Provisioning contexts for Satellite resources"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-contexts-for-satellite-resources"
---
# Chapter 7. Provisioning contexts for Satellite resources

A provisioning context is the combination of an organization and location that you specify for Satellite resources. The organization and location that a resource belongs to sets the ownership and access for that resource.

**Organizations** divide Red Hat Satellite resources into logical groups based on ownership, purpose, content, security level, and other divisions. You can create and manage multiple organizations through Red Hat Satellite and assign resources to each individual organization. This ensures Satellite Server provisions hosts within a certain organization and only uses resources that are assigned to that organization.

**Locations** function similar to organizations. The difference is that locations are based on physical or geographical setting. Users can nest locations in a hierarchy.

**Additional resources**

- [Managing organizations in Satellite in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-organizations-in-satellite)
- [Managing locations in Satellite in *Administering Red Hat Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-locations-in-satellite)

## 7.1. Setting the provisioning context by using Satellite web UI

When you set a provisioning context, you define which organization and location to use for provisioning hosts.

The organization and location menus are located in the menu bar, on the upper left of the Satellite web UI. If you have not selected an organization and location to use, the menu displays: **Any Organization** and **Any Location**.

**Procedure**

1. Click **Any Organization** and select the organization.
2. Click **Any Location** and select the location to use.
3. Each user can set their default provisioning context in their account settings. Click the user name in the upper right of the Satellite web UI and select **My account** to edit your user account settings.

## 7.2. Setting the provisioning context by using Hammer CLI

When you set a provisioning context, you define which organization and location to use for provisioning hosts.

**Procedure**

- When using the CLI, include either `--organization` or `--organization-label` and `--location` or `--location-id` as an option. For example:

  ```
  $ hammer host list --organization "My_Organization" --location "My_Location"
  ```

  This command outputs hosts allocated to `My_Organization` and `My_Location`.
