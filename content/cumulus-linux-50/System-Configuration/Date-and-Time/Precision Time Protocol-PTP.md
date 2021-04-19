---
title: Precision Time Protocol - PTP
author: NVIDIA
weight: 128
toc: 3
---
With the growth of low latency and high performance applications, precision timing has become increasingly important. Precision Time Protocol (PTP) is used to synchronize clocks in a network and is capable of sub-microsecond accuracy. The clocks are organized in a master-slave hierarchy. The slaves are synchronized to their masters, which can be slaves to their own masters. The hierarchy is created and updated automatically by the best master clock (BMC) algorithm, which runs on every clock. The grandmaster clock is the top-level master and is typically synchronized by using a Global Positioning System (GPS) time source to provide a high-degree of accuracy.

A boundary clock has multiple ports; one or more master ports and one or more slave ports. The master ports provide time (the time can originate from other masters further up the hierarchy) and the slave ports receive time. The boundary clock absorbs sync messages in the slave port, uses that port to set its clock, then generates new sync messages from this clock out of all of its master ports.

Cumulus Linux includes the `linuxptp` package for PTP, which uses the `phc2sys` daemon to synchronize the PTP clock with the system clock.

{{%notice note%}}
- PTP is supported in boundary clock mode only (the switch provides timing to downstream servers; it is a slave to a higher-level clock and a master to downstream clocks).
- The switch uses hardware time stamping to capture timestamps from an Ethernet frame at the physical layer. This allows PTP to account for delays in message transfer and greatly improves the accuracy of time synchronization.
- IPv4 and IPv6 UDP PTP packets are supported.
- Only multicast message mode is supported.
- Only a single PTP domain per network is supported. A PTP domain is a network or a portion of a network within which all the clocks are synchronized.
- PTP is supported on BGP unnumbered interfaces.
- You can isolate PTP traffic to a non-default VRF.
- You can not run both PTP and NTP on the switch.
{{%/notice%}}

In the following example, boundary clock 2 receives time from Master 1 (the grandmaster) on a PTP slave port, sets its clock and passes the time down from the PTP master port to boundary clock 1. Boundary clock 1 receives the time on a PTP slave port, sets its clock and passes the time down the hierarchy through the PTP master ports to the hosts that receive the time.

{{< img src = "/images/cumulus-linux/date-time-ptp-example.png" >}}

## Basic Configuration

To configure the PTP boundary clock:

1. Enable PTP on the switch to start the `ptp4l` and `phc2sys` processes:

   ```
   cumulus@switch:~$ cl set service ptp 1 enable on
   ```

2. Configure the interfaces on the switch that you want to use for PTP. Each interface must be configured as a layer 3 routed interface with an IP address.

   ```
   cumulus@switch:~$ cl set interface swp13s0 ip address 10.0.0.9/32
   cumulus@switch:~$ cl set interface swp13s0 ip address 10.0.0.10/32
   ```

3. Configure PTP options on the switch:

    - Set the clock mode to configure the switch to be a boundary clock. This is the only option at this time.
    - Set the priority, which selects the best master clock. You can set priority 1 or 2. For each priority, you can use a number between 0 and 255. The default priority is 255. For the boundary clock, use a number above 128. The lower priority is applied first.
    - Add the PTP master and slave interfaces. You do not specify which is a master interface and which is a slave interface; this is determined by the PTP packet received. The following commands provide an example configuration:

      ```
      cumulus@switch:~$ cl set service ptp 1 clock-mode boundary
      cumulus@switch:~$ cl set service ptp 1 priority2 254
      cumulus@switch:~$ cl set service ptp 1 priority1 254
      cumulus@switch:~$ cl set interface swp13s0 service ptp enable on
      cumulus@switch:~$ cl set interface swp13s1 service ptp enable on
      cumulus@switch:~$ cl config apply
      ```

The configuration is saved in the `/etc/ptp4l.conf` file.

