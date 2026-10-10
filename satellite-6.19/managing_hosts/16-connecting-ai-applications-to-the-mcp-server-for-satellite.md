---
title: "Connecting AI applications to the MCP server for Satellite"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_hosts"
guide_title: "Managing hosts"
chapter_number: "16"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_hosts/index#connecting-ai-applications-to-the-mcp-server-for-satellite"
---
# Chapter 16. Connecting AI applications to the MCP server for Satellite

Satellite provides a Model Context Protocol (MCP) server to enable integration with your MCP-compatible AI applications. You can obtain comprehensive AI-generated reports and data analysis of your Satellite inventory. Optionally, you can start the MCP server with permissions to edit the inventory.

> **Important**
>
> MCP server for Satellite is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

## 16.1. Satellite MCP integration overview

Satellite provides a Model Context Protocol (MCP) server so that users can use their preferred AI applications to obtain and process data about Satellite inventory.

Red Hat provides a container image that you use to deploy an MCP server for Satellite. On your system, you run an AI application, also known as MCP host. Your AI application runs an MCP client. The MCP client connects to your MCP server for Satellite. The MCP server obtains the data about Satellite inventory by making API calls to your Satellite Server with SSL-encrypted HTTP requests.

> **Important**
>
> For enhanced security, deploy the MCP server on the same system where the MCP client is running so that they can communicate over localhost. Avoid deploying the MCP server on a system exposed to the network.

Each Satellite user deploys their own MCP server and uses their credentials to access the Satellite inventory data. A user’s MCP client cannot obtain data that the user does not have permission to access.

When the connection is established, you query your AI application for data about your Satellite environment. The MCP client within the AI application obtains the required data from your Satellite inventory and returns it to the AI application. The AI application processes the data to answer your queries.

The MCP server runs in read-only mode by default. It extracts data from your Satellite inventory but cannot write, edit, or make any updates to the inventory. You can start the MCP server with permissions to make changes to the inventory, for example, to start remote execution jobs or publish and promote content views.

**Additional resources**

- [Model Context Protocol](https://modelcontextprotocol.io)

## 16.2. Deploying the MCP server for Satellite

Deploy the Model Context Protocol (MCP) server for Satellite as a container and make it accessible to your MCP client.

In this scenario, you deploy the MCP server on the same system where your MCP client will run. Do not deploy the MCP server on your Satellite Server to avoid insecure communication between the MCP server and client.

> **Important**
>
> In this scenario, the MCP server uses the *Streamable HTTP* transport mode for client-server communication. *Streamable HTTP* is the default MCP transport mode that can in some cases represent potential security risks. Consider using *stdio* transport mode instead. For more information, see [*Transports* in the Model Context Protocol documentation](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports).

**Prerequisites**

- You are logged in to the registry.redhat.io container registry.
- The CA bundle for your Satellite is available on your system. You can download it from `https://satellite.example.com/unattended/public/foreman_raw_ca`.

**Procedure**

1. Optional: Pull the latest version of the MCP container image from the registry:

   ```
   $ podman pull registry.redhat.io/satellite/foreman-mcp-server-rhel9:6.18
   ```
2. Run the container:

   ```
   $ podman run --interactive --tty --publish 127.0.0.1:8080:8080 \
     --volume Path_to_My_CA_Bundle:/app/ca.pem:ro,Z \
     registry.redhat.io/satellite/foreman-mcp-server-rhel9:6.18 \
     --foreman-url https://satellite.example.com
   ```

   The options used in the command include the following:

   `--publish`
   :   Maps port 8080 from inside the container to port 8080 on the host, binding the port to the localhost.

   `--volume`
   :   Mounts your CA certificate bundle from the host machine to the default location (`ca.pem`) inside the container.

       - `ro` makes the read-only mode inside the container
       - `Z` relabels the file with a private, unshared label

   `Path_to_My_CA_Bundle`
   :   Specifies the location of the Satellite CA bundle on the system. This is required to verify the connection to Satellite.

       > **Warning**
       >
       > Do not use the `--no-verify-ssl` option in production environments. Disabling SSL certificate verification with `--no-verify-ssl` compromises the security of your connection, making you vulnerable to security threats such as man-in-the-middle (MITM) attacks.

**Additional resources**

- [Red Hat Container Registry Authentication](https://access.redhat.com/articles/RegistryAuthentication)

## 16.3. Connecting the MCP client to the MCP server

Connect your Model Context Protocol (MCP) client to the MCP server so that your AI application can obtain data about your Satellite inventory.

In this scenario, your MCP client runs on the same system where you deployed the MCP server.

**Prerequisites**

- Your MCP client must support setting custom HTTP headers.

**Procedure**

1. Generate a personal access token (PAT) that the MCP client will use to connect to the MCP server:

   1. In the Satellite web UI, click the user menu in the top bar and select **My Account**.
   2. Select the **Personal Access Tokens** tab.
   3. Click **Add Personal Access Token**.

      > **Important**
      >
      > Red Hat recommends to set an expiration date for a PAT used to configure the MCP client.
2. Configure your client to pass credentials in an HTTP authorization request header. The exact configuration steps depend on your MCP client.

   For example, some clients require you to create a configuration file with the following contents:

   ```
   "my-mcp-server": {
   	"url": "http://localhost:8080/mcp/sse",
   	"type": "http",
   	"headers": {
   		"FOREMAN_USERNAME": "My_Username",
   		"FOREMAN_TOKEN": "My_PAT"
   	}
   }
   ```

**Additional resources**

- [Creating a Personal Access Token in *Using the Satellite REST API*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_satellite_rest_api/index#creating-a-personal-access-token_rest-api)

## 16.4. Querying the MCP server for Satellite

With your AI application connected to the Model Context Protocol (MCP) server for Satellite, you can use the AI application chatbot to request information about your Satellite deployment. The AI application retrieves and processes the relevant data from the Satellite inventory.

> **Warning**
>
> Always review content generated by AI before using it in production.

Red Hat provides examples of prompts and responses below. Results in your environment and their quality might vary depending on the capabilities of the large language model (LLM) that your AI application uses.

**Procedure**

- Type a prompt into your AI application. For example:

  ```
  Show a list of hosts that require patching.
  ```

  The AI application interprets the query and asks the MCP client to retrieve the relevant data from Satellite inventory through the MCP server. The MCP client fetches the data and returns it to the AI application, which then processes it to provide an answer to the user.

**Example 16.1. Prompt examples**

Querying hosts
:   To obtain a list of hosts that require patching and refine it, you can use the following prompts:

    ```
    Show a list of hosts that require patching on my Satellite.
    ```

    ```
    Categorize the list into hosts that require security patches
    and hosts that require bug fix patches.
    ```

Querying subnets
:   To obtain a report of all subnets in Satellite inventory, you can use the following prompts:

    ```
    Generate a static report of all subnets on my Satellite.
    Read API documentation for each of the needed resources
    before doing any searches.
    ```

    ```
    For each subnet, report its name, address, network mask,
    and number of hosts which are assigned to it.
    ```
