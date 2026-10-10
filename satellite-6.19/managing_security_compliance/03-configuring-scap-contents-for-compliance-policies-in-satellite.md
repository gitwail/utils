---
title: "Configuring SCAP contents for compliance policies in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_security_compliance"
guide_title: "Managing security compliance"
chapter_number: "3"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#configuring-scap-contents-for-compliance-policies-in-satellite"
---
# Chapter 3. Configuring SCAP contents for compliance policies in Satellite

You can upload SCAP data streams and tailoring files to define compliance policies. These policies define the requirements for scanning systems against security standards such as Defense Information Security Agency Security Technical Implementation Guide (DISA STIG) or Payment Card Industry Data Security Standard (PCI DSS).

## 3.1. Listing available SCAP contents using Satellite web UI

View what SCAP contents are already loaded in Satellite before uploading additional SCAP contents. You can use Satellite web UI to view available SCAP contents.

**Prerequisites**

- Your user account has a role assigned that has the `view_scap_contents` permission.

**Procedure**

- In the Satellite web UI, navigate to **Hosts** > **Compliance** > **SCAP contents**.

## 3.2. Listing available SCAP contents using CLI

View what SCAP contents are already loaded in Satellite before uploading additional SCAP contents. You can use Hammer CLI to view available SCAP contents.

**Prerequisites**

- Your user account has a role assigned that has the `view_scap_contents` permission.

**Procedure**

- Run the following Hammer command on Satellite Server:

  ```
  $ hammer scap-content list \
  --location "My_Location" \
  --organization "My_Organization"
  ```

## 3.3. Loading the default SCAP contents

By loading the default SCAP contents on Satellite Server, you ensure that the data streams from the SCAP Security Guide (SSG) are loaded and assigned to all organizations and locations.

