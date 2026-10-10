---
title: "Creating and managing roles"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#creating-and-managing-roles"
---
# Chapter 9. Creating and managing roles

Roles define a set of permissions and access levels through permission filters. Assign roles to users and user groups to control which actions they can perform in your environment.

## 9.1. Creating a role by using Satellite web UI

Create a role by using the Satellite web UI. You can add permissions to the role to control which actions users can perform.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Roles**.
2. Click **Create Role**.
3. Provide a **Name** for the role.
4. Click **Submit** to save your new role.

**Next steps**

- Add permissions to the role. To serve its purpose, a role must contain permissions.

## 9.2. Creating a role by using Hammer CLI

Create a role by using Hammer CLI. You can add permissions to the role to control which actions users can perform.

**Procedure**

- Create a role:

  ```
  $ hammer role create --name My_Role_Name
  ```

**Next steps**

- Add permissions to the role. To serve its purpose, a role must contain permissions.

## 9.3. Cloning a role

Clone an existing role in the Satellite web UI to quickly create a new role with similar permissions. You can edit the cloned role to customize permissions for your environment.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Roles** and select **Clone** from the drop-down menu to the right of the required role.
2. Provide a **Name** for the role.
3. Click **Submit** to clone the role.
4. Click the name of the cloned role and navigate to **Filters**.
5. Edit the permissions as required.
6. Click **Submit** to save your new role.

**Example 9.1. Creating an organization-specific manager role**

Use the Satellite web UI to create an administrative role restricted to a single organization named *org-1*.

1. In the Satellite web UI, navigate to **Administer** > **Roles**.
2. Clone the existing **Organization admin** role. Select **Clone** from the drop-down list next to the **Filters** button. You are then prompted to insert a name for the cloned role, for example *org-1 admin*.
3. Click the desired locations and organizations to associate them with the role.
4. Click **Submit** to create the role.
5. Click *org-1 admin*, and click **Filters** to view all associated filters. The default filters work for most use cases. However, you can optionally click **Edit** to change the properties for each filter. You can also click **New filter** to associate new filters with this role.

## 9.4. Adding permissions to a role by using Satellite web UI

Add permissions to a role in the Satellite web UI to define which actions users with that role can perform.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Roles**.
2. Select **Add Filter** from the drop-down list to the right of the required role.
3. Select the **Resource type** from the drop-down list. The *(Miscellaneous)* group gathers permissions that are not associated with any resource group.
4. Click the permissions you want to select from the **Permission** list.
5. Click **Next**.
6. Click **Submit** to save changes.

## 9.5. Adding permissions to a role by using Hammer CLI

Add permissions to a role by using Hammer CLI to define which actions users with that role can perform.

**Procedure**

1. List all available permissions:

   ```
   $ hammer filter available-permissions
   ```
2. Add permissions to a role:

   ```
   $ hammer filter create \
   --permission-ids My_Permission_ID_1,My_Permission_ID_2 \
   --role My_Role_Name
   ```

   For more information about roles and permissions parameters, enter the `hammer role --help` and `hammer filter --help` commands.

## 9.6. Viewing permissions of a role

View the permissions assigned to a role in the Satellite web UI to verify which actions users with that role can perform.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Roles**.
2. Click **Filters** to the right of the required role to get to the **Filters** page.

   The **Filters** page contains a table of permissions assigned to a role grouped by the resource type. It is also possible to generate a complete table of permissions and actions that you can use on your Satellite system. For more information, see [Section 9.7, “Creating a complete permission table”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Creating_a_Complete_Permission_Table_admin "9.7. Creating a complete permission table").

## 9.7. Creating a complete permission table

Generate a complete permission table from the Satellite console to review all available permissions and actions on your Satellite.

**Procedure**

1. Start the Satellite console:

   ```
   # foreman-rake console
   ```
2. Insert the following code into the console:

   ```
   f = File.open('/tmp/table.html', 'w')

   result = Foreman::AccessControl.permissions {|a,b| a.security_block <=> b.security_block}.collect do |p|
         actions = p.actions.collect { |a| "<li>#{a}</li>" }
         "<tr><td>#{p.name}</td><td><ul>#{actions.join('')}</ul></td><td>#{p.resource_type}</td></tr>"
   end.join("\n")

   f.write("<table border=\"1\"><tr><td>Permission name</td><td>Actions</td><td>Resource type</td></tr>\n")
   f.write(result)
   f.write("</table>\n")
   ```

   The above syntax creates a table of permissions and saves it to the `/tmp/table.html` file.
3. Press `Ctrl` + `D` to exit the Satellite console.
4. Open `/tmp/table.html` in a web browser to view the table.

## 9.8. Removing a role

You can remove a role from the Satellite web UI if you no longer need it to grant permissions to users.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Roles**.
2. Select **Delete** from the drop-down list to the right of the role to be deleted.
3. Click **Confirm** to delete the role.

## 9.9. Predefined roles available in Satellite

Review predefined roles in Satellite to understand which permissions each role grants before assigning roles to users.

