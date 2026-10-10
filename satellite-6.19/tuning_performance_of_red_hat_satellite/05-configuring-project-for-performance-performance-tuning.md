---
title: "Configuring Satellite for performance"
product: "Red Hat Satellite"
version: "6.19"
guide: "tuning_performance_of_red_hat_satellite"
guide_title: "Tuning performance of Red Hat Satellite"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/tuning_performance_of_red_hat_satellite/index#Configuring_Project_for_Performance_performance-tuning"
---
# Chapter 5. Configuring Satellite for performance

Satellite includes several components that communicate with each other. You can tune these components independently of each other to achieve the maximum possible performance for your scenario.

## 5.1. Considerations for performance tuning

You can optimize Satellite performance by adjusting various tunables to suit your workload.

Performance tuning requires careful testing in non-production environments with valid backups because most configuration changes require a Satellite restart. Setting up monitoring before applying changes helps you evaluate their effectiveness in your specific environment.

Our testing environment might be too far from what you will see although we are trying hard to mimic real world environment.

Optional: After any change, run this quick Satellite health check:

```
$ satellite-maintain health check
```

## 5.2. Puma tunings

Tune Puma to optimize Satellite performance for handling concurrent host operations and API requests. Proper Puma configuration is essential for deployments managing large numbers of hosts or frequent operations.

### 5.2.1. Puma workers and threads auto-tuning

Auto-tuning configures Puma workers and threads based on available CPU and memory to optimize Satellite performance. Understanding this default behavior helps you determine when manual tuning is necessary for your environment.

If you do not provide any Puma workers and thread values with `satellite-installer` or they are not present in your Satellite configuration, the `satellite-installer` configures a balanced number of workers. It follows this formula:

```
min(CPU_COUNT * 1.5, RAM_IN_GB - 1.5)
```

This should be fine for most cases, but with some usage patterns tuning is needed to either limit the amount of resources dedicated to Puma (so other Satellite components can use these) or for any other reason. Each Puma worker consumes around 1 GiB of RAM.

**View your current Satellite Server settings**

```
# cat /etc/systemd/system/foreman.service.d/installer.conf
```

**View the currently active Puma workers**

```
# systemctl status foreman
```

### 5.2.2. Manually tuning Puma workers and threads count

Manually configure Puma workers and threads count to optimize Satellite performance for your specific hardware and workload requirements when auto-tuning does not meet your needs.

For example, the following configuration uses two workers and five threads:

```
# satellite-installer \
--foreman-foreman-service-puma-workers 2 \
--foreman-foreman-service-puma-threads-max 5
```

### 5.2.3. Puma workers and threads recommendations

Configure Puma workers and threads based on your deployment size and hardware to optimize Satellite performance, especially for concurrent host registration workloads.

The main test used in this testing was concurrent registration with the following combinations along with different number of workers and threads. Our recommendation is based purely on concurrent registration performance, so it might not reflect your exact use-case. For example, if your setup is very content oriented with many publishes and promotes, you might want to limit resources consumed by Puma in favor of Pulp and PostgreSQL.

| Name | Number of hosts | RAM | Cores | Recommended Puma threads | Recommended Puma workers |
| --- | --- | --- | --- | --- | --- |
| default | 0 – 5000 | 20 GiB | 4 | 16 | 4 – 6 |
| medium | 5000 – 10000 | 32 GiB | 8 | 16 | 8 – 12 |
| large | 10000 – 20000 | 64 GiB | 16 | 16 | 12 – 18 |
| extra-large | 20000 – 60000 | 128 GiB | 32 | 16 | 16 – 24 |
| extra-extra-large | 60000+ | 256 GiB+ | 48+ | 16 | 20 – 26 |

Tuning number of workers is the more important aspect here and in some case we have seen up to 52% performance increase. Although installer uses 5 threads by default, we recommend 16 threads with all the tuning profiles in the table above. That is because we have seen up to 23% performance increase with 16 threads (14% for 8 and 10% for 32) when compared to setup with 4 threads.

To figure out these recommendations we used concurrent registrations test case which is a very specific use-case. It can be different on your Satellite which might have more balanced use-case (not only registrations). Keeping default 5 threads is a good choice as well.

These are some of our measurements that lead us to these recommendations:

|  | 4 workers, 4 threads | 4 workers, 8 threads | 4 workers, 16 threads | 4 workers, 32 threads |
| --- | --- | --- | --- | --- |
| Improvement | 0% | 14% | 23% | 10% |

