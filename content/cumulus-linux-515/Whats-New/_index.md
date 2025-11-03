---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.15 release, and lists new features and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.15, see the {{<link title="Cumulus Linux 5.15 Release Notes" text="Cumulus Linux 5.15 Release Notes">}}.
- To upgrade to Cumulus Linux 5.15, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.15

Cumulus Linux 5.15.0 contains new features and improvements, and provides bug fixes.
### New Features and Enhancements

- {{<link url="#new-changed-and-deprecated-nvue-commands" text="NVUE command changes">}}
- {{<link url="Packet-Trimming/#packet-trimming-counters" text="Packet trimming counters">}}
- {{<link url="Bidirectional-Forwarding-Detection-BFD" text="FRR-based BFD support">}}. Legacy BFD configuration and routing link state verification with PTMd is now deprecated.
- {{<link url="Latency-Monitoring" text="Switch latency monitoring">}}
- {{<link url="Docker-with-Cumulus-Linux" text="Enhanced NVUE support for docker containers">}}
- {{<link url="802.1X-Interfaces/#dynamic-ipv6-multi-tenancy" text="802.1x Dynamic IPv6 Multi-tenancy">}}
- {{<link url="SSH-for-Remote-Access/#ssh-ciphers" text="SSH cipher configuration">}}
- {{<link url="Upgrading-Cumulus-Linux/#offline-package-upgrade" text="Offline package upgrade">}}
- RoCE {{<link url="RDMA-over-Converged-Ethernet-RoCE/#lossy-multi-tc-profile" text="lossy multi TC profile">}} updated to map DSCP values 41-50 to traffic class 5
- {{<link url="User-Accounts/#aaa-authentication-restrictions" text="AAA authentication restrictions">}}
- {{<link url="Interface-Configuration-and-Management/#interface-fault-detection" text="Interface fault detection">}}
- {{<link url="Syslog/#selectors-and-filters" text="Rsyslog selector design changes">}}
- Telemetry
   - {{<link url="gNMI-Streaming/#gNOI-operational-commands" text="gNOI operational commands">}}
   - {{<link url="Open-Telemetry-Export/#routing-metrics-format" text="BGP graceful shutdown metric for OTLP">}}
   - {{<link url="Open-Telemetry-Export/#acl-statistics" text="ACL metrics for OTLP">}}
   - {{<link url="Open-Telemetry-Export/#control-plane-statistic-format" text="Additional control plane metrics for OTLP">}}
   - {{<link url="gNMI-Streaming/#metrics" text="ACL metrics for gNMI streaming">}}
   - {{<link url="gNMI-Streaming/#metrics" text="Packet trimming metrics for gNMI streaming">}}
   - {{<link url="gNMI-Streaming/#metrics" text="PHY metrics for gNMI streaming">}} (Number of bit errors corrected and upper boundary of the bin)
   - {{<link url="High-Frequency-Telemetry/#streaming-hft-export" text="High frequency telemetry streaming">}}
   - {{<link url="Open-Telemetry-Export/#congestion-notifications" text="Congestion event notifications">}}
   - {{< expand "New gNMI xPaths aligning with OTEL metrics:" >}}
**New Platform Metrics:**

