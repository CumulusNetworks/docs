---
title: Configure and Monitor What Just Happened
author: Cumulus Networks
weight: 810
toc: 4
---
The *What Just Happened* (WJH) feature, available on Mellanox switches, streams detailed and contextual telemetry data for analysis. This provides real-time visibility into problems in the network, such as hardware packet drops due to buffer congestion, incorrect routing, and ACL or layer 1 problems. You must have Cumulus Linux 4.0.0 or later and NetQ 2.4.0 or later to take advantage of this feature.

For a list of supported WJH events, refer to the {{<link title="WJH Event Messages Reference">}}.

{{<notice tip>}}

If your switches are sourced from a vendor other than Mellanox, this view is blank as no data is collected.

{{</notice>}}

When WJH capabilities are combined with NetQ, you have the ability to hone in on losses, anywhere in the fabric, from a single management console. You can:

- View any current or historic drop information, including the reason for the drop
- Identify problematic flows or endpoints, and pin-point exactly where communication is failing in the network

{{<notice info>}}

By default, Cumulus Linux 4.0.0 provides the NetQ 2.3.1 Agent and CLI. If you installed Cumulus Linux 4.0.0 on your Mellanox switch, you need to upgrade the NetQ Agent and optionally the CLI to release 2.4.0 or later (preferably the latest release).

<pre>
cumulus@<hostname>:~$ sudo apt-get update
cumulus@<hostname>:~$ sudo apt-get install -y netq-agent
cumulus@<hostname>:~$ sudo netq config restart agent
cumulus@<hostname>:~$ sudo apt-get install -y netq-apps
cumulus@<hostname>:~$ sudo netq config restart cli
</pre>

{{</notice>}}

## Configure the WJH Feature

WJH is enabled by default on Mellanox switches and no configuration is required in Cumulus Linux 4.0.0; however, you must enable the NetQ Agent to collect the data in NetQ 2.4.0 or later.

To enable WJH in NetQ:

1. Configure the NetQ Agent on the Mellanox switch.

    ```
    cumulus@switch:~$ sudo netq config add agent wjh
    ```

2. Restart the NetQ Agent to start collecting the WJH data.

    ```
    cumulus@switch:~$ sudo netq config restart agent
    ```

When you are finished viewing the WJH metrics, you might want to stop the NetQ Agent from collecting WJH data to reduce network traffic. Use `netq config del agent wjh` followed by `netq config restart agent` to disable the WJH feature on the given switch.

{{<notice note>}}

Using <em>wjh_dump.py</em> on a Mellanox platform that is running Cumulus Linux 4.0 and the NetQ 2.4.0 agent causes the NetQ WJH client to stop receiving packet drop call backs. To prevent this issue, run <em>wjh_dump.py</em> on a different system than the one where the NetQ Agent has WJH enabled, or disable <em>wjh_dump.py</em> and restart the NetQ Agent (run <code>netq config restart agent</code>).

{{</notice>}}

## Configure Latency and Congestion Thresholds

WJH latency and congestion metrics depend on threshold settings to trigger the events. Packet latency is measured as the time spent inside a single system (switch). Congestion is measured as a percentage of buffer occupancy on the switch. When WJH triggers events when the high and low thresholds are crossed.

To configure these thresholds, run:

```
netq config add agent wjh-threshold (latency|congestion) <text-tc-list> <text-port-list> <text-th-hi> <text-th-lo>
```

You can specify multiple traffic classes and multiple ports by separating the classes or ports by a comma (no spaces).

This example creates latency thresholds for Class *3* traffic on port *swp1* where the upper threshold is *10* and the lower threshold is *1*.

```
cumulus@switch:~$ sudo netq config add agent wjh-threshold latency 3 swp1 10 1
```

This example creates congestion thresholds for Class *4* traffic on port *swp1* where the upper threshold is *200* and the lower threshold is *10*.

