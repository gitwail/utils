---
title: "Provisioning virtual machines on OpenShift Virtualization"
product: "Red Hat Satellite"
version: "6.19"
guide: "provisioning_hosts"
guide_title: "Provisioning hosts"
chapter_number: "13"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#provisioning-virtual-machines-on-openshift-virtualization"
---
# Chapter 13. Provisioning virtual machines on OpenShift Virtualization

You can create a compute resource for OpenShift Virtualization to provision and manage virtual machines in OpenShift Container Platform by using Satellite. OpenShift Virtualization enables development teams to run existing virtual machine workloads alongside containerized applications in Red Hat OpenShift Container Platform.

Note that template provisioning is not supported for this release.

> **Important**
>
> The OpenShift Virtualization compute resource is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Before you start provisioning virtual machines on OpenShift Virtualization, ensure that your environment meets the following requirements:

- You must have the `get`, `delete`, `create`, `update`, `patch`, `list`, and `watch` permissions for VMs and other OpenShift Virtualization resources for the OpenShift Container Platform cluster in the specified namespace. You can get these permissions with the `kubevirt.io:edit` cluster role.
- To use auto-completion for network selection, you must have the `get` and `list` permissions for the `network-attachment-definitions.k8s.cni.cncf.io` resource.

- You can use synchronized content repositories for Red Hat Enterprise Linux. For more information, see [Synchronizing repositories ad hoc](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-repositories-ad-hoc) in *Managing content*.
- Provide an activation key for host registration. For more information, see [Creating an activation key by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-an-activation-key-by-using-web-ui) in *Managing content*.
- A Capsule Server managing a network on the OpenShift Container Platform cluster. Ensure that no other DHCP services run on this network to avoid conflicts with Capsule Server.
- Ensure the provisioning user has the required permissions to provision hosts.

> **Warning**
>
> By default, deleting a host entry associated with a virtual machine does not destroy the virtual machine on the compute resource.
>
> To change the default behavior, navigate to **Administer** > **Settings** > **Provisioning** and set **Destroy associated VM on host delete** to **Yes**.

**Additional resources**

- [Chapter 2, *Preparing networking for host management*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#preparing-networking-for-host-management "Chapter 2. Preparing networking for host management")
- [Authorization for OpenShift Container Platform Virtualization](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/virtualization/about#authorization_virt-security-policies)
- [Appendix D, *Permissions required to provision hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#permissions-required-to-provision-hosts "Appendix D. Permissions required to provision hosts")

## 13.1. Adding an OpenShift Virtualization connection to Satellite Server

To provision and manage virtual machines on OpenShift Container Platform, add OpenShift Virtualization as a compute resource to Satellite.

**Prerequisites**

- You have the `oc` command-line tool installed.

**Procedure**

1. Enter the following `satellite-installer` command to enable the OpenShift Virtualization plugin for Satellite:

   ```
   # satellite-installer --enable-foreman-plugin-kubevirt
   ```
2. Obtain a token to use for HTTP and HTTPs authentication:

   1. Create a service account:

      ```
      $ oc create serviceaccount My_Service_Account --namespace My_Namespace
      ```
   2. Add the `kubevirt.io:edit` role to the service account:

      ```
      $ oc create rolebinding My_Service_Account-kubevirt-edit --clusterrole=kubevirt.io:edit --serviceaccount=My_Namespace:My_Service_Account
      ```
   3. Add the `view` role to the service account:

      ```
      $ oc create rolebinding My_Service_Account-view --clusterrole=view --serviceaccount=My_Namespace:My_Service_Account
      ```
   4. Create a persistent token for the account:

      ```
      $ oc create --filename=- <<EOF
      apiVersion: v1
      kind: Secret
      metadata:
        name: My_SA_Token
        annotations:
          kubernetes.io/service-account.name: My_Service_Account
      type: kubernetes.io/service-account-token
      EOF
      ```
   5. Record the token to use later in this procedure.

      ```
      $ oc get secrets My_SA_Token --template='{{.data.token | base64decode}}'
      ```
3. In the Satellite web UI, navigate to **Infrastructure** > **Compute Resources**, and click **Create Compute Resource**.
4. In the **Name** field, enter a name for the new compute resource.
5. From the **Provider** list, select **OpenShift Virtualization**.
6. In the **Description** field, enter a description for the compute resource.
7. In the **Hostname** field, enter the FQDN, hostname, or IP address of the OpenShift Container Platform cluster.
8. In the **API Port** field, enter the port number that you want to use for provisioning requests from Satellite to OpenShift Virtualization.
9. In the **Namespace** field, enter the namespace of the OpenShift Container Platform cluster.
10. In the **Token** field, enter the token you recorded.
11. Optional: In the **X509 Certification Authorities** field, enter a certificate to enable client certificate authentication for API server calls.

**Additional resources**

- [OpenShift CLI (oc)](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/cli_tools/openshift-cli-oc)
