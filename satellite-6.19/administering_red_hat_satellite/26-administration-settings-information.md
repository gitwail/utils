---
title: "Administration settings information"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "F"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#administration-settings-information"
---
# Appendix F. Administration settings information

In the Satellite web UI, you can edit various settings to configure Satellite. You can find these settings by navigating to **Administer** > **Settings**.

## F.1. General settings information

The general settings define system-wide configuration options for Satellite, including administrator email, instance URL, user interface preferences, HTTP proxy settings, and default language and time zone.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Administrator email address** |  | The default administrator email address |
| **Satellite URL** |  | URL where your Satellite instance is reachable. See also **Provisioning** > **Unattended URL**. |
| **Entries per page** | 20 | Number of records shown per page in Satellite |
| **Fix DB cache** | No | Satellite maintains a cache of permissions and roles. When set to `Yes`, Satellite recreates this cache on the next restart. |
| **DB pending seed** | No | Should the `foreman-rake db:seed` be executed on the next run of the installer modules? |
| **Capsule request timeout** | 60 | Open and read timeout for HTTP requests from Satellite to Capsule (in seconds). |
| **Login page footer text** |  | Text to be shown in the login-page footer. |
| **HTTP(S) proxy** |  | Set a proxy for outgoing HTTP(S) connections from the Satellite product. System-wide proxies must be configured at the operating system level. |
| **HTTP(S) proxy except hosts** | [] | Set hostnames to which requests are not to be proxied. Requests to the local host are excluded by default. |
| **Show Experimental Labs** | No | Whether or not to show a menu to access experimental lab features (requires reload of page). |
| **Display FQDN for hosts** | Yes | If set to `Yes`, Satellite displays names of hosts as fully qualified domain names (FQDNs). |
| **Out of sync interval** | 30 | Hosts report periodically, and if the time between reports exceeds this duration in minutes, hosts are considered out of sync. You can override this on your hosts by adding the `outofsync_interval` parameter, per host, at **Hosts** > **All Hosts** > **$host** > **Edit** > **Parameters** > **Add Parameter**. |
| **Satellite UUID** |  | Satellite instance ID. Uniquely identifies a Satellite instance. |
| **Default language** |  | The UI for new users uses this language. |
| **Default timezone** |  | The time zone to use for new users. |
| **Instance title** |  | The instance title is shown on the top navigation bar (requires a page reload). |
| **Saved audits interval** |  | Duration in days to preserve audit data. Leave empty to disable the audits cleanup. |
| **New host details UI** | Yes | Satellite loads the new UI for host details. |
| **Red Hat documentation server URL** | <https://docs.redhat.com> | Defaults to Red Hat online documentation. Override this setting to your Red Hat Offline Knowledge Portal instance URL for offline documentation support. Supports only HTTP and HTTPS schemes. |

## F.2. Background tasks settings

The tasks settings define how Satellite manages background tasks, including timeouts, retry behavior, batch processing, and debugging options for the Dynflow console.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Sync task timeout** | 120 | Number of seconds to wait for a synchronous task to finish before an exception is raised. |
| **Enable dynflow console** | Yes | Enable the Dynflow console (`/foreman_tasks/dynflow`) for debugging. |
| **Require auth for dynflow console** | Yes | The user must be authenticated as having administrative rights before accessing the Dynflow console. |
| **Capsule action retry count** | 4 | Number of attempts permitted to start a task on the Capsule before failing. |
| **Capsule action retry interval** | 15 | Time in seconds between retries. |
| **Allow Capsule batch tasks** | Yes | Enable batch triggering of tasks on the Capsule. |
| **Capsule tasks batch size** | 100 | Number of tasks included in one request to the Capsule if `foreman_tasks_proxy_batch_trigger` is enabled. |
| **Tasks troubleshooting URL** |  | URL pointing to the task troubleshooting documentation. It should contain a `%{label}` placeholder that is replaced with a normalized task label (restricted to only alphanumeric characters)). A `%{version}` placeholder is also available. |
| **Polling intervals multiplier** | 1 | Polling multiplier used to multiply the default polling intervals. You can use this to prevent polling too frequently for long running tasks. |

## F.3. Template sync settings

