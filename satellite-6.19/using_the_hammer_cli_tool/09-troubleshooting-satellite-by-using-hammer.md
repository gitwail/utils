---
title: "Troubleshooting Satellite by using Hammer"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "9"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#troubleshooting-satellite-by-using-hammer"
---
# Chapter 9. Troubleshooting Satellite by using Hammer

You can use the `hammer ping` command to check the status of core Satellite services. Together with the `satellite-maintain service status` command, this can help you to diagnose and troubleshoot Satellite issues.

If all services are running as expected, the output looks as follows:

```
$ hammer ping
database:
    Status:          ok
    Server Response: Duration: 0ms
cache:
    servers:
     1) Status:          ok
        Server Response: Duration: 1ms
candlepin:
    Status:          ok
    Server Response: Duration: 17ms
candlepin_auth:
    Status:          ok
    Server Response: Duration: 14ms
candlepin_events:
    Status:          ok
    message:         4 Processed, 0 Failed
    Server Response: Duration: 0ms
katello_events:
    Status:          ok
    message:         5 Processed, 0 Failed
    Server Response: Duration: 0ms
pulp3:
    Status:          ok
    Server Response: Duration: 5083ms
pulp3_content:
    Status:          ok
    Server Response: Duration: 5051ms
foreman_tasks:
    Status:          ok
    Server Response: Duration: 2ms
```
