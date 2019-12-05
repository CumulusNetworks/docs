---
title: Cumulus NetQ 1.2
author: Cumulus Networks
weight: -12
aliases:
 - /display/NETQ121/Cumulus+NetQ
 - /pages/viewpage.action?pageId=8356534
pageID: 8356534
product: Cumulus NetQ
version: 1.2
imgData: cumulus-netq-121
siteSlug: cumulus-netq-121
subsection: true
---
## Introducing Cumulus NetQ</span>

Cumulus NetQ is a fabric-wide, telemetry-based validation system, that
enables organizations to validate network state, both during regular
operations and for post-mortem diagnostic analysis. Running on Cumulus
Linux switches and other certified systems — such as Ubuntu, Red Hat,
and CentOS hosts — NetQ captures network data and other state
information in real time, allowing cloud architects and network
operations teams to operate with visibility over the entire network.

The system uses a three-pronged approach to validating networks:

  - **Preventative**
    
    NetQ easily validates potential network configuration changes in a
    virtualized environment or lab using check, show and trace
    algorithms, eliminating the need to check nodes one by one and
    reducing manual errors before they are rolled into production (one
    of the main causes of network downtime).

  - **Proactive**
    
    NetQ detects faulty network states that can result in packet loss or
    connectivity issues, and alerts the user with precise fault location
    data to allow for faster remediation, greatly improving network
    agility, and reducing downtime costs.

  - **Diagnostic**
    
    NetQ provides the ability to trace network paths, replay the network
    state at a time in the past, review fabric-wide event changelogs and
    diagnose the root cause of state deviations.

This documentation is current as of March 28, 2018 for version 1.2.1.
Please visit the [Cumulus Networks Web
site](http://docs.cumulusnetworks.com) for the most up to date
documentation.

Read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115015123487)
for new features and known issues in this release.

## What's New in Cumulus NetQ 1.2.1</span>

Cumulus NetQ 1.2.1 includes updates required for compatibility with
Cumulus Linux 3.5.0.

### Compatibility with Cumulus Linux</span>

Cumulus NetQ 1.2.1 is compatible with Cumulus Linux versions 3.3.0
through 3.5.z.

## What's New in NetQ 1.2.0</span>

NetQ 1.2.0 includes the following new features and enhancements:

  - [High
    availability](/version/cumulus-netq-121/Getting-Started-with-NetQ/Configuring-High-Availability-Mode):
    Configure the NetQ telemetry server in high availability mode for
    redundancy and better robustness.

NetQ 1.2.0 includes [early
access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878-Early-Access-Features-Defined)
support for the following:

  - [NetQ Query
    Language](/version/cumulus-netq-121/Early-Access-Features/Querying-the-NetQ-Database)
    (NetQL): Search for even more NetQ data using the SQL-like NetQ
    Query Language (NetQL). Run your own custom analyses or simply
    extend NetQ functionality for your specific environment.

  - [Collecting interface
    statistics](/version/cumulus-netq-121/Early-Access-Features/Collecting-Interface-Statistics):
    NetQ now provides the ability to collect counters for network
    interfaces.

For further information regarding bug fixes and known issues present in
this release, refer to the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115015123487).

## NetQ Components</span>

{{% imgOld 0 %}}

NetQ comprises the following components:

  - NetQ Agent

  - NetQ Telemetry Server

  - NetQ Analysis Engine

  - NetQ Service Console

Each is described below.

### NetQ Agent</span>

The back-end Python agent installed on every monitored *node* in the
network — including Cumulus Linux switches, Linux bare-metal hosts and
virtual machines, or Docker containers. The agent pushes out data to the
NetQ Telemetry Server periodically, and when specific
[`netlink`](https://wiki.linuxfoundation.org/networking/netlink) events
occur. The agent monitors the following objects via `netlink`:

  - interfaces

  - address (IPv4 and IPv6)

  - route (IPv4 and IPv6)

  - link

  - bridge fdb

  - IP neighbor (IPv4 and IPv6)

Further, every 15 seconds, it gathers data for the following protocols:

  - Bridging protocols (LLDP, STP, MLAG)

  - Routing protocols (BGP, OSPF)

  - Network virtualization (LNV, VXLAN data plane)

  - Docker containers

It also listens to the Docker event stream to monitor Docker containers
running on a host and gathers container networking information such as
NAT translations, networks and container IP and MAC addresses.

### NetQ Telemetry Server</span>

The database/key-value store where all network information sent from
NetQ Agents running on the network is collected, aggregated and queried
from.

### NetQ Analysis Engine</span>

The NetQ Analysis Engine is the backend engine utilized when querying
NetQ via the CLI, service console, or notifier. The engine has two
parts:

  - The **NetQ Agent Command Line Interface**. The NetQ CLI can be used
    on every node and can be used on the NetQ Telemetry Server through
    `netq-shell`.
    
    {{%notice note%}}
    
    The NetQ command line interface runs on x86 and ARM switches and
    hosts only.
    
    {{%/notice%}}

  - The **NetQ Notifier**. The notifier runs on the telemetry server. It
    responds to events pushed by the NetQ Agent, sending alerts to a
    configured channel, such as Slack, PagerDuty or `syslog`.

### NetQ Service Console</span>

The [Service Console](/version/cumulus-netq-121/NetQ-Service-Console)
provides a browser-based window for accessing the NetQ CLI from
anywhere.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
