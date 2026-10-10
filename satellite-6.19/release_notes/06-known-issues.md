---
title: "Known issues"
product: "Red Hat Satellite"
version: "6.19"
guide: "release_notes"
guide_title: "Release notes"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/release_notes/index#known-issues"
---
# Chapter 6. Known issues

The following known issues have been identified in Red Hat Satellite 6.19. Review them to anticipate potential problems and identify workarounds for your environment.

## 6.1. Web UI

All Hosts page always links to the new host details UI
:   The links on the **Hosts** > **All Hosts** page always point to the new host details UI, even if the setting **New host details UI** is set to **No**.

    To work around this problem, display the old host details UI by clicking the options menu in the upper right and selecting **Legacy UI**.

    [Jira:SAT-37128](https://redhat.atlassian.net/browse/SAT-37128)

## 6.2. Installation and upgrade

"Permission Denied" errors on Lightspeed pages in secured systems
:   Incorrect file permissions on the `/var/lib/foreman/public/assets/apps` directory in combination with a non-default umask cause Lightspeed pages to fail with 403 "Permission Denied" errors. This occurs, for example, in systems secured in accordance with CIS and STIG profiles, which use non-default umasks.

    To work around this problem, manually change the file permissions. For more information, see the Red Hat Knowledgebase solution [Several 'Permission Denied' errors on the iop-core-engine container and other files/services after installing or upgrading to Satellite 6.18 with IOP enabled when non-default umask is applied](https://access.redhat.com/solutions/7138946).

    [Jira:SAT-41246](https://redhat.atlassian.net/browse/SAT-41246)

## 6.3. Red Hat Lightspeed

Red Hat Lightspeed vulnerability CVE map download fails with proxy
:   Satellite servers configured for the Red Hat Lightspeed vulnerability service in Satellite fail to download CVE mapping files if the Satellite server uses an HTTP proxy to reach https://security.access.redhat.com. This issue is caused by the `iop-cvemap-download.service` service lacking HTTP proxy configuration.

    To work around this problem, manually set the `HTTPS_PROXY` and `NO_PROXY` environment variables for the `iop-cvemap-download` service. For more information, see [Installing Red Hat Lightspeed in Satellite on a connected Satellite Server](https://docs.redhat.com/en/documentation/red_hat_satellite/latest/html/installing_satellite_server_in_a_connected_network_environment/performing-additional-configuration-on-server_satellite#installing-red-hat-lightspeed-in-satellite-on-a-connected-satellite-server).

    [Jira:SAT-39459](https://redhat.atlassian.net/browse/SAT-39459)

Red Hat Lightspeed might fail on Satellite servers with managed DNS
:   When the `named` service is already running on a Satellite server, the `aardvark-dns` service, which is required for running containers, fails to start. This is caused by a conflict between `named` and `podman` configurations for IPv4 connections. As a consequence, Red Hat Lightspeed installations might fail on Satellite servers configured for managed DNS. To work around this problem, perform the following steps:

    1. Set managed DNS in `satellite-installer` to `unmanaged`:

       ```
       # satellite-installer --foreman-proxy-dns-managed=false
       ```
    2. Configure your Satellite server to only listen on the local IP addresses by adding the following content to the `/etc/named/options.conf` file:

       ```
       listen-on-v6 { fd00:4::25; };
       listen-on { 192.168.4.25; };
       ```
    3. Restart the `named` service.
    4. You can verify that the configuration works by checking that the DNS service is listening on port `53`:

       ```
       [root@satellite6:/root]# netstat -tulpn| grep 53
       tcp        0      0 10.130.0.1:53           0.0.0.0:*               LISTEN      2199/aardvark-dns
       tcp        0      0 192.168.122.1:53        0.0.0.0:*               LISTEN      2252/dnsmasq
       tcp        0      0 192.168.4.25:53         0.0.0.0:*               LISTEN      1016/named
       tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      1016/named
       tcp6       0      0 fd00:4::25:53           :::*                    LISTEN      1016/named
       ```

    [Jira:SAT-39941](https://redhat.atlassian.net/browse/SAT-39941)

Cannot easily select all CVEs in Red Hat Lightspeed vulnerability
:   On the **Red Hat Lightspeed vulnerability** page, you cannot easily select all CVEs.

    To work around this problem, manually click the drop-down list near the **Select** button and choose **Select page (100 items)** for each page individually.

    [Jira:SAT-42758](https://redhat.atlassian.net/browse/SAT-42758)

Red Hat Lightspeed vulnerability service in Satellite does not work on IPv6 networks
:   Red Hat Lightspeed is configured with IPv4 networking only. On IPv6 networks, running a Red Hat Lightspeed vulnerability service update fails to sync vulnerability data.

    There is no known workaround.

    [Jira:SAT-41384](https://redhat.atlassian.net/browse/SAT-41384)

## 6.4. Security and authentication

FIPS-enabled hosts running RHEL 9.3 or earlier cannot upload OpenSCAP reports
:   On hosts that run RHEL 9.3 or earlier versions with FIPS mode enabled, uploading an OpenSCAP report fails with the following error:

    ```
    Unable to load certs
    Neither PUB key nor PRIV key
    ```

    For more details, see a related [Knowledgebase solution](https://access.redhat.com/solutions/7008468). Note that the problem is fixed for hosts that run RHEL 9.4 or later versions.

    No known workaround exists.

    [Jira:SAT-28297](https://redhat.atlassian.net/browse/SAT-28297)

## 6.5. Content management

Unable to synchronize custom repositories by using only the upstream username without password
:   Attempts to synchronize a custom repository by using only the upstream username fail with errors about unauthorized access.

    Satellite web UI displays the following error message:

    ```
    An error occurred saving the repository: Validation failed: Upstream username requires upstream password to be set.
    ```

    Hammer CLI displays the following error message:

    ```
    401, message='Unauthorized', url=<upstream_url>
    ```

    No known workaround is available.

    [Jira:SAT-41022](https://redhat.atlassian.net/browse/SAT-41022)

Unable to upload more than 127 packages at once from the Satellite web UI
:   When uploading packages to a repository from the Satellite web UI, you can upload up to only 127 RPMs or other files. This known issue occurs due to a limitation with the Rack gem.

    To work around this problem, use the API bulk uploader for operations that involve a large number of files.

    [Jira:SAT-35291](https://redhat.atlassian.net/browse/SAT-35291)

Legacy empty CCVs that were previously published and promoted cannot be deleted
:   In some situations, composite content views (CCVs) that do not contain any content views cannot be deleted. This issue affects CCVs that were created before Satellite 6.18 and were previously published and promoted.

    For example, when attempting to remove the CCV with the `hammer content-view remove` command, the command displays the following error:

    ```
    Could not remove objects from content view:
      PG::NotNullViolation: ERROR:  null value in column "katello_content_view_version_id" of relation "katello_content_view_histories" violates not-null constraint
    ```

    To work around this problem, publish a new version of the empty CCV and then delete it.

    [Jira:SAT-35940](https://redhat.atlassian.net/browse/SAT-35940)

Flatpak content becomes inaccessible after upgrading to Satellite 6.19
:   Upgrading to Satellite 6.19 prevents hosts from consuming Flatpak content managed by your Satellite Server. The Flatpak registry static index endpoint located at `https://<satellite.example.com>/pulpcore_registry/index/static` returns a server error.

    This issue exists because the Pulp Core version included in Satellite 6.19 implements response caching that requires JSON-serializable responses, while the pulp-container FlatpakIndex view returns a Python set in its response data.

    No known workaround is available.

    [Jira:SAT-44554](https://redhat.atlassian.net/browse/SAT-44554)

## 6.6. Host provisioning and management

PXE/TFTP provisioning of RHEL 7 hosts on UEFI (EFI-based) firmware fails due to incompatible bootloaders
:   During provisioning, Satellite copies the bootloader from the `/boot` directory of the underlying OS to the `/tftpboot` directory. Because RHEL 9.7 and later versions provide a bootloader that is incompatible with RHEL 7 and earlier versions, the provisioning of RHEL 7 with PXE/TFTP on UEFI (EFI-based) firmware fails.

    To work around this problem, manually provide the RHEL 7 systems with an older bootloader. For more information, see the Red Hat Knowledgebase solution [Provisioning a RHEL 7 client system stuck at "Booting Kickstart default PXEGrub2" on Red Hat Satellite Capsule 6.18](https://access.redhat.com/solutions/7138202).

    [Jira:SAT-41340](https://redhat.atlassian.net/browse/SAT-41340)

Logs incorrectly show missing resources in Red Hat OpenShift Virtualization host creation
:   In deployments with the Red Hat OpenShift Virtualization compute resource, which is a Technology Preview feature, the production log shows `<Kubeclient::ResourceNotFoundError> virtualmachineinstances.kubevirt.io "host.example.com" not found` errors even though no resources are missing from the provisioning. This is caused by attempts to access a missing VirtualMachineInstance (VMI) that report a warning due to `fog-kubevirt` exception handling.

    To work around this problem, ignore these warnings. No action is needed.

    [Jira:SAT-43378](https://redhat.atlassian.net/browse/SAT-43378)

Concurrent host registration fails with a database error
:   When you register multiple hosts of the same operating system version, the hosts initially fail to register. The redundant creation of an operating system entry in the Red Hat Subscription Management (RHSM) fact parser triggers a unique constraint violation.

    To work around this problem, rerun the registration. Note that this leads to an increase in registration time due to the need for retries.

    [Jira:SAT-43299](https://redhat.atlassian.net/browse/SAT-43299)

## 6.7. Backup and restore

Restoring from backup fails due to inconsistencies in the data
:   If the backup is generated from a database with inconsistencies, the restore fails. The `satellite-maintain` tool uses the PostgreSQL `amcheck` extension to detect inconsistencies in the data before backup to prevent issues during restore.

    To work around this problem, contact [Red Hat customer support](https://access.redhat.com/support/) to fix any detected inconsistencies before proceeding with the backup. For more information, see [Restoring Red Hat Satellite 6.16+ fails complaining about db duplicates on CREATE UNIQUE INDEX](https://access.redhat.com/solutions/7127707) in the *Red Hat Knowledgebase*.

    [Jira:SAT-35461](https://redhat.atlassian.net/browse/SAT-35461)

## 6.8. IPv6

`virt-who` is not supported on IPv6-only networks
:   Satellite does not support the `virt-who` agent in an IPv6-only network.

    No known workaround exists.

    [Jira:RHEL-40069](https://redhat.atlassian.net/browse/RHEL-40069)

Additional configuration is required in IPv6-only networks when using `kinit` for IdM and AD users
:   If your Satellite Server runs in an IPv6-only network and also runs on RHEL 9.6 and earlier versions, Kerberos authentication for external users from Identity Management (IdM) and Active Directory (AD) fails. This known issue is caused by a bug in the System Security Services Daemon (SSSD) and occurs when the DNS name of the IdM or AD server can be translated to both an IPv4 and IPv6 address but the IPv4 address is not accessible, for example because it is blocked by a firewall.

    To work around this problem, configure the `lookup_family_order` option in the `[domain/<domain_name>]` in the `/etc/sssd/sssd.conf` file:

    ```
    [domain/example.com]
    lookup_family_order = ipv6_only
    ```

    [Jira:SAT-32530](https://redhat.atlassian.net/browse/SAT-32530)

Mismatch of the IPv6 address entry when using a DHCPv6 server
:   When you use a DHCPv6 server to assign an IP address dynamically and you provision a host in an IPv6 network, Satellite contains an IPv6 address that does not match the actual IPv6 address of the host. This mismatch impairs host management capabilities, such as remote execution.

    To work around this problem, perform one of the following steps:

    - Execute `subscription-manager facts --upload` on the host.
    - Wait for the next facts upload to resolve the issue. Note that the **Ignore interfaces facts for provisioning** (`ignore_puppet_facts_for_provisioning`) setting can disable updating the interfaces from facts.

    [Jira:SAT-30601](https://redhat.atlassian.net/browse/SAT-30601)

Host discovery fails in an IPv6 network
:   When you attempt to discover an unknown host in an IPv6 network, the discovery fails with `Error: 1001: Failed to open TCP connection to satellite.example.com:443`.

    No known workaround exists.

    [Jira:SAT-30796](https://redhat.atlassian.net/browse/SAT-30796)

Failure to provision hosts in PXE-less Discovery over IPv6
:   After PXE-less host discovery on an IPv6 Satellite, when the host starts provisioning, fails to resolve the DNS entry for Satellite. As a result, the host fails to fetch Kickstart and the required files.

    No known workaround exists.

    [Jira:SAT-30794](https://redhat.atlassian.net/browse/SAT-30794)
