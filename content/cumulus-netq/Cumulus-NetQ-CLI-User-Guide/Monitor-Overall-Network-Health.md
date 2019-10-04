---
title: Monitor Overall Network Health
author: Cumulus Networks
weight: 33
aliases:
 - /display/NETQ/Monitor+Overall+Network+Health
 - /pages/viewpage.action?pageId=12321047
pageID: 12321047
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
---
NetQ provides the information you need to monitor the health of your
network fabric, devices, and interfaces. You are able to easily validate
the operation and view the configuration across the entire network from
switches to hosts to containers. For example, you can monitor the
operation of routing protocols and virtual network configurations, the
status of NetQ Agents and hardware components, and the operation and
efficiency of interfaces. When issues are present, NetQ makes it easy to
identify and resolve them. You can also see when changes have occurred
to the network, devices, and interfaces by viewing their operation,
configuration, and status at an earlier point in time.

## Validate Network Health

NetQ `check` commands validate the various elements of your network
fabric, looking for inconsistencies in configuration across your fabric,
connectivity faults, missing configuration, and so forth, and then and
display the results for your assessment. They can be run from any node
in the network.

### Validate the Network Fabric

You can validate the following network fabric elements:

```
cumulus@switch:/$ netq check 
    agents      :  Netq agent
    bgp         :  BGP info
    cl-version  :  Cumulus Linux version
    clag        :  Cumulus Multi-chassis LAG
    evpn        :  EVPN
    interfaces  :  network interface port
    license     :  License information
    lnv         :  Lightweight Network Virtualization info
    mtu         :  Link MTU
    ntp         :  NTP
    ospf        :  OSPF info
    sensors     :  Temperature/Fan/PSU sensors
    vlan        :  VLAN
    vxlan       :  VXLAN data path
```

For example, to determine the status of BGP running on your network:

    cumulus@switch:~$ netq check bgp
    Total Nodes: 15, Failed Nodes: 0, Total Sessions: 16, Failed Sessions: 0

You can see from this output that NetQ has validated the connectivity
and configuration of BGP across all of the nodes in the network and
found them all to be operating properly. If there were issues with any
of the nodes, NetQ would provide information about each node to aid in
resolving the issues.

There is a check command for each of the supported fabric elements. They
all behave in a similar manner, checking for connectivity,
configuration, and other problems, indicating the number of nodes that
they have checked and indicating the number that have failed.

Some additional examples—

Validate that EVPN is running correctly on all nodes:

    cumulus@switch:~$ netq check evpn
    Total Nodes: 15, Failed Nodes: 0, Total Sessions: 0, Failed Sessions: 0, Total VNIs: 0

Confirm all monitored nodes are running the NetQ Agent:

    cumulus@switch:~$ netq check agents
    Checked nodes: 25, Rotten nodes: 1
    Hostname          Status           Last Changed
    ----------------- ---------------- -------------------------
    leaf01            Rotten           8d:13h:34m:51s

Validate that all corresponding interface links have matching MTUs. The
first shows no mismatches, the second shows an error.

    cumulus@switch:~$ netq check mtu
    Checked Nodes: 15, Checked Links: 138, Failed Nodes: 0, Failed Links: 0
    No MTU Mismatch found
     
    cumulus@switch:~$ netq check mtu
    Checked Nodes: 13, Checked Links: 173, Failed Nodes: 1, Failed Links: 1
    MTU mismatch found on following links
    Hostname          Interface                 MTU    Peer              Peer Interface            Peer MTU Error
    ----------------- ------------------------- ------ ----------------- ------------------------- -------- ---------------
    leaf01            -                         -      -                 -                         -        Rotten Agent

Validate that VXLANs are configured and operating properly:

    cumulus@switch:~$ netq check vxlan 
    Checked Nodes: 6, Warning Nodes: 0, Failed Nodes: 6
    Nodes with error
    Hostname         Reason
    ---------------- ----------------------------------------------------------------
    exit01           inconsistent replication list for vni 104001                    
    exit02           inconsistent replication list for vni 104001                    
    leaf01           inconsistent replication list for vni 104001                    
    leaf02           inconsistent replication list for vni 104001                    
    leaf03           inconsistent replication list for vni 104001                    
    leaf04           inconsistent replication list for vni 104001                    