## Optional Configuration

### Transport Mode

By default, PTP messages are encapsulated in UDP/IPV4 frames. To configure PTP messages to be encapsulated in UDP/IPV6 frames:

```
cumulus@switch:~$ cl set interface swp6 service ptp transport ipv6
cumulus@switch:~$ cl config apply
```

## Message Modes

Cumulus Linux supports the following PTP message modes:
- Multicast, where the ports subscribe to two multicast addresses, one for event messages that are timestamped and the other for general messages that are not timestamped. The SYNC message sent by the master is a multicast message and is received by all slave ports. This is critical and is required, since the slaves need the master's time. The slave ports in turn generate a Delay Request to the master. This is a multicast message and is received not only by the Master for which the message is intended, but also by other slave ports. Similarly, the master's Delay Response is also received by all slave ports in addition to the intended slave port. The slave ports receiving the unintended Delay Requests and Responses need to drop them. This is unnecessary wastage of network bandwidth. It becomes worse when there are hundreds of slave ports. 
- Mixed, where the SYNC and Announce messages are sent as multicast messages but the Delay Request and Response messages are sent as unicast. This avoids the issue seen in pure multicast message mode where every slave port sees Delay Requests and Responses from every other slave port.

Multicast mode is the default setting. To set mthe message mode to *mixed*:

```
cumulus@switch:~$ cl set service ptp 1 message-mode mixed
cumulus@switch:~$ cl config apply
```

### One-step and Two-step Mode

The Cumulus Linux switch supports hardware packet time stamping and provides two modes:
- In *one-step* mode, the PTP packet is time stamped as it egresses the port and there is no need for a follow-up packet.
- In *two-step* mode, the time is noted when the PTP packet egresses the port and is sent in a separate (follow-up) message.

One-step mode is the default configuration. To configure the switch to use two-step mode:

```
cumulus@switch:~$ cl set service ptp 1 two-step on
cumulus@switch:~$ cl config apply
```

### Acceptable Master Table

The acceptable master table option is a security feature that prevents a rogue player pretending to be Master from taking over the PTP network. The clock IDs of known masters are configured in the Acceptable Master table. If you configure a PTP port on the switch with the acceptable master table option, the BMC algorithm checks if the master received on the Announce message is in this table and only then it proceeds with the Master selection. Thi option is disabled by default on PTP ports.

There is also an option to configure an AlternatePriority1 for the Masters. When configured (greater than zero), the priority1 value on the Announce message is replaced with the configured AlternatePriority1 value to be used in the BMC algorithm.

The following example commands enable the PTP acceptable master table option for swp6:

```
cumulus@switch:~$ cl set interface swp6 service ptp acceptable-master on
cumulus@switch:~$ cl config apply
```

### Forced Master

By default, ports configured for PTP are in auto mode, where the state of the port is determined by the BMC algorithm.

You can configure *Forced Master* mode on a PTP port so that it is always in a master state and the BMC algorithm is not run for this port. Any announce messages received on this port are ignored.

```
cumulus@switch:~$ cl set interface swp6 service ptp forced-master on
cumulus@switch:~$ cl config apply
```

### DSCP and TTL

You can configure the DiffServ code point (DSCP) value for all PTP IPv4 packets originated locally. You can set a value between 0 and 63.

```
cumulus@switch:~$ cl set interface swp6 service ptp forced-master on
cumulus@switch:~$ cl config apply
```

To restrict the number of hops a PTP message can travel, set the TTL on the PTP interface. You can set a value between 1 and 255.

```
cumulus@switch:~$ cl set interface swp6 service ptp ttl 20
cumulus@switch:~$ cl config apply
```

## Delete PTP Boundary Clock Configuration

To delete PTP configuration, delete the PTP master and slave interfaces. The following example commands delete the PTP interfaces `swp6`, `swp7`, and `swp8`.

