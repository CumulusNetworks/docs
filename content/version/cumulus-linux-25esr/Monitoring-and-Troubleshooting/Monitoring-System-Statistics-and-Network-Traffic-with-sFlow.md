---
title: Monitoring System Statistics and Network Traffic with sFlow
author: Cumulus Networks
weight: 163
aliases:
 - /display/CL25ESR/Monitoring+System+Statistics+and+Network+Traffic+with+sFlow
 - /pages/viewpage.action?pageId=5115966
pageID: 5115966
product: Cumulus Linux
version: 2.5 ESR
imgData: cumulus-linux-25esr
siteSlug: cumulus-linux-25esr
---
[sFlow](http://www.sflow.org/index.php) is a monitoring protocol that
samples network packets, application operations, and system counters.
sFlow enables you to monitor your network traffic as well as your switch
state and performance metrics. An outside server, known as an *sFlow
collector*, is required to collect and analyze this data.

`hsflowd` is the daemon that samples and sends sFlow data to configured
collectors. `hsflowd` is not included in the base Cumulus Linux
installation. After installation, `hsflowd` will automatically start
when the switch boots up.

## Installing hsflowd

To download and install the `hsflowd` package, use `apt-get`:

    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install -y hsflowd

## Configuring sFlow

You can configure `hsflowd` to send to the designated collectors via two
methods:

  - DNS service discovery (DNS-SD)
  - Manually configuring `/etc/hsflowd.conf`

### Configuring sFlow via DNS-SD

With this method, you need to configure your DNS zone to advertise the
collectors and polling information to all interested clients. Add the
following content to the zone file on your DNS server:

    _sflow._udp SRV 0 0 6343 collector1
    _sflow._udp SRV 0 0 6344 collector2
    _sflow._udp TXT (
    "txtvers=1"
    "sampling.1G=2048"
    "sampling.10G=4096"
    "sampling.40G=8192"
    "polling=20"
    )

The above snippet instructs `hsflowd` to send sFlow data to collector1
on port 6343 and to collector2 on port 6344. `hsflowd` will poll
counters every 20 seconds and sample 1 out of every 2048 packets.

After the initial configuration is ready, bring up the sFlow daemon by
running:

    cumulus@switch:~$ sudo service hsflowd start

No additional configuration is required in `/etc/hsflowd.conf`.

### Manually Configuring /etc/hsflowd.conf

With this method you will set up the collectors and variables on each
switch.

Edit `/etc/hsflowd.conf` and change *DNSSD = on* to *DNSSD = off*:

    DNSSD = off

Then set up your collectors and sampling rates in `/etc/hsflowd.conf`:

    # Manual Configuration (requires DNSSD=off above)
      #################################################
    
      # Typical configuration is to send every 30 seconds
      polling = 20
    
      sampling.1G=2048
      sampling.10G=4096
      sampling.40G=8192
    
      collector {
        ip = 192.0.2.100
        udpport = 6343
      }
    
      collector {
        ip = 192.0.2.200
        udpport = 6344
      }

This configuration polls the counters every 20 seconds, samples 1 of
every 2048 packets and sends this information to a collector at
192.0.2.100 on port 6343 and to another collector at 192.0.2.200 on port
6344.

{{%notice note%}}

Some collectors require each source to transmit on a different port,
others may listen on only one port. Please refer to the documentation
for your collector for more information.

{{%/notice%}}

## Configuring sFlow Visualization Tools

For information on configuring various sFlow visualization tools, read this 
[Help Center article](https://support.cumulusnetworks.com/hc/en-us/articles/201787866--WIP-Configuring-and-using-sFlow-visualization-tools).

## Configuration Files

  - /etc/hsflowd.conf

## Useful Links

  - [sFlow Collectors](http://www.sflow.org/products/collectors.php)
  - [sFlow Wikipedia page](http://en.wikipedia.org/wiki/SFlow)
