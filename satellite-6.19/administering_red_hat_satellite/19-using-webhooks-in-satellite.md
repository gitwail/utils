---
title: "Using webhooks in Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "19"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#using-webhooks-in-satellite"
---
# Chapter 19. Using webhooks in Satellite

A webhook is a way for a web page or web application to provide other applications with information in real time. You can use webhooks to define a call to an external API based on Satellite internal event by using a fire-and-forget message exchange pattern.

## 19.1. Webhook behavior and integration

You can use webhooks as a way to integrate Satellite with external systems. For example, webhooks can integrate with monitoring systems to send alerts when a host is created or deleted.

Webhooks are only triggered after an event occurs. The request usually contains details of the event. An event triggers callbacks, such as sending an e-mail confirming a host has been provisioned. The application sending the request does not wait for the response, or ignores it.

Because webhooks use HTTP, no new infrastructure needs be added to existing web services. Webhooks are useful where the action you want to perform in the external system can be achieved through its API.

Where it is necessary to run additional commands or edit files, the shellhooks plugin for Capsules is available. The shellhooks plugin enables you to define a shell script on the Capsule that can be executed through the API.

You can use webhooks successfully without installing the shellhooks plugin.

Payload of a webhook is created from webhook templates. Webhook templates use the same ERB syntax as Provisioning templates. Available variables:

- `@event_name`: Name of an event.
- `@webhook_id`: Unique event ID.
- `@payload`: Payload data, different for each event type. To access individual fields, use `@payload[:key_name]` Ruby hash syntax.
- `@payload[:object]`: Database object for events triggered by database actions (create, update, delete). Not available for custom events.
- `@payload[:context]`: Additional information as hash like request and session UUID, remote IP address, user, organization and location.

**Additional resources**

