---
title: Verify Network Connectivity
author: NVIDIA
weight: 1030
toc: 2
---
You can verify the connectivity between two devices in both an ad-hoc fashion and by defining connectivity checks to occur on a scheduled basis.
## Specifying Source and Destination Values

When specifying traces, the following options are available for the source and destination values:

| Trace Type | Source | Destination |
| ---- | ----| ---- |
| Layer 2 | Hostname | MAC address plus VLAN |
| Layer 2 | IPv4/IPv6 address plus VRF (if not default) | MAC address plus VLAN |
| Layer 2 | MAC Address | MAC address plus VLAN |
| Layer 3 | Hostname | IPv4/IPv6 address |
| Layer 3 | IPv4/IPv6 address plus VRF (if not default) | IPv4/IPv6 address |

{{<notice info>}}

If you use an IPv6 address, you must enter the complete, non-truncated address.

{{</notice>}}

### Known Addresses

The tracing function only knows about previously learned addresses. If you find that a path is invalid or incomplete, ping the identified device so that its address becomes known.

<!-- vale off -->
## Create On-demand Traces
<!-- vale on -->

You can view the current connectivity between two devices in your network by creating an on-demand trace. You can perform these traces at layer 2 or layer 3 using the NetQ UI or the NetQ CLI.

<!-- vale off -->
### Create a Layer 3 On-demand Trace Request
<!-- vale on -->

It is helpful to verify the connectivity between two devices when you suspect an issue is preventing proper communication between them. If you cannot find a layer 3 path, you might also try checking connectivity through a layer 2 path.

{{<tabs "TabID83" >}}

{{<tab "On-demand Trace Request" >}}

1. Determine the IP addresses of the two devices you want to trace.

    1. Open the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**. Under **Bulk data**, select **IP addresses**.

    2. Select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} **Filter** and enter a hostname.

    3. From the list of results, note the relevant address.

    4. Filter the list again for the other hostname, and note its address.

2. Open the Trace Request card.

    - On a new workbench: Type *trace* in the **Global search** field and select the card.
    - On a current workbench: Click {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}} **Add card**, then select the **Trace** card.

3. In the **Source** field, enter the hostname or IP address of the device where you want to start the trace.

4. In the **Destination** field, enter the IP address of the device where you want to end the trace.  

    {{<figure src="/images/netq/new-trace-request-card.png" width="500">}}

<div style="padding-left: 18px;"><div class="notices tip"><p>If you mistype an address, you must double-click it, or backspace over the error, and retype the address. You cannot select the address by dragging over it as this action attempts to move the card to another location.</p></div></div>

5. Click **Run now**. A corresponding Trace Results card is opened on your workbench.

{{</tab>}}

{{<tab "netq trace" >}}

Use the `netq trace` command to view the results in the terminal window. Use the `netq add trace` command to view the results in the NetQ UI.

To create a layer 3 on-demand trace and see the results in the terminal window, run:

```
netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]
```

Note the syntax requires the *destination* device address first and then the *source* device address or hostname.

This example shows a trace from 10.10.10.1 (source, leaf01) to 10.10.10.63 (destination, border01) on the underlay in pretty output. You could have used *leaf01* as the source instead of its IP address. The example first identifies the addresses for the source and destination devices using `netq show ip addresses` then runs the trace.

```
cumulus@switch:~$ netq border01 show ip addresses

Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
192.168.200.63/24         border01          eth0                                      Tue Nov  3 15:45:31 2020
10.0.1.254/32             border01          lo                        default         Mon Nov  2 22:28:54 2020
10.10.10.63/32            border01          lo                        default         Mon Nov  2 22:28:54 2020

cumulus@switch:~$ netq trace 10.10.10.63 from  10.10.10.1 pretty
Number of Paths: 12
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9216

 leaf01 swp54 -- swp1 spine04 swp6 -- swp54 border02 peerlink.4094 -- peerlink.4094 border01 lo
                                                     peerlink.4094 -- peerlink.4094 border01 lo
 leaf01 swp53 -- swp1 spine03 swp6 -- swp53 border02 peerlink.4094 -- peerlink.4094 border01 lo
                                                     peerlink.4094 -- peerlink.4094 border01 lo
 leaf01 swp52 -- swp1 spine02 swp6 -- swp52 border02 peerlink.4094 -- peerlink.4094 border01 lo
                                                     peerlink.4094 -- peerlink.4094 border01 lo
 leaf01 swp51 -- swp1 spine01 swp6 -- swp51 border02 peerlink.4094 -- peerlink.4094 border01 lo
                                                     peerlink.4094 -- peerlink.4094 border01 lo
 leaf01 swp54 -- swp1 spine04 swp5 -- swp54 border01 lo
 leaf01 swp53 -- swp1 spine03 swp5 -- swp53 border01 lo
 leaf01 swp52 -- swp1 spine02 swp5 -- swp52 border01 lo
 leaf01 swp51 -- swp1 spine01 swp5 -- swp51 border01 lo
```

