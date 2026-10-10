---
title: "Data representation in Hammer options"
product: "Red Hat Satellite"
version: "6.19"
guide: "hammer_reference"
guide_title: "Hammer reference"
chapter_number: "1"
section_type: "chapter"
source_url: "https://docs.redhat.com/en/documentation/red_hat_satellite/6.19/html-single/hammer_reference/index#data-representation-in-hammer-options"
---
# Chapter 1. Data representation in Hammer options

Hammer options accept the following types and values.

BOOLEAN
:   One of true/false, yes/no, 1/0

DATETIME
:   Date and time in YYYY-MM-DD HH:MM:SS or ISO 8601 format

ENUM
:   Possible values are described in the option’s description

FILE
:   Path to a file

KEY_VALUE_LIST
:   Comma-separated list of key=value. JSON is acceptable and preferred way for such parameters

LIST
:   Comma separated list of values. Values containing comma should be quoted or escaped with backslash. JSON is acceptable and preferred way for such parameters

MULTIENUM
:   Any combination of possible values described in the option’s description

NUMBER
:   Numeric value. Integer

SCHEMA
:   Comma separated list of values defined by a schema. JSON is acceptable and preferred way for such parameters

VALUE
:   Value described in the option’s description. Mostly simple string
