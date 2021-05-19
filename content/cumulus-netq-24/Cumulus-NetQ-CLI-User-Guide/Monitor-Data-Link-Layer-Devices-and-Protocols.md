---
title: Monitor Data Link Layer Devices and Protocols
author: Cumulus Networks
weight: 540
toc: 3
---
With NetQ, a network administrator can monitor OSI Layer 2 devices and
protocols, including switches, bridges, link control, and physical media
access. Keeping track of the various data link layer devices in your
network ensures consistent and error-free communications between
devices. NetQ provides the ability to:

  - Monitor and validate device and protocol configurations
  - View available communication paths between devices

It helps answer questions such as:

  - Is a VLAN misconfigured?
  - Is there an MTU mismatch in my network?
  - Is MLAG configured correctly?
  - Is there an STP loop?
  - Can device A reach device B using MAC addresses?

## Monitor LLDP Operation

LLDP is used by network devices for
advertising their identity, capabilities, and neighbors on a LAN. You
can view this information for one or more devices. You can also view the
information at an earlier point in time or view changes that have
occurred to the information during a specified timeframe. NetQ enables
you to view LLDP information for your devices using the `netq show lldp`
command. The syntax for this command is:

    netq [<hostname>] show lldp [<remote-physical-interface>] [around <text-time>] [json]
    netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type lldp [between <text-time> and <text-endtime>] [json]

### View LLDP Information for All Devices

This example shows the interface and peer information that is advertised for each device.

    cumulus@switch:~$ netq show lldp 
     
    Matching lldp records:
    Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ----------------- ------------------------- -------------------------
    exit01            swp1                      edge01            swp5                      Thu Feb  7 18:31:53 2019
    exit01            swp2                      edge02            swp5                      Thu Feb  7 18:31:53 2019
    exit01            swp3                      spine01           swp9                      Thu Feb  7 18:31:53 2019
    exit01            swp4                      spine02           swp9                      Thu Feb  7 18:31:53 2019
    exit01            swp5                      spine03           swp9                      Thu Feb  7 18:31:53 2019
    exit01            swp6                      firewall01        mac:00:02:00:00:00:11     Thu Feb  7 18:31:53 2019
    exit01            swp7                      firewall02        swp3                      Thu Feb  7 18:31:53 2019
    exit02            swp1                      edge01            swp6                      Thu Feb  7 18:31:49 2019
    exit02            swp2                      edge02            swp6                      Thu Feb  7 18:31:49 2019
    exit02            swp3                      spine01           swp10                     Thu Feb  7 18:31:49 2019
    exit02            swp4                      spine02           swp10                     Thu Feb  7 18:31:49 2019
    exit02            swp5                      spine03           swp10                     Thu Feb  7 18:31:49 2019
    exit02            swp6                      firewall01        mac:00:02:00:00:00:12     Thu Feb  7 18:31:49 2019
    exit02            swp7                      firewall02        swp4                      Thu Feb  7 18:31:49 2019
    firewall01        swp1                      edge01            swp14                     Thu Feb  7 18:31:26 2019
    firewall01        swp2                      edge02            swp14                     Thu Feb  7 18:31:26 2019
    firewall01        swp3                      exit01            swp6                      Thu Feb  7 18:31:26 2019
    firewall01        swp4                      exit02            swp6                      Thu Feb  7 18:31:26 2019
    firewall02        swp1                      edge01            swp15                     Thu Feb  7 18:31:31 2019
    firewall02        swp2                      edge02            swp15                     Thu Feb  7 18:31:31 2019
    firewall02        swp3                      exit01            swp7                      Thu Feb  7 18:31:31 2019
    firewall02        swp4                      exit02            swp7                      Thu Feb  7 18:31:31 2019
    server11          swp1                      leaf01            swp7                      Thu Feb  7 18:31:43 2019
    server11          swp2                      leaf02            swp7                      Thu Feb  7 18:31:43 2019
    server11          swp3                      edge01            swp16                     Thu Feb  7 18:31:43 2019
    server11          swp4                      edge02            swp16                     Thu Feb  7 18:31:43 2019
    server12          swp1                      leaf01            swp8                      Thu Feb  7 18:31:47 2019
    server12          swp2                      leaf02            swp8                      Thu Feb  7 18:31:47 2019

