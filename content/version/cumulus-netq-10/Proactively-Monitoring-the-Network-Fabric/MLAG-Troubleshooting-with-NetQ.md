---
title: MLAG Troubleshooting with NetQ
author: Cumulus Networks
weight: 43
aliases:
 - /display/NETQ10/MLAG+Troubleshooting+with+NetQ
 - /pages/viewpage.action?pageId=6488211
pageID: 6488211
product: Cumulus NetQ
version: "1.0"
imgData: cumulus-netq-10
siteSlug: cumulus-netq-10
old: true
---
This chapter outlines a few scenarios that illustrate how you use NetQ
to troubleshoot MLAG on Cumulus Linux switches. Each starts with a log
message that indicates the current of MLAG state.

## All Nodes Are Up</span>

When the MLAG configuration is running smoothly, NetQ Notifier sends out
a message that all nodes are up:

    2017-05-22T23:13:09.683429+00:00 noc-pr netq-notifier[5501]: INFO: CLAG: All nodes are up

Running `netq show clag` confirms this:

    cumulus@noc-pr:~$ netq show clag
    Matching CLAG session records are:
    Node             Peer             SysMac            State Backup #Bonds #Dual Last Changed
    ---------------- ---------------- ----------------- ----- ------ ------ ----- --------------
    mlx-2700-03      torc-11(P)       44:38:39:ff:ff:01 up    up     8      8     26s ago
    noc-pr(P)        noc-se           00:01:01:10:00:01 up    up     9      9     39m ago
    noc-se           noc-pr(P)        00:01:01:10:00:01 up    up     9      9     40m ago
    torc-11(P)       mlx-2700-03      44:38:39:ff:ff:01 up    up     8      8     27s ago
    torc-21(P)       torc-22          44:38:39:ff:ff:02 up    up     8      8     2h ago
    torc-22          torc-21(P)       44:38:39:ff:ff:02 up    up     8      8     2h ago

You can also verify a specific node is up:

    cumulus@noc-pr:~$ netq mlx-2700-03 show clag
    Matching CLAG session records are:
    Node             Peer             SysMac            State Backup #Bonds #Dual Last Changed
    ---------------- ---------------- ----------------- ----- ------ ------ ----- --------------
    mlx-2700-03      torc-11(P)       44:38:39:ff:ff:01 up    up     8      8     45s ago

Similarly, checking the MLAG state with NetQ also confirms this:

    cumulus@noc-pr:~$ netq check clag
    Checked Nodes: 6, Failed Nodes: 0

When you're directly on the switch, you can run `clagctl` to get the
state:

    cumulus@mlx-2700-03:/var/log# sudo clagctl
     
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

## Dual-connected Bond Is Down</span>

When dual connectivity is lost in an MLAG configuration, you'll receive
messages from NetQ Notifier similar to the following:

    2017-05-22T23:14:40.290918+00:00 noc-pr netq-notifier[5501]: WARNING: LINK: 1 link(s) are down. They are: mlx-2700-03 hostbond5
    2017-05-22T23:14:53.081480+00:00 noc-pr netq-notifier[5501]: WARNING: CLAG: 1 node(s) have failures. They are: mlx-2700-03
    2017-05-22T23:14:58.161267+00:00 noc-pr netq-notifier[5501]: WARNING: CLAG: 2 node(s) have failures. They are: mlx-2700-03, torc-11

To begin your investigation, show the status of the `clagd` service:

    cumulus@noc-pr:~$ netq mlx-2700-03 show service clagd
     
    Matching services records are:
    Node        Service   PID   VRF     Enabled   Active   Monitored   Status   Up Time   Last Changed
    ----------- --------- ----- ------- --------- -------- ----------- -------- --------- --------------
    mlx-2700-03 clagd     5802  default yes       yes      yes         warning  1h ago    2m ago

Checking the MLAG status provides the reason for the failure:

    cumulus@noc-pr:~$ netq check clag
    Checked Nodes: 6, Warning Nodes: 2
    Node             Reason
    ---------------- --------------------------------------------------------------------------
    mlx-2700-03      Link Down: hostbond5
    torc-11          Singly Attached Bonds: hostbond5

You can retrieve the output in JSON format for importing the output into
another tool:

    cumulus@noc-pr:~$ netq check clag json
    {
    "warningNodes": [
    { "node": "mlx-2700-03", "reason": "Link Down: hostbond5" }
    ,
    { "node": "torc-11", "reason": "Singly Attached Bonds: hostbond5" }
    ], 
    "failedNodes": [], 
    "summary":
    { "checkedNodeCount": 6, "failedNodeCount": 0, "warningNodeCount": 2 }
    }

