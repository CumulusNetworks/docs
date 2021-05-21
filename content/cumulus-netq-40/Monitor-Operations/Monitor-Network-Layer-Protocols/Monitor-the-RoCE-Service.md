---
title: Monitor the RoCE Service
author: NVIDIA
weight: 980
toc: 4
---

*RDMA over Converged Ethernet* ({{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE">}}) provides the ability to write to compute or storage elements using remote direct memory access (RDMA) over an Ethernet network instead of using host CPUs. RoCE relies on congestion control and lossless Ethernet to operate. Cumulus Linux supports features that can enable lossless Ethernet for RoCE environments.

RoCE helps you obtain a converged network, where all services run over the Ethernet infrastructure, including Infiniband apps.

You monitor RoCE in your network with the following commands:

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

- `netq show roce-counters`: Displays the RoCE counters for a given switch.

### View General Rx Counters

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

### View RoCE-specific Rx Counters

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

### View General Tx Counters

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

### View RoCE-specific Tx Counters

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

### View RoCE Counter Pools

- `netq show roce-counters pool`: Displays RoCE pools.

```
cumulus@switch:~$ netq show roce-counters pool 

Matching roce records:
Hostname          Lossy Default Ingress Size     Roce Reserved Ingress Size     Lossy Default Egress Size      Roce Reserved Egress Size
----------------- ------------------------------ ------------------------------ ------------------------------ ------------------------------
switch            104823                         104823                         104823                         104823
```

### View Counters for a Specific Switch Port

```
cumulus@switch:~$ netq show roce-counters swp1s1 rx general 

Matching roce records:
Hostname          Interface            PG packets           PG bytes             no buffer discard    buffer usage         buffer max usage     PG usage             PG max usage
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
switch            swp1s1               1643392              154094520            0                    0                    1                    0                    1
```

### View Results from Time in the Past

```
cumulus@switch:~$ netq show roce-counters swp1s1 rx general around 1h

Matching roce records:
Hostname          Interface            PG packets           PG bytes             no buffer discard    buffer usage         buffer max usage     PG usage             PG max usage
----------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- -------------------- --------------------
switch            swp1s1               661                  61856                0                    0                    1                    0                    1
```


## Related Information 

[RoCE and Cumulus Linux]({{<ref "cumulus-linux-43/Network-Solutions/RDMA-over-Converged-Ethernet-RoCE">}})
