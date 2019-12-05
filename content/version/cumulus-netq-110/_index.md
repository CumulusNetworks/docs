---
title: Cumulus NetQ 1.1
author: Cumulus Networks
weight: -11
aliases:
 - /display/NETQ110/Cumulus+NetQ
 - /pages/viewpage.action?pageId=7111294
pageID: 7111294
product: Cumulus NetQ
version: 1.1
imgData: cumulus-netq-110
siteSlug: cumulus-netq-110
subsection: true
---
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

## What's New in NetQ 1.1.0</span>

NetQ 1.1 includes the following new features and enhancements:

  - Improved container visibility: [Docker Swarm
    integration](/version/cumulus-netq-110/Monitoring-Container-Environments-with-NetQ)
    provides service- and application-level insights in containerized
    environments.

  - [Layer 1
    support](/version/cumulus-netq-110/Monitoring-the-Physical-Layer):
    checkMonitor your physical layer, check the status of the inventory,
    check peer connections and investigate link mismatches and flapping.

  - [EVPN](https://support.cumulusnetworks.com/hc/en-us/articles/115012060387#evpn):
    Fabric-wide configuration checks and traces enhancements so you can
    verify that your overlay control plane is configured correctly.

  - [NetQ
    Notifier](/version/cumulus-netq-110/Proactively-Monitoring-the-Network-Fabric/):
    Filter alerts and notifications based on severity, device and
    service, and redirect to the desired PagerDuty and Slack channels.
    Also, exporting NetQ data to [ELK and
    Splunk](/version/cumulus-netq-110/Proactively-Monitoring-the-Network-Fabric/)
    is now generally available.

  - [Telemetry
    server](/version/cumulus-netq-110/Getting-Started-with-NetQ/): The
    telemetry server is now available as a KVM-based virtual machine,
    which runs on Ubuntu 16.04 and Red Hat Enterprise Linux 7.

  - [Standalone
    repository](Getting-Started-with-NetQ.html#src-7111298_GettingStartedwithNetQ-agent):
    NetQ packages are in their own separate repository.

  - New [check and show
    commands](https://support.cumulusnetworks.com/hc/en-us/articles/115012263348)
    for more validation options.

NetQ 1.1.0 includes [early
access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878-Early-Access-Features-Defined)
support for the following:

  - [Facebook
    Backpack](/version/cumulus-netq-110/Early-Access-Features/Facebook-Backpack-Integration)
    chassis

  - Extending NetQ with [custom
    commands](/version/cumulus-netq-110/Early-Access-Features/Extending-NetQ-with-Custom-Commands)

For further information regarding bug fixes and known issues present in
this release, refer to the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115012060387).

## NetQ Components</span>

{{% imgOld 0 %}}

NetQ comprises the following components:

  - **NetQ Agent**
    
    The back-end Python agent installed on every monitored *node* in the
    network — including Cumulus Linux switches, Linux bare-metal hosts
    and virtual machines , or Docker containers. The agent pushes out
    data to the NetQ Telemetry Server periodically, and when specific
    [`netlink`](https://wiki.linuxfoundation.org/networking/netlink)
    events occur. The agent monitors the following objects via
    `netlink`:
    
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

  - **NetQ Telemetry Server**
    
    The database/key-value store where all network information sent from
    NetQ Agents running on the network is collected, aggregated and
    queried from.

  - **NetQ Analysis Engine**
    
    The NetQ Analysis Engine is the backend engine utilized when
    querying NetQ via the CLI, service console, or notifier. The engine
    has two parts:
    
      - The **NetQ Agent Command Line Interface**. The NetQ CLI can be
        used on every node and can be used on the NetQ Telemetry Server
        through `netq-shell`.
    
      - The **NetQ Notifier**. The notifier runs on the telemetry
        server. It responds to events pushed by the NetQ Agent, sending
        alerts to a configured channel, such as Slack, PagerDuty or
        `syslog`.

  - **NetQ Service Console**
    
    The Service Console provides a browser-based window for accessing
    the NetQ CLI from anywhere.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
