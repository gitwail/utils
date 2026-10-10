---
title: "Creating a complete permission table"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_rest_api"
guide_title: "Using the Satellite REST API"
chapter_number: "B"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#Creating_a_Complete_Permission_Table_rest-api"
---
# Appendix B. Creating a complete permission table

Generate a complete permission table from the Satellite console to review all available permissions and actions on your Satellite.

**Procedure**

1. Start the Satellite console:

   ```
   # foreman-rake console
   ```
2. Insert the following code into the console:

   ```
   f = File.open('/tmp/table.html', 'w')

   result = Foreman::AccessControl.permissions {|a,b| a.security_block <=> b.security_block}.collect do |p|
         actions = p.actions.collect { |a| "<li>#{a}</li>" }
         "<tr><td>#{p.name}</td><td><ul>#{actions.join('')}</ul></td><td>#{p.resource_type}</td></tr>"
   end.join("\n")

   f.write("<table border=\"1\"><tr><td>Permission name</td><td>Actions</td><td>Resource type</td></tr>\n")
   f.write(result)
   f.write("</table>\n")
   ```

   The above syntax creates a table of permissions and saves it to the `/tmp/table.html` file.
3. Press `Ctrl` + `D` to exit the Satellite console.
4. Open `/tmp/table.html` in a web browser to view the table.