{{%notice tip%}}

Both asymmetric and symmetric VXLAN configurations are validated with
this command.

{{%/notice%}}

You can be more granular in your validation as well, using the
additional options available for each of the check commands. For
example, validate BGP operation for nodes communicating over a
particular VRF:

```
cumulus@switch:~$ netq check bgp vrf DataVrf1081
Total Nodes: 25, Failed Nodes: 1, Total Sessions: 52 , Failed Sessions: 1
Hostname          VRF             Peer Name         Peer Hostname     Reason                                        Last Changed
----------------- --------------- ----------------- ----------------- --------------------------------------------- -------------------------
exit-1            DataVrf1081     swp7.3            firewall-2        BGP session with peer firewall-2 (swp7.3 vrf  1d:5h:47m:31s
                                                                      DataVrf1081) failed,                         
                                                                      reason: Peer not configured      
```

Each of the check commands provides a starting point for troubleshooting
configuration and connectivity issues within your network in real time.
They provide an additional option of viewing the network state at an
earlier time, using the `around` option.

For example, if you were notified of an issue on your VLANs that appears
to have occurred about 10 minutes ago, you could run:

    cumulus@switch:~$ netq check vlan around 10m
    Checked Nodes: 15, Checked Links: 138, Failed Nodes: 0, Failed Links: 0
    No VLAN or PVID Mismatch found

### Validate Device Status and Configuration

You can validate the following device elements:

  - NTP
  - Sensors
  - License

It is always important to have your devices in time synchronization to
ensure configuration and management events can be tracked and
correlations can be made between events. To validate time
synchronization, run:

    cumulus@switch:~$ netq check ntp
    Total Nodes: 15, Checked Nodes: 15, Rotten Nodes: 0, Unknown Nodes: 0, failed NTP Nodes: 8
    Hostname          NTP Sync Connect Time
    ----------------- -------- -------------------------
    exit01            no       2018-09-12 16:30:39      
    exit02            no       2018-09-12 16:30:45      
    leaf01            no       2018-09-12 16:30:43      
    leaf02            no       2018-09-12 16:30:36      
    leaf03            no       2018-09-12 16:30:36      
    leaf04            no       2018-09-12 16:30:34      
    spine01           no       2018-09-12 16:30:44      
    spine02           no       2018-09-12 16:30:40      

This example shows eight nodes that are not in time synchronization. You
can now continue to investigate these nodes, validating that the NetQ
Agents are active, whether an NTP server has become unreachable, and so
forth.

Hardware platforms have a number sensors to provide environmental data
about the switches. Knowing these are all within range is a good check
point for maintenance. For example, if you had a temporary HVAC failure
and you are concerned that some of your nodes are beginning to overheat,
you can run:

    cumulus@switch:~$ netq check sensors
    Total Nodes: 25, Failed Nodes: 0, Checked Sensors: 221, Failed Sensors: 0

You can also check for any nodes that have invalid licenses without
going to each node. Because switches do not operate correctly without a
valid license you might want to verify that your Cumulus Linux licenses
on a regular basis:

    cumulus@switch:~$ netq check license
    Total Nodes: 15, Failed Nodes: 0, Checked Licenses: 10, Failed Licenses: 0

{{%notice tip%}}

This command checks every node, meaning every switch and host in the
network. Hosts do not require a Cumulus Linux license, so the number of
licenses checked might be smaller than the total number of nodes
checked.

{{%/notice%}}

### Validate Interface Status and Configuration