The template sync settings define how Satellite synchronizes templates with Git repositories, including import and export behavior, filtering, locking, and metadata handling.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Associate** | New | Associate templates with operating system, organization, and location. |
| **Branch** |  | Default branch in Git repo. |
| **Commit message** | Templates export made by a Satellite user | Custom commit message for exported templates. |
| **Dirname** | / | The directory within the Git repo containing the templates. |
| **Filter** |  | Import or export of names matching this regex. Case-insensitive. Snippets are not filtered. |
| **Force import** | No | If set to `Yes`, locked templates are overwritten during an import. |
| **HTTP proxy policy** | Global default HTTP proxy | Whether to use an HTTP proxy to synchronize templates.    The `Custom HTTP proxy` value is available only if an HTTP proxy is configured under the selected organization and location and if your account has the **view_http_proxies** permission assigned. |
| **Lock templates** | Keep, do not lock new | How to handle lock for imported templates. |
| **Metadata export mode** | Refresh | Default metadata export mode.    Possible options:    `refresh` re-renders metadata.    `keep` keeps existing metadata.    `remove` exports the template without metadata. |
| **Negate** | No | Negate the filter for import or export. |
| **Prefix** |  | A string added as a prefix to imported templates. |
| **Repo** |  | Target path from where to import or export templates. Different protocols can be used, for example:    `/tmp/dir`    `git://example.com`    `https://example.com`    `ssh://example.com`    When exporting to `/tmp`, note that production deployments may be configured to use `private tmp`. |
| **Verbosity** | No | Choose verbosity for Rake task importing templates. |

## F.4. Host Discovery settings

The Discovery settings define how Satellite handles discovered hosts, including default organization and location assignment, hostname generation, auto-provisioning behavior, and fact organization.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Discovery location** |  | Indicates the default location to place discovered hosts in. |
| **Discovery organization** |  | Indicates the default organization to which discovered hosts are added. |
| **Interface fact** | discovery_bootif | Fact name to use for primary interface detection. |
| **Create bond interfaces** | No | Automatically create a bond interface if another interface is detected on the same VLAN using LLDP. |
| **Clean all facts** | No | Clean all reported facts (except discovery facts) during provisioning. |
| **Hostname facts** | discovery_bootif | List of facts to use for the hostname (comma separated, first wins). |
| **Auto provisioning** | No | Use the provisioning rules to automatically provision newly discovered hosts. |
| **Reboot** | Yes | Automatically reboot or kexec discovered hosts during provisioning. |
| **Hostname prefix** | mac | The default prefix to use for the hostname. Must start with a letter. |
| **Fact columns** |  | Extra facter columns to show in host lists (comma separated). |
| **Highlighted facts** |  | Regex to organize facts for highlights section – e.g. `^(abc|cde)$`. |
| **Storage facts** |  | Regex to organize facts for the storage section. |
| **Software facts** |  | Regex to organize facts for the software section. |
| **Hardware facts** |  | Regex to organize facts for the hardware section. |
| **Network facts** |  | Regex to organize facts for the network section. |
| **IPMI facts** |  | Regex to organize facts for the *Intelligent Platform Management Interface* (IPMI) section. |
| **Lock PXE** | No | Automatically generate a *Preboot Execution Environment* (PXE) configuration to pin a newly discovered host to discovery. |
| **Locked PXELinux template name** | pxelinux_discovery | PXELinux template to be used when pinning a host to discovery. |
| **Locked PXEGrub2 template name** | pxegrub2_discovery | PXEGrub2 template to be used when pinning a host to discovery. |
| **Force DNS** | Yes | Force the creation of DNS entries when provisioning a discovered host. |
| **Error on existing NIC** | No | Do not permit to discover an existing host matching the MAC of a provisioning *Network Interface Card* (NIC) (errors out early). |
| **Type of name generator** | Fact + prefix | Discovery hostname naming pattern. |
| **Prefer IPv6** | No | Prefer IPv6 to IPv4 when calling discovered nodes. |

## F.5. Boot disk settings

The boot disk settings define paths to boot loader images and templates used for generating bootable disk images, including iPXE, ISOLINUX, SYSLINUX, and Grub2 configurations.

