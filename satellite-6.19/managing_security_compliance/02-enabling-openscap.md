---
title: "Enabling OpenSCAP"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_security_compliance"
guide_title: "Managing security compliance"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#enabling-openscap"
---
# Chapter 2. Enabling OpenSCAP

The OpenSCAP plugin is enabled on your Satellite Server by default. To use the OpenSCAP plugin and SCAP content on Capsule Servers, you must enable OpenSCAP on each Capsule Server.

**Procedure**

- Enable OpenSCAP on your Capsule Server:

  ```
  # satellite-installer \
  --enable-foreman-proxy-plugin-openscap \
  --foreman-proxy-plugin-openscap-ansible-module true \
  --foreman-proxy-plugin-openscap-puppet-module true
  ```

**Verification**

1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**.
2. Select your Capsule.
3. Verify that the OpenSCAP feature is active.

**Next steps**

- If you want to use Puppet to deploy compliance policies, you must enable it first. For more information, see [*Managing configurations by using Puppet integration*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#).
