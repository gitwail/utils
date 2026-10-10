---
title: "API requests in various languages"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_satellite_rest_api"
guide_title: "Using the Satellite REST API"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#api-requests-in-various-languages"
---
# Chapter 4. API requests in various languages

You can interact with Satellite API using `curl` for quick testing, Ruby for automation scripts with apipie bindings, or Python for integration with existing Python-based workflows.

## 4.1. Calling the API in curl

You can use `curl` to test API endpoints, debug requests, and perform quick operations without writing scripts.

You can use `curl` to manipulate resources on your Satellite Server. API calls to Satellite require data in `json` format.

Red Hat Satellite requires the use of HTTPS, and by default, a certificate for host identification.

For user authentication, you can use the `--user` option to provide Satellite user credentials in the form `--user My_User_Name:My_Password`. If you do not include the password, the command prompts you to enter it. To reduce security risks, do not include the password as part of the command, because it then becomes part of your shell history. For simplicity, the examples in this section include the password.

Be aware that if you use the `--silent` option, `curl` does not display a progress meter or any error messages.

Examples in this chapter use the Python `json.tool` module to format the output.

**Additional resources**

- [Section 3.1, “SSL authentication overview”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#ssl-authentication-overview "3.1. SSL authentication overview")
- [Section 4.1.1, “Passing JSON data to the API request”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#passing-json-data-to-the-api-request "4.1.1. Passing JSON data to the API request")

### 4.1.1. Passing JSON data to the API request

You can pass JSON-formatted data to Satellite API requests either as inline strings or external files.

When specifying JSON data with the `--data` option, you must set the following HTTP headers with the `--header` option:

```
--header "Accept: application/json" \
--header "Content-Type: application/json"
```

Use one of the following options to include data with the `--data` option.

JSON-formatted string
:   Enclose the quoted JSON-formatted data in curly braces `{}`. When passing a value for a JSON type parameter, you must escape quotation marks `"` with backslashes `\`. For example, within curly braces, you must format `"Example JSON Variable"` as `\"Example JSON Variable\"`:

    ```
    --data {"id":44, "smart_class_parameter":{"override":"true", "parameter_type":"json", "default_value":"{\"GRUB_CMDLINE_LINUX\": {\"audit\":\"1\",\"crashkernel\":\"true\"}}"}}
    ```

JSON-formatted file
:   The unquoted JSON-formatted data enclosed in a file and specified by the `@` sign and the filename. For example:

    ```
    --data @file.json
    ```

Using external files for JSON formatted data has the following advantages:

- You can use your favorite text editor.
- You can use syntax checker to find and avoid mistakes.
- You can use tools to check the validity of JSON data or to reformat it.

Use the `json_verify` tool to check the validity of the JSON file:

```
$ json_verify < file.json
```

### 4.1.2. Retrieving a list of resources

You can retrieve lists of Satellite resources such as users, hosts, or organizations using GET requests, with responses containing both metadata for pagination and the actual resource data.

This example is a basic request that returns a list of Satellite resources, Satellite users in this case. Such requests return a list of data wrapped in metadata, while other request types only return the actual object.

Example API request
:   ```
    $ curl \
    --request GET \
    --user My_User_Name:My_Password \
    https://satellite.example.com/api/users \
    | python3 -m json.tool
    ```

Example API response
:   ```
    {
        "page": 1,
        "per_page": 20,
        "results": [
            {
                "admin": false,
                "auth_source_id": 1,
                "auth_source_name": "Internal",
                "created_at": "2024-09-21 08:59:22 UTC",
                "default_location": null,
                "default_organization": null,
                "description": "",
                "effective_admin": false,
                "firstname": "",
                "id": 5,
                "last_login_on": "2024-09-21 09:03:25 UTC",
                "lastname": "",
                "locale": null,
                "locations": [],
                "login": "test",
                "mail": "test@example.com",
                "organizations": [
                    {
                        "id": 1,
                        "name": "Default Organization"
                    }
                ],
                "ssh_keys": [],
                "timezone": null,
                "updated_at": "2024-09-21 09:04:45 UTC"
            },
            {
                "admin": true,
                "auth_source_id": 1,
                "auth_source_name": "Internal",
                "created_at": "2024-09-20 07:09:41 UTC",
                "default_location": null,
                "default_organization": {
                    "description": null,
                    "id": 1,
                    "name": "Default Organization",
                    "title": "Default Organization"
                },
                "description": "",
                "effective_admin": true,
                "firstname": "Admin",
                "id": 4,
                "last_login_on": "2024-12-07 07:31:09 UTC",
                "lastname": "User",
                "locale": null,
                "locations": [
                    {
                        "id": 2,
                        "name": "Default Location"
                    }
                ],
                "login": "admin",
                "mail": "admin@example.com",
                "organizations": [
                    {
                        "id": 1,
                        "name": "Default Organization"
                    }
                ],
                "ssh_keys": [],
                "timezone": null,
                "updated_at": "2024-11-14 08:19:46 UTC"
            }
        ],
        "search": null,
        "sort": {
            "by": null,
            "order": null
        },
        "subtotal": 2,
        "total": 2
    }
    ```

### 4.1.3. Creating a user

You can create Satellite user accounts using POST requests.

This example adds a user account named `test_user`.

Example API request
:   ```
    $ curl \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --request POST \
    --user My_User_Name:My_Password \
    --data "{\"firstname\":\"Test Name\",\"mail\":\"test@example.com\",\"login\":\"test_user\",\"password\":\"password123\",\"auth_source_id\":1}" \
    https://satellite.example.com/api/users \
    | python3 -m json.tool
    ```

### 4.1.4. Modifying a user

You can modify Satellite user accounts using PUT requests by specifying the user ID and the fields you want to update, such as login name or email address.

This example changes the given name and login for the `test_user` account.

Example API request
:   ```
    $ curl \
    --header "Accept: application/json" \
    --header "Content-Type: application/json" \
    --request PUT \
    --user My_User_Name:My_Password \
    --data "{\"firstname\":\"New Test Name\",\"mail\":\"test@example.com\",\"login\":\"new_test_user\",\"password\":\"password123\",\"auth_source_id\":1}" \
    https://satellite.example.com/api/users/8 \
    | python3 -m json.tool
    ```

## 4.2. Calling the API in Ruby

You can use Ruby to automate complex Satellite workflows. Use REST client libraries or apipie bindings to get type-safe API calls with built-in validation.

> **Important**
>
> These are example scripts and commands. Ensure you review these scripts carefully before use, and replace any variables, user names, passwords, and other information to suit your own deployment.

### 4.2.1. Creating objects by using Ruby

You can use Ruby-based REST clients to create Satellite organizations and lifecycle environments programmatically, with built-in error handling for existing resources.

This script connects to the Red Hat Satellite 6 API, creates an organization, and then creates three lifecycle environments in the organization. If the organization already exists, the script uses that organization. If any of the lifecycle environments already exist in the organization, the script returns an error and exits.

```
#!/usr/bin/ruby

require 'rest-client'
require 'json'

url = 'https://satellite.example.com/api/v2/'
katello_url = "#{url}/katello/api/v2/"

$username = '_My_User_Name_'
$password = '_My_Password_'

org_name = "_My_Organization_"
environments = [ "Development", "Testing", "Production" ]

# Performs a GET by using the passed URL location
def get_json(location)
  response = RestClient::Request.new(
    :method => :get,
    :url => location,
    :user => $username,
    :password => $password,
    :headers => { :accept => :json,
    :content_type => :json }
  ).execute
  JSON.parse(response.to_str)
end

# Performs a POST and passes the data to the URL location
def post_json(location, json_data)
  response = RestClient::Request.new(
    :method => :post,
    :url => location,
    :user => $username,
    :password => $password,
    :headers => { :accept => :json,
    :content_type => :json},
    :payload => json_data
  ).execute
  JSON.parse(response.to_str)
end

# Creates a hash with ids mapping to names for an array of records
def id_name_map(records)
  records.inject({}) do |map, record|
    map.update(record['id'] => record['name'])
  end
end

# Get list of existing organizations
orgs = get_json("#{katello_url}/organizations")
org_list = id_name_map(orgs['results'])

if !org_list.has_value?(org_name)
  # If our organization is not found, create it
  puts "Creating organization: \t#{org_name}"
  org_id = post_json("#{katello_url}/organizations", JSON.generate({"name"=> org_name}))["id"]
else
  # Our organization exists, so let's grab it
  org_id = org_list.key(org_name)
  puts "Organization \"#{org_name}\" exists"
end

# Get list of organization's lifecycle environments
envs = get_json("#{katello_url}/organizations/#{org_id}/environments")
env_list = id_name_map(envs['results'])
prior_env_id = env_list.key("Library")

# Exit the script if at least one life cycle environment already exists
environments.each do |e|
  if env_list.has_value?(e)
    puts "ERROR: One of the Environments is not unique to organization"
    exit
  end
end

 # Create life cycle environments
environments.each do |environment|
  puts "Creating environment: \t#{environment}"
  prior_env_id = post_json("#{katello_url}/organizations/#{org_id}/environments", JSON.generate({"name" => environment, "organization_id" => org_id, "prior_id" => prior_env_id}))["id"]
end
```

### 4.2.2. Using apipie bindings with Ruby

You can use apipie bindings in Ruby to automatically fetch and cache Satellite API definitions. This way, you can write type-safe API calls with built-in validation and reduce manual endpoint configuration.

```
#!/usr/bin/ruby

require 'apipie-bindings'

org_name = "_My_Organization_"
environments = [ "Development", "Testing", "Production" ]

# Create an instance of apipie bindings
@api = ApipieBindings::API.new({
  :uri => 'https://satellite.example.com/',
  :username => 'admin',
  :password => 'changeme',
  :api_version => 2
})

# Performs an API call with default options
def call_api(resource_name, action_name, params = {})
  http_headers = {}
  apipie_options = { :skip_validation => true }
  @api.resource(resource_name).call(action_name, params, http_headers, apipie_options)
end

# Creates a hash with IDs mapping to names for an array of records
def id_name_map(records)
  records.inject({}) do |map, record|
    map.update(record['id'] => record['name'])
  end
end

# Get list of existing organizations
orgs = call_api(:organizations, :index)
org_list = id_name_map(orgs['results'])

if !org_list.has_value?(org_name)
  # If our organization is not found, create it
  puts "Creating organization: \t#{org_name}"
  org_id = call_api(:organizations, :create, {'organization' => { :name => org_name }})['id']
else
  # Our organization exists, so let's grab it
  org_id = org_list.key(org_name)
  puts "Organization \"#{org_name}\" exists"
end

# Get list of organization's life cycle environments
envs = call_api(:lifecycle_environments, :index, {'organization_id' => org_id})
env_list = id_name_map(envs['results'])
prior_env_id = env_list.key("Library")

# Exit the script if at least one life cycle environment already exists
environments.each do |e|
  if env_list.has_value?(e)
    puts "ERROR: One of the Environments is not unique to organization"
    exit
  end
end

 # Create life cycle environments
environments.each do |environment|
  puts "Creating environment: \t#{environment}"
  prior_env_id = call_api(:lifecycle_environments, :create, {"name" => environment, "organization_id" => org_id, "prior_id" => prior_env_id })['id']
end
```

## 4.3. Calling the API in Python

You can use Python with the `requests` module to integrate Satellite API calls into existing Python automation workflows, data processing pipelines, or DevOps tooling.

> **Important**
>
> These are example scripts and commands. Ensure you review these scripts carefully before use, and replace any variables, user names, passwords, and other information to suit your own deployment.

Example scripts in this section do not use SSL verification for interacting with the REST API.

### 4.3.1. Creating objects by using Python

You can use the Python `requests` module to create Satellite organizations and lifecycle environments programmatically.

This script connects to the Satellite API, creates an organization, and then creates three lifecycle environments in the organization. If the organization already exists, the script uses that organization. If any of the lifecycle environments already exist in the organization, the script returns an error and exits.

```
#!/usr/bin/python3

import json
import sys

try:
    import requests
except ImportError:
    print("Please install the python-requests module.")
    sys.exit(-1)

# URL to your Satellite Server
URL = "https://satellite.example.com"
FOREMAN_API = f"{URL}/api/"
KATELLO_API = f"{URL}/katello/api/"
POST_HEADERS = {'content-type': 'application/json'}
# Default credentials to login to Satellite 6
USERNAME = "admin"
PASSWORD = "changeme"
# Ignore SSL for now
SSL_VERIFY = False

# Name of the organization to be either created or used
ORG_NAME = "MyOrg"
# Name for life cycle environments to be either created or used
ENVIRONMENTS = ["Development", "Testing", "Production"]

def get_json(location):
    """
    Performs a GET by using the passed URL location
    """
    r = requests.get(location, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
    return r.json()

def post_json(location, json_data):
    """
    Performs a POST and passes the data to the URL location
    """
    result = requests.post(
        location,
        data=json_data,
        auth=(USERNAME, PASSWORD),
        verify=SSL_VERIFY,
        headers=POST_HEADERS
    )
    return result.json()

def main():
    """
    Main routine that creates or re-uses an organization and
    life cycle environments.
    If life cycle environments already
    exist, exit out.
    """

    # Check if our organization already exists
    org = get_json(f"{FOREMAN_API}/organizations/{ORG_NAME}")

    # If our organization is not found, create it
    if org.get('error', None):
        org_id = post_json(
            f"{FOREMAN_API}/organizations/",
            json.dumps({"name": ORG_NAME})
        )["id"]
        print("Creating organization:\t" + ORG_NAME)
    else:
        # Our organization exists, so let's grab it
        org_id = org['id']
        print(f"Organization '{ORG_NAME}' exists.")

    # Now, let's fetch all available life cycle environments for this org...
    envs = get_json(
        f"{KATELLO_API}/organizations/{org_id}/environments/"
    )

    # ...and add them to a dictionary, with respective 'Prior' environment
    prior_env_id = 0
    env_list = {}
    for env in envs['results']:
        env_list[env['id']] = env['name']
        prior_env_id = env['id'] if env['name'] == "Library" else prior_env_id

    # Exit the script if at least one life cycle environment already exists
    if all(environment in env_list.values() for environment in ENVIRONMENTS):
        print("ERROR: One of the Environments is not unique to organization")
        sys.exit(-1)

    # Create life cycle environments
    for environment in ENVIRONMENTS:
        new_env_id = post_json(
            f"{KATELLO_API}/organizations/{org_id}/environments/",
            json.dumps({
                "name": environment,
                "organization_id": org_id,
                "prior": prior_env_id
            })
        )["id"]

        print("Creating environment:\t" + environment)
        prior_env_id = new_env_id

if __name__ == "__main__":
    main()
```

### 4.3.2. Retrieving resource information by using Python

You can use Python to retrieve and display Satellite resource information such as host details, facts, and subscriptions. With this script, you can then format the Satellite API response specifically for your reporting or monitoring workflows.

```
#!/usr/bin/env python3

import json
import sys

try:
    import requests
except ImportError:
    print("Please install the python-requests module.")
    sys.exit(-1)

HOSTNAME = "satellite.example.com"
# URL for the API to your Satellite Server
FOREMAN_API = f"https://{HOSTNAME}/api/"
KATELLO_API = f"https://{HOSTNAME}/katello/api/v2/"

POST_HEADERS = {'content-type': 'application/json'}
# Default credentials to login to Satellite 6
USERNAME = "admin"
PASSWORD = "password"
# Ignore SSL for now
SSL_VERIFY = False
#SSL_VERIFY = "./path/to/CA-certificate.crt" # Put the path to your CA certificate here to allow SSL_VERIFY

def get_json(url):
    # Performs a GET by using the passed URL location
    r = requests.get(url, auth=(USERNAME, PASSWORD), verify=SSL_VERIFY)
    return r.json()

def get_results(url):
    jsn = get_json(url)
    if jsn.get('error'):
        print("Error: " + jsn['error']['message'])
    else:
        if jsn.get('results'):
            return jsn['results']
        elif 'results' not in jsn:
            return jsn
        else:
            print("No results found")
    return None

def display_all_results(url):
    results = get_results(url)
    if results:
        print(json.dumps(results, indent=4, sort_keys=True))

def display_info_for_hosts(url):
    hosts = get_results(url)
    if hosts:
        print(f"{'ID':10}{'Name':40}{'IP':30}{'Operating System':30}")
        for host in hosts:
            print(f"{str(host['id']):10}{host['name']:40}{str(host['ip']):30}{str(host['operatingsystem_name']):30}")

def display_info_for_subs(url):
    subs = get_results(url)
    if subs:
        print(f"{'ID':10}{'Name':90}{'Start Date':30}")
        for sub in subs:
            print(f"{str(sub['id']):10}{sub['name']:90}{str(sub['start_date']):30}")

def main():
    host = HOSTNAME
    print(f"Displaying all info for host {host} ...")
    display_all_results(FOREMAN_API + 'hosts/' + host)

    print(f"Displaying all facts for host {host} ...")
    display_all_results(FOREMAN_API + f'hosts/{host}/facts')

    host_pattern = 'example'
    print(f"Displaying basic info for hosts matching pattern '{host_pattern}'...")
    display_info_for_hosts(FOREMAN_API + 'hosts?per_page=1&search=name~' + host_pattern)

    print(f"Displaying basic info for subscriptions")
    display_info_for_subs(KATELLO_API + 'subscriptions')

    environment = 'production'
    print(f"Displaying basic info for hosts in environment {environment}...")
    display_info_for_hosts(FOREMAN_API + 'hosts?search=environment=' + environment)

if __name__ == "__main__":
    main()
```
