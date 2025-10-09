---
title: VLAN
author: NVIDIA
weight: 910
toc: 3
---
A VLAN (Virtual Local Area Network) enables devices on one or more LANs to communicate as if they were on the same network, without being physically connected. The VLAN enables network administrators to partition a network for functional or security requirements without changing physical infrastructure. For an overview and how to configure VLANs in your network, refer to [Ethernet Bridging - VLANs]({{<ref "cumulus-linux-43/Layer-2/Ethernet-Bridging-VLANs">}}).

With the NetQ CLI, you can view the operation of VLANs for one or all devices. You can also view the information at an earlier point in time or view changes that have occurred to the information during a specified timeframe. NetQ enables you to view basic VLAN information for your devices using the `netq show vlan` command. Additional show commands provide information about VLAN interfaces, MAC addresses associated with VLANs, and events.

The syntax for these commands is:

```
netq [<hostname>] show vlan [<1-4096>] [around <text-time>] [json]

netq show interfaces type vlan [state <remote-interface-state>] [around <text-time>] [json]
netq <hostname> show interfaces type vlan [state <remote-interface-state>] [around <text-time>] [count] [json]

netq show macs [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]
netq <hostname> show macs [<mac>] [vlan <1-4096>] [origin | count] [around <text-time>] [json]
netq <hostname> show macs egress-port <egress-port> [<mac>] [vlan <1-4096>] [origin] [around <text-time>] [json]

netq [<hostname>] show events [level info | level error | level warning | level debug] type vlan [between <text-time> and <text-endtime>] [json]
```

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

When using the `between` option, you can enter the start time (`text-time`) and end time (`text-endtime`) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.

{{%/notice%}}

## View VLAN Information for All Devices

You can view the configuration information for all VLANs in your network by running the `netq show vlan` command. It lists VLANs by device, and indicates any switch virtual interfaces (SVIs) configured and the last time this configuration changed.

This example shows the VLANs configured across a network based on the NVIDIA reference architecture.

```
cumulus@switch:~$ netq show vlan
Matching vlan records:
Hostname          VLANs                     SVIs                      Last Changed
----------------- ------------------------- ------------------------- -------------------------
border01          1,10,20,30,4001-4002                                Wed Oct 28 14:46:33 2020
border02          1,10,20,30,4001-4002                                Wed Oct 28 14:46:33 2020
leaf01            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf02            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf03            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf04            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
```

## View All VLAN Information for a Given Device

You can view the configuration information for all VLANs running on a specific device using the `netq <hostname> show vlan` command. It lists VLANs running on the device, the ports used, whether an SVI is present, and the last time this configuration changed.

This example shows the VLANs configured on the *leaf02* switch.

```
cumulus@switch:~$ netq leaf02 show vlan
Matching vlan records:
Hostname          VLAN   Ports                               SVI  Last Changed
----------------- ------ ----------------------------------- ---- -------------------------
leaf02            20     bond2,vni20                         yes  Wed Oct 28 15:14:11 2020
leaf02            30     vni30,bond3                         yes  Wed Oct 28 15:14:11 2020
leaf02            1      peerlink                            no   Wed Oct 28 15:14:11 2020
leaf02            10     bond1,vni10                         yes  Wed Oct 28 15:14:11 2020
leaf02            4001   vniRED                              yes  Wed Oct 28 15:14:11 2020
leaf02            4002   vniBLUE                             yes  Wed Oct 28 15:14:11 2020
```

## View Information for a Given VLAN

You can view the configuration information for a particular VLAN using the `netq show vlan <vlan-id>` command. The ID must be a number between 1 and 4096.

This example shows that vlan *10* is running on the two border and four leaf switches.

```
cumulus@switch~$ netq show vlan 10
Matching vlan records:
Hostname          VLAN   Ports                               SVI  Last Changed
----------------- ------ ----------------------------------- ---- -------------------------
border01          10                                         no   Wed Oct 28 15:20:27 2020
border02          10                                         no   Wed Oct 28 15:20:28 2020
leaf01            10     bond1,vni10                         yes  Wed Oct 28 15:20:28 2020
leaf02            10     bond1,vni10                         yes  Wed Oct 28 15:20:28 2020
leaf03            10     bond1,vni10                         yes  Wed Oct 28 15:20:29 2020
leaf04            10     bond1,vni10                         yes  Wed Oct 28 15:20:29 2020
```

