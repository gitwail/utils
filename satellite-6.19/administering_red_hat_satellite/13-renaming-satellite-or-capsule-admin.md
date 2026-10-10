---
title: "Renaming Satellite Server or Capsule Server"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "13"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#renaming-satellite-or-capsule_admin"
---
# Chapter 13. Renaming Satellite Server or Capsule Server

You can rename Satellite Server or Capsule Server when its hostname or domain changes. After renaming, it is important to update all references to avoid communication and certificate errors.

## 13.1. Renaming Satellite Server

Rename Satellite Server when its hostname or domain changes so that components, Capsule Servers, and registered hosts continue to communicate correctly. Use the `satellite-change-hostname` script and update all references to the new hostname.

> **Warning**
>
> Renaming your Satellite Server host shuts down all Satellite services on that host. The services restart after the renaming is complete.

**Prerequisites**

- You have a backup of your Satellite Server before changing its host name. If you fail to successfully rename it, restore it from the backup. For more information, see [Chapter 11, *Backing up Satellite Server and Capsule Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin "Chapter 11. Backing up Satellite Server and Capsule Server").
- The `hostname` and `hostname -f` commands on Satellite Server both return the FQDN of Satellite Server. If both commands do not return the FQDN of Satellite Server, the `satellite-change-hostname` script will fail to complete.

  If the `hostname` command returns the shortname of Satellite Server instead of the FQDN, use `hostnamectl set-hostname My_Old_FQDN` to set the old FQDN correctly before using the `satellite-change-hostname` script.
- If Satellite Server has a custom SSL certificate installed, you have a new certificate for the new FQDN of the host. For more information, see [Configuring Satellite Server with a Custom SSL Certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#configuring-satellite-custom-server-certificate_satellite) in *Installing Satellite Server in a connected network environment*.

**Procedure**

1. On Satellite Server, run the `satellite-change-hostname` script, and provide the new host name. Choose one of the following methods:

   - If your Satellite Server is installed with the default self-signed SSL certificates:

     ```
     # satellite-change-hostname new-satellite \
     --username My_Username \
     --password 'My_Password'
     ```
   - If your Satellite Server is installed with custom SSL certificates:

     ```
     # satellite-change-hostname new-satellite \
     --username My_Username \
     --password 'My_Password' \
     --custom-cert "/root/ownca/test.com/test.com.crt" \
     --custom-key "/root/ownca/test.com/test.com.key"
     ```
2. If you have created a custom SSL certificate for the new Satellite Server host name, run the Satellite installation script to install the certificate. For more information about installing a custom SSL certificate, see [Deploying a Custom SSL Certificate to Satellite Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#Deploying_a_Custom_SSL_Certificate_to_Server_satellite) in *Installing Satellite Server in a connected network environment*.
3. Reregister all hosts and Capsule Servers that are registered to Satellite Server. For more information, see [Registering hosts by using global registration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-by-using-global-registration) in *Managing hosts*.
4. On all Capsule Servers, run the Satellite installation script to update references to the new host name:

   ```
   # satellite-installer \
   --foreman-proxy-foreman-base-url https://new-satellite.example.com \
   --foreman-proxy-trusted-hosts new-satellite.example.com
   ```
5. On Satellite Server, list all Capsule Servers:

   ```
   # hammer capsule list
   ```
6. On Satellite Server, synchronize content for each Capsule Server:

   ```
   # hammer capsule content synchronize \
   --id My_Capsule_ID
   ```
7. If you use the *virt-who* agent, update the *virt-who* configuration files with the new host name. For more information, see [Modifying a virt-who Configuration](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_virt_who_for_virtual_machine_subscriptions/index#troubleshooting-virt-who#modifying-virt-who-configuration_vm-subs-satellite) in *Configuring virt-who for virtual machine subscriptions*.
8. If you use external authentication, reconfigure Satellite Server for external authentication after you run the `satellite-change-hostname` script. For more information, see [*Configuring authentication for Red Hat Satellite users*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_authentication_for_red_hat_satellite_users/index#).

## 13.2. Renaming Capsule Server

Rename Capsule Server when its hostname or domain changes so that Satellite components and registered hosts continue to communicate correctly. Use the `satellite-change-hostname` script and update certificates and references to the new hostname.

> **Warning**
>
> Renaming your Capsule Server host shuts down all Satellite services on that host. The services restart after the renaming is complete.

**Prerequisites**

- You have a backup of your Capsule Server before renaming. If you fail to successfully rename it, restore it from the backup. For more information, see [Chapter 11, *Backing up Satellite Server and Capsule Server*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#backing-up-satellite-server-and-capsule_admin "Chapter 11. Backing up Satellite Server and Capsule Server").
- The `hostname` and `hostname -f` commands on Capsule Server both return the FQDN of Capsule Server. If both commands do not return the FQDN of Capsule Server, the `satellite-change-hostname` script will fail to complete.

  If the `hostname` command returns the shortname of Capsule Server instead of the FQDN, use `hostnamectl set-hostname My_Old_FQDN` to set the old FQDN correctly before attempting to use the `satellite-change-hostname` script.

**Procedure**

1. On your Satellite Server, generate a new certificates archive file for your Capsule Server.

   - If you are using the default SSL certificate, regenerate the default SSL certificates:

     ```
     # capsule-certs-generate \
     --certs-tar /root/new-capsule.example.com-certs.tar \
     --foreman-proxy-fqdn new-capsule.example.com
     ```

     Ensure that you enter the full path to the `.tar` file.
   - If you are using a custom SSL certificate, create a new SSL certificate for your Capsule Server. For more information, see [Configuring Capsule Server with a custom SSL certificate](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#configuring-capsule-server-with-a-custom-ssl-certificate) in *Installing Capsule Server*.
2. On your Satellite Server, copy the certificates archive file to your Capsule Server. For example, to copy the archive file to the `root` user’s home directory:

   ```
   # scp /root/new-capsule.example.com-certs.tar root@capsule.example.com:
   ```
3. On your Capsule Server, run the `satellite-change-hostname` script and provide the host’s new name, Satellite credentials, and certificates archive file name.

   ```
   # satellite-change-hostname new-capsule.example.com \
   --certs-tar /root/new-capsule.example.com-certs.tar \
   --password 'My_Password' \
   --username My_Username
   ```

   Ensure that you enter the full path to the `.tar` file.
4. If you have created a custom certificate for your Capsule Server, deploy the certificate to your Capsule Server by entering the `satellite-installer` command that the `capsule-certs-generate` command returned in a previous step. For more information, see [Deploying a Custom SSL Certificate to Capsule Server](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#deploying-a-custom-ssl-certificate-to-capsule-server_capsule) in *Installing Capsule Server*.
5. Reregister all hosts that are registered to your Capsule Server. For more information, see [Registering hosts to Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#registering-hosts-to-satellite) in *Managing hosts*.
6. Update the Capsule host name in the Satellite web UI.

   1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
   2. Locate Capsule Server in the list, and click **Edit**.
   3. Edit the **Name** and **URL** fields to match Capsule Server’s new host name, then click **Submit**.
   4. On your DNS server, add a record for the new hostname of your Capsule Server, and delete the record of the previous host name.