|  Name | Description |
|------ | ----------- |
| `/components/component[name]/state/name` | List of components, keyed by component name.|
| `/components/component[name]/state/serial-no` | Serial number of the component, keyed by component name.|
| `/components/component[name]/state/part-no` | Part number of the component, keyed by component name.|
| `/components/component[name]/storage/state/counters/rotation-rate-rpm` | Disk rotation rate in RPMs (supported only on SATA disks). |
| `/components/component[name]/storage/state/counters/write-cache` | Indicates whether the disk has a write cache (supported only on SATA disks). |
| `/components/component[name]/storage/state/counters/write-cache-enabled` | Indicates whether the disk write cache is enabled. (supported only on SATA disks) |
| `/components/component[name]/storage/state/counters/discard-seconds` | Number of seconds spent by all discards. |
| `/components/component[name]/storage/state/counters/discard-sectors` | Number of sectors discarded successfully.|
| `/components/component[name]/storage/state/counters/discard-completed` | Number of discards completed successfully. |
| `/components/component[name]/storage/state/counters/discard-merged` | Number of discards merged.|
| `/components/component[name]/storage/state/counters/flush-req-seconds` | Number of seconds spent by all flush requests. |
| `/components/component[name]/storage/state/counters/flush-req` | Number of flush requests completed successfully. |
| `/components/component[name]/storage/state/counters/io-ops-in-progress` | Number of I/Os currently in progress. |
| `/components/component[name]/storage/state/counters/io-seconds` | Total seconds spent doing I/Os. |
| `/components/component[name]/storage/state/counters/io-weighted-seconds` | The weighted # of seconds spent doing I/Os. |
| `/components/component[name]/storage/state/counters/read-bytes` | Number of bytes read successfully. |
| `/components/component[name]/storage/state/counters/read-seconds` | Number of seconds spent by all reads. |
| `/components/component[name]/storage/state/counters/read-ops` | Number of reads completed successfully. |
| `/components/component[name]/storage/state/counters/read-merged` | Number of reads merged. |
| `/components/component[name]/storage/state/counters/write-seconds` | Number of seconds spent by all writes. |
| `/components/component[name]/storage/state/counters/write-ops` | Number of writes completed successfully. |
| `/components/component[name]/storage/state/counters/write-merged` | Number of writes merged. |
| `/system/mount-points/mount-point[name]/state/files-total` | Filesystem total file nodes. |
| `/components/component[name]/storage/state/counters/write-bytes` | Number of bytes written successfully..|
| `/system/mount-points/mount-point[name]/state/files-available` | Filesystem total free file nodes. |
| `/system/mount-points/mount-point[name]/state/read-only` | Filesystem read-only status. |
| `/system/mount-points/mount-point[name]/state/device-error` | Whether an error occurred while getting statistics for the given device. |
| `/components/component[name=<fanid>]/fan/state/direction` | Fan direction. |
| `/components/component[name=<fanid>]/fan/state/max-speed` | Fan Maximum speed capacity. |
| `/components/component[name=<fanid>]/fan/state/min-speed` | Fan Minimum speed capacity. |
| `/components/component[name]/state/software-version` | The version of the currently running software. |

**New QoS Metrics:**

|  Name | Description |
|------ | ----------- |
| `/qos/interfaces/interface[interface-id]/priority-group/state/counters/in-pkts` | Number of received input packets for a priority group. |
| `/qos/interfaces/interface[interface-id]/state/priority-group/state/counters/in-octets` | Number of octets of input data received for a given priority group. |
| `/qos/interfaces/interface[interface-id]/switch-priority/state/counters/in-discards` | Number of discarded inbound packets. |
| `/qos/interfaces/interface[interface-id]/switch-priority/state/in-pause-duration` | Total time in microseconds packet transmission on the port has been paused. |
| `/qos/interfaces/interface[interface-id]/switch-priority/state/out-pause-duration` | Total time in microseconds that the far-end port has been requested to pause. |
| `/qos/interfaces/interface[interface-id]/output/queues/queue/state/instant-queue-len` | Transmit queue depth in bytes on traffic class selected by traffic_class of the port selected by local_port. |
| `/qos/interfaces/interface[interface-id]/output/queues/queue/state/transmit-uc-pkts` | Number of unicast packets transmitted by this queue.|

