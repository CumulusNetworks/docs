---
title: ASIC Monitoring
author: NVIDIA
weight: 1230
toc: 3
---
Cumulus Linux provides two ASIC monitoring tools that collect and distributes data about the state of the ASIC.
- Histogram Collection
- High Frequency Telemetry

## Histogram Collection

The histogram collection monitoring tool polls for data at specific intervals and takes certain actions so that you can identify and respond to problems, such as:
- Microbursts that result in longer packet latency.
- Packet buffer congestion that might lead to packet drops.
- Network problems with a particular switch, port, or traffic class.

Cumulus Linux provides several histograms:
- *Egress queue length* shows information about egress buffer utilization over time.
- *Ingress queue length* shows information about ingress buffer utilization over time.
- *Counter* shows information about bandwidth utilization for a port over time.
- *Latency* shows information about packet latency over time.
- *Packet drops due to errors* (Linux only).

{{%notice note%}}
Cumulus Linux supports:
- The egress queue length histogram on Spectrum 1 and later.
- The ingress queue length histogram and the latency histogram on Spectrum-2 and later.
- The counter histogram (transmitted packet, transmitted byte, received packet, received byte, and CRC counters) on Spectrum-2 and later.
- The counter histogram (layer 1 received byte counters and layer 1 transmitted byte counters) on Spectrum-4 only.
{{%/notice%}}

### Histogram Collection Example

The NVIDIA Spectrum ASIC provides a mechanism to measure and report ingress and egress queue lengths, counters and latency in histograms (a graphical representation of data, which it divides into intervals or bins). Each queue reports through a histogram with 10 bins, where each bin represents a range of queue lengths.

You configure the histogram with a minimum size boundary (Min) and a histogram size. You then derive the maximum size boundary (Max) by adding the minimum size boundary and the histogram size.

The 10 bins have numbers 0 through 9. Bin 0 represents queue lengths up to the Min specified, including queue length 0. Bin 9 represents queue lengths of Max and above. Bins 1 through 8 represent equal-sized ranges between the Min and Max (by dividing the histogram size by 8).

For example, consider the following histogram queue length ranges, in bytes:

- Min = 960
- Histogram size = 12288
- Max = 13248
- Range size = 1536
- Bin 0: 0:959
- Bin 1: 960:2495
- Bin 2: 2496:4031
- Bin 3: 4032:5567
- Bin 4: 5568:7103
- Bin 5: 7104:8639
- Bin 6: 8640:10175
- Bin 7: 10176:11711
- Bin 8: 11712:13247
- Bin 9: 13248:\*

The following illustration demonstrates a histogram showing how many times the queue length for a port was in the ranges specified by each bin. The example shows that the queue length was between 960 and 2495 bytes 125 times within one second.

{{< img src = "/images/cumulus-linux/asic-monior-histogram-queue.png" >}}

### Configure Histogram Collection

To configure Histogram Collection, you specify:
- The type of data to collect.
- The switch ports to monitor.
  - For the egress queue length and latency histograms, you can specify the traffic class you want to monitor for a port or range of ports.
  - For the ingress queue length histogram, you can specify the priority group you want to monitor for a port or range of ports.
- How and when to start reading the ASIC: at a specific queue length, number of packets or bytes received or transmitted, or number of nanoseconds latency.
- What actions to take: create a snapshot file, send a message to the `/var/log/syslog` file, or both.

### Enable Histogram Collection

To enable histogram collection:

{{< tabs "TabID62 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system telemetry enable on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The `asic-monitor` service manages the histogram collection tool (`systemd` manages the `asic-monitor` service). The `asic-monitor` service reads the `/etc/cumulus/datapath/monitor.conf` configuration file to determine what statistics to collect and when to trigger. The service always starts; however, if the configuration file is empty, the service exits.

{{%notice note%}}
Restarting the `asic-monitor` service does not disrupt traffic or require you to restart `switchd`.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

### Histogram Settings

Histogram settings include the type of data you want to collect, the ports you want the histogram to monitor, the sampling time of the histogram, the histogram size, and the minimum boundary size for the histogram.
- The ingress queue length histogram can monitor a specific priority group for a port or range of ports.
- The egress queue length histogram and the latency histogram can monitor a specific traffic class for a port or range of ports. Traffic class 0 through 7 is for unicast traffic and traffic class 8 through 15 is for multicast traffic.
- The latency histogram can monitor a specific traffic class for a port or range of ports. Traffic class 0 through 7 is for unicast traffic and traffic class 8 through 15 is for multicast traffic.
- The counter histogram can monitor the following counter types:
    - Received packet counters (`rx-packet`)
    - Transmitted packet counters (`tx-packet`)
    - Received byte counters (`rx-byte`)
    - Transmitted byte counters (`tx-byte`)
    - CRC counters (`crc`)
    - Layer 1 received byte counters (`l1-rx-byte`). The byte count includes layer 1<span class="a-tooltip">[IPG](## "Interpacket Gap")</span> bytes.
    - Layer 1 transmitted byte counters (`l1-tx-byte`). The byte count includes layer 1<span class="a-tooltip">[IPG](## "Interpacket Gap")</span> bytes.
- You can enable up to two counter histogram counter types per physical interface. The counter histogram does not support bonds or virtual interfaces.
- The default minimum boundary size is 960 bytes. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of queue lengths per bin.
- The default value for the sampling time is 1024 nanoseconds.

{{%notice note%}}
When you configure minimum boundary and histogram sizes, Cumulus Linux rounds down the configured byte value to the nearest multiple of the switch ASIC cell size before programming it into hardware. The cell size is a fixed number of bytes on each switching ASIC:

- Spectrum-1: 96 bytes
- Spectrum-2 and Spectrum-3: 144 bytes
- Spectrum-4: 192 bytes 
{{%/notice%}}

{{< tabs "TabID81 ">}}
{{< tab "NVUE Commands ">}}

The histogram type can be `egress-buffer`, `ingress-buffer`, `counter`, or `latency`.

- To change global histogram settings, run the `nv set system telemetry histogram <type>` command.
- To enable histograms on interfaces or to change interface level settings, run the `nv set interface <interface> telemetry histogram <type>` command.
  
{{< tabs "TabID93 ">}}
{{< tab "Egress Queue Length ">}}

The following example configures the egress queue length histogram and sets the minimum boundary size to 960, the histogram size to 12288, and the sampling interval to 1024. These settings apply to interfaces that have the `egress-buffer` histogram enabled and do not have different values configured for these settings at the interface level:

```
cumulus@switch:~$ nv set system telemetry histogram egress-buffer bin-min-boundary 960 
cumulus@switch:~$ nv set system telemetry histogram egress-buffer histogram-size 12288 
cumulus@switch:~$ nv set system telemetry histogram egress-buffer sample-interval 1024
cumulus@switch:~$ nv config apply
```

The following example enables the egress queue length histogram for traffic class 0 on swp1 through swp8 with the globally applied minimum boundary, histogram size, and sample interval. The example also enables the egress queue length histogram for traffic class 1 on swp9 through swp16 and sets the minimum boundary to 768 bytes, the histogram size to 9600 bytes, and the sampling interval to 2048 nanoseconds.

```
cumulus@switch:~$ nv set system telemetry enable on
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram egress-buffer traffic-class 0
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram egress-buffer traffic-class 1 bin-min-boundary 768
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram egress-buffer traffic-class 1 histogram-size 9600
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram egress-buffer traffic-class 1 sample-interval 2048
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Ingress Queue Length ">}}

The following example configures the ingress queue length histogram and sets the minimum boundary size to 960 bytes, the histogram size to 12288 bytes, and the sampling interval to 1024 nanoseconds. These settings apply to interfaces that have the `ingress-buffer` histogram enabled and do not have different values configured for these settings at the interface level:

```
cumulus@switch:~$ nv set system telemetry enable on
cumulus@switch:~$ nv set system telemetry histogram ingress-buffer bin-min-boundary 960 
cumulus@switch:~$ nv set system telemetry histogram ingress-buffer histogram-size 12288 
cumulus@switch:~$ nv set system telemetry histogram ingress-buffer sample-interval 1024
cumulus@switch:~$ nv config apply
```

The following example enables the ingress queue length histogram for priority group 0 on swp1 through swp8 with the globally applied minimum boundary, histogram size, and sample interval. The example also enables the ingress queue length histogram for priority group 1 on swp9 through swp16 and sets the minimum boundary to 768 bytes, the histogram size to 9600 bytes, and the sampling interval to 2048 nanoseconds.

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram ingress-buffer priority-group 0
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram ingress-buffer priority-group 1 bin-min-boundary 768
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram ingress-buffer priority-group 1 histogram-size 9600
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram ingress-buffer priority-group 1 sample-interval 2048
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Counter Histogram ">}}

The following example configures the counter histogram and sets the minimum boundary size to 960, the histogram size to 12288, and the sampling interval to 1024. The histogram monitors all counter types. These settings apply to interfaces that have the `counter` histogram enabled and do not have different values configured for these settings at the interface level:

```
cumulus@switch:~$ nv set system telemetry histogram counter bin-min-boundary 960
cumulus@switch:~$ nv set system telemetry histogram counter histogram-size 12288
cumulus@switch:~$ nv set system telemetry histogram counter sample-interval 1024
cumulus@switch:~$ nv config apply
```

The following example enables the counter histogram on swp1 through swp8 and uses the global settings for the minimum boundary size, histogram size, and the sampling interval. The histogram monitors all received packet counters on ports 1 through 8:

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram counter counter-type rx-packet
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Latency Histogram ">}}

The following example configures the latency histogram and sets the minimum boundary size to 960 and the histogram size to 12288. These settings apply to interfaces that have the `latency` histogram enabled and do not have different values configured for these settings at the interface level:

```
cumulus@switch:~$ nv set system telemetry histogram latency bin-min-boundary 960 
cumulus@switch:~$ nv set system telemetry histogram latency histogram-size 12288 
cumulus@switch:~$ nv config apply
```

The following example enables the latency histogram for traffic class 0 on swp1 through swp8 with the globally applied minimum boundary and histogram size. The example also enables the latency histogram for traffic class 1 on swp9 through swp16 and sets the minimum boundary to 768 bytes and the histogram size to 9600 bytes.

```
cumulus@switch:~$ nv set system telemetry enable on
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram latency traffic-class 0
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram latency traffic-class 1 bin-min-boundary 768
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram latency traffic-class 1 histogram-size 9600
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit settings in the `/etc/cumulus/datapath/monitor.conf` file, then restart the `asic-monitor` service with the `systemctl restart asic-monitor.service` command. The `asic-monitor` service reads the new configuration file and then runs until you stop the service with the `systemctl stop asic-monitor.service` command.

The following table describes the ASIC monitor settings.

| Setting| Description|
|------- |----------- |
| `port_group_list` | Specifies the names of the monitors (port groups) you want to use to collect data, such as `histogram_pg`. You can provide any name you want for the port group. You must use the same name for all the port group settings.<br><br>Example:<pre>monitor.port_group_list = [histogram_pg,discards_pg,buffers_pg,all_packets_pg]</pre>**Note**: You must specify at least one port group. If the port group list is empty, `systemd` shuts down the `asic-monitor` service. |
| `<port_group_name>.port_set` | Specifies the range of ports you want to monitor, such as `swp4,swp8,swp10-swp50`. To specify all ports, use the `all_ports` option.<br><br>Example:<pre>monitor.histogram_pg.port_set = swp1-swp50</pre><pre>monitor.histogram_pg.port_set = all_ports</pre> |
| `<port_group_name>.stat_type` | Specifies the type of data that the port group collects.<br><br>For egress queue length histograms, specify `histogram_tc`. For example:<pre>monitor.histogram_pg.stat_type = histogram_tc</pre>For ingress queue length histograms, specify `histogram_pg`. For example: <pre>monitor.histogram_pg.stat_type = histogram_pg</pre>For counter histograms, specify `histogram_counter`. For example:<pre>monitor.histogram_pg.stat_type = histogram_counter</pre>. For latency histograms, specify `histogram_latency`. For example:<pre> monitor.histogram_pg.stat_type = histogram_latency</pre>.|
| `<port_group_name>.cos_list` | For histogram monitoring, each CoS (Class of Service) value in the list has its own histogram on each port. The global limit on the number of histograms is an average of one histogram per port.<br><br>Example:<pre>monitor.histogram_pg.cos_list = [0]</pre> |
| `<port_group_name>.counter_type` | Specifies the counter type for counter histogram monitoring. The counter types can be `tx-pkt`,`rx-pkt`,`tx-byte`,`rx-byte`.<br><br>Example:<pre>monitor.histogram_pg.counter_type = [rx_byte]</pre> |
| `<port_group_name>.trigger_type` | Specifies the type of trigger that initiates data collection. The only option is timer. At least one port group must have a configured timer, otherwise no data is ever collected.<br><br>Example:<pre>monitor.histogram_pg.trigger_type = timer</pre> |
| `<port_group_name>.timer` | Specifies the frequency at which data collects; for example, a setting of 1s indicates that data collects one time per second. You can set the timer to the following:<br>1 to 60 seconds: 1s, 2s, and so on up to 60s<br>1 to 60 minutes: 1m, 2m, and so on up to 60m<br>1 to 24 hours: 1h, 2h, and so on up to 24h<br>1 to 7 days: 1d, 2d and so on up to 7d<br><br>Example:<pre>monitor.histogram_pg.timer = 4s</pre> |
| `<port_group_name>.histogram.minimum_bytes_boundary` | *For histogram monitoring*.<br><br>The minimum boundary size for the histogram in bytes. On a Spectrum switch, this number must be a multiple of 96. Adding this number to the size of the histogram produces the maximum boundary size. These values represent the range of queue lengths per bin.<br><br>Example:<pre>monitor.histogram_pg.histogram.minimum_bytes_boundary = 960</pre> |
| `<port_group_name>.histogram.histogram_size_bytes` | *For histogram monitoring*.<br><br>The size of the histogram in bytes. Adding this number and the minimum_bytes_boundary value together produces the maximum boundary size. These values represent the range of queue lengths per bin.<br><br>Example:<pre>monitor.histogram_pg.histogram.histogram_size_bytes = 12288</pre> |
| `<port_group_name>.histogram.sample_time_ns` | *For histogram monitoring*.<br><br>The sampling time of the histogram in nanoseconds.<br><br>Example:<pre>monitor.histogram_pg.histogram.sample_time_ns = 1024</pre> |

{{< tabs "TabID184 ">}}
{{< tab "Egress Queue Examples ">}}

The following example configures the egress queue length histogram and sets the minimum boundary size to 960, the histogram size to 12288, and the sampling interval to 1024. The histogram collects data every second for traffic class 0 through 15 on all ports:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/monitor.conf
...
monitor.port_group_list                               = [histogram_pg] 
monitor.histogram_pg.port_set                         = allports
monitor.histogram_pg.stat_type                        = histogram_tc
monitor.histogram_pg.cos_list                         = [0-15]
monitor.histogram_pg.trigger_type                     = timer
monitor.histogram_pg.timer                            = 1s
...
monitor.histogram_pg.histogram.minimum_bytes_boundary = 960
monitor.histogram_pg.histogram.histogram_size_bytes   = 12288
monitor.histogram_pg.histogram.sample_time_ns         = 1024
```

The following example configures the egress queue length histogram and sets the minimum boundary to 960 bytes, the histogram size to 12288 bytes, and the sampling interval to 1024 nanoseconds. The histogram collects data every second for traffic class 0 on swp1 through swp8, and for traffic class 1 on swp9 through swp16.

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/monitor.conf
...
monitor.port_group_list                                = [histogram_gr1, histogram_gr2] 
monitor.histogram_gr1.port_set                         = swp1-swp8
monitor.histogram_gr1.stat_type                        = histogram_tc
monitor.histogram_gr1.cos_list                         = [0]
monitor.histogram_gr1.trigger_type                     = timer
monitor.histogram_gr1.timer                            = 1s
...
monitor.histogram_gr1.histogram.minimum_bytes_boundary = 960
monitor.histogram_gr1.histogram.histogram_size_bytes   = 12288
monitor.histogram_gr1.histogram.sample_time_ns         = 1024

monitor.histogram_gr2.port_set                         = swp9-swp16
monitor.histogram_gr2.stat_type                        = histogram_tc
monitor.histogram_gr2.cos_list                         = [1]
monitor.histogram_gr2.trigger_type                     = timer
monitor.histogram_gr2.timer                            = 1s
...
monitor.histogram_gr2.histogram.minimum_bytes_boundary = 960
monitor.histogram_gr2.histogram.histogram_size_bytes   = 12288
monitor.histogram_gr2.histogram.sample_time_ns         = 1024
```

{{< /tab >}}
{{< tab "Ingress Queue Examples ">}}

The following example configures the ingress queue length histogram and sets the minimum boundary size to 960 bytes, the histogram size to 12288 bytes, and the sampling interval to 1024 nanoseconds. The histogram collects data every second for priority group 1 through 15 on all ports.

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/monitor.conf
...
monitor.port_group_list                               = [histogram_pg] 
monitor.histogram_pg.port_set                         = allports
monitor.histogram_pg.stat_type                        = histogram_pg
monitor.histogram_pg.cos_list                         = [0-15]
monitor.histogram_pg.trigger_type                     = timer
monitor.histogram_pg.timer                            = 1s
...
monitor.histogram_pg.histogram.minimum_bytes_boundary = 960
monitor.histogram_pg.histogram.histogram_size_bytes   = 12288
monitor.histogram_pg.histogram.sample_time_ns         = 1024
```

The following example configures the ingress queue length histogram and sets the minimum boundary size to 960, the histogram size to 12288, and the sampling interval to 1024. The histogram monitors priority group 0 on ports 1 through 8 and priority group 1 on ports 9 through 16:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/monitor.conf
...
monitor.port_group_list                                = [histogram_gr1, histogram_gr2] 
monitor.histogram_gr1.port_set                         = swp1-swp8
monitor.histogram_gr1.stat_type                        = histogram_pg
monitor.histogram_gr1.cos_list                         = [0]
monitor.histogram_gr1.trigger_type                     = timer
monitor.histogram_gr1.timer                            = 1s
...
monitor.histogram_gr1.histogram.minimum_bytes_boundary = 960
monitor.histogram_gr1.histogram.histogram_size_bytes   = 12288
monitor.histogram_gr1.histogram.sample_time_ns         = 1024

monitor.histogram_gr2.port_set                         = swp9-swp16
monitor.histogram_gr2.stat_type                        = histogram_pg
monitor.histogram_gr2.cos_list                         = [1]
monitor.histogram_gr2.trigger_type                     = timer
monitor.histogram_gr2.timer                            = 1s
...
monitor.histogram_gr2.histogram.minimum_bytes_boundary = 960
monitor.histogram_gr2.histogram.histogram_size_bytes   = 12288
monitor.histogram_gr2.histogram.sample_time_ns         = 1024
```

{{< /tab >}}
{{< tab "Counter Histogram Examples ">}}

The following example configures the counter histogram and sets the minimum boundary size to 960, the histogram size to 12288, and the sampling interval to 1024. The histogram monitors all counter types:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/monitor.conf
...
monitor.port_group_list                               = [histogram_pg] 
monitor.histogram_pg.port_set                         = allports
monitor.histogram_pg.stat_type                        = histogram_counter
monitor.histogram_pg.counter_type                     = [tx-pkt,rx-pkt,tx-byte,rx-byte]
monitor.histogram_pg.trigger_type                     = timer
monitor.histogram_pg.timer                            = 1s
...
monitor.histogram_pg.histogram.minimum_bytes_boundary = 960
monitor.histogram_pg.histogram.histogram_size_bytes   = 12288
monitor.histogram_pg.histogram.sample_time_ns         = 1024
```

The following example configures the counter histogram and sets the minimum boundary size to 960, the histogram size to 12288, and the sampling interval to 1024. The histogram monitors all received packets on ports 1 through 8:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/monitor.conf
...
monitor.port_group_list                               = [histogram_pg] 
monitor.histogram_pg.port_set                         = swp1-swp8
monitor.histogram_pg.stat_type                        = histogram_counter
monitor.histogram_pg.counter_type                     = [tx-pkt]
monitor.histogram_pg.trigger_type                     = timer
monitor.histogram_pg.timer                            = 1s
...
monitor.histogram_pg.histogram.minimum_bytes_boundary = 960
monitor.histogram_pg.histogram.histogram_size_bytes   = 12288
monitor.histogram_pg.histogram.sample_time_ns         = 1024
```

{{< /tab >}}
{{< tab "Latency Histogram Examples ">}}

The following example configures the latency histogram and sets the minimum boundary size to 960 and the histogram size to 12288. These settings apply to interfaces that have the `latency` histogram enabled and do not have different values configured for these settings at the interface level:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/monitor.conf
...
monitor.port_group_list                               = [latency_pg] 
monitor.histogram_pg.port_set                         = allports
monitor.histogram_pg.stat_type                        = histogram_latency
monitor.histogram_pg.cos_list                         = [0-15]
monitor.histogram_pg.trigger_type                     = timer
monitor.histogram_pg.timer                            = 1s
...
monitor.histogram_pg.histogram.minimum_bytes_boundary = 960
monitor.histogram_pg.histogram.histogram_size_bytes   = 12288
```

The following example enables the latency histogram for traffic class 0 on swp1 through swp8 with the globally applied minimum boundary and histogram size. The example also enables the latency histogram for traffic class 1 on swp9 through swp16 and sets the minimum boundary to 768 bytes and the histogram size to 9600 bytes.

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/monitor.conf
...
monitor.port_group_list                                = [histogram_gr1, histogram_gr2] 
monitor.histogram_gr1.port_set                         = swp1-swp8
monitor.histogram_gr1.stat_type                        = histogram_latency
monitor.histogram_gr1.cos_list                         = [0]
monitor.histogram_gr1.trigger_type                     = timer
monitor.histogram_gr1.timer                            = 1s
...
monitor.histogram_gr1.histogram.minimum_bytes_boundary = 960
monitor.histogram_gr1.histogram.histogram_size_bytes   = 12288

monitor.histogram_gr2.port_set                         = swp9-swp16
monitor.histogram_gr2.stat_type                        = histogram_latency
monitor.histogram_gr2.cos_list                         = [1]
monitor.histogram_gr2.trigger_type                     = timer
monitor.histogram_gr2.timer                            = 1s
...
monitor.histogram_gr2.histogram.minimum_bytes_boundary = 960
monitor.histogram_gr2.histogram.histogram_size_bytes   = 12288
```

{{< /tab >}}
{{< tab "Packet Drops Due to Errors Example ">}}

In the following example:
- Packet drops on swp1 through swp50 collect every two seconds.
- If the number of packet drops is greater than 100, the results write to the `/var/lib/cumulus/discard_stats` snapshot file and the system sends a message to the `/var/log/syslog` file.

```
monitor.port_group_list                            = [discards_pg]
monitor.discards_pg.port_set                       = swp1-swp50
monitor.discards_pg.stat_type                      = packet
monitor.discards_pg.action_list                    = [snapshot,log]
monitor.discards_pg.trigger_type                   = timer
monitor.discards_pg.timer                          = 2s
monitor.discards_pg.log.packet_error_drops         = 100
monitor.discards_pg.snapshot.packet_error_drops    = 100
monitor.discards_pg.snapshot.file                  = /var/lib/cumulus/discard_stats
monitor.discards_pg.snapshot.file_count            = 16
```

{{< /tab >}}
{{< tab "Collect Actions ">}}

A collect action triggers the collection of additional information. You can daisy chain multiple monitors (port groups) into a single collect action.

In the following example:
- Queue length histograms collect for swp1 through swp50 every second.
- The results write to the `/var/run/cumulus/histogram_stats` snapshot file.
- When the queue length reaches 500 bytes, the system sends a message to the /var/log/syslog file and collects additional data; buffer occupancy and all packets per port.
- Buffer occupancy data writes to the `/var/lib/cumulus/buffer_stats` snapshot file and all packets per port data writes to the `/var/lib/cumulus/all_packet_stats` snapshot file.
- In addition, packet drops on swp1 through swp50 collect every two seconds. If the number of packet drops is greater than 100, the monitor writes the results to the `/var/lib/cumulus/discard_stats` snapshot file and sends a message to the `/var/log/syslog` file.

```
monitor.port_group_list                               = [histogram_pg,discards_pg]

monitor.histogram_pg.port_set                         = swp1-swp50
monitor.histogram_pg.stat_type                        = buffer
monitor.histogram_pg.cos_list                         = [0]
monitor.histogram_pg.trigger_type                     = timer
monitor.histogram_pg.timer                            = 1s
monitor.histogram_pg.action_list                      = [snapshot,collect,log]
monitor.histogram_pg.snapshot.file                    = /var/run/cumulus/histogram_stats
monitor.histogram_pg.snapshot.file_count              = 64
monitor.histogram_pg.histogram.minimum_bytes_boundary = 960
monitor.histogram_pg.histogram.histogram_size_bytes   = 12288
monitor.histogram_pg.histogram.sample_time_ns         = 1024
monitor.histogram_pg.log.queue_bytes                  = 500
monitor.histogram_pg.collect.queue_bytes              = 500
monitor.histogram_pg.collect.port_group_list          = [buffers_pg,all_packet_pg]

monitor.buffers_pg.port_set                           = swp1-swp50
monitor.buffers_pg.stat_type                          = buffer
monitor.buffers_pg.action_list                        = [snapshot]
monitor.buffers_pg.snapshot.file                      = /var/lib/cumulus/buffer_stats
monitor.buffers_pg.snapshot.file_count                = 8

monitor.all_packet_pg.port_set                        = swp1-swp50
monitor.all_packet_pg.stat_type                       = packet_all
monitor.all_packet_pg.action_list                     = [snapshot]
monitor.all_packet_pg.snapshot.file                   = /var/lib/cumulus/all_packet_stats
monitor.all_packet_pg.snapshot.file_count             = 8

monitor.discards_pg.port_set                          = swp1-swp50
monitor.discards_pg.stat_type                         = packet
monitor.discards_pg.action_list                       = [snapshot,log]
monitor.discards_pg.trigger_type                      = timer
monitor.discards_pg.timer                             = 2s
monitor.discards_pg.log.packet_error_drops            = 100
monitor.discards_pg.snapshot.packet_error_drops       = 100
monitor.discards_pg.snapshot.file                     = /var/lib/cumulus/discard_stats
monitor.discards_pg.snapshot.file_count               = 16
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Bandwidth Gauge

{{%notice note%}}
Cumulus Linux supports the bandwidth gauge option on the Spectrum-4 switch only.
{{%/notice%}}

To track bandwidth usage for an interface, you can enable the bandwidth gauge option with the `nv set interface <interface-id> telemetry bw-gauge enable on` command:

```
cumulus@switch:~$ nv set interface swp1 telemetry bw-gauge enable on
cumulus@switch:~$ nv config apply
```

To disable the bandwidth gauge setting, run the `nv set interface <interface-id> telemetry bw-gauge enable off` command.

To show the bandwidth gauge setting for an interface, run the `nv show interface <interface> telemetry bw-gauge ` command:

```
cumulus@switch:~$ nv show interface swp1 telemetry bw-gauge
        operational  applied
------  -----------  -------
enable  on           on
```

To show a summary of the bandwidth for an interface, run the `nv show system telemetry bw-gauge interface` command:

```
cumulus@switch:~$ nv show system telemetry bw-gauge interface
Interface  Tx (Mbps)  Rx (Mbps)
---------  ---------  ---------
swp1       4          4
```

### Snapshots
<!-- vale off -->
To create a snapshot:
- Set how often to write to a snapshot file. The default value is 1 second.
- Provide the snapshot file name and location. The default location and file name is `/var/run/cumulus/histogram_stats`.
- Configure the number of snapshots to create before Cumulus Linux overwrites the first snapshot file. For example, if you set the snapshot file count to 30, the first snapshot file is `histogram_stats_0` and the 30th snapshot is `histogram_stats_30`. After the 30th snapshot, Cumulus Linux overwrites the original snapshot file (`histogram_stats_0`) and the sequence restarts. The default value is 64.
<!-- vale on -->
{{%notice note%}}
Snapshots provide you with more data; however, they can occupy a lot of disk space on the switch. To reduce disk usage, you can use a volatile partition for the snapshot files; for example, `/var/run/cumulus/histogram_stats`.
{{%/notice%}}

The following example creates the `/var/run/cumulus/histogram_stats` snapshot every 5 seconds. The number of snapshots that you can create before the first snapshot file is overwritten is set to 30.

{{< tabs "TabID171 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system telemetry snapshot-file name /var/run/cumulus/histogram_stats
cumulus@switch:~$ nv set system telemetry snapshot-file count 30
cumulus@switch:~$ nv set system telemetry snapshot-interval 5
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `snapshot.file` settings in the `/etc/cumulus/datapath/monitor.conf` file, then restart the `asic-monitor` service with the `systemctl restart asic-monitor.service` command. The `asic-monitor` service reads the new configuration file and then runs until you stop the service with the `systemctl stop asic-monitor.service` command.
<!-- vale off -->
| Setting| Description|
|------- |----------- |
| `<port_group_name>.action_list` | Specifies one or more actions that occur when data collects:<br>`snapshot` writes a snapshot of the data collection results to a file. If you specify this action, you must also specify a snapshot file (described below). You can also specify a threshold that initiates the snapshot action.<br><br>Example:<pre>monitor.histogram_pg.action_list = [snapshot]</pre>`collect` gathers additional data. If you specify this action, you must also specify the port groups for the additional data you want to collect.<br><br>Example:<pre>monitor.histogram_pg.action_list = [collect<br>monitor.histogram_pg.collect.port_group_list = [buffers_pg,all_packet_pg]</pre>`log` sends a message to the `/var/log/syslog` file. If you specify this action, you must also specify a threshold that initiates the log action.<br>Example:<pre>monitor.histogram_pg.action_list = [log]<br>monitor.histogram_pg.log.queue_bytes = 500</pre>You can use all three of these actions in one monitoring step. For example<pre>monitor.histogram_pg.action_list = [snapshot,collect,log]</pre> **Note**: If an action appears in the action list but does not have the required settings (such as a threshold for the log action), the ASIC monitor stops and reports an error. |
| `<port_group_name>.snapshot.file` | Specifies the name for the snapshot file. All snapshots use this name, with a sequential number appended to it. See the `snapshot.file_count` setting.<br><br>Example:<pre>monitor.histogram_pg.snapshot.file = /var/run/cumulus/histogram_stats</pre> |
| `<port_group_name>.snapshot.file_count` | Specifies the number of snapshots you can create before Cumulus Linux overwrites the first snapshot file. In the following example, because the snapshot file count is set to 64, the first snapshot file is `histogram_stats_0` and the 64th snapshot is `histogram_stats_63`. After the 65th snapshot, Cumulus Linux overwrites the original snapshot file (histogram_stats_0) and the sequence restarts.<br><br>Example:<pre>monitor.histogram_pg.snapshot.file_count = 64</pre>**Note**: While more snapshots provide you with more data, they can occupy a lot of disk space on the switch. |
<!-- vale on -->
{{< /tab >}}
{{< /tabs >}}

- To show an ingress queue snapshot, run the `nv show interface <interface> telemetry histogram ingress-buffer priority-group <value> snapshot` command
- To show an egress queue snapshot, run the `nv show interface <interface> telemetry histogram egress-buffer traffic-class <type> snapshot`
- To show a counter snapshot, run the `nv show interface <interface> telemetry histogram counter counter-type <type> snapshot`
- To show a latency snapshot, run the `nv show interface <interface> telemetry histogram latency traffic-class <type> snapshot`

The following example shows an ingress queue snapshot:

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram ingress-buffer priority-group 0 snapshot
Sl.No  Date-Time            Bin-0   Bin-1    Bin-2    Bin-3    Bin-4    Bin-5    Bin-6    Bin-7     Bin-8     Bin-9
-----  -------------------  ------  -------  -------  -------  -------  -------  -------  --------  --------  ---------
0      -                    (<864)  (<2304)  (<3744)  (<5184)  (<6624)  (<8064)  (<9504)  (<10944)  (<12384)  (>=12384)
1      2023-12-13 11:02:44  980318  0        0        0        0        0        0        0         0         0
2      2023-12-13 11:02:43  980318  0        0        0        0        0        0        0         0         0
3      2023-12-13 11:02:42  980318  0        0        0        0        0        0        0         0         0
4      2023-12-13 11:02:41  980318  0        0        0        0        0        0        0         0         0
5      2023-12-13 11:02:40  980488  0        0        0        0        0        0        0         0         0
6      2023-12-13 11:02:39  980149  0        0        0        0        0        0        0         0         0
7      2023-12-13 11:02:38  979809  0        0        0        0        0        0        0         0         0
8      2023-12-13 11:02:37  980488  0        0        0        0        0        0        0         0         0
9      2023-12-13 11:02:36  980318  0        0        0        0        0        0        0         0         0
```

{{%notice note%}}
Parsing the snapshot file and finding the information you need can be tedious; use a third-party analysis tool to analyze the data in the file.
{{%/notice%}}

### Log files

In addition to snapshots, you can configure the switch to send log messages to the `/var/log/syslog` file when the queue length reaches a specified number of bytes, the number of counters reach a specified value, or the latency reaches a specific number of nanoseconds.

{{< tabs "TabID293 ">}}
{{< tab "NVUE Commands ">}}

The following example sends a message to the `/var/log/syslog` file after the ingress queue length for priority group 1 on swp9 through swp16 reaches 5000 bytes:

```
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram ingress-buffer priority-group 1 threshold action log
cumulus@switch:~$ nv set interface swp9-16 telemetry histogram ingress-buffer priority-group 1 threshold value 5000
cumulus@switch:~$ nv config apply
```

The following example sends a message to the `/var/log/syslog` file after the number of received packets on swp1 through swp8 reaches 500:

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram counter counter-type rx-packet threshold log
cumulus@switch:~$ nnv set interface swp1-8 telemetry histogram counter counter-type rx-packet threshold value 500
cumulus@switch:~$ nv config apply
```

The following example sends a message to the `/var/log/syslog` file after packet latency for traffic class 0 on swp1 through swp8 reaches 500 nanoseconds:

```
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram latency traffic-class 0 threshold action log
cumulus@switch:~$ nv set interface swp1-8 telemetry histogram latency traffic-class 0 threshold value 500
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Set the log options in the `/etc/cumulus/datapath/monitor.conf` file, then restart the `asic-monitor` service with the `systemctl restart asic-monitor.service` command. The `asic-monitor` service reads the new configuration file and then runs until you stop the service with the `systemctl stop asic-monitor.service` command.

| Setting| Description|
|------- |----------- |
| `<port_group_name>.log.action_list` | Set this option to `log` to create a log message when the queue length or counter number reaches the threshold set. |
| `<port_group_name>.log.queue_bytes` | Specifies the length of the queue in bytes after which the switch sends a log message. |
| `<port_group_name>.log.count` | Specifies the number of counters to reach after which the switch sends a log message. |
| `<port_group_name>.log.value` | Specifies the number of latency nanoseconds to reach after which the switch sends a log message. |

The following example sends a message to the `/var/log/syslog` file after the ingress queue length reaches 5000 bytes:

```
...
monitor.histogram_pg.action_list  = [log]
...
monitor.histogram_pg.log.queue_bytes  = 5000
```

The following example sends a message to the `/var/log/syslog` file after the number of packets reaches 500:

```
...
monitor.histogram_pg.action_list  = [log]
...
monitor.histogram_pg.log.count  = 500
```

The following example sends a message to the `/var/log/syslog` file after packet latency reaches 500 nanoseconds:

```
...
monitor.histogram_pg.action_list  = [log]
...
monitor.histogram_pg.log.value  = 500
```

{{< /tab >}}
{{< /tabs >}}

The following shows an example syslog message:

```
2018-02-26T20:14:41.560840+00:00 cumulus asic-monitor-module INFO:  2018-02-26 20:14:41.559967: Egress queue(s) greater than 500 bytes in monitor port group histogram_pg.
```

{{%notice note%}}
When collecting data, the switch uses both the CPU and SDK process, which can affect `switchd`. Snapshots and logs can occupy a lot of disk space if you do not limit their number.
{{%/notice%}}

### Show Histogram Information

To show a list of the interfaces with enabled histograms, run the `nv show system telemetry histogram interface` command:

```
cumulus@switch:~$ nv show system telemetry histogram interface
Interface         ingress-buffer          egress-buffer            counter 
--------------------------------------------------------------------------------------- 
swp1              0,1,2                   -                        tx-byte,rx-byte 
swp2              -                       0,1,8                    tx-byte,tx-byte
```

To show the egress queue depth histogram samples collected at the configured interval for a traffic class for a port, run the `nv show interface <interface> telemetry histogram egress-buffer traffic-class <traffic-class>` command.

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram egress-buffer traffic-class 0
Time         0-863     864:2303    2304:3743.  3744:5183   5184:6623   6624:8063   8064:9503 9. 504:10943   10944:12383 
12384:* 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
08:56:19     978065        0           0           0          0            0           0             0          0
08:56:20     978532        0           0           0          0            0           0             0          0 
```

To show the ingress queue depth histogram samples collected at the configured interval for a priority group for a port, run the `nv show interface <interface> telemetry histogram ingress-buffer priority-group <priority-group>` command.

```
cumulus@switch:~$ nv show interface swp1 telemetry histogram ingress-buffer priority-group 0
Time      0-863     864:2303    2304:3743  3744:5183   5184:6623   6624:8063   8064:9503 9. 504:10943   10944:12383 
12384:* 
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
08:56:19  978065        0          0           0           0            0           0           0             0
08:56:20  978532        0          0           0           0            0           0           0             0
```

## High Frequency Telemetry

High frequency telemetry enables you to collect counters at very short sampling intervals (single digit milliseconds to microseconds), which is useful for <span class="a-tooltip">[AI](## "Artifical Intelligence")</span> training. The data can help you detect short duration events like microbursts, and provides information about where in time the events happen and for how long.

High frequency telemetry data provides time series data that traditional histograms cannot provide. The time series data helps you understand the shape of the traffic pattern and identify any spikes or dips, or jitter in the traffic.

{{%notice note%}}
- Cumulus Linux supports high frequency telemetry on Spectrum-4 switches.
- To correlate counters from different switches for debugging and profiling, the switches must have the same time (the switch adds timestamps in the metadata of the counters it collects). You can use either NTP or PTP. NVIDIA recommends using PTP because the timestamp is accurate among the switches in the fabric at the microsecond level.
{{%/notice%}}

You can export the collected data automatically to a configured influxDB service or export a `json` file with the collected data to an external location. You can then process the data, plot it into a time-series graph and see how the network behaves with high precision.

{{%notice note%}}
This collected data is available on the switch until you trigger the next data collection session or until you reboot the switch.
{{%/notice%}}

Cumulus Linux provides several options to configure high frequency telemetry; you can run NVUE commands (the preferred configuration method), use the Cumulus Linux job management tool (`cl-hft-tool`), or edit flat files. Using the `cl-hft-tool` command tool is a simplified way to perform Linux configuration; editing flat files provides more complexity. To show all the `cl-hft-tool` command options, run `cl-hft-tool help`.

To configure high frequency telemetry:
1. Enable telemetry with the `nv set system telemetry enable on` command.
2. Configure data collection.
3. Configure data export.
4. Configure the schedule.

### Configure Data Collection

High frequency telemetry uses profiles to configure data collection. A profile is a set of configurations. The default profile is `standard`. You can create a maximum of four new profiles (four profiles in addition to the default profile).

{{%notice note%}}
You cannot delete or modify a profile if sessions are already running or scheduled.
{{%/notice%}}

To configure data collection:
- Set the sampling interval in microseconds. You can specify a value between 100 and 12750. The value must be a multiple of 50. The default value is 5000 microseconds (30 seconds).
- Set the egress queue priorities (traffic class 0-15).
- Specify the type of data you want to collect (transferred bytes, received bytes, and traffic class occupancy). 

{{%notice note%}}
Use commas (no spaces) to separate the list of counter types you want to collect and the list of traffic classes. For example, to collect all counter types, specify `tx-byte,rx-byte,tc-occupancy`. To set traffic class 1, 3, and 6, specify `1,3,6`.
{{%/notice%}}

{{< tabs "TabID26 ">}}
{{< tab "NVUE Commands ">}}

The following example configures `profile1` and sets the sampling interval to 1000, the traffic class to 0, 3, and 7, and the type of data to collect to traffic class occupancy (`tc-occupancy`):

```
cumulus@switch:~$ nv set system telemetry hft profile profile1 sample-interval 1000
cumulus@switch:~$ nv set system telemetry hft profile profile1 traffic-class 0,3,7 
cumulus@switch:~$ nv set system telemetry hft profile profile1 counter tc-occupancy
cumulus@switch:~$ nv config apply
```

The following example configures `profile2` and sets the sampling interval to 1000, the traffic class to 1-9, and the type of data to collect to received bytes (`rx-byte`):

```
cumulus@switch:~$ nv set system telemetry hft profile profile1 sample-interval 1000
cumulus@switch:~$ nv set system telemetry hft profile profile1 traffic-class 0-9 
cumulus@switch:~$ nv set system telemetry hft profile profile1 counter rx-byte
cumulus@switch:~$ nv config apply
```

To delete a profile, run the `nv unset system telemetry hft profile <profile-id>` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "750 ">}}
{{< tab "Job Management Tool ">}}

The following example configures `profile1` and sets the sampling interval to 1000, the traffic class to 0, 3, and 7, and the type of data to collect to transferred bytes (`tx-byte`) and traffic class occupancy (`tc-occupancy`):

```
cumulus@switch:~$ cl-hft-tool profile-add --profile profile1 --counter tx-byte, tc-occupancy --tc 0-3,7 --interval 1000 
```

The following example configures `profile2` and sets the sampling interval to 1000, the traffic class to 1-9, and the type of data to collect to received bytes (`rx-byte`):

```
cumulus@switch:~$ cl-hft-tool profile-add --profile profile2 --counter rx-byte --tc 1-9 --interval 1000 
```

To delete a profile, run the `cl-hft-tool profile-delete --profile <profile>` command:

```
cumulus@switch:~$ cl-hft-tool profile-delete --profile profile1 
```

To delete all profiles, run the `cl-hft-tool profile-delete --profile all` command.

{{< /tab >}}
{{< tab "File Configuration ">}}

Edit the `/etc/cumulus/telemetry/hft/hft_profile.conf` file to configure the following parameters.

| Parameter | Description |
| --------- | ----------- |
| `hft.profile_list` | The name of the profile. |
| `hft.standard.counters_list` | The type of data you want to collect, which can be transferred bytes (`if_out_octets`), received bytes (`if_in_octets`), and, or traffic class occupancy (`tc_curr_occupancy`). |
| `hft.standard.sample_interval` | The sampling interval in microseconds. You can specify a value between 100 and 65535. The value must be a multiple of 50. The default value is 5000 microseconds.|
| `hft.standard.tc_list` | The list of egress queue priorities (traffic classes) per port on which you want to collect data. |

The following example configures `profile1` and sets the sampling interval to 1000, the traffic class to 0, 3, and 7, and the list of counters to `if_out_octets` and `tc_curr_occupancy`:

```
cumulus@switch:~$ sudo nano /etc/cumulus/telemetry/hft/hft_profile.conf
hft.profile_list = [profile1]
hft.standard.counters_list = [if_out_octets, tc_curr_occupancy]
hft.standard.sample_interval = [1000]
hft.standard.tc_list = [0,3,7]
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Configure Data Export

You can either:
- Export the data automatically to a configured influxDB service.
- Save the collected data locally to a `json` file in the `/var/run/cumulus/hft` directory, then export the `json` file to an external location with NVUE commands (or the API).

{{%notice note%}}
The collected data is available on the switch until you trigger the next data collection or until you reboot the switch.
{{%/notice%}}

{{< tabs "TabID56 ">}}
{{< tab "NVUE Commands ">}}

To save the collected data locally to a `json` file, run the `nv set system telemetry hft target local` command:

```
cumulus@switch:~$ nv set system telemetry hft target local
cumulus@switch:~$ nv config apply
```

The `json` format file includes the counter data for each sampling interval and a timestamp showing when the data was collected.
  
{{< expand "example json file" >}}
```
  { 
    "hostname":  "leaf01"
    "0": {
        "sample_index": 1, 
        "metadata": { 
            "sec": 1715957858, 
            "nsec": 714503118 
        }, 
        "port_data": { 
            "swp1": { 
                "if_out_octets": 0, 
                "if_in_octets": 0, 
                "tc_data": { 
                    "0": { 
                        "tc_curr_occupancy": 0 
                    }, 
                    "1": { 
                        "tc_curr_occupancy": 0 
                    }, 
                    "2": { 
                        "tc_curr_occupancy": 0 
                    }, 
                    "3": { 
                        "tc_curr_occupancy": 0 
                    }, 
                    "4": { 
                        "tc_curr_occupancy": 0 
                    }, 
                    "5": { 
                        "tc_curr_occupancy": 0 
                    }, 
                    "6": { 
                        "tc_curr_occupancy": 0 
                    }, 
                    "7": { 
                        "tc_curr_occupancy": 0 
                    } 
                } 
            } 
        } 
    }
}
```
{{< /expand >}}

You can export the file to an external location with the NVUE `nv action upload system telemetry hft job <hft-job-id> <remote-url>` command. To see the list of jobs, run the `nv show system telemetry hft job` command (see {{<link url="#show-high-frequency-telemetry-session-information" text="Show High Frequency Telemetry Session Information">}} below).

```
cumulus@switch:~$ nv action upload system telemetry hft job 1 scp://user1:user1-password@host1:~/ 
```

To export the data to influxDB, configure the following settings:
- The IP address and TCP port of the influxDB host. The default port is 8086.
- The influxDB bucket name where you want to insert the data.
- The InfluxDB organization name in which the bucket is located.
- The authentication token that ensures secure interaction between InfluxDB and Cumulus Linux.

{{%notice note%}}
NVUE takes the authentication token in plain text; however, the show commands do not show the token in plain text.
{{%/notice%}}

The following example configures the influxDB host IP address to 10.10.1.1, the TCP port to 12345, the bucket to `hft-data`, the organization to `nvidia` and authentication token to `token1`:

``` 
cumulus@switch:~$ nv set system telemetry hft target influxdb host 10.10.1.1 
cumulus@switch:~$ nv set system telemetry hft target influxdb port 12345 
cumulus@switch:~$ nv set system telemetry hft target influxdb bucket hft-data 
cumulus@switch:~$ nv set system telemetry hft target influxdb org nvidia 
cumulus@switch:~$ nv set system telemetry hft target influxdb token token1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "886 ">}}
{{< tab "Job Management Tool ">}}

The following example saves the collected data locally to a `json` file:

```
cumulus@switch:~$ cl-hft-tool target-add --target local
```

The following example configures the influxDB host IP address to 10.10.1.1, the TCP port to 12345, the bucket to `hft-data`, the organization to `nvidia` and authentication token to `token1` (the job management tool encrypts the token):

```
cumulus@switch:~$ cl-hft-tool  target-add --target influxdb –host “10.10.1.1” –port 12345 –bucket hft-data –org nvidia –token "*****"
```

To delete a target, run the `cl-hft-tool target-delete --target <target>` command, where target is either `local` or `influxdb`:

```
cumulus@switch:~$ cl-hft-tool target-delete --target influxdb 
```

{{< /tab >}}
{{< tab "File Configuration ">}}

Edit the `/etc/cumulus/telemetry/hft/hft_profile.conf` file to configure the following parameters.

| Parameter | Description |
| --------- | ----------- |
| `hft.target` | The external location where you want to export the collected data. Specify `local` save the collected data locally to a `json` file or `influxdb` to export the collected data to influxDB.|
| `hft.influxdb.host` | The IP address of the influxDB host. |
| `hft.influxdb.port` | The TCP port of the influxDB host. The default port is 8086. |
| `hft.influxdb.bucket` | The influxDB bucket name where you want to insert the data. |
| `hft.influxdb.org` | The InfluxDB organization name in which the bucket is located.
| `hft.influxdb.token` | The authentication token that ensures secure interaction between InfluxDB and Cumulus Linux. |

The following example saves the collected data locally to a `json` file:

```
cumulus@switch:~$ sudo nano /etc/cumulus/telemetry/hft/hft_profile.conf
hft.target = [local]
```

The following example configures the influxDB host IP address to 10.10.1.1, the TCP port to 12345, the bucket to `hft-data`, the organization to `nvidia` and authentication token to `token1`:

```
cumulus@switch:~$ sudo nano /etc/cumulus/telemetry/hft/hft_profile.conf
hft.target = [influxdb]
hft.influxdb.host = 10.10.1.1 
hft.influxdb.port = 12345
hft.influxdb.bucket = hft-data
hft.influxdb.org = nvidia
hft.influxdb.token =token1
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Configure the Schedule

To configure the schedule for a data collection profile, set:
- The start date and time.
- The session duration in seconds. The default value is 20 seconds.
- The ports on which you want to collect the data. You can specify a range of ports, multiple comma separated ranges of ports, or `all` for all the ports. The default value is `all`.

You can schedule a maximum of 25 sessions (jobs). The switch can retain data for 25 jobs (completed, cancelled, or failed) in addition to the active jobs.  

{{< tabs "TabID79 ">}}
{{< tab "NVUE Commands ">}}

The following example configures `profile1` to start on 2024-01-21 at 10:00:00, last 30 seconds, collect data on swp1 through swp9.

Specify the date and time in `YYYY-MM-DD HH:MM:SS` format.

``` 
cumulus@switch:~$ nv action schedule system telemetry hft job 2024-07-16 10:00:00 duration 30 profile profile1 ports swp1-swp9
```

You can provide a short reason why you are collecting the data (in quotes). A short description is optional.

``` 
cumulus@switch:~$ nv action schedule system telemetry hft job 2024-07-16 13:06:00 duration 30 profile profile1 ports swp1-swp9 description "bandwidth profiling"
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "803 ">}}
{{< tab "Job Management Tool ">}}

The following example configures `profile1` to start on 21-01-2024 at 10:00:00, last 30 seconds, collect data on swp1 through swp9.

Specify the date and time in `DD-MM-YYY-HH:MM:SS` format.

```
cumulus@switch:~$ cl-hft-tool job-schedule --time 21-01-2024-10:00:00 --duration 30 --profile profile1 --ports swp1-swp9  
```

{{< /tab >}}
{{< tab "File Configuration ">}}

Edit the `/etc/cumulus/telemetry/hft/hft_job.conf` file to configure the following parameters.

| Parameter | Description |
| --------- | ----------- |
| `hft.action_type` | The action type. `schedule` starts a new data collection session (job). |
| `hft.schedule.start_time` | The job start date and time in `YYYY-MM-DD HH:MM:SS` format. |
| `hft.schedule.duration` | The job duration in seconds. The default value is 20 seconds. |
| `hft.schedule.port_set` | The ports on which you want to collect the data. You can specify a range of ports, multiple comma separated ranges of ports, or `all` for all the ports. The default value is `all`.|
| `hft.schedule.profile_name` | The profile for this job. |
| `hft.schedule.description`| A short reason why you are collecting the data. |

The following example configures `profile1` to start on 2024-01-01 at 10:00:00, last 30 seconds, collect the data on swp1 through swp9 and add the session description `bandwidth profiling`.

```
cumulus@switch:~$  sudo nano /etc/cumulus/telemetry/hft/hft.conf
hft.action_type = schedule
hft.schedule.start_time =  2024-01-01 10:00:00
hft.schedule.duration = 30
hft.schedule.port_set = swp1-swp9
hft.schedule.profile_name = profile1
hft.schedule.description = Bandwidth profiling 
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Cancel Data Collection

You can cancel a specific or all data collection jobs, or a specific or all jobs for a profile.

{{< tabs "TabID102 ">}}
{{< tab "NVUE Commands ">}}

To cancel a scheduled telemetry job, run the `nv action cancel system telemetry hft job <job-id> profile <profile-id>` command.

The following example cancels all jobs for profile `profile1`:

```
cumulus@switch:~$ nv action cancel system telemetry hft job all profile profile1
Action executing ...
Action succeeded
```

The following example cancels job ID 6:

```
cumulus@switch:~$ nv action cancel system telemetry hft job 6
Action executing ...
Action succeeded
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "852 ">}}
{{< tab "Job Management Tool ">}}

To cancel a scheduled telemetry job, run the `cl-hft-tool  job-cancel --job <job-id>` command.

The following example cancels job 6:

```
cumulus@switch:~$ cl-hft-tool  job-cancel --job 6
```

To cancel all jobs, run the `cl-hft-tool  job-cancel --job all` command.

{{< /tab >}}
{{< tab "File Configuration ">}}

Edit the `/etc/cumulus/telemetry/hft/hft.conf` file to configure the following parameters.

| Parameter | Description |
| --------- | ----------- |
| `hft.action_type`| Specify the action type `cancel` to stop a scheduled job.  |
| `hft.cancel.job_id` | The ID of job you want to cancel. Every scheduled session has a unique job ID. |

The following example cancels job ID 6 for profile `profile1`:

```
cumulus@switch:~$  sudo nano /etc/cumulus/telemetry/hft/hft.conf
hft.action_type = schedule
hft.schedule.start_time =  2024-01-01 10:00:00
hft.schedule.duration = 30
hft.schedule.port_set = swp1-swp9
hft.schedule.profile_name = profile1
hft.schedule.description = Bandwidth profiling

hft.action_type cancel
hft.cancel.job_id = 6
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### Show Session Information

To show high frequency telemetry configuration:

```
cumulus@switch:~$ nv show system telemetry hft
profile
==========
    Profile   sample-interval  Summary              
    --------  ---------------  ---------------------
    profile1  1000             counter:      rx-byte
                               counter: tc-occupancy
                               traffic-class:      0
                               traffic-class:      3
                               traffic-class:      7
                               traffic-class:      1
                               traffic-class:      2
                               traffic-class:      4
                               traffic-class:      5
                               traffic-class:      6
                               traffic-class:      8
                               traffic-class:      9
    standard  5000             counter:      tx-byte
                               counter:      rx-byte
                               counter: tc-occupancy
                               traffic-class:      3
...
```

To show information for all data collection jobs, such as the start time, duration, status and ports on which the data is collected:

```
cumulus@switch:~$ nv show system telemetry hft job
Job Id      Start Time               Duration(s)        Profile     Ports    Status  

---------   --------------           ------------       ---------   -------   ---------  

1           10-05-2024 09:00:00      20                 standard    all       complete 
2           12-05-2024 09:00:00      20                 standard    all       complete 
3           15-05-2024 09:00:00      20                 standard    all       complete 
4           16-05-2024 09:00:00      20                 standard    all       complete 
5           17-05-2024 09:00:00      20                 standard    all       complete 
6           19-05-2024 09:00:00      20                 standard    all       complete 
7           19-05-2024 12:00:00      20                 standard    all       running 
8           20-05-2024 09:00:00      20                 standard    all       pending
```

To show the currently running data collection job:

```
cumulus@switch:~$ nv show system telemetry hft job –filter “status=running” 
Job Id     Start Time              Duration(s)        Profile     Ports    Status  
---------  --------------          ------------       ---------   -------  ---------  
7          19-05-2024 12:00:00     20                 standard    all      running
```

To show information about a specific data collection job:

```
cumulus@switch:~$ nv show system telemetry hft job 1 
                       operational
---------------------  ----------------- 
start-time             01-01-2024 12:00:00 
duration               20 
traffic-class          3 
counter                tx-byte,rx-byte,tc-occupancy 
sample-interval        5000 
ports                  swp1-swp64 
status                 pending 
target                 scp://abc@server1:/hft-data
```
