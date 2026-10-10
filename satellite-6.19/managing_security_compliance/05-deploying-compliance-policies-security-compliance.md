---
title: "Deploying compliance policies"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_security_compliance"
guide_title: "Managing security compliance"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#deploying-compliance-policies_security-compliance"
---
# Chapter 5. Deploying compliance policies

To deploy a compliance policy, you must install the SCAP client, update the cron schedule file, and upload the SCAP content selected in the policy onto a host. You specify the schedule for scans on Satellite and the scans are performed on hosts.

When a scan completes, a report in ARF format is generated and uploaded to Satellite. A compliance policy scan makes no changes to hosts.

## 5.1. Inclusion of remote SCAP resources

SCAP data streams can reference remote resources, such as OVAL files, that the SCAP client fetches over the internet when it runs on hosts. You can enable the download of these remote resources for hosts with internet access.

If a data stream requires a remote resource, you can see a warning from the OpenSCAP Scanner tool on your Satellite Server, such as:

```
# oscap info /usr/share/xml/scap/ssg/content/ssg-rhel8-ds.xml | grep "WARNING"
WARNING: Datastream component 'scap_org.open-scap_cref_security-data-oval-com.redhat.rhsa-RHEL8.xml.bz2'
points out to the remote 'https://access.redhat.com/security/data/oval/com.redhat.rhsa-RHEL8.xml.bz2'.
Use '--fetch-remote-resources' option to download it.
WARNING: Skipping 'https://access.redhat.com/security/data/oval/com.redhat.rhsa-RHEL8.xml.bz2' file
which is referenced from datastream
```

By default, the SCAP client is configured to ignore the remote resources and skip the XCCDF rules that rely on the resources. The skipped rules then result in the `notchecked` status.

