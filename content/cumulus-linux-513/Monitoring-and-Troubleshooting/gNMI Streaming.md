---
title: gNMI Streaming
author: NVIDIA
weight: 1234
toc: 4
---
You can use {{<exlink url="https://github.com/openconfig/gnmi" text="gRPC Network Management Interface">}} (gNMI) to collect system resource, interface, and counter information from Cumulus Linux and export it to your own gNMI client.

When you use gNMI, the switch connects to the collector as a gRPC server (gNMI server). The collector is the gRPC client. The session between the client and server MUST be encrypted using TLS and use X.509 certificate authentication.

{{%notice note%}}
When you enable gNMI, do not use {{<link url="Open-Telemetry-Export" text="Open Telemetry">}}.
{{%/notice%}}

## Configure gNMI

To configure gNMI in Cumulus Linux, you need to:
- Enable the gNMI server
- Configure the gRPC tunnel client

Before configuring gNMI on the switch, make sure the gRPC environment is installed on the gRPC client.

### Enable the gNMI Server

1. Optional. Import the CA certificate for mTLS and enable the certificate for the server.

   ```
   cumulus@switch:~$ nv set system gnmi-server mtls ca-certificate CACERT
   cumulus@switch:~$ nv config apply
   ```

2. Provide the listening address for the gNMI server and enable the gNMI server:

   ```
   cumulus@switch:~$ nv set system gnmi-server listening-address 10.1.1.100 
   cumulus@switch:~$ nv set system gnmi-server state enabled 
   cumulus@switch:~$ nv config apply
   ```

   Cumulus Linux uses a self-signed certificate. However, you can generate your own TLS server certificates and bind them with the gNMI server application.

3. Check the status of the gNMI agent and UMF components and view the most recent logs. The services show as active when the components are installed successfully.

   ```
   cumulus@switch:~$ sudo systemctl status nv-umf-gnmid.service
   cumulus@switch:~$ sudo systemctl status nv-umf-contractd.service
   cumulus@switch:~$ sudo systemctl status nv-umf-proxyd.service
   cumulus@switch:~$ sudo systemctl status nginx
   ```

### Configure the gRPC Tunnel Client

The gRPC tunnel client package includes the dial-out tunnel client. To configure the gRPC tunnel client package:

1. Import CA certificates:

   ```
   cumulus@switch:~$ nv action import system security ca-certificate CERT1 uri scp://user@pass:1.2.3.4:/opt/certs/cert.p12
   cumulus@switch:~$ nv config apply
   ```

   {{%notice note%}}
Cumulus Linux does not support mTLS on the underlying gRPC tunnel.
{{%/notice%}}

2. Enable localhost as a listening address for the gNMI server:

   ```
   cumulus@switch:~$ nv set system gnmi-server listening-address localhost 
   cumulus@switch:~$ nv config apply
   ```

3. Configure each tunnel server to which you want to connect. You must specify the listening address, port, target name, and the certificate for each tunnel server. You can also reconfigure the retry interval (optional). The default retry interval is 30 seconds.

   ```
   cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 address 10.1.1.10 
   cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 port 443 
   cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 target-name TARGET1 
   cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 ca-certificate CERT1
   cumulus@switch:~$ nv set system grpc-tunnel server SERVER1 retry-interval 40
   cumulus@switch:~$ nv set system grpc-tunnel server state enabled 
   cumulus@switch:~$ nv config apply
   ```

4. Import the server certificate on the switch and bind the certificate to the gNMI server.

   ```
   cumulus@switch:~$ nv action import system security certificate CERT1
   cumulus@switch:~$ nv set system gnmi-server certificate CERT1 
   cumulus@switch:~$ nv config apply
   ```

{{%notice note%}}
- Make sure to set the TLS WWW Server Authentication X.509v3 extended key usage (EKU) capability in the certificate (Section 4.2.1.12 - RFC 5280). Failure to set this capability prevents the certificate from being used by the gNMI server.
- Based on the gNMI client you use, the gNMI server certificate might require the management IP address of the Cumulus Linux switch to be included in the subject alternate name (`SAN`) field of the server certificate.
{{%/notice%}}

### Sample TLS Certificates for the gNMI Client

