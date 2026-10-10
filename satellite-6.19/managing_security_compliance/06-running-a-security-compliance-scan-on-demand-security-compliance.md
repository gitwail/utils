---
title: "Running a security compliance scan on demand"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_security_compliance"
guide_title: "Managing security compliance"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#running-a-security-compliance-scan-on-demand_security-compliance"
---
# Chapter 6. Running a security compliance scan on demand

Hosts perform OpenSCAP scans regularly by the CRON schedule defined in the compliance policies assigned to hosts. However, you can also run a scan on a host for all configured compliance policies manually at any time.

**Prerequisites**

- Your user account has a role assigned that has the `view_hosts`, `create_job_invocations`, and `view_job_invocations` permissions.
- You have created a compliance policy and deployed it on the host.

  - For more information about managing policies, see [Chapter 4, *Managing compliance policies*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#Managing_Compliance_Policies_security-compliance "Chapter 4. Managing compliance policies").
  - For more information about deploying policies, see [Chapter 5, *Deploying compliance policies*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#deploying-compliance-policies_security-compliance "Chapter 5. Deploying compliance policies").

**Procedure**

1. Navigate to **Hosts** > **All Hosts**.
2. Click the hostname of the required host.
3. On the host details page, expand the **Schedule a job** dropdown menu.
4. Select **Run OpenSCAP scan**.

**Verification**

1. In the host details overview, locate the **Recent jobs** card.
2. Select the **Running** tab. Unless the job has already finished, the table shows a job called **Run scan for all OpenSCAP policies**.
3. On the **Recent jobs** card, select the **Finished** tab.
4. If the job has finished successfully, you should see the **succeeded** status in the row of the job.
5. Optional: Click the job name to review invocation details.
