---
title: New and Updated Telemetry Metrics
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.17"
toc: 1
---
The following tables list the new, updated, and deprecated gNMI and OTEL metrics in Cumulus Linux 5.17.

## gNMI Metrics

{{< tabs "TabID13 ">}}
{{< tab "Control Plane">}}

|  Name | Description |
|------ | ----------- |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-receives`| IPv4 ingress packets received.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-addr-errors`| IPv4 ingress packet address errors.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-delivers`| IPv4 ingress packets delivered. |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-discarded-pkts`| IPv4 ingress packets discarded.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-hdr-errors`| IPv4 ingress packet hardware errors.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-unknown-protos`| IPv4 ingress packet unknown protocols.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-forwarded-pkts`| IPv4 forwarded ingress packets.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-reassembly-ok`| IPv4 ingress packets with reassembly OK .|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-reassembly-fails`| IPv4 ingress packets with reassembly fail.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-reassembly-reqd`| IPv4 ingress packets with reassembly required.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-no-routes`| IPv4 ingress packets with no routes.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-octets`| IPv4 ingress packet octets. |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-multicast-pkts`| IPv4 ingress mulicast packets.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-multicast-octets`| IPv4 ingress multicast packet octets.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-broadcast-pkts`| IPv4 ingress broadcast packets.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-truncated-pkts`| IPv4 ingress truncted packets. |
| `/system/control-plane-traffic/egress/ipv4/counters/out-requests`| IPv4 egress packet requests.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-discarded-pkts`| IPv4 egress packets discarded.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-no-routes`| IPv4 egress packets with no routes.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-frag-ok`| IPv4 egress packets with fragment OK.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-frag-fails`| IPv4 egress packets with fragment fails.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-frag-creates`| IPv4 egress packets with fragment creates.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-octets`| IPv4 egress packets octets.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-multicast-pkts`| IPv4 egress multicast packets.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-multicast-octets`| IPv4 egress multicast packet octets.|
| `/system/control-plane-traffic/egress/ipv4/counters/out-broadcast-pkts`| IPv4 egress broadcast packets.|
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-msgs`| IPv4 ICMP ingress packet messages.|
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-errors`| IPv4 ICMP ingress packet errors.|
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-dest-unreachs`| IPv4 ICMP ingress packets with destination unreachable.|
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-time-excds`| IPv4 ICMP ingress packets with time exceeds.|
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-echos`| IPv4 ICMP ingress packet echos.|
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-echo-reps`| IPv4 ICMP ingress packet echo repeats. |
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-msgs`| IPv4 ICMP egress packet messages.|
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-errors`| IPv4 ICMP egress packet errors.|
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-dest-unreachs`| IPv4 ICMP egress packets with destination unreachable.|
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-time-excds`| IPv4 ICMP egress packets with time exceeds.|
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-echos`| IPv4 ICMP egress packet echos.|
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-echo-reps`| IPv4 ICMP egress packet echo repeats.|
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/in-segs`| IPv4 TCP segments received.|
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/in-errs`| IPv4 TCP errors received.|
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/out-segs`| IPv4 TCP segments sent.|
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/retrans-segs`| IPv4 TCP segments retransmitted.|
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/active-opens`| IPv4 TCP active opens.|
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/passive-opens`| IPv4 TCP passive opens.|
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/attempt-fails`| IPv4 TCP attempt fails.|
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/estab-resets`| IPv4 TCP established resets.|
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/curr-estab`| IPv4 TCP currently established.|
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/out-rsts`| IPv4 TCP outgoing resets.|
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/listen-drops`| IPv4 TCP  listen drops.|
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/listen-overflows`| IPv4 TCP listen overflows|
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/tcp-timeouts`| IPv4 TCP timeouts.|
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/tcp-syn-retrans`| IPv4 TCP Syn retransmissions.|
| `/system/control-plane-traffic/ingress/ipv4/udp/counters/in-datagrams`| IPv4 UDP datagrams received.|
| `/system/control-plane-traffic/ingress/ipv4/udp/counters/in-errors`| IPv4 UDP errors received.|
| `/system/control-plane-traffic/ingress/ipv4/udp/counters/no-ports`| IPv4 UDP no ports.|
| `/system/control-plane-traffic/ingress/ipv4/udp/counters/rcvbuf-errors`| IPv4 UDP buffer errors received.|
| `/system/control-plane-traffic/egress/ipv4/udp/counters/out-datagrams`| IPv4 UDP datagrams sent.|
| `/system/control-plane-traffic/egress/ipv4/udp/counters/sndbuf-errors`| IPv4 UDP buffer errors sent.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-receives`| IPv6 ingress packets received.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-addr-errors`| IPv6 ingress packet address errors.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-delivers`| IPv6 ingress packets delivered.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-discarded-pkts`| IPv6 ingress packets discarded.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-hdr-errors`| IPv6 ingress packets with hardware errors. |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-unknown-protos`| IPv6 ingress packets with unknown protocols.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-no-routes`| IPv6 ingress packets with no routes.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-octets`| IPv6 ingress packets octets. |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-multicast-pkts`| IPv6 ingress multicast packets.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-multicast-octets`| IPv6 ingress multicast octets. |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-truncated-pkts`| IPv6 truncated ingress packets.|
| `/system/control-plane-traffic/egress/ipv6/counters/out-requests`| IPv6 egress request packets.|
| `/system/control-plane-traffic/egress/ipv6/counters/out-discarded-pkts`| IPv6 discarded egress packets.|
| `/system/control-plane-traffic/egress/ipv6/counters/out-no-routes`| IPv6 egress packets with no routes. |
| `/system/control-plane-traffic/egress/ipv6/counters/out-forwarded-pkts`| IPv6 forwarded egress packets. |
| `/system/control-plane-traffic/egress/ipv6/counters/out-frag-ok`|  IPv6 egress packets with fragment ok.|
| `/system/control-plane-traffic/egress/ipv6/counters/out-frag-fails`| IPv6 egress packets with fragment fails. |
| `/system/control-plane-traffic/egress/ipv6/counters/out-frag-creates`| IPv6 egress packets with fragment creates.|
| `/system/control-plane-traffic/egress/ipv6/counters/out-octets`| IPv6 egress octets.|
| `/system/control-plane-traffic/egress/ipv6/counters/out-multicast-pkts`| IPv6 multicast egress packets.|
| `/system/control-plane-traffic/egress/ipv6/counters/out-multicast-octets`| IPv6 multicast egress octets.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-reassembly-ok`| IPv6 ingress packets with reassembly ok.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-reassembly-fails`| IPv6 ingress packets with reassembly fails.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-reassembly-reqd`| IPv6 ingress packets with reassembly required.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-msgs`| IPv6 ICMP ingress messages.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-errors`| IPv6 ICMP ingress errors.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-dest-unreachs`| IPv6 ICMP ingress destination unreachable.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-time-excds`| IPv6 ICMP ingress time exceeds.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-echos`| IPv6 ICMP ingress echos.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-echo-replies`| IPv6 ICMP ingress echo replies.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-msgs`| IPv6 ICMP egress message.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-errors`| IPv6 ICMP egress errors.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-dest-unreachs`| IPv6 ICMP egress destination unreachable.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-time-excds`| IPv6 ICMP egress time exceeds.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-echos`| IPv6 ICMP egress echos.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-echo-replies`| IPv6 ICMP egress echo replies.|
| `/system/control-plane-traffic/ingress/ipv6/udp/counters/in-datagrams`| IPv6 UDP datagrams received.|
| `/system/control-plane-traffic/ingress/ipv6/udp/counters/in-errors`| IPv6 UDP errors received.|
| `/system/control-plane-traffic/ingress/ipv6/udp/counters/no-ports`| IPv6 UDP no ports received.|
| `/system/control-plane-traffic/ingress/ipv6/udp/counters/rcvbuf-errors`| IPv6 UDP receive errors.|
| `/system/control-plane-traffic/egress/ipv6/udp/counters/out-datagrams`| IPv6 UDP datagrams sent.|
| `/system/control-plane-traffic/egress/ipv6/udp/counters/sndbuf-errors`| IPv6 UDP send buffer errors sent.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-neighbor-advertisements`| IPv6 ICMP neighbor advertisements received.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-neighbor-solicits`| IPv6 ICMP neighbor solicits received.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-redirects`| IPv6 ICMP redirects received.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-router-advertisements`| IPv6 ICMP router advertisements received.|
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-router-solicits`| IPv6 ICMP router solicits received.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-neighbor-advertisements`| IPv6 ICMP neighbor advertisements sent.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-neighbor-solicits`| IPv6 ICMP neighbor solicits sent.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-redirects`| IPv6 ICMP redirects sent.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-router-advertisements`| IPv6 ICMP router advertisements sent.|
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-router-solicits`| IPv6 ICMP router solicits sent.|
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-redirects`| IPv4 ICMP redirects received.|
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-redirects`| IPv4 ICMP redirects sent|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-ce-pkts`| IPv6 Congestion Experienced packets received. |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-ect0-pkts`| IPv6 ECN-Capable Transport, codepoint 10 packets received.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-ect1-pkts`| IPv6 ECN-Capable Transport (1) codepoint (binary 01) packets received.|
| `/system/control-plane-traffic/ingress/ipv6/counters/in-no-ect-pkts`| IPv6 packets received with no Congestion Experienced.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-ce-pkts`| IPv4 Congestion Experienced packets received.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-ect0-pkts`| IPv4 ECN-Capable Transport, codepoint 10 packets received. |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-ect1-pkts`| IPv4 ECN-Capable Transport (1) codepoint (binary 01) packets received.|
| `/system/control-plane-traffic/ingress/ipv4/counters/in-no-ect-pkts` | IPv4 packets received with no Congestion Experienced.|