This section describes a very basic TLS certificate configuration for a gNMI client and tunnel server that you can use for initial testing.

The following TLS certificate configuration is only an example; you can use your own PKI infrastructure to generate and manage certificates.

1. Create a certificate request:

   ```
   cumulus@switch:~$ openssl genrsa 2048 > ca-key.pem 
   cumulus@switch:~$ openssl req -new -x509 -nodes -days 365000 \ 
        -key ca-key.pem \ 
        -out ca-cert.pem
   ```

2. Create a text file with the following contents:

   ```
   cumulus@switch:~$ sudo nano file.txt
   subjectAltName = @alt_names 
   extendedKeyUsage = clientAuth
   
   [alt_names] 
   IP = 127.0.0.1 <--- change to the IP address of the host running the gNMI client. 
   ```

3. Create the certificates:

   ```
   cumulus@switch:~$ openssl req -newkey rsa:2048 -nodes -days 365000 -keyout client-key.pem -out client-req.pem 
   cumulus@switch:~$ openssl x509 -req -days 365000 -set_serial 01 -in client-req.pem -out client-cert.pem -CA ca-cert.pem -CAkey ca-key.pem -extfile file.txt 
   ```

{{%notice note%}}
- The steps above describe how to generate an entity or leaf certificate for the gNMI client.
- When operating in dial-out mode, the tunnel server (running in the network) also needs a TLS server certificate.
- The dial-out tunnel client running on Cumulus Linux connects to the tunnel server and performs a TLS handshake.
- The tunnel client performs the standard one-way TLS and verifies the authenticity of the tunnel server certificate (root-of-trust PKI chain verification).
- Follow similar steps as described above and generate a TLS server certificate to use with the tunnel server.
- Include encoding the TLS WWW Server Authentication X.509v3 extended key usage (EKU) capability set (for example, `extendedKeyUsage = serverAuth`).
{{%/notice%}}

### TLS Certificates

For authentication on the gNMI gRPC with TLS:
- The gNMI server is configured with a public and private key in PEM format. 
- The gNMI client is configured with a public and private key in PEM format, and a username and password to authenticate the user.

For mTLS, the gNMI server also validates the client certificates. The gNMI server needs the root or intermediary CA certificate used to sign the gNMI client certificate.

For dial-out mode, the gRPC tunnel is also encrypted using TLS. For single-sided TLS:
- The tunnel server is configured with a public and private key in PEM format. 
- The tunnel client validates the tunnel server certificates. The tunnel client requires the root or intermediary CA certificate used to sign the tunnel server certificate.

To configure authentication:

1. Create public and private keys in PEM format for the device on which the gNMI client runs. You need these keys when running the gNMI collector; See how to use `gnmi_client.crt` and `gnmi_client.key` in {{<link url="#examples-with-gnmic" text="Examples with gNMIc">}}.
2. If mTLS on the gNMI RPC is required, import the certificate of the CA that signed the gNMI client keys (or the client certificate itself) to the switch and configure the gNMI server to use the certificate (`nv set system gnmi-server mtls ca-certificate <cert id>`).  
3. For dial-out mode, create public and private keys in PEM format for the tunnel server. You use these keys when running the tunnel server.
4. You must also import the certificate of the CA that signed the keys to the switch and configure the tunnel client to use it to connect to the server (`nv set system grpc-tunnel server <server name> ca-certificate <cert id>`).
5. Copy the certificate of the CA that signed the keys (or the client certificate itself) to the device running the tunnel server and use it in the tunnel server configuration.

## RPC Methods

