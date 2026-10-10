---
title: "Formatting Hammer output"
product: "Red Hat Satellite"
version: "6.19"
guide: "using_the_hammer_cli_tool"
guide_title: "Using the Hammer CLI tool"
chapter_number: "6"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/using_the_hammer_cli_tool/index#formatting-hammer-output"
---
# Chapter 6. Formatting Hammer output

Change the Hammer output format to simplify processing by other tools and applications. Hammer supports table, base, YAML, CSV, JSON, and silent output formats.

**Procedure**

- Set the output format with the `--output` option:

  ```
  $ hammer --output output_format organization list
  ```
- Define a custom separator for the CSV format:

  ```
  $ hammer --csv --csv-separator ";" organization list
  ```
