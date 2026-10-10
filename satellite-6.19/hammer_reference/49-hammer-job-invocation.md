---
title: "job-invocation"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "49"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-job-invocation"
---
# Chapter 49. job-invocation

Manage job invocations

**Usage**

```
# hammer job-invocation [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 49.1. job-invocation cancel

Cancel the job

**Usage**

```
# hammer job-invocation cancel [OPTIONS]
```

**Options**

- `--force BOOLEAN`
- `--id VALUE`
- `--location-id NUMBER` – Set the current location context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--search VALUE` – Search query to cancel tasks only on matching hosts. If not provided, the whole job invocation will be cancelled.
- `-h`, `--help` – Print help

## 49.2. job-invocation create

Create a job invocation

**Usage**

```
# hammer job-invocation create [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--bookmark VALUE` – Name to search by
- `--bookmark-id NUMBER`
- `--concurrency-level NUMBER` – Run at most N tasks at a time
- `--cron-line VALUE` – Create a recurring execution Cron line format `a b c d e`, where:

  1. is minute (range: 0-59)
  2. is hour (range: 0-23)
  3. is day of month (range: 1-31)
  4. is month (range: 1-12)
  5. is day of week (range: 0-6)
- `--description-format VALUE` – Override the description format from the template for this invocation only
- `--dynamic` – Dynamic search queries are evaluated at run time
- `--effective-user VALUE` – What user should be used to run the script (using sudo-like mechanisms). Defaults to a template parameter or global setting.
- `--effective-user-password VALUE` – Set password for effective user (using sudo-like mechanisms)
- `--end-time DATETIME` – Perform no more executions after this time, used with `--cron-line`
- `--execution-timeout-interval NUMBER` Override the timeout interval from the template for this invocation only
- `--feature VALUE` – Remote execution feature label that should be triggered, job template assigned to this feature will be used
- `--input-files KEY_VALUE_LIST` – Read input values from files Comma-separated list of key=file, where file is a path to a text file to be read
- `--inputs KEY_VALUE_LIST` – Specify inputs from command line
- `--job-template VALUE` – Name to search by
- `--job-template-id VALUE` – The job template to use, parameter is required unless feature was specified
- `--key-passphrase VALUE` – Set SSH key passphrase
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--max-iteration NUMBER` – Repeat a maximum of N times
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--password VALUE` – Set SSH password
- `--purpose VALUE` – Designation of a special purpose
- `--randomized-ordering BOOLEAN` – Execute the jobs on hosts in randomized order
- `--search-query VALUE`
- `--ssh-user VALUE` – Set SSH user
- `--start-at DATETIME` – Schedule the execution for a later time
- `--start-before DATETIME` – Execution should be cancelled if it cannot be started before `--start-at`
- `--tags VALUE` – A comma separated list of tags to use for Ansible run
- `--tags-flag ENUM` – IncludeExclude tags for Ansible run Possible value(s): `include`, `exclude`
- `--time-to-pickup NUMBER` – Override the global time to pickup interval for this invocation only
- `-h`, `--help` – Print help

## 49.3. job-invocation info

Show job invocation

**Usage**

```
# hammer job-invocation <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location-id NUMBER` – Set the current location context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--show-host-status` – Show job status for the hosts
- `--show-inputs` – Show the complete input of the job
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Description | x | x |
| Status | x | x |
| Success | x | x |
| Failed | x | x |
| Pending | x | x |
| Missing | x | x |
| Total | x | x |
| Start | x | x |
| Randomized ordering | x | x |
| Inputs | x | x |
| Job category | x | x |
| Mode | x | x |
| Cron line | x | x |
| Recurring logic id | x | x |
| Time to pickup | x | x |
| Hosts | x | x |

## 49.4. job-invocation list

List job invocations

**Usage**

```
# hammer job-invocation <list|index> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--order VALUE` – Sort and order by a searchable field, e.g. `<field> DESC`
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--page NUMBER` – Page number, starting at 1
- `--per-page VALUE` – Number of results per page to return, `all` to return all results
- `--search VALUE` – Filter results
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT |
| --- | --- | --- |
| Id | x | x |
| Description | x | x |
| Status | x | x |
| Success | x | x |
| Failed | x | x |
| Pending | x | x |
| Total | x | x |
| Start | x | x |
| Randomized ordering | x | x |
| Inputs | x | x |

## 49.5. job-invocation output

View the output for a host

**Usage**

```
# hammer job-invocation output [OPTIONS]
```

**Options**

- `--async` – Do not wait for job to complete, shows current output only
- `--host VALUE` – Host name
- `--host-id VALUE`
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 49.6. job-invocation rerun

Rerun the job

**Usage**

```
# hammer job-invocation rerun [OPTIONS]
```

**Options**

- `--failed-only BOOLEAN`
- `--id VALUE`
- `--location-id NUMBER` – Set the current location context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--succeeded-only BOOLEAN`
- `-h`, `--help` – Print help
