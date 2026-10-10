---
title: "Logging and reporting problems"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "B"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#Logging_and_Reporting_Problems_admin"
---
# Appendix B. Logging and reporting problems

Review the most commonly used log files and debugging tools available in Satellite.

## B.1. Configuring logging levels with Hammer CLI

You can use Hammer to log debugging information for various Satellite components. The default logging level is `INFO`.

- To list the components whose logging level you can change by using `hammer`:

  ```
  $ hammer admin logging --list
  ```
- To set `DEBUG` level logging for all components:

  ```
  $ hammer admin logging --all --level-debug
  # satellite-maintain service restart
  ```
- To set `PRODUCTION` level logging for all components:

  ```
  $ hammer admin logging --all --level-production
  # satellite-maintain service restart
  ```
- To set `DEBUG` level logging for a specific component:

  ```
  $ hammer admin logging --components My_Component --level-debug
  # satellite-maintain service restart
  ```
- To list all available logging options:

  ```
  $ hammer admin logging --help
  ```

**Additional resources**

- [Using the Hammer CLI tool](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#)

## B.2. Configuring logging type and layout

By default, Satellite uses file-based logging. You can use `satellite-installer` to change the logging type and logging layout.

**Procedure**

1. To use the `journald` service for logging:

   1. Change the logging type to `journald`:

      ```
      # satellite-installer \
      --foreman-logging-type journald \
      --foreman-proxy-log JOURNAL
      ```
   2. Inspect the log messages by using the `journalctl` utility. For example:

      - `journalctl --unit foreman` and `journalctl --unit foreman-proxy` show messages for the `foreman` and `foreman-proxy` units
      - `journalctl REQUEST=request_ID` shows messages for a specified request
2. To use file-based logging:

   1. Change the logging type to file-based:

      ```
      # satellite-installer \
      --reset-foreman-logging-type \
      --reset-foreman-proxy-log
      ```
   2. Inspect the log messages by viewing these files:

      - `/var/log/foreman/production.log`
      - `/var/log/foreman-proxy.log`
3. To use JSON output:

   1. Change the logging layout to JSON:

      ```
      # satellite-installer \
      --foreman-logging-layout json \
      --foreman-logging-type file
      ```
   2. Inspect the log messages by using `jq`:

      ```
      # cat /var/log/foreman/production.log | jq
      ```

**Additional resources**

- [Viewing logs using the command line in *Red Hat Enterprise Linux 9 Configuring basic system settings*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/configuring_basic_system_settings/index#viewing-logs-using-the-command-line_assembly_troubleshooting-problems-using-log-files)

## B.3. Enabling individual loggers for selective debugging

You can enable individual loggers to collect detailed diagnostics for specific Satellite components when you troubleshoot integration or performance issues, without increasing the global logging level.

**Procedure**

1. Enable the required individual loggers. For example, to enable `sql` and `ldap` loggers, enter the following command:

   ```
   # satellite-installer \
   --foreman-loggers ldap:true \
   --foreman-loggers sql:true
   ```
2. Optional: Reset all loggers to their default values:

   ```
   # satellite-installer --reset-foreman-loggers
   ```

## B.4. Overview of individual loggers

Review selected loggers and their default values. You can find the complete list of loggers with their default values in `/usr/share/foreman/config/application.rb` under `Foreman::Logging.add_loggers`.

`app`
:   Logs web requests and all general application messages.

    Default value: true.

`audit`
:   Logs additional fact statistics, numbers of added, updated, and removed facts.

    Default value: true.

`background`
:   Logs information from the background processing component.

`blob`
:   Logs contents of rendered templates for auditing purposes.

    > **Important**
    >
    > The `blob` logger might contain sensitive data.

`dynflow`
:   Logs information from the Dynflow process.

`ldap`
:   Logs high level LDAP queries and LDAP operations.

    Default value: false.

`notifications`
:   Logs information from the notifications component.

`permissions`
:   Logs queries to user roles, filters, and permissions when loading pages.

    Default value: false.

`sql`
:   Logs SQL queries made through Rails ActiveRecord.

    Default value: false.

`telemetry`
:   Logs debugging information from telemetry.

`templates`
:   Logs information from the template renderer component.

## B.5. Retrieving the status of services by using Hammer CLI

Satellite uses a set of back-end services. When troubleshooting, you can check the status of Satellite services by using Hammer CLI.

**Procedure**

- Get information from the database and Satellite services:

  ```
  $ hammer ping
  ```
- Check the status of the services running in systemd:

  ```
  # satellite-maintain service status
  ```

  Run `satellite-maintain service --help` for more information.
- Perform a health check:

  ```
  $ satellite-maintain health check
  ```

  Run `satellite-maintain health --help` for more information.

## B.6. Restarting Satellite services

Satellite uses a set of back-end services. When troubleshooting, you can restart the services if needed.

**Procedure**

- Restart Satellite services:

  ```
  # satellite-maintain service restart
  ```

## B.7. Utilities for processing log information

You can collect information from log files to troubleshoot Satellite.

sosreport
:   The `sos report` command collects configuration and diagnostic information from a Linux system, such as the running kernel version, loaded modules, running services, and system and service configuration files. Additionally, it collects information about Red Hat Satellite, such as its back-end services and tasks. This output is stored in a tar file located at `/var/tmp/sosreport-XXX-20171002230919.tar.xz`.

    For more information, run `sos report --help` or see [What is a sosreport and how can I create one?](https://access.redhat.com/solutions/3592) in the *Red Hat Knowledgebase*.

    > **Important**
    >
    > The `sos report` command removes security information such as passwords, tokens, and keys while collecting information. However, the tar files can still contain sensitive information about the Satellite Server. Send the tar files directly to the intended recipient and not to a public target.

foreman-tail
:   The `foreman-tail` command displays Satellite logs in real time.

    For more information, see the `foreman-tail(8)` man page.

## B.8. Log file directories

The following table provides an overview of selected log directories on Satellite Server.

| Log file directory | Description of log file content |
| --- | --- |
| `/var/log/candlepin/` | Subscription management |
| `/var/log/foreman-installer/` | Installer |
| `/var/log/foreman-maintain/` | Foreman maintain |
| `/var/log/foreman-proxy/` | Foreman proxy |
| `/var/log/foreman/` | Foreman |
| `/var/log/httpd/` | Apache HTTP server |
| `/var/log/messages/` | Various other log messages |
| `/var/log/puppetlabs/puppet/` | Puppet |
| `/var/log/tomcat/` | Candlepin web service logs |

## B.9. System journal metadata

The `journald` service uses metadata fields to filter logs. You can use these fields to filter logs when troubleshooting.

AUDIT_ACTION
:   Audit action performed

    Example: Create, update, or delete

AUDIT_TYPE
:   Audit resource type

    Example: Host, Subnet, or ContentView

AUDIT_ID
:   Audit resource database ID as a number

AUDIT_ATTRIBUTE
:   Audit resource field or an updated database column

AUDIT_FIELD_OLD
:   Old audit value of an update action

AUDIT_FIELD_NEW
:   New audit value of an update action

AUDIT_ID
:   Record database ID of the audit subject

AUDIT_ATTRIBUTE
:   Attribute name or column on which an action was performed

    Example: Name or description

EXCEPTION_MESSAGE
:   Exception message when error is logged

EXCEPTION_CLASS
:   Exception Ruby class when error is logged

EXCEPTION_BACKTRACE
:   Exception backtrace as a multiline string when error is logged

LOC_ID
:   Location database ID

LOC_NAME
:   Location name

LOC_LABEL
:   Location label

LOGGER
:   Logger name

    To see the current list of loggers enabled by default, enter this command:

    ```
    # awk '/add_loggers/,/^$/' /usr/share/foreman/config/application.rb
    ```

ORG_ID
:   Organization database ID

ORG_NAME
:   Organization name

ORG_LABEL
:   Organization label

REMOTE_IP
:   Remote IP address of a client

REQUEST
:   Request ID generated by the Action Dispatch module

SESSION
:   Random ID generated per session or a request for a sessionless request

TEMPLATE_NAME
:   Template name

TEMPLATE_DIGEST
:   Digest (SHA256) of rendered template contents

TEMPLATE_HOST_NAME
:   Host name for a rendered template if present

TEMPLATE_HOST_ID
:   Host database ID for a rendered template if present

USER_LOGIN
:   User login name
