---
title: "API syntax"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_rest_api"
guide_title: "Using the Satellite REST API"
chapter_number: "2"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#api-syntax"
---
# Chapter 2. API syntax

Understanding the basic syntax of API requests and JSON responses enables you to construct valid API calls and interpret the returned data.

> **Important**
>
> Even though versions 1 and 2 of the Satellite 6 API are available, Red Hat only supports version 2.

## 2.1. API request composition

You can use the built-in API reference documentation to compose valid API requests.

This example shows how to compose a `curl` API request.

The built-in API reference shows the API route, or path, preceded by an HTTP method:

```
HTTP_METHOD API_ROUTE
```

To work with the API, construct a command by using the `curl` command syntax and the API route from the reference document:

```
$ curl \
--data @My_Input_File.json \
--header "Accept: application/json" \
--header "Content-Type: application/json" \
--output My_Output_File
--request HTTP_METHOD \
--user "My_User_Name:My_Password" \
API_ROUTE \
| python3 -m json.tool
```

`--data`
:   For `POST` and `PUT` requests, use the `--data` option to pass JSON-formatted data.

`--header`
:   When passing the JSON data with the `--data` option, you must specify the following headers with the `--header` option.

`--output`
:   When downloading content from Satellite Server, specify the output file with the `--output` option.

`--request`
:   To use `curl` for the API call, specify an HTTP method with the `--request` option. For example, `--request POST`.

`--user`
:   Provide Satellite user credentials with the `--user` option.

`API_ROUTE`
:   Use the API route in the following format: `\https://satellite.example.com/api/architectures`. In Satellite 6, version 2 of the API is the default. Therefore, it is not necessary to use `v2` in the URL for API calls.

`json.tool`
:   Redirect the output to the Python `json.tool` module to make the output easier to read.

**Additional resources**