As with other `netq check` commands, you can validate the proper
operation of your interfaces across the network:

    cumulus@switch:~$ netq check interfaces 
    Checked Nodes: 15, Failed Nodes: 8
    Checked Ports: 118, Failed Ports: 8, Unverified Ports: 94
    Hostname          Interface                 Peer Hostname     Peer Interface            Message
    ----------------- ------------------------- ----------------- ------------------------- -----------------------------------
    leaf01            swp7                      firewall02        swp3                      Speed mismatch (10G, n/a),         
                                                                                            Autoneg mismatch (off, n/a)          
    leaf02            swp2                      server02          eth2                      Autoneg mismatch (off, on)         
    leaf03            swp1                      server03          eth1                      Autoneg mismatch (off, on)         
    leaf04            swp2                      server04          eth2                      Autoneg mismatch (off, on)         
    server01          eth1                      leaf01            swp1                      Autoneg mismatch (on, off)         
    server02          eth2                      leaf02            swp2                      Autoneg mismatch (on, off)         
    server03          eth1                      leaf03            swp1                      Autoneg mismatch (on, off)         
    server04          eth2                      leaf04            swp2                      Autoneg mismatch (on, off)         

When failures are seen, additional information is provided to start your
investigation. In this example, some reconfiguration is required for
auto-negotiation with peer interfaces.

### Create Filters for Provisioning Exceptions

With this release, you are able to configure filters to change validation errors to warnings that would normally occur due to the default expectations of the `netq check` commands. This applies to all protocols and services, except for Agents and LNV. For example, if you have provisioned BGP with configurations where a BGP peer is not expected or desired, you will get errors that a BGP peer is missing. By creating a filter, you can remove the error in favor of a warning.

To create a validation filter:

1. Navigate to the */etc/netq* directory.

2. Create or open the *check_filter.yml*  file using your text editor of choice.

    This file contains the syntax to follow to create one or more rules for one or more protocols or services. Create your own rules, and/or edit and un-comment any example rules you would like to use.

    ```
    # Netq check result filter rule definition file.  This is for filtering
    # results based on regex match on one or more columns of each test result.
    # Currently, only action 'filter' is supported. Each test can have one or
    # more rules, and each rule can match on one or more columns.  In addition,
    # rules can also be optionally defined under the 'global' section and will
    # apply to all tests of a check.
    #
    # syntax:
    #
    # <check name>:
    #   tests:
    #     <test name, as shown in test list when using the include/exclude and tab>:
    #       - rule:
    #           match:
    #             <column name>: regex
    #             <more columns and regex.., result is AND>
    #           action:
    #             filter
    #       - <more rules..>
    #   global:
    #     - rule:
    #         . . .
    #     - rule:
    #         . . .
    #
    # <another check name>:
    #   . . .
    #
    # e.g.
    #
    # bgp:
    #   tests:
    #     Address Families:
    #       - rule:
    #           match:
    #             Hostname: (^exit*|^firewall)
    #             VRF: DataVrf1080
    #             Reason: AFI/SAFI evpn not activated on peer
    #           action:
    #             filter
    #       - rule:
    #           match:
    #             Hostname: exit-2
    #             Reason: SAFI evpn not activated on peer
    #           action:
    #             filter
    #     Router ID:
    #       - rule:
    #           match:
    #             Hostname: exit-2
    #           action:
    #             filter
    #
    # evpn:
    #   tests:
    #     EVPN Type 2:
    #       - rule:
    #           match:
    #             Hostname: exit-1
    #           action:
    #             filter
    #
    ```

## View Network Details

The `netq show` commands display a wide variety of content about the
network and its various elements. You can show content for the
following:

    cumulus@switch:~$ netq show
        agents        :  Netq agent
        bgp           :  BGP info
        clag          :  Cumulus Multi-chassis LAG
        events        :  Display changes over time
        evpn          :  EVPN
        interfaces    :  network interface port
        inventory     :  Inventory information
        ip            :  IPv4 related info
        ipv6          :  IPv6 related info
        kubernetes    :  Kubernetes Information
        lldp          :  LLDP based neighbor info
        lnv           :  Lightweight Network Virtualization info
        macs          :  Mac table or MAC address info
        notification  :  Send notifications to Slack or PagerDuty
        ntp           :  NTP
        ospf          :  OSPF info
        sensors       :  Temperature/Fan/PSU sensors
        services      :  System services
        vlan          :  VLAN
        vxlan         :  VXLAN data path

