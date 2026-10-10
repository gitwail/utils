---
title: "Using JSON for complex parameters"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "8"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#using-json-for-complex-parameters"
---
# Chapter 8. Using JSON for complex parameters

Use JSON format to pass complex parameters with multiple nested values to Hammer commands.

An example of JSON formatted content appears below:

```
$ hammer compute-profile values create --compute-profile-id 22 --compute-resource-id 1 --compute-attributes=
'{
"cpus": 2,
"corespersocket": 2,
"memory_mb": 4096,
"firmware": "efi",
"resource_pool": "Resources",
"cluster": "Example_Cluster",
"guest_id": "rhel8",
"path": "/Datacenters/EXAMPLE/vm/",
"hardware_version": "Default",
"memoryHotAddEnabled": 0,
"cpuHotAddEnabled": 0,
"add_cdrom": 0,
"boot_order": [
               "disk",
               "network"
              ],
"scsi_controllers":[
      {
       "type":  "ParaVirtualSCSIController",
       "key":1000
       },
      {
        "type":  "ParaVirtualSCSIController",
        "key":1001
       }
                   ]
}'
```
