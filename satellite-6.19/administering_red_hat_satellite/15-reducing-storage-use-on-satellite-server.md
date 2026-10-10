---
title: "Reducing storage use on Satellite Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "15"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#reducing-storage-use-on-satellite-server"
---
# Chapter 15. Reducing storage use on Satellite Server

Satellite Server can accumulate a large amount of data over time, which can use a significant amount of disk space. You can clean up database records or reclaim disk space to reduce storage use.

## 15.1. Cleaning audit records

Audit records log changes that users make to Satellite resources, such as creating hosts or editing settings. You can clean up outdated audit records by deleting them.

### 15.1.1. Deleting audit records manually

You can use the `foreman-rake audits:expire` command to remove audit records at any time.

**Procedure**

- Delete the audit records using the `foreman-rake audits:expire` command:

  ```
  # foreman-rake audits:expire days=Number_Of_Days
  ```

  This command deletes all audit records older than `Number_Of_Days`.

### 15.1.2. Deleting audit records automatically

You can automatically delete audit records using the `Saved audits interval` setting. This setting is empty by default, meaning Satellite does not automatically delete the audit records.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Settings**.
2. On the **General** tab, find the **Saved audits interval** setting.
3. Set the value of the setting to the number of days after which you want Satellite to delete the audit records.

## 15.2. Cleaning report records

Report records are configuration reports that hosts send to Satellite after Puppet, Ansible, or Salt runs. Clean up outdated reports to reduce database growth and storage use.

### 15.2.1. Deleting report records

Satellite creates report records automatically. To remove old and unnecessary report records, you can delete them. This is useful for maintaining a clean and organized report history.

**Procedure**

- Use the `foreman-rake reports:expire` command to remove reports at any time. You can also use a cron job to schedule report record deletions at the set interval that you want.

  By default, using the `foreman-rake reports:expire` command removes report records that are older than 90 days. You can specify the number of days to keep the report records by adding the **days** option and add the number of days.

  For example, you can delete report records that are older than seven days:

  ```
  # foreman-rake reports:expire days=7
  ```

## 15.3. Cleaning task records

Task records track background jobs that Satellite executes, such as synchronizing repositories. Configure automatic cleanup or manually clean up outdated tasks to save database space.

### 15.3.1. Configuring the cleaning unused tasks feature

Satellite automatically cleans up old tasks. You can configure the automatic cleaning process according to your needs.

By default, Satellite executes a cron job that cleans tasks every day at 19:45. Satellite removes the following tasks during the cleaning:

- Tasks that have run successfully and are older than thirty days
- All tasks that are older than a year

You can configure the cleaning unused tasks feature using these options:

- To configure the time at which Satellite runs the cron job, set the `--foreman-plugin-tasks-cron-line` parameter to the time you want in cron format. For example, to schedule the cron job to run every day at 15:00, enter the following command:

  ```
  # satellite-installer --foreman-plugin-tasks-cron-line "00 15 * * *"
  ```
- To configure the period after which Satellite deletes the tasks, edit the `:rules:` section in the `/etc/foreman/plugins/foreman-tasks.yaml` file.
- To disable regular task cleanup on Satellite, enter the following command:

  ```
  # satellite-installer --foreman-plugin-tasks-automatic-cleanup false
  ```
- To reenable regular task cleanup on Satellite, enter the following command:

  ```
  # satellite-installer --foreman-plugin-tasks-automatic-cleanup true
  ```

### 15.3.2. Deleting task records

Satellite creates task records automatically. To remove old and unnecessary task records, you can delete them. This helps maintain system performance and keeps your task history organized.

**Procedure**

- Use the `foreman-rake foreman_tasks:cleanup` command to remove tasks at any time. You can also use a cron job to schedule Task record deletions at the set interval that you want.

  For example, you can delete task records from successful repository synchronizations:

  ```
  # foreman-rake foreman_tasks:cleanup TASK_SEARCH='label = Actions::Katello::Repository::Sync' STATES='stopped'
  ```

### 15.3.3. Deleting a task by ID

You can delete tasks by ID, for example if you have submitted confidential data by mistake.

**Procedure**

