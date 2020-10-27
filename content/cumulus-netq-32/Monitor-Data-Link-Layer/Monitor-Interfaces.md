---
title: Monitor Interfaces
author: Cumulus Networks
weight: 880
toc: 3
---
Interface (link) health can be monitored using the `netq show interfaces` command. You can view status of the links, whether they are operating over a VRF interface, the MTU of the link, and so forth. Using the `hostname` option enables you to view only the interfaces for a given device. View changes to interfaces using the `netq show events` command.

The syntax for these commands is:

```
netq [<hostname>] show interfaces [type bond|type bridge|type eth|type loopback|type macvlan|type swp|type vlan|type vrf|type vxlan] [state <remote-interface-state>] [around <text-time>] [json]
netq <hostname> show interfaces [type bond|type bridge|type eth|type loopback|type macvlan|type swp|type vlan|type vrf|type vxlan] [state <remote-interface-state>] [around <text-time>] [count] [json]
netq [<hostname>] show events [level info | level error | level warning | level critical | level debug] type interfaces [between <text-time> and <text-endtime>] [json]
```

### View Status for All Interfaces

Viewing the status of all interfaces at once can be helpful when you are trying to compare configuration or status of a set of links, or generally when changes have been made.

This example shows all interfaces networkwide.

```
cumulus@switch:~$ netq show interfaces
Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
exit01            bridge                    bridge           up         default         , Root bridge:  exit01,             Mon Apr 29 20:57:59 2019
                                                                                        Root port: , Members:  vxlan4001,
                                                                                        bridge,
exit01            eth0                      eth              up         mgmt            MTU: 1500                           Mon Apr 29 20:57:59 2019
exit01            lo                        loopback         up         default         MTU: 65536                          Mon Apr 29 20:57:58 2019
exit01            mgmt                      vrf              up                         table: 1001, MTU: 65536,            Mon Apr 29 20:57:58 2019
                                                                                        Members:  mgmt,  eth0,
exit01            swp1                      swp              down       default         VLANs: , PVID: 0 MTU: 1500          Mon Apr 29 20:57:59 2019
exit01            swp44                     swp              up         vrf1            VLANs: ,                            Mon Apr 29 20:57:58 2019
                                                                                        PVID: 0 MTU: 1500 LLDP: internet:sw
                                                                                        p1
exit01            swp45                     swp              down       default         VLANs: , PVID: 0 MTU: 1500          Mon Apr 29 20:57:59 2019
exit01            swp46                     swp              down       default         VLANs: , PVID: 0 MTU: 1500          Mon Apr 29 20:57:59 2019
exit01            swp47                     swp              down       default         VLANs: , PVID: 0 MTU: 1500          Mon Apr 29 20:57:59 2019
    
...
    
leaf01            bond01                    bond             up         default         Slave:swp1 LLDP: server01:eth1      Mon Apr 29 20:57:59 2019
leaf01            bond02                    bond             up         default         Slave:swp2 LLDP: server02:eth1      Mon Apr 29 20:57:59 2019
leaf01            bridge                    bridge           up         default         , Root bridge:  leaf01,             Mon Apr 29 20:57:59 2019
                                                                                        Root port: , Members:  vxlan4001,
                                                                                        bond02,  vni24,  vni13,  bond01,
                                                                                        bridge,  peerlink,
leaf01            eth0                      eth              up         mgmt            MTU: 1500                           Mon Apr 29 20:58:00 2019
leaf01            lo                        loopback         up         default         MTU: 65536                          Mon Apr 29 20:57:59 2019
leaf01            mgmt                      vrf              up                         table: 1001, MTU: 65536,            Mon Apr 29 20:57:59 2019
                                                                                        Members:  mgmt,  eth0,
leaf01            peerlink                  bond             up         default         Slave:swp50 LLDP: leaf02:swp49 LLDP Mon Apr 29 20:58:00 2019
                                                                                        : leaf02:swp50
...
```

## View Interface Status for a Given Device

If you are interested in only a the interfaces on a specific device, you can view only those.

This example shows all interfaces on the *spine01* device.

