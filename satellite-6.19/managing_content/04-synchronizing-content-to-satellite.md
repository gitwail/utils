---
title: "Synchronizing content to Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#synchronizing-content-to-satellite"
---
# Chapter 4. Synchronizing content to Satellite

Synchronize added repositories to download content into Satellite, then keep it current with ad hoc runs or recurring sync plans. Configure network access and HTTP proxies for restricted environments, and use advanced synchronization to troubleshoot issues.

## 4.1. Configuring network for content synchronization

Content synchronization requires outbound access to upstream URLs. Adjust SELinux, HTTP proxies, and per-product or per-repository HTTP proxy policies if your environment restricts or inspects that traffic.

### 4.1.1. Configuring SELinux to permit content synchronization on custom ports

Add a TCP port to the SELinux `http_port_t` type when upstream content servers use a port that Satellite cannot reach by default for synchronization.

By default, connecting to web servers running on the following ports is permitted: 80, 81, 443, 488, 8008, 8009, 8443, and 9000.

**Procedure**

1. On Satellite Server, verify the ports that are permitted by SELinux for content synchronization:

   ```
   # semanage port -l | grep ^http_port_t
   http_port_t     tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
   ```
2. Configure SELinux to permit a custom port for content synchronization, for example 10011:

   ```
   # semanage port -a -t http_port_t -p tcp 10011
   ```

### 4.1.2. Adding an HTTP proxy by using Satellite web UI

You can add HTTP proxies to Satellite. You can then specify which HTTP proxy to use for products, repositories, and supported compute resources.

**Prerequisites**

- Your HTTP proxy must allow access to the following hosts:

  | Host name | Port | Protocol |
  | --- | --- | --- |
  | subscription.rhsm.redhat.com | 443 | HTTPS |
  | cdn.redhat.com | 443 | HTTPS |
  | cert.console.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | api.access.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | cert-api.access.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | console.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | connect.cloud.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | *.akamaiedge.net (if using Red Hat Lightspeed in Satellite) | 443 | HTTPS |
- If Satellite Server uses an HTTP proxy to communicate with `subscription.rhsm.redhat.com` and `cdn.redhat.com`, then your HTTP proxy must not perform SSL inspection on these communications.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **HTTP Proxies**.
2. Select **New HTTP Proxy**.
3. In the **Name** field, enter a name for the HTTP proxy.
4. In the **URL** field, enter the URL for the HTTP proxy, including the port number.
5. If your HTTP proxy requires authentication, enter a **Username** and **Password**.
6. In the **Cacert** field, enter the SSL CA certificate if your HTTP proxy requires authentication.
7. Optional: In the **Test URL** field, enter a URL, then click **Test Connection** to ensure that Satellite Server can connect to the URL through your HTTP proxy.
8. Optional: Select the **Default content HTTP proxy** option to set your HTTP proxy as default to synchronize content.
9. Click the **Locations** tab and add a location.
10. Click the **Organization** tab and add an organization.
11. Click **Submit**.

**Additional resources**

