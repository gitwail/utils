---
title: "Working efficiently with Satellite web UI"
product: "Red Hat Satellite"
version: "6.19"
guide: "administering_red_hat_satellite"
guide_title: "Administering Red Hat Satellite"
chapter_number: "20"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/administering_red_hat_satellite/index#working-efficiently-with-web-ui"
---
# Chapter 20. Working efficiently with Satellite web UI

The Satellite web UI includes search, bookmarking, keyboard shortcuts, and various settings to help you work more efficiently.

## 20.1. Efficiency tips for Satellite web UI

Use these keyboard shortcuts and techniques to navigate and search more efficiently in the Satellite web UI.

`Ctrl + Shift + F` focuses the vertical navigation search bar
:   After pressing this shortcut, you can start typing in the vertical navigation search bar.

`/` focuses the page search bar
:   After pressing this shortcut, you can start typing in the page search bar.

Saving searches as bookmarks
:   You can save a search you frequently use as a bookmark. After entering your search query in the search field, click the arrow next to the **Search** button and select **Bookmark this search**. You can then give the bookmark a name and choose whether to make it public or private.

    To manage all bookmarks, navigate to **Administer** > **Bookmarks**.

Compact table mode
:   Navigate to the user menu in the top bar and select **My account**. Under the **UI Preferences** tab, you can enable compact table mode. With compact table mode enabled, Satellite web UI displays table rows with less space between items.

**Instance title** setting
:   If you have multiple Satellite instances, you can configure Satellite web UI to always show a banner with the instance title in the top bar to help you identify which instance you are currently using. To set an instance title, navigate to **Administer** > **Settings**, and edit the **Instance title** setting on the **General** tab. To set a color for the instance title banner, edit the **Instance color** setting.

## 20.2. Satellite web UI search query reference

Use search query syntax and operators in the Satellite web UI to filter lists of resources on Satellite web UI pages. Parameter-based queries help you find the resources you need faster and more precisely than free-text search in large inventories.

Search queries in the page search bar follow the pattern:

```
parameter operator value
```

To search text with whitespaces, enclose it in quotes:

```
hostgroup = "Web Servers"
```

Typing without specifying a parameter searches across multiple fields simultaneously, also known as free-text search. For example, typing `64` in the search bar on the hosts page displays all hosts that have `64` in their name, IP address, MAC address, and architecture.

> **Note**
>
> Free text search is slower and less accurate than parameter-based queries. Use specific parameters whenever possible for better performance and precision.

The search bar supports multiple date and time formats, including the following:

- "10 January 2017"
- "10 Jan 2017"
- 10-January-2017
- 10/January/2017
- "January 10, 2017"
- Today, yesterday, and similar keywords

Table 20.1. Comparison operators accepted by search

| Operator | Short Name | Description |
| --- | --- | --- |
| = | EQUALS | Accepts numerical, temporal, or text values. For text, exact case sensitive matches are returned. |
| != | NOT EQUALS |
| ~ | LIKE | Accepts text or temporal values. The search is not case-sensitive. Accepts the following wildcards: _ for a single character, % or * for any number of characters including zero. If no wildcard is specified, the string is treated as if surrounded by wildcards: %rhel7% |
| !~ | NOT LIKE |
| > | GREATER THAN | Accepts numerical or temporal values. For temporal values, the operator > is interpreted as "later than", and < as "earlier than". Both operators can be combined with EQUALS: >= <= |
| < | LESS THAN |
| ^ | IN | Compares an expression against a list of values, as in SQL. Returns matches that contain or not contain the values, respectively. |
| !^ | NOT IN |
| HAS or set? |  | Returns values that are present or not present, respectively. |
| NOT HAS or null? |  |

Table 20.2. Logical operators accepted by search

| Operator | Alternative Notations | | |
| --- | --- | --- | --- |
| and | & | && | <whitespace> |
| or | | | || |  |
| not | – | ! |  |

## 20.3. Useful search examples

The following examples demonstrate useful ways to filter and find resources in Satellite web UI. Use them as starting points to build your own searches that match your specific needs.

These search examples show how to filter hosts and are based on host attribute search parameters. You can use them on Satellite web UI pages that list hosts, such as **Hosts** > **All Hosts**. You can apply the same syntax to filter other resources on other Satellite web UI pages.

Find hosts by host global status and sub-status
:   Hosts that have an **OK** global status:

    ```
    global_status = ok
    ```

    Hosts that have an **Error** or **Warning** global status:

    ```
    global_status = error or global_status = warning
    ```

    Hosts that have at least one pending resource:

    ```
    status.pending > 0
    ```

    Hosts that restarted some service during last run:

    ```
    status.restarted > 0
    ```

    Hosts that have an interesting last run that might indicate something has happened:

    ```
    status.interesting = true
    ```

Find hosts that need attention
:   Hosts with security updates available:

    ```
    errata_status = security_needed
    ```

    Hosts that have email notifications for configuration errors enabled and are in a failed state:

    ```
    status.enabled = true AND status.failed = true
    ```

    Hosts that have not generated a report recently:

    ```
    last_report < "7 days ago"
    ```

Find hosts by configuration, environment, or registration date
:   Hosts in production that belong to a host group whose name includes a variation of the word "webservers":

    ```
    environment = production AND hostgroup ~ webservers
    ```

    Hosts registered in the last month:

    ```
    registered_at > "30 days ago"
    ```

    Hosts registered between specific dates:

    ```
    registered_at > 1-January-2026 AND registered_at < 31-January-2026
    ```

Exclude specific results
:   All hosts except hosts in a host group named "exceptions":

    ```
    NOT hostgroup = exceptions
    ```

    Hosts that are not compliant with policies:

    ```
    compliance_status != compliant
    ```

Use wildcards for flexible matching
:   Hosts with names that include the strings "web" and "prod":

    ```
    name ~ web*prod*
    ```

    Host groups starting with a specific prefix:

    ```
    hostgroup ~ rhel%
    ```