{{< /tab >}}
{{< tab "Link Debounce ">}}

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface[name=swp1]/hold-time/state/counters/ignored-up-events` | UP events suppressed because debounce timer had not yet expired (transient UP spikes filtered). This metric indicates Noise or short UP spikes being filtered.|
| `/interfaces/interface[name=swp1]/hold-time/state/counters/ignored-down-events` | DOWN events suppressed because debounce timer had not yet expired (transient link loss filtered). This metric indicates short interruptions being filtered.| 
| `/interfaces/interface[name=swp1]/hold-time/state/counters/received-up-events`| UP events accepted and propagated after debounce delay (stable link recovery). This metric indicates stable link recovery events.|
| `/interfaces/interface[name=swp1]/hold-time/state/counters/received-down-events` | DOWN events accepted and propagated after debounce delay (sustained link failure). This metric indicates sustained link failure events.| 
| `/interfaces/interface[name=swp1]/hold-time/state/counters/timer-cancellations` |  Timer aborted because link state reverted before timer expired (quick reversal). This metric indicates Link flapping or oscillation.| 
| `/interfaces/interface[name=swp1]/hold-time/state/counters/timer-expirations` |  Timer completed successfully, event sent after debounce delay (stable state change). This metric indicates Valid and stable state changes.|

{{< /tab >}}
{{< tab "PHY">}}

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface[name]/phy/link_down_events` | Total PHY link down events.|
| `/interfaces/interface[name]/phy/unintentional_link_down_events` | Unintentional link drops (local and remote).|
| `/interfaces/interface[name]/phy/intentional_link_down_events` | Intentional link drops (local and remote).|
| `/interfaces/interface[name]/phy/local_reason_opcode` | Opcode of link down reason at the local end.|
| `/interfaces/interface[name]/phy/remote_reason_opcode` | Opcode of link down reason at the remote end.|

