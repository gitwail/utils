---
title: "Technical users provided and required by Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "A"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#technical-users-provided-and-required-by-satellite"
---
# Appendix A. Technical users provided and required by Satellite

The Satellite installation process automatically creates system accounts. They manage files and process ownership of the components integrated into Satellite. The following table lists all the accounts created by Satellite during installation.

Some of these accounts have fixed UIDs and GIDs, while others take the next available UID and GID on the system instead. To control the UIDs and GIDs assigned to accounts, you can define accounts before installing Satellite. Because some of the accounts have hard-coded UIDs and GIDs, it is not possible to do this with all accounts created during Satellite installation.

You can predefine accounts that have **Yes** in the **Flexible UID and GID** column with custom UID and GID before installing Satellite.

Do not change the home and shell directories of system accounts because they are requirements for Satellite.

Because of potential conflicts with local users that Satellite creates, you cannot use external identity providers for the system users of the Satellite base operating system.

Table A.1. Technical users provided and required by Satellite

| User name | UID | Group name | GID | Flexible UID and GID | Home | Shell |
| --- | --- | --- | --- | --- | --- | --- |
| foreman | N/A | foreman | N/A | yes | /usr/share/foreman | /sbin/nologin |
| foreman-proxy | N/A | foreman-proxy | N/A | yes | /usr/share/foreman-proxy | /sbin/nologin |
| apache | 48 | apache | 48 | no | /usr/share/httpd | /sbin/nologin |
| postgres | 26 | postgres | 26 | no | /var/lib/pgsql | /bin/bash |
| pulp | N/A | pulp | N/A | no | N/A | /sbin/nologin |
| puppet | 52 | puppet | 52 | no | /opt/puppetlabs/server/data/puppetserver | /sbin/nologin |
| saslauth | N/A | saslauth | 76 | no | /run/saslauthd | /sbin/nologin |
| tomcat | 53 | tomcat | 53 | no | /usr/share/tomcat | /bin/nologin |
| unbound | N/A | unbound | N/A | yes | /etc/unbound | /sbin/nologin |