Use 4 – 6 workers on a default setup (4 CPUs) – we have seen about 25% higher performance with 5 workers when compared to 2 workers, but 8% lower performance with 8 workers when compared to 2 workers – see table below:

|  | 2 workers, 16 threads | 4 workers, 16 threads | 6 workers, 16 threads | 8 workers, 16 threads |
| --- | --- | --- | --- | --- |
| Improvement | 0% | 26% | 22% | -8% |

Use 8 – 12 workers on a medium setup (8 CPUs) – see table below:

|  | 2 workers, 16 threads | 4 workers, 16 threads | 8 workers, 16 threads | 12 workers, 16 threads | 16 workers, 16 threads |
| --- | --- | --- | --- | --- | --- |
| Improvement | 0% | 51% | 52% | 52% | 42% |

Use 16 – 24 workers on a 32 CPUs setup (this was tested on a 90 GiB RAM machine and memory turned out to be a factor here as system started swapping – proper *extra-large* should have 128 GiB), higher number of workers was problematic for higher registration concurrency levels we tested, so we cannot recommend it.

|  | 4 workers, 16 threads | 8 workers, 16 threads | 16 workers, 16 threads | 24 workers, 16 threads | 32 workers, 16 threads | 48 workers, 16 threads |
| --- | --- | --- | --- | --- | --- | --- |
| Improvement | 0% | 37% | 44% | 52% | too many failures | too many failures |

### 5.2.4. Puma workers configuration

Configure Puma workers to scale Satellite performance based on available CPU resources. Adding more workers increases concurrent request capacity, improving registration times, and overall system responsiveness.

If you have enough CPUs, adding more workers adds more performance. For example, we have compared Satellite setups with 8 and 16 CPUs:

Table 5.1. satellite-installer options used to test effect of workers count

| Satellite VM with 8 CPUs, 40 GiB RAM | Satellite VM with 16 CPUs, 40 GiB RAM |
| --- | --- |
| `--foreman-foreman-service-puma-threads-max 16` | `--foreman-foreman-service-puma-threads-max 16` |
| `--foreman-foreman-service-puma-workers {2|4|8|16}` | `--foreman-foreman-service-puma-workers {2|4|8|16}` |

In 8 CPUs setup, changing the number of workers from 2 to 16, improved concurrent registration time by 36%. In 16 CPUs setup, the same change caused 55% improvement.

Adding more workers can also help with total registration concurrency Satellite can handle. In our measurements, setup with 2 workers were able to handle up to 480 concurrent registrations, but adding more workers improved the situation.

### 5.2.5. Puma threads configuration

Configure Puma threads to improve parallel host registration performance and optimize resource utilization per worker process in Satellite.

For example, we have compared these two setups:

| Satellite VM with 8 CPUs, 40 GiB RAM | Satellite VM with 8 CPUs, 40 GiB RAM |
| --- | --- |
| `--foreman-foreman-service-puma-threads-max 16` | `--foreman-foreman-service-puma-threads-max 8` |
| `--foreman-foreman-service-puma-workers 2` | `--foreman-foreman-service-puma-workers 4` |

Using more workers and the same total number of threads results in about 11% of speedup in highly concurrent registrations scenario. Moreover, adding more workers did not consume more CPU and RAM but gets more performance.

## 5.3. Apache HTTPD performance tuning

Tune Apache httpd to improve Satellite performance and increase concurrency for Satellite web UI and API requests.

Apache httpd forms a core part of the Satellite and acts as a web server for handling the requests sent through the Satellite web UI or exposed APIs.

### 5.3.1. Tuning Apache httpd child processes

You can tune Apache httpd child processes to handle more concurrent requests and prevent HTTP 503 errors and component failures during high load.

By default, httpd uses event request handling mechanism. When the number of requests to httpd exceeds the maximum number of child processes that can be launched to handle the incoming connections, httpd raises an HTTP 503 Service Unavailable error. Amidst httpd running out of processes to handle, the incoming connections can also result in multiple component failures on your Satellite services side due to the dependency of some components on the availability of httpd processes.

You can adapt the configuration of httpd event to handle more concurrent requests based on your expected peak load.

> **Warning**
>
> Configuring these numbers in `custom-hiera.yaml` locks them. If you change these numbers using `satellite-installer --tuning=My_Tuning_Option`, your `custom-hiera.yaml` will overwrite this setting. Set your numbers only if you have specific need for it.

**Procedure**