## Monitor Interface Health

Interface (link) health can be monitored using the `netq show
interfaces` command. You can view status of the links, whether they are
operating over a VRF interface, the MTU of the link, and so forth. Using
the `hostname` option enables you to view only the interfaces for a
given device. View changes to interfaces using the `netq show events`
command.

The syntax for these commands is:

    netq [<hostname>] show interfaces [type bond|type bridge|type eth|type loopback|type macvlan|type swp|type vlan|type vrf|type vxlan] [state <remote-interface-state>] [around <text-time>] [json]
    netq <hostname> show interfaces [type bond|type bridge|type eth|type loopback|type macvlan|type swp|type vlan|type vrf|type vxlan] [state <remote-interface-state>] [around <text-time>] [count] [json]
    netq [<hostname>] show events [level info | level error | level warning | level critical | level debug] type interfaces [between <text-time> and <text-endtime>] [json]

### View Status for All Interfaces

Viewing the status of all interfaces at once can be helpful when you are
trying to compare configuration or status of a set of links, or
generally when changes have been made.

This example shows all interfaces network-wide.

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

### View Interface Status for a Given Device

If you are interested in only a the interfaces on a specific device, you
can view only those.

This example shows all interfaces on the *spine01* device.

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

### View All Interfaces of a Given Type

It can be can be useful to see the status of a particular type of
interface.

This example shows all bond interfaces that are down, and then those
that are up.

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

### View the Total Number of Interfaces

For a quick view of the amount of interfaces currently operating on a
device, use the `hostname` and `count` options together.

This example shows the count of interfaces on the *leaf03* switch.

    cumulus@switch:~$ netq leaf03 show interfaces count
    Count of matching link records: 28

### View the Total Number of a Given Interface Type

It can be useful to see how many interfaces of a particular type you
have on a device.

This example shows the count of swp interfaces are on the *leaf03*
switch.

    cumulus@switch:~$ netq leaf03 show interfaces type swp count
    Count of matching link records: 11

### View Changes to Interfaces

If you suspect that an interface is not working as expected, seeing a
drop in performance or a large number of dropped messages for example,
you can view changes that have been made to interfaces network-wide.

This example shows info level events for all interfaces in your network:

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

## Check for MTU Inconsistencies

The maximum transmission unit (MTU) determines the largest size packet
or frame that can be transmitted across a given communication link. When
the MTU is not configured to the same value on both ends of the link,
communication problems can occur. With NetQ, you can verify that the MTU
is correctly specified for each link using the netq check mtu command.

This example shows that four switches have inconsistently specified link
MTUs. Now the network administrator or operator can reconfigure the
switches and eliminate the communication issues associated with this
misconfiguration.

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

## Monitor VLAN Configurations