- [Section 19.4, “Available webhook events”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#webhooks-available-events_admin "19.4. Available webhook events")

## 19.2. Creating a webhook template

Webhook templates are used to generate the body of HTTP request to a configured target when a webhook is triggered. You can create a webhook template in the Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Webhook** > **Webhook Templates**.
2. Click **Clone an existing template** or **Create Template**.
3. Enter a name for the template.
4. Use the editor to make changes to the template payload.

   A webhook HTTP payload must be created using Satellite template syntax. The webhook template can use a special variable called `@object` that can represent the main object of the event. `@object` can be missing in case of certain events. You can determine what data are actually available with the `@payload` variable.

   For more information, see [Template Writing Reference](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts) in *Managing hosts* and for available template macros and methods, visit `/templates_doc` on Satellite Server.
5. Optional: Enter the description and audit comment.
6. Assign organizations and locations.
7. Click **Submit**.

**Example 19.1. Creating a webhook template**

When creating a webhook template, you must follow the format of the target application for which the template is intended. For example, an application can expect a `"text"` field with the webhook message. Refer to the documentation of your target application to find more about how your webhook template format should look like.

Running remote execution jobs
:   This webhook template defines a message with the ID and result of a remote execution job. The webhook which uses this template can be subscribed to events such as `Actions Remote Execution Run Host Job Succeeded` or `Actions Remote Execution Run Host Job Failed`.

    ```
    {
        "text": "job invocation <%= @object.job_invocation_id %> finished with result <%= @object.task.result %>"
    }
    ```

Creating users
:   This webhook template defines a message with the login and email of a created user. The webhook which uses this template should be subscribed to the `User Created` event.

    ```
    {
        "text": "user with login <%= @object.login %> and email <%= @object.mail %> created"
    }
    ```

## 19.3. Creating a webhook

When creating a webhook in the Satellite web UI, you can customize events, payloads, HTTP authentication, content type, and headers.

> **Note**
>
> When configuring webhooks with endpoints with non-standard HTTP or HTTPS ports, an SELinux port must be assigned, see [Configuring SELinux to ensure access to Satellite on custom ports](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/installing_satellite_server_in_a_connected_network_environment/index#configuring-selinux-to-ensure-access-on-custom-ports_satellite) in *Installing Satellite Server in a connected network environment*.

**Procedure**

1. In the Satellite web UI, navigate to **Administer** > **Webhook** > **Webhooks**.
2. Click **Create new**.
3. From the **Subscribe to** list, select an event.
4. Enter a **Name** for your webhook.
5. Enter a **Target URL**. Webhooks make HTTP requests to pre-configured URLs. The target URL can be a dynamic URL.
6. Click **Template** to select a template. Webhook templates are used to generate the body of the HTTP request to Satellite Server when a webhook is triggered.
7. Enter an HTTP method.
8. Optional: If you do not want activate the webhook when you create it, uncheck the **Enabled** flag.
9. Click the **Credentials** tab.
10. Optional: If HTTP authentication is required, enter **User** and **Password**.
11. Optional: Uncheck **Verify SSL** if you do not want to verify the server certificate against the system certificate store or Satellite CA.
12. On the **Additional** tab, enter the **HTTP Content Type**. For example, `application/json`, `application/xml` or `text/plain` on the payload you define. The application does not attempt to convert the content to match the specified content type.
13. Optional: Provide HTTP headers as JSON. ERB is also allowed.

## 19.4. Available webhook events

Review the webhook events that are available from the Satellite web UI.

`Action` events trigger webhooks only on `success`, so if an action fails, a webhook is not triggered.

For more information about payload, go to **Administer** > **About** > **Support** > **Templates DSL**. A list of available types is provided in the following table. Some events are marked as **custom**, in that case, the payload is an object object but a Ruby hash (key-value data structure) so syntax is different.

| Event name | Description | Payload |
| --- | --- | --- |
| Actions Katello Content View Promote Succeeded | A content view was successfully promoted. | Actions::Katello::ContentView::Promote |
| Actions Katello Content View Publish Succeeded | A repository was successfully synchronized. | Actions::Katello::ContentView::Publish |
| Actions Remote Execution Run Host Job Succeeded | A generic remote execution job succeeded for a host. This event is emitted for all Remote Execution jobs, when complete. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Errata Install Succeeded | Install errata using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Group Install Succeeded | Install package group using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Package Install Succeeded | Install package using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Group Remove | Remove package group using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Package Remove Succeeded | Remove package using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Service Restart Succeeded | Restart Services using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Group Update Succeeded | Update package group using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Package Update Succeeded | Update package using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Foreman OpenSCAP Run Scans Succeeded | Run OpenSCAP scan. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Ansible Run Host Succeeded | Runs an Ansible Playbook containing all the roles defined for a host. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Ansible Run Capsule Upgrade Succeeded | Upgrade Capsules on given Capsule Servers. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Ansible Configure Cloud Connector Succeeded | Configure Cloud Connector on given hosts. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Ansible Run Red Hat Lightspeed Plan Succeeded | Runs a given maintenance plan from Red Hat Access Red Hat Lightspeed given an ID. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Ansible Run Playbook Succeeded | Run an Ansible Playbook against given hosts. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Ansible Enable Web Console Succeeded | Run an Ansible Playbook to enable the web console on given hosts. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Puppet Run Host Succeeded | Perform a single Puppet run. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Katello Module Stream Action Succeeded | Perform a module stream action using the Katello interface. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Leapp Pre-upgrade Succeeded | Upgradeability check for RHEL 7 host. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Leapp Remediation Plan Succeeded | Run Remediation plan with Leapp. | Actions::RemoteExecution::RunHostJob |
| Actions Remote Execution Run Host Job Leapp Upgrade Succeeded | Run Leapp upgrade job for RHEL 7 host. | Actions::RemoteExecution::RunHostJob |
| Build Entered | A host entered the build mode. | Custom event: `@payload[:id]` (host id), `@payload[:hostname]` (host name). |
| Build Exited | A host build mode was canceled, either it was successfully provisioned or the user canceled the build manually. | Custom event: `@payload[:id]` (host id), `@payload[:hostname]` (host name). |
| Config Report Created/Updated/Destroyed | Common database operations on a configuration report. | ConfigReport |
| Content View Created/Updated/Destroyed | Common database operations on a content view. | Katello::ContentView |
| Domain Created/Updated/Destroyed | Common database operations on a domain. | Domain |
| Host Created/Updated/Destroyed | Common database operations on a host. | Host |
| Hostgroup Created/Updated/Destroyed | Common database operations on a hostgroup. | Hostgroup |
| Model Created/Updated/Destroyed | Common database operations on a model. | Model |
| Status Changed | Global host status of a host changed. | Custom event: `@payload[:id]` (host id), `@payload[:hostname]`, `@payload[:global_status]` (hash) |
| Subnet Created/Updated/Destroyed | Common database operations on a subnet. | Subnet |
| Template Render Performed | A report template was rendered. | Template |
| User Created/Updated/Destroyed | Common database operations on a user. | User |

## 19.5. Shellhooks plugin for Capsule

With webhooks, you can only map one Satellite event to one API call. For advanced integrations, where a single shell script can contain multiple commands, you can install a Capsule shellhooks plugin that exposes executables by using a REST HTTP API.

You can then configure a webhook to reach out to a Capsule API to run a predefined shellhook. A shellhook is an executable script that can be written in any language provided that it can be executed. The shellhook can for example contain commands or edit files.

You must place your executable scripts in `/var/lib/foreman-proxy/shellhooks` with only alphanumeric characters and underscores in their name.

You can pass input to shellhook script through the webhook payload. This input is redirected to standard input of the shellhook script. You can pass arguments to shellhook script by using HTTP headers in format `X-Shellhook-Arg-1` to `X-Shellhook-Arg-99`.

The HTTP method must be POST. An example URL would be: `https://capsule.example.com:9090/shellhook/My_Script`.

> **Note**
>
> Unlike the `shellhooks` directory, the URL must contain `/shellhook/` in singular to be valid.

You must enable **Capsule Authorization** for each webhook connected to a shellhook to enable it to authorize a call.

Standard output and standard error output are redirected to the Capsule logs as messages with debug or warning levels respectively.

The shellhook HTTPS calls do not return a value.

**Additional resources**

- [Section 19.7, “Passing arguments to shellhook script using webhooks”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#passing-arguments-to-shellhook-script-using-webhooks_admin "19.7. Passing arguments to shellhook script using webhooks")
- [Section 19.8, “Passing arguments to shellhook script using curl”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#passing-arguments-to-shellhook-script-using-curl_admin "19.8. Passing arguments to shellhook script using curl")
- [Section 19.9, “Creating a shellhook to print arguments”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#creating-a-shellhook-to-print-arguments_admin "19.9. Creating a shellhook to print arguments")

## 19.6. Installing the shellhooks plugin

Optionally, you can install and enable the shellhooks plugin on each Capsule used for shellhooks.

**Procedure**

- Install the shellhooks plugin on your Capsule:

  ```
  # satellite-installer --enable-foreman-proxy-plugin-shellhooks
  ```

## 19.7. Passing arguments to shellhook script using webhooks

You can pass dynamic values from a webhook event to a shellhook script by configuring HTTP headers when you create the webhook. This enables your script to use event-specific data such as object IDs or names without parsing the webhook payload.

**Procedure**

- When creating a webhook, on the **Additional** tab, create HTTP headers in the following format:

  ```
  {
    "X-Shellhook-Arg-1": "VALUE",
    "X-Shellhook-Arg-2": "VALUE"
  }
  ```

  Ensure that the headers have a valid JSON or ERB format. Only pass safe fields like database ID, name, or labels that do not include new lines or quote characters.

  For more information, see [Section 19.3, “Creating a webhook”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#creating-a-webhook_admin "19.3. Creating a webhook").

**Example 19.2. Passing arguments to shellhook script using webhooks**

```
{
  "X-Shellhook-Arg-1": "<%= @object.content_view_version_id %>",
  "X-Shellhook-Arg-2": "<%= @object.content_view_name %>"
}
```

## 19.8. Passing arguments to shellhook script using curl

You can pass custom values to a shellhook script by using a curl request. Use this when you need to test a script manually or call it directly, rather than through webhook automation.

**Procedure**

- When executing a shellhook script using `curl`, create HTTP headers in the following format:

  ```
  "X-Shellhook-Arg-1: VALUE"
  "X-Shellhook-Arg-2: VALUE"
  ```

**Example 19.3. Passing arguments to shellhook script using curl**

```
$ curl \
--data "" \
--header "Content-Type: text/plain" \
--header "X-Shellhook-Arg-1: Version 1.0" \
--header "X-Shellhook-Arg-2: My content view" \
--request POST \
--show-error \
--silent \
https://capsule.example.com:9090/shellhook/My_Script
```

## 19.9. Creating a shellhook to print arguments

Create a simple shellhook script that prints `Hello World!` when you run a remote execution job.

**Prerequisites**

- You have the webhooks and shellhooks plugins installed. For more information, see:

  - [Section 19.6, “Installing the shellhooks plugin”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#installing-shellhooks-plugin_admin "19.6. Installing the shellhooks plugin")

**Procedure**

1. Modify the `/var/lib/foreman-proxy/shellhooks/print_args` script to print arguments to standard error output so you can see them in the Capsule logs:

   ```bash
   #!/bin/sh
   #
   # Prints all arguments to stderr
   #
   echo "$@" >&2
   ```
2. In the Satellite web UI, navigate to **Administer** > **Webhook** > **Webhooks**.
3. Click **Create new**.
4. From the **Subscribe to** list, select **Actions Remote Execution Run Host Job Succeeded**.
5. Enter a **Name** for your webhook.
6. In the **Target URL** field, enter the URL of your Capsule Server followed by `:9090/shellhook/print_args`:

   ```
   https://capsule.example.com:9090/shellhook/print_args
   ```

   Note that `shellhook` in the URL is singular, unlike the `shellhooks` directory.
7. From the **Template** list, select **Empty Payload**.
8. On the **Credentials** tab, check **Capsule Authorization**.
9. On the **Additional** tab, enter the following text in the **Optional HTTP headers** field:

   ```
   {
       "X-Shellhook-Arg-1": "Hello",
       "X-Shellhook-Arg-2": "World!"
   }
   ```
10. Click **Submit**. You now have successfully created a shellhook that prints "Hello World!" to Capsule logs every time you a remote execution job succeeds.

**Verification**

1. Run a remote execution job on any host. You can use `time` as a command. For more information, see [Configuring and setting up remote jobs](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs) in *Managing hosts*.
2. Verify that the shellhook script was triggered and printed "Hello World!" to Capsule Server logs:

   ```
   # tail /var/log/foreman-proxy/proxy.log
   ```

   You should find the following lines at the end of the log:

   ```
   [I] Started POST /shellhook/print_args
   [I] Finished POST /shellhook/print_args with 200 (0.33 ms)
   [I] [3520] Started task /var/lib/foreman-proxy/shellhooks/print_args\ Hello\ World\!
   [W] [3520] Hello World!
   ```
