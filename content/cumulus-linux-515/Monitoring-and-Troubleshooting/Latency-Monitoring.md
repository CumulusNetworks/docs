---
title: Latency Monitoring
author: NVIDIA
weight: 1236
toc: 3
---
Latency monitoring enables you to precisely measure and analyze the time it takes for data packets to traverse between switches in a data center network fabric and helps to:
- Identify performance bottlenecks in large-scale data centers.
- Support real-time network health monitoring and proactive management.
- Plan network topology and capacity expansion.
- Manage incident responses in latency-sensitive environments.

You can monitor latency on Spectrum-4 and later switches, and on layer 3 and untagged physical links only.

{{%notice note%}}
Cumulus Linux does not support:
- Leaf to leaf or spine to spine latency measurement.
- Latency measurement of GPU or server facing interfaces.
- Link local IPv6 (routable addresses are required).
- One time or on-demand measurement.
- One-way latency.
{{%/notice%}}

## Latency Components Measured

Cumulus Linux measures the following components:

| Component | Description | Typical Range  |
| ------------- | -------------- | --------------- |
| Local Switch Egress Queue | The time in the outgoing queue of the leaf switch before transmission. | Between 0 and 10 microseconds. |
| Forward Path Cable  | The packet travel time from leaf to spine through a physical medium. | Between 5 and 10 microseconds. |
| Remote Switch Queue | The time in the spine switch ingress queue plus internal processing. | Between 0 and 10 microseconds. |
| Return Path Cable | The echo packet travel time from the spine back to the leaf.| Between 5 and 10 microseconds. |

## Configure Latency Monitoring

To configure latency monitoring, enable the feature and set options such as the periodic probe interval, and the interfaces and traffic classes you want to monitor. You can also configure the switch to export latency data to a configured telemetry module, such as gNMI or Open Telemetry.

To enable latency monitoring, run the `nv set system telemetry latency-measurement state enabled` command:

```
cumulus@switch:~$ nv set system telemetry latency-measurement state enabled
cumulus@switch:~$ nv config apply
```

You can configure the following parameters:
- The periodic probe interval in seconds.
- The traffic class and port you want to monitor with the source IP address, destination IP address, source MAC address, destination MAC address, VLAN or DSCP.

The following example sets the periodic interval to 2 seconds, and monitors traffic class 0, 3, and 6 on swp1 through 128:

```
cumulus@switch:~$ nv set system telemetry latency-measurement periodic-interval 2 
cumulus@switch:~$ nv set interface swp1-128 latency-measurement traffic-class 0,3,6
cumulus@switch:~$ nv config apply
```

The following example sets the periodic interval to 5, and monitors IPv6 packets on swp1 through swp51, traffic class 0 with DSCP af31:

```
cumulus@switch:~$ nv set system telemetry latency-measurement periodic-interval 5
cumulus@switch:~$ nv set interface swp1-51 latency-measurement traffic-class 0 protocol ipv6 dscp af31
cumulus@switch:~$ nv config apply
```

{{%notice infonopad%}}

To ensure accurate latency monitoring and appropriate resource utilization, adjust the periodic interval based on the number of traffic classes (TCs) configured with latency monitoring per port. NVIDIA recommends setting the minimum interval according to the total number of TCs enabled per port:<br><br>


| # of TCs per-port | Minimum periodic interval |
| ------- | ----------- |
| ≤ 4 | 1 second |
| > 4, but ≤ 8 | 2 seconds |
| > 8, but ≤ 12 | 3 seconds |
| > 12, but ≤ 16 | 4 seconds |

{{%/notice%}}

To export latency data to a configured telemetry module:

```
cumulus@switch:~$ nv set system telemetry latency-measurement export state enabled 
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
When using {{<link url="Open-Telemetry-Export/#customize-export" text="statistic groups">}} to specify which metrics are exported, add `latency-measurement` to the `stats-group` configuration to include latency metrics:

```
cumulus@switch:~$ nv set system telemetry stats-group <name> latency-measurement
cumulus@switch:~$ nv config apply
```
{{%/notice%}}

## Show Latency Information

To show latency measurement information for an interface, run the `nv show interface swp1 latency-measurement` command:

```
cumulus@switch:~$ nv show interface swp1 latency-measurement
traffic-class   protocol  DSCP   Latency   Status       Timestamp 
------------------------------------------------------------------------------- 
1               ipv4      12     19         SUCCESS     2025-01-25 10:15:32 
```

To show latency measurement information for an interface traffic class for IPv4, run the `nv show interface <interface-id> latency-measurement traffic-class <traffic-class> protocol ipv4` command:

```
cumulus@switch:~$ nv show interface swp1 latency-measurement traffic-class 0 protocol ipv4 
 DSCP: 0 
 Current Latency: 12.3 μs 
 Status: SUCCESS 
 Last Update: 2025-01-25 10:15:32 
```