SSG is provided by the operating system of Satellite Server and installed in `/usr/share/xml/scap/ssg/content/`. Note that the available data streams depend on the operating system version on which Satellite runs. You can only use this SCAP content to scan hosts that have the same minor RHEL version as your Satellite Server. For more information, see [Section 3.4, “Getting supported SCAP contents for RHEL”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#getting-supported-scap-contents-for-rhel_security-compliance "3.4. Getting supported SCAP contents for RHEL").

> **Important**
>
> The default SCAP contents on Satellite Server get updated with new patch versions of Satellite. They might not contain the latest available version of security policies but only the version that was available when the patch version was built. If the policy files in `/usr/share/xml/scap/ssg/content/` were updated after a new patch version became available, follow the procedure below to load them into Satellite.

**Prerequisites**

- Your user account has a role assigned that has the `create_scap_contents` permission.

**Procedure**

- On Satellite Server, load the default SCAP contents:

  ```
  $ hammer scap-content bulk-upload --type default
  ```

## 3.4. Getting supported SCAP contents for RHEL

You can obtain supported SCAP contents for Red Hat Enterprise Linux (RHEL) by downloading the latest SCAP Security Guide (SSG) to match your RHEL minor version from the Red Hat Customer Portal.

**Procedure**

1. Access the [SCAP Security Guide in the package browser](https://access.redhat.com/downloads/content/scap-security-guide/noarch/package-latest).
2. From the **Version** menu, select the latest SSG version for the minor version of RHEL that your hosts are running. For example, for RHEL 8.6, select a version named `*.el8_6`.
3. Download the RPM package.
4. Extract the data-stream file (`*-ds.xml`) from the RPM. For example:

   ```
   $ rpm2cpio scap-security-guide-0.1.69-3.el8_6.noarch.rpm \
   | cpio -iv --to-stdout ./usr/share/xml/scap/ssg/content/ssg-rhel8-ds.xml \
   > ssg-rhel-8.6-ds.xml
   ```
5. Upload the data stream to Satellite. For more information, see the following sections:

   - [Section 3.5, “Uploading additional SCAP content using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#uploading-additional-scap-content-using-web-ui "3.5. Uploading additional SCAP content using Satellite web UI")
   - [Section 3.6, “Uploading additional SCAP content using CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#uploading-additional-scap-content-using-cli "3.6. Uploading additional SCAP content using CLI")

**Additional resources**

- [SCAP Security Guide profiles supported in RHEL 9 in *Red Hat Enterprise Linux 9 Security hardening*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/scanning-the-system-for-configuration-compliance-and-vulnerabilities_security-hardening#scap-security-guide-profiles-supported-in-rhel-9_scanning-the-system-for-configuration-compliance-and-vulnerabilities)
- [SCAP Security Guide profiles supported in RHEL 8 in *Red Hat Enterprise Linux 8 Security hardening*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/security_hardening/scanning-the-system-for-configuration-compliance-and-vulnerabilities_security-hardening#scap-security-guide-profiles-supported-in-rhel_scanning-the-system-for-configuration-compliance-and-vulnerabilities)
- [SCAP Security Guide profiles supported in RHEL 7 in the *Red Hat Enterprise Linux 7 Security Guide*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/security_guide/scap-security-guide-profiles-supported-in-rhel-7_scanning-the-system-for-configuration-compliance-and-vulnerabilities)

## 3.5. Uploading additional SCAP content using Satellite web UI

You can upload additional SCAP content into Satellite Server, either content created by yourself or obtained elsewhere.

> **Note**
>
> Red Hat only provides support for SCAP content obtained from Red Hat.

**Prerequisites**

- Your user account has a role assigned that has the `create_scap_contents` permission.
- You have acquired a SCAP data-stream file.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Compliance** > **SCAP contents**.
2. Click **Upload New SCAP Content**.
3. Enter a title in the **Title** text box, such as `My SCAP Content`.
4. In **Scap File**, click **Choose file**, navigate to the location containing a SCAP data-stream file and click **Open**.
5. On the **Locations** tab, select locations.
6. On the **Organizations** tab, select organizations.
7. Click **Submit**.

**Verification**

- If the SCAP content file is loaded successfully, a message similar to `Successfully created My SCAP Content` is displayed.

## 3.6. Uploading additional SCAP content using CLI

You can upload additional SCAP content into Satellite Server, either content created by yourself or obtained elsewhere.

> **Note**
>
> Red Hat only provides support for SCAP content obtained from Red Hat.

**Prerequisites**

- Your user account has a role assigned that has the `create_scap_contents` permission.
- You have acquired a SCAP data-stream file.

**Procedure**

1. Place the SCAP data-stream file to a directory on your Satellite Server, such as `/usr/share/xml/scap/my_content/`.
2. Run the following Hammer command on Satellite Server:

   ```
   $ hammer scap-content bulk-upload --type directory \
   --directory /usr/share/xml/scap/my_content/ \
   --location "My_Location" \
   --organization "My_Organization"
   ```

**Verification**

- [List the available SCAP contents](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#listing-available-scap-contents-using-cli "3.2. Listing available SCAP contents using CLI"). The list of SCAP contents includes the new title.

## 3.7. Customizing XCCDF profiles with tailoring files

You can use tailoring files to customize existing XCCDF profiles without editing the original SCAP content. After uploading a tailoring file, you can apply it in a compliance policy to customize an XCCDF profile.

**Prerequisites**

- Your user account has a role assigned that has the `create_tailoring_files` permission.
- You have a tailoring file to upload to Satellite. You can create a tailoring file by using the [SCAP Workbench](https://www.open-scap.org/tools/scap-workbench/) tool. For more information on using the SCAP Workbench tool, see [Customizing SCAP Security Guide for your use case](https://www.open-scap.org/resources/documentation/customizing-scap-security-guide-for-your-use-case/).

  > **Note**
  >
  > A single tailoring file can contain customizations of multiple XCCDF profiles.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **Compliance** > **Tailoring Files**.
2. Click **New Tailoring File**.
3. Enter a name in the **Name** text box.
4. Click **Choose File**, navigate to the location containing the tailoring file and select **Open**.
5. Click **Submit** to upload the chosen tailoring file.
