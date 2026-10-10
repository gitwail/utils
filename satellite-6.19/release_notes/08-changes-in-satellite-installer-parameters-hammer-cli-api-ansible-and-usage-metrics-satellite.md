---
title: "Changes in satellite-installer parameters, Hammer CLI, REST API, and usage metrics"
product: "Red Hat Satellite"
version: "6.19"
guide: "release_notes"
guide_title: "Release notes"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#changes-in-satellite-installer-parameters-hammer-cli-api-ansible-and-usage-metrics_satellite"
---
# Chapter 8. Changes in satellite-installer parameters, Hammer CLI, REST API, and usage metrics

Review these changes to update your existing workflows and discover new capabilities in Red Hat Satellite.

## 8.1. satellite-installer parameters

New `satellite-installer` parameters
:   - `--foreman-db-extra-options`
    - `--reset-foreman-db-extra-options`
    - `--foreman-proxy-plugin-remote-execution-script-ssh-host-ca-public-keys-file`
    - `--reset-foreman-proxy-plugin-remote-execution-script-ssh-host-ca-public-keys-file`
    - `--foreman-proxy-plugin-remote-execution-script-ssh-user-ca-public-key-file`
    - `--reset-foreman-proxy-plugin-remote-execution-script-ssh-user-ca-public-key-file`
    - `--iop-core-engine-log-level-insights-core-dr`
    - `--reset-iop-core-engine-log-level-insights-core-dr`
    - `--iop-core-engine-log-level-insights-kafka-service`
    - `--reset-iop-core-engine-log-level-insights-kafka-service`
    - `--iop-core-engine-log-level-insights-messaging`
    - `--reset-iop-core-engine-log-level-insights-messaging`
    - `--iop-core-engine-log-level-root`
    - `--reset-iop-core-engine-log-level-root`
    - `--reset-puppet-agent-manage-environment`
    - `--puppet-agent-manage-environment`

Removed `satellite-installer` parameters
:   This release does not remove or replace any `satellite-installer` parameters.

## 8.2. Hammer CLI

New Hammer commands and subcommands
:   This release does not add any Hammer commands or subcommands.

New Hammer options
:   - `--lifecycle-environment-ids` is added to the following commands:

      - `hammer content-view create`
      - `hammer content-view update`
    - `--dependency-ids` is added to the `hammer flatpak-remote remote-repository mirror` subcommand
    - `--containerfile-install-command` is added to the `hammer host package` subcommand
    - `--persistence` is added to the `hammer host package` subcommand
    - `--clone` is added to the `hammer job-template` subcommand
    - `--ui-compact-mode` is added to the following commands:

      - `hammer user update`
      - `hammer user create`
    - `--clone` is added to the `hammer job-template` subcommand

Removed Hammer commands and subcommands
:   - `add-subscription`, `remove-subscription`, and `subscriptions` subcommands are removed from the `hammer activation-key` command
    - `attach` and `remove` subcommands are removed from the `hammer host subscription` command

Removed Hammer options
:   - `--auto-attach` is removed from the following commands:

      - `hammer activation-key create`
      - `hammer activation-key updatesubscriptions`
      - `hammer host subscription`
    - `--autoheal` is removed from the following commands:

      - `hammer host create`
      - `hammer host update`
    - `location`, `location-id`, `location-title`, `organization`, `organization-id`, and `organization-title` are removed from the following commands:

      - `hammer filter create`
      - `hammer filter update`
      - `hammer location create`
      - `hammer location delete`
      - `hammer location info`
      - `hammer location list`
      - `hammer location update`

**Additional resources**

- For more information, see [*Using the Hammer CLI tool*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index) or enter the commands with the `--help` option.

## 8.3. REST API

New API endpoints
:   **Host_debs** endpoints
    :   - `/api/host_debs/:id`
        - `/api/host_debs/compare`
        - `/api/host_debs/installed_debs`

    **Host_packages**
    :   - `/api/hosts/:host_id/transient_packages/containerfile_install_command`

    **Host_tracer** endpoints
    :   - `/api/hosts/bulk/traces/auto_complete_search`

    **Hosts_bulk_actions** endpoints
    :   - `api/hosts/bulk/assign_content_view_environments`
        - `/api/hosts/bulk/change_power_state`

Removed API endpoints
:   **Activation_keys** endpoints
    :   - `/api/activation_keys/:id/add_subscriptions`
        - `/api//activation_keys/:id/remove_subscriptions`
        - `/api/activation_keys/:id/auto_attach`
        - `/api/activation_keys/auto-attach`
        - `/api/activation_keys/:id/copy/auto-attach`

    **Hosts** endpoints
    :   - `/api/hosts/:host_id/subscriptions/add_subscriptions`
        - `/api/hosts/:host_id/subscriptions/remove_subscriptions`
        - `/api/hosts/bulk/remove_subscriptions`
        - `/api/hosts/bulk/add_subscriptions`
        - `/api/hosts/bulk/auto_attach`

## 8.4. Ansible modules

This release performs the following changes in the Satellite Ansible Collection.

New Ansible modules
:   - `redhat.satellite.content_view_history_info`

Removed Ansible modules
:   This release does not remove any Ansible modules.

## 8.5. Collected usage metrics

New usage metrics
:   - `rh_cloud_connector_enabled`
    - `rh_cloud_exclude_host_package_info`
    - `rh_cloud_hosts_count`
    - `rh_cloud_inventory_upload_enabled`
    - `rh_cloud_minimal_data_collection`
    - `rh_cloud_mismatched_auto_delete`
    - `rh_cloud_mismatched_hosts_count`
    - `rh_cloud_obfuscate_inventory_hostnames`
    - `rh_cloud_obfuscate_inventory_ips`
    - `rh_cloud_recommendations_sync_enabled`
    - `rh_cloud_total_hits`

**Additional resources**

- For more information, see [Usage metrics collection in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#usage-metrics-collection-in-satellite) in *Administering Red Hat Satellite*.