**New Interface Metrics:**

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface[name]/state/counters/carrier-up-transitions` | Total number of carrier up events on the interface. |
| `/interfaces/interface[name]/state/counters/out-hoq-drops` | Number of packets dropped at egress due to Head-of-Queue Timeout. |
| `/interfaces/interface[name]/state/counters/out-hoq-stall-drops` | Number of packets dropped at egress due to Head-of-Queue Timeout. |
| `/interfaces/interface[name]/state/counters/out-sll-drops` | Number of packets dropped at egress due to exceeding switch lifetime limit.|
| `/interfaces/interface[name]/state/counters/out-acl-drops` | Number of packets dropped at egress due to ACL policy. |
| `/interfaces/interface[name]/state/counters/out-stp-filter-drops` | Number of packets dropped at egress due to STP filter. |
| `/interfaces/interface[name]/state/counters/out-vlan-membership-drops` | Number of packets dropped at egress due to VLAN membership filter. |
| `/interfaces/interface[name]/state/counters/in-vlan-tag-allowance-drops ` | Number of packets dropped at ingress due to VLAN tag allowance filter. |
| `/interfaces/interface[name]/state/counters/in-link-down-drops` | Number of packets dropped at ingress due to egress link down. |
| `/interfaces/interface[name]/state/counters/in-vlan-membership-drops` | Number of packets dropped at ingress due to VLAN membership filter. |
| `/interfaces/interface[name]/state/counters/in-loopback-drops` | Number of packets dropped at ingress due to loopback filter. |
| `/interfaces/interface[name]/ethernet/state/counters/in-unknown-protos` | Number of MAC control frames received with an unsupported opcode. |
| `/interfaces/interface[name]/ethernet/state/counters/pkt_drop_events_probe_resource_lack` | Total number packets dropped by the probe due to lack of resources. |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-1519-2047-octets` | Total number of packets (including bad packets) received that were between 1519 and 2047 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-2048-4095-octets` | Total number of packets (including bad packets) received that were between 2048 and 4095 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-4096-8191-octets` | Total number of packets (including bad packets) received that were between 4096 and 8191 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-8192-9216-octets` | Total number of packets (including bad packets) received that were between 8192 and 10239 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/state/counters/no-buffer-mc-dropped-pkts ` | The number of multicast packets dropped due to lack of egress buffer resources. Valid only for Spectrum switches. |
| `/interfaces/interface[name]/state/counters/in-buffer-almost-full` | Number of times that the port Rx buffer passed a buffer utilization threshold. |
| `/interfaces/interface[name]/state/counters/in-buffer-full` | Number of times that the port Rx buffer reached 100% utilization. |
| `/interfaces/interface[name]/state/counters/in-ebp-pkts` | The number of received EBP packets. |
| `/interfaces/interface[name]/state/counters/out-ebp-pkts` | The number of transmitted EBP packets. |
| `/interfaces/interface[name]/state/counters/pkts-payload-internal-checksum-errors` | Number of packet payload internal checksum errors. |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-1024-1518-octets` | Total number of packets (including bad packets) transmitted that were between 1024 and 1518 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-128-255-octets` | Total number of packets (including bad packets) transmitted that were between 128 and 255 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-1519-2047-octets` | Total number of packets (including bad packets) transmitted that were between 1519 and 2047 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-2048-4095-octets` | Total number of packets (including bad packets) transmitted that were between 2048 and 4095 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-256-511-octets` | Total number of packets (including bad packets) transmitted that were between 256 and 511 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-4096-8191-octets` | Total number of packets (including bad packets) transmitted that were between 4096 and 8191 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-512-1023-octets` | Total number of packets (including bad packets) transmitted that were between 512 and 1023 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-64-octets` | Total number of packets (including bad packets) transmitted that were 64 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-65-127-octets` | Total number of packets (including bad packets) transmitted that were between 65 and 127 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-8192-9216-octets` | Total number of packets (including bad packets) transmitted that were between 8192 and 10239 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/state/counters/ecn-marked-pkts` | Count of packets marked as ECN or potentially marked as ECN |
| `/interfaces/interface[name]/state/counters/ece-marked-pkts` | Count of packets marked as ECE or potentially marked as ECE. |
| `/interfaces/interface[name]/state/counters/tx-wait` | Count of wire-speed, one-byte time intervals during which the port had data ready to transmit but did not send any data. |
| `/interfaces/interface[name]/phy/histograms/state/rs-num-corr-err[upper-boundary]/count`| Number of bit errors corrected that are less than or equal to upper boundary. |
| `/interfaces/interface[name]/phy/histograms/state/rs-num-corr-err[upper-boundary]/upper-boundary` | Upper boundary of the bin.|
| `/interfaces/interface[name]/ethernet/state/counters/out-mac-pause-frames` | Total number of MAC control frames transmitted with an opcode indicating the pause operation. |
| `/interfaces/interface[name]/ethernet/state/counters/in-maxsize-exceeded` | Total number of frames received that exceed the maximum permitted frame size. |
| `/interfaces/interface[name]/ethernet/state/counters/in-symbol-error` | Total number of received error frames due to a symbol error. |
| `/interfaces/interface[name]/ethernet/state/counters/in-fragment-frames` | Total number of packets received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad FCS with an integral number of octets (FCS error) or a bad FCS with a non-integral number of octets (alignment error). |
| `/interfaces/interface[name]/ethernet/state/counters/in-undersize-frames` | Total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed. |

**New Routing Metrics:**

|  Name | Description |
|------ | ----------- |
| `/tables/table[address-family=IPV4][protocol=BGP]/state/route-count` | IPv4 BGP route count in RIB. |
| `/tables/table[address-family=IPV6][protocol=BGP]/state/route-count` | IPv6 BGP route count in RIB. |
| `/tables/table[address-family=IPV4][protocol=DIRECTLY_CONNECTED]/state/route-count` | IPv4 connected route count. |
| `/tables/table[address-family=IPV6][protocol=DIRECTLY_CONNECTED]/state/route-count` | IPv6 connected route count. |
| `/tables/table[address-family=IPV4][protocol=STATIC]/state/route-count` | IPv4 static route count. |
| `/tables/table[address-family=IPV6][protocol=STATIC]/state/route-count` | IPv6 static route count. |
| `/tables/table[address-family=IPV4][protocol=OSPF]/state/route-count` | IPv4 OSPF route count in RIB. |
| `/tables/table[address-family=IPV6][protocol=OSPF]/state/route-count` | IPv6 OSPF route count in RIB. |
| `/tables/table[address-family=IPV4][protocol=KERNEL]/state/route-count` | IPv4 kernel route count. |
| `/tables/table[address-family=IPV6][protocol=KERNEL]/state/route-count` | IPv6 kernel route count. |
| `/tables/table[address-family=IPV4][protocol=POLICY_BASED_ROUTING]/state/route-count` | IPv4 PBR route count.|
| `/tables/table[address-family=IPV6][protocol=POLICY_BASED_ROUTING]/state/route-count` | IPv6 PBR route count.|
| `/tables/table[address-family=IPV4][protocol=TABLE_CONNECTION]/state/route-count` | IPv4 table connection route count.|
| `/tables/table[address-family=IPV6][protocol=TABLE_CONNECTION]/state/route-count` | IPv6 table connection route count.|
| `/network-instances/network-instance/tables/state/ipv4-route-count` | Total IPv4 route count.|
| `/network-instances/network-instance/tables/state/ipv6-route-count` | Total IPv6 route count.|
| `/network-instances/network-instance/tables/state/rib-nexthop-group-count` | Nexthop group count.|
{{< /expand >}}
   - {{< expand "Updated gNMI PHY metric names" >}}
Old Name | New Name|
| -------- | --------- |
| `/interfaces/interface[name]/ethernet/phy/state/effective-errors` | `/interfaces/interface[name]/phy/state/effective-errors` |
| `/interfaces/interface[name]/ethernet/phy/state/received-bits` | `/interfaces/interface[name]/phy/state/received-bits` |
| `/interfaces/interface[name]/ethernet/phy/state/symbol-errors` | `/interfaces/interface[name]/phy/state/symbol-errors` |
| `/interfaces/interface[name]/ethernet/phy/state/fec-time-since-last-clear` | `/interfaces/interface[name]/phy/fec/state/fec-time-since-last-clear` |
| `/interfaces/interface[name]/ethernet/phy/state/corrected-bits` | `/interfaces/interface[name]/phy/fec/state/corrected-bits` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-no-error-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-no-error-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-single-error-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-single-error-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-uncorrectable-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-uncorrectable-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/ber-time-since-last-clear` | `/interfaces/interface[name]/phy/ber/state/ber-time-since-last-clear` |
| `/interfaces/interface[name]/ethernet/phy/state/effective-ber` | `/interfaces/interface[name]/phy/ber/state/effective-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/symbol-ber` | `/interfaces/interface[name]/phy/ber/state/symbol-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/fc-fec-corrected-blocks` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/fc-fec-corrected-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/fc-fec-uncorrected-blocks` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/fc-fec-uncorrected-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/rs-fec-corrected-symbols` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/rs-fec-corrected-symbols` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/raw-ber` | `/interfaces/interface[name]/phy/channels/channel[id]/ber/state/raw-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/raw-errors` | `/interfaces/interface[name]/phy//channels/channel[id]/state/raw-errors` |
{{< /expand >}}
   - {{< expand "Deprecated OTEL Metrics" >}}
