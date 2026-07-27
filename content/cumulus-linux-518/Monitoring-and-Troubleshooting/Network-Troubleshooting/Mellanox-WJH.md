---
title: What Just Happened (WJH)
author: NVIDIA
weight: 1130
toc: 4
---
*What Just Happened* (WJH) provides real time visibility into network problems and has two components:
- The WJH agent (`nv-wjh.service`) enables you to stream detailed and contextual telemetry for off-switch analysis with tools such as {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-netq" text="NVIDIA NetQ" >}}.
- The WJH service enables you to diagnose network problems by looking at dropped packets. WJH can monitor layer 1, layer 2, layer 3, tunnel, buffer and ACL related issues. Cumulus Linux enables and runs the WJH service by default.

{{%notice note%}}
In Cumulus Linux 5.18 and later, the WJH agent is `nv-wjh.service`. In Cumulus Linux 5.17 and earlier, the WJH agent is `what-just-happened.service`.
{{%/notice%}}

## Configure WJH

You can choose which packet drops you want to monitor by creating channels and setting the packet drop categories (layer 1, layer 2, layer 3, tunnel, buffer and ACL) you want to monitor.

{{%notice note%}}
- A channel name must be between 4 and 16 characters long.
- You can enable each trigger for a single channel only.
{{%/notice%}}

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
cumulus@switch:~$ nv set system wjh channel acl1 trigger acl
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

### Filter Traffic Drops

You can filter traffic drops to prevent them from being monitored based on the reason for the drop, the severity level (error, warning, or notice), or IP address.

The following table shows the drop reasons on which you can filter:

| Traffic Drop Type | Drop Reasons |
| ----------------- | ------------ |
| ACL |egress-cpu-port-acl<br> egress-tunnel-acl<br>ingress-router-acl<br>egress-port-acl<br>ingress-cpu-port-acl<br>ingress-tunnel-acl<br>egress-router-acl<br>ingress-port-acl<br>multi-points-acl |
| Buffer | packet-latency-threshold-crossed<br>tail-drop<br>port-tc-congestion-threshold-crossed<br>wred |
| l2 |dest-mac-is-reserved<br>source-mac-is-multicast<br>ingress-spanning-tree-filter<br>source-mac-is-zero<br>ingress-vlan-filtering<br>unicast-egress-port-list-is-empty<br>mlag-port-isolation<br>unicast-mac-table-action-discard<br>multicast-egress-port-list-is-empty<br>vlan-or-vni-lookup-failed<br>port-loopback-filter<br>vlan-tagging-mismatch<br>source-mac-equals-dest-mac |
| l3 | blackhole-arp<br>blackhole-route<br>checksum-or-ipver-or-ipv4-ihl-too-short<br>dest-ip-is-loopback-addr<br>egress-router-intf-is-disabled<br>ingress-router-intf-is-disabled<br>ipv4-dest-ip-is-link-local<br>ipv4-dest-ip-is-local-network<br>ipv4-routing-table-unicast-miss<br>ipv4-src-ip-is-limited-broadcast<br>ipv6-dest-in-multicast-scope-ffx0<br>ipv6-dest-in-multicast-scope-ffx1<br>ipv6-routing-table-unicast-miss<br>multicast-mac-mismatch<br>non-ip-packet<br>non-routable-pck<br>packet-size-is-larger-than-router-intf-mtu<br>packet-source-ip-cant-be-verified<br>router-interface-loopback<br>src-ip-equals-dest-ip<br>src-ip-is-in-class-e<br>src-ip-is-loopback-addr<br>src-ip-is-multicast<br>src-ip-is-unspecified<br>ttl-value-is-too-small<br>unicast-dest-ip-but-multicast-dest-mac<br>unresolved-neighbor |
| Tunnel |decapsulation-error<br>encapsulation-port-isolation<br>overlay-switch-src-mac-equals-dest-mac<br>overlay-switch-src-mac-equals-zero<br>overlay-switch-src-mac-is-multicast |

To filter traffic drops due to a specific reason, run the `nv set system wjh channel <channel-id> drop-filter <filter-id> drop-type <type> drop-reason <reason>` command.

To filter traffic drops due to a specific severity, run the `nv set system wjh channel <channel-id> drop-filter <filter-id> drop-type <type> severity <severity-level>` command.

To filter traffic drops with a specific IP address, run the `nv set system wjh channel <channel-id> drop-filter <filter-id> ip <ip-address>` command.
- The `<channel-id>` is the channel name.
- The `<filter-id>` is name you want to provide for the filter.
- The `<type>` is `acl`, `buffer`, `l2`, `l3`, or `tunnel`.
- The `<reason>` can be any reason listed in the table above.

The following example creates a filter called TUNNEL1 that prevents traffic drops from being monitored because the overlay switch source MAC equals the destination MAC:

```
cumulus@switch:~$ nv set system wjh channel forwarding drop-filter TUNNEL1 drop-type tunnel drop-reason overlay-switch-src-mac-equals-dest-mac
cumulus@switch:~$ nv config apply
```

The following example creates a filter called SEVERITY that prevents layer 2 traffic drops from being monitored with the severity level notice:

```
cumulus@switch:~$ nv set system wjh channel forwarding drop-filter SEVERITY drop-type l2 severity notice
cumulus@switch:~$ nv config apply
```

The following example creates a filter called IP-DROPS that prevents traffic drops with the IP address 10.10.10.10 from being monitored:

```
cumulus@switch:~$ nv set system wjh channel forwarding drop-filter IP-DROPS ip 10.10.10.10
cumulus@switch:~$ nv config apply
```

To unset a traffic drop filter, run the `nv set system wjh channel <channel-id> drop-filter <filter-id>` command.

To show traffic drop filter configuration, run the `nv show system wjh channel <channel-id> drop-filter` command.

```
cumulus@switch:~$ nv show system wjh channel forwarding drop-filter
```

### Aggregation Interval and Cache Size

You can control the rate at which the switch sends events for a channel (the polling interval) and the number of WJH drops and aggregates to maintain in the cache (the aggregate cache size).

The polling interval for a channel can be between 5 and 300 seconds and the cache size between 500 and 5000.

The following example sets the aggregation interval for the forwarding channel to 100 seconds and the cache size to 1000:

```
cumulus@switch:~$ nv set system wjh channel forwarding polling-interval 100
cumulus@switch:~$ nv set system wjh channel forwarding aggregate-cache-size 1000
cumulus@switch:~$ nv config apply
```

- To unset the aggregation interval for a channel, run the `nv unset system wjh channel <channel-id> polling-interval` command.
- To unset the aggregate cache size, run the `nv unset system wjh channel <channel-id> aggregate-cache-size` command.

### Latency and Congestion Thresholds

If you configure a channel to monitor buffer packet drops, you can specify latency and congestion thresholds to apply to buffer drops for all or specific traffic classes and interfaces. WJH collects and sends events when a metric crosses the thresholds.
- Packet latency is the time spent in the switch.
- Congestion is a percentage of the buffer occupancy on the switch.

{{%notice note%}}
The Spectrum-6 switch does not support latency thresholds.
{{%/notice%}}

The following example sets the latency threshold to 10 seconds for all traffic classes on ports swp1, swp2, and swp3 and the congestion threshold to 4 for traffic class 3 on all interfaces.

```
cumulus@switch:~$ nv set system wjh channel forwarding buffer-threshold latency tc all interface swp1-3 high 100
cumulus@switch:~$ nv set system wjh channel forwarding buffer-threshold congestion tc 3 interface all high 4
cumulus@switch:~$ nv config apply
```

- To unset the packet latency threshold, run the `nv unset system wjh channel <channel-id> buffer-threshold latency` command.
- To unset the packet congestion threshold, run the `nv unset system wjh channel <channel-id> buffer-threshold congestion` command.

To show the latency and congestion threshold configuration, run the `nv show system wjh channel <channel-id> buffer-threshold` command:

```
cumulus@switch:~$ nv show system wjh channel buffer buffer-threshold
Latency buffer threshold
===========================
    Traffic Class  Interface  High threshold
    -------------  ---------  --------------
    all            all        1000

Congestion buffer threshold
==============================
    Traffic Class  Interface  High threshold
    -------------  ---------  --------------
    all            swp1       20
                   swp2       20
                   swp3       20
```

## Save Dropped Packets to a PCAP File

To save the most recent dropped packets to a PCAP file, run the `nv action export system wjh packet-buffer` command. The switch writes PCAP files to the `/var/run/nv-wjh/` directory with a timestamped filename that the system chooses.

```
cumulus@switch:~$ nv action export system wjh packet-buffer
```

To exclude metadata in the file, add `no-metadata` to the command:

```
cumulus@switch:~$ nv action export system wjh packet-buffer no-metadata
```

## Show Information about Dropped Packets

You can run the following commands to show information about dropped packets and diagnose problems.

{{< tabs "TabID76 ">}}
{{< tab "NVUE Commands ">}}

To show information about packet drops for all the channels you configure, run the `nv show system wjh packet-buffer` command. The command output includes the reason for the drop and the recommended action to take.

```
cumulus@switch:~$ nv show system wjh packet-buffer
Packet
=========
    #     dMAC               dPort  Dst IP:Port    EthType  Drop group  IP Proto  Drop reason - Recommended action                                            Severity  sMAC               sPort   Src IP:Port     Timestamp              VLAN  sLAG  dLAG
    ----  -----------------  -----  -------------  -------  ----------  --------  --------------------------------------------------------------------------  --------  -----------------  ------  --------------  ---------------------  ----  ----  ----
    1     2c:5e:ab:a5:ae:f0  N/A    10.1.2.3:200   IPv4     ACL         N/A       Ingress port ACL - Validate ACL configuration                               Notice    00:02:00:00:00:01  swp1s0  192.0.2.10:100  26/07/03 12:46:29.238  N/A   N/A   N/A 
    2     02:03:04:05:06:07  N/A    10.2.3.4:200   IPv4     L2          N/A       Port loopback filter - Validate MAC table for this destination MAC          Error     00:02:00:00:00:01  swp1s0  224.0.0.1:100   26/07/03 12:46:29.238  N/A   N/A   N/A 
    3     2c:5e:ab:a5:ae:f0  N/A    10.1.2.3:200   IPv4     L2          N/A       Source MAC is Zero - Bad packet was received from peer                      Error     00:00:00:00:00:00  swp1s0  10.1.2.3:100    26/07/03 12:46:29.238  N/A   N/A   N/A 
    4     02:03:04:05:06:07  N/A    127.0.0.1:200  IPv4     L2          N/A       Port loopback filter - Validate MAC table for this destination MAC          Error     00:02:00:00:00:01  swp1s0  224.0.0.1:100   26/07/03 12:46:29.238  N/A   N/A   N/A 
    5     02:03:04:05:06:07  N/A    10.1.2.3:200   IPv4     L2          N/A       Port loopback filter - Validate MAC table for this destination MAC          Error     00:02:00:00:00:01  swp1s0  10.1.2.3:100    26/07/03 12:46:29.238  N/A   N/A   N/A 
    6     2c:5e:ab:a5:ae:f0  N/A    10.1.2.3:200   IPv4     L3          N/A       Source IP equals destination IP - Bad packet was received from the peer     Error     00:02:00:00:00:01  swp1s0  10.1.2.3:100    26/07/03 12:46:29.238  N/A   N/A   N/A 

Packet ACL
=============
    #     Rule                                                                                                                                                                    
    ----  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    1     Priority[0];KEY[L3_TYPE: IPV4];KEY[SIP: 192.0.2.10/255.255.255.255];KEY[SRC_PORT: 65777];ACTION[COUNTER: COUNTER_ID = 614400];ACTION[FORWARD: FORWARD_ACTION = DISCARD];

Packet Buffer Info
=====================
No Data
```

To show the most recent aggregate buffer drop events, up to the maximum aggregate cache size specified, run the `nv show system wjh aggregate-buffer` command. 

```
cumulus@switch:~$ nv show system wjh aggregate-buffer
Aggregate Event
==================
    Event ID  Drop group  Count  Severity  Drop reason - Recommended action                                            Start timestamp        End timestamp          sPort   sLAG  dPort  dLAG  VLAN  sMAC               dMAC               EthType  Src IP:Port     Dst IP:Port    IP Proto
    --------  ----------  -----  --------  --------------------------------------------------------------------------  ---------------------  ---------------------  ------  ----  -----  ----  ----  -----------------  -----------------  -------  --------------  -------------  --------
    1         L3          30     Error     Destination IP is loopback address - Bad packet was received from the peer  26/07/03 10:29:38.281  26/07/03 10:30:07.287  swp1s0  N/A   N/A    N/A   N/A   00:02:00:00:00:01  2c:5e:ab:a5:ae:f0  IPv4     10.1.2.3:100    127.0.0.1:200  udp     
    2         L2          30     Error     Source MAC is Zero - Bad packet was received from peer                      26/07/03 10:29:38.281  26/07/03 10:30:07.287  swp1s0  N/A   N/A    N/A   N/A   00:00:00:00:00:00  2c:5e:ab:a5:ae:f0  IPv4     10.1.2.3:100    10.1.2.3:200   udp     
    3         L2          30     Error     Port loopback filter - Validate MAC table for this destination MAC          26/07/03 10:29:38.281  26/07/03 10:30:07.287  swp1s0  N/A   N/A    N/A   N/A   00:02:00:00:00:01  02:03:04:05:06:07  IPv4     10.1.2.3:100    10.1.2.3:200   udp     
    4         L2          30     Error     Port loopback filter - Validate MAC table for this destination MAC          26/07/03 10:29:38.281  26/07/03 10:30:07.287  swp1s0  N/A   N/A    N/A   N/A   00:02:00:00:00:01  02:03:04:05:06:07  IPv4     224.0.0.1:100   10.2.3.4:200   udp     
    5         ACL         33     Notice    Ingress port ACL - Validate ACL configuration                               26/07/03 10:29:35.280  26/07/03 10:30:07.287  swp1s0  N/A   N/A    N/A   N/A   00:02:00:00:00:01  2c:5e:ab:a5:ae:f0  IPv4     192.0.2.10:100  10.1.2.3:200   udp  

Aggregate Event ACL
======================
    Event ID  Rule                                                                                                                                                                    
    --------  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    5         Priority[0];KEY[L3_TYPE: IPV4];KEY[SIP: 192.0.2.10/255.255.255.255];KEY[SRC_PORT: 65777];ACTION[COUNTER: COUNTER_ID = 614400];ACTION[FORWARD: FORWARD_ACTION = DISCARD];

Aggregate Event Buffer
=========================
No Data
```

To show layer 1 buffer events, run the `nv show system wjh l1-buffer` command.

```
cumulus@switch:~$ nv show system wjh l1-buffer
Event ID  Port   State  Port down reason                Start timestamp        End timestamp          State change count  Symbol error count  CRC error count
--------  -----  -----  ------------------------------  ---------------------  ---------------------  ------------------  ------------------  ---------------
1         swp1   Up     N/A                             26/07/23 15:31:53.848  26/07/23 15:47:45.628  1                   0                   0
2         swp10  Down   Cable/transceiver is unplugged  26/07/23 15:31:53.848  26/07/23 15:47:45.628  0                   0                   0
3         swp11  Down   Cable/transceiver is unplugged  26/07/23 15:31:53.848  26/07/23 15:47:45.628  0                   0                   0
4         swp12  Down   Cable/transceiver is unplugged  26/07/23 15:31:53.848  26/07/23 15:47:45.628  0                   0                   0
```

To show the configuration for all WJH channels and the total drops, run the `nv show system wjh channel` command.

```
cumulus@switch:~$ nv show system wjh channel
Channel name  Trigger(s)      Polling interval  Type                                     Aggregate cache size  Total drops
------------  --------------  ----------------  ---------------------------------------  --------------------  -----------
acls          ACL             30                WJH_USER_CHANNEL_CYCLIC_AND_AGGREGATE_E  1024                  109        
buffer        BUFFER          30                WJH_USER_CHANNEL_CYCLIC_AND_AGGREGATE_E  1024                  0          
forwarding    L2, L3, TUNNEL  30                WJH_USER_CHANNEL_CYCLIC_AND_AGGREGATE_E  1024                  749        
layer-1       L1              30                WJH_USER_CHANNEL_AGGREGATE_E             1024                  0
```

To show the configuration for a specific WJH channel and the total drops, run the `nv show system wjh channel <channel>` command.

```
cumulus@switch:~$ nv show system wjh channel buffer
                      operational                              applied
--------------------  ---------------------------------------  -------
polling-interval      30                                       30
aggregate-cache-size  1024                                     1024
drop-category-list    BUFFER
type                  WJH_USER_CHANNEL_CYCLIC_AND_AGGREGATE_E
total-drops           0

Latency buffer threshold
===========================
    Traffic Class  Interface  High threshold
    -------------  ---------  --------------
    all            all        1000

Congestion buffer threshold
==============================
    Traffic Class  Interface  High threshold
    -------------  ---------  --------------
    all            swp1       20
                   swp2       20
                   swp3       20
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You can run the `nv-wjh-cli poll` command from the command line with the following options:
 
| Command Option | Description |
| -------------- | ----------- |
| `--data`  | You can specify `drops`, `aggregates`, or `l1`.<br>`drops` shows individual drops for each packet.<br>`aggregates` shows aggregated drops.<br>`l1` shows layer 1 port-state aggregates (only valid for channels with layer 1 in their trigger list).|
| `--output-type` | You can specify `table`, `json`, or `pcap`. `pcap` is only for data drops (`--data drops`).|
| `--no-metadata` | Writes PCAP output without embedded metadata. This option is only valid with `--data drops` and `--output-type pcap`. |
| `--channels <channel-name>,<channel-name>` | A comma-separated list of the channels to show. If you do not provide the `--channels` option, the command shows all configured channels. |
| `dump` | Shows diagnostic information. The output includes channel configuration, snapshots for each channel, and memory statistics. The command saves the output to the `/var/log/nv-wjh/diags-dump/<timestamp>` file. |

The following example shows aggregated drops:

```
cumulus@switch:~$ nv-wjh-cli poll --data aggregates
```

The following command saves dropped packets in the forwarding channel to a file in PCAP format without metadata:

```
cumulus@switch:~$ nv-wjh-cli poll --data drops --output-type pcap --channels forwarding --no-metadata
```

{{< /tab >}}
{{< /tabs >}}

## WJH Events

This section provides the supported WJH events with a brief description of each.

### Layer 1 Drops

Layer 1 drop events describe why a port is in the down state.

| Reason | Description|
| --- | --- |
| Link training failure | The link is not able to go operational up due to link training failure. |
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

Layer 2 drop events describe why the switch drops packets at layer 2.

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

Router drop events describe why the server is unable to route a packet.

| Reason | Severity | Description |
| --- | --- | --- |
| Non-routable packet |  Notice | The packet has no route in the routing table. |
| Blackhole route | Warning | The packet was received with an action equal to discard. |
| Unresolved next hop | Warning | The next hop in the route is unknown. |
| Blackhole ARP/neighbor | Warning | The packet was received with a blackhole adjacency. |
| IPv6 destination in multicast scope FFx0:/16 | Notice | The packet was received with a multicast destination address in FFx0:/16 address range. |
| IPv6 destination in multicast scope FFx1:/16 | Notice | The packet was received with a multicast destination address in FFx1:/16 address range. |
| Non-IP packet | Notice | Cannot read the packet header because it is not an IP packet. |
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

Tunnel drop events describe why a tunnel is down.

| Reason | Severity | Description |
| --- | --- | --- |
| Overlay switch - source MAC is multicast | Error | The source MAC address of the overlay packet is multicast. |
| Overlay switch - source MAC equals destination MAC | Error | The source MAC address of the overlay packet is the same as the destination MAC address. Supported on Spectrum-4 and later. |
| Decapsulation error | Error | Decapsulation produced an incorrect format for the packet. For example, encapsulation of a packet with many VLANs or IP options on the underlay can cause decapsulation to result in a short packet. |
| Source MAC equals Zero | Error |  The source MAC address equals 0.  |
| Encapsulation port isolation | Error | Encapsulation port isolation. |

### Buffer Drops

Buffer drop events describe why the server buffer has dropped packets.

| Reason | Severity | Description |
| --- | --- | --- |
| Tail drop | Warning | Tail drop is enabled and the buffer queue is filled to maximum capacity. |
| WRED | Warning | Weighted Random Early Detection is enabled and the buffer queue is filled to maximum capacity or the RED engine dropped the packet as a random congestion prevention. |
| Port TC Congestion Threshold Crossed | Warning | The percentage of the occupancy buffer exceeded or dropped below the specified high or low threshold. |
| Packet Latency Threshold Crossed | Warning | The time a packet spent within the switch exceeded or dropped below the specified high or low threshold. Not supported on Spectrum-1 and Spectrum-6. |

### ACL Drops

ACL drop events describe why an ACL has dropped packets.

| Reason | Severity | Description|
| --- | --- | --- |
| Ingress port ACL | Notice | An ACL action is set to deny on the physical ingress port or bond. |
| Ingress router ACL | Notice | An ACL action is set to deny on the ingress switch virtual interfaces (SVIs). |
| Egress port ACL | Notice | An ACL action is set to deny on the physical egress port or bond. |
| Egress router ACL | Notice | An ACL action is set to deny on the egress SVIs. |

## Considerations
<!--
### WJH and Package Upgrade

The Linux package upgrade command (`apt-get upgrade`) only upgrades existing packages and does not install newly introduced packages; therefore, `apt-get upgrade` does not install the new `nv-wjh` package, introduced in Cumulus 5.18.0.

When using WJH, make sure to use the NVUE package upgrade command `nv action upgrade system packages to latest use-vrf mgmt` or the Linux `apt-get dist-upgrade` command to perform a full package upgrade. You can also manually install the `nv-wjh` package after upgrade.
-->
### Buffer Packet Drop Monitoring

- Buffer packet drop monitoring is available on a switch with Spectrum-2 and later.
- Buffer packet drop monitoring uses a SPAN destination. If you configure SPAN, ensure that you do not exceed the total number of SPAN destinations allowed for your switch ASIC type; see {{<link url="SPAN-and-ERSPAN/#limitations" text="SPAN and ERSPAN">}}. If you need to remove the SPAN destination that buffer packet drop monitoring uses, delete the buffer monitoring drop category with the NVUE `nv unset system wjh channel buffer trigger buffer` command.

### WJH and the NVIDIA NetQ Agent

When you enable the NVIDIA NetQ agent on the switch, the WJH service stops and does not run. If you disable the NVIDIA NetQ service and want to use WJH, run the following commands to enable and start the WJH service:

{{< tabs "TabID14 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set system wjh state enabled
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo systemctl enable nv-wjh
cumulus@switch:~$ sudo systemctl start nv-wjh
```

{{< /tab >}}
{{< /tabs >}}
