---
title: "Host parameter hierarchy"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "D"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#host-parameter-hierarchy"
---
# Appendix D. Host parameter hierarchy

You can access host parameters when provisioning hosts.

Hosts inherit their parameters from the following locations, in order of increasing precedence:

| Parameter Level | Set in Satellite web UI |
| --- | --- |
| Globally defined parameters | **Configure** > **Global parameters** |
| Organization-level parameters | **Administer** > **Organizations** |
| Location-level parameters | **Administer** > **Locations** |
| Domain-level parameters | **Infrastructure** > **Domains** |
| Subnet-level parameters | **Infrastructure** > **Subnets** |
| Operating system-level parameters | **Hosts** > **Provisioning Setup** > **Operating Systems** |
| Host group-level parameters | **Configure** > **Host Groups** |
| Host parameters | **Hosts** > **All Hosts** |
