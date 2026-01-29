---
title: gNMI Streaming
author: NVIDIA
weight: 1234
toc: 4
---
You can use {{<exlink url="https://github.com/openconfig/gnmi" text="gRPC Network Management Interface">}} (gNMI) to collect system metrics and export the data to a gNMI client.

Cumulus Linux supports:
- {{<link url="/#gnmi-with-cumulus-linux" text="gNMI with Cumulus Linux">}}, where Cumulus Linux includes the gNMI agent that listens over port 9339.
- {{<link url="/#gnmi-with-netq" text="gNMI with NetQ">}}, where the `netq-agent` package includes the gNMI agent that listens over port 9339.

{{%notice note%}}
To use both gNMI streaming with Cumulus Linux and gNMI streaming with NetQ, you must use different ports.
{{%/notice%}}

## gNMI with Cumulus Linux

This section discusses how to configure and use gNMI with Cumulus Linux. To configure and use gNMI with NetQ, see {{<link url="/#gnmi-with-netq" text="gNMI with NetQ">}}.

{{%notice note%}}
Switches with the Spectrum 1 ASIC do not support gNMI streaming.
{{%/notice%}}
<!--
{{%notice note%}}
- When you enable gNMI with Cumulus Linux, do **not** enable and use {{<link url="Open-Telemetry-Export" text="Open Telemetry">}}.
- Switches with the Spectrum 1 ASIC do not support gNMI streaming.
{{%/notice%}}
-->
Cumulus Linux supports both gNMI dial-in mode, where a collector can start a connection with the switch to collect available statistics, and gNMI dial-out mode, where the switch streams statistics and exports them to a collector.

### Configure gNMI Dial-in Mode