{{< /tab >}}
{{< tab "Platform">}}
|  Name | Description |
|------ | ----------- |
| `/components/component[name]/state/name` | Component name.|
| `/components/component[name]/state/serial-no` | Component serial number, keyed by component name.|
| `/components/component[name]/state/part-no` | Component part number, keyed by component name.|
| `/components/component[name]/state/model-name`| Component model name.|
| `/components/component[name]/state/hardware-version`| Component hardware version.|
| `/components/component[name]/state/type`| Component type.|

{{< /tab >}}
{{< /tabs >}}

## OTEL Metrics

{{< tabs "TabID167 ">}}
{{< tab "Control Plane">}}

|  Name | Description |
|------ | ----------- |
| `node_netstat_Ip_InReceives` | The number of IP packets received. | 
| `node_netstat_Ip_InAddrErrors` | The umber of IP packets dropped upon receipt due to errors in the destination or source IP address.|  
| `node_netstat_Ip_InDelivers` | The number of received IP packets that were successfully delivered to higher-level protocols (such as TCP or UDP).|  
| `node_netstat_Ip_InDiscards` | The number of IP packets received but dropped, often due to errors.|  
| `node_netstat_Ip_InHdrErrors` | The number of input IP packets discarded due to errors in their headers (bad checksums, version mismatch, or invalid length). |  
| `node_netstat_Ip_InUnknownProtos` | The number of incoming IP packets received with an unknown or unsupported protocol. | 
| `node_netstat_Ip_ForwDatagrams` | The number of IP packets forwarded. | 
| `node_netstat_Ip_ReasmOKs` | The number of IP packets successfully reassembled after being fragmented.| 
| `node_netstat_Ip_ReasmFails` | The number of IP packets that failed to reassemble.| 
| `node_netstat_Ip_ReasmReqds` | The number of IP packets that required reassembly.| 
| `node_netstat_IpExt_InNoRoutes` | The number of incoming IP packets discarded because no route could be found to the destination address. | 
| `node_netstat_IpExt_InOctets` | The number of bytes received through IP, representing incoming network traffic. | 
| `node_netstat_IpExt_InMcastPkts` | The number of IP multicast packets received.| 
| `node_netstat_IpExt_InMcastOctets` | The number of IP multicast bytes received.| 
| `node_netstat_IpExt_InBcastPkts` | The number of incoming IP broadcast packets received.| 
| `node_netstat_IpExt_InTruncatedPkts` | The number of truncated packets received.| 
| `node_netstat_Ip_OutRequests` | The number of packets sent.| 
| `node_netstat_Ip_OutDiscards` | The number of outgoing IP packets that were discarded, even though no errors were detected to prevent their transmission.| 
| `node_netstat_Ip_OutNoRoutes` |  The number of IP packets dropped because a route could not be found. | 
| `node_netstat_Ip_FragOKs` |  The number of IP packets that have been successfully fragmented. | 
| `node_netstat_Ip_FragFails` |  The number of IP packets that have been discarded because they needed to be fragmented but could not be, or were otherwise failing fragmentation.| 
| `node_netstat_Ip_FragCreates` | The number of IP packets that have been generated as a result of fragmentation.| 
| `node_netstat_IpExt_OutOctets` | The number of bytes sent. | 
| `node_netstat_IpExt_OutMcastPkts` | The number of IP multicast packets sent.| 
| `node_netstat_IpExt_OutMcastOctets` | The number of IP multicast bytes sent. | 
| `node_netstat_IpExt_OutBcastPkts` | The number of IP broadcast packets sent.| 
| `node_netstat_Icmp_InMsgs` | The number of ICMP messages received.| 
| `node_netstat_Icmp_InErrors` | The number of ICMP errors received.| 
| `node_netstat_Icmp_InDestUnreachs` | The number of ICMP Destination Unreachable received. | 
| `node_netstat_Icmp_InTimeExcds` | The number of ICMP Time Exceeded messages received.| 
| `node_netstat_Icmp_InEchos` | The number of ICMP Echo Request messages (pings) received.| 
| `node_netstat_Icmp_InEchoReps` | The number of ICMP Echo Reply messages received.| 
| `node_netstat_Icmp_OutMsgs` | The number of ICMP messages sent.| 
| `node_netstat_Icmp_OutErrors` | The number of ICMP errors sent.| 
| `node_netstat_Icmp_OutDestUnreachs` | The number of outgoing ICMP Destination Unreachable packets sent.| 
| `node_netstat_Icmp_OutTimeExcds` | The number of ICMP Time Exceeded messages sent.| 
| `node_netstat_Icmp_OutEchos` | The number of ICMP Echo Request messages sent. |
| `node_netstat_Icmp_OutEchoReps` | The number of ICMP Echo Reply (ping reply) messages sent.| 
| `node_netstat_Tcp_InSegs` | The number of TCP segments received.| 
| `node_netstat_Tcp_InErrs` | The number of TCP segments received that contained errors.| 
| `node_netstat_Tcp_OutSegs` | The number of TCP segments sent.| 
| `node_netstat_Tcp_RetransSegs` | The number of TCP segments retransmitted.| 
| `node_netstat_Tcp_ActiveOpens` | The number of TCP connections that have made a direct transition from the CLOSED state to the SYN-SENT state.| 
| `node_netstat_Tcp_PassiveOpens` |  The number of TCP connections with a SYN that moved directly from the LISTEN state to SYN-RCVD.| 
| `node_netstat_Tcp_AttemptFails` |  The number of times TCP connections have made a failed attempt to connect.| 
| `node_netstat_Tcp_EstabResets` |  The number of TCP connections that have directly transitioned from an ESTABLISHED state to a CLOSED state.| 
| `node_netstat_Tcp_CurrEstab` |  The number of TCP connections in the ESTABLISHED or CLOSE-WAIT state.| 
| `node_netstat_Tcp_OutRsts` |  The number of TCP resends.| 
| `node_netstat_TcpExt_ListenDrops` |  The number of TCP listne drops.| 
| `node_netstat_TcpExt_ListenOverflows` |  The number of TCP listen overflows.| 
| `node_netstat_TcpExt_TCPTimeouts` |  The number of TCP connections that timed out.| 
| `node_netstat_TcpExt_TCPSynRetrans` |  The number of TCP SYN retransmissions.| 
| `node_netstat_Udp_InDatagrams` |  The number of UDP packets received.| 
| `node_netstat_Udp_InErrors` |  The number of UDP errors opens.| 
| `node_netstat_Udp_NoPorts` |  The number of UDP no ports opens.| 
| `node_netstat_Udp_RcvbufErrors` |  The number of UDP receive buffer errors. | 
| `node_netstat_Udp_OutDatagrams` | The number of UDP packets sent.| 
| `node_netstat_Udp_SndbufErrors` | The number of UDP send buffer errors.| 
| `node_netstat_Ip6_InReceives` | The number of IP packets received.| 
| `node_netstat_Ip6_InAddrErrors` | The number of IPv6 packets dropped due to address errors.| 
| `node_netstat_Ip6_InDelivers` | The number of incoming IPv6 packets delivered to upper-layer protocols.| 
| `node_netstat_Ip6_InDiscards` |  The number of incoming IPv6 packets discarded.| 
| `node_netstat_Ip6_InHdrErrors` | The number of incoming IPv6 packets with hardware errors.| 
| `node_netstat_Ip6_InUnknownProtos` | The number of incoming IPv6 packets with unknown protocols.| 
| `node_netstat_Ip6_InNoRoutes` | The number of incoming IPv6 packets with no routes.| 
| `node_netstat_Ip6_InOctets` | The number of bytes received through IPv6. | 
| `node_netstat_Ip6_InMcastPkts` | The number of incoming IPv6 multicast packets| 
| `node_netstat_Ip6_InMcastOctets` | The number of incoming multicast bytes received through IPv6.| 
| `node_netstat_Ip6_InTruncatedPkts` | The number of incoming IPv6 truncated packets.| 
| `node_netstat_Ip6_OutRequests` | The number of IPv6 packets sent.| 
| `node_netstat_Ip6_OutDiscards` | The number of outgoing IPv6 packets intentionally dropped.| 
| `node_netstat_Ip6_OutNoRoutes` | The number of IPv6 packets dropped because no route could be found to their destination.| 
| `node_netstat_Ip6_OutForwDatagrams` | The number of IPv6 packets that the local node forwarded to other destinations.| 
| `node_netstat_Ip6_FragOKs` | The number of IPv6 packets successfully fragmented.| 
| `node_netstat_Ip6_FragFails` | The number of IPv6 packets that could not be fragmented due to size restrictions or errors.| 
| `node_netstat_Ip6_FragCreates` | The number of IPv6 packets fragmented into multiple packets. | 
| `node_netstat_Ip6_OutOctets` | The number of bytes sent in IPv6 packets.| 
| `node_netstat_Ip6_OutMcastPkts` | The number of IPv6 multicast packets sent.| 
| `node_netstat_Ip6_OutMcastOctets` | The number of octets (bytes) transmitted in IPv6 multicast packets. | 
| `node_netstat_Ip6_ReasmOKs` | The number of IPv6 packets successfully reassembled.| 
| `node_netstat_Ip6_ReasmFails` | The number of IPv6 packets that failed to reassemble successfully.| 
| `node_netstat_Ip6_ReasmReqds` | The number of IPv6 fragments that need to be reassembled. | 
| `node_netstat_Icmp6_InMsgs` | The number of ICMPv6 messages received. | 
| `node_netstat_Icmp6_InErrors` | The number of ICMPv6 errors received.| 
| `node_netstat_Icmp6_InDestUnreachs` | The number of ICMPv6 Destination Unreachable packets received. | 
| `node_netstat_Icmp6_InTimeExcds` | The number of ICMPv6 "Time Exceeded" messages received.| 
| `node_netstat_Icmp6_InEchos` | The number of ICMPv6 Echo Request messages (pings) received.| 
| `node_netstat_Icmp6_InEchoReplies` | The number of ICMPv6 Echo Reply messages (pings) received.| 
| `node_netstat_Icmp6_OutMsgs` | The number of ICMPv6 messages sent. | 
| `node_netstat_Icmp6_OutErrors` | The number of ICMPv6 errors sent.| 
| `node_netstat_Icmp6_OutDestUnreachs` | The number of ICMPv6 Destination Unreachable packets sent.| 
| `node_netstat_Icmp6_OutTimeExcds` | The number of ICMPv6 "Time Exceeded" messages sent.| 
| `node_netstat_Icmp6_OutEchos` | The number of ICMPv6 Echo Request messages (pings) sent.| 
| `node_netstat_Icmp6_OutEchoReplies` | The number of ICMPv6 Echo Reply messages (pings) sent.| 
| `node_netstat_Udp6_InDatagrams` | The number of UDP packets delivered to IPv6 users.| 
| `node_netstat_Udp6_InErrors` | The number of received UDP6 datagrams that could not be delivered, often due to errors.| 
| `node_netstat_Udp6_NoPorts` | The number of UDP6 no ports.| 
| `node_netstat_Udp6_RcvbufErrors` | The number of times a UDP6 packet was dropped because the receive buffer (Rcvbuf) was full.| 
| `node_netstat_Udp6_OutDatagrams` | The number of UDP datagrams sent through IPv6.| 
| `node_netstat_Udp6_SndbufErrors` | The number of UDPv6 packets that could not be sent due to send buffer errors.| 
| `node_netstat_Icmp6_InNeighborAdvertisements` | The number of ICMPv6 Neighbor Advertisement messages received.| 
| `node_netstat_Icmp6_InNeighborSolicits` | The number of ICMPv6 Neighbor Solicitation messages received.| 
| `node_netstat_Icmp6_InRedirects` | The number of ICMPv6 redirect messages received. | 
| `node_netstat_Icmp6_InRouterAdvertisements` | The number of ICMPv6 Type 134 messages (Router Advertisements) received.| 
| `node_netstat_Icmp6_InRouterSolicits` | The number of ICMPv6 Router Solicitation (RS) messages received.| 
| `node_netstat_Icmp6_OutNeighborAdvertisements` | The number of ICMPv6 Neighbor Advertisement messages sent.| 
| `node_netstat_Icmp6_OutNeighborSolicits` | The number of ICMPv6 Neighbor Solicitation messages sent.| 
| `node_netstat_Icmp6_OutRedirects` | The number of ICMPv6 Redirect messages sent.| 
| `node_netstat_Icmp6_OutRouterAdvertisements` | The number of IPv6 Router Advertisement (RA) messages sent.| 
| `node_netstat_Icmp6_OutRouterSolicits` | The number of ICMPv6 Router Solicitation (Type 133) messages sent.| 
| `node_netstat_Icmp_InRedirects` | The number of ICMP Redirect messages received.| 
| `node_netstat_Icmp_OutRedirects` | The number of ICMP Out Redirects.| 
| `node_netstat_Ip6_InCEPkts` | The number of received IPv6 packets with the Congestion Experienced (CE) codepoint set.| 
| `node_netstat_Ip6_InECT0Pkts` | The number of received IPv6 packets with the ECN-Capable Transport (ECT) codepoint '0' set (ECT(0)).| 
| `node_netstat_Ip6_InECT1Pkts` | The number of incoming IPv6 packets received with the ECN (Explicit Congestion Notification) Codepoint 1 (ECT1) set. | 
| `node_netstat_Ip6_InNoECTPkts` | The number of incoming IPv6 packets received that do not have the ECN-Capable Transport (ECT) codepoint set.| 
| `node_netstat_IpExt_InCEPkts` | The number of incoming IP packets received with the Congestion Experienced (CE) codepoint set.| 
| `node_netstat_IpExt_InECT0Pkts` | The number of IP datagrams received with the ECN (Explicit Congestion Notification) codepoint "ECT(0)".| 
| `node_netstat_IpExt_InECT1Pkts` | The number of IP packets received with ECN (Explicit Congestion Notification) capable transport, specifically ECT(1) codepoint.| 
| `node_netstat_IpExt_InNoECTPkts` | The number of IP packets received with no ECN (Explicit Congestion Notification) capable transport.| 