After you fix the issue, you can show the MLAG state to see if all the
nodes are up. The notifications from NetQ Notifier indicate all nodes
are UP, and the `netq check` flag also indicates there are no failures.

    cumulus@noc-pr:~$ netq show clag
    Matching CLAG session records are:
    Node             Peer             SysMac            State Backup #Bonds #Dual Last Changed
    ---------------- ---------------- ----------------- ----- ------ ------ ----- --------------
    mlx-2700-03      torc-11(P)       44:38:39:ff:ff:01 up    up     8      7     52s ago
    noc-pr(P)        noc-se           00:01:01:10:00:01 up    up     9      9     27m ago
    noc-se           noc-pr(P)        00:01:01:10:00:01 up    up     9      9     27m ago
    torc-11(P)       mlx-2700-03      44:38:39:ff:ff:01 up    up     8      7     50s ago
    torc-21(P)       torc-22          44:38:39:ff:ff:02 up    up     8      8     1h ago
    torc-22          torc-21(P)       44:38:39:ff:ff:02 up    up     8      8     1h ago

When you're directly on the switch, you can run `clagctl` to get the
state:

    cumulus@mlx-2700-03:/var/log# sudo clagctl
     
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

## VXLAN Active-active Device or Interface Is Down</span>

When a VXLAN active-active device or interface in an MLAG configuration
is down, log messages also include VXLAN and LNV checks.

    2017-05-22T23:16:51.517522+00:00 noc-pr netq-notifier[5501]: WARNING: VXLAN: 2 node(s) have failures. They are: mlx-2700-03, torc-11
    2017-05-22T23:16:51.525403+00:00 noc-pr netq-notifier[5501]: WARNING: LINK: 2 link(s) are down. They are: torc-11 vx-37, mlx-2700-03 vx-37
    2017-05-22T23:16:54.194681+00:00 noc-pr netq-notifier[5501]: WARNING: LNV: 1 node(s) have failures. They are: torc-22
    2017-05-22T23:16:59.448755+00:00 noc-pr netq-notifier[5501]: WARNING: LNV: 3 node(s) have failures. They are: tor-2, torc-21, torc-22
    2017-05-22T23:17:04.703044+00:00 noc-pr netq-notifier[5501]: WARNING: CLAG: 2 node(s) have failures. They are: mlx-2700-03, torc-11

To begin your investigation, show the status of the `clagd` service:

    cumulus@noc-pr:~$ netq mlx-2700-03 show service clagd
    Matching services records are:
    Node        Service   PID   VRF     Enabled   Active   Monitored   Status   Up Time   Last Changed
    ----------- --------- ----- ------- --------- -------- ----------- -------- --------- --------------
    mlx-2700-03 clagd     5802  default yes       yes      yes         error    2h ago    3m ago

Checking the MLAG status provides the reason for the failure:

    cumulus@noc-pr:~$ netq check clag
    Checked Nodes: 6, Warning Nodes: 2, Failed Nodes: 2 
    Node             Reason
    ---------------- --------------------------------------------------------------------------
    mlx-2700-03      Protodown Bonds: vx-37:vxlan-single 
    torc-11          Protodown Bonds: vx-37:vxlan-single 

You can retrieve the output in JSON format for importing the output into
another tool:

    cumulus@noc-pr:~$ netq check clag json
    {
    "failedNodes": [
    { "node": "mlx-2700-03", "reason": "Protodown Bonds: vx-37:vxlan-single" }
    ,
    { "node": "torc-11", "reason": "Protodown Bonds: vx-37:vxlan-single" }
    ], 
    "summary":
    { "checkedNodeCount": 6, "failedNodeCount": 2, "warningNodeCount": 2 }
    }

After you fix the issue, you can show the MLAG state to see if all the
nodes are up:

    cumulus@noc-pr:~$ netq show clag
    Matching CLAG session records are:
    Node             Peer             SysMac            State Backup #Bonds #Dual Last Changed
    ---------------- ---------------- ----------------- ----- ------ ------ ----- --------------
    mlx-2700-03      torc-11(P)       44:38:39:ff:ff:01 up    up     8      7     52s ago
    noc-pr(P)        noc-se           00:01:01:10:00:01 up    up     9      9     27m ago
    noc-se           noc-pr(P)        00:01:01:10:00:01 up    up     9      9     27m ago
    torc-11(P)       mlx-2700-03      44:38:39:ff:ff:01 up    up     8      7     50s ago
    torc-21(P)       torc-22          44:38:39:ff:ff:02 up    up     8      8     1h ago
    torc-22          torc-21(P)       44:38:39:ff:ff:02 up    up     8      8     1h ago

When you're directly on the switch, you can run `clagctl` to get the
state:

    cumulus@mlx-2700-03:/var/log# sudo clagctl
     
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