## View VLAN Information for a Time in the Past

You can view the VLAN configuration information across the network or for a given device at a time in the past using the `around` option of the `netq show vlan` command. This can be helpful when you think changes might have occurred.

<!-- vale off -->
This example shows the VLAN configuration in the last 24 hours and 30 days ago. Note that some SVIs have been removed.
<!-- vale on -->

```
cumulus@switch:~$ netq show vlan
Matching vlan records:
Hostname          VLANs                     SVIs                      Last Changed
----------------- ------------------------- ------------------------- -------------------------
border01          1,10,20,30,4001-4002                                Wed Oct 28 14:46:33 2020
border02          1,10,20,30,4001-4002                                Wed Oct 28 14:46:33 2020
leaf01            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf02            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf03            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020
leaf04            1,10,20,30,4001-4002      10 20 30                  Wed Oct 28 14:46:34 2020

cumulus@switch:~$ netq show vlan around 30d
Matching vlan records:
Hostname          VLANs                     SVIs                      Last Changed
----------------- ------------------------- ------------------------- -------------------------
border01          1,10,20,30,4001-4002      10 20 30 4001-4002        Wed Oct 28 15:25:43 2020
border02          1,10,20,30,4001-4002      10 20 30 4001-4002        Wed Oct 28 15:25:43 2020
leaf01            1,10,20,30,4001-4002      10 20 30 4001-4002        Wed Oct 28 15:25:43 2020
leaf02            1,10,20,30,4001-4002      10 20 30 4001-4002        Wed Oct 28 15:25:43 2020
leaf03            1,10,20,30,4001-4002      10 20 30 4001-4002        Wed Oct 28 15:25:43 2020
leaf04            1,10,20,30,4001-4002      10 20 30 4001-4002        Wed Oct 28 15:25:43 2020
```

This example shows the VLAN configuration on *leaf02* in the last 24 hours and one week ago. In this case, no changes are present.

```
cumulus@switch:~$ netq leaf02 show vlan
Matching vlan records:
Hostname          VLAN   Ports                               SVI  Last Changed
----------------- ------ ----------------------------------- ---- -------------------------
leaf02            20     bond2,vni20                         yes  Wed Oct 28 15:14:11 2020
leaf02            30     vni30,bond3                         yes  Wed Oct 28 15:14:11 2020
leaf02            1      peerlink                            no   Wed Oct 28 15:14:11 2020
leaf02            10     bond1,vni10                         yes  Wed Oct 28 15:14:11 2020
leaf02            4001   vniRED                              yes  Wed Oct 28 15:14:11 2020
leaf02            4002   vniBLUE                             yes  Wed Oct 28 15:14:11 2020

cumulus@switch:~$ netq leaf02 show vlan around 7d
Matching vlan records:
Hostname          VLAN   Ports                               SVI  Last Changed
----------------- ------ ----------------------------------- ---- -------------------------
leaf02            20     bond2,vni20                         yes  Wed Oct 28 15:36:39 2020
leaf02            30     vni30,bond3                         yes  Wed Oct 28 15:36:39 2020
leaf02            1      peerlink                            no   Wed Oct 28 15:36:39 2020
leaf02            10     bond1,vni10                         yes  Wed Oct 28 15:36:39 2020
leaf02            4001   vniRED                              yes  Wed Oct 28 15:36:39 2020
leaf02            4002   vniBLUE                             yes  Wed Oct 28 15:36:39 2020
```

## View VLAN Interface Information

You can view the current or past state of the interfaces associated with VLANs using the `netq show interfaces` command. This provides the status of the interface, its specified MTU, whether it is running over a VRF, and the last time it changed.

```
cumulus@switch:~$ netq show interfaces type vlan
Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
border01          vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:48 2020
border01          vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:48 2020
border01          peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:48 2020
border02          vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:51 2020
border02          vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:51 2020
border02          peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:51 2020
fw1               borderBond.20             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:25 2020
fw1               borderBond.10             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:25 2020
leaf01            vlan20                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            vlan30                    vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            vlan10                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf01            peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:42 2020
leaf02            vlan20                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            vlan30                    vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            vlan10                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf02            peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:51 2020
leaf03            vlan20                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            vlan30                    vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            vlan10                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf03            peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:28:23 2020
leaf04            vlan20                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            vlan4002                  vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            vlan4001                  vlan             up         RED             MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            vlan30                    vlan             up         BLUE            MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            vlan10                    vlan             up         RED             MTU: 9216                           Tue Oct 27 22:29:06 2020
leaf04            peerlink.4094             vlan             up         default         MTU: 9216                           Tue Oct 27 22:29:06 2020
```