| Setting | Default Value | Description |
| --- | --- | --- |
| **iPXE directory** | `/usr/share/ipxe` | Path to directory containing iPXE images. |
| **ISOLINUX directory** | `/usr/share/syslinux` | Path to directory containing ISOLINUX images. |
| **SYSLINUX directory** | `/usr/share/syslinux` | Path to directory containing SYSLINUX images. |
| **Grub2 directory** | `/var/lib/tftpboot/grub2` | Path to directory containing `grubx64.efi` and `shimx64.efi`. |
| **Host image template** | Boot disk iPXE - host | iPXE template to use for host-specific boot disks. |
| **Generic image template** | Boot disk iPXE - generic host | iPXE template to use for generic host boot disks. |
| **Generic Grub2 EFI image template** | Boot disk Grub2 EFI - generic host | Grub2 template to use for generic *Extensible Firmware Interface* (EFI) host boot disks. |
| **ISO generation command** | genisoimage | Command to generate ISO image, use `genisoimage` or `mkisofs`. |
| **Installation media caching** | Yes | Installation media files are cached for full host images. |
| **Allowed bootdisk types** | [generic, host, full_host, subnet] | List of permitted bootdisk types. Leave blank to disable it. |

## F.6. Red Hat Cloud settings

The Red Hat Cloud settings define how Satellite integrates with Red Hat cloud services, including automatic inventory upload, Red Hat Lightspeed recommendations synchronization, and hostname and IP address obfuscation.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Automatic inventory upload** | Yes | Enable automatic upload of your host inventory to the Red Hat cloud. |
| **Synchronize recommendations Automatically** | No | Enable automatic synchronization of Red Hat Lightspeed recommendations from the Red Hat cloud. |
| **Obfuscate host names** | No | Obfuscate hostnames sent to the Red Hat cloud. |
| **Obfuscate host ipv4 addresses** | No | Obfuscate IPv4 addresses sent to the Red Hat cloud. |
| **ID of the RHC daemon** | ***** | RHC daemon id. |

## F.7. Content management settings

The content settings define how Satellite manages content repositories, subscriptions, content views, and host registration, including default templates, download policies, and synchronization behavior.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Default HTTP Proxy** |  | Default HTTP Proxy for syncing content. |
| **Default synced OS provisioning template** | Kickstart default | Default provisioning template for operating systems created from synced content. |
| **Default synced OS finish template** | Kickstart default finish | Default finish template for new operating systems created from synced content. |
| **Default synced OS user-data** | Kickstart default user data | Default user data for new operating systems created from synced content. |
| **Default synced OS PXELinux template** | Kickstart default PXELinux | Default PXELinux template for new operating systems created from synced content. |
| **Default synced OS PXEGrub2 template** | Kickstart default PXEGrub2 | Default PXEGrub2 template for new operating systems created from synced content. |
| **Default synced OS iPXE template** | Kickstart default iPXE | Default iPXE template for new operating systems created from synced content. |
| **Default synced OS partition table** | Kickstart default | Default partitioning table for new operating systems created from synced content. |
| **Default synced OS kexec template** | Discovery Red Hat kexec | Default kexec template for new operating systems created from synced content. |
| **Default synced OS Atomic template** | Atomic Kickstart default | Default provisioning template for new atomic operating systems created from synced content. |
| **Manifest refresh timeout** | 1200 | Timeout when refreshing a manifest (in seconds). |
| **Subscription connection enabled** | Yes | Can communicate with the Red Hat Portal for subscriptions. |
| **Installable errata from Content View** | No | Calculate errata host status based only on errata in a host’s content view and lifecycle environment. |
| **Restrict Composite Content View promotion** | No | If this is enabled, a composite content view cannot be published or promoted, unless the content view versions that it includes exist in the target environment. |
| **Check services before actions** | Yes | Check the status of backend services such as pulp and candlepin before performing actions? |
| **Batch size to sync repositories in** | 100 | How many repositories should be synced concurrently on a Capsule. A smaller number may lead to longer sync times. A larger number will increase dynflow load. |
| **Sync Capsules after Content View promotion** | Yes | Whether or not to auto sync Capsules after a content view promotion. |
| **Default Custom Repository download policy** | `immediate` | Default download policy for custom repositories. Either `immediate` or `on_demand`. |
| **Default Red Hat Repository download policy** | `on_demand` | Default download policy for enabled Red Hat repositories. Either `immediate` or `on_demand`. |
| **Default Capsule download policy** | `on_demand` | Default download policy for Capsule syncs. Either `inherit`, `immediate`, or `on_demand`. |
| **Pulp 3 export destination filepath** | `/var/lib/pulp/exports` | On-disk location for Pulp 3 exported repositories. |
| **Pulp client key** | `/etc/pki/katello/private/pulp-client.key` | Path for SSL key used for Pulp server authentication. |
| **Pulp client cert** | `/etc/pki/katello/certs/pulp-client.crt` | Path for SSL certificate used for Pulp server authentication. |
| **Sync Connection Timeout** | 300 | Total timeout in seconds for connections when syncing. |
| **Delete Host upon unregister** | No | When unregistering a host using subscription-manager, also delete the host record. Managed resources linked to the host such as virtual machines and DNS records might also be deleted. |
| **Subscription manager name registration fact** |  | When registering a host using subscription-manager, force use the specified fact for the host name (in the form of `fact.fact`). |
| **Subscription manager name registration fact strict matching** | No | If this is enabled, and `register_hostname_fact` is set and provided, registration looks for a new host by name only using that fact, and skips all hostname matching. |
| **Default Location subscribed hosts** | Default Location | Default location where new subscribed hosts are stored after registration. |
| **Expire soon days** | 120 | The number of days remaining in a subscription before you are reminded about renewing it. |
| **Content View Dependency Solving Default** | No | The default dependency solving value for new content views. |
| **Host Duplicate DMI UUIDs** | [] | If hosts fail to register because of duplicate *Desktop Management Interface* (DMI) UUIDs, add their comma-separated values here. Subsequent registrations generate a unique DMI UUID for the affected hosts. |
| **Host Profile Assume** | Yes | Enable new host registrations to assume registered profiles with matching hostname if the registering DMI UUID is not used by another host. |
| **Host Profile Can Change In Build** | No | Enable host registrations to bypass **Host Profile Assume** if the host is in build mode. |
| **Host Can Re-Register Only In Build** | No | Enable hosts to re-register only when they are in build mode. |
| **Host Tasks Workers Pool Size** | 5 | Number of workers in the pool to handle the execution of host-related tasks. When set to 0, the default queue is used. Restart of the dynflowd/foreman-tasks service is required. |
| **Applicability Batch Size** | 50 | Number of host applicability calculations to process per task. |
| **Autosearch** | Yes | For pages that support it, automatically perform the search while typing in search input. |
| **Autosearch delay** | 500 | If Autosearch is enabled, delay in milliseconds before executing searches while typing. |
| **Pulp bulk load size** | 2000 | The number of items fetched from a single paged Pulp API call. |
| **Upload profiles without Dynflow** | Yes | Enable Katello to update host installed packages, enabled repositories, and module inventory directly instead of wrapped in Dynflow tasks (try turning off if Puma processes are using too much memory). |
| **Orphaned Content Protection Time** | 1440 | Time in minutes to consider orphan content as orphaned. |
| **Prefer registered through Capsule for remote execution** | No | Prefer using a proxy to which a host is registered when using remote execution. |
| **Allow deleting repositories in published content views** | Yes | Enable removal of repositories that the user has previously published in one or more content view versions. |