Cumulus Linux supports the following <span class="a-tooltip">[RPC](## "Remote Procedure Call")</span> events:  
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
- `/qos/interfaces/interface[interface-id=<name>]/output/queues/queue[name=<0-15>]/state/transmit-octets`
- `/qos/interfaces/interface[interface-id=<name>]/output/queues/queue[name=<0-15>]/state/transmit-pkts`
- `/qos/interfaces/interface[interface-id=<name>]/output/queues/queue[name=<0-15>]/state/ecn-marked-pkts`
- `/interfaces/interface[name=<name>]/state/admin-status`
- `/interfaces/interface[name=<name>]/state/counters/in-broadcast-pkts`
- `/interfaces/interface[name=<name>]/state/counters/in-multicast-pkts`
- `/interfaces/interface[name=<name>]/state/counters/in-octets`
- `/interfaces/interface [name=<name>]/ethernet/state/port-speed`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-mac-pause-frames`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-oversize-frames`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-fcs-errors`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-64-octets`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-65-127-octets`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-128-255-octets`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-256-511-octets`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-512-1023-octets`
- `/interfaces/interface[name=<name>]/ethernet/state/counters/in-distribution/in-frames-1024-1518-octets`
- `/interfaces/interface[name=<name>]/rates/state/out-bits-rate`
- `/interfaces/interface[name=<name>]/rates/state/in-bits-rate`
- `/interfaces/interface[name=<name>]/rates/state/in-pkts-rate`
- `/interfaces/interface[name=<name>]/rates/state/out-pkts-rate`
- `/interfaces/interface[name=<name>]/state/mtu`
- `/interfaces/interface[name=<name>]/state/ifindex`
- `/interfaces/interface[name=<name>]/state/oper-status`
- `/interfaces/interface[name=<name>]/state/counters/in-errors`
- `/interfaces/interface[name=<name>]/state/counters/in-discards`
- `/interfaces/interface[name=<name>]/state/counters/out-octets`
- `/interfaces/interface[name=<name>]/state/counters/out-unicast-pkts`
- `/interfaces/interface[name=<name>]/state/counters/out-broadcast-pkts`
- `/interfaces/interface[name=<name>]/state/counters/out-discards`
- `/interfaces/interface[name=<name>]/state/counters/out-errors`
- `/qos/interfaces/interface[interface-id=<name>]/state/switch-priority[priority=<priority>]/counters/in-pause-pkts`
- `/qos/interfaces/interface[interface-id=<name>]/state/switch-priority[priority=<priority>]/counters/out-pause-pkts`
- `/interfaces/interface[name=<name>]/state/counters/out-multicast-pkts`
- `/interfaces/interface[name=<name>]/state/counters/in-unicast-pkts`
- `/interfaces/interface[name=<name>]/state/counters/carrier-transitions`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/rs-fec-uncorrectable-blocks`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/rs-fec-single-error-blocks`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/rs-fec-no-error-blocks`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/fc-fec-corrected-blocks`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/fc-fec-uncorrected-blocks`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/rs-fec-corrected-symbols`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/corrected-bits`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/effective-errors`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/effective-ber`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/raw-errors`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/received-bits`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/symbol-errors`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/symbol-ber`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/lane[lane=<lane>]/raw-ber`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/fec-time-since-last-clear`
- `/interfaces/interface[name=<name>]/ethernet/phy/state/ber-time-since-last-clear`

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

- The minimum sampling interval is 10 seconds. If you configure a shorter sampling interval, the switch might not behave as expected.
- NVIDIA has tested exporting a few hundred metrics at a time and recommends only using a similar scale. If you exceed this scale, the switch might not behave as expected. Do not subscribe to the root level (/) to avoid requesting multiple thousands of metrics at a time.
- ModelData, Origin, and Extensions fields are ignored in requests and not set in responses.
- For all X.509 certificates generated externally, make sure to set the correct X.509v3 fields:
  - Set the Purpose field correctly (TLS WWW Server Authentication versus TLS WWW Client Authentication) in the extended key usage (EKU) field.  
  - Set TLS WWW Server Authentication for TLS server applications to gNMI server (on the switch), and gRPC dial-out tunnel server (running in your network)
  - Set TLS WWW Client Authentication for TLS client applications to gRPC dial-out tunnel client (on the switch) and gNMI client (running in the network)
  - Set the Cumulus Linux switch management IP address included in the subject alternate name (SAN) field together with the localhost SAN DNS value applicable to the gNMI server certificate.
  - On the gNMI client and the dial-out tunnel server (within the network), ensure the management IP address is included in the subject alternate name (SAN) field together with localhost SAN DNS value.
- NVUE does not support mTLS configuration. NVIDIA recommends that you do not try to set mTLS related fields under gRPC tunnel configuration.
