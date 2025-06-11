---
title: Monitoring System Statistics and Network Traffic with sFlow
author: NVIDIA
weight: 1140
toc: 4
---
sFlow is a monitoring protocol that samples network packets, application operations, and system counters. sFlow collects both interface counters and sampled 5-tuple packet information so that you can monitor your network traffic as well as your switch state and performance metrics. To collect and analyze this data, you need an outside server; an *sFlow collector*.

{{%notice note%}}
If you intend to run this service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF#run-services-within-the-management-vrf" text="these steps">}} to configure the service.
{{%/notice%}}

## Configure sFlow

To configure sFlow:
- Provide the sFlow collectors. You must configure at least one collector if you enable sFlow.
- Set the sFlow sampling rate.
- Set the polling interval.
- Provide the IP address and interface of the sFlow agent.
- Configure the sFlow policer rate and policer burst.
- Enable sFlow

Cumulus Linux provides different sampling rate configurations. The value represents the sampling ratio; for example, if you specify a value of 400, SFlow samples one in every 400 packets.

| Sampling Rate | Default Value | Description |
| ------------- | ------------- | ----------- |
| `speed-100m` | 100 | The sampling rate on a 100Mbps port. |
| `speed-1g` | 1000 | The sampling rate on a 1Gbps port. |
| `speed-10g` | 10000 | The sampling rate on a 10Gbps port. |
| `speed-40g` | 40000 | The sampling rate on a 40Gbps port. |
| `speed-50g` | 50000 | The sampling rate on a 50Gbps port. |
| `speed-100g` | 100000 | The sampling rate on a 100Gbps port. |
| `speed-200g` | 200000 | The sampling rate on a 200Gbps port. |
| `speed-400g` | 400000 | The sampling rate on a 400Gbps port. |
| `speed-800g` | 800000 | The sampling rate on a 800Gbps port. |

{{%notice note%}}
Some collectors require each source to transmit on a different port, others listen on only one port. Refer to the documentation for your collector for more information.
{{%/notice%}}

### Configure Designated Collectors

{{< tabs "TabID79 ">}}
{{< tab "NVUE Commands ">}}

Specify the IP address, UDP port number, and interface for the designated collectors. The port number and interface are optional; If you do not specify a port number, Cumulus Linux uses the default port 6343.

The following example configures sFlow to send data to collector 192.0.2.100 on port 6343 and collector 192.0.2.200 on eth0:

```
cumulus@switch:~$ nv set system sflow collector 192.0.2.100 port 6344
cumulus@switch:~$ nv set system sflow collector 192.0.2.200 interface eth0
cumulus@switch:~$ nv config apply
```

Configure the sFlow sampling rate in number of packets if you do not want to use the default rate, and the polling interval in seconds.

The following example polls the counters every 20 seconds and samples one in every 40000 packets for 40G interfaces:

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-40g 40000
cumulus@switch:~$ nv set system sflow poll-interval 20
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/hsflowd.conf` file to set up the collectors, sampling rates, and polling interval in seconds, then restart the `hsflowd` service with the `sudo systemctl start hsflowd` command.

The following example polls the counters every 20 seconds, samples 1 of every 40000 packets for 40G interfaces, and sends this information to a collector at 192.0.2.100 on port 6343 and to another collector at 192.0.2.200 on interface eth0.

```
cumulus@switch:~$ sudo nano /etc/hsflowd.conf
sflow {
# ====== Sampling/Polling/Collectors ======
  # EITHER: automatic (DNS SRV+TXT from _sflow._udp):
  #   DNS-SD { }
  # OR: manual:
  #   Counter Polling:
        polling = 20
  #   default sampling N:
  #     sampling = 400
  #   sampling N on interfaces with ifSpeed:
        sampling.100M = 100
        sampling.1G = 1000
        sampling.10G = 10000
        sampling.40G = 40000
  #   sampling N for apache, nginx:
  #     sampling.http = 50
  #     sampling N for application (requires json):
  #     sampling.app.myapp = 100
  #   collectors:
  collector { ip=192.0.2.100 udpport=6344 }
  collector { ip=192.0.2.200 interface=eth0 }
}
```

```
cumulus@switch:~$ sudo systemctl start hsflowd
```

{{< /tab >}}
{{< /tabs >}}

### Configure the SFlow Agent

Provide the IP address or prefix, or the interface for the sFlow agent.

{{< tabs "TabID146 ">}}
{{< tab "NVUE Commands ">}}

The following example configures the sFlow agent prefix to 10.0.0.0/8:

```
cumulus@switch:~$ nv set system sflow agent ip 10.0.0.0/8
cumulus@switch:~$ nv config apply
```

The following example configures the sFlow agent interface to eth0:

``` 
cumulus@switch:~$ nv set system sflow agent interface eth0
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To provide the IP address or prefix for the sFlow agent, edit the `/etc/hsflowd.conf` file to set the `agent.CIDR` parameter, then restart the `hsflowd` service with the `sudo systemctl start hsflowd` command.