```
cumulus@switch:~$ netq spine01 show interfaces
Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
spine01           eth0                      eth              up         mgmt            MTU: 1500                           Mon Apr 29 21:12:47 2019
spine01           lo                        loopback         up         default         MTU: 65536                          Mon Apr 29 21:12:47 2019
spine01           mgmt                      vrf              up                         table: 1001, MTU: 65536,            Mon Apr 29 21:12:46 2019
                                                                                        Members:  mgmt,  eth0,
spine01           swp1                      swp              up         default         VLANs: ,                            Mon Apr 29 21:12:47 2019
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf01:swp5
                                                                                        1
spine01           swp2                      swp              up         default         VLANs: ,                            Mon Apr 29 21:12:47 2019
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf02:swp5
                                                                                        1
spine01           swp29                     swp              up         default         VLANs: ,                            Mon Apr 29 21:12:47 2019
                                                                                        PVID: 0 MTU: 9216 LLDP: exit02:swp5
                                                                                        1
spine01           swp3                      swp              up         default         VLANs: ,                            Mon Apr 29 21:12:46 2019
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf03:swp5
                                                                                        1
spine01           swp30                     swp              up         default         VLANs: ,                            Mon Apr 29 21:12:47 2019
                                                                                        PVID: 0 MTU: 9216 LLDP: exit01:swp5
                                                                                        1
spine01           swp31                     swp              up         default         VLANs: ,                            Mon Apr 29 21:12:46 2019
                                                                                        PVID: 0 MTU: 9216 LLDP: spine02:swp
                                                                                        31
spine01           swp32                     swp              up         default         VLANs: ,                            Mon Apr 29 21:12:46 2019
                                                                                        PVID: 0 MTU: 9216 LLDP: spine02:swp
                                                                                        32
spine01           swp4                      swp              up         default         VLANs: ,                            Mon Apr 29 21:12:47 2019
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf04:swp5
                                                                                        1
```

## View All Interfaces of a Given Type

It can be can be useful to see the status of a particular type of interface.

This example shows all bond interfaces that are down, and then those that are up.

```
cumulus@switch:~$ netq show interfaces type bond state down
No matching link records found
    
cumulus@switch:~$ netq show interfaces type bond state up
Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
leaf01            bond01                    bond             up         default         Slave:swp1 LLDP: server01:eth1      Mon Apr 29 21:19:07 2019
leaf01            bond02                    bond             up         default         Slave:swp2 LLDP: server02:eth1      Mon Apr 29 21:19:07 2019
leaf01            peerlink                  bond             up         default         Slave:swp50 LLDP: leaf02:swp49 LLDP Mon Apr 29 21:19:07 2019
                                                                                        : leaf02:swp50
leaf02            bond01                    bond             up         default         Slave:swp1 LLDP: server01:eth2      Mon Apr 29 21:19:07 2019
leaf02            bond02                    bond             up         default         Slave:swp2 LLDP: server02:eth2      Mon Apr 29 21:19:07 2019
leaf02            peerlink                  bond             up         default         Slave:swp50 LLDP: leaf01:swp49 LLDP Mon Apr 29 21:19:07 2019
                                                                                        : leaf01:swp50
leaf03            bond03                    bond             up         default         Slave:swp1 LLDP: server03:eth1      Mon Apr 29 21:19:07 2019
leaf03            bond04                    bond             up         default         Slave:swp2 LLDP: server04:eth1      Mon Apr 29 21:19:07 2019
leaf03            peerlink                  bond             up         default         Slave:swp50 LLDP: leaf04:swp49 LLDP Mon Apr 29 21:19:07 2019
                                                                                        : leaf04:swp50
leaf04            bond03                    bond             up         default         Slave:swp1 LLDP: server03:eth2      Mon Apr 29 21:19:07 2019
leaf04            bond04                    bond             up         default         Slave:swp2 LLDP: server04:eth2      Mon Apr 29 21:19:07 2019
leaf04            peerlink                  bond             up         default         Slave:swp50 LLDP: leaf03:swp49 LLDP Mon Apr 29 21:19:07 2019
                                                                                        : leaf03:swp50
server01          bond0                     bond             up         default         Slave:bond0 LLDP: leaf02:swp1       Mon Apr 29 21:19:07 2019
server02          bond0                     bond             up         default         Slave:bond0 LLDP: leaf02:swp2       Mon Apr 29 21:19:07 2019
server03          bond0                     bond             up         default         Slave:bond0 LLDP: leaf04:swp1       Mon Apr 29 21:19:07 2019
server04          bond0                     bond             up         default         Slave:bond0 LLDP: leaf04:swp2       Mon Apr 29 21:19:07 2019
```

## View the Total Number of Interfaces

For a quick view of the amount of interfaces currently operating on a device, use the `hostname` and `count` options together.

This example shows the count of interfaces on the *leaf03* switch.

```
cumulus@switch:~$ netq leaf03 show interfaces count
Count of matching link records: 28
```

