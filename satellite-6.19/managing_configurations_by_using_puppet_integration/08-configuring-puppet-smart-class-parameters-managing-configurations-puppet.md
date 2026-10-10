---
title: "Configuring Puppet smart class parameters"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_configurations_by_using_puppet_integration"
guide_title: "Managing configurations by using Puppet integration"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#Configuring_Puppet_Smart_Class_Parameters_managing-configurations-puppet"
---
# Chapter 8. Configuring Puppet smart class parameters

Configure Puppet smart class parameters in Satellite to override module defaults and tailor behavior per organization, location, or host.

## 8.1. Puppet parameter hierarchy

Puppet parameters follow a hierarchy so you can set defaults globally and override them per organization, location, host group, or host.

Parameters at a lower level override parameters of the higher levels:

1. Global parameters
2. Organization parameters
3. Location parameters
4. Host group parameters
5. Host parameters

For example, host specific parameters override the parameter at any higher level, and location parameters only override parameters at the organization or global level. This feature is especially useful when you use locations or organizations to group hosts.

## 8.2. Overriding a smart class parameter globally

You can configure a Puppet class after you have imported it to Satellite Server. This example overrides the default list of Network Time Protocol (NTP) servers.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Puppet ENC** > **Classes**.
2. Select the **ntp** Puppet class to change its configuration.
3. Select the **Smart Class Parameter** tab and search for **servers**.
4. Ensure the **Override** checkbox is selected.
5. Set the **Parameter Type** drop down menu to *array*.
6. Insert a list of ntp servers as **Default Value**:

   ```
   ["0.de.pool.ntp.org","1.de.pool.ntp.org","2.de.pool.ntp.org","3.de.pool.ntp.org"]
   ```

   An alternative way to describe the array is the `yaml` syntax:

   ```yaml
   - 0.de.pool.ntp.org
   - 1.de.pool.ntp.org
   - 2.de.pool.ntp.org
   - 3.de.pool.ntp.org
   ```
7. Click **Submit** to change the default configuration of the Puppet module `ntp`.

## 8.3. Overriding a smart class parameter for an organization

You can use groups of hosts to override Puppet parameters for multiple hosts at once. The following example chooses the *organization* context to illustrate setting context based parameters.

Note that *organization*-level Puppet parameters are overridden by *location*-level Puppet parameters.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Puppet ENC** > **Classes**.
2. Click a class name to select a class.
3. On the **Smart Class Parameter** tab, select a parameter.
4. Use the **Order** list to define the hierarchy of the Puppet parameters. The individual host (`fqdn`) marks the most and the organization context (`organization`) the least relevant.
5. Check **Merge Overrides** if you want to add all further matched parameters after finding the first match.
6. Check **Merge Default** if you want to also include the default value even if there are more specific values defined.
7. Check **Avoid Duplicates** if you want to create a list of unique values for the selected parameter.
8. The **matcher** field requires an *attribute type* from the *order* list.
9. Optional: Click **Add Matcher** to add more matchers.
10. Click **Submit** to save the changes.

## 8.4. Overriding a smart class parameter for a location

You can use groups of hosts to override Puppet parameters for multiple hosts at once. The following examples chooses the *location* context to illustrate setting context based parameters.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Puppet ENC** > **Classes**.
2. Click a class name to select a class.
3. On the **Smart Class Parameter** tab, select a parameter.
4. Use the **Order** list to define the hierarchy of the Puppet parameters. The individual host (`fqdn`) marks the most and the location context (`location`) the least relevant.
5. Check **Merge Overrides** if you want to add all further matched parameters after finding the first match.
6. Check **Merge Default** if you want to also include the default value even if there are more specific values defined.
7. Check **Avoid Duplicates** if you want to create a list of unique values for the selected parameter.
8. The **matcher** field requires an *attribute type* from the *order* list. For example, you can choose `Paris` as *location* context and set the value to French ntp servers.
9. Optional: Click **Add Matcher** to add more matchers.
10. Click **Submit** to save the changes.

## 8.5. Overriding a smart class parameter on an individual host

You can override parameters on individual hosts. This is recommended if you have multiple hosts and only want to make changes to a single one.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click a host name to select a host.
3. Click **Edit**.
4. On the **Host** tab, select a Puppet **Environment**.
5. Select the **Puppet ENC** tab.
6. Click **Override** to edit the Puppet parameter.
7. Click **Submit** to save the changes.
