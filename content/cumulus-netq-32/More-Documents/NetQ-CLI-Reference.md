---
title: NetQ CLI Reference
author: Cumulus Networks
weight: 1100
bookhidden: true
pdfhidden: true
---
This reference provides details about each of the NetQ CLI commands, starting with the xxx release. For an overview of the CLI structure and usage, read {{<link title="NetQ Command Line Overview">}}.

## Check Commands

All of the NetQ check commands begin with `netq check`. They are used to validate various elements in your network fabric. They are described here in alphabetical order.

### netq check agents

Collects [retrieves?] the communication status of all nodes (leafs, spines, and hosts) running the NetQ Agent in your network fabric. The output displays the total number of nodes found and how many of those have not been heard from in 90 seconds.

*Syntax*

```
netq check agents [json]
```

#### Options

| Option | Required | Description |
| ---- | ---- | ---- |
| json | No | Display the output in JSON file format instead of default on-screen text format.|

#### Command History

| Release | Description |
| ---- | ---- |
| 1.0 | Introduced |

#### Sample Usage

Find nodes in network fabric with stale communications
cumulus@switch:~$ netq check agents
Checked nodes: 11, Rotten nodes: 0
Find nodes in network fabric with stale communications and display the results in JSON format
cumulus@ts:~$ netq check agents json
{
    "failedNodes":[

    ],
    "summary":{
        "checkedNodeCount":11,
        "failedNodeCount":0
    }
}

#### Related Commands

- netq show agents (make these links)
- netq config agent

### netq check bgp
Validates that all configured route peering is established in your network fabric by looking for consistency across BGP sessions; in particular, whether duplicate router IDs exist and if any sessions are in the unestablished state. The output displays the total number of nodes found and how many are reporting session failures. It also displays the total number of [active] BGP sessions at the specified time and the number of session failures for all nodes. For nodes with session failures, additional details are displayed, including the cause of the failure.
If you have nodes that implement virtual routing and forwarding (VRF), you can request status based on the relevant routing table. VRF is commonly configured in multi-tenancy deployments to maintain separate domains for each tenant.
Syntax
netq check bgp 
		[vrf (default|mgmt)]
		[around <text-time>]
		[json]
Required Arguments
None
Optional Arguments
vrf (default|mgmt)
For nodes using VRF, indicate whether to use the default routing table or the management routing table. 
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find nodes running BGP with session failures (none found)
cumulus@ts:~$ netq check bgp
Total Nodes: 11, Failed Nodes: 0, Total Sessions: 16, Failed Sessions: 0
Find nodes running BGP with session failures (two found)
cumulus@ts:~$ netq check bgp
Total Nodes: 4, Failed Nodes: 2, Total Sessions: 8 , Failed Sessions: 2
Node     Neighbor    Peer ID    Reason              Time
-------  ----------  ---------  ------------------  -------
leaf03   swp51       spine01    Interface down      4m ago
spine01  swp3        leaf03     Hold Timer Expired  4m ago
This example shows that BGP peering on leaf03 connecting to spine01 failed 4 minutes ago and that it was caused by an interface failure on leaf03. This led to BGP hold timer expiration on spine01.
Find nodes running BGP with session failures an hour ago
cumulus@ts:~$ netq check bgp around 1h
Total Nodes: 11, Failed Nodes: 0, Total Sessions: 16, Failed Sessions: 0
Find nodes running BGP with VRF applied and session failures
cumulus@switch:~$ netq check bgp vrf mgmt
No BGP session info found. Total Nodes: 11, Failed Nodes: 0
Find nodes running BGP with VRF applied and session failures, and display the results in JSON format
cumulus@ts:~$ netq check bgp vrf mgmt json
{
    "failedNodes":[

    ],
    "summary":{
        "checkedNodeCount":11,
        "failedSessionCount":0,
        "failedNodeCount":0,
        "totalSessionCount":0
    }
}
Related Commands
netq show bgp

netq check clag
Verifies CLAG session consistency by identifying all CLAG and MLAG peers with errors or misconfigurations in the NetQ domain. In particular, it looks for:
multiple link pairs with the same system MAC address, 
any interfaces [links?] with only a single attachment,
peer connectivity, [failed links?] and 
whether the backup IP address is pointing to the correct peer.
The output displays the total number of nodes checked and how many are reporting errors, warnings, or misconfigurations. For any nodes with errors, it also displays the name of the node and the reason for the error.
Syntax
netq check clag 
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find CLAG peers with errors and/or misconfigurations (none found)
cumulus@ts:~$ netq check clag 
Checked Nodes: 4, Failed Nodes: 0
Find CLAG peers with errors and/or misconfigurations (two found)
cumulus@leaf01:~$ netq check clag
Checked Nodes: 6, Warning Nodes: 2
Node             Reason
---------------- ------------------------------------------------------
leaf01           Link Down: bond01
leaf02           Singly Attached Bonds: bond01
In this example we see two errors. The first row tells us that the bond1 link is down on the leaf01 node. The second row tells us that bond1 has only one attachment to leaf02 node. [The bond1 link should also be attached to ???]
Find all nodes running CLAG with session failures 30 seconds ago
cumulus@ts:~$ netq check bgp around 30s
Checked Nodes: 4, Failed Nodes: 0
Find all nodes running CLAG with session failures 30 seconds ago, and display the results in JSON format
cumulus@ts:~$ netq check clag around 30s json
{
    "failedNodes":[

    ],
    "summary":{
        "checkedNodeCount":4,
        "failedNodeCount":0,
        "warningNodeCount":0
    }
}
Related Commands
netq show clag

netq check evpn
Collects communication status for all nodes (leafs, spines, and hosts) running instances of Ethernet VPN (EVPN) in your network fabric. The output contains the total number of [VTEP?] nodes found and how many are reporting session failures. It also displays the total number of EVPN sessions running at the specified time and the number of session failures for all nodes. The total number of virtual network instances (VNIs) is also indicated.
Syntax
netq check evpn 
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.x
Introduced

Sample Usage
Find all nodes running EVPN with session failures
cumulus@ts:~$ netq check evpn 
Total Nodes: 11, Failed Nodes: 0, Total Sessions: 8, Failed Sessions: 0, Total VNIs: 2
Find all nodes running EVPN with session failures about 10 minutes ago
cumulus@ts:~$ netq check evpn around 10m
Total Nodes: 11, Failed Nodes: 0, Total Sessions: 8, Failed Sessions: 0, Total VNIs: 2
Find all nodes running EVPN with session failures about 10 minutes ago, and display the results in JSON format
cumulus@ts:~$ netq check evpn around 10m json
{
    "failedVtepNodes":[

    ],
    "failedBgpSessions":[

    ],
    "summary":{
        "checkedNodeCount":11,
        "checkedVnisCount":2,
        "failedBgpSessionCount":0,
        "failedNodeCount":0,
        "totalSessionCount":8
    }
}
Related Commands
netq show evpn  
 
netq check interfaces
Collects interface communication status for all nodes (leafs, spines, and hosts) or an interface between specific nodes in your network fabric. The output contains the total number of nodes found and how many are reporting interface failures. It also displays the total number of ports found and how many are reporting failures. Optionally, you can display the total number of unverified ports [unknown or not configured?].  This information is followed by a list of all nodes, and their related interfaces, peers, and any message about the interface. The same information is displayed for a single node when specified.
Note: When running this command for all nodes, no arguments are required. When running this command for a specific node, the node and peer node information is required.
Syntax
netq check interfaces 
		[unverified] 
		[<physical-hostname> <physical-port> | <physical-hostname>]
		[around <text-time>] 
		[json]
OR
netq check interfaces 
		<physical-hostname> <physical-port> 
		and 
		<peer-physical-hostname> <peer-physical-port> 
		[around <text-time>] 
		[json]
Required Arguments
physical-hostname
Name of the specific node on which to verify interface communication status; for example, leaf01 or spine02.
physical-port
Name of the port on the node to check; for example, eth0 or swp3.
peer-physical-hostname
Name of the peer node to check; for example server02 or mgmt-server.
peer-physical-port
Name of the peer port on the node to check; for example, eth2 or swp4.
Optional Arguments
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.x
Introduced

Sample Usage
Find all nodes with interface failures
cumulus@ts:~$ netq check interfaces
Checked Nodes: 11, Failed Nodes: 8
Checked Ports: 234, Failed Ports: 16, Unverified Ports: 190
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
leaf01            swp1                      server01          eth1                      Autoneg mismatch (off, on)         
leaf01            swp2                      server02          eth1                      Autoneg mismatch (off, on)         
leaf02            swp1                      server01          eth2                      Autoneg mismatch (off, on)         
leaf02            swp2                      server02          eth2                      Autoneg mismatch (off, on)         
leaf03            swp1                      server03          eth1                      Autoneg mismatch (off, on)         
leaf03            swp2                      server04          eth1                      Autoneg mismatch (off, on)         
leaf04            swp1                      server03          eth2                      Autoneg mismatch (off, on)         
leaf04            swp2                      server04          eth2                      Autoneg mismatch (off, on)         
server01          eth1                      leaf01            swp1                      Autoneg mismatch (on, off)         
server01          eth2                      leaf02            swp1                      Autoneg mismatch (on, off)         
server02          eth1                      leaf01            swp2                      Autoneg mismatch (on, off)         
server02          eth2                      leaf02            swp2                      Autoneg mismatch (on, off)         
server03          eth1                      leaf03            swp1                      Autoneg mismatch (on, off)         
server03          eth2                      leaf04            swp1                      Autoneg mismatch (on, off)         
server04          eth1                      leaf03            swp2                      Autoneg mismatch (on, off)         
server04          eth2                      leaf04            swp2                      Autoneg mismatch (on, off)         
Find interface failures on leaf01 node
cumulus@ts:~$ netq check interfaces leaf01 swp1 and server01 eth1
Checked Nodes: 1, Failed Nodes: 1
Checked Ports: 1, Failed Ports: 1, Unverified Ports: 0
Hostname          Interface                 Peer Hostname     Peer Interface            Message
----------------- ------------------------- ----------------- ------------------------- -----------------------------------
leaf01            swp1                      server01          eth1                      Autoneg mismatch (off, on)         
   
Find interface failures on leaf01 node and display the results in JSON format
cumulus@switch:~$ netq check interfaces leaf01 swp1 and server01 eth1 json
{
    "unverifiedNodes":[

    ],
    "failedNodes":[
        {
            "interface":"swp1",
            "peerInterface":"eth1",
            "message":"Autoneg mismatch (off, on)",
            "hostname":"leaf01",
            "peerHostname":"server01"
        }
    ],
    "summary":{
        "checkedNodeCount":1,
        "failedPortCount":1,
        "failedNodeCount":1,
        "checkedPortCount":1,
        "unverifiedPortCount":0
    }
}
Related Commands
netq show interfaces  

