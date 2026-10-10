---
title: "Anonymizing audit records"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "D"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#anonymizing-audit-records"
---
# Appendix D. Anonymizing audit records

You can anonymize audit records to remove user account and IP information while preserving the audit trail. This is useful for maintaining compliance with privacy regulations or internal security policies.

**Procedure**

- Use the `foreman-rake audits:anonymize` command to remove any user account or IP information while maintaining the audit records in the database. You can also use a cron job to schedule anonymizing the audit records at the set interval that you want.

  By default, using the `foreman-rake audits:anonymize` command anonymizes audit records that are older than 90 days. You can specify the number of days to keep the audit records by adding the **days** option and add the number of days.

  For example, you can anonymize audit records that are older than seven days:

  ```
  # foreman-rake audits:anonymize days=7
  ```
