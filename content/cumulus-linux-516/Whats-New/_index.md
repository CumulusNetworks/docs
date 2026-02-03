---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.16 release, and lists new features and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.16, see the {{<link title="Cumulus Linux 5.16 Release Notes" text="Cumulus Linux 5.16 Release Notes">}}.
- To upgrade to Cumulus Linux 5.16, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.16

Cumulus Linux 5.16 contains new features and improvements, and provides bug fixes.

### New Features and Enhancements

- {{<link url="Bidirectional-Forwarding-Detection-BFD/#bfd-offload" text="BFD offload">}}
- {{<link url="Optional-BGP-Configuration/#bgp-conditional-disaggregation" text="BGP conditional disaggregation">}}
- {{<link url="Optional-BGP-Configuration/#bgp-pic-anycast" text="BGP PIC anycast">}}
- {{<link url="802.1X-Interfaces/#preserve-dynamically-assigned-ipv6-addresses" text="802.1X preserve dynamically assigned IPv6 addresses">}}
- {{<link url="Understanding-the-cl-support-Output-File/#automatic-cl-support-file" text="Manage automatic cl-support file generation">}}
- {{<link url="Network-Troubleshooting/#extended-traceroute" text="Extended traceroute (RFC 5837)">}}
- {{<link url="DHCP-Relays/#dhcp-relay-for-ipv4-in-an-evpn-symmetric-environment-with-mlag" text="VRF-aware DHCP relay">}}
- {{<link url="Routing-Tables/#show-fib-table-entries" text="Show FIB table entries">}}
- {{<link url="Access-Control-List-Configuration/#match-on-inner-header" text="ACL matches on packet inner header">}} and {{<link url="Access-Control-List-Configuration/#match-on-packet-offset" text="ACL matches on packet offset">}}
- {{<link url="Quality-of-Service/#clear-qos-buffers" text="Clear QoS buffers on multiple interfaces">}}
- {{<link url="TACACS/#tacacs-per-command-authorization" text="TACACS per-command authorization supports NVUE tab completion, option listing (?), and command history navigation">}}
- {{<link url="Access-Control-List-Configuration/#clear-control-plane-policer-counters" text="Clear control plane policer counters">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#lag-hash-randomizer" text="LAG hash randomizer for adaptive routing">}}
- {{<link url="Interface-Configuration-and-Management/#tx-squelch-control" text="Tx squelch control">}} (Beta)
- {{<link url="Ethernet-Virtual-Private-Network-EVPN/#key-features" text="Support for EVPN VXLAN over an IPv6 underlay">}} (Beta)
- {{<link url="802.1X-Interfaces/#dynamic-vrf-assignment" text="802.1x dynamic VRF assignment">}} (Beta)
- {{<link url="Quality-of-Service/#shaping" text="PPS mode for QoS egress shapers">}}
- {{<link url="Quality-of-Service/#extra-lossy-headroom" text="Extra threshold for QoS lossy priority groups">}}
- {{<link url="FRRouting-Log-Message-Reference" text="New FRR high severity ERROR log messages">}}
- {{<link url="Monitoring-System-Hardware/#health-monitoring-reference" text="The SDK health monitoring service handles recovery and debug dump collection when detecting SDK health issues">}}
- {{<link url="NVUE-CLI/#replace-and-patch-a-pending-configuration" text="NVUE support for both unset and set commands for the same object in a single patch">}}
- Security features:
  - {{<link url="FIPS" text="FIPS mode">}}
  - {{<link url="SSH-for-Remote-Access/#configure-timeouts-and-sessions" text="Maximum SSH sessions allowed for a user and     for a user group">}}
  - {{<link url="TACACS/#local-fallback-authentication" text="NVUE support for TACACS local fallback authentication">}}
  - {{<link url="802.1X-Interfaces/#802.1x-reauthentication" text="802.1X reauthentication">}}
  - {{<link url="RADIUS-AAA/#required-radius-client-configuration" text="Yubikey authentication over RADIUS">}}
  - {{<link url="Syslog/#enable-secured-logs" text="Configure syslog messages">}} to include the date and time events occur, the source IP and username for NVUE commands, and when dynamic kernel modules load and unload
  - {{<link url="NVUE-API/#http-response-compression" text="HTTP response compression for API reponses">}}
- Telemetry
  - You can now use {{<link url="Open-Telemetry-Export" text="Open telemetry export">}} and {{<link url="gNMI-Streaming" text="gNMI streaming">}} at the same time.
  - {{< expand "New gNMI Metrics:" >}}

**802.1X:**

|  Name | Description |
|------ | ----------- |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/priority` | Radius server priority 1, 2 or 3. Lower number indicates higher priority. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/auth-port` | The port used for authentication and authorization. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/acct-port` | The port used for RADIUS accounting. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/vrf` | The VRF that contains the RADIUS server.|
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/source-address` | The source IP address for RADIUS authentication requests. If not configured, the address defaults to the IP address of the interface used to reach the RADIUS server, as determined by the kernel routing table. You can configure the address with the NVUE `client-src-ip` parameter. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/auth-type` | EAP authentication method (MD5, TLS, TTLS, PEAP, and so on). |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/vlan` | VLAN on which the supplicant connects to the switch and tries to authenticate. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/session-id` | 64 bytes/512 bit session ID. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/status` | Supplicant status. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/out-eapol-req-frames` | A count of all EAP request frames sent from the switch to the supplicant. Includes EAP request or OTP and any other challenge messages forwarded from the RADIUS Access Challenge. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-resp-frames` | Counts all EAP response frames received from the Supplicant identified by the MAC address to the switch. Includes responses carrying credentials, leading to RADIUS Access request and eventual Access accept. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/out-eapol-req-id-frames` | Counts EAP request identity frames sent from the switch to the Supplicant. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-start-frames` | Counts EAPOL start frames received from this Supplicant. This is the very first message when the client initiates the authentication process for the session. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-logoff-frames` | Counts EAPOL logoff frames received from this Supplicant. The client terminates the authenticated session, causing the port to transition from an `Authorized` to an `Unauthorized` state. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-invalid-frames` | Counts malformed or invalid EAPOL frames received from the Supplicant. These are error counters for frames that do not comply with the protocol. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-len-err-frames` | Counts EAPOL frames received from this Supplicant that have an incorrect length. These frames are discarded and counted as protocol errors for this session. |
| `/system/dot1x/state/reauth-timeout-ignore` | If enabled and if there is a reauthentication timeout with the RADIUS server, the timeout is ignored as long as the supplicant is currently in the authenticated state. |
| `/system/dot1x/state/dynamic-vlan` | Dynamic VLAN assignment mode with three states: required (RADIUS must assign a VLAN for authorization), optional (VLAN assignment is optional), or disabled (Dynamic VLAN feature is off). Default is disabled. |
| `/system/dot1x/state/max-stations` | The maximum number of authenticated MAC addresses allowed on a port. The default is 6. The range is between 1 and 255. |
| `/system/dot1x/state/dynamic-ipv6-multi-tenant` | Must be set to `enabled` for dynamic IPv6 multi-tenancy to be enabled. |  
| `/system/dot1x/radius/state/nas-ip-address` | The IP address used for accounting purposes by Cumulus Linux as a RADIUS client or NAS (Network Access Server) while communicating when a RADIUS server. This IP address is used in the initial Access-Request packet and is useful on the RADIUS server for accounting and not as a source IP address in packet to the RADIUS server. |
| `/system/dot1x/radius/state/nas-identifier` | Identifies the RADIUS client to a RADIUS server together with the NAS IP address. The NAS IP address is useful for accounting on the RADIUS server. |
| `/interfaces/interface[name]/ethernet/dot1x/state/eap` | If 802.1X is enabled or disabled on the interface. |
| `/interfaces/interface[name]/ethernet/dot1x/state/mba` | If MAC-based authentication (MBA) is enabled or disabled on the interface. |
| `/interfaces/interface[name]/ethernet/dot1x/state/host-mode` | The mode can be either multi-host or multi-host-authenticated. In multi-host mode, only the first host that connects to a dot1x (eap enabled) interface needs to be authenticated and any subsequent hosts do not. In multi-host-authenticated (MHA) mode, each and every host connecting to an interface needs to be authorized. MHA is the default host-mode. |
| `/interfaces/interface[name]/ethernet/dot1x/state/port-id` | The port ID is a unique 16-bit identifier for each interface that defaults to the last two bytes of the interface's MAC address or can be user-configured. The port ID is encoded into dynamically generated IPv6 addresses at the profile-specified offset, allowing the IPv6 address to identify which physical port authenticated each client for per-port tenant segmentation and routing policies. |
| `/interfaces/interface[name]/ethernet/dot1x/state/ipv6-profile` | The IPv6 profile associated with this interface. |
| `/interfaces/interface[name]/ethernet/dot1x/state/reauthenticate-interval` |  The recurring interval in seconds after which all already authenticated supplicants reauthenticate. By default, the interval is 0 (no reauthentication). |
| `/interfaces/interface[name]/ethernet/dot1x/state/auth-fail-vlan` | If auth-fail VLAN is configured. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/offset-in-bits` | Offset in bits from the beginning of the 64 bit IPv6 profile. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/length-in-bits` | The length of the property in bits. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/property-value` | The VSA ID, port ID, an integer or a hexadecimal value. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/isolation-property` | Enabled if this property is used for isolation (multi-tenancy). Setting this flag causes ACLs to be programmed. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/summarize-out` | If enabled, the summary route be advertised. There can be only one property in an IPv6 profile with the `summarize-out` label enabled. |
| `/system/dot1x/ipv6-profiles/profile[name]/state/route-tag` | Associates a policy tag with routes learned through this 802.1X IPv6 profile, allowing routing policy, redistribution control, and tenant isolation for the authenticated sessions. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/ipv6-prefix` |  The IPv6 prefix generated from all the IPv6 profile properties. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/counters/reauth-timeouts` | Counter that keeps track of authentication failures because the RADIUS server is unreachable after a successful authentication when the `reauth-timeout-ignore` option is enabled. |

**QoS Buffer:**

|  Name | Description |
|------ | ----------- |
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the priority group on the interface. |
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the priority group on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/max-occupancy-timestamp` |  Timestamp at which the highest shared‑buffer occupancy for the priority group on the interface was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the priority‑group descriptor on the interface.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the priority‑group descriptor on the interface during the most recent sampling interval. |
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the priority‑group descriptor on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the interface priority‑group descriptor was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the interface priority‑group descriptor were last cleared.|
|`/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/time-since-last-clear`| Elapsed time in milliseconds since watermark counters for the interface priority‑group were last cleared.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the interface traffic‑class queue were last cleared.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/counters/in-pkts` | The number of packets received at Ingress for a given priority group.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/counters/in-octets` | The number of octets of data received at Ingress for a given priority group.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the priority‑group on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the interface traffic‑class queue.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the traffic‑class queue on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the interface traffic‑class queue since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the interface traffic‑class queue was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the interface traffic‑class queue were last cleared.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the traffic‑class queue descriptor on the interface.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the interface traffic‑class queue descriptor during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the interface traffic‑class queue descriptor since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the interface traffic‑class queue descriptor was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the interface traffic‑class queue descriptor were last cleared.|
| `qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the interface ingress pool.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the interface ingress pool during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the interface ingress pool since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the interface ingress pool was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the interface ingress pool were last cleared.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the interface ingress‑pool descriptor.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the interface ingress‑pool descriptor during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the interface ingress‑pool descriptor since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the interface ingress‑pool descriptor was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the interface ingress‑pool descriptor were last cleared.|
| `/qos/interfaces/interface[interface-id]/ouput/pools/pool[id]/state/shared-buffer/data/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the interface egress pool.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/data/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the interface egress pool during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/data/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the interface egress pool since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/data/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the interface egress pool was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/data/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the interface egress pool were last cleared.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the interface egress‑pool descriptor.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the interface egress‑pool descriptor during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the interface egress‑pool descriptor since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the interface egress‑pool descriptor was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the interface egress‑pool descriptor were last cleared.|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for multicast traffic on the interface.|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for multicast traffic on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/max-occupancy` | Maximum shared‑buffer occupancy in bytes for multicast traffic on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for multicast traffic on the interface was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for multicast traffic on the interface were last cleared.|
| `/qos/shared-buffer/switch-priority[priority]/state/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for multicast traffic in the specified switch priority.|
| `/qos/shared-buffer/switch-priority[priority]/state/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for multicast traffic in the specified switch priority during the most recent sampling interval.|
| `/qos/shared-buffer/switch-priority[priority]/state/max-occupancy` | Maximum shared‑buffer occupancy in bytes for multicast traffic in the specified switch priority since the last watermark reset; software‑maintained.|
| `/qos/shared-buffer/switch-priority[priority]/state/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for multicast traffic in the specified switch priority was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/shared-buffer/switch-priority[priority]/state/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for multicast traffic in the specified switch priority were last cleared.|
| `/qos/shared-buffer/pools/pool[id]/state/data/instant-occupancy` | Instantaneous shared‑buffer occupancy in bytes for the given pool. This metric replaces `/qos/shared-buffer/pools/pool[id]/state/instant-occupancy` in previous releases. |
| `/qos/shared-buffer/pools/pool[id]/state/data/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy in bytes for the given pool during the most recent sampling interval. This metric replaces `/qos/shared-buffer/pools/pool[id]/state/max-occupancy-since-last-sample` in previous releases.|
| `/qos/shared-buffer/pools/pool[id]/state/data/max-occupancy` | Maximum shared‑buffer occupancy in bytes for the given pool since the last watermark reset; software‑maintained. This metric replaces `/qos/shared-buffer/pools/pool[id]/state/max-occupancy` in previous releases.|
| `/qos/shared-buffer/pools/pool[id]/state/data/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the given pool was recorded since the last watermark reset. Value is Unix epoch seconds (UTC). This metric replaces `/qos/shared-buffer/pools/pool[id]/state/max-occupancy-timestamp` in previous releases.|
| `/qos/shared-buffer/pools/pool[id]/state/data/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the given pool were last cleared. This metric replaces `/qos/shared-buffer/pools/pool[id]/state/time-since-last-clear` in previous releases.|
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/instant-occupancy` | Instantaneous shared‑buffer occupancy as number of descriptors for the given pool. |
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/max-occupancy-since-last-sample` | Maximum shared‑buffer occupancy as number of descriptors for the given pool during the most recent sampling interval. |
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/max-occupancy` | Maximum shared‑buffer occupancy as number of descriptors for the given pool since the last watermark reset; software‑maintained. |
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/max-occupancy-timestamp` | Timestamp at which the highest shared‑buffer occupancy for the given pool was recorded since the last watermark reset. Value is Unix epoch seconds (UTC). |
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the given pool were last cleared. |
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/instant-occupancy` | Instantaneous headroom-buffer occupancy in bytes for the specified buffer type (primary or secondary) in the priority group on the interface.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/max-occupancy-since-last-sample` | Maximum headroom‑buffer occupancy in bytes for the specified buffer type (primary or secondary) in the priority group on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/max-occupancy` | Maximum headroom‑buffer occupancy in bytes for the specified buffer type (primary or secondary) in the priority group on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/max-occupancy-timestamp` | Timestamp at which the highest headroom‑buffer occupancy for the specified buffer type (primary or secondary) in the priority group on the interface was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the specified buffer type (primary or secondary) in the priority group on the interface were last cleared.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/instant-occupancy` | Instantaneous headroom-buffer occupancy in bytes for the specified buffer type (primary or secondary) on the interface.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/max-occupancy-since-last-sample` | Maximum headroom‑buffer occupancy in bytes for the specified buffer type (primary or secondary) on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/max-occupancy` | Maximum headroom‑buffer occupancy in bytes for the specified buffer type (primary or secondary) on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/max-occupancy-timestamp` | Timestamp at which the highest headroom‑buffer occupancy for the specified buffer type (primary or secondary) on the interface was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/time-since-last-clear` | Elapsed time in milliseconds since watermark counters for the specified buffer type (primary or secondary) on the interface were last cleared.|
| `/qos/shared-buffer/state/cell-size` | Shared‑buffer allocation cell size in bytes; use to convert cell‑based counters to bytes.|

**Control Plane Policer:**

|  Name | Description |
|------ | ----------- |
|`/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/counters/buffer-drops` | Control plane receive buffer drops.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/counters/rx-bytes` | Control plane receive bytes.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/counters/rx-packets` | Control plane trap group receive packets.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/egress/counters/types/type[type]/tx-bytes` | Control plane transmit bytes.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/egress/counters/types/type[type]/tx-packets` | Control plane receive packets.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/counters/pkt-violations` | Control plane trap group packet violations.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/counters/rx-bytes` | Control plane trap group receive bytes.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/counters/rx-packets` | Control plane trap group receive packets.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/traps/trap[id]/counters/rx-bytes` | Control plane trap group receive bytes.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/traps/trap[id]/counters/rx-drops` | Control plane trap group receive drops.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/traps/trap[id]/counters/event-count` | Control plane trap group receive events.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/traps/trap[id]/counters/rx-packets` | Control plane trap group receive packets.|

**Interface:**

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface[name]/state/description`| The interface description.|
| `/interfaces/interface[name]/state/transceiver` | The transceiver on the interface. |

**Histogram:**

|  Name | Description |
|------ | ----------- |
| `/performance/interfaces/interface[name]/histograms/egress-buffer/traffic-class[tc][upper-boundary]/count`  | Histogram interface egress buffer queue depth.|
| `/performance/interfaces/interface[name]/histograms/ingress-buffer/priority-group[pg][upper-boundary]/count` | Histogram interface ingress buffer queue depth.|
| `/performance/interfaces/interface[name]/histograms/counter/counter-type[type][upper-boundary]/count` | Histogram interface counter data.|
| `/performance/interfaces/interface[name]/histograms/latency/traffic-class[tc][upper-boundary]/count` | Histogram interface latency data.|
{{< /expand >}}
   - {{< expand "Deprecated gNMI Metrics" >}}
|  Name | Removal Reason |
|------ | ----------- |
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/max-queue-len-cells` | New metric to get the cell size (`/qos/shared-buffer/state/cell-size`) |

{{< /expand >}}
   - {{< expand "New OTEL Metrics" >}}

**802.1X:**

| Name | Description |
|----- | ----------- |
| `nvswitch_dot1x_system_info` | Global 802.1X configuration (dynamic VLAN mode, dynamic IPv6 multi-tenant state, max stations per port, auth-fail VLAN ID, reauth-timeout-ignore state, reauthentication interval). |
| `nvswitch_dot1x_radius_client_info` | RADIUS client configuration (NAS identifier, NAS IP address, source IP). |
| `nvswitch_dot1x_radius_server_info` | RADIUS server configuration (IP address, authentication port, accounting port, priority, VRF). |
| `nvswitch_dot1x_supplicant_summary` | Summary showing MAC address, interface, authentication type, VLAN assignment, and session ID of each authenticated supplicant. |
| `nvswitch_dot1x_supplicant_eapol_counters` | EAPOL frame counters per supplicant, including start, logoff, request, response, invalid, and length-errored frames. |  
| `nvswitch_dot1x_interface_info` | Per-interface 802.1X configuration (EAP, MBA, host mode, port-id, IPv6 profile, auth-fail VLAN).|
| `nvswitch_dot1x_supplicant_status` | Authentication status of the supplicant. |
| `nvswitch_dot1x_ipv6_profile_info` | IPv6 profile configuration (profile name and route tag). | 
| `nvswitch_dot1x_ipv6_profile_property_info` | IPv6 profile property configuration (offset, length, value, isolation, summarization). |
| `nvswitch_dot1x_ipv6_profile_summary` | IPv6 prefix generated for each layer 3 authenticated session that is using an IPv6 profile. |
| `nvswitch_dot1x_reauth_timeouts` | Counter of reauthentication attempts with the RADIUS server that timed out but were ignored, keeping the supplicant in Authorized state when the `reauth-timeout-ignore` flag is enabled. |

**Buffer:**

| Name | Description |
|----- | ----------- |
| `nvswitch_shared_buffer_pool_desc_curr_occupancy` |  Current shared buffer occupancy as number of descriptors for the given pool.|
| `nvswitch_shared_buffer_pool_desc_watermark` | Maximum shared buffer occupancy for descriptors. |
| `nvswitch_shared_buffer_pool_desc_watermark_recorded_max` | Highest maximum shared buffer watermark for descriptors. |
| `nvswitch_shared_buffer_pool_desc_watermark_recorded_max_timestamp` | Time when the highest shared buffer descriptor watermark is recorded. |
| `nvswitch_shared_buffer_pool_desc_time_since_clear` | Time in milliseconds after shared buffer descriptor watermarks are last cleared.  |
{{< /expand >}}
   - {{< expand "Deprecated OTEL Metrics" >}}
|  Name | Removal Reason |
|------ | ----------- |
| `nvswitch_interface_shared_buffer_port_tc_watermark_recorded_max_bytes` | Deprecated.|
{{< /expand >}}

For a list of new NVUE commands, refer to {{<link url="New-and-Removed-NVUE-Commands" text="New and Removed NVUE Commands">}}.

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.16.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.16 from Cumulus Linux 5.14 and later. Package upgrade supports ISSU (warm boot) for these upgrade paths.

To upgrade to Cumulus Linux 5.16 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.16 from 5.12 or earlier, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.16.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.16 or after a new binary image installation:

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