## View the Number of VLAN Interfaces Configured

You can view the number of VLAN interfaces configured for a given device using the `netq show vlan` command with the `hostname` and `count` options.

This example shows the count of VLAN interfaces on the *leaf02* switch in the last 24 hours.

```
cumulus@switch:~$ netq leaf02 show interfaces type vlan count
Count of matching link records: 6
```

### View MAC Addresses Associated with a VLAN

You can determine the MAC addresses associated with a given VLAN using the `netq show macs vlan` command. The command also provides the hostnames of the devices, the egress port for the interface, whether the MAC address originated from the given device, whether it learns the MAC address from the peer (`remote=yes`), and the last time the configuration changed.

This example shows the MAC addresses associated with VLAN *10*.

```
cumulus@switch:~$ netq show macs vlan 10
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    00:00:00:00:00:1a  10     leaf04            bridge                         no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:37  10     leaf04            vni10                          no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:59  10     leaf04            vni10                          no     Tue Oct 27 22:29:07 2020
no     46:38:39:00:00:38  10     leaf04            vni10                          yes    Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:3e  10     leaf04            bond1                          no     Tue Oct 27 22:29:07 2020
no     46:38:39:00:00:3e  10     leaf04            bond1                          no     Tue Oct 27 22:29:07 2020
yes    44:38:39:00:00:5e  10     leaf04            bridge                         no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:32  10     leaf04            vni10                          yes    Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:5d  10     leaf04            peerlink                       no     Tue Oct 27 22:29:07 2020
no     46:38:39:00:00:44  10     leaf04            bond1                          no     Tue Oct 27 22:29:07 2020
no     46:38:39:00:00:32  10     leaf04            vni10                          yes    Tue Oct 27 22:29:07 2020
yes    36:ae:d2:23:1d:8c  10     leaf04            vni10                          no     Tue Oct 27 22:29:07 2020
yes    00:00:00:00:00:1a  10     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:59  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:37  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:38  10     leaf03            vni10                          yes    Tue Oct 27 22:28:24 2020
yes    36:99:0d:48:51:41  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:3e  10     leaf03            bond1                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:5e  10     leaf03            peerlink                       no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:3e  10     leaf03            bond1                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:32  10     leaf03            vni10                          yes    Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  10     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:44  10     leaf03            bond1                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:32  10     leaf03            vni10                          yes    Tue Oct 27 22:28:24 2020
yes    00:00:00:00:00:1a  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
no     44:38:39:00:00:59  10     leaf02            peerlink                       no     Tue Oct 27 22:28:51 2020
yes    44:38:39:00:00:37  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
no     46:38:39:00:00:38  10     leaf02            bond1                          no     Tue Oct 27 22:28:51 2020
no     44:38:39:00:00:3e  10     leaf02            vni10                          yes    Tue Oct 27 22:28:51 2020
no     46:38:39:00:00:3e  10     leaf02            vni10                          yes    Tue Oct 27 22:28:51 2020
no     44:38:39:00:00:5e  10     leaf02            vni10                          no     Tue Oct 27 22:28:51 2020
no     44:38:39:00:00:5d  10     leaf02            vni10                          no     Tue Oct 27 22:28:51 2020
no     44:38:39:00:00:32  10     leaf02            bond1                          no     Tue Oct 27 22:28:51 2020
no     46:38:39:00:00:44  10     leaf02            vni10                          yes    Tue Oct 27 22:28:51 2020
no     46:38:39:00:00:32  10     leaf02            bond1                          no     Tue Oct 27 22:28:51 2020
yes    4a:32:30:8c:13:08  10     leaf02            vni10                          no     Tue Oct 27 22:28:51 2020
yes    00:00:00:00:00:1a  10     leaf01            bridge                         no     Tue Oct 27 22:28:42 2020
no     44:38:39:00:00:37  10     leaf01            peerlink                       no     Tue Oct 27 22:28:42 2020
yes    44:38:39:00:00:59  10     leaf01            bridge                         no     Tue Oct 27 22:28:42 2020
no     46:38:39:00:00:38  10     leaf01            bond1                          no     Tue Oct 27 22:28:42 2020
no     44:38:39:00:00:3e  10     leaf01            vni10                          yes    Tue Oct 27 22:28:43 2020
no     46:38:39:00:00:3e  10     leaf01            vni10                          yes    Tue Oct 27 22:28:42 2020
no     44:38:39:00:00:5e  10     leaf01            vni10                          no     Tue Oct 27 22:28:42 2020
no     44:38:39:00:00:5d  10     leaf01            vni10                          no     Tue Oct 27 22:28:42 2020
no     44:38:39:00:00:32  10     leaf01            bond1                          no     Tue Oct 27 22:28:43 2020
no     46:38:39:00:00:44  10     leaf01            vni10                          yes    Tue Oct 27 22:28:43 2020
no     46:38:39:00:00:32  10     leaf01            bond1                          no     Tue Oct 27 22:28:42 2020
yes    52:37:ca:35:d3:70  10     leaf01            vni10                          no     Tue Oct 27 22:28:42 2020
```