Each row of the pretty output shows one of the 12 available paths, with each path described by hops using the following format:

source hostname and source egress port -- ingress port of first hop and device hostname and egress port -- n*(ingress port of next hop and device hostname and egress port) -- ingress port of destination device hostname

In this example, 8 of 12 paths use four hops to get to the destination and four use three hops. The overall MTU for all paths is 9216. No errors or warnings are present on any of the paths.

{{</tab>}}

{{<tab "netq add trace" >}}

To create a layer 3 on-demand trace and see the results in the On-demand Trace Results card, run:

```
netq add trace <ip> from (<src-hostname> | <ip-src>) [alert-on-failure]
```

This example shows a trace from 10.10.10.1 (source, leaf01) to 10.10.10.63 (destination, border01).

```
cumulus@switch:~$ netq add trace 10.10.10.63 from 10.10.10.1
Running job None src 10.10.10.1 dst 10.10.10.63
```

{{</tab>}}

{{</tabs>}}

<!-- vale off -->
### Create a Layer 3 On-demand Trace Through a Given VRF
<!-- vale on -->

{{<tabs "TabID264" >}}

{{<tab "On-demand Trace Request" >}}

To create the trace request:

Follow steps 1 through 4 as outlined in the {{<link url="#Create a Layer 3 On-demand Trace Request" text="previous section">}}.

5. In the **VRF** field, enter the identifier for the VRF associated with these devices.

6. Click **Run now**. A corresponding Trace Results card is opened on your workbench.

{{</tab>}}

{{<tab "netq trace">}}

Use the `netq trace` command to view the results in the terminal window. Use the `netq add trace` command to view the results in the NetQ UI.

To create a layer 3 on-demand trace through a given VRF and see the results in the terminal window, run:

```
netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]
```

Note the syntax requires the *destination* device address first and then the *source* device address or hostname.

This example shows a trace from 10.1.10.101 (source, server01) to 10.1.10.104 (destination, server04) through VRF RED in detail output. It first identifies the addresses for the source and destination devices and a VRF between them using `netq show ip addresses` then runs the trace. Note that the VRF name is case sensitive. The trace job might take some time to compile all the available paths, especially if there are many of them.

```
cumulus@switch:~$ netq server01 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
192.168.200.31/24         server01          eth0                      default         Tue Nov  3 19:50:21 2020
10.1.10.101/24            server01          uplink                    default         Tue Nov  3 19:50:21 2020

cumulus@switch:~$ netq server04 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.1.10.104/24            server04          uplink                    default         Tue Nov  3 19:50:23 2020
192.168.200.34/24         server04          eth0                      default         Tue Nov  3 19:50:23 2020

cumulus@switch:~$ netq trace 10.1.10.104 from 10.1.10.101 vrf RED
Number of Paths: 16
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9000

Id  Hop Hostname    InPort          InTun, RtrIf    OutRtrIf, Tun   OutPort
--- --- ----------- --------------- --------------- --------------- ---------------
1   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp54
    3   spine04     swp2            swp2            swp4            swp4
    4   leaf04      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
2   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp54
    3   spine04     swp2            swp2            swp3            swp3
    4   leaf03      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
3   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp53
    3   spine03     swp2            swp2            swp4            swp4
    4   leaf04      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
4   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp53
    3   spine03     swp2            swp2            swp3            swp3
    4   leaf03      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
5   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp52
    3   spine02     swp2            swp2            swp4            swp4
    4   leaf04      swp52           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
6   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp52
    3   spine02     swp2            swp2            swp3            swp3
    4   leaf03      swp52           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
7   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp51
    3   spine01     swp2            swp2            swp4            swp4
    4   leaf04      swp51           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
8   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp51
    3   spine01     swp2            swp2            swp3            swp3
    4   leaf03      swp51           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
9   1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp54
    3   spine04     swp1            swp1            swp4            swp4
    4   leaf04      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
10  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp54
    3   spine04     swp1            swp1            swp3            swp3
    4   leaf03      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
11  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp53
    3   spine03     swp1            swp1            swp4            swp4
    4   leaf04      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
12  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp53
    3   spine03     swp1            swp1            swp3            swp3
    4   leaf03      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
13  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp52
    3   spine02     swp1            swp1            swp4            swp4
    4   leaf04      swp52           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
14  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp52
    3   spine02     swp1            swp1            swp3            swp3
    4   leaf03      swp52           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
15  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp51
    3   spine01     swp1            swp1            swp4            swp4
    4   leaf04      swp51           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
16  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp51
    3   spine01     swp1            swp1            swp3            swp3
    4   leaf03      swp51           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
```
{{</tab>}}

