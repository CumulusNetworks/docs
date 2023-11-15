---
title: What Does DORMANT Mean for MLAG Bond Interfaces
author: NVIDIA
weight: 414
toc: 4
---

## Issue

In the output of `ip link show`, the MLAG downlink bond interface shows as DORMANT:

    cumulus@switch$ ip link show bond1
    222: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-v1 state UP mode DORMANT 
        link/ether 08:9e:01:ce:e4:13 brd ff:ff:ff:ff:ff:ff 

## Environment

- Cumulus Linux, all versions

## Explanation

DORMANT is a Linux term used in two contexts:

- Mode type
- Link state

In the example below, consider the following output, noting that `state` is UP and `mode` is DORMANT:

    cumulus@switch$ ip link show bond1
    222: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-v1 state UP mode DORMANT 
        link/ether 08:9e:01:ce:e4:13 brd ff:ff:ff:ff:ff:ff 

### Mode Type

The default **mode type** has the name *DEFAULT*. When an interface is in DEFAULT mode, the interface state transitions to UP when it meets the following condition:

- Link detected

When an interface is in *DORMANT* mode, there are additional criteria for the interface state to transition to UP. In DORMANT mode, the interface state transitions to UP when it meets both of the following conditions:

- Link detected
- MLAG finishes setting up everything for the bond

### Link State

In the context of *link state*, DORMANT indicates the interface is not in a condition to pass packets but is instead in a "pending" state waiting for some external event. For an interface to be usable for forwarding, it should be in an UP state as it is in the output shown above.

## Resolution

You should expect to see `mode DORMANT` in the output of `ip link show` for MLAG bond downlinks. To forward traffic on those interfaces, ensure that the bond link state is `state UP`.

### Example with Link State UP and Mode Type DORMANT

Here is sample output of an MLAG interface (bond1, the downlink), where everything is working as designed. swp7 and swp8 are members of bond1:

    cumulus@switch$ ip link show bond1
    222: bond1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-v1 state UP mode DORMANT 
        link/ether 08:9e:01:ce:e4:13 brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ ip link show swp7 
    9: swp7: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT qlen 500 
        link/ether 08:9e:01:ce:e4:13 brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ ip link show swp8
    10: swp8: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond1 state UP mode DEFAULT qlen 500 
        link/ether 08:9e:01:ce:e4:13 brd ff:ff:ff:ff:ff:ff

### Example with Link State UP and Mode Type DEFAULT

Here is sample output of an MLAG peerlink (bond0) where everything is working as designed. swp3 and swp4 are members of bond0. Notice that this peerlink is in DEFAULT mode and not DORMANT mode, because it is not the MLAG downlink &mdash; it is the interface that interconnects the MLAG peers.

    cumulus@switch$ ip link show bond0
    220: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-v1 state UP mode DEFAULT 
        link/ether 08:9e:01:ce:e4:0e brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ ip link show swp3 
    5: swp3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500 
        link/ether 08:9e:01:ce:e4:0e brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ ip link show swp4
    6: swp4: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500 
        link/ether 08:9e:01:ce:e4:0e brd ff:ff:ff:ff:ff:ff

### Example with Link State DORMANT and Mode Type DORMANT

Here is sample output of a bond (bond2) where swp5 is a member of bond2. Notice that this interface is in DORMANT state and also DORMANT mode, because the bond is not yet functional.  It does not pass traffic because the bond is in DORMANT state.

    cumulus@switch$ ip link show bond2
    281: bond2: <NO-CARRIER,BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state DORMANT mode DORMANT 
        link/ether 08:9e:01:ce:e4:10 brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ ip link show swp5 
    7: swp5: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond2 state UP mode DEFAULT qlen 500 
        link/ether 08:9e:01:ce:e4:10 brd ff:ff:ff:ff:ff:ff

## Additional Resources

For additional reading, refer to the following resources:

- {{<exlink url="https://tools.ietf.org/html/rfc2863" text="RFC 2863">}}
- {{<exlink url="https://www.kernel.org/doc/Documentation/networking/operstates.txt" text="kernel.org documentation on operational states">}}