## F.8. User authentication settings

The authentication settings define how Satellite handles user authentication and authorization, including OAuth configuration, SSL certificates, login delegation, idle timeouts, and OpenID Connect integration.

| Setting | Default Value | Description |
| --- | --- | --- |
| **OAuth active** | Yes | Satellite will use OAuth for API authorization.    This setting is for internal Satellite use only. Red Hat does not support using it to configure OAuth authentication for API calls. |
| **OAuth consumer key** | ***** | OAuth consumer key.    This setting is for internal Satellite use only. Red Hat does not support using it to configure OAuth authentication for API calls. |
| **OAuth consumer secret** | ***** | OAuth consumer secret.    This setting is for internal Satellite use only. Red Hat does not support using it to configure OAuth authentication for API calls. |
| **OAuth map users** | No | Satellite maps users by username in the request-header. If this is disabled, OAuth requests have administrator rights.    This setting is for internal Satellite use only. Red Hat does not support using it to configure OAuth authentication for API calls. |
| **Failed login attempts limit** | 30 | Satellite blocks user logins from an incoming IP address for 5 minutes after the specified number of failed login attempts. Set to 0 to disable brute force protection. |
| **Restrict registered Capsules** | Yes | Only known Capsules can access features that use Capsule authentication. |
| **Require SSL for capsules** | Yes | Client SSL certificates are used to identify Capsules (`:require_ssl` should also be enabled). |
| **Trusted hosts** | [] | List of hostnames, IPv4, IPv6 addresses or subnets to be trusted in addition to Capsules for access to fact/report importers and ENC output. |
| **SSL certificate** | `/etc/foreman/client_cert.pem` | SSL Certificate path that Satellite uses to communicate with its proxies. |
| **SSL CA file** | `/etc/foreman/proxy_ca.pem` | SSL CA file path that Satellite uses to communicate with its proxies. |
| **SSL private key** | `/etc/foreman/client_key.pem` | SSL Private Key path that Satellite uses to communicate with its proxies. |
| **SSL client DN env** | HTTP_SSL_CLIENT_S_DN | Environment variable containing the subject DN from a client SSL certificate. |
| **SSL client verify env** | HTTP_SSL_CLIENT_VERIFY | Environment variable containing the verification status of a client SSL certificate. |
| **SSL client cert env** | HTTP_SSL_CLIENT_CERT | Environment variable containing a client’s SSL certificate. |
| **Server CA file** |  | SSL CA file path used in templates to verify the connection to Satellite. |
| **Websockets SSL key** | `etc/pki/katello/private/katello-apache.key` | Private key file path that Satellite uses to encrypt websockets. |
| **Websockets SSL certificate** | `/etc/pki/katello/certs/katello-apache.crt` | Certificate path that Satellite uses to encrypt websockets. |
| **Websockets encryption** | Yes | VNC/SPICE websocket proxy console access encryption (`websockets_ssl_key/cert` setting required). |
| **Login delegation logout URL** |  | Redirect your users to this URL on logout. Enable **Authorize login delegation** also. |
| **Authorize login delegation auth source user autocreate** | External | Name of the external authentication source where unknown externally authenticated users (see **Authorize login delegation**) are created. Empty means no autocreation. |
| **Authorize login delegation** | No | Authorize login delegation with `REMOTE_USER HTTP` header. |
| **Authorize login delegation API** | No | Authorize login delegation with `REMOTE_USER HTTP` header for API calls too. |
| **Idle timeout** | 60 | Log out idle users after the specified number of minutes. |
| **BCrypt password cost** | 9 | Cost value of bcrypt password hash function for internal auth-sources (4 – 30). A higher value is safer but verification is slower, particularly for stateless API calls and UI logins. A password change is needed to affect existing passwords. |
| **BMC credentials access** | Yes | Permits access to BMC interface passwords through ENC YAML output and in templates. |
| **OIDC JWKs URL** |  | OpenID Connect *JSON Web Key Set* (JWKS) URL. Typically `https://keycloak.example.com/auth/realms/<realm name>/protocol/openid-connect/certs` when using Keycloak as an OpenID provider. |
| **OIDC Audience** | [] | Name of the OpenID Connect Audience that is being used for authentication. In the case of Keycloak this is the Client ID. |
| **OIDC Issuer** |  | The issuer claim identifies the principal that issued the *JSON Web tokens* (JWT), which exists at a `/.well-known/openid-configuration` in case of most of the OpenID providers. |
| **OIDC Algorithm** |  | The algorithm used to encode the JWT in the OpenID provider. |