{{<tab "netq add trace">}}

To create a layer 3 on-demand trace and see the results in the On-demand Trace Results card, run:

```
netq add trace <ip> from (<src-hostname> | <ip-src>) vrf <vrf>
```

This example shows a trace from 10.1.10.101 (source, server01) to 10.1.10.104 (destination, server04) through VRF RED.

```
cumulus@switch:~$ netq add trace 10.1.10.104 from 10.1.10.101 vrf RED
```

{{</tab>}}

{{</tabs>}}

<!-- vale off -->
### Create a Layer 2 On-demand Trace
<!-- vale on -->

It is helpful to verify the connectivity between two devices when you suspect an issue is preventing proper communication between them. If you cannot find a path through a layer 2 path, you might also try checking connectivity through a layer 3 path.

{{<tabs "Create Layer 2 On-demand Trace">}}

{{<tab "On-demand Trace Request">}}

To create a layer 2 trace request:

Follow steps 1 through 4 as outlined in the {{<link url="#Create a Layer 3 On-demand Trace Request" text="previous section">}}.

5. In the **VLAN ID** field, enter the identifier for the VLAN associated with the destination.

6. Click **Run Now**. A corresponding Trace Results card is opened on your workbench.

{{</tab>}}

{{<tab "netq trace" >}}

Use the `netq trace` command to view on-demand trace results in the terminal window.

To create a layer 2 on-demand trace and see the results in the terminal window, run:

```
netq trace (<mac> vlan <1-4096>) from <mac-src> [around <text-time>] [json|detail|pretty] [debug]
```

Note the syntax requires the *destination* device address first and then the *source* device address or hostname.

This example shows a trace from 44:38:39:00:00:32 (source, server01) to 44:38:39:00:00:3e (destination, server04) through VLAN 10 in detail output. It first identifies the MAC addresses for the two devices using `netq show ip neighbors`. Then it determines the VLAN using `netq show macs`. Then it runs the trace.