```
cumulus@switch:~$ sudo netq config add agent wjh-threshold congestion 4 swp1 200 10
```

## View What Just Happened Metrics

You can view the WJH metrics from the NetQ UI or the NetQ CLI.

{{< tabs "TabID88" >}}

{{< tab "NetQ UI" >}}

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} (main menu).

2. Click **What Just Happened** under the **Network** column.

    This view displays events based on conditions detected in the data plane. The most recent 1000 events from the last 24 hours are presented for each drop category.

    {{<figure src="/images/netq/main-menu-ntwk-wjh-l1-240.png" width="700">}}

3. By default the layer 1 drops are shown. Click one of the other drop categories to view those drops for all devices.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

Run one of the following commands:

```
netq [<hostname>] show wjh-drop <text-drop-type> [ingress-port <text-ingress-port>] [severity <text-severity>] [reason <text-reason>] [src-ip <text-src-ip>] [dst-ip <text-dst-ip>] [proto <text-proto>] [src-port <text-src-port>] [dst-port <text-dst-port>] [src-mac <text-src-mac>] [dst-mac <text-dst-mac>] [egress-port <text-egress-port>] [traffic-class <text-traffic-class>] [rule-id-acl <text-rule-id-acl>] [between <text-time> and <text-endtime>] [around <text-time>] [json]
netq [<hostname>] show wjh-drop [ingress-port <text-ingress-port>] [severity <text-severity>] [details] [between <text-time> and <text-endtime>] [around <text-time>] [json]
```

Use the various options to restrict the output accordingly.

This example uses the first form of the command to show drops on switch *leaf03* for the past week.

```
cumulus@switch:~$ netq leaf03 show wjh-drop between now and 7d
Matching wjh records:
Drop type          Aggregate Count
------------------ ------------------------------
L1                 560
Buffer             224
Router             144
L2                 0
ACL                0
Tunnel             0
```

This example uses the second form of the command to show drops on switch *leaf03* for the past week *including* the drop reasons.

```
cumulus@switch:~$ netq leaf03 show wjh-drop details between now and 7d

Matching wjh records:
Drop type          Aggregate Count                Reason
------------------ ------------------------------ ---------------------------------------------
L1                 556                            None
Buffer             196                            WRED
Router             144                            Blackhole route
Buffer             14                             Packet Latency Threshold Crossed
Buffer             14                             Port TC Congestion Threshold
L1                 4                              Oper down
```

This example shows the drops seen at layer 2 across the network.

```
cumulus@mlx-2700-03:mgmt:~$ netq show wjh-drop l2
Matching wjh records:
Hostname          Ingress Port             Reason                                        Agg Count          Src Ip           Dst Ip           Proto  Src Port         Dst Port         Src Mac            Dst Mac            First Timestamp                Last Timestamp
----------------- ------------------------ --------------------------------------------- ------------------ ---------------- ---------------- ------ ---------------- ---------------- ------------------ ------------------ ------------------------------ ----------------------------
mlx-2700-03       swp1s2                   Port loopback filter                          10                 27.0.0.19        27.0.0.22        0      0                0                00:02:00:00:00:73  0c:ff:ff:ff:ff:ff  Mon Dec 16 11:54:15 2019       Mon Dec 16 11:54:15 2019
mlx-2700-03       swp1s2                   Source MAC equals destination MAC             10                 27.0.0.19        27.0.0.22        0      0                0                00:02:00:00:00:73  00:02:00:00:00:73  Mon Dec 16 11:53:17 2019       Mon Dec 16 11:53:17 2019
mlx-2700-03       swp1s2                   Source MAC equals destination MAC             10                 0.0.0.0          0.0.0.0          0      0                0                00:02:00:00:00:73  00:02:00:00:00:73  Mon Dec 16 11:40:44 2019       Mon Dec 16 11:40:44 2019
```

{{< /tab >}}

{{< /tabs >}}
