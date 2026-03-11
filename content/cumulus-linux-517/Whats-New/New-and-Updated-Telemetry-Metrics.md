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
| `/system/control-plane-traffic/ingress/ipv4/counters/in-receives`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-addr-errors`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-delivers`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-discarded-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-hdr-errors`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-unknown-protos`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-forwarded-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-reassembly-ok`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-reassembly-fails`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-reassembly-reqd`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-no-routes`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-octets`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-multicast-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-multicast-octets`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-broadcast-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-truncated-pkts`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-requests`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-discarded-pkts`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-no-routes`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-frag-ok`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-frag-fails`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-frag-creates`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-octets`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-multicast-pkts`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-multicast-octets`| |
| `/system/control-plane-traffic/egress/ipv4/counters/out-broadcast-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-msgs`| |
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-errors`| |
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-dest-unreachs`| |
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-time-excds`| |
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-echos`| |
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-echo-reps`| |
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-msgs`| |
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-errors`| |
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-dest-unreachs`| |
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-time-excds`| |
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-echos`| |
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-echo-reps`| |
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/in-segs`| |
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/in-errs`| |
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/out-segs`| |
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/retrans-segs`| |
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/active-opens`| |
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/passive-opens`| |
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/attempt-fails`| |
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/estab-resets`| |
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/curr-estab`| |
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/out-rsts`| |
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/listen-drops`| |
| `/system/control-plane-traffic/ingress/ipv4/tcp/counters/listen-overflows`| |
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/tcp-timeouts`| |
| `/system/control-plane-traffic/egress/ipv4/tcp/counters/tcp-syn-retrans`| |
| `/system/control-plane-traffic/ingress/ipv4/udp/counters/in-datagrams`| |
| `/system/control-plane-traffic/ingress/ipv4/udp/counters/in-errors`| |
| `/system/control-plane-traffic/ingress/ipv4/udp/counters/no-ports`| |
| `/system/control-plane-traffic/ingress/ipv4/udp/counters/rcvbuf-errors`| |
| `/system/control-plane-traffic/egress/ipv4/udp/counters/out-datagrams`| |
| `/system/control-plane-traffic/egress/ipv4/udp/counters/sndbuf-errors`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-receives`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-addr-errors`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-delivers`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-discarded-pkts`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-hdr-errors`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-unknown-protos`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-no-routes`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-octets`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-multicast-pkts`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-multicast-octets`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-truncated-pkts`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-requests`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-discarded-pkts`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-no-routes`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-forwarded-pkts`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-frag-ok`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-frag-fails`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-frag-creates`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-octets`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-multicast-pkts`| |
| `/system/control-plane-traffic/egress/ipv6/counters/out-multicast-octets`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-reassembly-ok`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-reassembly-fails`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-reassembly-reqd`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-msgs`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-errors`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-dest-unreachs`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-time-excds`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-echos`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-echo-replies`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-msgs`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-errors`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-dest-unreachs`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-time-excds`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-echos`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-echo-replies`| |
| `/system/control-plane-traffic/ingress/ipv6/udp/counters/in-datagrams`| |
| `/system/control-plane-traffic/ingress/ipv6/udp/counters/in-errors`| |
| `/system/control-plane-traffic/ingress/ipv6/udp/counters/no-ports`| |
| `/system/control-plane-traffic/ingress/ipv6/udp/counters/rcvbuf-errors`| |
| `/system/control-plane-traffic/egress/ipv6/udp/counters/out-datagrams`| |
| `/system/control-plane-traffic/egress/ipv6/udp/counters/sndbuf-errors`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-neighbor-advertisements`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-neighbor-solicits`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-redirects`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-router-advertisements`| |
| `/system/control-plane-traffic/ingress/ipv6/icmp/counters/in-router-solicits`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-neighbor-advertisements`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-neighbor-solicits`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-redirects`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-router-advertisements`| |
| `/system/control-plane-traffic/egress/ipv6/icmp/counters/out-router-solicits`| |
| `/system/control-plane-traffic/ingress/ipv4/icmp/counters/in-redirects`| |
| `/system/control-plane-traffic/egress/ipv4/icmp/counters/out-redirects`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-ce-pkts`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-ect0-pkts`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-ect1-pkts`| |
| `/system/control-plane-traffic/ingress/ipv6/counters/in-no-ect-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-ce-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-ect0-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-ect1-pkts`| |
| `/system/control-plane-traffic/ingress/ipv4/counters/in-no-ect-pkts` | |

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
{{< /tabs >}}

## OTEL Metrics

{{< tabs "TabID167 ">}}
{{< tab "Control Plane">}}

|  Name | Description |
|------ | ----------- |

| `node_netstat_Ip_InReceives` | | 
| `node_netstat_Ip_InAddrErrors` | |  
| `node_netstat_Ip_InDelivers` | |  
| `node_netstat_Ip_InDiscards` | |  
| `node_netstat_Ip_InHdrErrors` | |  
| `node_netstat_Ip_InUnknownProtos` | | 
| `node_netstat_Ip_ForwDatagrams` | | 
| `node_netstat_Ip_ReasmOKs` | | 
| `node_netstat_Ip_ReasmFails` | | 
| `node_netstat_Ip_ReasmReqds` | | 
| `node_netstat_IpExt_InNoRoutes` | | 
| `node_netstat_IpExt_InOctets` | | 
| `node_netstat_IpExt_InMcastPkts` | | 
| `node_netstat_IpExt_InMcastOctets` | | 
| `node_netstat_IpExt_InBcastPkts` | | 
| `node_netstat_IpExt_InTruncatedPkts` | | 
| `node_netstat_Ip_OutRequests` | | 
| `node_netstat_Ip_OutDiscards` | | 
| `node_netstat_Ip_OutNoRoutes` | | 
| `node_netstat_Ip_FragOKs` | | 
| `node_netstat_Ip_FragFails` | | 
| `node_netstat_Ip_FragCreates` | | 
| `node_netstat_IpExt_OutOctets` | | 
| `node_netstat_IpExt_OutMcastPkts` | | 
| `node_netstat_IpExt_OutMcastOctets` | | 
| `node_netstat_IpExt_OutBcastPkts` | | 
| `node_netstat_Icmp_InMsgs` | | 
| `node_netstat_Icmp_InErrors` | | 
| `node_netstat_Icmp_InDestUnreachs` | | 
| `node_netstat_Icmp_InTimeExcds` | | 
| `node_netstat_Icmp_InEchos` | | 
| `node_netstat_Icmp_InEchoReps` | | 
| `node_netstat_Icmp_OutMsgs` | | 
| `node_netstat_Icmp_OutErrors` | | 
| `node_netstat_Icmp_OutDestUnreachs` | | 
| `node_netstat_Icmp_OutTimeExcds` | | 
| `node_netstat_Icmp_OutEchos` | | 
| `node_netstat_Icmp_OutEchoReps` | | 
| `node_netstat_Tcp_InSegs` | | 
| `node_netstat_Tcp_InErrs` | | 
| `node_netstat_Tcp_OutSegs` | | 
| `node_netstat_Tcp_RetransSegs` | | 
| `node_netstat_Tcp_ActiveOpens` | | 
| `node_netstat_Tcp_PassiveOpens` | | 
| `node_netstat_Tcp_AttemptFails` | | 
| `node_netstat_Tcp_EstabResets` | | 
| `node_netstat_Tcp_CurrEstab` | | 
| `node_netstat_Tcp_OutRsts` | | 
| `node_netstat_TcpExt_ListenDrops` | | 
| `node_netstat_TcpExt_ListenOverflows` | | 
| `node_netstat_TcpExt_TCPTimeouts` | | 
| `node_netstat_TcpExt_TCPSynRetrans` | | 
| `node_netstat_Udp_InDatagrams` | | 
| `node_netstat_Udp_InErrors` | | 
| `node_netstat_Udp_NoPorts` | | 
| `node_netstat_Udp_RcvbufErrors` | | 
| `node_netstat_Udp_OutDatagrams` | | 
| `node_netstat_Udp_SndbufErrors` | | 
| `node_netstat_Ip6_InReceives` | | 
| `node_netstat_Ip6_InAddrErrors` | | 
| `node_netstat_Ip6_InDelivers` | | 
| `node_netstat_Ip6_InDiscards` | | 
| `node_netstat_Ip6_InHdrErrors` | | 
| `node_netstat_Ip6_InUnknownProtos` | | 
| `node_netstat_Ip6_InNoRoutes` | | 
| `node_netstat_Ip6_InOctets` | | 
| `node_netstat_Ip6_InMcastPkts` | | 
| `node_netstat_Ip6_InMcastOctets` | | 
| `node_netstat_Ip6_InTruncatedPkts` | | 
| `node_netstat_Ip6_OutRequests` | | 
| `node_netstat_Ip6_OutDiscards` | | 
| `node_netstat_Ip6_OutNoRoutes` | | 
| `node_netstat_Ip6_OutForwDatagrams` | | 
| `node_netstat_Ip6_FragOKs` | | 
| `node_netstat_Ip6_FragFails` | | 
| `node_netstat_Ip6_FragCreates` | | 
| `node_netstat_Ip6_OutOctets` | | 
| `node_netstat_Ip6_OutMcastPkts` | | 
| `node_netstat_Ip6_OutMcastOctets` | | 
| `node_netstat_Ip6_ReasmOKs` | | 
| `node_netstat_Ip6_ReasmFails` | | 
| `node_netstat_Ip6_ReasmReqds` | | 
| `node_netstat_Icmp6_InMsgs` | | 
| `node_netstat_Icmp6_InErrors` | | 
| `node_netstat_Icmp6_InDestUnreachs` | | 
| `node_netstat_Icmp6_InTimeExcds` | | 
| `node_netstat_Icmp6_InEchos` | | 
| `node_netstat_Icmp6_InEchoReplies` | | 
| `node_netstat_Icmp6_OutMsgs` | | 
| `node_netstat_Icmp6_OutErrors` | | 
| `node_netstat_Icmp6_OutDestUnreachs` | | 
| `node_netstat_Icmp6_OutTimeExcds` | | 
| `node_netstat_Icmp6_OutEchos` | | 
| `node_netstat_Icmp6_OutEchoReplies` | | 
| `node_netstat_Udp6_InDatagrams` | | 
| `node_netstat_Udp6_InErrors` | | 
| `node_netstat_Udp6_NoPorts` | | 
| `node_netstat_Udp6_RcvbufErrors` | | 
| `node_netstat_Udp6_OutDatagrams` | | 
| `node_netstat_Udp6_SndbufErrors` | | 
| `node_netstat_Icmp6_InNeighborAdvertisements` | | 
| `node_netstat_Icmp6_InNeighborSolicits` | | 
| `node_netstat_Icmp6_InRedirects` | | 
| `node_netstat_Icmp6_InRouterAdvertisements` | | 
| `node_netstat_Icmp6_InRouterSolicits` | | 
| `node_netstat_Icmp6_OutNeighborAdvertisements` | | 
| `node_netstat_Icmp6_OutNeighborSolicits` | | 
| `node_netstat_Icmp6_OutRedirects` | | 
| `node_netstat_Icmp6_OutRouterAdvertisements` | | 
| `node_netstat_Icmp6_OutRouterSolicits` | | 
| `node_netstat_Icmp_InRedirects` | | 
| `node_netstat_Icmp_OutRedirects` | | 
| `node_netstat_Ip6_InCEPkts` | | 
| `node_netstat_Ip6_InECT0Pkts` | | 
| `node_netstat_Ip6_InECT1Pkts` | | 
| `node_netstat_Ip6_InNoECTPkts` | | 
| `node_netstat_IpExt_InCEPkts` | | 
| `node_netstat_IpExt_InECT0Pkts` | | 
| `node_netstat_IpExt_InECT1Pkts` | | 
| `node_netstat_IpExt_InNoECTPkts` | | 

{{< /tab >}}
{{< tab "Link Debounce ">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_link_debounce_ignored_up_events` | UP events suppressed because debounce timer had not yet expired (transient UP spikes filtered). This metric indicates Noise or short UP spikes being filtered.  |
| `nvswitch_interface_link_debounce_ignored_down_events`| DOWN events suppressed because debounce timer had not yet expired (transient link loss filtered). This metric indicates short interruptions being filtered. |
| `nvswitch_interface_link_debounce_received_up_events` | UP events accepted and propagated after debounce delay (stable link recovery). This metric indicates stable link recovery events.  |
| `nvswitch_interface_link_debounce_received_down_events` | DOWN events accepted and propagated after debounce delay (sustained link failure). This metric indicates sustained link failure events.  |
| `nvswitch_interface_link_debounce_timer_cancellations` | Timer aborted because link state reverted before timer expired (quick reversal). This metric indicates Link flapping or oscillation. |
| `nvswitch_interface_link_debounce_timer_expirations` | Timer completed successfully, event sent after debounce delay (stable state change). This metric indicates Valid and stable state changes.  |

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
{{< /tabs >}}