A VLAN (Virtual Local Area
Network) enables devices on one or more LANs to communicate as if they
were on the same network, without being physically connected. The VLAN
enables network administrators to
partition a network for functional or security requirements without
changing physical infrastructure. With NetQ, you can view the operation
of VLANs for one or all devices. You can also view the information at an
earlier point in time or view changes that have occurred to the
information during a specified timeframe. NetQ enables you to view basic
VLAN information for your devices using the `netq show vlan` command.
Additional show commands enable you to view VLAN information associated
with interfaces and MAC addresses. The syntax for these commands is:

    netq [<hostname>] show interfaces [type vlan] [state <remote-interface-state>] [around <text-time>] [json]
    netq <hostname> show interfaces [type vlan] [state <remote-interface-state>] [around <text-time>] [count] [json]
    netq [<hostname>] show events [level info | level error | level warning | level critical | level debug] type vlan [between <text-time> and <text-endtime>] [json]
    netq show macs [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
    netq <hostname> show macs [<mac>] [vlan <1-4096>] [origin | count] [around <text-time>] [json]
    netq <hostname> show macs egress-port <egress-port> [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
    netq [<hostname>] show vlan [<1-4096>] [around <text-time>] [json]

{{%notice note%}}
When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: week(s)
- **d**: day(s)
- **h**: hour(s)
- **m**: minute(s)
- **s**: second(s)
- **now**

For the `between` option, the start (`<text-time>`) and end time (`text-endtime>`) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{%/notice%}}

### View VLAN Information for All Devices

This example shows the VLANs configured across your network.

    cumulus@switch:~$ netq show vlan
    Matching vlan records:
    Hostname          VLANs                     SVIs                      Last Changed
    ----------------- ------------------------- ------------------------- -------------------------
    exit01            4001                      4001                      Thu Feb  7 18:31:38 2019
    exit02            4001                      4001                      Thu Feb  7 18:31:38 2019
    leaf01            1,13,24,4001              13 24 4001                Thu Feb  7 18:31:38 2019
    leaf02            1,13,24,4001              13 24 4001                Thu Feb  7 18:31:38 2019
    leaf03            1,13,24,4001              13 24 4001                Thu Feb  7 18:31:38 2019
    leaf04            1,13,24,4001              13 24 4001                Thu Feb  7 18:31:38 2019

### View VLAN Interface Information

You can view the current or past state of the interfaces associated with
VLANs using the `netq show interfaces` command. This provides the status
of the interface, its specified MTU, whether it is running over a VRF,
and the last time it was changed.

    cumulus@switch:~$ netq show interfaces type vlan 
    Matching link records:
    Hostname          Interface                 Type             State      VRF             Details                             Last Changed
    ----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
    exit01            vlan4001                  vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    exit02            vlan4001                  vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf01            peerlink.4094             vlan             up         default         MTU:9000                            Fri Feb  8 00:24:28 2019
    leaf01            vlan13                    vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf01            vlan24                    vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf01            vlan4001                  vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf02            peerlink.4094             vlan             up         default         MTU:9000                            Fri Feb  8 00:24:28 2019
    leaf02            vlan13                    vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf02            vlan24                    vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf02            vlan4001                  vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf03            peerlink.4094             vlan             up         default         MTU:9000                            Fri Feb  8 00:24:28 2019
    leaf03            vlan13                    vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf03            vlan24                    vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf03            vlan4001                  vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf04            peerlink.4094             vlan             up         default         MTU:9000                            Fri Feb  8 00:24:28 2019
    leaf04            vlan13                    vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf04            vlan24                    vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019
    leaf04            vlan4001                  vlan             up         vrf1            MTU:1500                            Fri Feb  8 00:24:28 2019

### View MAC Addresses Associated with a VLAN

You can determine the MAC addresses associated with a given VLAN using
the `netq show macs vlan` command. The command also provides the
hostnames of the devices, the egress port for the interface, whether the
MAC address originated from the given device, whether it learns the MAC
address from the peer (remote=yes), and the last time the configuration
was changed.

This example shows the MAC addresses associated with *VLAN13*.

    cumulus@switch:~$ netq show macs vlan 13 
    Matching mac records:
    Origin MAC Address        VLAN   Hostname          Egress Port          Remote Last Changed
    ------ ------------------ ------ ----------------- -------------------- ------ -------------------------
    no     00:03:00:11:11:01  13     leaf01            bond01:server01      no     Fri Feb  8 00:24:28 2019
    no     00:03:00:11:11:01  13     leaf02            bond01:server01      no     Fri Feb  8 00:24:28 2019
    no     00:03:00:11:11:01  13     leaf03            vni13:leaf01         yes    Fri Feb  8 00:24:28 2019
    no     00:03:00:11:11:01  13     leaf04            vni13:leaf01         yes    Fri Feb  8 00:24:28 2019
    no     00:03:00:33:33:01  13     leaf01            vni13:10.0.0.134     yes    Fri Feb  8 00:24:28 2019
    no     00:03:00:33:33:01  13     leaf02            vni13:10.0.0.134     yes    Fri Feb  8 00:24:28 2019
    no     00:03:00:33:33:01  13     leaf03            bond03:server03      no     Fri Feb  8 00:24:28 2019
    no     00:03:00:33:33:01  13     leaf04            bond03:server03      no     Fri Feb  8 00:24:28 2019
    no     02:03:00:11:11:01  13     leaf01            bond01:server01      no     Fri Feb  8 00:24:28 2019
    no     02:03:00:11:11:01  13     leaf02            bond01:server01      no     Fri Feb  8 00:24:28 2019
    no     02:03:00:11:11:01  13     leaf03            vni13:leaf01         yes    Fri Feb  8 00:24:28 2019
    no     02:03:00:11:11:01  13     leaf04            vni13:leaf01         yes    Fri Feb  8 00:24:28 2019
    no     02:03:00:11:11:02  13     leaf01            bond01:server01      no     Fri Feb  8 00:24:28 2019
    no     02:03:00:11:11:02  13     leaf02            bond01:server01      no     Fri Feb  8 00:24:28 2019
    no     02:03:00:11:11:02  13     leaf03            vni13:leaf01         yes    Fri Feb  8 00:24:28 2019
    no     02:03:00:11:11:02  13     leaf04            vni13:leaf01         yes    Fri Feb  8 00:24:28 2019
    no     02:03:00:33:33:01  13     leaf01            vni13:10.0.0.134     yes    Fri Feb  8 00:24:28 2019
    no     02:03:00:33:33:01  13     leaf02            vni13:10.0.0.134     yes    Fri Feb  8 00:24:28 2019
    no     02:03:00:33:33:01  13     leaf03            bond03:server03      no     Fri Feb  8 00:24:28 2019
    no     02:03:00:33:33:01  13     leaf04            bond03:server03      no     Fri Feb  8 00:24:28 2019
    no     02:03:00:33:33:02  13     leaf01            vni13:10.0.0.134     yes    Fri Feb  8 00:24:28 2019
    no     02:03:00:33:33:02  13     leaf02            vni13:10.0.0.134     yes    Fri Feb  8 00:24:28 2019
    no     02:03:00:33:33:02  13     leaf03            bond03:server03      no     Fri Feb  8 00:24:28 2019
    no     02:03:00:33:33:02  13     leaf04            bond03:server03      no     Fri Feb  8 00:24:28 2019
    yes    44:38:39:00:00:03  13     leaf01            bridge               no     Fri Feb  8 00:24:28 2019
    yes    44:38:39:00:00:15  13     leaf02            bridge               no     Fri Feb  8 00:24:28 2019
    yes    44:38:39:00:00:23  13     leaf03            bridge               no     Fri Feb  8 00:24:28 2019
    yes    44:38:39:00:00:5c  13     leaf04            bridge               no     Fri Feb  8 00:24:28 2019
    yes    44:39:39:ff:00:13  13     leaf01            bridge               no     Fri Feb  8 00:24:28 2019
    yes    44:39:39:ff:00:13  13     leaf02            bridge               no     Fri Feb  8 00:24:28 2019
    yes    44:39:39:ff:00:13  13     leaf03            bridge               no     Fri Feb  8 00:24:28 2019
    yes    44:39:39:ff:00:13  13     leaf04            bridge               no     Fri Feb  8 00:24:28 2019

### View MAC Addresses Associated with an Egress Port

You can filter that information down to just the MAC addresses that are
associated with a given VLAN that use a particular egress port. This
example shows MAC addresses associated with the *leaf03* switch and
*VLAN 13* that use the *bridge* port.

    cumulus@switch:~$ netq leaf03 show macs egress-port bridge vlan 13
    Matching mac records:
    Origin MAC Address        VLAN   Hostname          Egress Port          Remote Last Changed
    ------ ------------------ ------ ----------------- -------------------- ------ -------------------------
    yes    44:38:39:00:00:23  13     leaf03            bridge               no     Fri Feb  8 00:24:28 2019
    yes    44:39:39:ff:00:13  13     leaf03            bridge               no     Fri Feb  8 00:24:28 2019

### View the MAC Addresses Associated with VRR Configurations

You can view all of the MAC addresses associated with your VRR (virtual
router reflector) interface configuration using the `netq show
interfaces type macvlan` command. This is useful for determining if the
specified MAC address inside a VLAN is the same or different across your
VRR configuration.

    cumulus@switch:~$ netq show interfaces type macvlan
    Matching link records:
    Hostname          Interface                 Type             State      VRF             Details                             Last Changed
    ----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
    leaf01            vlan13-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:13,             Fri Feb  8 00:28:09 2019
                                                                                            Mode: Private
    leaf01            vlan24-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:24,             Fri Feb  8 00:28:09 2019
                                                                                            Mode: Private
    leaf02            vlan13-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:13,             Fri Feb  8 00:28:09 2019
                                                                                            Mode: Private
    leaf02            vlan24-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:24,             Fri Feb  8 00:28:09 2019
                                                                                            Mode: Private
    leaf03            vlan13-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:13,             Fri Feb  8 00:28:09 2019
                                                                                            Mode: Private
    leaf03            vlan24-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:24,             Fri Feb  8 00:28:09 2019
                                                                                            Mode: Private
    leaf04            vlan13-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:13,             Fri Feb  8 00:28:09 2019
                                                                                            Mode: Private
    leaf04            vlan24-v0                 macvlan          up         vrf1            MAC: 44:39:39:ff:00:24,             Fri Feb  8 00:28:09 2019
                                                                                            Mode: Private

## View the History of a MAC Address

It is useful when debugging to be able to see when a MAC address is learned, when and where it moved in the network after that, if there was a duplicate at any time, and so forth. The `netq show mac-history` command makes this information available. It enables you to see:

- each change that was made chronologically
- changes made between two points in time, using the `between` option
- only the difference between to points in time using the `diff` option
- to order the output by selected output fields using the `listby` option
- each change that was made for the MAC address on a particular VLAN, using the `vlan` option

And as with many NetQ commands, the default time range used is now to one hour ago. You can view the output in JSON format as well.

The syntax of the command is:

```
netq [<hostname>] show mac-history <mac> [vlan <1-4096>] [diff] [between <text-time> and <text-endtime>] [listby <text-list-by>] [json]
```

{{%notice note%}}
When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: week(s)
- **d**: day(s)
- **h**: hour(s)
- **m**: minute(s)
- **s**: second(s)
- **now**

For the `between` option, the start (`<text-time>`) and end time (`text-endtime>`) values can be entered as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{%/notice%}}

