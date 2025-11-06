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
To use both gNMI streaming with NetQ and gNMI streaming with Cumulus Linux, you must use different ports.
{{%/notice%}}

## gNMI with Cumulus Linux

This section discusses how to configure and use gNMI with Cumulus Linux.

To configure and use gNMI with NetQ, see {{<link url="/#gnmi-with-netq" text="gNMI with NetQ">}}.

{{%notice note%}}
- When you enable gNMI with Cumulus Linux, do **not** enable and use {{<link url="Open-Telemetry-Export" text="Open Telemetry">}}.
- Switches with the Spectrum 1 ASIC do not support gNMI streaming.
{{%/notice%}}

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
When you configure a CA certificate, entity certificate, or CRL, existing gNMI sessions are disconnected to apply the new certificate configuration.
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

### Configure gNMI Dial-Out Mode

In dial-out telemetry mode, the Cumulus Linux switch initiates the gRPC connection to the collector through a gRPC tunnel server and assumes the role of the gRPC client.

To configure gNMI dial-out mode, you must:
- Specify the listening address for each tunnel server to which you want to connect. Cumulus Linux supports a maximum of 10 tunnel servers.
- Enable the tunnel server.

To configure optional settings for each tunnel server:
- Specify the target name and target application you want to access. The default target application is GNMI-GNOI.
- Specify the retry interval. The default retry interval is 30 seconds.
- Import and enable a TLS or mTLS certificate for validation. You can also apply a <span class="a-tooltip">[CRL](## "Certificate Revocation List")</span>. For information about importing certificates and CRLs, refer to {{<link url="NVUE-CLI/#security-with-certificates-and-crls" text="Security with Certificates and CRLs">}}.

{{%notice note%}}
When you configure a CA certificate, entity certificate, or CRL, existing gNMI sessions are disconnected to apply the new certificate configuration.
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

Cumulus Linux supports the following metrics:
<!-- vale off -->
{{< tabs "TabID200 ">}}
{{< tab "Interface ">}}

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface/state/admin-status` | Admin state of an interface. |
| `/interfaces/interface/state/counters/in-broadcast-pkts` | Total number of broadcast packets received on an interface.|
| `/interfaces/interface/state/counters/in-multicast-pkts` | Total number of multicast packets received on an interface.|
| `/interfaces/interface/state/counters/in-octets` | Total number of octets received on an interface, including framing characters.|
| `/interfaces/interface/ethernet/state/counters/in-fcs-errors` | Total number of frames received on an interface that are an integral number of octets in length but do not pass the FCS check. This count does not include frames received with `frame-too-long` or `frame-too-short` error.|
| `/interfaces/interface/ethernet/state/counters/in-oversize-frames` | Total number of packets received longer than 1518 octets (excluding framing bits, but including FCS octets). |
| `/interfaces/interface/ethernet/state/counters/in-distribution/in-frames-1024-1518-octets` | Total number of packets (including bad packets) received between 1024 and 1518 octets in length inclusive (excluding framing bits but including FCS octets). |
| `/interfaces/interface/ethernet/state/counters/in-distribution/ in-frames-128-255-octets` | Total number of packets (including bad packets) received between 128 and 255 octets in length inclusive (excluding framing bits but including FCS octets).|
| `/interfaces/interface/ethernet/state/counters/in-distribution/in-frames-256-511-octets` | Total number of packets (including bad packets) received between 256 and 511 octets in length inclusive (excluding framing bits but including FCS octets).|
| `/interfaces/interface/ethernet/state/counters/in-distribution/in-frames-512-1023-octets` | Total number of packets (including bad packets) received between 512 and 1023 octets in length inclusive (excluding framing bits but including FCS octets).|
| `/interfaces/interface/ethernet/state/counters/in-distribution/in-frames-64-octets` | Total number of packets (including bad packets) received that are 64 octets in length (excluding framing bits but including FCS octets).|
| `/interfaces/interface/ethernet/state/counters/in-distribution/in-frames-65-127-octets` | Total number of packets (including bad packets) received between 65 and 127 octets in length inclusive (excluding framing bits but including FCS octets).|
| `/interfaces/interface/state/counters/out-broadcast-pkts` | Total number of broadcast packets transmitted out of an interface.|
| `/interfaces/interface/state/counters/out-octets` | Total number of octets transmitted out of an interface, including framing characters.|
| `/interfaces/interface/state/counters/out-unicast-pkts` | Total number of unicast packets transmitted out of an interface.|
| `/interfaces/interface/ethernet/state/port-speed` | An estimate of the interface current bandwidth in units of 1,000,000 bits per second.|
| `/interfaces/interface/rates/state/in-bits-rate` | Inbound bits per second on an interface.|
| `/interfaces/interface/state/ifindex` | A unique value, greater than zero, for each interface.|
| `/interfaces/interface/state/counters/in-discards` | Number of inbound packets discarded even though no errors are detected to prevent them from being deliverable to a higher-layer protocol. |
| `/interfaces/interface/state/counters/in-errors` | For packet-oriented interfaces, the number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.|
| `/interfaces/interface/state/counters/in-pkts`| Number of packets discarded from the egress queue of an interface. |
| `/interfaces/interface/state/counters/in-pkts-rate` | Inbound packets per second on an interface. |
| `/interfaces/interface/ethernet/state/counters/in-crc-errors` | Total number of frames received with a length (excluding framing bits, but including FCS octets) of between 64 and 1518 octets, inclusive, but had either a bad Frame Check Sequence (FCS) with an integral number of octets (FCS Error) or a bad FCS with a non-integral number of octets (Alignment Error).|
| `/interfaces/interface/ethernet/state/negotiated-duplex-mode` | When auto-negotiate is set to TRUE, and the interface has completed auto-negotiation with the remote peer, this value shows the negotiated duplex mode.|
| `/interfaces/interface/state/counters/in-acl-drops` | Number of inbound packets dropped because of an Access Control List (ACL).|
| `/interfaces/interface/ethernet/state/counters/in-mac-pause-frames` | Inbound MAC pause frames on an interface.|
| `/interfaces/interface/state/mtu` | Size of the largest packet that can be sent or received on the interface, specified in octets. For interfaces used for transmitting network datagrams, this is the size of the largest network datagram that the interface can send.|
| `/interfaces/interface/state/oper-status` | Current operational state of an interface. |
| `/interfaces/interface/rates/state/out-bits-rate` | Outbound bits per second on an interface. |
| `/interfaces/interface/state/counters/out-discards` | Number of outbound packets discarded even though no errors are detected to prevent them from being transmitted. |
| `/interfaces/interface/state/counters/out-errors` | For packet-oriented interfaces, the number of outbound packets not transmitted because of errors. For character-oriented or fixed-length interfaces, the number of outbound transmission units not transmitted because of errors. |
| `/interfaces/interface/state/counters/out-pkts` | Total number of packets transmitted out of the interface, including all unicast, multicast, broadcast, and bad packets.|
| `/interfaces/interface/state/counters/out-pkts-rate` | Outbound packets per second on an interface. |
| `/interfaces/interface/state/counters/out-multicast-pkts` | Total number of packets that higher-level protocols requested be transmitted, and which were addressed to a multicast address at this sub-layer, including those that were discarded or not sent. For a MAC layer protocol, this includes both Group and Functional addresses.|
| `/interfaces/interface/ethernet/state/counters/carrier-transitions` | Number of times since system boot that `ifOperStatus` changed.|
| `/interfaces/interface/ethernet/phy/state/rs-fec-uncorrectable-blocks` | Number of RS FEC uncorrectable blocks of an interface. |
| `/interfaces/interface/ethernet/phy/state/rs-fec-single-error-blocks` | Number of RS FEC uncorrectable blocks of an interface.|
| `/interfaces/interface/ethernet/phy/state/rs-fec-no-error-blocks` | Number of RS FEC no errors blocks of an interface.|
| `/interfaces/interface/ethernet/phy/state/lane/fc-fec-corrected-blocks` | Number FC FEC corrected blocks for a given lane of an interface.|
| `/interfaces/interface/ethernet/phy/state/lane/fc-fec-uncorrected-blocks` | Number of FC FEC uncorrectable blocks for a given lane of an interface. |
| `/interfaces/interface/ethernet/phy/state/lane/rs-fec-corrected-symbols` | Number of RS FEC corrected symbols for a given lane of an interface.|
| `/interfaces/interface/ethernet/phy/state/corrected-bits` | Number of phy corrected bits of an interface by the FEC engine.|
| `/interfaces/interface/ethernet/phy/state/effective-errors` | Number of phy effective errors of an interface.|
| `/interfaces/interface/ethernet/phy/state/effective-ber` | Phy effective BER of an interface.|
| `/interfaces/interface/ethernet/phy/state/lane/raw-errors` | Number of phy error bits identified for a given lane of an interface.|
| `/interfaces/interface/ethernet/phy/state/received-bits` | Number of phy total bits received for an interface.|
| `/interfaces/interface/ethernet/phy/state/symbol-errors` | Number of phy symbol errors for an interface.|
| `/interfaces/interface/ethernet/phy/state/symbol-ber` | Phy symbol BER for an interface.|
| `/interfaces/interface/ethernet/phy/state/lane/raw-ber` | Number of phy bit error rates for a given lane of an interface.|
| `/interfaces/interface/ethernet/phy/state/fec-time-since-last-clear` | Time after last clear of FEC stats(phy layer). |
| `/interfaces/interface/ethernet/phy/state/ber-time-since-last-clear` | Time after last clear of BER stats(phy layer). |

{{< /tab >}}
{{< tab "LLDP">}}

|  Name | Description |
|------ | ----------- |
| `/lldp/state/chassis-id` | The chassis component of the endpoint identifier associated with the transmitting LLDP agent.|
| `/lldp/state/chassis-id-type` | The format and source of the chassis identifier string.|
| `/lldp/state/system-description` | Description of the network entity including the full name and version identification of the system's hardware type, software operating system, and networking software.|
| `/lldp/state/system-name` | Administratively assigned name for the system.|
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/age` | LLDP neighbor age after discovery.|
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/management-address/type`| Enumerated value for the network address type identified in this TLV. |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/chassis-id` | Chassis component of the endpoint identifier associated with the transmitting LLDP agent.|
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/chassis-id-type` | Format and source of the chassis identifier string.|
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/system-name` | Administratively assigned name of the system associated with the transmitting LLDP agent.|
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/system-description` | Description of the network entity associated with the transmitting LLDP agent.|
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/port-id`| Port component of the endpoint identifier associated with the transmitting LLDP agent. |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/port-description` | Binary string containing the actual port identifier for the port from which this LLDP PDU was transmitted.|
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/port-id-type` | Format and source of the remote port ID string. |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/ttl` | Indicates how long information from the neighbor is considered valid. |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/capabilities/capability[name=<capability>]/state/enabled` | If the corresponding system capability is enabled on the neighbor.|

{{< /tab >}}
{{< tab "Platform">}}

|  Name | Description |
|------ | ----------- |
| `/components/component[name='PSU1']/state/name` | PSU Name.|
| `/components/component[name='PSU1']/state/oper-status` | PSU Status. |
| `/components/component[name='PSU1']/state/description` |  PSU description. |
| `/components/component[name='PSU1']/power-supply/state/capacity` | PSU capacity in watts. |
| `/components/component[name='PSU1']/power-supply/state/output-current` | PSU current in amperes. |
| `/components/component[name='PSU1']/power-supply/state/output-voltage` | PSU voltage in volts. |
| `/components/component[name='PSU1']/power-supply/state/output-power` | PSU power in watts. |
| `/components/component[name='fan0']/state/name` | Fan name. |
| `/components/component[name='fan0']/state/oper-status` | Fan Status. |
| `/components/component[name='fan0']/state/description` | Fan Description. |
| `/components/component[name='fan0']/fan/state/speed` | Current (instantaneous) fan speed. |
| `/components/component[name='temp-sensor0']/state/name` |  Temperature sensor name.|
| `/components/component[name='temp-sensor0'']/state/oper-status` |  Temperature sensor operational status. |
| `/components/component[name='temp-sensor0'']/state/description` | Temperature sensor description. |
| `/components/component[name='temp-sensor0']/state/temperature/instant` | Instant temperature.  |
| `/components/component[name='temp-sensor0']/state/temperature/alarm-status` | Temperature sensor alarm status. |
| `/components/component[name='transceiver+panelport#']/transceiver/physical-channels/channel[no]/state/input-power/instant` | Input optical power of a physical channel in units of 0.01dBm, which may be associated with individual physical channels or an aggregate of multiple physical channels. |
| `/components/component[name='transceiver+panelport#']/transceiver/physical-channels/channel[no]/state/laser-bias-current/instant` | Current applied by the system to the transmit laser to achieve the output power. The current is expressed in mA with up to two decimal precision. |
| `/components/component[name='transceiver+panelport']/transceiver/physical-channels/channel[no]/state/output-power/instant` | Output optical power of a physical channel in units of 0.01dBm, which might be associated with individual physical channels or an aggregate of multiple physical channels. |

{{< /tab >}}
{{< tab "QoS">}}

|  Name | Description |
|------ | ----------- |
| `/qos/interfaces/interface/state/switch-priority/counters/out-pause-pkts`| Number of pause packets for the priority class in the egress queue.|
| `/qos/interfaces/interface/state/priority-group/counters/watermark-max` | High watermark of cells used in a priority group since last time watermarks were reset. |
| `/qos/interfaces/interface/output/queues/queue/state/watermark-max` | High watermark of cells used in a queue since last time watermarks were reset. |
| `qos/interfaces/interface/output/queues/queue/state/ecn-marked-pkts`| Number of ECN marked packets from this egress queue. If the ECN counter is not enabled, the counter value is 0.|
| `qos/interfaces/interface/output/queues/queue/state/transmit-octets`| Number of transmitted bytes in the egress queue of an interface.|
| `qos/interfaces/interface/output/queues/queue/state/transmit-pkts`| Number of transmitted packets in the egress queue of an interface. |
| `/qos/interfaces/interface/output/queues/queue/state/wred-dropped-pkts` | Number of packets discarded from this egress queue of an interface. |
| `/qos/interfaces/interface/output/queues/queue/state/no-buffer-uc-dropped-pkts` | Number of packets discarded from this egress queue when there is no buffer left in the interface. |
| `/qos/interfaces/interface[interface-id]/output/queues/queue[name]/state/time-since-last-clear` | Time since last clear of watermarks in a queue.|
| `/qos/interfaces/interface[interface-id]/state/priority-group[priority_group]/counters/time-since-last-clear` | Time since last clear of watermarks in a priority group.|

{{< /tab >}}
{{< tab "Router">}}

|  Name | Description |
|------ | ----------- |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/session-state` | Operational state of the BGP peer.|
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/established-transitions` | Number of transitions to the established state for the neighbor session.|
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/messages/sent/UPDATE` | Number of BGP UPDATE messages announcing, withdrawing, or modifying paths exchanged.|
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/messages/received/UPDATE` | Number of BGP UPDATE messages announcing, withdrawing, or modifying paths exchanged.|
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/queues/input` | Number of messages received from the peer currently queued.|
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/queues/output` | Number of messages queued to be sent to the peer.|
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/afi-safis/afi-safi[afi-safi-name=<afi-safi-name>]/state/prefixes/received` | Number of prefixes received from the neighbor after applying policies (the number of prefixes present in the post-policy Adj-RIB-In for the neighbor).|
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/afi-safis/afi-safi[afi-safi-name=<afi-safi-name>]/state/prefixes/sent` | Number of prefixes advertised to the neighbor after applying policies (the number of prefixes present in the post-policy Adj-RIB-Out for the neighbor).|
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/afi-safis/afi-safi[afi-safi-name=<afi-safi-name>]/state/prefixes/installed` | Number of prefixes received from the neighbor that are installed in the network instance RIB and actively used for forwarding. |

{{< /tab >}}
{{< tab "System">}}

|  Name | Description |
|------ | ----------- |
| `/system/state/hostname` | System hostname. |
| `/system/state/software-version` | System software version. |
| `/system/state/boot-time` | System boot time. |
| `/system/state/current-datetime` | Current system date and time. |
| `/system/control-plane-traffic/ingress/ipv4/counters/`<br>`/system/control-plane-traffic/ingress/ipv6/counters/` | Number of input IP datagrams discarded in software including those received in error.|
| `/system/cpus/cpu[name=<cpu_id>]/state/user/seconds` | CPU user Seconds |
| `/system/cpus/cpu[name=<cpu_id>]/state/kernel/seconds` | CPU kernel seconds. |
| `/system/cpus/cpu[name=<cpu_id>]/state/nice/seconds` | CPU Nice seconds. |
| `/system/cpus/cpu[name=<cpu_id>]/state/idle/seconds` | CPU idle seconds. |
| `/system/cpus/cpu[name=<cpu_id>]/state/wait/seconds` | CPU wait seconds.|
| `/system/cpus/cpu[name=<cpu_id>]/state/hardware-interrupt/seconds` | CPU hardware interrupt seconds. |
| `/system/cpus/cpu[name=<cpu_id>]/state/software-interrupt/seconds` | CPU software interrupt seconds.|
| `/system/memory/state/free` | Free memory. |
| `/system/memory/state/physical` | Physical memory.|
| `/system/memory/state/reserved` | Memory reserved for system use. |
| `/system/mount-points/mount-point[name='filesystem0']/state/name` | Mount point name.|
| `/system/mount-points/mount-point[name='filesystem0']/state/storage-component` | A reference to the hosting component within the hierarchy. |
| `/system/mount-points/mount-point[name='filesystem0']/state/size` | Total size of the initialized filesystem.|
| `/system/mount-points/mount-point[name='filesystem0']/state/available` | Amount of unused space on the filesystem.|
| `/system/mount-points/mount-point[name='filesystem0']/state/type` | Filesystem type used for storage such flash, hard disk, tmpfsor or ramdisk, or remote or network based storage.|

{{< /tab >}}
{{< /tabs >}}
<!-- vale on -->
### User Credentials and Authentication

User authentication is enabled by default. gNMI subscription requests must include an HTTP Basic Authentication header according to RFC7617 containing the username and password of a user with NVUE API access permissions. You can enable this setting in the standard gNMI client (gNMIc) by setting the `auth-scheme` parameter to basic. Refer to {{<exlink url="https://gnmic.openconfig.net/global_flags/ - auth-scheme" text="https://gnmic.openconfig.net/global_flags/ - auth-scheme">}}.

{{%notice note%}}
Cumulus Linux ignores credentials in RPC metadata.
{{%/notice%}}

### gNMI Client Requests

You can use your gNMI client on a host to request capabilities and data to which the Agent subscribes. The examples below use the gNMIc client.

#### Dial-in Mode Example

The following example shows a Dial-in Mode Subscribe request:

```
gnmic subscribe --mode stream --path "/qos/interfaces/interface[interface-id=swp1]/output/queues/queue[name=1]/state/transmit-octets" -i 10s --tls-cert gnmi_client.crt --tls-key gnmi_client.key -u cumulus -p ******* --auth-scheme Basic --skip-verify -a 10.188.52.108:9339
```

#### Subscription Example

The following example shows a subscription response:
<!-- vale off -->
```
{ 
  "sync-response": true 
} 
{ 
  "source": "10.188.52.108:9339", 
  "subscription-name": "default-1737725382", 
  "timestamp": 1737725390247535267, 
  "time": "2025-01-24T13:29:50.247535267Z", 
  "updates": [ 
    { 
      "Path": "qos/interfaces/interface[interface-id=swp1]/output/queues/queue[name=1]/state/transmit-octets", 
      "values": { 
        "qos/interfaces/interface/output/queues/queue/state/transmit-octets": 0 
      } 
    } 
  ] 
} 
...
```

#### Capabilities Example

The following example shows a capabilities request:

```
gnmic capabilities --tls-cert gnmic-cert.pem --tls-key gnmic-key.pem -u cumulus -p ****** --auth-scheme Basic --skip-verify -a 10.188.52.108:9339
```

The following example shows the expected response to a capabilities request:

```
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
<!-- vale on -->
## gNMI with NetQ

This section discusses how to configure and use gNMI with NetQ.

To configure and use gNMI with Cumulus Linux, see {{<link url="/#gnmi-with-cumulus-linux" text="gNMI with Cumulus Linux">}}.

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
