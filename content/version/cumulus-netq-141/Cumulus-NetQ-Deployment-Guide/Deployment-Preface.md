---
title: Deployment Preface
author: Cumulus Networks
weight: 87
aliases:
 - /display/NETQ141/Deployment+Preface
 - /pages/viewpage.action?pageId=10453422
pageID: 10453422
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
A variety of resources are available for you to become familiar with
Cumulus NetQ and aid in its deployment. These are identified here along
with information about how the content is presented.

## What's New in Cumulus NetQ 1.4.0

Cumulus NetQ 1.4.0 includes the following new features and updates:

  - Added

      - support for monitoring up to 200 Cumulus Linux nodes
      - validation of symmetric VXLAN routes through CLI
      - validation of forward error correction (FEC) operation through
        NetQL

  - Updated

      - color cues for `netq show services` command to more easily view
        status of services at a glance
      - NetQ CLI syntax for creating NetQ Notifier filters t o improve
        usability and operation
      - trace functionality to improve usability and operation

  - Early access feature

      - Image and Provisioning Management (IPM) application

For further information regarding bug fixes and known issues present in
this release, refer to the [release notes](https://support.cumulusnetworks.com/hc/en-us/articles/360005898274).

## Available Documentation

The NetQ
documentation set has been reorganized and updated from prior releases.
They still provide the information you need to proactively monitor your
Linux-based network fabric using Cumulus NetQ. They assume that you have
already installed Cumulus Linux and NetQ.

You may
start anywhere in the documentation or read it from start to finish
depending on your role and familiarity with the NetQ software and Linux
networking. If you are
new to NetQ, you may want to read the Cumulus NetQ Primer before reading
the other available documents.

The following NetQ documents are
available:

  - [Cumulus NetQ Primer](/version/cumulus-netq-141/)
  - Cumulus NetQ Deployment Guide (this guide)
  - [Cumulus NetQ Telemetry User Guide](/version/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/)
  - [Cumulus NetQ Image and Provisioning Management User Guide](/version/cumulus-netq-141/Cumulus-NetQ-Image-and-Provisioning-Management-User-Guide/)
  - [Cumulus NetQ Release Notes](https://support.cumulusnetworks.com/hc/en-us/articles/360005898274)
  - [Cumulus NetQ Data Sheet](https://cumulusnetworks.com/learn/web-scale-networking-resources/product-collateral/netq-data-sheet/)

## Document Formatting

The Cumulus NetQ Deployment Guide uses the following typographical and
note conventions.

### Typographical Conventions

Throughout the guide, text formatting is used to convey contextual information about the content.

| **Text Format** | **Meaning ** |
| --------------- | ------------ |
| <span style="color: #008000;"> Green text</span> | Link to additional content within the topic or to another topic  |
| `Text in Monospace font`  | Filename, directory and path names, and command usage |
| \[`Text within square brackets`\]  | Optional command parameters; may be presented in mixed case or all caps text |
| \<`Text within angle brackets`\>   | Required command parameter values–variables that are to be replaced with a relevant value; may be presented in mixed case or all caps text  |

### Note Conventions

Several note types are used throughout the document. The formatting of the note indicates its intent and
urgency.

{{%notice tip%}}

Offers information to improve your experience with the tool, such as time-saving or shortcut options, or indicates the common or
recommended method for performing a particular task or process

{{%/notice%}}

{{%notice note%}}

Provides additional information or a reminder about a task or process
that may impact your next step or selection

{{%/notice%}}

{{%notice info%}}

Advises that failure to take or avoid specific action can result in
possible data loss

{{%/notice%}}

{{%notice warning%}}

Advises that failure to take or avoid specific action can result in
possible physical harm to yourself, hardware equipment, or facility

{{%/notice%}}
