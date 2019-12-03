---
title: EVPN Enhancements
author: Cumulus Networks
weight: 352
aliases:
product: Cumulus Linux
version: '4.0'
---
This section describes EVPN enhancements.

## Configure Static MAC Addresses

MAC addresses that are intended to be pinned to a particular VTEP can be provisioned on the VTEP as a static bridge FDB entry. EVPN picks up these MAC addresses and advertises them to peers as remote static MACs. You configure static bridge FDB entries for MACs under the bridge configuration:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bridge post-up bridge fdb add 00:11:22:33:44:55 dev swp1 vlan 101 master static
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

For a bridge in [traditional mode](../../../Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/), you must edit the bridge configuration in the `/etc/network/interfaces` file using a text editor:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto br101
iface br101
    bridge-ports swp1.101 vni10101
    post-up bridge fdb add 00:11:22:33:44:55 dev swp1.101 master static
...
```

</details>

<details>

<summary>Linux Commands </summary>

Edit the `/etc/network/interfaces` file. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-ports swp1 vni10101
    bridge-vids 101
    bridge-vlan-aware yes
    post-up bridge fdb add 00:11:22:33:44:55 dev swp1 vlan 101 master static
...
```

</details>

## Filter EVPN Routes

A common deployment scenario for large data centers is to sub divide the data center into multiple pods with full host mobility within a pod but only do prefix-based routing across pods. You can achieve this by only exchanging EVPN type-5 routes across pods.

To filter EVPN routes based on the route-type and allow only certain types of EVPN routes to be advertised in the fabric:

<details>

<summary>NCLU Commands </summary>

Use these commands `net add routing route-map <route_map_name> (deny|permit) <1-65535> match evpn default-route` and the `net add routing route-map <route_map_name> (deny|permit) <1-65535> match evpn route-type (macip|prefix|multicast)` commands.

The following example command configures EVPN to advertise type-5 routes only:

```
cumulus@switch:~$ net add routing route-map map1 permit 1 match evpn route-type prefix
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

The following example command configures EVPN to advertise type-5 routes only:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# route-map map1 permit 1
switch(config)# match evpn route-type prefix
switch(config)# end
switch# write memory
switch# exit
cumulus@switch:~$ 
```

</details>

## Advertise SVI IP Addresses

In a typical EVPN deployment, you *reuse* SVI IP addresses on VTEPs across multiple racks. However, if you use *unique* SVI IP addresses across multiple racks and you want the local SVI IP address to be reachable via remote VTEPs, you can enable the `advertise-svi-ip` option. This option advertises the SVI IP/MAC address as a type-2 route and eliminates the need for any flooding over VXLAN to reach the IP from a remote VTEP/rack.

{{%notice note%}}

