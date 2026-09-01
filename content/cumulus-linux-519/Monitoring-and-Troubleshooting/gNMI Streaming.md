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

The following example sets the gNMI server listening address to 10.10.10.1 and the port to 1024, and enables the gNMI server:

```
cumulus@switch:~$ nv set system gnmi-server listening-address 10.10.10.1
cumulus@switch:~$ nv set system gnmi-server port 1024
cumulus@switch:~$ nv set system gnmi-server state enabled
cumulus@switch:~$ nv config apply
```

The following example imports and sets the CA certificate `CERT1` and the CRL `crl.crt` for mTLS:

```
cumulus@switch:~$ nv action import system security ca-certificate CERT1 uri scp://user@pass:1.2.3.4:/opt/certs/cert.p12
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
cumulus@switch:~$ nv action import system security ca-certificate CACERT1 uri scp://user@pass:1.2.3.4:/opt/certs/ca-cert.pem
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

Cumulus Linux provides a list of supported gNMI metrics {{<exlink url="https://github.com/NVIDIA/networking-yang" text="here" >}}. To see a list of the new metrics for Cumulus Linux 5.19, refer to {{<link url="New-and-Updated-Telemetry-Metrics" text="New and Updated Telemetry Metrics">}}.

### User Credentials and Authentication

User authentication is enabled by default. gNMI subscription requests must include the user authentication credentials with NVUE API access permissions, either in an HTTP basic authentication header according to RFC7617 or a gRPC metadata header.

### gNMI Client Requests

You can use your gNMI client on a host to request capabilities and data to which the gNMI agent subscribes.

{{%notice note%}}
- Cumulus Linux processes gNMI client subscription create and delete requests sequentially (one at a time). The switch rejects concurrent subscription requests with a `CANCELLED: System is busy`​ gRPC status and the gNMI client must reinitiate the request with the appropriate backoff. This limitation applies only to subscription setup or teardown. After the subscription establishes, multiple subscriptions run concurrently and stream telemetry data independently.
- For better performance, NVIDIA recommends that you enable gzip in your gNMI client tools. For example, for `gnmic`, add `--gzip` to the command line arguments.
{{%/notice%}}

#### Dial-in Mode Examples

The following example shows a basic dial-in mode subscribe request in an HTTP basic authentication header:

```
gnmic subscribe gnmic --gzip --mode stream -i 10s --tls-cert gnmi_client.crt --tls-key gnmi_client.key -u cumulus -p ******* --auth-scheme Basic -a 192.168.200.3:9339 --prefix "system/cpus/cpu[index=0]" --path "state"
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

The following example uses the `install` RPC to copy the `/media/node/cumulus-linux-mlx-amd64-5.19.bin.devsigned` image file on the local client to the switch with the version `5.18.0`:

```
cumulus@host:mgmt:~$ gnoic  --username test1 --password test1 --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key os install --pkg /media/node/cumulus-linux-mlx-amd64-5.19.bin.devsigned --version 5.18.0
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

The following example uses the `activate` RPC to activate the `5.19.0` image as the next boot image without reboot the switch:

```
cumulus@host:mgmt:~$ gnoic  --username test1 --password test1 --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key os activate --version 5.19.0 --no-reboot
INFO[0190] target "10.1.1.100:9339" activate response "activate_ok:{}"
cumulus@host:mgmt:~$
```

The following example uses the `activate` RPC to activate the `5.19.0` image as the next boot image and reboots the switch.

```
cumulus@host:mgmt:~$ gnoic  --username cumulus --password NvidiaR0cks! --address 10.1.1.100 --port 9339 --tls-ca /home/cumulus/dut_ca.crt --tls-cert /home/cumulus/gnmic_client.crt --tls-key /home/cumulus/gnmic_client.key os activate --version 5.19.0 
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

<!-- REVIEW: the openconfig-platform row in the table below gains Type and a sentence naming the
     component types. The specification states no quality level and is a Confluence-style page with
     no Scope, Known Limitations, or Open Issues sections, so there is nothing to check the claim
     against except a candidate build. Its component table also has a "Deprecation Details" column
     whose contents did not survive text extraction; confirm nothing is deprecated before
     publishing. Delete this comment before publishing. -->

Cumulus Linux supports the following OpenConfig models:
<!-- vale off -->
| Model| Supported Data |
| --------- | ------ |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-interfaces.yang" text="openconfig-interfaces">}} | Name, Operstatus, AdminStatus, IfIndex, MTU, LoopbackMode, Enabled, Counters (InPkts, OutPkts, InOctets, InUnicastPkts, InDiscards, InMulticastPkts, InBroadcastPkts, InErrors, OutOctets, OutUnicastPkts, OutMulticastPkts, OutBroadcastPkts, OutDiscards, OutErrors) |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-if-ethernet.yang" text="openconfig-if-ethernet">}} | AutoNegotiate, PortSpeed, MacAddress, NegotiatedPortSpeed, Counters (InJabberFrames, InOversizeFrames,​ InUndersizeFrames)|
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/interfaces/openconfig-if-ethernet-ext.yang" text="openconfig-if-ethernet-ext">}} | Frame size counters (InFrames_64Octets, InFrames_65_127Octets, InFrames_128_255Octets, InFrames_256_511Octets, InFrames_512_1023Octets, InFrames_1024_1518Octets) |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/system/openconfig-system.yang" text="openconfig-system">}} | Memory, CPU |
| {{<exlink url="https://github.com/openconfig/public/blob/master/release/models/platform/openconfig-platform.yang" text="openconfig-platform">}} | Platform data (Name, Description, Type, Version). Cumulus Linux reports the component type for the ASIC (`INTEGRATED_CIRCUIT`), transceivers (`TRANSCEIVER`), fans (`FAN`), storage disks (`STORAGE`), and temperature and leakage sensors (`SENSOR`). Because temperature sensors and leakage sensors share the `SENSOR` type, use the component name to tell them apart. |
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
