---
title: "Required Red Hat repositories"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "A"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#required-red-hat-repositories"
---
# Appendix A. Required Red Hat repositories

Enable the Red Hat repositories for your release and host architecture so Satellite can synchronize content from the Red Hat CDN to manage Red Hat Enterprise Linux hosts. Enable matching Kickstart repositories when you provision hosts with the Anaconda installer.

To register and manage hosts with Satellite, you need the following repositories:

For Red Hat Enterprise Linux 10 hosts
:   - Red Hat Enterprise Linux 10 for x86_64 - BaseOS (RPMs)
    - Red Hat Enterprise Linux 10 for x86_64 - AppStream (RPMs)

For Red Hat Enterprise Linux 9 hosts
:   - Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)
    - Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)

For Red Hat Enterprise Linux 8 hosts
:   - Red Hat Enterprise Linux 8 for x86_64 - BaseOS (RPMs)
    - Red Hat Enterprise Linux 8 for x86_64 - AppStream (RPMs)

For Red Hat Enterprise Linux 7 hosts
:   - Red Hat Enterprise Linux 7 Server (RPMs)

To provision hosts by using the Anaconda installer with Kickstart, you additionally need the following repositories:

For Red Hat Enterprise Linux 10 hosts
:   - Red Hat Enterprise Linux 10 for x86_64 - BaseOS (Kickstart)
    - Red Hat Enterprise Linux 10 for x86_64 - AppStream (Kickstart)

For Red Hat Enterprise Linux 9 hosts
:   - Red Hat Enterprise Linux 9 for x86_64 - BaseOS (Kickstart)
    - Red Hat Enterprise Linux 9 for x86_64 - AppStream (Kickstart)

For Red Hat Enterprise Linux 8 hosts
:   - Red Hat Enterprise Linux 8 for x86_64 - BaseOS (Kickstart)
    - Red Hat Enterprise Linux 8 for x86_64 - AppStream (Kickstart)

For Red Hat Enterprise Linux 7 hosts
:   - Red Hat Enterprise Linux 7 Server (Kickstart)

For other supported architectures, substitute your architecture for x86_64 in the repository names.
