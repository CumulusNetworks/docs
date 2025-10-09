---
title: Monitor Interfaces
author: NVIDIA
weight: 880
toc: 3
---
Interface (link) health can be monitored using the `netq show interfaces` command. You can view status of the links, whether they are operating over a VRF interface, the MTU of the link, and so forth. Using the `hostname` option enables you to view only the interfaces for a given device. View changes to interfaces using the `netq show events` command.

The syntax for these commands is:

```
netq show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan) [state <remote-interface-state>] [around <text-time>] [json]
netq <hostname> show interfaces type (bond|bridge|eth|loopback|macvlan|swp|vlan|vrf|vxlan) [state <remote-interface-state>] [around <text-time>] [count] [json]
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
spine01           swp5                      swp              up         default         VLANs: ,                            Mon Jan 11 05:56:54 2021
                                                                                        PVID: 0 MTU: 9216 LLDP: border01:sw
                                                                                        p51
spine01           swp6                      swp              up         default         VLANs: ,                            Mon Jan 11 05:56:54 2021
                                                                                        PVID: 0 MTU: 9216 LLDP: border02:sw
                                                                                        p51
spine01           lo                        loopback         up         default         MTU: 65536                          Mon Jan 11 05:56:54 2021
spine01           eth0                      eth              up         mgmt            MTU: 1500                           Mon Jan 11 05:56:54 2021
spine01           vagrant                   swp              down       default         VLANs: , PVID: 0 MTU: 1500          Mon Jan 11 05:56:54 2021
spine01           mgmt                      vrf              up         mgmt            table: 1001, MTU: 65536,            Mon Jan 11 05:56:54 2021
                                                                                        Members:  eth0,  mgmt,
spine01           swp1                      swp              up         default         VLANs: ,                            Mon Jan 11 05:56:54 2021
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf01:swp5
                                                                                        1
spine01           swp2                      swp              up         default         VLANs: ,                            Mon Jan 11 05:56:54 2021
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf02:swp5
                                                                                        1
spine01           swp3                      swp              up         default         VLANs: ,                            Mon Jan 11 05:56:54 2021
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf03:swp5
                                                                                        1
spine01           swp4                      swp              up         default         VLANs: ,                            Mon Jan 11 05:56:54 2021
                                                                                        PVID: 0 MTU: 9216 LLDP: leaf04:swp5
                                                                                        1
cumulus@switch:~$ 
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
border01          peerlink                  bond             up         default         Slave: swp49 (LLDP: border02:swp49) Mon Jan 11 05:56:35 2021
                                                                                        ,
                                                                                        Slave: swp50 (LLDP: border02:swp50)
border01          bond1                     bond             up         default         Slave: swp3 (LLDP: fw1:swp1)        Mon Jan 11 05:56:36 2021
border02          peerlink                  bond             up         default         Slave: swp49 (LLDP: border01:swp49) Mon Jan 11 05:56:38 2021
                                                                                        ,
                                                                                        Slave: swp50 (LLDP: border01:swp50)
border02          bond1                     bond             up         default         Slave: swp3 (LLDP: fw1:swp2)        Mon Jan 11 05:56:38 2021
fw1               borderBond                bond             up         default         Slave: swp1 (LLDP: border01:swp3),  Mon Jan 11 05:56:36 2021
                                                                                        Slave: swp2 (LLDP: border02:swp3)
leaf01            bond2                     bond             up         default         Slave: swp2 (LLDP: server02:mac:44: Mon Jan 11 05:56:39 2021
                                                                                        38:39:00:00:34)
leaf01            peerlink                  bond             up         default         Slave: swp49 (LLDP: leaf02:swp49),  Mon Jan 11 05:56:39 2021
                                                                                        Slave: swp50 (LLDP: leaf02:swp50)
leaf01            bond3                     bond             up         default         Slave: swp3 (LLDP: server03:mac:44: Mon Jan 11 05:56:39 2021
                                                                                        38:39:00:00:36)
leaf01            bond1                     bond             up         default         Slave: swp1 (LLDP: server01:mac:44: Mon Jan 11 05:56:39 2021
                                                                                        38:39:00:00:32)
leaf02            bond2                     bond             up         default         Slave: swp2 (LLDP: server02:mac:44: Mon Jan 11 05:56:31 2021
                                                                                        38:39:00:00:3a)
leaf02            peerlink                  bond             up         default         Slave: swp49 (LLDP: leaf01:swp49),  Mon Jan 11 05:56:31 2021
                                                                                        Slave: swp50 (LLDP: leaf01:swp50)
leaf02            bond3                     bond             up         default         Slave: swp3 (LLDP: server03:mac:44: Mon Jan 11 05:56:31 2021
                                                                                        38:39:00:00:3c)
leaf02            bond1                     bond             up         default         Slave: swp1 (LLDP: server01:mac:44: Mon Jan 11 05:56:31 2021
                                                                                        38:39:00:00:38)
leaf03            bond2                     bond             up         default         Slave: swp2 (LLDP: server05:mac:44: Mon Jan 11 05:56:37 2021
                                                                                        38:39:00:00:40)
leaf03            peerlink                  bond             up         default         Slave: swp49 (LLDP: leaf04:swp49),  Mon Jan 11 05:56:37 2021
                                                                                        Slave: swp50 (LLDP: leaf04:swp50)
leaf03            bond3                     bond             up         default         Slave: swp3 (LLDP: server06:mac:44: Mon Jan 11 05:56:37 2021
                                                                                        38:39:00:00:42)
leaf03            bond1                     bond             up         default         Slave: swp1 (LLDP: server04:mac:44: Mon Jan 11 05:56:37 2021
                                                                                        38:39:00:00:3e)
leaf04            bond2                     bond             up         default         Slave: swp2 (LLDP: server05:mac:44: Mon Jan 11 05:56:43 2021
                                                                                        38:39:00:00:46)
leaf04            peerlink                  bond             up         default         Slave: swp49 (LLDP: leaf03:swp49),  Mon Jan 11 05:56:43 2021
                                                                                        Slave: swp50 (LLDP: leaf03:swp50)
leaf04            bond3                     bond             up         default         Slave: swp3 (LLDP: server06:mac:44: Mon Jan 11 05:56:43 2021
                                                                                        38:39:00:00:48)
leaf04            bond1                     bond             up         default         Slave: swp1 (LLDP: server04:mac:44: Mon Jan 11 05:56:43 2021
                                                                                        38:39:00:00:44)
server01          uplink                    bond             up         default         Slave: eth2 (LLDP: leaf02:swp1),    Mon Jan 11 05:35:22 2021
                                                                                        Slave: eth1 (LLDP: leaf01:swp1)
server02          uplink                    bond             up         default         Slave: eth2 (LLDP: leaf02:swp2),    Mon Jan 11 05:34:52 2021
                                                                                        Slave: eth1 (LLDP: leaf01:swp2)
server03          uplink                    bond             up         default         Slave: eth2 (LLDP: leaf02:swp3),    Mon Jan 11 05:34:47 2021
                                                                                        Slave: eth1 (LLDP: leaf01:swp3)
server04          uplink                    bond             up         default         Slave: eth2 (LLDP: leaf04:swp1),    Mon Jan 11 05:34:52 2021
                                                                                        Slave: eth1 (LLDP: leaf03:swp1)
server05          uplink                    bond             up         default         Slave: eth2 (LLDP: leaf04:swp2),    Mon Jan 11 05:34:41 2021
                                                                                        Slave: eth1 (LLDP: leaf03:swp2)
server06          uplink                    bond             up         default         Slave: eth2 (LLDP: leaf04:swp3),    Mon Jan 11 05:35:03 2021
                                                                                        Slave: eth1 (LLDP: leaf03:swp3)
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

## View Aliases for Interfaces

You can see which interfaces have been configured with aliases.

```
cumulus@switch:~$ netq show interfaces alias swp2

Matching link records:
Hostname          Interface                 Alias                          State   Last Changed
----------------- ------------------------- ------------------------------ ------- -------------------------
border01          swp2                                                     down    Mon Jan 11 05:56:35 2021
border02          swp2                                                     down    Mon Jan 11 05:56:38 2021
fw1               swp2                                                     up      Mon Jan 11 05:56:36 2021
fw2               swp2                      rocket                         down    Mon Jan 11 05:56:34 2021
leaf01            swp2                                                     up      Mon Jan 11 23:16:42 2021
leaf02            swp2                      turtle                         up      Mon Jan 11 05:56:30 2021
leaf03            swp2                                                     up      Mon Jan 11 05:56:37 2021
leaf04            swp2                                                     up      Mon Jan 11 05:56:43 2021
spine01           swp2                                                     up      Mon Jan 11 05:56:54 2021
spine02           swp2                                                     up      Mon Jan 11 05:56:35 2021
spine03           swp2                                                     up      Mon Jan 11 05:56:35 2021
spine04           swp2                                                     up      Mon Jan 11 05:56:35 2021
```

If you do not specify a switch port or host, all configured aliases are displayed.

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
