---
title: "Managing locations in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#managing-locations-in-satellite"
---
# Chapter 7. Managing locations in Satellite

Locations group Satellite resources and hosts based on physical or geographical settings. Use locations to manage and isolate resources within a hierarchical structure in a single Satellite deployment.

Organizations and locations have the following conceptual differences:

- Locations are based on physical or geographical settings.
- Locations have a hierarchical structure.

You can structure locations hierarchically by providing a parent location. Unless otherwise specified, locations inherit the settings from their parent location.

## 7.1. Creating a location by using Satellite web UI

Create a location by using the Satellite web UI. You can use the location to assign hosts and resources to the location.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Locations**.
2. Click **New Location**.
3. Optional: From the **Parent** list, select a parent location. This creates a location hierarchy.
4. In the **Name** field, enter a name for the location.
5. Optional: In the **Description** field, enter a description for the location.
6. Click **Submit**.
7. If you have hosts with no location assigned, add any hosts that you want to assign to the new location, then click **Proceed to Edit**.
8. Assign any infrastructure resources that you want to add to the location. This includes networking resources, installation media, Kickstart templates, and other parameters. You can return to this page at any time by navigating to **Administer** > **Locations** and then selecting a location to edit.
9. Click **Submit** to save your changes.

## 7.2. Creating a location by using Hammer CLI

Create a location by using Hammer CLI. You can use the location to assign hosts and resources to the location.

**Procedure**

- Create a location:

  ```
  $ hammer location create \
  --description "My_Location_Description" \
  --name "My_Location" \
  --parent-id "My_Location_Parent_ID"
  ```

**Example 7.1. Creating multiple locations**

The following example Bash script creates three locations – London, Munich, Boston – and assigns them to the Example Organization.

```shell-session
ORG="Example Organization"
LOCATIONS="London Munich Boston"

for LOC in ${LOCATIONS}
do
  hammer location create --name "${LOC}"
  hammer location add-organization --name "${LOC}" --organization "${ORG}"
done
```

## 7.3. Setting the location context by using Satellite web UI

Set the location context in the Satellite web UI to define which location applies to hosts and their associated resources.

**Procedure**

1. In the Satellite web UI, navigate to the top menu bar. The location menu is the second menu item in the menu bar, on the upper left of the Satellite web UI.
2. If you have not selected a current location, the menu displays **Any Location**. Click **Any location** and select the location to use.

## 7.4. Setting the location context by using Hammer CLI

Set the location context when using Hammer CLI to define which location applies to hosts and their associated resources.

**Procedure**

- While using the CLI, include either `--location "My_Location"` or `--location-id "My_Location_ID"` as an option. For example:

  ```
  $ hammer host list --location "My_Location"
  ```

  This command lists hosts associated with the *My_Location* location.

## 7.5. Deleting a location by using Satellite web UI

You can delete a location from the Satellite web UI if you no longer need it for resource management.

> **Important**
>
> Do not delete **Default Location** created during installation because the default location is a placeholder for any unassociated hosts in your Satellite environment. There must be at least one location in the environment at any given time.

**Procedure**

1. If there are any lifecycle environments or host groups associated with the location you are about to delete, remove them by navigating to **Administer** > **Locations** and clicking the relevant location.
2. In the Satellite web UI, navigate to **Administer** > **Locations**.
3. Select **Delete** from the list to the right of the name of the location you want to delete.
4. Click **OK** to delete the location.

## 7.6. Deleting a location by using Hammer CLI

You can delete a location by using Hammer CLI if you no longer need it for resource management.

> **Important**
>
> Do not delete **Default Location** created during installation because the default location is a placeholder for any unassociated hosts in your Satellite environment. There must be at least one location in the environment at any given time.

**Procedure**

1. If there are any lifecycle environments or host groups associated with the location you are about to delete, remove them by navigating to **Administer** > **Locations** and clicking the relevant location.
2. View all locations:

   ```
   $ hammer location list
   ```

   From the output, note the ID of the location that you want to delete.
3. Delete a location:

   ```
   $ hammer location delete --id My_Location_ID
   ```
