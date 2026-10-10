---
title: "Host management and monitoring by using the RHEL web console"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "13"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#host-management-and-monitoring-by-using-cockpit"
---
# Chapter 13. Host management and monitoring by using the RHEL web console

You can use the RHEL web console web interface to perform actions and monitor Red Hat Enterprise Linux hosts. Enable RHEL web console integration in Satellite to view host dashboards and use RHEL web console features, such as Red Hat Image Builder, from within the Satellite web UI.

## 13.1. Enabling the RHEL web console on Satellite

You can enable the RHEL web console on Satellite Server so that you can access RHEL web console features for your hosts from within the Satellite web UI.

**Prerequisites**

- You have root or sudo access on Satellite Server.

**Procedure**

- Enable the RHEL web console on your Satellite Server:

  ```
  # satellite-installer --enable-foreman-plugin-remote-execution-cockpit --reset-foreman-plugin-remote-execution-cockpit-ensure
  ```

## 13.2. Managing and monitoring hosts using the RHEL web console

You can access the RHEL web console UI through the Satellite web UI to manage and monitor Red Hat Enterprise Linux hosts. Use it to view dashboards, run commands, or use integrated features such as Red Hat Image Builder.

**Prerequisites**

- You have enabled the RHEL web console in Satellite.
- You have installed the RHEL web console on the host that you want to manage and monitor.

  Satellite provides a job template named **Service Action – Enable Web Console** under the **Ansible Services** job category that you can use to install the RHEL web console. For more information about running remote jobs, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").
- Satellite or Capsule can authenticate to the host with SSH keys. For more information, see [Section 19.2.3, “Distributing SSH keys for remote execution”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Distributing_SSH_Keys_for_Remote_Execution_managing-hosts "19.2.3. Distributing SSH keys for remote execution").

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts** and select the host that you want to manage and monitor with the RHEL web console.
2. In the upper right of the host window, open the options menu and select **Web Console**.

   You can now access the full range of features available for host monitoring and management, for example, Red Hat Image Builder, through the RHEL web console.

**Additional resources**

- [*Managing systems using the RHEL 9 web console*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/managing_systems_using_the_rhel_9_web_console/index)
- [*Managing systems using the RHEL 8 web console*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/managing_systems_using_the_rhel_8_web_console/index)
- [*Managing systems using the RHEL 7 web console*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/managing_systems_using_the_rhel_7_web_console/index)
- [*Accessing the RHEL image builder dashboard in the RHEL web console* in *Composing a customized RHEL system image* (RHEL 9)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/composing_a_customized_rhel_system_image/creating-system-images-with-composer-web-console-interface_composing-a-customized-rhel-system-image#accessing-composer-gui-in-the-rhel-8-web-console_creating-system-images-with-composer-web-console-interface)
- [*Accessing the RHEL image builder dashboard in the RHEL web console* in *Composing a customized RHEL system image* (RHEL 8)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/composing_a_customized_rhel_system_image/creating-system-images-with-composer-web-console-interface_composing-a-customized-rhel-system-image#accessing-composer-gui-in-the-rhel-8-web-console_creating-system-images-with-composer-web-console-interface)
- [*Accessing Image Builder GUI in the RHEL 7 web console* in *Image Builder Guide* (RHEL 7)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/image_builder_guide/chap-documentation-image_builder-test_chapter_4#sect-Documentation-Image_Builder-Chapter4)

## 13.3. Disabling the RHEL web console on Satellite

You can disable the RHEL web console on Satellite Server when you no longer need to access RHEL web console features for hosts from the Satellite web UI.

**Procedure**

- Disable the RHEL web console on your Satellite Server:

  ```
  # satellite-installer --foreman-plugin-remote-execution-cockpit-ensure absent
  ```

  > **Important**
  >
  > You can enable or disable RHEL web console integration independently on Capsule Servers. After completing the procedure on your Satellite Server, you can disable RHEL web console integration on your Capsule Servers:
  >
  > ```
  > # satellite-installer --foreman-proxy-plugin-remote-execution-script-cockpit-integration false
  > ```