This example shows how to view a full chronology of changes for a MAC Address. The caret (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 00:03:00:11:11:77 vlan 13

Matching mac-history records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Mon Nov  4 20:21:13 2019  leaf01            13     no     bond01                                  no     no
Mon Nov  4 20:21:13 2019  leaf02            13     no     bond01                                  no     no
Mon Nov  4 20:21:13 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:21:13 2019  leaf03            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf03            ^      ^      bond03                                  no     ^
Mon Nov  4 20:22:40 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf02            13     no     vni13            10.0.0.134             yes    no
Mon Nov  4 20:22:40 2019  leaf01            13     no     vni13            10.0.0.134             yes    no
```

This example shows how to view the history of a MAC address by hostname. The caret (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 00:03:00:11:11:77 vlan 13 listby hostname

Matching mac-history records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Mon Nov  4 20:21:13 2019  leaf03            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf03            ^      ^      bond03                                  no     ^
Mon Nov  4 20:21:13 2019  leaf02            13     no     bond01                                  no     no
Mon Nov  4 20:22:40 2019  leaf02            ^      ^      vni13            10.0.0.134             yes    ^
Mon Nov  4 20:21:13 2019  leaf01            13     no     bond01                                  no     no
Mon Nov  4 20:22:40 2019  leaf01            ^      ^      vni13            10.0.0.134             yes    ^
Mon Nov  4 20:21:13 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf04            ^      ^      bond03                                  no     ^
```

This example shows show to view the history of a MAC address between now and two hours ago. The caret (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 00:03:00:11:11:77 vlan 13 between now and 2h

Matching mac-history records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Mon Nov  4 20:21:13 2019  leaf01            13     no     bond01                                  no     no
Mon Nov  4 20:21:13 2019  leaf02            13     no     bond01                                  no     no
Mon Nov  4 20:21:13 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:21:13 2019  leaf03            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf03            ^      ^      bond03                                  no     ^
Mon Nov  4 20:22:40 2019  leaf04            13     no     vni13            10.0.0.112             yes    no
Mon Nov  4 20:22:40 2019  leaf02            13     no     vni13            10.0.0.134             yes    no
Mon Nov  4 20:22:40 2019  leaf01            13     no     vni13            10.0.0.134             yes    no
```

## Monitor MLAG Configurations

Multi-Chassis Link Aggregation (MLAG) is used to enable a server or
switch with a two-port bond (such as a link aggregation group/LAG,
EtherChannel, port group or trunk) to connect those ports to different
switches and operate as if they are connected to a single, logical
switch. This provides greater redundancy and greater system throughput.
Dual-connected devices can create LACP bonds that contain links to each
physical switch. Therefore, active-active links from the dual-connected
devices are supported even though they are connected to two different
physical switches.

{{%notice tip%}}

**MLAG or CLAG?**
The Cumulus Linux implementation of MLAG is referred to by other vendors
as CLAG, MC-LAG or VPC. You will even see references to CLAG in Cumulus
Linux and Cumulus NetQ, including the management daemon, named `clagd`, and other options
in the code, such as `clag-id`, which exist for historical purposes. The
Cumulus Linux implementation is truly a multi-chassis link aggregation
protocol, so we call it MLAG.

{{%/notice%}}

For instructions on configuring MLAG, refer to the [MLAG]({{<ref "/cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}}) topic in the Cumulus Linux User Guide.

With NetQ, you can view the configuration and operation of devices using
MLAG using the `netq show clag` command. You can view the current
configuration and the configuration at a prior point in time, as well as
view any changes that have been made within a timeframe. The syntax for
the show command is:

    netq [<hostname>] show clag [around <text-time>] [json]
    netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type clag [between <text-time> and <text-endtime>] [json]

### View MLAG Configuration and Status for all Devices

This example shows the configuration and status of MLAG for all devices.
In this case, three MLAG pairs are seen between leaf11 and leaf12 (which
happens to be down), edge01(P) and edge02, and leaf21(P) and leaf22.

    cumulus@switch:~$ netq show clag
    Matching clag records:
    Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                              s
    ----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
    leaf11                              44:38:39:ff:ff:01  down       n/a    0     0     Thu Feb  7 18:30:49 2019
    leaf12                              44:38:39:ff:ff:01  down       down   8     0     Thu Feb  7 18:30:53 2019
    edge01(P)         edge02            00:01:01:10:00:01  up         up     25    25    Thu Feb  7 18:31:02 2019
    edge02            edge01(P)         00:01:01:10:00:01  up         up     25    25    Thu Feb  7 18:31:15 2019
    leaf21(P)         leaf22            44:38:39:ff:ff:02  up         up     8     8     Thu Feb  7 18:31:20 2019
    leaf22            leaf21(P)         44:38:39:ff:ff:02  up         up     8     8     Thu Feb  7 18:31:30 2019

You can go back in time to see when this first MLAG pair went down.
These results indicate that the pair became disconnected some time in
the last five minutes.

    cumulus@switch:~$ netq show clag around 5m
    Matching clag records:
    Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                             s
    ----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
    edge01(P)         edge02            00:01:01:10:00:01  up         up     25    25    Thu Feb  7 18:31:30 2019
    edge02            edge01(P)         00:01:01:10:00:01  up         up     25    25    Thu Feb  7 18:31:30 2019
    leaf11(P)         leaf12            44:38:39:ff:ff:01  up         up     8     8     Thu Feb  7 18:31:30 2019
    leaf12            leaf11(P)         44:38:39:ff:ff:01  up         up     8     8     Thu Feb  7 18:31:30 2019
    leaf21(P)         leaf22            44:38:39:ff:ff:02  up         up     8     8     Thu Feb  7 18:31:30 2019
    leaf22            leaf21(P)         44:38:39:ff:ff:02  up         up     8     8     Thu Feb  7 18:31:30 2019

### View MLAG Configuration and Status for Given Devices

This example shows that leaf22 is up and MLAG properly configured with a
peer connection to leaf21 through 8 bonds, all of which are dual bonded.

    cumulus@switch:~$ netq leaf22 show clag
    Matching CLAG session records are:
    Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                              s
    ----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
    leaf22            leaf21(P)         44:38:39:ff:ff:02  up         up     8     8     Thu Feb  7 18:31:30 2019

When you're directly on the switch, you can run `clagctl` to get the
state:

    cumulus@switch:~$ sudo clagctl
     
    The peer is alive
    Peer Priority, ID, and Role: 4096 00:02:00:00:00:4e primary
    Our Priority, ID, and Role: 8192 44:38:39:00:a5:38 secondary
    Peer Interface and IP: peerlink-3.4094 169.254.0.9
    VxLAN Anycast IP: 36.0.0.20
    Backup IP: 27.0.0.20 (active)
    System MAC: 44:38:39:ff:ff:01
     
    CLAG Interfaces
    Our Interface    Peer Interface   CLAG Id Conflicts            Proto-Down Reason
    ---------------- ---------------- ------- -------------------- -----------------
    vx-38            vx-38            -       -                    -
    vx-33            vx-33            -       -                    -
    hostbond4        hostbond4        1       -                    -
    hostbond5        hostbond5        2       -                    -
    vx-37            vx-37            -       -                    -
    vx-36            vx-36            -       -                    -
    vx-35            vx-35            -       -                    -
    vx-34            vx-34            -       -                    -

## Monitor Time Synchronization Status for Devices

It is important that the switches and hosts remain in time
synchronization with the NetQ Platform to ensure collected data is
properly captured and processed. You can use the `netq show ntp` command
to view the time synchronization status for all devices or filter for
devices that are either in synchronization or out of synchronization,
currently or at a time in the past. The syntax for the show command is:

    netq [<hostname>] show ntp [out-of-sync|in-sync] [around <text-time>] [json]
    netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type ntp [between <text-time> and <text-endtime>] [json]

This example shows the time synchronization status for all devices in
the network.

    cumulus@switch:~$ netq show ntp
     
    Matching ntp records:
    Hostname          NTP Sync Current Server    Stratum NTP App
    ----------------- -------- ----------------- ------- ---------------------
    edge01            yes      services01.it.c   3       ntpq
    exit01            yes      time.tritn.com    2       ntpq
    exit02            yes      time.tritn.com    2       ntpq
    internet          no       -                 16      ntpq
    leaf01            yes      services01.it.c   2       ntpq
    leaf02            yes      services01.it.c   2       ntpq
    leaf03            yes      107.181.191.189   2       ntpq
    leaf04            yes      grom.polpo.org    2       ntpq
    oob-mgmt-server   yes      linode227395.st   2       ntpq
    server01          yes      192.168.0.254     3       ntpq
    server02          yes      192.168.0.254     3       ntpq
    server03          yes      192.168.0.254     3       ntpq
    server04          yes      192.168.0.254     3       ntpq
    spine01           yes      107.181.191.189   2       ntpq
    spine02           yes      t2.time.bf1.yah   2       ntpq

This example shows all devices in the network that are out of time
synchronization, and consequently might need to be investigated.

    cumulus@switch:~$ netq show ntp out-of-sync
     
    Matching ntp records:
    Hostname          NTP Sync Current Server    Stratum NTP App
    ----------------- -------- ----------------- ------- ---------------------
    internet          no       -                 16      ntpq

This example shows the time synchronization status for *leaf01*.

    cumulus@switch:~$ netq leaf01 show ntp
     
    Matching ntp records:
    Hostname          NTP Sync Current Server    Stratum NTP App
    ----------------- -------- ----------------- ------- ---------------------
    leaf01            yes      kilimanjaro       2       ntpq

## Monitor Spanning Tree Protocol Configuration

The Spanning Tree Protocol (STP) is used
in Ethernet-based networks to prevent communication loops when you have
redundant paths on a bridge or switch. Loops cause excessive broadcast
messages greatly impacting the network performance. With NetQ, you can
view the STP topology on a bridge or switch to ensure no loops have been
created using the `netq show stp topology` command. You can also view
the topology information for a prior point in time to see if any changes
were made around then. The syntax for the show command is:

    netq <hostname> show stp topology [around <text-time>] [json]

This example shows the STP topology as viewed from the *spine1* switch.

    cumulus@switch:~$ netq spine1 show stp topology
    Root(spine1) -- spine1:sw_clag200 -- leaf2:EdgeIntf(sng_hst2) -- hsleaf21
                                      -- leaf2:EdgeIntf(dual_host2) -- hdleaf2
                                      -- leaf2:EdgeIntf(dual_host1) -- hdleaf1
                                      -- leaf2:ClagIsl(peer-bond1) -- leaf1
                                      -- leaf1:EdgeIntf(sng_hst2) -- hsleaf11
                                      -- leaf1:EdgeIntf(dual_host2) -- hdleaf2
                                      -- leaf1:EdgeIntf(dual_host1) -- hdleaf1
                                      -- leaf1:ClagIsl(peer-bond1) -- leaf2
                 -- spine1:ClagIsl(peer-bond1) -- spine2
                 -- spine1:sw_clag300 -- edge1:EdgeIntf(sng_hst2) -- hsedge11
                                      -- edge1:EdgeIntf(dual_host2) -- hdedge2
                                      -- edge1:EdgeIntf(dual_host1) -- hdedge1
                                      -- edge1:ClagIsl(peer-bond1) -- edge2
                                      -- edge2:EdgeIntf(sng_hst2) -- hsedge21
                                      -- edge2:EdgeIntf(dual_host2) -- hdedge2
                                      -- edge2:EdgeIntf(dual_host1) -- hdedge1
                                      -- edge2:ClagIsl(peer-bond1) -- edge1
    Root(spine2) -- spine2:sw_clag200 -- leaf2:EdgeIntf(sng_hst2) -- hsleaf21
                                      -- leaf2:EdgeIntf(dual_host2) -- hdleaf2
                                      -- leaf2:EdgeIntf(dual_host1) -- hdleaf1
                                      -- leaf2:ClagIsl(peer-bond1) -- leaf1
                                      -- leaf1:EdgeIntf(sng_hst2) -- hsleaf11
                                      -- leaf1:EdgeIntf(dual_host2) -- hdleaf2
                                      -- leaf1:EdgeIntf(dual_host1) -- hdleaf1
                                      -- leaf1:ClagIsl(peer-bond1) -- leaf2
                 -- spine2:ClagIsl(peer-bond1) -- spine1
                 -- spine2:sw_clag300 -- edge2:EdgeIntf(sng_hst2) -- hsedge21
                                      -- edge2:EdgeIntf(dual_host2) -- hdedge2
                                      -- edge2:EdgeIntf(dual_host1) -- hdedge1
                                      -- edge2:ClagIsl(peer-bond1) -- edge1
                                      -- edge1:EdgeIntf(sng_hst2) -- hsedge11
                                      -- edge1:EdgeIntf(dual_host2) -- hdedge2
                                      -- edge1:EdgeIntf(dual_host1) -- hdedge1
                                      -- edge1:ClagIsl(peer-bond1) -- edge2

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