```
cumulus@switch:~$ netq show ip neighbors
Matching neighbor records:
IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
...
192.168.200.1             server04          eth0                      44:38:39:00:00:6d  default         no     Tue Nov  3 19:50:23 2020
10.1.10.1                 server04          uplink                    00:00:00:00:00:1a  default         no     Tue Nov  3 19:50:23 2020
10.1.10.101               server04          uplink                    44:38:39:00:00:32  default         no     Tue Nov  3 19:50:23 2020
10.1.10.2                 server04          uplink                    44:38:39:00:00:5d  default         no     Tue Nov  3 19:50:23 2020
10.1.10.3                 server04          uplink                    44:38:39:00:00:5e  default         no     Tue Nov  3 19:50:23 2020
192.168.200.250           server04          eth0                      44:38:39:00:01:80  default         no     Tue Nov  3 19:50:23 2020
192.168.200.1             server03          eth0                      44:38:39:00:00:6d  default         no     Tue Nov  3 19:50:22 2020
192.168.200.250           server03          eth0                      44:38:39:00:01:80  default         no     Tue Nov  3 19:50:22 2020
192.168.200.1             server02          eth0                      44:38:39:00:00:6d  default         no     Tue Nov  3 19:50:22 2020
10.1.20.1                 server02          uplink                    00:00:00:00:00:1b  default         no     Tue Nov  3 19:50:22 2020
10.1.20.2                 server02          uplink                    44:38:39:00:00:59  default         no     Tue Nov  3 19:50:22 2020
10.1.20.3                 server02          uplink                    44:38:39:00:00:37  default         no     Tue Nov  3 19:50:22 2020
10.1.20.105               server02          uplink                    44:38:39:00:00:40  default         no     Tue Nov  3 19:50:22 2020
192.168.200.250           server02          eth0                      44:38:39:00:01:80  default         no     Tue Nov  3 19:50:22 2020
192.168.200.1             server01          eth0                      44:38:39:00:00:6d  default         no     Tue Nov  3 19:50:21 2020
10.1.10.1                 server01          uplink                    00:00:00:00:00:1a  default         no     Tue Nov  3 19:50:21 2020
10.1.10.2                 server01          uplink                    44:38:39:00:00:59  default         no     Tue Nov  3 19:50:21 2020
10.1.10.3                 server01          uplink                    44:38:39:00:00:37  default         no     Tue Nov  3 19:50:21 2020
10.1.10.104               server01          uplink                    44:38:39:00:00:3e  default         no     Tue Nov  3 19:50:21 2020
192.168.200.250           server01          eth0                      44:38:39:00:01:80  default         no     Tue Nov  3 19:50:21 2020
...

cumulus@switch:~$ netq show macs
Matching mac records:
Origin MAC Address        VLAN   Hostname          Egress Port                    Remote Last Changed
------ ------------------ ------ ----------------- ------------------------------ ------ -------------------------
yes    44:38:39:00:00:5e  4002   leaf04            bridge                         no     Fri Oct 30 22:29:16 2020
no     46:38:39:00:00:46  20     leaf04            bond2                          no     Fri Oct 30 22:29:16 2020
no     44:38:39:00:00:5d  30     leaf04            peerlink                       no     Fri Oct 30 22:29:16 2020
yes    00:00:00:00:00:1a  10     leaf04            bridge                         no     Fri Oct 30 22:29:16 2020
yes    44:38:39:00:00:5e  20     leaf04            bridge                         no     Fri Oct 30 22:29:16 2020
yes    7e:1a:b3:4f:05:b8  20     leaf04            vni20                          no     Fri Oct 30 22:29:16 2020
...
no     46:38:39:00:00:3e  10     leaf01            vni10                          yes    Fri Oct 30 22:28:50 2020
...
yes    44:38:39:00:00:4d  4001   border01          bridge                         no     Fri Oct 30 22:28:53 2020
yes    7a:4a:c7:bb:48:27  4001   border01          vniRED                         no     Fri Oct 30 22:28:53 2020
yes    ce:93:1d:e3:08:1b  4002   border01          vniBLUE                        no     Fri Oct 30 22:28:53 2020

cumulus@switch:~$ netq trace 44:38:39:00:00:3e vlan 10 from 44:38:39:00:00:32
Number of Paths: 16
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 9000

Id  Hop Hostname    InPort          InTun, RtrIf    OutRtrIf, Tun   OutPort
--- --- ----------- --------------- --------------- --------------- ---------------
1   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp54
    3   spine04     swp2            swp2            swp4            swp4
    4   leaf04      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
2   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp54
    3   spine04     swp2            swp2            swp3            swp3
    4   leaf03      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
3   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp53
    3   spine03     swp2            swp2            swp4            swp4
    4   leaf04      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
4   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp53
    3   spine03     swp2            swp2            swp3            swp3
    4   leaf03      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
5   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp52
    3   spine02     swp2            swp2            swp4            swp4
    4   leaf04      swp52           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
6   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp52
    3   spine02     swp2            swp2            swp3            swp3
    4   leaf03      swp52           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
7   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp51
    3   spine01     swp2            swp2            swp4            swp4
    4   leaf04      swp51           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
8   1   server01                                                    mac:44:38:39:00
                                                                    :00:38
    2   leaf02      swp1                            vni: 10         swp51
    3   spine01     swp2            swp2            swp3            swp3
    4   leaf03      swp51           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
9   1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp54
    3   spine04     swp1            swp1            swp4            swp4
    4   leaf04      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
10  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp54
    3   spine04     swp1            swp1            swp3            swp3
    4   leaf03      swp54           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
11  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp53
    3   spine03     swp1            swp1            swp4            swp4
    4   leaf04      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
12  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp53
    3   spine03     swp1            swp1            swp3            swp3
    4   leaf03      swp53           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
13  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp52
    3   spine02     swp1            swp1            swp4            swp4
    4   leaf04      swp52           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
14  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp52
    3   spine02     swp1            swp1            swp3            swp3
    4   leaf03      swp52           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
15  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp51
    3   spine01     swp1            swp1            swp4            swp4
    4   leaf04      swp51           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
16  1   server01                                                    mac:44:38:39:00
                                                                    :00:32
    2   leaf01      swp1                            vni: 10         swp51
    3   spine01     swp1            swp1            swp3            swp3
    4   leaf03      swp51           vni: 10                         bond1
    5   server04    uplink
--- --- ----------- --------------- --------------- --------------- ---------------
```

