---
title: "Metrics data retention"
product: "Red Hat Satellite"
version: "6.19"
guide: "monitoring_satellite_performance"
guide_title: "Monitoring Satellite performance"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/monitoring_satellite_performance/index#metrics-data-retention_monitoring"
---
# Chapter 4. Metrics data retention

PCP data retention is controlled by three factors: logged metrics, logging interval, and retention policy. Understanding these settings helps you balance monitoring detail with available disk space.

The following factors determine the storage capacity required by PCP data logging:

- The logged metrics
- The logging interval
- The retention policy

The default logging (sampling) interval is 60 seconds. The default retention policy is to compress archives older than one day and to keep archives for the last 14 days.

You can increase the logging interval or shorten the retention policy to save storage space. If you require high-resolution sampling, you can decrease the logging interval. In such case, ensure that you have enough storage space.

PCP archive logs are stored in the `/var/log/pcp/pmlogger/satellite.example.com` directory.

## 4.1. Changing default logging interval

Change the default logging interval to adjust how often PCP collects metrics, allowing you to save disk space with longer intervals or capture more detailed data with shorter intervals.

**Procedure**

1. Open the `/etc/pcp/pmlogger/control.d/local` configuration file.
2. Locate the `LOCALHOSTNAME` line.
3. Append `-t XXs`, where *XX* is the required time interval in seconds.
4. Save the file.
5. Restart the `pmlogger` service:

   ```
   # systemctl restart pmlogger
   ```

## 4.2. Changing data retention policy

Change the data retention policy to control how long PCP keeps archived data, allowing you to save disk space by deleting older data sooner or retain data longer for analysis.

**Procedure**

1. Open the `/etc/sysconfig/pmlogger_timers` file.
2. Locate the `PMLOGGER_DAILY_PARAMS` line.
3. If the line is commented, uncomment the line.
4. Configure the following parameters:

   - Ensure the default `-E` parameter is present.
   - Append the `-x` parameter and add a value for the required number of days after which data is archived.
   - Append the `-k` parameter and add a value for the number of days after which data is deleted.

   For example, the parameters `-x 4 -k 7` specify that data will be compressed after 4 days and deleted after 7 days.
5. Save the file.

## 4.3. Viewing data storage statistics

View data storage statistics to see how much disk space each metric uses per day, helping you plan storage capacity and adjust retention settings.

Example storage statistics:

```
logged every 60 sec: 61752 bytes or 84.80 Mbytes/day
```

**Procedure**

- On your Satellite Server, view data storage statistics:

  ```
  # less /var/log/pcp/pmlogger/satellite.example.com/pmlogger.log
  ```