netq check license
Collects license status for all nodes (leafs, spines, and hosts) in your network fabric. The output contains the total number of nodes found and how many are reporting expired licenses. It also displays the total number of licenses checked at the specified time and how many were expired.
Syntax
netq check license 
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
around <text-time>
Indicates how far to go back in time for the license information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find the number of nodes with expired licenses
cumulus@ts:~$ netq check license 
Total Nodes: 11, Failed Nodes: 0, Checked Licenses: 7, Failed Licenses: 0
Find the number of nodes with expired licenses about 7 days ago
cumulus@ts:~$ netq check license around 7d
Total Nodes: 11, Failed Nodes: 0, Checked Licenses: 7, Failed Licenses: 0
Find the number of nodes with expired licenses about 7 days ago, and display the results in JSON format
cumulus@ts:~$ netq check license around 7d json
{
    "failedNodes":[

    ],
    "summary":{
        "checkedNodeCount":11,
        "failedLicenseCount":0,
        "failedNodeCount":0,
        "checkedLicenseCount":0
    }
}
Related Commands
None
 
netq check lnv
Collects status for all nodes (leafs, spines, and hosts) running Lightweight Network Virtualization (LNV)  in your network fabric. The output contains the total number of nodes found and how many are reporting LNV failures. It also displays the total number of sessions checked at the specified time and how many were expired.
[Mellanox HotTo: Lightweight Network Virtualization (LNV) enables the deployment of a VXLAN without the need for a central controller on a bare metal switch.
LNV runs the VXLAN service and registration daemons on Cumulus Linux without any additional external controller or software suite.
Establishing a data path between bridge entities on top of a layer 3 fabric is done by coupling a service node with traditional MAC address learning.]

Syntax
netq check lnv 
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find all nodes with LNV failures
cumulus@ts:~$ netq check lnv 
Total Nodes: 11, Failed Nodes: 0, Checked Licenses: 7, Failed Licenses: 0 [replace with appropriate output]
Find all nodes with LNV failures about 2 days ago
cumulus@ts:~$ netq check lnv around 2d
Total Nodes: 11, Failed Nodes: 0, Checked Licenses: 7, Failed Licenses: 0 [replace with appropriate output]
Find tall nodes with LNV failures about 2 days ago, and display the results in JSON format
cumulus@ts:~$ netq check lnv around 2d json
{
    "failedNodes":[

    ],
    "summary":{
        "checkedNodeCount":11,
        "failedLicenseCount":0,
        "failedNodeCount":0,
        "checkedLicenseCount":0
    }
}[Replace with accurate output]
Related Commands
netq show lnv
 
netq check mtu
Verifies consistency of the maximum transmission unit (MTU) across all links in your network fabric. MTU consistency is verified at the level that is appropriate to the specific type of link. For example, bond interfaces have their MTU enforced at the bond level and not at the
individual slave level. For CLAG bonds, verification confirms whether or not both ends of the bond have the same MTU value configured for their local instance of the bond. 
The output contains the total number of nodes found and how many are reporting MTU inconsistencies. It also displays the total number of links checked at the specified time and how many are reporting MTU inconsistencies. Optionally, you can display the number of unverified interfaces.
Syntax
netq check mtu 
		[unverified]
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
unverified
Display the number of unverifiable interfaces in the output.
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find all links with MTU inconsistencies
cumulus@ts:~$ netq check mtu 
Checked Nodes: 11, Checked Links: 304, Failed Nodes: 0, Failed Links: 0
No MTU Mismatch found
Find all links with MTU inconsistencies about 4 days ago
cumulus@ts:~$ netq check mtu around 4d
Checked Nodes: 10, Checked Links: 300, Failed Nodes: 0, Failed Links: 0
No MTU Mismatch found
Find all links with MTU inconsistencies, and display the results in JSON format
cumulus@ts:~$ netq check mtu json
{
    "summary":{
        "checkedNodeCount":11,
        "failedNodeCount":0,
        "totalLinkCount":304,
        "failedLinkCount":0
    },
    "failedNodes":[

    ],
    "unverifiedLinks":[

    ]
}
Related Commands
netq trace
netq resolve 

netq check ntp
Verifies network time synchronization using NTP for all nodes (leafs, spines, and hosts)  in your network fabric. [something about the importance of time sync--impact to data, communications, etc. --Nodes that are not in time synchronization with the telemetry server xxx.] The output contains the total number of nodes found and how many are reporting NTP failures, have not been heard from in 90 seconds, and are unknown to the system. It also displays details about any nodes without time synchronization.
Syntax
netq check ntp 
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find all nodes that have lost time synchronization
cumulus@ts:~$ netq check ntp 
Total Nodes: 11, Checked Nodes: 11, Rotten Nodes: 0, Unknown Nodes: 0, failed NTP Nodes: 7
Hostname          NTP Sync Connect Time
----------------- -------- ------------
leaf01            no       2018-05-16 1
                           6:45:18     
leaf02            no       2018-05-16 1
                           6:33:54     
leaf03            no       2018-05-16 1
                           6:53:21     
leaf04            no       2018-05-16 1
                           6:33:31     
switch   no       2018-05-16 1
                           6:30:35     
spine01           no       2018-05-16 1
                           6:28:23     
spine02           no       2018-05-16 1
                           6:31:31     

Find all nodes that have lost time synchronization about 3 days ago
cumulus@ts:~$ netq check ntp around 3d
Total Nodes: 11, Checked Nodes: 10, Rotten Nodes: 0, Unknown Nodes: 0, failed NTP Nodes: 0
Find all nodes that have lost time synchronization, and display the results in JSON format
cumulus@ts:~$ netq check ntp json
{
    "failedNodes":[
        {
            "ntpSync":"no",
            "hostname":"leaf01",
            "connectTime":"1526489118.6"
        },
        {
            "ntpSync":"no",
            "hostname":"leaf02",
            "connectTime":"1526488434.46"
        },
        {
            "ntpSync":"no",
            "hostname":"leaf03",
            "connectTime":"1526489601.67"
        },
        {
            "ntpSync":"no",
            "hostname":"leaf04",
            "connectTime":"1526488411.43"
        },
        {
            "ntpSync":"no",
            "hostname":"switch",
            "connectTime":"1526488235.8"
        },
        {
            "ntpSync":"no",
            "hostname":"spine01",
            "connectTime":"1526488103.44"
        },
        {
            "ntpSync":"no",
            "hostname":"spine02",
            "connectTime":"1526488291.38"
        }
    ],
    "summary":{
        "checkedNodeCount":11,
        "totalNodeCount":11,
        "rottenNodeCount":0,
        "failedNodeCount":7,
        "unknownNodeCount":0
    }
}
Related Commands
netq show ntp


netq check ospf
Validates that all configured route peering is established in your network fabric by looking for consistency across OSPF sessions; in particular, whether duplicate router IDs exist and if any sessions are in the unestablished state. The output displays the total number of nodes found and how many are reporting session failures. It also displays the total number of [active] BGP sessions at the specified time and the number of session failures for all nodes. For nodes with session failures, additional details are displayed, including the cause of the failure.
Syntax
netq check ospf 
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find all nodes with OSPF session failures
cumulus@ts:~$ netq check ospf 
[enter output here]
Find all nodes with OSPF session failures about 3 days ago
cumulus@ts:~$ netq check ospf around 3d
[enter output here]
Find all nodes with OSPF session failures, and display the results in JSON format
cumulus@ts:~$ netq check ospf json
[enter output here]
Related Commands
netq show ospf

netq check sensors
Collects status of temperature, cooling fan, and power supply sensors for all nodes in your network fabric. The output displays the total number of nodes found and how many are reporting sensor alarms. It also displays the total number of sensors checked and how many of them are reporting alarms. For nodes with sensor alarms, additional details are displayed[, including the sensor type, alert description/name, and a timestamp when the alert occurred].
Syntax
netq check sensors 
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find all nodes with sensor alarms
cumulus@ts:~$ netq check sensors 
Total Nodes: 11, Failed Nodes: 0, Checked Sensors: 119, Failed Sensors: 0
Find all nodes with sensor alarms about 2 hours ago
cumulus@ts:~$ netq check sensors around 2h
[enter output here]
Find all nodes with sensor alarms, and display the results in JSON format
cumulus@ts:~$ netq check sensors json
[enter output here]
Related Commands
netq show sensors
   

netq check vlan
Verifies consistency of the virtual local area network (VLAN) nodes and interfaces across all links in your network fabric. VLAN consistency is verified [xxx]
The output contains the total number of nodes checked and how many are reporting interface/link inconsistencies. It also displays the total number of links checked at the specified time and how many are reporting link inconsistencies. Optionally, you can display the number of unverified interfaces.
Syntax
netq check vlan 
		[unverified]
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
unverified
Display the number of unverifiable interfaces in the output.
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find all nodes with VLAN inconsistencies
cumulus@ts:~$ netq check vlan 
Checked Nodes: 11, Checked Links: 304, Failed Nodes: 0, Failed Links: 0
No VLAN or PVID Mismatch found
Find all nodes with VLAN inconsistencies and any unverified interfaces
cumulus@ts:~$ netq check vlan unverified
Checked Nodes: 11, Checked Links: 304, Failed Nodes: 0, Failed Links: 0
No VLAN or PVID Mismatch found
Vlan check could not be done on:
Hostname          Interface                 Vlans                     Peer              Peer Interface            Reason
----------------- ------------------------- ------------------------- ----------------- ------------------------- ---------------------------------------------
spine02           swp29                                                                                           Peer is unknown
spine02           swp30                                                                                           Peer is unknown
spine01           swp30                                                                                           Peer is unknown
spine01           swp29                                                                                           Peer is unknown
switch   swp1                                                                                            Peer is unknown

Find all nodes with VLAN inconsistencies about 2 hours ago
cumulus@ts:~$ netq check vlan around 2h
Checked Nodes: 11, Checked Links: 304, Failed Nodes: 0, Failed Links: 0
No VLAN or PVID Mismatch found
Find all nodes with VLAN inconsistencies and unverified interfaces, and display the results in JSON format
cumulus@ts:~$ netq check vlan unverified json
{
    "summary":{
        "checkedNodeCount":11,
        "failedNodeCount":0,
        "totalLinkCount":304,
        "failedLinkCount":0
    },
    "failedNodes":[

    ],
    "unverifiedLinks":[
        {
            "hostname":"spine02",
            "peerInterface":"",
            "peer":"",
            "reason":"Peer is unknown",
            "interface":"swp29",
            "vlans":""
        },
        {
            "hostname":"spine02",
            "peerInterface":"",
            "peer":"",
            "reason":"Peer is unknown",
            "interface":"swp30",
            "vlans":""
        },
        {
            "hostname":"spine01",
            "peerInterface":"",
            "peer":"",
            "reason":"Peer is unknown",
            "interface":"swp30",
            "vlans":""
        },
        {
            "hostname":"spine01",
            "peerInterface":"",
            "peer":"",
            "reason":"Peer is unknown",
            "interface":"swp29",
            "vlans":""
        },
        {
            "hostname":"switch",
            "peerInterface":"",
            "peer":"",
            "reason":"Peer is unknown",
            "interface":"swp1",
            "vlans":""
        }
    ]
}
Related Commands
netq show vlan    