```
cumulus@switch:~$ sudo nano /etc/hsflowd.conf
...
sflow { 
  agent.CIDR = 10.0.0.0/8 
} 
```

```
cumulus@switch:~$ sudo systemctl start hsflowd
```

To provide an interface for the sFlow agent, edit the `/etc/hsflowd.conf` file to set the `agent` parameter, then restart the `hsflowd` service with the `sudo systemctl start hsflowd` command.:

```
cumulus@switch:~$ sudo nano /etc/hsflowd.conf
...
sflow { 
  agent = eth0 
} 
```

```
cumulus@switch:~$ sudo systemctl start hsflowd
```

{{< /tab >}}
{{< /tabs >}}

### Configure sFlow Policer Rate and Burst Size

You can limit the number of sFlow samples per second and the sample burst size per second that the switch sends.

The default number of sFlow samples and default sample size is 16384. You can specify a value between 0 and 16384.

The following example sets the number of sFlow samples to 800 and the sample size to 900:

{{< tabs "TabID183 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system sflow policer rate 8000
cumulus@switch:~$ nv set system sflow policer burst 9000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/datapath/traffic.conf` file to change the `sflow.rate` and `sflow.burst` parameters, then reload `switchd` with the `sudo systemctl reload switchd.service` command.

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
# Set sflow/sample ingress cpu packet rate and burst in packets/sec 
# Values: {0..16384} 
sflow.rate = 8000
sflow.burst = 9000 
```

```
cumulus@switch:~$ sudo systemctl reload switchd.service 
```

{{< /tab >}}
{{< /tabs >}}

## Enable sFlow

{{< tabs "TabID15 ">}}
{{< tab "NVUE Commands ">}}

To enable sFlow:

```
cumulus@switch:~$ nv set system sflow state enabled 
cumulus@switch:~$ nv config apply
```

To disable sFlow, run the `nv set system sflow state disabled` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

By default, the `hsflowd` service is `off` and does *not* start automatically when the switch boots up.

To enable and start the `hsflowd` service:

```
cumulus@switch:~$ sudo systemctl enable hsflowd
cumulus@switch:~$ sudo systemctl start hsflowd
```

To disable the `hsflowd` service:

```
cumulus@switch:~$ sudo systemctl stop hsflowd
cumulus@switch:~$ sudo systemctl disable hsflowd
```

{{< /tab >}}
{{< /tabs >}}

## Interface Configuration

By default, sFlow is `off` on interfaces that are operationally UP. To disable sFlow on an interface:

{{< tabs "TabID216 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 sflow state disabled 
cumulus@switch:~$ nv config apply
```

To enable sFlow on an interface, run the `nv set interface <interface> sflow state enabled` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

By default, sFlow is `off` on interfaces that are operationally UP. To disable sFlow on a specific interface, edit the `/etc/cumulus/switchd.conf` file and set the `interface.<interface>.sflow.enable` parameter to `FALSE`:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
interface.swp1.sflow.enable = FALSE 
```

To enable sFlow on an interface, set the `interface.<interface>.sflow.enable` parameter to `TRUE`.

{{< /tab >}}
{{< /tabs >}}

To configure the sFlow sample rate on an interface.

{{< tabs "TabID243 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp1 sflow sample-rate 100000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.conf` file and set the `interface.<interface-id>.sflow.sample_rate.ingress` parameter:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
interface.swp1.sflow.sample_rate.ingress = 100000 
```

{{< /tab >}}
{{< /tabs >}}

## Monitor Dropped Packets

You can configure sFlow to monitor dropped packets in hardware.

{{< tabs "TabID268 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system sflow dropmon hw 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/hsflowd.conf` file to change `start` to `on` in the `dropmon { group=1 start=off limit=1000 }` line.

```
cumulus@switch:~$ sudo nano /etc/hsflowd.conf
dropmon { group=1 start=on limit=1000 }
```

Restart the `hsflowd` service with the `sudo systemctl start hsflowd` command.
  
{{< /tab >}}
{{< /tabs >}}

## Configure sFlow Visualization Tools

For information on configuring various sFlow visualization tools, read this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Monitoring/Configure-and-Use-sFlow-Visualization-Tools" >}}).

## Show sFlow Configuration

To show all sFlow configuration on the switch:

```
cumulus@switch:~$ nv show system sflow
                operational  applied    
-------------  -----------  -----------
poll-interval               20         
state                       enabled    
[collector]                 192.0.2.100
[collector]                 192.0.2.200
sampling-rate                          
  default                   400        
  speed-100m                100        
  speed-1g                  1000       
  speed-10g                 10000      
  speed-25g                 25000      
  speed-40g                 40000      
  speed-50g                 50000      
  speed-100g                100000     
  speed-200g                200000     
  speed-400g                400000     
  speed-800g                800000     
agent                                  
  ip                        10.0.0.0/8 
  interface                 eth0       
policer                                
  rate                      8000       
  burst                     9000       
[dropmon]                   sw
```

To show sFlow collector configuration:

```
cumulus@switch:~$ nv show system sflow collector
Ip                    Port 
--------------------------------- 
192.0.2.100           6343 
192.0.2.200           6344
```

To show the sFlow sampling rate configuration:

```
cumulus@switch:~$ nv show system sflow sampling-rate
            applied
----------  -------
default     400    
speed-100m  100    
speed-1g    1000   
speed-10g   10000  
speed-25g   25000  
speed-40g   40000  
speed-50g   50000  
speed-100g  100000 
speed-200g  200000 
speed-400g  400000 
speed-800g  800000 
```

To show sFlow agent configuration:

```
cumulus@switch:~$ nv show system sflow agent
           operational  applied   
---------  -----------  ----------
ip                      10.0.0.0/8
interface               eth0
```

To show the number of samples per second and the sample burst size per second that the switch sends out:

```
cumulus@switch:~$ nv show system sflow policer
---------------------- 
       applied
-----  -------
rate   8000   
burst  9000
```

To show sFlow configuration on a specific interface:

```
cumulus@switch:~$ nv show interface swp1 sflow
---------------------- 
             operational  applied
-----------  -----------  -------
sample-rate  0            100000 
state        disabled     enabled
```

## Considerations

Cumulus Linux does not support sFlow egress sampling.

## Related Information

- {{<exlink url="https://sflow.net/host-sflow-linux-config.php" text="sFlow documentation">}}):
- {{<exlink url="http://www.sflow.org/products/collectors.php" text="sFlow Collectors">}}
- {{<exlink url="http://en.wikipedia.org/wiki/SFlow" text="sFlow Wikipedia page">}}
