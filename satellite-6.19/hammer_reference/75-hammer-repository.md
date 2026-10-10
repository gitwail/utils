---
title: "repository"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "75"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#hammer-repository"
---
# Chapter 75. repository

Manipulate repositories

**Usage**

```
# hammer repository [OPTIONS] SUBCOMMAND [ARG] ...
```

**Options**

- `-h`, `--help` – Print help

## 75.1. repository create

Create a custom repository

**Usage**

```
# hammer repository create [OPTIONS]
```

**Options**

- `--ansible-collection-auth-token VALUE` – The token key to use for authentication.
- `--ansible-collection-auth-url VALUE` – The URL to receive a session token from, e.g. used with Automation Hub.
- `--ansible-collection-requirements VALUE` – Contents of requirement yaml file to sync from URL
- `--ansible-collection-requirements-file VALUE` Location of the ansible collections requirements.yml file.
- `--arch VALUE` – Architecture of content in the repository
- `--checksum-type VALUE` – Checksum used for published repository contents. Supported types: sha256, sha384, sha512
- `--content-type VALUE` – Type of repository to create. View available types with "hammer repository types"
- `--deb-architectures VALUE` – Whitespace-separated list of architectures to be synced from deb-archive
- `--deb-components VALUE` – Whitespace-separated list of repo components to be synced from deb-archive
- `--deb-releases VALUE` – Whitespace-separated list of releases to be synced from deb-archive
- `--depth NUMBER` – An option to specify how many ostree commits to traverse.
- `--description VALUE` – Description of the repository
- `--docker-upstream-name VALUE` – Name of the upstream docker repository
- `--download-concurrency NUMBER` – Used to determine download concurrency of the repository in pulp3. Use value less than 20. Defaults to 10
- `--download-policy ENUM` – Download policy for deb, docker, file and yum repos (either `immediate` or `on_demand`) Possible value(s): `immediate`, `on_demand`
- `--exclude-refs LIST` – A comma-separated list of tags to exclude during an ostree sync. The wildcards *, ? are recognized. `exclude_refs` is evaluated after `include_refs`.
- `--exclude-tags LIST` – Comma-separated list of tags to exclude when syncing a container image repository. Default: any tag ending in “-source”
- `--excludes LIST` – Python packages to exclude from the upstream URL, names separated by newline. You may also specify versions, for example: django~=2.0.
- `--gpg-key-id NUMBER` – Id of the gpg key that will be assigned to the new repository
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – ID of a HTTP proxy
- `--http-proxy-policy ENUM` – Policies for HTTP proxy for content sync Possible value(s): `global_default_http_proxy`, `none`, `use_selected_http_proxy`
- `--ignorable-content LIST` – List of content units to ignore while syncing a yum repository. Must be subset of srpm,treeinfo
- `--include-refs LIST` – A comma-separated list of refs to include during an ostree sync. The wildcards *, ? are recognized.
- `--include-tags LIST` – Comma-separated list of tags to sync for a container image repository
- `--includes LIST` – Python packages to include from the upstream URL, names separated by newline. You may also specify versions, for example: django~=2.0. Leave empty to include every package.
- `--keep-latest-packages NUMBER` – The amount of latest versions of a package to keep on sync, includes pre-releases if synced. Default 0 keeps all versions.
- `--label VALUE`
- `--metadata-expire NUMBER` – Time to expire yum metadata in seconds. Only relevant for custom yum repositories.
- `--mirroring-policy ENUM` – Policy to set for mirroring content. Must be one of additive. Possible value(s): `additive`, `mirror_complete`, `mirror_content_only`
- `--name VALUE` – Name of the repository
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER`
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--os-versions LIST` – Identifies whether the repository should be unavailable on a client with a non-matching OS version. Pass [] to make repo available for clients regardless of OS version. Maximum length 1; allowed tags are: rhel-6, rhel-7, rhel-8, rhel-9, rhel-10
- `--package-types LIST` – Package types to sync for Python content, separated by comma. Leave empty to get every package type. Package types are: bdist_dmg,bdist_dumb,bdist_egg,bdist_msi,bdist_rpm,bdist_wheel,bdist_wininst,sdist.
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product the repository belongs to
- `--publish-via-http BOOLEAN` – Publish Via HTTP
- `--retain-package-versions-count NUMBER` – The maximum number of versions of each package to keep.
- `--ssl-ca-cert-id NUMBER` – Identifier of the content credential containing the SSL CA Cert
- `--ssl-client-cert-id NUMBER` – Identifier of the content credential containing the SSL Client Cert
- `--ssl-client-key-id NUMBER` – Identifier of the content credential containing the SSL Client Key
- `--upstream-authentication-token VALUE` – Upstream authentication token string for yum repositories.
- `--upstream-password VALUE` – Password of the upstream repository user used for authentication
- `--upstream-username VALUE` – Username of the upstream repository user used for authentication
- `--url VALUE` – Repository source url
- `--verify-ssl-on-sync BOOLEAN` – If true, Katello will verify the upstream url`s SSL certifcates are signed by a trusted CA
- `-h`, `--help` – Print help

## 75.2. repository delete

Destroy a custom repository

**Usage**

```
# hammer repository <delete|destroy> [OPTIONS]
```

**Options**

- `--delete-empty-repo-filters BOOLEAN` – Delete content view filters that have this repository as the last associated repository. Defaults to true. If false, such filters will now apply to all repositories in the content view.
- `--id NUMBER`
- `--name VALUE` – Repository name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--remove-from-content-view-versions BOOLEAN` Force delete the repository by removing it from all content view versions
- `-h`, `--help` – Print help

