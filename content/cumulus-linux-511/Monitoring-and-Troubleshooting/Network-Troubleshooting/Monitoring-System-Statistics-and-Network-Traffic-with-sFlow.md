---
title: Monitoring System Statistics and Network Traffic with sFlow
author: NVIDIA
weight: 1140
toc: 4
---
{{<exlink url="http://www.sflow.org/index.php" text="sFlow">}} is a monitoring protocol that samples network packets, application operations, and system counters. sFlow collects both interface counters and sampled 5-tuple packet information so that you can monitor your network traffic as well as your switch state and performance metrics. To collect and analyze this data, you need an outside server; an *sFlow collector*.

`hsflowd` is the daemon that samples and sends sFlow data to configured collectors. By default, Cumulus Linux disables `hsflowd` and it does *not* start automatically when the switch boots up.

{{%notice note%}}
If you intend to run this service within a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}, including the {{<link url="Management-VRF" text="management VRF">}}, follow {{<link url="Management-VRF#run-services-within-the-management-vrf" text="these steps">}} to configure the service.
{{%/notice%}}

## Configure sFlow

To configure `hsflowd` to send to the designated collectors, either:

- Use DNS service discovery (DNS-SD)
- Manually configure the `/etc/hsflowd.conf` file
<!-- vale off -->
### Configure sFlow with DNS-SD
<!-- vale on -->
You can configure your DNS zone to advertise the collectors and polling information to all interested clients. Add the following content to the zone file on your DNS server:

```
_sflow._udp SRV 0 0 6343 collector1
_sflow._udp SRV 0 0 6344 collector2
_sflow._udp TXT (
"txtvers=1"
"sampling.100M=100"
"sampling.1G=1000"
"sampling.10G=10000"
"sampling.40G=40000"
"sampling.100G=100000"
"polling=20"
)
```

The above snippet instructs `hsflowd` to send sFlow data to collector1 on port 6343 and to collector2 on port 6344. `hsflowd` polls counters every 20 seconds and samples 1 out of every 2048 packets.

{{%notice note%}}
The hardware can deliver a maximum of 16K samples per second. You can configure the number of samples per second in the `/etc/cumulus/datapath/traffic.conf` file:

```
# Set sflow/sample ingress cpu packet rate and burst in packets/sec
# Values: {0..16384}
#sflow.rate = 16384
#sflow.burst = 16384
```
{{%/notice%}}

Start the sFlow daemon:

```
cumulus@switch:~$ sudo systemctl start hsflowd.service
```

You do not need to configure anything else in the `/etc/hsflowd.conf` file.
<!-- vale off -->
### Manually Configure /etc/hsflowd.conf
<!-- vale on -->
You can set up the collectors and variables on each switch. Edit the `/etc/hsflowd.conf` file to set up your collectors and sampling rates in the `/etc/hsflowd.conf` file. For example:

```
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
  collector { ip=192.0.2.100 udpport=6343 }
  collector { ip=192.0.2.200 udpport=6344 }
}
```

This configuration polls the counters every 20 seconds, samples 1 of every 40000 packets for 40G interfaces, and sends this information to a collector at 192.0.2.100 on port 6343 and to another collector at 192.0.2.200 on port 6344.

{{%notice note%}}
Some collectors require each source to transmit on a different port, others listen on only one port. Refer to the documentation for your collector for more information.
{{%/notice%}}

To configure the IP address for the sFlow agent, configure one of the following in the `/etc/hsflowd.conf` file (following the recommendations in the {{<exlink url="https://sflow.net/host-sflow-linux-config.php" text="sFlow documentation">}}):

- The agent CIDR. For example, `agent.cidr = 10.0.0.0/8`. The IP address must fall within this range.
- The agent interface. For example, if the agent is using eth0, select the IP address for this interface.

To check the agent IP, run this command:

```
cumulus@switch:~$ grep agentIP /etc/hsflowd.auto
```

## Configure sFlow Visualization Tools

For information on configuring various sFlow visualization tools, read this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Monitoring/Configure-and-Use-sFlow-Visualization-Tools" >}}).

## Considerations

Cumulus Linux does not support sFlow egress sampling.

## Related Information

- {{<exlink url="http://www.sflow.org/products/collectors.php" text="sFlow Collectors">}}
- {{<exlink url="http://en.wikipedia.org/wiki/SFlow" text="sFlow Wikipedia page">}}