## View the Total Number of a Given Interface Type

It can be useful to see how many interfaces of a particular type you have on a device.

This example shows the count of swp interfaces are on the *leaf03* switch.

```
cumulus@switch:~$ netq leaf03 show interfaces type swp count
Count of matching link records: 11
```

## View Changes to Interfaces

If you suspect that an interface is not working as expected, seeing a drop in performance or a large number of dropped messages for example, you can view changes that have been made to interfaces networkwide.

This example shows info level events for all interfaces in your network.

```
cumulus@switch:~$ netq show events level info type interfaces between now and 30d
Matching events records:
Hostname          Message Type             Severity         Message                             Timestamp
----------------- ------------------------ ---------------- ----------------------------------- -------------------------
server03          link                     info             HostName server03 changed state fro 3d:12h:8m:28s
                                                            m down to up Interface:eth2
server03          link                     info             HostName server03 changed state fro 3d:12h:8m:28s
                                                            m down to up Interface:eth1
server01          link                     info             HostName server01 changed state fro 3d:12h:8m:30s
                                                            m down to up Interface:eth2
server01          link                     info             HostName server01 changed state fro 3d:12h:8m:30s
                                                            m down to up Interface:eth1
server02          link                     info             HostName server02 changed state fro 3d:12h:8m:34s
                                                            m down to up Interface:eth2
...
```

## Check for MTU Inconsistencies

The maximum transmission unit (MTU) determines the largest size packet or frame that can be transmitted across a given communication link. When the MTU is not configured to the same value on both ends of the link, communication problems can occur. With NetQ, you can verify that the MTU is correctly specified for each link using the netq check mtu command.

This example shows that four switches have inconsistently specified link MTUs. Now the network administrator or operator can reconfigure the switches and eliminate the communication issues associated with this misconfiguration.

```
cumulus@switch:~$ netq check mtu
Checked Nodes: 15, Checked Links: 215, Failed Nodes: 4, Failed Links: 7
MTU mismatch found on following links
Hostname          Interface                 MTU    Peer              Peer Interface            Peer MTU Error
----------------- ------------------------- ------ ----------------- ------------------------- -------- ---------------
spine01           swp30                     9216   exit01            swp51                     1500     MTU Mismatch
exit01            swp51                     1500   spine01           swp30                     9216     MTU Mismatch
spine01           swp29                     9216   exit02            swp51                     1500     MTU Mismatch
exit02            -                         -      -                 -                         -        Rotten Agent
exit01            swp52                     1500   spine02           swp30                     9216     MTU Mismatch
spine02           swp30                     9216   exit01            swp52                     1500     MTU Mismatch
spine02           swp29                     9216   exit02            swp52                     1500     MTU Mismatch
```


## Validate Paths between Devices

If you have VLANs configured, you can view the available paths between two devices on the VLAN currently and at a time in the past using their MAC addresses  . You can view the output in one of three formats (*json*, *pretty*, and *detail*). JSON output provides the output in a JSON file format for ease of importing to other applications or software. Pretty output lines up the paths in a pseudo-graphical manner to help visualize multiple paths. Detail output is useful for traces with higher hop counts where the pretty output wraps lines, making it harder to interpret the results. The detail output displays a table with a row for each path.

To view the paths:

1.  Identify the MAC address and VLAN ID for the destination device

2.  Identify the IP address or hostname for the source device

3.  Use the `netq trace` command to see the available paths between
    those devices.

The trace command syntax is:

    netq trace <mac> [vlan <1-4096>] from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]

{{%notice note%}}

The syntax requires the destination device address first, `mac`, and
then the source device address or hostname. Additionally, the `vlan`
keyword-value pair is required for layer 2 traces even though the syntax
indicates it is optional.

The tracing function only knows about addresses that have already been
learned. If you find that a path is invalid or incomplete, you may need
to ping the identified device so that its address becomes known.

{{%/notice%}}

### View Paths between Two Switches with Pretty Output

This example shows the available paths between a top of rack switch,
*tor-1*, and a server, *server11*. The request is to go through VLAN
*1001* from the VRF *vrf1*. The results include a summary of the trace,
including the total number of paths available, those with errors and
warnings, and the MTU of the paths. In this case, the results are
displayed in pseudo-graphical output.

