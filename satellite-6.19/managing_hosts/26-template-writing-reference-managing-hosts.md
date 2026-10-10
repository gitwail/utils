---
title: "Template writing reference"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "B"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Template_Writing_Reference_managing-hosts"
---
# Appendix B. Template writing reference

Embedded Ruby (ERB) is a tool for generating text files based on templates that combine plain text with Ruby code. You can use the following Satellite-specific macros and variables in your ERB templates.

## B.1. Template rendering and ERB context

You can review how Red Hat Satellite renders ERB templates during provisioning and remote jobs, why safemode is enabled by default, and which features use ERB syntax.

When you provision a host or run a remote job, the code in the ERB runs and variables are replaced with host-specific values. This process is called **rendering**. Satellite Server enables the safemode rendering option by default so harmful template code cannot execute.

Note that the default templates provided by Red Hat Satellite (**Hosts** > **Templates** > **Provisioning Templates**, **Hosts** > **Templates** > **Job templates**, **Monitor** > **Reports** > **Report Templates** ) also provide a good source of ERB syntax examples.

Red Hat Satellite uses ERB syntax in the following cases:

Provisioning templates
:   For more information, see [Creating provisioning templates in Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-provisioning-templates-by-using-web-ui) in *Provisioning hosts*.

Remote execution job templates
:   For more information, see [Chapter 19, *Configuring and setting up remote jobs*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#configuring-and-setting-up-remote-jobs "Chapter 19. Configuring and setting up remote jobs").

Report templates
:   For more information, see [Chapter 17, *Using report templates to monitor hosts*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#Using_Report_Templates_to_Monitor_Hosts_managing-hosts "Chapter 17. Using report templates to monitor hosts").

Templates for partition tables
:   For more information, see [Creating partition tables by using Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/provisioning_hosts/index#creating-partition-tables-by-using-web-ui) in *Provisioning hosts*.

Smart Class Parameters
:   For more information, see [Configuring Puppet smart class parameters](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_configurations_by_using_puppet_integration/index#Configuring_Puppet_Smart_Class_Parameters_managing-configurations-puppet) in *Managing configurations by using Puppet integration*.

## B.2. Accessing the template writing reference in the Satellite web UI

You can open the template writing reference from the Satellite web UI to look up ERB macros, variables, and syntax when writing or editing provisioning templates, job templates, or report templates.

**Procedure**

1. Log in to the Satellite web UI.
2. In the Satellite web UI, navigate to **Administer** > **About**.
3. Click the **Templates DSL** link in the Support section.

## B.3. Using autocompletion in templates

You can access a list of available macros and usage information in the template editor with the autocompletion option. This works for all templates within Satellite.

**Procedure**

1. In the Satellite web UI, navigate to either **Hosts** > **Templates** > **Partition tables**, **Hosts** > **Templates** > **Provisioning Templates**, or **Hosts** > **Templates** > **Job templates**.
2. Click the **settings** icon at the top right corner of the template editor and select **Autocompletion**.
3. Press `Ctrl` + `Space` in the template editor to access a list of all available macros. You can narrow down the list of macros by typing in more information about what you are looking for. For example, if you are looking for a method to list the ID of the content source for a host, you can type `host` and check the list of available macros for content source.
4. A window next to the dropdown provides a description of the macro, its usage, and the value it will return.
5. When you find the method you are looking for, hit `Enter` to input the method.

   You can also enable **Live Autocompletion** in the **settings** menu to view a list of macros that match the pattern whenever you type something. However, this might input macros in unintended places, like package names in a provisioning template.

## B.4. Writing ERB templates

You can use the following common tags in your ERB templates.

> **Note**
>
> Because of the varying lengths of the ERB tags, indenting the ERB syntax might seem messy. ERB syntax ignores white space. One method of handling the indentation is to declare the ERB tag at the beginning of each new line and then use white space within the ERB tag to outline the relationships within the syntax, for example:
>
> ```
> <%- load_hosts.each do |host| -%>
> <%-   if host.build? %>
> <%=     host.name %> build is in progress
> <%-   end %>
> <%- end %>
> ```

<% %>
:   All Ruby code is enclosed within `<% %>` in an ERB template. The code is executed when the template is rendered. It can contain Ruby control flow structures as well as Satellite-specific macros and variables. For example:

    ```
    <% if @host.operatingsystem.family == "Redhat" && @host.operatingsystem.major.to_i > 6 -%>
    systemctl <%= input("action") %> <%= input("service") %>
    <% else -%>
    service <%= input("service") %> <%= input("action") %>
    <% end -%>
    ```

    Note that this template silently performs an action with a service and returns nothing at the output.

<%= %>
:   This provides the same functionality as `<% %>` but when the template is executed, the code output is inserted into the template. This is useful for variable substitution, for example:

    Example input:

    ```
    echo <%= @host.name %>
    ```

    Example rendering:

    ```
    host.example.com
    ```

    Example input:

    ```
    <% server_name = @host.fqdn %>
    <%= server_name %>
    ```

    Example rendering:

    ```
    host.example.com
    ```

    Note that if you enter an incorrect variable, no output is returned. However, if you try to call a method on an incorrect variable, the following error message returns:

    Example input:

    ```
    <%= @example_incorrect_variable.fqdn -%>
    ```

    Example rendering:

    ```
    undefined method `fqdn' for nil:NilClass
    ```

<% -%>, <%= -%>
:   By default, a newline character is inserted after a Ruby block if it is closed at the end of a line:

    Example input:

    ```
    <%= "line1" %>
    <%= "line2" %>
    ```

    Example rendering:

    ```
    line1
    line2
    ```

    To change the default behavior, modify the enclosing mark with `-%>`:

    Example input:

    ```
    <%= "line1" -%>
    <%= "line2" %>
    ```

    Example rendering:

    ```
    line1line2
    ```

    This is used to reduce the number of lines, where Ruby syntax permits, in rendered templates. White spaces in ERB tags are ignored.

    An example of how this would be used in a report template to remove unnecessary newlines between a FQDN and IP address:

    Example input:

    ```
    <%= @host.fqdn -%>
    <%= @host.ip -%>
    ```

    Example rendering:

    ```
    host.example.com10.10.181.216
    ```

<%# %>
:   Encloses a comment that is ignored during template rendering:

    Example input:

    ```
    <%# A comment %>
    ```

    This generates no output.

## B.5. Troubleshooting ERB templates

You can use the Satellite web UI to troubleshoot ERB templates.

The Satellite web UI provides two ways to verify the template rendering for a specific host:

- **Directly in the template editor** – when editing a template (under **Hosts** > **Templates** > **Partition tables**, **Hosts** > **Templates** > **Provisioning Templates**, or **Hosts** > **Templates** > **Job templates**), on the **Template** tab click **Preview** and select a host from the list. The template then renders in the text field using the selected host’s parameters. Preview failures can help to identify issues in your template.
- **At the host’s details page** – select a host at **Hosts** > **All Hosts** and click the **Templates** tab to list templates associated with the host. Select **Review** from the list next to the selected template to view it’s rendered version.

## B.6. Generic Satellite-specific macros

You can use Satellite-specific macros in your ERB templates to generate URLs, indent code, and reuse common patterns across templates.

Table B.1. Generic macros

| Name | Description |
| --- | --- |
| indent(n) | Indents the block of code by n spaces, useful when using a snippet template that is not indented. |
| foreman_url(kind) | Returns the full URL to host-rendered templates of the given kind. For example, templates of the "provision" type usually reside at `http://satellite.example.com/unattended/provision`. |
| snippet(name) | Renders the specified snippet template. Useful for nesting provisioning templates. |
| snippets(file) | Renders the specified snippet found in the Foreman database, attempts to load it from the `unattended/snippets/` directory if it is not found in the database. |
| snippet_if_exists(name) | Renders the specified snippet, skips if no snippet with the specified name is found. |

## B.7. Template macros reference

You can use macros in ERB templates to add user inputs, load host data, and perform other tasks when writing provisioning, job, or report templates. Availability and options vary by template type.

For more information about the macros available for each template type, navigate to the following pages in the Satellite web UI:

- **Monitor** > **Reports** > **Report Templates** > **Create Template** for report templates
- **Hosts** > **Templates** > **Job templates** > **New Job Template** for job templates

Click the **Help** tab on these pages for more details.

input
:   Using the `input` macro, you can customize the input data that the template can work with. You can define the input name, type, and the options that are available for users. For report templates, you can only use user inputs. When you define a new input and save the template, you can then reference the input in the ERB syntax of the template body.

    ```
    <%= input('cpus') %>
    ```

    This loads the value from user input `cpus`.

load_hosts
:   Using the `load_hosts` macro, you can generate a complete list of hosts.

    ```
    <%- load_hosts().each_record do |host| -%>
    <%=     host.name %>
    ```

    Use the `load_hosts` macro with the `each_record` macro to load records in batches of 1000 to reduce memory consumption.

    If you want to filter the list of hosts for the report, you can add the option `search: input('Example_Host')`:

    ```
    <% load_hosts(search: input('Example_Host')).each_record do |host| -%>
    <%=  host.name %>
    <% end -%>
    ```

    In this example, you first create an input that you then use to refine the search criteria that the `load_hosts` macro retrieves.

report_row
:   Using the `report_row` macro, you can create a formatted report for ease of analysis. The `report_row` macro requires the `report_render` macro to generate the output.

    Example input:

    ```
    <%- load_hosts(search: input('Example_Host')).each_record do |host| -%>
    <%-   report_row(
            'Server FQDN': host.name
          ) -%>
    <%- end -%>
    <%= report_render -%>
    ```

    Example rendering:

    ```
    Server FQDN
    host1.example.com
    host2.example.com
    host3.example.com
    host4.example.com
    host5.example.com
    host6.example.com
    ```

    You can add extra columns to the report by adding another header. The following example adds IP addresses to the report:

    Example input:

    ```
    <%- load_hosts(search: input('host')).each_record do |host| -%>
    <%-   report_row(
          'Server FQDN': host.name,
               'IP': host.ip
          ) -%>
    <%- end -%>
    <%= report_render -%>
    ```

    Example rendering:

    ```
    Server FQDN,IP
    host1.example.com,10.8.30.228
    host2.example.com,10.8.30.227
    host3.example.com,10.8.30.226
    host4.example.com,10.8.30.225
    host5.example.com,10.8.30.224
    host6.example.com,10.8.30.223
    ```

report_render
:   This macro is available only for report templates.

    Using the `report_render` macro, you create the output for the report. During the template rendering process, you can select the format that you want for the report. YAML, JSON, HTML, and CSV formats are supported.

    ```
    <%= report_render -%>
    ```

render_template()
:   This macro is available only for job templates.

    Using this macro, you can render a specific template. You can also enable and define arguments that you want to pass to the template.

truthy
:   Using the `truthy` macro, you can declare if the value passed is true or false, regardless of whether the value is an integer or boolean or string.

    This macro helps to avoid confusion when your template contains multiple value types. For example, the boolean value `true` is not the same as the string value `"true"`. With this macro, you can declare how you want the template to interpret the value and avoid confusion.

    You can use `truthy` to declare values as follows:

    ```
    truthy?("true") => true
    truthy?(1) => true
    truthy?("false") => false
    truthy?(0) => false
    ```

falsy
:   The falsy macro serves the same purpose as the truthy macro.

    Using the `falsy` macro, you can declare if the value passed in is true or false, regardless of whether the value is an integer or boolean or string.

    You can use `falsy` to declare values as follows:

    ```
    falsy?("true") => false
    falsy?(1) => false
    falsy?("false") => true
    falsy?(0) => true
    ```

## B.8. Host-specific variables in templates

You can use host-specific variables in templates to access host data such as architecture and operating system.

Note that job templates accept only `@host` variables.

Table B.2. Host-specific variables and macros

| Name | Description |
| --- | --- |
| `@host.architecture` | The architecture of the host. |
| `@host.bond_interfaces` | Returns an array of all bonded interfaces. See [Section B.11, “Parsing arrays in templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#parsing-arrays-in-templates "B.11. Parsing arrays in templates"). |
| `@host.capabilities` | The method of system provisioning, can be either build (for example Kickstart) or image. |
| `@host.certname` | The SSL certificate name of the host. |
| `@host.diskLayout` | The disk layout of the host. Can be inherited from the operating system. |
| `@host.domain` | The domain of the host. |
| `@host.environment` **Deprecated** Use the `host_puppet_environment` variable instead. | The Puppet environment of the host. |
| `@host.facts` | Returns a Ruby hash of facts from Facter. For example to access the 'ipaddress' fact from the output, specify @host.facts['ipaddress']. |
| `@host.grub_pass` | Returns the host’s boot loader password. |
| `@host.hostgroup` | The host group of the host. |
| `host_enc['parameters']` | Returns a Ruby hash containing information on host parameters. For example, use host_enc['parameters']['lifecycle_environment'] to get the lifecycle environment of a host. |
| `@host.image_build?` | Returns `true` if the host is provisioned using an image. |
| `@host.interfaces` | Contains an array of all available host interfaces including the primary interface. See [Section B.11, “Parsing arrays in templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#parsing-arrays-in-templates "B.11. Parsing arrays in templates"). |
| `@host.interfaces_with_identifier('IDs')` | Returns array of interfaces with given identifier. You can pass an array of multiple identifiers as an input, for example @host.interfaces_with_identifier(['eth0', 'eth1']). See [Section B.11, “Parsing arrays in templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#parsing-arrays-in-templates "B.11. Parsing arrays in templates"). |
| `@host.ip` | The IP address of the host. |
| `@host.location` | The location of the host. |
| `@host.mac` | The MAC address of the host. |
| `@host.managed_interfaces` | Returns an array of managed interfaces (excluding BMC and bonded interfaces). See [Section B.11, “Parsing arrays in templates”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#parsing-arrays-in-templates "B.11. Parsing arrays in templates"). |
| `@host.medium` | The assigned operating system installation medium. |
| `@host.name` | The full name of the host. |
| `@host.operatingsystem.family` | The operating system family. |
| `@host.operatingsystem.major` | The major version number of the assigned operating system. |
| `@host.operatingsystem.minor` | The minor version number of the assigned operating system. |
| `@host.operatingsystem.name` | The assigned operating system name. |
| `@host.operatingsystem.boot_files_uri(medium_provider)` | Full path to the kernel and initrd, returns an array. |
| `@host.os.medium_uri(@host)` | The URI used for provisioning (path configured in installation media). |
| `host_param('parameter_name')` | Returns the value of the specified host parameter. |
| `host_param_false?('parameter_name')` | Returns `false` if the specified host parameter evaluates to false. |
| `host_param_true?('parameter_name')` | Returns `true` if the specified host parameter evaluates to true. |
| `@host.primary_interface` | Returns the primary interface of the host. |
| `@host.provider` | The compute resource provider. |
| `@host.provision_interface` | Returns the provisioning interface of the host. Returns an interface object. |
| `@host.ptable` | The partition table name. |
| `@host.puppet_ca_server` **Deprecated** Use the `host_puppet_ca_server` variable instead. | The Puppet CA server the host must use. |
| `@host.puppetmaster` **Deprecated** Use the `host_puppet_server` variable instead. | The OpenVox server the host must use. |
| `@host.pxe_build?` | Returns `true` if the host is provisioned using the network or PXE. |
| `@host.shortname` | The short name of the host. |
| `@host.sp_ip` | The IP address of the BMC interface. |
| `@host.sp_mac` | The MAC address of the BMC interface. |
| `@host.sp_name` | The name of the BMC interface. |
| `@host.sp_subnet` | The subnet of the BMC network. |
| `@host.subnet.dhcp` | Returns `true` if a DHCP proxy is configured for this host. |
| `@host.subnet.dns_primary` | The primary DNS server of the host. |
| `@host.subnet.dns_secondary` | The secondary DNS server of the host. |
| `@host.subnet.gateway` | The gateway of the host. |
| `@host.subnet.mask` | The subnet mask of the host. |
| `@host.url_for_boot(:initrd)` | Full path to the initrd image associated with this host. Not recommended, as it does not interpolate variables. |
| `@host.url_for_boot(:kernel)` | Full path to the kernel associated with this host. Not recommended, as it does not interpolate variables, prefer boot_files_uri. |
| `@provisioning_type` | Equals to `host` or `hostgroup` depending on type of provisioning. |
| `@static` | Returns `true` if the network configuration is static. |
| `@template_name` | Name of the template being rendered. |
| `grub_pass` | Returns a boot loader argument to set the encrypted boot loader password, such as **--md5pass=#{@host.grub_pass}**. |
| `ks_console` | Returns a string assembled using the port and the baud rate of the host which can be added to a kernel line. For example **console=ttyS1,9600**. |
| `root_pass` | Returns the root password configured for the system. |

The majority of common Ruby methods can be applied on host-specific variables. For example, to extract the last segment of the host’s IP address, you can use:

```
<% @host.ip.split('.').last %>
```

## B.9. Kickstart-specific variables

You can use Kickstart-specific variables in provisioning templates to inject host data and installation options.

Table B.3. Kickstart-specific variables

| Name | Description |
| --- | --- |
| @arch | The host architecture name, same as @host.architecture.name. |
| @dynamic | Returns `true` if the partition table being used is a %pre script (has the #Dynamic option as the first line of the table). |
| @epel | A command which will automatically install the correct version of the epel-release RPM. Use in a %post script. |
| @mediapath | The full Kickstart line to provide the URL command. |
| @osver | The operating system major version number, same as @host.operatingsystem.major. |

## B.10. Conditional statements in ERB

In your templates, you might perform different actions depending on which value exists. To achieve this, you can use conditional statements in your ERB syntax.

In the following example, the ERB syntax searches for a specific host name and returns an output depending on the value it finds:

- Example input:

  ```
  <% load_hosts().each_record do |host| -%>
  <% if @host.name == "host1.example.com" -%>
  <%      result="positive" -%>
  <%  else -%>
  <%      result="negative" -%>
  <%  end -%>
  <%= result -%>
  ```
- Example rendering:

  ```
  host1.example.com
  positive
  ```

## B.11. Parsing arrays in templates

While writing or modifying templates, you might encounter variables that return arrays. Use Ruby methods to parse arrays so that you can extract parameter values from specific entries, such as interface data from `@host.interfaces`.

The following procedure is an example that you can use to find the relevant methods to parse arrays in your template. In this example, a report template is used, but the steps are applicable to other templates.

**Procedure**

1. To retrieve the NIC of a host, in this example, using the `@host.interfaces` variable returns class values that you can then use to find methods to parse the array.

   Example input:

   ```
   <%= @host.interfaces -%>
   ```

   Example rendering:

   ```
   <Nic::Base::ActiveRecord_Associations_CollectionProxy:0x00007f734036fbe0>
   ```
2. In the Create Template window, click the **Help** tab and search for the `ActiveRecord_Associations_CollectionProxy` and `Nic::Base` classes.
3. For `ActiveRecord_Associations_CollectionProxy`, in the **Allowed methods or members** column, you can view the following methods to parse the array:

   ```
   [] each find_in_batches first map size to_a
   ```
4. For `Nic::Base`, in the **Allowed methods or members** column, you can view the following method to parse the array:

   ```
   alias? attached_devices attached_devices_identifiers attached_to bond_options children_mac_addresses domain fqdn identifier inheriting_mac ip ip6 link mac managed? mode mtu nic_delay physical? primary provision shortname subnet subnet6 tag virtual? vlanid
   ```
5. To iterate through an interface array, add the relevant methods to the ERB syntax:

   Example input:

   ```
   <% load_hosts().each_record do |host| -%>
   <%    host.interfaces.each do |iface| -%>
     iface.alias?: <%= iface.alias? %>
     iface.attached_to: <%= iface.attached_to %>
     iface.bond_options: <%= iface.bond_options %>
     iface.children_mac_addresses: <%= iface.children_mac_addresses %>
     iface.domain: <%= iface.domain %>
     iface.fqdn: <%= iface.fqdn %>
     iface.identifier: <%= iface.identifier %>
     iface.inheriting_mac: <%= iface.inheriting_mac %>
     iface.ip: <%= iface.ip %>
     iface.ip6: <%= iface.ip6 %>
     iface.link: <%= iface.link %>
     iface.mac: <%= iface.mac %>
     iface.managed?: <%= iface.managed? %>
     iface.mode: <%= iface.mode %>
     iface.mtu: <%= iface.mtu %>
     iface.physical?: <%= iface.physical? %>
     iface.primary: <%= iface.primary %>
     iface.provision: <%= iface.provision %>
     iface.shortname: <%= iface.shortname %>
     iface.subnet: <%= iface.subnet %>
     iface.subnet6: <%= iface.subnet6 %>
     iface.tag: <%= iface.tag %>
     iface.virtual?: <%= iface.virtual? %>
     iface.vlanid: <%= iface.vlanid %>
   <%- end -%>
   ```

   Example rendering:

   ```
   host1.example.com
     iface.alias?: false
     iface.attached_to:
     iface.bond_options:
     iface.children_mac_addresses: []
     iface.domain:
     iface.fqdn: host1.example.com
     iface.identifier: ens192
     iface.inheriting_mac: 00:50:56:8d:4c:cf
     iface.ip: 10.10.181.13
     iface.ip6:
     iface.link: true
     iface.mac: 00:50:56:8d:4c:cf
     iface.managed?: true
     iface.mode: balance-rr
     iface.mtu:
     iface.physical?: true
     iface.primary: true
     iface.provision: true
     iface.shortname: host1.example.com
     iface.subnet:
     iface.subnet6:
     iface.tag:
     iface.virtual?: false
     iface.vlanid:
   ```

## B.12. Example template snippets

Example template snippets show the correct ERB template syntax and common use cases. You can use these snippets as a starting point when writing your own templates.

**Example B.1. Checking if a host has Puppet and Puppetlabs enabled**

The following example checks if the host has the Puppet and Puppetlabs repositories enabled:

```
<%
pm_set = @host.puppetmaster.empty? ? false : true
puppet_enabled = pm_set || host_param_true?('force-puppet')
puppetlabs_enabled = host_param_true?('enable-puppetlabs-repo')
%>
```

**Example B.2. Capturing major and minor versions of a host’s operating system**

The following example shows how to capture the minor and major version of the host’s operating system, which can be used for package related decisions:

```
<%
os_major = @host.operatingsystem.major.to_i
os_minor = @host.operatingsystem.minor.to_i
%>

<% if ((os_minor < 2) && (os_major < 14)) -%>
...
<% end -%>
```

**Example B.3. Importing snippets to a template**

The following example imports the **subscription_manager_registration** snippet to the template and indents it by four spaces:

```
<%= indent 4 do
snippet 'subscription_manager_registration'
end %>
```

**Example B.4. Conditionally importing a Kickstart snippet**

The following example imports the `kickstart_networking_setup` snippet if the host’s subnet has the DHCP boot mode enabled:

```
<% subnet = @host.subnet %>
<% if subnet.respond_to?(:dhcp_boot_mode?) -%>
<%= snippet 'kickstart_networking_setup' %>
<% end -%>
```

**Example B.5. Parsing values from host custom facts**

You can use the `host.facts` variable to parse values from a host’s facts and custom facts. In this example `luks_stat` is a custom fact that you can parse in the same manner as `dmi::system::serial_number`, which is a host fact:

```
'Serial': host.facts['dmi::system::serial_number'],
'Encrypted': host.facts['luks_stat'],
```

In this example, you can customize the Applicable Errata report template to parse for custom information about the kernel version of each host:

```
<%-     report_row(
          'Host': host.name,
          'Operating System': host.operatingsystem,
          'Kernel': host.facts['uname::release'],
          'Environment': host.single_lifecycle_environment ? host.single_lifecycle_environment.name : nil,
          'Erratum': erratum.errata_id,
          'Type': erratum.errata_type,
          'Published': erratum.issued,
          'Applicable since': erratum.created_at,
          'Severity': erratum.severity,
          'Packages': erratum.package_names,
          'CVEs': erratum.cves,
          'Reboot suggested': erratum.reboot_suggested,
        ) -%>
```