netq check vxlan
Verifies consistency of the virtual extensible local area network (VXLAN) nodes and interfaces across all links in your network fabric. VxLAN consistency is verified [xxx]
The output contains the total number of nodes checked and how many are reporting interface/link inconsistencies. It also displays the total number of links checked at the specified time and how many are reporting link inconsistencies. 
Syntax
netq check vxlan 
		[around <text-time>]
		[json]
Required Arguments
	None
Optional Arguments
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
Find all nodes with VXLAN inconsistencies
cumulus@ts:~$ netq check vxlan 
Checked Nodes: 4, Warning Nodes: 0, Failed Nodes: 0
Find all nodes with VxLAN inconsistencies about 2 days ago
cumulus@ts:~$ netq check vxlan around 2d
Checked Nodes: 4, Warning Nodes: 0, Failed Nodes: 0
Find all nodes with VLAN inconsistencies, and display the results in JSON format
cumulus@ts:~$ netq check vxlan around 2d json
{
    "failedNodes":[

    ],
    "summary":{
        "checkedNodeCount":4,
        "failedNodeCount":0,
        "warningNodeCount":0
    }
}
Related Commands
netq show vxlan    

SHOW COMMANDS
All of the NetQ show commands begin with netq show. They are used to view the health of various elements in your network fabric. They are described here in alphabetical order.
netq show agents
Displays basic configuration, health, and connectivity status for all nodes or a specific node running NetQ Agent in your network fabric. The output provides:
whether each node has been heard recently (last 90 seconds), 
if it is in time synchronization [with the ts?], 
the NetQ Agent software version currently running on the node, 
how long the node has been up, 
how long the NetQ Agent has been up, 
the last time the NetQ Agent was reinitialized, and 
How long ago the last change was made to the [node or NetQ Agent configuration of status?].
Optionally you may also display the changes (add, delete, xxx) made to all nodes or a specific node.
This command gives you an easy way to see if any NetQ Agents or their nodes have lost power, may have difficulty communicating with the telemetry server, and whether agents are running different versions of software. Any of these situations could cause problems in the operation of your network.
Syntax
netq [<hostname>] show agents 
		[changes] 
		[json]
Required Arguments
	None
Optional Arguments
hostname
Text used to identify a particular node in your network fabric; for example, leaf01 or swp3.
changes
Display changes made to one or all nodes along with standard output.
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
View status of all nodes with NetQ Agent installed
cumulus@ts:~$ netq show agents 
Matching agents records:
Hostname          Status           NTP Sync Version                              Sys Uptime                Agent Uptime              Reinitialize Time          Last Changed
----------------- ---------------- -------- ------------------------------------ ------------------------- ------------------------- -------------------------- -------------------------
border01          Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:54 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:38 2020
border02          Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:57 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:33 2020
fw1               Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:44 2020  Tue Sep 29 21:24:48 2020  Tue Sep 29 21:24:48 2020   Thu Oct  1 16:07:26 2020
fw2               Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:04:42 2020  Tue Sep 29 21:24:48 2020  Tue Sep 29 21:24:48 2020   Thu Oct  1 16:07:22 2020
leaf01            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 16:49:04 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:10 2020
leaf02            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:14 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:30 2020
leaf03            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:37 2020  Tue Sep 29 21:24:49 2020  Tue Sep 29 21:24:49 2020   Thu Oct  1 16:07:24 2020
leaf04            Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:35 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:13 2020
oob-mgmt-server   Fresh            yes      3.1.1-ub18.04u29~1599111022.78b9e43  Mon Sep 21 16:43:58 2020  Mon Sep 21 17:55:00 2020  Mon Sep 21 17:55:00 2020   Thu Oct  1 16:07:31 2020
server01          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:16 2020
server02          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:24 2020
server03          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:56 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:12 2020
server04          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:07 2020  Tue Sep 29 21:13:07 2020   Thu Oct  1 16:07:17 2020
server05          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:25 2020
server06          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:19:57 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:21 2020
server07          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:06:48 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:28 2020
server08          Fresh            yes      3.2.0-ub18.04u30~1601393774.104fb9e  Mon Sep 21 17:06:45 2020  Tue Sep 29 21:13:10 2020  Tue Sep 29 21:13:10 2020   Thu Oct  1 16:07:31 2020
spine01           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:34 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:20 2020
spine02           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:33 2020  Tue Sep 29 21:24:58 2020  Tue Sep 29 21:24:58 2020   Thu Oct  1 16:07:16 2020
spine03           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:34 2020  Tue Sep 29 21:25:07 2020  Tue Sep 29 21:25:07 2020   Thu Oct  1 16:07:20 2020
spine04           Fresh            yes      3.2.0-cl4u30~1601410518.104fb9ed     Mon Sep 21 17:03:32 2020  Tue Sep 29 21:25:07 2020  Tue Sep 29 21:25:07 2020   Thu Oct  1 16:07:33 2020

View status of all nodes with NetQ Agents, and display the results in JSON format
cumulus@ts:~$ netq show agents json
{
    "agents":[
        {
            "status":"Fresh",
            "lastChanged":1526584467.1063349247,
            "reinitializeTime":1526068569.3166179657,
            "hostname":"server02",
            "version":"1.3.0-ub16.04u9~1522971904.b08ca60",
            "sysUptime":1526068557.7966170311,
            "ntpSync":"yes",
            "agentUptime":1526068569.316617012
        },
        {
            "status":"Fresh",
            "lastChanged":1526584450.6665298939,
            "reinitializeTime":1526068569.3423800468,
            "hostname":"server04",
            "version":"1.3.0-ub16.04u9~1522971904.b08ca60",
            "sysUptime":1526068557.8123779297,
            "ntpSync":"yes",
            "agentUptime":1526068569.3423779011
        },
        {
            "status":"Fresh",
            "lastChanged":1526584450.0170140266,
            "reinitializeTime":1526577085.9067358971,
            "hostname":"server01",
            "version":"1.3.0-ub16.04u9~1522971904.b08ca60",
            "sysUptime":1526068558.8021190166,
            "ntpSync":"yes",
            "agentUptime":1526068570.452119112
        },
        {
            "status":"Fresh",
            "lastChanged":1526584461.5413489342,
            "reinitializeTime":1526068569.4015939236,
            "hostname":"server03",
            "version":"1.3.0-ub16.04u9~1522971904.b08ca60",
            "sysUptime":1526068557.7815930843,
            "ntpSync":"yes",
            "agentUptime":1526068569.4015929699
        },
        {
            "status":"Fresh",
            "lastChanged":1526584444.7508759499,
            "reinitializeTime":1526068529.5848419666,
            "hostname":"spine02",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526059415.8448050022,
            "ntpSync":"yes",
            "agentUptime":1526068529.5848050117
        },
        {
            "status":"Fresh",
            "lastChanged":1526584450.869822979,
            "reinitializeTime":1526318846.8988080025,
            "hostname":"leaf04",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526055851.829241991,
            "ntpSync":"yes",
            "agentUptime":1526068529.5392420292
        },
        {
            "status":"Fresh",
            "lastChanged":1526584444.1613891125,
            "reinitializeTime":1526068529.5949180126,
            "hostname":"leaf02",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526053212.2249178886,
            "ntpSync":"yes",
            "agentUptime":1526068529.5949180126
        },
        {
            "status":"Fresh",
            "lastChanged":1526584444.1491498947,
            "reinitializeTime":1526068529.6256389618,
            "hostname":"leaf03",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526053793.9156200886,
            "ntpSync":"yes",
            "agentUptime":1526068529.6256198883
        },
        {
            "status":"Fresh",
            "lastChanged":1526584443.1579871178,
            "reinitializeTime":1526576730.014993906,
            "hostname":"spine01",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526057852.8196310997,
            "ntpSync":"yes",
            "agentUptime":1526068529.6696310043
        },
        {
            "status":"Fresh",
            "lastChanged":1526584450.865801096,
            "reinitializeTime":1526392781.1005580425,
            "hostname":"leaf01",
            "version":"1.3.0-cl3u9~1522970647.b08ca60",
            "sysUptime":1526053158.7921569347,
            "ntpSync":"yes",
            "agentUptime":1526068529.7521569729
        },
        {
            "status":"Fresh",
            "lastChanged":1526584456.1811571121,
            "reinitializeTime":1526576736.1758289337,
            "hostname":"switch",
            "version":"1.4.0-cl3u10~1525711818.58b9c8f",
            "sysUptime":1526283003.6326210499,
            "ntpSync":"yes",
            "agentUptime":1526314445.2926208973
	}
    ],
    "truncatedResult":false
}
Related Commands
netq check agents    

netq show bgp
There are two forms of this command. One displays all nodes or a specific node running BGP in your network fabric. In this form, the output displays the following for each node::
the neighbor nodes to the given node, 
whether multiple routing tables (VRF) have been applied, 
the autonomous system number (ASN) assigned to the node, 
the peer ASN for each neighbor, 
the PfxRx [what is this?], and 
how long ago the last change was made to the node.
The second form of this command displays all of the changes (add, delete, xxx) made to the nodes running BGP over a period of time in addition to the metrics displayed for the first form. 
If you have nodes that implement virtual routing and forwarding (VRF), you can request status based on the relevant routing table. VRF is commonly configured in multi-tenancy deployments to maintain separate domains for each tenant.
This command gives you an easy way to see [xxx]
Syntax
netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] 
		[vrf <default|mgmt>] 
		[around <text-time>] 
		[json]
OR
netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] 
		[vrf <default|mgmt>] 
		changes [between <text-time> and <text-endtime>]
		[json]

