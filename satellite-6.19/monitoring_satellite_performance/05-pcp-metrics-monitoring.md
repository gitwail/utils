---
title: "PCP metrics"
product: "Red Hat Satellite"
version: "6.19"
guide: "monitoring_satellite_performance"
guide_title: "Monitoring Satellite performance"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/monitoring_satellite_performance/index#pcp-metrics_monitoring"
---
# Chapter 5. PCP metrics

You can monitor Satellite performance using PCP metrics, which provide system-level data (CPU, memory, network) and Satellite-specific data (processes, PostgreSQL, Rails) in a structured format. Understanding PCP metrics helps you identify performance bottlenecks and optimize your deployment.

Metrics are stored in a tree-like structure. For example, all network metrics are stored in a node named `network`. Each metric can be a single value, or a list of values, known as instances. For example, kernel load has three instances, the 1-minute, 5-minute, and 15-minute average.

For every metric entry, PCP stores both its data and metadata. This includes the metrics description, data type, units, and dimensions. For example, the metadata enables PCP to output multiple metrics with different dimensions.

If a metric is a counter, its value can only increase. For example, a count of disk write operations on a specific device only increases. When you query the value of a counter metric, PCP converts this into a rate value by default.

In addition to system metrics, such as CPU, memory, kernel, XFS, disk, and network, the following metrics are configured:

| Metric | Description |
| --- | --- |
| hotproc.* | Basic metrics of key Satellite processes |
| apache.* | Apache HTTP Server metrics |
| postgresql.* | Basic PostgreSQL statistics |
| openmetrics.foreman.fm_rails_* | Satellite metrics |

## 5.1. Identifying available metrics

Use these commands to discover what PCP metrics are available on your system, including both system-level metrics and Satellite-specific telemetry data, and to locate archived metric logs for historical analysis.

- List all metrics available through PCP:

  ```
  # pminfo
  ```
- List all Satellite metrics and their descriptions:

  ```
  # foreman-rake telemetry:metrics
  ```
- List the archived metrics:

  ```
  # less /var/log/pcp/pmlogger/satellite.example.com/pmlogger.log
  ```
- The `pmlogger` daemon archives data as received, according to its configuration. Retrieve the name of the active log file:

  ```
  # pcp | grep logger
  ```

  The output includes the file name of the active log file, for example:

  ```
   pmlogger: primary logger: /var/log/pcp/pmlogger/satellite.example.com/20230831.00.10
  ```

## 5.2. Retrieving live metrics

You can retrieve real-time performance data using PCP command-line tools to monitor disk activity, system performance, and other metrics while troubleshooting or analyzing Satellite performance issues.

**Procedure**

- To print current values of a particular metric, enter the following command:

  ```
  # pmval -f 1 disk.partitions.write
  ```

  In this example, metric instances on writes to disk partitions are displayed. PCP converts the number of writes to disk partitions from a counter value to a rate value. The `-f 1` argument specifies to abbreviate the values to one decimal place.

  Example output:

  ```
  metric:    disk.partitions.write
  host:      satellite.example.com
  semantics: cumulative counter (converting to rate)
  units:     count (converting to count / sec)
  samples:   all

                   vda1                  vda2                   sr0
                    0.0                  12.0                   0.0
                    0.0                   1.0                   0.0
                    0.0                   1.0                   0.0
                    0.0                   2.0                   0.0
  ```
- To print system performance summary every 2 seconds, enter the following command:

  ```
  # pmstat -t 2sec
  ```

## 5.3. Retrieving archived metrics

Use these commands to analyze historical performance data from PCP archive files, including viewing specific metrics over time ranges, comparing time periods, and investigating past performance issues on your Satellite.

- List all metrics that were enabled when the archive file was created:

  ```
  # pminfo --archive archive_file
  ```
- View the host and time period covered by an archive file:

  ```
  # pmdumplog -l archive_file
  ```
- List disk writes for each partition, over the time period covered by the archive file:

  ```
  # pmval --archive /var/log/pcp/pmlogger/satellite.example.com/20230831.00.10 \
    -f 1 disk.partitions.write
  ```
- List disk write operations per partition, with a 2-second interval, over the time period between 14:00 and 14:15:

  ```
  # pmval --archive /var/log/pcp/pmlogger/satellite.example.com/20230831.00.10 \
    -d -t 2sec \
    -f 3 disk.partitions.write \
    -S @14:00 -T @14:15
  ```
- List average values of all performance metrics, including the time and value of the minimum/maximum, over the time period between 14:00 and 14:30, and format the values as a table:

  ```
  # pmlogsummary /var/log/pcp/pmlogger/satellite.example.com/20230831.00.10 \
    -HlfiImM \
    -S @14:00 \
    -T @14:30 \
    disk.partitions.write \
    mem.freemem
  ```
- Display system metrics stored in an archive, starting from 14:00, in an interactive manner similar to the `top` tool:

  ```
  # pcp --archive /var/log/pcp/pmlogger/satellite.example.com/20230831.00.10 \
    -S @14:00 \
    atop
  ```

## 5.4. Retrieving metrics in the web UI

You can access the Grafana web interface to visualize Satellite performance metrics through customizable dashboards, making it easier to monitor trends and identify issues without using command-line tools.

**Procedure**

- Open the following URL in a browser: http://*satellite.example.com*:3000

**Additional resources**

- [Grafana Labs website](https://grafana.com/)
