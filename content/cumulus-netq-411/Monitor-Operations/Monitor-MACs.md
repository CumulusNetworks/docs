---
title: MAC Addresses
author: NVIDIA
weight: 870
toc: 3
---
A MAC (media access control) address is a layer 2 construct that uses 48 bits to uniquely identify a network interface controller (NIC) for communication within a network.

With NetQ, you can:

- View MAC addresses across the network and for a given device, VLAN, egress port on a VLAN, and VRR
- View a count of MAC addresses on a given device
- View where MAC addresses have lived in the network (MAC history)
- View commentary on changes to MAC addresses (MAC commentary)
- View events related to MAC addresses

<!-- vale off -->
MAC addresses are associated with switch interfaces. They are classified as:

- **Origin**: MAC address is owned by a particular switch, on one or more interfaces. A MAC address typically has only one origin node. The exceptions are when MLAG is configured, the MAC on the VRR interfaces for the MLAG pair is the same, and when EVPN is configured, the MAC is distributed across the layer 3 gateways.
- **Remote**: MAC address is learned or distributed by the control plane on a tunnel interface pointing to a particular remote location. For a given MAC address and VLAN there is only one first-hop switch (or switch pair), but multiple nodes can have the same remote MAC address.
- **Local** (not origin and not remote): MAC address is learned on a bridge and points to an interface on another switch. If the LLDP neighbor of the interface is a host, then this switch is the first-hop switch where the MAC address is learned. For a given MAC address and VLAN there is only one first-hop switch, except if the switches are part of an MLAG pair, and the interfaces on both switches form a dually or singly connected bond.
<!-- vale on -->

The NetQ UI provides a listing of current MAC addresses that you can filter by hostname, timestamp, MAC address, VLAN, and origin. You can sort the list by these parameters and also remote, static, and next hop.

Monitor MAC addresses with the following commands. Refer to the {{<link title="show/#netq-show-macs" text="command line reference">}} for additional options, definitions, and examples.

```
netq show macs
netq <hostname> show macs egress-port <egress-port>
netq show mac-history <mac>
netq show mac-commentary <mac> vlan <1-4096>
netq show events message_type macs
```

## View MAC Addresses Networkwide

You can view all MAC addresses across your network with the NetQ UI or the NetQ CLI.

{{<tabs "TabID49" >}}

{{<tab "NetQ UI" >}}