{{</tab>}}

{{<tab "netq add trace" >}}

Use the `netq add trace` command to view on-demand trace results in the NetQ UI.

To create a layer 2 on-demand trace and see the results in the On-demand Trace Results card, run:

```
netq add trace <mac> vlan <1-4096> from <mac-src>
```

This example shows a trace from 44:38:39:00:00:32 (source, server01) to 44:38:39:00:00:3e (destination, server04) through VLAN 10.

```
cumulus@switch:~$ netq add trace 44:38:39:00:00:3e vlan 10 from 44:38:39:00:00:32
```

{{</tab>}}

{{</tabs>}}

<!-- vale off -->
## View On-demand Trace Results
<!-- vale on -->

After you have started an on-demand trace or run the `netq add trace` command, the results appear in either the UI or CLI. In the CLI, run the `netq show trace results` command. In the UI, locate the On-demand Trace Result card: 

{{<tabs "TabID832" >}}

{{<tab "Trace Results card" >}}

After you click **Run now**, the corresponding results card opens on your workbench. While it is working on the trace, a notice appears on the card indicating it is running. When it is finished, the results are displayed: 
{{<figure src="/images/netq/trace-results-med-450.png" width="200">}}

To view additional information, expand the card to its largest size and click on a trace. From this screen, you can view configuration details, error and warning messages, and granular data for individual paths.

    {{<figure src="/images/netq/trace-results-details-450.png" width="1100">}}

{{</tab>}}

{{</tabs>}}
## Create Scheduled Traces

There might be paths through your network that you consider critical or particularly important to your everyday operations. In these cases, it might be useful to create one or more traces to periodically confirm that at least one path is available between the relevant two devices. You can create scheduled traces at layer 2 or layer 3 in your network, from the NetQ UI and the NetQ CLI.

### Create a Layer 3 Scheduled Trace

{{<tabs "TabID920" >}}

{{<tab "NetQ UI" >}}

To schedule a trace:

Follow steps 1 through 4 as outlined in the {{<link url="#Create a Layer 3 On-demand Trace Request" text="previous section">}}.

5. Select a timeframe under **Schedule** to specify how often you want to run the trace.

    {{<figure src="/images/netq/trace-schedule-450.png" width="300">}}

6. Accept the default starting time, or click in the **Starting** field to specify the day you want the trace to run for the first time.

7. Verify your entries are correct, then click **Save as new**.

8. Provide a name for the trace. **Note**: This name must be unique for a given user.

9. Click **Save**.

    You can now run this trace on demand by selecting it from the dropdown list, or wait for it to run on its defined schedule.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To create a layer 3 scheduled trace and see the results in the Scheduled Trace Results card, run:

```
netq add trace name <text-new-trace-name> <ip> from (<src-hostname>|<ip-src>) interval <text-time-min>
```

This example shows the creation of a scheduled trace between *leaf01* (source, *10.10.10.1*) and *border01* (destination, *10.10.10.63*) with a name of *L01toB01Daily* that runs on an daily basis. The `interval` option value is *1440* minutes, as denoted by the units indicator (*m*).