### View MAC Addresses Associated with an Egress Port

You can filter information down to just the MAC addresses associated with a given VLAN on a device that use a particular egress port. Use the `netq <hostname> show macs` command with the `egress-port` and `vlan` options.

This example shows MAC addresses associated with the *leaf02* switch and VLAN *10* that use the *bridge* port.

```
cumulus@netq-ts:~$ netq leaf02 show macs egress-port bridge vlan 10
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    00:00:00:00:00:1a  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
yes    44:38:39:00:00:37  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
```

### View the MAC Addresses Associated with VRR Configurations

You can view all MAC addresses associated with your VRR (virtual router reflector) interface configuration using the `netq show interfaces type macvlan` command. This is useful for determining if the specified MAC address inside a VLAN is the same or different across your VRR configuration.

```
cumulus@switch:~$ netq show interfaces type macvlan
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    00:00:00:00:00:1a  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
yes    44:38:39:00:00:37  10     leaf02            bridge                         no     Tue Oct 27 22:28:51 2020
cumulus@netq-ts:~$ netq show interfaces type macvlan

Matching link records:
Hostname          Interface                 Type             State      VRF             Details                             Last Changed
----------------- ------------------------- ---------------- ---------- --------------- ----------------------------------- -------------------------
leaf01            vlan10-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1a,             Tue Oct 27 22:28:42 2020
                                                                                        Mode: Private
leaf01            vlan20-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1b,             Tue Oct 27 22:28:42 2020
                                                                                        Mode: Private
leaf01            vlan30-v0                 macvlan          up         BLUE            MAC: 00:00:00:00:00:1c,             Tue Oct 27 22:28:42 2020
                                                                                        Mode: Private
leaf02            vlan10-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1a,             Tue Oct 27 22:28:51 2020
                                                                                        Mode: Private
leaf02            vlan20-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1b,             Tue Oct 27 22:28:51 2020
                                                                                        Mode: Private
leaf02            vlan30-v0                 macvlan          up         BLUE            MAC: 00:00:00:00:00:1c,             Tue Oct 27 22:28:51 2020
                                                                                        Mode: Private
leaf03            vlan10-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1a,             Tue Oct 27 22:28:23 2020
                                                                                        Mode: Private
leaf03            vlan20-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1b,             Tue Oct 27 22:28:23 2020
                                                                                        Mode: Private
leaf03            vlan30-v0                 macvlan          up         BLUE            MAC: 00:00:00:00:00:1c,             Tue Oct 27 22:28:23 2020
                                                                                        Mode: Private
leaf04            vlan10-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1a,             Tue Oct 27 22:29:06 2020
                                                                                        Mode: Private
leaf04            vlan20-v0                 macvlan          up         RED             MAC: 00:00:00:00:00:1b,             Tue Oct 27 22:29:06 2020
                                                                                        Mode: Private
leaf04            vlan30-v0                 macvlan          up         BLUE            MAC: 00:00:00:00:00:1c,             Tue Oct 27 22:29:06 2020
```

## View All VLAN Events

You can view all VLAN-related events using the `netq show events type vlan` command.

This example shows that there have been no VLAN events in the last 24 hours or the last 30 days.

```
cumulus@switch:~$ netq show events type vlan
No matching event records found

cumulus@switch:~$ netq show events type vlan between now and 30d
No matching event records found
```