For example, to validate the the status of the NetQ agents running in
the fabric, run `netq show agents`. A *Fresh* status indicates the Agent
is running as expected. The Agent sends a heartbeat every 30 seconds,
and if three consecutive heartbeats are missed, its status changes to
*Rotten*.

```
cumulus@switch:~$ netq show agents
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
exit01            Fresh            yes      2.3.0-cl3u21~1569246310.30858c3      1d:21h:30m:19s            1d:21h:30m:9s             1d:21h:30m:9s              Tue Sep 24 22:45:03 2019
exit02            Fresh            yes      2.3.0-cl3u21~1569246310.30858c3      1d:21h:32m:1s             1d:21h:31m:51s            1d:21h:31m:51s             Tue Sep 24 22:43:35 2019
leaf01            Fresh            yes      2.3.0-cl3u21~1569246310.30858c3      1d:21h:31m:14s            1d:21h:31m:5s             1d:21h:31m:5s              Tue Sep 24 22:44:25 2019
leaf02            Fresh            yes      2.3.0-cl3u21~1569246310.30858c3      1d:21h:31m:57s            1d:21h:31m:47s            1d:21h:31m:47s             Tue Sep 24 22:44:20 2019
leaf03            Fresh            yes      2.3.0-cl3u21~1569246310.30858c3      1d:21h:31m:4s             1d:21h:30m:55s            1d:21h:30m:55s             Tue Sep 24 22:44:19 2019
leaf04            Fresh            yes      2.3.0-cl3u21~1569246310.30858c3      1d:21h:32m:37s            1d:21h:32m:28s            1d:21h:32m:28s             Tue Sep 24 22:43:05 2019
server01          Fresh            no       2.3.0-ub18.04u21~1569246309.30858c3  1d:21h:10m:50s            1d:21h:10m:38s            1d:21h:10m:38s             Tue Sep 24 22:49:10 2019
server02          Fresh            yes      2.3.0-ub18.04u21~1569246309.30858c3  1d:21h:10m:50s            1d:21h:10m:38s            1d:21h:10m:38s             Wed Sep 25 18:35:44 2019
server03          Fresh            yes      2.3.0-ub18.04u21~1569246309.30858c3  1d:21h:10m:50s            1d:21h:10m:38s            1d:21h:10m:38s             Wed Sep 25 15:37:10 2019
server04          Fresh            yes      2.3.0-ub18.04u21~1569246309.30858c3  1d:21h:10m:49s            1d:21h:10m:37s            1d:21h:10m:37s             Tue Sep 24 22:49:33 2019
spine01           Fresh            yes      2.3.0-cl3u21~1569246310.30858c3      1d:21h:30m:10s            1d:21h:30m:1s             1d:21h:30m:1s              Tue Sep 24 22:44:40 2019
spine02           Fresh            yes      2.3.0-cl3u21~1569246310.30858c3      1d:21h:30m:16s            1d:21h:30m:6s             1d:21h:30m:6s              Tue Sep 24 22:43:32 2019
```

Some additional examples follow.

