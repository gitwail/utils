---
title: "Reverting Satellite Server to download content from Red Hat CDN by using Satellite web UI"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_satellite_server_in_a_disconnected_network_environment"
guide_title: "Installing Satellite Server in a disconnected network environment"
chapter_number: "B"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_disconnected_network_environment/index#reverting-server-to-download-content-from-red-hat-cdn-by-using-web-ui"
---
# Appendix B. Reverting Satellite Server to download content from Red Hat CDN by using Satellite web UI

If your environment changes from disconnected to connected, you can reconfigure a disconnected Satellite Server to download content directly from the Red Hat CDN.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Subscriptions**.
2. Click **Manage Manifest**.
3. Switch to the **CDN Configuration** tab.
4. Select **Red Hat CDN**.
5. Edit the **URL** field to point to the Red Hat CDN URL:

   ```
   https://cdn.redhat.com
   ```
6. Click **Update**.

   Satellite Server is now configured to download content from the Red Hat CDN the next time that it synchronizes repositories.