|  Name | Removal Reason |
|------ | ----------- |
| `nvswitch_interface_discards_egress_link_down` | Unsupported on Spectrum switches. |
| `nvswitch_interface_discards_ingress_discard_all` | Unsupported on Spectrum switches. |
| `nvswitch_interface_discards_port_isolation` | Unsupported on Spectrum switches. |
| `nvswitch_interface_dot3_stats_alignment_errors` | Unsupported on Spectrum switches. |
| `nvswitch_interface_dot3_stats_excessive_collisions` | Unsupported on Spectrum switches. |
| `nvswitch_interface_dot3_stats_internal_mac_receive_errors` | Unsupported on Spectrum switches. |
| `nvswitch_interface_dot3_stats_internal_mac_transmit_errors` | Unsupported on Spectrum switches. |
| `nvswitch_interface_dot3_stats_late_collisions` | Unsupported on Spectrum switches. |
| `nvswitch_interface_dot3_stats_multiple_collision_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_dot3_stats_single_collision_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_dot3_stats_sqe_test_errors` | Unsupported on Spectrum switches. |
| `nvswitch_interface_ether_stats_collisions` | Unsupported on Spectrum switches. |
| `nvswitch_interface_if_in_unknown_protos` | Unsupported on Spectrum switches. |
| `nvswitch_interface_pg_rx_buffer_discard` | Unsupported on Spectrum switches. |
| `nvswitch_interface_pg_rx_shared_buffer_discard` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_rx_bc_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_rx_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_rx_mc_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_rx_octets` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_rx_pause_transition` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_rx_uc_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_tx_bc_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_tx_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_tx_mc_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_tx_octets` | Unsupported on Spectrum switches. |
| `nvswitch_interface_sp_tx_uc_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_tc_tx_bc_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_tc_tx_mc_frames` | Unsupported on Spectrum switches. |
| `nvswitch_interface_discards_egress_general` | Duplicate of `nvswitch_interface_if_out_discards` |
| `nvswitch_interface_discards_ingress_general` | Duplicate of `nvswitch_interface_if_in_discards` |
| `nvswitch_interface_if_in_broadcast_pkts` | Duplicate of `nvswitch_interface_ether_stats_broadcast_pkts` |
| `nvswitch_interface_if_in_multicast_pkts` | Duplicate of `nvswitch_interface_ether_stats_multicast_pkts` |
| `nvswitch_interface_if_in_octets` | Duplicate of `nvswitch_interface_ether_stats_octets` |
{{< /expand >}}
- NVUE
  - {{<link url="Secure-Mount-Directory-Encryption" text="Secure Mount Directory Encryption">}}
  - {{<link url="New-and-Changed-NVUE-Commands" text="Changed command syntax and output">}}
  - `--expand` option for {{<link url="NVUE-CLI/#view-differences-between-configurations" text="nv config diff command">}}, {{<link url="NVUE-CLI/#show-switch-configuration" text="nv config show command">}}, and {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="nv config find command">}}
  - `expand=true` parameter for API calls to {{<link url="NVUE-API/#view-differences-between-configurations" text="View differences between configurations">}}, {{<link url="NVUE-API/#view-a-configuration" text="view a configuration">}}, and {{<link url="NVUE-API/#use-filters-in-a-query" text="search for a specific configuration">}}
  - Aging time added to {{<link url="Address-Resolution-Protocol-ARP/#show-the-arp-table" text="IPv4">}} and {{<link url="Neighbor-Discovery-ND/#show-the-ip-neighbor-table" text="IPv6">}} neighbor tables
  - {{<link url="System-Power-and-Switch-Reboot/" text="Switch reboot options changed">}} from configured reboot modes to NVUE reboot action commands
  - Timestamp format in `nv show` command output changed from UTC to duration (days, hour:minutes:seconds)
  - {{<link url="NVUE-API/#patch-a-batch-of-configuration-commands" text="Batch execution support for patching in CLI commands through the API">}}. This feature also improves performance when patching in text commands {{<link url="NVUE-CLI/#replace-and-patch-a-pending-configuration" text="through the CLI">}}.
  - Improved command completion when using tab to view CLI command options

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.15.

### New, Changed, and Deprecated NVUE Commands

{{%notice warning%}}
To align with a long-term vision of a common interface between Cumulus Linux, Nvidia OS (NVOS), and Host-Based Networking, many NVUE commands in Cumulus Linux 5.15 have changed. Before you upgrade to 5.15, review the list of {{<link url="New-and-Changed-NVUE-Commands" text="New, Changed, and Deprecated NVUE Commands">}} and be sure to make any necessary changes to your automation.
{{%/notice%}}

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} to upgrade the switch to Cumulus Linux 5.15 from Cumulus Linux 5.12 and later.

You can use {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.15 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- Cumulus Linux 5.14.0
- Cumulus Linux 5.13.1
- Cumulus Linux 5.13.0

To upgrade to Cumulus Linux 5.15 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.15 from 5.12, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.15.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.15 or after a new binary image installation:

1.  Disable NVUE auto save:

   ```
   cumulus@switch:~$ nv set system config auto-save state disabled
   cumulus@switch:~$ nv config apply
   cumulus@switch:~$ nv config save
   ```

2. Delete the `/etc/nvue.d/startup.yaml` file:

   ```
   cumulus@switch:~$ sudo rm -rf /etc/nvue.d/startup.yaml
   ```

3. Add the `PASSWORD_NVUE_SYNC=no` line to the `/etc/default/nvued` file:
   ```
   cumulus@switch:~$ sudo nano /etc/default/nvued
   PASSWORD_NVUE_SYNC=no
   ```

### DHCP Lease with the host-name Option

When a Cumulus Linux switch with NVUE enabled receives a DHCP lease containing the host-name option, it ignores the received hostname and does not apply it. For details, see this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Hostname-Option-Received-From-DHCP-Ignored" >}}).

### NVUE Commands After Upgrade

After you upgrade to Cumulus Linux, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA AIR">}}.