In dial-in telemetry mode, the data collector initiates the <span class="a-tooltip">[gRPC](## "Remote Procedure Calls")</span> connection, the Cumulus Linux switch assumes the role of the gRPC server and the receiver (collector) is the client. The switch pushes data to the collector.

To configure gNMI dial-in mode, you must:
- Specify the gNMI server listening address
- Enable the gNMI server.

To configure optional settings for gNMI dial-in mode:
- Specify the listening port. The default port is 9339.
- Enable a TLS certificate for validation.
  - Cumulus Linux uses a self-signed certificate. You can generate your own TLS server certificate and bind it with the gNMI server application.
  - If you need to use mTLS on the gNMI RPC, import the certificate of the CA that signed the gNMI client keys (or the client certificate itself) to the switch and configure the gNMI server to use the certificate. You can also apply a <span class="a-tooltip">[CRL](## "Certificate Revocation List")</span>. Specify either `uri` (a local or remote URI from where to retrieve the crl bundle file) or `data` (for a PEM encoded CRL).

{{%notice note%}}
When you configure a CA certificate, entity certificate, or CRL, the configuration will apply to any new gNMI sessions that establish. Existing dial-in connections will continue to use the prior configuration until they reestablish.
{{%/notice%}}

The following example sets the gNMI server listening address to 10.10.10.1 and the port to 443, and enables the gNMI server:

```
cumulus@switch:~$ nv set system gnmi-server listening-address 10.10.10.1
cumulus@switch:~$ nv set system gnmi-server port 443
cumulus@switch:~$ nv set system gnmi-server state enabled
cumulus@switch:~$ nv config apply
```

The following example imports and sets the CA certificate `CERT1` and the CRL `crl.crt` for mTLS:

```
cumulus@switch:~$ nv action import system security ca-certificate CERT1 passphrase mypassphrase uri-bundle scp://user@pass:1.2.3.4:/opt/certs/cert.p12
cumulus@switch:~$ nv set system gnmi-server mtls ca-certificate CERT1
cumulus@switch:~$ nv action import system security crl uri scp://user:password@hostname/path/crl.crt
cumulus@switch:~$ nv set system gnmi-server mtls crl /etc/ssl/certs/crl.crt
cumulus@switch:~$ nv config apply
```

### Configure gNMI Dial-out Mode

In dial-out telemetry mode, the Cumulus Linux switch initiates the gRPC connection to the collector through a gRPC tunnel server and assumes the role of the gRPC client.

To configure gNMI dial-out mode, you must:
- Specify the listening address for each tunnel server to which you want to connect. Cumulus Linux supports a maximum of 10 tunnel servers.
- Enable the tunnel server.

To configure optional settings for each tunnel server:
- Specify the target name and target application you want to access. The default target application is GNMI-GNOI.
- Specify the retry interval. The default retry interval is 30 seconds.
- Import and enable a TLS or mTLS certificate for validation. You can also apply a <span class="a-tooltip">[CRL](## "Certificate Revocation List")</span>. For information about importing certificates and CRLs, refer to {{<link url="NVUE-CLI/#security-with-certificates-and-crls" text="Security with Certificates and CRLs">}}.

{{%notice note%}}
When you configure a CA certificate, entity certificate, or CRL, existing dial-out gNMI sessions are disconnected to apply the new certificate configuration.
{{%/notice%}}

The following example sets the listening address for tunnel server SERVER1 to 10.1.1.10, and enables the tunnel server:

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 address 10.1.1.10 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 state enabled 
cumulus@switch:~$ nv config apply
```

The following example sets the listening address for tunnel server SERVER1 to 10.1.1.10 and the port to 443, the target name to TARGET1, the retry interval to 40, the CA certificate to CACERT1, and enables the tunnel server:

```
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 address 10.1.1.10 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 port 443 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 target-name TARGET1 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 retry-interval 40
cumulus@switch:~$ nv action import system security ca-certificate CACERT1 uri-public-key scp://user@pass:1.2.3.4:/opt/certs/ca-cert.pem uri-private-key scp://user@pass:1.2.3.4:/opt/certs/ca-cert-key.pem
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 ca-certificate CACERT1
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 state enabled 
cumulus@switch:~$ nv config apply
```

### Show gNMI Configuration and Status Information

To show gNMI server configuration and connection information, such the number of active subscriptions, received and rejected subscription requests, and received capability requests, run the `nv show system gnmi-server` command.

```
cumulus@switch:~$ nv show system gnmi-server 
                                  operational  applied    
--------------------------------  -----------  -----------
state                             disabled     enabled   
certificate                       self-signed  self-signed
port                              9339         9339
[listening-address]               10.1.1.100   10.1.1.100        
version                                                   
status                                                    
  total-active-subscriptions      0                       
  received-subscription-requests  0                       
  rejected-subscriptions          0                       
  received-capabilities-requests  0                       
  [client]
```

To show the listening address of the gNMI server, run the `nv show system gnmi-server listening-address` command:

```
cumulus@switch:~$ nv show system gnmi-server listening-address
----------
10.1.1.100
```

To show gNMI server mTLS information, run the `nv show system gnmi-server mtls` command:

```
cumulus@switch:~$ nv show system gnmi-server mtls
                operational  applied  pending         
--------------  -----------  -------  ----------------
ca-certificate  CACERT1       CACERT1   CACERT          
crl                                   abcdefghijklmnop
```

To show only gNMI server connection information, run the `nv show system gnmi-server status` command:

```
cumulus@switch:~$ nv show system gnmi-server status
                                operational
------------------------------  -----------
total-active-subscriptions      0          
received-subscription-requests  0          
rejected-subscriptions          0          
received-capabilities-requests  0
```

To show gRPC tunnel server configuration and connection information, run the `nv show system grpc-tunnel server <server>` command:

```
cumulus@switch:~$ nv show system grpc-tunnel server SERVER1
nv show system grpc-tunnel server SERVER1
                 operational           applied  
---------------  --------------------  ---------
state            disabled              enabled  
target-name      TARGET1               TARGET1  
address          10.1.1.10             10.1.1.10
port             443                   443      
target-type      gnmi-gnoi             gnmi-gnoi
retry-interval   40                    40       
status                                          
  local-port     0                              
  remote-port    0                              
  connection                                    
    established  1970-01-01T00:00:00Z           
    register     no                             
    tunnel       no
```

To show the local and remote port, and connection information, run the `nv show system grpc-tunnel server SERVER1 status` command:

```
cumulus@switch:~$ nv show system grpc-tunnel server SERVER1 status
               operational         
-------------  --------------------
local-port     0                   
remote-port    0                   
connection                         
  established  1970-01-01T00:00:00Z
  register     no                  
  tunnel       no
```

To show only connection information, run the `nv show system grpc-tunnel server SERVER1 status connection` command:

```
cumulus@switch:~$ nv show system grpc-tunnel server SERVER1 status connection 
             operational         
-----------  --------------------
established  1970-01-01T00:00:00Z
register     no                  
tunnel       no
```

### RPC Methods

Cumulus Linux supports the following <span class="a-tooltip">[RPC](## "Remote Procedure Call")</span> methods:  
- Capabilities
- Subscription types and options:  
  - STREAM (sample_interval, updates_only, suppress_redundant, and heartbeat_interval)
  - ON_CHANGE (updates_only and heartbeat_interval)
- Notification and update types:  
  - sync_response
  - update
  - delete

{{%notice note%}}
Cumulus Linux does not support GET or SET RPC events.
{{%/notice%}}

### Encoding Types

Cumulus Linux supports the Protobuf and JSON data formats.

### Wildcard Support

Cumulus Linux supports wildcard matching of keys. For example:

```
qos/interfaces/interface[interface-id=*]/output/queues/queue[name=*]/state/transmit-octets
```

You can use a combination of wildcard and specific keys; for example, to collect a metric for all queues on a specific interface:

```
/qos/interfaces/interface[interface-id=<name>]/output/queues/queue[*]/state/transmit-octets.
```

Regex for specific keys (such as `“interface-id=swp*”`) is not supported.

### Metrics

Cumulus Linux supports the following metrics.

{{%notice note%}}
An asterisk (*) in the `Description` column of the tables below indicates that metric is new for Cumulus Linux 5.16.
{{%/notice%}}

<!-- vale off -->
{{< tabs "TabID250 ">}}
{{< tab "802.1X">}}

|  Name | Description |
|------ | ----------- |
| `/system/aaa/server-groups/server-group[dot1x]/servers/server[address]/radius/state/priority` | *RADIUS server priority 1, 2 or 3. |
| `/system/aaa/server-groups/server-group[dot1x]/servers/server[address]/radius/state/auth-port` | *The port used for authentication and authorization. |
| `/system/aaa/server-groups/server-group[dot1x]/servers/server[address]/radius/state/acct-port` | *The port used for RADIUS accounting. |
| `/system/aaa/server-groups/server-group[dot1x]/servers/server[address]/radius/state/vrf` | *The VRF that contains the RADIUS server.|
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/auth-type` | *MD5 (Message Digest algorithm 5) or TLS (Transport Layer Security). |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/vlan` | *VLAN on which the supplicant connects to the switch and tries to authenticate. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/session-id` | *64 bytes/512 bit session ID. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/status` | *Supplicant status. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/out-eapol-req-frames` | *A count of all EAP request frames sent from the switch to the supplicant. Includes EAP request or OTP and any other challenge messages forwarded from the RADIUS Access Challenge. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-resp-frames` | *Counts all EAP response frames received from the Supplicant identified by the MAC address to the switch. Includes responses carrying credentials, leading to RADIUS Access request and eventual Access accept. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/out-eapol-req-id-frames` | *Counts EAP request identity frames sent from the switch to the Supplicant. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-start-frames` | *Counts EAPOL start frames received from this Supplicant. This is the very first message when the client initiates the authentication process for the session. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-logoff-frames` | *Counts EAPOL logoff frames received from this Supplicant. The client terminates the authenticated session, causing the port to transition from an `Authorized` to an `Unauthorized` state. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-invalid-frames` | *Counts malformed or invalid EAPOL frames received from the Supplicant. These are error counters for frames that do not comply with the protocol. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/counters/in-eapol-len-err-frames` | *Counts EAPOL frames received from this Supplicant that have an incorrect length. These frames are discarded and counted as protocol errors for this session. |
| `/system/dot1x/state/reauth-timeout-ignore` | *If enabled and if there is a reauthentication timeout with the RADIUS server, the timeout is ignored as long as the supplicant is currently in the authenticated state. |
| `/system/dot1x/state/dynamic-vlan` | *Indicates if the RADIUS server must assign a VLAN dynamically for the supplicant to be authorized or if Dynamic VLAN is `disabled`. Dynamic VLAN is `disabled` by default. |
| `/system/dot1x/state/max-stations` | *The maximum number of authenticated MAC addresses allowed on a port. The default is 6. The range is between 1 and 255. |
| `/system/dot1x/state/dynamic-ipv6-multi-tenant` | *Must be set to `enabled` for dynamic IPv6 multi-tenancy to be enabled. | 
| `/system/aaa/server-groups/server-group[dot1x]/servers/server[address]/radius/state/source-address` | The fixed source IP address that the switch as a RADIUS client uses to send authentication requests to the RADIUS server on behalf of supplicants. |  
| `/system/dot1x/radius/state/nas-ip-address` | *The IP address used for accounting purposes by Cumulus Linux as a RADIUS client or NAS (Network Access Server) while communicating when a RADIUS server. This IP address is used in the initial Access-Request packet and is useful on the RADIUS server for accounting and not as a source IP address in packet to the RADIUS server. |
| `/system/dot1x/radius/state/nas-identifier` | *Identifies the RADIUS client to a RADIUS server together with the NAS IP address. The NAS IP address is useful for accounting on the RADIUS server. |
| `/interfaces/interface[name]/ethernet/dot1x/state/eap` | *If 802.1X is enabled or disabled on the interface. |
| `/interfaces/interface[name]/ethernet/dot1x/state/mba` | *If MAC-based authentication (MBA) is enabled or disabled on the interface. |
| `/interfaces/interface[name]/ethernet/dot1x/state/host-mode` | *If multi host mode is enabled or disabled on the interface. |
| `/interfaces/interface[name]/ethernet/dot1x/state/port-id` | *The 802.1X port ID. |
| `/interfaces/interface[name]/ethernet/dot1x/state/ipv6-profile-name` | *The IPv6 profile associated with this interface. |
| `/interfaces/interface[name]/ethernet/dot1x/state/reauthenticate-interval` | * The recurring interval in seconds after which all already authenticated supplicants reauthenticate. By default, the interval is 0 (no reauthentication). |
| `/interfaces/interface[name]/ethernet/dot1x/state/auth-fail-vlan` | *If auth-fail VLAN is configured. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/offset-in-bits` | *Offset in bits from the beginning of the 64 bit IPv6 profile. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/length-in-bits` | *The length of the property in bits. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/property-value` | *The VSA ID, port ID, an integer or a hexadecimal value. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/isolation-property` | *Enabled if this property is used for isolation (multi-tenancy). Setting this flag causes ACLs to be programmed. |
| `/system/dot1x/ipv6-profiles/profile[name]/properties/property[id]/state/summarize-out` | *If enabled, the summary route be advertised. There can be only one property in an IPv6 profile with the `summarize-out` label enabled. |
| `/system/dot1x/ipv6-profiles/profile[name]/state/route-tag` | *Associates a policy tag with routes learned through this 802.1X IPv6 profile, allowing routing policy, redistribution control, and tenant isolation for the authenticated sessions. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/state/ipv6-prefix` | * The IPv6 prefix generated from all the IPv6 profile properties. |
| `/interfaces/interface[name]/ethernet/authenticated-sessions/authenticated-session[mac]/counters/reauth-timeouts` | *Counter that keeps track of authentication failures because the RADIUS server is unreachable after a successful authentication when the `reauth-timeout-ignore` option is enabled. |

{{< /tab >}}
{{< tab "ACLs ">}}

|  Name | Description |
|------ | ----------- |
| `/acl/interfaces/interface[name]/state/id` | Interface ACL state. |
| `/acl/interfaces/interface[name]/ingress-acl-sets/ingress-acl-set[set-name][acl-type]/state/set-name`| Interface ingress ACL set name. |
| `/acl/interfaces/interface[name]/ingress-acl-sets/ingress-acl-set[set-name][acl-type]/state/type` | Interface ingress ACL type. |
| `/acl/interfaces/interface[name]/ingress-acl-sets/ingress-acl-set[set-name][acl-type]/acl-entries/acl-entry[sequence-id='<entry-id>']/state/sequence-id` | Interface ingress ACL sequence. |
| `/acl/interfaces/interface[name]/ingress-acl-sets/ingress-acl-set[set-name][acl-type]/acl-entries/acl-entry[sequence-id]/state/matched-packets` | Interface ingress ACL sequence matched packets.|
| `/acl/interfaces/interface[name]/ingress-acl-sets/ingress-acl-set[set-name][acl-type]/acl-entries/acl-entry[sequence-id]/state/matched-octets` | Interface ingress ACL matched bytes. |
| `/acl/interfaces/interface[name]/egress-acl-sets/egress-acl-set[set-name][acl-type]/state/set-name` | Interface egress ACL set name. |
| `/acl/interfaces/interface[name]/egress-acl-sets/egress-acl-set[set-name][acl-type]/state/type` | Interface egress ACL type. |
| `/acl/interfaces/interface[name]/egress-acl-sets/egress-acl-set[set-name][acl-type]/acl-entries/acl-entry[sequence-id='<entry-id>']/state/sequence-id` | Interface egress ACL sequence. |
| `/acl/interfaces/interface[name]/egress-acl-sets/egress-acl-set[set-name][acl-type]/acl-entries/acl-entry[sequence-id]/state/matched-packets`| Interface egress ACL matched packets. |
| `/acl/interfaces/interface[name]/egress-acl-sets/egress-acl-set[set-name][acl-type]/acl-entries/acl-entry[sequence-id]/state/matched-octets` | Interface egress ACL matched bytes. |
| `/acl/acl-sets/acl-set[name][acl-type]/state/name` | ACL name. |
| `/acl/acl-sets/acl-set[name][acl-type]/state/type` | ACL type. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/state/sequence-id` | ACL sequence. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/l2/state/source-mac` | ACL sequence L2 source MAC address. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/l2/state/source-mac-mask` | ACL sequence L2 source MAC mask. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/l2/state/destination-mac` | ACL sequence L2 destination MAC address. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/l2/state/destination-mac-mask` | ACL sequence L2 destination MAC mask. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/l2/state/ethertype` | ACL sequence L2 ethertype. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv4/state/source-address` | ACL sequence IPv4 source address. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv4/state/destination-address` | ACL sequence IPv4 destination address. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv4/state/dscp` | ACL sequence IPv4 DSCP. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv4/state/protocol` | ACL sequence IPv4 protocol. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv4/state/hop-limit` | ACL sequence IPv4 hop limit. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv4/icmpv4/state/type` | ACL sequence ICMPv4 type. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv6/state/source-address` | ACL sequence IPv6 source address. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv6/state/destination-address` | ACL sequence IPv6 destination address. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv6/state/dscp` | ACL sequence IPv6 DSCP. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv6/state/protocol` | ACL sequence IPv6 protocol. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv6/state/hop-limit` | ACL sequence IPv6 hop limit. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/ipv6/icmpv6/state/type` | ACL sequence ICMPv6 type. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/action/state/forwarding-action` | ACL sequence forwarding action. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/action/state/log-action` | ACL sequence log action. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/transport/state/source-port` | ACL sequence L4 source port. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/transport/state/destination-port` | ACL sequence L4 destination port. |
| `/acl/acl-sets/acl-set[name][acl-type]/acl-entries/acl-entry[sequence-id]/transport/state/explicit-tcp-flags` | ACL sequence L4 TCP flags. |

{{< /tab >}}
{{< tab "Adaptive Routing">}}

|  Name | Description |
|------ | ----------- |
| `/system/adaptive-routing/state/counters/congestion-changes` | The number of adaptive routing change events that triggered due to congestion or link down.|

{{< /tab >}}
{{< tab "Control Plane Policer">}}

|  Name | Description |
|------ | ----------- |
|`/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/counters/buffer-drops` | *Control plane receive buffer drops.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/counters/rx-bytes` | *Control plane receive bytes.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/counters/rx-packets` | *Control plane trap group receive packets.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/egress/counters/types/type[type]/tx-bytes` | *Control plane transmit bytes.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/egress/counters/types/type[type]/tx-packets` | *Control plane receive packets.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/counters/pkt-violations` | *Control plane trap group packet violations.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/counters/rx-bytes` | *Control plane trap group receive bytes.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/counters/rx-packets` | *Control plane trap group receive packets.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/traps/trap[id]/counters/rx-bytes` | *Control plane trap group receive bytes.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/traps/trap[id]/counters/rx-drops` | *Control plane trap group receive drops.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/traps/trap[id]/counters/event-count` | *Control plane trap group receive events.|
| `/components/component/integrated-circuit/pipeline-counters/control-plane-traffic/vendor/nvidia/spectrum/state/ingress/trap-groups/trap-group[name]/traps/trap[id]/counters/rx-packets` | *Control plane trap group receive packets.|

{{< /tab >}}
{{< tab "Histogram">}}

|  Name | Description |
|------ | ----------- |
| `/performance/interfaces/interface[name]/histograms/egress-buffer/traffic-class[tc][upper-boundary]/count`  | *Histogram interface egress buffer queue depth.|
| `/performance/interfaces/interface[name]/histograms/ingress-buffer/priority-group[pg][upper-boundary]/count` | *Histogram interface ingress buffer queue depth.|
| `/performance/interfaces/interface[name]/histograms/counter/counter-type[type][upper-boundary]/count` | *Histogram interface counter data.|
| `/performance/interfaces/interface[name]/histograms/latency/traffic-class[tc][upper-boundary]/count` | *Histogram interface latency data.|

{{< /tab >}}
{{< tab "Interface">}}

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface[name]/phy/ber/state/ber-time-since-last-clear` | Time since last clear of BER stats (phy layer stats). |
| `/interfaces/interface[name]/phy/fec/state/corrected-bits` | Number of phy corrected bits of an interface by FEC engine.|
| `/interfaces/interface[name]/phy/ber/state/effective-ber` | Phy effective BER of an interface.|
| `/interfaces/interface[name]/phy/state/effective-errors` | Number of phy effective errors of an interface.|
| `/interfaces/interface[name]/phy/fec/state/fec-time-since-last-clear` | Time after last clear of FEC stats (phy layer). |
| `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/fc-fec-corrected-blocks` | Number FC FEC corrected blocks for a given lane of an interface.|
| `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/fc-fec-uncorrected-blocks` | Number of RS FEC uncorrectable blocks of an interface. |
| `/interfaces/interface[name]/phy/channels/channel[id]/ber/state/raw-ber` | Number of phy bit error rates for a given lane of an interface.|
| `/interfaces/interface[name]/phy//channels/channel[id]/state/raw-errors` | Number of phy error bits identified for a given lane of an interface.|
| `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/rs-fec-corrected-symbols` | Number of RS FEC corrected symbols for a given lane of an interface.|
| `/interfaces/interface[name]/phy/state/received-bits` | Number of phy total bits received for an interface.|
| `/interfaces/interface[name]/phy/fec/state/rs-fec-no-error-blocks` | Number of RS FEC no errors blocks of an interface.|
| `/interfaces/interface[name]/phy/fec/state/rs-fec-single-error-blocks` | Number of RS FEC uncorrectable blocks of an interface.|
| `/interfaces/interface[name]/phy/fec/state/rs-fec-uncorrectable-blocks` | Number of FC FEC uncorrectable blocks for a given lane of an interface. |
| `/interfaces/interface[name]/phy/ber/state/symbol-ber` | Phy symbol BER for an interface.|
| `/interfaces/interface[name]/phy/state/symbol-errors` | Number of phy symbol errors for an interface.|
| `/interfaces/interface[name]/phy/histograms/state/rs-num-corr-err[upper-boundary]/count`| Number of bit errors corrected that are less than or equal to upper boundary. |
| `/interfaces/interface[name]/phy/histograms/state/rs-num-corr-err[upper-boundary]/upper-boundary` | Upper boundary of the bin.|
| `/interfaces/interface[name]/ethernet/state/counters/in-crc-errors` | Total number of frames received with a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).|
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-1024-1518-octets` | Total number of packets (including bad packets) received between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-128-255-octets` | Total number of packets (including bad packets) received between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets).|
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-256-511-octets` | Total number of packets (including bad packets) received between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets).|
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-512-1023-octets` | Total number of packets (including bad packets) received between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets).|
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-64-octets` | Total number of packets (including bad packets) received that are 64 octets in length (excluding framing bits but including FCS octets).|
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-65-127-octets` | Total number of packets (including bad packets) received between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets).|
| `/interfaces/interface[name]/ethernet/state/counters/in-fcs-errors` | Total number of frames received on an interface that are an integral number of octets in length but do not pass the FCS check. This count does not include frames received with `frame-too-long` or `frame-too-short` error.|
| `/interfaces/interface[name]/ethernet/state/counters/in-jabber-frames` | Number of Jabber frames received on the interface.|
| `/interfaces/interface[name]/ethernet/state/counters/in-mac-pause-frames` | Inbound MAC pause frames on an interface.|
| `/interfaces/interface[name]/ethernet/state/counters/in-oversize-frames` | Total number of packets received longer than 1518 octets (excluding framing bits, but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/hw-mac-address` | System defined default MAC address for the interface. |
| `/interfaces/interface[name]/ethernet/state/mac-address​` | MAC address for the interface.|
| `/interfaces/interface[name]/ethernet/state/negotiated-duplex-mode` | When auto-negotiate is set to TRUE, and the interface has completed auto-negotiation with the remote peer, this value shows the negotiated duplex mode.|
| `/interfaces/interface[name]/ethernet/state/auto-negotiate` | Indicates if the interface is configured for auto-negotiation.|
| `/interfaces/interface[name]/ethernet/state/negotiated-port-speed` | If auto-negotiation is enabled, this is the negotiated port speed. If auto-negotiation is disabled, you do not see this metric. |
| `/interfaces/interface[name]/ethernet/state/counters/out-mac-pause-frames` | Total number of MAC control frames transmitted with an opcode indicating the pause operation. |
| `/interfaces/interface[name]/ethernet/state/counters/in-maxsize-exceeded` | Total number of frames received that exceed the maximum permitted frame size. |
| `/interfaces/interface[name]/ethernet/state/counters/in-symbol-error` | Total number of received error frames due to a symbol error. |
| `/interfaces/interface[name]/ethernet/state/counters/in-fragment-frames` | Total number of packets received that were less than 64 octets in length (excluding framing bits but including FCS octets) and had either a bad FCS with an integral number of octets (FCS error) or a bad FCS with a non-integral number of octets (alignment error). |
| `/interfaces/interface[name]/ethernet/state/counters/in-undersize-frames` | Total number of packets received that were less than 64 octets long (excluding framing bits, but including FCS octets) and were otherwise well formed. |
| `/interfaces/interface[name]/state/counters/carrier-down-transitions` | Total number of carrier down events on the interface. |
| `/interfaces/interface[name]/state/counters/carrier-up-transitions` | Total number of carrier up events on the interface. |
| `/interfaces/interface[name]/state/counters/out-hoq-drops` | Number of packets dropped at egress due to Head-of-Queue Timeout. |
| `/interfaces/interface[name]/state/counters/out-hoq-stall-drops` | Number of packets dropped at egress due to Head-of-Queue Timeout. |
| `/interfaces/interface[name]/state/counters/out-sll-drops` | Number of packets dropped at egress due to exceeding switch lifetime limit.|
| `/interfaces/interface[name]/state/counters/out-acl-drops` | Number of packets dropped at egress due to ACL policy. |
| `/interfaces/interface[name]/ethernet/state/counters/out-stp-filter-drops` | Number of packets dropped at egress due to STP filter. |
| `/interfaces/interface[name]/ethernet/state/counters/out-vlan-membership-drops` | Number of packets dropped at egress due to VLAN membership filter. |
| `/interfaces/interface[name]/ethernet/state/counters/in-vlan-tag-allowance-drops` | Number of packets dropped at ingress due to VLAN tag allowance filter. |
| `/interfaces/interface[name]/ethernet/state/counters/in-link-down-drops` | Number of packets dropped at ingress due to egress link down. |
| `/interfaces/interface[name]/ethernet/state/counters/in-vlan-membership-drops` | Number of packets dropped at ingress due to VLAN membership filter. |
| `/interfaces/interface[name]/ethernet/state/counters/in-loopback-drops` | Number of packets dropped at ingress due to loopback filter. |
| `/interfaces/interface[name]/state/counters/in-unknown-protos` | Number of MAC control frames received with an unsupported opcode. |
| `/interfaces/interface[name]/ethernet/state/counters/pkt-drop-events-probe-resource-lack` | Total number packets dropped by the probe due to lack of resources. |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-1519-2047-octets` | Total number of packets (including bad packets) received that were between 1519 and 2047 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-2048-4095-octets` | Total number of packets (including bad packets) received that were between 2048 and 4095 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-4096-8191-octets` | Total number of packets (including bad packets) received that were between 4096 and 8191 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/in-distribution/in-frames-8192-9216-octets` | Total number of packets (including bad packets) received that were between 8192 and 10239 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/no-buffer-multicast-dropped-pkts` | The number of multicast packets dropped due to lack of egress buffer resources. Valid only for Spectrum switches. |
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
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-65-127-octets` |  Total number of packets (including bad packets) transmitted that were between 65 and 127 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/ethernet/state/counters/out-distribution/out-frames-8192-9216-octets` | Total number of packets (including bad packets) transmitted that were between 8192 and 10239 octets in length (excluding framing bits but including FCS octets). |
| `/interfaces/interface[name]/state/counters/ecn-marked-pkts` | Count of packets marked as ECN or potentially marked as ECN |
| `/interfaces/interface[name]/state/counters/ece-marked-pkts` | Count of packets marked as ECE or potentially marked as ECE. |
| `/interfaces/interface[name]/state/counters/tx-wait` | Count of wire-speed, one-byte time intervals during which the port had data ready to transmit but did not send any data. |
| `/interfaces/interface[name]/ethernet/state/port-speed` | If auto-negotiation is enabled, the port speed is the highest advertised speed. If auto-negotiation is disabled, the port speed is the operational speed value.|
| `/interfaces/interface[name]/rates/state/in-bits-rate` | The calculated received rate of the interface, measured in bits per second.|
| `/interfaces/interface[name]/rates/state/in-pkts-rate` | The calculated received rate of the interface, measured in packets per second.|
| `/interfaces/interface[name]/rates/state/out-bits-rate` | The calculated transmitted rate of the interface, measured in bits per second.|
| `/interfaces/interface[name]/rates/state/out-pkts-rate` | The calculated transmitted rate of the interface, measured in packets per second.|
| `/interfaces/interface[name]/state/admin-status` | Admin state of an interface. |
| `/interfaces/interface[name]/state/counters/carrier-transitions` | Number of times since system boot that `ifOperStatus` changed.|
| `/interfaces/interface[name]/state/counters/in-acl-drops` | Number of packets dropped at ingress due to ACL Policy.|
| `/interfaces/interface[name]/state/counters/in-broadcast-pkts` | Total number of broadcast packets received on an interface.|
| `/interfaces/interface[name]/state/counters/in-discards` | Number of inbound packets discarded even though no errors are detected to prevent them from being deliverable to a higher-layer protocol. |
| `/interfaces/interface[name]/state/counters/in-errors` | For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.|
| `/interfaces/interface[name]/state/counters/in-multicast-pkts` | Total number of multicast packets received on an interface.|
| `/interfaces/interface[name]/state/counters/in-pkts`| Number of packets discarded from the egress queue of an interface. |
| `/interfaces/interface[name]/state/counters/in-unicast-pkts` | The number of packets, delivered by this sub-layer to a higher (sub-)layer, that were not addressed to a multicast or broadcast address at this sub-layer. |
| `/interfaces/interface[name]/state/counters/out-broadcast-pkts` | Total number of broadcast packets transmitted out of an interface.|
| `/interfaces/interface[name]/state/counters/out-discards` | Number of outbound packets discarded even though no errors are detected to prevent them from being transmitted. |
| `/interfaces/interface[name]/state/counters/out-errors` | For packet-oriented interfaces, the number of outbound packets not transmitted because of errors. For character-oriented or fixed-length interfaces, the number of outbound transmission units not transmitted because of errors. |
| `/interfaces/interface[name]/state/counters/out-multicast-pkts` | Total number of packets that higher-level protocols requested be transmitted, and which were addressed to a multicast address at this sub-layer, including those that were discarded or not sent. For a MAC layer protocol, this includes both Group and Functional addresses.|
| `/interfaces/interface[name]/state/counters/out-octets` | Total number of octets transmitted out of an interface, including framing characters.|
| `/interfaces/interface[name]/state/counters/out-pkts` | Total number of packets transmitted out of the interface, including all unicast, multicast, broadcast, and bad packets.|
| `/interfaces/interface[name]/state/counters/out-unicast-pkts` | Total number of unicast packets transmitted out of an interface.|
| `/interfaces/interface[name]/state/ifindex` | A unique value, greater than zero, for each interface.|
| `/interfaces/interface[name]/state/last-change` | The last time the state of the interface changed.|
| `/interfaces/interface[name]/state/mtu` | Size of the largest packet that can be sent or received on the interface, specified in octets. For interfaces used for transmitting network datagrams, this is the size of the largest network datagram that the interface can send.|
| `/interfaces/interface[name]/state/name​` | The name of the interface.|
| `/interfaces/interface[name]/state/oper-status` | Current operational state of an interface. |
| `/interfaces/interface[name]/state/protodown​` | Indicates if the interface is administratively held down by a protocol or system process rather than by user action.|
| `/interfaces/interface[name]/state/type​` | The inteface type. |
| `/interfaces/interface[name]/state/description`| *The interface description.|
| `/interfaces/interface[name]/state/transceiver` | *The transceiver on the interface. |

{{< /tab >}}
{{< tab "LLDP">}}

|  Name | <div style="width: 300px;">Description</div> |
|------ | ----------- |
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/capabilities/capability[name]/state/enabled` | If the corresponding system capability is enabled on the neighbor.|
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/age` | LLDP neighbor age after discovery.|
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/chassis-id` | Chassis component of the endpoint identifier associated with the transmitting LLDP agent.|
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/chassis-id-type` | Format and source of the chassis identifier string.|
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/management-addresses[address]/type`| Enumerated value for the network address type identified in this TLV. |
| `/lldp/interfaces/interface/neighbors/neighbor/state/port-description` | Binary string containing the actual port identifier for the port from which this LLDP PDU was transmitted.|
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/port-description`| Port component of the endpoint identifier associated with the transmitting LLDP agent. |
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/port-id` | The Port ID is a mandatory TLV which identifies the port component of the endpoint identifier associated with the transmitting LLDP agent. If the specified port is an IEEE 802.3 Repeater port, then this TLV is optional.|
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/port-id-type` | Format and source of the remote port ID string. |
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/system-description` | Description of the network entity associated with the transmitting LLDP agent.|
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/system-name` | Administratively assigned name of the system associated with the transmitting LLDP agent.|
| `/lldp/interfaces/interface[name]/neighbors/neighbor[id]/state/ttl` | Indicates how long information from the neighbor is considered valid. |
| `/lldp/interfaces/interface[name]/state/enabled`| If LLDP is enabled on the interface. |
| `/lldp/state/chassis-id` | The chassis component of the endpoint identifier associated with the transmitting LLDP agent.|
| `/lldp/state/chassis-id-type` | The format and source of the chassis identifier string.|
| `/lldp/state/system-description` | Description of the network entity including the full name and version identification of the system's hardware type, software operating system, and networking software.|
| `/lldp/state/system-name` | Administratively assigned name for the system.|
| `/lldp/state/enable` | If LLDP is enabled.|

{{< /tab >}}
{{< tab "Packet Trimming">}}

|  Name | Description |
|------ | ----------- |
| `/qos/packet-trimming/state/counters/trimmed-unicast-pkts`| The number of trimmed packets.|
| `/qos/interfaces/interface[interface-id]/packet-trimming/state/counters/trimmed-unicast-pkts`| The number packets that were trimmed on the interface.|
| `/qos/interfaces/interface[interface-id]/packet-trimming/state/counters/trimmed-tx-unicast-pkts`| The number of packets that were trimmed and sent succesfully on the interface.|
| `/qos/interfaces/interface[interface-id]/packet-trimming/output/queues/queue[name]/state/trimmed-unicast-pkts`| The number of packets that were trimmed on the interface queue.|

{{< /tab >}}
{{< tab "Performance">}}

|  Name | Description |
|------ | ----------- |
| `/performance/interfaces/interface[name=<interface>]/ measurements/measurement[traffic-class=<tc>][protocol=<proto>]/state/timestamp`| The timestamp when the latency measurement was recorded.|
| `/performance/interfaces/interface[name=<interface>]/ measurements/measurement[traffic-class=<tc>][protocol=<proto>]/state/error-code`| The measurement error code. [`0` indicates success, non-zero values indicate an error code] |
| `/performance/interfaces/interface[name=<interface>]/ measurements/measurement[traffic-class=<tc>][protocol=<proto>]/state/latency/rtt`| The measured latency in microseconds for the specified traffic class and protocol.|
| `/performance/interfaces/interface[name=<interface>]/ measurements/measurement[traffic-class=<tc>][protocol=<proto>]/state/error-type`| The type of error encountered, if any, during the latency measurement.|
| `/performance/interfaces/interface[name=<interface>]/ measurements/measurement[traffic-class=<tc>][protocol=<proto>]/state/error-message`| Details about any error encountered.|

{{< /tab >}}
{{< tab "Platform">}}

|  Name | Description |
|------ | ----------- |
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
| `/components/component[name]/fan/state/speed` | Current (instantaneous) fan speed. |
| `/components/component[name]/power-supply/state/capacity` | Maximum power capacity of the power supply. |
| `/components/component[name]/power-supply/state/input-current` | Input current draw of the power supply.|
| `/components/component[name]/power-supply/state/input-voltage` | Input voltage to power supply.|
| `/components/component[name]/power-supply/state/output-current` | Output current supplied by the power supply. |
| `/components/component[name]/power-supply/state/output-power` | Output power supplied by the power supply. |
| `/components/component[name]/power-supply/state/output-voltage` | Output voltage supplied by the power supply.|
| `/components/component[name]/state/description` | System-supplied description of the component. |
| `/components/component[name]/state/firmware-version` | For hardware components, the version of associated firmware running on the component, if applicable.|
| `/components/component[name]/state/last-reboot-reason​` | The reason for the component's last reboot.|
| `/components/component[name]/state/last-reboot-time​` | The time of the last reboot. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/components/component[name]/state/name` | Device name for the component. |
| `/components/component[name]/state/oper-status` | If applicable, the current operational status of the component. |
| `/components/component[name]/state/temperature/alarm-severity` | Severity of the current alarm.|
| `/components/component[name]/state/temperature/alarm-status` | A value of `true` indicates the alarm has been raised or asserted. The value is false when the alarm is cleared. |
| `/components/component[name]/state/temperature/alarm-threshold` | The threshold value crossed for this alarm. |
| `/components/component[name]/state/temperature/avg​` | Arithmetic mean value of the statistic over the sampling period.|
| `/components/component[name]/state/temperature/instant` | Instantaneous value of the statistic.  |
| `/components/component[name]/state/temperature/interval` | If supported by the system, the time interval over which the minimum, maximum, and average statistics are computed by the system.|
| `/components/component[name]/state/temperature/max​` | The maximum value of the statistic over the sampling period.|
| `/components/component[name]/state/temperature/max​-time` | Absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/components/component[name]/state/temperature/min​` | Minimum value of the statistic over the sampling period.|
| `/components/component[name]/state/temperature/min-time​` | Absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/components/component[name]/transceiver/host-lanes/lane[lane-number]/state/tx-cdr-lol` | Transmitter clock-and-data-recovery loss-of-lock flag.|
| `/components/component[name]/transceiver/host-lanes/lane[lane-number]/state/tx-los` | Transmitter loss-of-signal flag.|
| `/components/component[name]/transceiver/physical-channels/channel[index]/state/input-power/instant` | Input optical power of a physical channel in units of 0.01dBm, which may be associated with individual physical channels or an aggregate of multiple physical channels. |
| `/components/component[name]/transceiver/physical-channels/channel[index]/state/laser-bias-current/instant` | Current applied by the system to the transmit laser to achieve the output power. The current is expressed in mA with up to two decimal precision. |
| `/components/component[name]/transceiver/physical-channels/channel[index]/state/output-power/instant` | Output optical power of a physical channel in units of 0.01dBm, which might be associated with individual physical channels or an aggregate of multiple physical channels. |
| `/components/component[name]/transceiver/physical-channels/channel[index]/state/rx-cdr-lol` | Receiver clock-and-data-recovery loss-of-lock flag.|
| `/components/component[name]/transceiver/physical-channels/channel[index]/state/rx-los` | Receiver loss-of-signal flag.|
| `/components/component[name]/transceiver/state/date-code​` | Representation of the transceiver date code, typically stored as YYMMDD. The time portion of the value is undefined and not intended to be read. |
| `/components/component[name]/transceiver/state/enabled​` | Turns power on or off to the transceiver. Provides a means to power on or off the transceiver (in the case of SFP, SFP+, QSFP) or enable high-power mode (in the case of CFP, CFP2, CFP4). This is optionally supported (device can choose to always enable). True = power on - high power. False = powered off.|
| `/components/component[name]/transceiver/state/ethernet-pmd`| Ethernet PMD (physical medium dependent sublayer) that the transceiver supports. |
| `/components/component[name]/transceiver/state/form-factor​` | Type of optical transceiver used on this port. If the client port is built into the device and not pluggable, `non-pluggable` is the corresponding state. If a device port supports multiple form factors, the value of the transceiver installed is reported. If no transceiver is present, the value of the highest rate form factor is reported. |
| `/components/component[name]/transceiver/state/present​` | Indicates if a transceiver is present in the specified client port.|
| `/components/component[name]/transceiver/state/serial-no​` | Transceiver serial number. 16-octet field that contains ASCII characters, left-aligned and padded on the right with ASCII spaces (20h). If part serial number is undefined, all 16 octets = 0h.|
| `/components/component[name]/transceiver/state/supply-voltage/instant` | Input voltage as measured by the transceiver.|
| `/components/component[name]/transceiver/state/vendor​` | Full name of transceiver vendor. |
| `/components/component[name]/transceiver/state/vendor-part​` | Transceiver vendor part number.|
| `/components/component[name]/transceiver/state/vendor-rev​` | Transceiver vendor revision number. |

{{< /tab >}}
{{< tab "QoS">}}

|  Name | Description |
|------ | ----------- |
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the priority group on the interface. |
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the priority group on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the priority group on the interface was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the priority‑group descriptor on the interface.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the priority‑group descriptor on the interface during the most recent sampling interval. |
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the priority‑group descriptor on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the interface priority‑group descriptor was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/descriptors/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the interface priority‑group descriptor were last cleared.|
|`/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/time-since-last-clear`| *Elapsed time in milliseconds since watermark counters for the interface priority‑group were last cleared.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the interface traffic‑class queue were last cleared.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/counters/in-pkts` | *The number of packets received at Ingress for a given priority group.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/counters/in-octets` | *The number of octets of data received at Ingress for a given priority group.|
| `/qos/interfaces/interface[interface-id]/input/priority-group[pg-id]/state/shared-buffer/data/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the priority‑group on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the interface traffic‑class queue.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the traffic‑class queue on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the interface traffic‑class queue since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the interface traffic‑class queue was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/data/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the interface traffic‑class queue were last cleared.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the traffic‑class queue descriptor on the interface.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the interface traffic‑class queue descriptor during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the interface traffic‑class queue descriptor since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the interface traffic‑class queue descriptor was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/shared-buffer/descriptors/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the interface traffic‑class queue descriptor were last cleared.|
| `qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the interface ingress pool.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the interface ingress pool during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the interface ingress pool since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the interface ingress pool was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/data/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the interface ingress pool were last cleared.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the interface ingress‑pool descriptor.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the interface ingress‑pool descriptor during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the interface ingress‑pool descriptor since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the interface ingress‑pool descriptor was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/pools/pool[id]/state/shared-buffer/descriptors/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the interface ingress‑pool descriptor were last cleared.|
| `/qos/interfaces/interface[interface-id]/ouput/pools/pool[id]/state/shared-buffer/data/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the interface egress pool.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/data/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the interface egress pool during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/data/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the interface egress pool since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/data/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the interface egress pool was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/data/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the interface egress pool were last cleared.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the interface egress‑pool descriptor.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the interface egress‑pool descriptor during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the interface egress‑pool descriptor since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the interface egress‑pool descriptor was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/pools/pool[id]/state/shared-buffer/descriptors/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the interface egress‑pool descriptor were last cleared.|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for multicast traffic on the interface.|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for multicast traffic on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for multicast traffic on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for multicast traffic on the interface was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/output/state/shared-buffer/multicast/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for multicast traffic on the interface were last cleared.|
| `/qos/shared-buffer/switch-priority[priority]/state/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for multicast traffic in the specified switch priority.|
| `/qos/shared-buffer/switch-priority[priority]/state/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for multicast traffic in the specified switch priority during the most recent sampling interval.|
| `/qos/shared-buffer/switch-priority[priority]/state/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for multicast traffic in the specified switch priority since the last watermark reset; software‑maintained.|
| `/qos/shared-buffer/switch-priority[priority]/state/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for multicast traffic in the specified switch priority was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/shared-buffer/switch-priority[priority]/state/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for multicast traffic in the specified switch priority were last cleared.|
| `/qos/shared-buffer/pools/pool[id]/state/data/instant-occupancy` | *Instantaneous shared‑buffer occupancy in bytes for the given pool. This metric replaces `/qos/shared-buffer/pools/pool[id]/state/instant-occupancy` in previous releases. |
| `/qos/shared-buffer/pools/pool[id]/state/data/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy in bytes for the given pool during the most recent sampling interval. This metric replaces `/qos/shared-buffer/pools/pool[id]/state/max-occupancy-since-last-sample` in previous releases.|
| `/qos/shared-buffer/pools/pool[id]/state/data/max-occupancy` | *Maximum shared‑buffer occupancy in bytes for the given pool since the last watermark reset; software‑maintained. This metric replaces `/qos/shared-buffer/pools/pool[id]/state/max-occupancy` in previous releases.|
| `/qos/shared-buffer/pools/pool[id]/state/data/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the given pool was recorded since the last watermark reset. Value is Unix epoch seconds (UTC). This metric replaces `/qos/shared-buffer/pools/pool[id]/state/max-occupancy-timestamp` in previous releases.|
| `/qos/shared-buffer/pools/pool[id]/state/data/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the given pool were last cleared. This metric replaces `/qos/shared-buffer/pools/pool[id]/state/time-since-last-clear` in previous releases.|
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/instant-occupancy` | *Instantaneous shared‑buffer occupancy as number of descriptors for the given pool. |
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/max-occupancy-since-last-sample` | *Maximum shared‑buffer occupancy as number of descriptors for the given pool during the most recent sampling interval. |
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/max-occupancy` | *Maximum shared‑buffer occupancy as number of descriptors for the given pool since the last watermark reset; software‑maintained. |
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/max-occupancy-timestamp` | *Timestamp at which the highest shared‑buffer occupancy for the given pool was recorded since the last watermark reset. Value is Unix epoch seconds (UTC). |
| `/qos/shared-buffer/pools/pool[id]/state/descriptors/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the given pool were last cleared. |
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/instant-occupancy` | *Instantaneous headroom-buffer occupancy in bytes for the specified buffer type (primary or secondary) in the priority group on the interface.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/max-occupancy-since-last-sample` | *Maximum headroom‑buffer occupancy in bytes for the specified buffer type (primary or secondary) in the priority group on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/max-occupancy` | *Maximum headroom‑buffer occupancy in bytes for the specified buffer type (primary or secondary) in the priority group on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/max-occupancy-timestamp` | *Timestamp at which the highest headroom‑buffer occupancy for the specified buffer type (primary or secondary) in the priority group on the interface was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/priority-group[pg-id]/state/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the specified buffer type (primary or secondary) in the priority group on the interface were last cleared.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/instant-occupancy` | *Instantaneous headroom-buffer occupancy in bytes for the specified buffer type (primary or secondary) on the interface.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/max-occupancy-since-last-sample` | *Maximum headroom‑buffer occupancy in bytes for the specified buffer type (primary or secondary) on the interface during the most recent sampling interval.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/max-occupancy` | *Maximum headroom‑buffer occupancy in bytes for the specified buffer type (primary or secondary) on the interface since the last watermark reset; software‑maintained.|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/max-occupancy-timestamp` | *Timestamp at which the highest headroom‑buffer occupancy for the specified buffer type (primary or secondary) on the interface was recorded since the last watermark reset. Value is Unix epoch seconds (UTC).|
| `/qos/interfaces/interface[interface-id]/input/headroom-buffer[buffer-type]/state/time-since-last-clear` | *Elapsed time in milliseconds since watermark counters for the specified buffer type (primary or secondary) on the interface were last cleared.|
| `/qos/shared-buffer/state/cell-size` | *Shared‑buffer allocation cell size in bytes; use to convert cell‑based counters to bytes.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/ecn-marked-pkts`| Number of ECN marked packets from this egress queue. If the ECN counter is not enabled, the counter value is 0.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/no-buffer-uc-dropped-pkts` | Number of packets discarded from this egress queue when there is no buffer left in the interface. |
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/time-since-last-clear` | Time since last clear of watermarks in a queue.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/transmit-octets`| Number of transmitted bytes in the egress queue of an interface.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/transmit-pkts`| Number of transmitted packets in the egress queue of an interface. |
| `/qos/interfaces/interface[name]/output/queues/queue[name]/state/max-queue-len` | Maximum queue length for a queue since last time watermarks were reset.|
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/wred-dropped-pkts` | Number of packets discarded from this egress queue of an interface. |
| `/qos/interfaces/interface[interface-id]/priority-group[priority_group]/state/counters/time-since-last-clear` | Time since last clear of watermarks in a priority group.|
| `/qos/interfaces/interface[interface-id]/switch-priority[priority]/state/counters/in-pause-pkts` | Number of pause packets for the priority class in the ingress queue.|
| `/qos/interfaces/interface[interface-id]/switch-priority[priority]/state/counters/out-pause-pkts`| Number of pause packets for the priority class in the egress queue.|
| `/qos/interfaces/interface[interface-id]/priority-group[priority_group]/state/counters/in-pkts` | Number of received input packets for a priority group. |
| `/qos/interfaces/interface[interface-id]/state/priority-group[priority_group]/state/counters/in-octets` | Number of octets of input data received for a given priority group. |
| `/qos/interfaces/interface[interface-id]/switch-priority[priority]/state/counters/in-discards` | Number of discarded inbound packets. |
| `/qos/interfaces/interface[interface-id]/switch-priority[priority]/state/in-pause-duration` | Total time in microseconds packet transmission on the port has been paused. |
| `/qos/interfaces/interface[interface-id]/switch-priority[priority]/state/out-pause-duration` | Total time in microseconds that the far-end port has been requested to pause. |
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/instant-queue-len` | Transmit queue depth in bytes on traffic class selected by traffic_class of the port selected by local_port. |
| `/qos/interfaces/interface[interface-id]/output/queues/queue/[name]state/transmit-uc-pkts` | Number of unicast packets transmitted by this queue.|

{{%notice note%}}
The `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/max-queue-len-cells` is no longer supported in Cumulus Linux 5.16 and later.
{{%/notice%}}

{{< /tab >}}
{{< tab "Routing">}}

|  Name | Description |
|------ | ----------- |
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp` |Top-level configuration and state for the BGP router. |
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/afi-safis/afi-safi[afi-safi-name]/state/prefixes/installed` | The number of prefixes received from the neighbor that are installed in the network instance RIB and actively used for forwarding.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/afi-safis/afi-safi[afi-safi-name]/state/prefixes/received` | The number of prefixes that are received from the neighbor after applying any policies. This count is the number of prefixes present in the post-policy Adj-RIB-In for the neighbor.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/afi-safis/afi-safi[afi-safi-name]/state/prefixes/sent` | The number of prefixes that are advertised to the neighbor after applying any policies. This count is the number of prefixes present in the post-policy Adj-RIB-Out for the neighbor.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state` | BGP neighbor state.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/description` | BGP neighbor state description.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/established-transitions` | Number of transitions to the Established state for the neighbor session. |
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/last-established` | The time that the BGP session last transitioned in or out of the Established state. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC). |
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/local-as` | The local autonomous system number used when establishing sessions with the remote peer or peer group, if this differs from the global BGP router autonomous system number.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/messages` | Counters for BGP messages sent and received from the neighbor.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/messages/received` | Counters for BGP messages received from the neighbor. |
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/messages/received/last-notification-error-code` | The last BGP error sent or received on the peering session.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/messages/received/UPDATE` | Number of BGP UPDATE messages announcing, withdrawing, or modifying paths exchanged.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/messages/sent` | Counters relating to BGP messages sent to the neighbor.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/messages/sent/last-notification-error-code` | The last BGP error sent or received on the peering session.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/messages/sent/UPDATE` | Number of BGP UPDATE messages announcing, withdrawing or modifying paths exchanged.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/neighbor-address` | Address of the BGP peer, either in IPv4 or IPv6.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/peer-as` | AS number of the peer.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/peer-group` | The peer-group with which this neighbor is associated|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/peer-type` | Explicitly designate the peer or peer group as internal (iBGP) or external (eBGP).|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/queues/input` | The number of messages received from the peer currently queued.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/queues/output` | The number of messages queued to be sent to the peer.|
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/session-state` | Operational state of the BGP peer. |
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor/state` | Operational state data for interface hold-time.|
| `network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/graceful-shutdown` | BGP graceful shutdown state.|
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
{{< /tab >}}
{{< tab "SRv6">}}

|  Name | Description |
|------ | ----------- |
|`/network-instances/network-instance[name]/srv6/global/state/counters/no-sid-drops` | The number of packets dropped due to no matching SRv6 SID.|
| `/network-instances/network-instance[name]/srv6/sids/sid[id]/id`| The SRv6 SID (segment identifier).|
| `/network-instances/network-instance[name]/srv6/sids/sid[id]/state/counters/in-pkts` | The number of packets received for this SRv6 SID.|

{{< /tab >}}
{{< tab "System">}}

|  Name | Description |
|------ | ----------- |
| `/system/state/up-time` | Continuous operational time of the system since last reboot. |
| `/system/state/hostname` | System hostname. |
| `/system/state/software-version` | System software version. |
| `/system/state/boot-time` | System boot time. |
| `/system/state/current-datetime` | Current system date and time. |
| `/system/control-plane-traffic/ingress/ipv4/counters/`<br>`/system/control-plane-traffic/ingress/ipv6/counters/` | Number of input IP datagrams discarded in software including those received in error.|
| `/system/cpus/cpu[index]/state/hardware-interrupt/avg` | The arithmetic mean value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/hardware-interrupt/instant` | The instantaneous percentage value.|
| `/system/cpus/cpu[index]/state/hardware-interrupt/interval` | If supported by the system, the time interval over which the minimum, maximum, and average statistics are computed by the system.|
| `/system/cpus/cpu[index]/state/hardware-interrupt/max` | The maximum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/hardware-interrupt/max-time` | The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/hardware-interrupt/min` | The minimum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/hardware-interrupt/min-time` | The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/hardware-interrupt/seconds` | The total number of seconds spent servicing hardware interrupts.|
| `/system/cpus/cpu[index]/state/idle/avg` | The arithmetic mean value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/idle/instant` |The instantaneous percentage value.|
| `/system/cpus/cpu[index]/state/idle/interval` | If supported by the system, the time interval over which the minimum, maximum, and average statistics are computed by the system.|
| `/system/cpus/cpu[index]/state/idle/max` | The maximum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/idle/max-time` | The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/idle/min` | The minimum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/idle/min-time` | The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/idle/seconds` |  The total number of seconds spent idle.|
| `/system/cpus/cpu[index]/state/kernel/avg` | The arithmetic mean value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/kernel/instant` | The instantaneous percentage value.|
| `/system/cpus/cpu[index]/state/kernel/interval` | If supported by the system, the time interval over which the minimum, maximum, and average statistics are computed by the system. |
| `/system/cpus/cpu[index]/state/kernel/max` | The maximum value of the percentage measure of the statistic over the time interval. |
| `/system/cpus/cpu[index]/state/kernel/max-time` | The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/kernel/min` | The minimum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/kernel/min-time` | The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/kernel/seconds` | The total number of seconds spent running in kernel space.|
| `/system/cpus/cpu[index]/state/nice/avg` | The arithmetic mean value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/nice/instant` | The instantaneous percentage value. |
| `/system/cpus/cpu[index]/state/nice/interval` | If supported by the system, the time interval over which the minimum, maximum, and average statistics are computed by the system.|
| `/system/cpus/cpu[index]/state/nice/max` | The maximum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/nice/max-time` | The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/nice/min` |  The minimum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/nice/min-time` | The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/nice/seconds` |  The total number of seconds spent running low-priority (niced) user processes.|
| `/system/cpus/cpu[index]/state/software-interrupt/avg` | The arithmetic mean value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/software-interrupt/instant` | The instantaneous percentage value.|
| `/system/cpus/cpu[index]/state/software-interrupt/interval` | If supported by the system, the time interval over which the minimum, maximum, and average statistics are computed by the system.|
| `/system/cpus/cpu[index]/state/software-interrupt/max` | The maximum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/software-interrupt/max-time` | The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/software-interrupt/min` | The minimum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/software-interrupt/min-time` | The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/software-interrupt/seconds` |  The total number of seconds spent servicing software interrupts.|
| `/system/cpus/cpu[index]/state/total/avg` | The arithmetic mean value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/total/instant` | The instantaneous percentage value. |
| `/system/cpus/cpu[index]/state/total/interval` | If supported by the system, the time interval over which the minimum, maximum, and average statistics are computed by the system.|
| `/system/cpus/cpu[index]/state/total/max` | The maximum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/total/max-time` | The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/total/min` | The minimum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/total/min-time` | The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/user/avg` | The arithmetic mean value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/user/instant` | The instantaneous percentage value.|
| `/system/cpus/cpu[index]/state/user/interval` | If supported by the system, the time interval over which the minimum, maximum, and average statistics are computed by the system.|
| `/system/cpus/cpu[index]/state/user/max` | The maximum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/user/max-time` | The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/user/min` | The minimum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/user/min-time` | The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/user/seconds` | The total number of seconds spent running in user space.|
| `/system/cpus/cpu[index]/state/wait/avg` | The arithmetic mean value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/wait/instant` | The instantaneous percentage value.|
| `/system/cpus/cpu[index]/state/wait/interval` | If supported by the system, this reports the time interval over which the minimum, maximum, and average statistics are computed by the system.|
| `/system/cpus/cpu[index]/state/wait/max` | The maximum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/wait/max-time` | The absolute time at which the maximum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/wait/min` | The minimum value of the percentage measure of the statistic over the time interval.|
| `/system/cpus/cpu[index]/state/wait/min-time` | The absolute time at which the minimum value occurred. The value is the timestamp in nanoseconds relative to the Unix Epoch (Jan 1, 1970 00:00:00 UTC).|
| `/system/cpus/cpu[index]/state/wait/seconds` | The total number of seconds spent waiting I/O.|
| `/system/memory/state/free` | Memory that is not used and is available for allocation. |
| `/system/memory/state/physical` | The total physical memory available on the system.|
| `/system/memory/state/reserved` | Memory reserved for system use. |
| `/system/memory/state/used​` | Memory that has been used and not available for allocation.|
| `/system/mount-points/mount-point[name]/state/utilized` | The amount of space currently in use on the filesystem.|
| `/system/mount-points/mount-point[name]/state/name` | Mount point name.|
| `/system/mount-points/mount-point[name]/state/storage-component` | A reference to the hosting component within the hierarchy. |
| `/system/mount-points/mount-point[name]/state/size` | Total size of the initialized filesystem.|
| `/system/mount-points/mount-point[name]/state/available` | The amount of unused space on the filesystem.|
| `/system/mount-points/mount-point[name]/state/type` | Filesystem type used for storage such flash, hard disk, tmpfsor or ramdisk, or remote or network based storage.|
| `/system/processes/process[pid]/state/cpu-usage-user` | CPU time consumed by this process in user mode in nanoseconds. |
| `/system/processes/process[pid]/state/cpu-usage-system` | CPU time consumed by this process in kernel mode in nanoseconds. |
| `/system/processes/process[pid]/state/start-time` | Start time of the process in seconds since epoch. |
| `/system/processes/process[pid]/state/name` | Process name. |
| `/system/processes/process[pid]/state/pid`| Process PID |
| `/system/processes/process[pid]/state/memory-usage` | Bytes allocated and still in use by the process. |
| `/system/processes/process[pid]/state/memory-utilization` | Percentage of RAM that the process is using. |
| `/system/processes/process[pid]/state/cpu-utilization` | Percentage of CPU that the process is using, relative to total system CPU capacity (all cores combined). |

{{< /tab >}}
{{< /tabs >}}
<!-- vale on -->
### User Credentials and Authentication

User authentication is enabled by default. gNMI subscription requests must include the user authentication credentials with NVUE API access permissions, either in an HTTP basic authentication header according to RFC7617 or a gRPC metadata header.

### gNMI Client Requests

You can use your gNMI client on a host to request capabilities and data to which the gNMI agent subscribes.

#### Dial-in Mode Examples

The following example shows a basic dial-in mode subscribe request in an HTTP basic authentication header:

```
gnmic subscribe --mode stream -i 10s --tls-cert gnmi_client.crt --tls-key gnmi_client.key -u cumulus -p ******* --auth-scheme Basic -a 192.168.200.3:9339 --prefix "system/cpus/cpu[index=0]" --path "state"
...
```

The following example shows a dial-in mode subscribe request in a gRPC metadata header with authorization information encoded in base64 format:

```
gnmic subscribe --metadata authorization="Basic Y3VtdWx1czpOdmlkaWFSMGNrcyE=" --address 192.168.200.3:9339 --tls-cert cert/umf-crt.pem --tls-key cert/umf-key.pem --encoding proto --mode stream --stream-mode sample --sample-interval 1s --prefix "system/cpus/cpu[index=0]" --path "state"
...
```

The following example shows a dial-in mode subscribe request in a gRPC metadata header with the username and password specified in the request:

```
gnmic subscribe --mode stream -i 10s --tls-cert cert/umf-crt.pem --tls-key cert/umf-key.pem -u cumulus -p NvidiaR0cks! --skip-verify -a  192.168.200.3:9339  --timeout 30s --prefix "system/cpus/cpu[index=0]" --path "state"
```

#### Subscription Response Example

The following example shows a subscription response:

```
{
  "source": "192.168.200.3:9339",
  "subscription-name": "default-1752848659",
  "timestamp": 1752848657055588821,
  "time": "2025-07-18T14:24:17.055588821Z",
  "prefix": "system/cpus/cpu[index=0]",
  "updates": [
    {
      "Path": "state/kernel/max-time",
      "values": {
        "state/kernel/max-time": 1752848657055588900
      }
    },
    {
      "Path": "state/kernel/max",
      "values": {
        "state/kernel/max": 0.33359713753109865
      }
    },
    {
      "Path": "state/kernel/min",
      "values": {
        "state/kernel/min": 0
      }
    },
    {
      "Path": "state/kernel/avg",
      "values": {
        "state/kernel/avg": 0.33359713753109865
      }
    },
    {
      "Path": "state/kernel/min-time",
      "values": {
        "state/kernel/min-time": 1752848657055588900
      }
    },
    {
      "Path": "state/kernel/seconds",
      "values": {
        "state/kernel/seconds": 595
      }
    },
    {
      "Path": "state/kernel/instant",
      "values": {
        "state/kernel/instant": 0.33359713753109865
      }
    },
    {
      "Path": "state/user/avg",
      "values": {
        "state/user/avg": 0.2680692284537066
      }
    },
...
```

#### Capabilities Example

The following example shows a capabilities request and the expected response:

```
gnmic capabilities --tls-cert gnmic-cert.pem --tls-key gnmic-key.pem -u cumulus -p ****** --auth-scheme Basic --skip-verify -a 10.188.52.108:9339

gNMI version: 0.10.0 
supported models: 
  - openconfig-ospf-types, OpenConfig working group, 0.1.3 
...
  - openconfig-platform-fabric, OpenConfig working group, 0.1.0 
  - openconfig-platform-healthz, OpenConfig working group, 0.1.1 
supported encodings: 
  - JSON 
  - JSON_IETF 
  - PROTO 
```
### gNOI Operational Commands

The gNMI server agent on Cumulus Linux supports <span class="a-tooltip">[gNOI](## "gRPC Network Operations Interface")</span> so that you can run operational tasks from a client, such as switch reboot or file transfer. The gNOI server is enabled when you configure {{<link url="gNMI-Streaming/#configure-gnmi-dial-in-mode" text="gNMI dial-in mode">}}. The gNOI server uses the same listening address, port, TLS configuration, and user credentials as your gNMI server configuration.

Cumulus Linux supports the following OpenConfig gNOI RPCs:

- {{<exlink url="https://github.com/openconfig/gnoi/blob/main/system/system.proto#L78" text="System Reboot">}}, supporting warm and cold reboot modes. The `reboot` gNOI RPC maps to the `nv action system reboot mode <mode>` command.
- {{<exlink url="https://github.com/openconfig/gnoi/blob/main/os/os.proto#L139" text="Software Image Install">}}, supporting copy operations of images to the switch. The `install` gNOI RPC maps to the `nv action fetch system image <image>` command.
- {{<exlink url="https://github.com/openconfig/gnoi/blob/main/os/os.proto#L145" text="Software Image Activation">}}, supporting optimized image installation and activation. The `activate` gNOI RPC maps to the `nv action install system image files <image>`, `nv action boot-next system image other`, and  `nv action system reboot mode <mode> commands if a reboot is requested.
- {{<exlink url="https://github.com/openconfig/gnoi/blob/main/os/os.proto#L46" text="Software Image Installation">}}
- {{<exlink url="https://github.com/openconfig/gnoi/blob/main/file/file.proto" text="File Management">}}, supporting retrieval, viewing, or deleting files. The following file management gNOI RPCs are supported:
  - {{<exlink url="https://github.com/openconfig/gnoi/blob/main/file/file.proto#L34" text="Get">}}, the equivalent of the `nv action upload system file-path [local-path] [remote-url]` command.
  - {{<exlink url="https://github.com/openconfig/gnoi/blob/main/file/file.proto#L52" text="Put">}}, the equivalent of the `nv action fetch system file-path [local-path][remote-url] [file-permissions]` command.
  - {{<exlink url="https://github.com/openconfig/gnoi/blob/main/file/file.proto#L57" text="Stat">}}, the equivalent of the `nv action list system file-path [local-path]` command.  
  - {{<exlink url="https://github.com/openconfig/gnoi/blob/main/file/file.proto#L62" text="Remove">}}, the equivalent of the `nv action delete system file-path [local-path]` command.

{{%notice note%}}
The following gNOI RPCs are not supported:
- system `cancel-reboot`
- system `reboot-status`
- system `set-package`
- system `reboot` with `--method=FAST` (fast reboot mode)
- file `transfer`
{{%/notice%}}


You can view the number of gNOI RPCs received on the switch with the `nv show system gnmi-server status gnoi-rpc` command:

```
cumulus@switch:mgmt:~$ nv show system gnmi-server status gnoi-rpc
gnoi-rpc-name failed-rpc-requests received-rpc-requests
------------- ------------------- ---------------------
File.Get      0                   4
File.Put      0                   1
File.Remove   0                   1
File.Stat     0                   46
OS.Install    0                   1
```

#### gNOI Client Requests

You can use your gNOI client to send supported RPCs to a switch for operational commands.

The following example uses the `Stat` RPC to view the `/var/support` directory on a switch:

```
cumulus@host:mgmt:~$ gnoic  --username test1 --password test1 --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key file stat --path /var/support/
+--------------------+----------------------------------------------------------+----------------------+------------+------------+---------+
|    Target Name     |                           Path                           |     LastModified     |    Perm    |   Umask    |  Size   |
+--------------------+----------------------------------------------------------+----------------------+------------+------------+---------+
| 10.1.1.100:9339 | /var/support//cl_support_mlx-3700-79_20251031_171813.txz | 2025-10-31T17:18:54Z | -rw-r--r-- | -----w--w- | 9992512 |
|                    | /var/support//core                                       | 2025-10-30T21:49:56Z | drwxr-xr-x | -----w--w- | 4096    |
+--------------------+----------------------------------------------------------+----------------------+------------+------------+---------+
cumulus@host:mgmt:~$
```

The following example uses the file `get` RPC to retrieve the `/var/support/cl_support_mlx-3700-79_20251031_171813.txz` file and copy it to `/tmp/` on the local client system.

```
cumulus@host:mgmt:~$ gnoic  --username test1 --password test1 --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key file get --file /var/support/cl_support_mlx-3700-79_20251031_171813.txz --dst /tmp/
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 1048576 bytes
INFO[0001] "10.1.1.100:9339" received 555328 bytes
INFO[0001] "10.1.1.100:9339" file "/var/support/cl_support_mlx-3700-79_20251031_171813.txz" saved
cumulus@host:mgmt:~$
```

The following example uses the file `remove` RPC to delete the `/var/support/cl_support_mlx-3700-79_20251031_171813.txz` file on the switch.

```
cumulus@host:mgmt:~$ gnoic  --username root --password NvidiaR0ots! --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key file remove --path /var/support/cl_support_mlx-3700-79_20251031_171813.txz
INFO[0000] "10.1.1.100:9339" file "/var/support/cl_support_mlx-3700-79_20251031_171813.txz" removed successfully
cumulus@host:mgmt:~$
```

The following example uses the file `put` RPC to copy the `/tmp/gnmic_ca.crt` file on the local client host to the switch at `/tmp/gnmic.crt`:

```
cumulus@host:mgmt:~$ gnoic  --username test1 --password test1 --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key file put --file /tmp/gnmic_ca.crt --dst /tmp/gnmi.crt
INFO[0000] "10.1.1.100:9339" sending file="/tmp/gnmic_ca.crt" hash
INFO[0000] "10.1.1.100:9339" file "/tmp/gnmic_ca.crt" written successfully
cumulus@host:mgmt:~$
```

The following example uses the `install` RPC to copy the `/media/node/cumulus-linux-mlx-amd64-5.16.bin.devsigned` image file on the local client to the switch with the version `5.16.0`:

```
cumulus@host:mgmt:~$ gnoic  --username test1 --password test1 --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key os install --pkg /media/node/cumulus-linux-mlx-amd64-5.16.bin.devsigned --version 5.16.0
INFO[0000] starting install RPC
INFO[0000] target "10.1.1.100:9339": starting Install stream
INFO[0000] target "10.1.1.100:9339": TransferProgress bytes_received:5242880
INFO[0000] target "10.1.1.100:9339": TransferProgress bytes_received:10485760
...
INFO[0011] target "10.1.1.100:9339": TransferProgress bytes_received:980418560
INFO[0011] target "10.1.1.100:9339": TransferProgress bytes_received:985661440
INFO[0011] target "10.1.1.100:9339": sending TransferEnd
INFO[0011] target "10.1.1.100:9339": TransferProgress bytes_received:990904320
INFO[0011] target "10.1.1.100:9339": TransferContent done...
INFO[0011] target "10.1.1.100:9339": TransferProgress bytes_received:994600465
cumulus@host:mgmt:~$
```

The following example uses the `activate` RPC to activate the `5.16.0` image as the next boot image without reboot the switch:

```
cumulus@host:mgmt:~$ gnoic  --username test1 --password test1 --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key os activate --version 5.16.0 --no-reboot
INFO[0190] target "10.1.1.100:9339" activate response "activate_ok:{}"
cumulus@host:mgmt:~$
```

The following example uses the `activate` RPC to activate the `5.16.0` image as the next boot image and reboots the switch.

```
cumulus@host:mgmt:~$ gnoic  --username cumulus --password NvidiaR0cks! --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key os activate --version 5.16.0 
INFO[0182] target "10.1.1.100:9339" activate response "activate_ok:{}"
cumulus@host:mgmt:~$
```

The following example uses the system `reboot` RPC to reboot the switch with warm reboot mode:

```
cumulus@host:mgmt:~$ gnoic  --username test1 --password test1 --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key system reboot --method WARM
INFO[0074] "10.1.1.100:9339" System Reboot Request successful
cumulus@host:mgmt:~$
```

{{%notice infonopad%}}
When you issue a switch reboot with the gNOI system `reboot` RPC or the `activate` RPC without the `--no-reboot` option, the switch reboots immediately; no confirmation is required.
{{%/notice%}}

## gNMI with NetQ

This section discusses how to configure and use gNMI with NetQ. To configure and use gNMI with Cumulus Linux, see {{<link url="/#gnmi-with-cumulus-linux" text="gNMI with Cumulus Linux">}}.

### Configure the gNMI Agent

The `netq-agent` package includes the gNMI agent, which it disables by default. To enable the gNMI agent:

```
cumulus@switch:~$ sudo systemctl enable netq-agent.service
cumulus@switch:~$ sudo systemctl start netq-agent.service
cumulus@switch:~$ netq config add agent gnmi-enable true
cumulus@switch:~$ netq config restart agent
```

The gNMI agent listens over port 9339. You can change the default port in case you use that port in another application. The `/etc/netq/netq.yml` file stores the configuration.

Use the following commands to adjust the settings:

1. Disable the gNMI agent:

   ```
   cumulus@switch:~$ netq config add agent gnmi-enable false
   ```

2. Change the default port over which the gNMI agent listens:

   ```
   cumulus@switch:~$ netq config add agent gnmi-port <gnmi_port>
   ```

3. Restart the NetQ Agent to incorporate the configuration changes:

   ```
   cumulus@switch:~$ netq config restart agent
   ```

{{%notice note%}}
The gNMI agent relies on the data it collects from the NVUE service. For complete data collection with gNMI, you must enable the NVUE service. To check the status of the `nvued` service, run the `sudo systemctl status nvued.service` command:

```
cumulus@switch:mgmt:~$ sudo systemctl status nvued.service
● nvued.service - NVIDIA User Experience Daemon
   Loaded: loaded (/lib/systemd/system/nvued.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2023-03-09 20:00:17 UTC; 6 days ago
```

If necessary, enable and start the service:

```
cumulus@switch:mgmt:~$ sudo systemctl enable nvued.service
cumulus@switch:mgmt:~$ sudo systemctl start nvued.service
```

{{%/notice%}}

### Use the gNMI Agent Only

NVIDIA recommends that you collect data with both the gNMI and NetQ agents. However, if you do not want to collect data with both agents or you are not streaming data to NetQ, you can disable the NetQ agent. Cumulus Linux then sents data only to the gNMI agent.

To disable the NetQ agent:

```
cumulus@switch:~$ netq config add agent opta-enable false
```

{{%notice note%}}
You cannot disable both the NetQ and gNMI agent. If you enable both agents on Cumulus Linux and a NetQ server is unreachable, the switch does not send the data to gNMI from the following models:
- `openconfig-interfaces`
- `openconfig-if-ethernet`
- `openconfig-if-ethernet-ext`
- `openconfig-system`
- `nvidia-if-ethernet-ext`

WJH, `openconfig-platform`, and `openconfig-lldp` data continue streaming to gNMI in this state. If you are only using gNMI and a NetQ telemetry server does not exist, disable the NetQ agent by setting `opta-enable` to `false`.
{{%/notice%}}

### Supported Subscription Modes

Cumulus Linux supports the following gNMI {{<exlink url="https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#3515-creating-subscriptions" text="subscription modes">}}:

- `POLL` mode
- `ONCE` mode
- `STREAM` mode, supported for `ON_CHANGE` subscriptions only

### Supported Models

Cumulus Linux supports the following OpenConfig models:
<!-- vale off -->
| Model| Supported Data |
| --------- | ------ |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-interfaces.yang" text="openconfig-interfaces">}} | Name, Operstatus, AdminStatus, IfIndex, MTU, LoopbackMode, Enabled, Counters (InPkts, OutPkts, InOctets, InUnicastPkts, InDiscards, InMulticastPkts, InBroadcastPkts, InErrors, OutOctets, OutUnicastPkts, OutMulticastPkts, OutBroadcastPkts, OutDiscards, OutErrors) |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-if-ethernet.yang" text="openconfig-if-ethernet">}} | AutoNegotiate, PortSpeed, MacAddress, NegotiatedPortSpeed, Counters (InJabberFrames, InOversizeFrames,​ InUndersizeFrames)|
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-if-ethernet-ext.yang" text="openconfig-if-ethernet-ext">}} | Frame size counters (InFrames_64Octets, InFrames_65_127Octets, InFrames_128_255Octets, InFrames_256_511Octets, InFrames_512_1023Octets, InFrames_1024_1518Octets) |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/system/openconfig-system.yang" text="openconfig-system">}} | Memory, CPU |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/platform/openconfig-platform.yang" text="openconfig-platform">}} | Platform data (Name, Description, Version) |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/lldp/openconfig-lldp.yang" text="openconfig-lldp">}} | LLDP data (PortIdType, PortDescription, LastUpdate, SystemName, SystemDescription, ChassisId, Ttl, Age, ManagementAddress, ManagementAddressType, Capability) |

| Model| Supported Data |
| --------- | ------ |
| nvidia-if-wjh-drop-aggregate | Aggregated WJH drops, including layer 1, layer 2, router, ACL, tunnel, and buffer drops |
| nvidia-if-ethernet-ext | Extended Ethernet counters (AlignmentError, InAclDrops, InBufferDrops, InDot3FrameErrors, InDot3LengthErrors, InL3Drops, InPfc0Packets, InPfc1Packets, InPfc2Packets, InPfc3Packets, InPfc4Packets, InPfc5Packets, InPfc6Packets, InPfc7Packets, OutNonQDrops, OutPfc0Packets, OutPfc1Packets, OutPfc2Packets, OutPfc3Packets, OutPfc4Packets, OutPfc5Packets, OutPfc6Packets, OutPfc7Packets, OutQ0WredDrops, OutQ1WredDrops, OutQ2WredDrops, OutQ3WredDrops, OutQ4WredDrops, OutQ5WredDrops, OutQ6WredDrops, OutQ7WredDrops, OutQDrops, OutQLength, OutWredDrops, SymbolErrors, OutTxFifoFull)|

The client can use the following YANG models as a reference:

{{<expand "nvidia-if-ethernet-ext">}}
```
module nvidia-if-ethernet-counters-ext {
    // xPath --> /interfaces/interface[name=*]/ethernet/counters/state/

   namespace "http://nvidia.com/yang/nvidia-ethernet-counters";
   prefix "nvidia-if-ethernet-counters-ext";


  // import some basic types
  import openconfig-interfaces { prefix oc-if; }
  import openconfig-if-ethernet { prefix oc-eth; }
  import openconfig-yang-types { prefix oc-yang; }


  revision "2021-10-12" {
    description
      "Initial revision";
    reference "1.0.0.";
  }

  grouping ethernet-counters-ext {

    leaf alignment-error {
      type oc-yang:counter64;
    }

    leaf in-acl-drops {
      type oc-yang:counter64;
    }

    leaf in-buffer-drops {
      type oc-yang:counter64;
    }

    leaf in-dot3-frame-errors {
      type oc-yang:counter64;
    }

    leaf in-dot3-length-errors {
      type oc-yang:counter64;
    }

    leaf in-l3-drops {
      type oc-yang:counter64;
    }

    leaf in-pfc0-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc1-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc2-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc3-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc4-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc5-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc6-packets {
      type oc-yang:counter64;
    }

    leaf in-pfc7-packets {
      type oc-yang:counter64;
    }

    leaf out-non-q-drops {
      type oc-yang:counter64;
    }

    leaf out-pfc0-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc1-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc2-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc3-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc4-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc5-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc6-packets {
      type oc-yang:counter64;
    }

    leaf out-pfc7-packets {
      type oc-yang:counter64;
    }

    leaf out-q0-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q1-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q2-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q3-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q4-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q5-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q6-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q7-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q8-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q9-wred-drops {
      type oc-yang:counter64;
    }

    leaf out-q-drops {
      type oc-yang:counter64;
    }

    leaf out-q-length {
      type oc-yang:counter64;
    }

    leaf out-wred-drops {
      type oc-yang:counter64;
    }

    leaf symbol-errors {
      type oc-yang:counter64;
    }

    leaf out-tx-fifo-full {
      type oc-yang:counter64;
    }

  }

  augment "/oc-if:interfaces/oc-if:interface/oc-eth:ethernet/" +
    "oc-eth:state/oc-eth:counters" {
      uses ethernet-counters-ext;
  }

}
```
{{</expand>}}
{{<expand "nvidia-if-wjh-drop-aggregate">}}

```
module nvidia-wjh {
    // Entrypoint /oc-if:interfaces/oc-if:interface
    //
    // xPath L1     --> interfaces/interface[name=*]/wjh/aggregate/l1
    // xPath L2     --> /interfaces/interface[name=*]/wjh/aggregate/l2/reasons/reason[id=*][severity=*]
    // xPath Router --> /interfaces/interface[name=*]/wjh/aggregate/router/reasons/reason[id=*][severity=*]
    // xPath Tunnel --> /interfaces/interface[name=*]/wjh/aggregate/tunnel/reasons/reason[id=*][severity=*]
    // xPath Buffer --> /interfaces/interface[name=*]/wjh/aggregate/buffer/reasons/reason[id=*][severity=*]
    // xPath ACL    --> /interfaces/interface[name=*]/wjh/aggregate/acl/reasons/reason[id=*][severity=*]

    import openconfig-interfaces { prefix oc-if; }

    namespace "http://nvidia.com/yang/what-just-happened-config";
    prefix "nvidia-wjh";

    revision "2021-10-12" {
        description
            "Initial revision";
        reference "1.0.0.";
    }

    augment "/oc-if:interfaces/oc-if:interface" {
        uses interfaces-wjh;
    }

    grouping interfaces-wjh {
        description "Top-level grouping for What-just happened data.";
        container wjh {
            container aggregate {
                container l1 {
                    container state {
                        leaf drop {
                            type string;
                            description "Drop list based on wjh-drop-types module encoded in JSON";
                        }
                    }
                }
                container l2 {
                    uses reason-drops;
                }
                container router {
                    uses reason-drops;
                }
                container tunnel {
                    uses reason-drops;
                }
                container acl {
                    uses reason-drops;
                }
                container buffer {
                    uses reason-drops;
                }
            }
        }
    }

    grouping reason-drops {
        container reasons {
            list reason {
                key "id severity";
                leaf id {
                    type leafref {
                        path "../state/id";
                    }
                    description "reason ID";
                }
                leaf severity {
                    type leafref {
                        path "../state/severity";
                    }
                    description "Reason severity";
                }
                container state {
                    leaf id {
                        type uint32;
                        description "Reason ID";
                    }
                    leaf name {
                        type string;
                        description "Reason name";
                    }
                    leaf severity {
                        type string;
                        mandatory "true";
                        description "Reason severity";
                    }
                    leaf drop {
                        type string;
                        description "Drop list based on wjh-drop-types module encoded in JSON";
                    }
                }
            }
        }
    }
}

module wjh-drop-types {
    namespace "http://nvidia.com/yang/what-just-happened-config-types";
    prefix "wjh-drop-types";

    container l1-aggregated {
        uses l1-drops;
    }
    container l2-aggregated {
        uses l2-drops;
    }
    container router-aggregated {
        uses router-drops;
    }
    container tunnel-aggregated {
        uses tunnel-drops;
    }
    container acl-aggregated {
        uses acl-drops;
    }
    container buffer-aggregated {
        uses buffer-drops;
    }

    grouping reason-key {
        leaf id {
            type uint32;
            mandatory "true";
            description "reason ID";
        }
        leaf severity {
            type string;
            mandatory "true";
            description "Severity";
        }
    }

    grouping reason_info {
        leaf reason {
                type string;
                mandatory "true";
                description "Reason name";
        }
        leaf drop_type {
            type string;
            mandatory "true";
            description "reason drop type";
        }
        leaf ingress_port {
            type string;
            mandatory "true";
            description "Ingress port name";
        }
        leaf ingress_lag {
            type string;
            description "Ingress LAG name";
        }
        leaf egress_port {
            type string;
            description "Egress port name";
        }
        leaf agg_count {
            type uint64;
            description "Aggregation count";
        }
        leaf severity {
            type string;
            description "Severity";
        }
        leaf first_timestamp {
            type uint64;
            description "First timestamp";
        }
        leaf end_timestamp {
            type uint64;
            description "End timestamp";
        }
    }

    grouping packet_info {
        leaf smac {
            type string;
            description "Source MAC";
        }
        leaf dmac {
            type string;
            description "Destination MAC";
        }
        leaf sip {
            type string;
            description "Source IP";
        }
        leaf dip {
            type string;
            description "Destination IP";
        }
        leaf proto {
            type uint32;
            description "Protocol";
        }
        leaf sport {
            type uint32;
            description "Source port";
        }
        leaf dport {
            type uint32;
            description "Destination port";
        }
    }

    grouping l1-drops {
        description "What-just happened drops.";
        leaf ingress_port {
            type string;
            description "Ingress port";
        }
        leaf is_port_up {
            type boolean;
            description "Is port up";
        }
        leaf port_down_reason {
            type string;
            description "Port down reason";
        }
        leaf description {
            type string;
            description "Description";
        }
        leaf state_change_count {
            type uint64;
            description "State change count";
        }
        leaf symbol_error_count {
            type uint64;
            description "Symbol error count";
        }
        leaf crc_error_count {
            type uint64;
            description "CRC error count";
        }
        leaf first_timestamp {
            type uint64;
            description "First timestamp";
        }
        leaf end_timestamp {
            type uint64;
            description "End timestamp";
        }
        leaf timestamp {
            type uint64;
            description "Timestamp";
        }
    }
    grouping l2-drops {
        description "What-just happened drops.";
        uses reason_info;
        uses packet_info;
    }

    grouping router-drops {
        description "What-just happened drops.";
        uses reason_info;
        uses packet_info;
    }

    grouping tunnel-drops {
        description "What-just happened drops.";
        uses reason_info;
        uses packet_info;
    }

    grouping acl-drops {
        description "What-just happened drops.";
        uses reason_info;
        uses packet_info;
        leaf acl_rule_id {
            type uint64;
            description "ACL rule ID";
        }
        leaf acl_bind_point {
            type uint32;
            description "ACL bind point";
        }
        leaf acl_name {
            type string;
            description "ACL name";
        }
        leaf acl_rule {
            type string;
            description "ACL rule";
        }
    }

    grouping buffer-drops {
        description "What-just happened drops.";
        uses reason_info;
        uses packet_info;
        leaf traffic_class {
            type uint32;
            description "Traffic Class";
        }
        leaf original_occupancy {
            type uint32;
            description "Original occupancy";
        }
        leaf original_latency {
            type uint64;
            description "Original latency";
        }
    }
}
```

{{</expand>}}
<!-- vale on -->
### Collect WJH Data with gNMI

You can export {{<link title="What Just Happened (WJH)" text="What Just Happened (WJH)">}} data from the NetQ agent to your own gNMI client. Refer to the `nvidia-if-wjh-drop-aggregate` reference YANG model, above.

The gNMI Agent supports `Capabilities` and `STREAM` subscribe requests for WJH events.

### WJH Drop Reasons
<!-- vale off -->
The data that NetQ sends to the gNMI agent is in the form of WJH drop reasons. The SDK generates the drop reasons and Cumulus Linux stores them in the `/usr/etc/wjh_lib_conf.xml` file. Use this file as a guide to filter for specific reason types (L1, ACL, and so on), reason IDs, or event severeties.

#### Layer 1 Drop Reasons

<!-- L1 aggregate drops do not have severity column as it's missing from the SDK, and hence it's not exported -->

| Reason ID | Reason | Description |
| --------- | ------ | ----------- |
| 10021 | Port admin down | Validate port configuration |
| 10022 | Auto-negotiation failure | Set port speed manually, disable auto-negotiation |
| 10023 | Logical mismatch with peer link | Check cable or transceiver |
| 10024 | Link training failure | Check cable or transceiver |
| 10025 | Peer is sending remote faults | Replace cable or transceiver |
| 10026 | Bad signal integrity | Replace cable or transceiver |
| 10027 | Cable or transceiver is not supported | Use supported cable or transceiver |
| 10028 | Cable or transceiver is unplugged | Plug cable or transceiver |
| 10029 | Calibration failure | Check cable or transceiver |
| 10030 | Cable or transceiver bad status | Check cable or transceiver |
| 10031 | Other reason | Other L1 drop reason|

#### Layer 2 Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 201 | MLAG port isolation | Notice | Expected behavior |
| 202 | Destination MAC is reserved (DMAC=01-80-C2-00-00-0x) | Error | Bad packet received from the peer |
| 203 | VLAN tagging mismatch | Error | Validate the VLAN tag configuration on both ends of the link |
| 204 | Ingress VLAN filtering | Error | Validate the VLAN membership configuration on both ends of the link |
| 205 | Ingress spanning tree filter | Notice | Expected behavior |
| 206 | Unicast MAC table action discard | Error | Validate MAC table for this destination MAC |
| 207 | Multicast egress port list is empty | Warning | Validate why IGMP join or multicast router port does not exist |
| 208 | Port loopback filter | Error | Validate MAC table for this destination MAC |
| 209 | Source MAC is multicast | Error | Bad packet received from peer |
| 210 | Source MAC equals destination MAC | Error | Bad packet received from peer |

#### Router Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 301 | Non-routable packet | Notice | Expected behavior |
| 302 | Blackhole route | Warning | Validate routing table for this destination IP |
| 303 | Unresolved neighbor or next hop | Warning | Validate ARP table for the neighbor or next hop |
| 304 | Blackhole ARP or neighbor | Warning | Validate ARP table for the next hop |
| 305 | IPv6 destination in multicast scope FFx0:/16 | Notice | Expected behavior - packet is not routable |
| 306 | IPv6 destination in multicast scope FFx1:/16 | Notice | Expected behavior - packet is not routable |
| 307 | Non-IP packet | Notice | Destination MAC is the router, packet is not routable |
| 308 | Unicast destination IP but multicast destination MAC | Error | Bad packet received from the peer |
| 309 | Destination IP is loopback address | Error | Bad packet received from the peer |
| 310 | Source IP is multicast | Error | Bad packet received from the peer |
| 311 | Source IP is in class E | Error | Bad packet received from the peer |
| 312 | Source IP is loopback address | Error | Bad packet received from the peer |
| 313 | Source IP is unspecified | Error | Bad packet received from the peer |
| 314 | Checksum or IPver or IPv4 IHL too short | Error | Bad cable or bad packet received from the peer |
| 315 | Multicast MAC mismatch | Error | Bad packet received from the peer |
| 316 | Source IP equals destination IP | Error | Bad packet received from the peer |
| 317 | IPv4 source IP is limited broadcast | Error | Bad packet received from the peer |
| 318 | IPv4 destination IP is local network (destination=0.0.0.0/8) | Error | Bad packet received from the peer || 319 | IPv4 destination IP is link local (destination in 169.254.0.0/16) | Error | Bad packet received from the peer |
| 320 | Ingress router interface is disabled | Warning | Validate your configuration |
| 321 | Egress router interface is disabled | Warning | Validate your configuration |
| 323 | IPv4 routing table (LPM) unicast miss | Warning | Validate routing table for this destination IP |
| 324 | IPv6 routing table (LPM) unicast miss | Warning | Validate routing table for this destination IP |
| 325 | Router interface loopback | Warning | Validate the interface configuration |
| 326 | Packet size is larger than router interface MTU | Warning | Validate the router interface MTU configuration |
| 327 | TTL value is too small | Warning | Actual path is longer than the TTL |

#### Tunnel Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 402 | Overlay switch - Source MAC is multicast | Error | The peer sent a bad packet |
| 403 | Overlay switch - Source MAC equals destination MAC | Error | The peer sent a bad packet |
| 404 | Decapsulation error | Error | The peer sent a bad packet |

#### ACL Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 601 | Ingress port ACL | Notice | Validate Access Control List configuration |
| 602 | Ingress router ACL | Notice | Validate Access Control List |
| 603 | Egress router ACL | Notice | Validate Access Control List |
| 604 | Egress port ACL | Notice | Validate Access Control List |

#### Buffer Drop Reasons

| Reason ID | Reason | Severity | Description |
| --------- | ------ | -------- | ----------- |
| 503 | Tail drop | Warning | Monitor network congestion |
| 504 | WRED | Warning | Monitor network congestion |
| 505 | Port TC congestion threshold crossed | Notice | Monitor network congestion |
| 506 | Packet latency threshold crossed | Notice | Monitor network congestion |

### gNMI Client Requests

You can use your gNMI client on a host to request capabilities and data to which the Agent subscribes. The examples below use the {{<exlink url="https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#3515-creating-subscriptions" text="gNMIc client.">}}.

The following example shows a gNMIc `STREAM` request for WJH data:

```
gnmic -a 10.209.37.121:9339 -u cumulus -p ****** --skip-verify subscribe --path "wjh/aggregate/l2/reasons/reason[id=209][severity=error]/state/drop" --mode stream --prefix "/interfaces/interface[name=swp8]/" --target netq

{
  "source": "10.209.37.121:9339",
  "subscription-name": "default-1677695197",
  "timestamp": 1677695102858146800,
  "time": "2023-03-01T18:25:02.8581468Z",
  "prefix": "interfaces/interface[name=swp8]/wjh/aggregate/l2/reasons/reason[severity=error][id=209]",
  "target": "netq",
  "updates": [
    {
      "Path": "state/drop",
      "values": {
        "state/drop": "[{\"AggCount\":283,\"Dip\":\"0.0.0.0\",\"Dmac\":\"1c:34:da:17:93:7c\",\"Dport\":0,\"DropType\":\"L2\",\"EgressPort\":\"\",\"EndTimestamp\":1677695102,\"FirstTimestamp\":1677695072,\"Hostname\":\"neo-switch01\",\"IngressLag\":\"\",\"IngressPort\":\"swp8\",\"Proto\":0,\"Reason\":\"Source MAC is multicast\",\"ReasonId\":209,\"Severity\":\"Error\",\"Sip\":\"0.0.0.0\",\"Smac\":\"01:00:5e:00:00:01\",\"Sport\":0}]"
      }
    }
  ]
}
{
  "source": "10.209.37.121:9339",
  "subscription-name": "default-1677695197",
  "timestamp": 1677695132988218890,
  "time": "2023-03-01T18:25:32.98821889Z",
  "prefix": "interfaces/interface[name=swp8]/wjh/aggregate/l2/reasons/reason[severity=error][id=209]",
  "target": "netq",
  "updates": [
    {
      "Path": "state/drop",
      "values": {
        "state/drop": "[{\"AggCount\":287,\"Dip\":\"0.0.0.0\",\"Dmac\":\"1c:34:da:17:93:7c\",\"Dport\":0,\"DropType\":\"L2\",\"EgressPort\":\"\",\"EndTimestamp\":1677695132,\"FirstTimestamp\":1677695102,\"Hostname\":\"neo-switch01\",\"IngressLag\":\"\",\"IngressPort\":\"swp8\",\"Proto\":0,\"Reason\":\"Source MAC is multicast\",\"ReasonId\":209,\"Severity\":\"Error\",\"Sip\":\"0.0.0.0\",\"Smac\":\"01:00:5e:00:00:01\",\"Sport\":0}]"
      }
    }
  ]
}
```

The following example shows a gNMIc `ONCE` mode request for interface port speed:

```
gnmic -a 10.209.37.121:9339 -u cumulus -p ****** --skip-verify subscribe --path "ethernet/state/port-speed" --mode once --prefix "/interfaces/interface[name=swp1]/" --target netq
{
  "source": "10.209.37.123:9339",
  "subscription-name": "default-1677695151",
  "timestamp": 1677256036962254134,
  "time": "2023-02-24T16:27:16.962254134Z",
  "target": "netq",
  "updates": [
    {
      "Path": "interfaces/interface[name=swp1]/ethernet/state/port-speed",
      "values": {
        "interfaces/interface/ethernet/state/port-speed": "SPEED_1GB"
      }
    }
  ]
}
```

The following example shows a gNMIc `POLL` mode request for interface status:

```
gnmic -a 10.209.37.121:9339 -u cumulus -p ****** --skip-verify subscribe --path "state/oper-status" --mode poll --prefix "/interfaces/interface[name=swp1]/" --target netq
{
  "timestamp": 1677644403153198642,
  "time": "2023-03-01T04:20:03.153198642Z",
  "prefix": "interfaces/interface[name=swp1]",
  "target": "netq",
  "updates": [
    {
      "Path": "state/oper-status",
      "values": {
        "state/oper-status": "UP"
      }
    }
  ]
}
received sync response 'true' from '10.209.37.123:9339'
{
  "timestamp": 1677644403153198642,
  "time": "2023-03-01T04:20:03.153198642Z",
  "prefix": "interfaces/interface[name=swp1]",
  "target": "netq",
  "updates": [
    {
      "Path": "state/oper-status",
      "values": {
        "state/oper-status": "UP"
      }
    }
  ]
}
```
<!-- vale on -->

### Considerations

When using gNMI with Cumulus Linux:
- The minimum sampling interval is 1 second. If you configure a shorter sampling interval, the switch might not behave as expected.
- ModelData, Origin, and Extensions fields are ignored in requests and not set in responses.

## Related Information

- {{<exlink url="https://datatracker.ietf.org/meeting/101/materials/slides-101-netconf-grpc-network-management-interface-gnmi-00" text="gNMI presentation to IETF">}}
- {{<exlink url="https://gnmic.openconfig.net/" text="gNMIc client">}}
- {{<exlink url="https://github.com/openconfig/reference/blob/master/rpc/gnmi/gnmi-specification.md#3515-creating-subscriptions" text="gNMI subscription mode documentation">}}
