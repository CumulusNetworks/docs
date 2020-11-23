---
title: Migrating from LNV to EVPN
author: NVIDIA
weight: 60
toc: 3
---
Lightweight network virtualization (LNV) is deprecated in Cumulus Linux 4.0 in favor of Ethernet virtual private networks ({{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}) to enable interoperability with switches from other manufacturers, to commit to industry standards, and because the benefits of EVPN outweigh those of LNV.

If your network is configured for LNV, you need to migrate your network configuration to a BGP EVPN configuration that is functionally equivalent **before** you upgrade to Cumulus Linux 4.0 or later.

## Migration Considerations

You *cannot* run LNV and EVPN at the same time for the following reasons:

- It is *not* possible to reconcile the bridge-learning configuration on all of the VTEP interfaces if both LNV and EVPN are enabled at the same time. LNV requires MAC learning to be enabled on the VXLAN VTEP interfaces. EVPN requires MAC learning to be *disabled* on the VXLAN VTEP interfaces.
- The Linux bridge installs MAC address entries differently when LNV is enabled than when EVPN is enabled. Different flags are set on the MAC addresses in the Linux kernel depending on how the address is learned. Duplicate and/or conflicting bridge entries and race conditions become a possibility when both are enabled at the same time. Because the kernel bridging table is the basis for programming the forwarding ASICs, this might lead to downstream inconsistencies in the hardware forwarding tables.
- The standard IPv4 unicast address family is commonly used to route inside the fabric for spine and leaf Clos networks. Because FRRouting does not currently support BGP dynamic capability negotiation, enabling the EVPN address family requires all of the neighbors to restart for the changes to take effect. This results in a brief disruption to traffic forwarding.

## Upgrade to EVPN

Use automation, such as Ansible to upgrade to EVPN. Automation ensures minimal downtime, reduces human error, and is useful at almost any scale.

Using {{<link url="Network-Command-Line-Utility-NCLU" text="NCLU">}} to update the configuration provides several benefits:

- NCLU restarts services and reloads interfaces automatically so the changes can take effect.
- With the transactional commit model of NCLU, the order in which the NCLU commands are entered is of no consequence. This further reduces complexity and hidden dependencies.

The upgrade steps described here are based on the following example topology (based on the {{<exlink url="https://github.com/CumulusNetworks/cldemo-vagrant" text="Reference Topology">}}):

{{< img src = "/images/cumulus-linux/lnv-to-evpn-topo.png" >}}

This topology:

- Uses {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} to accommodate dual-attached servers
- Uses active-active (anycast) mode for VXLAN VTEPs (leaf and exit nodes)
- LNV service nodes (`vxsnd`) run in anycast mode on all spines
- Vlan13 and Vlan24 are extended between the two racks (leaf01 and leaf02) and (leaf03 and leaf04)
- VXLAN routing uses {{<link url="Inter-subnet-Routing" text="centralized routing">}} at the exit nodes

The BGP EVPN configuration for a centralized routing topology is slightly different on the exit/routing leafs compared to the other ToR leaf switches.

1. Run the following NCLU commands on each type of device shown (leaf, exit, spine):

    **Leaf node NCLU commands**

    ```
    # BGP changes
    cumulus@switch:~$ net add bgp l2vpn evpn neighbor swp51-52 activate
    cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni

    # Disable MAC learning on VNI
    cumulus@switch:~$ net add vxlan vni-13 bridge learning off
    cumulus@switch:~$ net add vxlan vni-24 bridge learning off

    # Remove LNV (vxrd) configuration
    cumulus@switch:~$ net del loopback lo vxrd-src-ip
    cumulus@switch:~$ net del loopback lo vxrd-svcnode-ip
    ```

    **Exit node NCLU commands**

    ```
    # BGP changes
    cumulus@switch:~$ net add bgp l2vpn evpn neighbor swp51-52 activate
    cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
    cumulus@switch:~$ net add bgp l2vpn evpn advertise-default-gw

    # Disable MAC learning on VNI
    cumulus@switch:~$ net add vxlan vni-13 bridge learning off
    cumulus@switch:~$ net add vxlan vni-24 bridge learning off

    # Remove LNV (vxrd) configuration
    cumulus@switch:~$ net del loopback lo vxrd-src-ip
    cumulus@switch:~$ net del loopback lo vxrd-svcnode-ip
    ```

    **Spine node NCLU commands**

    ```
    # BGP changes
    cumulus@switch:~$ net add bgp l2vpn evpn neighbor swp1-4 activate

    # Remove LNV service node (vxsnd) configuration
    cumulus@switch:~$ net del lnv service-node anycast-ip 10.0.0.200
    cumulus@switch:~$ net del lnv service-node peers 10.0.0.21 10.0.0.22
    cumulus@switch:~$ net del lnv service-node source [primary-loopback-ip]

    # Remove unused LNV anycast address 10.0.0.200
    cumulus@switch:~$ net del loopback lo ip address 10.0.0.200/32
    cumulus@switch:~$ net del bgp ipv4 unicast network 10.0.0.200/32
    ```

2. Manually disable and stop the LNV daemons. NCLU can remove the LNV configuration from the configuration files, but you must manually stop and disable these daemons before you commit the NCLU changes. After you commit the NCLU changes, NCLU restarts the BGP daemon, which enables the EVPN address family.

    {{%notice note%}}

Traffic loss can start to occur at this point.

    {{%/notice%}}

3. To disable and stop the LNV registration daemon, run the following commands on the leaf and exit nodes:

    ```
    cumulus@switch:~$ sudo systemctl disable vxrd
    cumulus@switch:~$ sudo systemctl stop vxrd
    ```

4. To disable and stop the LNV service node daemon, run the following commands on the spine nodes:

    ```
    cumulus@switch:~$ sudo systemctl disable vxsnd
    cumulus@switch:~$ sudo systemctl stop vxsnd
    ```

5. To commit and apply the pending NCLU changes, run the following command on all the nodes:

    ```
    cumulus@switch:~$ net commit
    ```

## Verify the Upgrade

To check that LNV is disabled, run the `net show lnv` command on any node. This command returns no output when LNV is disabled.

{{%notice note%}}

This command is for verification on Cumulus Linux 3.x only. This command has been removed in Cumulus Linux 4.0 and does not work after you upgrade.

{{%/notice%}}

```
cumulus@switch:~$ net show lnv
```

To ensure that EVPN BGP neighbors are up, run the `net show bgp l2vpn summary` command:

```
cumulus@switch:~$ net show bgp l2vpn evpn summary
BGP router identifier 10.0.0.11, local AS number 65011 vrf-id 0
BGP table version 0
RIB entries 23, using 3496 bytes of memory
Peers 2, using 39 KiB of memory
Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
spine01(swp51)  4      65020   10932   11064        0    0    0 00:14:28           48
spine02(swp52)  4      65020   10938   11068        0    0    0 00:14:27           48
Total number of neighbors 2
```

To examine the EVPN routes, run the `net show bgp l2vpn evpn route` command. Because a MAC address only appears as a type-2 route if the host has generated traffic and its MAC is learned by the local EVPN-enabled switch, a host that does not send any traffic does not create a type-2 EVPN route until it sends a frame that ingresses the
EVPN-enabled local switch.

```
cumulus@switch:~$ net show bgp l2vpn evpn route  
BGP table version is 45, local router ID is 10.0.0.11
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[ESI]:[EthTag]:[IPlen]:[IP]
    Network          Next Hop            Metric LocPrf Weight Path
Route Distinguisher: 10.0.0.11:2
*> [2]:[0]:[0]:[48]:[00:03:00:11:11:01]
                    10.0.0.100                         32768 i
*> [2]:[0]:[0]:[48]:[02:03:00:11:11:01]
                    10.0.0.100                         32768 i
*> [2]:[0]:[0]:[48]:[02:03:00:11:11:02]
                    10.0.0.100                         32768 i
*> [3]:[0]:[32]:[10.0.0.100]
                    10.0.0.100                         32768 i
Route Distinguisher: 10.0.0.11:3
*> [2]:[0]:[0]:[48]:[00:03:00:22:22:02]
                    10.0.0.100                         32768 i
*> [2]:[0]:[0]:[48]:[02:03:00:22:22:01]
                    10.0.0.100                         32768 i
*> [2]:[0]:[0]:[48]:[02:03:00:22:22:02]
                    10.0.0.100                         32768 i
*> [3]:[0]:[32]:[10.0.0.100]
                    10.0.0.100                         32768 i
Route Distinguisher: 10.0.0.13:2
*  [2]:[0]:[0]:[48]:[00:03:00:33:33:01]
                    10.0.0.101                             0 65020 65013 i
*> [2]:[0]:[0]:[48]:[00:03:00:33:33:01]
                    10.0.0.101                             0 65020 65013 i
*  [2]:[0]:[0]:[48]:[02:03:00:33:33:01]
                    10.0.0.101                             0 65020 65013 i
*> [2]:[0]:[0]:[48]:[02:03:00:33:33:01]
                    10.0.0.101                             0 65020 65013 i
*  [2]:[0]:[0]:[48]:[02:03:00:33:33:02]
                    10.0.0.101                             0 65020 65013 i
*> [2]:[0]:[0]:[48]:[02:03:00:33:33:02]
                    10.0.0.101                             0 65020 65013 i
*  [3]:[0]:[32]:[10.0.0.101]
                    10.0.0.101                             0 65020 65013 i
*> [3]:[0]:[32]:[10.0.0.101]
                    10.0.0.101                             0 65020 65013 i
...
```

{{%notice tip%}}

You can filter the EVPN route output by route type. The multicast route type corresponds to type-3. The prefix route type is type-5 (but is not used here).

```
cumulus@switch:~$ net show bgp l2vpn evpn route type 
   macip      : MAC-IP (Type-2) route
   multicast  : Multicast
   prefix     : An IPv4 or IPv6 prefix
```

{{%/notice%}}

In the EVPN route output below, Cumulus Linux learned 00:03:00:33:33:01 with a next-hop (VTEP IP address) of 10.0.0.101. The MAC address of server03 is 00:03:00:33:33:01.

```
cumulus@leaf01:~$ net show bgp l2vpn evpn route
...

Route Distinguisher: 10.0.0.13:2
*  [2]:[0]:[0]:[48]:[00:03:00:33:33:01]
                     10.0.0.101                             0 65020 65013 i
...
```

To ensure the type-2 route is installed in the bridge table, run the `net show bridge macs <mac-address>` command on leaf01:

```
cumulus@leaf01:~$ net show bridge macs 00:03:00:33:33:01
VLAN      Master  Interface  MAC                TunnelDest  State  Flags          LastSeen
--------  ------  ---------  -----------------  ----------  -----  -------------  --------
13        bridge  vni-13     00:03:00:33:33:01                     offload        00:01:49
untagged          vni-13     00:03:00:33:33:01  10.0.0.101         self, offload  00:01:49
```
