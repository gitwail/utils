---
title: "Upgrading hosts to next major Red Hat Enterprise Linux release"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "11"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Upgrading_Hosts_to_Next_Major_Release_managing-hosts"
---
# Chapter 11. Upgrading hosts to next major Red Hat Enterprise Linux release

You can use a job template to upgrade your Red Hat Enterprise Linux hosts to the next major release. This helps you keep hosts on a supported release and can be run across multiple hosts by using remote execution.

Red Hat supports the following upgrade paths:

- Red Hat Enterprise Linux 7 to Red Hat Enterprise Linux 8
- Red Hat Enterprise Linux 8 to Red Hat Enterprise Linux 9
- Red Hat Enterprise Linux 9 to Red Hat Enterprise Linux 10

**Prerequisites**

- Your Red Hat Enterprise Linux hosts meet the requirements for the upgrade.

  - For Red Hat Enterprise Linux 7 to Red Hat Enterprise Linux 8 upgrade, see [Planning an upgrade](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/upgrading_from_rhel_7_to_rhel_8/planning-an-upgrade_upgrading-from-rhel-7-to-rhel-8) in *Upgrading from RHEL 7 to RHEL 8*.
  - For Red Hat Enterprise Linux 8 to Red Hat Enterprise Linux 9 upgrade, see [Planning an upgrade to RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/upgrading_from_rhel_8_to_rhel_9/planning-an-upgrade-to-rhel-9_upgrading-from-rhel-8-to-rhel-9) in *Upgrading from RHEL 8 to RHEL 9*.
  - For Red Hat Enterprise Linux 9 to Red Hat Enterprise Linux 10 upgrade, see [Planning an upgrade to RHEL 10](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/upgrading_from_rhel_9_to_rhel_10/planning-an-upgrade-to-rhel-10) in *Upgrading from RHEL 9 to RHEL 10*.
