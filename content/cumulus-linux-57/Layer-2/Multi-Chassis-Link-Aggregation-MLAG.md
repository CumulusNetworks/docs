---
title: Multi-Chassis Link Aggregation - MLAG
author: NVIDIA
weight: 490
toc: 3
---
{{%notice note%}}
**MLAG or CLAG**: Other vendors refer to the Cumulus Linux implementation of <span style="background-color:#F5F5DC">[MLAG](## "Multi-chassis Link Aggregation")</span> as CLAG, MC-LAG or VPC. You even see references to CLAG in Cumulus Linux, including the management daemon, named `clagd`, and other options in the code, such as `clag-id`, which exist for historical purposes. The Cumulus Linux implementation is truly a multi-chassis link aggregation protocol so this document uses MLAG.
{{%/notice%}}

<span style="background-color:#F5F5DC">[MLAG](## "Multi-chassis Link Aggregation")</span> enables a server or switch with a two-port bond, such as a link aggregation group (LAG), EtherChannel, port group or trunk, to connect those ports to different switches and operate as if they connect to a single, logical switch. This provides greater redundancy and greater system throughput.

Dual-connected devices can create LACP bonds that contain links to each physical switch; Cumulus Linux supports active-active links from the dual-connected devices even though they connect to two different physical switches.

## How Does MLAG Work?

A basic MLAG configuration looks like this:

| | |
|---|---|
|<div style="width:400px">{{< img src="/images/cumulus-linux/mlag-basic-setup.png" width="400" >}}|<br> <ul><li>The two switches, leaf01 and leaf02, known as *peer switches*, appear as a single device to the bond on server01.</li><li>server01 distributes traffic between the two links to leaf01 and leaf02 in the way you configure on the host. </li><li>Traffic inbound to server01 can traverse leaf01 or leaf02 and arrive at server01.</li></ul>|

More elaborate configurations are also possible. The number of links between the host and the switches can be greater than two and does not have to be symmetrical. Also, because the two peer switches appear as a single switch to other bonding devices, you can also connect pairs of MLAG switches to each other in a switch-to-switch MLAG configuration:

| | |
|---|---|
|<div style="width:400px">{{< img src="/images/cumulus-linux/mlag-two-pair.png" width="350" >}} |<br><br> <ul><li>leaf01 and leaf02 are also MLAG peer switches and present a two-port bond from a single logical system to spine01 and spine02.</li></ul>|
<!-- vale off -->
### LACP and Dual-connected Links
<!-- vale on -->
{{<link url="Bonding-Link-Aggregation" text="Link Aggregation Control Protocol (LACP)">}}, the IEEE standard protocol for managing bonds, verifies dual-connectedness. <span style="background-color:#F5F5DC">[LACP](## "Link Aggregation Control Protocol")</span> runs on the dual-connected devices and on each of the MLAG peer switches. On a dual-connected device, the only configuration requirement is to create a bond that LACP manages.

On each of the peer switches, you must place the links that connect to the dual-connected host or switch in the bond. This is true even if the links are a single port on each peer switch, where each port is in a bond, as shown below:

{{< img src = "/images/cumulus-linux/mlag-dual-connect.png" >}}

The dual-connected bonds on the peer switches have their system ID set to the MLAG system ID. Therefore, from the point of view of the hosts, each of the links in its bond connects to the same system and so the host uses both links.

Each peer switch periodically makes a list of the LACP partner MAC addresses for its bonds and sends that list to its peer (using the `clagd` service). The LACP partner MAC address is the MAC address of the system at the other end of a bond (server01, server02, and server03 in the figure above). When a switch receives this list from its peer, it compares the list to the LACP partner MAC addresses on its switch. If there are any matches and the `clag-id` for those bonds match, then that bond is a dual-connected bond.

### Requirements

MLAG has these requirements:

- The two peer switches with MLAG must be directly connected. This is typically a bond for increased reliability and bandwidth.
- There must be only two peer switches in one MLAG configuration, but you can have multiple configurations in a network for *switch-to-switch MLAG*.
- Both switches in the MLAG pair must be identical; they must both be the same model of switch and run the same Cumulus Linux release. See {{<link url="Upgrading-Cumulus-Linux#upgrade-switches-in-an-mlag-pair" text="Upgrading Cumulus Linux">}}.
- The dual-connected devices (servers or switches) can use LACP (IEEE 802.3ad or 802.1ax) to form the {{<link url="Bonding-Link-Aggregation" text="bond">}}. In this case, the peer switches must also use LACP.

{{%notice note%}}
- MLAG is *not* supported in a multiple VLAN-aware bridge configuration.
- Both MLAG peers must use the same {{<link url="VXLAN-Devices" text="VXLAN device type">}} (single or traditional).
{{%/notice%}}

## Basic Configuration

To configure MLAG, you need to create a bond that uses LACP on the dual-connected devices and configure the interfaces (including bonds, VLANs, bridges, and peer links) on each peer switch. Follow these steps on each peer switch in the MLAG pair:

1. On the dual-connected device, such as a host or server that sends traffic to and from the switch, create a bond that uses LACP. The method you use varies with the type of device you are configuring.

   {{%notice note%}}
If you cannot use LACP in your environment, you can configure the bonds in {{<link url="Bonding-Link-Aggregation" text="balance-xor mode">}}.
{{%/notice%}}

2. Place every interface that connects to the MLAG pair from a dual-connected device into a {{<link url="Bonding-Link-Aggregation" text="bond">}}, even if the bond contains only a single link on a single physical switch.

   The following examples place swp1 in bond1 and swp2 in bond2.

    {{< tabs "TabID70 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond1 description bond1-on-swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond2 description bond2-on-swp1
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the following lines to the `/etc/network/interfaces` file. The example also adds a description for the bonds (an alias), which is optional.

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    alias bond1 on swp1
    bond-slaves swp1
...

auto bond2
iface bond2
    alias bond2 on swp2
    bond-slaves swp2
...
```

{{< /tab >}}
{{< /tabs >}}

3. Add a unique MLAG ID to each bond.

   You must specify a unique MLAG ID (clag-id) for every dual-connected bond on each peer switch so that switches know which links dual-connect or connect to the same host or switch. The value must be between 1 and 65535 and must be the same on both peer switches. A value of 0 disables MLAG on the bond.

   The example commands below add an MLAG ID of 1 to bond1 and 2 to bond2:

    {{< tabs "TabID123 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2 
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/network/interfaces` file, add the line `clag-id 1` to the `auto bond1` stanza and `clag-id 2` to `auto bond2` stanza:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto bond1
iface bond1
    alias bond1 on swp1
    bond-slaves swp1
    clag-id 1

auto bond2
iface bond2
    alias bond2 on swp2
    bond-slaves swp2
    clag-id 2
...
```

{{< /tab >}}
{{< /tabs >}}

4. Add the bonds you created above to a bridge. The example commands below add bond1 and bond2 to a VLAN-aware bridge.

   You must add **all** VLANs configured on the MLAG bond to the bridge so that traffic to the downstream device connected in MLAG redirects over the peerlink in case the MLAG bond fails.

   {{< tabs "TabID150 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set interface bond1-2 bridge domain br_default 
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the `bridge-ports bond1 bond2` lines to the `auto bridge` stanza:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports bond1 bond2
    bridge-vlan-aware yes
...
```

{{< /tab >}}
{{< /tabs >}}

5. Create the inter-chassis bond and the peer link VLAN (as a VLAN subinterface). You also need to provide the peer link IP address, the MLAG bond interfaces, the MLAG system MAC address, and the backup interface.
   - By default, Cumulus Linux configures the inter-chassis bond with the name *peerlink* and the peer link VLAN with the name *peerlink.4094*. Use *peerlink.4094* to ensure that the VLAN is independent of the bridge and spanning tree forwarding decisions.
   - The peer link IP address is a link-local address that provides layer 3 connectivity between the peer switches.
   - NVIDIA provides a reserved range of MAC addresses for MLAG (between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff). Use a MAC address from this range to prevent conflicts with other interfaces in the same bridged network.
      - Do not to use a multicast MAC address.
      - Do not use the same MAC address for different MLAG pairs; make sure you specify a different MAC address for each MLAG pair in the network.  
   - The backup IP address is any layer 3 backup interface for the peer link, which the switch uses when the peer link goes down. You must add the backup IP address, which **must** be different than the peer link IP address. Make sure that any route that does not use the peer link can reach the backup IP address. Use the loopback or management IP address of the switch.
      {{< expand "Loopback or Management IP Address?" >}}
- If your MLAG configuration has **bridged uplinks** (such as a campus network or a large, flat layer 2 network), use the peer switch **eth0** address. When the peer link is down, the secondary switch routes towards the eth0 address using the OOB network (provided you have implemented an OOB network).
- If your MLAG configuration has **routed uplinks** (a modern approach to the data center fabric network), use the peer switch **loopback** address. When the peer link is down, the secondary switch routes towards the loopback address using uplinks (towards the spine layer). If the primary switch also has a more significant problem (for example, `switchd` does not respond or stops), the secondary switch promotes itself to primary and the traffic flows.

   {{%notice note%}}
When using BGP, to ensure IP connectivity between the loopbacks, the MLAG peer switches must use unique BGP ASNs; if they use the same ASN, you must bypass the BGP loop prevention check on the `AS_PATH` attribute.
{{%/notice%}}

{{< /expand >}}

   The following examples show commands for both MLAG peers (leaf01 and leaf02).

   {{< tabs "TabID222 ">}}
{{< tab "NVUE Commands ">}}

   {{< tabs "TabID223 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv config apply
```

To configure the backup link to a VRF, include the name of the VRF with the `backup-ip` parameter. The following example configures the backup link to VRF `mgmt`:

```
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2 vrf mgmt
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set mlag mac-address 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv config apply
```

To configure the backup link to a VRF, include the name of the VRF with the backup-ip parameter. The following example configures the backup link to VRF `mgmt`:

```
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1 vrf mgmt
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the following parameters, then run the `sudo ifreload -a` command.
- The inter-chasis bond (`peerlink`) with two ports in the bond (swp49 and swp50 in the example command below)
- The `peerlink` bond to the bridge
- The peer link VLAN (`peerlink.4094`) with the backup IP address, the peer link IP address (`linklocal`), and the MLAG system MAC address (from the reserved range of addresses).

   {{< tabs "TabID315 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink
    bridge-vlan-aware yes
...
auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:BE:EF:AA
...
```

To configure the backup link to a VRF, include the name of the VRF with the `clagd-backup-ip` parameter. The following example configures the backup link to VRF RED:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.2 vrf RED
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:BE:EF:AA
...
```

Run the `sudo ifreload -a` command to apply all the configuration changes:

```
cumulus@leaf01:~$ sudo ifreload -a
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports bond1 bond2 peerlink
    bridge-vlan-aware yes
...
auto peerlink
iface peerlink
    bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.1
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:BE:EF:AA
...
```

To configure the backup link to a VRF, include the name of the VRF with the `clagd-backup-ip` parameter. The following example configures the backup link to VRF RED:

```
cumulus@leaf02:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.1 vrf RED
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:BE:EF:AA
...
```

Run the `sudo ifreload -a` command to apply all the configuration changes:

```
cumulus@leaf02:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- Do *not* add VLAN 4094 to the bridge VLAN list; You **cannot** configure VLAN 4094 for the peer link subinterface as a bridged VLAN with bridge VIDs under the bridge.
- Do not use 169.254.0.1 as the MLAG peer link IP address; Cumulus Linux uses this address for {{<link url="Border-Gateway-Protocol-BGP#bgp-unnumbered" text="BGP unnumbered">}} interfaces.
- When you configure MLAG manually in the `/etc/network/interfaces` file, the changes take effect when you bring the peer link interface up with the `sudo ifreload -a` command. Do **not** use `systemctl restart clagd.service` to apply the new configuration.
- The MLAG bond does not support layer 3 configuration.
{{%/notice%}}

MLAG synchronizes the dynamic state between the two peer switches but it does not synchronize the switch configurations. After modifying the configuration of one peer switch, you must make the same changes to the configuration on the other peer switch. This applies to all configuration changes, including:
- Port configuration, such as VLAN membership, {{<link url="#mtu-and-mlag" text="MTU">}} and bonding parameters.
- Bridge configuration, such as spanning tree parameters or bridge properties.
- Static address entries, such as static FDB entries and static IGMP entries.
- QoS configuration, such as ACL entries.

## Optional Configuration

This section describes optional configuration procedures.

### Set Roles and Priority

Each MLAG-enabled switch in the pair has a *role*. When the peering relationship establishes between the two switches, one switch goes into the *primary* role and the other into the *secondary* role. When an MLAG-enabled switch is in the secondary role, it does not send STP BPDUs on dual-connected links; it only sends BPDUs on single-connected links. The switch in the primary role sends STP BPDUs on all single- and dual-connected links.

By default, the switch determines the role by comparing the MAC addresses of the two sides of the peering link; the switch with the lower MAC address assumes the primary role. You can override this by setting the `priority` option for the peer link:

{{< tabs "TabID308 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set mlag priority 2084
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the `clagd-priority` option, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-priority 2048
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

The switch with the lower priority value is in the primary role; the default value is 32768 and the range is between 0 and 65535.

When the MLAG service exits during switch reboot or if you stop the service on the primary switch, the peer switch that is in the secondary role becomes the primary.

However, if the primary switch goes down without stopping the MLAG service or if the peer link goes down, the secondary switch does **not** change its role. If the peer switch is not alive, the switch in the secondary role rolls back the LACP system ID to be the bond interface MAC address instead of the MLAG system MAC address (`clagd-sys-mac`). The switch in the primary role uses the MLAG system MAC address as the LACP system ID on the bonds.

### Set clagctl Timers

The `clagd` service has several timers that you can tune for enhanced performance.

| <div style="width:250px">Timer | Description |
| ----- | ----------- |
| `--reloadTimer <seconds>` | The number of seconds to wait for the peer switch to become active. If the peer switch does not become active after the timer expires, the MLAG bonds leave the initialization ({{<link url="#peer-link-interfaces-and-the-protodown-state" text="protodown">}}) state and become active. This provides `clagd` with sufficient time to determine whether the peer switch is coming up or if it is permanently unreachable. <br>The default is 300 seconds.|
| `--peerTimeout <seconds>`<br> | The number of seconds `clagd` waits without receiving any messages from the peer switch before it determines that the peer is no longer active. At this point, the switch reverts all configuration changes so that it operates as a standard non-MLAG switch. This includes removing all statically assigned MAC addresses, clearing the egress forwarding mask, and allowing addresses to move from any port to the peer port. After a message is again received from the peer, MLAG operation restarts. If this parameter is not specified, `clagd` uses ten times the local `lacpPoll` value. |
| `--initDelay <seconds>` | The number of seconds `clagd` delays bringing up MLAG bonds and anycast IP addresses. <br>The default is 180 seconds. NVIDIA recommends you set this parameter to 300 seconds in a scaled environment.<br>This timer sets to 0 automatically under the following conditions:<ul><li>When the peer is not alive and the backup link is not active after a reload timeout</li><li>When the peer sends a goodbye (through the peer link or the backup link)</li><li>When both MLAG sessions come up at the same time</li></ul>|
| `--sendTimeout <seconds>` | The number of seconds `clagd` waits until the sending socket times out. If it takes longer than the `sendTimeout` value to send data to the peer, `clagd` generates an exception. <br>The default is 30 seconds. |
| `--lacpPoll <seconds>` | The number of seconds `clagd` waits before obtaining local LACP information. <br>The default is 2 seconds.|

{{< tabs "TabID363 ">}}
{{< tab "NVUE Commands ">}}

The only timer you can set with NVUE is the initial delay timer. The following example NVUE Command sets the initial delay to 100 seconds:

```
cumulus@leaf01:~$ nv set mlag init-delay 100
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To set the `clagd` timers, edit the `/etc/network/interfaces` file to add the `clagd-args --<timer>` line to the peerlink.4094 stanza, then run the `ifreload -a` command.

The following example command sets the initial delay timer to 100 seconds:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-args --initDelay 100
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-priority 2048
...
```

```
cumulus@leaf01:~$ sudo ifreload -a
```

The following example command sets the peer timeout to 900 seconds:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-args --peerTimeout 900
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-priority 2048
...
```

```
cumulus@leaf01:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

### Configure MLAG with a Traditional Bridge

To configure MLAG with a traditional mode bridge instead of a {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware mode bridge">}}, you must configure the peer link and all dual-connected links as {{<link url="Traditional-Bridge-Mode" text="untagged (native)">}} ports on a bridge (note the absence of any VLANs in the `bridge-ports` line and the lack of the `bridge-vlan-aware` parameter below):

```
...
auto br0
iface br0
    bridge-ports peerlink bond1 bond2
...
```

The following example shows you how to allow VLAN 10 across the peer link:

```
...
auto br0.10
iface br0.10
    bridge-ports peerlink.10 bond1.10 bond2.10
    bridge-stp on
...
```

{{%notice note%}}
In an MLAG and traditional bridge configuration, NVIDIA recommends that you set bridge learning to off on all VLANs over the peerlink except for the layer 3 peer link subinterface; for example:

```
...
auto peerlink
iface peerlink
    bridge-learning off
    
auto peerlink.1510
iface peerlink.1510
    bridge-learning off

auto peerlink.4094
iface peerlink.4094
...
```

{{%/notice%}}

### Configure a Backup UDP Port

By default, Cumulus Linux uses UDP port 5342 with the backup IP address. To change the backup UDP port, edit the `/etc/network/interfaces` file to add `clagd-args --backupPort <port>` to the `auto peerlink.4094` stanza. For example:

```
...
auto peerlink.4094
iface peerlink.4094
    clagd-args --backupPort 5400
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:BE:EF:AA
...
```

Run the `sudo ifreload -a` command to apply all the configuration changes:

```
cumulus@leaf01:~$ sudo ifreload -a
```
<!-- vale off -->
## Unconfigure MLAG
<!-- vale on -->
To unconfigure MLAG:

{{< tabs "TabID532 ">}}
{{< tab "NVUE Commands ">}}

Run the following commands to unset MLAG, and unset the peerlink and the peerlink VLAN subinterface that Cumulus Linux creates automatically. You must run the commands at the same time with the `nv config apply` command.

```
cumulus@leaf01:~$ nv unset mlag
cumulus@leaf01:~$ nv unset interface peerlink
cumulus@leaf01:~$ nv unset interface peerlink.4094
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file.

1. Remove the `auto peerlink` stanza; for example, remove lines similar to the following:

  ```
  ...
  auto peerlink
  iface peerlink
      bond-slaves swp49 swp50
  auto peerlink.4094
  iface peerlink.4094
  clagd-backup-ip 10.10.10.2
  clagd-peer-ip linklocal
  clagd-sys-mac 44:38:39:BE:EF:AA
  ...
  ```

2. Remove the `clag-id` line from the bond stanzas. In the following example, remove `clag-id 1` from the `auto bond1` stanza and `clag-id 2` from the `auto bond2` stanza:

  ```
  ...
  auto bond1
  iface bond1
      alias bond1 on swp1
      bond-slaves swp1
      clag-id 1

  auto bond2
  iface bond2
      alias bond2 on swp2
      bond-slaves swp2
      clag-id 2
  ...
  ```

3. Remove `peerlink` from the `bridge-ports` line of the bridge stanza. In the following example, remove `peerlink` from the `auto br_default` stanza:

  ```
  auto br_default
  iface br_default
      bridge-ports bond1 bond2 peerlink
      bridge-vlan-aware yes
  ```

4. Run the `sudo ifreload -a` command:

  ```
  cumulus@leaf01:~$ sudo ifreload -a
  ```

{{< /tab >}}
{{< /tabs >}}

## Best Practices

Follow these best practices when configuring MLAG on your switches.

### MTU and MLAG

The bridge MTU determines the {{<link url="Switch-Port-Attributes#mtu" text="MTU">}} in MLAG traffic. The lowest MTU setting of an interface that is a member of the bridge determines the bridge MTU. If you want to set an MTU other than the default of 9216 bytes, you must configure the MTU on each physical interface and the bond interface that is a member of every MLAG bridge in the entire bridged domain.

The following example commands set an MTU of 1500 for each of the bond interfaces (peer link, uplink, bond1, bond2), which are members of bridge *bridge*:

{{< tabs "TabID498 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set interface peerlink.4094 link mtu 1500
cumulus@leaf01:~$ nv set interface uplink link mtu 1500
cumulus@leaf01:~$ nv set interface bond1 link mtu 1500
cumulus@leaf01:~$ nv set interface bond2 link mtu 1500
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto br_default
iface br_default
    bridge-ports peerlink uplink bond1 bond2

auto peerlink
iface peerlink
    mtu 1500

auto bond1
iface bond1
    mtu 1500

auto bond2
iface bond2
    mtu 1500

auto uplink
iface uplink
    mtu 1500
...
```

```
cumulus@leaf01:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

### STP and MLAG

Always enable <span style="background-color:#F5F5DC">[STP](## "Spanning Tree Protocol")</span> in your layer 2 network and {{<link title="Spanning Tree and Rapid Spanning Tree - STP#bpdu-guard" text="BPDU Guard">}} on the host-facing bond interfaces.

- The STP global configuration must be the same on both peer switches.
- The STP configuration for dual-connected ports must be the same on both peer switches.
- The STP priority must be the same on both peer switches.
- In a multiple bridge configuration, the STP priority must be the same on all bridges on both peer switches.
- To minimize convergence times when a link transitions to the forwarding state, configure the edge ports (for tagged and untagged frames) with PortAdminEdge and BPDU guard enabled.
- Do not use a multicast MAC address for the LACP ID on systems connected to MLAG bonds; the switch drops STP BPDUs from a multicast MAC address.

### Peer Link Sizing

The peer link carries little traffic when compared to the bandwidth consumed by data plane traffic. In a typical MLAG configuration, most connections between the two switches in the MLAG pair are dual-connected; the only traffic going across the peer link is traffic from the `clagd` process and some LLDP or LACP traffic. The switch does not forward traffic received on the peer link out of the dual-connected bonds.

However, there are some instances where a host connects to only one switch in the MLAG pair; for example:

- You have a hardware limitation on the host where there is only one PCIE slot, and therefore, one NIC on the system, so the host is only single-connected across that interface.
- The host does not support 802.3ad and you cannot create a bond on it.
- You are accounting for a link failure, where the host becomes single connected until the failure resolves.

Determine how much bandwidth is traveling across the single-connected interfaces and set half of that bandwidth to the peer link. On average, one half of the traffic destined to the single-connected host arrives on the switch directly connected to the single-connected host and the other half arrives on the switch that is not directly connected to the single-connected host. When this happens, only the traffic that arrives on the switch that is not directly connected to the single-connected host needs to traverse the peer link.

In addition, you can add extra links to the peer link bond to handle link failures in the peer link bond itself.

| | |
|---|---|
|<div style="width:600px">{{< img src="/images/cumulus-linux/mlag-peerlink-sizing.png" width="800" >}}| <br><ul><li>Each host has two 10G links, with each 10G link going to each switch in the MLAG pair. </li><li>Each host has 20G of dual-connected bandwidth; all three hosts have a total of 60G of dual-connected bandwidth. </li><li>Set at least 15G of bandwidth for each peer link bond, which represents half of the single-connected bandwidth.</li></ul>

When planning for link failures for a full rack, you need only set enough bandwidth to meet your site strategy for handling failure scenarios. For example, for a full rack with 40 servers and two switches, you can plan for four to six servers to lose connectivity to a single switch and become single connected before you respond to the event. Therefore, if you have 40 hosts each with 20G of bandwidth dual-connected to the MLAG pair, you can set between 20G and 30G of bandwidth to the peer link, which accounts for half of the single-connected bandwidth for four to six hosts.

### Peer Link Routing

When enabling a routing protocol in an MLAG environment, it is also necessary to manage the uplinks; by default MLAG is not aware of layer 3 uplink interfaces. If there is a peer link failure, MLAG does not remove static routes or bring down a BGP or OSPF adjacency unless you use a separate link state daemon such as `ifplugd`.

When you use MLAG with VRR, set up a routed adjacency across the peerlink.4094 interface. If a routed connection is not built across the peer link, during an uplink failure on one of the switches in the MLAG pair, egress traffic does not forward if the destination is on the switch whose uplinks are down.

To set up the adjacency, configure a {{<link url="Border-Gateway-Protocol-BGP#bgp-unnumbered" text="BGP">}} or {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} unnumbered peering, as appropriate for your network.

{{%notice note%}}
- For switches with the Spectrum ASIC, the {{<link url="#large-packet-drops-on-the-peer-link-interface" text="MLAG loop avoidance mechanism">}} also drops routed traffic that arrives on an MLAG peer link interface and routes to a dual-connected VNI. If you need to route unencapsulated traffic to an MLAG peer switch for VXLAN forwarding to accommodate uplink failures or other design needs, configure a routing adjacency across a separate routed interface that is not the MLAG `peerlink`.
- Switches with the Spectrum-2 ASIC and later allow packets arriving on the peer link to route to a VNI for VXLAN encapsulation.
{{%/notice%}}

For BGP, use a configuration like this:

{{< tabs "TabID704 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router bgp neighbor peerlink.4094 remote-as internal
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor peerlink.4094 remote-as external
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

If you are using {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}} and MLAG, you need to enable the EVPN address family across the peerlink.4094 interface as well:

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor peerlink.4094 remote-as external
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# neighbor peerlink.4094 activate
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

For OSPF, use a configuration like this:

```
cumulus@leaf01:~$ nv set interface peerlink.4094 router ospf area 0.0.0.1
cumulus@leaf01:~$ nv config apply
```

### MLAG Routing Support

In addition to the routing adjacency over the [peer link](#peer-link-routing), Cumulus Linux supports routing adjacencies from attached network devices to MLAG switches under the following conditions:
- The router must physically attach to a single interface of a switch.
- The attached router must peer directly to a local address on the physically connected switch.

{{%notice note%}}
The router cannot:
- Attach to the switch over a MLAG bond interface.
- Form routing adjacencies to a virtual address (VRR or VRRP).
{{%/notice%}}

{{< figure src="/images/cumulus-linux/mlag-supported-routing.png" width="700" >}}

## Troubleshooting

Use the following troubleshooting tips to check MLAG configuration.

### Check MLAG Status

To verify MLAG configuration, run the `nv show mlag` command:

```
cumulus@leaf01:mgmt:~$ nv show mlag
                operational              applied            description
--------------  -----------------------  -----------------  ------------------------------------------------------
enable                                   on                 Turn the feature 'on' or 'off'.  The default is 'off'.
debug                                    off                Enable MLAG debugging
init-delay                               100                The delay, in seconds, before bonds are brought up.
mac-address     44:38:39:be:ef:aa        44:38:39:BE:EF:AA  Override anycast-mac and anycast-id
peer-ip         fe80::4638:39ff:fe00:5a  linklocal          Peer Ip Address
priority        32768                    32768              Mlag Priority
[backup]        10.10.10.2               10.10.10.2         Set of MLAG backups
backup-active   False                                       Mlag Backup Status
backup-reason                                               Mlag Backup Reason
local-id        44:38:39:00:00:59                           Mlag Local Unique Id
local-role      primary                                     Mlag Local Role
peer-alive      True                                        Mlag Peer Alive Status
peer-id         44:38:39:00:00:5a                           Mlag Peer Unique Id
peer-interface  peerlink.4094                               Mlag Peerlink Interface
peer-priority   32768                                       Mlag Peer Priority
peer-role       secondary                                   Mlag Peer Role
```

Run the `net show mlag` command or the `clagctl` command to show the MLAG interface information:

```
cumulus@leaf01:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 32768 44:38:39:00:00:11 primary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:12 secondary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:12 (linklocal)
                      Backup IP: 10.10.10.2 (active)
                     System MAC: 44:38:39:be:ef:aa

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
           bond1   bond1              1         -                      -
           bond2   bond2              2         -                      -
           bond3   bond3              3         -                      -
```

### Show All MLAG Settings

To see all MLAG settings, run the `clagctl params` command:

```
cumulus@leaf01:~$ clagctl params
clagVersion = 1.4.0
clagDataVersion = 1.4.0
clagCmdVersion = 1.1.0
peerIp = linklocal
peerIf = peerlink.4094
sysMac = 44:38:39:be:ef:aa
lacpPoll = 2
currLacpPoll = 2
peerConnect = 1
cmdConnect = 1
peerLinkPoll = 1
switchdReadyTimeout = 120
reloadTimer = 300
periodicRun = 4
priority = 32768
quiet = False
debug = 0x0
verbose = False
log = syslog
vm = True
peerPort = 5342
peerTimeout = 20
initDelay = 100
sendTimeout = 30
...
```

### View the MLAG Log File

By default, when running, the `clagd` service logs status messages to the `/var/log/clagd.log` file and to `syslog`:

```
cumulus@spine01:~$ sudo tail /var/log/clagd.log
2016-10-03T20:31:50.471400+00:00 spine01 clagd[1235]: Initial config loaded
2016-10-03T20:31:52.479769+00:00 spine01 clagd[1235]: The peer switch is active.
2016-10-03T20:31:52.496490+00:00 spine01 clagd[1235]: Initial data sync to peer done.
2016-10-03T20:31:52.540186+00:00 spine01 clagd[1235]: Role is now primary; elected
2016-10-03T20:31:54.250572+00:00 spine01 clagd[1235]: HealthCheck: role via backup is primary
2016-10-03T20:31:54.252642+00:00 spine01 clagd[1235]: HealthCheck: backup active
2016-10-03T20:31:54.537967+00:00 spine01 clagd[1235]: Initial data sync from peer done.
2016-10-03T20:31:54.538435+00:00 spine01 clagd[1235]: Initial handshake done.
2016-10-03T22:47:35.255317+00:00 spine01 clagd[1235]: leaf01-02 is now dual connected.
```

### Monitor the clagd Service

Due to the critical nature of the `clagd` service, `systemd` continuously monitors its status by receiving notify messages every 30 seconds. If the `clagd` service terminates or becomes unresponsive for any reason and `systemd` receives no messages after 60 seconds, `systemd` restarts the `clagd` service. `systemd` logs these failures in the `/var/log/syslog` file and, on the first failure, also generates a `cl-support`file.

Monitoring occurs automatically as long as:
- You enable the `clagd` service.
- You configure the peer IP address (`clagd-peer-ip`), the MLAG system MAC address (`clagd-sys-mac`), and the backup IP address (`clagd-backup-ip`) for an interface.
- The `clagd` service is running. If you stop `clagd` with the `systemctl stop clagd.service` command, `clagd` monitoring also stops.

You can check if `clagd` is running with the `systemctl status` command:

```
cumulus@leaf01:~$ systemctl status clagd.service
 ● clagd.service - Cumulus Linux Multi-Chassis LACP Bonding Daemon
    Loaded: loaded (/lib/systemd/system/clagd.service; enabled)
    Active: active (running) since Fri 2021-06-11 16:17:19 UTC; 12min ago
        Docs: man:clagd(8)
    Main PID: 27078 (clagd)
    CGroup: /system.slice/clagd.service
            └─27078 /usr/bin/python3 /usr/sbin/clagd --daemon linklocal peerlink.4094 44:38:39:BE:EF:AA --priority 32768
```

### Peer Link Consistency Check

When you make an MLAG configuration change, Cumulus Linux automatically validates the corresponding parameters on both MLAG peers and takes action based on the type of conflict it sees. For every conflict, the `/var/log/clagd.log` file records a log message.

The following table shows the conflict types and actions that Cumulus Linux takes.

|  Conflict       | Type   | Action|
| --------------- | ------ | ----- |
| Bridge STP mode | Global |  Protodown only the MLAG bonds on the secondary switch when there is an <span style="background-color:#F5F5DC">[STP](## "Spanning Tree Protocol")</span> mode mismatch across peers. |
| MLAG native VLAN | Interface | Protodown only the MLAG bonds on the secondary switch when there is a native VLAN mismatch. |
| STP root bridge priority | Global | Protodown the MLAG bonds and VNIs on the secondary switch when there is an <span style="background-color:#F5F5DC">[STP](## "Spanning Tree Protocol")</span> priority mismatch across peers. |
| MLAG system MAC address | Global  | Protodown the MLAG bonds and VNIs on the secondary switch when there is an MLAG system MAC address mismatch across peers.|
| Peer IP | Global   | Protodown the MLAG bonds and VNIs on the secondary switch when there is an IP address mismatch within the same subnet between peers. The consistency checker does not trigger an IP address mismatch between the link-local keyword and a static IPv4 address, or between IPv4 addresses across subnets.|
| Peer link MTU | Global | Protodown the MLAG bonds and VNIs on the secondary switch when there is a peer link MTU mismatch across peers. |
| Peer link native VLAN | Global | Protodown the MLAG bonds and VNIs on the secondary switch when there is a peer link VLAN mismatch across peers.<br>Protodown the MLAG bonds and VNIs on the secondary switch when there is no PVID. |
| VXLAN anycast IP address | Global | Protodown the MLAG bonds and VNIs on the secondary switch when there is an anycast IP address mismatch across peers.<br>Protodown the MLAG bonds and VNIs on the node where there is no configured anycast IP address. |
| Peer link bridge member | Global | Protodown the MLAG bonds and VNIs on the MLAG switch where there is a peer link bridge member conflict.</div>{{%notice note%}}The peer value always displays `NOT-SYNCED` for this consistency check because Cumulus Linux does not enforce the same interface name for the peerlink and because of limitations with traditional bridges.{{%/notice%}} |
| MLAG bond bridge member | Interface | Protodown the MLAG bonds and VNIs on the MLAG switch if the MLAG bond is not a bridge member.</div>{{%notice note%}}The peer value always displays `NOT-SYNCED` for this consistency check because Cumulus Linux does not enforce the same interface name for the peerlink and because of limitations with traditional bridges.{{%/notice%}} |
| LACP partner MAC address | Interface | Protodown the MLAG bonds on the MLAG switch if there is an LACP partner MAC address mismatch or if there is a duplicate LACP partner MAC address. |
| MLAG VLANs| Interface   |  Suspend the inconsistent VLANs on either MLAG peer if the VLANs are not part of the peer link or if there is mismatch of VLANs configured on the MLAG bonds between the MLAG peers. |
| Peer link VLANs| Global | Suspend the inconsistent VLANs on either MLAG peer on all the dual-connected MLAG bonds and VXLAN interfaces. |
| MLAG protocol version | Global | The consistency check records an MLAG protocol version mismatch between the MLAG peers. Cumulus Linux does not take any disruptive action. |
| MLAG package version | Global| The consistency check records an MLAG package version mismatch between the MLAG peers. Cumulus Linux does not take any disruptive action.|

You can also manually check for MLAG inconsistencies with the following commands:

{{< tabs "TabID851 ">}}
{{< tab "NVUE Commands ">}}

The following example command shows global MLAG settings for each peer and indicates that the MLAG system MAC address does not match.

```
cumulus@leaf01:mgmt:~$ nv show mlag consistency-checker global
Global Consistency-checker
=============================
    Parameter               LocalValue                 PeerValue                  Conflict  Summary
    ----------------------  -------------------------  -------------------------  --------  -------
    anycast-ip              -                          -                          -                
    bridge-priority         32768                      32768                      -                
    bridge-stp              on                         on                         -                
    bridge-type             vlan-aware                 vlan-aware                 -                
    clag-pkg-version        1.6.0-cl5.7.0u2            1.6.0-cl5.7.0u2            -                
    clag-protocol-version   1.6.1                      1.6.1                      -                
    peer-ip                 fe80::4ab0:2dff:fe3c:61d1  fe80::4ab0:2dff:fe3c:61d1  -                
    peerlink-bridge-member  Yes                        Yes                        -                
    peerlink-mtu            9216                       9216                       -                
    peerlink-native-vlan    1                          1                          -                
    peerlink-vlans          1, 10, 20, 30              1, 10, 20, 30              -                
    redirect2-enable        yes                        yes                        -                
    system-mac              44:38:39:be:ef:aa          44:38:39:be:ef:aa          system mac mismatch between clag peers
```

The following example command shows MLAG settings for all interfaces on each peer with no conflicts:

```
cumulus@leaf01:mgmt:~$ nv show interface --view=mlag-cc
Interface  Conflict  LocalValue         Parameter         PeerValue
---------  --------  -----------------  ----------------  -----------------
bond1    -         yes                bridge-learning   yes
bond1    -         1                  clag-id           1
bond1    -         44:38:39:be:ef:aa  lacp-actor-mac    44:38:39:be:ef:aa
bond1    -         00:00:00:00:00:00  lacp-partner-mac  00:00:00:00:00:00
bond1    -         br_default         master            NOT-SYNCED
bond1    -         9216               mtu               9216
bond1    -         1                  native-vlan       1
bond1    -         1, 10, 20, 30      vlan-id           1, 10, 20, 30
bond2    -         yes                bridge-learning   yes
bond2    -         2                  clag-id           2
bond2    -         44:38:39:be:ef:aa  lacp-actor-mac    44:38:39:be:ef:aa
bond2    -         00:00:00:00:00:00  lacp-partner-mac  00:00:00:00:00:00
bond2    -         br_default         master            NOT-SYNCED
bond2    -         9216               mtu               9216
bond2    -         1                  native-vlan       1
bond2    -         1, 10, 20, 30      vlan-id           1, 10, 20, 30
bond3    -         yes                bridge-learning   yes
bond3    -         3                  clag-id           3
bond3    -         44:38:39:be:ef:aa  lacp-actor-mac    44:38:39:be:ef:aa
bond3    -         00:00:00:00:00:00  lacp-partner-mac  00:00:00:00:00:00
bond3    -         br_default         master            NOT-SYNCED
bond3    -         9216               mtu               9216
bond3    -         1                  native-vlan       1
bond3    -         1, 10, 20, 30      vlan-id           1, 10, 20, 30
```

The following example command shows the MLAG settings for bond1 on each peer and indicates that the MTU does not match:

```
cumulus@leaf01:mgmt:~$ nv show interface bond1 bond mlag consistency-checker
Parameter           LocalValue         PeerValue          Conflict  Summary
------------------  -----------------  -----------------  --------  -------
bridge-learning   yes                yes                -
clag-id           1                  1                  -
lacp-actor-mac    44:38:39:be:ef:aa  44:38:39:be:ef:aa  -
lacp-partner-mac  00:00:00:00:00:00  00:00:00:00:00:00  -
master            br_default         NOT-SYNCED         -
mtu               4800               1500               mtu mismatch on clag interface between clag peers
native-vlan       1                  1                  -
vlan-id           1, 10, 20, 30      1, 10, 20, 30      -
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The following example command shows global MLAG settings for each peer and indicates that the MLAG system MAC address does not match.

```
cumulus@leaf02:mgmt:~$ clagctl consistency-check global
Parameter              LocalValue               PeerValue                Conflict
---------------------  -----------------------  -----------------------  --------------------------------------
system-mac             44:38:39:be:ef:ab        44:38:39:be:ef:aa        system mac mismatch between clag peers
clag-protocol-version  1.6.0                    1.6.0                    -
clag-pkg-version       1.6.0-cl5.0.1+u15        1.6.0-cl5.0.1+u15        -
bridge-priority        32768                    32768                    -
anycast-ip             -                        -                        -
peer-ip                fe80::4638:39ff:fe00:59  fe80::4638:39ff:fe00:59  -
redirect2-enable       yes                      yes                      -
peerlink-mtu           9216                     9216                     -
bridge-type            vlan-aware               vlan-aware               -
peerlink-master        br_default               NOT-SYNCED               -
peerlink-vlans         1, 10, 20, 30            1, 10, 20, 30            -
bridge-stp             on                       on                       -
peerlink-native-vlan   1                        1                        -
```

The following example command shows MLAG settings for all interfaces on each peer with no conflicts:

```
cumulus@leaf01:mgmt:~$ clagctl consistency-check interface
Clag Interface: bond1
=====================
Parameter         LocalValue         PeerValue          Conflict
----------------  -----------------  -----------------  ----------
clag-id           1                  1                  -
lacp-partner-mac  00:00:00:00:00:00  00:00:00:00:00:00  -
lacp-actor-mac    44:38:39:be:ef:aa  44:38:39:be:ef:aa  -
vlan-id           1, 10, 20, 30      1, 10, 20, 30      -
native-vlan       1                  1                  -
master            br_default         NOT-SYNCED         -
mtu               9216               9216               -
bridge-learning   yes                yes                -

Clag Interface: bond2
=====================
Parameter         LocalValue         PeerValue          Conflict
----------------  -----------------  -----------------  ----------
clag-id           2                  2                  -
lacp-partner-mac  00:00:00:00:00:00  00:00:00:00:00:00  -
lacp-actor-mac    44:38:39:be:ef:aa  44:38:39:be:ef:aa  -
vlan-id           1, 10, 20, 30      1, 10, 20, 30      -
native-vlan       1                  1                  -
master            br_default         NOT-SYNCED         -
mtu               9216               9216               -
bridge-learning   yes                yes                -

Clag Interface: bond3
=====================
Parameter         LocalValue         PeerValue          Conflict
----------------  -----------------  -----------------  ----------
clag-id           3                  3                  -
lacp-partner-mac  00:00:00:00:00:00  00:00:00:00:00:00  -
lacp-actor-mac    44:38:39:be:ef:aa  44:38:39:be:ef:aa  -
vlan-id           1, 10, 20, 30      1, 10, 20, 30      -
native-vlan       1                  1                  -
master            br_default         NOT-SYNCED         -
mtu               9216               9216               -
bridge-learning   yes                yes                -
```

The following example command shows MLAG parameters for bond1 on each peer and indicates that the MTU does not match:

```
cumulus@leaf01:mgmt:~$ clagctl consistency-check interface bond1
Parameter         LocalValue         PeerValue          Conflict
----------------  -----------------  -----------------  ----------
clag-id           1                  1                  -
lacp-partner-mac  00:00:00:00:00:00  00:00:00:00:00:00  -
lacp-actor-mac    44:38:39:be:ef:aa  44:38:39:be:ef:aa  -
vlan-id           1, 10, 20, 30      1, 10, 20, 30      -
native-vlan       1                  1                  -
master            br_default         NOT-SYNCED         -
mtu               1480               1500               mtu mismatch on clag interface between clag peers
bridge-learning   yes                yes                -
```

{{< /tab >}}
{{< /tabs >}}

The actions that Cumulus Linux takes when there is a conflict are disruptive. If you prefer, you can configure the switch to not take any action when there is a conflict. Edit the `/etc/network/interfaces` file to add the `clagd-args --gracefulConsistencyCheck FALSE` parameter in the peer link stanza.

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto peerlink.4094
iface peerlink.4094
    clagd-args --gracefulConsistencyCheck FALSE
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-sys-mac 44:38:39:BE:EF:AA
...
```

### Large Packet Drops on the Peer Link Interface

You can expect a large volume of packet drops across one of the peer link interfaces. These drops serve to prevent looping of BUM (broadcast, unknown unicast, multicast) packets. When the switch receives a packet across the peer link, if the destination lookup results in an egress interface that is a dual-connected bond, the switch does not forward the packet (to prevent loops). The peer link records a dropped packet.

To check packet drops across peer link interfaces, run the `ethtool -S <interface>` command:

```
cumulus@leaf01:mgmt:~$ ethtool -S swp49
NIC statistics:
     rx_queue_0_packets: 136
     rx_queue_0_bytes: 36318
     rx_queue_0_drops: 0
     rx_queue_0_xdp_packets: 0
     rx_queue_0_xdp_tx: 0
     rx_queue_0_xdp_redirects: 0
     rx_queue_0_xdp_drops: 0
     rx_queue_0_kicks: 1
     tx_queue_0_packets: 200
     tx_queue_0_bytes: 44244
     tx_queue_0_xdp_tx: 0
     tx_queue_0_xdp_tx_drops: 0
     tx_queue_0_kicks: 195
```

You can also run the `net show counters` command. The number of dropped packets shows in the `RX_DRP` column.

```
cumulus@leaf01:mgmt:~$ net show counters

Kernel Interface table
Iface            MTU    RX_OK    RX_ERR    RX_DRP    RX_OVR    TX_OK    TX_ERR    TX_DRP    TX_OVR  Flg
-------------  -----  -------  --------  --------  --------  -------  --------  --------  --------  -----
bond1           9216        0         0         0         0      542         0         0         0  BMmU
bond2           9216        0         0         0         0      542         0         0         0  BMmU
bridge          9216        0         0         0         0       17         0         0         0  BMRU
eth0            1500     5497         0         0         0      933         0         0         0  BMRU
lo             65536     1328         0         0         0     1328         0         0         0  LRU
mgmt           65536      790         0         0         0        0         0        33         0  OmRU
peerlink        9216    23626         0       520         0    23665         0         0         0  BMmRU
peerlink.4094   9216     8013         0         0         0     8017         0         0         0  BMRU
swp1            9216        5         0         0         0      553         0         0         0  BMsRU
swp2            9216        3         0         0         0      552         0         0         0  BMsRU
swp49           9216    11822         0         0         0    11852         0         0         0  BMsRU
swp50           9216    11804         0         0         0    11841         0         0         0  BMsRU
swp51           9216        0         0         0         0      292         0         0         0  BMRU
```

### Peer Link Interfaces and the protodown State

In addition to the standard UP and DOWN administrative states, an interface that is a member of an MLAG bond can also be in a `protodown` state. When MLAG detects a problem that can result in connectivity issues, it puts that interface into `protodown` state. Such connectivity issues include:

- When the peer link goes down but the peer switch is up (the backup link is active).
- When the bond has an MLAG ID but the `clagd` service is not running (you either stop the service or it crashes).
- When an MLAG-enabled node boots or reboots, the switch puts the MLAG bonds in a `protodown` state until the node establishes a connection to its peer switch, or after five minutes.

When an interface goes into a `protodown` state, it results in a local OPER DOWN (carrier down) on the interface.

To show an interface in `protodown` state, run the Linux `ip link show` command or the `net show bridge link` command. For example:

```
cumulus@leaf01:mgmt:~$ ip link show
3: swp1 state DOWN: <NO-CARRIER,BROADCAST,MULTICAST,MASTER,UP> mtu 9216 master pfifo_fast master host-bond1 state DOWN mode DEFAULT qlen 500 protodown on
    link/ether 44:38:39:00:69:84 brd ff:ff:ff:ff:ff:ff
```

### LACP Partner MAC Address Duplicate or Mismatch

Cumulus Linux puts interfaces in a protodown state under the following conditions:

- When there is an LACP partner MAC address mismatch. For example if a bond comes up with a `clag-id` and the peer is using a bond with the same `clag-id` but a different LACP partner MAC address. The NVUE `nv show mlag lacp-conflict` or the Linux `clagctl` command output shows the protodown reason as a `partner-mac-mismatch`.

- When there is a duplicate LACP partner MAC address. For example, when there are multiple LACP bonds between the same two LACP endpoints. The NVUE `nv show mlag lacp-conflict` or the Linux `clagctl` command output shows the protodown reason as a `duplicate-partner-mac`.

  To prevent a bond from coming up when an MLAG bond with an LACP partner MAC address already in use comes up, use the `--clag-args --allowPartnerMacDup False` option. This option puts the slaves of that bond interface in a protodown state and the `clagctl` output shows the protodown reason as a `duplicate-partner-mac`.

After you make the necessary cable or configuration changes to avoid the protodown state and you want MLAG to reevaluate the LACP partners, run the NVUE `nv action clear mlag lacp-conflict` command or the Linux `clagctl clearconflictstate` command to remove `duplicate-partner-mac` or `partner-mac-mismatch` from the protodown bonds, allowing them to come back up.

## Configuration Example

The example below shows a basic MLAG configuration, where:
- leaf01 and leaf02 are MLAG peers
- MLAG is on three bonds, each with a single port, a peer link that is a bond with two member ports, and three VLANs on each port

{{< figure src="/images/cumulus-linux/mlag-config.png" width="450" >}}

For an example configuration with MLAG and BGP, see the {{<link title="Configuration Example" text="BGP configuration example">}}.

{{< tabs "TabID1087 ">}}
{{< tab "NVUE ">}}

{{< tabs "TabID1090 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1-3,swp49-51
cumulus@leaf01:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf01:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:~$ nv set interface bond1-3 bridge domain br_default 
cumulus@leaf01:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf01:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:~$ nv set mlag init-delay 100
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:~$ nv set interface swp1-3,swp49-51
cumulus@leaf02:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:~$ nv set interface bond3 bond member swp3
cumulus@leaf02:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf02:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:~$ nv set interface vlan30 ip address 10.1.30.3/24
cumulus@leaf02:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf02:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:~$ nv set system global anycast-mac 44:38:39:BE:EF:AA
cumulus@leaf02:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:~$ nv set mlag init-delay 100
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1-2
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml ">}}

{{< tabs "TabID1132 ">}}
{{< tab "leaf01 ">}}

```
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '10': {}
            '20': {}
            '30': {}
    interface:
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default: {}
        type: bond
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default: {}
        type: bond
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            enable: on
            id: 3
        bridge:
          domain:
            br_default: {}
        type: bond
      lo:
        ip:
          address:
            10.10.10.1/32: {}
        type: loopback
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        base-interface: peerlink
        type: sub
        vlan: 4094
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      vlan10:
        ip:
          address:
            10.1.10.2/24: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.2/24: {}
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.2/24: {}
        type: svi
        vlan: 30
    mlag:
      backup:
        10.10.10.2: {}
      enable: on
      init-delay: 100
      peer-ip: linklocal
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:AA
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '10': {}
            '20': {}
            '30': {}
    interface:
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            enable: on
            id: 1
        bridge:
          domain:
            br_default: {}
        type: bond
      bond2:
        bond:
          member:
            swp2: {}
          mlag:
            enable: on
            id: 2
        bridge:
          domain:
            br_default: {}
        type: bond
      bond3:
        bond:
          member:
            swp3: {}
          mlag:
            enable: on
            id: 3
        bridge:
          domain:
            br_default: {}
        type: bond
      lo:
        ip:
          address:
            10.10.10.2/32: {}
        type: loopback
      peerlink:
        bond:
          member:
            swp49: {}
            swp50: {}
        type: peerlink
      peerlink.4094:
        base-interface: peerlink
        type: sub
        vlan: 4094
      swp1:
        type: swp
      swp2:
        type: swp
      swp3:
        type: swp
      swp49:
        type: swp
      swp50:
        type: swp
      swp51:
        type: swp
      vlan10:
        ip:
          address:
            10.1.10.3/24: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.3/24: {}
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.3/24: {}
        type: svi
        vlan: 30
    mlag:
      backup:
        10.10.10.1: {}
      enable: on
      init-delay: 100
      peer-ip: linklocal
    system:
      global:
        anycast-mac: 44:38:39:BE:EF:AA
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
- set:
    interface:
      lo:
        ip:
          address:
            10.10.10.101/32: {}
        type: loopback
      swp1:
        type: swp
      swp2:
        type: swp
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces">}}

{{< tabs "TabID1150 ">}}
{{< tab "leaf01 ">}}

```
auto lo
iface lo inet loopback
    address 10.10.10.1/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1
auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 2
auto bond3
iface bond3
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 3
auto vlan10
iface vlan10
    address 10.1.10.2/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.2/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.2/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 30
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 100
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink
    hwaddress 44:38:39:22:01:b1
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
auto lo
iface lo inet loopback
    address 10.10.10.2/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1
auto swp2
iface swp2
auto swp3
iface swp3
auto swp49
iface swp49
auto swp50
iface swp50
auto swp51
iface swp51
auto bond1
iface bond1
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 1
auto bond2
iface bond2
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 2
auto bond3
iface bond3
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
    clag-id 3
auto vlan10
iface vlan10
    address 10.1.10.3/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.3/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.3/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 30
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 100
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
auto lo
iface lo inet loopback
    address 10.10.10.101/32
auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto
auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt
auto swp1
iface swp1

auto swp2
iface swp2
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Try It " >}}
    {{< simulation name="Try It CL56 - MLAGv2" showNodes="leaf01,leaf02,spine01,server01,server02,server03" >}}

This simulation is running Cumulus Linux 5.6. The Cumulus Linux 5.7 simulation is coming soon.

This simulation starts with the example MLAG configuration. The demo is pre-configured using {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVUE">}} commands.

To validate the configuration, run the commands listed in the troubleshooting section above.

{{< /tab >}}
{{< /tabs >}}

## Related Information

- [MLAG Redundancy Scenarios]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/MLAG-Redundancy-Scenarios" >}})
- [Compare Traditional Bridge Mode to VLAN-aware Bridge Mode]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode" >}})
