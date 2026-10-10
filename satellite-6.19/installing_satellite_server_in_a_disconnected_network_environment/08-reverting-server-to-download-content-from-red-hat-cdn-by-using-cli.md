---
title: "Reverting Satellite Server to download content from Red Hat CDN by using Hammer CLI"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_disconnected_network_environment"
guide_title: "Installing Satellite Server in a disconnected network environment"
chapter_number: "C"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#reverting-server-to-download-content-from-red-hat-cdn-by-using-cli"
---
# Appendix C. Reverting Satellite Server to download content from Red Hat CDN by using Hammer CLI

If your environment changes from disconnected to connected, you can reconfigure a disconnected Satellite Server to download content directly from the Red Hat CDN.

**Procedure**

1. Log in to the Satellite Server using SSH.
2. Use Hammer to reconfigure the CDN:

   ```
   $ hammer organization configure-cdn --name="My_Organization" --type=redhat_cdn
   ```
