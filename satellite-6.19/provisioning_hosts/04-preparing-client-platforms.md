---
title: "Preparing client platforms"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-client-platforms"
---
# Chapter 4. Preparing client platforms

You have to configure the platforms that you will provision. That entails creating a hardware model, CPU architecture, and operating system.

> **Note**
>
> The records for Red Hat supported platforms are created automatically when you enable a Red Hat repository.

## 4.1. Compute profiles in Satellite

You can predefine virtual machine hardware details such as CPUs, memory, and storage, by using compute profiles.

A default installation of Red Hat Satellite contains three predefined profiles:

- `1-Small`
- `2-Medium`
- `3-Large`

You can apply compute profiles to all supported compute resources. For supported compute resources, see the following information:

- [Section 1.4, “Supported cloud providers”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#supported-cloud-providers "1.4. Supported cloud providers")
- [Section 1.5, “Supported virtualization infrastructures”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#supported-virtualization-infrastructures "1.5. Supported virtualization infrastructures")

For information on creating a custom compute profile, see [Section 4.9, “Creating compute profiles by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-compute-profiles-by-using-web-ui "4.9. Creating compute profiles by using Satellite web UI").

## 4.2. Creating operating systems by using Satellite web UI

An operating system is a collection of resources that define how Satellite Server installs a base operating system on a host. Operating system entries combine previously defined resources, such as installation media, partition tables, provisioning templates, and others.

Importing operating systems from Red Hat’s CDN creates new entries on the **Hosts** > **Provisioning Setup** > **Operating Systems** page. To import operating systems from Red Hat’s CDN, enable the Red Hat repositories of the operating systems and synchronize the repositories to Satellite.

You can also add custom operating systems using the following procedure.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Operating systems** and click **New Operating** system.
2. In the **Name** field, enter a name to represent the operating system entry.
3. In the **Major** field, enter the number that corresponds to the major version of the operating system.
4. In the **Minor** field, enter the number that corresponds to the minor version of the operating system.
5. In the **Description** field, enter a description of the operating system.
6. From the **Family** list, select the operating system’s family.
7. From the **Root Password Hash** list, select the encoding method for the root password.
8. From the **Architectures** list, select the architectures that the operating system uses.
9. Click the **Partition table** tab and select the possible partition tables that apply to this operating system.
10. Optional: If you use non-Red Hat content, click the Installation Media tab and select the installation media that apply to this operating system.
11. Click the **Templates** tab and select a **PXELinux template**, a **Provisioning template**, and a **Finish template** for your operating system to use. You can select other templates, for example an **iPXE template**, if you plan to use iPXE for provisioning.
12. Click **Submit** to save your provisioning template.

**Additional resources**

- [Enabling Red Hat repositories by using Satellite web UI in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-web-ui)
- [Synchronizing repositories ad hoc in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc)
- [Adding installation media to Satellite by using Satellite web UI in *Provisioning hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#adding-installation-media-to-satellite-by-using-web-ui)

## 4.3. Creating operating systems by using Hammer CLI

An operating system is a collection of resources that define how Satellite Server installs a base operating system on a host. Operating system entries combine previously defined resources, such as installation media, partition tables, provisioning templates, and others.

Importing operating systems from Red Hat’s CDN creates new entries on the **Hosts** > **Provisioning Setup** > **Operating Systems** page. To import operating systems from Red Hat’s CDN, enable the Red Hat repositories of the operating systems and synchronize the repositories to Satellite.

You can also add custom operating systems using the following procedure.

**Procedure**

- Create an operating system:

  ```
  $ hammer os create \
  --architectures "x86_64" \
  --description "Red Hat Enterprise Linux 9" \
  --family "Redhat" \
  --major 9 \
  --media "Red Hat" \
  --minor 5 \
  --name "Red Hat Enterprise Linux" \
  --partition-tables "My_Partition_Table" \
  --provisioning-templates "My_Provisioning_Template"
  ```

**Additional resources**

- [Enabling Red Hat repositories by using Hammer CLI in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-red-hat-repositories-by-using-cli)
- [Synchronizing repositories ad hoc in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc)

## 4.4. Updating the details of multiple operating systems

Update multiple operating systems to assign partition tables, configuration templates, and provisioning templates by using a Bash script.

This example assigns each operating system a partition table called `Kickstart default`, a configuration template called `Kickstart default PXELinux`, and a provisioning template called `Kickstart Default`.

**Procedure**

1. On Satellite Server, run the following Bash script:

   ```bash
   PARTID=$(hammer --csv partition-table list | grep "Kickstart default," | cut -d, -f1)
   PXEID=$(hammer --csv template list --per-page=1000 | grep "Kickstart default PXELinux" | cut -d, -f1)
   SATELLITE_ID=$(hammer --csv template list --per-page=1000 | grep "provision" | grep ",Kickstart default" | cut -d, -f1)

   for i in $(hammer --no-headers --csv os list | awk -F, {'print $1'})
   do
      hammer partition-table add-operatingsystem --id="${PARTID}" --operatingsystem-id="${i}"
      hammer template add-operatingsystem --id="${PXEID}" --operatingsystem-id="${i}"
      hammer os set-default-template --id="${i}" --config-template-id=${PXEID}
      hammer os add-config-template --id="${i}" --config-template-id=${SATELLITE_ID}
      hammer os set-default-template --id="${i}" --config-template-id=${SATELLITE_ID}
   done
   ```
2. Display information about the updated operating system to verify that the operating system is updated correctly:

   ```
   $ hammer os info --id 1
   ```

## 4.5. Creating architectures by using Satellite web UI

You can group hosts and operating systems in Satellite by creating custom architectures. Satellite automatically creates architectures when hosts check in with Puppet, and x86_64 is already preset.

> **Note**
>
> Only the Intel x86_64 architecture is supported for provisioning using PXE, Discovery, and boot disk. For more information, see the Red Hat Knowledgebase solution [Supported architectures and provisioning scenarios in Satellite 6](https://access.redhat.com/solutions/2674001).

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Provisioning Setup** > **Architectures**.
2. Click **Create Architecture**.
3. In the **Name** field, enter a name for the architecture.
4. From the **Operating Systems** list, select an operating system. If none are available, you can create and assign them under **Hosts** > **Provisioning Setup** > **Operating Systems**.
5. Click **Submit**.

## 4.6. Creating architectures by using Hammer CLI

You can group hosts and operating systems in Satellite by creating custom architectures. Satellite automatically creates architectures when hosts check in with Puppet, and x86_64 is already preset.

> **Note**
>
> Only the Intel x86_64 architecture is supported for provisioning using PXE, Discovery, and boot disk. For more information, see the Red Hat Knowledgebase solution [Supported architectures and provisioning scenarios in Satellite 6](https://access.redhat.com/solutions/2674001).

**Procedure**

- Create an architecture:

  ```
  $ hammer architecture create \
  --name "My_Architecture" \
  --operatingsystems "My_Operating_System"
  ```

## 4.7. Creating hardware models by using Satellite web UI

Create a hardware model in Satellite so that you can specify which hardware model a host uses.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Provisioning Setup** > **Hardware Models**.
2. Click **Create Model**.
3. In the **Name** field, enter a name for the hardware model.
4. Optionally, in the **Hardware Model** and **Vendor Class** fields, you can enter corresponding information for your system.
5. In the **Info** field, enter a description of the hardware model.
6. Click **Submit** to save your hardware model.

## 4.8. Creating hardware models by using Hammer CLI

Create a hardware model in Satellite so that you can specify which hardware model a host uses.

**Procedure**

- Create a hardware model:

  ```
  $ hammer model create \
  --hardware-model "My_Hardware_Model" \
  --info "My_Description" \
  --name "My_Hardware_Model_Name" \
  --vendor-class "My_Vendor_Class"
  ```

## 4.9. Creating compute profiles by using Satellite web UI

You can create custom compute profiles in addition to the default predefined profiles to bundle CPU cores, memory, and storage details.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Compute Profiles**.
2. Click **Create Compute Profile**.
3. In the **Name** field, enter a name for the profile.
4. Click **Submit**. A new window opens with the name of the compute profile.
5. In the new window, click the name of each compute resource and edit the attributes you want to set for this compute profile.

## 4.10. Creating compute profiles by using Hammer CLI

You can create custom compute profiles in addition to the default predefined profiles to bundle CPU cores, memory, and storage details.

For more information about creating compute profiles by using Hammer, enter `hammer compute-profile --help`.

**Procedure**

1. Create a compute profile:

   ```
   $ hammer compute-profile create --name "My_Compute_Profile"
   ```
2. Set attributes for the compute profile:

   ```
   $ hammer compute-profile values create \
   --compute-attributes "flavor=m1.small,cpus=2,memory=4GB,cpu_mode=default \
   --compute-resource "My_Compute_Resource" \
   --compute-profile "My_Compute_Profile" \
   --volume size=40GB
   ```
3. Optional: To update the attributes of a compute profile, specify the attributes you want to change. For example, to change the number of CPUs and memory size:

   ```
   $ hammer compute-profile values update \
   --compute-resource "My_Compute_Resource" \
   --compute-profile "My_Compute_Profile" \
   --attributes "cpus=2,memory=4GB" \
   --interface "type=network,bridge=br1,index=1" \
   --volume "size=40GB"
   ```
4. Optional: To change the name of the compute profile, use the `--new-name` attribute:

   ```
   $ hammer compute-profile update \
   --name "My_Compute_Profile" \
   --new-name "My_New_Compute_Profile"
   ```