- Your Red Hat Enterprise Linux hosts are prepared for the upgrade.

  - For Red Hat Enterprise Linux 7 to Red Hat Enterprise Linux 8 upgrade, see [Preparing a RHEL 7 system for the upgrade](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/upgrading_from_rhel_7_to_rhel_8/assembly_preparing-for-the-upgrade_upgrading-from-rhel-7-to-rhel-8#preparing-a-rhel-7-system-for-the-upgrade_upgrading-from-rhel-7-to-rhel-8) in *Upgrading from RHEL 7 to RHEL 8*.
  - For Red Hat Enterprise Linux 8 to Red Hat Enterprise Linux 9 upgrade, see [Preparing a RHEL 8 system for the upgrade](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/upgrading_from_rhel_8_to_rhel_9/assembly_preparing-for-the-upgrade_upgrading-from-rhel-8-to-rhel-9#preparing-a-rhel-8-system-for-the-upgrade_upgrading-from-rhel-8-to-rhel-9) in *Upgrading from RHEL 8 to RHEL 9*.
  - For Red Hat Enterprise Linux 9 to Red Hat Enterprise Linux 10 upgrade, see [Preparing a RHEL 9 system for the upgrade](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/upgrading_from_rhel_9_to_rhel_10/preparing-for-the-upgrade#preparing-a-rhel-9-system-for-the-upgrade) in *Upgrading from RHEL 9 to RHEL 10*.
- Satellite SSH keys are distributed to the hosts that you want to upgrade. For more information, see [Section 19.2.3, “Distributing SSH keys for remote execution”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Distributing_SSH_Keys_for_Remote_Execution_managing-hosts "19.2.3. Distributing SSH keys for remote execution").

**Procedure**

1. Optional: Customize the upgrade by modifying the default pre-upgrade check and upgrade job templates.

   1. Clone and modify the **Run preupgrade via Leapp** template, the **Run upgrade via Leapp** template, or both. For more information, see [Section 19.6.6, “Customizing job templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#customizing-job-templates "19.6.6. Customizing job templates").
   2. In the Satellite web UI, navigate to **Administer** > **Remote Execution Features**.
   3. If you modified the pre-upgrade template, click **leapp_preupgrade**. If you modified the upgrade template, click **leapp_upgrade**.
   4. In the **Job Template** drop-down menu, select your template.
   5. Click **Submit**. The **leap_preupgrade** and **leapp_upgrade** remote execution features now point to the modified templates.
2. Run a pre-upgrade check:

   1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
   2. Select the hosts that you want to upgrade.
   3. If you want to upgrade to the latest available release, expand the **Schedule a Job** drop-down menu and select **Preupgrade check with Leapp**.
   4. If you want to upgrade to a specific release version, click **Schedule a job**. From the **Job category** list, select **Leapp - Preupgrade**. Follow the job wizard to start the preupgrade check.
3. Review the results of the pre-upgrade check:

   > **Note**
   >
   > The results of the pre-upgrade check are only available in the legacy Satellite web UI job invocation details page.

   1. Navigate to **Monitor** > **Jobs**. Click the pre-upgrade check job.
   2. From the **Rerun all** dropdown menu, click **Legacy UI**.
   3. Click the **Leapp preupgrade report** tab to see if Leapp has found any issues on your hosts. Issues that have the **Inhibitor** flag are considered crucial and are likely to break the upgrade procedure. Issues that have the **Has Remediation** flag contain remediation that can help you fix the issue.
   4. Click an issue that is flagged as **Has Remediation** to expand it.

      - If the issue contains a remediation **Command**, you can fix it directly from Satellite using remote execution. Select the issue.
      - If the issue contains only a remediation **Hint**, use the hint to fix the issue on the host manually.

      Repeat this step for other issues.
   5. After you selected any issues with remediation commands, click **Fix Selected** and submit the job.
   6. After the issues are fixed, click **Rerun**, and then click **Submit** to run the pre-upgrade check again to verify that the hosts you are upgrading do not have any issues and are ready to be upgraded.
4. Start the upgrade:

   1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
   2. Select the hosts that you want to upgrade.
   3. If you want to upgrade to the latest available release version, expand the **Schedule a Job** drop-down menu and select **Upgrade with Leapp**.
   4. If you want to upgrade to a specific release version, click **Schedule a job**. From the **Job category** list, select **Leapp - Upgrade**. Follow the job wizard to start the upgrade.

**Next steps**

- Verify the post-upgrade state of each host and perform the required post-upgrade tasks:

  - For Red Hat Enterprise Linux 7 to Red Hat Enterprise Linux 8 upgrade, see [Verifying the post-upgrade state of the RHEL 8 system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/upgrading_from_rhel_7_to_rhel_8/verifying-the-post-upgrade-state-of-the-rhel-8-system_upgrading-from-rhel-7-to-rhel-8) and [Performing post-upgrade tasks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/upgrading_from_rhel_7_to_rhel_8/performing-post-upgrade-tasks-rhel-7-to-rhel-8_upgrading-from-rhel-7-to-rhel-8) in *Upgrading from RHEL 7 to RHEL 8*.
  - For Red Hat Enterprise Linux 8 to Red Hat Enterprise Linux 9 upgrade, see [Verifying the post-upgrade state](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/upgrading_from_rhel_8_to_rhel_9/verifying-the-post-upgrade-state_upgrading-from-rhel-8-to-rhel-9) and [Performing post-upgrade tasks on the RHEL 9 system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/upgrading_from_rhel_8_to_rhel_9/performing-post-upgrade-tasks-on-the-rhel-9-system_upgrading-from-rhel-8-to-rhel-9) in *Upgrading from RHEL 8 to RHEL 9*.
  - For Red Hat Enterprise Linux 9 to Red Hat Enterprise Linux 10 upgrade, see [Verifying the post-upgrade state](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/upgrading_from_rhel_9_to_rhel_10/verifying-the-post-upgrade-state) and [Performing post-upgrade tasks on the RHEL 10 system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/upgrading_from_rhel_9_to_rhel_10/performing-post-upgrade-tasks-on-the-rhel-10-system) in *Upgrading from RHEL 9 to RHEL 10*.
