---
title: "Hammer configuration option"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#hammer-configuration-option"
---
# Chapter 4. Hammer configuration option

You can customize Hammer behavior by modifying global configuration in `/etc/hammer/` or user-specific settings in `~/.hammer/`, including log levels, output formatting, and CLI module settings.

The default location for global Hammer configuration is:

- `/etc/hammer/cli_config.yml` for general Hammer settings
- `/etc/hammer/cli.modules.d/` for CLI module configuration files

You can set user specific directives for Hammer (in `~/.hammer/cli_config.yml`) as well as for CLI modules (in respective `.yml` files under `~/.hammer/cli.modules.d/`).

To see the order in which configuration files are loaded, as well as versions of loaded modules, use:

```
$ hammer -d --version
```

> **Note**
>
> Loading configuration for many CLI modules can slow down the execution of Hammer commands. In such a case, consider disabling CLI modules that are not regularly used.

Apart from saving credentials as described in [Chapter 3, *Hammer authentication*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#hammer-authentication "Chapter 3. Hammer authentication"), you can set several other options in the `~/.hammer/` configuration directory. For example, you can change the default log level and set log rotation with the following directives in `~/.hammer/cli_config.yml`. These directives affect only the current user and are not applied globally.

```
:log_level: 'warning'
:log_size: 5 #in MB
```

Similarly, you can configure user interface settings. For example, set the number of entries displayed per request in the Hammer output by changing the following line:

```
:per_page: 30
```

This setting is an equivalent of the `--per-page` Hammer option.

## 4.1. Setting a default organization and location context

Set a default organization and location context for Hammer to simplify commands and avoid repeatedly specifying the `--organization` and `--location` options. This is useful when you primarily manage a single organization.

**Procedure**

1. Set a default organization:

   ```
   $ hammer defaults add --param-name organization \
   --param-value "Your_Organization"
   ```

   You can find the name of your organization with the `hammer organization list` command.
2. Optional: Set a default location:

   ```
   $ hammer defaults add --param-name location \
   --param-value "Your_Location"
   ```

   You can find the name of your location with the `hammer location list` command.

**Verification**

1. Review the currently specified default settings:

   ```
   $ hammer defaults list
   ```

## 4.2. Increasing the logging level for Hammer

Increase Hammer logging to `debug` to capture detailed CLI activity when troubleshooting command-line errors or API responses.

Hammer writes logs to `~/.hammer/log/hammer.log`.

**Procedure**

- In `/etc/hammer/cli_config.yml`, set the `:log_level:` option to `debug`:

  ```yaml
  :log_level: 'debug'
  ```