## F.9. Email notification settings

The email settings define how Satellite sends email notifications, including delivery method, SMTP configuration, reply addresses, and welcome email options.

> **Important**
>
> The `sendmail` command is a deprecated feature. Deprecated functionality is still included in Satellite and continues to be supported. However, it will be removed in a future release of this product and is not recommended for new deployments.
>
> Use an SMTP service instead.
>
> For the most recent list of major functionality that has been deprecated or removed within Satellite, refer to the *Deprecated features* section of the Satellite release notes.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Email reply address** |  | Email reply address for emails that Satellite is sending. |
| **Email subject prefix** |  | Prefix to add to all outgoing email. |
| **Send welcome email** | No | Send a welcome email including username and URL to new users. |
| **Delivery method** | Sendmail | Method used to deliver email. |
| **SMTP enable StartTLS auto** | Yes | SMTP automatically enables StartTLS. |
| **SMTP OpenSSL verify mode** | Default verification mode | When using TLS, you can set how OpenSSL checks the certificate. |
| **SMTP address** |  | SMTP address to connect to. |
| **SMTP port** | 25 | SMTP port to connect to. |
| **SMTP HELO/EHLO domain** |  | HELO/EHLO domain. |
| **SMTP username** |  | Username to use to authenticate, if required. |
| **SMTP password** | ***** | Password to use to authenticate, if required. |
| **SMTP authentication** | none | Specify authentication type, if required. |
| **Sendmail arguments** | -i | Specify additional options to sendmail. Only used when the delivery method is set to sendmail. |
| **Sendmail location** | `/usr/sbin/sendmail` | The location of the sendmail executable. Only used when the delivery method is set to sendmail. |

## F.10. RSS notifications settings