1. Modify the number of concurrent requests in `/etc/foreman-installer/custom-hiera.yaml` by changing or adding the following lines:

   ```
   apache::mod::event::serverlimit: 64
   apache::mod::event::maxrequestworkers: 1024
   apache::mod::event::maxrequestsperchild: 4000
   ```
2. Reconfigure your Satellite:

   ```
   # satellite-installer
   ```

   The example is identical to running `satellite-installer --tuning=medium` or higher on Satellite Server.

## 5.4. Tuning Dynflow

When you have many hosts checking in and running concurrent tasks, you can increase the number of Dynflow workers to improve Satellite task execution performance.

Dynflow is the workflow management system and task orchestrator which is a Satellite plugin and is used to execute the different tasks of Satellite in an out-of-order execution manner. Under the conditions when there are many hosts checking in on Satellite and running several tasks, Dynflow can take some help from an added tuning specifying how many executors it can launch.

For more information about the tunings involved related to Dynflow, see `https://satellite.example.com/foreman_tasks/sidekiq`.

Satellite contains a Dynflow service called `dynflow-sidekiq` that performs tasks scheduled by Dynflow. Sidekiq workers can be grouped into various queues to ensure that many tasks of one type will not block execution of tasks of other type.

Red Hat recommends increasing the number of sidekiq workers to scale the Foreman tasking system for bulk concurrent tasks. Typical concurrent tasks are multiple content view publications and promotions, content synchronizations, and synchronizations to Capsule Servers. There are two options available:

- You can increase the number of threads used by a worker (worker’s concurrency). This has limited impact for values larger than five due to Ruby implementation of the concurrency of threads.
- You can increase the number of workers, which is recommended.

**Procedure**

1. Increase the number of workers from one worker to three while remaining five threads/concurrency of each:

   ```
   # satellite-installer --foreman-dynflow-worker-instances 3    # optionally, add --foreman-dynflow-worker-concurrency 5
   ```
2. Optional: Check if there are three worker services:

   ```
   # systemctl -a | grep dynflow-sidekiq@worker-[0-9]
   dynflow-sidekiq@worker-1.service        loaded    active   running   Foreman jobs daemon - worker-1 on sidekiq
   dynflow-sidekiq@worker-2.service        loaded    active   running   Foreman jobs daemon - worker-2 on sidekiq
   dynflow-sidekiq@worker-3.service        loaded    active   running   Foreman jobs daemon - worker-3 on sidekiq
   ```

**Additional resources**

