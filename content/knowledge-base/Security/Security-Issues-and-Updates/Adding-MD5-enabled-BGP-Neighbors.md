---
title: Adding MD5-enabled BGP Neighbors
author: NVIDIA
weight: 453
toc: 4
---

## Issue

Some organizations use MD5 on BGP for security reasons or because existing partners require MD5. This article describes how you can enable it.

## Environment

- Cumulus Linux 2.1 and later.
- This article assumes that you are using FRR for your routing platform. The setup consists of two switches, AS 65000 and 65001, connected by the link 192.0.2.100/30.

## Resolution

You enable MD5 for your BGP neighbors in one of two ways:

- Using FRR's modal CLI, `vtysh`.
- By hand editing the `frr.conf` configuration file in Cumulus Linux.

Before you enable MD5, switch1's configuration looks like this:

    frr# show ip bgp sum
    BGP router identifier 192.0.2.2, local AS number 65001
    RIB entries 0, using 0 bytes of memory
    Peers 1, using 6652 bytes of memory
    Neighbor V AS MsgRcvd MsgSent TblVer InQ OutQ Up/Down State/PfxRcd
    192.0.2.102 4 65000 2 3 0 0 0 00:00:04 0
    Total number of neighbors 1

And switch2's configuration looks like this:

    frr# sho ip bgp sum
    BGP router identifier 192.0.2.5, local AS number 65000
    RIB entries 0, using 0 bytes of memory
    Peers 1, using 6652 bytes of memory
    Neighbor V AS MsgRcvd MsgSent TblVer InQ OutQ Up/Down State/PfxRcd
    192.0.2.101 4 65001 2 3 0 0 0 00:00:49 0
    Total number of neighbors 1

### Enable MD5 Using vtysh

1.  SSH into switch1.

2.  Run `sudo vtysh`.

3.  Run these FRR commands:  

        frr# configure terminal
        frr(config)# router bgp 65000
        frr(config-router)# neighbor 192.0.2.101 password mypassword

4.  SSH into switch2, then run these FRR commands:  

        frr# configure terminal
        frr(config)# router bgp 65001
        frr(config-router)# neighbor 192.0.2.102 password mypassword

5.  When you configure both sides properly, BGP should reestablish automatically; confirm using `show ip bgp summary` on each switch. Here is the output from switch2:  

        frr# show ip bgp summary  
        BGP router identifier 192.0.2.5, local AS number 65000
        RIB entries 0, using 0 bytes of memory
        Peers 1, using 6652 bytes of memory
        
        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        192.0.2.101     4 65001     257     284        0    0    0 00:08:11        0
        
        Total number of neighbors 1

6.  Run `write memory` on each switch if you want this configuration to
    persist after FRR restarts.

### Enable MD5 by Hand Editing the Configuration

1.  SSH into switch1.

2.  Using a text editor (the article assumes you are using `vi`), edit `frr.conf`.

3.  Run `vi /etc/frr/frr.conf`. If you are running Cumulus Linux 2.0, `sudo vi /etc/frr/frr.conf`.

4.  Find switch1's BGP configuration under `/bgp`:  

        router bgp 65000
        bgp router-id 192.0.2.2
        neighbor 192.0.2.101 remote-as 65001

5.  Enter insert mode, then add the following line:  

        neighbor 192.0.2.101 password mypassword

6.  Save and exit (`:wq!`).

7.  Restart FRR (`sudo systemctl restart frr`).

    {{%notice warning%}}

This tears down any other layer 3 sessions and affects network traffic.

{{%/notice%}}

8.  Confirm this worked using `net show bgp summary`:  

        cumulus@switch:~$ net show bgp summary 
        BGP router identifier 192.0.2.2, local AS number 65001
        RIB entries 0, using 0 bytes of memory
        Peers 1, using 6652 bytes of memory
        
        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        192.0.2.102     4 65000     200     227        0    0    0 00:00:03        0
        
        Total number of neighbors 1

9.  SSH into switch2, then edit `frr.conf` there:  

        vi /etc/frr/frr.conf

    If you are running Cumulus Linux 2.0 or later:

        sudo vi /etc/frr/frr.conf

10. Find switch2's BGP configuration under `/bgp`:  

        router bgp 65001
        bgp router-id 192.0.2.5
        neighbor 192.0.2.102 remote-as 65000

11. Enter insert mode, then add the following line:  

        neighbor 192.0.2.102 password mypassword

12. Save and exit (`:wq!`).

13. Restart FRR (`sudo systemctl restart frr`).

    {{%notice warning%}}

This tears down any other layer 3 sessions and affects network traffic.

{{%/notice%}}

14. Confirm this worked using `net show bgp summary`:  

        BGP router identifier 192.0.2.5, local AS number 65000
        RIB entries 0, using 0 bytes of memory
        Peers 1, using 6652 bytes of memory
        
        Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
        192.0.2.101     4 65001     255     282        0    0    0 00:06:29        0
        
        Total number of neighbors 1
