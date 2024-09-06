---
title: Monitoring System Statistics and Network Traffic with sFlow
author: NVIDIA
weight: 1140
toc: 4
---
{{<exlink url="http://www.sflow.org/index.php" text="sFlow">}} is a monitoring protocol that samples network packets, application operations, and system counters. sFlow collects both interface counters and sampled 5-tuple packet information so that you can monitor your network traffic as well as your switch state and performance metrics. To collect and analyze this data, you need an outside server; an *sFlow collector*.

{{%notice note%}}
If you intend to run this service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF#run-services-within-the-management-vrf" text="these steps">}} to configure the service.
{{%/notice%}}

## Enable sFlow

{{< tabs "TabID15 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system sflow state enabled 
cumulus@switch:~$ nv config apply
```

To disable sFlow, run the `nv set system sflow state disabled` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

By default, the `hsflowd` service is disabled and does *not* start automatically when the switch boots up.

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

## Configure sFlow

To configure sFlow:
- Provide the sFlow collectors. You must configure at least one collector if you enable sFlow.
- Set the sFlow sampling rate.
- Set the polling interval.
- Provide the IP address and interface of the sFlow agent.

Cumulus Linux provides different sampling rate configurations. The value represents the sampling ratio; for example, if you specify a value of 400, SFlow samples one in every 400 packets.

| Sampling Rate | Default Value | Description | 
| ------------- | ------------- | ----------- |
| `default` | 400 | The Default sampling rate for ports with no speed or application with no sampling setting. |
| `speed-100m` | 100 | The sampling rate on a 100Mbps port. |
| `speed-1g` | 1000 | The sampling rate on a 1Gbps port. |
| `speed-10g` | 10000 | The sampling rate on a 10Gbps port. |
| `speed-40g` | 40000 | The sampling rate on a 40Gbps port. |
| speed-50g | 50000 | The sampling rate on a 50Gbps port. |
| speed-100g | 100000 | The sampling rate on a 100Gbps port. |
| speed-200g | 200000 | The sampling rate on a 200Gbps port. |
| speed-400g | 400000 | The sampling rate on a 400Gbps port. |
| speed-800g | 800000 | The sampling rate on a 800Gbps port. |

{{%notice note%}}
Some collectors require each source to transmit on a different port, others listen on only one port. Refer to the documentation for your collector for more information.
{{%/notice%}}

### Configure Designated Collectors

{{< tabs "TabID28 ">}}
{{< tab "NVUE Commands ">}}

Specify the IP address, UDP port number, and interface for the designated collectors. The port number and interface are optional; If you do not specify a port number, Cumulus Linux uses the default port 6343.

The following example configures sFlow to send data to collector 192.0.2.100 on port 6343 and collector 192.0.2.200 on eth0:

```
cumulus@switch:~$ nv set system sflow collector 192.0.2.100 port 6344
cumulus@switch:~$ nv set system sflow collector 192.0.2.200 interface eth0
cumulus@switch:~$ nv config apply
```

Configure the sflow sampling rate in number of packets if you do not want to use the default rate, and the polling interval in seconds.

The following example polls the counters every 20 seconds and samples one in every 40000 packets for 40G interfaces:

```
cumulus@switch:~$ nv set system sflow sampling-rate speed-40g default 40000
cumulus@switch:~$ nv set system sflow poll-interval 20
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/hsflowd.conf` file to set up the collectors, sampling rates, and polling interval in seconds, then restart the `hsflowd` service with the `sudo systemctl start hsflowd` c                                             ommand.

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

{{< tabs "TabID138 ">}}
{{< tab "NVUE Commands ">}}

The following example configures the sFlow agent prefix to 10.0.0.0/8:

```
cumulus@switch:~$ nv set system sflow agent ip 10.0.0.0/8 
```

The following example configures the sFlow agent interface to eth0:

``` 
cumulus@switch:~$ nv set system sflow agent interface eth0
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To configure the IP address for the sFlow agent, configure one of the following in the `/etc/hsflowd.conf` file (following the recommendations in the {{<exlink url="https://sflow.net/host-sflow-linux-config.php" text="sFlow documentation">}}):

- The agent CIDR. For example, `agent.cidr = 10.0.0.0/8`. The IP address must fall within this range.
- The agent interface. For example, if the agent is using eth0, select the IP address for this interface.

To check the agent IP, run the `grep agentIP /etc/hsflowd.auto` command.

{{< /tab >}}
{{< /tabs >}}

## Configure sFlow to Collect Dropped Packets

You can configure sFlow to monitor dropped packets in software or hardware.

{{< tabs "TabID171 ">}}
{{< tab "NVUE Commands ">}}

The following example configures sFlow to monitor dropped packets in software:
```
cumulus@switch:~$ nv set system sflow dropmon sw 
cumulus@switch:~$ nv config apply
```

The following example configures sFlow to monitor dropped packets in hardware:
```
cumulus@switch:~$ nv set system sflow dropmon hw 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/hsflowd.conf` file to add the `dropmon { group=1 start=on sw=off hw=on }` line to monitor dropped packets in hardware or the `dropmon { group=1 start=on sw=on hw=off }` line to monitor dropped packets in software:

```
cumulus@switch:~$ sudo nano /etc/hsflowd.conf
dropmon { group=1 start=on sw=off hw=on }
```

Restart the `hsflowd` service with the `sudo systemctl start hsflowd` command.
  
{{< /tab >}}
{{< /tabs >}}

## Configure sFlow Visualization Tools

For information on configuring various sFlow visualization tools, read this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Monitoring/Configure-and-Use-sFlow-Visualization-Tools" >}}).

## Considerations

Cumulus Linux does not support sFlow egress sampling.

## Related Information

- {{<exlink url="http://www.sflow.org/products/collectors.php" text="sFlow Collectors">}}
- {{<exlink url="http://en.wikipedia.org/wiki/SFlow" text="sFlow Wikipedia page">}}
