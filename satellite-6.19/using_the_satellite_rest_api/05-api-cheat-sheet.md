---
title: "API cheat sheet"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_rest_api"
guide_title: "Using the Satellite REST API"
chapter_number: "5"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#api-cheat-sheet"
---
# Chapter 5. API cheat sheet

Use the Red Hat Satellite API to automate host management, lifecycle environments, content uploads, and searches.

You can use the API on Satellite Server via HTTPS on port 443.

For example, in Ruby, you can specify the Satellite Server URL as follows:

```
url = 'https://satellite.example.com/api/v2/'
katello_url = 'https://satellite.example.com/katello/api/v2/'
```

You can use these values to fully automate your scripts, removing any need to verify which ports to use.

The following examples use `curl` for sending API requests.

## 5.1. Working with hosts

You can use API requests to manage hosts. Namely, you can list, query, search, and delete hosts programmatically.

### 5.1.1. Listing hosts

You can retrieve a list of all registered hosts from Satellite.

This example returns a list of registered hosts.

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/v2/hosts \
    | python3 -m json.tool
    ```

API response
:   ```
    {
          ...
           "total" => 2,
        "subtotal" => 2,
            "page" => 1,
        "per_page" => 1000,
          "search" => nil,
            "sort" => {
               "by" => nil,
            "order" => nil
        },
         "results" => [
          ...
    }
    ```

### 5.1.2. Requesting information for a host

You can retrieve detailed information about a specific host, including architecture, build status, and capabilities.

This request returns information for `host.example.com`.

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/v2/hosts/host.example.com \
    | python3 -m json.tool
    ```

Example API response
:   ```
    {
        "all_puppetclasses": [],
        "architecture_id": 1,
        "architecture_name": "x86_64",
        "build": false,
        "capabilities": [
            "build"
        ],
        "certname": "host.example.com",
        "comment": null,
        "compute_profile_id": null,
        ...
    }
    ```

### 5.1.3. Listing host facts

You can retrieve system facts such as hardware details, BIOS version, and installed software for a specific host.

This request returns all facts for the host `satellite.example.com`.

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/v2/hosts/satellite.example.com/facts \
    | python3 -m json.tool
    ```

Example API response
:   ```
    {
        ...
        "results": {
            "satellite.example.com": {
                "augeasversion": "1.0.0",
                "bios_release_date": "01/01/2007",
                "bios_version": "0.5.1",
                "blockdevice_sr0_size": "1073741312",
                "facterversion": "1.7.6",
                ...
    }
    ```

### 5.1.4. Searching for hosts with matching patterns

You can filter hosts by hostname patterns or other matching criteria.

This query returns all hosts that match the pattern "example".

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/v2/hosts?search=example \
    | python3 -m json.tool
    ```

Example API response
:   ```
    {
        ...
        "results": [
            {
                "name": "satellite.example.com",
                ...
            }
        ],
        "search": "example",
        ...
    }
    ```

### 5.1.5. Searching for hosts in an environment

You can filter hosts by environment to retrieve all hosts assigned to a specific environment.

This query returns all hosts in the `production` environment.

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/v2/hosts?search=environment=production \
    | python3 -m json.tool
    ```

Example API response
:   ```
    {
        ...
        "results": [
            {
                "environment_name": "production",
                "name": "satellite.example.com",
                ...
            }
        ],
        "search": "environment=production",
        ...
    }
    ```

### 5.1.6. Searching for hosts with a specific fact value

You can filter hosts by specific fact values such as host group, operating system, or custom facts.

This query returns all hosts with the host group `My Host Group`.

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/v2/hosts?search=hostgroup=%22My+Host+Group%22 \
    | python3 -m json.tool
    ```

Example API response
:   ```
    {
        ...
        "results": [
            {
                ...
                "hostgroup_id": 1,
                "hostgroup_name": "My Host Group",
                "name": "my-host.example.com",
                ...
            }
        ],
        "search": "hostgroup=\"My Host Group\"",
        ...
    }
    ```

### 5.1.7. Deleting a host

You can permanently remove a host from Satellite when decommissioning a server, reclaiming software subscriptions, or clearing out stale inventory data to maintain accurate compliance reporting.

This example request deletes a host with a name *host1.example.com*.

Example API request
:   ```
    $ curl \
    --request DELETE \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/v2/hosts/host1.example.com \
    | python3 -m json.tool
    ```

### 5.1.8. Downloading a full-host boot disk image

You can download a bootable ISO image for a host to handle provisioning or recovery scenarios.

This request downloads a full boot disk image for a host by its ID.

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    --output My_Image.iso \
    https://satellite.example.com/api/bootdisk/hosts/host_ID?full=true
    ```

## 5.2. Working with lifecycle environments

Lifecycle environments represent stages in your application life cycle such as development, testing, and production, enabling controlled content promotion through linked lifecycle environment paths.

To create linked lifecycle environments with the API, use the `prior_id` parameter.

You can find the built-in API reference for lifecycle environments at `https://satellite.example.com/apidoc/v2/lifecycle_environments.html`. The API routes include `/katello/api/environments` and `/katello/api/organizations/:organization_id/environments`.

### 5.2.1. Listing lifecycle environments

You can retrieve all lifecycle environments for an organization to view your content promotion paths.

Example API request
:   ```
    $ curl \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/katello/api/organizations/1/environments \
    | python3 -m json.tool`
    ```

Example API response
:   ```
          output omitted
       "description": null,
       "id": 1,
       "label": "Library",
       "library": true,
       "name": "Library",
       "organization": {
            "id": 1,
            "label": "Default_Organization",
            "name": "Default Organization"
       },
       "permissions": {
           "destroy_lifecycle_environments": false,
           "edit_lifecycle_environments": true,
           "promote_or_remove_content_views_to_environments": true,
           "view_lifecycle_environments": true
       },
       "prior": null,
       "successor": null,
       output truncated
    ```

### 5.2.2. Creating linked lifecycle environments

Create a linked path of lifecycle environments to establish a controlled content promotion workflow from development through testing to production stages.

This procedure uses the default Library environment with ID `1` as the starting point for creating lifecycle environments.

**Procedure**

1. Choose an existing lifecycle environment that you want to use as a starting point. List the environment by using its ID. In this case, the environment with ID `1`:

   Example request:

   ```
   $ curl \
   --request GET \
   --user My_User_Name:My_Password \
   https://satellite.example.com/katello/api/environments/1 \
   | python3 -m json.tool
   ```

   Example response:

   ```
     output omitted
      "id": 1,
      "label": "Library",
   	output omitted
       "prior": null,
       "successor": null,
     output truncated
   ```
2. Create a JSON file, for example, `life-cycle.json`, with the following content:

   ```
   {"organization_id":1,"label":"api-dev","name":"API Development","prior":1}
   ```
3. Create a lifecycle environment by using the `prior` option set to `1`.

   Example request:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request POST \
   --user My_User_Name:My_Password \
   --data @life-cycle.json \
   https://satellite.example.com/katello/api/environments \
   | python3 -m json.tool
   ```

   Example response:

   ```
         output omitted
       "description": null,
       "id": 2,
       "label": "api-dev",
       "library": false,
       "name": "API Development",
       "organization": {
           "id": 1,
           "label": "Default_Organization",
           "name": "Default Organization"
       },
       "permissions": {
           "destroy_lifecycle_environments": true,
           "edit_lifecycle_environments": true,
           "promote_or_remove_content_views_to_environments": true,
           "view_lifecycle_environments": true
       },
      "prior": {
           "id": 1,
           "name": "Library"
       },
       output truncated
   ```

   In the command output, you can see the ID for this lifecycle environment is `2`, and the lifecycle environment before this one is `1`. Use the lifecycle environment with ID `2` to create a successor to this environment.
4. Edit the previously created `life-cycle.json` file to update the `label`, `name`, and `prior` values.

   ```
   {"organization_id":1,"label":"api-qa","name":"API QA","prior":2}
   ```
5. Create a lifecycle environment using the `prior` option set to `2`.

   Example request:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request POST \
   --user My_User_Name:My_Password \
   --data @life-cycle.json \
   https://satellite.example.com/katello/api/environments \
   | python3 -m json.tool
   ```

   Example response:

   ```
         output omitted
      "description": null,
      "id": 3,
       "label": "api-qa",
       "library": false,
       "name": "API QA",
       "organization": {
           "id": 1,
           "label": "Default_Organization",
           "name": "Default Organization"
       },
       "permissions": {
           "destroy_lifecycle_environments": true,
           "edit_lifecycle_environments": true,
           "promote_or_remove_content_views_to_environments": true,
           "view_lifecycle_environments": true
       },
      "prior": {
           "id": 2,
           "name": "API Development"
       },
       "successor": null,
       output truncated
   ```

   In the command output, you can see the ID for this lifecycle environment is `3`, and the lifecycle environment before this one is `2`.

### 5.2.3. Updating a lifecycle environment

You can modify lifecycle environment attributes such as name or description using a PUT request.

This example request updates a description of the lifecycle environment with ID `3`.

Example API request
:   ```
    $ curl \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --request PUT \
    --user My_User_Name:My_Password \
    --data '{"description":"Quality Acceptance Testing"}' \
    https://satellite.example.com/katello/api/environments/3 \
    | python3 -m json.tool
    ```

Example API response
:   ```
          output omitted
        "description": "Quality Acceptance Testing",
        "id": 3,
        "label": "api-qa",
        "library": false,
        "name": "API QA",
        "organization": {
            "id": 1,
            "label": "Default_Organization",
            "name": "Default Organization"
        },
        "permissions": {
            "destroy_lifecycle_environments": true,
            "edit_lifecycle_environments": true,
            "promote_or_remove_content_views_to_environments": true,
            "view_lifecycle_environments": true
        },
        "prior": {
            "id": 2,
            "name": "API Development"
        },
        output truncated
    ```

### 5.2.4. Deleting a lifecycle environment

You can remove lifecycle environments that have no successors to clear unused promotion paths.

When deleting lifecycle environments, delete them in reverse order.

Example API request
:   ```
    $ curl \
    --request DELETE \
    --user My_User_Name:My_Password \
    https://satellite.example.com/katello/api/environments/:id
    ```

## 5.3. Uploading Content to Satellite Server

You can upload and import files up to 2 MB to custom repositories on Satellite, automate content management for packages, scripts, and other repository artifacts.

This process involves the following steps:

1. Create an upload request.
2. Upload the content.
3. Import the content.
4. Delete the upload request.

The maximum file size that you can upload is 2 MB. For information about uploading larger content, see [Section 5.3.1, “Uploading content larger than 2 MB”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#uploading-content-larger-than-2-mb "5.3.1. Uploading content larger than 2 MB").

**Procedure**

1. Assign the package name to the variable `name`:

   Example request:

   ```
   $ export name=jq-1.6-2.el7.x86_64.rpm
   ```
2. Assign the checksum of the file to the variable `checksum`:

   Example request:

   ```
   $ export checksum=$(sha256sum $name|cut -c 1-65)
   ```
3. Assign the file size to the variable `size`:

   Example request:

   ```
   $ export size=$(du -bs $name|cut -f 1)
   ```
4. Create an upload request that returns the upload ID of the request by using `size` and `checksum`.

   Example request:

   ```
   $ curl \
   --header 'Content-Type: application/json' \
   --request POST \
   --user My_User_Name:My_Password \
   --data "{\"size\": \"$size\", \"checksum\":\"$checksum\"}" \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads
   ```

   where 76, in this case, is an example Repository ID.

   Example request:

   ```
   {"upload_id":"37eb5900-597e-4ac3-9bc5-2250c302fdc4"}
   ```
5. Assign the upload ID to the variable `upload_id`:

   ```
   $ export upload_id=37eb5900-597e-4ac3-9bc5-2250c302fdc4
   ```
6. Assign the path of the package you want to upload to the variable `path`:

   ```
   $ export path=/root/jq/jq-1.6-2.el7.x86_64.rpm
   ```
7. Upload your content. Ensure you use the correct MIME type when you upload data. The API uses the `application/json` MIME type for the requests to Satellite unless stated otherwise. Combine the upload ID, MIME type, and other parameters to upload content.

   Example request:

   ```
   $ curl \
   --user My_User_Name:My_Password \
   --header Accept:application/json \
   --header Content-Type:multipart/form-data \
   --request PUT \
   --data-urlencode size=$size \
   --data-urlencode offset=0 \
   --data-urlencode content@${path} \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads/$upload_id
   ```
8. After you have uploaded the content to your Satellite Server, you need to import it into the appropriate repository. Until you complete this step, Satellite Server does not detect the new content.

   Example request:

   ```
   $ curl \
   --header "Content-Type: application/json" \
   --request PUT \
   --user My_User_Name:My_Password \
   --data "{\"uploads\":[{\"id\": \"$upload_id\", \"name\": \"$name\", \"checksum\": \"$checksum\" }]}" \
   https://satellite.example.com/katello/api/v2/repositories/76/import_uploads
   ```
9. After you have successfully uploaded and imported your content, you can delete the upload request. This frees any temporary disk space that data is using during the upload.

   Example request:

   ```
   $ curl \
   --header 'Content-Type: application/json' \
   --request DELETE \
   --user My_User_Name:My_Password \
   --data "{}" \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads/$upload_id
   ```

### 5.3.1. Uploading content larger than 2 MB

To upload packages and ISO images that are larger than 2 MB, split them into smaller chunks before uploading each piece to repositories in Satellite sequentially.

Note that this example uses sample content, host names, user names, repository ID, and file names.

**Procedure**

1. Assign the package name to the variable `name`:

   ```
   $ export name=bpftool-3.10.0-1160.2.1.el7.centos.plus.x86_64.rpm
   ```
2. Assign the checksum of the file to the variable `checksum`:

   ```
   $ export checksum=$(sha256sum $name|cut -c 1-65)
   ```
3. Assign the file size to the variable `size`:

   ```
   $ export size=$(du -bs $name|cut -f 1)
   ```
4. The following command creates a new upload request and returns the upload ID of the request using `size` and `checksum`.

   Example request:

   ```
   $ curl \
   --header 'Content-Type: application/json' \
   --request POST \
   --user My_User_Name:My_Password \
   --data "{\"size\": \"$size\", \"checksum\":\"$checksum\"}" \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads
   ```

   where 76, in this case, is an example Repository ID.

   Example output

   ```
   {"upload_id":"37eb5900-597e-4ac3-9bc5-2250c302fdc4"}
   ```
5. Assign the upload ID to the variable `upload_id`:

   ```
   $ export upload_id=37eb5900-597e-4ac3-9bc5-2250c302fdc4
   ```
6. Split the file in 2MB chunks:

   ```
   $ split \
   --bytes 2MB \
   --numeric-suffixes \
   --suffix-length=1 \
   bpftool-3.10.0-1160.2.1.el7.centos.plus.x86_64.rpm bpftool
   ```

   View the file chunks:

   ```
   $ ls -l bpftool[0-9]
   ```

   Example output:

   ```
   -rw-r--r--. 1 root root 2000000 Mar 31 14:15 bpftool0
   -rw-r--r--. 1 root root 2000000 Mar 31 14:15 bpftool1
   -rw-r--r--. 1 root root 2000000 Mar 31 14:15 bpftool2
   -rw-r--r--. 1 root root 2000000 Mar 31 14:15 bpftool3
   -rw-r--r--. 1 root root  868648 Mar 31 14:15 bpftool4
   ```
7. Assign the prefix of the split files to the variable path.

   ```
   $ export path=/root/tmp/bpftool
   ```
8. Upload the file chunks. The offset starts at 0 bytes for the first chunk and increases by 2000000 bytes for each file. Note the use of the offset parameter and how it relates to the file size. Note also that the indexes are used after the path variable, for example, ${path}0, ${path}1.

   Example requests:

   ```
   $ curl \
   --user My_User_Name:My_Password \
   --header Accept:application/json \
   --header Content-Type:multipart/form-data \
   --request PUT \
   --data-urlencode size=$size \
   --data-urlencode offset=0 \
   --data-urlencode content@${path}0 \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads/$upload_id

   $ curl \
   --user My_User_Name:My_Password \
   --header Accept:application/json \
   --header Content-Type:multipart/form-data \
   --request PUT \
   --data-urlencode size=$size \
   --data-urlencode offset=2000000 \
   --data-urlencode content@${path}1 \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads/$upload_id

   $ curl \
   --user My_User_Name:My_Password \
   --header Accept:application/json \
   --header Content-Type:multipart/form-data \
   --request PUT \
   --data-urlencode size=$size \
   --data-urlencode offset=4000000 \
   --data-urlencode content@${path}2 \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads/$upload_id

   $ curl \
   --user My_User_Name:My_Password \
   --header Accept:application/json \
   --header Content-Type:multipart/form-data \
   --request PUT \
   --data-urlencode size=$size \
   --data-urlencode offset=6000000
   --data-urlencode content@${path}3 \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads/$upload_id

   $ curl \
   --user My_User_Name:My_Password \
   --header Accept:application/json \
   --header Content-Type:multipart/form-data \
   --request PUT \
   --data-urlencode size=$size \
   --data-urlencode offset=8000000 \
   --data-urlencode content@${path}4 \
   https://satellite.example.com/katello/api/v2/repositories/76/content_uploads/$upload_id
   ```
9. Import the complete upload to the repository:

   ```
   $ curl \
   --header "Content-Type: application/json" \
   --request PUT \
   --user My_User_Name:My_Password \
   --data "{\"uploads\":[{\"id\": \"$upload_id\", \"name\": \"$name\", \"checksum\": \"$checksum\" }]}" \
   https://satellite.example.com/katello/api/v2/repositories/76/import_uploads
   ```
10. Delete the upload request:

    ```
    $ curl \
    --header 'Content-Type: application/json' \
    --request DELETE \
    --user My_User_Name:My_Password \
    --data "{}" \
    https://satellite.example.com/katello/api/v2/repositories/76/content_uploads/$upload_id
    ```

### 5.3.2. Uploading duplicate content

Reuse existing content when uploading files with matching checksums to save storage space and transfer time.

**Procedure**

- Upload content to Satellite:

  ```
  $ curl \
  --header 'Content-Type: application/json' \
  --request POST \
  --user My_User_Name:My_Password \
  --data "{\"size\": \"$size\", \"checksum\":\"$checksum\"}" \
  https://satellite.example.com/katello/api/v2/repositories/76/content_uploads
  ```

  The call will return a content unit ID instead of an upload ID, similar to this:

  ```
  {"content_unit_href":"/pulp/api/v3/content/file/files/c1bcdfb8-d840-4604-845e-86e82454c747/"}
  ```

  You can copy this output and call import uploads directly to add the content to a repository.

  Example API response:

  ```
  $ curl \
  --header "Content-Type: application/json" \
  --request PUT \
  --user My_User_Name:My_Password \
  --data "{\"uploads\":[{\"content_unit_id\": \"/pulp/api/v3/content/file/files/c1bcdfb8-d840-4604-845e-86e82454c747/\", \"name\": \"$name\", \ \"checksum\": \"$checksum\" }]}" \
  https://satellite.example.com/katello/api/v2/repositories/76/import_uploads
  ```

  Note that the call changes from using `upload_id` to using `content_unit_id`.

## 5.4. Using extended searches

You can combine search parameters in your API queries to filter hosts. This way you can target specific hosts by their operating system or hardware model.

For more information, see [Working efficiently with Satellite web UI](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui) in *Administering Red Hat Satellite*.

For example, you can search for hosts.

**Procedure**

1. In the Satellite web UI, navigate to **Hosts** > **All Hosts**.
2. Click the **Search** field to display a list of search parameters.
3. Locate the search parameters that you want to use. For this example, locate **os_title** and **model**.
4. Combine the search parameters in your API query as follows:

   Example request:

   ```
   $ curl \
   --user My_User_Name:My_Password \
   https://satellite.example.com/api/v2/hosts?search=os_title=\"RedHat+7.7\",model=\"PowerEdge+R330\" \
   | python3 -m json.tool
   ```

   Example response:

   ```
     {
       ...
       "results": [
           {
               "model_id": 1,
               "model_name": "PowerEdge R330",
               "name": "satellite.example.com",
               "operatingsystem_id": 1,
               "operatingsystem_name": "RedHat 7.7",
               ...
           }
       ],
       "search": "os_title=\"RedHat 7.7\",model=\"PowerEdge R330\"",
       "subtotal": 1,
       "total": 11
   }
   ```

## 5.5. Using searches with pagination control

You can control how many results an API query returns per page and which page to retrieve in order to manage large datasets efficiently.

The `per_page` parameter specifies the number of results per page and the `page` parameter specifies which page, as calculated by the `per_page` parameter, to return.

The number of items to be presented is set using the setting `entries_per_page`, which defaults to `20`. However, you can change it per request by using the parameter `per_page`.

This example returns a list of architectures for an organization with ID `1` in pages. The list contains 5 entries per page and returns the second page.

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/katello/api/architectures?organization_id=1&amp;per_page=5&amp;page=2
    ```

### 5.5.1. Returning multiple pages

You can iterate through multiple pages of API results to retrieve complete datasets when the total number of items exceeds the per-page limit.

Bash script
:   ```bash
    $ for i in seq 1 3; do \
      curl \
      --request GET \
      --user My_User_Name:My_Password \
      https://satellite.example.com/katello/api/content_views?per_page=5&amp;page=$i; \
    done
    ```

## 5.6. Overriding Smart Class parameters

You can override Smart Class parameters to customize Puppet configuration values for specific hosts or host groups. This way you customize different environments without changing the original Puppet classes.

You can find the full list of attributes that you can modify in the built-in API reference at `https://satellite.example.com/apidoc/v2/smart_class_parameters/update.html`.

**Procedure**

1. Find the ID of the Smart Class parameter you want to change:

   - List all Smart Class Parameters.

     Example request:

     ```
     $ curl \
     --request GET \
     --user My_User_Name:My_Password \
     https://satellite.example.com/api/smart_class_parameters
     ```
   - If you know the Puppet class ID, for example 5, you can restrict the scope: Example request:

     ```
     $ curl \
     --request GET \
     --user My_User_Name:My_Password \
     https://satellite.example.com/api/puppetclasses/5/smart_class_parameters
     ```

     Both calls accept a search parameter. You can view the full list of searchable fields in the Satellite web UI. Navigate to **Configure** > **Smart variables** and click in the search query box to reveal the list of fields.

     Two particularly useful search parameters are `puppetclass_name` and `key`, which you can use to search for a specific parameter. For example, use the `--data` option to pass URL encoded data.

     Example request:

     ```
     $ curl \
     --request GET \
     --user My_User_Name:My_Password \
     --data 'search=puppetclass_name = access_insights_client and key = authmethod' \
     https://satellite.example.com/api/smart_class_parameters
     ```

     Satellite supports standard scoped-search syntax.
2. When you find the ID of the parameter, list the full details including current override values.

   Example request:

   ```
   $ curl \
   --request GET \
   --user My_User_Name:My_Password \
   https://satellite.example.com/api/smart_class_parameters/63
   ```
3. Enable overriding of parameter values.

   Example request:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request PUT \
   --user My_User_Name:My_Password \
   --data '{"smart_class_parameter":{"override":true}}' \
   https://satellite.example.com/api/smart_class_parameters/63
   ```

   Note that you cannot create or delete the parameters manually. You can only modify their attributes. Satellite creates and deletes parameters only upon class import from Capsules.
4. Add custom override matchers.

   Example request:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request PUT \
   --user My_User_Name:My_Password \
   --data '{"smart_class_parameter":{"override_value":{"match":"hostgroup=Test","value":"2.4.6"}}}' \
   https://satellite.example.com/api/smart_class_parameters/63
   ```

   For more information about override values, see `https://satellite.example.com/apidoc/v2/override_values.html`.
5. You can delete override values.

   Example request:

   ```
   $ curl \
   --request DELETE \
   --user My_User_Name:My_Password \
   https://satellite.example.com/api/smart_class_parameters/63/override_values/3
   ```

## 5.7. Modifying a Smart Class parameter by using an external file

You can modify Puppet Smart Class parameters by using external JSON files to simplify working with complex parameter values. That way, you can enable syntax highlighting and error detection in your editor.

This example uses a MOTD Puppet manifest.

**Procedure**

1. Search for the Puppet Class by name, `motd` in this case.

   Example request:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request GET \
   --user My_User_Name:My_Password \
   https://satellite.example.com/api/smart_class_parameters?search=puppetclass_name=motd \
   | python3 -m json.tool
   ```
2. Examine the following output. Each Smart Class Parameter has an ID that is global for the same Satellite instance. The `content` parameter of the `motd` class has `id=3`. Do not confuse this with the Puppet Class ID that displays before the Puppet Class name.

   Example response:

   ```
   {
   	"avoid_duplicates": false,
   		"created_at": "2024-02-06 12:37:48 UTC", # Remove this line.
   			"default_value": "", # Add a new value here.
   			"description": "",
   		"hidden_value": "",
   		"hidden_value?": false,
   		"id": 3,
   		"merge_default": false,
   		"merge_overrides": false,
   		"override": false, # Set the override value to true.
   			"override_value_order": "fqdn\nhostgroup\nos\ndomain",
   		"override_values": [], # Remove this line.
   			"override_values_count": 0,
   		"parameter": "content",
   		"parameter_type": "string",
   		"puppetclass_id": 3,
   		"puppetclass_name": "motd",
   		"required": false,
   		"updated_at": "2024-02-07 11:56:55 UTC", # Remove this line.
   			"use_puppet_default": false,
   		"validator_rule": null,
   		"validator_type": ""
   }
   ```
3. Use the parameter ID `3` to get the information specific to the `motd` parameter and redirect the output to a file, for example, **output_file.json**.

   Example request:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request GET \
   --user My_User_Name:My_Password \
   https://satellite.example.com/api/smart_class_parameters/3 \
   | python3 -m json.tool > output_file.json
   ```
4. Copy the file created in the previous step to a new file for editing, for example, `changed_file.json`:

   ```
   $ cp output_file.json changed_file.json
   ```
5. Modify the required values in the file. In this example, change the content parameter of the `motd` module, which requires changing the `override` option from `false` to `true`:

   ```
   {
   	"avoid_duplicates": false,
   		"created_at": "2024-02-06 12:37:48 UTC", # Remove this line.
   			"default_value": "", # Add a new value here.
   			"description": "",
   		"hidden_value": "",
   		"hidden_value?": false,
   		"id": 3,
   		"merge_default": false,
   		"merge_overrides": false,
   		"override": false, # Set the override value to true.
   			"override_value_order": "fqdn\nhostgroup\nos\ndomain",
   		"override_values": [], # Remove this line.
   			"override_values_count": 0,
   		"parameter": "content",
   		"parameter_type": "string",
   		"puppetclass_id": 3,
   		"puppetclass_name": "motd",
   		"required": false,
   		"updated_at": "2024-02-07 11:56:55 UTC", # Remove this line.
   			"use_puppet_default": false,
   		"validator_rule": null,
   		"validator_type": ""
   }
   ```
6. After editing the file, verify that it looks as follows and then save the changes:

   ```
   {
   	"avoid_duplicates": false,
   		"default_value": "No Unauthorized Access Allowed",
   			"description": "",
   		"hidden_value": "",
   		"hidden_value?": false,
   		"id": 3,
   		"merge_default": false,
   		"merge_overrides": false,
   		"override": true,
   			"override_value_order": "fqdn\nhostgroup\nos\ndomain",
   		"override_values_count": 0,
   		"parameter": "content",
   		"parameter_type": "string",
   		"puppetclass_id": 3,
   		"puppetclass_name": "motd",
   		"required": false,
   		"use_puppet_default": false,
   		"validator_rule": null,
   		"validator_type": ""
   }
   ```
7. Submit the file to Satellite:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request PUT \
   --user My_User_Name:My_Password \
   --data @changed_file.json \
   https://satellite.example.com/api/smart_class_parameters/3
   ```

## 5.8. Deleting OpenSCAP reports

Delete OpenSCAP compliance reports to free up storage space or remove outdated scan results, either individually by ID or in bulk using a bash script for large-scale cleanup.

**Procedure**

1. List all OpenSCAP reports. Note the IDs of the reports that you want to delete.

   Example request:

   ```
   $ curl \
   --user My_User_Name:My_Password \
   https://satellite.example.com/api/v2/compliance/arf_reports/ \
   | python3 -m json.tool
   ```

   Example response:

   ```
   {
       "page": 1,
       "per_page": 20,
       "results": [
           {
               "created_at": "2024-05-16 13:27:09 UTC",
               "failed": 0,
               "host": "host1.example.com",
               "id": 404,
               "othered": 0,
               "passed": 0,
               "updated_at": "2024-05-16 13:27:09 UTC"
           },
           {
               "created_at": "2024-05-16 13:26:07 UTC",
               "failed": 0,
               "host": "host2.example.com,
               "id": 405,
               "othered": 0,
               "passed": 0,
               "updated_at": "2024-05-16 13:26:07 UTC"
           },
           {
               "created_at": "2024-05-16 13:25:07 UTC",
               "failed": 0,
               "host": "host3.example.com",
               "id": 406,
               "othered": 0,
               "passed": 0,
               "updated_at": "2024-05-16 13:25:07 UTC"
           },
           {
               "created_at": "2024-05-16 13:24:07 UTC",
               "failed": 0,
               "host": "host4.example.com",
               "id": 407,
               "othered": 0,
               "passed": 0,
               "updated_at": "2024-05-16 13:24:07 UTC"
           },
       ],
       "search": null,
       "sort": {
           "by": null,
           "order": null
       },
       "subtotal": 29,
       "total": 29
   ```
2. Using an ID from the previous step, delete the OpenSCAP report. Repeat for each ID that you want to delete.

   Example request:

   ```
   $ curl \
   --user My_User_Name:My_Password \
   --header "Content-Type: application/json" \
   --request DELETE \
   https://satellite.example.com/api/v2/compliance/arf_reports/405
   ```

   Example response:

   ```
   HTTP/1.1 200 OK
   Date: Thu, 18 May 2024 07:14:36 GMT
   Server: Apache/2.4.6 (Red Hat Enterprise Linux)
   X-Frame-Options: SAMEORIGIN
   X-XSS-Protection: 1; mode=block
   X-Content-Type-Options: nosniff
   Foreman_version: 3.11.0.76
   Foreman_api_version: 2
   Apipie-Checksum: 2d39dc59aed19120d2359f7515e10d76
   Cache-Control: max-age=0, private, must-revalidate
   X-Request-Id: f47eb877-35c7-41fe-b866-34274b56c506
   X-Runtime: 0.661831
   X-Powered-By: Phusion Passenger 4.0.18
   Set-Cookie: request_method=DELETE; path=/
   Set-Cookie: _session_id=d58fe2649e6788b87f46eabf8a461edd; path=/; secure; HttpOnly
   ETag: "2574955fc0afc47cb5394ce95553f428"
   Status: 200 OK
   Vary: Accept-Encoding
   Transfer-Encoding: chunked
   Content-Type: application/json; charset=utf-8
   ```

**Example 5.1. Example BASH script to delete all OpenSCAP reports**

```bash
#!/bin/bash

# this script removes all ARF reports from your Satellite Server

# settings
USER="My_User_Name"
PASS="My_Password"
URI="https://satellite.example.com"

# check amount of reports
 while [ $(curl --user $USER:$PASS $URI/api/v2/compliance/arf_reports/ | python3 -m json.tool | grep \"\total\": | cut --fields=2 --delimiter":" | cut --fields=1 --delimiter"," | sed "s/ //g") -gt 0 ]; do

# fetch reports
 for i in $(curl --user $USER:$PASS $URI/api/v2/compliance/arf_reports/ | python3 -m json.tool | grep \"\id\": | cut --fields=2 --delimiter":" | cut --fields=1 --delimiter"," | sed "s/ //g")

# delete reports
  do
  curl --user $USER:$PASS --header "Content-Type: application/json" --request DELETE $URI/api/v2/compliance/arf_reports/$i
  done
done
```