1. Select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the Network section, select **MACs**.

    {{<figure src="/images/netq/macs-full-470.png" alt="table listing all devices and their associated MAC addresses" width="1100">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the `netq show macs` command to view all MAC addresses.

This example shows all MAC addresses in the Cumulus Networks reference topology.

```
cumulus@switch:~$ netq show macs
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
no     46:38:39:00:00:46  20     leaf04            bond2                          no     Tue Oct 27 22:29:07 2020
yes    44:38:39:00:00:5e  20     leaf04            bridge                         no     Tue Oct 27 22:29:07 2020
yes    00:00:00:00:00:1a  10     leaf04            bridge                         no     Tue Oct 27 22:29:07 2020
yes    44:38:39:00:00:5e  4002   leaf04            bridge                         no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:5d  30     leaf04            peerlink                       no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:37  30     leaf04            vni30                          no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:59  30     leaf04            vni30                          no     Tue Oct 27 22:29:07 2020
yes    7e:1a:b3:4f:05:b8  20     leaf04            vni20                          no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:36  30     leaf04            vni30                          yes    Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:59  20     leaf04            vni20                          no     Tue Oct 27 22:29:07 2020
no     44:38:39:00:00:37  20     leaf04            vni20                          no     Tue Oct 27 22:29:07 2020
...
yes    7a:4a:c7:bb:48:27  4001   border01          vniRED                         no     Tue Oct 27 22:28:48 2020
yes    ce:93:1d:e3:08:1b  4002   border01          vniBLUE                        no     Tue Oct 27 22:28:48 2020
```

{{</tab>}}

{{</tabs>}}

## View MAC Addresses for a Given Device

{{<tabs "TabID98" >}}

{{<tab "NetQ UI" >}}

1. Select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the Network section, select **MACs**.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} **Filters** and enter a hostname:

    {{<figure src="/images/netq/macs-filter-470.png" alt="filter dialog prompting user to enter a hostname" width="400">}}

4. Click **Apply**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the `netq <hostname> show macs` command to view MAC address on a given device.

This example shows all MAC addresses on the *leaf03* switch.

```
cumulus@switch:~$ netq leaf03 show macs
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    2e:3d:b4:55:40:ba  4002   leaf03            vniBLUE                        no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:5e  20     leaf03            peerlink                       no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:46  20     leaf03            bond2                          no     Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  4001   leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    00:00:00:00:00:1a  10     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  30     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    26:6e:54:35:3b:28  4001   leaf03            vniRED                         no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:37  30     leaf03            vni30                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:59  30     leaf03            vni30                          no     Tue Oct 27 22:28:24 2020
yes    72:78:e6:4e:3d:4c  20     leaf03            vni20                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:36  30     leaf03            vni30                          yes    Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:59  20     leaf03            vni20                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:37  20     leaf03            vni20                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:59  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:37  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:48  30     leaf03            bond3                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:38  10     leaf03            vni10                          yes    Tue Oct 27 22:28:24 2020
yes    36:99:0d:48:51:41  10     leaf03            vni10                          no     Tue Oct 27 22:28:24 2020
yes    1a:6e:d8:ed:d2:04  30     leaf03            vni30                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:36  30     leaf03            vni30                          yes    Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:5e  30     leaf03            peerlink                       no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:3e  10     leaf03            bond1                          no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:34  20     leaf03            vni20                          yes    Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:5e  10     leaf03            peerlink                       no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:3c  30     leaf03            vni30                          yes    Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:3e  10     leaf03            bond1                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:34  20     leaf03            vni20                          yes    Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:42  30     leaf03            bond3                          no     Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  4002   leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  20     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:be:ef:bb  4002   leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:32  10     leaf03            vni10                          yes    Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  10     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    00:00:00:00:00:1b  20     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:44  10     leaf03            bond1                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:42  30     leaf03            bond3                          no     Tue Oct 27 22:28:24 2020
yes    44:38:39:be:ef:bb  4001   leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    00:00:00:00:00:1c  30     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:32  10     leaf03            vni10                          yes    Tue Oct 27 22:28:24 2020
no     44:38:39:00:00:40  20     leaf03            bond2                          no     Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:3a  20     leaf03            vni20                          yes    Tue Oct 27 22:28:24 2020
no     46:38:39:00:00:40  20     leaf03            bond2                          no     Tue Oct 27 22:28:24 2020
```

{{</tab>}}

{{</tabs>}}

## View MAC Addresses Associated with a VLAN

{{<tabs "TabID185" >}}

{{<tab "NetQ UI" >}}

1. Select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the Network section, select **MACs**.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} **Filters** and enter a VLAN ID.

4. Click **Apply**.

5. (Optional) Select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} **Filters** and add the additional hostname filter to view the MAC addresses for a VLAN on a particular device.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the `netq show macs` command with the `vlan` option to view the MAC addresses for a given VLAN.

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

Use the `netq show macs` command with the `hostname` and `vlan` options to view the MAC addresses for a given VLAN on a particular device.

This example shows the MAC addresses associated with VLAN *10* on the *leaf02* switch.

```
cumulus@switch:~$ netq leaf02 show macs vlan 10
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
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
```

{{</tab>}}

{{</tabs>}}

## View MAC Addresses Associated with an Egress Port

{{<tabs "TabID301" >}}

{{<tab "NetQ UI" >}}

1. Select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the Network section, select **MACs**.

3. Locate the **Egress port** column. Hover over the column header and select it to sort A-Z or Z-A order of the egress port used by a MAC address.