The notifications settings define how Satellite retrieves and displays RSS notifications from external feeds.

| Setting | Default Value | Description |
| --- | --- | --- |
| **RSS enable** | Yes | Pull RSS notifications. |
| **RSS URL** | <https://www.redhat.com/en/rss/blog/channel/red-hat-satellite> | URL from which to fetch RSS notifications. |

## F.11. Host provisioning settings

The provisioning settings define how Satellite provisions hosts, including default passwords, template rendering, PXE boot configuration, hostname generation, and virtual machine management.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Host owner** |  | Default owner on provisioned hosts, if empty Satellite uses the current user. |
| **Root password** | ***** | Default encrypted root password on provisioned hosts. |
| **Unattended URL** |  | URL that hosts retrieve templates from during the build. When it starts with https, unattended, or userdata, controllers cannot be accessed using HTTP. |
| **Safemode rendering** | `Yes` | Enables safe mode rendering of provisioning templates. The default and recommended option `Yes` denies access to variables and any object that is not listed in Satellite.    When set to `No`, any object may be accessed by a user with permission to use templating features, either by editing templates, parameters or smart variables. This permits users full remote code execution on Satellite Server, effectively disabling all authorization. This is not a safe option, especially in larger companies. |
| **Access unattended without build** | No | Enable access to unattended URLs without build mode being used. |
| **Query local nameservers** | No | Satellite queries the locally configured resolver instead of the SOA/NS authorities. |
| **Installation token lifetime** | 360 | Time in minutes that installation tokens should be valid for. Set to 0 to disable the token. |
| **SSH timeout** | 120 | Time in seconds before SSH provisioning times out. |
| **Libvirt default console address** | 0.0.0.0 | The IP address that should be used for the console listen address when provisioning new virtual machines using libvirt. |
| **Update IP from built request** | No | Satellite updates the host IP with the IP that made the build request. |
| **Use short name for VMs** | No | Satellite uses the short hostname instead of the FQDN for creating new virtual machines. |
| **DNS timeout** | [5, 10, 15, 20] | List of timeouts (in seconds) for DNS lookup attempts such as the `dns_lookup` macro and DNS record conflict validation. |
| **Clean up failed deployment** | Yes | Satellite deletes the virtual machine if the provisioning script ends with a non-zero exit code. |
| **Type of name generator** | `Random-based` | Specifies the method used to generate a hostname when creating a new host.    The default `Random-based` option generates a unique random hostname which you can but do not have to use. This is useful for users who create many hosts and do not know how to name them.    The `MAC-based` option is for bare-metal hosts only. If you delete a host and create it later on, it receives the same hostname based on the MAC address. This can be useful for users who recycle servers and want them to always get the same hostname.    The `Off` option disables the name generator function and leaves the hostname field blank. |
| **Default PXE global template entry** |  | Default PXE menu item in a global template – `local`, `discovery` or custom, use blank for template default. |
| **Default PXE local template entry** |  | Default PXE menu item in local template – `local`, `local_chain_hd0`, or custom, use blank for template default. |
| **iPXE intermediate script** | iPXE intermediate script | Intermediate iPXE script for unattended installations. |
| **Destroy associated VM on host delete** | No | Destroy associated VM on host delete. When enabled, VMs linked to hosts are deleted on Compute Resource. When disabled, VMs are unlinked when the host is deleted, meaning they remain on Compute Resource and can be re-associated or imported back to Satellite again. This does not automatically power off the VM |
| **Maximum structured facts** | 100 | Maximum number of keys in structured subtree, statistics stored in `satellite::dropped_subtree_facts`. |
| **Default Global registration template** | Global Registration | Global Registration template. |
| **Default 'Host initial configuration' template** | Linux host_init_config default | Default 'Host initial configuration' template, automatically assigned when a new operating system is created. |
| **Global default PXEGrub2 template** | PXEGrub2 global default | Global default PXEGrub2 template. This template is deployed to all configured TFTP servers. It is not affected by upgrades. |
| **Global default PXELinux template** | PXELinux global default | Global default PXELinux template. This template is deployed to all configured TFTP servers. It is not affected by upgrades. |
| **Global default iPXE template** | iPXE global default | Global default iPXE template. This template is deployed to all configured TFTP servers. It is not affected by upgrades. |
| **Local boot PXEGrub2 template** | PXEGrub2 default local boot | Template that is selected as PXEGrub2 default for local boot. |
| **Local boot PXELinux template** | PXELinux default local boot | Template that is selected as PXELinux default for local boot. |
| **Local boot iPXE template** | iPXE default local boot | Template that is selected as iPXE default for local boot. |
| **Manage PuppetCA** | Yes | Satellite automates certificate signing upon provision of a new host. |
| **Use UUID for certificates** | No | Satellite uses random UUIDs for certificate signing instead of hostnames. |
| **Show unsupported provisioning templates** | No | Show unsupported provisioning templates. When enabled, all the available templates are shown. When disabled, only Red Hat supported templates are shown. |