## 75.3. repository info

Show a repository

**Usage**

```
# hammer repository <info|show> [OPTIONS]
```

**Options**

- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Repository ID
- `--name VALUE` – Repository name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Label | x | x |  |
| Description | x | x |  |
| Organization | x | x |  |
| Red hat repository | x | x |  |
| Content type | x | x |  |
| Content label | x | x |  |
| Checksum type | x | x |  |
| Mirroring policy | x | x |  |
| Url | x | x |  |
| Publish via http | x | x |  |
| Published at | x | x |  |
| Relative path | x | x |  |
| Download policy | x | x |  |
| Metadata expiration | x | x |  |
| Upstream repository name | x | x |  |
| Container image tags filter | x | x |  |
| Container repository name | x | x |  |
| Ignorable content units | x | x |  |
| Publish settings/restrict to architecture | x | x |  |
| Publish settings/restrict to os version | x | x |  |
| Http proxy/id | x | x |  |
| Http proxy/name | x | x |  |
| Http proxy/http proxy policy | x | x |  |
| Product/id | x | x |  |
| Product/name | x | x |  |
| Gpg key/id | x | x |  |
| Gpg key/name | x | x |  |
| Gpg key/gpg key path | x | x |  |
| Sync/status | x | x |  |
| Sync/last sync date | x | x |  |
| Created | x | x |  |
| Updated | x | x |  |
| Content counts/packages | x | x |  |
| Content counts/srpms | x | x |  |
| Content counts/module streams | x | x |  |
| Content counts/package groups | x | x |  |
| Content counts/errata | x | x |  |
| Content counts/debian packages | x | x |  |
| Content counts/container tags | x | x |  |
| Content counts/container manifests | x | x |  |
| Content counts/container manifest lists | x | x |  |
| Content counts/files | x | x |  |
| Content counts/ansible collections | x | x |  |
| Content counts/ostree refs | x | x |  |
| Content counts/python packages | x | x |  |

## 75.4. repository list

List of enabled repositories

**Usage**

```
# hammer repository <list|index> [OPTIONS]
```

**Options**

- `--ansible-collection VALUE` – Name to search by
- `--ansible-collection-id VALUE` – Id of an ansible collection to find repositories that contain the ansible collection
- `--archived BOOLEAN` – Show archived repositories
- `--available-for VALUE` – Interpret specified object to return only Repositories that can be associated with specified object. Only `content_view` & `content_view_version` are supported.
- `--content-type VALUE` – Limit the repository type to return. View available types with "hammer repository types"
- `--content-view VALUE` – Content view name to search by
- `--content-view-id NUMBER` – ID of a content view to show repositories in
- `--content-view-version VALUE` – Content view version number
- `--content-view-version-id NUMBER` ID of a content view version to show repositories in
- `--deb VALUE` – Name to search by
- `--deb-id VALUE` – Id of a deb package to find repositories that contain the deb
- `--description VALUE` – Description of the repository
- `--download-policy ENUM` – Limit to only repositories with this download policy Possible value(s): `immediate`, `on_demand`
- `--environment VALUE` – Lifecycle environment name to search by (--environment is deprecated: Use
- `--lifecycle-environment` instead)
- `--environment-id NUMBER` – (--environment-id is deprecated: Use `--lifecycle-environment-id` instead)
- `--erratum-id VALUE` – Id of an erratum to find repositories that contain the erratum
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--file-id VALUE` – Id of a file to find repositories that contain the file
- `--full-result BOOLEAN` – Whether or not to show all results
- `--label VALUE` – Label of the repository
- `--library BOOLEAN` – Show repositories in Library and the default content view
- `--lifecycle-environment VALUE` – Lifecycle environment name to search by
- `--lifecycle-environment-id NUMBER` ID of an environment to show repositories in
- `--name VALUE` – Name of the repository
- `--order VALUE` – Sort field and order, eg. `id DESC`
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – ID of an organization to show repositories in
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--page NUMBER` – Page number, starting at 1
- `--per-page NUMBER` – Number of results per page to return
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – ID of a product to show repositories of
- `--rpm-id VALUE` – Id of a rpm package to find repositories that contain the rpm
- `--search VALUE` – Search string
- `--username VALUE` – Only show the repositories readable by this user with this username
- `--with-content VALUE` – Limit the repository type to return. View available types with "hammer repository types"
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Id | x | x | x |
| Name | x | x | x |
| Product | x | x |  |
| Content type | x | x |  |
| Content label | x | x |  |
| Url | x | x |  |
| Upstream repository name | x |  |  |