4. (Optional) Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} **Filters** and enter a hostname to view the MAC addresses on a particular device.


{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the `netq <hostname> show macs egress-port <egress-port>` command to view the MAC addresses on a given device that use a given egress port. Note that you cannot view this information across all devices.

This example shows MAC addresses associated with the *leaf03* switch that use the *bridge* port for egress.

```
cumulus@switch:~$ netq leaf03 show macs egress-port bridge
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    44:38:39:00:00:5d  4001   leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    00:00:00:00:00:1a  10     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  30     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  4002   leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  20     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:be:ef:bb  4002   leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:00:00:5d  10     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    00:00:00:00:00:1b  20     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    44:38:39:be:ef:bb  4001   leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
yes    00:00:00:00:00:1c  30     leaf03            bridge                         no     Tue Oct 27 22:28:24 2020
```

{{</tab>}}

{{</tabs>}}

## View MAC Addresses Associated with VRR Configurations

You can view all MAC addresses associated with your VRR (virtual router reflector) interface configuration using the `netq show interfaces type macvlan` command. This is useful for determining if the specified MAC address inside a VLAN is the same or different across your VRR configuration.

```
cumulus@switch:~$ netq show interfaces type macvlan
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
                                                                                        Mode: Private
```

## View the History of a MAC Address

<!-- vale off -->
It is useful when debugging to be able to see whether a MAC address is learned, where it moved in the network after that, if there was a duplicate at any time, and so forth. The `netq show mac-history` command makes this information available. It enables you to see:
<!-- vale on -->

- Each change made chronologically.
- Changes made between two points in time, using the `between` option.
- Only the differences in the changes between two points in time using the `diff` option.
- The output ordered by selected output fields using the `listby` option.
- Each change made for the MAC address on a particular VLAN, using the `vlan` option.

The default time range used is now to one hour ago. You can view the output in JSON format as well.

### View MAC Address Changes in Chronological Order

View the full listing of changes for a MAC address for the last hour in chronological order using the `netq show mac-history` command.

This example shows how to view a full chronology of changes for a MAC address of *44:38:39:00:00:5d*. When shown, the caret (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 44:38:39:00:00:5d
Matching machistory records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Tue Oct 27 22:28:24 2020  leaf03            10     yes    bridge                                  no     no
Tue Oct 27 22:28:42 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Tue Oct 27 22:28:51 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            10     no     peerlink                                no     yes
Tue Oct 27 22:28:24 2020  leaf03            4002   yes    bridge                                  no     no
Tue Oct 27 22:28:24 2020  leaf03            0      yes    peerlink                                no     no
Tue Oct 27 22:28:24 2020  leaf03            20     yes    bridge                                  no     no
Tue Oct 27 22:28:42 2020  leaf01            20     no     vni20            10.0.1.2               no     yes
Tue Oct 27 22:28:51 2020  leaf02            20     no     vni20            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            20     no     peerlink                                no     yes
Tue Oct 27 22:28:24 2020  leaf03            4001   yes    bridge                                  no     no
Tue Oct 27 22:28:24 2020  leaf03            30     yes    bridge                                  no     no
Tue Oct 27 22:28:42 2020  leaf01            30     no     vni30            10.0.1.2               no     yes
Tue Oct 27 22:28:51 2020  leaf02            30     no     vni30            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            30     no     peerlink                                no     yes
```

### View MAC Address Changes for a Given Time Frame

View a listing of changes for a MAC address for a given timeframe using the `netq show mac-history` command with the `between` option. When shown, the caret (^) notation indicates no change in this value from the row above.

This example shows changes for a MAC address of *44:38:39:00:00:5d* between now three and seven days ago.

```
cumulus@switch:~$ netq show mac-history 44:38:39:00:00:5d between 3d and 7d
Matching machistory records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Tue Oct 20 22:28:19 2020  leaf03            10     yes    bridge                                  no     no
Tue Oct 20 22:28:24 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Tue Oct 20 22:28:37 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Tue Oct 20 22:28:53 2020  leaf04            10     no     peerlink                                no     yes
Wed Oct 21 22:28:19 2020  leaf03            10     yes    bridge                                  no     no
Wed Oct 21 22:28:26 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Wed Oct 21 22:28:44 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Wed Oct 21 22:28:55 2020  leaf04            10     no     peerlink                                no     yes
Thu Oct 22 22:28:20 2020  leaf03            10     yes    bridge                                  no     no
Thu Oct 22 22:28:28 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Thu Oct 22 22:28:45 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Thu Oct 22 22:28:57 2020  leaf04            10     no     peerlink                                no     yes
Fri Oct 23 22:28:21 2020  leaf03            10     yes    bridge                                  no     no
Fri Oct 23 22:28:29 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Fri Oct 23 22:28:45 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Fri Oct 23 22:28:58 2020  leaf04            10     no     peerlink                                no     yes
Sat Oct 24 22:28:28 2020  leaf03            10     yes    bridge                                  no     no
Sat Oct 24 22:28:29 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Sat Oct 24 22:28:45 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Sat Oct 24 22:28:59 2020  leaf04            10     no     peerlink                                no     yes
Tue Oct 20 22:28:19 2020  leaf03            4002   yes    bridge                                  no     no
Tue Oct 20 22:28:19 2020  leaf03            0      yes    peerlink                                no     no
Tue Oct 20 22:28:19 2020  leaf03            20     yes    bridge                                  no     no
Tue Oct 20 22:28:24 2020  leaf01            20     no     vni20            10.0.1.2               no     yes
Tue Oct 20 22:28:37 2020  leaf02            20     no     vni20            10.0.1.2               no     yes
Tue Oct 20 22:28:53 2020  leaf04            20     no     peerlink                                no     yes
Wed Oct 21 22:28:19 2020  leaf03            20     yes    bridge                                  no     no
Wed Oct 21 22:28:26 2020  leaf01            20     no     vni20            10.0.1.2               no     yes
Wed Oct 21 22:28:44 2020  leaf02            20     no     vni20            10.0.1.2               no     yes
Wed Oct 21 22:28:55 2020  leaf04            20     no     peerlink                                no     yes
Thu Oct 22 22:28:20 2020  leaf03            20     yes    bridge                                  no     no
Thu Oct 22 22:28:28 2020  leaf01            20     no     vni20            10.0.1.2               no     yes
Thu Oct 22 22:28:45 2020  leaf02            20     no     vni20            10.0.1.2               no     yes
Thu Oct 22 22:28:57 2020  leaf04            20     no     peerlink                                no     yes
Fri Oct 23 22:28:21 2020  leaf03            20     yes    bridge                                  no     no
Fri Oct 23 22:28:29 2020  leaf01            20     no     vni20            10.0.1.2               no     yes
Fri Oct 23 22:28:45 2020  leaf02            20     no     vni20            10.0.1.2               no     yes
Fri Oct 23 22:28:58 2020  leaf04            20     no     peerlink                                no     yes
Sat Oct 24 22:28:28 2020  leaf03            20     yes    bridge                                  no     no
Sat Oct 24 22:28:29 2020  leaf01            20     no     vni20            10.0.1.2               no     yes
Sat Oct 24 22:28:45 2020  leaf02            20     no     vni20            10.0.1.2               no     yes
Sat Oct 24 22:28:59 2020  leaf04            20     no     peerlink                                no     yes
Tue Oct 20 22:28:19 2020  leaf03            4001   yes    bridge                                  no     no
Tue Oct 20 22:28:19 2020  leaf03            30     yes    bridge                                  no     no
Tue Oct 20 22:28:24 2020  leaf01            30     no     vni30            10.0.1.2               no     yes
Tue Oct 20 22:28:37 2020  leaf02            30     no     vni30            10.0.1.2               no     yes
Tue Oct 20 22:28:53 2020  leaf04            30     no     peerlink                                no     yes
Wed Oct 21 22:28:19 2020  leaf03            30     yes    bridge                                  no     no
Wed Oct 21 22:28:26 2020  leaf01            30     no     vni30            10.0.1.2               no     yes
Wed Oct 21 22:28:44 2020  leaf02            30     no     vni30            10.0.1.2               no     yes
Wed Oct 21 22:28:55 2020  leaf04            30     no     peerlink                                no     yes
Thu Oct 22 22:28:20 2020  leaf03            30     yes    bridge                                  no     no
Thu Oct 22 22:28:28 2020  leaf01            30     no     vni30            10.0.1.2               no     yes
Thu Oct 22 22:28:45 2020  leaf02            30     no     vni30            10.0.1.2               no     yes
Thu Oct 22 22:28:57 2020  leaf04            30     no     peerlink                                no     yes
Fri Oct 23 22:28:21 2020  leaf03            30     yes    bridge                                  no     no
Fri Oct 23 22:28:29 2020  leaf01            30     no     vni30            10.0.1.2               no     yes
Fri Oct 23 22:28:45 2020  leaf02            30     no     vni30            10.0.1.2               no     yes
Fri Oct 23 22:28:58 2020  leaf04            30     no     peerlink                                no     yes
Sat Oct 24 22:28:28 2020  leaf03            30     yes    bridge                                  no     no
Sat Oct 24 22:28:29 2020  leaf01            30     no     vni30            10.0.1.2               no     yes
Sat Oct 24 22:28:45 2020  leaf02            30     no     vni30            10.0.1.2               no     yes
Sat Oct 24 22:28:59 2020  leaf04            30     no     peerlink                                no     yes
```

### View Only the Differences in MAC Address Changes

Instead of viewing the full chronology of change made for a MAC address within a given timeframe, you can view only the differences between two snapshots using the `netq show mac-history` command with the `diff` option. When shown, the caret (^) notation indicates no change in this value from the row above.

This example shows only the differences in the changes for a MAC address of *44:38:39:00:00:5d* between now and an hour ago.

```
cumulus@switch:~$ netq show mac-history 44:38:39:00:00:5d diff
Matching machistory records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Tue Oct 27 22:29:07 2020  leaf04            30     no     peerlink                                no     yes
```

This example shows only the differences in the changes for a MAC address of *44:38:39:00:00:5d* between now and 30 days ago.

```
cumulus@switch:~$ netq show mac-history 44:38:39:00:00:5d diff between now and 30d
Matching machistory records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Mon Sep 28 00:02:26 2020  leaf04            30     no     peerlink                                no     no
Tue Oct 27 22:29:07 2020  leaf04            ^      ^      ^                ^                      ^      yes
```

### View MAC Address Changes by a Given Attribute

You can order the output of the MAC address changes by many of the attributes associated with the changes that you can make using the `netq show mac-history` command with the `listby` option. For example, you can order the output by hostname, link, destination, and so forth.

This example shows the history of MAC address *44:38:39:00:00:5d* ordered by hostname. When shown, the caret (^) notation indicates no change in this value from the row above.

```
cumulus@switch:~$ netq show mac-history 44:38:39:00:00:5d listby hostname
Matching machistory records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Tue Oct 27 22:28:51 2020  leaf02            20     no     vni20            10.0.1.2               no     yes
Tue Oct 27 22:28:24 2020  leaf03            4001   yes    bridge                                  no     no
Tue Oct 27 22:28:24 2020  leaf03            0      yes    peerlink                                no     no
Tue Oct 27 22:28:24 2020  leaf03            4002   yes    bridge                                  no     no
Tue Oct 27 22:28:42 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            10     no     peerlink                                no     yes
Tue Oct 27 22:29:07 2020  leaf04            30     no     peerlink                                no     yes
Tue Oct 27 22:28:42 2020  leaf01            30     no     vni30            10.0.1.2               no     yes
Tue Oct 27 22:28:42 2020  leaf01            20     no     vni20            10.0.1.2               no     yes
Tue Oct 27 22:28:51 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            20     no     peerlink                                no     yes
Tue Oct 27 22:28:51 2020  leaf02            30     no     vni30            10.0.1.2               no     yes
Tue Oct 27 22:28:24 2020  leaf03            10     yes    bridge                                  no     no
Tue Oct 27 22:28:24 2020  leaf03            20     yes    bridge                                  no     no
Tue Oct 27 22:28:24 2020  leaf03            30     yes    bridge                                  no     no
```

### View MAC Address Changes for a Given VLAN

View a listing of changes for a MAC address for a given VLAN using the `netq show mac-history` command with the `vlan` option. When shown, the caret (^) notation indicates no change in this value from the row above.

This example shows changes for a MAC address of *44:38:39:00:00:5d* and VLAN *10*.

```
cumulus@switch:~$ netq show mac-history 44:38:39:00:00:5d vlan 10
Matching machistory records:
Last Changed              Hostname          VLAN   Origin Link             Destination            Remote Static
------------------------- ----------------- ------ ------ ---------------- ---------------------- ------ ------------
Tue Oct 27 22:28:24 2020  leaf03            10     yes    bridge                                  no     no
Tue Oct 27 22:28:42 2020  leaf01            10     no     vni10            10.0.1.2               no     yes
Tue Oct 27 22:28:51 2020  leaf02            10     no     vni10            10.0.1.2               no     yes
Tue Oct 27 22:29:07 2020  leaf04            10     no     peerlink                                no     yes
```

### View MAC Address Commentary

You can get more descriptive information about changes to a given MAC address on a specific VLAN. Commentary is available for the following MAC address-related events based on their classification (refer to the definition of these at the beginning of this topic):

<!-- vale off -->
| Event Triggers | Example Commentary |
| --- | --- |
| A MAC address is created, or the MAC address on the interface is changed via the `hwaddress` option in */etc/network/interface* | leaf01 00:00:5e:00:00:03 configured on interface vlan1000-v0 |
| An interface becomes a slave in, or is removed from, a bond | leaf01 00:00:5e:00:00:03 configured on interface vlan1000-v0|
| An interface is a bridge and it inherits a different MAC address due to a membership change | leaf01 00:00:5e:00:00:03 configured on interface vlan1000-v0 |
| A remote MAC address is learned or installed by control plane on a tunnel interface | 44:38:39:00:00:5d learned/installed on vni vni10 pointing to remote dest 10.0.1.34 |
| A remote MAC address is flushed or expires | leaf01 44:38:39:00:00:5d is flushed or expired |
| A remote MAC address moves from behind one remote switch to another remote switch or becomes a local MAC address | leaf02: 00:08:00:00:aa:13 moved from remote dest 27.0.0.22 to remote dest 27.0.0.34 <br> 00:08:00:00:aa:13 moved from remote dest 27.0.0.22 to local interface hostbond2 |
| A MAC address is learned at the first-hop switch (or MLAG switch pair) | leaf04 (and MLAG peer leaf05): 44:38:39:00:00:5d learned on first hop switch, pointing to local interface bond4 |
| A local MAC address is flushed or expires | leaf04 (and MLAG peer leaf05) 44:38:39:00:00:5d is flushed or expires from bond4 |
| A local MAC address moves from one interface to another interface or to another switch | leaf04: 00:08:00:00:aa:13 moved from hostbond2 to hostbond3 <br> 00:08:00:00:aa:13 moved from hostbond2 to remote dest 27.0.0.13 |
<!-- vale on -->

{{<tabs "MAC commentary" >}}

{{<tab "NetQ UI" >}}

To view MAC address commentary:

1. Select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the **Network** heading, select **MACs**.

3. Select the checkbox next to one of the entries, then select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Open card** above the table.

4. Choose a time range, then click **Continue**.

5. You can scroll through the list to see comments related to the MAC address moves and changes:

   {{<figure src="/images/netq/mac-move-commentary-card.png" alt="MAC move commentary card displaying 7 results from the past 24 hours" width="500">}}

8. (Optional) From here, you can filter the list by a given device by selecting {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" width="18" height="18">}} **Filters**. 

<div style="padding-left: 18px;">A red dot on the filter icon indicates that filtering is active. To remove the filter, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" width="18" height="18">}} again, then click <strong>Clear Filter</strong>.</div>

{{</tab>}}

{{<tab "NetQ CLI" >}}

To see MAC address commentary, use the `netq show mac-commentary` command. The following examples show the commentary seen in common situations.

#### MAC Address Configured Locally

In this example, the 46:38:39:00:00:44 MAC address was configured on the VlanA-1 interface of multiple switches, so we see the MAC configured commentary on each of them.

```
cumulus@server-01:~$ netq show mac-commentary 46:38:39:00:00:44 between now and 1hr 
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Mon Aug 24 2020 14:14:33  leaf11           100    leaf11: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:03  leaf12           100    leaf12: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:19  leaf21           100    leaf21: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:40  leaf22           100    leaf22: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:19  leaf21           1003   leaf21: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:40  leaf22           1003   leaf22: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:16:32  leaf02           1003   leaf02: 00:00:5e:00:01:01 configured on interface VlanA-1
```

#### MAC Address Configured on Server and Learned from a Peer

<!-- vale off -->
In this example, the 00:08:00:00:aa:13 MAC address was configured on server01. As a result, both leaf11 and leaf12 learned this address on the next hop interface serv01bond2 (learned locally), whereas, the leaf01 switch learned this address remotely on vx-34 (learned remotely).
<!-- vale on -->

```
cumulus@server11:~$ netq show mac-commentary 00:08:00:00:aa:13 vlan 1000 between now and 5hr 
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Tue Aug 25 2020 10:29:23  leaf12           1000     leaf12: 00:08:00:00:aa:13 learned on first hop switch interface serv01bond2
Tue Aug 25 2020 10:29:23  leaf11           1000     leaf11: 00:08:00:00:aa:13 learned on first hop switch interface serv01bond2
Tue Aug 25 2020 10:29:23  leaf01           1000     leaf01: 00:08:00:00:aa:13 learned/installed on vni vx-34 pointing to remote dest 36.0.0.24
```

#### MAC Address Removed

<!-- vale off -->
In this example the bridge FDB entry for the 00:02:00:00:00:a0 MAC address, interface VlanA-1, and VLAN 100 was deleted impacting leaf11 and leaf12.
<!-- vale on -->

```
cumulus@server11:~$ netq show mac-commentary 00:02:00:00:00:a0 vlan 100 between now and 5hr 
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Mon Aug 24 2020 14:14:33  leaf11           100    leaf11: 00:02:00:00:00:a0 configured on interface VlanA-1
Mon Aug 24 2020 14:15:03  leaf12           100    leaf12: 00:02:00:00:00:a0 learned on first hop switch interface peerlink-1
Tue Aug 25 2020 13:06:52  leaf11           100    leaf11: 00:02:00:00:00:a0 unconfigured on interface VlanA-1
```

#### MAC Address Moved on Server and Learned from a Peer

The MAC address on server11 changed from 00:08:00:00:aa:13. In this example, the MAC learned remotely on leaf01 is now a locally learned MAC address from its local interface swp6. Similarly, the locally learned MAC addresses on leaf11 and leaf12 are now learned from remote dest 27.0.0.22.

```
cumulus@server11:~$ netq show mac-commentary 00:08:00:00:aa:13 vlan 1000 between now and 5hr
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Tue Aug 25 2020 10:29:23  leaf12           1000   leaf12: 00:08:00:00:aa:13 learned on first hop switch interface serv01bond2
Tue Aug 25 2020 10:29:23  leaf11           1000   leaf11: 00:08:00:00:aa:13 learned on first hop switch interface serv01bond2
Tue Aug 25 2020 10:29:23  leaf01           1000   leaf01: 00:08:00:00:aa:13 learned/installed on vni vx-34 pointing to remote dest 36.0.0.24
Tue Aug 25 2020 10:33:06  leaf01           1000   leaf01: 00:08:00:00:aa:13 moved from remote dest 36.0.0.24 to local interface swp6
Tue Aug 25 2020 10:33:06  leaf12           1000   leaf12: 00:08:00:00:aa:13 moved from local interface serv01bond2 to remote dest 27.0.0.22
Tue Aug 25 2020 10:33:06  leaf11           1000   leaf11: 00:08:00:00:aa:13 moved from local interface serv01bond2 to remote dest 27.0.0.22
```

#### MAC Address Learned from MLAG Pair

In this example, after the local first hop learning of the 00:02:00:00:00:1c MAC address on leaf11 and leaf12, the MLAG exchanged the learning on the dually connected interface serv01bond3.

```
cumulus@server11:~$ netq show mac-commentary 00:02:00:00:00:1c vlan 105 between now and 2d
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Sun Aug 23 2020 14:13:39  leaf11          105    leaf11: 00:02:00:00:00:1c learned on first hop switch interface serv01bond3
Sun Aug 23 2020 14:14:02  leaf12          105    leaf12: 00:02:00:00:00:1c learned on first hop switch interface serv01bond3
Sun Aug 23 2020 14:14:16  leaf11          105    leaf11: 00:02:00:00:00:1c moved from interface serv01bond3 to interface serv01bond3
Sun Aug 23 2020 14:14:23  leaf12          105    leaf12: 00:02:00:00:00:1c learned on MLAG peer dually connected interface serv01bond3
Sun Aug 23 2020 14:14:37  leaf11          105    leaf11: 00:02:00:00:00:1c learned on MLAG peer dually connected interface serv01bond3
Sun Aug 23 2020 14:14:39  leaf12          105    leaf12: 00:02:00:00:00:1c moved from interface serv01bond3 to interface serv01bond3
Sun Aug 23 2020 14:53:31  leaf11          105    leaf11: 00:02:00:00:00:1c learned on MLAG peer dually connected interface serv01bond3
Mon Aug 24 2020 14:15:03  leaf12          105    leaf12: 00:02:00:00:00:1c learned on MLAG peer dually connected interface serv01bond3
```

#### MAC Address Flushed

<!-- vale off -->
In this example, the interface VlanA-1 associated with the 00:02:00:00:00:2d MAC address and VLAN 1008 is deleted, impacting leaf11 and leaf12.
<!-- vale on -->

```
cumulus@server11:~$ netq show mac-commentary 00:02:00:00:00:2d vlan 1008 between now and 5hr 
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Mon Aug 24 2020 14:14:33  leaf11           1008   leaf11:  00:02:00:00:00:2d learned/installed on vni vx-42 pointing to remote dest 27.0.0.22
Mon Aug 24 2020 14:15:03  leaf12           1008   leaf12:  00:02:00:00:00:2d learned/installed on vni vx-42 pointing to remote dest 27.0.0.22
Mon Aug 24 2020 14:16:03  leaf01           1008   leaf01:  00:02:00:00:00:2d learned on MLAG peer dually connected interface swp8
Tue Aug 25 2020 11:36:06  leaf11           1008   leaf11:  00:02:00:00:00:2d is flushed or expired
Tue Aug 25 2020 11:36:06  leaf11           1008   leaf11:  00:02:00:00:00:2d on vni 1008 remote dest changed to 27.0.0.22
```

{{</tab>}}

{{</tabs>}}
