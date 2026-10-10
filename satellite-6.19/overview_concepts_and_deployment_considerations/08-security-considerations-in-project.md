---
title: "Security considerations in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#security-considerations-in-project"
---
# Chapter 8. Security considerations in Satellite

Satellite supports multiple security mechanisms to provide additional layers of protection. Implementing these security features enhances the overall security of your Satellite deployment.

> **Note**
>
> These security considerations apply to both Satellite Server and Capsule Server environments.

Federal Information Processing Standards (FIPS) Mode
:   Satellite supports running on FIPS-enabled Red Hat Enterprise Linux hosts to comply with security standards for cryptographic modules. However, Satellite itself is not FIPS-certified. In addition, you cannot enable FIPS mode after the installation of Satellite.

    FIPS mode enforces the use of validated cryptographic algorithms and modules. Enabling FIPS mode ensures that all cryptographic operations within the system adhere to strict security standards.

    > **Note**
    >
    > Satellite supports DEFAULT and FIPS crypto-policies. The FUTURE crypto-policy is not supported for Satellite Server and Capsule Server installations. The FUTURE policy is a stricter forward-looking security level intended for testing a possible future policy.

File Access Policy Daemon (`fapolicyd`)
:   By enabling `fapolicyd` on your Satellite Server, you can monitor and control file and directory access, which provides an additional security layer.

    This feature helps prevent unauthorized code execution and enhances system integrity. You can enable or disable `fapolicyd` on both Satellite Server and Capsule Server at any time, depending on your security requirements.

Post-Quantum Cryptography (PQC)
:   Red Hat does not support PQC compatibility for Satellite.

Security-Enhanced Linux (SELinux)
:   Satellite requires SELinux, a mandatory access control system that restricts system access and reduces the risk of security vulnerabilities. SELinux enforces policies that define which processes can access specific system resources, providing protection against unauthorized access and exploitation.

    To maintain a high-security environment, Red Hat recommends running Satellite with SELinux in enforcing mode. It ensures that access control policies are strictly enforced, minimizing the risk of privilege escalation or unauthorized actions.

Additional Security Recommendations
:   Regularly updating security policies and configurations, as well as monitoring system logs and security policies, can help detect and respond to potential threats effectively.

Security compliance
:   For certain use cases, your Satellite Server must meet the requirements of security compliance. You can use Security Content Automation Protocol (SCAP) to scan your system for security policy compliance.

**Additional resources**

- [Switching RHEL to FIPS mode in *Red Hat Enterprise Linux 9 Security hardening*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening)
- [Using system-wide cryptographic policies in *Red Hat Enterprise Linux 9 Security hardening*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening)
- [Blocking and allowing applications by using fapolicyd in *Red Hat Enterprise Linux 9 Security hardening*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/assembly_blocking-and-allowing-applications-using-fapolicyd_security-hardening)
- [*Managing security compliance*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_security_compliance/index#)
