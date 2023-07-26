---
title: brctl showstp Shows Carrier Down Ports as Blocking
author: NVIDIA
weight: 410
toc: 4
---

## Issue

`brctl showstp` shows ports that are {{<link url="Monitor-Interface-Administrative-State-and-Physical-State-on-Cumulus-Linux" text="admin up/carrier down">}} as *blocking*:

    cumulus@switch$ sudo brctl show bridge
    bridge  name bridge id     STP enabled  interfaces
    bridge  8000.c45444bcfc8a  yes          swp1

    cumulus@switch$ ip l sh swp1
    28: swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast master bridge state DOWN mode DEFAULT qlen 500 
    link/ether c4:54:44:bc:fc:8a brd ff:ff:ff:ff:ff:ff

``` 
 cumulus@switch$ sudo brctl showstp bridge
 ...
 swp1 (1)
 port id 8001 state blocking
 ...
```

## Environment

- Cumulus Linux, all versions

## Resolution

Use `mstpctl showportdetail BRIDGE PORT`, which more accurately reflects the port state as *Disabled*/*discarding*.

    cumulus@switch$ sudo mstpctl showportdetail bridge swp1
     bridge:swp1 
     CIST info enabled no role Disabled
     port id 8.001 state discarding
     ...