**Search and order fields**

- `container_repository_name` – string
- `content_label` – string
- `content_type` – string
- `content_view_id` – integer
- `description` – text
- `distribution_arch` – string
- `distribution_bootable` – boolean
- `distribution_family` – string
- `distribution_variant` – string
- `distribution_version` – string
- `download_policy` – string
- `label` – string
- `name` – string
- `product` – string
- `product_id` – integer
- `product_name` – string
- `redhat` – Values: true, false

## 75.5. repository reclaim-space

Reclaim space from an On Demand repository

**Usage**

```
# hammer repository reclaim-space [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Repository ID
- `--name VALUE` – Repository name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `-h`, `--help` – Print help

## 75.6. repository remove-content

Remove content from a repository

**Usage**

```
# hammer repository remove-content [OPTIONS]
```

**Options**

- `--content-type VALUE` – The type of content unit to remove (srpm, docker_manifest, etc.). View removable types with "hammer repository types"
- `--id NUMBER` – Repository ID
- `--ids LIST` – Array of content ids to remove
- `--name VALUE` – Repository name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--sync-capsule BOOLEAN` – Whether or not to sync an external capsule after upload. Default: true
- `-h`, `--help` – Print help

## 75.7. repository republish

Forces a republish of the specified repository.

**Usage**

```
# hammer repository republish [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--force BOOLEAN` – Force metadata regeneration to proceed. Dangerous when repositories use the `Complete Mirroring` mirroring policy
- `--id NUMBER` – Repository identifier
- `--name VALUE` – Repository name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `-h`, `--help` – Print help

## 75.8. repository synchronize

Sync a repository

**Usage**

```
# hammer repository synchronize [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Repository ID
- `--incremental BOOLEAN` – Perform an incremental import
- `--name VALUE` – Repository name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--skip-metadata-check BOOLEAN` Force sync even if no upstream changes are detected. Only used with yum or deb repositories.
- `--validate-contents BOOLEAN` – Force a sync and validate the checksums of all content. Only used with yum repositories.
- `-h`, `--help` – Print help

## 75.9. repository types

Show the available repository types

**Usage**

```
# hammer repository types [OPTIONS]
```

**Options**

- `--creatable BOOLEAN` – When set to `True` repository types that are creatable will be returned
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `-h`, `--help` – Print help

**Predefined field sets**

| FIELDS | ALL | DEFAULT | THIN |
| --- | --- | --- | --- |
| Name | x | x | x |
| Content types/type | x | x |  |
| Content types/generic? | x | x |  |
| Content types/removable? | x | x |  |
| Content types/uploadable? | x | x |  |
| Content types/indexed? | x | x |  |

## 75.10. repository update

Update a repository

**Usage**

```
# hammer repository update [OPTIONS]
```

**Options**

