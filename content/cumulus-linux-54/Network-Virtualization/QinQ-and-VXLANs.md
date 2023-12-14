---
title: QinQ and VXLANs
author: NVIDIA
weight: 630
toc: 3
---
*QinQ* is an amendment to the {{<exlink url="http://www.ieee802.org/1/pages/802.1Q.html" text="IEEE 802.1Q specification">}} that enables you to insert multiple VLAN tags into a single Ethernet frame.

QinQ with VXLAN is typically used by a service provider who offers multi-tenant layer 2 connectivity between different customer data centers over a virtualized layer 3 provider network.  The customer VLANs are transparent to the provider network.

Cumulus Linux supports the standard 802.1ad with a VLAN-aware bridge where you map a customer (S-tag) to a VNI and preserve the inner VLAN (C-tag) inside a VXLAN packet.

Cumulus Linux also supports a special case with a VLAN-unaware bridge where you use both the S-tag, C-tag tuple for forwarding lookup and mapping to a VNI. Both the S-tag and C-tag are removed during VXLAN encapsulation; Cumulus Linux refers to this configuration as Double Tag Translation.

{{%notice note%}}
You must disable ARP and ND suppression on VXLAN bridges when using QinQ.
{{%/notice%}}

## 802.1ad with a VLAN-aware Bridge

In the standard 802.1ad QinQ model, the customer-facing interface is a QinQ access port and the outer S-tag is the PVID representing the customer. Cumulus Linux translates the S-tag to a VXLAN VNI. The inner C-tag is transparent to the provider. It is also possible that the provider has VLAN trunks connected to the same bridge, carrying traffic from different customers on the same port. In this case, the S-tag maps to a VNI. Cumulus Linux removes the S-tag during VXLAN encapsulation and adds it after decapsulation.

An example configuration in VLAN-aware bridge mode looks like this:

{{< img src="/images/cumulus-linux/QinQ-single-tag-translation.png" width="600" >}}

You configure two switches: one at the service provider edge that faces the customer (the switch on the left above), and one on the remote provider edge with a VLAN trunk (the switch on the right above).

