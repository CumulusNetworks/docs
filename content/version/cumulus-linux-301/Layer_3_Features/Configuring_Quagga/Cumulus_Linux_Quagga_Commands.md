---
title: Cumulus Linux Quagga Commands
author: Cumulus Networks
weight: 267
aliases:
 - /display/CL30/Cumulus+Linux+Quagga+Commands
 - /pages/viewpage.action?pageId=5118387
pageID: 5118387
product: Cumulus Linux
version: '3.0'
imgData: cumulus-linux-301
siteSlug: cumulus-linux-301
---
Using the `vtysh` modal CLI is the primary way to [configure
Quagga](/version/cumulus-linux-301/Layer_3_Features/Configuring_Quagga/)
in Cumulus Linux. However, an alternative exists in the form of a
non-modal CLI containing a suite of Cumulus Linux-specific commands,
structured similar to the Linux `ip` command. The available commands are
as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Command</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>cl-bgp</p></td>
<td><p><a href="/version/cumulus-linux-301/Layer_3_Features/Border_Gateway_Protocol_-_BGP">BGP</a> commands. See <code>man cl-bgp </code>for details.</p></td>
</tr>
<tr class="even">
<td><p>cl-ospf</p></td>
<td><p><a href="/version/cumulus-linux-301/Layer_3_Features/Open_Shortest_Path_First_-_OSPF_-_Protocol">OSPFv2</a> commands. For example:<br />
<code>cumulus@switch:~$ sudo cl-ospf area 0.0.0.1 range 10.10.10.0/24</code></p></td>
</tr>
<tr class="odd">
<td><p>cl-ospf6</p></td>
<td><p><a href="/version/cumulus-linux-301/Layer_3_Features/Open_Shortest_Path_First_v3_-_OSPFv3_-_Protocol">OSPFv3</a> commands.</p></td>
</tr>
<tr class="even">
<td><p>cl-ra</p></td>
<td><p>Route advertisement commands. See <code>man cl-ra</code> for details.</p></td>
</tr>
<tr class="odd">
<td><p>cl-rctl</p></td>
<td><p>Zebra and non-routing protocol-specific commands. See <code>man cl-rctl</code> for details.</p></td>
</tr>
</tbody>
</table>

## <span>Comparing vtysh and Cumulus Linux Commands</span>

This section describes how you can use the various Cumulus Linux CLI
commands to configure Quagga, without using `vtysh`.

### <span>Displaying the Routing Table</span>

To display the routing table under Quagga, you would run:

    switch# show ip route

To display the routing table with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-rctl route

### <span>Creating a New Neighbor</span>

To create a new neighbor under Quagga, you would run:

    switch(config)# router bgp 65002
    switch(config-router)# neighbor 14.0.0.22 remote-as 65007

To create a new neighbor with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-bgp as 65002 neighbor add 14.0.0.22 remote-as 65007

### <span>Redistributing Routing Information</span>

To redistribute routing information from static route entries into RIP
tables under Quagga, you would run:

    switch(config)# router bgp 65002
    switch(config-router)# redistribute static

To redistribute routing information from static route entries into RIP
tables with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-bgp as 65002 redistribute add static

### <span>Defining a Static Route</span>

If you intend to use static routes, you only need to enable the `zebra`
daemon.

To define a static route under Quagga, you would run:

    switch(config)# ip route 155.1.2.20/24 br2 45

To define a static route with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-rctl ip route add 175.0.0.0/28 interface br1 distance 25

### <span>Configuring an IPv6 Interface</span>

To configure an IPv6 address under Quagga, you would run:

    switch(config)# int br3
    switch(config-if)# ipv6 address  3002:2123:1234:1abc::21/64

To configure an IPv6 address with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-rctl interface add swp3 ipv6 address 3002:2123:abcd:2120::41/64

### <span>Enabling PTM</span>

To enable topology checking (PTM) under Quagga, you would run:

    switch(config)# ptm-enable

To enable topology checking (PTM) with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-rctl ptm-enable set

### <span>Configuring MTU in IPv6 Network Discovery</span>

To configure
[MTU](Layer_1_and_Switch_Port_Attributes.html#src-5118373_Layer1andSwitchPortAttributes-mtu)
in IPv6 network discovery for an interface under Quagga, you would run:

    switch(config)# int swp3
    switch(config-if)# ipv6 nd mtu 9000

To configure MTU in IPv6 network discovery for an interface with the
Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ra interface swp3 set mtu 9000

### <span>Logging OSPF Adjacency Changes</span>

To log adjacency of OSPF changes under Quagga, you would run:

    switch(config)# router ospf
    switch(config-router)# router-id 2.0.0.21
    switch(config-router)# log-adjacency-changes

To log adjacency changes of OSPF with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ospf log-adjacency-changes set
    cumulus@switch:~$ sudo cl-ospf router-id set 3.0.0.21

### <span>Setting OSPF Interface Priority</span>

To set the OSPF interface priority under Quagga, you would run:

    switch(config)# int swp3
    switch(config-if)# ip ospf priority  120

To set the OSPF interface priority with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ospf interface set swp3 priority 120

### <span>Configuring Timing for OSPF SPF Calculations</span>

To configure timing for OSPF SPF calculations under Quagga, you would
run:

    switch(config)# router ospf6
    switch(config-ospf6)# timer throttle spf 40 50 60

To configure timing for OSPF SPF calculations with the Cumulus Linux
CLI, run:

    cumulus@switch:~$ sudo cl-ospf6 timer add throttle spf 40 50 60

### <span>Configuring Hello Packet Intervals</span>

To configure the OSPF Hello packet interval in number of seconds for an
interface under Quagga, you would run:

    switch(config)# int swp4
    switch(config-if)# ipv6 ospf6 hello-interval  60

To configure the OSPF Hello packet interval in number of seconds for an
interface with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ospf6 interface set swp4 hello-interval 60

### <span>Displaying OSPF Debugging Status</span>

To display OSPF debugging status under Quagga, you would run:

    switch# show debugging ospf

To display OSPF debugging status with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-ospf debug show

### <span>Displaying BGP Information</span>

To display BGP information under Quagga, you would run:

    switch# show ip bgp summary

To display BGP information with the Cumulus Linux CLI, run:

    cumulus@switch:~$ sudo cl-bgp summary