1. Connect to your Satellite Server using SSH:

   ```
   # ssh root@satellite.example.com
   ```
2. Optional: View the task:

   ```
   $ hammer task info --id My_Task_ID
   ```
3. Delete the task:

   ```
   # foreman-rake foreman_tasks:cleanup TASK_SEARCH="id=My_Task_ID"
   ```
4. Optional: Ensure the task has been removed from Satellite Server:

   ```
   $ hammer task info --id My_Task_ID
   ```

   Note that because the task is deleted, this command returns a non-zero exit code.

## 15.4. Reclaiming disk space

Satellite can consume a significant amount of disk space, especially in large deployments. By reclaiming disk space, you can reduce the amount of disk space used by Satellite.

### 15.4.1. Recovering from a full disk

If a logical volume (LV) with the Pulp database on it is full, Pulp tasks can fail due to insufficient space. You can recover from the situation by increasing the amount of free space available on the LV.

**Procedure**

1. Let running Pulp tasks finish but do not trigger any new ones as they can fail due to the full disk.
2. Ensure that the LV with the `/var/lib/pulp` directory on it has sufficient free space. Here are some ways to achieve that:

   1. Remove orphaned content:

      ```
      # foreman-rake katello:delete_orphaned_content RAILS_ENV=production
      ```

      This is run weekly so it will not free much space.
   2. Change the download policy from **Immediate** to **On Demand** for as many repositories as possible and remove already downloaded packages. See the Red Hat Knowledgebase solution [How to change syncing policy for Repositories on Satellite from "Immediate" to "On-Demand"](https://access.redhat.com/solutions/2785021) on the Red Hat Customer Portal for instructions.
   3. Grow the file system on the LV with the `/var/lib/pulp` directory on it. For more information, see [Growing a logical volume and file system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_and_managing_logical_volumes/index#growing-a-logical-volume-and-file-system_modifying-the-size-of-a-logical-volume) in *Red Hat Enterprise Linux 9 Configuring and managing logical volumes*.

      > **Note**
      >
      > If you use an untypical file system (other than for example ext3, ext4, or xfs), you might need to unmount the file system so that it is not in use. In that case, complete the following steps:
      >
      > 1. Stop Satellite services:
      >
      >    ```
      >    # satellite-maintain service stop
      >    ```
      > 2. Grow the file system on the LV.
      > 3. Start Satellite services:
      >
      >    ```
      >    # satellite-maintain service start
      >    ```
3. If some Pulp tasks failed due to the full disk, run them again.

### 15.4.2. Reclaiming PostgreSQL space

If the PostgreSQL database is using a large amount of disk space, you can reclaim space by vacuuming the database. By reclaiming PostgreSQL space, you can reduce the amount of disk space used by Satellite.

**Procedure**

1. Stop all services, except for the `postgresql` service:

   ```
   # satellite-maintain service stop --exclude postgresql
   ```
2. Switch to the `postgres` user and reclaim space on the database:

   ```
   # su - postgres -c 'vacuumdb --full --all'
   ```
3. Start the other services when the vacuum completes:

   ```
   # satellite-maintain service start
   ```

### 15.4.3. Reclaiming space from on-demand repositories

If you set the *download policy* to on demand, Satellite downloads packages only when the clients request them. You can clean up these packages to reclaim space.

> **Note**
>
> Space reclamation requires an existing repository. For deleted repositories, wait for the next scheduled orphan cleanup or remove orphaned content manually:
>
> ```
> # foreman-rake katello:delete_orphaned_content
> ```

**Procedure**

1. If you want to reclaim space for a single repository:

   1. In the Satellite web UI, navigate to **Content** > **Products**.
   2. Select a product.
   3. On the **Repositories** tab, click the repository name.
   4. From the **Select Actions** list, select **Reclaim Space**.
2. If you want to reclaim space for multiple repositories:

   1. In the Satellite web UI, navigate to **Content** > **Products**.
   2. Select the product name.
   3. On the **Repositories** tab, select the checkbox of the repositories.
   4. Click **Reclaim Space** at the top right corner.
3. If you want to reclaim space for Capsules:

   1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
   2. Select the Capsule Server.
   3. Click **Reclaim space**.