```
cumulus@switch:~$ netq trace 00:02:00:00:00:02 vlan 1001 from leaf01 vrf vrf1 pretty
Number of Paths: 4
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9152
 leaf01 vni: 34 uplink-2 -- downlink-5 spine02 downlink-2 -- uplink-2 vni: 34 leaf12 hostbond4 -- swp2 server11  
               uplink-2 -- downlink-5 spine02 downlink-1 -- uplink-2 vni: 34 leaf11 hostbond4 -- swp1 server11  
 leaf01 vni: 34 uplink-1 -- downlink-5 spine01 downlink-2 -- uplink-1 vni: 34 leaf12 hostbond4 -- swp2 server11  
               uplink-1 -- downlink-5 spine01 downlink-1 -- uplink-1 vni: 34 leaf11 hostbond4 -- swp1 server11    
```

Alternately, you can use the IP address of the source device, as shown
in this example.

    cumulus@redis-1:~$  netq trace 00:02:00:00:00:02 vlan 1001 from 10.0.0.8 vrf vrf1 pretty
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
     server11 swp1 -- swp5 <vlan1000> tor-1 <vlan1001> vni: 34 uplink-2 -- downlink-5 spine02 downlink-2 -- uplink-2 vni: 34 <vlan1001> leaf12 hostbond4 -- swp2 server11  
                                                               uplink-2 -- downlink-5 spine02 downlink-1 -- uplink-2 vni: 34 <vlan1001> leaf11 hostbond4 -- swp1 server11  
              swp1 -- swp5 <vlan1000> tor-1 <vlan1001> vni: 34 uplink-1 -- downlink-5 spine01 downlink-2 -- uplink-1 vni: 34 <vlan1001> leaf12 hostbond4 -- swp2 server11  
                                                               uplink-1 -- downlink-5 spine01 downlink-1 -- uplink-1 vni: 34 <vlan1001> leaf11 hostbond4 -- swp1 server11

### View Paths between Two Switches with Detailed Output

This example provides the same path information as the pretty output,
but displays the information in a tabular output.

    cumulus@switch:~$ netq trace 00:02:00:00:00:02 vlan 1001 from 10.0.0.8 vrf vrf1 detail
    Number of Paths: 4
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 9152
    Id  Hop Hostname        InPort          InVlan InTunnel              InRtrIf         InVRF           OutRtrIf        OutVRF          OutTunnel             OutPort         OutVlan
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    1   1   server11                                                                                                                                           swp1            1000
        2   leaf01          swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-2
        3   spine02         downlink-5                                   downlink-5      default         downlink-2      default                               downlink-2
        4   leaf12          uplink-2               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   server11        swp2
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    2   1   server11                                                                                                                                           swp1            1000
        2   leaf01          swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-2
        3   spine02         downlink-5                                   downlink-5      default         downlink-1      default                               downlink-1
        4   leaf11          uplink-2               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   server11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    3   1   server11                                                                                                                                           swp1            1000
        2   leaf01          swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-1
        3   spine01         downlink-5                                   downlink-5      default         downlink-2      default                               downlink-2
        4   leaf12          uplink-1               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   server11        swp2
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    4   1   server11                                                                                                                                           swp1            1000
        2   leaf01          swp5            1000                         vlan1000        vrf1            vlan1001        vrf1            vni: 34               uplink-1
        3   spine01         downlink-5                                   downlink-5      default         downlink-1      default                               downlink-1
        4   leaf11          uplink-1               vni: 34               vlan1001        vrf1                                                                  hostbond4       1001
        5   server11        swp1
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------

### View Paths between Two Switches with Drops Detected

If you have a Mellanox switch, the What Just Happened feature detects various drop statistics. These are visible in the results of trace requests. This example shows the available paths between a switch with IP address 6.0.2.66 and a switch with IP address 6.0.2.70, where drops have been detected on path 1.

```
cumulus@mlx-2700:~$ netq trace 6.0.2.66 from 6.0.2.70
Number of Paths: 1
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Top packet drops along the paths in the last hour:
  Path: 1 at mlx-2700:swp3s1, type: L2, reason: Source MAC equals destination MAC, flow: src_ip: 6.0.2.70, dst_ip: 6.0.2.66, protocol: 0, src_port: 0, dst_port: 0
Path MTU: 9152
Id  Hop Hostname    InPort          InTun, RtrIf    OutRtrIf, Tun   OutPort
--- --- ----------- --------------- --------------- --------------- ---------------
1   1   hosts-11                                                    swp1.1008
    2   mlx-2700-03 swp3s1
--- --- ----------- --------------- --------------- --------------- ---------------
```

## Monitor Layer 2 Drops on Mellanox Switches

