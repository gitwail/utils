---
title: "Using noVNC to access virtual machines"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "A"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#using-novnc-to-access-virtual-machines"
---
# Appendix A. Using noVNC to access virtual machines

You can use your browser to access the VNC console of VMs created by Satellite.

Satellite supports using noVNC on the following virtualization platforms:

- VMware
- Libvirt

**Prerequisites**

- You have a virtual machine created by Satellite.
- For existing virtual machines, ensure that the **Display type** in the **Compute Resource** settings is **VNC**.
- You have imported the CA certificate used for Satellite into your browser. Adding a security exception in the browser is not enough for using noVNC. For more information, see [Importing the Katello root CA certificate by using browser](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#importing-the-katello-root-ca-certificate-by-using-browser) in *Configuring authentication for Red Hat Satellite users*.

**Procedure**

1. On your Satellite Server, configure the firewall to allow VNC service on ports 5900 to 5930.

   ```
   # firewall-cmd --add-port=5900-5930/tcp
   # firewall-cmd --add-port=5900-5930/tcp --permanent
   ```
2. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources** and select the name of a compute resource.
3. In the **Virtual Machines** tab, select the name of your virtual machine. Ensure the machine is powered on and then select **Console**.