- [How to add sidekiq workers in Satellite6?](https://access.redhat.com/solutions/6293741)

## 5.5. Pull-based REX transport tuning

You can adjust MQTT broker settings and client polling intervals to optimize pull-based remote execution performance for the scale and network conditions of your environment.

**Additional resources**

- [Transport modes for remote execution in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#transport-modes-for-remote-execution_managing-hosts)

### 5.5.1. Increasing host limit for pull-based REX transport

Tune the `mosquitto` MQTT server on your Capsule to support more than the default limit of 1024 connected hosts when scaling pull-based remote execution to larger deployments.

**Prerequisites**

- You have enabled pull-based remote execution on your Capsule. For more information, see [Configuring pull-based transport for remote execution](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-pull-based-transport-for-remote-execution_capsule) in *Installing Capsule Server*.

**Procedure**

1. On your Capsule, set the upper limit of connected hosts for pull-based remote execution in `/etc/foreman-installer/custom-hiera.yaml`:

   ```yaml
   systemd::dropin_files:
     limits.conf:
       unit: mosquitto.service
       content: "[Service]\nLimitNOFILE=5000\n"
   ```

   This example configures the `mosquitto` service on your Capsule to handle up to 5000 hosts.
2. Re-run the installer for the changes to take effect:

   ```
   # satellite-installer
   ```

### 5.5.2. Decreasing performance impact of the pull-based REX transport

Configure MQTT rate limiting and timing parameters to prevent connection exhaustion on Capsule Server when running high-concurrency remote execution jobs in pull-based mode.

When Satellite Server is configured with the pull-based transport mode for remote execution jobs by using the Script provider, Capsule Server sends notifications about new jobs to hosts through MQTT. This notification does not include the actual workload that the host is supposed to execute. After a host receives a notification about a new remote execution job, it queries Capsule Server for its actual workload. During the job, the host periodically sends outputs of the job to Capsule Server, further increasing the number of requests to Capsule Server.

These requests to Capsule Server together with high concurrency allowed by the MQTT protocol can cause exhaustion of available connections on Capsule Server. Some requests might fail, making some child tasks of remote execution jobs unresponsive. This also depends on actual job workload, as some jobs are causing additional load to Satellite Server, making it compete for resources if hosts are registered to Satellite Server.

To avoid this, configure your Satellite Server and Capsule Server with the following parameters:

- MQTT Time To Live – Time interval in seconds given to the host to pick up the job before considering the job undelivered
- MQTT Resend Interval – Time interval in seconds at which the notification should be re-sent to the host until the job is picked up or canceled
- MQTT Rate Limit – Number of jobs that are allowed to run at the same time. You can limit the concurrency of remote execution by tuning the rate limit which means you are going to put more load on Satellite.

Capsule Server uses Webrick HTTP server (no httpd or Puma involved), so there is no simple way to increase its capacity.

**Procedure**

- Tune the MQTT parameters on your Satellite Server:

  ```
  # satellite-installer \
  --foreman-proxy-plugin-remote-execution-script-mqtt-rate-limit My_MQTT_Rate_Limit \
  --foreman-proxy-plugin-remote-execution-script-mqtt-resend-interval My_MQTT_Resend_Interval \
  --foreman-proxy-plugin-remote-execution-script-mqtt-ttl My_MQTT_Time_To_Live
  ```

## 5.6. Tuning PostgreSQL

Configure PostgreSQL database settings in Satellite to improve response times and operational performance. Tuning PostgreSQL reduces database query latency and enhances overall system responsiveness, especially in environments with high database activity.

The PostgreSQL authors recommend disabling Transparent Hugepage on servers running PostgreSQL. For more information, see [Section 4.2, “Transparent Hugepage and database performance”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/tuning_performance_of_red_hat_satellite/index#transparent-hugepage-and-database-performance "4.2. Transparent Hugepage and database performance").

You can apply a set of tunings to PostgreSQL to improve its response times, which will modify the `postgresql.conf` file. You can use this to effectively tune down your Satellite instance irrespective of a tuning profile.

**Procedure**

1. Append `/etc/foreman-installer/custom-hiera.yaml` to tune PostgreSQL:

   ```yaml
   postgresql::server::config_entries:
     max_connections: 1000
     shared_buffers: 2GB
     work_mem: 8MB
     autovacuum_vacuum_cost_limit: 2000
   ```

   This tuning configuration alters the following keys:

   `max_connections`
   :   The key defines the maximum number of connections that can be accepted by the PostgreSQL processes that are running.

   `shared_buffers`
   :   The shared buffers define the memory used by all the active connections inside PostgreSQL to store the data for the different database operations. An optimal value for this will vary between 2 GiB to a maximum of 25% of your total system memory depending upon the frequency of the operations being conducted on Satellite.

   `work_mem`
   :   The work_mem is the memory that is allocated on per process basis for PostgreSQL and is used to store the intermediate results of the operations that are being performed by the process. Setting this value to 8 MB should be more than enough for most of the intensive operations on Satellite.

   `autovacuum_vacuum_cost_limit`
   :   The key defines the cost limit value for the vacuuming operation inside the autovacuum process to clean up the dead tuples inside the database relations. The cost limit defines the number of tuples that can be processed in a single run by the process. Red Hat recommends setting the value to `2000` as it is for the *medium*, *large*, *extra-large*, and *extra-extra-large* profiles, based on the general load that Satellite pushes on the PostgreSQL server process.
2. Reconfigure your Satellite:

   ```
   # satellite-installer
   ```

### 5.6.1. Benchmarking raw database performance

Use `pgbench` to measure raw PostgreSQL performance and validate storage behavior on your Satellite environment. Benchmarking helps you establish baseline performance metrics and verify that tuning changes improve database responsiveness.

**Prerequisites**

- A non-production system with a valid backup.

> **Warning**
>
> - Never run benchmarks on a production system or without a valid backup.
> - Before you start testing, determine how large the database files are. Testing with a very small database does not produce meaningful results. For example, if the database is only 20 GiB and the buffer pool is 32 GiB, the benchmark does not show problems with a large number of connections because the data fits entirely in the buffer pool.

**Procedure**

1. To identify the largest tables by disk space for Candlepin, Foreman, and Pulp, use the [postgres-size-report](https://github.com/RedHatSatellite/satellite-support/blob/master/postgres-size-report) script in the [satellite-support](https://github.com/RedHatSatellite/satellite-support) Git repository. For more information, see [github.com/RedHatSatellite/satellite-support](https://github.com/RedHatSatellite/satellite-support).
2. Ensure the PostgreSQL data directory `/var/lib/pgsql` has enough space for the benchmark workload. You might need to resize the volume to 100 GiB or more, depending on how long the benchmark runs and how much data it generates.

   > **Note**
   >
   > Choice of filesystem for PostgreSQL data directory might matter as well.
3. Install the PGBench utility:

   ```
   # dnf install postgresql-contrib
   ```

## 5.7. Redis tuning

Understanding Redis tuning in Satellite helps you optimize caching and task tracking performance. Properly configured Redis ensures stable memory consumption and improves responsiveness of Satellite operations.

Redis is an in-memory data store. Foreman and Pulp use Redis for caching and Dynflow uses Redis to track its tasks. Given the way Satellite uses Redis, its memory consumption should be stable.

The Redis authors recommend disabling Transparent Hugepage on servers running Redis.

**Additional resources**

- [Section 4.2, “Transparent Hugepage and database performance”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/tuning_performance_of_red_hat_satellite/index#transparent-hugepage-and-database-performance "4.2. Transparent Hugepage and database performance")

## 5.8. Capsule configuration tuning

Understanding Capsule tuning helps you optimize load distribution and content delivery across different networks in your Satellite environment. Properly configured Capsules reduce load on your Satellite Server and improve performance for remote execution and content distribution tasks.

What Capsules cannot help with is anything which extensively uses Satellite API, such as host registration or package profile update.

### 5.8.1. Capsule performance tests

Review performance test results for different Capsule hardware configurations to determine the optimal sizing for your deployment. Understanding these benchmarks helps you choose the right resources based on your expected workload for content delivery, host registration, and remote execution tasks.

Red Hat tested the following configurations:

| Capsule HW configuration | CPUs | RAM |
| --- | --- | --- |
| minimal | 4 | 12 GiB |
| large | 8 | 24 GiB |
| extra large | 16 | 46 GiB |

Content delivery use case
:   In a download test where we concurrently downloaded a 40MB repo of 2000 packages on 100, 200, .. 1000 hosts, we saw roughly 50% improvement in average download duration every time when we doubled Capsule Server resources. For more precise numbers, see the table below.

| Concurrent downloading hosts | Minimal (4 CPU and 12 GiB RAM) → Large (8 CPU and 24 GiB RAM) | Large (8 CPU and 24 GiB RAM) → Extra Large (16 CPU and 46 GiB RAM) | Minimal (4 CPU and 12 GiB RAM) → Extra Large (16 CPU and 46 GiB RAM) |
| --- | --- | --- | --- |
| Average Improvement | ~ 50% (e.g. for 700 concurrent downloads in average 9 seconds vs. 4.4 seconds per package) | ~ 40% (e.g. for 700 concurrent downloads in average 4.4 seconds vs. 2.5 seconds per package) | ~ 70% (e.g. for 700 concurrent downloads in average 9 seconds vs. 2.5 seconds per package) |

When we compared download performance from Satellite Server vs. from Capsule Server, we have seen only about 5% speedup, but that is expected as Capsule Server’s main benefit is in getting content closer to geographically distributed clients (or clients in different networks) and in handling part of the load Satellite Server would have to handle itself. In some smaller hardware configurations (8 CPUs and 24 GiB), Satellite Server was not able to handle downloads from more than 500 concurrent clients, while a Capsule Server with the same hardware configuration was able to service more than 1000 and possibly even more.

Concurrent registrations use case
:   For concurrent registrations, a bottleneck is usually CPU speed, but all configs were able to handle even high concurrency without swapping. Hardware resources used for Capsule have only minimal impact on registration performance. For example, Capsule Server with 16 CPUs and 46 GiB RAM have at most a 9% registration speed improvement when compared to a Capsule Server with 4 CPUs and 12 GiB RAM. During periods of very high concurrency, you might experience timeouts in the Capsule Server to Satellite Server communication. You can alleviate this by increasing the default timeout by using the following tunable in `/etc/foreman-installer/custom-hiera.yaml`:

```
apache::mod::proxy::proxy_timeout: 600
```

Remote execution use case
:   We have tested executing remote execution jobs by using both SSH and Ansible backend on 500, 2000 and 4000 hosts. All configurations were able to handle all of the tests without errors, except for the smallest configuration (4 CPUs and 12 GiB memory) which failed to finish on all 4000 hosts.