- [Section 4.1.1, “Passing JSON data to the API request”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#passing-json-data-to-the-api-request "4.1.1. Passing JSON data to the API request")

### 2.1.1. Using the GET HTTP method

Use the GET HTTP method to get data from the API about an existing entry or resource. This example requests the number of registered hosts.

**Procedure**

- Submit a GET request by using `curl`.

  Example API request:

  ```
  $ curl \
  --request GET \
  --user My_User_Name:My_Password \
  https://satellite.example.com/api/hosts \
  | python3 -m json.tool
  ```

  Example API response:

  ```
  {
    "total": 2,
    "subtotal": 2,
    "page": 1,
    "per_page": 20,
    "search": null,
    "sort": {
      "by": null,
      "order": null
    },
    "results":
      output truncated
  }
  ```

  The response from the API indicates that there are two results in total, this is the first page of the results, and the maximum results per page is set to 20. For more information, see [Section 2.2, “JSON response format”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#json-response-format "2.2. JSON response format").

### 2.1.2. Using the POST HTTP method

Use the POST HTTP method to create new resources such as activation keys or hosts.

You must submit the data in JSON format. For more information, see [Section 4.1.1, “Passing JSON data to the API request”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#passing-json-data-to-the-api-request "4.1.1. Passing JSON data to the API request").

**Procedure**

1. Create a test file, for example, `activation-key.json`, with the following content:

   ```
   {"organization_id":1, "name":"TestKey", "description":"Just for testing"}
   ```
2. Create an activation key by applying the data in the `activation-key.json` file.

   Example API request:

   ```
   $ curl \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --request POST \
   --user My_User_Name:My_Password \
   --data @activation-key.json \
   https://satellite.example.com/katello/api/activation_keys \
   | python3 -m json.tool
   ```

   Example API response:

   ```
   {
       "id": 2,
       "name": "TestKey",
       "description": "Just for testing",
       "unlimited_hosts": true,
       "auto_attach": true,
       "content_view_id": null,
       "environment_id": null,
       "usage_count": 0,
       "user_id": 3,
       "max_hosts": null,
       "release_version": null,
       "service_level": null,
       "content_overrides": [

       ],
       "organization": {
           "name": "Default Organization",
           "label": "Default_Organization",
           "id": 1
       },
       "created_at": "2024-02-16 12:37:47 UTC",
       "updated_at": "2024-02-16 12:37:48 UTC",
       "content_view": null,
       "environment": null,
       "products": null,
       "host_collections": [

       ],
       "permissions": {
           "view_activation_keys": true,
           "edit_activation_keys": true,
           "destroy_activation_keys": true
       }
   }
   ```

**Verification**

- In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Activation Keys** to view your activation keys.

### 2.1.3. Using the PUT HTTP method

Use the PUT HTTP method to update existing resources such as changing activation key properties or host configurations.

You must submit the data in JSON format. For more information, see [Section 4.1.1, “Passing JSON data to the API request”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#passing-json-data-to-the-api-request "4.1.1. Passing JSON data to the API request").

**Procedure**

1. Edit the `activation-key.json` file created previously as follows:

   ```
   {"organization_id":1, "name":"TestKey", "description":"Just for testing","max_hosts":"10" }
   ```
2. Apply the changes in the JSON file.

   Example API request:

   ```
   $ curl \
   --request PUT \
   --header "Accept: application/json" \
   --header "Content-Type: application/json" \
   --user My_User_Name:My_Password \
   --data @activation-key.json \
   https://satellite.example.com/katello/api/activation_keys/2 \
   | python3 -m json.tool
   ```

   Example API response:

   ```
   {
       "id": 2,
       "name": "TestKey",
       "description": "Just for testing",
       "unlimited_hosts": false,
       "auto_attach": true,
       "content_view_id": null,
       "environment_id": null,
       "usage_count": 0,
       "user_id": 3,
       "max_hosts": 10,
       "release_version": null,
       "service_level": null,
       "content_overrides": [

       ],
       "organization": {
           "name": "Default Organization",
           "label": "Default_Organization",
           "id": 1
       },
       "created_at": "2024-02-16 12:37:47 UTC",
       "updated_at": "2024-02-16 12:46:17 UTC",
       "content_view": null,
       "environment": null,
       "products": null,
       "host_collections": [

       ],
       "permissions": {
           "view_activation_keys": true,
           "edit_activation_keys": true,
           "destroy_activation_keys": true
       }
   }
   ```

**Verification**

- In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Activation Keys** to view the updated activation keys.

### 2.1.4. Using the DELETE HTTP method

Use the DELETE HTTP method with an API route to permanently remove resources such as activation keys or hosts from Satellite.

This example deletes the `TestKey` activation key, whose ID is 2.

**Procedure**

- Submit a DELETE request by using `curl`.

  Example API request:

  ```
  $ curl \
  --header "Accept: application/json" \
  --header "Content-Type: application/json" \
  --request DELETE \
  --user My_User_Name:My_Password \
  https://satellite.example.com/katello/api/activation_keys/2 \
  | python3 -m json.tool
  ```

  Example API response:

  ```
  output omitted
      "started_at": "2024-02-16 12:58:17 UTC",
      "ended_at": "2024-02-16 12:58:18 UTC",
      "state": "stopped",
      "result": "success",
      "progress": 1.0,
      "input": {
          "activation_key": {
              "id": 2,
              "name": "TestKey"
  output truncated
  ```

## 2.2. JSON response format

Satellite API returns results in JSON format, which you can parse programmatically to extract data from single-object responses or collections responses.

### 2.2.1. JSON response format for single objects

You can use single-object JSON responses to work with a single object. API requests to a single object require the unique identifier `:id` of the object.

This is an example of the format for a single-object request for the Satellite domain which ID is 23:

API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/domains/23 \
    | python3 -m json.tool
    ```

API response
:   ```
    {
        "id": 23,
        "name": "qa.lab.example.com",
        "fullname": "QA",
        "dns_id": 10,
        "created_at": "2024-08-13T09:02:31Z",
        "updated_at": "2024-08-13T09:02:31Z"
    }
    ```

### 2.2.2. JSON response format for collections

Collections return lists of objects, such as hosts and domains. Each response includes pagination metadata and a results section containing the data you can iterate through.

This is an example of the format for a collection request for a list of Satellite domains:

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/domains \
    | python3 -m json.tool
    ```

Example API response
:   ```
    {
        "total": 3,
        "subtotal": 3,
        "page": 1,
        "per_page": 20,
        "search": null,
        "sort": {
            "by": null,
            "order": null
        },
        "results": [
            {
                "id": 23,
                "name": "qa.lab.example.com",
                "fullname": "QA",
                "dns_id": 10,
                "created_at": "2024-08-13T09:02:31Z",
                "updated_at": "2024-08-13T09:02:31Z"
            },
            {
                "id": 25,
                "name": "dev.lab.example.com",
                "fullname": "DEVEL",
                "dns_id": 8,
                "created_at": "2024-08-13T08:32:48Z",
                "updated_at": "2024-08-14T07:04:03Z"
            },
            {
                "id": 32,
                "name": "hr.lab.example.com",
                "fullname": "HR",
                "dns_id": 8,
                "created_at": "2024-08-16T08:32:48Z",
                "updated_at": "2024-08-16T07:04:03Z"
            }
        ]
    }
    ```

### 2.2.3. JSON response metadata

Review the metadata fields in Satellite API responses to understand pagination, search results, and collection information when working with the API.

Satellite API responses contain the following metadata fields:

`total`
:   The total number of objects without any search parameters.

`subtotal`
:   The number of objects returned with the given search parameters. If there is no search, then subtotal is equal to total.

`page`
:   The page number.

`per_page`
:   The maximum number of objects returned per page.

`limit`
:   The specified number of objects to return in a collection response.

`offset`
:   The number of objects skipped before returning a collection.

`search`
:   The search string based on `scoped_scoped` syntax.

`sort`
:   - `by` – Specifies by what field the API sorts the collection.
    - `order` – The sort order, either ASC for ascending or DESC for descending.

`results`
:   The collection of objects.

## 2.3. Relating API error messages to the API reference

You can map API error messages to the corresponding sections in the API reference documentation by translating the RAILS error format to the reference format. This helps you locate the relevant documentation when troubleshooting API errors.

The API uses a RAILs format to indicate an error:

```
Nested_Resource.Attribute_Name
```

This translates to the following format used in the API reference:

```
Resource[Nested_Resource_attributes][Attribute_Name_id]
```
