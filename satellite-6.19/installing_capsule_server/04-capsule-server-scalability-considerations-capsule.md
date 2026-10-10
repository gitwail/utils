---
title: "Capsule Server scalability considerations when managing Puppet clients"
product: "Red Hat Satellite"
version: "6.19"
guide: "installing_capsule_server"
guide_title: "Installing Capsule Server"
chapter_number: "A"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_capsule_server/index#capsule-server-scalability-considerations_capsule"
---
# Appendix A. Capsule Server scalability considerations when managing Puppet clients

Capsule Server scalability when managing Puppet clients depends on the number of CPUs, the run-interval distribution, and the number of Puppet managed resources.

Capsule Server has a limitation of 100 concurrent OpenVox agents running at any single point in time. Running more than 100 concurrent OpenVox agents results in a 503 HTTP error.

For example, assuming that OpenVox agent runs are evenly distributed with less than 100 concurrent OpenVox agents running at any single point during a run-interval, a Capsule Server with 4 CPUs has a maximum of 1250 – 1600 Puppet clients with a moderate workload of 10 Puppet classes assigned to each Puppet client. Depending on the number of Puppet clients required, the Satellite installation can scale out the number of Capsule Servers to support them.

If you want to scale your Capsule Server when managing Puppet clients, the following assumptions are made:

- There are no external Puppet clients reporting directly to your Satellite Server.
- All other Puppet clients report directly to Capsule Servers.
- There is an evenly distributed run-interval of all OpenVox agents.

> **Note**
>
> Deviating from the even distribution increases the risk of overloading Satellite Server. The limit of 100 concurrent requests applies.

The following table describes the scalability limits using the recommended 4 CPUs.

Table A.1. Puppet scalability using 4 CPUs

| Puppet Managed Resources per Host | Run-Interval Distribution |
| --- | --- |
| 1 | 3000 – 2500 |
| 10 | 2400 – 2000 |
| 20 | 1700 – 1400 |

The following table describes the scalability limits using the minimum 2 CPUs.

Table A.2. Puppet scalability using 2 CPUs

| Puppet Managed Resources per Host | Run-Interval Distribution |
| --- | --- |
| 1 | 1700 – 1450 |
| 10 | 1500 – 1250 |
| 20 | 850 – 700 |
