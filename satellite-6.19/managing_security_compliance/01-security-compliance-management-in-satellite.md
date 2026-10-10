---
title: "Security compliance management in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_security_compliance"
guide_title: "Managing security compliance"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#security-compliance-management-in-satellite"
---
# Chapter 1. Security compliance management in Satellite

Security compliance management involves defining security policies, auditing hosts for compliance with those policies, and resolving instances of non-compliance. With Satellite, you can centralize compliance management by scheduling compliance auditing and reporting on your hosts.

## 1.1. Security content automation protocol

Satellite uses the Security Content Automation Protocol (SCAP) standard to define security policies.

SCAP is a framework of several specifications based on XML, such as checklists described in the Extensible Checklist Configuration Description Format (XCCDF) and vulnerabilities described in the Open Vulnerability and Assessment Language (OVAL). These specifications are encapsulated as *data stream* files.

Checklist items in XCCDF, also known as *rules*, express the desired configuration of a system item. For example, a rule may specify that no one can log in to a host over SSH by using the `root` user account. Rules can be grouped into one or more *XCCDF profiles*, which allows multiple profiles to share a rule.

The OpenSCAP scanner tool evaluates system items on a host against the rules and generates a report in the Asset Reporting Format (ARF), which is then returned to Satellite for monitoring and analysis.

Table 1.1. Specifications in the SCAP framework 1.3 supported by the OpenSCAP scanner

|  |  |  |
| --- | --- | --- |
| **Title** | **Description** | **Version** |
| SCAP | Security Content Automation Protocol | 1.3 |
| XCCDF | Extensible Configuration Checklist Description Format | 1.2 |
| OVAL | Open Vulnerability and Assessment Language | 5.11 |
| - | Asset Identification | 1.1 |
| ARF | Asset Reporting Format | 1.1 |
| CCE | Common Configuration Enumeration | 5.0 |
| CPE | Common Platform Enumeration | 2.3 |
| CVE | Common Vulnerabilities and Exposures | 2.0 |
| CVSS | Common Vulnerability Scoring System | 2.0 |

**Additional resources**

- [OpenSCAP project](https://www.open-scap.org/)

## 1.2. SCAP content in Satellite

In Satellite, you use an XCCDF profile from SCAP content and, eventually, a tailoring file, to define a *compliance policy*. Satellite includes default SCAP contents from SCAP Security Guide provided by the OpenSCAP project.

SCAP content is a SCAP data-stream file that contains implementation of compliance, configuration, or security baselines. A single data stream usually includes multiple XCCDF profiles. An XCCDF profile defines an industry standard or custom security standard against which you can evaluate compliance of host configuration in Satellite, such as Protection Profile for General Purpose Operating Systems (OSPP), Health Insurance Portability and Accountability Act (HIPAA), and PCI-DSS v3.2.1 Control Baseline for Red Hat Enterprise Linux 9. You can adapt existing XCCDF profiles according to your requirements by using *tailoring files*.

Satellite supports content of SCAP versions 1.2 and 1.3.

**Additional resources**

- [OpenSCAP project](https://www.open-scap.org/)