{{< /tab >}}
{{< tab "Link Debounce ">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_link_debounce_ignored_events[event][interface]` | UP: Events suppressed because debounce timer had not yet expired (transient UP spikes filtered). This metric indicates Noise or short UP spikes being filtered.<br>DOWN: Events suppressed because debounce timer had not yet expired (transient link loss filtered). This metric indicates short interruptions being filtered.  |
| `nvswitch_interface_link_debounce_received_events[event][interface]` | UP: Events accepted and propagated after debounce delay (stable link recovery). This metric indicates stable link recovery events.<br>DOWN: Events accepted and propagated after debounce delay (sustained link failure). This metric indicates sustained link failure events.  |
| `nvswitch_interface_link_debounce_timer_cancellations[interface]` | Timer aborted because link state reverted before timer expired (quick reversal). This metric indicates Link flapping or oscillation. |
| `nvswitch_interface_link_debounce_timer_expirations[interface]` | Timer completed successfully, event sent after debounce delay (stable state change). This metric indicates Valid and stable state changes.  |

{{< /tab >}}
{{< tab "PHY">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_phy_stats_link_down_events` | Total PHY link down events. |
| `nvswitch_interface_phy_stats_intentional_link_down_events` | Intentional link down events. |
| `nvswitch_interface_phy_stats_unintentional_link_down_events` | Unintentional link down events. |
| `nvswitch_interface_phy_stats_link_down_reason_code_local ` | Opcode of link down reason at the local end.|
| `nvswitch_interface_phy_stats_link_down_reason_code_remote ` | Opcode of link down reason at the remote end. |

{{< /tab >}}
{{< tab "Platform">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_info_hw_details` | Hardware details such as the version, model name, part number, serial number, type, and name.|

{{< /tab >}}
{{< /tabs >}}