Required Arguments
changes
Display changes made to one or all nodes.
Optional Arguments
hostname
Text used to identify a particular node in your network fabric; for example, leaf01 or swp3.
bgp session
Only display results for the specified BGP session; for example 5468354.
asn <number-asn>
Only display results for the specified ASN number; for example 65013.
vrf (default|mgmt)
For nodes using VRF, indicate whether to use the default routing table or the management routing table. 
around <text-time>
Indicates how far to go back in time for the network state information. The <text-time> value is written using text (versus a UTP representation for example). Valid values include:
<1-xx>s: number of seconds
<1-xx>m: number of minutes
<1-xx>h: number of hours
<1-xx>d: number of days
Use number of days to go back weeks, months, or years. [how much data is stored by default?] Also note there is no space between the number and unit of time.
Between <text-time> and <text-endtime>
Indicates the timeframe for which you want to view changes. [explain how this works--which variable is the more recent time???]
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
View status of all nodes running BGP
cumulus@ts:~$ netq show bgp 
Matching bgp records:
Hostname          Neighbor                         VRF              ASN        Peer ASN   PfxRx        Last Changed
----------------- -------------------------------- ---------------- ---------- ---------- ------------ ----------------
leaf01            swp51(spine01)                   default          65011      65020      5/-/23       2d:15h:2m:29s
leaf01            swp52(spine02)                   default          65011      65020      5/-/23       2d:15h:2m:29s
leaf02            swp51(spine01)                   default          65012      65020      6/-/23       5d:23h:30m:50s
leaf02            swp52(spine02)                   default          65012      65020      6/-/23       5d:23h:30m:50s
leaf03            swp51(spine01)                   default          65013      65020      5/-/24       5d:23h:30m:50s
leaf03            swp52(spine02)                   default          65013      65020      5/-/24       5d:23h:30m:50s
leaf04            swp51(spine01)                   default          65014      65020      6/-/24       5d:23h:30m:50s
leaf04            swp52(spine02)                   default          65014      65020      6/-/24       5d:23h:30m:50s
spine01           swp1(leaf01)                     default          65020      65011      2/-/12       1d:23h:11m:24s
spine01           swp2(leaf02)                     default          65020      65012      2/-/12       1d:23h:11m:24s
spine01           swp3(leaf03)                     default          65020      65013      2/-/12       1d:23h:11m:24s
spine01           swp4(leaf04)                     default          65020      65014      2/-/11       1d:23h:11m:24s
spine02           swp1(leaf01)                     default          65020      65011      2/-/12       5d:23h:30m:50s
spine02           swp2(leaf02)                     default          65020      65012      2/-/12       5d:23h:30m:50s
spine02           swp3(leaf03)                     default          65020      65013      2/-/12       5d:23h:30m:50s
spine02           swp4(leaf04)                     default          65020      65014      2/-/11       5d:23h:30m:50s
View the changes made to all nodes running BGP
cumulus@ts:~$ netq show agents changes
Matching bgp records:
Hostname          Neighbor                     VRF              ASN        Peer ASN   PfxRx        DbState  Last Changed
----------------- ---------------------------- ---------------- ---------- ---------- ------------ -------- ----------------
spine01           swp4(leaf04)                 default          65020      65014      2/-/11       Add      1d:23h:58m:13s
spine01           swp3(leaf03)                 default          65020      65013      2/-/12       Add      1d:23h:58m:13s
spine01           swp2(leaf02)                 default          65020      65012      2/-/12       Add      1d:23h:58m:13s
spine01           swp1(leaf01)                 default          65020      65011      2/-/12       Add      1d:23h:58m:13s
leaf01            swp52(spine02)               default          65011      65020      5/-/23       Add      2d:15h:49m:18s
leaf01            swp51(spine01)               default          65011      65020      5/-/23       Add      2d:15h:49m:18s
spine02           swp4(leaf04)                 default          65020      65014      2/-/10       Add      6d:0h:17m:39s
spine02           swp4(leaf04)                 default          65020      65014      2/-/11       Add      6d:0h:17m:39s
spine02           swp3(leaf03)                 default          65020      65013      2/-/10       Add      6d:0h:17m:39s
spine02           swp3(leaf03)                 default          65020      65013      2/-/12       Add      6d:0h:17m:39s
spine02           swp2(leaf02)                 default          65020      65012      2/-/10       Add      6d:0h:17m:39s
spine02           swp2(leaf02)                 default          65020      65012      2/-/12       Add      6d:0h:17m:39s
spine02           swp1(leaf01)                 default          65020      65011      2/-/10       Add      6d:0h:17m:39s
spine02           swp1(leaf01)                 default          65020      65011      2/-/11       Add      6d:0h:17m:39s
spine02           swp1(leaf01)                 default          65020      65011      2/-/12       Add      6d:0h:17m:39s
spine01           swp4(leaf04)                 default          65020      65014      2/-/2        Add      6d:0h:17m:39s
spine01           swp4(leaf04)                 default          65020      65014      2/-/10       Add      6d:0h:17m:39s
spine01           swp4(leaf04)                 default          65020      65014      2/-/11       Add      6d:0h:17m:39s
spine01           swp3(leaf03)                 default          65020      65013      2/-/2        Add      6d:0h:17m:39s
spine01           swp3(leaf03)                 default          65020      65013      2/-/10       Add      6d:0h:17m:39s
spine01           swp3(leaf03)                 default          65020      65013      2/-/12       Add      6d:0h:17m:39s
spine01           swp2(leaf02)                 default          65020      65012      2/-/2        Add      6d:0h:17m:39s
spine01           swp2(leaf02)                 default          65020      65012      2/-/10       Add      6d:0h:17m:39s
spine01           swp2(leaf02)                 default          65020      65012      2/-/12       Add      6d:0h:17m:39s
spine01           swp1(leaf01)                 default          65020      65011      2/-/2        Add      6d:0h:17m:39s
spine01           swp1(leaf01)                 default          65020      65011      2/-/10       Add      6d:0h:17m:39s
spine01           swp1(leaf01)                 default          65020      65011      2/-/11       Add      6d:0h:17m:39s
spine01           swp1(leaf01)                 default          65020      65011      2/-/12       Add      6d:0h:17m:39s
leaf04            swp52(spine02)               default          65014      65020      6/-/20       Add      6d:0h:17m:39s
leaf04            swp52(spine02)               default          65014      65020      6/-/23       Add      6d:0h:17m:39s
leaf04            swp52(spine02)               default          65014      65020      6/-/24       Add      6d:0h:17m:39s
leaf04            swp51(spine01)               default          65014      65020      6/-/20       Add      6d:0h:17m:39s
leaf04            swp51(spine01)               default          65014      65020      6/-/23       Add      6d:0h:17m:39s
leaf04            swp51(spine01)               default          65014      65020      6/-/24       Add      6d:0h:17m:39s
leaf03            swp52(spine02)               default          65013      65020      5/-/20       Add      6d:0h:17m:39s
leaf03            swp52(spine02)               default          65013      65020      5/-/23       Add      6d:0h:17m:39s
leaf03            swp52(spine02)               default          65013      65020      5/-/24       Add      6d:0h:17m:39s
leaf03            swp51(spine01)               default          65013      65020      5/-/20       Add      6d:0h:17m:39s
leaf03            swp51(spine01)               default          65013      65020      5/-/23       Add      6d:0h:17m:39s
leaf03            swp51(spine01)               default          65013      65020      5/-/24       Add      6d:0h:17m:39s
leaf02            swp52(spine02)               default          65012      65020      6/-/4        Add      6d:0h:17m:39s
leaf02            swp52(spine02)               default          65012      65020      6/-/20       Add      6d:0h:17m:39s
leaf02            swp52(spine02)               default          65012      65020      6/-/23       Add      6d:0h:17m:39s
leaf02            swp51(spine01)               default          65012      65020      6/-/4        Add      6d:0h:17m:39s
leaf02            swp51(spine01)               default          65012      65020      6/-/20       Add      6d:0h:17m:39s
leaf02            swp51(spine01)               default          65012      65020      6/-/23       Add      6d:0h:17m:39s
leaf01            swp52(spine02)               default          65011      65020      5/-/4        Add      6d:0h:17m:39s
leaf01            swp52(spine02)               default          65011      65020      5/-/20       Add      6d:0h:17m:39s
leaf01            swp52(spine02)               default          65011      65020      5/-/23       Add      6d:0h:17m:39s
leaf01            swp51(spine01)               default          65011      65020      5/-/4        Add      6d:0h:17m:39s
leaf01            swp51(spine01)               default          65011      65020      5/-/20       Add      6d:0h:17m:39s
leaf01            swp51(spine01)               default          65011      65020      5/-/23       Add      6d:0h:17m:39s
spine02           swp4(leaf04)                 default          65020      65014      2/-/2        Add      6d:0h:17m:40s
spine02           swp3(leaf03)                 default          65020      65013      2/-/2        Add      6d:0h:17m:40s
spine02           swp2(leaf02)                 default          65020      65012      2/-/2        Add      6d:0h:17m:40s
spine02           swp1(leaf01)                 default          65020      65011      2/-/2        Add      6d:0h:17m:40s
leaf04            swp52(spine02)               default          65014      65020      6/-/4        Add      6d:0h:17m:40s
leaf04            swp51(spine01)               default          65014      65020      6/-/4        Add      6d:0h:17m:40s
leaf03            swp52(spine02)               default          65013      65020      5/-/4        Add      6d:0h:17m:40s
leaf03            swp51(spine01)               default          65013      65020      5/-/4        Add      6d:0h:17m:40s
View status of nodes running BGP with particular ASN
cumulus@ts:~$ netq show bgp asn 65013
Matching bgp records:
Hostname          Neighbor                         VRF              ASN        Peer ASN   PfxRx        Last Changed
----------------- -------------------------------- ---------------- ---------- ---------- ------------ ----------------
leaf03            swp51(spine01)                   default          65013      65020      5/-/24       5d:23h:44m:57s
leaf03            swp52(spine02)                   default          65013      65020      5/-/24       5d:23h:44m:57s
View status of a specific node running BGP, and display the results in JSON format
cumulus@ts:~$ netq leaf02 show bgp json
{
    "bgp":[
        {
            "lastChanged":1526068547.0,
            "pfxrx":"6/-/23",
            "hostname":"leaf02",
            "peerAsn":65020,
            "vrf":"default",
            "neighbor":"swp51(spine01)",
            "asn":65012
        },
        {
            "lastChanged":1526068547.0,
            "pfxrx":"6/-/23",
            "hostname":"leaf02",
            "peerAsn":65020,
            "vrf":"default",
            "neighbor":"swp52(spine02)",
            "asn":65012
	}
    ],
    "truncatedResult":false
}
Related Commands
netq check bgp    

netq show changes
Displays changes made to a specific node, identified by its name, IP address and/or VRF, in your network fabric. The output provides:
xxx 
xxx
This command gives you an easy way to see [xxx]
Syntax
 netq [<hostname>] show changes 
		[<ipv4>|<ipv6>|<ipv4> vrf <vrf>|<ipv6> vrf <vrf>|vrf <vrf>]
		between <text-time> and <text-endtime> 
		[json]