- When you enable the `advertise-svi-ip` option, the anycast IP/MAC address pair is not advertised. Be sure **not** to enable both the `advertise-svi-ip` option and the `advertise-default-gw` option at the same time. (The `advertise-default-gw` option configures the gateway VTEPs to advertise their IP/MAC address. See [Advertising the Default Gateway](../Inter-subnet-Routing#centralized-routing).
- If your switch is in an MLAG configuration, refer to [Advertise Primary IP Address](../Inter-subnet-Routing/#advertise-primary-ip-address).

{{%/notice%}}

To advertise *all* SVI IP/MAC addresses on the switch, run these commands:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp l2vpn evpn advertise-svi-ip
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# advertise-svi-ip
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$

cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
address-family l2vpn evpn
  advertise-svi-ip
exit-address-family
...
```

</details>

To advertise a *specific* SVI IP/MAC address, run these commands:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp l2vpn evpn vni 10 advertise-svi-ip
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# vni 10
switch(config-router-af-vni)# advertise-svi-ip
switch(config-router-af-vni)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

</details>

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
address-family l2vpn evpn
  vni 10
  advertise-svi-ip
exit-address-family
...
```

## Extended Mobility

Cumulus Linux supports scenarios where the IP to MAC binding for a host or virtual machine changes across the move. In addition to the simple mobility scenario where a host or virtual machine with a binding of `IP1`, `MAC1` moves from one rack to another, Cumulus Linux supports additional scenarios where a host or virtual machine with a binding of `IP1`, `MAC1` moves and takes on a new binding of `IP2`, `MAC1` or `IP1`, `MAC2`. The EVPN protocol mechanism to handle extended mobility continues to use the MAC mobility extended community and is the same as the standard mobility procedures. Extended mobility defines how the sequence number in this attribute is computed when binding changes occur.

Extended mobility not only supports virtual machine *moves*, but also where one virtual machine shuts down and another is provisioned on a different rack that uses the IP address or the MAC address of the previous virtual machine. For example, in an EVPN deployment with OpenStack, where virtual machines for a tenant are provisioned and shut down very dynamically, a new virtual machine can use the same IP address as an earlier virtual machine but with a different MAC address.

The support for extended mobility is enabled by default and does not require any additional configuration.

You can examine the sequence numbers associated with a host or virtual machine MAC address and IP address with the NCLU `net show evpn mac vni <vni> mac <address>` command or the vtysh `show evpn mac vni <vni> mac <address>` command. For example:

```
cumulus@switch:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:42
MAC: 00:02:00:00:00:42
  Remote VTEP: 10.0.0.2
  Local Seq: 0 Remote Seq: 3
  Neighbors:
    10.1.1.74 Active

cumulus@switch:~$ net show evpn arp vni 10100 ip 10.1.1.74
IP: 10.1.1.74
  Type: local
  State: active
  MAC: 44:39:39:ff:00:24
  Local Seq: 2 Remote Seq: 3
```

## Duplicate Address Detection

Cumulus Linux is able to detect duplicate MAC and IPv4/IPv6 addresses on hosts or virtual machines in a VXLAN-EVPN configuration. The Cumulus Linux switch (VTEP) considers a host MAC or IP address to be duplicate if the address moves across the network more than a certain number of times within a certain number of seconds (five moves within 180 seconds by default). In addition to legitimate host or VM mobility scenarios, address movement can occur when IP addresses are misconfigured on hosts or when packet looping occurs in the network due to faulty configuration or behavior.

Duplicate address detection is enabled by default and triggers when:

- Two hosts have the same MAC address (the host IP addresses might be the same or different)
- Two hosts have the same IP address but different MAC addresses

By default, when a duplicate address is detected, Cumulus Linux flags the address as a duplicate and generates an error in syslog so that you can troubleshoot the reason and address the fault, then clear the duplicate address flag. No functional action is taken on the address.

{{%notice note%}}

If a MAC address is flagged as a duplicate, all IP addresses associated with that MAC are flagged as duplicates.

{{%/notice%}}

{{%notice note%}}

In an MLAG configuration, duplicate address detection runs independently on each switch in the MLAG pair. Based on the sequence in which local learn and/or route withdrawal from the remote VTEP occurs, an IP address might be flagged as duplicate only on one of the switches in the MLAG pair. In rare cases, neither switch might flag the IP address as a duplicate.

{{%/notice%}}

### When Does Duplicate Address Detection Trigger?

The VTEP that sees an address move from remote to local begins the detection process by starting a timer. Each VTEP runs duplicate address detection independently. Detection always starts with the first mobility event from *remote* to *local*. If the address is initially remote, the detection count can start with the very first move for the address. If the address is initially local, the detection count starts only with the second or higher move for the address. If an address is undergoing a mobility event between remote VTEPs, duplicate detection is not started. 

The following illustration shows VTEP-A, VTEP-B, and VTEP-C in an EVPN configuration. Duplicate address detection triggers on VTEP-A when there is a duplicate MAC address for two hosts attached to VTEP-A and VTEP-B. However, duplicate detection does *not* trigger on VTEP-A when mobility events occur between two remote VTEPs (VTEP-B and VTEP-C).

{{< img src = "/images/cumulus-linux/evpn-dad-example.png" >}}

### Configure Duplicate Address Detection

To change the threshold for MAC and IP address moves, run the `net add bgp l2vpn evpn dup-addr-detection max-moves <number-of-events> time <duration>` command. You can specify `max-moves` to be between 2 and 1000 and `time` to be between 2 and 1800 seconds.

The following example command sets the maximum number of address moves allowed to 10 and the duplicate address detection time interval to 1200 seconds.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection max-moves 10 time 1200 
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# dup-addr-detection max-moves 10 time 1200
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$ 
```

</details>

To disable duplicate address detection, see [Disable Duplicate Address Detection](#disable-duplicate-address-detection) below.

### Example syslog Messages

The following example shows the syslog message that is generated when Cumulus Linux detects a MAC address as a duplicate during a local update:

```
2018/11/06 18:55:29.463327 ZEBRA: [EC 4043309149] VNI 1001: MAC 00:01:02:03:04:11 detected as duplicate during local update, last VTEP 172.16.0.16
```

The following example shows the syslog message that is generated when Cumulus Linux detects an IP address as a duplicate during a remote update:

```
2018/11/09 22:47:15.071381 ZEBRA: [EC 4043309151] VNI 1002: MAC aa:22:aa:aa:aa:aa IP 10.0.0.9 detected as duplicate during remote update, from VTEP 172.16.0.16
```

### Freeze a Detected Duplicate Address

Cumulus Linux provides a *freeze* option that takes action on a detected duplicate address. You can freeze the address *permanently* (until you intervene) or for a *defined amount of time*, after which it is cleared automatically.

When you enable the freeze option and a duplicate address is detected:

- If the MAC or IP address is learned from a remote VTEP at the time it is frozen, the forwarding information in the kernel and hardware is not updated, leaving it in the prior state. Any future remote updates are processed but they are not reflected in the kernel entry. If the remote VTEP sends a MAC-IP route withdrawal, the local VTEP removes the frozen remote entry. Then, if the local VTEP has a locally-learned entry already present in its kernel, FRR will originate a corresponding MAC-IP route and advertise it to all remote VTEPs.
- If the MAC or IP address is locally learned on this VTEP at the time it is frozen, the address is not advertised to remote VTEPs. Future local updates are processed but are not advertised to remote VTEPs. If FRR receives a local entry delete event, the frozen entry is removed from the FRR database. Any remote updates (from other VTEPs) change the state of the entry to remote but the entry is not installed in the kernel (until cleared).

**To recover from a freeze**, shut down the faulty host or VM or fix any other misconfiguration in the network. If the address is frozen *permanently,* issue the [clear command](#clear-duplicate-addresses) on the VTEP where the address is marked as duplicate. If the address is frozen for a defined period of time, it is cleared automatically after the timer expires (you can clear the duplicate address before the timer expires with the [clear command](#clear-duplicate-addresses)).

{{%notice note%}}

If you issue the clear command or the timer expires before you address the fault, duplicate address detection might occur repeatedly.

{{%/notice%}}

After you clear a frozen address, if it is present behind a remote VTEP, the kernel and hardware forwarding tables are updated. If the address is locally learned on this VTEP, the address is advertised to remote VTEPs. All VTEPs get the correct address as soon as the host communicates . Silent hosts are learned only after the faulty entries age out, or you intervene and clear the faulty MAC and ARP table entries.

### Configure the Freeze Option

To enable Cumulus Linux to *freeze* detected duplicate addresses, run the `net add bgp l2vpn evpn dup-addr-detection freeze <duration>|permanent` command. The duration can be any number of seconds between 30 and 3600.

The following example command freezes duplicate addresses for a period of 1000 seconds, after which it is cleared automatically:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection freeze 1000
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn
switch(config-router-af)# dup-addr-detection freeze 1000
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$ 
```

</details>

{{%notice note%}}

Cumulus Networks recommends you set the freeze timer to be three times the duplicate address detection window. For example, if the duplicate address detection window is set to the default of 180 seconds, set the freeze timer to 540 seconds.

{{%/notice%}}

The following example command freezes duplicate addresses permanently (until you issue the [clear command](#clear-duplicate-addresses)):

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection freeze permanent
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# dup-addr-detection freeze permanent
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$ 
```

</details>

### Clear Duplicate Addresses

You can clear a duplicate MAC or IP address (and unfreeze a frozen address). The following example command clears IP address 10.0.0.9 for VNI 101.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net clear evpn dup-addr vni 101 ip 10.0.0.9
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# clear evpn dup-addr vni 101 ip 10.0.0.9
switch)# exit
cumulus@switch:~$ 
```

</details>

To clear duplicate addresses for all VNIs, run the following command:

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net clear evpn dup-addr vni all
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# clear evpn dup-addr vni all
switch)# exit
cumulus@switch:~$ 
```

</details>

{{%notice note%}}

In an MLAG configuration, you need to run the [clear command](#clear-duplicate-addresses) on both the MLAG primary and secondary switch.

{{%/notice%}}

{{%notice note%}}

When you clear a duplicate MAC address, all its associated IP addresses are also cleared. However, you cannot clear an associated IP address if its MAC address is still in a duplicate state.

{{%/notice%}}

### Disable Duplicate Address Detection

By default, duplicate address detection is enabled and a syslog error is generated when a duplicate address is detected. To disable duplicate address detection, run the following command.

<details>

<summary>NCLU Commands </summary>

```
cumulus@switch:~$ net del bgp l2vpn evpn dup-addr-detection
```

</details>

<details>

<summary>vtysh Commands </summary>

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router bgp 65011
switch(config-router)# address-family l2vpn evpn 
switch(config-router-af)# no dup-addr-detection
switch(config-router-af)# end
switch)# write memory
switch)# exit
cumulus@switch:~$
```

</details>

When you disable duplicate address detection, Cumulus Linux clears the configuration and all existing duplicate addresses.

### Show Detected Duplicate Address Information

During the duplicate address detection process, you can see the start time and current detection count with the NCLU `net show evpn mac vni <vni_id> mac <mac_addr>` command or the vtysh `show evpn mac vni <vni_id> mac <mac_addr>` command. The following command example shows that detection started for MAC address 00:01:02:03:04:11 for VNI 1001 on Tuesday, Nov 6 at 18:55:05 and the number of moves detected is 1.

```
cumulus@switch:~$ net show evpn mac vni 1001 mac 00:01:02:03:04:11
MAC: 00:01:02:03:04:11
  Intf: hostbond3(15) VLAN: 1001
  Local Seq: 1 Remote Seq: 0
  Duplicate detection started at Tue Nov  6 18:55:05 2018, detection count 1
  Neighbors:
    10.0.1.26 Active
```

After the duplicate MAC address is cleared, the NCLU `net show evpn mac vni <vni_id> mac <mac_addr>` command or the vtysh `show evpn mac vni <vni_id> mac <mac_addr>` command shows:

```
MAC: 00:01:02:03:04:11
  Remote VTEP: 172.16.0.16
  Local Seq: 13 Remote Seq: 14
  Duplicate, detected at Tue Nov  6 18:55:29 2018
  Neighbors:
    10.0.1.26 Active
```

To display information for a duplicate IP address, run the NCLU `net show evpn arp-cache vni <vni_id> ip <ip_addr>` command or the vtysh `show evpn arp-cache vni <vni_id> ip <ip_addr>` command. The following command example shows information for IP address 10.0.0.9 for VNI 1001.

```
cumulus@switch:~$ net show evpn arp-cache vni 1001 ip 10.0.0.9
IP: 10.0.0.9
  Type: remote
  State: inactive
  MAC: 00:01:02:03:04:11
  Remote VTEP: 10.0.0.34
  Local Seq: 0 Remote Seq: 14
  Duplicate, detected at Tue Nov  6 18:55:29 2018
```

To show a list of MAC addresses detected as duplicate for a specific VNI or for all VNIs, run the NCLU `net show evpn mac vni <vni-id|all> duplicate` command or the vtysh `show evpn mac vni <vni-id|all> duplicate` command. The following example command shows a list of duplicate MAC addresses for VNI 1001:

``` 
cumulus@switch:~$ net show evpn mac vni 1001 duplicate
Number of MACs (local and remote) known for this VNI: 16
MAC               Type   Intf/Remote VTEP      VLAN
aa:bb:cc:dd:ee:ff local  hostbond3             1001  
```

To show a list of IP addresses detected as duplicate for a specific VNI or for all VNIs, run the NCLU `net show evpn arp-cache vni <vni-id|all> duplicate` command or the vtysh `show evpn arp-cache vni <vni-id|all> duplicate` command. The following example command shows a list of duplicate IP addresses for VNI 1001:

```
cumulus@switch:~$ net show evpn arp-cache vni 1001 duplicate
Number of ARPs (local and remote) known for this VNI: 20
IP                Type   State    MAC                Remote VTEP
10.0.0.8          local  active   aa:11:aa:aa:aa:aa
10.0.0.9          local  active   aa:11:aa:aa:aa:aa
10.10.0.12        remote active   aa:22:aa:aa:aa:aa  172.16.0.16
```

To show configured duplicate address detection parameters, run the NCLU `net show evpn` command or the vtysh `show evpn` command:

```
cumulus@switch:~$ net show evpn
L2 VNIs: 4
L3 VNIs: 2
Advertise gateway mac-ip: No
Duplicate address detection: Enable
  Detection max-moves 7, time 300
  Detection freeze permanent
```