- [How to access Red Hat Subscription Manager (RHSM) through a firewall or proxy](https://access.redhat.com/solutions/65300)

### 4.1.3. Adding an HTTP proxy by using Hammer CLI

You can add HTTP proxies to Satellite. You can then specify which HTTP proxy to use for products, repositories, and supported compute resources.

**Prerequisites**

- Your HTTP proxy must allow access to the following hosts:

  | Host name | Port | Protocol |
  | --- | --- | --- |
  | subscription.rhsm.redhat.com | 443 | HTTPS |
  | cdn.redhat.com | 443 | HTTPS |
  | cert.console.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | api.access.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | cert-api.access.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | console.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | connect.cloud.redhat.com (if using Red Hat Lightspeed) | 443 | HTTPS |
  | *.akamaiedge.net (if using Red Hat Lightspeed in Satellite) | 443 | HTTPS |
- If Satellite Server uses an HTTP proxy to communicate with `subscription.rhsm.redhat.com` and `cdn.redhat.com`, then your HTTP proxy must not perform SSL inspection on these communications.

**Procedure**

- Add your HTTP proxy to Satellite:

  ```
  $ hammer http-proxy create \
  --name My_HTTP_Proxy \
  --url http-proxy.example.com:8080
  ```

  Optional: To set the HTTP proxy as default for content synchronization, add the `--content-default-http-proxy true` option.

  If your HTTP proxy requires authentication, add the `--username My_User_Name` and `--password My_Password` options.

**Additional resources**

- [How to access Red Hat Subscription Manager (RHSM) through a firewall or proxy](https://access.redhat.com/solutions/65300)

### 4.1.4. Changing the HTTP proxy policy for a product

For granular control over network traffic, you can set an HTTP proxy policy for each product. An HTTP proxy policy of a product applies to all repositories in the product, unless you set a different policy for individual repositories.

To set an HTTP proxy policy for individual repositories, see [Section 4.1.5, “Changing the HTTP proxy policy for a repository by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#changing-the-http-proxy-policy-for-a-repository-by-using-web-ui "4.1.5. Changing the HTTP proxy policy for a repository by using Satellite web UI").

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products** and select the products that you want to change.
2. From the **Select Action** list, select **Manage HTTP Proxy**.
3. Select an **HTTP Proxy Policy** from the list:

   - **Global Default**: Use the global default proxy setting.
   - **No HTTP Proxy**: Do not use an HTTP proxy, even if a global default proxy is configured.
   - **Use specific HTTP Proxy**: Select an **HTTP Proxy** from the list. You must add HTTP proxies to Satellite before you can select a proxy from this list. For more information, see [Section 4.1.2, “Adding an HTTP proxy by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-an-http-proxy-by-using-web-ui "4.1.2. Adding an HTTP proxy by using Satellite web UI").
4. Click **Update**.

### 4.1.5. Changing the HTTP proxy policy for a repository by using Satellite web UI

You can set an HTTP proxy policy to synchronize repositories to Satellite Server. Use an HTTP proxy for repository synchronization if your network restricts access to the internet.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products** and click the name of the product that contains the repository.
2. In the **Repositories** tab, click the name of the repository.
3. Locate the **HTTP Proxy** field and click the edit icon.
4. Select an **HTTP Proxy Policy** from the list:

   - **Global Default**: Use the global default HTTP proxy setting.
   - **No HTTP Proxy**: Do not use an HTTP proxy, even if a global default HTTP proxy is configured.
   - **Use specific HTTP Proxy**: Select an **HTTP Proxy** from the list. You must add HTTP proxies to Satellite before you can select a proxy from this list.
5. Click **Save**.

**Additional resources**

- [Section 4.1.2, “Adding an HTTP proxy by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-an-http-proxy-by-using-web-ui "4.1.2. Adding an HTTP proxy by using Satellite web UI")
- [Section 4.1.4, “Changing the HTTP proxy policy for a product”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#changing-the-http-proxy-policy-for-a-product "4.1.4. Changing the HTTP proxy policy for a product")

### 4.1.6. Changing the HTTP proxy policy for a repository by using Hammer CLI

You can set an HTTP proxy policy to synchronize repositories to Satellite Server. Use an HTTP proxy for repository synchronization if your network restricts access to the internet.

**Procedure**

- Specify the HTTP proxy policy you want to use:

  ```
  $ hammer repository update \
  --http-proxy-policy My_HTTP_Proxy_Policy \
  --id My_Repository_ID
  ```

  Specify one of the following options for `--http-proxy-policy`:

  - `none`: Do not use an HTTP proxy, even if a global default HTTP proxy is configured.
  - `global_default_http_proxy`: Use the global default HTTP proxy setting.
  - `use_selected_http_proxy`: Specify an HTTP proxy using either `--http-proxy My_HTTP_Proxy_Name` or `--http-proxy-id My_HTTP_Proxy_ID`.

**Additional resources**

- [Section 4.1.3, “Adding an HTTP proxy by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-an-http-proxy-by-using-cli "4.1.3. Adding an HTTP proxy by using Hammer CLI")
- [Section 4.1.4, “Changing the HTTP proxy policy for a product”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#changing-the-http-proxy-policy-for-a-product "4.1.4. Changing the HTTP proxy policy for a product")

## 4.2. Synchronizing repositories ad hoc

You must synchronize repositories to download content into Satellite. Use ad hoc synchronization for the initial download or whenever you need to update repositories manually.

The synchronization duration depends on the size of each repository and the speed of your network connection. The following table provides estimates of how long it would take to synchronize content, depending on the available internet bandwidth:

Table 4.1. Estimated duration for first-time synchronization

|  | Single Package (10Mb) | Minor Release (750Mb) | Major Release (6Gb) |
| --- | --- | --- | --- |
| 256 Kbps | 5 Mins 27 Secs | 6 Hrs 49 Mins 36 Secs | 2 Days 7 Hrs 55 Mins |
| 512 Kbps | 2 Mins 43.84 Secs | 3 Hrs 24 Mins 48 Secs | 1 Day 3 Hrs 57 Mins |
| T1 (1.5 Mbps) | 54.33 Secs | 1 Hr 7 Mins 54.78 Secs | 9 Hrs 16 Mins 20.57 Secs |
| 10 Mbps | 8.39 Secs | 10 Mins 29.15 Secs | 1 Hr 25 Mins 53.96 Secs |
| 100 Mbps | 0.84 Secs | 1 Min 2.91 Secs | 8 Mins 35.4 Secs |
| 1000 Mbps | 0.08 Secs | 6.29 Secs | 51.54 Secs |

Schedule product synchronization by creating a sync plan to ensure updates on a regular basis.

**Additional resources**

- [Section 4.5, “Advanced synchronization options”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#advanced-synchronization-options "4.5. Advanced synchronization options")
- [Section 4.3, “Scheduling product synchronization”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#scheduling-product-synchronization "4.3. Scheduling product synchronization")

### 4.2.1. Synchronizing repositories by using Satellite web UI

Run an ad hoc synchronization for selected repositories to download the latest upstream content into Satellite.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select the product that contains the repositories that you want to synchronize.
3. Select the repositories that you want to synchronize and click **Sync Now**.

**Verification**

1. In the Satellite web UI, navigate to **Content** > **Sync Status**.
2. Expand the corresponding product or repository tree.
3. Verify that the synchronization is complete.

### 4.2.2. Synchronizing repositories by using Hammer CLI

Run an ad hoc synchronization for a product or individual repository to download the latest upstream content into Satellite.

**Procedure**

- Synchronize an entire product:

  ```
  $ hammer product synchronize \
  --name "My_Product" \
  --organization "My_Organization"
  ```
- Synchronize an individual repository:

  ```
  $ hammer repository synchronize \
  --name "My_Repository" \
  --organization "My_Organization" \
  --product "My_Product"
  ```

### 4.2.3. Synchronizing all repositories in an organization

Run an asynchronous Hammer CLI script to synchronize every repository in an organization when you need to refresh all content at once.

**Procedure**

1. Log in to your Satellite Server using SSH.
2. Run the following Bash script:

   ```shell-session
   ORG="My_Organization"

   for i in $(hammer --no-headers --csv repository list --organization $ORG --fields Id)
   do
     hammer repository synchronize --id ${i} --organization $ORG --async
   done
   ```

## 4.3. Scheduling product synchronization

Sync plans run repository synchronization on a schedule. Assign a sync plan to one or more products so updates are fetched automatically.

### 4.3.1. Best practices for sync plans

Apply sync plan scheduling and automation patterns that keep content current without overloading Satellite during large synchronizations.

- Add sync plans to products and regularly synchronize content to keep the load on Satellite low during synchronization. Synchronize content rather more often than less often. For example, setup a sync plan to synchronize content every day rather than only once a month.
- Automate the creation and update of sync plans by using a Hammer script or an [Ansible Playbook](https://theforeman.github.io/foreman-ansible-modules/develop/index.html).
- Distribute synchronization tasks over several hours to reduce the task load by creating multiple sync plans with the **Custom Cron** option.

**Example 4.1. Custom Cron expressions**

| Cron expression | Explanation |
| --- | --- |
| `0 22 * * 1-5` | every day at 22:00 from Monday to Friday |
| `30 3 * * 6,0` | at 03:30 every Saturday and Sunday |
| `30 2 8-14 * *` | at 02:30 every day between the 8th and the 14th days of the month |

### 4.3.2. Creating a sync plan by using Satellite web UI

A sync plan checks and updates the content at a scheduled date and time. In Satellite, you can create a sync plan and assign products to the plan.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Sync Plans**.
2. Click **New Sync Plan**.
3. In the **Name** field, enter a name for the plan.
4. Optional: In the **Description** field, enter a description of the plan.
5. From the **Interval** list, select the interval at which you want the plan to run.
6. From the **Start Date** and **Start Time** lists, select when to start running the sync plan.
7. Click **Save**.

### 4.3.3. Creating a sync plan by using Hammer CLI

A sync plan checks and updates the content at a scheduled date and time. In Satellite, you can create a sync plan and assign products to the plan.

**Procedure**

- Create a sync plan:

  ```
  $ hammer sync-plan create \
  --description "My_Description" \
  --enabled true \
  --interval daily \
  --name "My_Products" \
  --organization "My_Organization" \
  --sync-date "2023-01-01 01:00:00"
  ```

**Verification**

- View the available sync plans for an organization to verify that the sync plan has been created:

  ```
  $ hammer sync-plan list --organization "My_Organization"
  ```

### 4.3.4. Assigning a sync plan to a product by using Satellite web UI

A sync plan checks and updates the content at a scheduled date and time. In Satellite, you can assign a sync plan to products to update content regularly.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Select a product.
3. On the **Details** tab, select a **Sync Plan** from the drop down menu.

### 4.3.5. Assigning a sync plan to a product by using Hammer CLI

A sync plan checks and updates the content at a scheduled date and time. In Satellite, you can assign a sync plan to products to update content regularly.

**Procedure**

- Assign a sync plan to a product:

  ```
  $ hammer product set-sync-plan \
  --name "My_Product_Name" \
  --organization "My_Organization" \
  --sync-plan "My_Sync_Plan_Name"
  ```

### 4.3.6. Assigning a sync plan to multiple products

Assign one sync plan to every product in an organization that has been synchronized at least once and has repositories by using a Hammer script.

**Procedure**

1. Run the following Bash script:

   ```shell-session
   ORG="My_Organization"
   SYNC_PLAN="daily_sync_at_3_a.m"

   hammer sync-plan create --name $SYNC_PLAN --interval daily --sync-date "2023-04-5 03:00:00" --enabled true --organization $ORG
   for i in $(hammer --no-headers --csv --csv-separator="|" product list --organization $ORG --per-page 999 | grep -vi not_synced | awk -F'|' '$5 != "0" { print $1}')
   do
     hammer product set-sync-plan --sync-plan $SYNC_PLAN --organization $ORG --id $i
   done
   ```
2. After executing the script, view the products assigned to the sync plan:

   ```
   $ hammer product list --organization $ORG --sync-plan $SYNC_PLAN
   ```

## 4.4. Refreshing content counts on Capsule

Refresh content counts on your Capsule that mirrors content so you can verify which content views and repositories are available to hosts.

**Procedure**

1. In the Satellite web UI, navigate to **Infrastructure** > **Capsules**, and select the Capsule where you want to see the synchronized content.
2. Select the **Overview** tab.
3. Under **Content Sync**, toggle the **Synchronize** button to do an **Optimized Sync** or a **Complete Sync** to synchronize the Capsule which refreshes the content counts.
4. Select the **Content** tab.
5. Choose an **Environment** to view content views available to those Capsules by clicking **>**.
6. Expand the content view by clicking **>** to view repositories available to the content view and the specific version for the environment.
7. View the number of content counts under **Packages** specific to yum repositories.
8. View the number of errata, package groups, files, container tags, container manifests, and Ansible collections under **Additional content**.
9. Click the options icon in the column to the right next to the environment and click **Refresh counts** to refresh the content counts synchronized on the Capsule under **Packages**.

## 4.5. Advanced synchronization options

Use advanced synchronization when standard synchronization leaves packages missing or corrupted on Satellite Server.

Advanced synchronization has the following options:

Optimized Sync
:   Synchronizes the repository bypassing packages that have no detected differences from the upstream packages.

Complete Sync
:   Synchronizes all packages regardless of detected changes. Use this option if specific packages could not be downloaded to the local repository even though they exist in the upstream repository.

Verify Content Checksum
:   Synchronizes all packages and then verifies the checksum of all packages locally. If the checksum of an RPM differs from the upstream, it re-downloads the RPM. This option is relevant only for Yum content. Use this option if you have one of the following errors:

    - Specific packages cause a `404` error while synchronizing with `yum`.
    - `Package does not match intended download` error, which means that specific packages are corrupted.

**Additional resources**

- [Chapter 10, *Recovering corrupted content*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#recovering-corrupted-content "Chapter 10. Recovering corrupted content")