Required Arguments	
Between <text-time> and <text-endtime>
Indicates the timeframe for which you want to view changes. [explain how this works--which variable is the more recent time???]
Optional Arguments
hostname
Text used to identify a particular node in your network fabric; for example, leaf01 or swp3.
<ipv4>
Display changes made to node with specified IP version 4 address. Do not indicate mask address.
<ipv6>
Display changes made to node with specified IP version 6 address. Do not indicate mask address.
vrf (default|mgmt)
For nodes using VRF, indicate whether to use the default routing table or the management routing table. 
json
Display the output in JSON file format instead of the default on-screen text format.
Command History
	
Release
Description
1.0
Introduced

Sample Usage
View status of all nodes with NetQ Agent installed
cumulus@ts:~$ netq show agents 
Matching agents records:


cumulus@switch:~$ netq show 
    changes     :  How this infomation has changed with time
    clag        :  Cumulus Multi-chassis LAG
    docker      :  Docker Info
    evpn        :  EVPN
    interfaces  :  network interface port
    inventory   :  Inventory information
    ip          :  IPv4 related info
    ipv6        :  IPv6 related info
    kubernetes  :  Kubernetes Information
    lldp        :  LLDP based neighbor info
    lnv         :  Lightweight Network Virtualization info
    macs        :  Mac table or MAC address info
    ntp         :  NTP
    ospf        :  OSPF info
    sensors     :  Temperature/Fan/PSU sensors
    services    :  System services
    vlan        :  VLAN
    vxlan       :  VXLAN data path
CONFIGURATION COMMANDS
All of the NetQ configuration commands begin with netq config.
They are described here in alphabetical order by component group:
Add-on Configuration Commands
Agent Configuration Commands
Parser
Server
Telemetry Server

Add-on Configuration Commands
netq config (add|del) addons
Installs or removes all additional software components available with a given release. [in a particular directory?]
Syntax
netq config add addons
netq config del addons
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
	None
Run From
	Telemetry server, leaf, spine, host?
Command History
	
Release
Description
1.0
Introduced

Usage Guidelines
Sample Usage
Related Commands




NetQ Agent Configuration Commands
netq config (add|del) agent (stats|sensors)
Installs or removes [Starts or stops? Enables or disables?] collection of statistics or sensor measurements by NetQ Agent on [all or specific node?].
Syntax
	netq config add agent stats
	netq config del agent stats
netq config add agent sensors
neq config del agent sensors
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
	None
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Starting statistical collection on agent node [check to see if it is running?]
cumulus@ts:~$ netq config add agent stats
Related Commands
Netq config add agent docker-monitor
Netq config add agent loglevel
Netq config add agent kubernetes-monitor

netq config add agent docker-monitor
Installs [Starts? Enables?] the Docker monitoring service on [all or specific node?].
Syntax
	netq config add agent docker-monitor [poll-period <text-duration-period>]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
poll-period
The amount of time to monitor a docker container for statistics collection. The <text-duration-period> value must be specified in [seconds, minutes, hours?]
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Set the monitoring duration of a docker container to one hour
cumulus@ts:~$ netq config add agent docker-monitor poll-period 3600
Related Commands
netq config add agent addons
netq config add agent loglevel
netq config add agent kubernetes-monitor

netq config add agent loglevel
Specifies the level of detail to display in the [system] log file[s?].
Syntax
	netq config add agent loglevel [debug|info|warning|error]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments
debug
Display errors, warnings, and informational events the system receives or generates.
info
Display only informational events
warning
Display warnings and informational events
error
Display xxx
Run From
	Telemetry server, leaf, spine, host?
JSON Output
	Not applicable
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	If no level is specified, the xxx level is used by default.
Changing the logging level takes place immediately, but prior content is not removed. 
[add definition of errors, warnings and info--what is the criteria/differentiation between…]
Sample Usage
	Set the display level of the [system?] log file to capture xxx
cumulus@ts:~$ netq config add agent loglevel warning
Related Commands
netq config add agent addons
netq config add agent docker-monitor
netq config add agent kubernetes-monitor

netq config add agent kubernetes-monitor
Installs [Starts? Enables?] the Kubernetes monitoring service on [all or specific node?].
Syntax
	netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
Abbreviated Syntax
	Not applicable
Required Arguments
	None
Optional Arguments	
poll-period
The amount of time to monitor a kubernetes container for statistics collection. The <text-duration-period> value must be specified in [seconds, minutes, hours?]
Run From
	Telemetry server, leaf, spine, host?
Command History

Release
Description
1.0
Introduced
Usage Guidelines
	Use this command when you want to xxx. Be careful of xxx. Note yyy.
Sample Usage
	Set the monitoring duration of a kubernetes container to one hour
cumulus@ts:~$ netq config add agent kubernetes-monitor poll-period 3600
Related Commands
netq config add agent addons
netq config add agent docker-monitor
netq config add agent loglevel

Parser Configuration Commands
Server Configuration Commands
Telemetry Server Configuration Commands


TRACE COMMAND

RESOLVE COMMANDS
AGENT NOTIFIER COMMANDS

 netq config (add|del) experimental
   netq config (add|del) agent (stats|sensors)
   netq config reload parser
   netq config show server [json]
   netq config add server <ip-server>|<text-server-name> [port <1025-65535>] [vrf <text-vrf>]
   netq config add server <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  [vrf <text-vrf>]
   netq config del server
   netq config (start|stop|status|restart) agent
   netq config add agent loglevel [debug|info|warning|error]
   netq config del agent loglevel
   netq config show agent [kubernetes-monitor|loglevel|stats|sensors|frr-monitor|wjh|wjh-threshold|cpu-limit] [json]
netq config add agent docker-monitor [poll-period <text-duration-period>]
netq config del agent docker-monitor
netq config ts add notifier slack <text-notifier-name> webhook <text-webhook-url> [severity info | severity warning | severity error | severity debug | severity info] [tag <text-slack-tag>]
   netq config ts add notifier pagerduty <text-notifier-name> api-access-key <text-api-access-key> api-integration-key <text-api-integration-key> [severity info | severity warning | severity error | severity debug | severity info]
   netq config ts add notifier pagerduty <text-notifier-name> api-integration-key <text-api-integration-key> api-access-key <text-api-access-key> [severity info | severity warning | severity error | severity debug | severity info]
   netq config ts add notifier filter <text-filter-name> before <text-filter-name-anchor>
   netq config ts add notifier filter <text-filter-name> after <text-filter-name-anchor>
   netq config ts add notifier filter <text-filter-name> rule (BgpSession|ClagSession|LnvSession|Link|Port|Services|OS|Temp|Fan|PSU|License) <text-rule-value>
   netq config ts add notifier filter <text-filter-name> output <text-notifier-name>
   netq config ts add notifier loglevel [debug|info|warning|error]
   netq config ts del notifier loglevel
   netq config ts del notifier slack|pagerduty <text-notifier-name>
   netq config ts del notifier filter <text-notifier-name>
   netq config ts (start|stop|status|restart) notifier
   netq config ts show notifier [json]
   netq config ts show notifier loglevel [json]
   netq config ts add server <ip-master> <ip-replica> <ip-replica>
   netq config ts show server [<ip-server>|<text-server-name>|config] [json]
   netq config ts reset-cluster
netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config del agent kubernetes-monitor


netq config 
Description
Syntax
Abbreviated Syntax
Required Arguments
Optional Arguments
JSON Output
Command History
Usage Guidelines
Sample Usage
Related Commands



netq
cumulus@switch:~$ netq help list

netq - Query data across all nodes in fabric