For hosts with internet access, you can enable the download of remote resources on hosts in Satellite. For information about applying remote SCAP resources to hosts that cannot access the internet, see [Section 5.2, “Applying remote SCAP resources in a disconnected environment”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#applying-remote-scap-resources-in-a-disconnected-environment_security-compliance "5.2. Applying remote SCAP resources in a disconnected environment").

Using the Ansible deployment method
:   Override the following Ansible variable:

    - Name: `foreman_scap_client_fetch_remote_resources`
    - Type: `boolean`
    - Value: `true`

    For more information, see [Overriding Ansible Variables in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_ansible_integration/index#Overriding_Ansible_Variables_in_satellite_ansible) in *Managing configurations by using Ansible integration*.

Using the Puppet deployment method
:   Configure the following Puppet Smart Class Parameter:

    - Name: `fetch_remote_resources`
    - Type: `boolean`
    - Value: `true`

    For more information, see [Configuring Puppet Smart Class Parameters](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#Configuring_Puppet_Smart_Class_Parameters_managing-configurations-puppet) in *Managing configurations by using Puppet integration*.

## 5.2. Applying remote SCAP resources in a disconnected environment

SCAP data streams can contain remote resources, such as OVAL files, that the SCAP client can fetch over the internet when it runs on hosts. If your hosts do not have internet access, you must download remote SCAP resources and distribute them from Satellite Server to your hosts as local files.

**Prerequisites**

- You have registered your host to Satellite with remote execution enabled.
- Fetching remote resources must be disabled, which is the default. For more information, see [Section 5.1, “Inclusion of remote SCAP resources”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#inclusion-of-remote-scap-resources_security-compliance "5.1. Inclusion of remote SCAP resources").

**Procedure**

1. On your Satellite Server, examine the data stream you use in your compliance policy to find out which missing resource you must download:

   ```
   # oscap info /usr/share/xml/scap/ssg/content/ssg-rhel8-ds.xml | grep "WARNING"
   WARNING: Datastream component 'scap_org.open-scap_cref_security-data-oval-com.redhat.rhsa-RHEL8.xml.bz2'
   points out to the remote 'https://access.redhat.com/security/data/oval/com.redhat.rhsa-RHEL8.xml.bz2'.
   Use '--fetch-remote-resources' option to download it.
   WARNING: Skipping 'https://access.redhat.com/security/data/oval/com.redhat.rhsa-RHEL8.xml.bz2' file
   which is referenced from datastream
   ```
2. Examine the name of the local file that is referenced by the data stream:

   ```
   # oscap info /usr/share/xml/scap/ssg/content/ssg-rhel8-ds.xml
   ...
   		Referenced check files:
   			ssg-rhel8-oval.xml
   				system: http://oval.mitre.org/XMLSchema/oval-definitions-5
   			ssg-rhel8-ocil.xml
   				system: http://scap.nist.gov/schema/ocil/2
   			security-data-oval-com.redhat.rhsa-RHEL8.xml.bz2
   				system: http://oval.mitre.org/XMLSchema/oval-definitions-5
   ...
   ```
3. On an online machine, download the missing resource:

   ```
   # curl -o security-data-oval-com.redhat.rhsa-RHEL8.xml.bz2 https://www.redhat.com/security/data/oval/com.redhat.rhsa-RHEL8.xml.bz2
   ```

   > **Important**
   >
   > Ensure that the name of the downloaded file matches the name the data stream references.
4. Add the file as new custom file type content into your Satellite Server. For more information, see [Managing custom file type content in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-custom-file-type-content-in-satellite) in *Managing content*.

   Note the URL on which your repository is published, such as `http://satellite.example.com/pulp/content/My_Organization_Label/Library/custom/My_Product_Label/My_Repo_Label/`.
5. Schedule a remote job to upload the file to the home directory of `root` on your host. For example, use the `Run Command - Script Default` job template and enter the following command:

   ```
   # curl -o /root/security-data-oval-com.redhat.rhsa-RHEL8.xml.bz2 http://satellite.example.com/pulp/content/My_Organization_Label/Library/custom/My_Product_Label/My_Repo_Label/security-data-oval-com.redhat.rhsa-RHEL8.xml.bz2
   ```

   For more information about running remote jobs, see [Configuring and setting up remote jobs](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs) in *Managing hosts*.

**Next steps**

- Continue with deploying your compliance policy.

**Additional resources**

- [Downloading files to a host from a custom file type repository by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#downloading-files-to-a-host-from-a-custom-file-type-repository-by-using-web-ui)

## 5.3. Deploying a policy in a host group using Ansible

After you deploy a compliance policy in a host group using Ansible, the Ansible role installs the SCAP client and configures OpenSCAP scans on the hosts according to the selected compliance policy.

The SCAP content in the compliance policy might require remote resources. For more information, see [Section 5.1, “Inclusion of remote SCAP resources”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#inclusion-of-remote-scap-resources_security-compliance "5.1. Inclusion of remote SCAP resources").

**Prerequisites**

- You have enabled OpenSCAP on your Capsule. For more information, see [Chapter 2, *Enabling OpenSCAP*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#enabling-openscap "Chapter 2. Enabling OpenSCAP").
- Repositories for the operating system version of the host are synchronized on Satellite Server and enabled on the host.

  - Red Hat Enterprise Linux 10: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 9: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 8: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 7: Server and Extras RPMs repositories
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server, available in the content view environments of the host, and enabled for the host. For more information, see [Changing the repository sets status for a host in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Changing_the_Repository_Sets_Status_for-a-Host-in_satellite_content-management) in *Managing content*. This repository is required for installing the SCAP client.
- You have [created a compliance policy](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Creating_a_Compliance_Policy_security-compliance "4.2. Creating a compliance policy") with the Ansible deployment option and assigned the host group.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. Click the host group that you want to configure for OpenSCAP reporting.
3. From the **OpenSCAP Capsule** list, select the Capsule with OpenSCAP enabled that you want to use.
4. On the **Ansible Roles** tab, assign the `theforeman.foreman_scap_client` Ansible role.
5. Optional: On the **Parameters** tab, configure any Ansible variables of the role.
6. Click **Submit** to save your changes.
7. In the row of the required host group, navigate to the **Actions** column and select **Run all Ansible roles**.

## 5.4. Deploying a policy on a host using Ansible

After you deploy a compliance policy on a host using Ansible, the Ansible role installs the SCAP client and configures OpenSCAP scans on the host according to the selected compliance policy.

The SCAP content in the compliance policy might require remote resources. For more information, see [Section 5.1, “Inclusion of remote SCAP resources”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#inclusion-of-remote-scap-resources_security-compliance "5.1. Inclusion of remote SCAP resources").

**Prerequisites**

- You have enabled OpenSCAP on your Capsule. For more information, see [Chapter 2, *Enabling OpenSCAP*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#enabling-openscap "Chapter 2. Enabling OpenSCAP").
- Repositories for the operating system version of the host are synchronized on Satellite Server and enabled on the host.

  - Red Hat Enterprise Linux 10: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 9: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 8: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 7: Server and Extras RPMs repositories
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server, available in the content view environments of the host, and enabled for the host. For more information, see [Changing the repository sets status for a host in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Changing_the_Repository_Sets_Status_for-a-Host-in_satellite_content-management) in *Managing content*. This repository is required for installing the SCAP client.
- You have [created a compliance policy](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Creating_a_Compliance_Policy_security-compliance "4.2. Creating a compliance policy") with the Ansible deployment option.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select **Edit** on the host you want to configure for OpenSCAP reporting.
3. From the **OpenSCAP Capsule** list, select the Capsule with OpenSCAP enabled that you want to use.
4. On the **Ansible Roles** tab, add the `theforeman.foreman_scap_client` Ansible role.
5. Optional: On the **Parameters** tab, configure any Ansible variables of the role.
6. Click **Submit** to save your changes.
7. Click the **Hosts** breadcrumbs link to navigate back to the host index page.
8. From the top options menu, select **Legacy UI**.
9. Select the host or hosts to which you want to add the policy.
10. Click **Select Action**.
11. Select **Assign Compliance Policy** from the list.
12. In the **Assign Compliance Policy** window, select **Remember hosts selection for the next bulk action**.
13. Select the required policy from the list of available policies and click **Submit**.
14. Click **Select Action**.
15. Select **Run all Ansible roles** from the list.

## 5.5. Deploying a policy in a host group using Puppet

After you deploy a compliance policy in a host group using Puppet, the OpenVox agent installs the SCAP client and configures OpenSCAP scans on the hosts on the next Puppet run according to the selected compliance policy.

The SCAP content in your compliance policy might require remote resources. For more information, see [Section 5.1, “Inclusion of remote SCAP resources”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#inclusion-of-remote-scap-resources_security-compliance "5.1. Inclusion of remote SCAP resources").

**Prerequisites**

- You have enabled OpenSCAP on your Capsule. For more information, see [Chapter 2, *Enabling OpenSCAP*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#enabling-openscap "Chapter 2. Enabling OpenSCAP").
- Repositories for the operating system version of the host are synchronized on Satellite Server and enabled on the host.

  - Red Hat Enterprise Linux 10: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 9: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 8: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 7: Server and Extras RPMs repositories
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server, available in the content view environments of the host, and enabled for the host. For more information, see [Changing the repository sets status for a host in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Changing_the_Repository_Sets_Status_for-a-Host-in_satellite_content-management) in *Managing content*. This repository is required for installing the SCAP client.
- You have [created a compliance policy](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Creating_a_Compliance_Policy_security-compliance "4.2. Creating a compliance policy") with the Puppet deployment option and assigned the host group.

**Procedure**

1. In the Satellite web UI, navigate to **Configure** > **Host Groups**.
2. Click the host group that you want to configure for OpenSCAP reporting.
3. In the **Environment** list, select the Puppet environment that contains the `foreman_scap_client*` Puppet classes.
4. In the **OpenSCAP Capsule** list, select the Capsule with OpenSCAP enabled that you want to use.
5. On the **Puppet ENC** tab, add the `foreman_scap_client` Puppet class.
6. Optional: Configure any **Puppet Class Parameters**.
7. Click **Submit** to save your changes.

## 5.6. Deploying a policy on a host using Puppet

After you deploy a compliance policy on a host using Puppet, the OpenVox agent installs the SCAP client and configures OpenSCAP scans on the host on the next Puppet run according to the selected compliance policy.

The SCAP content in your compliance policy might require remote resources. For more information, see [Section 5.1, “Inclusion of remote SCAP resources”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#inclusion-of-remote-scap-resources_security-compliance "5.1. Inclusion of remote SCAP resources").

**Prerequisites**

- You have enabled OpenSCAP on your Capsule. For more information, see [Chapter 2, *Enabling OpenSCAP*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#enabling-openscap "Chapter 2. Enabling OpenSCAP").
- Repositories for the operating system version of the host are synchronized on Satellite Server and enabled on the host.

  - Red Hat Enterprise Linux 10: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 9: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 8: BaseOS and AppStream RPMs repositories
  - Red Hat Enterprise Linux 7: Server and Extras RPMs repositories
- Red Hat Satellite Client 6 repository for the operating system version of the host is synchronized on Satellite Server, available in the content view environments of the host, and enabled for the host. For more information, see [Changing the repository sets status for a host in Satellite](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Changing_the_Repository_Sets_Status_for-a-Host-in_satellite_content-management) in *Managing content*. This repository is required for installing the SCAP client.
- You have [created a compliance policy](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Creating_a_Compliance_Policy_security-compliance "4.2. Creating a compliance policy") with the Puppet deployment option.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Select **Edit** on the host you want to configure for OpenSCAP reporting.
3. From the **Environment** list, select the Puppet environment that contains the `foreman_scap_client` and `foreman_scap_client::params` Puppet classes.
4. From the **OpenSCAP Capsule** list, select the Capsule with OpenSCAP enabled that you want to use.
5. On the **Puppet ENC** tab, add the `foreman_scap_client` Puppet class.
6. Optional: Configure any **Puppet Class Parameters**.
7. Click the **Hosts** breadcrumbs link to navigate back to the host index page.
8. From the top options menu, select **Legacy UI**.
9. Select the host or hosts to which you want to add the policy.
10. Click **Select Action**.
11. Select **Assign Compliance Policy** from the list.
12. In the **Assign Compliance Policy** window, select **Remember hosts selection for the next bulk action**.
13. Select the required policy from the list of available policies and click **Submit**.
