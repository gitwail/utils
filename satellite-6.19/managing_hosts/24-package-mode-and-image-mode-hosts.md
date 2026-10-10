---
title: "Package mode and image mode hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "24"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#package-mode-and-image-mode-hosts"
---
# Chapter 24. Package mode and image mode hosts

Image mode simplifies enterprise operations by enabling development, operations, and solution providers to use the same container-native tools and techniques to manage both applications and the underlying operating system. Satellite supports image mode for hosts in addition to package mode.

## 24.1. Overview of image mode for hosts

Satellite identifies an image mode host as any system that reports a container image from its bootc status through Subscription Manager. It classifies all other hosts as package mode hosts.

In image mode, users can install and manage packages, but with limitations. Job templates run the `bootc usr-overlay` command or use the `dnf --transient` flag to ensure that packages are installed correctly. Any packages installed on image mode hosts are temporary and disappear after a reboot. Because of this, installing packages is generally discouraged, except for debugging purposes or, in some cases, when applying critical security patches. If you need new packages on an image mode host, consider building a new container image the includes the necessary packages. After upgrading the image mode host to this image, the new packages will be installed permanently.

On the **All Hosts** page, you can display the **Type** column, which includes a mode indicator. This column is disabled by default.

Image mode hosts include additional fields that reflect their boot status. These fields track the container images used in various scenarios:

- **Booted Image & Digest**: Indicates the container image the host is currently using.
- **Staged Image & Digest**: Indicates the container image the host uses after the next reboot.
- **Available Image & Digest**: Represents the container image cached by running `bootc upgrade --check`.
- **Rollback Image & Digest**: Represents the container image the host reverts to after the next reboot if `Bootc rollback` is applied.

**Additional resources**

- [RHEL Image Mode quick start guide](https://www.redhat.com/en/blog/image-mode-red-hat-enterprise-linux-quick-start-guide)

## 24.2. Viewing booted container images by using Satellite web UI

These actions streamline the management of image mode hosts, providing flexibility and control over host operations through Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Container Images**.
2. Select the **Booted** tab to view all images used by image mode hosts. This tab displays the spread of digests under specific image paths. More digests under an image path indicate greater drift in the host ecosystem, ideally minimized by ensuring all hosts run the most up-to-date image version.
3. Click the host count to navigate to the **All Hosts** page, which identifies the hosts associated with each specific image and displays the number of hosts using each digest.
4. Select a host and on the **Details** tab, locate the **Image mode details** card to see the current `bootc` status.
5. Click the link to the **Bootc Action - Script Default** remote execution job in this card to perform a Bootc action on the host. For pull-mode remote execution, the `foreman_ygg_worker` package must be included in the container image of the image mode hosts.

## 24.3. Viewing booted container images by using Hammer CLI

These actions streamline the management of image mode hosts, providing flexibility and control over host operations through Satellite.

**Procedure**

- Run the `hammer host bootc images` command.

## 24.4. Package persistence on image mode hosts

Packages installed on an image mode host after image creation are installed with transient package persistence. Transient packages are temporary and are lost after a reboot.

You can view the persistence of installed packages on an image mode host by navigating to the host details in the Satellite web UI, selecting **Content** > **Packages**, and checking the **Persistence** column. In Hammer CLI, you can view the persistence by running `hammer host package list --host-id My_Host_ID --fields ALL`.

To persist packages on an image mode host, you can build a new container image that includes the necessary packages. After upgrading the image mode host to the new image, the new packages are installed permanently on the host.

## 24.5. Persisting transient packages in your image

You can generate a Containerfile install command using the transient packages on your image mode host. Then, you can use this command to rebuild your image to make the packages persistent.

### 24.5.1. Generating a Containerfile command by using Satellite web UI

You can generate a Containerfile install command by using Satellite web UI to persist transient packages in your container image.

**Prerequisites**

- Your Satellite account has a role that grants the `view_hosts` permission.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the name of a host.
3. Select the **Content** tab.
4. Select the **Packages** tab.
5. Select the packages you want to include in the command.
6. Click the package table menu icon.
7. Select **Generate containerfile install command**.
8. If Satellite does not recognize persistence for any of the selected packages and you want to include them in the command, enable **Include packages with unknown persistence**.
9. Click **Copy** to copy the command to your clipboard.

**Next steps**

- Include the generated command in your Containerfile and rebuild the image.

### 24.5.2. Generating a Containerfile command by using Hammer CLI

You can generate a Containerfile install command by using Hammer CLI to persist transient packages in your container image.

**Prerequisites**

- Your Satellite account has a role that grants the `view_hosts` permission.

**Procedure**

1. Generate the Containerfile command:

   ```
   $ hammer host package containerfile-install-command --host-id My_Host_ID
   ```
2. Copy the generated command from the output.

**Next steps**

- Include the generated command in your Containerfile and rebuild the image.

### 24.5.3. Generating a Containerfile command by using Satellite API

You can generate a Containerfile install command by using Satellite API to persist transient packages in your container image.

**Prerequisites**

- Your Satellite account has a role that grants the `view_hosts` permission.

**Procedure**

1. Send a `GET` request to the `/api/hosts/:host_id/transient_packages/containerfile_install_command` endpoint.
2. Copy the generated command from the response.

**Next steps**

- Include the generated command in your Containerfile and rebuild the image.

## 24.6. Remote execution jobs for image mode hosts

You can use the remote execution jobs under the **Bootc** job category to manage image mode hosts:

- **Bootc Action - Script Default**: Select any Bootc action from the dropdown menu, enter arguments, and specify a target.
- **Bootc Rollback - Script Default**: Run Bootc rollback to revert to a previous image.
- **Bootc Status - Script Default**: Run Bootc status with optional extra parameters to check the status.
- **Bootc Switch - Script Default**: Run Bootc switch with a mandatory image input and optional extra parameters to switch to a different image.
- **Bootc Upgrade - Script Default**: Run Bootc upgrade with optional extra parameters to update the image.

For pull-mode remote execution, the `foreman_ygg_worker` package must be included in the container image of the image mode hosts.

**Additional resources**

- [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs")
