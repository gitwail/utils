---
title: "Hiding header output from Hammer commands"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "7"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#hiding-header-output-from-hammer-commands"
---
# Chapter 7. Hiding header output from Hammer commands

When you use any Hammer command, you have the option of hiding headers from the output. If you want to pipe or use the output in custom scripts, hiding the output is useful.

**Procedure**

- Add the `--no-headers` option to any Hammer command to hide the header output:

  ```
  $ hammer --no-headers command
  ```
