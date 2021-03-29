---
title: NVIDIA Cumulus Linux Configuration Guide for NSX-T Deployments
author: NVIDIA Networking
product: NVIDIA Networking Guides
---

VMware NSX-T provides an agile software-defined infrastructure to build cloud-native application environments. It aims to provide automation, simplicity in operations, networking, and security.
NSX-T supports various type of environments like multi-hypervisor, bare-metal workloads, hybrid/public clouds and more. It serves as the control-plane, data-plane, and management-plane for virtualized overlay solutions.

VMware virtualized environment requires all virtual and physical elements such as ESXi hypervisors and NSX Edges to communicate to each other over an underlay IP fabric. NVIDIA Spectrum switches provides best-in-class underlay hardware leveraging the Spectrum ASIC providing speeds of 1 to 400Gbps. With NVIDIA Cumulus Linux OS software, the underlying fabric configuration can be easily provisioned to ensure VMware NSX-T proper operations.

This configuration guide examines a few of the most common use-cases of VMware NSX-T deployments and shows the required underlay switches configurations of Cumulus Linux.  
In the following scenarios, the underlay IP fabric configured with [Multi-Chassis Link Aggregation - MLAG](https://docs.cumulusnetworks.com/cumulus-linux/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/) for active/active physical layer 2 connectivity, [Virtual Router Redundancy - VRR and VRRP](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP/) for active/active and redundant layer 3 gateways, and [Border Gateway Protocol - BGP](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP/) to provide underlay IP fabric connectivity between all physical and logical elements. Our best-practice is using [eBGP](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP/#ebgp-and-ibgp) for all Leaf-Spine underlay peerings.

{{%notice note%}}

NSX-T configuration will not be covered in this guide, for more information regarding VMware NSX-T design, installation and configuration check - [VMware NSX-T Reference Design](https://communities.vmware.com/t5/VMware-NSX-Documents/VMware-NSX-T-Reference-Design/ta-p/2778093), [NSX-T Data Center Installation Guide](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/installation/GUID-3E0C4CEC-D593-4395-84C4-150CD6285963.html), and [NSX-T Data Center Administration Guide](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/administration/GUID-FBFD577B-745C-4658-B713-A3016D18CB9A.html).

{{%/notice %}}

# Pure Virtualized Environment

This use-case covers the basic VMware environment where it’s all virtualized and based on pure IP fabric underlay, like a greenfield environment. It means all the communication is between Virtual Machines (VMs) located on ESXi hypervisors.

NSX-T uses Generic Networking Virtualization Encapsulation (Geneve) as the overlay protocol to transmit virtualized traffic over layer 2 tunnels on top of the layer 3 underlay fabric. The Geneve protocol is like the well-known VXLAN encapsulation, but it has an extended header with more options. Each NSX-T "prepared host" (ESXi added to NSX-T manager) is installed with kernel modules to act as a Tunnel Endpoint (TEP) device. TEP devices are responsible for encapsulating and decapsulating traffic between virtual machines inside the virtualized network.

The below underlay IP fabric configuration based on this example topology diagram and physical connectivity

{{<figure src="/images/guides/cumulus-nsxt/pure_L2.JPG">}}

**Rack 1** – Two NVIDIA Switches in MLAG + One ESXi hypervisor connected in active/active bonding  
**Rack 2** – Two NVIDIA Switches in MLAG + One ESXi hypervisor connected in active/active bonding

## Physical Connectivity

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

## MTU Configuration

The VMware recommendation is to configure Jumbo MTU (9000) on all virtual and physical network elements end-to-end. On VMkernel ports, Virtual switches (VDS), VDS Port-Groups, N-VDS and the underlay physical network. Geneve encapsulation, requires a minimum MTU of `1600B` (`1700B` is required for extended options). It is recommended to use 9000-byte MTU for the entire network path. This improves the throughput of storage, vSAN, vMotion, NFS and vSphere Replication.

Using the below commands, you can examine switches' physical interfaces MTU settings. By default, all interfaces on Cumulus Linux have MTU 9216 configured.

{{< tabs "4tt16 ">}}

{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show interface
State  Name   Spd  MTU    Mode      LLDP                          Summary
-----  -----  ---  -----  --------  ----------------------------  ---------------------------
UP     lo     N/A  65536  Loopback                                IP: 127.0.0.1/8
       lo                                                         IP: ::1/128
UP     eth0   1G   1500   Mgmt      oob-mgmt-switch (swp10)       Master: mgmt(UP)
       eth0                                                       IP: 192.168.200.11/24(DHCP)
UP     swp1   1G   9216   Default   esxi01 (44:38:39:00:00:32)
UP     swp49  1G   9216   Default   leaf02 (swp49)
UP     swp50  1G   9216   Default   leaf02 (swp50)
UP     swp51  1G   9216   Default   spine01 (swp1)
UP     swp52  1G   9216   Default   spine02 (swp1)
UP     mgmt   N/A  65536  VRF                                     IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show interface
State  Name   Spd  MTU    Mode      LLDP                          Summary
-----  -----  ---  -----  --------  ----------------------------  ---------------------------
UP     lo     N/A  65536  Loopback                                IP: 127.0.0.1/8
       lo                                                         IP: ::1/128
UP     eth0   1G   1500   Mgmt      oob-mgmt-switch (swp11)       Master: mgmt(UP)
       eth0                                                       IP: 192.168.200.12/24(DHCP)
UP     swp1   1G   9216   Default   esxi01 (44:38:39:00:00:38)
UP     swp49  1G   9216   Default   leaf01 (swp49)
UP     swp50  1G   9216   Default   leaf01 (swp50)
UP     swp51  1G   9216   Default   spine01 (swp2)
UP     swp52  1G   9216   Default   spine02 (swp2)
UP     mgmt   N/A  65536  VRF                                     IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show interface
State  Name   Spd  MTU    Mode      LLDP                          Summary
-----  -----  ---  -----  --------  ----------------------------  ---------------------------
UP     lo     N/A  65536  Loopback                                IP: 127.0.0.1/8
       lo                                                         IP: ::1/128
UP     eth0   1G   1500   Mgmt      oob-mgmt-switch (swp12)       Master: mgmt(UP)
       eth0                                                       IP: 192.168.200.13/24(DHCP)
UP     swp1   1G   9216   Default   esxi03 (44:38:39:00:00:3e)
UP     swp49  1G   9216   Default   leaf04 (swp49)
UP     swp50  1G   9216   Default   leaf04 (swp50)
UP     swp51  1G   9216   Default   spine01 (swp3)
UP     swp52  1G   9216   Default   spine02 (swp3)
UP     mgmt   N/A  65536  VRF                                     IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show interface
State  Name   Spd  MTU    Mode      LLDP                          Summary
-----  -----  ---  -----  --------  ----------------------------  ---------------------------
UP     lo     N/A  65536  Loopback                                IP: 127.0.0.1/8
       lo                                                         IP: ::1/128
UP     eth0   1G   1500   Mgmt      oob-mgmt-switch (swp13)       Master: mgmt(UP)
       eth0                                                       IP: 192.168.200.14/24(DHCP)
UP     swp1   1G   9216   Default   esxi03 (44:38:39:00:00:44)
UP     swp49  1G   9216   Default   leaf03 (swp49)
UP     swp50  1G   9216   Default   leaf03 (swp50)
UP     swp51  1G   9216   Default   spine01 (swp4)
UP     swp52  1G   9216   Default   spine02 (swp4)
UP     mgmt   N/A  65536  VRF                                     IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
cumulus@spine01:mgmt:~$ net show interface
State  Name  Spd  MTU    Mode      LLDP                     Summary
-----  ----  ---  -----  --------  -----------------------  ---------------------------
UP     lo    N/A  65536  Loopback                           IP: 127.0.0.1/8
       lo                                                   IP: ::1/128
UP     eth0  1G   1500   Mgmt      oob-mgmt-switch (swp14)  Master: mgmt(UP)
       eth0                                                 IP: 192.168.200.21/24(DHCP)
UP     swp1  1G   9216   Default   leaf01 (swp51)
UP     swp2  1G   9216   Default   leaf02 (swp51)
UP     swp3  1G   9216   Default   leaf03 (swp51)
UP     swp4  1G   9216   Default   leaf04 (swp51)
UP     mgmt  N/A  65536  VRF                                IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
cumulus@spine02:mgmt:~$ net show interface
State  Name  Spd  MTU    Mode      LLDP                     Summary
-----  ----  ---  -----  --------  -----------------------  ---------------------------
UP     lo    N/A  65536  Loopback                           IP: 127.0.0.1/8
       lo                                                   IP: ::1/128
UP     eth0  1G   1500   Mgmt      oob-mgmt-switch (swp15)  Master: mgmt(UP)
       eth0                                                 IP: 192.168.200.22/24(DHCP)
UP     swp1  1G   9216   Default   leaf01 (swp52)
UP     swp2  1G   9216   Default   leaf02 (swp52)
UP     swp3  1G   9216   Default   leaf03 (swp52)
UP     swp4  1G   9216   Default   leaf04 (swp52)
UP     mgmt  N/A  65536  VRF                                IP: 127.0.0.1/8
```
{{< /tab >}}
{{< /tabs >}}

To manually define the MTU use the `net add interface` command.
```
cumulus@switch:~$ net add interface swp1 mtu 9216
```

To restore the MTU to the default value of 9216 use `net del interface mtu`.
```
cumulus@switch:~$ net del interface swp1 mtu
```

## MLAG and VRR Configuration

In the example topology, VMs are located on two different physical ESXi hypervisors, and share the same application. They are in the same IP subnet and connected to the same VMware Logical Switch or Segment (like a VLAN in a physical network). But, as they are divided by a layer 3 underlay network, we must ensure the Geneve layer 2 overlay traffic to pass over it.

The ESXi hypervisors connected using active/active LAG to the leaf switches for redundancy and additional throughput. For that, we create active/active, redundant layer 2 and layer 3 connectivity using MLAG protocol with VRR on top. The below Cumulus Linux switches configuration demonstrates how to configure MLAG and VRR.  
Make sure to set MLAG+VRR regardless the N-VDS uplink profile (active/active or active/standby), unless of course, only one ToR (leaf) or a single link is used to connect the hypervisor.

### MLAG General Configuration

Cumulus Linux MLAG configuration is done by a single command. It automatically creates the peer link bond and configures all MLAG related configuration.

{{< tabs "TABtgbID123013 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:01 interface swp49-50 primary backup-ip 192.168.200.12 vrf mgmt
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:01 interface swp49-50 secondary backup-ip 192.168.200.11 vrf mgmt
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:02 interface swp49-50 primary backup-ip 192.168.200.14 vrf mgmt
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:02 interface swp49-50 secondary backup-ip 192.168.200.13 vrf mgmt
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

### MLAG Interfaces Configuration - Active/Active LACP LAG N-VDS Uplink Profile

If the recommended active/active LAG (LACP) N-VDS uplink profile is used, switch downlink interfaces for ESXi must be bonded into MLAG ports (LACP bonds).  
This action also automatically adds the MLAG interfaces into the bridge and sets them as trunk ports (VLAN tagging) with all VLANs allowed.

{{%notice note%}}

For active/standby environments, do not configure MLAG. Follow the instructions under the [Switch Ports Configuration - Non-LAG N-VDS Uplink Profile](#esxi-downlink-ports-configuration---activestandby-n-vds-uplink) section.  
Do not use active/active LACP LAG uplink profile for the Overlay Transport Zone on N-VDS.

{{%/notice %}}

{{< tabs "TABID0213 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add clag port bond esxi01 interface swp1 clag-id 1
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add clag port bond esxi01 interface swp1 clag-id 1
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add clag port bond esxi03 interface swp1 clag-id 1
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add clag port bond esxi03 interface swp1 clag-id 1
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

For information on how to assign VLANs to trunk ports reference the [VLAN Tagging](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-2/Ethernet-Bridging-VLANs/VLAN-Tagging/) page for more information and commands.

### Switch Ports Configuration - Non-LAG N-VDS Uplink Profile

If active/standby or active/active, non-LAG N-VDS uplink profiles used, the switch downlink interfaces for ESXi must be left as regular ports and not use any MLAG port configurations. They must be added to the bridge as trunk ports.

{{< tabs "TABID0112213 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add interface swp1 bridge trunk
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add interface swp1 bridge trunk
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add interface swp1 bridge trunk
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add interface swp1 bridge trunk
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

### MLAG Configuration Verification

To verify configurations the command `net show clag` can be used. In this example `esxi01` and `esxi03` are the MLAG interfaces connected to ESXi hosts.

{{< tabs "TABID012 ">}}
{{< tab "leaf01 ">}}
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

{{%notice note%}}

In the case of a non-LAG N-VDS uplink profile, no **MLAG ports** will be seen in the MLAG show output. The lack of MLAG ports doesn't mean that MLAG is not functional. MLAG is mandatory for using VRR, which is enhanced VRRP and is needed also for the non-LAG uplink profiles.

{{%/notice %}}

### VRR Configuration

ESXi uses active/active uplinks to spread Geneve encapsulated traffic to both ToR leaf switches. Each TEP device sends traffic to its default-gateway. As each TEP device has its own VLAN on the underlying fabric switch, layer 3 gateways (VRR) need to be created for it.  
ESXi TEP IP addresses can be on the same or different subnets. VMware best-practice configuration for TEP IP pool is to assign different subnets per physical rack.

{{%notice note%}}

VMware requires a VLAN per each type of traffic, for example, storage, vSAN, vMotion, or Overlay (TEP) traffic. This use case focus is only on the overlay VM to VM traffic and switches configurations.

{{%/notice %}}

The VLAN ID is a local parameter and not shared between the hypervisors. For deployment simplicity, use the same VLAN ID for all TEP devices used in both racks.

{{< tabs "101231231210 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add vlan 100
cumulus@leaf01:mgmt:~$ net add vlan 100 ip address 10.1.1.252/24
cumulus@leaf01:mgmt:~$ net add vlan 100 ip address-virtual 00:00:00:00:01:00 10.1.1.254/24
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add vlan 100
cumulus@leaf02:mgmt:~$ net add vlan 100 ip address 10.1.1.253/24
cumulus@leaf02:mgmt:~$ net add vlan 100 ip address-virtual 00:00:00:00:01:00 10.1.1.254/24
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add vlan 100
cumulus@leaf03:mgmt:~$ net add vlan 100 ip address 10.2.2.252/24
cumulus@leaf03:mgmt:~$ net add vlan 100 ip address-virtual 00:00:00:01:00:00 10.2.2.254/24
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add vlan 100
cumulus@leaf04:mgmt:~$ net add vlan 100 ip address 10.2.2.253/24
cumulus@leaf04:mgmt:~$ net add vlan 100 ip address-virtual 00:00:00:01:00:00 10.2.2.254/24
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

### VRR Configuration Verification

SVI and VRR interfaces will be displayed in the `net show interface` output as `vlanXXX` and `vlanXXX-v0`.

{{< tabs "101231d23f10 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode          LLDP                          Summary
-----  -------------  ---  -----  ------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                    IP: 127.0.0.1/8
       lo                                                                     IP: ::1/128
UP     eth0           1G   1500   Mgmt          oob-mgmt-switch (swp10)       Master: mgmt(UP)
       eth0                                                                   IP: 192.168.200.11/24(DHCP)
UP     swp1           1G   9216   BondMember    esxi01 (44:38:39:00:00:32)    Master: esxi01(UP)
UP     swp49          1G   9216   BondMember    leaf02 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember    leaf02 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   Default       spine01 (swp1)
UP     swp52          1G   9216   Default       spine02 (swp1)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi01         1G   9216   802.3ad                                     Master: bridge(UP)
       esxi01                                                                 Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                         IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                     Master: bridge(UP)
       peerlink                                                               Bond Members: swp49(UP)
       peerlink                                                               Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   Default
UP     vlan100        N/A  9216   Interface/L3                                IP: 10.1.1.252/24
UP     vlan100-v0     N/A  9216   Interface/L3                                IP: 10.1.1.254/24
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode          LLDP                          Summary
-----  -------------  ---  -----  ------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                    IP: 127.0.0.1/8
       lo                                                                     IP: ::1/128
UP     eth0           1G   1500   Mgmt          oob-mgmt-switch (swp11)       Master: mgmt(UP)
       eth0                                                                   IP: 192.168.200.12/24(DHCP)
UP     swp1           1G   9216   BondMember    esxi01 (44:38:39:00:00:38)    Master: esxi01(UP)
UP     swp49          1G   9216   BondMember    leaf01 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember    leaf01 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   Default       spine01 (swp2)
UP     swp52          1G   9216   Default       spine02 (swp2)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi01         1G   9216   802.3ad                                     Master: bridge(UP)
       esxi01                                                                 Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                         IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                     Master: bridge(UP)
       peerlink                                                               Bond Members: swp49(UP)
       peerlink                                                               Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   Default
UP     vlan100        N/A  9216   Interface/L3                                IP: 10.1.1.253/24
UP     vlan100-v0     N/A  9216   Interface/L3                                IP: 10.1.1.254/24
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode          LLDP                          Summary
-----  -------------  ---  -----  ------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                    IP: 127.0.0.1/8
       lo                                                                     IP: ::1/128
UP     eth0           1G   1500   Mgmt          oob-mgmt-switch (swp12)       Master: mgmt(UP)
       eth0                                                                   IP: 192.168.200.13/24(DHCP)
UP     swp1           1G   9216   BondMember    esxi03 (44:38:39:00:00:3e)    Master: esxi03(UP)
UP     swp49          1G   9216   BondMember    leaf04 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember    leaf04 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   Default       spine01 (swp3)
UP     swp52          1G   9216   Default       spine02 (swp3)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi03         1G   9216   802.3ad                                     Master: bridge(UP)
       esxi03                                                                 Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                         IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                     Master: bridge(UP)
       peerlink                                                               Bond Members: swp49(UP)
       peerlink                                                               Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   Default
UP     vlan100        N/A  9216   Interface/L3                                IP: 10.2.2.252/24
UP     vlan100-v0     N/A  9216   Interface/L3                                IP: 10.2.2.254/24
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode          LLDP                          Summary
-----  -------------  ---  -----  ------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                    IP: 127.0.0.1/8
       lo                                                                     IP: ::1/128
UP     eth0           1G   1500   Mgmt          oob-mgmt-switch (swp13)       Master: mgmt(UP)
       eth0                                                                   IP: 192.168.200.14/24(DHCP)
UP     swp1           1G   9216   BondMember    esxi03 (44:38:39:00:00:44)    Master: esxi03(UP)
UP     swp49          1G   9216   BondMember    leaf03 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember    leaf03 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   Default       spine01 (swp4)
UP     swp52          1G   9216   Default       spine02 (swp4)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi03         1G   9216   802.3ad                                     Master: bridge(UP)
       esxi03                                                                 Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                         IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                     Master: bridge(UP)
       peerlink                                                               Bond Members: swp49(UP)
       peerlink                                                               Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   Default
UP     vlan100        N/A  9216   Interface/L3                                IP: 10.2.2.253/24
UP     vlan100-v0     N/A  9216   Interface/L3                                IP: 10.2.2.254/24
```
{{< /tab >}}
{{< /tabs >}}

## BGP Configuration

All underlay IP fabric BGP peerings in this guide are based on eBGP. Cumulus Linux [Auto BGP](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP/#auto-bgp) and [BGP Unnumbered](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered) configurations are used.

{{%notice note%}}

Auto BGP configuration is only available using NCLU. If you want to use `vtysh` configuration, a BGP ASN must be configured.  
For additional details refer to the [Configuring FRRouting](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/FRRouting/Configure-FRRouting/#) documentation.

{{%/notice %}}

### BGP Peerings Establishment

{{< tabs "10 ">}}
{{< tab "NCLU Commands ">}}
{{< tabs "109 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf01:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf01:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf01:mgmt:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf01:mgmt:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf02:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf02:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf02:mgmt:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf02:mgmt:~$ net add bgp router-id 10.10.10.2
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf03:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf03:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf03:mgmt:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf03:mgmt:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf04:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf04:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf04:mgmt:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf04:mgmt:~$ net add bgp router-id 10.10.10.4
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " spine01 ">}}
```
cumulus@spine01:mgmt:~$ net add bgp autonomous-system spine
cumulus@spine01:mgmt:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp2 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp3 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp4 remote-as external
cumulus@spine01:mgmt:~$ net add bgp bestpath as-path multipath-relax   
cumulus@spine01:mgmt:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " spine02 ">}}
```
cumulus@spine02:mgmt:~$ net add bgp autonomous-system spine
cumulus@spine02:mgmt:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp2 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp3 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp4 remote-as external
cumulus@spine02:mgmt:~$ net add bgp bestpath as-path multipath-relax   
cumulus@spine02:mgmt:~$ net add bgp router-id 10.10.10.102
cumulus@spine02:mgmt:~$ net commit
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

ESXi hypervisors build layer 2 overlay tunnels to send Geneve encapsulated traffic over the layer 3 underlay. The undelaying IP fabric must be aware of each TEP device in the network. This is done by advertising the local Overlay TEP VLAN (TEP subnet) we created earlier into BGP.

Use the `redistribute connected` command to inject the directly connected routes into BGP.  
This command can be used also with filtering to avoid unwanted/unnecessary subnets get into BGP. For more information and commands. check [Route Filtering and Redistribution](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Routing/Route-Filtering-and-Redistribution/) page.

{{< tabs "101rr0 ">}}
{{< tab "NCLU Commands ">}}
{{< tabs "109dd0 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add bgp redistribute connected
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add bgp redistribute connected
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add bgp redistribute connected
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add bgp redistribute connected
cumulus@leaf04:mgmt:~$ net commit
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

To verify all BGP peerings established correctly, use the `net show bgp summary` command in NCLU, or `show ip bgp summary` in `vtysh`

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

Once all BGP peerings established, all the redistributed local TEP VLANs (subnets) should appear in the routing table of each switch. Use the `net show route` command in NCLU, or `show ip route` in `vtysh` to check the routing table 

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

## Traffic Flow

ESXi hypervisors can reach each other's TEP addresses and build Geneve tunnels for the overlay VM traffic.

Two traffic flow examples are described below.

### Layer 2 Virtualized Traffic

Both VMs are assigned to the same VMware logical segment (logical switch), which means they are in the same subnet. Each segment has its own unique Virtual Network Identifier (VNI) assigned by NSX-T. This VNI is added into the Geneve packet header on the source TEP. The destination TEP identifies which segment the traffic belongs to base on this VNI. All segments that share the same Overlay Transport Zone, uses the same TEP addresses to establish the tunnels. It is possible to have more than one Overlay TZ on the N-VDS, but for this case, more VLANs needs to be configured and advertised on the underlay switches. This scenario uses only one Overlay TZ (one TEP VLAN).

{{<figure src="/images/guides/cumulus-nsxt/Pure_L2_VNI.JPG">}}

VM1 `172.16.0.1` on ESXi01 sends traffic to VM3 `172.16.0.3` on ESXi03: 
1. The packet reaches the local hypervisor's TEP device `10.1.1.1`.
2. The local TEP device encapsulates it into a new Geneve packet and inserts the assigned to segment VNI `65510`.  
The new encapsulated packet's source IP address is the local TEP IP `10.1.1.1`, and the destination IP address is the remote TEP device `10.2.2.1`.
3. The encapsulated packet is routed to the remote TEP device through the underlay network.
4. The remote TEP device (ESXi03) receives and decapsulates the Geneve encapsulated packet.
5. The traffic forwarded to the destination VM3 based on the VNI inside the Geneve header.

### Layer 3 Virtualized Traffic

This scenario examines two segments (logical switches) with two VMs assigned to each. As different segments means different subnets, a unique VNI assigned to each.  
For different subnets to communicate, traffic needs to be routed. In a regular physical world, the switches could route between the subnets using directly connected routing, or by any other routing protocol (e.g. BGP, OSPF). But as all the traffic is between virtual machines, it's all inside the virtual world, so none of the underlaying switches are aware of it.

To route between logical segments within the virtualized world, or as VMware calls it "east-west traffic" traffic, Tier 1 Gateway (aka T1 Router) can be used. T1 Router is a logical distributed router which "lives" in each ESXi hypervisors and has virtual downlinks to the logical segments. It acts as segment's (VLAN) default-gateway and using its routing table sends traffic between different segments. it works like a regular router just within the virtual world.

As T1 router is logically distributed over all the physical devices (ESXI), the packet doesn't even leave the local hypervisor to be routed. Therefore, the routing is done locally on the ESXi and the new segment's (subnet) VNI determined based on the destination VM segment (and T1 routing table).

{{%notice note%}}

Routing in VMware environments always done closest to the source as possible. 

{{%/notice %}}

{{<figure src="/images/guides/cumulus-nsxt/T1.JPG">}}

VM1 and VM3 are in `VLAN100` `172.16.0.0/24` - VNI `65510`. VM2 and VM4 are in `VLAN200` `172.16.1.0/24` - VNI 65520. Both segments assigned to the same Overlay TZ which uses `10.1.1.0` and `10.2.2.1` as TEP IPs to maintain Geneve tunnel between the physical ESXi01 and ESX03 hypervisors.  
Traffic within the same segment handled the same way as [Layer 2 Virtualized Traffic](#layer-2-virtualized-environment) scenario.

{{%notice note%}}

It is possible to use many T1 Routers and assign different segments to different routers for load-balancing etc. Then their communication is done by Tier 0 Gateway which will be covered later. In addition, T1 Router doesn't route traffic outside the virtual world, it is done by T0 as well.

{{%/notice %}}

From the underlay IP fabric perspective, routing between logical segments means absolutely nothing. As both segments share the same Overlay TZ, they still use the same TEP IP addresses (TEP VLAN) to establish overlay Geneve tunnel between hypervisors, so no additional configuration is needed on the switches.

VM1 `172.16.0.1` on ESXi01 sends traffic to VM4 `172.16.1.4` on ESXi03: 
1. The packet reaches the T1 Router as its destination IP address in different subnet (T1 is logical router so the packet is still in ESXi01). 
2. T1 examines its routing table to determine the destination path. 
3. As `VLAN200` segment is also attached to the same T1 router, the destination path to VM4 is the remote ESXi hypervisor via the TEP interface.
4. Local TEP encapsulates the packet into Geneve using VNI `65520` of `VLAN200` segment. Geneve packet's source and destination IP addresses are of the TEP devices `10.1.1.1`-`10.2.2.1)`. As the routing is done internally on the ESXi, between the hypervisors is the same layer 2 tunnel (routing and then bridging).
5. The encapsulated packet sent to remote TEP device over the Geneve overlay tunnel based on the underlay IP fabric BGP routing.
6. Remote TEP device (ESXi03) receives and decapsulates the Geneve encapsulated packet.
7. The traffic forwarded to the destination VM4 based on the VNI inside the Geneve header.







# Virtualized and Bare-Metal Server Environment

This use-case covers VMware virtualized environment with the need to connect to a Bare-Metal (BM) server. This could the when the virtualized environment deployed as part of an already existing fabric (brownfield) and VMs need to communicate with a legacy or any other server which doesn't run VMs (not part of the virtualized world).

As we already know from the [Pure Virtualized Environment](#pure-virtualized-environment), for VMs to communicate to each other, NSX-T uses Geneve encapsulation in layer 2 overlay tunnels over layer 3 fabric. But, in cases where VM needs to communicate with BM servers, Geneve tunnels not the answer. So, for traffic to be sent between the virtualized and the physical worlds, it must be sent Geneve encapsulated, decapsulated, and sent as regular IP packet in the underlay network. This is handled by NSX-T component called [NSX Edge](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.0/installation/GUID-5EF2998C-4867-4DA6-B1C6-8A6F8EBCC411.html). In a nutshell, NSX Edge is a gateway between the virtualized and the outside physical worlds. It acts as TEP devic0 and as underlay router, it establishes BGP/OSPF peering with the underlay fabric to route traffic in/out the virtualized environment.

{{%notice note%}}

There is an option for VM-BM communication using Geneve encapsulation - [NSX Edge on Bare Metal](https://docs.vmware.com/en/VMware-NSX-T-Data-Center/3.1/installation/GUID-21E4C80B-5900-433A-BEA2-EA41FBE690FE.html), but it's out of scope of this guide.

{{%/notice %}}

The below underlay IP fabric configuration based on this example topology diagram and physical connectivity

{{<figure src="/images/guides/cumulus-nsxt/virt_bare_metal.JPG">}}

**Rack 1** – Two NVIDIA Switches in MLAG + One ESXi hypervisor connected in active/active bonding  
**Rack 2** – Two NVIDIA Switches in MLAG + One ESXi hypervisor and One Bare-Metal server, both connected in active/active bonding

## Physical Connectivity

{{< tabs "TABID01022 ">}}

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
swp2       1G     Default  server01         44:38:39:00:00:40
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
swp2       1G     Default  server01         44:38:39:00:00:46
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

## MTU Configuration

VMware recommendation is to use Jumbo MTU (9k) on all virtual and physical network elements end-to-end, including the BM servers as well. Geneve encapsulation, requires a minimum MTU of `1600B` (`1700B` for extended Geneve header options). But it is better to use 9k MTU for the entire network path. This improves the throughput of storage, vSAN, vMotion, NFS and vSphere Replication.

Using the below commands, you can examine switches’ physical interfaces MTU settings. By default, all interfaces on Cumulus Linux have Jumbo 9k MTU.

{{< tabs "455516 ">}}

{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show interface
State  Name   Spd  MTU    Mode      LLDP                          Summary
-----  -----  ---  -----  --------  ----------------------------  ---------------------------
UP     lo     N/A  65536  Loopback                                IP: 127.0.0.1/8
       lo                                                         IP: ::1/128
UP     eth0   1G   1500   Mgmt      oob-mgmt-switch (swp10)       Master: mgmt(UP)
       eth0                                                       IP: 192.168.200.11/24(DHCP)
UP     swp1   1G   9216   Default   esxi01 (44:38:39:00:00:32)
UP     swp49  1G   9216   Default   leaf02 (swp49)
UP     swp50  1G   9216   Default   leaf02 (swp50)
UP     swp51  1G   9216   Default   spine01 (swp1)
UP     swp52  1G   9216   Default   spine02 (swp1)
UP     mgmt   N/A  65536  VRF                                     IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show interface
State  Name   Spd  MTU    Mode      LLDP                          Summary
-----  -----  ---  -----  --------  ----------------------------  ---------------------------
UP     lo     N/A  65536  Loopback                                IP: 127.0.0.1/8
       lo                                                         IP: ::1/128
UP     eth0   1G   1500   Mgmt      oob-mgmt-switch (swp11)       Master: mgmt(UP)
       eth0                                                       IP: 192.168.200.12/24(DHCP)
UP     swp1   1G   9216   Default   esxi01 (44:38:39:00:00:38)
UP     swp49  1G   9216   Default   leaf01 (swp49)
UP     swp50  1G   9216   Default   leaf01 (swp50)
UP     swp51  1G   9216   Default   spine01 (swp2)
UP     swp52  1G   9216   Default   spine02 (swp2)
UP     mgmt   N/A  65536  VRF                                     IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show interface
State  Name   Spd  MTU    Mode      LLDP                          Summary
-----  -----  ---  -----  --------  ----------------------------  ---------------------------
UP     lo     N/A  65536  Loopback                                IP: 127.0.0.1/8
       lo                                                         IP: ::1/128
UP     eth0   1G   1500   Mgmt      oob-mgmt-switch (swp12)       Master: mgmt(UP)
       eth0                                                       IP: 192.168.200.13/24(DHCP)
UP     swp1   1G   9216   Default   esxi04 (44:38:39:00:00:3e)
UP     swp2   1G   9216   Default   server01 (44:38:39:00:00:40)
UP     swp49  1G   9216   Default   leaf04 (swp49)
UP     swp50  1G   9216   Default   leaf04 (swp50)
UP     swp51  1G   9216   Default   spine01 (swp3)
UP     swp52  1G   9216   Default   spine02 (swp3)
UP     mgmt   N/A  65536  VRF                                     IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show interface
State  Name   Spd  MTU    Mode      LLDP                          Summary
-----  -----  ---  -----  --------  ----------------------------  ---------------------------
UP     lo     N/A  65536  Loopback                                IP: 127.0.0.1/8
       lo                                                         IP: ::1/128
UP     eth0   1G   1500   Mgmt      oob-mgmt-switch (swp13)       Master: mgmt(UP)
       eth0                                                       IP: 192.168.200.14/24(DHCP)
UP     swp1   1G   9216   Default   esxi03 (44:38:39:00:00:44)
UP     swp2   1G   9216   Default   server01 (44:38:39:00:00:46)
UP     swp49  1G   9216   Default   leaf03 (swp49)
UP     swp50  1G   9216   Default   leaf03 (swp50)
UP     swp51  1G   9216   Default   spine01 (swp4)
UP     swp52  1G   9216   Default   spine02 (swp4)
UP     mgmt   N/A  65536  VRF                                     IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "spine01 ">}}
```
cumulus@spine01:mgmt:~$ net show interface
State  Name  Spd  MTU    Mode      LLDP                     Summary
-----  ----  ---  -----  --------  -----------------------  ---------------------------
UP     lo    N/A  65536  Loopback                           IP: 127.0.0.1/8
       lo                                                   IP: ::1/128
UP     eth0  1G   1500   Mgmt      oob-mgmt-switch (swp14)  Master: mgmt(UP)
       eth0                                                 IP: 192.168.200.21/24(DHCP)
UP     swp1  1G   9216   Default   leaf01 (swp51)
UP     swp2  1G   9216   Default   leaf02 (swp51)
UP     swp3  1G   9216   Default   leaf03 (swp51)
UP     swp4  1G   9216   Default   leaf04 (swp51)
UP     mgmt  N/A  65536  VRF                                IP: 127.0.0.1/8
```
{{< /tab >}}
{{< tab "spine02 ">}}
```
cumulus@spine02:mgmt:~$ net show interface
State  Name  Spd  MTU    Mode      LLDP                     Summary
-----  ----  ---  -----  --------  -----------------------  ---------------------------
UP     lo    N/A  65536  Loopback                           IP: 127.0.0.1/8
       lo                                                   IP: ::1/128
UP     eth0  1G   1500   Mgmt      oob-mgmt-switch (swp15)  Master: mgmt(UP)
       eth0                                                 IP: 192.168.200.22/24(DHCP)
UP     swp1  1G   9216   Default   leaf01 (swp52)
UP     swp2  1G   9216   Default   leaf02 (swp52)
UP     swp3  1G   9216   Default   leaf03 (swp52)
UP     swp4  1G   9216   Default   leaf04 (swp52)
UP     mgmt  N/A  65536  VRF                                IP: 127.0.0.1/8
```
{{< /tab >}}
{{< /tabs >}}

To manually define the MTU use the `net add interface` command.
```
cumulus@switch:~$ net add interface swp1 mtu 9216
```

To restore the MTU to the default value of 9216 use `net del interface mtu`.
```
cumulus@switch:~$ net del interface swp1 mtu
```

## MLAG and VRR Configuration

In our example topology, VM will be located on one physical ESXi01 hypervisor and Edge VM on the other ESXI03. As Edge VM responsible for virtualized traffic to be sent out-of-the virtual world, both VM and Edge must share the same Overlay TZ (VLAN) to communicate. But, as they are divided by a layer 3 underlay network, we must ensure the Geneve layer 2 overlay traffic to pass over it. In addition, the BM server is also part of the network and located in the physical world. So, Edge will have to know how to reach it as well. 

The ESXi hypervisors and the BM server connected using active/active LAG to the leaf switches for redundancy and more throughput. For that, we create active/active, redundant layer 2 and layer 3 connectivity using MLAG protocol with VRR on top. The below Cumulus Linux switches configuration demonstrates how to configure MLAG and VRR.
Make sure to set MLAG+VRR regardless the N-VDS uplink profile (active/active or active/standby), unless of course, only one ToR (leaf) or a single link is used to connect the hypervisor.

### MLAG General Configuration 

Cumulus Linux MLAG configuration is done by a single command. It automatically creates the peerlink bond and configures all MLAG related configuration.

{{< tabs "TABIDd013 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:01 interface swp49-50 primary backup-ip 192.168.200.12 vrf mgmt
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:01 interface swp49-50 secondary backup-ip 192.168.200.11 vrf mgmt
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:02 interface swp49-50 primary backup-ip 192.168.200.14 vrf mgmt
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:02 interface swp49-50 secondary backup-ip 192.168.200.13 vrf mgmt
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

### MLAG Interfaces Configuration - Active/Active LACP LAG Bare-Metal and N-VDS Uplink Profile

If the recommended active/active LAG (LACP) N-VDS uplink profile is used, switch downlink interfaces for ESXi must be bonded into MLAG ports (LACP bonds).
This action also automatically adds the MLAG interfaces into the bridge and sets them as trunk ports (VLAN tagging) with all VLANs allowed. The same should be done for the switch downlinks to the BM server

{{%notice note%}}

For active/standby environments, do not configure MLAG. Follow the instructions under the [Switch Ports Configuration - non-LAG Bare-Metal and N-VDS Uplink Profile ](#switch-ports-configuration---non-lag-bare-metal-and-n-vds-uplink-profile) section.
Do not use active/active LACP LAG uplink profile for the Overlay Transport Zone on N-VDS nor LACP bond on BM server.

{{%/notice %}}

{{< tabs "TABID0dd213 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add clag port bond esxi01 interface swp1 clag-id 1
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add clag port bond esxi01 interface swp1 clag-id 1
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add clag port bond esxi03 interface swp1 clag-id 1    
cumulus@leaf03:mgmt:~$ net add clag port bond server01 interface swp2 clag-id 2
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add clag port bond esxi03 interface swp1 clag-id 1
cumulus@leaf04:mgmt:~$ net add clag port bond server01 interface swp2 clag-id 2
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

### Switch Ports Configuration - non-LAG Bare-Metal and N-VDS Uplink Profile 

if active/standby or active/active non-LAG N-VDS uplink profiles used, switch downlink interfaces for ESXi must be left regular ports and not use any MLAG ports configuration. They must be added into the bridge as trunk ports.

{{< tabs "TABID0dd112213 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add interface swp1 bridge trunk
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add interface swp1 bridge trunk
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add interface swp1 bridge trunk
cumulus@leaf03:mgmt:~$ net add interface swp2 bridge trunk
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add interface swp1 bridge trunk
cumulus@leaf04:mgmt:~$ net add interface swp2 bridge trunk
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

### MLAG Configuration Verification

To verify configurations the command `net show clag` can be used. In this example `esxi01` and `esxi03` are the MLAG interfaces connected to ESXi hosts. `server01` is MLAG interfaces connected to the BM server.  

{{< tabs "TABID2dd2012 ">}}
{{< tab "leaf01 ">}}
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
        server01   server01           2         -                      -
```
{{< /tab >}}
{{< tab "leaf04 ">}}
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
        server01   server01           2         -                      -
```
{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}

In the case of a non-LAG N-VDS uplink profile, no **MLAG ports** will be seen in the MLAG show output. The lack of MLAG ports doesn't mean that MLAG is not functional. MLAG is mandatory for using VRR, which is enhanced VRRP and is needed also for the non-LAG uplink profiles.

{{%/notice %}}

### VRR Configuration

ESXi hypervisors and the BM server use active/active uplinks to spread traffic to both ToR leaf switches. For that, they must send the traffic to their default-gateways. As all elements in our network have their own IP subnet and VLAN (ESXi01 TEP, Edge TEP on ESXi03, BM server), layer 3 gateways (VRR) need to be created for each.  
ESXi TEP IP addresses can be on a same or different subnet. VMware best-practice configuration for TEP IP pool is to assign different subnet (e.g., /24) per physical rack. Each hypervisor (ESXi) must have at least one physical NIC connected to its Top-of-Rack (ToR/Leaf) switch.

{{%notice note%}}

VMware requires a VLAN per each type of traffic, for example, storage, vSAN, vMotion, or Overlay (TEP) traffic. This use case focus is only on the overlay VM to VM traffic and switches configurations.

{{%/notice %}}

NSX Edge uses two additional virtual uplinks to communicate with the physical world, each uplink in different VLAN. One uplink towards the left leaf switch, the second towards the right. Over these virtual uplinks, it establishes BGP peerings to route traffic to the physical world. As Edge VM is part of the Overlay TZ for virtualized traffic, and VLAN TZ for traffic in/out the physical world, both transport-zones use the same ESXi uplinks (trunk port), but as said, in different VLANs. 

To establish BGP peering with the underlay switches, they must be configured with additional VLANs and SVIs. In our case, we use [Subinterfaces](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/#subinterfaces) configuration instead. But, of course, VLANs and SVIs could serve for that as well.

Create VLAN, SVI, Virtual IP (VRR), and the subinterfaces for the Edge uplinks.  
The VLAN ID is a local parameter and not shared between the hypervisors. For deployment simplicity, use the same VLAN ID for all TEP devices used in both racks.

{{< tabs "10D ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add vlan 100                                                       ### TEP VLAN
cumulus@leaf01:mgmt:~$ net add vlan 100 ip address 10.1.1.252/24                              ### TEP SVI
cumulus@leaf01:mgmt:~$ net add vlan 100 ip address-virtual 00:00:00:00:01:00 10.1.1.25 4/24   ### TEP VRR (GW)
cumulus@leaf01:mgmt:~$ net commit                                                             
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add vlan 100                                                       ### TEP VLAN    
cumulus@leaf02:mgmt:~$ net add vlan 100 ip address 10.1.1.253/24                              ### TEP SVI
cumulus@leaf02:mgmt:~$ net add vlan 100 ip address-virtual 00:00:00:00:01:00 10.1.1.254/24    ### TEP VRR (GW)
cumulus@leaf02:mgmt:~$ net commit                                                                   
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add vlan 100                                                       ### TEP VLAN
cumulus@leaf03:mgmt:~$ net add vlan 100 ip address 10.2.2.252/24                              ### TEP SVI
cumulus@leaf03:mgmt:~$ net add vlan 100 ip address-virtual 00:00:00:01:00:00 10.2.2.254/24    ### TEP VRR (GW)
cumulus@leaf03:mgmt:~$ net add vlan 200                                                       ### BM VLAN
cumulus@leaf03:mgmt:~$ net add vlan 200 ip address 20.2.2.252/24                              ### BM SVI
cumulus@leaf03:mgmt:~$ net add vlan 200 ip address-virtual 00:00:00:02:00:00 20.2.2.254/24    ### BM VRR (GW)
cumulus@leaf03:mgmt:~$ net add interface swp1.300 ip address 30.0.0.254/24                    ### Edge VLAN300 subinterface
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add vlan 100                                                       ### TEP VLAN                                               
cumulus@leaf04:mgmt:~$ net add vlan 100 ip address 10.2.2.253/24                              ### TEP SVI                              
cumulus@leaf04:mgmt:~$ net add vlan 100 ip address-virtual 00:00:00:01:00:00 10.2.2.254/24    ### TEP VRR (GW)     
cumulus@leaf04:mgmt:~$ net add vlan 200                                                       ### BM VLAN                                                     
cumulus@leaf04:mgmt:~$ net add vlan 200 ip address 20.2.2.253/24                              ### BM SVI    
cumulus@leaf04:mgmt:~$ net add vlan 200 ip address-virtual 00:00:00:02:00:00 20.2.2.254/24    ### BM VRR (GW)        
cumulus@leaf04:mgmt:~$ net add interface swp1.301 ip address 31.0.0.254/24                    ### Edge VLAN301 subinterface                              
cumulus@leaf04:mgmt:~$ net commit                                                                     
```
{{< /tab >}}
{{< /tabs >}}

### VRR and Subinterfaces Configuration Verification

SVI and VRR interfaces will be displayed in the `net show interface` output as `vlanXXX` and `vlanXXX-v0`. Subinterfaces will be shown as `swpX.xxx`

{{< tabs "10h1d23f10 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode          LLDP                          Summary
-----  -------------  ---  -----  ------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                    IP: 127.0.0.1/8
       lo                                                                     IP: ::1/128
UP     eth0           1G   1500   Mgmt          oob-mgmt-switch (swp10)       Master: mgmt(UP)
       eth0                                                                   IP: 192.168.200.11/24(DHCP)
UP     swp1           1G   9216   BondMember    esxi01 (44:38:39:00:00:32)    Master: esxi01(UP)
UP     swp49          1G   9216   BondMember    leaf02 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember    leaf02 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   Default       spine01 (swp1)
UP     swp52          1G   9216   Default       spine02 (swp1)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi01         1G   9216   802.3ad                                     Master: bridge(UP)
       esxi01                                                                 Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                         IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                     Master: bridge(UP)
       peerlink                                                               Bond Members: swp49(UP)
       peerlink                                                               Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   Default
UP     vlan100        N/A  9216   Interface/L3                                IP: 10.1.1.252/24
UP     vlan100-v0     N/A  9216   Interface/L3                                IP: 10.1.1.254/24
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode          LLDP                          Summary
-----  -------------  ---  -----  ------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                    IP: 127.0.0.1/8
       lo                                                                     IP: ::1/128
UP     eth0           1G   1500   Mgmt          oob-mgmt-switch (swp11)       Master: mgmt(UP)
       eth0                                                                   IP: 192.168.200.12/24(DHCP)
UP     swp1           1G   9216   BondMember    esxi01 (44:38:39:00:00:38)    Master: esxi01(UP)
UP     swp49          1G   9216   BondMember    leaf01 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember    leaf01 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   Default       spine01 (swp2)
UP     swp52          1G   9216   Default       spine02 (swp2)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi01         1G   9216   802.3ad                                     Master: bridge(UP)
       esxi01                                                                 Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                         IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                     Master: bridge(UP)
       peerlink                                                               Bond Members: swp49(UP)
       peerlink                                                               Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   Default
UP     vlan100        N/A  9216   Interface/L3                                IP: 10.1.1.253/24
UP     vlan100-v0     N/A  9216   Interface/L3                                IP: 10.1.1.254/24
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode          LLDP                          Summary
-----  -------------  ---  -----  ------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                    IP: 127.0.0.1/8
       lo                                                                     IP: ::1/128
UP     eth0           1G   1500   Mgmt          oob-mgmt-switch (swp12)       Master: mgmt(UP)
       eth0                                                                   IP: 192.168.200.13/24(DHCP)
UP     swp1           1G   9216   BondMember    esxi03 (44:38:39:00:00:3e)    Master: esxi03(UP)
UP     swp1.300       1G   9216   SubInt/L3                                   IP: 30.0.0.254/24
UP     swp2           1G   9216   BondMember    server01 (44:38:39:00:00:40)  Master: server01(UP)
UP     swp49          1G   9216   BondMember    leaf04 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember    leaf04 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   Default       spine01 (swp3)
UP     swp52          1G   9216   Default       spine02 (swp3)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi03         1G   9216   802.3ad                                     Master: bridge(UP)
       esxi03                                                                 Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                         IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                     Master: bridge(UP)
       peerlink                                                               Bond Members: swp49(UP)
       peerlink                                                               Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   Default
UP     server01       1G   9216   802.3ad                                     Master: bridge(UP)
       server01                                                               Bond Members: swp2(UP)
UP     vlan100        N/A  9216   Interface/L3                                IP: 10.2.2.252/24
UP     vlan100-v0     N/A  9216   Interface/L3                                IP: 10.2.2.254/24
UP     vlan200        N/A  9216   Interface/L3                                IP: 20.2.2.252/24
UP     vlan200-v0     N/A  9216   Interface/L3                                IP: 20.2.2.254/24
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode          LLDP                          Summary
-----  -------------  ---  -----  ------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                    IP: 127.0.0.1/8
       lo                                                                     IP: ::1/128
UP     eth0           1G   1500   Mgmt          oob-mgmt-switch (swp13)       Master: mgmt(UP)
       eth0                                                                   IP: 192.168.200.14/24(DHCP)
UP     swp1           1G   9216   BondMember    esxi03 (44:38:39:00:00:44)    Master: esxi03(UP)
UP     swp1.301       1G   9216   SubInt/L3                                   IP: 31.0.0.254/24
UP     swp2           1G   9216   BondMember    server01 (44:38:39:00:00:46)  Master: server01(UP)
UP     swp49          1G   9216   BondMember    leaf03 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember    leaf03 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   Default       spine01 (swp4)
UP     swp52          1G   9216   Default       spine02 (swp4)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi03         1G   9216   802.3ad                                     Master: bridge(UP)
       esxi03                                                                 Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                         IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                     Master: bridge(UP)
       peerlink                                                               Bond Members: swp49(UP)
       peerlink                                                               Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   Default
UP     server01       1G   9216   802.3ad                                     Master: bridge(UP)
       server01                                                               Bond Members: swp2(UP)
UP     vlan100        N/A  9216   Interface/L3                                IP: 10.2.2.253/24
UP     vlan100-v0     N/A  9216   Interface/L3                                IP: 10.2.2.254/24
UP     vlan200        N/A  9216   Interface/L3                                IP: 20.2.2.253/24
UP     vlan200-v0     N/A  9216   Interface/L3                                IP: 20.2.2.254/24
```
{{< /tab >}}
{{< /tabs >}}

## BGP Configuration

As mentioned earlier, all underlay IP fabric BGP peerings in this guide are based on eBGP. To ease the configuration deployment to minimum efforts, Cumulus Linux [Auto BGP](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP/#auto-bgp) and [BGP Unnumbered](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered) configuration is used.

The subinterfaces on `leaf03` and `leaf04` to peer with Edge uplinks have IPv4 addresses. BGP peering between them must be with ASN and numbered as Edge doesn't support otherwise.

{{%notice note%}}

Auto BGP configuration is only available using NCLU. If you want to use `vtysh` configuration, BGP ASN must be configured.  
To configure BGP using `vtysh`, first enable `bgpd` daemon as described in [Configure FRRouting](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/FRRouting/Configure-FRRouting/#) page.

{{%/notice %}}

### BGP Peerings Establishment 

{{< tabs "112dfff30 ">}}
{{< tab "NCLU Commands ">}}
{{< tabs "13rr3309 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf01:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf01:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf01:mgmt:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf01:mgmt:~$ net add bgp router-id 10.10.10.1
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf02:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf02:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf02:mgmt:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf02:mgmt:~$ net add bgp router-id 10.10.10.2
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf03:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf03:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf03:mgmt:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf03:mgmt:~$ net add bgp neighbor 30.0.0.1 remote-as 65555            ### BGP to Edge VM in ASN 65555
cumulus@leaf03:mgmt:~$ net add bgp router-id 10.10.10.3
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf04:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf04:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf04:mgmt:~$ net add bgp neighbor swp52 remote-as external
cumulus@leaf04:mgmt:~$ net add bgp neighbor 31.0.0.1 remote-as 65555            ### BGP to Edge VM in ASN 65555
cumulus@leaf04:mgmt:~$ net add bgp router-id 10.10.10.4
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " spine01 ">}}
```
cumulus@spine01:mgmt:~$ net add bgp autonomous-system spine
cumulus@spine01:mgmt:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp2 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp3 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp4 remote-as external
cumulus@spine01:mgmt:~$ net add bgp bestpath as-path multipath-relax
cumulus@spine01:mgmt:~$ net add bgp router-id 10.10.10.101
cumulus@spine01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " spine02 ">}}
```
cumulus@spine02:mgmt:~$ net add bgp autonomous-system spine
cumulus@spine02:mgmt:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp2 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp3 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp4 remote-as external
cumulus@spine02:mgmt:~$ net add bgp bestpath as-path multipath-relax
cumulus@spine02:mgmt:~$ net add bgp router-id 10.10.10.102
cumulus@spine02:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "vtysh Commands ">}}
{{< tabs "203ssr34d5 ">}}
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
leaf03(config-router)# neighbor 30.0.0.1 remote-as 65555
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
leaf04(config-router)# neighbor 31.0.0.1 remote-as 65555
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

### TEP VLAN, Edge Virtual Uplinks and Bare-Metal Subnets Advertisement into BGP 

As we already know, ESXi hypervisors builds layer 2 overlay tunnels to send Geneve encapsulated traffic over the layer 3 underlay. For that, the undelaying IP fabric must be aware about how to reach each TEP, Edge uplink and BM server in the network. In addition, NSX edge must know the underlay subnets (BM). This is done by advertising the local Overlay TEP VLANs, Edge uplinks and BM subnets we created earlier into BGP.

There are two ways to advertise networks into BGP, by `network` command to advertise specifically, or by `redistribute` command to inject subnets into BGP from a non-BGP protocol. In our case we use the `redistribute connected` command to inject the directly connected routes into BGP.

There are two ways to advertise networks into BGP, by network command to advertise specifically, or by redistribute command to inject subnets into BGP from a non-BGP protocol. In our case we use the redistribute connected command to inject the directly connected routes into BGP.
This command can be used also with filtering to avoid unwanted/unnecessary subnets get into BGP. For more information and commands check out the [Route Filtering and Redistribution](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Routing/Route-Filtering-and-Redistribution/) page.


{{< tabs "10u1rr0 ">}}
{{< tab "NCLU Commands ">}}
{{< tabs "109daussd0 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add bgp redistribute connected
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add bgp redistribute connected
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add bgp redistribute connected
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add bgp redistribute connected
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "vtysh Commands ">}}
{{< tabs "sssus ">}}
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

To verify all BGP peerings established correctly, use the `net show bgp summary` command in NCLU, or `show ip bgp summary` in `vtysh`

{{< tabs "TABID1ufr431 ">}}
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
leaf02(peerlink.4094) 4 4259632649     25181     25185        0    0    0 00:22:42            6        6
spine01(swp51)        4 4200000000     25181     25180        0    0    0 00:22:43            6        6
spine02(swp52)        4 4200000000     25160     25159        0    0    0 00:22:01            6        6

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
leaf01(peerlink.4094) 4 4259632651     25188     25188        0    0    0 00:22:59            6        6
spine01(swp51)        4 4200000000     25195     25188        0    0    0 00:23:02            5        6
spine02(swp52)        4 4200000000     25173     25164        0    0    0 00:22:20            5        6

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
leaf04(peerlink.4094) 4 4259632667     50465     50468        0    0    0 00:22:41            5        6
spine01(swp51)        4 4200000000     50480     50503        0    0    0 00:22:54            3        6
spine02(swp52)        4 4200000000     50466     50491        0    0    0 00:22:35            4        6
30.0.0.1              4 65555           1023      1035        0    0    0 00:11:23            2        6

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
31.0.0.1              4 65555           1056      1076        0    0    0 00:11:35            2        6

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
leaf01(swp1)    4 4259632651     70978     71007        0    0    0 00:32:59            2        6
leaf02(swp2)    4 4259632649     70986     71031        0    0    0 00:33:02            2        6
leaf03(swp3)    4 4259632661     71046     71078        0    0    0 00:32:36            5        6
leaf04(swp4)    4 4259632667     71039     71087        0    0    0 00:32:24            5        6

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
leaf01(swp1)    4 4259632651     70954     70970        0    0    0 00:32:46            2        6
leaf02(swp2)    4 4259632649     70957     70990        0    0    0 00:32:49            2        6
leaf03(swp3)    4 4259632661     71029     71071        0    0    0 00:32:46            5        6
leaf04(swp4)    4 4259632667     71019     71061        0    0    0 00:32:49            5        6

Total number of neighbors 4
```
{{< /tab >}}
{{< /tabs >}}

Once  all BGP peerings established, all the redistributed local TEP VLANs, Edge uplinks and BM subnets should appear in the routing table of each switch. Use the `net show route` command in NCLU, or `show ip route` in `vtysh` to check the routing table

{{< tabs "TABuIDgg1631 ">}}
{{< tab "leaf01 ">}}
Leaf01 has two ECMP routes (via both spine switches) to ESXi03 TEP, Edge virtual uplinks and the BM subnet received by BGP - `10.2.2.0/24`, `192.168.0.0/24`, `30.0.0.0/24`, `31.0.0.0/24`, `172.16.0.0/24`. There are unnecessary prefixed learned, so consider filtering them as needed
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
C * 10.1.1.0/24 [0/1024] is directly connected, vlan100-v0, 00:34:45
C>* 10.1.1.0/24 is directly connected, vlan100, 00:34:45
B>* 10.2.2.0/24 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 00:34:13
  *                    via fe80::4638:39ff:fe00:3, swp52, weight 1, 00:34:13
B>* 30.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 00:20:12
  *                    via fe80::4638:39ff:fe00:3, swp52, weight 1, 00:20:12
B>* 31.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 00:20:56
  *                    via fe80::4638:39ff:fe00:3, swp52, weight 1, 00:20:56
B>* 172.16.0.0/24 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 00:23:16
  *                      via fe80::4638:39ff:fe00:3, swp52, weight 1, 00:23:16
B>* 192.168.0.0/24 [20/0] via fe80::4638:39ff:fe00:1, swp51, weight 1, 00:23:16
  *                       via fe80::4638:39ff:fe00:3, swp52, weight 1, 00:23:16
```
{{< /tab >}}
{{< tab "leaf02 ">}}
Leaf02 has two ECMP routes (via both spine switches) to ESXi03 TEP, Edge virtual uplinks and the BM subnet received by BGP - `10.2.2.0/24`, `192.168.0.0/24`, `30.0.0.0/24`, `31.0.0.0/24`, `172.16.0.0/24`. There are unnecessary prefixed learned, so consider filtering them as needed
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
C * 10.1.1.0/24 [0/1024] is directly connected, vlan100-v0, 00:37:07
C>* 10.1.1.0/24 is directly connected, vlan100, 00:37:07
B>* 10.2.2.0/24 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 00:36:27
  *                    via fe80::4638:39ff:fe00:b, swp52, weight 1, 00:36:27
B>* 30.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 00:22:26
  *                    via fe80::4638:39ff:fe00:b, swp52, weight 1, 00:22:26
B>* 31.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 00:23:09
  *                    via fe80::4638:39ff:fe00:b, swp52, weight 1, 00:23:09
B>* 172.16.0.0/24 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 00:25:26
  *                      via fe80::4638:39ff:fe00:b, swp52, weight 1, 00:25:26
B>* 192.168.0.0/24 [20/0] via fe80::4638:39ff:fe00:9, swp51, weight 1, 00:25:30
  *                       via fe80::4638:39ff:fe00:b, swp52, weight 1, 00:25:30
```
{{< /tab >}}
{{< tab "leaf03 ">}}
Leaf03 has two ECMP routes (via both spine switches) to ESXi01 TEP subnet received by BGP - `10.1.1.0/24`. It has directly connected BM and Edge uplink subnets - `192.168.0.0/24`, `30.0.0.0/24`, and the virtual machines and the peer Edge uplink subnets - `172.16.0.0/24`, `31.0.0.0/24` also received by BGP
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
B>* 10.1.1.0/24 [20/0] via fe80::4638:39ff:fe00:11, swp51, weight 1, 00:39:14
  *                    via fe80::4638:39ff:fe00:13, swp52, weight 1, 00:39:14
C * 10.2.2.0/24 [0/1024] is directly connected, vlan100-v0, 00:39:25
C>* 10.2.2.0/24 is directly connected, vlan100, 00:39:25
C>* 30.0.0.0/24 is directly connected, swp1.300, 00:25:14
B>* 31.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:5e, peerlink.4094, weight 1, 00:25:57
B>* 172.16.0.0/24 [20/0] via 30.0.0.1, swp1.300, weight 1, 00:25:57
C * 192.168.0.0/24 [0/1024] is directly connected, vlan200-v0, 00:28:18
C>* 192.168.0.0/24 is directly connected, vlan200, 00:28:18
```
{{< /tab >}}
{{< tab "leaf04 ">}}
Leaf04 has two ECMP routes (via both spine switches) to ESXi01 TEP subnet received by BGP - `10.1.1.0/24`. It has directly connected BM and Edge uplink subnets - `192.168.0.0/24`, `31.0.0.0/24`, and the virtual machine and the peer Edge uplink subnets - `172.16.0.0/24`, `30.0.0.0/24` also received by BGP.
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
B>* 10.1.1.0/24 [20/0] via fe80::4638:39ff:fe00:19, swp51, weight 1, 00:41:26
  *                    via fe80::4638:39ff:fe00:1b, swp52, weight 1, 00:41:26
C * 10.2.2.0/24 [0/1024] is directly connected, vlan100-v0, 00:41:25
C>* 10.2.2.0/24 is directly connected, vlan100, 00:41:25
B>* 30.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:5d, peerlink.4094, weight 1, 00:27:23
C>* 31.0.0.0/24 is directly connected, swp1.301, 00:28:07
B>* 172.16.0.0/24 [20/0] via 31.0.0.1, swp1.301, weight 1, 00:28:21
C * 192.168.0.0/24 [0/1024] is directly connected, vlan200-v0, 00:29:16
C>* 192.168.0.0/24 is directly connected, vlan200, 00:29:16
```
{{< /tab >}}
{{< tab "spine01 ">}}
Spine01 has all BGP advertised subnets (unnecessary prefixes can be filtered)
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
B>* 10.1.1.0/24 [20/0] via fe80::4638:39ff:fe00:2, swp1, weight 1, 00:45:41
  *                    via fe80::4638:39ff:fe00:a, swp2, weight 1, 00:45:41
B>* 10.2.2.0/24 [20/0] via fe80::4638:39ff:fe00:12, swp3, weight 1, 00:45:10
  *                    via fe80::4638:39ff:fe00:1a, swp4, weight 1, 00:45:10
B>* 30.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:12, swp3, weight 1, 00:31:09
B>* 31.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:1a, swp4, weight 1, 00:31:52
B>* 172.16.0.0/24 [20/0] via fe80::4638:39ff:fe00:12, swp3, weight 1, 00:33:00
  *                      via fe80::4638:39ff:fe00:1a, swp4, weight 1, 00:33:00
B>* 192.168.0.0/24 [20/0] via fe80::4638:39ff:fe00:12, swp3, weight 1, 00:33:01
  *                       via fe80::4638:39ff:fe00:1a, swp4, weight 1, 00:33:01
```
{{< /tab >}}
{{< tab "spine02 ">}}
Spine02 has all BGP advertised subnets (unnecessary prefixes can be filtered)
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
B>* 10.1.1.0/24 [20/0] via fe80::4638:39ff:fe00:4, swp1, weight 1, 00:45:55
  *                    via fe80::4638:39ff:fe00:c, swp2, weight 1, 00:45:55
B>* 10.2.2.0/24 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:45:55
  *                    via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:45:55
B>* 30.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:31:55
B>* 31.0.0.0/24 [20/0] via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:32:38
B>* 172.16.0.0/24 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:33:47
  *                      via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:33:47
B>* 192.168.0.0/24 [20/0] via fe80::4638:39ff:fe00:14, swp3, weight 1, 00:33:48
  *                       via fe80::4638:39ff:fe00:1c, swp4, weight 1, 00:33:48
```
{{< /tab >}}
{{< /tabs >}}

## Traffic Flow

This scenario examines a VM which assigned to a logical segment `VLAN100` in the virtualized world, BM server in `VLAN200` on the underlay network (physical world), and NSX Edge VM located on ESXi03 host. Edge VM is the gateway between the logical and the physical worlds ("north-south" traffic) and uses two logical uplinks in VLANs `30` and `31` which has BGP peering to the underlay leaf switches to route VM-BM traffic.

In this diagram we also have Tier 1 and Tier 0 gateways which are part of the NSX Edge. T1 router has logical downlink into the virtual segment, and a logical uplink to the T0 router. T0 router has logical downlink to T1, and two logical uplinks to the leaf switches in the physical world - `VLAN30`, `VLAN31`. T0 router has the BGP peering with the leaf switches, and by that it advertises the logical segments to the underlaying fabric and receives the physical subnets.

{{<figure src="/images/guides/cumulus-nsxt/edge.jpg">}}

{{%notice note%}}

Links between T1-T0 routers are created automatically by NSX-T/Edge and should be advertised into BGP. Then the undelay fabric will be aware of the virtualized subnets and vice versa.

{{%/notice %}}

{{%notice note%}}

NSX Edge VM has virtual NICs (vNICs) in each of the Overlay and VLAN Transport Zones. It will receive Geneve encapsulated traffic via the TEP device in Overlay TZ (east-west traffic) and forward it to the VLAN TZ by T0 (north-south traffic).

{{%/notice %}}

VM1 `172.16.0.1` on ESXi01 sends traffic to the BM server `192.168.0.1`:

1. The packet reaches the T1 Router as its destination IP address located in different subnet (T1 is logical so the packet is still in ESXi01).
2. T1 examines its routing table to determine the destination path.
3. As BM subnet is `192.168.0.0` received from T0 router, it will be the destination nexthop
4. Local TEP encapsulates the packet into Geneve using VNI `65010` of `VLAN100` segment. As the destination is T0 router, which is on the Edge, the packet sent to it with source-destination IPs of the TEP devices `10.1.1.1`-`10.2.2.1`.
5. Edge TEP, which is part of the Overlay TZ will (and `VLAN100`) decapsulate the packet and forwards it to the T0 router. 
6. T0 router which is part of the underlay VLAN TZ, will examines its routing table to determine the packet's destination.
7. As packet's destination is the BM server in the underlay network (based on BGP advertisements), a regular IP traffic will be sent over the virtual uplinks to `leaf03` and `leaf04` (ECMP) to reach their directly connected BM subnet `192.168.0.0/24`




# Virtualized Environment Over EVPN Fabric

## EVPN underlay Fabric

Not always the virtualized environment deployed over a pure IP underlay (e.g., brownfield). There are cases when VMware environment added to an underlay fabric which uses [Network Virtualization](https://docs.cumulusnetworks.com/cumulus-linux-43/Network-Virtualization/) with [Ethernet Virtual Private Network - EVPN](https://docs.cumulusnetworks.com/cumulus-linux-43/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/). Even though, it still needs to work separately from the underlaying fabric - VM traffic sent only within the virtual world. In that case, the underlaying IP fabric has also VXLAN and EVPN configuration.

From NSX-T virtualized fabric perspective, there is no real difference. When using VXLAN/EVPN underlay fabric, the Geneve packets encapsulated into VXLAN packets on the leaf switches and transmitted over the IP fabric. In other words, the overlay packet is double-encapsulated. Furthermore, when using such deployment, we can set all TEP addresses into same subnet and leverage VXLAN layer 2 stretch over the layer 3 fabric as well. 

{{%notice note%}}

If different TEP devices subnets used in EVPN underlay deployment, VXLAN routing must be done. This requires more complicated VXLAN configuration and won't be covered in this example. For more information check out EVPN [Inter-subnet Routing](https://docs.cumulusnetworks.com/cumulus-linux-43/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/) page.

{{%/notice %}}

{{<figure src="/images/guides/cumulus-nsxt/T1_vxlan.JPG">}}

Switches configuration below based on layer 2 bridging with [VXLAN Active-active Mode](https://docs.cumulusnetworks.com/cumulus-linux-43/Network-Virtualization/VXLAN-Active-Active-Mode/) over BGP-EVPN underlay. 

### TEP VLAN Configuration

As mentioned above, our use-case covers layer 2 VXLAN/EVPN underlay fabric. Therefore, ESXi TEP IPs for all racks are in the same subnet, which means, it is stretched by VXLAN over layer 3 underlay fabric. In that case, TEP VLAN default-gateway is not needed (no SVI nor VRR) as no routing is done on the underlay. Instead, VXLAN interfaces must be configured to map the TEP VLAN to VXLAN VNI. 

VXLAN Tunnel Endpoints (VTEPs) uses local loopback IP address as the tunnel source and destination. For that, loopback interfaces need be configured on all leaf switches and then advertised via BGP. In VXLAN active/active mode (MLAG), `clag vxlan-anycast-ip` must be configured, so the two MLAG peers will have the same virtual tunnel IP address which is used as VXLAN tunnel source. VTEPs are the underlay leaf switches, so spine switches don’t need any VXLAN configuration.

## MLAG and VXLAN Configuration

### MLAG General Configuration 

As we saw in all above use-cases, to create active/active and redundant layer 2 connectivity for the ESXi hypervisors, we use our MLAG protocol. The below Cumulus Linux switches configuration required for any N-VDS uplink profile (active/active or active/standby). 

Cumulus Linux MLAG configuration is done by a single command. It automatically creates the ISL (Inter Switch Link) bond, and configure all MLAG related configuration (bridge, sys-mac, peer-priority, etc.)

{{< tabs "TABID123013 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:01 interface swp49-50 primary backup-ip 192.168.200.12 vrf mgmt
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:01 interface swp49-50 secondary backup-ip 192.168.200.11 vrf mgmt
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:02 interface swp49-50 primary backup-ip 192.168.200.14 vrf mgmt
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add clag peer sys-mac 44:38:39:FF:00:02 interface swp49-50 secondary backup-ip 192.168.200.13 vrf mgmt
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

### Loopback, MLAG and VXLAN Interfaces Configuration - Active/Active LACP LAG N-VDS Uplink Profile

In our scenario, all ESXi physical uplink ports are set with active/active LACP LAG uplink profile. Thus, switch downlink interfaces for ESXi must be bonded into MLAG ports (LACP bonds). 
This action also automatically adds the MLAG interfaces into the bridge and sets them as trunk ports (VLAN tagging) with all VLANs allowed.  

In our case, all logical segments are part of the same overlay TZ. It means that all the virtualized traffic uses the same TEP IP addresses to build Geneve tunnels. Geneve encapsulated packets will be encapsulated again into VXLAN by the VTEPs using the loopback address as the tunnel source IP. 

For non-MLAG uplinks, use interfaces configuration from Pure Virtualized Environment [Switch Ports Configuration - Non-LAG N-VDS Uplink Profile](#switch-ports-configuration---non-lag-n-vds-uplink-profile).

Configure MLAG Ports, Loopbacks and VXLAN interfaces:

{{< tabs "TABIDttii0213 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add clag port bond esxi01 interface swp1 clag-id 1
```
```
cumulus@leaf01:mgmt:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:mgmt:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.1
```
```
cumulus@leaf01:mgmt:~$ net add vxlan vxlan100 vxlan id 100100
cumulus@leaf01:mgmt:~$ net add vxlan vxlan100 vxlan local-tunnelip 10.10.10.1
cumulus@leaf01:mgmt:~$ net add vxlan vxlan100 bridge access 100
cumulus@leaf01:mgmt:~$ net add vxlan vxlan100 bridge arp-nd-suppress on
cumulus@leaf01:mgmt:~$ net add vxlan vxlan100 stp bpduguard
cumulus@leaf01:mgmt:~$ net add vxlan vxlan100 stp portbpdufilter
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add clag port bond esxi01 interface swp1 clag-id 1
```
```
cumulus@leaf02:mgmt:~$ net add loopback lo ip address 10.10.10.2/32
cumulus@leaf02:mgmt:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.1
```
```
cumulus@leaf02:mgmt:~$ net add vxlan vxlan100 vxlan id 100100
cumulus@leaf02:mgmt:~$ net add vxlan vxlan100 vxlan local-tunnelip 10.10.10.2
cumulus@leaf02:mgmt:~$ net add vxlan vxlan100 bridge access 100
cumulus@leaf02:mgmt:~$ net add vxlan vxlan100 bridge arp-nd-suppress on
cumulus@leaf02:mgmt:~$ net add vxlan vxlan100 stp bpduguard
cumulus@leaf02:mgmt:~$ net add vxlan vxlan100 stp portbpdufilter
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add clag port bond esxi03 interface swp1 clag-id 1
```
```
cumulus@leaf03:mgmt:~$ net add loopback lo ip address 10.10.10.3/32
cumulus@leaf03:mgmt:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.2
```
```
cumulus@leaf03:mgmt:~$ net add vxlan vxlan100 vxlan id 100100
cumulus@leaf03:mgmt:~$ net add vxlan vxlan100 vxlan local-tunnelip 10.10.10.3
cumulus@leaf03:mgmt:~$ net add vxlan vxlan100 bridge access 100
cumulus@leaf03:mgmt:~$ net add vxlan vxlan100 bridge arp-nd-suppress on
cumulus@leaf03:mgmt:~$ net add vxlan vxlan100 stp bpduguard
cumulus@leaf03:mgmt:~$ net add vxlan vxlan100 stp portbpdufilter
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add clag port bond esxi03 interface swp1 clag-id 1
```
```
cumulus@leaf04:mgmt:~$ net add loopback lo ip address 10.10.10.4/32
cumulus@leaf04:mgmt:~$ net add loopback lo clag vxlan-anycast-ip 10.0.1.2
```
```
cumulus@leaf04:mgmt:~$ net add vxlan vxlan100 vxlan id 100100
cumulus@leaf04:mgmt:~$ net add vxlan vxlan100 vxlan local-tunnelip 10.10.10.4
cumulus@leaf04:mgmt:~$ net add vxlan vxlan100 bridge access 100
cumulus@leaf04:mgmt:~$ net add vxlan vxlan100 bridge arp-nd-suppress on
cumulus@leaf04:mgmt:~$ net add vxlan vxlan100 stp bpduguard
cumulus@leaf04:mgmt:~$ net add vxlan vxlan100 stp portbpdufilter
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}

### Loopback, MLAG and VXLAN Interfaces Configuration Verification

All switches have a default loopback `lo` interface, the same interface we use as our VXLAN tunnel source. After loopback IP and `clag vxlan-anycast-ip` configuration set, we will see them in this `net show interface` output.  
The created VXLAN interfaces seen below as `vxlanXXX` (which are in layer 2 access mode), and MLAG interfaces `esxi01` and `esxi03` of LACP `802.3ad` type bonds.

{{< tabs "101tr210 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode           LLDP                          Summary
-----  -------------  ---  -----  -------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                     IP: 127.0.0.1/8
       lo                                                                      IP: 10.10.10.1/32
       lo                                                                      IP: 10.0.1.1/32
       lo                                                                      IP: ::1/128
UP     eth0           1G   1500   Mgmt           oob-mgmt-switch (swp10)       Master: mgmt(UP)
       eth0                                                                    IP: 192.168.200.11/24(DHCP)
UP     swp1           1G   9216   BondMember     esxi01 (44:38:39:00:00:32)    Master: esxi01(UP)
UP     swp49          1G   9216   BondMember     leaf02 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember     leaf02 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   BGPUnnumbered  spine01 (swp1)
UP     swp52          1G   9216   BGPUnnumbered  spine02 (swp1)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi01         1G   9216   802.3ad                                      Master: bridge(UP)
       esxi01                                                                  Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                          IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                      Master: bridge(UP)
       peerlink                                                                Bond Members: swp49(UP)
       peerlink                                                                Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   BGPUnnumbered
UP     vxlan100       N/A  9216   Access/L2                                    Master: bridge(UP)
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode           LLDP                          Summary
-----  -------------  ---  -----  -------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                     IP: 127.0.0.1/8
       lo                                                                      IP: 10.10.10.2/32
       lo                                                                      IP: 10.0.1.1/32
       lo                                                                      IP: ::1/128
UP     eth0           1G   1500   Mgmt           oob-mgmt-switch (swp11)       Master: mgmt(UP)
       eth0                                                                    IP: 192.168.200.12/24(DHCP)
UP     swp1           1G   9216   BondMember     esxi01 (44:38:39:00:00:38)    Master: esxi01(UP)
UP     swp49          1G   9216   BondMember     leaf01 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember     leaf01 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   BGPUnnumbered  spine01 (swp2)
UP     swp52          1G   9216   BGPUnnumbered  spine02 (swp2)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi01         1G   9216   802.3ad                                      Master: bridge(UP)
       esxi01                                                                  Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                          IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                      Master: bridge(UP)
       peerlink                                                                Bond Members: swp49(UP)
       peerlink                                                                Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   BGPUnnumbered
UP     vxlan100       N/A  9216   Access/L2                                    Master: bridge(UP)
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode           LLDP                          Summary
-----  -------------  ---  -----  -------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                     IP: 127.0.0.1/8
       lo                                                                      IP: 10.10.10.3/32
       lo                                                                      IP: 10.0.1.2/32
       lo                                                                      IP: ::1/128
UP     eth0           1G   1500   Mgmt           oob-mgmt-switch (swp12)       Master: mgmt(UP)
       eth0                                                                    IP: 192.168.200.13/24(DHCP)
UP     swp1           1G   9216   BondMember     esxi03 (44:38:39:00:00:3e)    Master: esxi03(UP)
UP     swp49          1G   9216   BondMember     leaf04 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember     leaf04 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   BGPUnnumbered  spine01 (swp3)
UP     swp52          1G   9216   BGPUnnumbered  spine02 (swp3)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi03         1G   9216   802.3ad                                      Master: bridge(UP)
       esxi03                                                                  Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                          IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                      Master: bridge(UP)
       peerlink                                                                Bond Members: swp49(UP)
       peerlink                                                                Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   BGPUnnumbered
UP     vxlan100       N/A  9216   Access/L2                                    Master: bridge(UP)
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show interface
State  Name           Spd  MTU    Mode           LLDP                          Summary
-----  -------------  ---  -----  -------------  ----------------------------  ---------------------------
UP     lo             N/A  65536  Loopback                                     IP: 127.0.0.1/8
       lo                                                                      IP: 10.10.10.4/32
       lo                                                                      IP: 10.0.1.2/32       
       lo                                                                      IP: ::1/128
UP     eth0           1G   1500   Mgmt           oob-mgmt-switch (swp13)       Master: mgmt(UP)
       eth0                                                                    IP: 192.168.200.14/24(DHCP)
UP     swp1           1G   9216   BondMember     esxi03 (44:38:39:00:00:44)    Master: esxi03(UP)
UP     swp49          1G   9216   BondMember     leaf03 (swp49)                Master: peerlink(UP)
UP     swp50          1G   9216   BondMember     leaf03 (swp50)                Master: peerlink(UP)
UP     swp51          1G   9216   BGPUnnumbered  spine01 (swp4)
UP     swp52          1G   9216   BGPUnnumbered  spine02 (swp4)
UP     bridge         N/A  9216   Bridge/L2
UP     esxi03         1G   9216   802.3ad                                      Master: bridge(UP)
       esxi03                                                                  Bond Members: swp1(UP)
UP     mgmt           N/A  65536  VRF                                          IP: 127.0.0.1/8
UP     peerlink       2G   9216   802.3ad                                      Master: bridge(UP)
       peerlink                                                                Bond Members: swp49(UP)
       peerlink                                                                Bond Members: swp50(UP)
UP     peerlink.4094  2G   9216   BGPUnnumbered
UP     vxlan100       N/A  9216   Access/L2                                    Master: bridge(UP)
```
{{< /tab >}}
{{< /tabs >}}

### MLAG and VXLAN Interfaces Configuration Verification

As MLAG downlinks bonds to the ESXi hosts, VXLAN interfaces will be active/active on both MLAG peers as well

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
        vxlan100   vxlan100           -         -                      -
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
        vxlan100   vxlan100           -         -                      -
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
        vxlan100   vxlan100           -         -                      -
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
        vxlan100   vxlan100           -         -                      -
```
{{< /tab >}}
{{< /tabs >}}

## BGP Configuration

### BGP IPv4 and EVPN Peerings Establishment 

In addition to the regular underlay IP connectivity based on eBGP, EVPN control-plane must be set to advertise layer 2 subnets over the layer 3 fabric. For that, BGP-EVPN neighbors set by activating the IPv4 neighbors in EVPN address-family 

{{< tabs "101ad3d ">}}
{{< tab "NCLU Commands ">}}
{{< tabs "10gagtg9 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf01:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf01:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf01:mgmt:~$ net add bgp neighbor swp52 remote-as external
```
```
cumulus@leaf01:mgmt:~$ net add bgp evpn neighbor peerlink.4094 activate
cumulus@leaf01:mgmt:~$ net add bgp evpn neighbor swp51 activate
cumulus@leaf01:mgmt:~$ net add bgp evpn neighbor swp52 activate
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf02:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf02:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf02:mgmt:~$ net add bgp neighbor swp52 remote-as external
```
```
cumulus@leaf02:mgmt:~$ net add bgp evpn neighbor peerlink.4094 activate
cumulus@leaf02:mgmt:~$ net add bgp evpn neighbor swp51 activate
cumulus@leaf02:mgmt:~$ net add bgp evpn neighbor swp52 activate
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf03:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf03:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf03:mgmt:~$ net add bgp neighbor swp52 remote-as external
```
```
cumulus@leaf03:mgmt:~$ net add bgp evpn neighbor peerlink.4094 activate
cumulus@leaf03:mgmt:~$ net add bgp evpn neighbor swp51 activate
cumulus@leaf03:mgmt:~$ net add bgp evpn neighbor swp52 activate
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add bgp autonomous-system leaf
cumulus@leaf04:mgmt:~$ net add bgp neighbor peerlink.4094 remote-as external
cumulus@leaf04:mgmt:~$ net add bgp neighbor swp51 remote-as external
cumulus@leaf04:mgmt:~$ net add bgp neighbor swp52 remote-as external
```
```
cumulus@leaf01:mgmt:~$ net add bgp evpn neighbor peerlink.4094 activate
cumulus@leaf04:mgmt:~$ net add bgp evpn neighbor swp51 activate
cumulus@leaf04:mgmt:~$ net add bgp evpn neighbor swp52 activate
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " spine01 ">}}
```
cumulus@spine01:mgmt:~$ net add bgp autonomous-system spine
cumulus@spine01:mgmt:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp2 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp3 remote-as external
cumulus@spine01:mgmt:~$ net add bgp neighbor swp4 remote-as external
cumulus@spine01:mgmt:~$ net add bgp bestpath as-path multipath-relax
cumulus@spine01:mgmt:~$ net add bgp router-id 10.10.10.101
```
```
cumulus@spine01:mgmt:~$ net add bgp evpn neighbor swp1 activate
cumulus@spine01:mgmt:~$ net add bgp evpn neighbor swp2 activate
cumulus@spine01:mgmt:~$ net add bgp evpn neighbor swp3 activate
cumulus@spine01:mgmt:~$ net add bgp evpn neighbor swp4 activate
cumulus@spine01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " spine02 ">}}
```
cumulus@spine02:mgmt:~$ net add bgp autonomous-system spine
cumulus@spine02:mgmt:~$ net add bgp neighbor swp1 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp2 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp3 remote-as external
cumulus@spine02:mgmt:~$ net add bgp neighbor swp4 remote-as external
cumulus@spine02:mgmt:~$ net add bgp bestpath as-path multipath-relax
cumulus@spine02:mgmt:~$ net add bgp router-id 10.10.10.102
```
```
cumulus@spine02:mgmt:~$ net add bgp evpn neighbor swp1 activate
cumulus@spine02:mgmt:~$ net add bgp evpn neighbor swp2 activate
cumulus@spine02:mgmt:~$ net add bgp evpn neighbor swp3 activate
cumulus@spine02:mgmt:~$ net add bgp evpn neighbor swp4 activate
cumulus@spine02:mgmt:~$ net commit
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
leaf01(config-router)# neighbor peerlink.4094 interface remote-as external
leaf01(config-router)# neighbor swp51 remote-as external
leaf01(config-router)# neighbor swp52 remote-as external
```
```
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# neighbor peerlink.4094 activate
leaf01(config-router-af)# neighbor swp51 activate
leaf01(config-router-af)# neighbor swp52 activate
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
leaf02(config-router)# neighbor peerlink.4094 interface remote-as external
leaf02(config-router)# neighbor swp51 remote-as external
leaf02(config-router)# neighbor swp52 remote-as external
```
```
leaf02(config-router)# address-family l2vpn evpn
leaf02(config-router-af)# neighbor peerlink.4094 activate
leaf02(config-router-af)# neighbor swp51 activate
leaf02(config-router-af)# neighbor swp52 activate
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
leaf03(config-router)# neighbor peerlink.4094 interface remote-as external
leaf03(config-router)# neighbor swp51 remote-as external
leaf03(config-router)# neighbor swp52 remote-as external
```
```
leaf03(config-router)# address-family l2vpn evpn
leaf03(config-router-af)# neighbor peerlink.4094 activate
leaf03(config-router-af)# neighbor swp51 activate
leaf03(config-router-af)# neighbor swp52 activate
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
leaf04(config-router)# neighbor peerlink.4094 interface remote-as external
leaf04(config-router)# neighbor swp51 remote-as external
leaf04(config-router)# neighbor swp52 remote-as external
```
```
leaf04(config-router)# address-family l2vpn evpn
leaf04(config-router-af)# neighbor peerlink.4094 activate
leaf04(config-router-af)# neighbor swp51 activate
leaf04(config-router-af)# neighbor swp52 activate
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
spine01(config-router)# bgp router-id 10.10.10.101
spine01(config-router)# neighbor swp1 remote-as external
spine01(config-router)# neighbor swp2 remote-as external
spine01(config-router)# neighbor swp3 remote-as external
spine01(config-router)# neighbor swp4 remote-as external
spine01(config-router)# bgp bestpath as-path multipath-relax
```
```
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
spine02(config-router)# bgp router-id 10.10.10.102
spine02(config-router)# neighbor swp1 remote-as external
spine02(config-router)# neighbor swp2 remote-as external
spine02(config-router)# neighbor swp3 remote-as external
spine02(config-router)# neighbor swp4 remote-as external
spine02(config-router)# bgp bestpath as-path multipath-relax
```
```
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

As VXLAN tunnels created using local loopback addresses (and `clag vxlan-anycast-ip` with MLAG), all the VTEP IPs must be reachable over the undelaying IP fabric. For that, BGP must advertise the local loopbacks and anycast-ip addresses into BGP IPv4 (default) address-family.

For the EVPN control-plane to know which VXLAN VNI belongs to which VTEP, the VNIs previously mapped to VXLAN interfaces (interfaces which also mapped to a VLAN) must be advertised in EVPN address-family. This is done using `advertise-all-vni` command under EVPN.

As stated, as VTEPs are the leaf switches, both above actions needed only on them. Spine switches are only serving as the EVPN control-plane transit path. 

There are two ways to advertise networks into BGP, by `network` command to advertise specifically, or by `redistribute` command to inject subnets into BGP from a non-BGP protocol. In our case we use the redistribute connected command to inject the directly connected routes into BGP. 
This command can be used also with filtering to avoid unwanted/unnecessary subnets get into BGP. For more information and commands. check [Route Filtering and Redistributio](https://docs.cumulusnetworks.com/cumulus-linux-43/Layer-3/Routing/Route-Filtering-and-Redistribution/) page.  

{{< tabs "101rrgss0 ">}}
{{< tab "NCLU Commands ">}}
{{< tabs "1gttt09dd0 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net add bgp redistribute connected
```
```
cumulus@leaf01:mgmt:~$ net add bgp evpn advertise-all-vni
cumulus@leaf01:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net add bgp redistribute connected
```
```
cumulus@leaf02:mgmt:~$ net add bgp evpn advertise-all-vni
cumulus@leaf02:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net add bgp redistribute connected
```
```
cumulus@leaf03:mgmt:~$ net add bgp evpn advertise-all-vni
cumulus@leaf03:mgmt:~$ net commit
```
{{< /tab >}}
{{< tab " leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net add bgp redistribute connected
```
```
cumulus@leaf04:mgmt:~$ net add bgp evpn advertise-all-vni
cumulus@leaf04:mgmt:~$ net commit
```
{{< /tab >}}
{{< /tabs >}}
{{< /tab >}}
{{< tab "vtysh Commands ">}}
{{< tabs "21d0asdasdgtt5 ">}}
{{< tab " leaf01 ">}}
```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# router bgp 
leaf01(config-router)# address-family ipv4 unicast
leaf01(config-router-af)# redistribute connected
```
```
leaf01(config-router)# address-family l2vpn evpn
leaf01(config-router-af)# advertise-all-vni
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
```
```
leaf02(config-router)# address-family l2vpn evpn
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
leaf03(config)# router bgp 
leaf03(config-router)# address-family ipv4 unicast
leaf03(config-router-af)# redistribute connected
```
```
leaf03(config-router)# address-family l2vpn evpn
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
leaf04(config)# router bgp 
leaf04(config-router)# address-family ipv4 unicast
leaf04(config-router-af)# redistribute connected
```
```
leaf04(config-router)# address-family l2vpn evpn
leaf04(config-router-af)# advertise-all-vni
leaf04(config-router-af)# end
leaf04# write memory
leaf04# exit
```
{{< /tab >}}
{{< /tab >}}
{{< /tabs >}}
{{< /tabs >}}

### BGP/EVPN Peerings and VTEP/VNI Advertisement Verification

To verify all BGP IPv4 and EVPN peerings established correctly, use the `net show bgp summary` command in NCLU, or `show ip bgp summary` in `vtysh`

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

Once all BGP IPV4 peerings established, all the redistributed loopback and anycast-ip prefixes should appear in the routing table of each switch. Use `net show route` command in NCLU, or `show ip route` in `vtysh` to check the routing table 

{{< tabs "TAB22sIGTD1631 ">}}
{{< tab "leaf01 ">}}
Leaf01 has two ECMP routes (via both spine switches) to other leaf’s loopbacks and anycast-IPs received by BGP - `10.0.1.2/32`
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
Leaf02 has two ECMP routes (via both spine switches) to other leaf’s loopbacks and anycast-IPs received by BGP - `10.0.1.2/32`
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
Leaf03 has two ECMP routes (via both spine switches) to other leaf’s loopbacks and anycast-IPs received by BGP - `10.0.1.1/32`
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
Leaf04 has two ECMP routes (via both spine switches) to other leaf’s loopbacks and anycast-IPs received by BGP - `10.0.1.1/32`
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
Spine01 has two ECMP routes to each of the anycast-IPs and a single route to each loopback
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

### EVPN Routes and MAC Addresses Population

After EVPN control-plane converged, all TEP IP and MAC addresses should be populated by EVPN across the underlay fabric. That way, all virtualized traffic from ESXi TEPs which is Geneve  encapsulated, sent as layer 2 over layer 3 underlay fabric but with additional VXLAN encapsulation (tunnel in a tunnel). 

{{< tabs "TGTT123 ">}}
{{< tab "leaf01 ">}}
```
cumulus@leaf01:mgmt:~$ net show bridge macs

VLAN      Master  Interface  MAC                TunnelDest   State      Flags               LastSeen
--------  ------  ---------  -----------------  -----------  ---------  ------------------  --------
1         bridge  esxi01     46:38:39:00:00:32                                              00:00:27
1         bridge  esxi01     46:38:39:00:00:38                                              00:00:57
100       bridge  esxi01     44:38:39:00:00:38                                              00:01:03
100       bridge  vxlan100   44:38:39:00:00:44                          extern_learn        00:03:19
untagged          vxlan100   00:00:00:00:00:00  10.0.1.2     permanent  self                00:04:17
untagged          vxlan100   44:38:39:00:00:44  10.0.1.2                self, extern_learn  00:03:19
untagged  bridge  esxi01     44:38:39:00:00:31               permanent                      00:04:50
untagged  bridge  peerlink   44:38:39:00:00:59               permanent                      00:04:50
untagged  bridge  vxlan100   22:0c:97:fd:30:e2               permanent                      00:04:50
```
```
cumulus@leaf01:mgmt:~$ net show bgp evpn route
BGP table version is 2, local router ID is 10.10.10.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
                    Extended Community
Route Distinguisher: 10.10.10.1:2
*> [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                           32768 i
                    ET:8 RT:54795:100100
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                           32768 i
                    ET:8 RT:54795:100100
Route Distinguisher: 10.10.10.3:2
*  [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                               0 4259632649 4200000000 4259632661 i
                    RT:54805:100100 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                               0 4200000000 4259632661 i
                    RT:54805:100100 ET:8
*  [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                               0 4259632649 4200000000 4259632661 i
                    RT:54805:100100 ET:8
*> [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                               0 4200000000 4259632661 i
                    RT:54805:100100 ET:8
Route Distinguisher: 10.10.10.4:2
*  [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                               0 4259632649 4200000000 4259632667 i
                    RT:54811:100100 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                               0 4200000000 4259632667 i
                    RT:54811:100100 ET:8
*  [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                               0 4259632649 4200000000 4259632667 i
                    RT:54811:100100 ET:8
*> [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                               0 4200000000 4259632667 i
                    RT:54811:100100 ET:8

Displayed 6 prefixes (10 paths)
```
{{< /tab >}}
{{< tab "leaf02 ">}}
```
cumulus@leaf02:mgmt:~$ net show bridge macs

VLAN      Master  Interface  MAC                TunnelDest   State      Flags               LastSeen
--------  ------  ---------  -----------------  -----------  ---------  ------------------  --------
1         bridge  esxi01     46:38:39:00:00:32                                              00:01:13
1         bridge  esxi01     46:38:39:00:00:38                                              00:00:02
100       bridge  esxi01     44:38:39:00:00:38                                              00:01:21
100       bridge  vxlan100   44:38:39:00:00:44                          extern_learn        00:04:35
untagged          vxlan100   00:00:00:00:00:00  10.0.1.2     permanent  self                00:05:32
untagged          vxlan100   44:38:39:00:00:44  10.0.1.2                self, extern_learn  00:04:35
untagged  bridge  esxi01     44:38:39:00:00:37               permanent                      00:06:00
untagged  bridge  peerlink   44:38:39:00:00:5a               permanent                      00:06:00
untagged  bridge  vxlan100   6a:f5:8a:e5:2d:61               permanent                      00:06:00
```
```
cumulus@leaf02:mgmt:~$ net show bgp evpn route
BGP table version is 2, local router ID is 10.10.10.2
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
                    Extended Community
Route Distinguisher: 10.10.10.2:2
*> [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                           32768 i
                    ET:8 RT:54793:100100
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                           32768 i
                    ET:8 RT:54793:100100
Route Distinguisher: 10.10.10.3:2
*  [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                               0 4259632651 4200000000 4259632661 i
                    RT:54805:100100 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                               0 4200000000 4259632661 i
                    RT:54805:100100 ET:8
*  [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                               0 4259632651 4200000000 4259632661 i
                    RT:54805:100100 ET:8
*> [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                               0 4200000000 4259632661 i
                    RT:54805:100100 ET:8
Route Distinguisher: 10.10.10.4:2
*  [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                               0 4259632651 4200000000 4259632667 i
                    RT:54811:100100 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                               0 4200000000 4259632667 i
                    RT:54811:100100 ET:8
*  [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                               0 4259632651 4200000000 4259632667 i
                    RT:54811:100100 ET:8
*> [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                               0 4200000000 4259632667 i
                    RT:54811:100100 ET:8

Displayed 6 prefixes (10 paths)
```
{{< /tab >}}
{{< tab "leaf03 ">}}
```
cumulus@leaf03:mgmt:~$ net show bridge macs

VLAN      Master  Interface  MAC                TunnelDest   State      Flags               LastSeen
--------  ------  ---------  -----------------  -----------  ---------  ------------------  --------
1         bridge  esxi03     46:38:39:00:00:3e                                              <1 sec
1         bridge  esxi03     46:38:39:00:00:44                                              00:03:00
100       bridge  esxi03     44:38:39:00:00:44                                              00:05:33
100       bridge  vxlan100   44:38:39:00:00:38                          extern_learn        00:03:17
untagged          vxlan100   00:00:00:00:00:00  10.0.1.1     permanent  self                00:06:31
untagged          vxlan100   44:38:39:00:00:38  10.0.1.1                self, extern_learn  00:03:17
untagged  bridge  esxi03     44:38:39:00:00:3d               permanent                      00:06:55
untagged  bridge  peerlink   44:38:39:00:00:5d               permanent                      00:06:55
untagged  bridge  vxlan100   22:fc:c1:e6:5f:c7               permanent                      00:06:55
```
```
cumulus@leaf03:mgmt:~$ net show bgp evpn route
BGP table version is 3, local router ID is 10.10.10.3
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
                    Extended Community
Route Distinguisher: 10.10.10.1:2
*  [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                               0 4259632667 4200000000 4259632651 i
                    RT:54795:100100 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                               0 4200000000 4259632651 i
                    RT:54795:100100 ET:8
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                               0 4200000000 4259632651 i
                    RT:54795:100100 ET:8
*  [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                               0 4259632667 4200000000 4259632651 i
                    RT:54795:100100 ET:8
Route Distinguisher: 10.10.10.2:2
*  [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                               0 4259632667 4200000000 4259632649 i
                    RT:54793:100100 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                               0 4200000000 4259632649 i
                    RT:54793:100100 ET:8
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                               0 4200000000 4259632649 i
                    RT:54793:100100 ET:8
*  [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                               0 4259632667 4200000000 4259632649 i
                    RT:54793:100100 ET:8
Route Distinguisher: 10.10.10.3:2
*> [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                           32768 i
                    ET:8 RT:54805:100100
*> [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                           32768 i
                    ET:8 RT:54805:100100

Displayed 6 prefixes (10 paths)
```
{{< /tab >}}
{{< tab "leaf04 ">}}
```
cumulus@leaf04:mgmt:~$ net show bridge macs

VLAN      Master  Interface  MAC                TunnelDest   State      Flags               LastSeen
--------  ------  ---------  -----------------  -----------  ---------  ------------------  --------
1         bridge  esxi03     46:38:39:00:00:3e                                              00:00:46
1         bridge  esxi03     46:38:39:00:00:44                                              00:00:01
100       bridge  esxi03     44:38:39:00:00:44                                              00:02:16
100       bridge  vxlan100   44:38:39:00:00:38                          extern_learn        00:04:17
untagged          vxlan100   00:00:00:00:00:00  10.0.1.1     permanent  self                00:07:33
untagged          vxlan100   44:38:39:00:00:38  10.0.1.1                self, extern_learn  00:04:17
untagged  bridge  esxi03     44:38:39:00:00:43               permanent                      00:07:49
untagged  bridge  peerlink   44:38:39:00:00:5e               permanent                      00:07:49
untagged  bridge  vxlan100   4e:3e:3a:d1:77:0e               permanent                      00:07:49
```
```
cumulus@leaf04:mgmt:~$ net show bgp evpn route
BGP table version is 2, local router ID is 10.10.10.4
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
                    Extended Community
Route Distinguisher: 10.10.10.1:2
*  [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                               0 4259632661 4200000000 4259632651 i
                    RT:54795:100100 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                               0 4200000000 4259632651 i
                    RT:54795:100100 ET:8
*  [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                               0 4259632661 4200000000 4259632651 i
                    RT:54795:100100 ET:8
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                               0 4200000000 4259632651 i
                    RT:54795:100100 ET:8
Route Distinguisher: 10.10.10.2:2
*  [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                               0 4259632661 4200000000 4259632649 i
                    RT:54793:100100 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:38]
                    10.0.1.1                               0 4200000000 4259632649 i
                    RT:54793:100100 ET:8
*  [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                               0 4259632661 4200000000 4259632649 i
                    RT:54793:100100 ET:8
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                               0 4200000000 4259632649 i
                    RT:54793:100100 ET:8
Route Distinguisher: 10.10.10.4:2
*> [2]:[0]:[48]:[44:38:39:00:00:44]
                    10.0.1.2                           32768 i
                    ET:8 RT:54811:100100
*> [3]:[0]:[32]:[10.0.1.2]
                    10.0.1.2                           32768 i
                    ET:8 RT:54811:100100

Displayed 6 prefixes (10 paths)
```
{{< /tab >}}
{{< /tabs >}}

### Traffic Flow

Virtualized traffic in same or different logical segments will be sent as in [Layer 2](#layer-2-virtualized-environment) or [Layer 3](#layer-3-virtualized-environment) pure virtualized environments scenarios (if all segments belong to same Overlay TZ with the same TEPs). The only difference in our case, is the EVPN underlay fabric. Here, Geneve encapsuled traffic from ESXi TEP is encapsulated again into VXLAN packets on the ToR switches (VTEP) using the `clag vxlan-anycast-ip` addresses as the tunnel sources/destination. Then it transmitted as layer 2 VXLAN over the layer 3 fabric. Once the VXLAN encapsulated packet reaches its destination VTEP (leaf), it is decapsulated and sent as Geneve to the ESXI hypervisor. The ESXi as we know, decapsulates the Geneve header and forwards the packet to the VM.

## EVPN Underlay Fabric with External Network (Type-5)

{{<figure src="/images/guides/cumulus-nsxt/edge_type5.jpg">}}

There are cases when virtualized traffic is destined to external networks (as we saw in BM scenario), but outside of the EVPN domain. To answer that need, NSX Edge can act as VXLAN-VTEP with BGP-EVPN control-plane. By that, it receives EVPN Type-5 external routs which are used for external traffic routing in EVPN fabrics. 

As mentioned, Edge VM establishes IPv4 BGP peerings with its ToR switches. On top of that, EVPN peerings are set and EVPN control-plane is built. In the above diagram, Edge VM located on ESXi03 hypervisor. It establishes BGP-EVPN peerings with his local `leaf03` and `leaf04` switches. Those leaf switches, which are called "Border Leafs" (EVPN fabric gateway to external networks), are part of the underlay EVPN fabric, and have EVPN type-5 route to the external server. This route is then populated also to the Edge VM.

Edge VM also acts as VXLAN-VTEP, and for that it uses its own loopback interface (which also must be advertised into BGP) as VXLAN tunnel source. By that, it acts the same as the physical switches in VXLAN/EVPN environment. 

Traffic flow from VM1 on ESXi01 to Edge is like the regular virtualized environment over EVPN fabric [Traffic Flow](#traffic-flow-2). In the current case of external server, which is the traffic destination, the difference is in the Edge actions afterwards. Instead of decapsulating the Geneve header received from the other TEP and sending regular IP traffic to the underlay fabric, it encapsulates the traffic into VXLAN packet. Then, the packet sent to its destination VTEP, which is determined by the next-hop of the EVPN type-5 route. In our diagram, packet's destination VTEP are the local ToR switches, which will decapsulate the VXLAN header and send it out of the EVPN domain as regular IP packet. 

That way, virtualized traffic destined to EVPN external networks is sent over EVPN underlay fabric.
