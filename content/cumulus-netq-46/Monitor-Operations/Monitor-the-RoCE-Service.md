---
title: RoCE
author: NVIDIA
weight: 940
toc: 3
---

Use the UI or CLI to monitor RDMA over Converged Ethernet (RoCE) in your network.

RoCe commands include:

```
    netq [<hostname>] show roce-counters [<text-port>] tx | rx [roce | general] [around <text-time>] [json]
    netq [<hostname>] show roce-config [<text-port>] [around <text-time>] [json]
    netq [<hostname>] show roce-counters pool [json]
    netq [<hostname>] show events [message_type tca_roce]
    netq [<hostname>] show events [message_type roceconfig]
```
{{<notice note>}}

Priority code point (PCP) monitoring requires NetQ Agent 4.5.

{{</notice>}}
## View the RoCE Configuration

To view the RoCE configuration, run `netq show roce-config`.

{{<expand "show roce-config">}}
```
cumulus@switch:~$ netq show roce-config 

Matching roce records:
Hostname          Interface       RoCE Mode  Enabled TCs  Mode     ECN Max  ECN Min  DSCP->SP   PCP->SP  SP->PG   SP->TC   PFC SPs  PFC Rx     PFC Tx     ETS Mode   Last Changed
----------------- --------------- ---------- ------------ -------- -------- -------- ---------- -------- -------- -------- -------- ---------- ---------- ---------- -------------------------
mlx-2700a1-19     swp13           Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
mlx-2700a1-19     swp18           Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
mlx-2700a1-19     swp12           Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
mlx-2700a1-19     swp28           Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
mlx-2700a1-19     swp9            Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
mlx-2700a1-19     swp2            Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
mlx-2700a1-19     swp24           Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
mlx-2700a1-19     swp23           Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
mlx-2700a1-19     swp31           Lossless   0,3          ECN      1505280  153600   26 -> 2    4 -> 3   3 -> 1   3 -> 3   -        disabled   enabled    dwrr       Thu Jan 12 11:43:49 2023
ufm-switch23      swp32           Lossless   0,3          ECN      1505280  153600   26 -> 3    3 -> 3   3 -> 1   3 -> 3   3        enabled    enabled    dwrr       Thu Jan 12 12:12:39 2023
ufm-switch23      swp1            Lossless   0,3          ECN      1505280  153600   26 -> 3    3 -> 3   3 -> 1   3 -> 3   3        enabled    enabled    dwrr       Thu Jan 12 12:12:39 2023
ufm-switch23      swp8            Lossless   0,3          ECN      1505280  153600   26 -> 3    3 -> 3   3 -> 1   3 -> 3   3        enabled    enabled    dwrr       Thu Jan 12 12:12:39 2023
ufm-switch23      swp11           Lossless   0,3          ECN      1505280  153600   26 -> 3    3 -> 3   3 -> 1   3 -> 3   3        enabled    enabled    dwrr       Thu Jan 12 12:12:39 2023
ufm-switch23      swp22           Lossless   0,3          ECN      1505280  153600   26 -> 3    3 -> 3   3 -> 1   3 -> 3   3        enabled    enabled    dwrr       Thu Jan 12 12:12:39 2023
...
```
{{</expand>}}
## View RoCE Counters

You can view the following RoCE counters for a given switch through the UI or CLI:

- Rx and Tx counters
- General, CNP, and RoCE-specific counters
- Counter pools
- Port-specific counters

### View Rx Counters

{{<tabs "View Rx counters">}}

{{<tab "NetQ UI">}}

1. To view Rx counters, open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Expand the card to the largest size, then select **RoCE Counters** from the side menu:

{{<figure src="/images/netq/roce-rx-counters-fs-4.0.0.png" alt="full-size switch card with RoCe Counters tab selected" width="700">}}

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

{{<tabs "View Tx counters">}}

{{<tab "NetQ UI">}}

1. To view Tx counters, open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Expand the card to the largest size, then select **RoCE Counters** from the side menu.
1. Select **Tx** from the toggle above the table:

{{<figure src="/images/netq/roce-rx-counters-fs-4.0.0.png" alt="switch card with table displaying Rx and Tx RoCe toggle" width="700">}}

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
1. Switch to the full-screen card, then click **RoCE Counters**. Look for these columns: **Lossy Default Ingress Size**, **RoCE Reserved Ingress Size**, **Lossy Default Egress Size**, and **RoCE Reserved Egress Size**.

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

1. Open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Select a port from the list on the left:

{{<figure src="/images/netq/roce-l3-card-4.0.0.png" alt="switch card displaying list of ports" width="500">}}

{{</tab>}}

{{<tab "NetQ CLI">}}

To view counters for a specific switch port, include the switch name with the command:

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

To view counters for a time period in the past:

1. Open the large switch card, then click the RoCE icon ({{<img src="/images/netq/icon-roce-4.0.0.png" width="34px">}}).
1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/18-Time/time-stopwatch.svg" height="18" width="18"/> in the header and select a different time period.

{{</tab>}}

{{<tab "NetQ CLI">}}

Use `around` with any RoCE-related command to view counters from a previous time period:

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

To disable RoCE monitoring:

1. Edit `/etc/netq/commands/cl4-netq-commands.yml` and comment out the following lines:

        cumulus@netq-ts:~$ sudo nano /etc/netq/commands/cl4-netq-commands.yml

        #- period: "60"
        #  key: "roce"
        #  isactive: true
        #  command: "/usr/lib/cumulus/mlxcmd --json roce counters"
        #  parser: "local"

1. Delete the `/var/run/netq/netq_commands.yml` file:

        cumulus@netq-ts:~$ sudo rm /var/run/netq/netq_commands.yml

1. Restart the NetQ Agent:

       cumulus@netq-ts:~$ netq config agent restart

## Related Information

- {{<link title="Configure Threshold-Crossing Event Notifications" text="Configure notifications for TCA events">}}
- {{<link title="TCA Event Messages Reference#roce" text="RoCE TCA event reference">}}
- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-53/Layer-1-and-Switch-Ports/Quality-of-Service/RDMA-over-Converged-Ethernet-RoCE/" text="RoCE and Cumulus Linux">}}