View the status of BGP:

    cumulus@switch:~$ netq show bgp
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    exit01            swp44(internet)              vrf1            65041      25253      2/-/-        Fri Apr 19 16:00:40 2019
    exit01            swp51(spine01)               default         65041      65020      8/-/59       Fri Apr 19 16:00:40 2019
    exit01            swp52(spine02)               default         65041      65020      8/-/59       Fri Apr 19 16:00:40 2019
    exit02            swp44(internet)              vrf1            65042      25253      7/-/-        Fri Apr 19 16:00:40 2019
    exit02            swp51(spine01)               default         65042      65020      8/-/59       Fri Apr 19 16:00:40 2019
    exit02            swp52(spine02)               default         65042      65020      8/-/59       Fri Apr 19 16:00:40 2019
    leaf01            peerlink.4094(leaf02)        default         65011      65011      9/-/34       Fri Apr 19 16:00:40 2019
    leaf01            swp51(spine01)               default         65011      65020      6/-/34       Fri Apr 19 16:00:40 2019
    leaf01            swp52(spine02)               default         65011      65020      6/-/34       Fri Apr 19 16:00:40 2019
    leaf02            peerlink.4094(leaf01)        default         65011      65011      9/-/34       Fri Apr 19 16:00:40 2019
    leaf02            swp51(spine01)               default         65011      65020      6/-/34       Fri Apr 19 16:00:40 2019
    leaf02            swp52(spine02)               default         65011      65020      6/-/34       Fri Apr 19 16:00:40 2019
    leaf03            peerlink.4094(leaf04)        default         65012      65012      9/-/34       Fri Apr 19 16:00:40 2019
    leaf03            swp51(spine01)               default         65012      65020      6/-/34       Fri Apr 19 16:00:40 2019
    leaf03            swp52(spine02)               default         65012      65020      6/-/34       Fri Apr 19 16:00:40 2019
    leaf04            peerlink.4094(leaf03)        default         65012      65012      9/-/34       Fri Apr 19 16:00:40 2019
    leaf04            swp51(spine01)               default         65012      65020      6/-/34       Fri Apr 19 16:00:40 2019
    leaf04            swp52(spine02)               default         65012      65020      6/-/34       Fri Apr 19 16:00:40 2019
    spine01           swp1(leaf01)                 default         65020      65011      3/-/14       Fri Apr 19 16:00:40 2019
    spine01           swp2(leaf02)                 default         65020      65011      3/-/14       Fri Apr 19 16:00:40 2019
    spine01           swp29(exit02)                default         65020      65042      1/-/3        Fri Apr 19 16:00:40 2019
    spine01           swp3(leaf03)                 default         65020      65012      3/-/14       Fri Apr 19 16:00:40 2019
    spine01           swp30(exit01)                default         65020      65041      1/-/3        Fri Apr 19 16:00:40 2019
    spine01           swp4(leaf04)                 default         65020      65012      3/-/14       Fri Apr 19 16:00:40 2019
    spine02           swp1(leaf01)                 default         65020      65011      3/-/12       Fri Apr 19 16:00:40 2019
    spine02           swp2(leaf02)                 default         65020      65011      3/-/12       Fri Apr 19 16:00:40 2019
    spine02           swp29(exit02)                default         65020      65042      1/-/3        Fri Apr 19 16:00:40 2019
    spine02           swp3(leaf03)                 default         65020      65012      3/-/12       Fri Apr 19 16:00:40 2019
    spine02           swp30(exit01)                default         65020      65041      1/-/3        Fri Apr 19 16:00:40 2019
    spine02           swp4(leaf04)                 default         65020      65012      3/-/12       Fri Apr 19 16:00:40 2019

View the status of your VLANs:

    cumulus@switch:~$ netq show vlan
    Matching vlan records:
    Hostname          VLANs                     SVIs                      Last Changed
    ----------------- ------------------------- ------------------------- -------------------------
    server11          1                                                   Thu Feb  7 00:17:48 2019
    server21          1                                                   Thu Feb  7 00:17:48 2019
    server11          1                                                   Thu Feb  7 00:17:48 2019
    server13          1                                                   Thu Feb  7 00:17:48 2019
    server21          1                                                   Thu Feb  7 00:17:48 2019
    server23          1                                                   Thu Feb  7 00:17:48 2019
    leaf01            100-106,1000-1009         100-106 1000-1009         Thu Feb  7 00:17:49 2019
    leaf02            100-106,1000-1009         100-106 1000-1009         Thu Feb  7 00:17:49 2019
    leaf11            100-106,1000-1009         100-106 1000-1009         Thu Feb  7 00:17:49 2019
    leaf12            100-106,1000-1009         100-106 1000-1009         Thu Feb  7 00:17:50 2019
    leaf21            100-106,1000-1009         100-106 1000-1009         Thu Feb  7 00:17:50 2019
    leaf22            100-106,1000-1009         100-106 1000-1009         Thu Feb  7 00:17:50 2019

