---
title: Monitoring System Statistics and Network Traffic with sFlow
author: Cumulus Networks
weight: 473
aliases:
 - /display/DOCS/Monitoring+System+Statistics+and+Network+Traffic+with+sFlow
 - /pages/viewpage.action?pageId=8362597
pageID: 8362597
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
[sFlow](http://www.sflow.org/index.php) is a monitoring protocol that
samples network packets, application operations, and system counters.
sFlow collects both interface counters and sampled 5-tuple packet
information, enabling you to monitor your network traffic as well as
your switch state and performance metrics. An outside server, known as
an *sFlow collector*, is required to collect and analyze this data.

`hsflowd` is the service that samples and sends sFlow data to configured
collectors. By default, `hsflowd` is disabled and does *not* start
automatically when the switch boots up.

{{%notice note%}}

If you intend to run this service within a
[VRF](/cumulus-linux/Layer_3/Virtual_Routing_and_Forwarding_-_VRF),
including the [management VRF](/cumulus-linux/Layer_3/Management_VRF),
follow [these
steps](Management_VRF.html#src-8362940_ManagementVRF-services) for
configuring the service.

{{%/notice%}}

## <span>Configure sFlow</span>

To configure `hsflowd` to send to the designated collectors, either:

  - Use DNS service discovery (DNS-SD)

  - Manually configure the `/etc/hsflowd.conf` file

### <span>Configure sFlow via DNS-SD</span>

You can configure your DNS zone to advertise the collectors and polling
information to all interested clients.

Add the following content to the zone file on your DNS server:

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

The above snippet instructs `hsflowd` to send sFlow data to collector1
on port 6343 and to collector2 on port 6344. `hsflowd` will poll
counters every 20 seconds and sample 1 out of every 2048 packets.

{{%notice note%}}

The maximum samples per second delivered from the hardware is limited to
16K. You can configure the number of samples per second in the
`/etc/cumulus/datapath/traffic.conf` file, as shown below:

    # Set sflow/sample ingress cpu packet rate and burst in packets/sec
    # Values: {0..16384}
    #sflow.rate = 16384
    #sflow.burst = 16384

{{%/notice%}}

Start the sFlow daemon:

    cumulus@switch:~$ sudo systemctl start hsflowd.service

No additional configuration is required in `/etc/hsflowd.conf`.

### <span>Manually Configure /etc/hsflowd.conf</span>

You can set up the collectors and variables on each switch.

Edit the `/etc/hsflowd.conf` file to set up your collectors and sampling
rates in `/etc/hsflowd.conf`. For example:

    # ====== Sampling/Polling/Collectors ======
      # EITHER: automatic (DNS SRV+TXT from _sflow._udp):
      #   DNS-SD { }
      # OR: manual:
      #   Counter Polling:
      #     polling = 20
      #   default sampling N:
      #     sampling = 400
      #   sampling N on interfaces with ifSpeed:
            sampling.100M = 100
            sampling.1G = 1000
            sampling.10G = 10000
            sampling.40G = 40000
      #   sampling N for apache, nginx:
      #     sampling.http = 50
      #   sampling N for application (requires json):
      #     sampling.app.myapp = 100
      #   collectors:
      collector { ip=192.0.2.100 udpport=6343 }
      collector { ip=192.0.2.200 udpport=6344 }

This configuration polls the counters every 20 seconds, samples 1 of
every 2048 packets, and sends this information to a collector at
192.0.2.100 on port 6343 and to another collector at 192.0.2.200 on port
6344.

{{%notice note%}}

Some collectors require each source to transmit on a different port,
others listen on only one port. Refer to the documentation for your
collector for more information.

{{%/notice%}}

## <span>Configure sFlow Visualization Tools</span>

For information on configuring various sFlow visualization tools, read
this [Help Center
article](https://support.cumulusnetworks.com/hc/en-us/articles/201787866--WIP-Configuring-and-using-sFlow-visualization-tools).

## <span>Related Information</span>

  - [sFlow Collectors](http://www.sflow.org/products/collectors.php)

  - [sFlow Wikipedia page](http://en.wikipedia.org/wiki/SFlow)
