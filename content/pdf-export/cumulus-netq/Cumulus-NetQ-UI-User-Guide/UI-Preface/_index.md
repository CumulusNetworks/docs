---
title: UI Preface
author: Cumulus Networks
weight: 87
aliases:
 - /display/NETQ/UI+Preface
 - /pages/viewpage.action?pageId=12321978
pageID: 12321978
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
A variety of resources are available for you to become familiar with
Cumulus NetQ and to take advantage of its monitoring and analytic
capabilities. These resources are identified here along with information
about how the content is presented.

## What's New in Cumulus NetQ 2.2

Cumulus NetQ is now available as a cloud service, making it even easier
to scale with your network growth. Just like Cumulus NetQ deployed in
your premises, real-time data collection and fabric-wide performance
analysis are available through the cloud service. New functionality has
also been added to the NetQ UI.

**Cumulus NetQ 2.2.0** includes the following new features and
improvements:

*For on-site and in-cloud solutions*

  - Graphical User Interface (UI)
      - Added ability to monitor and validate OSPF network protocol and
        services operation
      - Added ability to validate MTU, Sensors, VLAN and VXLAN protocols
      - Added events for MTU, OSPF, VLAN, and VXLAN
      - Added new standard user role, *user*, with reduced access
        permission compared to the administrative user
      - Added Prescriptive Topology Manager (PTM) events
  - Command Line Interface (CLI)
      - Included Interface Statistics as an early access feature

*For in-cloud solution only*

  - Released new Cumulus NetQ Cloud Appliance to speed deployment and
    get monitoring as quickly as possible
  - Added CLI support for installation and configuration of the Cumulus
    NetQ Cloud Appliance
  - Added support for multiple data centers

For further information regarding new
features, improvements, bug fixes, and known issues present in this
release, refer to the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/360017779214).

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

  - [Cumulus NetQ Deployment Guide](/cumulus-netq/Cumulus-NetQ-Deployment-Guide/)
  - [Cumulus NetQ CLI User Guide](/cumulus-netq/Cumulus-NetQ-CLI-User-Guide/)
  - Cumulus NetQ UI User Guide (this guide)
  - [Cumulus NetQ Release Notes](https://support.cumulusnetworks.com/hc/en-us/articles/360025451374)
  - [What the NetQ Validation System Checks](https://support.cumulusnetworks.com/hc/en-us/articles/360021961394)
  - [Cumulus NetQ Release Versioning and Support Policy](https://support.cumulusnetworks.com/hc/en-us/articles/360020782534)
  - [Cumulus NetQ Cloud Release Versioning and Support Policy](https://support.cumulusnetworks.com/hc/en-us/articles/360024807054)

This Cumulus NetQ CLI User Guide is available in [PDF](/Cumulus_NetQ_220_UI_User_Guide.pdf) for offline viewing.

## Document Formatting

This guide uses the following typographical and note conventions.

### Typographical Conventions

Throughout the guide, text formatting is
used to convey contextual information about the content.

| **Text Format**                   | **Meaning**                                                                                                                                |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <span style="color: #008000;"> Green text </span>                        | Link to additional content within the topic or to another topic                                                                                                                   |
| `Text in Monospace font`                                                 |  Filename, directory and path names, and command usage                                                                                      |
| \[`Text within square brackets`\] | Optional command parameters; may be presented in mixed case or all caps text                                                              |
| \<`Text within angle brackets`\> | Required command parameter values–variables that are to be replaced with a relevant value; may be presented in mixed case or all caps text |

### Note Conventions

Several note types are used throughout
the document. The formatting of the note indicates its intent and
urgency.

{{%notice tip%}}

Offers information to improve your
experience with the tool, such as time-saving or shortcut options, or indicates the common or
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
