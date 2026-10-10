---
title: "Managing Flatpak repositories in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "15"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-flatpak-repositories-in-project"
---
# Chapter 15. Managing Flatpak repositories in Satellite

Flatpak remotes in Satellite connect to external application indexes so you can scan available repositories, mirror them into products, and distribute desktop application content to hosts.

Flatpak repositories function similarly to other content repositories in Satellite. You can synchronize, manage access permissions, and assign repositories to specific lifecycle environments to control which applications are available to hosts. You can also use Hammer CLI to manage Flatpak remotes and repositories.

Flatpak repositories in Satellite have the `docker` content type. You can export Flatpak repositories and import them into other Satellite instances.

**Additional resources**

- [Chapter 11, *Synchronizing content between Satellite Servers*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Synchronizing_Content_Between_Servers_content-management "Chapter 11. Synchronizing content between Satellite Servers")
- [Installing Flatpak applications on hosts in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#installing-flatpak-applications-on-hosts)
- [Installing applications using Flatpak](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/administering_the_system_using_the_gnome_desktop_environment/assembly_installing-applications-using-flatpak_administering-the-system-using-the-gnome-desktop-environment)

## 15.1. Creating a Flatpak remote by using Satellite web UI

Add a Flatpak remote to your Satellite inventory to scan it, mirror selected repositories into your products, and distribute desktop application content to hosts.

**Prerequisites**

- Your Satellite account has a role that grants the `create_flatpak_remotes` permission.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Flatpak Remotes**.
2. Click **Create new**.
3. In the **Name** field, enter a name for the Flatpak remote.
4. In the **URL** field, enter the URL of the Flatpak remote. For example, to use the Red Hat Flatpak index, enter: `https://flatpaks.redhat.io/rhel/`.
5. If the Flatpak remote requires authentication, enter the required credentials. For example, synchronizing Red Hat Flatpaks from `registry.redhat.io` requires authentication. For more information, see [Creating Registry Service Accounts](https://access.redhat.com/articles/RegistryAuthentication#creating-registry-service-accounts-6).
6. Click **Create**.

## 15.2. Creating a Flatpak remote by using Hammer CLI

Add a Flatpak remote to your Satellite inventory to scan it, mirror selected repositories into your products, and distribute desktop application content to hosts.

**Prerequisites**

- Your Satellite account has a role that grants the `create_flatpak_remotes` permission.

**Procedure**

- Create your Flatpak remote:

  ```
  $ hammer flatpak-remote create \
  --name My_Flatpak_Remote_Name \
  --organization-id My_Organization_ID \
  --url My_Flatpak_Remote_URL
  ```

  For example, to use the Red Hat Flatpak index, enter: `https://flatpaks.redhat.io/rhel/`.

  If the Flatpak remote requires authentication, enter the required credentials. For example, synchronizing Red Hat Flatpaks from `registry.redhat.io` requires authentication. For more information, see [Creating Registry Service Accounts](https://access.redhat.com/articles/RegistryAuthentication#creating-registry-service-accounts-6).

## 15.3. Scanning a Flatpak remote by using Satellite web UI

Scan a Flatpak remote to discover the repositories its index hosts before you mirror them into products. Rescan the remote when new repositories are added.

**Prerequisites**

- A Flatpak remote exists in Satellite.
- Your Satellite account has a role that grants the `view_flatpak_remotes` and `edit_flatpak_remotes` permissions.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Flatpak Remotes**.
2. Select the Flatpak remote that you want to scan.
3. Click **Scan**.

## 15.4. Scanning a Flatpak remote by using Hammer CLI

Scan a Flatpak remote to discover the repositories its index hosts before you mirror them into products. Rescan the remote when new repositories are added.

**Prerequisites**

- A Flatpak remote exists in Satellite.
- Your Satellite account has a role that grants the `view_flatpak_remotes` and `edit_flatpak_remotes` permissions.

**Procedure**

- Scan your Flatpak remote:

  ```
  $ hammer flatpak-remote scan --id My_Flatpak_Remote_ID
  ```

## 15.5. Viewing Flatpak remote details by using Satellite web UI

Review the repositories a scanned Flatpak remote provides to decide which ones to mirror into your products.

**Prerequisites**

- The Flatpak remote has been scanned.
- Your Satellite account has a role that grants the `view_flatpak_remotes` permission.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Flatpak Remotes**.
2. Click the name of the Flatpak remote you want to view.
3. The page displays a list of repositories available from the scanned Flatpak remote.

## 15.6. Viewing Flatpak remote details by using Hammer CLI

Review the repositories a scanned Flatpak remote provides to decide which ones to mirror into your products.

**Prerequisites**

- The Flatpak remote has been scanned.
- Your Satellite account has a role that grants the `view_flatpak_remotes` permission.

**Procedure**

- View details of your Flatpak remote:

  ```
  $ hammer flatpak-remote info --id My_Flatpak_Remote_ID
  ```

## 15.7. Mirroring remote Flatpak repositories to Satellite products by using Satellite web UI

Mirror a Flatpak repository from a scanned remote into an existing product so you can synchronize it and publish application content to hosts through content views.

This action creates a new repository inside the product you selected. You can now synchronize the repository to pull down its content. Flatpak repositories are container repositories and you can add them to content views like other container repositories.

Flatpak applications require a corresponding runtime environment, which the Flatpak remote also provides. To make the Red Hat Enterprise Linux 10 Mozilla Firefox Flatpak available to a host, ensure that the host can access the matching `rhel10/flatpak-runtime` repository.

**Prerequisites**

- The Flatpak remote has been scanned.
- Your Satellite account has a role that grants the `view_flatpak_remotes` and `edit_flatpak_remotes` permissions.
- You have created a custom product on Satellite.
- Flatpak runtime repositories are available to hosts alongside application repositories. Flatpak applications, such as `rhel9/firefox-flatpak`, depend on the runtime for installation.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Flatpak Remotes**.
2. In the list of Flatpak Remotes, click the name of the remote you want to mirror.
3. In the list of remote repositories, locate the repository you want to mirror.
4. Select the **Mirror Action** menu on the row of the repository.
5. In the **Mirror** window, select the existing product where you want to create the new repository.
6. Click **Mirror**.

**Next steps**

- [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc")

## 15.8. Mirroring remote Flatpak repositories to Satellite products by using Hammer CLI

Mirror a Flatpak repository from a scanned remote into an existing product so you can synchronize it and publish application content to hosts through content views.

This action creates a new repository inside the product you selected. You can now synchronize the repository to pull down its content. Flatpak repositories are container repositories and you can add them to content views like other container repositories.

Flatpak applications require a corresponding runtime environment, which the Flatpak remote also provides. To make the Red Hat Enterprise Linux 10 Mozilla Firefox Flatpak available to a host, ensure that the host can access the matching `rhel10/flatpak-runtime` repository.

**Prerequisites**

- The Flatpak remote has been scanned.
- Your Satellite account has a role that grants the `view_flatpak_remotes` and `edit_flatpak_remotes` permissions.
- You have created a custom product on Satellite.
- Flatpak runtime repositories are available to hosts alongside application repositories. Flatpak applications, such as `rhel9/firefox-flatpak`, depend on the runtime for installation.

**Procedure**

- Mirror a Flatpak repository into your product:

  ```
  $ hammer flatpak-remote remote-repository mirror \
  --flatpak-remote-id My_Flatpak_Remote_ID \
  --id My_Flatpak_Repository_ID \
  --product-id My_Product_ID
  ```

**Next steps**

- [Section 4.2, “Synchronizing repositories ad hoc”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc "4.2. Synchronizing repositories ad hoc")