## F.12. Host facts settings

The facts settings define how Satellite processes and uses facts reported by hosts, including automatic host creation, location and organization assignment, interface updates, and fact filtering.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Create new host when facts are uploaded** | Yes | Satellite creates the host when new facts are received. |
| **Location fact** | satellite_location | Hosts created after a Puppet run are placed in the location specified by this fact. |
| **Organization fact** | satellite_organization | Hosts created after a Puppet run are placed in the organization specified by this fact. The content of this fact should be the full label of the organization. |
| **Default location** | Default Location | Hosts created after a Puppet run that did not send a location fact are placed in this location. |
| **Default organization** | Default Organization | Hosts created after a Puppet run that did not send an organization fact are placed in this organization. |
| **Update hostgroup from facts** | Yes | Satellite updates a host’s hostgroup from its facts. |
| **Ignore facts for operating system** | No | Stop updating operating system from facts. |
| **Ignore facts for domain** | No | Stop updating domain values from facts. |
| **Update subnets from facts** | None | Satellite updates a host’s subnet from its facts. |
| **Ignore interfaces facts for provisioning** | No | Stop updating IP and MAC address values from facts (affects all interfaces). |
| **Ignore interfaces with matching identifier** | [`lo`, `en*v*`, `usb*`, `vnet*`, `macvtap*`, `;vdsmdummy;`, `veth*`, `tap*`, `qbr*`, `qvb*`, `qvo*`, `qr-*`, `qg-*`, `vlinuxbr*`, `vovsbr*`, `br-int`] | Skip creating or updating host network interfaces objects with identifiers matching these values from incoming facts. You can use a * wildcard to match identifiers with indexes, e.g. `macvtap*`. The ignored interface raw facts are still stored in the database, see the **Exclude pattern** setting for more details. |
| **Exclude pattern for facts stored in Satellite** | [`lo`, `en*v*`, `usb*`, `vnet*`, `macvtap*`, `;vdsmdummy;`, `veth*`, `tap*`, `qbr*`, `qvb*`, `qvo*`, `qr-*`, `qg-*`, `vlinuxbr*`, `vovsbr*`, `br-int`, `load_averages::*`, `memory::swap::available*`, `memory::swap::capacity`, `memory::swap::used*`, `memory::system::available*`, `memory::system::capacity`, `memory::system::used*`, `memoryfree`, `memoryfree_mb`, `swapfree`, `swapfree_mb`, `uptime_hours`, `uptime_days`] | Exclude pattern for all types of imported facts (Puppet, Ansible, rhsm). Those facts are not stored in the satellite database. You can use a * wildcard to match names with indexes, e.g. `ignore*` filters out ignore, ignore123 as well as a::ignore or even a::ignore123::b. |

## F.13. Configuration management settings

The configuration management settings define how Satellite integrates with configuration management tools, including automatic host creation from reports, smart class parameter evaluation, and configuration status tracking.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Create new host when report is uploaded** | Yes | Satellite creates the host when a report is received. |
| **Matchers inheritance** | Yes | Satellite matchers are inherited by children when evaluating smart class parameters for hostgroups, organizations, and locations. |
| **Default parameters lookup path** | [`fqdn`, `hostgroup`, `os`, `domain`] | Satellite evaluates host smart class parameters in this order by default. |
| **Interpolate ERB in parameters** | Yes | Satellite parses ERB in parameters value in the ENC output. |
| **Always show configuration status** | No | All hosts show a configuration status even when a Puppet Capsule is not assigned. |

## F.14. Remote execution settings

