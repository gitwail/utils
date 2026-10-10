---
title: "Hammer cheat sheet"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#hammer-cheat-sheet"
---
# Chapter 10. Hammer cheat sheet

You can use the examples in the cheat sheet as templates for common Hammer CLI tasks to configure and manage a Satellite Server by using either CLI commands or shell script automation. Run `hammer full-help` on Satellite to view the complete Hammer CLI help.

## 10.1. General information

Review essential information for using Hammer CLI in Red Hat Satellite. There are certain options that apply to all commands, such as authentication and getting help.

Authentication in examples
:   This cheat sheet assumes saved credentials in `~/.hammer/cli_config.yml`. For more information, see [Chapter 3, *Hammer authentication*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#hammer-authentication "Chapter 3. Hammer authentication").

`--help`
:   Displays Hammer commands and options. You can append it after a subcommand to get more information.

*organization-specific*
:   The command requires you to specify an organization. You can append `--organization My_Organization` to the command or set a default organization:

    ```
    hammer defaults add \
    --param-name organization_id \
    --param-value org_ID
    ```

*location-specific*
:   The command requires you to specify a location. You can append `--location My_Location` to the command or set a default location:

    ```
    hammer defaults add \
    --param-name location_id \
    --param-value loc_ID
    ```

## 10.2. Organizations, locations, and repositories

You can manage organizations, locations, and repositories in Red Hat Satellite by using Hammer CLI commands.

| Subcommand | Description and tasks |
| --- | --- |
| `organization` | Create an organization:   `hammer organization create \ --name org_name`  List organizations:   `hammer organization list` |
| `location` | See the options for organization |
| `subscription`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Upload a subscription manifest:   `hammer subscription upload \ --file path` |
| `repository-set`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Enable a repository:   `hammer repository-set enable \ --product prod_name \ --basearch base_arch \ --releasever rel_v \ --name repo_name` |
| `repository`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Synchronize a repository:   `hammer repository synchronize \ --product prod_name \ --name repo_name`  Create a custom repository:   `hammer repository create \ --product prod_name \ --content-type cont_type \ --publish-via-http true \ --url repo_url \ --name repo_name`  Upload content to a custom repository:   `hammer repository upload-content \ --product prod_name \ --id repo_id \ --path path_to_dir` |

## 10.3. Content life cycles

You can manage content views in lifecycle environments in Red Hat Satellite by using Hammer CLI commands.

| Subcommand | Description and tasks |
| --- | --- |
| `lifecycle-environment`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Create a life cycle environment:   `hammer lifecycle-environment create \ --name env_name --description env_desc --prior prior_env_name`  List life cycle environments:   `hammer lifecycle-environment list` |
| `content-view`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Create a content view:   `hammer content-view create \ --name cv_n \ --repository-ids repo_ID1,... \ --description cv_description`  Add repositories to a content view:   `hammer content-view add-repository \ --name cv_n \ --repository-id repo_ID`  Add Puppet modules to a content view:   `hammer content-view puppet-module add \ --content-view cv_n \ --name module_name`  Publishing a content view:   `hammer content-view publish \ --id cv_ID`  Promoting a content view:   `hammer content-view version promote \ --content-view cv_n \ --to-lifecycle-environment env_name`  Incremental update of a content view:   `hammer content-view version incremental-update \ --content-view-version-id cv_ID \ --packages pkg_n1,... \ --lifecycle-environment-ids env_ID1,...` |

## 10.4. Provisioning environments

You can prepare provisioning infrastructure in Red Hat Satellite by using Hammer CLI commands.

| Subcommand | Description and tasks |
| --- | --- |
| `domain` | Create a domain:   `hammer domain create \ --name domain_name` |
| `subnet`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information")[*location-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Add a subnet:   `hammer subnet create \ --name subnet_name \ --organization-ids org_ID1,... \ --location-ids loc_ID1,... \ --domain-ids dom_ID1,... \ --boot-mode boot_mode \ --network network_address \ --mask netmask --ipam ipam` |
| `compute-resource`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information")[*location-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Create a compute resource:   `hammer compute-resource create \ --name cr_name \ --organization-ids org_ID1,... \ --location-ids loc_ID1,... \ --provider provider_name` |
| `medium` | Add an installation medium:   `hammer medium create \ --name med_name \ --path path_to_medium` |
| `partition-table` | Add a partition table:   `hammer partition-table create \ --name tab_name \ --path path_to_file \ --os-family os_family` |
| `template` | Add a provisioning template:   `hammer template create \ --name tmp_name \ --file path_to_template` |
| `os` | Add an operating system:   `hammer os create \ --name os_name \ --version version_num` |

## 10.5. Activation keys

You can create activation keys and add subscriptions in Red Hat Satellite by using Hammer CLI commands.

| Subcommand | Description and tasks |
| --- | --- |
| `activation-key`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Create an activation key:   `hammer activation-key create \ --name ak_name \ --content-view cv_n \ --lifecycle-environment lc_name`  Add a subscription to the activation key:   `hammer activation-key add-subscription \ --id ak_ID \ --subscription-id sub_ID` |

## 10.6. Users and permissions

You can manage users, user groups, roles, and filters in Red Hat Satellite by using Hammer CLI commands.

| Subcommand | Description and tasks |
| --- | --- |
| `user`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Create a user:   `hammer user create \ --login user_name \ --mail user_mail \ --auth-source-id 1 \ --organization-ids org_ID1,org_ID2,...`  Add a role to a user:   `hammer user add-role \ --id user_id \ --role role_name` |
| `user-group` | Create a user group:   `hammer user-group create \ --name ug_name`  Add a role to a user group:   `hammer user-group add-role \ --id ug_id \ --role role_name` |
| `role` | Create a role:   `hammer role create \ --name role_name` |
| `filter` | Create a filter and add it to a role:   `hammer filter create \ --role role_name \ --permission-ids perm_ID1,perm_ID2,...` |

## 10.7. Errata

You can manage security updates and patches in Red Hat Satellite by using Hammer CLI commands.

| Subcommand | Description and tasks |
| --- | --- |
| `erratum` | List errata:   `hammer erratum list`  Find erratum by CVE:   `hammer erratum list --cve CVE`  Inspect erratum:   `hammer erratum info --id err_ID` |
| `host` | List errata applicable to a host:   `hammer host errata list \ --host host_name`  Apply errata to a host:   `hammer host errata apply \ --host host_name \ --errata-ids err_ID1,err_ID2,...` |

## 10.8. Hosts

You can manage hosts, host groups, and remote job execution in Red Hat Satellite by using Hammer CLI commands.

| Subcommand | Description and tasks |
| --- | --- |
| `hostgroup`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information")[*location-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Create a host group:   `hammer hostgroup create \ --name hg_name \ --puppet-environment env_name \ --architecture arch_name \ --domain domain_name \ --subnet subnet_name \ --puppet-proxy proxy_name \ --puppet-ca-proxy ca-proxy_name \ --operatingsystem os_name \ --partition-table table_name \ --medium medium_name \ --organization-ids org_ID1,... \ --location-ids loc_ID1,...`  Add an activation key to a host group:   `hammer hostgroup set-parameter \ --hostgroup "hg_name" \ --name "kt_activation_keys" \ --value key_name` |
| `host`[*organization-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information")[*location-specific*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#general-information "10.1. General information") | Create a host (inheriting parameters from a host group):   `hammer host create \ --name host_name \ --hostgroup hg_name \ --interface="primary=true, \ mac=mac_addr, ip=ip_addr, \ provision=true" \ --organization-id org_ID \ --location-id loc_ID \ --ask-root-password yes`  Remove the host from host group:   `hammer host update --name host_name --hostgroup NIL` |
| `job-template` | Add a job template for remote execution:   `hammer job-template create \ --file path \ --name template_name \ --provider-type SSH \ --job-category category_name` |
| `job-invocation` | Start a remote job:   `hammer job-invocation create \ --job-template template_name \ --inputs key1=value,... \ --search-query query`  Monitor the remote job:   `hammer job-invocation output \ --id job_id --host host_name` |

## 10.9. Tasks

You can list tasks and monitor their progress in Red Hat Satellite by using Hammer CLI commands.

| Subcommand | Description and tasks |
| --- | --- |
| `task` | List all tasks:   `hammer task list`  Monitor progress of a running task:   `hammer task progress \ --id task_ID` |
