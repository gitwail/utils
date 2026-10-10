---
title: "Increasing logging levels of Satellite components"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "C"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#increasing-logging-levels-of-satellite-components"
---
# Appendix C. Increasing logging levels of Satellite components

Satellite components use configurable logging levels to record operational events. Increase the level to `debug` when you need detailed output to troubleshoot a specific service.

## C.1. Increasing the logging level for Foreman

Increase Foreman logging to `debug` to capture detailed Satellite activity when diagnosing application or API issues. Reset the level when debugging is complete to avoid excessive log volume.

By default, Foreman writes logs to `/var/log/foreman/production.log`. For more information, see [Section B.2, “Configuring logging type and layout”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#configuring-logging-type-and-layout "B.2. Configuring logging type and layout").

> **Note**
>
> For more information about Satellite logging settings, use `satellite-installer` with the `--full-help` option:
>
> ```
> # satellite-installer --full-help | grep logging
> ```

**Procedure**

1. Set the logging level to `debug`:

   ```
   # satellite-installer --foreman-logging-level debug
   ```
2. After you complete debugging, reset the logging level to the default value:

   ```
   # satellite-installer --reset-foreman-logging-level
   ```

## C.2. Increasing the logging level for Red Hat Lightspeed in Satellite

Increase Red Hat Lightspeed in Satellite logging to `DEBUG` to capture detailed diagnostic output when troubleshooting Red Hat Lightspeed operations on your Satellite Server.

**Example C.1. Log entries of Red Hat Lightspeed in Satellite**

```
Feb  3 10:39:54 satellite.example.com iop-core-engine[213708]: INFO:insights.core.dr:Trying telemetry.rules.plugins.sap.sap_hana_loose_sudo.check_group_members
Feb  3 10:39:54 satellite.example.com iop-core-engine[213708]: INFO:insights.core.dr:Trying telemetry.rules.plugins.sap.sap_hana_loose_sudo.report
Feb  3 10:39:54 satellite.example.com iop-core-engine[213708]: INFO:insights.core.dr:Trying telemetry.rules.plugins.ros.ros_instance_evaluation.find_solution
Feb  3 10:39:54 satellite.example.com iop-core-engine[213708]: INFO:insights.core.dr:Trying telemetry.rules.plugins.ros.ros_instance_evaluation.report
Feb  3 10:39:54 satellite.example.com iop-core-engine[213708]: INFO:insights_kafka_service.consumer:Completed processing request id 4be0099772a23aad477e493990247876
Feb  3 10:39:54 satellite.example.com iop-core-engine[213708]: INFO:insights_messaging.consumers.kafka:Completed one payload
```

The default logging levels for Red Hat Lightspeed in Satellite are as follows:

```
loggers:
  insights.core.dr:
    level: "ERROR"
  insights_messaging:
    level: "INFO"
  insights_kafka_service:
    level: "INFO"
  "":
    level: "INFO"
```

**Prerequisites**

- You have installed Red Hat Lightspeed in Satellite on your Satellite Server. For more information, see the following resources:

  - [Installing and configuring Red Hat Lightspeed in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#installing-and-configuring-red-hat-lightspeed-in-satellite) in *Installing Satellite Server in a connected network environment*
  - [Installing and configuring Red Hat Lightspeed in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#installing-and-configuring-red-hat-lightspeed-in-satellite) in *Installing Satellite Server in a disconnected network environment*

**Procedure**

- Increase the logging levels to `DEBUG`:

  ```
  # satellite-installer \
  --iop-core-engine-log-level-insights-core-dr DEBUG \
  --iop-core-engine-log-level-insights-kafka-service DEBUG \
  --iop-core-engine-log-level-insights-messaging DEBUG \
  --iop-core-engine-log-level-root DEBUG
  ```

**Verification**

- Check the logging levels of Red Hat Lightspeed in Satellite:

  ```
  # podman exec iop-core-engine cat /var/config.yml | grep -A15 "logging:"
  ```

## C.3. Increasing the logging level for Hammer

Increase Hammer logging to `debug` to capture detailed CLI activity when troubleshooting command-line errors or API responses.

Hammer writes logs to `~/.hammer/log/hammer.log`.

**Procedure**

- In `/etc/hammer/cli_config.yml`, set the `:log_level:` option to `debug`:

  ```yaml
  :log_level: 'debug'
  ```

## C.4. Increasing the logging level for Capsule

Increase Capsule logging to `debug` to capture detailed Capsule activity when troubleshooting communication between Satellite and hosts. Reset the level when debugging is complete to avoid excessive log volume.

By default, Capsule writes logs to `/var/log/foreman-proxy/proxy.log`. For more information, see [Section B.2, “Configuring logging type and layout”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#configuring-logging-type-and-layout "B.2. Configuring logging type and layout").

**Procedure**

1. Set the logging level to `debug`:

   ```
   # satellite-installer --foreman-proxy-log-level DEBUG
   ```
2. After you complete debugging, reset the logging level to the default value:

   ```
   # satellite-installer --reset-foreman-proxy-log-level
   ```

## C.5. Increasing the logging level for Candlepin

Increase Candlepin logging to `DEBUG` when you need detailed subscription and content management diagnostics on your Red Hat Satellite.

Candlepin writes logs to `/var/log/candlepin/candlepin.log` and `/var/log/candlepin/error.log`.

**Procedure**

1. Set the logging level to `DEBUG`:

   ```
   # satellite-installer --katello-candlepin-loggers log4j.logger.org.candlepin:DEBUG
   ```

   If the candlepin log files are too verbose, you can decrease the default debug level:

   ```
   # satellite-installer \
   --katello-candlepin-loggers log4j.logger.org.candlepin:DEBUG \
   --katello-candlepin-loggers log4j.logger.org.candlepin.resource.ConsumerResource:WARN \
   --katello-candlepin-loggers log4j.logger.org.candlepin.resource.HypervisorResource:WARN
   ```
2. After you complete debugging, reset the logging level to the default value:

   ```
   # satellite-installer --reset-katello-candlepin-loggers
   ```

## C.6. Increasing the logging level for Redis

Increase Redis logging to `debug` to capture detailed cache activity when troubleshooting performance or connectivity issues.

Redis writes logs to `/var/log/redis/redis.log`.

**Procedure**

1. In `/etc/redis/redis.conf`, set the logging level to `debug`:

   ```
   loglevel debug
   ```
2. Restart the Redis service:

   ```
   # systemctl restart redis
   ```

   > **Note**
   >
   > Running `satellite-installer` will revert the setting to default.

## C.7. Increasing the logging level for satellite-installer

Increase `satellite-installer` verbose output to `debug` when you need detailed installation and configuration diagnostics during setup or upgrades.

**Procedure**

- Increase the logging level of the `satellite-installer` utility:

  ```
  # satellite-installer --verbose-log-level debug
  ```

  Note that this only affects standard output but not any log files written to disk.

## C.8. Increasing the logging level for Pulp

Increase Pulp logging to `DEBUG` when you need detailed content repository diagnostics.

Pulp writes logs to the systemd journal. You can view them with `journalctl --unit 'pulpcore*'`.

**Procedure**

1. In `/etc/pulp/settings.py`, set the logging level to `DEBUG`:

   ```
   LOGGING = {"dynaconf_merge": True, "loggers": {'': {'handlers': ['console'], 'level': 'DEBUG'}}}
   ```
2. Restart the Pulp services:

   ```
   # systemctl restart \
   pulpcore-api \
   pulpcore-content \
   pulpcore-resource-manager \
   pulpcore-worker@\*
   ```

   > **Note**
   >
   > Running `satellite-installer` will revert the setting to default.

## C.9. Increasing the logging level for OpenVox agent

Increase OpenVox agent logging to `debug` when you need detailed configuration application diagnostics on hosts.

OpenVox agent writes logs to `/var/log/puppetlabs/puppet/`.

**Prerequisites**

- You have enabled Puppet on your Satellite. For more information, see [Enabling Puppet integration with Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#enabling-puppet-integration-with-satellite) in *Managing configurations by using Puppet integration*.

**Procedure**

- Set the logging level to `debug`:

  ```
  # satellite-installer --puppet-agent-additional-settings log_level:debug
  ```

## C.10. Increasing the logging level for OpenVox server

Increase OpenVox server logging to `debug` when you need detailed catalog compilation and agent communication diagnostics.

OpenVox server writes logs to `/var/log/puppetlabs/puppetserver/`.

**Prerequisites**

- You have enabled Puppet on your Satellite. For more information, see [Enabling Puppet integration with Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#enabling-puppet-integration-with-satellite) in *Managing configurations by using Puppet integration*.

**Procedure**

- Set the logging level to `debug`:

  ```
  # satellite-installer --puppet-server-additional-settings log_level:debug
  ```