View the status of the hardware sensors:

    cumulus@switch:~$ netq show sensors all
     
    Matching sensors records:
    Hostname          Name            Description                         State      Message                             Last Changed
    ----------------- --------------- ----------------------------------- ---------- ----------------------------------- -------------------------
    exit01            fan1            fan tray 1, fan 1                   ok                                             Wed Feb  6 23:02:35 2019
    exit01            fan2            fan tray 1, fan 2                   ok                                             Wed Feb  6 23:02:35 2019
    exit01            fan3            fan tray 2, fan 1                   ok                                             Wed Feb  6 23:02:35 2019
    exit01            fan4            fan tray 2, fan 2                   ok                                             Wed Feb  6 23:02:35 2019
    exit01            fan5            fan tray 3, fan 1                   ok                                             Wed Feb  6 23:02:35 2019
    exit01            fan6            fan tray 3, fan 2                   ok                                             Wed Feb  6 23:02:35 2019
    exit01            psu1fan1        psu1 fan                            ok                                             Wed Feb  6 23:02:35 2019
    exit01            psu2fan1        psu2 fan                            ok                                             Wed Feb  6 23:02:35 2019
    exit02            fan1            fan tray 1, fan 1                   ok                                             Wed Feb  6 23:03:35 2019
    exit02            fan2            fan tray 1, fan 2                   ok                                             Wed Feb  6 23:03:35 2019
    exit02            fan3            fan tray 2, fan 1                   ok                                             Wed Feb  6 23:03:35 2019
    exit02            fan4            fan tray 2, fan 2                   ok                                             Wed Feb  6 23:03:35 2019
    exit02            fan5            fan tray 3, fan 1                   ok                                             Wed Feb  6 23:03:35 2019
    exit02            fan6            fan tray 3, fan 2                   ok                                             Wed Feb  6 23:03:35 2019
    exit02            psu1fan1        psu1 fan                            ok                                             Wed Feb  6 23:03:35 2019
    exit02            psu2fan1        psu2 fan                            ok                                             Wed Feb  6 23:03:35 2019
    leaf01            fan1            fan tray 1, fan 1                   ok                                             Wed Feb  6 23:01:12 2019
    leaf01            fan2            fan tray 1, fan 2                   ok                                             Wed Feb  6 23:01:12 2019
    leaf01            fan3            fan tray 2, fan 1                   ok                                             Wed Feb  6 23:01:12 2019
    leaf01            fan4            fan tray 2, fan 2                   ok                                             Wed Feb  6 23:01:12 2019
    leaf01            fan5            fan tray 3, fan 1                   ok                                             Wed Feb  6 23:01:12 2019
    leaf01            fan6            fan tray 3, fan 2                   ok                                             Wed Feb  6 23:01:12 2019
    leaf01            psu1fan1        psu1 fan                            ok                                             Wed Feb  6 23:01:12 2019
    leaf01            psu2fan1        psu2 fan                            ok                                             Wed Feb  6 23:01:12 2019
    leaf02            fan1            fan tray 1, fan 1                   ok                                             Wed Feb  6 22:59:54 2019
    leaf02            fan2            fan tray 1, fan 2                   ok                                             Wed Feb  6 22:59:54 2019
    leaf02            fan3            fan tray 2, fan 1                   ok                                             Wed Feb  6 22:59:54 2019
    leaf02            fan4            fan tray 2, fan 2                   ok                                             Wed Feb  6 22:59:54 2019
    leaf02            fan5            fan tray 3, fan 1                   ok                                             Wed Feb  6 22:59:54 2019
    ...
