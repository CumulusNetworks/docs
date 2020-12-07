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

## View Status for All Interfaces

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
