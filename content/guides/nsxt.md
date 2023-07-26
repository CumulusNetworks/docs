---
title: Cumulus Linux Deployment Guide for VMware NSX-T
author: NVIDIA Networking
weight: 50
product: Technical Guides
---

VMware NSX-T provides an agile software-defined infrastructure to build cloud-native application environments. It aims to provide automation, simplicity in operations, networking, and security.
NSX-T supports various type of environments like multi-hypervisor, bare metal workloads, hybrid/public clouds and more. It serves as the control-plane, data-plane, and management-plane for VMware virtualized overlay solutions.

A VMware virtualized environment requires all virtual and physical elements such as ESXi hypervisors and NSX Edges to communicate to one another over an underlay IP fabric. NVIDIA Spectrum switches provides best-in-class underlay hardware leveraging the Spectrum ASIC providing speeds of 1 to 400Gbps. With NVIDIA Cumulus Linux OS software, the underlying fabric configuration can be easily provisioned to ensure VMware NSX-T proper operations.

This guide shows the physical infrastructure configuration required for a few of the most common use cases of VMware NSX-T deployments. The underlay fabric configuration is based on Cumulus Linux 5.X using the NVIDIA User Experience ([NVUE](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-52/System-Configuration/NVIDIA-User-Experience-NVUE/NVUE-CLI/)) CLI.

{{%notice note%}}
We focus only on the VM-to-VM and VM-to-BM user traffic. Thus, other networks such as management, vMotion, and others are not covered in the configuration.
{{%/notice%}}

This guide describes the following scenarios:

- [Pure Virtualized Environment](#pure-virtualized-environment)
- [Virtualized and Bare Metal Server Environment](#virtualized-and-bare-metal-server-environment)
- [Virtualized Environment Over EVPN Fabric](#virtualized-environment-over-evpn-fabric)
- [Virtualized Environment Over EVPN Fabric with an External Network (EVPN Type-5 Routes)](#virtualized-environment-over-evpn-fabric-with-an-external-network-evpn-type-5-routes)

To accomplish the above scenarios, we use the following features and protocols:

- [Multi-Chassis Link Aggregation - MLAG]({{<ref "/cumulus-linux-52/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}}) for active-active physical layer 2 connectivity
- [Virtual Router Redundancy - VRR and VRRP]({{<ref "/cumulus-linux-52/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP" >}}) for active-active and redundant layer 3 gateways
- [Border Gateway Protocol - BGP]({{<ref "/cumulus-linux-52/Layer-3/Border-Gateway-Protocol-BGP" >}}) for underlay IP fabric connectivity between all physical and logical elements. We use [Auto BGP]({{<ref "/cumulus-linux-52/Layer-3/Border-Gateway-Protocol-BGP/#auto-bgp" >}}) and [BGP Unnumbered]({{<ref "/cumulus-linux-52/Layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered" >}}) for faster and easier fabric configuration. This is the preferred best practice.
- [Virtual Extensible LAN - VXLAN]({{<ref "/cumulus-linux-52/Network-Virtualization" >}}) for overlay encapsulation data plane.
- [Ethernet Virtual Private Network - EVPN]({{<ref "/cumulus-linux-52/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN" >}}) control plane to provide [EVPN Layer 2 Extension]({{<ref "/cumulus-linux-52/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Basic-Configuration" >}}) for ESXi hosts.

{{%notice note%}}

NSX-T configuration is not covered in this guide. Check out the this [How-to](https://docs.nvidia.com/networking/pages/releaseview.action?pageId=71022743#Howto:InstallandConfigureanNSXTwithNVIDIANetworkFabric.-Network) guide for some examples.

For more information regarding VMware NSX-T specific design, installation and configuration check the following resources:

- [NSX-T Reference Design](https://nsx.techzone.vmware.com/resource/nsx-t-reference-design-guide-3-0)
- [NSX-T Physical Infrastructure of the Data Center](https://nsx.techzone.vmware.com/resource/nsx-t-reference-design-guide-3-0#_Physical_Infrastructure_of_1) 
- [NSX-T Data Center Installation Guide](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/installation/GUID-3E0C4CEC-D593-4395-84C4-150CD6285963.html)
- [NSX-T Data Center Administration Guide](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/administration/GUID-FBFD577B-745C-4658-B713-A3016D18CB9A.html).

{{%/notice %}}

The below is the referance topology used for this guide. New devices may be added to match different scenarios.

{{<figure src="images/guides/cumulus-nsxt/pure_L2.jpg">}}

**Rack 1** – Two NVIDIA Switches in MLAG + One ESXi hypervisor connected in active-active bonding  
**Rack 2** – Two NVIDIA Switches in MLAG + One ESXi hypervisor connected in active-active bonding

### Physical Connectivity

{{< tabs "TABID010 ">}}

{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost       RemotePort
---------  -----  -------  ---------------  -----------------
eth0       1G     Mgmt     oob-mgmt-switch  swp10
swp1       1G     Default  esxi01           44:38:39:00:00:32
swp49      1G     Default  leaf02           swp49
swp50      1G     Default  leaf02           swp50
swp51      1G     Default  spine01          swp1
swp52      1G     Default  spine02          swp1
```
{{< /tab >}}

{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost       RemotePort
---------  -----  -------  ---------------  -----------------
eth0       1G     Mgmt     oob-mgmt-switch  swp11
swp1       1G     Default  esxi01           44:38:39:00:00:38
swp49      1G     Default  leaf01           swp49
swp50      1G     Default  leaf01           swp50
swp51      1G     Default  spine01          swp2
swp52      1G     Default  spine02          swp2
```
{{< /tab >}}

{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost       RemotePort
---------  -----  -------  ---------------  -----------------
eth0       1G     Mgmt     oob-mgmt-switch  swp12
swp1       1G     Default  esxi03           44:38:39:00:00:3e
swp49      1G     Default  leaf04           swp49
swp50      1G     Default  leaf04           swp50
swp51      1G     Default  spine01          swp3
swp52      1G     Default  spine02          swp3
```
{{< /tab >}}

{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost       RemotePort
---------  -----  -------  ---------------  -----------------
eth0       1G     Mgmt     oob-mgmt-switch  swp13
swp1       1G     Default  esxi03           44:38:39:00:00:44
swp49      1G     Default  leaf03           swp49
swp50      1G     Default  leaf03           swp50
swp51      1G     Default  spine01          swp4
swp52      1G     Default  spine02          swp4
```
{{< /tab >}}

{{< tab "spine01 ">}}
```
cumulus@spine01:mgmt:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost       RemotePort
---------  -----  -------  ---------------  ----------
eth0       1G     Mgmt     oob-mgmt-switch  swp14
swp1       1G     Default  leaf01           swp51
swp2       1G     Default  leaf02           swp51
swp3       1G     Default  leaf03           swp51
swp4       1G     Default  leaf04           swp51
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
cumulus@spine02:mgmt:~$ net show lldp

LocalPort  Speed  Mode     RemoteHost       RemotePort
---------  -----  -------  ---------------  ----------
eth0       1G     Mgmt     oob-mgmt-switch  swp15
swp1       1G     Default  leaf01           swp52
swp2       1G     Default  leaf02           swp52
swp3       1G     Default  leaf03           swp52
swp4       1G     Default  leaf04           swp52
```

{{< /tab >}}
{{< /tabs >}}

### MTU Configuration

VMware recommends configuring jumbo MTU (9KB) on all virtual and physical network elements end-to-end. On VMkernel ports, virtual switches (VDS), VDS Port-Groups, N-VDS and the underlay physical network. Geneve encapsulation, requires a minimum MTU of `1600B` (but `1700B` for extended options). VMware recommends using at least a 9000-byte MTU for the entire network path. This improves the throughput of storage, vSAN, vMotion, NFS and vSphere Replication.

Using the below commands, you can examine switches' physical interfaces MTU settings. By default, all interfaces on Cumulus Linux have MTU 9216 configured, and require no additional configuration.

{{< tabs "4tt16 ">}}

{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv show interface
Interface  MTU    Speed  State  Remote Host      Remote Port        Type      Summary
---------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ eth0     1500   1G     up     oob-mgmt-switch  swp10              eth       IP Address: 192.168.200.11/24
+ lo       65536         up                                         loopback  IP Address:       127.0.0.1/8
  lo                                                                          IP Address:           ::1/128
+ swp1     9216   1G     up     esxi01           44:38:39:00:00:32  swp
+ swp49    9216   1G     up     leaf02           swp49              swp
+ swp50    9216   1G     up     leaf02           swp50              swp
+ swp51    9216   1G     up     spine01          swp1               swp
+ swp52    9216   1G     up     spine02          swp1               swp
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv show interface
Interface  MTU    Speed  State  Remote Host      Remote Port        Type      Summary
---------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ eth0     1500   1G     up     oob-mgmt-switch  swp11              eth       IP Address: 192.168.200.12/24
+ lo       65536         up                                         loopback  IP Address:       127.0.0.1/8
  lo                                                                          IP Address:           ::1/128
+ swp1     9216   1G     up     esxi01           44:38:39:00:00:38  swp
+ swp49    9216   1G     up     leaf01           swp49              swp
+ swp50    9216   1G     up     leaf01           swp50              swp
+ swp51    9216   1G     up     spine01          swp2               swp
+ swp52    9216   1G     up     spine02          swp2               swp
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv show interface
Interface  MTU    Speed  State  Remote Host      Remote Port        Type      Summary
---------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ eth0     1500   1G     up     oob-mgmt-switch  swp12              eth       IP Address: 192.168.200.13/24
+ lo       65536         up                                         loopback  IP Address:       127.0.0.1/8
  lo                                                                          IP Address:           ::1/128
+ swp1     9216   1G     up     esxi03           44:38:39:00:00:3e  swp
+ swp49    9216   1G     up     leaf04           swp49              swp
+ swp50    9216   1G     up     leaf04           swp50              swp
+ swp51    9216   1G     up     spine01          swp3               swp
+ swp52    9216   1G     up     spine02          swp3               swp
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv show interface
Interface  MTU    Speed  State  Remote Host      Remote Port        Type      Summary
---------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ eth0     1500   1G     up     oob-mgmt-switch  swp13              eth       IP Address: 192.168.200.14/24
+ lo       65536         up                                         loopback  IP Address:       127.0.0.1/8
  lo                                                                          IP Address:           ::1/128
+ swp1     9216   1G     up     esxi03           44:38:39:00:00:44  swp
+ swp49    9216   1G     up     leaf03           swp49              swp
+ swp50    9216   1G     up     leaf03           swp50              swp
+ swp51    9216   1G     up     spine01          swp4               swp
+ swp52    9216   1G     up     spine02          swp4               swp
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
cumulus@spine01:mgmt:~$ nv show interface
Interface  MTU    Speed  State  Remote Host      Remote Port  Type      Summary
---------  -----  -----  -----  ---------------  -----------  --------  -----------------------------
+ eth0     1500   1G     up     oob-mgmt-switch  swp14        eth       IP Address: 192.168.200.21/24
+ lo       65536         up                                   loopback  IP Address:       127.0.0.1/8
  lo                                                                    IP Address:           ::1/128
+ swp1     9216   1G     up     leaf01           swp51        swp
+ swp2     9216   1G     up     leaf02           swp51        swp
+ swp3     9216   1G     up     leaf03           swp51        swp
+ swp4     9216   1G     up     leaf04           swp51        swp
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
cumulus@spine02:mgmt:~$ nv show interface
Interface  MTU    Speed  State  Remote Host      Remote Port  Type      Summary
---------  -----  -----  -----  ---------------  -----------  --------  ----------------------------
+ eth0     1500   1G     up     oob-mgmt-switch  swp15        eth       IP Address:192.168.200.22/24
+ lo       65536         up                                   loopback  IP Address:      127.0.0.1/8
  lo                                                                    IP Address:          ::1/128
+ swp1     9216   1G     up     leaf01           swp52        swp
+ swp2     9216   1G     up     leaf02           swp52        swp
+ swp3     9216   1G     up     leaf03           swp52        swp
+ swp4     9216   1G     up     leaf04           swp52        swp
```
{{< /tab >}}
{{< /tabs >}}

# Pure Virtualized Environment

This use case covers a basic VMware environment - 100% virtualization based on a pure IP fabric underlay. All communications are between virtual machines (VMs) located on ESXi hypervisors.

NSX-T uses Generic Networking Virtualization Encapsulation (Geneve) as the overlay protocol to transmit virtualized traffic over layer 2 tunnels on top of the layer 3 underlay fabric. The Geneve protocol is like the well-known VXLAN encapsulation, but it has an extended header with more options. You install each NSX-T *prepared host* (with ESXi added to the NSX-T manager) with kernel modules to act as a Tunnel Endpoint (TEP) device. TEP devices are responsible for encapsulating and decapsulating traffic between virtual machines inside the virtualized network.

In the referance topology, VMs are on two different physical ESXi hypervisors. They are in the same IP subnet and connected to the same VMware Logical Switch. Because a layer 3 underlay network divides them, the NSX overlay provides VM-to-VM communication.

The ESXi hypervisors connect to the Top-of-Rack (ToR) (or leaf) switches using active-active LAG for redundancy and additional throughput. The Cumulus Linux MLAG and VRR configurations support this ESXi requirement.

{{%notice info%}}
<!-- vale off -->
You must configure MLAG and VRR when using two switch connections, regardless of which N-VDS uplink profile is in use.
<!-- vale on -->

{{% /notice %}}

### MLAG Configuration

Configure MLAG parameters and the `peerlink` interface

{{< tabs "TABtgbID123013 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:mgmt:~$ nv set interface peerlink type bond
cumulus@leaf01:mgmt:~$ nv set mlag mac-address 44:38:39:FF:00:01
cumulus@leaf01:mgmt:~$ nv set mlag backup 192.168.200.12 vrf mgmt
cumulus@leaf01:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:mgmt:~$ nv set mlag priority 1000
cumulus@leaf01:mgmt:~$ nv config apply -y
cumulus@leaf01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:mgmt:~$ nv set interface peerlink type bond
cumulus@leaf02:mgmt:~$ nv set mlag mac-address 44:38:39:FF:00:01
cumulus@leaf02:mgmt:~$ nv set mlag backup 192.168.200.11 vrf mgmt
cumulus@leaf02:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:mgmt:~$ nv set mlag priority 2000
cumulus@leaf02:mgmt:~$ nv config apply -y
cumulus@leaf02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf03:mgmt:~$ nv set interface peerlink type bond
cumulus@leaf03:mgmt:~$ nv set mlag mac-address 44:38:39:FF:00:02
cumulus@leaf03:mgmt:~$ nv set mlag backup 192.168.200.14 vrf mgmt
cumulus@leaf03:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf03:mgmt:~$ nv set mlag priority 1000
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf04:mgmt:~$ nv set interface peerlink type bond
cumulus@leaf04:mgmt:~$ nv set mlag mac-address 44:38:39:FF:00:02
cumulus@leaf04:mgmt:~$ nv set mlag backup 192.168.200.13 vrf mgmt
cumulus@leaf04:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf04:mgmt:~$ nv set mlag priority 2000
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
### N-VDS Active-Active LACP LAG Uplink Profile
<!-- vale on -->

If you use the recommended active-active LAG (LACP) N-VDS uplink profile, you must bond the switch downlink interfaces for ESXi into MLAG ports (LACP bonds).

Then, add the bond interface into the default bridge `br_default` and set its stp and lacp parameters. This action also automatically set the MLAG bond as trunk port (VLAN tagging) with all VLANs allowed.

For more information on how to assign VLANs to trunk ports, see [VLAN-aware Bridge Mode]({{<ref "/cumulus-linux-52/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode" >}}) and [Traditional Bridge Mode]({{<ref "/cumulus-linux-52/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode" >}}).

{{%notice info%}}
<!-- vale off -->
For active-standby (or active-active non-LAG) ESXi connectivity, do not configure MLAG ports and do not use the active-active LACP LAG uplink profile for the Overlay Transport Zone on N-VDS. 
<!-- vale on -->
Follow the instructions under the [N-VDS Non-LAG Uplink Profile](#n-vds-non-lag-uplink-profile) section to configure the switchports.  
{{%/notice %}}

{{< tabs "TABID0213 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv set interface esxi01 bond member swp1
cumulus@leaf01:mgmt:~$ nv set interface esxi01 type bond
cumulus@leaf01:mgmt:~$ nv set interface esxi01 bond mode lacp
cumulus@leaf01:mgmt:~$ nv set interface esxi01 bond mlag id 1
cumulus@leaf01:mgmt:~$ nv set interface esxi01 bridge domain br_default
cumulus@leaf01:mgmt:~$ nv set interface esxi01 bridge domain br_default stp bpdu-guard on
cumulus@leaf01:mgmt:~$ nv set interface esxi01 bridge domain br_default stp admin-edge on
cumulus@leaf01:mgmt:~$ nv set interface esxi01 bond lacp-bypass on
cumulus@leaf01:mgmt:~$ nv config apply -y
cumulus@leaf01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv set interface esxi01 bond member swp1
cumulus@leaf02:mgmt:~$ nv set interface esxi01 type bond
cumulus@leaf02:mgmt:~$ nv set interface esxi01 bond mode lacp
cumulus@leaf02:mgmt:~$ nv set interface esxi01 bond mlag id 1
cumulus@leaf02:mgmt:~$ nv set interface esxi01 bridge domain br_default
cumulus@leaf02:mgmt:~$ nv set interface esxi01 bridge domain br_default stp bpdu-guard on
cumulus@leaf02:mgmt:~$ nv set interface esxi01 bridge domain br_default stp admin-edge on
cumulus@leaf02:mgmt:~$ nv set interface esxi01 bond lacp-bypass on
cumulus@leaf02:mgmt:~$ nv config apply -y
cumulus@leaf02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set interface esxi03 bond member swp1
cumulus@leaf03:mgmt:~$ nv set interface esxi03 type bond
cumulus@leaf03:mgmt:~$ nv set interface esxi03 bond mode lacp
cumulus@leaf03:mgmt:~$ nv set interface esxi03 bond mlag id 1
cumulus@leaf03:mgmt:~$ nv set interface esxi03 bridge domain br_default
cumulus@leaf03:mgmt:~$ nv set interface esxi03 bridge domain br_default stp bpdu-guard on
cumulus@leaf03:mgmt:~$ nv set interface esxi03 bridge domain br_default stp admin-edge on
cumulus@leaf03:mgmt:~$ nv set interface esxi03 bond lacp-bypass on
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set interface esxi03 bond member swp1
cumulus@leaf04:mgmt:~$ nv set interface esxi03 type bond
cumulus@leaf04:mgmt:~$ nv set interface esxi03 bond mode lacp
cumulus@leaf04:mgmt:~$ nv set interface esxi03 bond mlag id 1
cumulus@leaf04:mgmt:~$ nv set interface esxi03 bridge domain br_default
cumulus@leaf04:mgmt:~$ nv set interface esxi03 bridge domain br_default stp bpdu-guard on
cumulus@leaf04:mgmt:~$ nv set interface esxi03 bridge domain br_default stp admin-edge on
cumulus@leaf04:mgmt:~$ nv set interface esxi03 bond lacp-bypass on
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}

<!-- vale off -->
### N-VDS Non-LAG Uplink Profile
<!-- vale on -->

If you use active-standby or active-active, non-LAG N-VDS uplink profiles, you must keep the switch downlink interfaces for ESXi configured as regular switchports; do not use any MLAG port configurations. You must add them to the default bridge `br_default`, they are automaticaly will be set as trunk ports.

{{< tabs "TABID0112213 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bridge domain br_default
cumulus@leaf01:mgmt:~$ nv config apply -y
cumulus@leaf01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv set interface swp1 bridge domain br_default
cumulus@leaf02:mgmt:~$ nv config apply -y
cumulus@leaf02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set interface swp1 bridge domain br_default
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set interface swp1 bridge domain br_default
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}

### MLAG Configuration Verification

Use the `nv show mlag` command to verify MLAG configurations and `net show clag` or `clagctl` commands to see the MLAG interfaces information. In this example `esxi01` and `esxi03` are the MLAG bond interfaces connected to ESXi hosts.

{{< tabs "TABID012 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv show mlag
                operational              applied            description
--------------  -----------------------  -----------------  ------------------------------------------------------
enable                                   on                 Turn the feature 'on' or 'off'.  The default is 'off'.
debug                                    off                Enable MLAG debugging
init-delay                               100                The delay, in seconds, before bonds are brought up.
mac-address     44:38:39:ff:00:01        44:38:39:ff:00:01  Override anycast-mac and anycast-id
peer-ip         fe80::4638:39ff:fe00:5a  linklocal          Peer Ip Address
priority        1000                     2000               Mlag Priority
[backup]        192.168.200.12           192.168.200.12     Set of MLAG backups
backup-active   False                                       Mlag Backup Status
backup-reason                                               Mlag Backup Reason
local-id        44:38:39:00:00:59                           Mlag Local Unique Id
local-role      primary                                     Mlag Local Role
peer-alive      True                                        Mlag Peer Alive Status
peer-id         44:38:39:00:00:5a                           Mlag Peer Unique Id
peer-interface  peerlink.4094                               Mlag Peerlink Interface
peer-priority   2000                                        Mlag Peer Priority
peer-role       secondary                                   Mlag Peer Role
```
```
cumulus@leaf01:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 1000 44:38:39:00:00:59 primary
    Peer Priority, ID, and Role: 2000 44:38:39:00:00:5a secondary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:5a (linklocal)
                      Backup IP: 192.168.200.12 vrf mgmt (active)
                     System MAC: 44:38:39:ff:00:01

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
          esxi01   esxi01             1         -                      -
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv show mlag
                operational              applied            description
--------------  -----------------------  -----------------  ------------------------------------------------------
enable                                   on                 Turn the feature 'on' or 'off'.  The default is 'off'.
debug                                    off                Enable MLAG debugging
init-delay                               100                The delay, in seconds, before bonds are brought up.
mac-address     44:38:39:ff:00:01        44:38:39:ff:00:01  Override anycast-mac and anycast-id
peer-ip         fe80::4638:39ff:fe00:59  linklocal          Peer Ip Address
priority        2000                     1000               Mlag Priority
[backup]        192.168.200.11           192.168.200.11     Set of MLAG backups
backup-active   False                                       Mlag Backup Status
backup-reason                                               Mlag Backup Reason
local-id        44:38:39:00:00:5a                           Mlag Local Unique Id
local-role      secondary                                   Mlag Local Role
peer-alive      True                                        Mlag Peer Alive Status
peer-id         44:38:39:00:00:59                           Mlag Peer Unique Id
peer-interface  peerlink.4094                               Mlag Peerlink Interface
peer-priority   1000                                        Mlag Peer Priority
peer-role       primary                                     Mlag Peer Role
```
```
cumulus@leaf02:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 2000 44:38:39:00:00:5a secondary
    Peer Priority, ID, and Role: 1000 44:38:39:00:00:59 primary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:59 (linklocal)
                      Backup IP: 192.168.200.11 vrf mgmt (active)
                     System MAC: 44:38:39:ff:00:01

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
          esxi01   esxi01             1         -                      -
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv show mlag
                operational              applied            description
--------------  -----------------------  -----------------  ------------------------------------------------------
enable                                   on                 Turn the feature 'on' or 'off'.  The default is 'off'.
debug                                    off                Enable MLAG debugging
init-delay                               100                The delay, in seconds, before bonds are brought up.
mac-address     44:38:39:ff:00:02        44:38:39:ff:00:02  Override anycast-mac and anycast-id
peer-ip         fe80::4638:39ff:fe00:5e  linklocal          Peer Ip Address
priority        1000                     2000               Mlag Priority
[backup]        192.168.200.14           192.168.200.14     Set of MLAG backups
backup-active   False                                       Mlag Backup Status
backup-reason                                               Mlag Backup Reason
local-id        44:38:39:00:00:5d                           Mlag Local Unique Id
local-role      primary                                     Mlag Local Role
peer-alive      True                                        Mlag Peer Alive Status
peer-id         44:38:39:00:00:5e                           Mlag Peer Unique Id
peer-interface  peerlink.4094                               Mlag Peerlink Interface
peer-priority   2000                                        Mlag Peer Priority
peer-role       secondary                                   Mlag Peer Role
```
```
cumulus@leaf03:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 1000 44:38:39:00:00:5d primary
    Peer Priority, ID, and Role: 2000 44:38:39:00:00:5e secondary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:5e (linklocal)
                      Backup IP: 192.168.200.14 vrf mgmt (active)
                     System MAC: 44:38:39:ff:00:02

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
          esxi03   esxi03             1         -                      -
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv show mlag
                operational              applied            description
--------------  -----------------------  -----------------  ------------------------------------------------------
enable                                   on                 Turn the feature 'on' or 'off'.  The default is 'off'.
debug                                    off                Enable MLAG debugging
init-delay                               100                The delay, in seconds, before bonds are brought up.
mac-address     44:38:39:ff:00:02        44:38:39:ff:00:02  Override anycast-mac and anycast-id
peer-ip         fe80::4638:39ff:fe00:5e  linklocal          Peer Ip Address
priority        2000                     1000               Mlag Priority
[backup]        192.168.200.13           192.168.200.13     Set of MLAG backups
backup-active   False                                       Mlag Backup Status
backup-reason                                               Mlag Backup Reason
local-id        44:38:39:00:00:5e                           Mlag Local Unique Id
local-role      secondary                                   Mlag Local Role
peer-alive      True                                        Mlag Peer Alive Status
peer-id         44:38:39:00:00:5d                           Mlag Peer Unique Id
peer-interface  peerlink.4094                               Mlag Peerlink Interface
peer-priority   1000                                        Mlag Peer Priority
peer-role       primary                                     Mlag Peer Role
```
```
cumulus@leaf04:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 2000 44:38:39:00:00:5e secondary
    Peer Priority, ID, and Role: 1000 44:38:39:00:00:5d primary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:5d (linklocal)
                      Backup IP: 192.168.200.13 vrf mgmt (active)
                     System MAC: 44:38:39:ff:00:02

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
          esxi03   esxi03             1         -                      -
```
{{< /tab >}}
{{< /tabs >}}

{{%notice info%}}
<!-- vale off -->
In Non-LAG N-VDS uplink profiles scenarios, MLAG ports **will not** appear in the show output. The lack of MLAG ports does not mean that MLAG is not functional. 
<!-- vale on -->
MLAG is mandatory for using VRR &mdash; also known as enhanced VRRP, which you need for the non-LAG uplink profiles as well.

{{%/notice %}}

### VRR Configuration

You can set the ESXi TEP IP addresses on the same or different subnets. The VMware best practice configuration for the TEP IP pool is to assign different subnets for each physical rack for simplicity.

VRR on the ToR switches provides redundant, active-active TEP subnet's default gateways to the ESXi servers.

{{%notice note%}}

VMware requires a VLAN per each type of traffic, for example, storage, vSAN, vMotion, or Overlay (TEP) traffic. Thus, SVI and VRR instances must be configured for each of them. In this example, we show only the overlay VM-to-VM communication, so only TEP VLAN and SVI/VRR are shown in switch configurations.

{{%/notice %}}

{{%notice info%}}

As this guide shows how to handle the virtualized traffic only, all configuration examples are based on the `default` VRF. In many cases, different VMware networks (traffic types) will be separated by different VRFs (e.g. Mgmt. network in `vrfX` and TEP network in `vrfY`). In this case, you should create custom VRFs for each, insert the SVIs into them and make the needed [BGP Underlay Network Configuration](http://localhost:1313/guides/nsxt/#bgp-underlay-network-configuration).

Check out [Virtual Routing and Forwarding - VRF](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-52/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF/) documentation and its [BGP](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-52/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF/#bgp) section for more information.

{{%/notice %}}

The VLAN ID is a local parameter and not shared between the hypervisors. For deployment simplicity, use the same VLAN ID for all TEP devices used in across racks. We use `VLAN 100` for our deploymet.

{{< tabs "101231231210 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 100
cumulus@leaf01:mgmt:~$ nv set interface vlan100 ip address 10.1.1.252/24
cumulus@leaf01:mgmt:~$ nv set interface vlan100 ip vrr address 10.1.1.254/24
cumulus@leaf01:mgmt:~$ nv set interface vlan100 ip vrr mac-address 00:00:00:00:01:00
cumulus@leaf01:mgmt:~$ nv set interface vlan100 ip vrr state up 
cumulus@leaf01:mgmt:~$ nv config apply -y
cumulus@leaf01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv set bridge domain br_default vlan 100
cumulus@leaf02:mgmt:~$ nv set interface vlan100 ip address 10.1.1.253/24
cumulus@leaf02:mgmt:~$ nv set interface vlan100 ip vrr address 10.1.1.254/24
cumulus@leaf02:mgmt:~$ nv set interface vlan100 ip vrr mac-address 00:00:00:00:01:00
cumulus@leaf02:mgmt:~$ nv set interface vlan100 ip vrr state up 
cumulus@leaf02:mgmt:~$ nv config apply -y
cumulus@leaf02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 100
cumulus@leaf03:mgmt:~$ nv set interface vlan100 ip address 10.2.2.252/24
cumulus@leaf03:mgmt:~$ nv set interface vlan100 ip vrr address 10.2.2.254/24
cumulus@leaf03:mgmt:~$ nv set interface vlan100 ip vrr mac-address 00:00:00:01:00:00
cumulus@leaf03:mgmt:~$ nv set interface vlan100 ip vrr state up 
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set bridge domain br_default vlan 100
cumulus@leaf04:mgmt:~$ nv set interface vlan100 ip address 10.2.2.253/24
cumulus@leaf04:mgmt:~$ nv set interface vlan100 ip vrr address 10.2.2.254/24
cumulus@leaf04:mgmt:~$ nv set interface vlan100 ip vrr mac-address 00:00:00:01:00:00
cumulus@leaf04:mgmt:~$ nv set interface vlan100 ip vrr state up 
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}

### VRR Configuration Verification

Use the `nv show interface` command to check the status of the SVI and VRR. In this output SVI and VRR interfaces are shown as `vlanXXX` and `vlanXXX-v0`.

{{< tabs "101231d23f10 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv show interface
Interface         MTU    Speed  State  Remote Host      Remote Port        Type      Summary
----------------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ esxi01          9216   1G     up                                         bond
+ eth0            1500   1G     up     oob-mgmt-switch  swp10              eth       IP Address: 192.168.200.11/24
+ lo              65536         up                                         loopback  IP Address:       127.0.0.1/8
  lo                                                                                 IP Address:           ::1/128
+ peerlink        9216   2G     up                                         bond
+ peerlink.4094   9216          up                                         sub
+ swp1            9216   1G     up     esxi01           44:38:39:00:00:32  swp
+ swp49           9216   1G     up     leaf02           swp49              swp
+ swp50           9216   1G     up     leaf02           swp50              swp
+ swp51           9216   1G     up     spine01          swp1               swp
+ swp52           9216   1G     up     spine02          swp1               swp
+ vlan100         9216          up                                         svi       IP Address:     10.1.1.252/24
+ vlan100-v0      9216          up                                         svi       IP Address:     10.1.1.254/24
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv show interface
Interface         MTU    Speed  State  Remote Host      Remote Port        Type      Summary
----------------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ esxi01          9216   1G     up                                         bond
+ eth0            1500   1G     up     oob-mgmt-switch  swp10              eth       IP Address: 192.168.200.12/24
+ lo              65536         up                                         loopback  IP Address:       127.0.0.1/8
  lo                                                                                 IP Address:           ::1/128
+ peerlink        9216   2G     up                                         bond
+ peerlink.4094   9216          up                                         sub
+ swp1            9216   1G     up     esxi01           44:38:39:00:00:38  swp
+ swp49           9216   1G     up     leaf01           swp49              swp
+ swp50           9216   1G     up     leaf01           swp50              swp
+ swp51           9216   1G     up     spine01          swp2               swp
+ swp52           9216   1G     up     spine02          swp2               swp
+ vlan100         9216          up                                         svi       IP Address:     10.1.1.253/24
+ vlan100-v0      9216          up                                         svi       IP Address:     10.1.1.254/24
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv show interface
Interface         MTU    Speed  State  Remote Host      Remote Port        Type      Summary
----------------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ esxi03          9216   1G     up                                         bond
+ eth0            1500   1G     up     oob-mgmt-switch  swp12              eth       IP Address: 192.168.200.13/24
+ lo              65536         up                                         loopback  IP Address:       127.0.0.1/8
  lo                                                                                 IP Address:           ::1/128
+ peerlink        9216   2G     up                                         bond
+ peerlink.4094   9216          up                                         sub
+ swp1            9216   1G     up     esxi03           44:38:39:00:00:3e  swp
+ swp49           9216   1G     up     leaf04           swp49              swp
+ swp50           9216   1G     up     leaf04           swp50              swp
+ swp51           9216   1G     up     spine01          swp3               swp
+ swp52           9216   1G     up     spine02          swp3               swp
+ vlan100         9216          up                                         svi       IP Address:     10.2.2.252/24
+ vlan100-v0      9216          up                                         svi       IP Address:     10.2.2.254/24
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv show interface
Interface         MTU    Speed  State  Remote Host      Remote Port        Type      Summary
----------------  -----  -----  -----  ---------------  -----------------  --------  -----------------------------
+ esxi03          9216   1G     up                                         bond
+ eth0            1500   1G     up     oob-mgmt-switch  swp13              eth       IP Address: 192.168.200.14/24
+ lo              65536         up                                         loopback  IP Address:       127.0.0.1/8
  lo                                                                                 IP Address:           ::1/128
+ peerlink        9216   2G     up                                         bond
+ peerlink.4094   9216          up                                         sub
+ swp1            9216   1G     up     esxi03           44:38:39:00:00:44  swp
+ swp49           9216   1G     up     leaf03           swp49              swp
+ swp50           9216   1G     up     leaf03           swp50              swp
+ swp51           9216   1G     up     spine01          swp4               swp
+ swp52           9216   1G     up     spine02          swp4               swp
+ vlan100         9216          up                                         svi       IP Address:     10.2.2.253/24
+ vlan100-v0      9216          up                                         svi       IP Address:     10.2.2.254/24
```
{{< /tab >}}
{{< /tabs >}}

### BGP Underlay Network Configuration

All underlay IP fabric BGP peerings in this guide use eBGP as the basis for the configuration. For simple and easy BGP configuration, use the Cumulus Linux [Auto BGP]({{<ref "/cumulus-linux-52/Layer-3/Border-Gateway-Protocol-BGP/#auto-bgp" >}}) and [BGP Unnumbered]({{<ref "/cumulus-linux-52/Layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered" >}}) configurations. 

{{%notice note%}}

The auto BGP `leaf` or `spine` keywords are only used to configure the ASN. The configuration files and `nv show` commands display the AS number.

{{%/notice %}}

{{%notice note%}}

Auto BGP configuration is only available using NVUE. If you want to use `vtysh` configuration, you must configure a BGP ASN.  
For additional details refer to the [Configuring FRRouting]({{<ref "/cumulus-linux-52/Layer-3/FRRouting" >}}) documentation.

{{%/notice %}}

{{< tabs "10 ">}}
{{< tab "NVUE Commands ">}}
{{< tabs "109 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv set router bgp enable on
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp autonomous-system leaf
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor peerlink.4094 remote-as external
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp router-id 10.10.10.1
cumulus@leaf01:mgmt:~$ nv config apply -y
cumulus@leaf01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv set router bgp enable on
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp autonomous-system leaf
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp neighbor peerlink.4094 remote-as external
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp router-id 10.10.10.2
cumulus@leaf02:mgmt:~$ nv config apply -y
cumulus@leaf02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set router bgp enable on
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp autonomous-system leaf
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor peerlink.4094 remote-as external
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp router-id 10.10.10.3
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set router bgp enable on
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp autonomous-system leaf
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor peerlink.4094 remote-as external
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp router-id 10.10.10.4
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " spine01 ">}}
```
cumulus@spine01:mgmt:~$ nv set router bgp enable on
cumulus@spine01:mgmt:~$ nv set vrf default router bgp autonomous-system spine
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp2 remote-as external
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp3 remote-as external
cumulus@spine01:mgmt:~$ nv set vrf default router bgp neighbor swp4 remote-as external
cumulus@spine01:mgmt:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on   
cumulus@spine01:mgmt:~$ nv set vrf default router bgp router-id 10.10.10.101
cumulus@spine01:mgmt:~$ nv config apply -y
cumulus@spine01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " spine02 ">}}
```
cumulus@spine02:mgmt:~$ nv set router bgp enable on
cumulus@spine02:mgmt:~$ nv set vrf default router bgp autonomous-system spine
cumulus@spine02:mgmt:~$ nv set vrf default router bgp neighbor swp1 remote-as external
cumulus@spine02:mgmt:~$ nv set vrf default router bgp neighbor swp2 remote-as external
cumulus@spine02:mgmt:~$ nv set vrf default router bgp neighbor swp3 remote-as external
cumulus@spine02:mgmt:~$ nv set vrf default router bgp neighbor swp4 remote-as external
cumulus@spine02:mgmt:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on   
cumulus@spine02:mgmt:~$ nv set vrf default router bgp router-id 10.10.10.102
cumulus@spine02:mgmt:~$ nv config apply -y
cumulus@spine02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "vtysh Commands ">}}
{{< tabs "205 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# bgp router-id 10.10.10.1
leaf01(config-router)# neighbor peerlink.4094 interface remote-as external
leaf01(config-router)# neighbor swp51 remote-as external
leaf01(config-router)# neighbor swp52 remote-as external
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf03:~$ sudo vtysh
leaf02# configure terminal
leaf02(config)# router bgp 65102
leaf02(config-router)# bgp router-id 10.10.10.2
leaf02(config-router)# neighbor peerlink.4094 interface remote-as external
leaf02(config-router)# neighbor swp51 remote-as external
leaf02(config-router)# neighbor swp52 remote-as external
leaf02(config-router)# end
leaf02# write memory
leaf02# exit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:~$ sudo vtysh
leaf03# configure terminal
leaf03(config)# router bgp 65103
leaf03(config-router)# bgp router-id 10.10.10.3
leaf03(config-router)# neighbor peerlink.4094 interface remote-as external
leaf03(config-router)# neighbor swp51 remote-as external
leaf03(config-router)# neighbor swp52 remote-as external
leaf03(config-router)# end
leaf03# write memory
leaf03# exit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:~$ sudo vtysh
leaf04# configure terminal
leaf04(config)# router bgp 65104
leaf04(config-router)# bgp router-id 10.10.10.4
leaf04(config-router)# neighbor peerlink.4094 interface remote-as external
leaf04(config-router)# neighbor swp51 remote-as external
leaf04(config-router)# neighbor swp52 remote-as external
leaf04(config-router)# end
leaf04# write memory
leaf04# exit
```
{{< /tab >}}
{{< tab " spine01 ">}}
```
cumulus@spine01:~$ sudo vtysh
spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# bgp router-id 10.10.10.101
spine01(config-router)# neighbor swp1 remote-as external
spine01(config-router)# neighbor swp2 remote-as external
spine01(config-router)# neighbor swp3 remote-as external
spine01(config-router)# neighbor swp4 remote-as external
spine01(config-router)# bgp bestpath as-path multipath-relax
spine01(config-router)# end
spine01# write memory
spine01# exit
```
{{< /tab >}}
{{< tab " spine02 ">}}
```
cumulus@spine02:~$ sudo vtysh
spine02# configure terminal
spine02(config)# router bgp 65199
spine02(config-router)# bgp router-id 10.10.10.102
spine02(config-router)# neighbor swp1 remote-as external
spine02(config-router)# neighbor swp2 remote-as external
spine02(config-router)# neighbor swp3 remote-as external
spine02(config-router)# neighbor swp4 remote-as external
spine02(config-router)# bgp bestpath as-path multipath-relax
spine02(config-router)# end
spine02# write memory
spine02# exit
```
{{< /tab >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tabs >}}

### TEP VLAN Subnets Advertisement into BGP

ESXi hypervisors build layer 2 overlay tunnels to send Geneve encapsulated traffic over the layer 3 underlay. The underlying IP fabric must be aware of each TEP device address in the network. Advertising the local Overlay TEP VLAN (TEP subnet) you created earlier into BGP makes this happen.

Use the `redistribute connected` command to inject directly connected routes into BGP. You can also use this command with filtering to prevent the advertising of unwanted routes into BGP. For more information, see the [Route Filtering and Redistribution]({{<ref "/cumulus-linux-52/Layer-3/Routing/Route-Filtering-and-Redistribution" >}}) documentation.

{{< tabs "101rr0 ">}}
{{< tab "NVUE Commands ">}}
{{< tabs "109dd0 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf01:mgmt:~$ nv config apply -y
cumulus@leaf01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf02:mgmt:~$ nv config apply -y
cumulus@leaf02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "vtysh Commands ">}}
{{< tabs "21d05 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 
leaf01(config-router)# address-family ipv4 unicast
leaf01(config-router-af)# redistribute connected
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:~$ sudo vtysh
leaf02# configure terminal
leaf02(config)# router bgp 
leaf02(config-router)# address-family ipv4 unicast
leaf02(config-router-af)# redistribute connected
leaf02(config-router)# end
leaf02# write memory
leaf02# exit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:~$ sudo vtysh
leaf03# configure terminal
leaf03(config)# router bgp 
leaf03(config-router)# address-family ipv4 unicast
leaf03(config-router-af)# redistribute connected
leaf03(config-router)# end
leaf03# write memory
leaf03# exit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:~$ sudo vtysh
leaf04# configure terminal
leaf04(config)# router bgp 
leaf04(config-router)# address-family ipv4 unicast
leaf04(config-router-af)# redistribute connected
leaf04(config-router)# end
leaf04# write memory
leaf04# exit
```
{{< /tab >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tabs >}}

### BGP Peerings and Route Advertisement Verification

Use the `net show bgp summary` command in NVUE, or `show ip bgp summary` in `vtysh` to verify BGP peerings status and information.

{{< tabs "TABID1431 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.1, local AS number 4259632651 vrf-id 0
BGP table version 2
RIB entries 3, using 576 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf02(peerlink.4094) 4 4259632649       367       366        0    0    0 00:18:05            2        2
spine01(swp51)        4 4200000000       366       364        0    0    0 00:17:59            1        2
spine02(swp52)        4 4200000000       368       366        0    0    0 00:18:04            1        2

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.2, local AS number 4259632649 vrf-id 0
BGP table version 3
RIB entries 3, using 576 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(peerlink.4094) 4 4259632651       410       412        0    0    0 00:20:16            2        2
spine01(swp51)        4 4200000000       413       412        0    0    0 00:20:19            2        2
spine02(swp52)        4 4200000000       411       410        0    0    0 00:20:13            2        2

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.3, local AS number 4259632661 vrf-id 0
BGP table version 2
RIB entries 3, using 576 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf04(peerlink.4094) 4 4259632667       418       417        0    0    0 00:20:38            2        2
spine01(swp51)        4 4200000000       419       417        0    0    0 00:20:37            1        2
spine02(swp52)        4 4200000000       417       415        0    0    0 00:20:32            1        2

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.4, local AS number 4259632667 vrf-id 0
BGP table version 3
RIB entries 3, using 576 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf03(peerlink.4094) 4 4259632661       448       449        0    0    0 00:22:10            2        2
spine01(swp51)        4 4200000000       449       448        0    0    0 00:22:09            2        2
spine02(swp52)        4 4200000000       447       446        0    0    0 00:22:03            2        2

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
cumulus@spine01:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.101, local AS number 4200000000 vrf-id 0
BGP table version 27
RIB entries 3, using 576 bytes of memory
Peers 4, using 85 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(swp1)    4 4259632651     46052     46073        0    0    0 00:22:34            1        2
leaf02(swp2)    4 4259632649     46061     46091        0    0    0 00:22:43            1        2
leaf03(swp3)    4 4259632661     46125     46147        0    0    0 00:22:33            1        2
leaf04(swp4)    4 4259632667     46133     46168        0    0    0 00:22:33            1        2

Total number of neighbors 4
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
cumulus@spine02:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.102, local AS number 4200000000 vrf-id 0
BGP table version 21
RIB entries 3, using 576 bytes of memory
Peers 4, using 85 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(swp1)    4 4259632651     46047     46061        0    0    0 00:23:04            1        2
leaf02(swp2)    4 4259632649     46049     46073        0    0    0 00:23:03            1        2
leaf03(swp3)    4 4259632661     46112     46158        0    0    0 00:22:53            1        2
leaf04(swp4)    4 4259632667     46111     46149        0    0    0 00:22:53            1        2

Total number of neighbors 4
```
{{< /tab >}}
{{< /tabs >}}

After establishing all BGP peerings, every redistributed local TEP subnet appears in the routing table of each switch. Use the `net show route` command in NVUE, or `show ip route` in `vtysh` to check the routing table.

{{< tabs "TABID1631 ">}}
{{< tab "leaf01 ">}}
Leaf01 has two ECMP routes (via both spine switches) to ESXi03 TEP subnet received by BGP - `10.2.2.0/24`
```
cumulus@leaf01:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
C * 10.1.1.0/24 [0/1024] is directly connected, vlan100-v0, 00:28:07
C>* 10.1.1.0/24 is directly connected, vlan100, 00:28:07
B>* 10.2.2.0/24 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 00:10:13
  *                    via fe80::4638:39ff:fe00:3, swp52, weight 1, 00:10:13
```
{{< /tab >}}
{{< tab "leaf02 ">}}
Leaf02 has two ECMP routes (via both spine switches) to ESXi03 TEP subnet received by BGP - `10.2.2.0/24`
```
cumulus@leaf02:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
C * 10.1.1.0/24 [0/1024] is directly connected, vlan100-v0, 00:28:17
C>* 10.1.1.0/24 is directly connected, vlan100, 00:28:17
B>* 10.2.2.0/24 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 00:10:19
  *                    via fe80::4638:39ff:fe00:b, swp52, weight 1, 00:10:19
```
{{< /tab >}}
{{< tab "leaf03 ">}}
Leaf03 has two ECMP routes (via both spine switches) to ESXi01 TEP subnet received by BGP - `10.1.1.0/24`
```
cumulus@leaf03:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.1.1.0/24 [20/0] via fe80::4638:39ff:fe00:11, swp51, weight 1, 00:10:27
  *                    via fe80::4638:39ff:fe00:13, swp52, weight 1, 00:10:27
C * 10.2.2.0/24 [0/1024] is directly connected, vlan100-v0, 00:28:11
C>* 10.2.2.0/24 is directly connected, vlan100, 00:28:11
```
{{< /tab >}}
{{< tab "leaf04 ">}}
Leaf04 has two ECMP routes (via both spine switches) to ESXi01 TEP subnet received by BGP - `10.1.1.0/24`
```
cumulus@leaf04:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.1.1.0/24 [20/0] via fe80::4638:39ff:fe00:19, swp51, weight 1, 00:10:30
  *                    via fe80::4638:39ff:fe00:1b, swp52, weight 1, 00:10:30
C * 10.2.2.0/24 [0/1024] is directly connected, vlan100-v0, 00:28:11
C>* 10.2.2.0/24 is directly connected, vlan100, 00:28:11
```
{{< /tab >}}
{{< tab "spine01 ">}}
Spine01 has two ECMP routes to each of the ESXi hypervisors' TEP subnet received by BGP - `10.1.1.0/24` and `10.2.2.0/24`
```
cumulus@spine01:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.1.1.0/24 [20/0] via fe80::4638:39ff:fe00:2, swp1, weight 1, 00:07:44
  *                    via fe80::4638:39ff:fe00:a, swp2, weight 1, 00:07:44
B>* 10.2.2.0/24 [20/0] via fe80::4638:39ff:fe00:12, swp3, weight 1, 00:07:39
  *                    via fe80::4638:39ff:fe00:1a, swp4, weight 1, 00:07:39
```
{{< /tab >}}
{{< tab "spine02 ">}}
Spine02 has two ECMP routes to each of the ESXi hypervisors' TEP subnet received by BGP - `10.1.1.0/24` and `10.2.2.0/24`
```
cumulus@spine02:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.1.1.0/24 [20/0] via fe80::4638:39ff:fe00:4, swp1, weight 1, 00:09:28
  *                    via fe80::4638:39ff:fe00:c, swp2, weight 1, 00:09:28
B>* 10.2.2.0/24 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:09:24
  *                    via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:09:24
```
{{< /tab >}}
{{< /tabs >}}

### Traffic Flow

ESXi hypervisors can reach each TEP address and build Geneve tunnels for the overlay VM-to-VM traffic.

This section describes two traffic flow examples:
- [Layer 2 Virtualized Traffic](#layer-2-virtualized-traffic)
- [Layer 3 Virtualized Traffic](#layer-3-virtualized-traffic)

### Layer 2 Virtualized Traffic

ESXi assigns both VMs to the same VMware logical segment, placing them into the same subnet. Each segment has its own unique virtual network identifier (VNI) assigned by NSX-T. It adds this VNI into the Geneve packet header on the source TEP. The destination TEP identifies which segment the traffic belongs to based on this VNI. All segments that share the same Overlay Transport Zone, use the same TEP addresses to establish the tunnels. It is possible to have more than one Overlay TZ on the N-VDS, but for this case, you need to configure more TEP VLANs and advertise them on the underlay switches. This scenario uses only one Overlay TZ (one TEP VLAN).

{{<figure src="images/guides/cumulus-nsxt/Pure_L2_VNI.jpg">}}

VM1 `172.16.0.1` on ESXi01 sends traffic to VM3 `172.16.0.3` on ESXi03:
1. The packet reaches the local hypervisor's TEP device `10.1.1.1`.
2. The local TEP device encapsulates it into a new Geneve packet and inserts the assigned to segment VNI `65510`.  
The new encapsulated packet's source IP address is the local TEP IP `10.1.1.1`, and the destination IP address is the remote TEP device `10.2.2.1`.
3. The encapsulated packet is routed to the remote TEP device through the underlay network.
4. The remote TEP device (ESXi03) receives and decapsulates the Geneve encapsulated packet.
5. The traffic forwarded to the destination VM3 based on the VNI inside the Geneve header.

### Layer 3 Virtualized Traffic

This scenario examines two segments (logical switches) with two VMs assigned to each. A unique VNI is assigned to each segment.
For communication between segments, or as VMware calls it “east-west traffic” traffic, the traffic must be routed using a Tier 1 Gateway (T1 Router). The T1 Router is a logical distributed router that exists in each ESXi hypervisor and connects to each of the logical segments. It is the segment’s default gateway and routes traffic between different segments.

{{%notice info%}}

Routing in VMware environments always done as close to the source as possible.

{{%/notice %}}

{{<figure src="images/guides/cumulus-nsxt/T1.jpg">}}

VM1 and VM3 are in `VLAN100` `172.16.0.0/24` - VNI `65510`.  
VM2 and VM4 are in `VLAN200` `172.16.1.0/24` - VNI `65520`.

Both segments assigned to the same Overlay TZ which uses the same TEP VLAN (with TEP IPs `10.1.1.0` and `10.2.2.1`) to establish overlay Geneve tunnel between the physical ESXi01 and ESX03 hypervisors. No additional configuration is required on the switches.  
Traffic within the same segment handled the same way as [Layer 2 Virtualized Traffic](#layer-2-virtualized-traffic) scenario.

{{%notice note%}}

Multiple T1 routers may be used for load balancing across segments. Then those routers connected using Tier-0 Gateway (T0 Router). T1-to-T0 routers model is described in the [traffic flows](#traffic-flow-1) section of Virtual and bare metal Server Environments.

{{%/notice %}}

VM1 `172.16.0.1` on ESXi01 sends traffic to VM4 `172.16.1.4` on ESXi03:

1. Inside ESXi01 a routed packet arrives at the local T1 router.
2. The T1 router examines its routing table to determine the destination path.
3. As `VLAN200` segment is also attached to the same T1 router, the packet is routed into the destination VLAN200 segment.
4. The local TEP then encapsulates the packet into Geneve using VNI `65520` of `VLAN200` segment. The Geneve packet's source and destination IP addresses are of the TEP devices `10.1.1.1` and `10.2.2.1)`.
5. The encapsulated packet sent to remote TEP device over the Geneve overlay tunnel based on the underlay IP fabric BGP routing.
6. Remote TEP device (ESXi03) receives and decapsulates the Geneve encapsulated packet.
7. The traffic forwarded to the destination VM4 based on the VNI inside the Geneve header.

# Virtualized and Bare Metal Server Environment

This use case covers VMware virtualized environment with the need to connect to a bare metal (BM) server. This could the when the virtualized environment is deployed as part of an already existing fabric (brownfield) and VMs need to communicate with a legacy or any other server which doesn’t run VMs (not part of the virtualized world).

In cases where VMs needs to communicate with non-NSX (bare metal) servers an [NSX Edge](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/installation/GUID-5EF2998C-4867-4DA6-B1C6-8A6F8EBCC411.html) deployment is required. The NSX Edge is a gateway between the virtualized Geneve overlay and the outside physical underlay. It acts as a TEP device and as an underlay router by establishing BGP (or OSPF) peering with the underlay fabric to route traffic in and out of the virtualized environment.

{{%notice note%}}

There is an option for VM to bare metal communication using Geneve encapsulation that is described in the [NSX Edge on Bare Metal](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.2/installation/GUID-21E4C80B-5900-433A-BEA2-EA41FBE690FE.html). This is beyond the scope of this guide.

{{%/notice %}}

The example configurations are based on the following topology:

{{<figure src="images/guides/cumulus-nsxt/virt_bare_metal.jpg">}}

**Rack 1** – Two NVIDIA Switches in MLAG + One ESXi hypervisor connected in active-active bonding  
**Rack 2** – Two NVIDIA Switches in MLAG + One ESXi hypervisor and One bare metal server, both connected in active-active bonding

The configurations to support an NSX Edge node are nearly identical to the existing ESXi configurations previously described.
Only the required changes to support an NSX Edge device are described below.

### VRR Configuration

NSX Edge uses two additional virtual uplinks (VLANs) to communicate with the physical world. One VLAN is used to provide connectivity to the underlay physical network while the second VLAN connects to the virtual overlay network. NSX Edge nodes do not support LACP bonding. To provide load balancing each VLAN will be configured over a single link to a single top-of-rack switch.

{{% notice note %}}
The following example utilizes Subinterfaces.  
VLANs may also also be configured for NSX Edge node connectivity. There is no technical reason to choose VLANs or subinterfaces.
{{% /notice %}}

{{< tabs "10D ">}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 100                            ### TEP VLAN
cumulus@leaf03:mgmt:~$ nv set interface vlan100 ip address 10.2.2.252/24                   ### TEP SVI
cumulus@leaf03:mgmt:~$ nv set interface vlan100 ip vrr address 10.2.2.254/24               ### TEP VRR IP (GW)
cumulus@leaf03:mgmt:~$ nv set interface vlan100 ip vrr mac-address 00:00:00:01:00:00       ### TEP VRR MAC (GW)
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 200                            ### BM VLAN
cumulus@leaf03:mgmt:~$ nv set interface vlan200 ip address 192.168.0.252/24                ### BM SVI
cumulus@leaf03:mgmt:~$ nv set interface vlan200 ip vrr address 192.168.0.254/24            ### BM VRR IP (GW)
cumulus@leaf03:mgmt:~$ nv set interface vlan200 ip vrr mac-address 00:00:00:19:21:68       ### BM VRR MAC (GW)
cumulus@leaf03:mgmt:~$ nv set interface swp1.30 type sub                                   ### Edge VLAN30 subinterface
cumulus@leaf03:mgmt:~$ nv set interface swp1.30 ip address 10.30.0.254/24                  ### Edge VLAN30 subinterface SVI
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set bridge domain br_default vlan 100                            ### TEP VLAN
cumulus@leaf04:mgmt:~$ nv set interface vlan100 ip address 10.2.2.253/24                   ### TEP SVI
cumulus@leaf04:mgmt:~$ nv set interface vlan100 ip vrr address 10.2.2.254/24               ### TEP VRR IP (GW)
cumulus@leaf04:mgmt:~$ nv set interface vlan100 ip vrr mac-address 00:00:00:01:00:00       ### TEP VRR MAC (GW)
cumulus@leaf04:mgmt:~$ nv set bridge domain br_default vlan 200                            ### BM VLAN
cumulus@leaf04:mgmt:~$ nv set interface vlan200 ip address 192.168.0.253/24                ### BM SVI
cumulus@leaf04:mgmt:~$ nv set interface vlan200 ip vrr address 192.168.0.254/24            ### BM VRR IP (GW)
cumulus@leaf04:mgmt:~$ nv set interface vlan200 ip vrr mac-address 00:00:00:19:21:68       ### BM VRR MAC (GW)
cumulus@leaf04:mgmt:~$ nv set interface swp1.31 type sub                                   ### Edge VLAN31 subinterface
cumulus@leaf04:mgmt:~$ nv set interface swp1.31 ip address 10.31.0.254/24                  ### Edge VLAN31 subinterface SVI
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save                                                                     
```
{{< /tab >}}
{{< /tabs >}}

### VRR and Subinterfaces Configuration Verification

The `nv show interface` output displays the SVI and VRR interfaces as `vlanXXX` and `vlanXXX-v0`. It shows subinterfaces as `swpX.xx`

{{< tabs "10h1d23f10 ">}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv show interface
Interface         MTU    Speed  State  Remote Host      Remote Port        Type      Summary
----------------  -----  -----  -----  ---------------  -----------------  --------  -------------------------------
+ esxi03          9216   1G     up                                         bond
+ eth0            1500   1G     up     oob-mgmt-switch  swp12              eth       IP Address:   192.168.200.13/24
+ lo              65536         up                                         loopback  IP Address:         127.0.0.1/8
  lo                                                                                 IP Address:             ::1/128
+ peerlink        9216   2G     up                                         bond
+ peerlink.4094   9216          up                                         sub
+ swp1            9216   1G     up     esxi03           44:38:39:00:00:3e  swp       
+ swp1.30         9216          up                                         sub       IP Address:       10.30.0.254/24
+ swp49           9216   1G     up     leaf04           swp49              swp
+ swp50           9216   1G     up     leaf04           swp50              swp
+ swp51           9216   1G     up     spine01          swp3               swp
+ swp52           9216   1G     up     spine02          swp3               swp
+ vlan100         9216          up                                         svi       IP Address:        10.2.2.252/24
+ vlan100-v0      9216          up                                         svi       IP Address:        10.2.2.254/24
+ vlan200         9216          up                                         svi       IP Address:     192.168.0.252/24
+ vlan200-v0      9216          up                                         svi       IP Address:     192.168.0.254/24
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv show interface
Interface         MTU    Speed  State  Remote Host      Remote Port        Type      Summary
----------------  -----  -----  -----  ---------------  -----------------  --------  -------------------------------
+ esxi03          9216   1G     up                                         bond
+ eth0            1500   1G     up     oob-mgmt-switch  swp13              eth       IP Address:   192.168.200.14/24
+ lo              65536         up                                         loopback  IP Address:         127.0.0.1/8
  lo                                                                                 IP Address:             ::1/128
+ peerlink        9216   2G     up                                         bond
+ peerlink.4094   9216          up                                         sub
+ swp1            9216   1G     up     esxi03           44:38:39:00:00:44  swp       
+ swp1.30         9216          up                                         sub       IP Address:       10.31.0.254/24
+ swp49           9216   1G     up     leaf03           swp49              swp
+ swp50           9216   1G     up     leaf03           swp50              swp
+ swp51           9216   1G     up     spine01          swp4               swp
+ swp52           9216   1G     up     spine02          swp4               swp
+ vlan100         9216          up                                         svi       IP Address:        10.2.2.253/24
+ vlan100-v0      9216          up                                         svi       IP Address:        10.2.2.254/24
+ vlan200         9216          up                                         svi       IP Address:     192.168.0.253/24
+ vlan200-v0      9216          up                                         svi       IP Address:     192.168.0.254/24
```
{{< /tab >}}
{{< /tabs >}}

### BGP Underlay Network Configuration

All underlay IP fabric BGP peerings in this guide use eBGP as the basis for the configuration. The example configurations use Cumulus Linux [Auto BGP]({{<ref "/cumulus-linux-52/Layer-3/Border-Gateway-Protocol-BGP/#auto-bgp" >}}) and [BGP Unnumbered]({{<ref "/cumulus-linux-52/Layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered" >}}) configurations.

You must configure the subinterfaces on `leaf03` and `leaf04` with unique IPv4 addresses. NSX Edge nodes doesn't support BGP unnumbered.

{{%notice note%}}

Auto BGP configuration is only available using NVUE. If you want to use `vtysh` configuration, you must configure a BGP ASN.  
For additional details refer to the [Configuring FRRouting]({{<ref "/cumulus-linux-52/Layer-3/FRRouting" >}}) documentation.

{{%/notice %}}

The only change from the previous configurations is to add numbered BGP peerings from the leaf notes to the Edge Node server.

{{< tabs "112dfff30 ">}}
{{< tab "NVUE Commands ">}}
{{< tabs "13rr3309 ">}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp autonomous-system leaf
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor peerlink.4094 remote-as external
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp neighbor 10.30.0.1 remote-as 65555            ### BGP to Edge VM in ASN 65555
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp router-id 10.10.10.3
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp autonomous-system leaf
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor peerlink.4094 remote-as external
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor swp51 remote-as external
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor swp52 remote-as external
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp neighbor 10.31.0.1 remote-as 65555            ### BGP to Edge VM in ASN 65555
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp router-id 10.10.10.4
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "vtysh Commands ">}}
{{< tabs "203ssr34d5 ">}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:~$ sudo vtysh
leaf03# configure terminal
leaf03(config)# router bgp 65103
leaf03(config-router)# bgp router-id 10.10.10.3
leaf03(config-router)# neighbor peerlink.4094 interface remote-as external
leaf03(config-router)# neighbor swp51 remote-as external
leaf03(config-router)# neighbor swp52 remote-as external
leaf03(config-router)# neighbor 10.30.0.1 remote-as 65555
leaf03(config-router)# end
leaf03# write memory
leaf03# exit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:~$ sudo vtysh
leaf04# configure terminal
leaf04(config)# router bgp 65101
leaf04(config-router)# bgp router-id 10.10.10.4
leaf04(config-router)# neighbor peerlink.4094 interface remote-as external
leaf04(config-router)# neighbor swp51 remote-as external
leaf04(config-router)# neighbor swp52 remote-as external
leaf04(config-router)# neighbor 10.31.0.1 remote-as 65555
leaf04(config-router)# end
leaf04# write memory
leaf04# exit
```
{{< /tab >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tabs >}}

### BGP Peerings and Route Advertisement Verification

To verify all BGP peerings are established correctly, use the `net show bgp summary` command in NVUE, or `show ip bgp summary` in `vtysh`.

The numbered BGP peering to the Edge Node should appear in BGP neighbor list.

{{< tabs "TABID1ufr431 ">}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.3, local AS number 4259632661 vrf-id 0
BGP table version 2
RIB entries 3, using 576 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf04(peerlink.4094) 4 4259632667     50465     50468        0    0    0 00:22:41            5        6
spine01(swp51)        4 4200000000     50480     50503        0    0    0 00:22:54            3        6
spine02(swp52)        4 4200000000     50466     50491        0    0    0 00:22:35            4        6
10.30.0.1             4 65555           1023      1035        0    0    0 00:11:23            2        6

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.4, local AS number 4259632667 vrf-id 0
BGP table version 3
RIB entries 3, using 576 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf03(peerlink.4094) 4 4259632661     25231     25236        0    0    0 00:25:44            5        6
spine01(swp51)        4 4200000000     25232     25236        0    0    0 00:25:45            5        6
spine02(swp52)        4 4200000000     25233     25228        0    0    0 00:25:41            4        6
10.31.0.1             4 65555           1056      1076        0    0    0 00:11:35            2        6

Total number of neighbors 3
```
{{< /tab >}}
{{< /tabs >}}

### Traffic Flow

This scenario examines a VM assigned to a logical segment, `VLAN100`, in the virtualized network, a bare metal server in `VLAN200`, in the underlay network, and NSX Edge VM located on the ESXi03 host. The Edge VM is the gateway between the virtual and the physical networks (“north-south” traffic in VMware terminology). It uses two logical uplinks in VLANs 30 and 31, which have BGP peering to the underlay leaf switches to route VM to bare metal traffic.

This diagram also has both tier 0 and tier 1 routers. The T0 router has BGP peerings with the leaf switches and advertises the Overlay network routes. The T1 router is the gateway for virtual hosts.

The T0 router has a logical downlink to T1 and two logical uplinks to the leaf switches in the physical world through `VLAN30` and `VLAN31`.

The T1 router has a logical downlink into the virtual segment and a logical uplink to the T0 router.

{{%notice note%}}

NSX automatically creates the links between the T1-T0 routers and the T0 router must advertise them into the underlay BGP network.

{{%/notice %}}

{{%notice note%}}

NSX Edge VM has virtual NICs (vNICs) in each of the Overlay and VLAN Transport Zones. It receives Geneve encapsulated traffic via the TEP device in Overlay TZ (east-west traffic) and forward it to the VLAN TZ by T0 (north-south traffic).

{{%/notice %}}

{{<figure src="images/guides/cumulus-nsxt/edge.jpg">}}

As an example traffic flow, VM1 at `172.16.0.1` on ESXi01 sends traffic to the bare metal server `192.168.0.1`:

1. The packet from VM1 arrives at the local T1 Router, VM1's default gateway.
2. The T1 router examines its routing table to determine the destination path.
3. The bare metal subnet of `192.168.0.0/24` was received from the T0 router, and becomes the next hop via a Geneve tunnel.
4. Local TEP on ESXi01 encapsulates the packet into Geneve using VNI `65010` for the `VLAN100` segment. The destination is the T0 router on the Edge, ESXi03.
5. The packet is sent to ESXi03 with source and destination IPs of the TEP devices `10.1.1.1` and `10.2.2.1`.
6. The Edge TEP decapsulates the packet and forwards it to the T0 router also located inside host ESXi03.
7. The T0 router receives an IP packet with destination address `192.168.0.1` and has a next hop via the BGP peer on leaf03.
8. The packet is sent to leaf03 in VLAN30, where it is routed to VLAN200 and delivered to the bare metal server.

# Virtualized Environment Over EVPN Fabric

### EVPN Underlay Fabric

The previous examples discussed deploying NSX on a pure IP fabric. Modern data centers are often designed using [EVPN]({{<ref "/cumulus-linux-52/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN" >}}) to support multi-tenancy and layer 2 extension without VMware NSX. When NSX is deployed over an EVPN fabric it works identically as when it is deployed in a pure IP fabric. NSX operates independently from the EVPN


When using an EVPN underlay fabric, the NSX-generated Geneve packets are encapsulated into VXLAN packets on the leaf switches and transmitted over the network. When using an EVPN deployment, the simple deployment option is to configure all TEP addresses in the same subnet and use the VXLAN layer 2 extension to provide TEP to TEP connectivity.

{{%notice note%}}

Unique subnets can be used across TEP devices in an EVPN network, however, VXLAN routing must be configured in the underlay network. This deployment model is beyond the scope of this guide. For more information reference the EVPN [Inter-subnet Routing]({{<ref "/cumulus-linux-52/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing" >}}) documentation.

{{%/notice %}}

Switches configuration below based on layer 2 bridging with [VXLAN Active-active Mode]({{<ref "/cumulus-linux-52/Network-Virtualization/VXLAN-Active-Active-Mode" >}}) over BGP-EVPN underlay.

### TEP VLAN Configuration

When all TEP IP addresses exist within the same subnet, the TEP VLAN default-gateway is not required.

For the VXLAN encapsulated traffic to reach the appropriate VLAN on the other side, TEP VLAN must be mapped to the same VNI on all ToR switches connected to the ESXi hosts where the virtualized traffic might be sent.

VXLAN Tunnel Endpoints (VTEPs) use local loopback IP addresses as the tunnel source and destination. Loopback interfaces with unique IP addresses must be configured on all leaf switches and then advertised via BGP into the underlay network. When using MLAG, this is referred to as VXLAN active-active and MLAG anycast-IP must be configured using the `nve vxlan mlag shared-address` command. This causes the MLAG peers to have the same VTEP IP address which is used as the inbound VXLAN tunnel destination. 

Spine switches do not require any VXLAN specific configuration but must enable the BGP `l2vpn-evpn` address family with the leaf peers to advertise EVPN routes.

### EVPN MLAG Configuration

No modifications are required to configure MLAG for EVPN. For specific MLAG configurations reference the earlier [MLAG Configuration](#mlag-configuration) section.

{{% notice note %}}

For non-MLAG uplinks, use interfaces configuration from Pure Virtualized Environment [Switch Ports Configuration - Non-LAG N-VDS Uplink Profile](#switch-ports-configuration---non-lag-n-vds-uplink-profile).

{{% /notice %}}

### VXLAN-EVPN Configuration

Each leaf requires a unique Loopback IP to be advertised into the underlay network. It will be used as the NVE source address to establish VXLAN tunnel. 
The control-plane is based on BGP EVPN advertisements.  

The `nve vxlan mlag shared-address` must be configured on the NVE interface on both MLAG-peers so that they can be identified as one in the virtualized network.
The VLAN (`VLAN 100` in our example) assigned to the MLAG bond must be mapped to the same VNI on all ToR switches.

To configure the Loopback IPs, NVE interface and VLAN-to-VNI mapping:

{{< tabs "TABIDttii0213 ">}}
{{< tab "leaf01 ">}}
Configure the Loopback IP and the VXLAN shared-address for MLAG
```
cumulus@leaf01:mgmt:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:mgmt:~$ nv set nve vxlan mlag shared-address 10.0.1.1
```

Create NVE interface with all reqired parameters and map VLAN 100 to VNI to create the VXLAN tunnel
```
cumulus@leaf01:mgmt:~$ nv set nve vxlan enable on
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 100 vni 100100
cumulus@leaf01:mgmt:~$ nv set nve vxlan source address 10.10.10.1
cumulus@leaf01:mgmt:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf01:mgmt:~$ nv config apply -y
cumulus@leaf01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf02 ">}}
Configure the Loopback IP and the VXLAN shared-address for MLAG
```
cumulus@leaf02:mgmt:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:mgmt:~$ nv set nve vxlan mlag shared-address 10.0.1.1
```

Create NVE interface with all reqired parameters and map VLAN 100 to VNI to create the VXLAN tunnel
```
cumulus@leaf02:mgmt:~$ nv set nve vxlan enable on
cumulus@leaf02:mgmt:~$ nv set bridge domain br_default vlan 100 vni 100100
cumulus@leaf02:mgmt:~$ nv set nve vxlan source address 10.10.10.2
cumulus@leaf02:mgmt:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf02:mgmt:~$ nv config apply -y
cumulus@leaf02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf03 ">}}
Configure the Loopback IP and the VXLAN shared-address for MLAG
```
cumulus@leaf03:mgmt:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:mgmt:~$ nv set nve vxlan mlag shared-address 10.0.1.2
```

Create NVE interface with all reqired parameters and map VLAN 100 to VNI to create the VXLAN tunnel
```
cumulus@leaf03:mgmt:~$ nv set nve vxlan enable on
cumulus@leaf03:mgmt:~$ nv set bridge domain br_default vlan 100 vni 100100
cumulus@leaf03:mgmt:~$ nv set nve vxlan source address 10.10.10.3
cumulus@leaf03:mgmt:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab "leaf04 ">}}
Configure the Loopback IP and the VXLAN shared-address for MLAG
```
cumulus@leaf04:mgmt:~$ nv set interface lo ip address 10.10.10.4/32
cumulus@leaf04:mgmt:~$ nv set nve vxlan mlag shared-address 10.0.1.2
```

Create NVE interface with all reqired parameters and map VLAN 100 to VNI to create the VXLAN tunnel
```
cumulus@leaf04:mgmt:~$ nv set nve vxlan enable on
cumulus@leaf04:mgmt:~$ nv set bridge domain br_default vlan 100 vni 100100
cumulus@leaf04:mgmt:~$ nv set nve vxlan source address 10.10.10.4
cumulus@leaf04:mgmt:~$ nv set nve vxlan arp-nd-suppress on
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}

### BGP-EVPN Peerings Configuration

Configure EVPN control plane to advertise L2 information over the layer 3 fabric. Set all BGP neighbors to use `l2vpn-evpn` address-family.

{{%notice info%}}
Prior to configuring EVPN, make sure to configure the underlay fabric connectivity. Use the previous [BGP Configuration](#bgp-configuration) in the [Pure Virtualized Environment](#pure-virtualized-environment) section.
{{% /notice %}}

{{%notice note%}}
In the case of multiple VRFs, this configuration must be done for each VRF. 
{{% /notice %}}

{{< tabs "101ad3d ">}}
{{< tab "NVUE Commands ">}}
{{< tabs "10gagtg9 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv set evpn enable on
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@leaf01:mgmt:~$ nv set vrf default router neighbor peerlink.4094 address-family l2vpn-evpn enable on
cumulus@leaf01:mgmt:~$ nv set vrf default router neighbor swp51 address-family l2vpn-evpn enable on
cumulus@leaf01:mgmt:~$ nv set vrf default router neighbor swp52 address-family l2vpn-evpn enable on
cumulus@leaf01:mgmt:~$ nv config apply -y
cumulus@leaf01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv set evpn enable on
cumulus@leaf02:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@leaf02:mgmt:~$ nv set vrf default router neighbor peerlink.4094 address-family l2vpn-evpn enable on
cumulus@leaf02:mgmt:~$ nv set vrf default router neighbor swp51 address-family l2vpn-evpn enable on
cumulus@leaf02:mgmt:~$ nv set vrf default router neighbor swp52 address-family l2vpn-evpn enable on
cumulus@leaf02:mgmt:~$ nv config apply -y
cumulus@leaf02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv set evpn enable on
cumulus@leaf03:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@leaf03:mgmt:~$ nv set vrf default router neighbor peerlink.4094 address-family l2vpn-evpn enable on
cumulus@leaf03:mgmt:~$ nv set vrf default router neighbor swp51 address-family l2vpn-evpn enable on
cumulus@leaf03:mgmt:~$ nv set vrf default router neighbor swp52 address-family l2vpn-evpn enable on
cumulus@leaf03:mgmt:~$ nv config apply -y
cumulus@leaf03:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv set evpn enable on
cumulus@leaf04:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@leaf04:mgmt:~$ nv set vrf default router neighbor peerlink.4094 address-family l2vpn-evpn enable on
cumulus@leaf04:mgmt:~$ nv set vrf default router neighbor swp51 address-family l2vpn-evpn enable on
cumulus@leaf04:mgmt:~$ nv set vrf default router neighbor swp52 address-family l2vpn-evpn enable on
cumulus@leaf04:mgmt:~$ nv config apply -y
cumulus@leaf04:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " spine01 ">}}
```
cumulus@spine01:mgmt:~$ nv set evpn enable on
cumulus@spine01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine01:mgmt:~$ nv set vrf default router neighbor swp1 address-family l2vpn-evpn enable on
cumulus@spine01:mgmt:~$ nv set vrf default router neighbor swp2 address-family l2vpn-evpn enable on
cumulus@spine01:mgmt:~$ nv set vrf default router neighbor swp3 address-family l2vpn-evpn enable on
cumulus@spine01:mgmt:~$ nv set vrf default router neighbor swp4 address-family l2vpn-evpn enable on
cumulus@spine01:mgmt:~$ nv config apply -y
cumulus@spine01:mgmt:~$ nv config save
```
{{< /tab >}}
{{< tab " spine02 ">}}
```
cumulus@spine02:mgmt:~$ nv set evpn enable on
cumulus@spine02:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
cumulus@spine02:mgmt:~$ nv set vrf default router neighbor swp1 address-family l2vpn-evpn enable on
cumulus@spine02:mgmt:~$ nv set vrf default router neighbor swp2 address-family l2vpn-evpn enable on
cumulus@spine02:mgmt:~$ nv set vrf default router neighbor swp3 address-family l2vpn-evpn enable on
cumulus@spine02:mgmt:~$ nv set vrf default router neighbor swp4 address-family l2vpn-evpn enable on
cumulus@spine02:mgmt:~$ nv config apply -y
cumulus@spine02:mgmt:~$ nv config save
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "vtysh Commands ">}}
{{< tabs "20grtsd5 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 65101
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# neighbor peerlink.4094 activate
leaf01(config-router-af)# neighbor swp51 activate
leaf01(config-router-af)# neighbor swp52 activate
leaf01(config-router-af)# advertise-all-vni
leaf01(config-router-af)# end
leaf01# write memory
leaf01# exit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf03:~$ sudo vtysh
leaf02# configure terminal
leaf02(config)# router bgp 65102
leaf02(config-router)# address-family l2vpn evpn
leaf02(config-router-af)# neighbor peerlink.4094 activate
leaf02(config-router-af)# neighbor swp51 activate
leaf02(config-router-af)# neighbor swp52 activate
leaf02(config-router-af)# advertise-all-vni
leaf02(config-router-af)# end
leaf02# write memory
leaf02# exit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:~$ sudo vtysh
leaf03# configure terminal
leaf03(config)# router bgp 65103
leaf03(config-router)# address-family l2vpn evpn
leaf03(config-router-af)# neighbor peerlink.4094 activate
leaf03(config-router-af)# neighbor swp51 activate
leaf03(config-router-af)# neighbor swp52 activate
leaf03(config-router-af)# advertise-all-vni
leaf03(config-router-af)# end
leaf03# write memory
leaf03# exit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:~$ sudo vtysh
leaf04# configure terminal
leaf04(config)# router bgp 65101
leaf04(config-router)# address-family l2vpn evpn
leaf04(config-router-af)# neighbor peerlink.4094 activate
leaf04(config-router-af)# neighbor swp51 activate
leaf04(config-router-af)# neighbor swp52 activate
leaf04(config-router-af)# advertise-all-vni
leaf04(config-router-af)# end
leaf04# write memory
leaf04# exit
```
{{< /tab >}}
{{< tab " spine01 ">}}
```
cumulus@spine01:~$ sudo vtysh
spine01# configure terminal
spine01(config)# router bgp 65199
spine01(config-router)# address-family l2vpn evpn
spine01(config-router-af)# neighbor swp1 activate
spine01(config-router-af)# neighbor swp2 activate
spine01(config-router-af)# neighbor swp3 activate
spine01(config-router-af)# neighbor swp4 activate
spine01(config-router-af)# end
spine01# write memory
spine01# exit
```
{{< /tab >}}
{{< tab " spine02 ">}}
```
cumulus@spine02:~$ sudo vtysh
spine02# configure terminal
spine02(config)# router bgp 65199
spine02(config-router)# address-family l2vpn evpn
spine02(config-router-af)# neighbor swp1 activate
spine02(config-router-af)# neighbor swp2 activate
spine02(config-router-af)# neighbor swp3 activate
spine02(config-router-af)# neighbor swp4 activate
spine02(config-router-af)# end
spine02# write memory
spine02# exit
```
{{< /tab >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tabs >}}

### VXLAN VTEP IP Advertisement into BGP and VNI Into EVPN

VXLAN tunnels created using local loopback addresses and `nve vxlan mlag shared-address` must be reachable over the underlaying fabric using BGP IPv4 route advertisements.

You accomplish this by using the `redistribute connected` command described earlier in the [BGP Configuration](#bgp-configuration) section.

### VXLAN-EVPN Configuration Verification

You can verify NVE configuration using the `nv show nve` command that shows the created NVE interface, its operational state, tunnel source and mlag-shared addresses.

{{< tabs "101tr210 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv show nve
                            operational  applied     description
--------------------------  -----------  ----------  ----------------------------------------------------------------------
vxlan
  enable                    on           on          Turn the feature 'on' or 'off'.  The default is 'off'.
  arp-nd-suppress           on           on          Controls dynamic MAC learning over VXLAN tunnels based on received...
  mac-learning              off          off         Controls dynamic MAC learning over VXLAN tunnels based on received...
  mtu                       9216         9216        interface mtu
  port                      4789         4789        UDP port for VXLAN frames
  flooding
    enable                  on           on          Turn the feature 'on' or 'off'.  The default is 'off'.
    [head-end-replication]  evpn         evpn        BUM traffic is replicated and individual copies sent to remote dest...
  mlag
    shared-address          10.0.1.1     10.0.1.1    shared anycast address for MLAG peers
  source
    address                 10.10.10.1   10.10.10.1  IP addresses of this node's VTEP or 'auto'.  If 'auto', use the pri...
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv show nve
                            operational  applied     description
--------------------------  -----------  ----------  ----------------------------------------------------------------------
vxlan
  enable                    on           on          Turn the feature 'on' or 'off'.  The default is 'off'.
  arp-nd-suppress           on           on          Controls dynamic MAC learning over VXLAN tunnels based on received...
  mac-learning              off          off         Controls dynamic MAC learning over VXLAN tunnels based on received...
  mtu                       9216         9216        interface mtu
  port                      4789         4789        UDP port for VXLAN frames
  flooding
    enable                  on           on          Turn the feature 'on' or 'off'.  The default is 'off'.
    [head-end-replication]  evpn         evpn        BUM traffic is replicated and individual copies sent to remote dest...
  mlag
    shared-address          10.0.1.1     10.0.1.1    shared anycast address for MLAG peers
  source
    address                 10.10.10.2   10.10.10.2  IP addresses of this node's VTEP or 'auto'.  If 'auto', use the pri...
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv show nve
                            operational  applied     description
--------------------------  -----------  ----------  ----------------------------------------------------------------------
vxlan
  enable                    on           on          Turn the feature 'on' or 'off'.  The default is 'off'.
  arp-nd-suppress           on           on          Controls dynamic MAC learning over VXLAN tunnels based on received...
  mac-learning              off          off         Controls dynamic MAC learning over VXLAN tunnels based on received...
  mtu                       9216         9216        interface mtu
  port                      4789         4789        UDP port for VXLAN frames
  flooding
    enable                  on           on          Turn the feature 'on' or 'off'.  The default is 'off'.
    [head-end-replication]  evpn         evpn        BUM traffic is replicated and individual copies sent to remote dest...
  mlag
    shared-address          10.0.1.2     10.0.1.2    shared anycast address for MLAG peers
  source
    address                 10.10.10.3   10.10.10.3  IP addresses of this node's VTEP or 'auto'.  If 'auto', use the pri...
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv show nve
                            operational  applied     description
--------------------------  -----------  ----------  ----------------------------------------------------------------------
vxlan
  enable                    on           on          Turn the feature 'on' or 'off'.  The default is 'off'.
  arp-nd-suppress           on           on          Controls dynamic MAC learning over VXLAN tunnels based on received...
  mac-learning              off          off         Controls dynamic MAC learning over VXLAN tunnels based on received...
  mtu                       9216         9216        interface mtu
  port                      4789         4789        UDP port for VXLAN frames
  flooding
    enable                  on           on          Turn the feature 'on' or 'off'.  The default is 'off'.
    [head-end-replication]  evpn         evpn        BUM traffic is replicated and individual copies sent to remote dest...
  mlag
    shared-address          10.0.1.2     10.0.1.2    shared anycast address for MLAG peers
  source
    address                 10.10.10.4   10.10.10.4  IP addresses of this node's VTEP or 'auto'.  If 'auto', use the pri...
```
{{< /tab >}}
{{< /tabs >}}

### MLAG and VXLAN Interfaces Configuration Verification

When NVE interface set with mlag-shared address, it is active-active on both MLAG peers. You can view it alongside the other MLAG bonds by running `net show clag`.

{{< tabs "10aqtr210 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 1000 44:38:39:00:00:59 primary
    Peer Priority, ID, and Role: 2000 44:38:39:00:00:5a secondary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:5a (linklocal)
               VxLAN Anycast IP: 10.0.1.1
                      Backup IP: 192.168.200.12 vrf mgmt (active)
                     System MAC: 44:38:39:ff:00:01

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
          esxi01   esxi01             1         -                      -
         vxlan48   vxlan48            -         -                      -
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 2000 44:38:39:00:00:5a secondary
    Peer Priority, ID, and Role: 1000 44:38:39:00:00:59 primary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:59 (linklocal)
               VxLAN Anycast IP: 10.0.1.1
                      Backup IP: 192.168.200.11 vrf mgmt (active)
                     System MAC: 44:38:39:ff:00:01

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
          esxi01   esxi01             1         -                      -
         vxlan48   vxlan48            -         -                      -
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 1000 44:38:39:00:00:5d primary
    Peer Priority, ID, and Role: 2000 44:38:39:00:00:5e secondary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:5e (linklocal)
               VxLAN Anycast IP: 10.0.1.2
                      Backup IP: 192.168.200.14 vrf mgmt (active)
                     System MAC: 44:38:39:ff:00:02

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
          esxi03   esxi03             1         -                      -
         vxlan48   vxlan48            -         -                      -
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show clag
The peer is alive
     Our Priority, ID, and Role: 2000 44:38:39:00:00:5e secondary
    Peer Priority, ID, and Role: 1000 44:38:39:00:00:5d primary
          Peer Interface and IP: peerlink.4094 fe80::4638:39ff:fe00:5d (linklocal)
               VxLAN Anycast IP: 10.0.1.2
                      Backup IP: 192.168.200.13 vrf mgmt (active)
                     System MAC: 44:38:39:ff:00:02

CLAG Interfaces
Our Interface      Peer Interface     CLAG Id   Conflicts              Proto-Down Reason
----------------   ----------------   -------   --------------------   -----------------
          esxi03   esxi03             1         -                      -
         vxlan48   vxlan48            -         -                      -
```
{{< /tab >}}
{{< /tabs >}}


### BGP-EVPN Peerings and VTEP Addresses Advertisement Verification

BGP-EVPN peering verification is similar to IPv4 verification. Each "address-family" lists the neighbors configured and their peer states. Use `net show bgp summary` command in NVUE, or `show ip bgp summary` in `vtysh` to view the BGP peering table.

{{< tabs "TABI556D1431 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.1, local AS number 4259632651 vrf-id 0
BGP table version 96
RIB entries 11, using 2112 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf02(peerlink.4094) 4 4259632649     28055     28052        0    0    0 00:51:58            5        6
spine01(swp51)        4 4200000000     28066     28058        0    0    0 00:49:27            4        6
spine02(swp52)        4 4200000000     28070     28061        0    0    0 00:48:50            4        6

Total number of neighbors 3

show bgp l2vpn evpn summary
===========================
BGP router identifier 10.10.10.1, local AS number 4259632651 vrf-id 0
BGP table version 0
RIB entries 7, using 1344 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf02(peerlink.4094) 4 4259632649     28055     28052        0    0    0 00:51:58            2        3
spine01(swp51)        4 4200000000     28067     28059        0    0    0 00:49:27            2        3
spine02(swp52)        4 4200000000     28070     28061        0    0    0 00:48:50            2        3

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.2, local AS number 4259632649 vrf-id 0
BGP table version 89
RIB entries 11, using 2112 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(peerlink.4094) 4 4259632651     28032     28045        0    0    0 00:51:23            5        6
spine01(swp51)        4 4200000000     28044     28044        0    0    0 00:48:53            5        6
spine02(swp52)        4 4200000000     28064     28050        0    0    0 00:48:16            5        6

Total number of neighbors 3

show bgp l2vpn evpn summary
===========================
BGP router identifier 10.10.10.2, local AS number 4259632649 vrf-id 0
BGP table version 0
RIB entries 7, using 1344 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(peerlink.4094) 4 4259632651     28032     28045        0    0    0 00:51:24            2        3
spine01(swp51)        4 4200000000     28044     28044        0    0    0 00:48:54            2        3
spine02(swp52)        4 4200000000     28064     28050        0    0    0 00:48:17            2        3

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.3, local AS number 4259632661 vrf-id 0
BGP table version 85
RIB entries 11, using 2112 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf04(peerlink.4094) 4 4259632667     53298     53295        0    0    0 00:48:56            5        6
spine01(swp51)        4 4200000000     53309     53327        0    0    0 00:47:12            4        6
spine02(swp52)        4 4200000000     53317     53320        0    0    0 00:46:34            4        6

Total number of neighbors 3

show bgp l2vpn evpn summary
===========================
BGP router identifier 10.10.10.3, local AS number 4259632661 vrf-id 0
BGP table version 0
RIB entries 7, using 1344 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf04(peerlink.4094) 4 4259632667     53298     53295        0    0    0 00:48:57            2        3
spine01(swp51)        4 4200000000     53309     53327        0    0    0 00:47:13            2        3
spine02(swp52)        4 4200000000     53317     53320        0    0    0 00:46:35            2        3

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.4, local AS number 4259632667 vrf-id 0
BGP table version 74
RIB entries 11, using 2112 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf03(peerlink.4094) 4 4259632661     27978     27990        0    0    0 00:48:07            5        6
spine01(swp51)        4 4200000000     27997     27994        0    0    0 00:46:23            5        6
spine02(swp52)        4 4200000000     28009     27995        0    0    0 00:45:45            5        6

Total number of neighbors 3

show bgp l2vpn evpn summary
===========================
BGP router identifier 10.10.10.4, local AS number 4259632667 vrf-id 0
BGP table version 0
RIB entries 7, using 1344 bytes of memory
Peers 3, using 64 KiB of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf03(peerlink.4094) 4 4259632661     27978     27990        0    0    0 00:48:07            2        3
spine01(swp51)        4 4200000000     27997     27994        0    0    0 00:46:23            2        3
spine02(swp52)        4 4200000000     28010     27996        0    0    0 00:45:45            2        3

Total number of neighbors 3
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
cumulus@spine01:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.101, local AS number 4200000000 vrf-id 0
BGP table version 165
RIB entries 11, using 2112 bytes of memory
Peers 4, using 85 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(swp1)    4 4259632651     88151     88190        0    0    0 00:49:55            3        6
leaf02(swp2)    4 4259632649     88154     88213        0    0    0 00:49:55            3        6
leaf03(swp3)    4 4259632661     88206     88256        0    0    0 00:49:55            3        6
leaf04(swp4)    4 4259632667     88207     88266        0    0    0 00:49:55            3        6

Total number of neighbors 4

show bgp l2vpn evpn summary
===========================
BGP router identifier 10.10.10.101, local AS number 4200000000 vrf-id 0
BGP table version 0
RIB entries 7, using 1344 bytes of memory
Peers 4, using 85 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(swp1)    4 4259632651     88151     88190        0    0    0 00:49:55            1        4
leaf02(swp2)    4 4259632649     88154     88213        0    0    0 00:49:55            1        4
leaf03(swp3)    4 4259632661     88206     88256        0    0    0 00:49:55            1        4
leaf04(swp4)    4 4259632667     88207     88266        0    0    0 00:49:55            1        4

Total number of neighbors 4
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
cumulus@spine02:mgmt:~$ net show bgp summary
show bgp ipv4 unicast summary
=============================
BGP router identifier 10.10.10.102, local AS number 4200000000 vrf-id 0
BGP table version 112
RIB entries 11, using 2112 bytes of memory
Peers 4, using 85 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(swp1)    4 4259632651     73653     73680        0    0    0 00:49:41            3        6
leaf02(swp2)    4 4259632649     73654     73696        0    0    0 00:49:41            3        6
leaf03(swp3)    4 4259632661     73712     73776        0    0    0 00:49:41            3        6
leaf04(swp4)    4 4259632667     73717     73771        0    0    0 00:49:40            3        6

Total number of neighbors 4

show bgp l2vpn evpn summary
===========================
BGP router identifier 10.10.10.102, local AS number 4200000000 vrf-id 0
BGP table version 0
RIB entries 7, using 1344 bytes of memory
Peers 4, using 85 KiB of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt
leaf01(swp1)    4 4259632651     73653     73680        0    0    0 00:49:42            1        4
leaf02(swp2)    4 4259632649     73654     73696        0    0    0 00:49:42            1        4
leaf03(swp3)    4 4259632661     73712     73776        0    0    0 00:49:42            1        4
leaf04(swp4)    4 4259632667     73717     73771        0    0    0 00:49:41            1        4

Total number of neighbors 4
```
{{< /tab >}}
{{< /tabs >}}

All all loopback and VXLAN anycast IP prefixes should appear in the routing table of each switch. Use `net show route` command in NVUE (`route -n` in Linux) or `show ip route` in `vtysh` to check the routing table.

{{< tabs "TAB22sIGTD1631 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
C>* 10.10.10.1/32 is directly connected, lo, 02:12:49
B>* 10.10.10.2/32 [20/0] via fe80::4638:39ff:fe00:5a, peerlink.4094, weight 1, 01:09:21
B>* 10.10.10.3/32 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 01:06:14
  *                      via fe80::4638:39ff:fe00:3, swp52, weight 1, 01:06:14
B>* 10.10.10.4/32 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 01:06:13
  *                      via fe80::4638:39ff:fe00:3, swp52, weight 1, 01:06:13
C>* 10.0.1.1/32 is directly connected, lo, 02:12:49
B>* 10.0.1.2/32 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 01:06:14
  *                    via fe80::4638:39ff:fe00:3, swp52, weight 1, 01:06:14
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.10.10.1/32 [20/0] via fe80::4638:39ff:fe00:59, peerlink.4094, weight 1, 01:08:59
C>* 10.10.10.2/32 is directly connected, lo, 01:42:41
B>* 10.10.10.3/32 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 01:05:51
  *                      via fe80::4638:39ff:fe00:b, swp52, weight 1, 01:05:51
B>* 10.10.10.4/32 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 01:05:50
  *                      via fe80::4638:39ff:fe00:b, swp52, weight 1, 01:05:50
C>* 10.0.1.1/32 is directly connected, lo, 01:41:37
B>* 10.0.1.2/32 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 01:05:51
  *                    via fe80::4638:39ff:fe00:b, swp52, weight 1, 01:05:51
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.10.10.1/32 [20/0] via fe80::4638:39ff:fe00:11, swp51, weight 1, 01:04:41
  *                      via fe80::4638:39ff:fe00:13, swp52, weight 1, 01:04:41
B>* 10.10.10.2/32 [20/0] via fe80::4638:39ff:fe00:11, swp51, weight 1, 01:04:41
  *                      via fe80::4638:39ff:fe00:13, swp52, weight 1, 01:04:41
C>* 10.10.10.3/32 is directly connected, lo, 02:03:38
B>* 10.10.10.4/32 [20/0] via fe80::4638:39ff:fe00:5e, peerlink.4094, weight 1, 01:07:02
B>* 10.0.1.1/32 [20/0] via fe80::4638:39ff:fe00:11, swp51, weight 1, 01:04:41
  *                    via fe80::4638:39ff:fe00:13, swp52, weight 1, 01:04:41
C>* 10.0.1.2/32 is directly connected, lo, 02:03:38
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.10.10.1/32 [20/0] via fe80::4638:39ff:fe00:19, swp51, weight 1, 00:54:36
  *                      via fe80::4638:39ff:fe00:1b, swp52, weight 1, 00:54:36
B>* 10.10.10.2/32 [20/0] via fe80::4638:39ff:fe00:19, swp51, weight 1, 00:54:36
  *                      via fe80::4638:39ff:fe00:1b, swp52, weight 1, 00:54:36
B>* 10.10.10.3/32 [20/0] via fe80::4638:39ff:fe00:5d, peerlink.4094, weight 1, 00:56:57
C>* 10.10.10.4/32 is directly connected, lo, 01:53:17
B>* 10.0.1.1/32 [20/0] via fe80::4638:39ff:fe00:19, swp51, weight 1, 00:54:36
  *                    via fe80::4638:39ff:fe00:1b, swp52, weight 1, 00:54:36
C>* 10.0.1.2/32 is directly connected, lo, 01:40:22
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
cumulus@spine02:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.10.10.1/32 [20/0] via fe80::4638:39ff:fe00:4, swp1, weight 1, 00:50:51
B>* 10.10.10.2/32 [20/0] via fe80::4638:39ff:fe00:c, swp2, weight 1, 00:50:51
B>* 10.10.10.3/32 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:50:51
B>* 10.10.10.4/32 [20/0] via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:50:50
B>* 10.0.1.1/32 [20/0] via fe80::4638:39ff:fe00:4, swp1, weight 1, 00:50:51
  *                    via fe80::4638:39ff:fe00:c, swp2, weight 1, 00:50:51
B>* 10.0.1.2/32 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:50:50
  *                    via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:50:50
```
{{< /tab >}}
{{< tab "spine02 ">}}
Spine02 has two ECMP routes to each of the anycast-IPs and a single route to each loopback
```
cumulus@spine02:mgmt:~$ net show route
show ip route
=============
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued, r - rejected, b - backup
       t - trapped, o - offload failure
B>* 10.10.10.1/32 [20/0] via fe80::4638:39ff:fe00:4, swp1, weight 1, 00:53:58
B>* 10.10.10.2/32 [20/0] via fe80::4638:39ff:fe00:c, swp2, weight 1, 00:53:58
B>* 10.10.10.3/32 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:53:58
B>* 10.10.10.4/32 [20/0] via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:53:57
B>* 10.0.1.1/32 [20/0] via fe80::4638:39ff:fe00:4, swp1, weight 1, 00:53:58
  *                    via fe80::4638:39ff:fe00:c, swp2, weight 1, 00:53:58
B>* 10.0.1.2/32 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:53:57
  *                    via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:53:57
```
{{< /tab >}}
{{< /tabs >}}

### MAC Addresses Population by EVPN Control Plane

The EVPN control-plane advertises host MAC address, host IPs and associated VTEP endpoints. You can view the MAC addresses intalled into the local MAC table using the `nv show bridge domain br_default mac-table` command. 

{{%notice note%}}

To check out all EVPN learned information, use the `net show bgp evpn route` command.

{{%/notice %}}

{{< tabs "TGTT123 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ nv show bridge domain br_default mac-table 
      age   bridge-domain  entry-type  interface   last-update  mac                src-vni  vlan  vni   Summary
----  ----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  --------------------
+ 0   1917  br_default     static      peerlink    76           48:b0:2d:4f:19:a9           100
+ 1   1931  br_default     permanent   peerlink    1931         48:b0:2d:cf:2b:02
+ 2   76    br_default                 esxi01      1776         48:b0:2d:c7:ee:11           100
+ 3   17    br_default                 esxi01      1815         4a:b0:2d:c7:ee:11           1
+ 4   7     br_default                 esxi01      1914         4a:b0:2d:cc:76:e2           1
+ 5   1931  br_default     permanent   esxi01      1931         48:b0:2d:7a:24:3f           1
+ 6   1869  br_default                 vxlan48     1776         48:b0:2d:54:9e:04           100   None  remote-dst: 10.0.1.2
+ 7   1810  br_default                 vxlan48     1810         48:b0:2d:fa:2c:e7           100   None  remote-dst: 10.0.1.2
+ 8   1909  br_default                 vxlan48     1909         48:b0:2d:1d:86:92           100   None  remote-dst: 10.0.1.2
+ 9   1931  br_default     permanent   vxlan48     1931         16:52:da:47:60:83           1     None
+ 10  1909                 permanent   vxlan48     759          00:00:00:00:00:00  100100         None  remote-dst: 10.0.1.2
+ 11                       permanent   br_default               00:00:00:00:01:00
+ 12  1931  br_default     permanent   br_default  1931         48:b0:2d:d9:76:5f           100
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ nv show bridge domain br_default mac-table 
      age   bridge-domain  entry-type  interface   last-update  mac                src-vni  vlan  vni   Summary
----  ----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  --------------------
+ 0   1941  br_default     static      peerlink    118          48:b0:2d:d9:76:5f           100
+ 1   1952  br_default     permanent   peerlink    1952         48:b0:2d:d6:f2:59
+ 2   118   br_default                 esxi01      1806         48:b0:2d:c7:ee:11           100
+ 3   3     br_default                 esxi01      1840         4a:b0:2d:c7:ee:11           1
+ 4   39    br_default                 esxi01      1939         4a:b0:2d:cc:76:e2           1
+ 5   1952  br_default     permanent   esxi01      1952         48:b0:2d:5e:3b:e0           1
+ 6   1894  br_default                 vxlan48     1806         48:b0:2d:54:9e:04           100   None  remote-dst: 10.0.1.2
+ 7   1835  br_default                 vxlan48     1835         48:b0:2d:fa:2c:e7           100   None  remote-dst: 10.0.1.2
+ 8   1934  br_default                 vxlan48     1934         48:b0:2d:1d:86:92           100   None  remote-dst: 10.0.1.2
+ 9   1952  br_default     permanent   vxlan48     1952         7e:d0:78:12:12:d4                 None
+ 10  1934                 permanent   vxlan48     1934         00:00:00:00:00:00  100100         None  remote-dst: 10.0.1.2
+ 11                       permanent   br_default               00:00:00:00:01:00
+ 12  1952  br_default     permanent   br_default  1952         48:b0:2d:4f:19:a9           100
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ nv show bridge domain br_default mac-table 
      age   bridge-domain  entry-type  interface   last-update  mac                src-vni  vlan  vni   Summary
----  ----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  --------------------
+ 0   1999  br_default     static      peerlink    197          48:b0:2d:1d:86:92           100
+ 1   2032  br_default     permanent   peerlink    2032         48:b0:2d:60:25:13           1
+ 2   1869  br_default                 vxlan48     1864         48:b0:2d:c7:ee:11           100   None  remote-dst: 10.0.1.1
+ 3   1907  br_default                 vxlan48     1907         48:b0:2d:d9:76:5f           100   None  remote-dst: 10.0.1.1
+ 4   1998  br_default                 vxlan48     1998         48:b0:2d:4f:19:a9           100   None  remote-dst: 10.0.1.1
+ 5   2032  br_default     permanent   vxlan48     2032         5a:98:f1:44:32:66                 None
+ 6   1998                 permanent   vxlan48     1958         00:00:00:00:00:00  100100         None  remote-dst: 10.0.1.1
+ 7   174   br_default                 esxi01      1892         48:b0:2d:54:9e:04           1
+ 8   118   br_default                 esxi01      1896         4a:b0:2d:54:9e:04           1
+ 9   0     br_default                 esxi01      1994         4a:b0:2d:8e:62:83           1
+ 10  2032  br_default     permanent   esxi01      2032         48:b0:2d:a9:72:5d           1
+ 11                       permanent   br_default               00:00:00:00:01:00
+ 12  2031  br_default     permanent   br_default  2031         48:b0:2d:fa:2c:e7           100
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ nv show bridge domain br_default mac-table 
      age   bridge-domain  entry-type  interface   last-update  mac                src-vni  vlan  vni   Summary
----  ----  -------------  ----------  ----------  -----------  -----------------  -------  ----  ----  --------------------
+ 0   2033  br_default     static      peerlink    2033         48:b0:2d:fa:2c:e7           100
+ 1   2044  br_default     permanent   peerlink    2044         48:b0:2d:5b:60:e6           1
+ 2   1904  br_default                 vxlan48     1904         48:b0:2d:c7:ee:11           100   None  remote-dst: 10.0.1.1
+ 3   1942  br_default                 vxlan48     1942         48:b0:2d:d9:76:5f           100   None  remote-dst: 10.0.1.1
+ 4   2034  br_default                 vxlan48     2034         48:b0:2d:4f:19:a9           100   None  remote-dst: 10.0.1.1
+ 5   2044  br_default     permanent   vxlan48     2044         ca:3b:a6:3d:ab:0c                 None
+ 6   2034                 permanent   vxlan48     1108         00:00:00:00:00:00  100100         None  remote-dst: 10.0.1.1
+ 7   207   br_default                 esxi01      1927         48:b0:2d:54:9e:04           1
+ 8   5     br_default                 esxi01      1931         4a:b0:2d:54:9e:04           1
+ 9   130   br_default                 esxi01      2029         4a:b0:2d:8e:62:83           1
+ 10  2044  br_default     permanent   esxi01      2044         48:b0:2d:ce:39:9f           1
+ 11                       permanent   br_default               00:00:00:01:00:00
+ 12  2044  br_default     permanent   br_default  2044         48:b0:2d:1d:86:92           100
```
{{< /tab >}}
{{< /tabs >}}

### Traffic Flow

{{<figure src="images/guides/cumulus-nsxt/T1_vxlan.jpg">}}

The NSX traffic will be unchanged from the scenarios described earlier. Reference the [Layer 2](#layer-2-virtualized-traffic) or [Layer 3](#layer-3-virtualized-traffic) virtulized traffic examples for details. Traffic destined outside of the NSX fabric will follow the same traffic flow as described in the [Virtualized and Bare Metal](#virtualized-and-bare-metal-server-environment) section.

With VXLAN in the network fabric, Geneve traffic from ESXi TEP is encapsulated again into VXLAN packets on the leaf switch using the local loopback IP addresses as the tunnel sources and the remote VXLAN anycast IP as the destination.  
When the remote leaf receives the VXLAN packet, it is decapsulated and fowared to the correct ESXi (same VNI) host where the Geneve packet is decapsulated and forwared to the correct local VM.

# Virtualized Environment Over EVPN Fabric with an External Network (EVPN Type-5 Routes)

{{<figure src="images/guides/cumulus-nsxt/edge_type5.jpg">}}

There are cases when virtualized traffic is destined for external networks (as we saw in the BM scenario) but outside the EVPN domain. NSX Edge can act as VXLAN-VTEP with a BGP-EVPN control-plane to answer that need. By that, it receives EVPN Type-5 external routes, which are used for external traffic routing in EVPN fabrics. 

{{%notice note%}}

This guide does not cover the configuration commands for this scenario. Check out previous sections and the [Prefix-based Routing](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-52/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/#prefix-based-routing) documentation to learn how to handle EVPN Type-5 routes.

{{%/notice %}}

{{%notice note%}}

In these cases, you will probably use VRFs. Check out [Virtual Routing and Forwarding - VRF](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-52/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF/) documentation and its [BGP](https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-52/Layer-3/VRFs/Virtual-Routing-and-Forwarding-VRF/#bgp) section for more information and configuration examples.

{{%/notice %}}

Edge VM establishes IPv4 BGP peerings with its ToR switches. On top of that, EVPN address-family peerings are set, and the EVPN control-plane is built. 

In the above diagram, Edge VM is located on the ESXi03 hypervisor. It establishes BGP-EVPN peerings with his local leaf03 and leaf04 switches. Those leaf switches, which are called "Border Leafs" (EVPN fabric gateway to external networks), are part of the underlay EVPN fabric and have an EVPN type-5 route to the external server. This route is then populated also to the Edge VM.

Edge VM also acts as VXLAN-VTEP, and for that, it uses its loopback interface (which also must be advertised into BGP) as a VXLAN tunnel source. By that, it acts the same as the physical switches in the VXLAN-EVPN environment.

### Traffic Flow

Traffic flow from VM1 on ESXi01 to Edge is like the regular virtualized environment over EVPN fabric [Traffic Flow](#traffic-flow-2). 

In the current case of traffic sent to an external server, which is the traffic destination, the difference is in the Edge actions afterward. Instead of decapsulating the Geneve header received from the other TEP and sending regular IP traffic to the underlay fabric, it encapsulates the traffic into the VXLAN packet. Then, the packet is sent to its destination VTEP, which is determined by the next-hop of the EVPN type-5 route. In our diagram, the packet's destination VTEP is the local ToR switches, which will decapsulate the VXLAN header and send it out of the EVPN domain as a regular IP packet.