The *What Just Happened* (WJH) feature, available on Mellanox switches, streams detailed and contextual telemetry data for analysis. This provides real-time visibility into problems in the network, such as hardware packet drops due to buffer congestion, incorrect routing, and ACL or layer 1 problems. You must have Cumulus Linux 4.0.0 or later and NetQ 2.4.0 or later to take advantage of this feature.

When WJH capabilities are combined with Cumulus Linux 4.0.0 and NetQ 2.4.0, giving you the ability to hone in on losses, anywhere in the fabric, from a single management console. You can:

- View any current or historic drop information, including the reason for the drop
- Identify problematic flows or endpoints, and pin-point exactly where communication is failing in the network

{{%notice info%}}
By default, Cumulus Linux 4.0.0 provides the NetQ 2.3.1 Agent and CLI. If you installed Cumulus Linux 4.0.0 on your Mellanox switch, you need to upgrade the NetQ Agent and optionally the CLI to release 2.4.0 or later.

```
cumulus@<hostname>:~$ sudo apt-get update
cumulus@<hostname>:~$ sudo apt-get install -y netq-agent
cumulus@<hostname>:~$ netq config restart agent
cumulus@<hostname>:~$ sudo apt-get install -y netq-apps
cumulus@<hostname>:~$ netq config restart cli
```

{{%/notice%}}

### Configure the WJH Feature

WJH is enabled by default on Mellanox switches and no configuration is required in Cumulus Linux 4.0.0; however, you must enable the NetQ Agent to collect the data in NetQ 2.4.0.

To enable WJH in NetQ:

1. Configure the NetQ Agent on the Mellanox switch.

```
cumulus@switch:~$ netq config add agent wjh
```

2. Restart the NetQ Agent to start collecting the WJH data.

```
cumulus@switch:~$ netq config restart agent
```

When you are finished viewing the WJH metrics, you might want to disable the NetQ Agent to reduce network traffic. Use `netq config del agent wjh` followed by `netq config restart agent` to disable the WJH feature on the given switch.

{{%notice note%}}
Using *wjh_dump.py* on a Mellanox platform that is running Cumulus Linux 4.0 and the NetQ 2.4.0 agent causes the NetQ WJH client to stop receiving packet drop call backs. To prevent this issue, run *wjh_dump.py* on a different system than the one where the NetQ Agent has WJH enabled, or disable *wjh_dump.py* and restart the NetQ Agent (run `netq config restart agent`).
{{%/notice%}}

### View What Just Happened Metrics

View layer 2 drop statistics using the `netq show wjh-drop` NetQ CLI command. The full syntax for this command is:

```
netq [<hostname>] show wjh-drop <text-drop-type>] [ingress-port <text-ingress-port>] [reason <text-reason>] [src-ip <text-src-ip>] [dst-ip <text-dst-ip>] [proto <text-proto>] [src-port <text-src-port>] [dst-port <text-dst-port>] [src-mac <text-src-mac>] [dst-mac <text-dst-mac>] [egress-port <text-egress-port>;] [traffic-class <text-traffic-class>] [rule-id-acl <text-rule-id-acl>] [between <text-time> and <text-endtime>] [around <text-time>] [json]
```

This example shows the drops seen at layer 2 across the network:

```
cumulus@mlx-2700-03:mgmt:~$ netq show wjh-drop l2
Matching wjh records:
Hostname          Ingress Port             Reason                                        Agg Count          Src Ip           Dst Ip           Proto  Src Port         Dst Port         Src Mac            Dst Mac            First Timestamp                Last Timestamp
----------------- ------------------------ --------------------------------------------- ------------------ ---------------- ---------------- ------ ---------------- ---------------- ------------------ ------------------ ------------------------------ ----------------------------
mlx-2700-03       swp1s2                   Port loopback filter                          10                 27.0.0.19        27.0.0.22        0      0                0                00:02:00:00:00:73  0c:ff:ff:ff:ff:ff  Mon Dec 16 11:54:15 2019       Mon Dec 16 11:54:15 2019
mlx-2700-03       swp1s2                   Source MAC equals destination MAC             10                 27.0.0.19        27.0.0.22        0      0                0                00:02:00:00:00:73  00:02:00:00:00:73  Mon Dec 16 11:53:17 2019       Mon Dec 16 11:53:17 2019
mlx-2700-03       swp1s2                   Source MAC equals destination MAC             10                 0.0.0.0          0.0.0.0          0      0                0                00:02:00:00:00:73  00:02:00:00:00:73  Mon Dec 16 11:40:44 2019       Mon Dec 16 11:40:44 2019
```
