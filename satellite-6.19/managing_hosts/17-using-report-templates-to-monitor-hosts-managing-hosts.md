---
title: "Using report templates to monitor hosts"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "17"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Using_Report_Templates_to_Monitor_Hosts_managing-hosts"
---
# Chapter 17. Using report templates to monitor hosts

You can use report templates to query Satellite data to obtain information about, for example, host status, registered hosts, applicable errata, applied errata, and user activity. You can use the report templates that ship with Satellite or write your own custom report templates to suit your requirements.

## 17.1. Generating host monitoring reports by using Satellite web UI

You can generate host monitoring reports from the Satellite web UI so that you can view host data, such as installed packages or compliance status, in a report template. You can also schedule reports or send them by e-mail.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Reports** > **Report Templates**. For example, the **Host – Installed Products** template generates a report with installed product information along with other metrics, including system purpose attributes.
2. To the right of the report template that you want to use, click **Generate**.
3. Optional: To schedule a report, to the right of the **Generate at** field, click the icon to select the date and time you want to generate the report at.
4. Optional: To send a report to an e-mail address, select the **Send report via e-mail** checkbox, and in the **Deliver to e-mail addresses** field, enter the required e-mail address.
5. Optional: Apply search query filters. To view all available results, do not populate the filter field with any values.
6. Click **Submit**. A CSV file that contains the report is downloaded. If you have selected the **Send report via e-mail** checkbox, the host monitoring report is sent to your e-mail address.

## 17.2. Generating host monitoring reports by using Hammer CLI

You can generate host monitoring reports by using Hammer CLI so that you can view host data, such as installed packages or compliance status, in a report template. To schedule reports, configure a cron job.

**Procedure**

1. List all available report templates:

   ```
   $ hammer report-template list
   ```
2. Generate a report:

   ```
   $ hammer report-template generate --id My_Template_ID
   ```

   This command waits until the report fully generates before completing. If you want to generate the report as a background task, you can use the `hammer report-template schedule` command.

**Example 17.1. Generating a report based on the Subscription - General template**

To generate the **Subscription - General** report, add the `Days from Now` option to specify the latest expiration time of general subscriptions.

- To show all subscriptions:

  ```
  $ hammer report-template generate \
  --inputs "Days from Now=no limit" \
  --name "Subscription - General Report"
  ```
- To show all subscriptions that are going to expire within 60 days:

  ```
  $ hammer report-template generate \
  --inputs "Days from Now=60" \
  --name "Subscription - General Report"
  ```

## 17.3. Creating a report template

In Satellite, you can create a report template and customize the template to suit your requirements. You can import existing report templates and further customize them with snippets and template macros.

Report templates use Embedded Ruby (ERB) syntax. To view information about working with ERB syntax and macros, in the Satellite web UI, navigate to **Monitor** > **Reports** > **Report Templates**, and click **Create Template**, and then click the **Help** tab.

When you create a report template in Satellite, safe mode is enabled by default.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Reports** > **Report Templates**.
2. Click **Create Template**.
3. In the **Name** field, enter a unique name for your report template.
4. If you want the template to be available to all locations and organizations, select **Default**.
5. Create the template directly in the template editor or import a template from a text file by clicking **Import**. For more information about importing templates, see [Section 17.7, “Importing report templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Importing_Report_Templates_managing-hosts "17.7. Importing report templates").
6. Optional: In the **Audit Comment** field, you can add any useful information about this template.
7. Click the **Input** tab, and in the **Name** field, enter a name for the input that you can reference in the template in the following format: `input('name')`. Note that you must save the template before you can reference this input value in the template body.
8. Select whether the input value is mandatory. If the input value is mandatory, select the **Required** checkbox.
9. From the **Value Type** list, select the type of input value that the user must input.
10. Optional: If you want to use facts for template input, select the **Advanced** checkbox.
11. Optional: In the **Options** field, define the options that the user can select from. If this field remains undefined, the users receive a free-text field in which they can enter the value they want.
12. Optional: In the **Default** field, enter a value, for example, a host name, that you want to set as the default template input.
13. Optional: In the **Description** field, you can enter information that you want to display as inline help about the input when you generate the report.
14. Optional: Click the **Type** tab, and select whether this template is a snippet to be included in other templates.
15. Click the **Location** tab and add the locations where you want to use the template.
16. Click the **Organizations** tab and add the organizations where you want to use the template.
17. Click **Submit** to save your changes.

