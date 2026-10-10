---
title: "Setting up the metrics monitoring solution"
product: "Red Hat Satellite"
version: "6.19"
guide: "monitoring_satellite_performance"
guide_title: "Monitoring Satellite performance"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/monitoring_satellite_performance/index#setting-up-the-metrics-monitoring-solution_monitoring"
---
# Chapter 3. Setting up the metrics monitoring solution

The metrics monitoring solution uses Performance Co-Pilot (PCP) to collect and analyze system performance data, helping you find slowdowns and improve resource usage.

## 3.1. Installing PCP

Install Performance Co-Pilot (PCP) packages and enable the data collection daemons to begin gathering system performance metrics on your Satellite Server.

**Prerequisites**

- Ensure you have a minimum of 20 GB space available in the `/var/log/pcp` directory.

  With the default PCP data retention settings, data storage is estimated to use between 100 MB and 500 MB of disk space per day, but might use up to several gigabytes over time. For more information, see [Chapter 4, *Metrics data retention*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/monitoring_satellite_performance/index#metrics-data-retention_monitoring "Chapter 4. Metrics data retention").

**Procedure**

1. Install the PCP packages:

   ```
   # satellite-maintain packages install pcp \
   pcp-pmda-apache \
   pcp-pmda-openmetrics \
   pcp-pmda-postgresql \
   pcp-pmda-redis \
   pcp-system-tools \
   foreman-pcp
   ```
2. Enable and start the Performance Metrics Collector daemon and Performance Metrics Logger daemon:

   ```
   # systemctl enable --now pmcd pmlogger
   ```

## 3.2. Configuring PCP data collection

Configure PCP to collect detailed performance data from Satellite processes and services, such as Apache HTTP Server, PostgreSQL, and Redis to enable complete monitoring.

**Procedure**

1. Symlink the Satellite-specific configuration to PMDA process monitoring:

   ```
   # ln -s /etc/pcp/proc/foreman-hotproc.conf /var/lib/pcp/pmdas/proc/hotproc.conf
   ```

   By default, PCP only collects basic system metrics. This step enables detailed metrics about the following Satellite processes:

   - Java
   - PostgreSQL
   - Redis
   - Dynflow
   - Puma
   - Pulpcore
2. Install the process monitoring PMDA:

   ```
   # cd /var/lib/pcp/pmdas/proc
   # ./Install
   ```
3. Configure PCP to collect metrics from Apache HTTP Server.

   1. Enable the Apache HTTP Server extended status module:

      ```
      # satellite-installer --enable-apache-mod-status
      ```
   2. Enable the Apache HTTP Server PMDA:

      ```
      # cd /var/lib/pcp/pmdas/apache
      # ./Install
      ```
4. Configure PCP to collect metrics from PostgreSQL:

   ```
   # cd /var/lib/pcp/pmdas/postgresql
   # ./Install
   ```
5. Configure PCP to collect metrics from Redis:

   ```
   # cd /var/lib/pcp/pmdas/redis
   # ./Install
   ```
6. Enable the telemetry feature in Satellite:

   ```
   # satellite-installer --foreman-telemetry-prometheus-enabled true
   ```
7. Configure PCP to collect data from Satellite:

   ```
   # cd /var/lib/pcp/pmdas/openmetrics
   # echo "https://satellite.example.com/metrics" > config.d/foreman.url
   # ./Install
   ```
8. Restart PCP to begin data collection:

   ```
   # systemctl restart pmcd pmlogger pmproxy
   ```

## 3.3. Verifying PCP configuration

Verify that PCP is configured correctly and all monitoring services are running to ensure data collection is working as expected.

**Procedure**

- Print a summary of the active PCP configuration:

  ```
  # pcp
  ```

  Example output of the `pcp` command:

  ```
  Performance Co-Pilot configuration on satellite.example.com:

   platform: Linux satellite.example.com 4.18.0-372.32.1.el8_6.x86_64 #1 SMP Fri Oct 7 12:35:10 EDT 2022 x86_64
   hardware: 16 cpus, 2 disks, 1 node, 31895MB RAM
   timezone: UTC
   services: pmcd pmproxy
       pmcd: Version 5.3.7-17, 13 agents, 4 clients
       pmda: root pmcd proc pmproxy xfs redis linux apache mmv kvm
             postgresql jbd2 openmetrics
   pmlogger: primary logger: /var/log/pcp/pmlogger/satellite.example.com/20230831.00.10
       pmie: primary engine: /var/log/pcp/pmie/satellite.example.com/pmie.log
  ```

  In this example, both the Performance Metrics Collector Daemon (pmcd) and Performance Metrics Proxy Daemon (pmproxy) services are running. It also confirms the PMDA that are collecting metrics. Finally, it lists the active log file, in which `pmlogger` is currently storing metrics.

## 3.4. Enabling web UI access to metrics

Enable web UI access to metrics by installing Grafana to visualize performance data through interactive dashboards.

**Procedure**

1. Install Grafana and the Grafana PCP plugin on your Satellite Server:

   ```
   # satellite-maintain packages install grafana grafana-pcp
   ```
2. Start and enable the Grafana web service and the PCP proxy service:

   ```
   # systemctl enable --now pmproxy grafana-server
   ```
3. Open the firewall port to allow access to the Grafana web interface:

   ```
   # firewall-cmd --permanent --add-service=grafana
   ```
4. Reload the firewall configuration to apply the changes:

   ```
   # firewall-cmd --reload
   ```
5. Install PCP Redis and configure Grafana to load it. For more information, see [Configuring PCP Redis](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/setting-up-graphical-representation-of-pcp-metrics_monitoring-and-managing-system-status-and-performance#configuring-pcp-redis_setting-up-graphical-representation-of-pcp-metrics) in *Red Hat Enterprise Linux 9 Monitoring and managing system status and performance*.
6. Access the Grafana web UI, enable the PCP plugin, and add PCP Redis as a data source. For more information, see [Accessing the Grafana web UI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/monitoring_and_managing_system_status_and_performance/setting-up-graphical-representation-of-pcp-metrics_monitoring-and-managing-system-status-and-performance#accessing-the-grafana-web-ui_setting-up-graphical-representation-of-pcp-metrics) in *Red Hat Enterprise Linux 9 Monitoring and managing system status and performance*.
