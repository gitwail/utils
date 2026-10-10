---
title: "Propagating SCAP content through the load balancer"
product: "Red Hat Satellite"
version: "6.19"
guide: "configuring_capsules_with_a_load_balancer"
guide_title: "Configuring Capsules with a load balancer"
chapter_number: "10"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/configuring_capsules_with_a_load_balancer/index#propagating-scap-content-through-the-load-balancer_load-balancing"
---
# Chapter 10. Propagating SCAP content through the load balancer

If you use OpenSCAP to manage security compliance on your clients, you must configure the SCAP client to send ARF reports to the load balancer instead of Capsule. The configuration procedure depends on the method you have selected to deploy compliance policies.

## 10.1. Propagating SCAP content using Ansible deployment

Propagate Security Content Automation Protocol (SCAP) content through the load balancer when using Ansible deployment so that compliance reports reach Satellite through the load balancer.

**Prerequisites**

- Ensure that you have configured Satellite for Ansible deployment of compliance policies. For more information, see [Configuring Compliance Policy Deployment Methods](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#configuring-compliance-policy-deployment-methods_security-compliance) in *Managing security compliance*.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Ansible** > **Variables**.
2. Search for the `foreman_scap_client_port` variable and click its name.
3. In the **Default Behavior** area, ensure that the **Override** checkbox is selected.
4. In the **Parameter Type** list, ensure that `integer` is selected.
5. In the **Default Value** field, enter `9090`.
6. In the **Specify Matchers** area, remove all matchers that override the default value.
7. Click **Submit**.
8. Search for the `foreman_scap_client_server` variable and click its name.
9. In the **Default Behavior** area, ensure that the **Override** checkbox is selected.
10. In the **Parameter Type** list, ensure that `string` is selected.
11. In the **Default Value** field, enter the FQDN of your load balancer, such as `loadbalancer.example.com`.
12. In the **Specify Matchers** area, remove all matchers that override the default value.
13. Click **Submit**.
14. Continue with deploying a compliance policy using Ansible. For more information, see:

    - [Deploying a Policy in a Host Group Using Ansible](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Deploying_a_Policy_in_a_Host_Group_Using_Ansible_security-compliance) in *Managing security compliance*
    - [Deploying a Policy on a Host Using Ansible](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Deploying_a_Policy_on_a_Host_Using_Ansible_security-compliance) in *Managing security compliance*

**Verification**

- On the client, verify that the `/etc/foreman_scap_client/config.yaml` file contains the following lines:

  ```yaml
  # Foreman proxy to which reports should be uploaded
  :server: 'loadbalancer.example.com'
  :port: 9090
  ```

## 10.2. Propagating SCAP content using Puppet deployment

Propagate Security Content Automation Protocol (SCAP) content through the load balancer when using Puppet deployment so that compliance reports reach Satellite through the load balancer.

**Prerequisites**

- Ensure that you have configured Satellite for Puppet deployment of compliance policies. For more information, see [Configuring Compliance Policy Deployment Methods](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#configuring-compliance-policy-deployment-methods_security-compliance) in *Managing security compliance*.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Puppet ENC** > **Classes**.
2. Click `foreman_scap_client`.
3. Click the **Smart Class Parameter** tab.
4. In the pane to the left of the **Smart Class Parameter** window, click `port`.
5. In the **Default Behavior** area, select the **Override** checkbox.
6. From the **Key Type** list, select `integer`.
7. In the **Default Value** field, enter `9090`.
8. In the pane to the left of the **Smart Class Parameter** window, click `server`.
9. In the **Default Behavior** area, select the **Override** checkbox.
10. From the **Key Type** list, select `string`.
11. In the **Default Value** field, enter the FQDN of your load balancer, such as `loadbalancer.example.com`.
12. In the lower left of the **Smart Class Parameter** window, click **Submit**.
13. Continue with deploying a compliance policy using Puppet. For more information, see:

    - [Deploying a Policy in a Host Group Using Puppet](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Deploying_a_Policy_in_a_Host_Group_Using_Puppet_security-compliance) in *Managing security compliance*
    - [Deploying a Policy on a Host Using Puppet](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Deploying_a_Policy_on_a_Host_Using_Puppet_security-compliance) in *Managing security compliance*

**Verification**

- On the client, verify that the `/etc/foreman_scap_client/config.yaml` file contains the following lines:

  ```yaml
  # Foreman proxy to which reports should be uploaded
  :server: 'loadbalancer.example.com'
  :port: 9090
  ```