Usage:
   netq help [<text-keywords>]
   netq help verbose
   netq help list

   netq resolve [vrf <vrf>|vlan <1-4096>] [around <text-time>]
   netq trace <mac> [vlan <1-4096>] from <src-hostname> [vrf <vrf>] [around <text-time>] [json]
   netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json]

   netq [<hostname>] show docker container [<ipv4> | <ipv6>] [portmap] [name <container-name> | image <container-image> | service <swarm-service-name> | network <network-name> ] [around <text-time>] [json]
   netq [<hostname>] show docker container [<ipv4> | <ipv6>] [portmap] [name <container-name> | image <container-image> | service <swarm-service-name> | network <network-name> ] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker container [<ipv4> | <ipv6>] <proto> [<port>] [network <network-name>] [around <text-time>] [json]
   netq [<hostname>] show docker container [<ipv4> | <ipv6>] <proto> [<port>] [network <network-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker container [<ipv4> | <ipv6> | name <container-name> | image <container-image> | service <swarm-service-name> | network <network-name> ] connectivity [around <text-time>] [json]
   netq <hostname> show docker container adjacent [interfaces <remote-physical-interface>] [around <text-time>] [json]

   netq [<hostname>] show docker summary [<docker-version>] [around <text-time>] [json]
   netq [<hostname>] show docker summary [<docker-version>] changes [between <text-time> and <text-endtime>] [json]

    netq config add agent docker-monitor [poll-period <text-duration-period>]
    netq config del agent docker-monitor

   netq [<hostname>] show docker network [name <network-name> | <ipv4/prefixlen>] [brief] [around <text-time>] [json]
   netq [<hostname>] show docker network [name <network-name> | <ipv4/prefixlen>] [brief] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker network driver <network-driver> [brief] [around <text-time>] [json]
   netq [<hostname>] show docker network driver <network-driver> [brief] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show docker service [name <swarm-service-name> | mode <mode>] [around <text-time>] [json]
   netq [<hostname>] show docker service [name <swarm-service-name> | mode <mode>] connectivity [vrf <vrf>] [around <text-time>] [json]
   netq <hostname> show impact docker service [<swarm-service-name>] [vrf <vrf>] [around <text-time>] [json]

   netq [<hostname>] show docker swarm cluster [<cluster-name>] [node-name <cluster-node>] [around <text-time>] [json]
   netq <hostname>   show docker swarm cluster [<cluster-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker swarm network [<swarm-service-name>] [around <text-time>] [json]
   netq  <hostname>  show docker swarm network [<swarm-service-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show docker swarm node [<node-name> | role <role>] [cluster <cluster-name>] [around <text-time>] [json]
   netq  <hostname>  show docker swarm node [<node-name> | role <role>] [cluster <cluster-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show ntp [out-of-sync | in-sync] [around <text-time>] [json]
   netq [<hostname>] show ntp changes [between <text-time> and <text-endtime>] [json]
   netq check ntp [around <text-time>] [json]

   netq [<hostname>] show services [<service-name>] [vrf <vrf>] [active|monitored] [around <text-time>] [json]
   netq [<hostname>] show services [<service-name>] [vrf <vrf>] [active|monitored] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) [around <text-time>] [json]
   netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show services [<service-name>] [vrf <vrf>] status (ok|warning|error|fail) changes [json]

   netq [<hostname>] show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
   netq [<hostname>] show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
   netq [<hostname>] show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show interfaces [<remote-interface>] [state <remote-interface-state>] [around <text-time>] [count] [json]
   netq [<hostname>] show interfaces [<remote-interface>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan) [state <remote-interface-state>] [around <text-time>] [count] [json]
   netq [<hostname>] show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan) changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>]  [around <text-time>] [count] [json]
   netq [<hostname>] show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [count] [json]
   netq [<hostname>] show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
   netq [<hostname>] show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
   netq [<hostname>] show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show interfaces physical [<physical-port>] [empty|plugged] [peer] [vendor <module-vendor> | model <module-model>| module] [around <text-time>] [json]
   netq [<hostname>] show interfaces physical [<physical-port>] [empty|plugged] [vendor <module-vendor> | model <module-model> | module] changes [between <text-time> and <text-endtime>] [json]
   netq check interfaces [unverified] [<physical-hostname> <physical-port> | <physical-hostname>] [around <text-time>] [json]
   netq check interfaces <physical-hostname> <physical-port> and <peer-physical-hostname> <peer-physical-port> [around <text-time>] [json]

   netq check license [around <text-time>] [json]
   netq [<hostname>] show inventory brief [json]
   netq [<hostname>] show inventory asic [vendor <asic-vendor>| model <asic-model>| model-id <asic-model-id>] [json]
   netq [<hostname>] show inventory board [vendor <board-vendor>|model <board-model>] [json]
   netq [<hostname>] show inventory cpu [arch <cpu-arch>] [json]
   netq [<hostname>] show inventory disk [name <disk-name>|transport <disk-transport>| vendor <disk-vendor>] [json]
   netq [<hostname>] show inventory license [cumulus] [around <text-time>] [json]
   netq [<hostname>] show inventory license [cumulus] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show inventory memory [type <memory-type>|vendor <memory-vendor>] [json]
   netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [json]
   netq [<hostname>] show inventory os [version <os-version>|name <os-name>] changes [between <text-time> and <text-endtime>] [json]

   netq check sensors [around <text-time>] [json]
   netq [<hostname>] show sensors all [changes|around <text-time>] [json]
   netq [<hostname>] show sensors psu [<psu-name>] [changes|around <text-time>] [json]
   netq [<hostname>] show sensors temp [<temp-name>] [changes|around <text-time>] [json]
   netq [<hostname>] show sensors fan [<fan-name>] [changes|around <text-time>] [json]

   netq check evpn [around <text-time>] [json]
   netq [<hostname>] show evpn [vni <text-vni>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show evpn [vni <text-vni>] [around <text-time>] [json]

   netq check lnv [around <text-time>] [json]
   netq [<hostname>] show lnv [around <text-time>] [json]
   netq [<hostname>] show lnv changes [between <text-time> and <text-endtime>] [json]
   netq check vxlan [around <text-time>] [json]
   netq [<hostname>] show vxlan [vni <text-vni>] [around <text-time>] [json]
   netq [<hostname>] show vxlan [vni <text-vni>] changes [between <text-time> and <text-endtime>] [json]
   netq check agents [json]
   netq [<hostname>] show agents [changes] [json]

   netq [<hostname>] show changes [<ipv4>|<ipv6>|<ipv4> vrf <vrf>|<ipv6> vrf <vrf>|vrf <vrf>] between <text-time> and <text-endtime> [json]

   netq config (add|del) experimental
   netq config (add|del) addons
   netq config (add|del) agent (stats|sensors)
   netq config reload parser

   netq config show server [json]
   netq config add server <ip-server>|<text-server-name> [port <1025-65535>] [vrf <text-vrf>]
   netq config add server <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  <ip-server>|<text-server-name>  [vrf <text-vrf>]
   netq config del server


   netq config (start|stop|status|restart) agent
   netq config add agent loglevel [debug|info|warning|error]
   netq config del agent loglevel
   netq config show agent [kubernetes-monitor|docker-monitor|loglevel|stats|sensors] [json]

   netq example check bgp
   netq example check clag
   netq example check mtu
   netq example find-duplicates
   netq example find-origin
   netq example ha-setup
   netq example query
   netq example regexp
   netq example resolve macs
   netq example resolve routes
   netq example startup
   netq example stats
   netq example trace
   netq config ts add notifier slack <text-notifier-name> webhook <text-webhook-url> [severity info | severity warning | severity error | severity debug | severity info] [tag <text-slack-tag>]
   netq config ts add notifier pagerduty <text-notifier-name> api-access-key <text-api-access-key> api-integration-key <text-api-integration-key> [severity info | severity warning | severity error | severity debug | severity info]
   netq config ts add notifier pagerduty <text-notifier-name> api-integration-key <text-api-integration-key> api-access-key <text-api-access-key> [severity info | severity warning | severity error | severity debug | severity info]
   netq config ts add notifier filter <text-filter-name> before <text-filter-name-anchor>
   netq config ts add notifier filter <text-filter-name> after <text-filter-name-anchor>
   netq config ts add notifier filter <text-filter-name> rule (BgpSession|ClagSession|LnvSession|Link|Port|Services|OS|Temp|Fan|PSU|License) <text-rule-value>
   netq config ts add notifier filter <text-filter-name> output <text-notifier-name>
   netq config ts add notifier loglevel [debug|info|warning|error]
   netq config ts del notifier loglevel
   netq config ts del notifier slack|pagerduty <text-notifier-name>
   netq config ts del notifier filter <text-notifier-name>
   netq config ts (start|stop|status|restart) notifier
   netq config ts show notifier [json]
   netq config ts show notifier loglevel [json]


   netq config ts add server <ip-master> <ip-replica> <ip-replica>
   netq config ts show server [<ip-server>|<text-server-name>|config] [json]
   netq config ts reset-cluster

   netq ts decommission <hostname-to-purge> purge

   netq [<hostname>] show kubernetes cluster [name <kube-cluster-name>] [around <text-time>] [json]
   netq [<hostname>]   show kubernetes cluster [name <kube-cluster-name>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show kubernetes node [components] [name <kube-node-name>] [cluster <kube-cluster-name> ] [label <kube-node-label>] [around <text-time>] [json]
   netq [<hostname>]  show kubernetes node [components] [name <kube-node-name>] [cluster <kube-cluster-name> ] [label <kube-node-label>] changes [between <text-time> and <text-endtime>] [json]

    netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config del agent kubernetes-monitor

   netq [<hostname>] show kubernetes daemon-set [name <kube-ds-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-ds-label>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes daemon-set [name <kube-ds-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-ds-label>] connectivity [around <text-time>] [json]
   netq  [<hostname>]  show kubernetes daemon-set [name <kube-ds-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-ds-label>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes deployment [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes deployment [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] connectivity [around <text-time>] [json]
   netq [<hostname>] show kubernetes deployment [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes pod [name <kube-pod-name>] [cluster <kube-cluster-name> ] [namespace <namespace>] [label <kube-pod-label>] [pod-ip <kube-pod-ipaddress>] [node <kube-node-name>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes pod [name <kube-pod-name>] [cluster <kube-cluster-name> ] [namespace <namespace>] [label <kube-pod-label>] [pod-ip <kube-pod-ipaddress>] [node <kube-node-name>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes replication-controller [name <kube-rc-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rc-label>] [around <text-time>] [json]
   netq [<hostname>]  show kubernetes replication-controller [name <kube-rc-name>] [cluster <kube-cluster-name>] [namespace <namespace>]  [label <kube-rc-label>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes replica-set [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes replica-set [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] connectivity [around <text-time>] [json]
   netq [<hostname>]  show kubernetes replica-set [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show kubernetes service [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] [around <text-time>] [json]
   netq [<hostname>] show kubernetes service [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] connectivity [around <text-time>] [json]
   netq [<hostname>] show kubernetes service [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] changes [between <text-time> and <text-endtime>] [json]

   netq  <hostname>  show impact kubernetes service [master <kube-master-node>] [name <kube-service-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-service-label>] [service-cluster-ip <kube-service-cluster-ip>] [service-external-ip <kube-service-external-ip>] [around <text-time>] [json]
   netq <hostname> show impact kubernetes replica-set [master <kube-master-node>] [name <kube-rs-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-rs-label>] [around <text-time>] [json]
   netq <hostname> show impact kubernetes deployment [master <kube-master-node>] [name <kube-deployment-name>] [cluster <kube-cluster-name>] [namespace <namespace>] [label <kube-deployment-label>] [around <text-time>] [json]

   netq check clag [around <text-time>] [json]
   netq [<hostname>] show clag [around <text-time>] [json]
   netq [<hostname>] show clag changes [between <text-time> and <text-endtime>] [json]

   netq [<hostname>] show lldp [<remote-physical-interface>] [around <text-time>] [json]
   netq [<hostname>] show lldp [<remote-physical-interface>] changes [between <text-time> and <text-endtime>] [json]
   netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
   netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [around <text-time>] count [json]
   netq [<hostname>] show macs [<mac>] [vlan <1-4096>] [origin] changes [between <text-time> and <text-endtime>] [json]
   netq <hostname> show macs egress-port <egress-port> [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
   netq <hostname> show macs egress-port <egress-port> [<mac>] [vlan <1-4096>] [origin] changes [between <text-time> and <text-endtime>] [json]

   netq <hostname> show stp topology [around <text-time>] [json]

   netq check vlan [unverified] [around <text-time>] [json]
   netq [<hostname>] show vlan [<1-4096>] [around <text-time>] [json]
   netq [<hostname>] show vlan [<1-4096>] changes [between <text-time> and <text-endtime>] [json]

   netq check bgp [vrf <vrf>] [around <text-time>] [json]
   netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] [vrf <vrf>] [around <text-time>] [json]
   netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]

   netq check mtu [unverified] [around <text-time>] [json]
   netq check ospf [around <text-time>] [json]
   netq [<hostname>] show ospf [<remote-interface>] [area <area-id>] [around <text-time>] [json]
   netq [<hostname>] show ospf [<remote-interface>] [area <area-id>] changes [between <text-time> and <text-endtime>] [json]

Options:
   all                          : Information about all sub components
   around                       : Go back in time to around ...
   between                      : Specify start and end times for output desired
   config                       : Configure NetQ
   count                        : Count of matching entries
   example                      : Show examples of usage and workflow
   help                         : Show usage info
   ip                           : IPv4 related info
   ipv6                         : IPv6 related info
   json                         : Provide output in JSON
   list                         : Show all help commands
   notifier                     : Start/Stop/Restart/Query status of netq notifier
   origin                       : Owner of route or mac
   show                         : Show fabric-wide info about specified object
   verbose                      : More help on help
   <example>                    : name of example
   <hostname>                   : Name of the remote node you want to query
   <ip-server>                  : IP address of DB server
   <ipv4>                       : IPv4 address (no mask)
   <ipv6>                       : IPv6 address (no mask)
   <ip>                         : IPv4 or v6 address (no mask)
   <ipv4/prefixlen>             : IPv4 address with mask
   <ipv6/prefixlen>             : IPv6 address with mask
   <ip/prefixlen>               : IPv4 or IPv6 address with mask
   <mac>                        : MAC address
   <role>                       : Docker Swarm Node Role (worker, master)
   <text-time>                  : Time string such as 10m, 30s, 1h
   <text-endtime>               : Time string such as 10m, 30s, 1h
   <vrf>                        : Backend VRF
   <text-vlan>                  : VLAN

   resolve                      : Annotate input with names and interesting info

   trace                        : Control plane trace path across fabric
   from                         : Starting node or IP
   vlan                         : VLAN
   vrf                          : VRF
   <ip-src>                     : Source IP address used in trace
   <1-4096>                     : VLAN number range
   <vrf>                        : Name of VRF
   <mac>                        : MAC address
   <src-hostname>               : Hostname of source node for trace

   adjacent                     : Adjacent to the node
   container                    : Container information
   docker                       : Docker Info
   image                        : Container image name
   portmap                      : Check docker container exposed ports
   name                         : Container
   network                      : Container network information
   service                      : Docker Service
   <container-id>               : Container Id
   <container-image>            : Container image name
   <container-name>             : Container Name
   <network-name>               : Network name
   <port>                       : L4 Port
   <proto>                      : IP Protocol
   <remote-physical-interface>  : Name of the physical interface on the remote node
   <swarm-service-name>         : Name of Docker Swarm service

   docker                       : Docker Info
   summary                      : Summary of container info
   <docker-version>             : Docker engine version

    docker-monitor              : Monitor docker containers
    poll-period                 : Poll period in seconds (default is 15 seconds)
    <text-duration-period>      : Number of seconds for poll period between 10-120 seconds, inclusive

   brief                        : Summary information
   docker                       : Docker Info
   driver                       : Docker network driver
   name                         : Network name
   network                      : Network information
   <network-name>               : Docker Network Name
   <network-driver>             : Network Driver Name

   docker                       : Docker Info
   service                      : Service Info
   impact                       : Impact due to node outage
   connectivity                 : Connectivity graph
   mode                         : Docker service mode
   name                         : Swarm service
   <swarm-service-name>         : Name of the swarm service
   <mode>                       : Name of swarm service mode
   cluster                      : Server Cluster
   docker                       : Docker Info
   network                      : Network information
   mode                         : Docker service mode
   node                         : Compute node
   node-name                    : Docker Swarm node name
   role                         : Cluster node role
   swarm                        : Docker Swarm
   <cluster-name>               : Cluster name
   <cluster-node>               : Docker Swarm cluster node name
   <node-name>                  : Docker Swarm node name
   <role>                       : Cluster node role
   <swarm-service-name>         : Name of Docker Swarm service
   ntp                     : NTP
   out-of-sync             : NTP out of sync nodes
   in-sync                 : NTP in sync nodes
   active                       : Service is active
   error                        : Service has errors
   fail                         : Service has failed
   ok                           : Service is OK
   monitored                    : Service output is analyzed by NetQ
   services                     : System services
   warning                      : Service has warnings
   <service-name>               : Name of service

   addresses                    : IPv4/v6 addresses
   bond                         : Name of bond on device
   bridge                       : Name of bridge on device
   eth                          : ethX interface
   interfaces                   : network interface port
   loopback                     : Loopback interface
   macvlan                      : macvlan interface
   swp                          : swpX interface
   vlan                         : VLAN
   vrf                          : VRF
   vxlan                        : VxLAN
   state                        : Interface State
   type                         : Network interface type (such as bond, bridge)
   <remote-interface>           : Name of the interface on the remote node
   <remote-physical-interface>  : Name of the physical intf on the remote node
   <remote-interface-state>     : Interface State
   neighbors                    : IP neighbor info (ARP/ND)

   routes                       : IPv4/v6 routes
   empty                        : Empty Physical Interface
   module                       : Interface Module Info
   physical                     : Physical Interfaces
   plugged                      : Plugged Physical Interface
   peer                         : Peer Physical Interface
   and                          : Specify Peer Physical Interface
   model                        : Interface Module Model
   vendor                       : Interface Module Vendor
   <module-vendor>              : Interface Module Vendor
   <module-model>               : Interface Module Model
   <physical-port>              : Physical Interface name
   <physical-hostname>          : Hostname
   <peer-physical-hostname>     : Peer Hostname
   <peer-physical-port>         : Peer Physical Interface

   arch                         : CPU Architecture
   asic                         : Network Processor
   board                        : Switch Board
   brief                        : Brief summary
   cpu                          : Management Processor
   cumulus                      : Cumulus Linux
   disk                         : Storage Disk
   inventory                    : Inventory information
   license                      : License information
   memory                       : Hardware RAM
   model                        : Model
   model-id                     : Model ID
   name                         : Name of disk or OS
   os                           : Operating System
   transport                    : Disk Transport
   type                         : Memory type
   vendor                       : Vendor
   version                      : Version
   <asic-vendor>                : Network ASIC Vendor
   <asic-model>                 : Network ASIC Model
   <asic-model-id>              : Network ASIC Model ID
   <board-vendor>               : Board Vendor
   <board-model>                : Board Model
   <cpu-arch>                   : CPU Architecture
   <disk-name>                  : Disk Name
   <disk-transport>             : Disk Transport
   <disk-vendor>                : Disk Vendor
   <inventory-search>           : Search inventory for e.g., dell, trident2, x86, qsfp28, ddr3
   <memory-type>                : Memory Type info
   <memory-vendor>              : Memory Vendor
   <os-version>                 : Operating System version
   <os-name>                    : Operating System name

   fan                          : Fan sensor
   psu                          : Power supply sensor
   sensors                      : Temperature/Fan/PSU sensors
   temp                         : Temperature sensor
   <fan-name>                   : Fan sensor name
   <psu-name>                   : Power supply sensor name
   <temp-name>                  : Temperature sensor name

   vni                          : Virtual Network Id (or Vxlan ID)
   <text-vni>                   : VNI number to query
   evpn                         : EVPN

   check                        : Perform fabric-wide checks
   lnv                          : Lightweight Network Virtualization info
   check                        : Perform fabric-wide checks
   vxlan                        : VXLAN data path

   agents                       : Netq agent

   changes                      : How this infomation has changed with time

   add                          : Add feature
   del                          : Delete or remove feature
   experimental                 : Experimental features
   addons                       : Custom or user-specified features
   config                       : Configuration of NetQ
   reload                       : Reload configuration
   parser                       : Command parser
   stats                        : Start pushing interface metrics(experimental)
   add                          : Add netq server configuration
   del                          : Delete or remove netq server configuration
   server                       : Backend DB server
   show                         : Display current netq server configuration
   <ip-master>                  : Master data node for cluster
   <ip-replica>                 : IP address of replica server node
   <ip-server>                  : IP address of backend NetQ server_addr
   <text-server-name>           : Hostname of backend NetQ server
   <1025-65535>                 : TCP port of backend NetQ server
   <text-vrf>                   : VRF info
   agent                        : Troubleshooting daemon
   restart                      : Restart daemon
   start                        : Start daemon
   stop                         : Stop daemon
   status                       : Display daemon status
   debug                        : Debug-level
   info                         : Informational (default)
   warning                      : Warning conditions
   error                        : Error conditions
   loglevel                     : Daemon logging information
   docker-monitor               : Monitor docker containers
   kubernetes-monitor           : Monitor kubernetes events


   find-duplicates              : Find Duplicate IP or MAC
   find-origin                  : Find Origin of Route/MAC
   ha-setup                     : High Availability Setup
   query                        : Query using SQL-like NetQ Query Language
   regexp                       : Using Regular Expressions
   startup                      : NetQ Quickstart
   stats                        : Enable Gathering Interface Statistics
   trace                        : Control Path Trace
   resolve macs                 : Annotate MAC entries
   resolve routes               : Annotate your routing output
   check bgp                    : Check BGP Status Across the Fabric
   check clag                   : Check CLAG Status Across the Fabric
   check mtu                    : Check MTU Consistency Across the Fabric   restart                      : Restart daemon
   start                        : Start daemon
   stop                         : Stop daemon
   status                       : Display daemon status
   add                          : Add netq server/notifier configuration
   del                          : Delete netq notifier configuration
   notifier                     : Netq notifier integration
   loglevel                     : Daemon logging information
   integration                  : Integration with other notification systems
   filter                       : Filter the output before notifying integration
   severity                     : Optional Severity for notification (default is info)
   tag                          : Tag included with notification
   slack                        : Integration type for Slack
   pagerduty                    : Integration type for Pager Duty
   before                       : Position the object before the named object
   webhook                      : Slack integrations use a webhook URL to post messages
   output                       : Send the Notification to the named Integrator
   debug                        : Service has debugs
   info                         : Service has info
   warning                      : Service has warnings
   error                        : Service has errors
   rule                         : Define a filter object and regex match string
   after                        : Position the object after the named object
   api-access-key               : Pager Duty API Access Key
   api-integration-key          : Pager Duty Integration Key
   BgpSession                   : When BGP session state changes
   ClagSession                  : When CLAG role, peer role, peer state changes
   LnvSession                   : When Lnv session state changes
   Link                         : Notify when link oper_state changes
   Port                         : Notify when port is empty, plugged
   Services                     : When active service state changes
   OS                           : Notify when OS version changes
   Temp                         : Notify when sensor s_state changes
   Fan                          : Notify when sensor s_state changes
   PSU                          : Notify when sensor s_state changes
   License                      : Notify when license state changes
   <text-filter-name>           : Name of the filter
   <text-filter-name-anchor>    : Filter name used for inserting new filter
   <text-notifier-name>         : Textual name for notifier integration or filter
   <text-rule-key>              : Textual filter key
   <text-rule-value>            : Regular Expression used to filter based on key
   <text-webhook-url>           : Webhook URL used to direct Slack notifications
   <text-slack-tag>             : Optional Tag to include with Slack notifications
   <text-api-access-key>        : Value for Pager Duty API Access Key
   <text-api-integration-key>   : Value of Pager Duty Integration Key

   add                          : Add netq server/notifier configuration
   reset-cluster                : Reset DB cluster to force into known state
   server                       : Backend DB server
   show                         : Display current netq server configuration
   ts                           : Telemetry server
   <ip-master>                  : Master data node for cluster
   <ip-replica>                 : IP address of replica server node
   <ip-server>                  : IP address of backend NetQ server_addr
   <text-server-name>           : Hostname of backend NetQ server
   decommission                 : Decommission a node
   purge                        : Purge all the information from the DB
   <hostname-to-purge>          : Name of node whose info needs to be purged
   cluster                      : Server Cluster
   components                   : Compute Node components
   deployment                   : Pod Deployment
   kubernetes                   : Kubernetes Information
   node                         : Compute Node
   label                        : Kubernetes node
   <kube-cluster-name>          : Cluster name
   <kube-node-name>             : Kubernetes node name
    kubernetes-monitor          : Monitor kubernetes events
    poll-period                 : Poll period in seconds (default is 15 seconds)
    <text-duration-period>      : Number of seconds for poll period between 10-120 seconds, inclusive
   daemon-set                   : Daemon Set
   <kube-ds-name>               : Kubernetes Daemon Set name
   <kube-ds-label>              : Kubernetes Daemon Set Label
   deployment                   : Pod Deployment
   <kube-deployment-label>      : Deployment label
   <kube-deployment-name>       : Kubernetes Replication Controller name
   name                         : Kubernetes pod
   namespace                    : Namespace
   pod                          : Pod (Container Group)
   pod-ip                       : Pod IP address
   <kube-node-name>             : Kubernetes Node Name
   <kube-pod-label>             : Kubernetes Pod Label
   <kube-pod-name>              : Kubernetes Pod name
   <namespace>                  : Namespace name
   <kube-pod-ipaddress>         : Kuberentes Pod IP address
   replication-controller       : Kubernetes Replication Controller
   replica-set                  : Kubernetes Replica Set
   <kube-rc-name>               : Kubernetes Replication Controller name
   <kube-rs-name>               : Kubernetes Replica Set name
   <kube-rc-label>              : Kubernetes Replication Controller Label
   <kube-rs-label>              : Kubernetes Replication Set Label
    service-external-ip         : Kubernetes Service External IP
    service-cluster-ip          : Kubernetes Service Cluster IP
   <kube-service-label>         : Kubernetes Service Label
   <kube-service-name>          : Kubernetes Service name
   <kube-service-cluster-ip>    : Kubernetes Service Cluster IP
   <kube-service-external-ip>   : Kubernetes Service External IP
   deployment                   : Pod Deployment
   master                       : Master Node
   replica-set                  : Replica Set

   <kube-deployment-label>      : Deployment label
   <kube-deployment-name>       : Kubernetes Replication Controller name
   <kube-master-node>           : Kubernetes Master Node name
   <kube-rc-name>               : Kubernetes Replication Controller name
   <kube-rs-name>               : Kubernetes Replica Set name
   <kube-rc-label>              : Kubernetes Replication Controller Label
   <kube-rs-label>              : Kubernetes Replication Set Label
   <kube-service-label>         : Kubernetes service Label
   <kube-service-name>          : Kubernetes service name

   clag                         : Cumulus Multi-chassis LAG

   lldp                         : LLDP based neighbor info

   macs                         : Mac table or MAC address info
   egress-port                  : Outgoing interface
   <egress-port>                : Name of outgoing interface
   <0-4096>                     : VLAN ID
   <1-4096>                     : VLAN ID, between 1-4096


   stp                          : Spanning Tree
   topology                     : Active STP topology

   vlan                         : VLAN
   clag                         : Cumulus Multi-chassis LAG
   unverified                   : Show also the unverifiable interfaces

   bgp                          : BGP info
   asn                          : BGP Autonomous System Number (ASN)
   <bgp-session>                : BGP session (IP Address or interface name)
   <number-asn>                 : Specific ASN of interest

   mtu                          : Link MTU
   unverified                   : Show also the unverifiable interfaces

   ospf                         : OSPF info
   area                         : OSPF area
   <area-id>                    : Specific value of OSPF area


### Notification Commands Overview

The NetQ Command Line Interface (CLI) is used to filter and send notifications to third-party tools based on severity, service, event-type, and device. You can use TAB completion or the `help` option to assist when needed.

The command syntax for standard events is:

    ##Channels
    netq add notification channel slack <text-channel-name> webhook <text-webhook-url> [severity info|severity warning|severity error|severity debug] [tag <text-slack-tag>]
    netq add notification channel pagerduty <text-channel-name> integration-key <text-integration-key> [severity info|severity warning|severity error|severity debug]
     
    ##Rules and Filters
    netq add notification rule <text-rule-name> key <text-rule-key> value <text-rule-value>
    netq add notification filter <text-filter-name> [severity info|severity warning|severity error|severity debug] [rule <text-rule-name-anchor>] [channel <text-channel-name-anchor>] [before <text-filter-name-anchor>|after <text-filter-name-anchor>]
     
    ##Management
    netq del notification channel <text-channel-name-anchor>
    netq del notification filter <text-filter-name-anchor>
    netq del notification rule <text-rule-name-anchor>
    netq show notification [channel|filter|rule] [json]

The command syntax for events with user-configurable thresholds is:

    ##Rules and Filters
    netq add tca event_id <event-name> scope <regex-filter> [severity <critical|info>] threshold <value>

    ##Management
    netq add tca tca_id <tca-rule-name> is_active <true|false>
    netq add tca tca_id <tca-rule-name> channel drop <channel-name>
    netq del tca tca_id <tca-rule-name>
    netq show tca [tca_id <tca-rule-name>]

The command syntax for a server proxy is:

    ##Proxy
    netq add notification proxy <text-proxy-hostname> [port <text-proxy-port>]
    netq show notification proxy
    netq del notification proxy

The various command options are described in the following sections where they are used.

## LCM Commands

The NetQ CLI provides a number of `netq lcm` commands to perform LCM. The syntax of these commands is:

    netq lcm upgrade name <text-job-name> image-id <text-image-id> license <text-cumulus-license> hostnames <text-switch-hostnames> [order <text-upgrade-order>] [run-before-after]
    netq lcm add credentials (username <text-switch-username> password <text-switch-password> | ssh-key <text-ssh-key>)
    netq lcm add role (superspine | spine | leaf | exit) switches <text-switch-hostnames>
    netq lcm del credentials
    netq lcm show credentials [json]
    netq lcm show switches [version <text-cumulus-linux-version>] [json]
    netq lcm show status <text-lcm-job-id> [json]
    netq lcm add image <text-image-path>
    netq lcm del image <text-image-id>
    netq lcm show images [<text-image-id>] [json]
    netq lcm show upgrade-jobs [json]

## Agent Commands

The agent configuration commands include:

    netq config add agent cluster-servers <text-opta-ip-list> [port <text-opta-port>] [vrf <text-vrf-name>]
    netq config add agent cpu-limit [<text-limit-number>]
    netq config add agent frr-monitor [<text-frr-docker-name>]
    netq config add agent kubernetes-monitor [poll-period <text-duration-period>]
    netq config add agent loglevel [debug|error|info|warning]
    netq config add agent sensors
    netq config add agent server <text-opta-ip> [port <text-opta-port>] [vrf <text-vrf-name>]
    netq config (start|stop|status|restart) agent
    netq config del agent (cluster-servers|cpu-limit|frr-monitor|kubernetes-monitor|loglevel|sensors|server|stats|wjh)
    netq config show agent [cpu-limit|frr-monitor|kubernetes-monitor|loglevel|sensors|stats|wjh] [json]

## Inventory Commands

### Hardware Commands

The NetQ CLI provides a number of commands to monitor hardware inventory on switches. The syntax of these commands is:

```
netq [<hostname>] show inventory brief [opta] [json]
netq [<hostname>] show inventory asic [vendor <asic-vendor>|model <asic-model>|model-id <asic-model-id>] [opta] [json]
netq [<hostname>] show inventory board [vendor <board-vendor>|model <board-model>] [opta] [json]
netq [<hostname>] show inventory cpu [arch <cpu-arch>] [opta] [json]
netq [<hostname>] show inventory disk [name <disk-name>|transport <disk-transport>|vendor <disk-vendor>] [opta] [json]
netq [<hostname>] show inventory license [cumulus] [status ok|status missing] [around <text-time>] [opta] [json]
netq [<hostname>] show inventory memory [type <memory-type>|vendor <memory-vendor>] [opta] [json]
netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [opta] [json]

netq [<hostname>] show sensors all [around <text-time>] [json]
netq [<hostname>] show sensors psu [<psu-name>] [around <text-time>] [json]
netq [<hostname>] show sensors temp [<temp-name>] [around <text-time>] [json]
netq [<hostname>] show sensors fan [<fan-name>] [around <text-time>] [json]

netq [<hostname>] show interface-stats [errors|all] [<physical-port>] [around <text-time>] [json]
netq [<hostname>] show interface-utilization [<text-port>] [tx|rx] [around <text-time>] [json]
netq [<hostname>] show resource-util [cpu | memory] [around <text-time>] [json]
netq [<hostname>] show resource-util disk [<text-diskname>] [around <text-time>] [json]
netq [<hostname>] show cl-ssd-util [around <text-time>] [json]
netq [<hostname>] show cl-btrfs-info [around <text-time>] [json]
```

{{<notice note>}}
The keyword values for the <code>vendor</code>, <code>model</code>, <code>model-id</code>, <code>arch</code>, <code>name</code>, <code>transport</code>, <code>type</code>, <code>version</code>, <code>psu</code>, <code>temp</code>, and <code>fan</code> keywords are specific to your deployment. For example, if you have devices with CPU architectures of only one type, say Intel x86, then that is the only option available for the <code>cpu-arch</code> keyword value. If you have multiple CPU architectures, say you also have ARMv7, then that would also be an option for you.
{{</notice>}}

### Software Commands

The NetQ CLI provides a number of commands to monitor software inventory on switches. The syntax for these commands is:

```
netq [<hostname>] show agents
netq [<hostname>] show inventory brief [json]
netq [<hostname>] show inventory license [cumulus] [status ok|status missing] [around <text-time>] [json]
netq [<hostname>] show inventory os [version <os-version>|name <os-name>] [json]

netq [<hostname>] show cl-manifest [json]
netq [<hostname>] show cl-pkg-info [<text-package-name>] [around <text-time>] [json]
netq [<hostname>] show recommended-pkg-version [release-id <text-release-id>] [package-name <text-package-name>] [json]
netq [<hostname>] show cl-resource acl [ingress | egress] [around <text-time>] [json]
netq [<hostname>] show cl-resource forwarding [around <text-time>] [json]
```

{{<notice note>}}
The values for the <code>name</code> option are specific to your deployment. For example, if you have devices with only one type of OS, say Cumulus Linux, then that is the only option available for the <code>os-name</code> option value. If you have multiple OSs running, say you also have Ubuntu, then that would also be an option for you.
{{</notice>}}
