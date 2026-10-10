---
title: "Metrics solution components"
product: "Red Hat Satellite"
version: "6.19"
guide: "monitoring_satellite_performance"
guide_title: "Monitoring Satellite performance"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/monitoring_satellite_performance/index#metrics-solution-components_monitoring"
---
# Chapter 2. Metrics solution components

The metrics monitoring solution uses multiple components to collect, store, and visualize Satellite performance data for analysis and troubleshooting.

Performance Co-Pilot (PCP)
:   Performance Co-Pilot is a suite of tools and libraries for acquiring, storing, and analyzing system-level performance measurements. You can use PCP to analyze live and historical metrics in the CLI.

Performance Metric Domain Agents (PMDA)
:   A Performance Metric Domain Agent is a PCP add-on that enables access to metrics of an application or service. To gather all metrics relevant to Satellite, you have to install PMDA for Apache HTTP Server and PostgreSQL.

Grafana
:   A web application that visualizes metrics collected by PCP. To analyze metrics in the web UI, you have to install Grafana and the Grafana PCP plugin.
