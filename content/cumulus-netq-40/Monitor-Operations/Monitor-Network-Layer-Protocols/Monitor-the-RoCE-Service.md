---
title: Monitor the RoCE Service
author: NVIDIA
weight: 980
toc: 4
---

*RDMA over Converged Ethernet* ({{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE">}}) provides the ability to write to compute or storage elements using remote direct memory access (RDMA) over an Ethernet network instead of using host CPUs. RoCE relies on congestion control and lossless Ethernet to operate. Cumulus Linux and SONiC both support features that can enable lossless Ethernet for RoCE environments.

RoCE helps you obtain a converged network, where all services run over the Ethernet infrastructure, including Infiniband apps.

You monitor RoCE in your network with the UI and with the following CLI commands:

    netq [<hostname>] show roce-counters [<text-port>] tx | rx [roce | general] [around <text-time>] [json]
    netq [<hostname>] show roce-config [<text-port>] [around <text-time>] [json]
    netq [<hostname>] show roce-counters pool [json]
    netq [<hostname>] show events tca_roce
    netq [<hostname>] show events roceconfig

## View the RoCE Configuration

To view the RoCE configuration, run `netq show roce-config`:

```
cumulus@switch:~$ netq show roce-config 

Matching roce records:
Hostname          Interface       RoCE Mode  Enabled TCs  Mode     ECN Max  ECN Min  DSCP->SP   SP->PG   SP->TC   PFC SPs  PFC Rx     PFC Tx     ETS Mode   Last Changed
----------------- --------------- ---------- ------------ -------- -------- -------- ---------- -------- -------- -------- ---------- ---------- ---------- -------------------------
switch            swp34           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp47           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp19           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp37           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp30           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp45           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp57           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp33           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp31           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp39           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp24           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp13           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp53           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp1s1          Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp6            Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp29           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp42           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
switch            swp35           Lossy      0,3          ECN      10432    1088     26 -> 3    3 -> 2   3 -> 3   3        disabled   disabled   dwrr       Thu May 20 22:05:48 2021
...
```

## View RoCE Counters

Various RoCE counters are available for viewing for a given switch, including:

- Rx and Tx counters
- General, CNP and RoCE-specific counters
- Counter pools
- Port-specific counters

You can also go back in time to view counters at a particular point in the past.

### View Rx Counters

You can view RoCE Rx counters in both the UI and CLI.

{{<tabs "View Rx counters">}}

{{<tab "NetQ UI">}}

1. To view Rx counters, open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Switch to the full-screen card, then click **RoCE Counters**.

{{<figure src="/images/netq/roce-rx-counters-fs-4.0.0.png" width="700">}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To view general and CNP Rx counters, run `netq show roce-counters rx general`:

```
cumulus@switch:~$ netq show roce-counters rx general

Matching roce records:
Hostname          Interface            PG packets           PG bytes             no buffer discard    buffer usage         buffer max usage     PG usage             PG max usage
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
switch            swp1s1               1627273              152582910            0                    0                    1                    0                    1
switch            swp1s2               1627273              152582910            0                    0                    1                    0                    1
switch            swp63s1              1618361              160178796            0                    0                    2                    0                    2
switch            swp1s0               1627273              152582910            0                    0                    1                    0                    1
switch            swp63s3              1618361              160178796            0                    0                    2                    0                    2
switch            swp1s3               1627273              152582910            0                    0                    1                    0                    1
switch            swp63s0              1094532              120228456            0                    0                    1                    0                    1
switch            swp63s2              1618361              160178796            0                    0                    2                    0                    2
```

To view RoCE-specific Rx counters, run `netq show roce-counters rx roce`:

```
cumulus@switch:~$ netq show roce-counters rx roce

Matching roce records:
Hostname          Interface       PG packets   PG bytes     no buffer discard  PFC pause packets  PFC pause duration buffer usage buffer max usage   PG usage     PG max usage
----------------- --------------- ------------ ------------ ------------------ ------------------ ------------------ ------------ ------------------ ------------ ---------------
switch            swp1s1          0            0            0                  0                  0                  0            0                  0            0
switch            swp1s2          0            0            0                  0                  0                  0            0                  0            0
switch            swp63s1         0            0            0                  0                  0                  0            0                  0            0
switch            swp1s0          0            0            0                  0                  0                  0            0                  0            0
switch            swp63s3         0            0            0                  0                  0                  0            0                  0            0
switch            swp1s3          0            0            0                  0                  0                  0            0                  0            0
switch            swp63s0         0            0            0                  0                  0                  0            0                  0            0
switch            swp63s2         0            0            0                  0                  0                  0            0                  0            0
```

{{</tab>}}

{{</tabs>}}

### View Tx Counters

You can view RoCE Tx counters in both the UI and CLI.

{{<tabs "View Tx counters">}}

{{<tab "NetQ UI">}}

1. To view Tx counters, open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Switch to the full-screen card, then click **RoCE Counters**.
1. Click **Tx** above the panel on the right.

{{<figure src="/images/netq/roce-rx-counters-fs-4.0.0.png" width="700">}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To view general and CNP Tx counters, run `netq show roce-counters tx general`:

```
cumulus@switch:~$ netq show roce-counters tx general 

Matching roce records:
Hostname          Interface       ECN marked packets   TC packets   TC bytes     unicast no buffer discard buffer usage buffer max usage   TC usage     TC max usage
----------------- --------------- -------------------- ------------ ------------ ------------------------- ------------ ------------------ ------------ ------------
switch            swp1s1          0                    0            0            0                         0            0                  0            0
switch            swp1s2          0                    0            0            0                         0            0                  0            0
switch            swp63s1         0                    0            0            0                         0            0                  0            0
switch            swp1s0          0                    0            0            0                         0            0                  0            0
switch            swp63s3         0                    0            0            0                         0            0                  0            0
switch            swp1s3          0                    0            0            0                         0            0                  0            0
switch            swp63s0         0                    0            0            0                         0            0                  0            0
switch            swp63s2         0                    0            0            0                         0            0                  0            0
cumulus@switch      :~$ 
```

To view RoCE-specific Tx counters, run `netq show roce-counters tx roce`:

```
cumulus@switch:~$ netq show roce-counters tx roce 

Matching roce records:
Hostname          Interface       TC packets TC bytes   unicast no buffer discard PFC pause packets  PFC pause duration buffer usage buffer max usage   TC usage   TC max usage
----------------- --------------- ---------- ---------- ------------------------- ------------------ ------------------ ------------ ------------------ ---------- ---------------
switch            swp1s1          0          0          0                         0                  0                  0            0                  0          0
switch            swp1s2          0          0          0                         0                  0                  0            0                  0          0
switch            swp63s1         0          0          0                         0                  0                  0            0                  0          0
switch            swp1s0          0          0          0                         0                  0                  0            0                  0          0
switch            swp63s3         0          0          0                         0                  0                  0            0                  0          0
switch            swp1s3          0          0          0                         0                  0                  0            0                  0          0
switch            swp63s0         0          0          0                         0                  0                  0            0                  0          0
switch            swp63s2         0          0          0                         0                  0                  0            0                  0          0
```

{{</tab>}}

{{</tabs>}}

### View RoCE Counter Pools

{{<tabs "View RoCE counter pools">}}

{{<tab "NetQ UI">}}

1. To view RoCE counter pools, open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Switch to the full-screen card, then click **RoCE Counters**. Look for these columns: **Lossy Default Ingress Size**, **Roce Reserved Ingress Size**, **Lossy Default Egress Size**, and **Roce Reserved Egress Size**.

{{<figure src="/images/netq/roce-rx-counters-fs-4.0.0.png" width="700">}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To view the RoCE counter pools, run `netq show roce-counters pool`:

```
cumulus@switch:~$ netq show roce-counters pool 

Matching roce records:
Hostname          Lossy Default Ingress Size     Roce Reserved Ingress Size     Lossy Default Egress Size      Roce Reserved Egress Size
----------------- ------------------------------ ------------------------------ ------------------------------ ------------------------------
switch            104823                         104823                         104823                         104823
```

{{</tab>}}

{{</tabs>}}

### View Counters for a Specific Switch Port

{{<tabs "View counters for a specific port">}}

{{<tab "NetQ UI">}}

To view counters for a specific port:

1. Open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Select a port on the left.

{{<figure src="/images/netq/roce-l3-card-4.0.0.png" width="500">}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To view counters for a specific switch port, include the switch name with the command.

```
cumulus@switch:~$ netq show roce-counters swp1s1 rx general 

Matching roce records:
Hostname          Interface            PG packets           PG bytes             no buffer discard    buffer usage         buffer max usage     PG usage             PG max usage
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
switch            swp1s1               1643392              154094520            0                    0                    1                    0                    1
```

{{</tab>}}

{{</tabs>}}

### View Results from a Time in the Past

{{<tabs "View results in the past">}}

{{<tab "NetQ UI">}}

To view counters for a different time period in the past:

1. Open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/> in the header and select a different time period.

{{</tab>}}

{{<tab "NetQ CLI">}}

You can use the `around` keyword with any RoCE-related command to go back in time to view counters.

```
cumulus@switch:~$ netq show roce-counters swp1s1 rx general around 1h

Matching roce records:
Hostname          Interface            PG packets           PG bytes             no buffer discard    buffer usage         buffer max usage     PG usage             PG max usage
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
switch            swp1s1               661                  61856                0                    0                    1                    0                    1
```

{{</tab>}}

{{</tabs>}}

## Disable RoCE Monitoring

If you need to disable RoCE monitoring, do the following:

1. Edit `/etc/netq/commands/cl4-netq-commands.yml` and comment out the following lines:

        cumulus@netq-ts:~$ sudo nano /etc/netq/commands/cl4-netq-commands.yml

        #- period: "60"
        #  key: "roce"
        #  isactive: true
        #  command: "/usr/lib/cumulus/mlxcmd --json roce counters"
        #  parser: "local"

1. Delete the `/var/run/netq/netq_commands.yml` file:

        cumulus@netq-ts:~$ sudo rm /var/run/netq/netq_commands.yml

1. Restart the NetQ agent:

       cumulus@netq-ts:~$ netq config agent restart

## Related Information

- {{<link title="Configure Threshold-Based Event Notifications" text="Configure notifications for TCA events">}}
- {{<link title="TCA Event Messages Reference#roce" text="RoCE TCA event reference">}}
- [RoCE and Cumulus Linux]({{<ref "cumulus-linux-43/Network-Solutions/RDMA-over-Converged-Ethernet-RoCE">}})