For a complete set of predefined roles and the permissions they grant, log in to Satellite web UI as the privileged user and navigate to **Administer** > **Roles**. For more information, see [Section 9.6, “Viewing permissions of a role”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Viewing_Permissions_of_a_Role_admin "9.6. Viewing permissions of a role").

| Predefined role | Permissions the role provides | Additional information |
| --- | --- | --- |
| Auditor | View the Audit log. |  |
| Default role | View tasks and jobs invocations. | Satellite automatically assigns this role to every user in the system. |
| Manager | View and edit global settings. |  |
| Organization admin | All permissions except permissions for managing organizations. | An administrator role defined per organization. The role has no visibility into resources in other organizations.    By cloning this role and assigning an organization, you can delegate administration of that organization to a user. |
| Site manager | View permissions for various items.    Permissions to manage hosts in the infrastructure. | A restrained version of the Manager role. |
| System admin | Edit global settings in **Administer** > **Settings**.    View, create, edit, and destroy users, user groups, and roles.    View, create, edit, destroy, and assign organizations and locations but not view resources within them. | Users with this role can create users and assign all roles to them. Give this role only to trusted users. |
| Viewer | View the configuration of every element of the Satellite structure, logs, reports, and statistics. |  |

## 9.10. Granular permission filtering

With granular permission filters, you can limit permissions of a user to selected instances of a resource type.

### 9.10.1. Creating a granular permission filter by using Satellite web UI

Create a granular permission filter in the Satellite web UI to limit role permissions to specific resource instances.

Satellite does not apply search conditions to create actions. For example, limiting the *create_locations* action with *name = "Default Location"* expression in the search field does not prevent the user from assigning a custom name to the newly created location.

**Procedure**

1. Specify a query in the **Search** field on the **Edit Filter** page. Queries have the following form:

   ```
   field_name operator value
   ```

   - *field_name* marks the field to be queried. The range of available field names depends on the resource type. For example, the *Partition Table* resource type offers *family*, *layout*, and *name* as query parameters.
   - *operator* specifies the type of comparison between *field_name* and *value*. See [Section 9.10.4, “Supported operators for granular search”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Supported_Operators_for_Granular_Search_admin "9.10.4. Supported operators for granular search") for an overview of applicable operators.
   - *value* is the value used for filtering. This can be for example a name of an organization. Two types of wildcard characters are supported: underscore (_) provides single character replacement, while percent sign (%) replaces zero or more characters.

     > **Note**
     >
     > For most resource types, the **Search** field provides a drop-down list suggesting the available parameters. This list appears after placing the cursor in the search field. For many resource types, you can combine queries using logical operators such as *and*, *not* and *has* operators.

### 9.10.2. Creating a granular permission filter by using Hammer CLI

Create a granular permission filter by using Hammer CLI to limit role permissions to specific resource instances.

Satellite does not apply search conditions to create actions. For example, limiting the *create_locations* action with *name = "Default Location"* expression in the search field does not prevent the user from assigning a custom name to the newly created location.

**Procedure**

- To create a granular filter, enter the `hammer filter create` command with the `--search` option to limit permission filters, for example:

  ```
  $ hammer filter create \
  --permission-ids 91 \
  --search "name ~ ccv*" \
  --role qa-user
  ```

  This command adds to the **qa-user** role a permission to view, create, edit, and destroy content views that only applies to content views with name starting with `ccv`.

### 9.10.3. Examples of using granular permission filters

As an administrator, you can allow selected users to make changes in a certain part of the environment path. For example, you can allow users to work with content while it is in the development stage of the application lifecycle, but not once the content is pushed to production.

The following query applies any permissions specified for the Host resource type only to hosts in the group named host-editors:

```
hostgroup = host-editors
```

The following query returns records where the name matches *XXXX*, *Yyyy*, or *zzzz* example strings:

```
name ^ (XXXX, Yyyy, zzzz)
```

You can also limit permissions to a selected environment. To do so, specify the environment name in the **Search** field, for example:

```
Dev
```

### 9.10.4. Supported operators for granular search

You can use logical and symbolic operators to build precise search queries when limiting user permissions.

Table 9.1. Logical operators

|  |  |
| --- | --- |
| Operator | Description |
| and | Combines search criteria. |
| not | Negates an expression. |
| has | Object must have a specified property. |

Table 9.2. Symbolic operators

|  |  |
| --- | --- |
| Operator | Description |
| = | *Is equal to*. An equality comparison that is case-sensitive for text fields. |
| != | *Is not equal to*. An inversion of the = operator. |
| ~ | *Like*. A case-insensitive occurrence search for text fields. |
| !~ | *Not like*. An inversion of the ~ operator. |
| ^ | *In*. An equality comparison that is case-sensitive search for text fields. This generates a different SQL query to the *Is equal to* comparison, and is more efficient for multiple value comparison. |
| !^ | *Not in*. An inversion of the ^ operator. |
| >, >= | *Greater than*, *greater than or equal to*. Supported for numerical fields only. |
| <, ⇐ | *Less than*, *less than or equal to*. Supported for numerical fields only. |