## Remote-side clagd Stopped by systemctl Command</span>

In the event the `clagd` service is stopped via the `systemctl` command,
NetQ Notifier sends messages similar to the following:

    2017-05-22T23:51:19.539033+00:00 noc-pr netq-notifier[5501]: WARNING: VXLAN: 1 node(s) have failures. They are: torc-11
    2017-05-22T23:51:19.622379+00:00 noc-pr netq-notifier[5501]: WARNING: LINK: 2 link(s) flapped and are down. They are: torc-11 hostbond5, torc-11 hostbond4
    2017-05-22T23:51:19.622922+00:00 noc-pr netq-notifier[5501]: WARNING: LINK: 23 link(s) are down. They are: torc-11 VlanA-1-104-v0, torc-11 VlanA-1-101-v0, torc-11 VlanA-1, torc-11 vx-33, torc-11 vx-36, torc-11 vx-37, torc-11 vx-34, torc-11 vx-35, torc-11 swp7, torc-11 VlanA-1-102-v0, torc-11 VlanA-1-103-v0, torc-11 VlanA-1-100-v0, torc-11 VlanA-1-106-v0, torc-11 swp8, torc-11 VlanA-1.106, torc-11 VlanA-1.105, torc-11 VlanA-1.104, torc-11 VlanA-1.103, torc-11 VlanA-1.102, torc-11 VlanA-1.101, torc-11 VlanA-1.100, torc-11 VlanA-1-105-v0, torc-11 vx-38
    2017-05-22T23:51:27.696572+00:00 noc-pr netq-notifier[5501]: INFO: LINK: 15 link(s) are up. They are: torc-11 VlanA-1.106, torc-11 VlanA-1-104-v0, torc-11 VlanA-1.104, torc-11 VlanA-1.103, torc-11 VlanA-1.101, torc-11 VlanA-1-100-v0, torc-11 VlanA-1.100, torc-11 VlanA-1.102, torc-11 VlanA-1-101-v0, torc-11 VlanA-1-102-v0, torc-11 VlanA-1.105, torc-11 VlanA-1-103-v0, torc-11 VlanA-1-106-v0, torc-11 VlanA-1, torc-11 VlanA-1-105-v0
    2017-05-22T23:51:30.863789+00:00 noc-pr netq-notifier[5501]: WARNING: LNV: 1 node(s) have failures. They are: torc-11
    2017-05-22T23:51:36.156708+00:00 noc-pr netq-notifier[5501]: WARNING: CLAG: 2 node(s) have failures. They are: mlx-2700-03, torc-11
    2017-05-22T23:51:36.183638+00:00 noc-pr netq-notifier[5501]: WARNING: LNV: 2 node(s) have failures. They are: spine-2, torc-11
    2017-05-22T23:51:41.444670+00:00 noc-pr netq-notifier[5501]: WARNING: LNV: 1 node(s) have failures. They are: torc-11

Showing the MLAG state reveals which nodes are down:

    cumulus@noc-pr:~$ netq show clag
    Matching CLAG session records are:
    Node             Peer             SysMac            State Backup #Bonds #Dual Last Changed
    ---------------- ---------------- ----------------- ----- ------ ------ ----- --------------
    mlx-2700-03                       44:38:39:ff:ff:01 down  down   8      0     33s ago
    noc-pr(P)        noc-se           00:01:01:10:00:01 up    up     9      9     1h ago
    noc-se           noc-pr(P)        00:01:01:10:00:01 up    up     9      9     1h ago
    torc-11                           44:38:39:ff:ff:01 down  n/a    0      0     32s ago
    torc-21(P)       torc-22          44:38:39:ff:ff:02 up    up     8      8     2h ago
    torc-22          torc-21(P)       44:38:39:ff:ff:02 up    up     8      8     2h ago

Checking the MLAG status provides the reason for the failure:

    cumulus@noc-pr:~$ netq check clag
    Checked Nodes: 6, Warning Nodes: 1, Failed Nodes: 2 
    Node             Reason
    ---------------- --------------------------------------------------------------------------
    mlx-2700-03      Peer Connectivity failed 
    torc-11          Peer Connectivity failed 

You can retrieve the output in JSON format for importing the output into
another tool:

    cumulus@noc-pr:~$ netq check clag json
    {
    "failedNodes": [
    { "node": "mlx-2700-03", "reason": "Peer Connectivity failed" }
    ,
    { "node": "torc-11", "reason": "Peer Connectivity failed" }
    ], 
    "summary":
    { "checkedNodeCount": 6, "failedNodeCount": 2, "warningNodeCount": 1 }
    }

When you're directly on the switch, you can run `clagctl` to get the
state:

    root@mlx-2700-03:/var/log# clagctl
     
     
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
