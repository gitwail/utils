---
title: "Content access control for hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#content-access-control-for-hosts"
---
# Chapter 7. Content access control for hosts

You can cap host access to repositories and packages with content view environments, overrides, composite content views, and strict architecture or release rules that you evaluate in a deliberate order. Use activation keys at registration time and optional operating system or architecture limits on custom repositories to keep hosts on the intended content.

## 7.1. Content access strategies

You narrow which repositories and packages registered hosts consume from Satellite by combining content views, lifecycle environments, overrides, and tighter rules where needed. Evaluate those options from lifecycle environments through overrides toward the strictest architecture or release limits.

Red Hat recommends considering implementing the strategies in the order as listed here:

Content views and lifecycle environments
:   Use content views and lifecycle environments, incorporating content view filters as needed.

    For more information about content views, see [Chapter 9, *Managing content views and content view environments*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-views-and-content-view-environments "Chapter 9. Managing content views and content view environments").

    For more information about lifecycle environments, see [Chapter 8, *Managing application lifecycles*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Application_Lifecycles_content-management "Chapter 8. Managing application lifecycles").

Content overrides
:   By default, content hosted by Satellite can be either enabled or disabled. In custom products, repositories are always disabled by default, while Red Hat products can be either enabled or disabled by default depending on the specific repository. Enabling a repository gives the host access to the repository packages or other content, allowing hosts to download and install the available content.

    If a repository is disabled, the host is not able to access the repository content. A content override provides you with the option to override the default enablement value of either **Enabled** or **Disabled** for any repository. You can add content overrides to hosts or activation keys.

    For more information about adding content overrides to hosts, see [Enabling and Disabling Repositories on Hosts](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Enabling_and_Disabling_Repositories_on_Hosts_managing-hosts) in *Managing hosts*.

    For more information about adding content overrides to activation keys, see [Section 12.6, “Enabling and disabling repositories on activation key”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#enabling-and-disabling-repositories-on-activation-key_content-management "12.6. Enabling and disabling repositories on activation key").

Content view environments
:   Assign hosts to multiple content view environments to provide access to content from more than one content view. For more information about multiple content view environments, see [Section 9.8, “Managing content view environments”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#managing-content-view-environments "9.8. Managing content view environments").

Composite content views
:   You can use composite content views to combine and give hosts access to the content from multiple content views. For more information about composite content views, see [Section 9.6.2, “Creating a composite content view by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-composite-content-view-by-using-web-ui "9.6.2. Creating a composite content view by using Satellite web UI").

Architecture and operating system version restrictions
:   In custom products, you can set restrictions on the architecture and operating system versions for `yum` repositories on which the product will be available. For example, if you restrict a custom repository to **Red Hat Enterprise Linux 9**, it is only available on hosts running Red Hat Enterprise Linux 9. Architecture and operating system version restrictions hold the highest priority among all other strategies. They cannot be overridden or invalidated by content overrides, changes to content views, or changes to lifecycle environments. For this reason, Red Hat recommends considering the other strategies mentioned before that use architecture or operating system version restrictions. Red Hat repositories set architecture and operating system version restrictions automatically.

Release version
:   Certain Red Hat repositories, such as the Red Hat Enterprise Linux dot release repositories, include a **Release version** in their repository metadata. The release version is then compared with the release version specified in the **System purpose** properties of the host. Access to content may be limited or restricted based on this comparison.

**Additional resources**

- [Editing the system purpose of a host by using Satellite web UI in *Managing hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#editing-the-system-purpose-of-a-host-by-using-web-ui)

## 7.2. Conditions for content availability

A host can access a repository only when that repository is in a content view environment of the host, passes filters, is enabled, and matches any architecture or operating system version restrictions. When any requirement fails, packages stay unavailable to the host even though Satellite still publishes the repository.

A host can access a package or repository only if all of the following conditions are true:

- The repository is included in the content view environments of the host.
- The content view of the host has been published after the repository was added to it.
- The repository has not been filtered out by a content view filter.
- The repository is enabled by default or overridden to **Enabled** by using a content override.
- The repository has no architecture or operating system version restrictions or it has architecture or operating system version restrictions that match the host.
- For certain Red Hat repositories either no release version is set or the release version matches that of the host.

## 7.3. Activation keys and content access

During registration, you use activation keys to assign content view environments, attach content overrides, and set system purpose attributes so hosts inherit the repository access you intend. After registration, adjust access per host or through bulk actions instead of changing the activation keys.

You can use activation keys to perform the following actions:

- Assign hosts to content view environments.
- Add content overrides to hosts.
- Set system purpose attributes on hosts, including a release version.

Activation keys only affect hosts during registration. If a host is already registered, you can change the content access individually for each host or through host bulk actions.

**Additional resources**

- [Chapter 12, *Managing activation keys*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Activation_Keys_content-management "Chapter 12. Managing activation keys")

## 7.4. Restricting a custom repository to a specific operating system or architecture in Satellite

You restrict access to a custom repository so only matching hosts consume the repository from Satellite. For example, expose the repository only to Red Hat Enterprise Linux 9 hosts.

> **Note**
>
> Only restrict architecture and operating system version for custom products. Satellite applies these restrictions automatically for Red Hat repositories.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Click the product that contains the repository sets you want to restrict.
3. In the **Repositories** tab, click the repository you want to restrict.
4. In the **Publishing Settings** section, set the following options:

   - Set **Restrict to OS version** to restrict the operating system version.
   - Set **Restrict to architecture** to restrict the architecture.