{{%notice note%}}
- All edges must support QinQ with VXLANs.
- You *cannot* mix 802.1Q and 802.1ad subinterfaces on the same switch port.
- When configuring bridges in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}}, all VLANs that are members of the same switch port must use the same `vlan_protocol`.
- When using switches in an <span class="a-tooltip">[MLAG](## "Multi-chassis Link Aggregation")</span> pair:
  - Configure the peerlink (peerlink.4094) between the MLAG pair for VLAN protocol 802.1ad.
  - You cannot use the peerlink as a backup datapath in case one of the MLAG peers loses all uplinks.
- When the bridge VLAN protocol is 802.1ad and is VXLAN-enabled, all bridge ports must be either access ports (except for the MLAG peerlink) or VLAN trunks.
{{%/notice%}}
<!-- vale off -->
### Remote Provider Edge Switch
<!-- vale on -->
For the switch facing the remote provider cloud:

- Configure the bridge with `vlan_protocol` set to *802.1ad*.
- The VNI maps back to S-tag (customer).
- A trunk port connected to the public cloud is the QinQ trunk and packets are double tagged, where the S-tag is for the customer and the C-tag is for the service.

To configure the remote provider switch:

{{< tabs "TabID51 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this configuration.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the following configuration:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 100=1000 200=3000
    bridge-learning off

auto br_default
iface br_default
    bridge-ports swp3 vxlan48
    bridge-vids 100 200
    bridge-vlan-aware yes
    bridge-pvid 1
    bridge-vlan-protocol 802.1ad
...
```

Run the `ifreload -a` command to load the new configuration:

```
cumulus@switch:~$ ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
### Customer-facing Edge Switch
<!-- vale on -->
For the switch facing the customer:

- Configure the bridge with `vlan_protocol` set to *802.1ad*.
- The customer interface is the QinQ access port, the PVID is the S-tag (customer) and maps to a VNI.
- The service VLAN tags (C-tags) do not change during VXLAN encapsulation.

To configure the customer-facing switch:

{{< tabs "TabID118 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for this configuration.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the following configuration:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 100=1000 200=3000
    bridge-learning off

auto swp3
iface swp3
    bridge-access 100

auto swp4
iface swp4
    bridge-access 200

auto br_default
iface br_default
    bridge-ports swp3 swp4 vxlan48
    bridge-vids 100 200
    bridge-vlan-aware yes
    bridge-pvid 1
    bridge-vlan-protocol 802.1ad
...
```

{{< /tab >}}
{{< /tabs >}}

### View the Configuration

In the output below, customer A is on VLAN 100 (S-TAG) and customer B is on VLAN 200 (S-TAG).

To check the remote provider switch, run the `net show  <bridge-name> vlan` command:

```
cumulus@switch:~$ net show bridge vlan

Interface      VLAN  Flags                  VNI
-----------  ------  ---------------------  -----
swp3             1   PVID, Egress Untagged
               100
               200
vni-1000       100   PVID, Egress Untagged   1000
vni-3000       200   PVID, Egress Untagged   3000
```

To check the customer-facing switch, run the `net show  <bridge-name> vlan` command:

```
cumulus@switch:~$ net show bridge vlan
Interface      VLAN  Flags                  VNI
-----------  ------  ---------------------  -----
swp3            100  PVID, Egress Untagged
swp4            200  PVID, Egress Untagged
vni-1000        100  PVID, Egress Untagged  1000
vni-3000        200  PVID, Egress Untagged  3000
```

<!-- vale off -->
To verify that the bridge is configured for QinQ, run the `ip -d link show bridge` commands and check for *vlan\_protocol 802.1ad* in the output:
<!-- vale on -->
```
cumulus@switch:~$ sudo ip -d link show bridge
287: bridge: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default
    link/ether 06:a2:ae:de:e3:43 brd ff:ff:ff:ff:ff:ff promiscuity 0
    bridge forward_delay 1500 hello_time 200 max_age 2000 ageing_time 30000 stp_state 2 priority 32768 vlan_filtering 1 vlan_protocol 802.1ad bridge_id 8000.6:a2:ae:de:e3:43 designated_root 8000.6:a2:ae:de:e3:43 root_port 0 root_path_cost 0 topology_change 0 topology_change_detected 0 hello_timer    0.00 tcn_timer    0.00 topology_change_timer    0.00 gc_timer   64.29 vlan_default_pvid 1 vlan_stats_enabled 1 group_fwd_mask 0 group_address 01:80:c2:00:00:08 mcast_snooping 0 mcast_router 1 mcast_query_use_ifaddr 0 mcast_querier 0 mcast_hash_elasticity 4096 mcast_hash_max 4096 mcast_last_member_count 2 mcast_startup_query_count 2 mcast_last_member_interval 100 mcast_membership_interval 26000 mcast_querier_interval 25500 mcast_query_interval 12500 mcast_query_response_interval 1000 mcast_startup_query_interval 3125 mcast_stats_enabled 1 mcast_igmp_version 2 mcast_mld_version 1 nf_call_iptables 0 nf_call_ip6tables 0 nf_call_arptables 0 addrgenmode eui64
```

### Example Configuration

This example shows a configuration for 802.1ad QinQ in traditional bridge mode on a leaf.

{{< expand "Example /etc/network/interfaces File" >}}

```
auto swp3.11
iface swp3.11
    vlan-protocol 802.1ad

auto vxlan1000101
iface vxlan1000101
    vxlan-id 1000101
    vxlan-local-tunnelip 10.0.0.13

auto br11
iface br11
    bridge-ports swp3.11 vxlan1000101
```

{{< /expand >}}

## Double Tag Translation

Double tag translation includes a bridge with double-tagged member interfaces, where a combination of the C-tag and S-tag map to a VNI. You create the configuration only at the edge facing the public cloud. The VXLAN configuration at the customer-facing edge does not need to change.

The double tag is always a cloud connection. The customer-facing edge is either single-tagged or untagged. At the public cloud handoff point, the VNI maps to double VLAN tags, with the S-tag indicating the customer and the C-tag indicating the service.

The configuration in Cumulus Linux uses the outer tag for the customer and the inner tag for the service.

{{%notice note%}}
You can use double tag translation:
- On Spectrum-2 and Spectrum-3 switches in a VXLAN configuration on native interfaces only. You cannot configure double tag translation on bonds.
- With bridges in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}} only.
- With 802.1Q bridge mode.
- *Without* MLAG.

Double tag translation uses:
- ACL resources internally, which can increase ACL resource utilization. To see the number of ACL entries used, run the `sudo cat /cumulus/switchd/run/acl_info/iacl_resource` command.
- Internal VLANs for each traditional-mode bridge, which has a default range of 275. To change the range, edit the `/etc/cumulus/switchd.conf` file to uncomment the `#resv_vlan_range = 3725-3999` line and specify the range you want to use.
{{%/notice%}}

To configure a double-tagged interface, stack the VLANs as `<port>.<outer tag>.<inner tag>`. For example, swp1.100.10, where the outer tag is VLAN 100, which represents the customer, and the inner tag is VLAN 10, which represents the service.

An example configuration:

{{< img src = "/images/cumulus-linux/qinq-double-tag-translation.png" >}}

{{< tabs "TabID268 ">}}
{{< tab "NVUE Commands ">}}

NVUE does not support double tag translation.

{{< /tab >}}
{{< tab "Linux Commands ">}}

To configure the switch for double tag translation using the above example, edit the `/etc/network/interfaces` file in a text editor and add the following:

```
auto swp3.100.10
iface swp3.100.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard yes

auto vni1000
iface vni1000
    vxlan-local-tunnelip  10.0.0.1
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard yes
    vxlan-id 1000

auto custA-10-azr
iface custA-10-azr
    bridge-ports swp3.100.10 vni1000
    bridge-vlan-aware no
```

{{< /tab >}}
{{< /tabs >}}

To check the configuration, run the `brctl show` command:

```
cumulus@switch:~$ sudo brctl show
bridge name     bridge id               STP enabled     interfaces
custA-10-azr    8000.00020000004b       yes             swp3.100.10
                                                        vni1000
custB-20-azr    8000.00020000004b       yes             swp3.200.20
                                                        vni3000
```

## Considerations

The Linux kernel limits interface names to 15 characters in length, which can be a problem for QinQ interfaces. To work around this issue, create two VLANs as nested VLAN raw devices, one for the outer tag and one for the inner tag. For example, you cannot create an interface called swp50s0.1001.101 because it contains 16 characters. Instead, edit the `/etc/network/interfaces` file to create VLANs with IDs 1001 and 101:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vlan1001
iface vlan1001
      vlan-id 1001
       vlan-raw-device swp50s0

auto vlan1001-101
iface vlan1001-101
       vlan-id 101
       vlan-raw-device vlan1001

auto bridge101
iface bridge101
    bridge-ports vlan1001-101 vxlan1000101
...
```
