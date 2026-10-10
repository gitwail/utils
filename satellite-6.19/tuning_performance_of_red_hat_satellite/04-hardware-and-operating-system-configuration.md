---
title: "Hardware and operating system configuration"
product: "Red Hat Satellite"
version: "6.19"
guide: "tuning_performance_of_red_hat_satellite"
guide_title: "Tuning performance of Red Hat Satellite"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/tuning_performance_of_red_hat_satellite/index#hardware-and-operating-system-configuration"
---
# Chapter 4. Hardware and operating system configuration

You can tune the hardware and operating system to optimize Satellite performance for your scenario.

CPU
:   The more physical cores that are available to Satellite, the higher throughput can be achieved for the tasks. Some of the Satellite components such as Puppet and PostgreSQL are CPU intensive applications and can really benefit from the higher number of available CPU cores.

Memory
:   The higher amount of memory available in the system running Satellite, the better will be the response times for the Satellite operations. Since Satellite uses PostgreSQL as the database solutions, any additional memory coupled with the tunings will provide a boost to the response times of the applications due to increased data retention in the memory.

Disk
:   Satellite should be deployed using SSDs to avoid performance bottlenecks. Components such as PostgreSQL benefit from using SSDs due to their lower latency compared to HDDs.

Network
:   The communication between the Satellite Server and Capsules is impacted by the network performance. A decent network with a minimum jitter and low latency is required to enable hassle free operations such as Satellite Server and Capsules synchronization. At the very least, ensure it is not causing connection resets and similar problems.

Server Power Management
:   Your server by default is likely to be configured to conserve power. While this is a good approach to keep the max power consumption in check, it also has a side effect of lowering the performance that Satellite can achieve. For a server running Satellite, it is recommended to set the BIOS to enable the system to be run in performance mode to boost the maximum performance levels that Satellite can achieve.

## 4.1. Enabling tuned profiles

Enable tuned profiles to automatically optimize the performance settings of Satellite for its workloads. This improves overall system performance by applying configuration optimizations tailored to your environment.

**Procedure**

1. Install `tuned` on your Capsule:

   ```
   # satellite-maintain packages install tuned
   ```
2. Check if `tuned` is running:

   ```
   # systemctl status tuned
   ```
3. If `tuned` is not running, enable it:

   ```
   # systemctl enable --now tuned
   ```
4. Optional: View a list of available `tuned` profiles:

   ```
   # tuned-adm list
   ```
5. Enable a `tuned` profile depending on your scenario:

   ```
   # tuned-adm profile "My_Tuned_Profile"
   ```

## 4.2. Transparent Hugepage and database performance

Disable Transparent Hugepage to improve database performance in Satellite, especially for PostgreSQL and Redis workloads that perform poorly with this memory management feature enabled.

Transparent Hugepage is a memory management technique used by the Linux kernel to reduce the overhead of using the Translation Lookaside Buffer (TLB) by using larger sized memory pages. Due to databases having Sparse Memory Access patterns instead of Contiguous Memory access patterns, database workloads often perform poorly when Transparent Hugepage is enabled.

In deployments with databases running on separate servers, the benefit of using Transparent Hugepage on the Satellite Server might be limited.

**Additional resources**

- [How to disable transparent hugepages (THP) on Red Hat Enterprise Linux](https://access.redhat.com/solutions/1320153)