**Additional resources**

- [Appendix B, *Template writing reference*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts "Appendix B. Template writing reference")
- [Section B.7, “Template macros reference”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#template-macros-reference "B.7. Template macros reference")

## 17.4. Exporting report templates by using Satellite web UI

You can export report templates that you create in Satellite from Satellite web UI.

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Reports** > **Report Templates**.
2. Locate the template that you want to export, and from the list in the **Actions** column, select **Export**.
3. Repeat this action for every report template that you want to download.

## 17.5. Exporting report templates by using Hammer CLI

You can export report templates that you create in Satellite by using Hammer CLI.

**Procedure**

1. To view the report templates available for export, enter the following command:

   ```
   $ hammer report-template list
   ```

   Note the template ID of the template that you want to export in the output of this command.
2. To export a report template, enter the following command:

   ```
   $ hammer report-template dump --id My_Template_ID > example_export.erb
   ```

## 17.6. Exporting report templates using the Satellite API

You can use the Satellite `report_templates` API to export report templates from Satellite.

**Procedure**

1. Use the following request to retrieve a list of available report templates. For example:

   ```
   $ curl \
   --user "My_User_Name:My_Password" \
   https://satellite.example.com/api/report_templates \
   | json_reformat
   ```

   In this example, the `json_reformat` tool is used to format the JSON output.

   Example response:

   ```
   {
       "total": 6,
       "subtotal": 6,
       "page": 1,
       "per_page": 20,
       "search": null,
       "sort": {
           "by": null,
           "order": null
       },
       "results": [
           {
               "created_at": "2019-11-20 17:49:52 UTC",
               "updated_at": "2019-11-20 17:49:52 UTC",
               "name": "Applicable errata",
               "id": 112
           },
           {
               "created_at": "2019-11-20 17:49:52 UTC",
               "updated_at": "2019-11-20 17:49:52 UTC",
               "name": "Applied Errata",
               "id": 113
           },
           {
               "created_at": "2019-11-30 16:15:24 UTC",
               "updated_at": "2019-11-30 16:15:24 UTC",
               "name": "Hosts - complete list",
               "id": 158
           },
           {
               "created_at": "2019-11-20 17:49:52 UTC",
               "updated_at": "2019-11-20 17:49:52 UTC",
               "name": "Host statuses",
               "id": 114
           },
           {
               "created_at": "2019-11-20 17:49:52 UTC",
               "updated_at": "2019-11-20 17:49:52 UTC",
               "name": "Registered hosts",
               "id": 115
           },
           {
               "created_at": "2019-11-20 17:49:52 UTC",
               "updated_at": "2019-11-20 17:49:52 UTC",
               "name": "Subscriptions",
               "id": 116
           }
       ]
   }
   ```
2. Note the `id` of the template that you want to export, and use the following request to export the template.

   Example request:

   ```
   $ curl \
   --output /tmp/_Example_Export_Template.erb_ \
   --user "My_User_Name:My_Password" \
   https://satellite.example.com/api/report_templates/My_Template_ID/export
   ```

   In this example, the exported template is redirected to `host_complete_list.erb`.

## 17.7. Importing report templates

You can import a report template into the body of a new template that you want to create. Note that using the Satellite web UI, you can only import templates individually.

**Prerequisites**

- Templates are exported from Satellite for use in new templates. For more information see [Section 17.4, “Exporting report templates by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#exporting-report-templates-by-using-web-ui "17.4. Exporting report templates by using Satellite web UI") and [Section 17.5, “Exporting report templates by using Hammer CLI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#exporting-report-templates-by-using-cli "17.5. Exporting report templates by using Hammer CLI").

**Procedure**

1. In the Satellite web UI, navigate to **Monitor** > **Reports** > **Report Templates**.
2. In the upper right of the Report Templates window, click **Create Template**.
3. On the upper right of the **Editor** tab, click the folder icon, and select the `.erb` file that you want to import.
4. Edit the template to suit your requirements.
5. Click **Submit**.

**Additional resources**

- [Appendix B, *Template writing reference*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts "Appendix B. Template writing reference")
- [Section 17.8, “Importing report templates using the Satellite API”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Importing_Report_Templates_Using_the_API_managing-hosts "17.8. Importing report templates using the Satellite API")

## 17.8. Importing report templates using the Satellite API

You can use the Satellite API to import report templates into Satellite. Importing report templates using the Satellite API automatically parses the report template metadata and assigns organizations and locations.

**Prerequisites**

- A template is created using `.erb` syntax or exported from another Satellite.

  For more information about writing templates, see [Appendix B, *Template writing reference*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts "Appendix B. Template writing reference").

  For more information about exporting templates from Satellite, see [Section 17.6, “Exporting report templates using the Satellite API”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Exporting_Report_Templates_Using_the_API_managing-hosts "17.6. Exporting report templates using the Satellite API").

**Procedure**

1. Use the following example to format the template that you want to import to a `.json` file:

   ```
   # cat Example_Template.json
   {
       "name": "Example Template Name",
       "template": "
       Enter ERB Code Here
   "
   }
   ```

   Example JSON file with ERB template:

   ```
   {
       "name": "Hosts - complete list",
       "template": "
   <%#
   name: Hosts - complete list
   snippet: false
   template_inputs:
   - name: host
     required: false
     input_type: user
     advanced: false
     value_type: plain
     resource_type: Katello::ActivationKey
   model: ReportTemplate
   -%>
   <% load_hosts(search: input('host')).each_record do |host| -%>
   <%
         report_row(
             'Server FQDN': host.name
         )
   -%>
   <%  end -%>
   <%= report_render %>
   "
   }
   ```
2. Use the following request to import the template:

   ```
   $ curl \
   --data @Example_Template.json \
   --header "Content-Type: application/json" \
   --request POST \
   --user "My_User_Name:My_Password" \
   https://satellite.example.com/api/report_templates/import
   ```
3. Use the following request to retrieve a list of report templates and validate that you can view the template in Satellite:

   ```
   $ curl \
   --user "My_User_Name:My_Password" \
   https://satellite.example.com/api/report_templates \
   | json_reformat
   ```

## 17.9. Report template safe mode

When you create report templates in Satellite, report template safe mode is enabled by default. Safe mode helps prevent rendering problems and enforces best practices in report templates.

Report template safe mode limits the macros and variables that you can use in the report template. The list of supported macros and variables is available in the Satellite web UI.

To view the macros and variables that are available, in the Satellite web UI, navigate to **Monitor** > **Reports** > **Report Templates** and click **Create Template**. In the Create Template window, click the **Help** tab and expand **Safe mode methods**.

While safe mode is enabled, if you try to use a macro or variable that is not listed in **Safe mode methods**, the template editor displays an error message.

To view the status of safe mode in Satellite, in the Satellite web UI, navigate to **Administer** > **Settings** and click the **Provisioning** tab. Locate the **Safemode rendering** row to check the value.

## 17.10. Writing report templates

Report templates are Ruby scripts executed on Satellite Server and are able to extract, process, and present information from internal databases in a tabular form. They represent an easy way within Satellite to generate customizable reports.

Satellite contains a selection of generic report templates. In the Satellite web UI, navigate to **Monitor** > **Reports** > **Report Templates** for a list of all templates.

As an example, this guide shows you how to write a template, which returns the number and kind of installable errata on hosts. Errata contain information to update and/or patch software. They cover security updates, bugfixes, or new software features. For this purpose, every erratum contains a list of packages affected by the update. Keeping a watchful eye on errata is therefore always a good idea to keep your hosts up to date. In this context, Satellite distinguishes between two types of errata, *installable* and *available* errata:

- *Available* errata for a host are always determined with respect to the latest packages maintained by Satellite.
- *Available* errata may differ from *installable* errata, because hosts are normally registered to a frozen state of packages, so called content views.

The final template shows both the number of *applicable* and *installable* errata for each host.

Report templates allow access to all functionalities of the Satellite API and Satellite variables.

**Example 17.2. Report template to view applicable errata**

You can create a custom report template to get a summary of all hosts that have applicable errata:

```
<%#
name: View applicable errata
description: A basic report template to view all applicable errata.
model: ReportTemplate
-%>

<%# Loop over all hosts-%>
<%-  load_hosts(includes: [:operatingsystem, :applicable_errata, :lifecycle_environment]).each_record do |host| -%>
<%-    @errata = 0 -%>
<%-    if host.operatingsystem.family != "Windows" -%>
<%-      # Loop over all errata for the single host -%>
<%-      host_applicable_errata_filtered(host).each do |erratum| -%>
<%-        @errata = @errata+1 -%>
<%-      end -%>
<%-      report_row(
          'Host': host.name,
          'Operating system': host.operatingsystem,
          'Lifecycle environment': host.lifecycle_environment,
          'Total': @errata,
         ) -%>
<%-    end -%>
<%-  end -%>

<%= report_render -%>
```

The first code block is a comment that contains meta data, as indicated by the brackets `<%# …​ -%>`.

The second code block contains executable Ruby code, as indicated by the brackets `<%- -%>`. The macro `load_hosts` loads the host data contained in Satellite. The processed information is determined by the `includes` keyword. This example requires the operating system, the lifecycle environment, and the applicable errata. The following `each_record do |host|` iterates over all returned hosts entries saved in `host`. Hosts running Windows are explicitly excluded from the list of hosts. The applicable errata for each host are then processed through the `host_applicable_errata_filtered()` macro. The exact number of applicable errata is then summed up in the counter `@errata` and passed to the `report_row()` macro, which adds a corresponding host line to the report table.

The third block renders the report.

Table 17.1. Example report template output

| Host | Operating system | Lifecycle environment | Total |
| --- | --- | --- | --- |
| host1.example.com | Red Hat Enterprise Linux | Testing | 32 |
| host2.example.com | Red Hat Enterprise Linux | Production | 163 |
| host3.example.com | Red Hat Enterprise Linux | Development | 23 |

**Example 17.3. Report template to view errata types**

You can extend the report template to allow users to restrict the report to a list of hosts instead of all hosts and to display the kind of errata in the report. The modified template looks as follows:

```
<%#
name: Applicable Errata
description: A basic report template for gathering all applicable errata.
template_inputs:
- name: Hosts filter
  required: false
  input_type: user
  advanced: false
  value_type: plain
  hidden_value: false
model: ReportTemplate
-%>
<%# Loop over all or input list of hosts -%>
<%-  load_hosts(search: input('Hosts filter'), includes: [:operatingsystem, :applicable_errata, :lifecycle_environment]).each_record do |host| -%>
<%-    if host.operatingsystem.family != "Windows" -%>
<%-      @errata = 0 -%>
<%-      @bugfix = 0 -%>
<%-      @misc_err = 0 -%>
<%-      @enhancement = 0 -%>
<%-      @security = 0 -%>
<%-      # Loop over all errata for the single host -%>
<%-      host_applicable_errata_filtered(host).each do |erratum| -%>
<%-        @errata = @errata+1 -%>
<%-        if erratum[:errata_type]=="security" -%>
<%-          @security=@security+1 -%>
<%-        elsif erratum[:errata_type]=="bugfix" -%>
<%-          @bugfix=@bugfix+1 -%>
<%-        elsif erratum[:errata_type]=="recommended" -%>
<%-          @bugfix=@bugfix+1 -%>
<%-        elsif erratum[:errata_type]=="enhancement" -%>
<%-          @enhancement=@enhancement+1 -%>
<%-        elsif erratum[:errata_type]=="optional" -%>
<%-          @enhancement=@enhancement+1 -%>
<%-        else -%>
<%-          @misc_err=@misc_err+1 -%>
<%-        end -%>
<%-      end -%>
<%-      report_row(
          'Host': host.name,
          'Operating system': host.operatingsystem,
          'Lifecycle environment': host.lifecycle_environment,
          # Library specific errata
          'Security': @security,
          'Bugfix': @bugfix,
          'Enhance': @enhancement,
          'Misc': @misc_err,
          'Total': @errata,
         ) -%>
<%-    end -%>
<%-  end -%>
<%= report_render -%>
```

`load_hosts` is extended by `search: input('Hosts filter')`. The `input` macro allows users to add input during execution of the template. In this case, it limits the search to a list of hosts. The template now distinguishes between security, bugfix, and enhancement errata.

Add the input name `Hosts filter` to the **Inputs** tab of the template.

Table 17.2. Example report template output

| Host | Operating system | Lifecycle environment | Security | Bugfix | Enhance | Misc | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| host.example.com | Red Hat Enterprise Linux | Testing | 9 | 20 | 2 | 1 | 32 |

**Example 17.4. Report template to view installable and available errata**

You can extend the report template to view errata that are installable on the host and how many packages are affected by available errata.

```
<%#
name: Applicable Errata
description: A basic report template for gathering all applicable errata.
template_inputs:
- name: Hosts filter
  required: false
  input_type: user
  advanced: false
  value_type: plain
  hidden_value: false
model: ReportTemplate
-%>
<%# Loop over all or input list of hosts -%>
<%-  load_hosts(search: input('Hosts filter'), includes: [:operatingsystem, :applicable_errata, :lifecycle_environment]).each_record do |host| -%>
<%-    if host.operatingsystem.family != "Windows" -%>
<%-      @errata = 0 -%>
<%-      @bugfix = 0 -%>
<%-      @misc_err = 0 -%>
<%-      @enhancement = 0 -%>
<%-      @security = 0 -%>
<%-      #Content View Errata%>
<%-      @cv_misc_err = host.content_facet_attributes.errata_counts[:total] -%>
<%-      @cv_misc_err = @cv_misc_err - host.content_facet_attributes.errata_counts[:enhancement] -%>
<%-      @cv_misc_err = @cv_misc_err - host.content_facet_attributes.errata_counts[:bugfix] -%>
<%-      @cv_misc_err = @cv_misc_err - host.content_facet_attributes.errata_counts[:security] -%>
<%-      # Loop over all errata for the single host -%>
<%-      host_applicable_errata_filtered(host).each do |erratum| -%>
<%-          @errata = @errata+1 -%>
<%-          if erratum[:errata_type]=="security" -%>
<%-             @security=@security+1 -%>
<%-          elsif erratum[:errata_type]=="bugfix" -%>
<%-             @bugfix=@bugfix+1 -%>
<%-          elsif erratum[:errata_type]=="recommended" -%>
<%-             @bugfix=@bugfix+1 -%>
<%-          elsif erratum[:errata_type]=="enhancement" -%>
<%-             @enhancement=@enhancement+1 -%>
<%-          elsif erratum[:errata_type]=="optional" -%>
<%-             @enhancement=@enhancement+1 -%>
<%-          else -%>
<%-             @misc_err=@misc_err+1 -%>
<%-         end -%>
<%-      end -%>
<%-      report_row(
          'Host': host.name,
          'Operating system': host.operatingsystem,
          'Lifecycle environment': host.lifecycle_environment,
          # Library specific errata
          'Security': @security,
          'Bugfix': @bugfix,
          'Enhance': @enhancement,
          'Misc': @misc_err,
          'Total': @errata,
          # Content View specific errata
          'CV Security': host.content_facet_attributes.errata_counts[:security],
          'CV Bugfix': host.content_facet_attributes.errata_counts[:bugfix],
          'CV Enhance': host.content_facet_attributes.errata_counts[:enhancement],
          'CV Misc': @cv_misc_err,
          'CV Total': host.content_facet_attributes.errata_counts[:total],
          'Packages': host.content_facet_attributes.applicable_deb_count+host.content_facet_attributes.applicable_rpm_count,
         ) -%>
<%-    end -%>
<%-  end -%>
<%= report_render -%>
```

Satellite provides the number of installable errata through the host attribute `host.content_facet_attributes.errata_counts`.

Table 17.3. Example report template output

| Host | CV Security | CV Bugfix | CV Enhance | CV Misc | CV Total | Packages |
| --- | --- | --- | --- | --- | --- | --- |
| host.example.com | 6 | 13 | 1 | 0 | 20 | 242 |

If the number of installable errata is smaller than the number of available errata, update the corresponding content view as soon as possible. Afterwards, update your host.