```
cumulus@switch:~$ netq add trace name Lf01toBor01Daily 10.10.10.63 from 10.10.10.1 interval 1440m
Successfully added/updated Lf01toBor01Daily running every 1440m
```

View the results in the NetQ UI.

{{</tab>}}

{{</tabs>}}

### Create a Layer 3 Scheduled Trace through a Given VRF

{{<tabs "TabID1004" >}}

{{<tab "NetQ UI" >}}

To schedule a trace from the NetQ UI:

Follow steps 1 through 4 as outlined in the {{<link url="#Create a Layer 3 On-demand Trace Request" text="previous section">}}.

5. Enter a **VRF** interface if you are using anything other than the default VRF.

6. Select a timeframe under **Schedule** to specify how often you want to run the trace.

    {{<figure src="/images/netq/trace-schedule-450.png" width="300">}}

6. Accept the default starting time, or click in the **Starting** field to specify the day you want the trace to run for the first time.

7. Verify your entries are correct, then click **Save as new**.

8. Provide a name for the trace. **Note**: This name must be unique for a given user.

9. Click **Save**.

    You can now run this trace on demand by selecting it from the dropdown list, or wait for it to run on its defined schedule.
{{</tab>}}

{{<tab "NetQ CLI" >}}

To create a layer 3 scheduled trace that uses a VRF other than default and then see the results in the Scheduled Trace Results card, run:

```
netq add trace name <text-new-trace-name> <ip> from (<src-hostname>|<ip-src>) vrf <vrf> interval <text-time-min>
```

This example shows the creation of a scheduled trace between *server01* (source, *10.1.10.101*) and *server04* (destination, *10.1.10.104*) with a name of *Svr01toSvr04Hrly* that runs on an hourly basis. The `interval` option value is *60* minutes, as denoted by the units indicator (*m*).

```
cumulus@switch:~$ netq add trace name Svr01toSvr04Hrly 10.1.10.104 from 10.10.10.1 interval 60m
Successfully added/updated Svr01toSvr04Hrly running every 60m
```

View the results in the NetQ UI.

{{</tab>}}

{{</tabs>}}

### Create a Layer 2 Scheduled Trace

{{<tabs "TabID1069" >}}

{{<tab "NetQ UI" >}}

To schedule a layer 2 trace:

Follow steps 1 through 4 as outlined in the {{<link url="#Create a Layer 3 On-demand Trace Request" text="previous section">}}.

5. In the **VLAN** field, enter the VLAN ID associated with the destination device.

6. Select a timeframe under **Schedule** to specify how often you want to run the trace.

    {{<figure src="/images/netq/trace-schedule-450.png" width="300">}}

7. Accept the default starting time, or click in the **Starting** field to specify the day you want the trace to run for the first time.

8. Verify your entries are correct, then click **Save as new**.

9. Provide a name for the trace. **Note**: This name must be unique for a given user.

10. Click **Save**.

    You can now run this trace on demand by selecting it from the dropdown list, or wait for it to run on its defined schedule.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To create a layer 2 scheduled trace and then see the results in the Scheduled Trace Result card, run:

```
netq add trace name <text-new-trace-name> <mac> vlan <1-4096> from (<src-hostname> | <ip-src>) [vrf <vrf>] interval <text-time-min>
```

This example shows the creation of a scheduled trace between *server01* (source, *10.1.10.101*) and *server04* (destination, *44:38:39:00:00:3e*) on VLAN 10 with a name of *Svr01toSvr04x3Hrs* that runs every three hours. The `interval` option value is *180* minutes, as denoted by the units indicator (*m*).

```
cumulus@switch:~$ netq add trace name Svr01toSvr04x3Hrs 44:38:39:00:00:3e vlan 10 from 10.1.10.101 interval 180m
Successfully added/updated Svr01toSvr04x3Hrs running every 180m
```

View the results in the NetQ UI.

{{</tab>}}

{{</tabs>}}

## View Scheduled Trace Results

{{<tabs "TabID1166" >}}

{{<tab "NetQ UI" >}}

The results of scheduled traces are displayed on the Scheduled Trace Results card. To view the results:

