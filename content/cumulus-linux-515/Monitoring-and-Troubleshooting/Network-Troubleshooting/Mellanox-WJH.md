---
title: What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
*What Just Happened* (WJH) provides real time visibility into network problems and has two components:
- The WJH agent enables you to stream detailed and contextual telemetry for off-switch analysis with tools such as {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq" text="NVIDIA NetQ" >}}.
- The WJH service (`what-just-happened`) enables you to diagnose network problems by looking at dropped packets. WJH can monitor layer 1, layer 2, layer 3, tunnel, buffer and ACL related issues. Cumulus Linux enables and runs the WJH service by default.

{{%notice note%}}
WJH runs in Docker. If you exhaust the Docker ten percent global limit of overall resources, then start WJH, you might see issues when using WJH. Make sure to free up Docker resources, then launch WJH again.
{{%/notice%}}

## Configure WJH

You can choose which packet drops you want to monitor by creating channels and setting the packet drop categories (layer 1, layer 2, layer 3, tunnel, buffer and ACL) you want to monitor.

{{< tabs "TabID24 ">}}
{{< tab "NVUE Commands ">}}

The following example configures two separate channels:
- The `forwarding` channel monitors layer 2, layer 3, and tunnel packet drops.
- The `layer-1` channel monitors layer 1 packet drops.

```
cumulus@switch:~$ nv set system wjh channel forwarding trigger l2
cumulus@switch:~$ nv set system wjh channel forwarding trigger l3
cumulus@switch:~$ nv set system wjh channel forwarding trigger tunnel
cumulus@switch:~$ nv set system wjh channel layer-1 trigger l1
cumulus@switch:~$ nv config apply
```

The following example configures a channel to monitor buffer packet drops and a channel to monitor ACL packet drops:

```
cumulus@switch:~$ nv set system wjh channel buffer trigger buffer
cumulus@switch:~$ nv set system wjh channel acl trigger acl
cumulus@switch:~$ nv config apply
```

You can stop monitoring specific packet drops by unsetting a category in the channel list. The following command example stops monitoring layer 2 packet drops that are in the `forwarding` channel:

```
cumulus@switch:~$ nv unset system wjh channel forwarding trigger l2
cumulus@switch:~$ nv config apply
```

To remove a channel, run the `nv unset system wjh channel <channel>` command. The following command example removes the `layer-1` channel:

```
cumulus@switch:~$ nv unset system wjh channel layer-1 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/what-just-happened/what-just-happened.json` file:
- For each drop category you want to monitor, include the drop category value inside the square brackets ([]). 
- For each drop category you do **not** want to monitor, remove the drop category value from inside the square brackets.

After you edit the file, you must restart the WJH service with the `sudo systemctl restart what-just-happened` command.

The following example configures a channel to monitor layer 2, layer 3, and tunnel packet drops and a channel to monitor layer 1 packet drops.

```
cumulus@switch:~$ sudo nano /etc/what-just-happened/what-just-happened.json
{
    "what-just-happened": {
        "channels": {
            "forwarding": {
                "drop_category_list": [
                    "l2",
                    "l3",
                    "tunnel"
                ]
            },
            "layer-1": {
                "drop_category_list": [
                    "l1"
                ]
            }
        }
    }
}
```

```
cumulus@switch:~$ sudo systemctl restart what-just-happened
```

The following example configures a channel to monitor buffer packet drops and a channel to monitor ACL packet drops.

```
cumulus@switch:~$ sudo nano /etc/what-just-happened/what-just-happened.json
{
    "what-just-happened": {
        "channels": {
            "buffer": {
                "drop_category_list": ["buffer"]
            },
            "acl": {
                "drop_category_list": ["acl"]
            }
        }
    }
}
```

```
cumulus@switch:~$ sudo systemctl restart what-just-happened
```

{{< /tab >}}
{{< /tabs >}}

## Show Information about Dropped Packets

You can run the following commands to show information about dropped packets and diagnose problems.

{{< tabs "TabID76 ">}}
{{< tab "NVUE Commands ">}}

To show information about packet drops for all the channels you configure, run the `nv show system wjh packet-buffer ` command. The command output includes the reason for the drop and the recommended action to take.

You can also show the WJH configuration on the switch:
- To show the configuration for a channel, run the `nv show system wjh channel <channel>` command. For example, `nv show system wjh channel forwarding`.
- To show the configuration for packet drop categories in a channel, run the `nv show system wjh channel <channel> trigger` command. For example, `nv show system wjh channel forwarding trigger`.

The following example shows information about layer 1 packet drops:

```
cumulus@switch:~$ nv show system wjh packet-buffer
#   dMAC  dPort  Dst IP:Port  EthType  Drop group  IP Proto  Drop reason - Recommended action                         Severity  sMAC  sPort    Src IP:Port  Timestamp              VLAN
--  ----  -----  -----------  -------  ----------  --------  -------------------------------------------------------  --------  ----  -------  -----------  ---------------------  ----
1   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp17    N/A          22/11/03 01:00:35.458  N/A
2   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp18    N/A          22/11/03 01:00:35.458  N/A
3   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp19    N/A          22/11/03 01:00:35.458  N/A
4   N/A   N/A    N/A          N/A      L1          N/A       Generic L1 event - Check layer 1 aggregated information  Warn      N/A   swp20    N/A          22/11/03 01:00:35.458  N/A
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You can run the following commands from the command line.

| <div style="width:450px">Command  | Description |
| -------  | ----------- |
| `what-just-happened poll` | Shows information about packet drops for all the channels you configure. The output includes the reason for the drop and the recommended action to take.<br><br>The `what-just-happened poll <channel>` command shows information for the channel you specify. |
| `what-just-happened poll --aggregate` | Shows information about dropped packets aggregated by the reason for the drop. This command also shows the number of times the dropped packet occurs.<br><br>The `what-just-happened poll <channel> --aggregate` command shows information for the channel you specify. |
| `what-just-happened poll --export` | Saves information about dropped packets to a file in PCAP format.<br><br>The `what-just-happened poll <channel> --export` command saves information for the channel you specify. |
| `what-just-happened poll --export --no_metadata` | Saves information about dropped packets to a file in PCAP format without metadata.<br><br> The `what-just-happened poll <channel> --export --no_metadata` command saves information for the channel you specify.|
| `what-just-happened dump` | Displays all diagnostic information on the command line. |

Run the `what-just-happened -h` command to see all the WJH command options.

To show all dropped packets and the reason for the drop, run the NVUE `nv show system wjh packet-buffer` command or the `what-just-happened poll` command.

The following example shows that packets drop five times because the source MAC address equals the destination MAC address:

```
cumulus@switch:~$ what-just-happened poll --aggregate
Sample Window : 2021/06/16 12:57:23.046 - 2021/06/16 14:46:17.701

#  sPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Count  Severity  Drop reason - Recommended action
-- ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1  swp4   N/A   44:38:39:00:a4:87  44:38:39:00:a4:87  IPv4     0.0.0.0:0    0.0.0.0:0    ip        100    Error     Source MAC equals destination MAC - Bad packet was received from peer
2  swp1   N/A   44:38:39:00:a4:80  44:38:39:00:a4:80  IPv4     0.0.0.0:0    0.0.0.0:0    ip        100    Error     Source MAC equals destination MAC - Bad packet was received from peer
```

The following command saves dropped packets to a file in PCAP format

```
cumulus@switch:~$ what-just-happened poll --export --no_metadata
PCAP file path : /var/log/mellanox/wjh/wjh_user_2021_06_16_12_03_15.pcap

#    Timestamp              sPort  dPort  VLAN  sMAC               dMAC               EthType  Src IP:Port  Dst IP:Port  IP Proto  Drop   Severity  Drop reason - Recommended action
                                                                                                                                   Group
---- ---------------------- ------ ------ ----- ------------------ ------------------ -------- ------------ ------------ --------- ------ --------- -----------------------------------------------
1    21/06/16 12:03:12.728  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet as received from peer
2    21/06/16 12:03:12.728  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
3    21/06/16 12:03:12.745  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
4    21/06/16 12:03:12.745  swp1   N/A    N/A   44:38:39:00:a4:84  44:38:39:00:a4:84  IPv4     N/A          N/A          N/A       L2     Error     Source MAC equals destination MAC - Bad packet was received from peer
```

{{< /tab >}}
{{< /tabs >}}

## WJH Metrics

This section provides the supported WJH metrics with a brief description of each.

### Layer 1 Drops

Layer 1 drop metrics describe why a port is in the down state.

| Reason | Description|
| --- | --- |
| Auto-negotiation failure | Port speed negotiation with the peer failed. |
| Logical mismatch with peer link | Logical mismatch with the peer link. |
| Link training failure | The link is not able to go operational up due to link training failure. |
| Peer is sending remote faults | The peer node is not operating correctly. |
| Bad signal integrity | The integrity of the signal on the port is not sufficient for good communication. |
| Cable/transceiver is not supported | The port does not support the attached cable or transceiver.|
| Cable/transceiver is unplugged | A cable or transceiver is missing or not fully inserted into the port. |
| Calibration failure | Calibration failure. |
| Port state changes counter | The cumulative number of state changes. |
| Symbol error counter | The cumulative number of symbol errors. |
| CRC error counter | The cumulative number of CRC errors. |

In addition to the reason, the information provided for these drops includes:

| Parameter | Description |
| --- | --- |
| Corrective Action | Recommended actions to resolve the port down state. |
| First Timestamp | The date and time the port was marked as down for the first time. |
| Ingress Port | The port accepting incoming traffic. |
| CRC Error Count | The number of CRC errors that this port generated. |
| Symbol Error Count | The number of Symbol errors that this port generated. |
| State Change Count | The number of state changes on this port. |
| OPID | Operation identifier; for internal purposes. |
| Is Port Up | Indicates if the port is in an Up (true) or Down (false) state. |

### Layer 2 Drops

Layer 2 drop metrics describe why a link is down.

| Reason | Severity | Description |
| --- | --- | --- |
| MLAG port isolation | Notice | Not supported for port isolation implemented with the system ACL. |
| Destination MAC is reserved (DMAC=01-80-C2-00-00-0x) | Error | The link cannot use the MAC address. |
| VLAN tagging mismatch | Error | The source and destination VLAN tags do not match. |
| Ingress VLAN filtering | Error | Frames whose port is not a member of the VLAN are discarded. |
| Ingress spanning tree filter | Notice | The port is in a Spanning Tree blocking state. |
| Unicast MAC table action discard | Notice | The packet is dropped due to a MAC table configuration rule. |
| Multicast egress port list is empty | Warning | No ports are defined for multicast egress. |
| Port loopback filter | Error | The port is operating in loopback mode; packets are being sent to itself (source MAC address is the same as the destination MAC address). |
| Source MAC is multicast | Error | Packets have a multicast source MAC address. |
| Source MAC equals destination MAC | Error | The source MAC address is the same as the destination MAC address. |

In addition to the reason, the information provided for these drops includes:

| Parameter | Description|
| --- | --- |
| Source Port | The port ID where the link originates. |
| Source IP | The port IP address where the link originates. |
| Source MAC | The port MAC address where the link originates. |
| Destination Port | The port ID where the link terminates. |
| Destination IP | The port IP address where the link terminates. |
| Destination MAC | The port MAC address where the link terminates. |
| First Timestamp | The date and time this link is marked as down for the first time. |
| Aggregate Count  | The total number of dropped packets. |
| Protocol | The ID of the communication protocol running on this link. |
| Ingress Port | The port accepting incoming traffic. |
| OPID | The operation identifier; for internal purposes. |

### Router Drops

Router drop metrics describe why the server is unable to route a packet.

| Reason | Severity | Description |
| --- | --- | --- |
| Non-routable packet |  Notice | The packet has no route in the routing table. |
| Blackhole route | Warning | The packet was received with an action equal to discard. |
| Unresolved next hop | Warning | The next hop in the route is unknown. |
| Blackhole ARP/neighbor | Warning | The packet was received with a blackhole adjacency. |
| IPv6 destination in multicast scope FFx0:/16 | Notice | The packet was received with a multicast destination address in FFx0:/16 address range. |
| IPv6 destination in multicast scope FFx1:/16 | Notice | The packet was received with a multicast destination address in FFx1:/16 address range. |
| Non-IP packet | Notice | Cannot read the packet header because it is not an IP packet. |
| Unicast destination IP but non-unicast destination MAC | Error | Cannot read the packet with the IP unicast address when the destination MAC address is not unicast (FF:FF:FF:FF:FF:FF). |
| Destination IP is loopback address | Error | Cannot read the packet because the destination IP address is a loopback address (dip=>127.0.0.0/8). |
| Source IP is multicast | Error | Cannot read the packet because the source IP address is a multicast address (ipv4 SIP => 224.0.0.0/4). |
| Source IP is in class E | Error | Cannot read the packet because the source IP address is a Class E address. |
| Source IP is loopback address | Error | Cannot read the packet because the source IP address is a loopback address (ipv4 => 127.0.0.0/8 for ipv6 => ::1/128). |
| Source IP is unspecified | Error | Cannot read the packet because the source IP address is unspecified (ipv4 = 0.0.0.0/32; for ipv6 = ::0). |
| Checksum or IP ver or IPv4 IHL too short | Error | Cannot read the packet due to a header checksum error or IP version mismatch, or because the IPv4 header length is too short. |
| Multicast MAC mismatch |  Error | For IPv4, the destination MAC address is not equal to {0x01-00-5E-0 (25 bits), DIP\[22:0\]} and the DIP is multicast. For IPv6, the destination MAC address is not equal to {0x3333, DIP\[31:0\]} and the DIP is multicast. |
| Source IP equals destination IP | Error | The packet has a source IP address equal to the destination IP address. |
| IPv4 source IP is limited broadcast | Error | The packet has a broadcast source IP address. |
| IPv4 destination IP is local network (destination = 0.0.0.0/8) | Error | The packet has an IPv4 destination address that is a local network (destination=0.0.0.0/8). |
| IPv4 destination IP is link-local (destination in 169.254.0.0/16) | Error | The packet has an IPv4 destination address that is a local link. |
| Ingress router interface is disabled | Warning | The packet is destined to a different subnet but cannot be routed because the ingress router interface is disabled. |
| Egress router interface is disabled | Warning | The packet is destined to a different subnet but cannot be routed because the egress router interface is disabled. |
| IPv4 routing table (LPM) unicast miss | Warning | There is no route available in the routing table for the packet. |
| IPv6 routing table (LPM) unicast miss | Warning | There is no route available in the routing table for the packet. |
| Router interface loopback | Warning | The packet has a destination IP address that is local. For example, SIP = 1.1.1.1, DIP = 1.1.1.128. |
| Packet size is larger than MTU | Warning | The packet has a larger MTU configured than the VLAN. |
| TTL value is too small | Warning | The packet has a TTL value of 1. |

### Tunnel Drops

Tunnel drop metrics describe why a tunnel is down.

| Reason | Severity | Description |
| --- | --- | --- |
| Overlay switch - source MAC is multicast | Error | The source MAC address of the overlay packet is multicast. |
| Overlay switch - source MAC equals destination MAC | Error | The source MAC address of the overlay packet is the same as the destination MAC address. |
| Decapsulation error | Error | Decapsulation produced an incorrect format for the packet. For example, encapsulation of a packet with many VLANs or IP options on the underlay can cause decapsulation to result in a short packet. |
| Tunnel interface is disabled | Error | The packet cannot decapsulate because the tunnel interface is disabled. |

### Buffer Drops

Buffer drop metrics describe why the server buffer has dropped packets.

| Reason | Severity | Description |
| --- | --- | --- |
| Tail drop | Warning | Tail drop is enabled and the buffer queue is filled to maximum capacity. |
| WRED | Warning | Weighted Random Early Detection is enabled and the buffer queue is filled to maximum capacity or the RED engine dropped the packet as a random congestion prevention. |
| Port TC Congestion Threshold Crossed | Warning | The percentage of the occupancy buffer exceeded or dropped below the specified high or low threshold. |
| Packet Latency Threshold Crossed | Warning | The time a packet spent within the switch exceeded or dropped below the specified high or low threshold. |

### ACL Drops

ACL drop metrics describe why an ACL has dropped packets.

| Reason | Severity | Description|
| --- | --- | --- |
| Ingress port ACL | Notice | An ACL action is set to deny on the physical ingress port or bond. |
| Ingress router ACL | Notice | An ACL action is set to deny on the ingress switch virtual interfaces (SVIs). |
| Egress port ACL | Notice | An ACL action is set to deny on the physical egress port or bond. |
| Egress router ACL | Notice | An ACL action is set to deny on the egress SVIs. |

## Considerations

### Buffer Packet Drop Monitoring

- Buffer packet drop monitoring is available on a switch with Spectrum-2 and later.
- Buffer packet drop monitoring uses a SPAN destination. If you configure SPAN, ensure that you do not exceed the total number of SPAN destinations allowed for your switch ASIC type; see {{<link url="SPAN-and-ERSPAN/#limitations" text="SPAN and ERSPAN">}}. If you need to remove the SPAN destination that buffer packet drop monitoring uses, delete the buffer monitoring drop category either with the NVUE `nv unset system wjh channel buffer trigger buffer` command or by editing the `/etc/what-just-happened/what-just-happened.json` file and reloading the `what-just-happened` service.

### Cumulus Linux and Docker

WJH runs in a Docker container. By default, when Docker starts, it creates a bridge called `docker0`. However, for compatibility reasons Cumulus Linux disables the `docker0` bridge in the `/etc/docker/daemon.json` file with the attribute `"bridge: none"`.

### WJH and the NVIDIA NetQ Agent

When you enable the NVIDIA NetQ agent on the switch, the WJH service stops and does not run. If you disable the NVIDIA NetQ service and want to use WJH, run the following commands to enable and start the WJH service:

{{< tabs "TabID14 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set system wjh enable on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo systemctl enable what-just-happened
cumulus@switch:~$ sudo systemctl start what-just-happened
```

{{< /tab >}}
{{< /tabs >}}