```
cumulus@switch:~$ cl unset interface swp6 service ptp
cumulus@switch:~$ cl unset interface swp7 service ptp
cumulus@switch:~$ cl unset interface swp8 service ptp
cumulus@switch:~$ cl config apply
```

## Troubleshooting

To view a summary of the PTP configuration on the switch, run the `net show configuration ptp` command:

```
cumulus@switch:~$ net show configuration ptp

ptp
  global

    slaveOnly
      0

    priority1
      255

    priority2
      255

    domainNumber
      0

    logging_level
      5

    path_trace_enabled
      0

    use_syslog
      1

    verbose
      0

    summary_interval
      0

    time_stamping
      hardware

    gmCapable
      0
  swp15s0
  swp15s1
...
```

### View PTP Status Information

To view PTP status information, run the `net show ptp parent_data_set` command:

```
cumulus@switch:~$ net show ptp parent_data_set
parent_data_set
===============
parentPortIdentity                    000200.fffe.000001-1
parentStats                           0
observedParentOffsetScaledLogVariance 0xffff
observedParentClockPhaseChangeRate    0x7fffffff
grandmasterPriority1                  127
gm.ClockClass                         248
gm.ClockAccuracy                      0xfe
gm.OffsetScaledLogVariance            0xffff
grandmasterPriority2                  127
grandmasterIdentity                   000200.fffe.000001
```

To view the additional PTP status information, including the delta in nanoseconds from the master clock, run the `sudo pmc -u -b 0 'GET TIME_STATUS_NP'` command:

```
cumulus@switch:~$ sudo pmc -u -b 0 'GET TIME_STATUS_NP'
sending: GET TIME_STATUS_NP
    7cfe90.fffe.f56dfc-0 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
        master_offset              12610
        ingress_time               1525717806521177336
        cumulativeScaledRateOffset +0.000000000
        scaledLastGmPhaseChange    0
        gmTimeBaseIndicator        0
        lastGmPhaseChange          0x0000'0000000000000000.0000
        gmPresent                  true
        gmIdentity                 000200.fffe.000005
    000200.fffe.000005-1 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
        master_offset              0
        ingress_time               0
        cumulativeScaledRateOffset +0.000000000
        scaledLastGmPhaseChange    0
        gmTimeBaseIndicator        0
        lastGmPhaseChange          0x0000'0000000000000000.0000
        gmPresent                  false
        gmIdentity                 000200.fffe.000005
    000200.fffe.000006-1 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
        master_offset              5544033534
        ingress_time               1525717812106811842
        cumulativeScaledRateOffset +0.000000000
        scaledLastGmPhaseChange    0
        gmTimeBaseIndicator        0
        lastGmPhaseChange          0x0000'0000000000000000.0000
        gmPresent                  true
        gmIdentity                 000200.fffe.000005
```

## Example Configuration

In the following example, the boundary clock on the switch receives time from Master 1 (the grandmaster) on PTP slave port swp3s0, sets its clock and passes the time down through PTP master ports swp3s1, swp3s2, and swp3s3 to the hosts that receive the time.

{{< img src = "/images/cumulus-linux/date-time-ptp-config.png" >}}

The configuration for the above example is shown below. The example assumes that you have already configured the layer 3 routed interfaces (`swp3s0`, `swp3s1`, `swp3s2`, and `swp3s3`) you want to use for PTP.

```
cumulus@switch:~$ cl set service ptp 1 clock-mode boundary
cumulus@switch:~$ cl set service ptp 1 priority2 254
cumulus@switch:~$ cl set service ptp 1 priority1 254
cumulus@switch:~$ cl set interface swp13s0 service ptp enable on
cumulus@switch:~$ cl set interface swp13s1 service ptp enable on
cumulus@switch:~$ cl set interface swp13s2 service ptp enable on
cumulus@switch:~$ cl set interface swp13s3 service ptp enable on
cumulus@switch:~$ cl config apply
```