- `--ansible-collection-auth-token VALUE` – The token key to use for authentication.
- `--ansible-collection-auth-url VALUE` – The URL to receive a session token from, e.g. used with Automation Hub.
- `--ansible-collection-requirements VALUE` – Contents of requirement yaml file to sync from URL
- `--ansible-collection-requirements-file VALUE` Location of the ansible collections requirements.yml file.
- `--arch VALUE` – Architecture of content in the repository
- `--checksum-type VALUE` – Checksum used for published repository contents. Supported types: sha256, sha384, sha512
- `--deb-architectures VALUE` – Whitespace-separated list of architectures to be synced from deb-archive
- `--deb-components VALUE` – Whitespace-separated list of repo components to be synced from deb-archive
- `--deb-releases VALUE` – Whitespace-separated list of releases to be synced from deb-archive
- `--depth NUMBER` – An option to specify how many ostree commits to traverse.
- `--description VALUE` – Description of the repository
- `--docker-digest VALUE` – Container Image manifest digest
- `--docker-tag VALUE` – Container Image tag
- `--docker-upstream-name VALUE` – Name of the upstream docker repository
- `--download-concurrency NUMBER` – Used to determine download concurrency of the repository in pulp3. Use value less than 20. Defaults to 10
- `--download-policy ENUM` – Download policy for deb, docker, file and yum repos (either `immediate` or `on_demand`) Possible value(s): `immediate`, `on_demand`
- `--exclude-refs LIST` – A comma-separated list of tags to exclude during an ostree sync. The wildcards *, ? are recognized. `exclude_refs` is evaluated after `include_refs`.
- `--exclude-tags LIST` – Comma-separated list of tags to exclude when syncing a container image repository. Default: any tag ending in “-source”
- `--excludes LIST` – Python packages to exclude from the upstream URL, names separated by newline. You may also specify versions, for example: django~=2.0.
- `--gpg-key-id NUMBER` – Id of the gpg key that will be assigned to the new repository
- `--http-proxy VALUE` – Name to search by
- `--http-proxy-id NUMBER` – ID of a HTTP proxy
- `--http-proxy-policy ENUM` – Policies for HTTP proxy for content sync Possible value(s): `global_default_http_proxy`, `none`, `use_selected_http_proxy`
- `--id NUMBER` – Repository ID
- `--ignorable-content LIST` – List of content units to ignore while syncing a yum repository. Must be subset of srpm,treeinfo
- `--include-refs LIST` – A comma-separated list of refs to include during an ostree sync. The wildcards *, ? are recognized.
- `--include-tags LIST` – Comma-separated list of tags to sync for a container image repository
- `--includes LIST` – Python packages to include from the upstream URL, names separated by newline. You may also specify versions, for example: django~=2.0. Leave empty to include every package.
- `--keep-latest-packages NUMBER` – The amount of latest versions of a package to keep on sync, includes pre-releases if synced. Default 0 keeps all versions.
- `--metadata-expire NUMBER` – Time to expire yum metadata in seconds. Only relevant for custom yum repositories.
- `--mirroring-policy ENUM` – Policy to set for mirroring content. Must be one of additive. Possible value(s): `additive`, `mirror_complete`, `mirror_content_only`
- `--name VALUE`
- `--new-name VALUE`
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--os-versions LIST` – Identifies whether the repository should be unavailable on a client with a non-matching OS version. Pass [] to make repo available for clients regardless of OS version. Maximum length 1; allowed tags are: rhel-6, rhel-7, rhel-8, rhel-9, rhel-10
- `--package-types LIST` – Package types to sync for Python content, separated by comma. Leave empty to get every package type. Package types are: bdist_dmg,bdist_dumb,bdist_egg,bdist_msi,bdist_rpm,bdist_wheel,bdist_wininst,sdist.
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `--publish-via-http BOOLEAN` – Publish Via HTTP
- `--retain-package-versions-count NUMBER` – The maximum number of versions of each package to keep.
- `--ssl-ca-cert-id NUMBER` – Identifier of the content credential containing the SSL CA Cert
- `--ssl-client-cert-id NUMBER` – Identifier of the content credential containing the SSL Client Cert
- `--ssl-client-key-id NUMBER` – Identifier of the content credential containing the SSL Client Key
- `--upstream-authentication-token VALUE` – Upstream authentication token string for yum repositories.
- `--upstream-password VALUE` – Password of the upstream repository user used for authentication
- `--upstream-username VALUE` – Username of the upstream repository user used for authentication
- `--url VALUE` – Repository source url
- `--verify-ssl-on-sync BOOLEAN` – If true, Katello will verify the upstream url`s SSL certifcates are signed by a trusted CA
- `-h`, `--help` – Print help

## 75.11. repository upload-content

This endpoint is primarily designed for UI interactions and uploading content into the repository. For API-based uploads, please use the 'content_uploads' endpoint instead.

**Usage**

```
# hammer repository upload-content [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task.
- `--content-type VALUE` – The type of content unit to upload (srpm, file, etc.). View uploadable types with "hammer repository types"
- `--fields LIST` – Show specified fields or predefined field sets only. (See below)
- `--id NUMBER` – Repository ID
- `--name VALUE` – Repository name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id NUMBER` – Organization ID
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title
- `--ostree-repository-name VALUE` Name of OSTree repository in archive.
- `--path FILE` – Upload file, directory of files, or glob of files as content for a repository. Globs must be escaped by single or double quotes
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `-h`, `--help` – Print help

**Predefined field sets**

|  |
| --- |
| FIELDS |

## 75.12. repository verify-checksum

Verify checksum of repository contents

**Usage**

```
# hammer repository verify-checksum [OPTIONS]
```

**Options**

- `--async` – Do not wait for the task
- `--id NUMBER` – Repository ID
- `--name VALUE` – Repository name to search by
- `--organization VALUE` – Organization name to search by
- `--organization-id VALUE` – Organization ID to search by
- `--organization-label VALUE` – Organization label to search by
- `--organization-title VALUE` – Organization title to search by
- `--product VALUE` – Product name to search by
- `--product-id NUMBER` – Product numeric identifier
- `-h`, `--help` – Print help
