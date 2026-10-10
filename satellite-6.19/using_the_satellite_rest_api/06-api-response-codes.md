---
title: "API response codes"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_rest_api"
guide_title: "Using the Satellite REST API"
chapter_number: "A"
section_type: "appendix"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#api-response_codes"
---
# Appendix A. API response codes

The Red Hat Satellite 6 API provides HTTP response status codes for API calls. The following codes are common for all resources in the Satellite API.

Table A.1. API response codes

| Response | Explanation |
| --- | --- |
| 200 OK | For a successful request action: show, index, update, or delete (GET, PUT, DELETE requests). |
| 201 Created | For a successful create action (POST request). |
| 301 Moved Permanently | Redirect when Satellite is restricted to use HTTPS and HTTP is attempted. |
| 400 Bad Request | A required parameter is missing or the search query has invalid syntax. |
| 401 Unauthorized | Failed to authorize the user, for example, due to incorrect credentials. |
| 403 Forbidden | The user has insufficient permissions to perform the action or read the resource, or the action is unsupported in general. |
| 404 Not Found | The record with the given ID does not exist. It can appear in show and delete actions when the requested record does not exist; or in create, update and delete actions when one of the associated records does not exist. |
| 409 Conflict | Could not delete the record due to existing dependencies, for example, host groups that still contain hosts. |
| 415 Unsupported Media Type | The content type of the HTTP request is not JSON. |
| 422 Unprocessable Entity | Failed to create an entity due to some validation errors. Applies to create or update actions only. |
| 500 Internal Server Error | Unexpected internal server error. |
| 503 Service Unavailable | The server is not running. |
