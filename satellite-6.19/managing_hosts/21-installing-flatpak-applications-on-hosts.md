---
title: "Installing Flatpak applications on hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "21"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#installing-flatpak-applications-on-hosts"
---
# Chapter 21. Installing Flatpak applications on hosts

After you synchronize Flatpak repositories in Satellite, you can install Flatpak applications on hosts from Satellite Server or Capsule Server. On each host, add a Flatpak remote, authenticate to the container registry, and install the applications you need.

**Additional resources**

- [Managing Flatpak repositories in Satellite in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-flatpak-repositories-in-project)
- [Installing applications using Flatpak](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/administering_the_system_using_the_gnome_desktop_environment/assembly_installing-applications-using-flatpak_administering-the-system-using-the-gnome-desktop-environment)

## 21.1. Configuring Podman to trust the certificate authority

Configure Podman to trust the Satellite certificate authority so that you can push and pull container images without disabling TLS verification.

Podman locates the CA file in the `/etc/containers/certs.d/` path. Copy the root CA file to that path, with the exact path determined by the server hostname, and name the file `ca.crt`.

In the following examples, replace `hostname.example.com` with `satellite.example.com` or `capsule.example.com`, depending on your use case.

**Prerequisites**

- You have the root CA certificate file for Satellite Server or Capsule Server.
- You have root or sudo access on the host where Podman is installed.

**Procedure**

1. Create the relevant directory:

   ```
   # mkdir --parents /etc/containers/certs.d/hostname.example.com
   ```
2. Copy the CA file to the directory:

   ```
   # cp My_Root_CA.pem /etc/containers/certs.d/hostname.example.com/ca.crt
   ```

**Verification**

- Verify that you no longer need to use the `--tls-verify=false` option when logging in to the registry:

  ```
  $ podman login hostname.example.com
  ```

## 21.2. Installing Flatpak applications on a host from Satellite Server

Connect your host to the Flatpak remote on Satellite Server, authenticate to the container registry, and install Flatpak applications published through your content views.

**Prerequisites**

- Flatpak is installed on the host. For more information, see [Setting up Flatpak](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/administering_the_system_using_the_gnome_desktop_environment/assembly_installing-applications-using-flatpak_administering-the-system-using-the-gnome-desktop-environment#setting-up-flatpak_assembly_installing-applications-using-flatpak).
- Flatpak application repositories are published through content views.
- Flatpak runtime repositories are available to hosts alongside application repositories. Flatpak applications, such as `rhel9/firefox-flatpak`, depend on the runtime for installation.
- The Red Hat Flatpak remote is enabled.
- Podman is installed on the host.
- Podman is configured to trust the certificate authority of Satellite Server. For more information, see [Section 21.1, “Configuring Podman to trust the certificate authority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-podman-to-trust-the-certificate-authority "21.1. Configuring Podman to trust the certificate authority").
- Your Satellite account has the `view_lifecycle_environments`, `view_products`, and `view_content_views` permissions, unless the lifecycle environment allows unauthenticated pull.
- Your Satellite account has a role that grants the `create_personal_access_tokens` permission to generate an access token for authentication. Satellite generates a token automatically when you run `podman login`.

**Procedure**

1. On the managed host, add your Satellite Server as a Flatpak remote:

   ```
   $ flatpak remote-add --authenticator-name=org.flatpak.Authenticator.Oci katello oci+https://satellite.example.com/
   ```
2. Log in the host to the container registry using one of the following methods:

   - Certificate authentication

     - When registering a host to Satellite or Capsule, select the **Set up container registry certs** checkbox.
     - If the host is already registered, run the **Flatpak - Login to registry via podman** job template on the host. Set **Set up certificate authentication** to `true` and enter the URL of your Capsule as the registry URL.
   - Using Podman

     - Log in using Podman:

       ```
       $ podman login satellite.example.com
       ```
3. Install your application. For example, to install the Mozilla Firefox Flatpak:

   ```
   $ flatpak install firefox
   ```

**Additional resources**

- [Launching Flatpak applications](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/administering_the_system_using_the_gnome_desktop_environment/assembly_installing-applications-using-flatpak_administering-the-system-using-the-gnome-desktop-environment#launching-flatpak-applications_assembly_installing-applications-using-flatpak)
- [Updating Flatpak applications](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/administering_the_system_using_the_gnome_desktop_environment/assembly_installing-applications-using-flatpak_administering-the-system-using-the-gnome-desktop-environment#updating-flatpak-applications_assembly_installing-applications-using-flatpak)

## 21.3. Installing Flatpak applications on a host from Capsule Server

Connect your host to the Flatpak remote on Capsule Server, authenticate to the container registry, and install Flatpak applications.

> **Note**
>
> Capsules synchronize Flatpaks and make them available to all hosts, but not organizations, content views, or lifecycle environments. Clients receive the latest Flatpaks synchronized on the Capsule globally.

**Prerequisites**

- Flatpak repositories are synchronized to Capsule Server. For more information, see [Adding lifecycle environments to Capsule Servers by using Satellite web UI in *Managing content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-lifecycle-environments-by-using-web-ui).
- Flatpak is installed on the host. For more information, see [Setting up Flatpak](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/administering_the_system_using_the_gnome_desktop_environment/assembly_installing-applications-using-flatpak_administering-the-system-using-the-gnome-desktop-environment#setting-up-flatpak_assembly_installing-applications-using-flatpak).
- Flatpak runtime repositories are available to hosts alongside application repositories. Flatpak applications, such as `rhel9/firefox-flatpak`, depend on the runtime for installation.
- Podman is installed on the host.
- Podman is configured to trust the certificate authority of Capsule Server. For more information, see [Section 21.1, “Configuring Podman to trust the certificate authority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-podman-to-trust-the-certificate-authority "21.1. Configuring Podman to trust the certificate authority").

**Procedure**

1. On the managed host, add the Capsule as a Flatpak remote:

   ```
   $ flatpak remote-add --authenticator-name=org.flatpak.Authenticator.Oci katello oci+https://capsule.example.com/
   ```
2. Log in the host to the container registry using one of the following methods:

   - Certificate authentication

     - When registering a host to Capsule, select the **Set up container registry certs** checkbox.
     - If the host is already registered, run the **Flatpak - Login to registry via podman** job template on the host. Set **Set up certificate authentication** to `true` and enter the URL of your Capsule as the registry URL.
   - Using Podman

     - Log in using Podman:

       ```
       $ podman login capsule.example.com
       ```

       You might need to log in to the registry again if you have not saved your credentials.
3. Optional: Save your credentials permanently using one of the following options:

   - To save the credentials for the current user:

     ```
     $ cp $XDG_RUNTIME_DIR/containers/auth.json $HOME/.config/flatpak/oci-auth.json
     ```
   - To save the credentials system-wide:

     ```
     $ cp $XDG_RUNTIME_DIR/containers/auth.json /etc/flatpak/oci-auth.json
     ```
4. Install your application. For example, to install the Mozilla Firefox Flatpak:

   ```
   $ flatpak install firefox
   ```
