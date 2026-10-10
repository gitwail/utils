---
title: "Selecting an installation size"
product: "Red Hat Satellite"
version: "6.19"
guide: "tuning_performance_of_red_hat_satellite"
guide_title: "Tuning performance of Red Hat Satellite"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/tuning_performance_of_red_hat_satellite/index#selecting-an-installation-size"
---
# Chapter 2. Selecting an installation size

You can tune your Satellite Server based on expected host counts and hardware allocation by using built-in tuning profiles included in Satellite that are available by using the installation routine’s tuning flag. For more information, see [Tuning Satellite Server performance with predefined profiles](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#tuning-satellite-server-performance-with-predefined-profiles) in *Installing Satellite Server in a connected network environment*.

There are four sizes provided based on estimates of the number of hosts your Satellite manages. You can find the specific tuning settings for each profile in the configuration files contained in `/usr/share/foreman-installer/config/foreman.hiera/tuning/sizes`.

| Name | Number of hosts | Recommend RAM | Recommend Cores |
| --- | --- | --- | --- |
| default | 0 – 5000 | 20 GiB | 4 |
| medium | 5000 – 10000 | 32 GiB | 8 |
| large | 10000 – 20000 | 64 GiB | 16 |
| extra-large | 20000 – 60000 | 128 GiB | 32 |
| extra-extra-large | 60000+ | 256 GiB+ | 48+ |

**Procedure**

1. Select an installation size: `default`, `medium`, `large`, `extra-large`, or `extra-extra-large`. The default value is `default`.
2. Run `satellite-installer`:

   ```
   # satellite-installer --tuning "My_Installation_Size"
   ```
3. Optional: Run a health check. For more information, see [Section 5.1, “Considerations for performance tuning”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/tuning_performance_of_red_hat_satellite/index#considerations-for-performance-tuning "5.1. Considerations for performance tuning").
4. Optional: Tune the Ruby app server directly by using the Puma Tuning section. For more information, see [Section 5.2, “Puma tunings”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/tuning_performance_of_red_hat_satellite/index#puma-tunings "5.2. Puma tunings").
