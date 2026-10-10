---
title: "Hammer authentication"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#hammer-authentication"
---
# Chapter 3. Hammer authentication

Hammer requires Satellite credentials for authentication. You can authenticate using sessions, configuration files, or command-line options depending on whether you run commands manually or automatically.

## 3.1. Authenticating Hammer using a configuration file

Store Hammer credentials in the configuration file to automate tasks without interactive prompts. This method is recommended for running Hammer commands from scripts or cron jobs.

> **Important**
>
> If you ran the Satellite installation with `--foreman-initial-admin-username` and `--foreman-initial-admin-password` options, credentials you entered are stored in the `~/.hammer/cli.modules.d/foreman.yml` configuration file on Satellite Server. If you change your credentials on Satellite Server, you must update the configuration file manually. The installer does not overwrite the configuration file.

**Procedure**

- Add your credentials to the `~/.hammer/cli.modules.d/foreman.yml` configuration file:

  ```
  :foreman:
   :username: 'username'
   :password: 'password'
  ```

  Use only spaces for indentation in Hammer configuration files, do not use tabs.

## 3.2. Authenticating Hammer using CLI options

If you do not have your Satellite credentials saved in the `~/.hammer/cli.modules.d/foreman.yml` configuration file, Hammer prompts you for them each time you enter a command.

> **Note**
>
> Examples in this guide assume that you have saved credentials in the configuration file or are using a Hammer authentication session.

**Procedure**

- Specify your credentials when executing a command as follows:

  ```
  $ hammer -u username -p password subcommands
  ```

## 3.3. Authenticating Hammer using sessions

The Hammer authentication session is a cache that stores your credentials, and you have to provide them only once, at the beginning of the session. This method is suited to running several Hammer commands in succession, for example a script containing Hammer commands.

**Prerequisites**

- You have enabled sessions by adding `:use_sessions: true` to the `~/.hammer/cli.modules.d/foreman.yml` file:

  ```yaml
  :foreman:
   :use_sessions: true
  ```

  Note that if you enable sessions, credentials stored in the configuration file will be ignored.
- Optional: You can change the length of a session, for example, to 30 minutes:

  ```
  $ hammer settings set \
  --name idle_timeout \
  --value 30
  ```

  The default length is 60 minutes.

**Procedure**

- Start a session:

  ```
  $ hammer auth login
  ```

  You are prompted for your Satellite credentials, and logged in. You will not be prompted for the credentials again until your session expires.

**Verification**

- View the current status of the session:

  ```
  $ hammer auth status
  ```

**Next steps**

- End the session:

  ```
  $ hammer auth logout
  ```