1. Locate the Scheduled Trace Request card on your workbench and expand it to its largest size:

    {{<figure src="/images/netq/scheduled-trace-results-450.png" width="900">}}

2. Select the scheduled trace results you want to view. Above the table, select {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}} **Open card**. This opens the medium Scheduled Trace Results card(s) for the selected items.

{{</tab>}}

{{<tab "NetQ CLI" >}}

### View a Summary of All Scheduled Traces

You can view a summary of all scheduled traces using the `netq show trace summary` command. The summary displays the name of the trace, a job ID, status, and timestamps for when was run and when it completed.

This example shows all scheduled traces run in the last 24 hours.

```
cumulus@switch:~$ netq show trace summary
Name            Job ID       Status           Status Details               Start Time           End Time
--------------- ------------ ---------------- ---------------------------- -------------------- ----------------
leaf01toborder0 f8d6a2c5-54d Complete         0                            Fri Nov  6 15:04:54  Fri Nov  6 15:05
1               b-44a8-9a5d-                                               2020                 :21 2020
                9d31f4e4701d
New Trace       0e65e196-ac0 Complete         1                            Fri Nov  6 15:04:48  Fri Nov  6 15:05
                5-49d7-8c81-                                               2020                 :03 2020
                6e6691e191ae
Svr01toSvr04Hrl 4c580c97-8af Complete         0                            Fri Nov  6 15:01:16  Fri Nov  6 15:01
y               8-4ea2-8c09-                                               2020                 :44 2020
                038cde9e196c
Abc             c7174fad-71c Complete         1                            Fri Nov  6 14:57:18  Fri Nov  6 14:58
                a-49d3-8c1d-                                               2020                 :11 2020
                67962039ebf9
Lf01toBor01Dail f501f9b0-cca Complete         0                            Fri Nov  6 14:52:35  Fri Nov  6 14:57
y               3-4fa1-a60d-                                               2020                 :55 2020
                fb6f495b7a0e
L01toB01Daily   38a75e0e-7f9 Complete         0                            Fri Nov  6 14:50:23  Fri Nov  6 14:57
                9-4e0c-8449-                                               2020                 :38 2020
                f63def1ab726
leaf01toborder0 f8d6a2c5-54d Complete         0                            Fri Nov  6 14:34:54  Fri Nov  6 14:57
1               b-44a8-9a5d-                                               2020                 :20 2020
                9d31f4e4701d
leaf01toborder0 f8d6a2c5-54d Complete         0                            Fri Nov  6 14:04:54  Fri Nov  6 14:05
1               b-44a8-9a5d-                                               2020                 :20 2020
                9d31f4e4701d
New Trace       0e65e196-ac0 Complete         1                            Fri Nov  6 14:04:48  Fri Nov  6 14:05
                5-49d7-8c81-                                               2020                 :02 2020
                6e6691e191ae
Svr01toSvr04Hrl 4c580c97-8af Complete         0                            Fri Nov  6 14:01:16  Fri Nov  6 14:01
y               8-4ea2-8c09-                                               2020                 :43 2020
                038cde9e196c
...
L01toB01Daily   38a75e0e-7f9 Complete         0                            Thu Nov  5 15:50:23  Thu Nov  5 15:58
                9-4e0c-8449-                                               2020                 :22 2020
                f63def1ab726
leaf01toborder0 f8d6a2c5-54d Complete         0                            Thu Nov  5 15:34:54  Thu Nov  5 15:58
1               b-44a8-9a5d-                                               2020                 :03 2020
                9d31f4e4701d
```

### View Scheduled Trace Settings for a Given Trace

You can view the configuration settings used by a give scheduled trace using the `netq show trace settings` command.

This example shows the settings for the scheduled trace named *Lf01toBor01Daily*.

```
cumulus@switch:~$ netq show trace settings name Lf01toBor01Daily
```

### View Scheduled Trace Results for a Given Trace

You can view the results for a give scheduled trace using the `netq show trace results` command.

This example obtains the job ID for the trace named *Lf01toBor01Daily*, then shows the results.

```
cumulus@switch:~$ netq show trace summary name Lf01toBor01Daily json
cumulus@switch:~$ netq show trace results f501f9b0-cca3-4fa1-a60d-fb6f495b7a0e
```

