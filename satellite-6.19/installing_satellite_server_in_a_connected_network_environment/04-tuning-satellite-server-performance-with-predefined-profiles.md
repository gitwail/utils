---
title: "Tuning Satellite Server performance with predefined profiles"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_connected_network_environment"
guide_title: "Installing Satellite Server in a connected network environment"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#tuning-satellite-server-performance-with-predefined-profiles"
---
# Chapter 4. Tuning Satellite Server performance with predefined profiles

If your Satellite deployment includes a large number of hosts, you can use predefined tuning profiles to configure your Satellite Server to use the optimal amount of CPU cores and memory. This can help improve Satellite performance.

## 4.1. How predefined tuning profiles apply

When you run the `satellite-installer` command with the `--tuning` option, deployment configuration settings from multiple sources are applied to Satellite in a specific order. This order defines the priority of these settings.

Satellite loads tuning configuration settings from the following sources:

Custom Hiera settings
:   If you use custom Hiera settings on your Satellite Server, you can find them in the `/etc/foreman-installer/custom-hiera.yaml` file.

Predefined tuning profile
:   This is the profile that you select when running the `satellite-installer` command with the `--tuning` option. The settings for these profiles are defined in the `/usr/share/foreman-installer/config/foreman.hiera/tuning/sizes/` directory.

Base tuning profile
:   The settings for this profile are defined in the `/usr/share/foreman-installer/config/foreman.hiera/tuning/common.yaml` file.

When merging these settings, Satellite applies them in the following order:

- Custom settings in the `/etc/foreman-installer/custom-hiera.yaml` file override the settings in any predefined profile and the base profile.
- Predefined profile settings override the settings in the base profile.

## 4.2. Predefined tuning profiles

The following predefined tuning profiles are available in Satellite to right-size your Satellite Server based on the number of hosts your Satellite manages and available hardware resources.

The predefined tuning profiles are available in the `/usr/share/foreman-installer/config/foreman.hiera/tuning/sizes` directory. Each profile targets a managed-host range and minimum RAM and CPU cores.

Table 4.1. Predefined tuning profiles

| Tuning profile | Number of hosts | RAM | Number of CPU cores |
| --- | --- | --- | --- |
| default | 0 – 5000 | 20G | 4 |
| medium | 5001 – 10000 | 32G | 8 |
| large | 10001 – 20000 | 64G | 16 |
| extra-large | 20001 – 60000 | 128G | 32 |
| extra-extra-large | 60000+ | 256G | 48+ |

## 4.3. Applying a predefined tuning profile

Run `satellite-installer` with the `--tuning` option to apply a profile. Choosing the right tuning profile helps your Satellite Server use its CPU cores and memory better.

> **Note**
>
> You cannot use predefined tuning profiles on Capsule Servers.

**Procedure**

1. If you use a `custom-hiera.yaml` file on your Satellite Server, perform the following steps:

   1. Optional: Back up your `custom-hiera.yaml` file:

      ```
      # cp /etc/foreman-installer/custom-hiera.yaml \
      /etc/foreman-installer/custom-hiera.original.yaml
      ```

      This ensures you can restore the `custom-hiera.yaml` file to its original state if it becomes corrupted.
   2. Review the definitions of the base tuning profile in `/usr/share/foreman-installer/config/foreman.hiera/tuning/common.yaml` and the tuning profile that you want to apply in `/usr/share/foreman-installer/config/foreman.hiera/tuning/sizes/`.
   3. Compare the configuration entries against the entries in your `/etc/foreman-installer/custom-hiera.yaml` file.
   4. Remove any duplicated configuration settings that you find in `custom-hiera.yaml`. This ensures the settings in `custom-hiera.yaml` do not override the settings in the base tuning profile and your chosen predefined tuning profile.
2. Apply the tuning profile:

   ```
   # satellite-installer --tuning medium
   ```
