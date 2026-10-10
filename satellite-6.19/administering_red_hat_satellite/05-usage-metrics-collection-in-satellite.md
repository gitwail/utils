---
title: "Usage metrics collection in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#usage-metrics-collection-in-satellite"
---
# Chapter 5. Usage metrics collection in Satellite

Satellite collects information on product usage to improve how Red Hat prioritizes future development and to help with debugging. The collected usage metrics include information such as which Satellite features are used and the number of objects in the database.

## 5.1. Overview of usage metrics collection in Satellite

Satellite includes the `satellite-maintain report generate` command, which can collect information from user environments to better understand how Satellite is used.

The following `systemd` timers collect the data:

`satellite-usage-metrics-generate.timer`
:   This timer collects the full list of usage metrics. It executes the `satellite-maintain report generate` command on your Satellite Server and then stores the collected data in the `/var/lib/foreman-maintain/satellite_metrics.yml` file. The timer runs weekly.

`satellite-usage-metrics-condense.timer`
:   This timer collects the same set of metrics as `satellite-usage-metrics-generate.timer`, condenses them so that they can be uploaded as custom Red Hat Subscription Manager facts, and stores them in the `/etc/rhsm/facts/foreman.facts` file. The timer runs weekly.

When you use the `sos report` command to generate a report for Red Hat Technical Support, the report will include the `satellite_metrics.yml` and `/etc/rhsm/facts/foreman.facts` files, along with the other configuration, diagnostics, and troubleshooting data that `sos` collects.

**Additional resources**

- [Appendix G, *Usage metrics collected by Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#usage-metrics-collected-by-satellite "Appendix G. Usage metrics collected by Satellite")

## 5.2. Reviewing usage metrics collected from your Satellite

You can review the usage metrics that Satellite collects from your deployment by using the `satellite-maintain report` command on your Satellite Server.

**Procedure**

1. Display the list of full usage metrics:

   ```
   # satellite-maintain report generate
   ```
2. Display the list of condensed usage metrics:

   ```
   # satellite-maintain report condense
   ```

**Example 5.1. Example output of `satellite-maintain report generate`**

```
# satellite-maintain report generate
Running Generate the usage reports
================================================================================
Check if OpenSCAP is used:                                            [OK]
--------------------------------------------------------------------------------
Checks the use of External auth source:                               [OK]
--------------------------------------------------------------------------------
Check how resources are grouped:                                      [OK]
--------------------------------------------------------------------------------

[... output truncated ...]

compliance_policy_count: 0
compliance_policy_with_tailoring_file_count: 0
compliance_scap_contents_count: 5

[... output truncated ...]
```

## 5.3. Disabling the collection of usage metrics

You can opt out of the default usage metrics collection by masking the `systemd` timers that collect the data on your Satellite Server.

**Procedure**

1. To disable the collection of the full usage metrics:

   1. Mask the `satellite-usage-metrics-generate.timer` unit:

      ```
      # systemctl mask satellite-usage-metrics-generate.timer
      ```
   2. If the timer has been executed already at least once, remove the generated usage metrics file:

      ```
      # rm /var/lib/foreman-maintain/satellite_metrics.yml
      ```
2. To disable the collection of the condensed usage metrics:

   1. Mask the `satellite-usage-metrics-condensed.timer` unit:

      ```
      # systemctl mask satellite-usage-metrics-condensed.timer
      ```
   2. If the timer has been executed already at least once, remove the generated usage metrics file:

      ```
      # rm /etc/rhsm/facts/foreman.facts
      ```

**Verification**

1. On your Satellite Server, verify the status of the timer you want to disable. For example, to verify the status of the `satellite-usage-metrics-generate.timer` unit:

   ```
   # systemctl status satellite-usage-metrics-generate.timer
   ```
2. Verify that no generated usage metrics file exists:

   ```
   # cat /var/lib/foreman-maintain/satellite_metrics.yml
   ```
