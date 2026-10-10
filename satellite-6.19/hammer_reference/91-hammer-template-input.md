---
title: "template-input"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "91"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-template-input"
---
# Chapter 91. template-input

Manage template inputs

**Usage**

```
# hammer template-input [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 91.1. template-input create

Create a template input

**Usage**

```
# hammer template-input create [OPTIONS]
```

**Options**

- `--advanced BOOLEAN` – Input is advanced
- `--default VALUE` – Default value for user input
- `--description VALUE` – Input description
- `--fact-name VALUE` – Fact name, used when input type is Fact value
- `--hidden-value BOOLEAN` – The value contains sensitive information and shouldn not be normally visible, useful e.g. for passwords
- `--input-type ENUM` – Input type Possible value(s): `puppet_parameter`, `user`, `fact`, `variable`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Input name
- `--options LIST` – Selectable values for user inputs
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--puppet-class-name VALUE` – Puppet class name, used when input type is Puppet parameter
- `--puppet-parameter-name VALUE` Puppet parameter name, used when input type is Puppet parameter
- `--required BOOLEAN` – Input is required
- `--resource-type ENUM` – For values of type search, this is the resource the value searches in Possible value(s): `AnsibleRole`, `AnsibleVariable`, `Architecture`, `Audit`, `AuthSource`, `Bookmark`, `ComputeProfile`, `ComputeResource`, `ConfigReport`, `DiscoveryRule`, `Domain`, `ExternalUsergroup`, `FactValue`, `Filter`, `ForemanOpenscap::ArfReport`, `ForemanOpenscap::Policy`, `ForemanOpenscap::ScapContent`, `ForemanOpenscap::TailoringFile`, `ForemanPuppet::ConfigGroup`, `ForemanPuppet::Environment`, `ForemanPuppet::HostClass`, `ForemanPuppet::Puppetclass`, `ForemanPuppet::PuppetclassLookupKey`, `ForemanRhCloud`, `ForemanTasks::RecurringLogic`, `ForemanTasks::Task`, `ForemanVirtWhoConfigure::Config`, `Host`, `Hostgroup`, `HttpProxy`, `Image`, `InsightsHit`, `JobInvocation`, `JobTemplate`, `Katello::ActivationKey`, `Katello::AlternateContentSource`, `Katello::ContentCredential`, `Katello::ContentView`, `Katello::FlatpakRemote`, `Katello::HostCollection`, `Katello::KTEnvironment`, `Katello::Product`, `Katello::Subscription`, `Katello::SyncPlan`, `KeyPair`, `Location`, `LookupValue`, `MailNotification`, `Medium`, `Model`, `Operatingsystem`, `Organization`, `Parameter`, `PersonalAccessToken`, `ProvisioningTemplate`, `Ptable`, `Realm`, `RemoteExecutionFeature`, `ReportTemplate`, `Role`, `Setting`, `SmartProxy`, `SshKey`, `Subnet`, `Template`, `TemplateInvocation`, `User`, `Usergroup`, `Webhook`, `WebhookTemplate`
- `--template-id VALUE`
- `--value-type ENUM` – Value type, defaults to plain Possible value(s): `plain`, `search`, `date`, `resource`
- `--variable-name VALUE` – Variable name, used when input type is Variable
- `-h`, `--help` – Print help

## 91.2. template-input delete

Delete a template input

**Usage**

```
# hammer template-input <delete|destroy> [OPTIONS]
```

**Options**

- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--template-id VALUE`
- `-h`, `--help` – Print help

## 91.3. template-input info

Show template input details

**Usage**

```
# hammer template-input <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id VALUE`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Name to search by
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--template-id VALUE`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Input type | x | x |  |
| Fact name | x | x |  |
| Variable name | x | x |  |
| Puppet parameter name | x | x |  |
| Options | x | x |  |
| Default value | x | x |  |

## 91.4. template-input list

List template inputs

**Usage**

```
# hammer template-input <list|index> [OPTIONS]
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
- `--template-id VALUE`
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Input type | x | x |  |

**Search and order fields**

- `id` – integer
- `input_type` – string
- `name` – string

## 91.5. template-input update

Update a template input

**Usage**

```
# hammer template-input update [OPTIONS]
```

**Options**

- `--advanced BOOLEAN` – Input is advanced
- `--default VALUE` – Default value for user input
- `--description VALUE` – Input description
- `--fact-name VALUE` – Fact name, used when input type is Fact value
- `--hidden-value BOOLEAN` – The value contains sensitive information and shouldn not be normally visible, useful e.g. for passwords
- `--id VALUE`
- `--input-type ENUM` – Input type Possible value(s): `puppet_parameter`, `user`, `fact`, `variable`
- `--location VALUE` – Set the current location context for the request
- `--location-id NUMBER` – Set the current location context for the request
- `--location-title VALUE` – Set the current location context for the request
- `--name VALUE` – Input name
- `--new-name VALUE` – Input name
- `--options LIST` – Selectable values for user inputs
- `--organization VALUE` – Set the current organization context for the request
- `--organization-id NUMBER` – Set the current organization context for the request
- `--organization-title VALUE` – Set the current organization context for the request
- `--puppet-class-name VALUE` – Puppet class name, used when input type is Puppet parameter
- `--puppet-parameter-name VALUE` Puppet parameter name, used when input type is Puppet parameter
- `--required BOOLEAN` – Input is required
- `--resource-type ENUM` – For values of type search, this is the resource the value searches in Possible value(s): `AnsibleRole`, `AnsibleVariable`, `Architecture`, `Audit`, `AuthSource`, `Bookmark`, `ComputeProfile`, `ComputeResource`, `ConfigReport`, `DiscoveryRule`, `Domain`, `ExternalUsergroup`, `FactValue`, `Filter`, `ForemanOpenscap::ArfReport`, `ForemanOpenscap::Policy`, `ForemanOpenscap::ScapContent`, `ForemanOpenscap::TailoringFile`, `ForemanPuppet::ConfigGroup`, `ForemanPuppet::Environment`, `ForemanPuppet::HostClass`, `ForemanPuppet::Puppetclass`, `ForemanPuppet::PuppetclassLookupKey`, `ForemanRhCloud`, `ForemanTasks::RecurringLogic`, `ForemanTasks::Task`, `ForemanVirtWhoConfigure::Config`, `Host`, `Hostgroup`, `HttpProxy`, `Image`, `InsightsHit`, `JobInvocation`, `JobTemplate`, `Katello::ActivationKey`, `Katello::AlternateContentSource`, `Katello::ContentCredential`, `Katello::ContentView`, `Katello::FlatpakRemote`, `Katello::HostCollection`, `Katello::KTEnvironment`, `Katello::Product`, `Katello::Subscription`, `Katello::SyncPlan`, `KeyPair`, `Location`, `LookupValue`, `MailNotification`, `Medium`, `Model`, `Operatingsystem`, `Organization`, `Parameter`, `PersonalAccessToken`, `ProvisioningTemplate`, `Ptable`, `Realm`, `RemoteExecutionFeature`, `ReportTemplate`, `Role`, `Setting`, `SmartProxy`, `SshKey`, `Subnet`, `Template`, `TemplateInvocation`, `User`, `Usergroup`, `Webhook`, `WebhookTemplate`
- `--template-id VALUE`
- `--value-type ENUM` – Value type, defaults to plain Possible value(s): `plain`, `search`, `date`, `resource`
- `--variable-name VALUE` – Variable name, used when input type is Variable
- `-h`, `--help` – Print help
