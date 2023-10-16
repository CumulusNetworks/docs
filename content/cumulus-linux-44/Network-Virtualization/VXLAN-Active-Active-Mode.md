---
title: VXLAN Active-active Mode
author: NVIDIA
weight: 615
toc: 3
---
*VXLAN active-active mode* enables a pair of {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} switches to act as a single VTEP, providing active-active VXLAN termination for bare metal as well as virtualized workloads.

## Terminology

| <div style="width:200px">Term | Definition |
| ------------------------------| ---------- |
| VTEP| The virtual tunnel endpoint. This is an encapsulation and decapsulation point for VXLANs.|
| active-active VTEP | A pair of switches acting as a single VTEP. |
| ToR | The top of rack switch; also referred to as a leaf or access switch. |
| spine | The aggregation switch for multiple leafs. Specifically used when a data center is using a {{<exlink url="https://en.wikipedia.org/wiki/Clos_network" text="Clos network architecture">}}. Read more about spine-leaf architecture in this {{<exlink url="https://resource.nvidia.com/en-us-scalability/building-scalable-data-center-networks?xs=257738" text="white paper">}}. |
| exit leaf | A switch dedicated to peering the Clos network to an outside network; also referred to as a border leaf, service leaf, or edge leaf. |
| anycast | An IP address that advertises from multiple locations. Anycast enables multiple devices to share the same IP address and load balance traffic across them. With VXLAN, anycast shares a VTEP IP address between a pair of MLAG switches. |
| VXLAN routing | The industry standard term for routing in and out of a VXLAN. |
<!-- vale off -->
## Configure VXLAN Active-active Mode
<!-- vale on -->
VXLAN active-active mode requires the following underlying technologies to work correctly.
- MLAG. Refer to {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} for more detailed configuration information.
- OSPF or BGP. Refer to {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} or {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}} for more detailed configuration information. 
- STP. You must enable {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP#bpdu-filter" text="BPDU filter">}} and {{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP#bpdu-guard" text="BPDU guard">}} in the VXLAN interfaces if the bridge that connects to the VXLAN has STP.
<!-- vale off -->
### Active-active VTEP Anycast IP Behavior
<!-- vale on -->
You must provision each individual switch within an MLAG pair with a virtual IP address in the form of an anycast IP address for VXLAN data-path termination. The VXLAN termination address is an anycast IP address that you configure as a `clagd` parameter (`clagd-vxlan-anycast-ip`) under the loopback interface. `clagd` dynamically adds and removes this address as the loopback interface address as follows:

1. When the switches boot up, `ifupdown2` places all VXLAN interfaces in a PROTO_DOWN state. The configured anycast addresses are not configured yet.
2. MLAG peering takes place and a successful VXLAN interface consistency check between the switches occurs.
3. The `clagd` daemon responsible for MLAG adds the anycast address to the loopback interface as a second address. It then changes the local IP address of the VXLAN interface from a unique address to the anycast virtual IP address and puts the interface in an UP state.

{{%notice note%}}
For the anycast address to activate, you must configure a VXLAN interface on each switch in the MLAG pair.
{{%/notice%}}

### Failure Scenario Behaviors

| <div style="width:250px">Scenario | Behavior |
| --------------------------------- | ---------|
| The peer link goes down. | The primary MLAG switch continues to keep all VXLAN interfaces up with the anycast IP address while the secondary switch brings down all VXLAN interfaces and places them in a PROTO_DOWN state. The secondary MLAG switch removes the anycast IP address from the loopback interface. |
| One of the switches goes down. | The other operational switch continues to use the anycast IP address. |
| `clagd` stops. | All VXLAN interfaces go in a PROTO_DOWN state. The switch removes the anycast IP address from the loopback interface and the local IP addresses of the VXLAN interfaces change from the anycast IP address to unique non-virtual IP addresses. |
| MLAG peering does not establish between the switches. | `clagd` brings up all the VXLAN interfaces after the reload timer expires with the configured anycast IP address. This allows the VXLAN interface to be up and running on both switches even though peering is not established. |
| The peer link goes down but the peer switch is up (the backup link is active). | All VXLAN interfaces go into a PROTO_DOWN state on the secondary switch. |
| The anycast IP address is different on the MLAG peers. | The VXLAN interface goes into a PROTO_DOWN state on the secondary switch. |

### VXLAN Interface Configuration Consistency

The active-active configuration for a given VXLAN interface must be consistent between the MLAG switches for correct traffic behavior. MLAG ensures that the configuration is consistent before bringing up the VXLAN interfaces:

- The anycast virtual IP address for VXLAN termination must be the same on the switches in the MLAG pair.
- You must configure a VXLAN interface with the same VXLAN ID, which must be administratively up on both switches in the MLAG pair.

Run the `clagctl` command to check if any VXLAN switches are in a PROTO_DOWN state.

### Configure the Anycast IP Address

With MLAG peering, both switches use an anycast IP address for VXLAN encapsulation and decapsulation. This enables remote VTEPs to learn the host MAC addresses attached to the MLAG switches against one logical VTEP, even though the switches independently encapsulate and decapsulate layer 2 traffic originating from the host.
<!-- vale off -->
{{< img src = "/images/cumulus-linux/vxlan-active-active-config.png" >}}
<!-- vale on -->
{{< tabs "TabID67 ">}}
{{< tab "NCLU Commands ">}}

{{< tabs "TabID70 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.12
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.12
cumulus@leaf02:~$ net pending
cumulus@leaf02:~$ net commit
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID81 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:~$ nv set nve vxlan mlag shared-address 10.0.1.12
cumulus@leaf02:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

You can configure the anycast IP address under the loopback interface, as shown below.

{{< tabs "TabID291 ">}}
{{< tab "leaf01 ">}}

```
auto lo
iface lo inet loopback
  address 10.10.10.1/32
  clagd-vxlan-anycast-ip 10.0.1.12
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
auto lo
iface lo inet loopback
  address 10.10.10.2/32
  clagd-vxlan-anycast-ip 10.0.1.12
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}
<!-- vale off -->
## Example VXLAN Active-Active Configuration

{{< img src = "/images/cumulus-linux/vxlan-active-active-example.png" >}}
<!-- vale on -->
The VXLAN interfaces have individual IP addresses, which `clagd` changes to anycast upon MLAG peering.

### FRRouting Configuration

You can configure the layer 3 fabric using {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}}
or {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}}. The following example uses BGP unnumbered. For simplicity, the example does not show the exit leafs.

### Layer 3 IP Addressing

{{< tabs "TabID136 ">}}
{{< tab "leaf01 ">}}

```
auto lo
iface lo inet loopback
    address 10.10.10.1/32
    clagd-vxlan-anycast-ip 10.0.1.12
    vxlan-local-tunnelip 10.10.10.1

auto eth0
iface eth0 inet dhcp

# peerlinks
auto swp49
iface swp49

auto swp50
iface swp50

auto peerlink
iface peerlink
  bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
    clagd-backup-ip 10.10.10.2
    clagd-peer-ip linklocal
    clagd-priority 1000
    clagd-sys-mac 44:38:39:BE:EF:AA
    clagd-args --initDelay 10

# Downlinks
auto swp1
iface swp1

auto bond1
iface bond1
    bond-slaves swp1
    clag-id 1
    bond-lacp-bypass-allow yes

auto bridge
iface bridge
  bridge-vlan-aware yes
  bridge-ports peerlink bond1 vni10 vni20
  bridge-vids 10 20

auto vlan10
iface vlan10
  vlan-raw-device bridge
  vlan-id 10

auto vlan20
iface vlan20
  vlan-raw-device bridge
  vlan-id 20

auto vni10
iface vni10
  vxlan-id 10
  bridge-access 10
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

auto vni20
iface vni20
  vxlan-id 20
  bridge-access 20
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes


# uplinks
auto swp51
iface swp51

auto swp52
iface swp52
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
auto lo
iface lo inet loopback
  address 10.10.10.2/32
  clagd-vxlan-anycast-ip 10.0.1.12
  vxlan-local-tunnelip 10.10.10.2

auto eth0
iface eth0 inet dhcp

# peerlinks
auto swp49
iface swp49

auto swp50
iface swp50

auto peerlink
iface peerlink
  bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
  clagd-backup-ip 10.10.10.1
  clagd-peer-ip linklocal
  clagd-priority 32768
  clagd-sys-mac 44:38:39:BE:EF:AA
  clagd-args --initDelay 10

# Downlinks
auto swp1
iface swp1

auto bond1
iface bond1
    bond-slaves swp1
    clag-id 1
    bond-lacp-bypass-allow yes

auto bridge
iface bridge
  bridge-vlan-aware yes
  bridge-ports peerlink bond1 vni10 vni20
  bridge-vids 10 20

auto vlan10
iface vlan10
  vlan-raw-device bridge
  vlan-id 10
  
auto vlan20
iface vlan20
  vlan-raw-device bridge
  vlan-id 20

auto vni10
iface vni10
  vxlan-id 10
  bridge-access 10
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

auto vni20
iface vni20
  vxlan-id 20
  bridge-access 20
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

# uplinks
auto swp51
iface swp51

auto swp52
iface swp52
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
auto lo
iface lo inet loopback
  address 10.10.10.3/32
  clagd-vxlan-anycast-ip 10.0.1.34
  vxlan-local-tunnelip 10.10.10.3

auto eth0
iface eth0 inet dhcp

# peerlinks
auto swp49
iface swp49

auto swp50
iface sw50p

auto peerlink
iface peerlink
  bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
  clagd-backup-ip 10.10.10.4
  clagd-peer-ip linklocal
  clagd-priority 1000
  clagd-sys-mac 44:38:39:BE:EF:BB
  clagd-args --initDelay 10

# Downlinks
auto swp1
iface swp1
  
auto bond1
iface bond1
    bond-slaves swp1
    clag-id 1
    bond-lacp-bypass-allow yes

auto bridge
iface bridge
  bridge-vlan-aware yes
  bridge-ports peerlink bond1 vni10 vni20
  bridge-vids 10 20

auto vlan10
iface vlan10
  vlan-raw-device bridge
  vlan-id 10
  
auto vlan20
iface vlan20
  vlan-raw-device bridge
  vlan-id 20

auto vni10
iface vni10
  vxlan-id 10
  bridge-access 10
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

auto vni20
iface vni20
  vxlan-id 20
  bridge-access 20
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

# uplinks
auto swp51
iface swp51

auto swp52
iface swp52
```

{{< /tab >}}
{{< tab "leaf04 ">}}

```
auto lo
iface lo inet loopback
  address 10.10.10.4/32
  clagd-vxlan-anycast-ip 10.0.1.34
  vxlan-local-tunnelip 10.10.10.4

auto eth0
iface eth0 inet dhcp

# peerlinks
auto swp49
iface swp49

auto swp50
iface swp50

auto peerlink
iface peerlink
  bond-slaves swp49 swp50

auto peerlink.4094
iface peerlink.4094
  clagd-backup-ip 10.10.10.3
  clagd-peer-ip linklocal
  clagd-priority 32768
  clagd-sys-mac 44:38:39:BE:EF:BB
  clagd-args --initDelay 10

# Downlinks
auto swp1
iface swp1
  
auto bond1
iface bond1
    bond-slaves swp1
    clag-id 1
    bond-lacp-bypass-allow yes

auto bridge
iface bridge
  bridge-vlan-aware yes
  bridge-ports peerlink bond1 vni10 vni20
  bridge-vids 10 20

auto vlan10
iface vlan10
  vlan-raw-device bridge
  vlan-id 10
  
auto vlan20
iface vlan20
  vlan-raw-device bridge
  vlan-id 20

auto vni10
iface vni10
  vxlan-id 10
  bridge-access 10
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes

auto vni20
iface vni20
  vxlan-id 20
  bridge-access 20
  mstpctl-bpduguard yes
  mstpctl-portbpdufilter yes
  
# uplinks
auto swp51
iface swp51

auto swp52
iface swp52
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
auto lo
iface lo inet loopback
  address 10.10.10.101/32

auto eth0
iface eth0 inet dhcp

# downlinks
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
```

{{< /tab >}}
{{< tab "spine02 ">}}

```
auto lo
iface lo inet loopback
    address 10.10.10.102/32

auto eth0
iface eth0 inet dhcp

# downlinks
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
```

{{< /tab >}}
{{< /tabs >}}

### Host Configuration

In this example, the servers are running Ubuntu 14.04. A layer 2 bond links from server01 and server03 to the respective switch. In Ubuntu, you use subinterfaces.

{{< tabs "TabID492 ">}}
{{< tab "server01 ">}}

```
auto lo
iface lo inet loopback

auto lo
iface lo inet static
  address 10.0.0.31/32
  
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet manual
    bond-master bond1

auto eth2
iface eth2 inet manual
    bond-master bond1

auto bond1
iface bond1 inet static
  bond-slaves none
  bond-miimon 100
  bond-min-links 1
  bond-mode 802.3ad
  bond-xmit-hash-policy layer3+4
  bond-lacp-rate 1
  address 172.16.1.101/24

auto bond1.10
iface bond1.10 inet static
  address 172.16.10.101/24
  
auto bond1.20
iface bond1.20 inet static
  address 172.16.20.101/24
```

{{< /tab >}}
{{< tab "server03 ">}}

```
auto lo
iface lo inet loopback

auto lo
iface lo inet static
  address 10.0.0.33/32
  
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet manual
    bond-master bond0

auto eth2
iface eth2 inet manual
    bond-master bond0

auto bond1
iface bond1 inet static
  bond-slaves none
  bond-miimon 100
  bond-min-links 1
  bond-mode 802.3ad
  bond-xmit-hash-policy layer3+4
  bond-lacp-rate 1
  address 172.16.1.103/24

auto bond1.10
iface bond1.10 inet static
  address 172.16.10.103/24
  
auto bond1.20
iface bond1.20 inet static
  address 172.16.20.103/24
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

Run the `clagctl` command to show MLAG behavior and any inconsistencies between an MLAG pair.

```
cumulus@leaf01$ clagctl
The peer is alive
      Our Priority, ID, and Role: 32768 44:38:39:00:00:35 primary
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:36 secondary
          Peer Interface and IP: peerlink.4094 169.254.1.2
                VxLAN Anycast IP: 10.0.1.12
                      Backup IP: 10.10.10.2 (inactive)
                      System MAC: 44:38:39:BE:EF:AA
CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts     Proto-Down Reason
----------------   ----------------   -------   -----------   -----------------
           bond1   bond1              1         -             -
         vxlan20   vxlan20            -         -             -
          vxlan1   vxlan1             -         -             -
         vxlan10   vxlan10            -         -             -
```

The additions to normal MLAG behavior are:

| <div style="width:200px">Output | Explanation |
| ------------------------------- | ----------- |
| `VXLAN Anycast IP: 10.10.10.30` | The anycast IP address shared by the MLAG pair for VTEP termination is in use and is 10.10.10.30. |
| `Conflicts: -` | No conflicts exist for this MLAG Interface. |
| `Proto-Down Reason: -` | The VXLAN is up and running (there is no Proto-Down). |

In the following example, VXLAN10 has the wrong `vxlan-id`. When you run the `clagctl` command, VXLAN10 is down because this switch is the secondary switch and the peer switch takes control of VXLAN. The reason code is `vxlan-single` indicating that there is a `vxlan-id` mis-match on VXLAN10.

```
cumulus@leaf02$ clagctl
The peer is alive
    Peer Priority, ID, and Role: 32768 44:38:39:00:00:11 primary
      Our Priority, ID, and Role: 32768 44:38:39:00:00:12 secondary
          Peer Interface and IP: peerlink.4094 169.254.1.1
                VxLAN Anycast IP: 10.0.1.12
                      Backup IP: 10.10.10.1 (inactive)
                      System MAC: 44:38:39:BE:EF:AA
CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts      Proto-Down Reason
----------------   ----------------   -------   ------------   -----------------
           bond1   bond1              1         -              -
         vxlan20   vxlan20            -         -              -
          vxlan1   vxlan1             -         -              -
         vxlan10   -                  -         -              vxlan-single
```

## Considerations

### VLAN for Peer Link Layer 3 Subinterface

Do not reuse the VLAN for the peer link layer 3 subinterface for any other interface in the system. Use a high VLAN ID value. For more information on VLAN ID ranges, refer to the {{<link url="VLAN-aware-Bridge-Mode#reserved-vlan-range" text="VLAN-aware Bridge Mode">}}.

### Bonds with Vagrant in Cumulus VX

Bonds (or LACP Etherchannels) fail to work in a Vagrant configuration unless the link is in *promiscuous* mode. This is a limitation on virtual topologies only.

```
auto swp49
iface swp49
  #for vagrant so bonds work correctly
  post-up ip link set $IFACE promisc on

auto swp50
iface swp50
  #for vagrant so bonds work correctly
  post-up ip link set $IFACE promisc on
```

For more information on using Cumulus VX and Vagrant, refer to the [Cumulus VX documentation]({{<ref "/cumulus-vx" >}}).
