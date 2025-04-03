---
title: gNMI Streaming
author: NVIDIA
weight: 1234
toc: 4
---
You can use {{<exlink url="https://github.com/openconfig/gnmi" text="gRPC Network Management Interface">}} (gNMI) to collect system metrics and export the data to a gNMI client.

{{%notice note%}}
When you enable gNMI, do not use {{<link url="Open-Telemetry-Export" text="Open Telemetry">}}.
{{%/notice%}}

## Configure gNMI

Cumulus Linux supports both gNMI dial-in mode, where a collector can initiate a connection with the switch to collect available statistics, and gNMI dial-out mode, where the switch streams statistics and exports them to a collector.

### Configure gNMI Dial-in Mode

In dial-in telemetry mode, the data collector initiates the <span class="a-tooltip">[gRPC](## "Remote Procedure Calls")</span> connection, the Cumulus Linux switch assumes the role of the gRPC server and the receiver (collector) is the client. The switch pushes data to the collector.

To configure gNMI dial-in mode, you must:
- Specify the gNMI server listening address
- Enable the gNMI server.

To configure optional settings for gNMI dial-in mode:
- Specify the listening port. The default port is 9339.
- Enable a TLS certificate for validation.
  - Cumulus Linux uses a self-signed certificate. You can generate your own TLS server certificate and bind it with the gNMI server application.
  - If mTLS on the gNMI RPC is required, import the certificate of the CA that signed the gNMI client keys (or the client certificate itself) to the switch and configure the gNMI server to use the certificate.

The following example sets the gNMI server listening address to 10.10.10.1 and the port to 443, and enables the gNMI server:

```
cumulus@switch:~$ nv set system gnmi-server listening-address 10.10.10.1
cumulus@switch:~$ nv set system gnmi-server port 443
cumulus@switch:~$ nv set system gnmi-server state enabled
cumulus@switch:~$ nv config apply
```

The following example imports and enables the CA certificate CERT1 for mTLS:

```
cumulus@switch:~$ nv action import system security certificate CERT1 passphrase mypassphrase uri-bundle scp://user@pass:1.2.3.4:/opt/certs/cert.p12
cumulus@switch:~$ nv set system gnmi-server mtls ca-certificate CERT1
cumulus@switch:~$ nv config apply
```

### Configure gNMI Dial-Out Mode

In dial-out telemetry mode, the Cumulus Linux switch initiates the gRPC connection to the collector through a gRPC tunnel server and assumes the role of the gRPC client.

To configure gNMI dial-out mode, you must:
- Set the gNMI server listening address to localhost.
- Specify the listening address for each tunnel server to which you want to connect. Cumulus Linux supports a maximum of 10 tunnel servers.
- Enable the tunnel server.

To configure optional settings for each tunnel server:
- Specify the target name and target application you want to access. The default target application is GNMI-GNOI.
- Specify the retry interval. The default retry interval is 30 seconds.
- Import and enable a TLS certificate for validation.

The following example sets the listening address for the gNMI server to localhost, the listening address for tunnel server SERVER1 to 10.1.1.10, and enables the tunnel server:

```
cumulus@switch:~$ nv set system gnmi-server listening-address localhost 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 address 10.1.1.10 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 state enabled 
cumulus@switch:~$ nv config apply
```

The following example sets the listening address for the gNMI server to localhost, the listening address for tunnel server SERVER1 to 10.1.1.10 and the port to 443, the target name to TARGET1, the retry interval to 40, the CA certificate to CACERT, and enables the tunnel server:

```
cumulus@switch:~$ nv set system gnmi-server listening-address localhost 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 address 10.1.1.10 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 port 443 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 target-name TARGET1 
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 retry-interval 40
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 ca-certificate CACERT uri scp://user@pass:1.2.3.4:/opt/certs/cert.p12
cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 state enabled 
cumulus@switch:~$ nv config apply
```

## Show gNMI Configuration and Status Information

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
ca-certificate  CACERT       CACERT   CACERT          
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

## RPC Methods

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

## Encoding Types

Cumulus Linux supports the Protobuf and JSON data formats.

## Wildcare Support

Cumulus Linux supports wildcard matching of keys. For example:

```
qos/interfaces/interface[interface-id=*]/output/queues/queue[name=*]/state/transmit-octets
```

You can use a combination of wildcard and specific keys; for example, to collect a metric for all queues on a specific interface.

```
/qos/interfaces/interface[interface-id=<name>]/output/queues/queue[*]/state/transmit-octets.
```

Regex for specific keys (such as `“interface-id=swp*”`) is not supported.

## Metrics

Cumulus Linux supports the following metrics:

{{< tabs "TabID200 ">}}
{{< tab "Interface ">}}

|  Name | Description |
|------ | ----------- |
| `/qos/interfaces/interface[interface-id=<name>]/output/queues/queue[name=<0-15>]/state/transmit-octets` | |
| `/qos/interfaces/interface[interface-id=<name>]/output/queues/queue[name=<0-15>]/state/transmit-pkts` | |
| `/qos/interfaces/interface[interface-id=<name>]/output/queues/queue[name=<0-15>]/state/ecn-marked-pkts` | |
| `/interfaces/interface[name=<name>]/state/admin-status`| |
| `/interfaces/interface[name=<name>]/state/counters/in-broadcast-pkts` | |
| `/interfaces/interface[name=<name>]/state/counters/in-multicast-pkts` | |
| `/interfaces/interface[name=<name>]/state/counters/in-octets` | |
| `/interfaces/interface [name=<name>]/ethernet/state/port-speed` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-mac-pause-frames` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-oversize-frames` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-fcs-errors` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-64-octets` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-65-127-octets` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-128-255-octets` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-256-511-octets` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-512-1023-octets` | |
| `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-1024-1518-octets` | |
| `/interfaces/interface[name=<name>]/rates/state/out-bits-rate` | |
| `/interfaces/interface[name=<name>]/rates/state/in-bits-rate` | |
| `/interfaces/interface[name=<name>]/rates/state/in-pkts-rate` | |
| `/interfaces/interface[name=<name>]/rates/state/out-pkts-rate` | |
| `/interfaces/interface[name=<name>]/state/mtu` | |
| `/interfaces/interface[name=<name>]/state/ifindex` | |
| `/interfaces/interface[name=<name>]/state/oper-status` | |
| `/interfaces/interface[name=<name>]/state/counters/in-errors` | |
| `/interfaces/interface[name=<name>]/state/counters/in-discards` | |
| `/interfaces/interface[name=<name>]/state/counters/out-octets` | |
| `/interfaces/interface[name=<name>]/state/counters/out-unicast-pkts` | |
| `/interfaces/interface[name=<name>]/state/counters/out-broadcast-pkts` | |
| `/interfaces/interface[name=<name>]/state/counters/out-discards` | |
| `/interfaces/interface[name=<name>]/state/counters/out-errors` | |
| `/qos/interfaces/interface[interface-id=<name>]/state/switch-priority[priority=<priority>]/counters/in-pause-pkts` | |
| `/qos/interfaces/interface[interface-id=<name>]/state/switch-priority[priority=<priority>]/counters/out-pause-pkts` | |
| `/interfaces/interface[name=<name>]/state/counters/out-multicast-pkts` | |
| `/interfaces/interface[name=<name>]/state/counters/in-unicast-pkts` | |
| `/interfaces/interface[name=<name>]/state/counters/carrier-transitions` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/rs-fec-uncorrectable-blocks` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/rs-fec-single-error-blocks` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/rs-fec-no-error-blocks` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/fc-fec-corrected-blocks` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/fc-fec-uncorrected-blocks` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/rs-fec-corrected-symbols` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/corrected-bits` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/effective-errors` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/effective-ber` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/raw-errors` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/received-bits` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/symbol-errors` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/symbol-ber` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/raw-ber` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/fec-time-since-last-clear` | |
| `/interfaces/interface[name=<name>]/ethernet/phy/state/ber-time-since-last-clear` | |

{{< /tab >}}
{{< tab "Router">}}

|  Name | Description |
|------ | ----------- |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor/state` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/session-state` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/established-transitions` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/messages/sent/UPDATE` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/messages/received/UPDATE` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/queues/input` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/state/queues/output` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/afi-safis/afi-safi[afi-safi-name=<afi-safi-name>]/state/prefixes/received` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/afi-safis/afi-safi[afi-safi-name=<afi-safi-name>]/state/prefixes/sent` | |
| `/network-instances/network-instance[name=<vrf>]/protocols/protocol[identifier=BGP][name=BGP]/bgp/neighbors/neighbor[neighbor-address=<address>]/afi-safis/afi-safi[afi-safi-name=<afi-safi-name>]/state/prefixes/installed` | |

{{< /tab >}}
{{< tab "LLDP">}}

|  Name | Description |
|------ | ----------- |
| `/lldp/state/chassis-id` | |
| `/lldp/state/system-description` | |
| `/lldp/state/system-name` | |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/age` | |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/management-address` | |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/management-address-type` | |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/port-description` | |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/port-id-type | |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/state/ttl` | |
| `/lldp/interfaces/interface[name=<name>]/neighbors/neighbor[id=<id>]/capabilities/capability[name=<capability>]/state/enabled` | |

{{< /tab >}}
{{< /tabs >}}

## User Credentials and Authentication

User authentication is enabled by default. gNMI subscription requests must include an HTTP Basic Authentication header according to RFC7617 containing the username and password of a user with NVUE API access permissions. You can enable this setting in the standard gNMI client (gNMIc) by setting the `auth-scheme` parameter to basic. Refer to {{<exlink url="https://gnmic.openconfig.net/global_flags/ - auth-scheme" text="https://gnmic.openconfig.net/global_flags/ - auth-scheme">}}.

{{%notice note%}}
Cumulus Linux ignores credentials in RPC metadata.
{{%/notice%}}

## gNMI Client Requests

You can use your gNMI client on a host to request capabilities and data to which the Agent subscribes. The examples below use the gNMIc client.

### Dial-in Mode Example

The following example shows a Dial-in Mode Subscribe request with TLS:

```
gnmic subscribe --mode stream --path "/qos/interfaces/interface[interface-id=swp1]/output/queues/queue[name=1]/state/transmit-octets" -i 10s --tls-cert gnmi_client.crt --tls-key gnmi_client.key -u cumulus -p ******* --auth-scheme Basic --skip-verify -a 10.188.52.108:9339
```

The following example shows a Dial-in Mode Subscribe request without TLS:

{{%notice note%}}
NVIDIA recommends using TLS. To test without TLS, you must also edit the NGINX configuration file on the switch.
{{%/notice%}}

```
gnmic subscribe --mode stream --path "/qos/interfaces/interface[interface-id=swp1]/output/queues/queue[name=1]/state/transmit-octets" -i 10s --insecure -u cumulus -p ******* --auth-scheme Basic -a 10.188.52.108:9339
```

### Subscription Example

The following example shows a subscription response:

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

### Capabilities Example

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

## Considerations

- The minimum sampling interval is 5 seconds. If you configure a shorter sampling interval, the switch might not behave as expected.
- NVIDIA has tested exporting a few hundred metrics at a time and recommends only using a similar scale. If you exceed this scale, the switch might not behave as expected. Do not subscribe to the root level (/) to avoid requesting multiple thousands of metrics at a time.
- ModelData, Origin, and Extensions fields are ignored in requests and not set in responses.
- For all X.509 certificates generated externally, make sure to set the correct X.509v3 fields:
  - Set the Purpose field correctly (TLS WWW Server Authentication versus TLS WWW Client Authentication) in the extended key usage (EKU) field.  
  - Set TLS WWW Server Authentication for TLS server applications to gNMI server (on the switch), and gRPC dial-out tunnel server (running in your network)
  - Set TLS WWW Client Authentication for TLS client applications to gRPC dial-out tunnel client (on the switch) and gNMI client (running in the network)
  - Set the Cumulus Linux switch management IP address included in the subject alternate name (SAN) field together with the localhost SAN DNS value applicable to the gNMI server certificate.
  - On the gNMI client and the dial-out tunnel server (within the network), ensure the management IP address is included in the subject alternate name (SAN) field together with localhost SAN DNS value.
- NVUE does not support mTLS configuration. NVIDIA recommends that you do not try to set mTLS related fields under gRPC tunnel configuration.
