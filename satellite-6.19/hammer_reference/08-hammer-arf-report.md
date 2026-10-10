---
title: "arf-report"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-arf-report"
---
# Chapter 8. arf-report

Manipulate compliance reports

**Usage**

```
# hammer arf-report [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 8.1. arf-report delete

Delete an ARF Report

**Usage**

```
# hammer arf-report <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `-h`, `--help` – Print help

## 8.2. arf-report download

Download bzipped ARF report

**Usage**

```
# hammer arf-report download [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--path VALUE` – Path to directory where downloaded file will be saved
- `-h`, `--help` – Print help

## 8.3. arf-report download-html

Download ARF report in HTML

**Usage**

```
# hammer arf-report download-html [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `--path VALUE` – Path to directory where downloaded file will be saved
- `-h`, `--help` – Print help

## 8.4. arf-report info

Show an ARF report

**Usage**

```
# hammer arf-report <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Name to search by
- `--location-id NUMBER` – Set the current location context for the request
- `--organization VALUE` – Name to search by
- `--organization-id NUMBER` – Set the current organization context for the request
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Reported at | x | x |  |
| Host name | x | x | x |
| Openscap proxy name | x | x |  |
| Policy name | x | x |  |
| Passed | x | x |  |
| Failed | x | x |  |
| Othered | x | x |  |
| Host id | x | x |  |
| Openscap proxy id | x | x |  |
| Policy id | x | x |  |
| Locations/ | x | x |  |
| Organizations/ | x | x |  |

## 8.5. arf-report list

List ARF reports

**Usage**

```
# hammer arf-report <list|index> [OPTIONS]
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

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Reported at | x | x |  |
| Host name | x | x | x |
| Openscap proxy name | x | x |  |
| Policy name | x | x |  |
| Passed | x | x |  |
| Failed | x | x |  |
| Othered | x | x |  |

**Search and order fields**

- `compliance_policy` – string
- `compliance_status` – Values: compliant, incompliant, inconclusive
- `comply_with` – string
- `environment` – string
- `eventful` – Values: true, false
- `host` – string
- `host_collection` – string
- `host_id` – integer
- `host_owner_id` – integer
- `hostgroup` – string
- `hostgroup_fullname` – string
- `hostgroup_title` – string
- `id` – integer
- `inconclusive_with` – string
- `last_for` – Values: host, policy
- `last_report` – datetime
- `lifecycle_environment` – string
- `location` – string
- `location_id` – integer
- `log` – text
- `not_comply_with` – string
- `openscap_proxy` – string
- `organization` – string
- `organization_id` – integer
- `origin` – string
- `policy` – string
- `reported` – datetime
- `resource` – text
- `xccdf_rule_failed` – string
- `xccdf_rule_name` – text
- `xccdf_rule_othered` – string
- `xccdf_rule_passed` – string