{{</tab>}}

{{</tabs>}}

## Modify a Scheduled Trace

You can modify scheduled traces at any time as described below. An administrator can also manage scheduled traces through the NetQ management dashboard.

{{%notice note%}}

Be aware that changing the configuration of a trace can cause the results to be inconsistent with prior runs of the trace. If this is an unacceptable result, create a new scheduled trace. Optionally you can remove the original trace.

{{%/notice%}}

To modify a scheduled trace:

1. Open the Trace Request card.

2. Select the trace from the **New trace request** dropdown.

3. Edit the schedule, VLAN, or VRF and select **Update**.

4. From the confirmation dialog, click **Yes** to complete the changes or select the link to change the name of the previous version of this scheduled trace.

    The validation can now be selected from the New Trace listing and run immediately by selecting **Go** or **Run now**. Alternately, you can wait for it to run the first time according to the schedule you specified.

## Remove Scheduled Traces

If you have reached the maximum of 15 scheduled traces for your premises, you will need to remove traces to create additional ones.
{{%notice note%}}

Both a standard user and an administrative user can remove scheduled traces. No notification is generated on removal. Be sure to communicate with other users before removing a scheduled trace to avoid confusion and support issues.

{{%/notice%}}

{{<tabs "TabID1372" >}}

{{<tab "NetQ UI" >}}

1. Open the Trace Request card and expand the card to the largest size.

2. Select one or more traces.

3. Above the table, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} **Delete**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

1. Find the name of the scheduled trace you want to remove:

    ```
    netq show trace summary [name <text-trace-name>] [around <text-time-hr>] [json]
    ```

    The following example shows all scheduled traces in JSON format:

    ```
    cumulus@switch:~$ netq show trace summary json
    [
        {
            "job_end_time": 1605300327131,
            "job_req_time": 1604424893944,
            "job_start_time": 1605300318198,
            "jobid": "f8d6a2c5-54db-44a8-9a5d-9d31f4e4701d",
            "status": "Complete",
            "status_details": "1",
            "trace_name": "leaf01toborder01",
            "trace_params": {
                "alert_on_failure": "0",
                "dst": "10.10.10.63",
                "src": "10.10.10.1",
                "vlan": "-1",
                "vrf": ""
            }
        },
        {
            "job_end_time": 1605300237448,
            "job_req_time": 1604424893944,
            "job_start_time": 1605300206939,
            "jobid": "f8d6a2c5-54db-44a8-9a5d-9d31f4e4701d",
            "status": "Complete",
            "status_details": "1",
            "trace_name": "leaf01toborder01",
            "trace_params": {
                "alert_on_failure": "0",
                "dst": "10.10.10.63",
                "src": "10.10.10.1",
                "vlan": "-1",
                "vrf": ""
            }
        },
        {
            "job_end_time": 1605300223824,
            "job_req_time": 1604599038706,
            "job_start_time": 1605300206930,
            "jobid": "c7174fad-71ca-49d3-8c1d-67962039ebf9",
            "status": "Complete",
            "status_details": "1",
            "trace_name": "Abc",
            "trace_params": {
                "alert_on_failure": "1",
                "dst": "27.0.0.2",
                "src": "27.0.0.1",
                "vlan": "-1",
                "vrf": ""
            }
        },
        {
            "job_end_time": 1605300233045,
            "job_req_time": 1604519423182,
            "job_start_time": 1605300206930,
            "jobid": "38a75e0e-7f99-4e0c-8449-f63def1ab726",
            "status": "Complete",
            "status_details": "1",
            "trace_name": "L01toB01Daily",
            "trace_params": {
                "alert_on_failure": "0",
                "dst": "10.10.10.63",
                "src": "10.10.10.1",
                "vlan": "-1",
                "vrf": ""
            }
        },
    ...
    ```

2. To remove the trace, run:

    ```
    netq del trace <text-trace-name>
    ```

    This example removes the *leaf01toborder01* trace.

    ```
    cumulus@switch:~$ netq del trace leaf01toborder01
    Successfully deleted schedule trace leaf01toborder01
    ```

3. Repeat these steps to remove additional traces.

{{</tab>}}

{{</tabs>}}