The remote execution settings define how Satellite executes commands and scripts on remote hosts, including SSH configuration, user management, Capsule selection, and job template synchronization.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Fallback to Any Capsule** | No | Search the host for any proxy with Remote Execution. This is useful when the host has no subnet or the subnet does not have an execution proxy. |
| **Enable Global Capsule** | Yes | Search for Remote Execution proxy outside of the proxies assigned to the host. The search is limited to the host’s organization and location. |
| **SSH User** | root | Default user to use for SSH. You can override per host by setting the `remote_execution_ssh_user` parameter. |
| **Effective User** | root | Default user to use for executing the script. If the user differs from the SSH user, su or sudo is used to switch the user. |
| **Effective User Method** | sudo | The command used to switch to the effective user. One of [`sudo`, `dzdo`, `su`] |
| **Effective user password** | ***** | Effective user password. See **Effective User**. |
| **Sync Job Templates** | Yes | Whether to sync templates from disk when running `db:seed`. |
| **SSH Port** | 22 | Port to use for SSH communication. Default port 22. You can override per host by setting the `remote_execution_ssh_port` parameter. |
| **Connect by IP** | No | Whether the IP addresses on host interfaces are preferred over the FQDN. It is useful when the DNS is not resolving the FQDNs properly. You can override this per host by setting the `remote_execution_connect_by_ip` parameter. For dual-stacked hosts, consider the `remote_execution_connect_by_ip_prefer_ipv6` setting. |
| **Prefer IPv6 over IPv4** | No | When connecting using an IP address, are IPv6 addresses preferred? If no IPv6 address is set, it falls back to IPv4 automatically. You can override this per host by setting the `remote_execution_connect_by_ip_prefer_ipv6` parameter. By default and for compatibility, IPv4 is preferred over IPv6. |
| **Default SSH password** | ***** | Default password to use for SSH. You can override per host by setting the `remote_execution_ssh_password` parameter. |
| **Default SSH key passphrase** | ***** | Default key passphrase to use for SSH. You can override per host by setting the `remote_execution_ssh_key_passphrase` parameter. |
| **Workers pool size** | 5 | Number of workers in the pool to handle the execution of the remote execution jobs. Restart of the `dynflowd/satellite-tasks` service is required. |
| **Cleanup working directories** | Yes | Whether working directories are removed after task completion. You can override this per host by setting the `remote_execution_cleanup_working_dirs` parameter. |
| **Cockpit URL** |  | Where to find the Cockpit instance for the Web Console button. By default, no button is shown. |
| **Form Job Template** | Run Command - Script Default | Choose a job template that is pre-selected in job invocation form. |
| **Job Invocation Report Template** | Jobs - Invocation report template | Select a report template used for generating a report for a particular remote execution job. |
| **Time to pickup** | 86400 | Time in seconds within which the host has to pick up a job. If the job is not picked up within this limit, the job will be canceled. Applies only to pull-mqtt based jobs. Defaults to one day. |

## F.15. Ansible integration settings

The Ansible settings define how Satellite integrates with Ansible for configuration management, including connection types, verbosity levels, timeout values, and role import behavior.

| Setting | Default Value | Description |
| --- | --- | --- |
| **Private Key Path** |  | Use this to supply a path to an SSH Private Key that Ansible uses instead of a password. Override with the `ansible_ssh_private_key_file` host parameter. |
| **Connection type** | ssh | Use this connection type by default when running Ansible Playbooks. You can override this on hosts by adding the `ansible_connection` parameter. |
| **WinRM cert Validation** | validate | Enable or disable WinRM server certificate validation when running Ansible Playbooks. You can override this on hosts by adding the `ansible_winrm_server_cert_validation` parameter. |
| **Default verbosity level** | Disabled | Satellite adds this level of verbosity for additional debugging output when running Ansible Playbooks. |
| **Post-provision timeout** | 360 | Timeout (in seconds) to set when Satellite triggers an Ansible roles task playbook after a host is fully provisioned. Set this to the maximum time you expect a host to take until it is ready after a reboot. |
| **Ansible report timeout** | 30 | Timeout (in minutes) when hosts should have reported. |
| **Ansible out of sync disabled** | No | Disable host configuration status turning to out of sync for Ansible after a report does not arrive within the configured interval. |
| **Default Ansible inventory report template** | Ansible - Ansible Inventory | Satellite uses this template to schedule the report with Ansible inventory. |
| **Ansible roles to ignore** | [] | The roles to exclude when importing roles from Capsule. The expected input is comma separated values and you can use * wildcard metacharacters. For example: `foo*`, `*b*`, `*bar`. |
| **Capsule tasks batch size for Ansible** |  | Number of tasks which should be sent to the Capsule in one request if `satellite_tasks_proxy_batch_trigger` is enabled. If set, it overrides `satellite_tasks_proxy_batch_size` setting for Ansible jobs. |
