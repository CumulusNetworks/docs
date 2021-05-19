---
title: Resolve MLAG Issues
author: NVIDIA
weight: 1070
toc: 4
---
This topic outlines a few scenarios that illustrate how you use NetQ to troubleshoot [MLAG]({{<ref "/cumulus-linux-43/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}}) on Cumulus Linux switches. Each starts with a log message that indicates the current MLAG state.

NetQ can monitor many aspects of an MLAG configuration, including:

- Verifying the current state of all nodes
- Verifying the dual connectivity state
- Checking that the peer link is part of the bridge
- Verifying whether MLAG bonds are not bridge members
- Verifying whether the VXLAN interface is not a bridge member
- Checking for remote-side service failures caused by `systemctl`
- Checking for VLAN-VNI mapping mismatches
- Checking for layer 3 MTU mismatches on peerlink subinterfaces
- Checking for VXLAN active-active address inconsistencies
- Verifying that STP priorities are the same across both peers

## Scenario 1: All Nodes Are Up

When the MLAG configuration is running smoothly, NetQ sends out a message that all nodes are up:

    2017-05-22T23:13:09.683429+00:00 noc-pr netq-notifier[5501]: INFO: CLAG: All nodes are up

Running `netq show mlag` confirms this:

```
cumulus@switch:~$ netq show mlag
Matching clag records:
Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                            s
----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
spine01(P)        spine02           00:01:01:10:00:01  up         up     24    24    Thu Feb  7 18:30:49 2019
spine02           spine01(P)        00:01:01:10:00:01  up         up     24    24    Thu Feb  7 18:30:53 2019
leaf01(P)         leaf02            44:38:39:ff:ff:01  up         up     12    12    Thu Feb  7 18:31:15 2019
leaf02            leaf01(P)         44:38:39:ff:ff:01  up         up     12    12    Thu Feb  7 18:31:20 2019
leaf03(P)         leaf04            44:38:39:ff:ff:02  up         up     12    12    Thu Feb  7 18:31:26 2019
leaf04            leaf03(P)         44:38:39:ff:ff:02  up         up     12    12    Thu Feb  7 18:31:30 2019
```

You can also verify a specific node is up:

```
cumulus@switch:~$ netq spine01 show mlag
Matching mlag records:
Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                            s
----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
spine01(P)        spine02           00:01:01:10:00:01  up         up     24    24    Thu Feb  7 18:30:49 2019
```

Similarly, checking the MLAG state with NetQ also confirms this:

```
cumulus@switch:~$ netq check mlag
clag check result summary:

Total nodes         : 6
Checked nodes       : 6
Failed nodes        : 0
Rotten nodes        : 0
Warning nodes       : 0


Peering Test             : passed
Backup IP Test           : passed
Clag SysMac Test         : passed
VXLAN Anycast IP Test    : passed
Bridge Membership Test   : passed
Spanning Tree Test       : passed
Dual Home Test           : passed
Single Home Test         : passed
Conflicted Bonds Test    : passed
ProtoDown Bonds Test     : passed
SVI Test                 : passed
```

{{%notice note%}}
The `clag` keyword has been deprecated and replaced by the `mlag` keyword. The
`clag` keyword continues to work for now, but you should start using the `mlag`
keyword instead. Keep in mind you should also update any scripts that use the `clag`
keyword.
{{%/notice%}}

When you are logged directly into a switch, you can run `clagctl` to get
the state:

```
cumulus@switch:/var/log$ sudo clagctl
    
The peer is alive
Peer Priority, ID, and Role: 4096 00:02:00:00:00:4e primary
Our Priority, ID, and Role: 8192 44:38:39:00:a5:38 secondary
Peer Interface and IP: peerlink-3.4094 169.254.0.9
VxLAN Anycast IP: 36.0.0.20
Backup IP: 27.0.0.20 (active)
System MAC: 44:38:39:ff:ff:01
    
CLAG Interfaces
Our Interface    Peer Interface   CLAG Id Conflicts            Proto-Down Reason
---------------- ---------------- ------- -------------------- -----------------
vx-38            vx-38            -       -                    -
vx-33            vx-33            -       -                    -
hostbond4        hostbond4        1       -                    -
hostbond5        hostbond5        2       -                    -
vx-37            vx-37            -       -                    -
vx-36            vx-36            -       -                    -
vx-35            vx-35            -       -                    -
vx-34            vx-34            -       -                    -
```

## Scenario 2: Dual-connected Bond Is Down

When dual connectivity is lost in an MLAG configuration, you receive messages from NetQ similar to the following:

    2017-05-22T23:14:40.290918+00:00 noc-pr netq-notifier[5501]: WARNING: LINK: 1 link(s) are down. They are: spine01 hostbond5
    2017-05-22T23:14:53.081480+00:00 noc-pr netq-notifier[5501]: WARNING: CLAG: 1 node(s) have failures. They are: spine01
    2017-05-22T23:14:58.161267+00:00 noc-pr netq-notifier[5501]: WARNING: CLAG: 2 node(s) have failures. They are: spine01, leaf01

To begin your investigation, show the status of the `clagd` service:

```
cumulus@switch:~$ netq spine01 show services clagd
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
spine01           clagd                2678  default         yes     yes    yes       ok               23h:57m:16s               Thu Feb  7 18:30:49 2019
```

Checking the MLAG status provides the reason for the failure:

```
cumulus@switch:~$ netq check mlag
Checked Nodes: 6, Warning Nodes: 2
Node             Reason
---------------- --------------------------------------------------------------------------
spine01          Link Down: hostbond5
leaf01           Singly Attached Bonds: hostbond5
```

You can retrieve the output in JSON format for export to another tool:

```
cumulus@switch:~$ netq check mlag json
{
    "warningNodes": [
        { 
            "node": "spine01", 
            "reason": "Link Down: hostbond5" 
        }
        ,
        { 
            "node": "lea01", 
            "reason": "Singly Attached Bonds: hostbond5" 
        }
    ],
    "failedNodes":[
    ],
    "summary":{
        "checkedNodeCount":6,
        "failedNodeCount":0,
        "warningNodeCount":2
    }
}
```

After you fix the issue, you can show the MLAG state to see if all the nodes are up. The notifications from NetQ indicate all nodes are UP, and the `netq check` flag also indicates there are no failures.

```
cumulus@switch:~$ netq show mlag
    
Matching clag records:
Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                            s
----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
spine01(P)        spine02           00:01:01:10:00:01  up         up     24    24    Thu Feb  7 18:30:49 2019
spine02           spine01(P)        00:01:01:10:00:01  up         up     24    24    Thu Feb  7 18:30:53 2019
leaf01(P)         leaf02            44:38:39:ff:ff:01  up         up     12    12    Thu Feb  7 18:31:15 2019
leaf02            leaf01(P)         44:38:39:ff:ff:01  up         up     12    12    Thu Feb  7 18:31:20 2019
leaf03(P)         leaf04            44:38:39:ff:ff:02  up         up     12    12    Thu Feb  7 18:31:26 2019
leaf04            leaf03(P)         44:38:39:ff:ff:02  up         up     12    12    Thu Feb  7 18:31:30 2019
```

When you are logged directly into a switch, you can run `clagctl` to get the state:

```
cumulus@switch:/var/log$ sudo clagctl
    
The peer is alive
Peer Priority, ID, and Role: 4096 00:02:00:00:00:4e primary
Our Priority, ID, and Role: 8192 44:38:39:00:a5:38 secondary
Peer Interface and IP: peerlink-3.4094 169.254.0.9
VxLAN Anycast IP: 36.0.0.20
Backup IP: 27.0.0.20 (active)
System MAC: 44:38:39:ff:ff:01
    
CLAG Interfaces
Our Interface    Peer Interface   CLAG Id Conflicts            Proto-Down Reason
---------------- ---------------- ------- -------------------- -----------------
vx-38            vx-38            -       -                    -
vx-33            vx-33            -       -                    -
hostbond4        hostbond4        1       -                    -
hostbond5        -                2       -                    -
vx-37            vx-37            -       -                    -
vx-36            vx-36            -       -                    -
vx-35            vx-35            -       -                    -
vx-34            vx-34            -       -                    -
```

## Scenario 3: VXLAN Active-active Device or Interface Is Down

When a VXLAN active-active device or interface in an MLAG configuration is down, log messages also include VXLAN checks.

    2017-05-22T23:16:51.517522+00:00 noc-pr netq-notifier[5501]: WARNING: VXLAN: 2 node(s) have failures. They are: spine01, leaf01
    2017-05-22T23:16:51.525403+00:00 noc-pr netq-notifier[5501]: WARNING: LINK: 2 link(s) are down. They are: leaf01 vx-37, spine01 vx-37
    2017-05-22T23:17:04.703044+00:00 noc-pr netq-notifier[5501]: WARNING: CLAG: 2 node(s) have failures. They are: spine01, leaf01

To begin your investigation, show the status of the `clagd` service:

```
cumulus@switch:~$ netq spine01 show services clagd
    
Matching services records:
Hostname          Service              PID   VRF             Enabled Active Monitored Status           Uptime                    Last Changed
----------------- -------------------- ----- --------------- ------- ------ --------- ---------------- ------------------------- -------------------------
spine01           clagd                2678  default         yes     yes    yes       error            23h:57m:16s               Thu Feb  7 18:30:49 2019
```

Checking the MLAG status provides the reason for the failure:

    cumulus@switch:~$ netq check mlag
    Checked Nodes: 6, Warning Nodes: 2, Failed Nodes: 2
    Node             Reason
    ---------------- --------------------------------------------------------------------------
    spine01          Protodown Bonds: vx-37:vxlan-single
    leaf01           Protodown Bonds: vx-37:vxlan-single

You can retrieve the output in JSON format for export to another tool:

    cumulus@switch:~$ netq check mlag json
    {
        "failedNodes": [
            { 
                "node": "spine01", 
                "reason": "Protodown Bonds: vx-37:vxlan-single" 
            }
            ,
            { 
                "node": "leaf01", 
                "reason": "Protodown Bonds: vx-37:vxlan-single" 
            }
        ],
        "summary":{ 
                "checkedNodeCount": 6, 
                "failedNodeCount": 2, 
                "warningNodeCount": 2 
        }
    }

After you fix the issue, you can show the MLAG state to see if all the
nodes are up:

    cumulus@switch:~$ netq show mlag
    Matching clag session records are:
    Hostname          Peer              SysMac             State      Backup #Bond #Dual Last Changed
                                                                             s
    ----------------- ----------------- ------------------ ---------- ------ ----- ----- -------------------------
    spine01(P)        spine02           00:01:01:10:00:01  up         up     24    24    Thu Feb  7 18:30:49 2019
    spine02           spine01(P)        00:01:01:10:00:01  up         up     24    24    Thu Feb  7 18:30:53 2019
    leaf01(P)         leaf02            44:38:39:ff:ff:01  up         up     12    12    Thu Feb  7 18:31:15 2019
    leaf02            leaf01(P)         44:38:39:ff:ff:01  up         up     12    12    Thu Feb  7 18:31:20 2019
    leaf03(P)         leaf04            44:38:39:ff:ff:02  up         up     12    12    Thu Feb  7 18:31:26 2019
    leaf04            leaf03(P)         44:38:39:ff:ff:02  up         up     12    12    Thu Feb  7 18:31:30 2019

When you are logged directly into a switch, you can run `clagctl` to get
the state:

    cumulus@switch:/var/log$ sudo clagctl
     
    The peer is alive
    Peer Priority, ID, and Role: 4096 00:02:00:00:00:4e primary
    Our Priority, ID, and Role: 8192 44:38:39:00:a5:38 secondary
    Peer Interface and IP: peerlink-3.4094 169.254.0.9
    VxLAN Anycast IP: 36.0.0.20
    Backup IP: 27.0.0.20 (active)
    System MAC: 44:38:39:ff:ff:01
     
    CLAG Interfaces
    Our Interface    Peer Interface   CLAG Id Conflicts            Proto-Down Reason
    ---------------- ---------------- ------- -------------------- -----------------
    vx-38            vx-38            -       -                    -
    vx-33            vx-33            -       -                    -
    hostbond4        hostbond4        1       -                    -
    hostbond5        hostbond5        2       -                    -
    vx-37            -                -       -                    vxlan-single
    vx-36            vx-36            -       -                    -
    vx-35            vx-35            -       -                    -
    vx-34            vx-34            -       -                    -

## Scenario 4: Remote-side clagd Stopped by systemctl Command

In the event the `clagd` service is stopped via the `systemctl` command, NetQ Notifier sends messages similar to the following:

    2017-05-22T23:51:19.539033+00:00 noc-pr netq-notifier[5501]: WARNING: VXLAN: 1 node(s) have failures. They are: leaf01
    2017-05-22T23:51:19.622379+00:00 noc-pr netq-notifier[5501]: WARNING: LINK: 2 link(s) flapped and are down. They are: leaf01 hostbond5, leaf01 hostbond4
    2017-05-22T23:51:19.622922+00:00 noc-pr netq-notifier[5501]: WARNING: LINK: 23 link(s) are down. They are: leaf01 VlanA-1-104-v0, leaf01 VlanA-1-101-v0, leaf01 VlanA-1, leaf01 vx-33, leaf01 vx-36, leaf01 vx-37, leaf01 vx-34, leaf01 vx-35, leaf01 swp7, leaf01 VlanA-1-102-v0, leaf01 VlanA-1-103-v0, leaf01 VlanA-1-100-v0, leaf01 VlanA-1-106-v0, leaf01 swp8, leaf01 VlanA-1.106, leaf01 VlanA-1.105, leaf01 VlanA-1.104, leaf01 VlanA-1.103, leaf01 VlanA-1.102, leaf01 VlanA-1.101, leaf01 VlanA-1.100, leaf01 VlanA-1-105-v0, leaf01 vx-38
    2017-05-22T23:51:27.696572+00:00 noc-pr netq-notifier[5501]: INFO: LINK: 15 link(s) are up. They are: leaf01 VlanA-1.106, leaf01 VlanA-1-104-v0, leaf01 VlanA-1.104, leaf01 VlanA-1.103, leaf01 VlanA-1.101, leaf01 VlanA-1-100-v0, leaf01 VlanA-1.100, leaf01 VlanA-1.102, leaf01 VlanA-1-101-v0, leaf01 VlanA-1-102-v0, leaf01 VlanA-1.105, leaf01 VlanA-1-103-v0, leaf01 VlanA-1-106-v0, leaf01 VlanA-1, leaf01 VlanA-1-105-v0
    2017-05-22T23:51:36.156708+00:00 noc-pr netq-notifier[5501]: WARNING: CLAG: 2 node(s) have failures. They are: spine01, leaf01

Showing the MLAG state reveals which nodes are down:

    cumulus@switch:~$ netq show mlag
    Matching CLAG session records are:
    Node             Peer             SysMac            State Backup #Bonds #Dual Last Changed
    ---------------- ---------------- ----------------- ----- ------ ------ ----- -------------------------
    spine01(P)       spine02           00:01:01:10:00:01 up   up     9      9     Thu Feb  7 18:30:53 2019
    spine02          spine01(P)        00:01:01:10:00:01 up   up     9      9     Thu Feb  7 18:31:04 2019
    leaf01                             44:38:39:ff:ff:01 down n/a    0      0     Thu Feb  7 18:31:13 2019
    leaf03(P)        leaf04            44:38:39:ff:ff:02 up   up     8      8     Thu Feb  7 18:31:19 2019
    leaf04           leaf03(P)         44:38:39:ff:ff:02 up   up     8      8     Thu Feb  7 18:31:25 2019

Checking the MLAG status provides the reason for the failure:

    cumulus@switch:~$ netq check mlag
    Checked Nodes: 6, Warning Nodes: 1, Failed Nodes: 2
    Node             Reason
    ---------------- --------------------------------------------------------------------------
    spine01          Peer Connectivity failed
    leaf01           Peer Connectivity failed

You can retrieve the output in JSON format for export to another tool:

    cumulus@switch:~$ netq check mlag json
    {
        "failedNodes": [
            { 
                "node": "spine01", 
                "reason": "Peer Connectivity failed" 
            }
            ,
            { 
                "node": "leaf01", 
                "reason": "Peer Connectivity failed" 
            }
        ],
        "summary":{ 
            "checkedNodeCount": 6, 
            "failedNodeCount": 2, 
            "warningNodeCount": 1 
        }
    }

When you are logged directly into a switch, you can run `clagctl` to get
the state:

```
cumulus@switch:~$ sudo clagctl
    
The peer is not alive
Our Priority, ID, and Role: 8192 44:38:39:00:a5:38 primary
Peer Interface and IP: peerlink-3.4094 169.254.0.9
VxLAN Anycast IP: 36.0.0.20
Backup IP: 27.0.0.20 (inactive)
System MAC: 44:38:39:ff:ff:01
    
CLAG Interfaces
Our Interface    Peer Interface   CLAG Id Conflicts            Proto-Down Reason
---------------- ---------------- ------- -------------------- -----------------
vx-38            -                -       -                    -
vx-33            -                -       -                    -
hostbond4        -                1       -                    -
hostbond5        -                2       -                    -
vx-37            -                -       -                    -
vx-36            -                -       -                    -
vx-35            -                -       -                    -
vx-34            -                -       -                    -
```
