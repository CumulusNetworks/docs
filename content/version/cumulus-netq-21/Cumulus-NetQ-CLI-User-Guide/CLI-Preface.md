---
title: CLI Preface
author: Cumulus Networks
weight: 29
aliases:
 - /display/NETQ21/CLI+Preface
 - /pages/viewpage.action?pageId=12321065
pageID: 12321065
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq-21
siteSlug: cumulus-netq-21
---
A variety of resources are available for you to become familiar with
Cumulus NetQ and to take advantage of its monitoring and analytic
capabilities. These resources are identified here along with information
about how the content is presented.

## What's New in Cumulus NetQ 2.1

Cumulus NetQ has been reinvented to scale with the fast adoption rate of open networks and rapid network growth. In addition to the real-time data collection and fabric-wide performance analysis that are already supported in Cumulus NetQ 1.4.1, Cumulus NetQ now offers a graphical user interface for:

- Data visualizations of the overlay and underlay networks,
- Simplified network troubleshooting with network-wide roll-ups of health and alarm status in a single card, and
- Proactive validation of the network status and configuration to regularly detect network issues.

**Cumulus NetQ 2.1.2** includes the following new features and improvements:

- Updates to the NetQ UI, including:
   - Added user-defined settings for display of date format and time zone
   - Added support for OSPF validation, both on-demand and scheduled
   - Added ability for user to change their account password
   - Updated the Events Reference to include additional events for BGP, license, sensors, and services
   - Added views of all MACs and VLANs in the network
- Updates to the NetQ CLI, including:
   - Added netq add notification proxy command to enable configuration of a proxy server for event notification management
   - Added netq show opta-health to view the status of the various applications and services running on the NetQ Platform or Appliance
   - Simplified the netq check interfaces command
- Fixes for a number of issues. See Issues Fixed in Cumulus NetQ 2.1.2 below.

**Cumulus NetQ 2.1.1** includes the following new features and improvements:

- Updates to the NetQ UI, including:
   - Added scheduled validations that let you schedule when to validate the operation of the network protocols and services running in your network
   - Added Management workbench which provides a single location to manage access to the NetQ UI, as well as view, add, and export scheduled validations and traces
   - Improved display of trace results on the full screen Trace Results card
   - Collapsed Navigation History into a menu to provide additional space for cards on the workbench
   - Added user option to display the application in a light or dark color theme
- Fixes for a number of issues. See Issues Fixed in Cumulus NetQ 2.1.1 below.
- The LNV protocol is deprecated with this NetQ release. It is supported only through the NetQ CLI and API for users on Cumulus Linux 3.7.x and earlier.

**Cumulus NetQ 2.1.0** includes the following new features and improvements:

- Modern microservices architecture enables scalable and agile network with real-time data collection
- Supports up to 1,000 nodes
- Graphical User Interface (UI) provides a visual representation of the health and operation of the network, network devices and events
   - Monitor network-wide health
   - Monitor individual device health and configuration
   - View network devices inventory and device component inventory
   - Monitor and validate network protocol and services operation
   - Track alarms and informational events across the network and for individual devices and components, protocols and services
   - Monitor connectivity with network tracing
   - Customize your own monitoring workbench to meet your needs
   - RESTful API provides access to data for use in third-party analytic tools
   - NetQ Appliance with the NetQ Platform pre-installed to speed deployment and get monitoring as quickly as possible
- Several CLI improvements have been made. To view all changes, refer to the CLI user guide.
   - Instead of using the `netq show commands` to display changes between two points in time, a new `netq show events` command is available to see these changes.
   - The `netq config ts` commands used to configure the Telemetry Server has been deprecated. `netq config` commands remain for local file-based configuration and netq notification commands have been added for configuring event notifications.
   - Timestamps which indicate when a change occurred are displayed as an absolute time (Mon Feb 4 07:23:18 2019) versus relative to the current time (0d:2h:58m:34s ago). Uptimes remain relative to the current time.

Features supported in Cumulus NetQ 1.4.1 and earlier continue to be supported, with the following exceptions:

- The early access features provided with NetQ 1.4 that were not fully productized are not available with this release.
   - Extension of NetQ CLI with custom commands
   - NetQL, query language for directly accessing the database. This data will be available through the NetQ UI or API over time.
   - Export of interface statistics to third-party analytics tools (like Grafana). This data will be available through the NetQ UI or API over time.
   - Image and Provisioning Management (IPM) application. Life cycle management is in development for a future release.
- Support for Docker and Docker Swarm. Use Kubernetes to manage containers instead.
- `netq-shell` command. A subset of NetQ commands had to be run on the Telemetry Server. Commands that ran on the Telemetry Server have been removed and the replacement commands can be run from any node.
- Service Console. Web-based UI access to the CLI is not currently available. Access the CLI directly through a terminal window.

For further information regarding new features, improvements, bug fixes,
and known issues present in this release, refer to the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/360025451374).

## Available Documentation

The NetQ documentation set has been reorganized and updated from prior
releases. They still provide the information you need to proactively
monitor your Linux-based network fabric using Cumulus NetQ. They assume
that you have already installed Cumulus Linux and NetQ.

You may start anywhere in the documentation or read it from start to
finish depending on your role and familiarity with the NetQ software and
Linux networking. If you are new to NetQ, you may want to read the
Cumulus NetQ Primer before reading the other available documents.

The following NetQ documents are available:

  - [Cumulus NetQ Deployment Guide](/version/cumulus-netq-21/Cumulus-NetQ-Deployment-Guide/)

  - Cumulus NetQ CLI User Guide (this guide)

  - [Cumulus NetQ UI User Guide](/version/cumulus-netq-21/Cumulus-NetQ-UI-User-Guide/)

  - [Cumulus NetQ Release Notes](https://support.cumulusnetworks.com/hc/en-us/articles/360025451374)

  - [What the NetQ Validation System Checks](https://support.cumulusnetworks.com/hc/en-us/articles/360021961394)

  - [Cumulus NetQ Release Versioning and Support Policy](https://support.cumulusnetworks.com/hc/en-us/articles/360020782534)

  - [Cumulus NetQ Cloud Release Versioning and Support Policy](https://support.cumulusnetworks.com/hc/en-us/articles/360024807054)

## Document Formatting

This guide uses the following typographical and note conventions.

### Typographical Conventions

Throughout the guide, text formatting is used to convey contextual information about the content.

| **Text Format** | **Meaning** |
| --------------- | ----------- |
| <span style="color: #008000;"> Green text </span> | Link to additional content within the topic or to another topic |
| `Text in Monospace font` | Filename, directory and path names, and command usage |
| \[`Text within square brackets`\] | Optional command parameters; may be presented in mixed case or all caps text |
| \<`Text within angle brackets`\> | Required command parameter values–variables that are to be replaced with a relevant value; may be presented in mixed case or all caps text |

### Note Conventions

Several note types are used throughout
the document. The formatting of the note indicates its intent and
urgency.

{{%notice tip%}}

Offers information to improve your experience with the tool, such as time-saving or shortcut options, or indicates the common or recommended method for performing a particular task or process

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

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
