---
title: "Expense management for Red Hat subscriptions"
product: "Red Hat Satellite"
version: "6.19"
guide: "overview_concepts_and_deployment_considerations"
guide_title: "Overview, concepts, and deployment considerations"
chapter_number: "4"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#expense-management-for-red-hat-subscriptions"
---
# Chapter 4. Expense management for Red Hat subscriptions

Red Hat provides you with several tools to control costs and optimize spending on Red Hat subscriptions.

## 4.1. Subscriptions usage data

For the purposes of expense management and to optimize your spending, track your subscriptions usage data that you can get from your Satellite environment and Red Hat. You can track usage, capacity, and utilization of your Red Hat subscriptions.

Usage
:   Measures the consumption of installed Red Hat products.

    This data tells you: How much am I using? For example: I have 42 hypervisors, each with 2 sockets, tagged with the Production usage type.

Capacity
:   Measures the amount of Red Hat products that have been purchased. It is the upper limit of usage.

    This data tells you: How much have I purchased? For example: I purchased QTY 52 of RH00001. Each RH00001 covers a 2-socket hypervisor and all of its guests.

Utilization
:   Measures how much of the purchased capacity has been exhausted.

    This data tells you: How much of my capacity is being used? For example: I am using 42 of my 52 RH00001, leaving 10 free for additional use.

**Additional resources**

- [How to use the subscription data in the views in *Getting Started with the Subscriptions Service*](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_the_subscriptions_service)

## 4.2. Subscriptions tracking tools

You can track subscriptions usage by combining the following tools.

System Purpose
:   Defines non-technical system attributes for hosts to aid accurate inventory reporting:

    - Service Level Agreement (SLA): Self-Support, Standard, Premium
    - Usage type: Production, Development/Test
    - Role: Server, Workstation

    System purpose is configured by using the Subscription Manager tool.

Insights client
:   Collects data from hosts and sends it to Satellite. Satellite then forwards the data and host inventory to the Red Hat Hybrid Cloud Console for analysis. You can install the Insights client on hosts and Satellite Server.

Subscriptions service
:   Provides capacity data, calculates utilization, and reports subscription usage in connected scenarios. This service is hosted on the [Red Hat Hybrid Cloud Console](https://console.redhat.com) and is not available in disconnected environments.

Red Hat Satellite
:   Provides reports on products installed on hosts. You can download these reports in various formats, such as YAML, JSON, HTML, and CSV. You can use these reports to calculate utilization locally.

## 4.3. Subscriptions tracking scenarios

You can track your subscription usage in one of the following scenarios, depending on your environment and data sensitivity.

Connected scenario
:   You share all collected data with Red Hat.

    - Satellite uploads inventory data to the Red Hat Hybrid Cloud Console automatically.
    - Red Hat Hybrid Cloud Console provides all services.
    - Services powered by Red Hat Lightspeed analyze the data.
    - Subscriptions service in the Red Hat Hybrid Cloud Console calculates utilization data.

Connected data-sensitive scenario
:   You share just enough data with Red Hat to enable subscription reporting.

    - You control what data is uploaded by enabling obfuscation or exclusion settings.
    - Satellite uploads inventory data to the Red Hat Hybrid Cloud Console automatically.
    - Red Hat Hybrid Cloud Console provides limited services.
    - Subscriptions service in the Red Hat Hybrid Cloud Console calculates utilization data.

Disconnected scenario
:   You do not share any data with Red Hat. Instead, you track your subscription usage as follows:

    - You can get usage data from the **Host - Installed Products** report in Satellite.
    - You can get capacity data from the Subscriptions service in the Red Hat Hybrid Cloud Console.
    - You can calculate utilization data locally using a tool of your choosing.

## 4.4. Additional resources

You can use the following additional resources.

- [Section 11.11, “Subscriptions tracking configuration”](https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/overview_concepts_and_deployment_considerations/index#subscriptions-tracking-configuration "11.11. Subscriptions tracking configuration")
- [Maximize Your RHEL Subscription Benefits (YouTube video)](https://www.youtube.com/watch?v=zREEfPWqAo8&t=983s)
- [*Getting Started with the Subscriptions Service*](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_the_subscriptions_service)
- [Policies and guidelines: Red Hat subscription model FAQ](https://www.redhat.com/en/about/subscription-model-faq)
