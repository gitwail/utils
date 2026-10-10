---
title: "Managing container images"
product: "Red Hat Satellite"
version: "6.19"
guide: "managing_content"
guide_title: "Managing content"
chapter_number: "14"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#Managing_Container_Images_content-management"
---
# Chapter 14. Managing container images

Import container image repositories, configure registry access and naming, and push or pull images to manage container content across lifecycle environments in Satellite.

**Additional resources**

- [*Red Hat Enterprise Linux 10 Building, running, and managing containers*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/building_running_and_managing_containers/index)
- [*Red Hat Enterprise Linux 9 Building, running, and managing containers*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/building_running_and_managing_containers/index)
- [*Red Hat Enterprise Linux 8 Building, running, and managing containers*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index)
- [Getting Started with Containers in *Red Hat Enterprise Linux Atomic Host 7*](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_atomic_host/7/html/getting_started_with_containers/index)

## 14.1. Importing container image repositories

Import container image repositories into Satellite from Red Hat Registry or other image registries to synchronize external images and make them available through content views.

### 14.1.1. Discovering container image repositories in a registry

Discover container image repositories in an external registry from the Satellite web UI to quickly import multiple repositories without entering each repository URL manually.

**Prerequisites**

- If the container image registry requires authentication, you have valid credentials for the registry.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products** and click **Repo Discovery**.
2. From the **Repository Type** list, select **Container Images**.
3. In the **Registry to Discover** field, enter the URL of the registry to import images from.
4. In the **Registry Username** field, enter the name that corresponds with your user name for the container image registry.
5. In the **Registry Password** field, enter the password that corresponds with the user name that you enter.
6. In the **Registry Search Parameter** field, enter any search criteria that you want to use to filter your search, and then click **Discover**.
7. Optional: To further refine the **Discovered Repository** list, in the **Filter** field, enter any additional search criteria that you want to use.
8. From the **Discovered Repository** list, select any repositories that you want to import, and then click **Create Selected**.
9. Optional: To change the download policy for this container repository to *on demand*, see [Section 6.4, “Updating the download policy for a repository by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#updating-the-download-policy-for-a-repository-by-using-web-ui "6.4. Updating the download policy for a repository by using Satellite web UI").
10. Optional: If you want to create a product, from the **Product** list, select **New Product**.
11. In the **Name** field, enter a product name.
12. Optional: In the **Repository Name** and **Repository Label** columns, you can edit the repository names and labels.
13. Click **Run Repository Creation**.
14. When repository creation is complete, you can click each new repository to view more information.
15. Optional: To filter the content you import to a repository, click a repository, and then navigate to **Limit Sync Tags**. Click to edit, and add any tags that you want to limit the content that synchronizes to Satellite.
16. In the Satellite web UI, navigate to **Content** > **Products** and select the name of your product.
17. Select the new repositories and then click **Sync Now** to start the synchronization process.

**Next steps**

- To view the progress of the synchronization, navigate to **Content** > **Sync Status** and expand the repository tree.
- When the synchronization completes, you can click **Container Image Manifests** to list the available manifests. From the list, you can also remove any manifests that you do not require.

### 14.1.2. Importing a container image repository manually by using Satellite web UI

Manually import a container image repository in the Satellite web UI when you know the repository URL and want to add a single repository to a product.

**Prerequisites**

- A product exists in your organization.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Products**.
2. Click the name of the required product.
3. Click **New repository**.
4. From the **Type** list, select **docker**.
5. Enter the details for the repository, and click **Save**.
6. Select the new repository, and click **Sync Now**.

**Next steps**

- To view the progress of the synchronization, navigate to **Content** > **Sync Status** and expand the repository tree.
- When the synchronization completes, you can click **Container Image Manifests** to list the available manifests. From the list, you can also remove any manifests that you do not require.

**Additional resources**

- [Chapter 3, *Adding content to Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite "Chapter 3. Adding content to Satellite")

### 14.1.3. Importing a container image repository by using Hammer CLI

Import a container image repository by using the Hammer CLI to add and synchronize container content as part of automated Satellite administration.

**Procedure**

1. Create the custom `Red Hat Container Catalog` product:

   ```
   $ hammer product create \
   --description "My_Description" \
   --name "Red Hat Container Catalog" \
   --organization "My_Organization" \
   --sync-plan "My_Sync_Plan"
   ```
2. Create the repository for the container images:

   ```
   $ hammer repository create \
   --content-type "docker" \
   --docker-upstream-name "rhel7" \
   --name "RHEL7" \
   --organization "My_Organization" \
   --product "Red Hat Container Catalog" \
   --url "http://registry.access.redhat.com/"
   ```
3. Synchronize the repository:

   ```
   $ hammer repository synchronize \
   --name "RHEL7" \
   --organization "My_Organization" \
   --product "Red Hat Container Catalog"
   ```

**Additional resources**

- [Chapter 3, *Adding content to Satellite*](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#adding-content-to-satellite "Chapter 3. Adding content to Satellite")

## 14.2. Configuring the Satellite container registry

Registry name patterns and authentication settings control how container images are named and who can access them in each lifecycle environment of the Satellite container registry.

### 14.2.1. Configuring container registry name patterns for a lifecycle environment

Set a registry name pattern for a lifecycle environment to override default container image names and to avoid naming conflicts when you pull images from Satellite.

When you use Satellite to create and manage your containers, as the container moves through content view versions and different stages of the Satellite lifecycle environment, the container name changes at each stage. For example, if you synchronize a container image with the name `ssh` from an upstream repository, when you add it to a Satellite product and organization and then publish as part of a content view, the container image can have the following name: `my_organization_production-custom_spin-my_product-custom_ssh`. This can create problems when you want to pull a container image because container registries can contain only one instance of a container name.

> **Warning**
>
> Proceed with caution when defining registry naming patterns for your containers.
>
> If you use a registry name pattern to manage container naming conventions, because registry naming patterns must generate globally unique names, you might experience naming conflict problems. For example:
>
> - If you set the `repository.docker_upstream_name` registry name pattern, you cannot publish or promote content views with container content with identical repository names to the `Production` lifecycle.
> - If you set the `lifecycle_environment.name` registry name pattern, this can prevent the creation of a second container repository with the identical name.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Lifecycle Environments**.
2. Create a lifecycle environment or select an existing lifecycle environment to edit.
3. In the **Container Image Registry** area, click the edit icon to the right of **Registry Name Pattern** area.
4. Use the list of variables and examples to determine which registry name pattern you require.
5. In the **Registry Name Pattern** field, enter the registry name pattern that you want to use. For example, to use the `repository.docker_upstream_name`:

   ```
   <%= repository.docker_upstream_name %>
   ```
6. Click **Save**.

### 14.2.2. Controlling container registry access for a lifecycle environment

Control whether users must authenticate to pull container images from a lifecycle environment, for example to allow unauthenticated access in production.

By default, users must authenticate to access container images in Satellite. You can specify whether users must authenticate to access container images in a lifecycle environment. For example, you might want to permit users to access container images from the `Production` lifecycle environment without any authentication requirement and restrict access to the `Development` and `QA` environments to authenticated users.

**Procedure**

1. In the Satellite web UI, navigate to **Content** > **Lifecycle** > **Lifecycle Environments**.
2. Select the lifecycle environment that you want to manage authentication for.
3. To permit unauthenticated access to the containers in this lifecycle environment, select the **Unauthenticated Pull** checkbox. To restrict unauthenticated access, clear the **Unauthenticated Pull** checkbox.
4. Click **Save**.

## 14.3. Using the Satellite container registry

Use Podman or Docker to push container images to the Satellite container registry or pull images that you publish and promote through content views.

The Satellite container registry follows the Open Containers Initiative (OCI) specification, so you can push content to Satellite by using the same methods that apply to other container registries.

Container registries on Capsules
:   On Capsules with content, the Container Gateway Capsule plugin acts as the container registry. It caches authentication information from Katello and proxies incoming requests to Pulp. The Container Gateway is available by default on Capsules with content.

**Additional resources**

- [Open Container Initiative Distribution Specification](https://opencontainers.org/)
- [Container Gateway Capsule plugin](https://github.com/Katello/smart_proxy_container_gateway)

### 14.3.1. Considerations for using the Satellite container registry

Review naming, push, and pull limitations before you use the Satellite container registry so that container workflows succeed without unexpected errors.

- You cannot push to repositories created by the general repositories endpoints, only to repositories created by the container push workflow.
- You can only push content to Satellite Server itself. If you need pushed content on Capsule Servers as well, use Capsule syncing.
- The pushed container registry name must contain only lowercase characters.
- Unless pushed repositories are published in a content view version, they do not follow the registry name pattern. This is to ensure that users can push and pull from the same path.
- Users are required to push and pull from the same path. If you use the label-based schema, pull using labels. If you use the ID-based schema, pull using IDs.

**Additional resources**

- [Section 14.2.1, “Configuring container registry name patterns for a lifecycle environment”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#configuring-container-registry-name-patterns-for-a-lifecycle-environment "14.2.1. Configuring container registry name patterns for a lifecycle environment")

### 14.3.2. Configuring Podman to trust the certificate authority

Configure Podman to trust the Satellite certificate authority so that you can push and pull container images without disabling TLS verification.

Podman locates the CA file in the `/etc/containers/certs.d/` path. Copy the root CA file to that path, with the exact path determined by the server hostname, and name the file `ca.crt`.

In the following examples, replace `hostname.example.com` with `satellite.example.com` or `capsule.example.com`, depending on your use case.

**Prerequisites**

- You have the root CA certificate file for Satellite Server or Capsule Server.
- You have root or sudo access on the host where Podman is installed.

**Procedure**

1. Create the relevant directory:

   ```
   # mkdir --parents /etc/containers/certs.d/hostname.example.com
   ```
2. Copy the CA file to the directory:

   ```
   # cp My_Root_CA.pem /etc/containers/certs.d/hostname.example.com/ca.crt
   ```

**Verification**

- Verify that you no longer need to use the `--tls-verify=false` option when logging in to the registry:

  ```
  $ podman login hostname.example.com
  ```

### 14.3.3. Configuring Docker to trust the certificate authority

Configure Docker to trust the Satellite certificate authority so that you can push and pull container images without disabling TLS verification.

Docker locates the CA file in the `/etc/docker/certs.d/` path. Copy the root CA file to that path, with the exact path determined by the server hostname, and name the file `ca.crt`.

In the following examples, replace `hostname.example.com` with `satellite.example.com` or `capsule.example.com`, depending on your use case.

**Prerequisites**

- You have the root CA certificate file for Satellite Server or Capsule Server.
- You have root or sudo access on the host where Docker is installed.

**Procedure**

1. Create the relevant directory:

   ```
   # mkdir --parents /etc/docker/certs.d/hostname.example.com
   ```
2. Copy the CA file to the directory:

   ```
   # cp My_Root_CA.pem /etc/docker/certs.d/hostname.example.com/ca.crt
   ```

**Verification**

- Verify that you no longer need to use the `--tls-verify=false` option when logging in to the registry:

  ```
  $ docker login hostname.example.com
  ```

### 14.3.4. Pushing container images to Satellite

Push container images to the Satellite container registry to distribute custom images to hosts and lifecycle environments through Satellite content management.

**Prerequisites**

- You have reviewed [Section 14.3.1, “Considerations for using the Satellite container registry”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#considerations-for-using-the-satellite-container-registry "14.3.1. Considerations for using the Satellite container registry").
- If Satellite Server uses a self-signed certificate, you have configured Podman or Docker to trust the Satellite certificate authority. For more information, see one of the following resources:

  - [Section 14.3.2, “Configuring Podman to trust the certificate authority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#configuring-podman-to-trust-the-certificate-authority "14.3.2. Configuring Podman to trust the certificate authority")
  - [Section 14.3.3, “Configuring Docker to trust the certificate authority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#configuring-docker-to-trust-the-certificate-authority "14.3.3. Configuring Docker to trust the certificate authority")
- Your Satellite account has the `edit_products` permission.
- A product exists in your organization. For more information, see [Section 3.6.1, “Creating a custom product by using Satellite web UI”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#creating-a-custom-product-by-using-web-ui "3.6.1. Creating a custom product by using Satellite web UI").
- Your Satellite account has the `create_personal_access_tokens` permission. Satellite automatically generates a token when you run `podman login`.

**Procedure**

1. Log in to the container registry:

   ```
   $ podman login satellite.example.com
   ```
2. Push a container image to the Satellite container registry. To indicate which organization, product, and repository the container image belongs to, include the organization and product in the container image path.

   You can specify the container image destination by using one of the following schemas:

   - Push the container image by using the label-based schema:

     ```
     $ podman push My_Container_Image_ID satellite.example.com/My_Organization_Label/My_Product_Label/My_Repository_Name[:My_Tag]
     ```
   - Push the container image by using the ID-based schema:

     ```
     $ podman push My_Container_Image_ID satellite.example.com/id/My_Organization_ID/My_Product_ID/My_Repository_Name[:My_Tag]
     ```

   The image tag is optional.
3. After the content push has completed, Satellite creates the repository.

### 14.3.5. Pulling container images from Satellite

Pull container images from the Satellite container registry by using Podman or Docker to deploy images that you publish in content views across lifecycle environments.

**Prerequisites**

- You have reviewed [Section 14.3.1, “Considerations for using the Satellite container registry”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#considerations-for-using-the-satellite-container-registry "14.3.1. Considerations for using the Satellite container registry").
- If Satellite Server uses a self-signed certificate, you have configured Podman or Docker to trust the Satellite certificate authority. For more information, see one of the following resources:

  - [Section 14.3.2, “Configuring Podman to trust the certificate authority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#configuring-podman-to-trust-the-certificate-authority "14.3.2. Configuring Podman to trust the certificate authority")
  - [Section 14.3.3, “Configuring Docker to trust the certificate authority”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/managing_content/index#configuring-docker-to-trust-the-certificate-authority "14.3.3. Configuring Docker to trust the certificate authority")
- Your Satellite account has the `view_lifecycle_environments`, `view_products`, and `view_content_views` permissions, unless the lifecycle environment allows unauthenticated pull.
- Your Satellite account has the `create_personal_access_tokens` permission. Satellite automatically generates a token when you run `podman login`.

**Procedure**

1. Log in to the container registry:

   ```
   $ podman login satellite.example.com
   ```
2. List container images:

   ```
   $ podman search satellite.example.com/
   ```
3. Pull a container image:

   ```
   $ podman pull satellite.example.com/My_Image_Path[:My_Tag]
   ```

   Pull the image by using the same image path schema as the one used to push the image. The path schema can be either label-based or ID-based.

   The image tag is optional. If you do not specify a tag, `podman` pulls the latest tag.
