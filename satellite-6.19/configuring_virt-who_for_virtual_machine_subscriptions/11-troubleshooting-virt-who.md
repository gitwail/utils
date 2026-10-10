---
title: "Troubleshooting virt-who"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_virt-who_for_virtual_machine_subscriptions"
guide_title: "Configuring virt-who for virtual machine subscriptions"
chapter_number: "11"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt-who_for_virtual_machine_subscriptions/index#troubleshooting-virt-who"
---
# Chapter 11. Troubleshooting virt-who

You can troubleshoot virt-who by checking the service status, logs, and by identifying configuration issues.

## 11.1. Checking virt-who status by using Satellite web UI

Monitor the status of your virt-who instances to verify they are successfully reporting virtual machines to Satellite Server. This helps you troubleshoot connectivity issues and ensure accurate subscription management for your virtualized infrastructure.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Virt-who Configurations**.
2. Check the **Status** column of each virt-who instance.

   The `OK` status indicates that virt-who is successfully connecting to Satellite Server and reporting the virtual machines managed by each hypervisor.

## 11.2. Checking virt-who status by using Hammer CLI

Monitor the status of your virt-who instances by using Hammer CLI to verify they are successfully reporting virtual machines to Satellite Server. This helps you troubleshoot connectivity issues and ensure accurate subscription management for your virtualized infrastructure.

**Procedure**

- List the status of all virt-who instances:

  ```
  $ hammer virt-who-config list
  ```

  The output includes the date and time when each virt-who instance reported to Satellite Server.

## 11.3. Enabling RHSM debug logging by using Satellite web UI

You can enable Red Hat Subscription Manager (RHSM) debug logging for the `/var/log/rhsm/rhsm.log` file by using Satellite web UI.

After you resolve the problem, you must disable debug logging and redeploy the virt-who configuration.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Virt-who Configurations**.
2. Select **Edit** in the **Actions** column of a virt-who configuration.
3. Select **Enable debugging output**.
4. Click **Submit**.
5. Redeploy the virt-who configuration on the target host.

## 11.4. Enabling RHSM debug logging by using Hammer CLI

You can enable Red Hat Subscription Manager (RHSM) debug logging for the `/var/log/rhsm/rhsm.log` file by using Hammer CLI.

After you resolve the problem, you must disable debug logging and redeploy the virt-who configuration.

**Procedure**

1. Set the logging level to `debug`:

   ```
   $ hammer virt-who-config update \
   --debug true
   ```
2. Redeploy the virt-who configuration on the target host.

## 11.5. Virt-who troubleshooting methods

If you encounter the following problems when using virt-who in Satellite, you might resolve them by using the following solutions.

virt-who does not report to Satellite Server
:   virt-who might not report to Satellite Server if Satellite Server is configured to use a proxy server in `rhsm.conf` while virt-who is configured not to use a proxy server in `/etc/sysconfig/virt-who`.

    The virt-who setting is ignored by the Subscription Manager. As a result, virt-who attempts to connect to Satellite Server through a proxy server and fails.

    To work around this problem, add the following parameter to the `/etc/rhsm/rhsm.conf` file:

    ```
    no_proxy = server.example.com
    ```

Identifying issues when using multiple virt-who configuration files
:   If you have multiple virt-who configuration files on one server, move one file at a time to a different directory while testing after each file move. If the issue no longer occurs, the cause is associated with the most recently moved file. After you have resolved the issue, return the virt-who configuration files to their original location.

    Alternatively, you can test an individual file after moving it by using the `--config` option to specify its location. For example:

    ```
    $ virt-who --debug --one-shot --config /tmp/conf_name.conf
    ```

Identifying duplicate hypervisors
:   Duplicate hypervisors can cause subscription and entitlement errors. Enter the following commands to check for duplicate hypervisors:

    ```
    # systemctl stop virt-who
    # virt-who -op >/tmp/virt-who.json
    # systemctl start virt-who
    # cat /tmp/virt-who.json | json_reformat | grep name | sort | uniq -c | sort -nr | head -n5
      3    "name": "localhost"
      1    "name": "rhel1.example.com"
      1    "name": "rhel2.example.com"
      1    "name": "rhel3.example.com"
      1    "name": "rhel4.example.com"
    ```

    In this example, three hypervisors have the same FQDN (`localhost`), and must be corrected to use unique FQDNs.

Identifying duplicate virtual machines
:   Enter the following commands to check for duplicate virtual machines:

    ```
    # systemctl stop virt-who
    # virt-who -op >/tmp/virt-who.json
    # systemctl start virt-who
    # cat /tmp/virt-who.json | json_reformat | grep "guestId" | sort | uniq -c | sort -nr | head -n10
    ```

Checking the number of hypervisors
:   Enter the following commands to check the number of hypervisors virt-who currently reports:

    ```
    # systemctl stop virt-who
    # virt-who -op >/tmp/virt-who.json
    # systemctl start virt-who
    # cat /tmp/virt-who.json | json_reformat | grep name | sort | uniq -c | wc -l
    ```

Checking the number of virtual machines
:   Enter the following commands to check the number of virtual machines that virt-who currently reports:

    ```
    # systemctl stop virt-who
    # virt-who -op >/tmp/virt-who.json
    # systemctl start virt-who
    # cat /tmp/virt-who.json | json_reformat | grep "guestId" | sort | uniq -c | wc -l
    ```

**Additional resources**

- [Troubleshooting documentation in *Getting Started with RHEL System Registration*](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/)
