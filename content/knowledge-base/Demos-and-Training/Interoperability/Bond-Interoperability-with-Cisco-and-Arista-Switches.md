---
title: Bond Interoperability with Cisco and Arista Switches
author: NVIDIA
weight: 512
toc: 4
---

This knowledge base article discusses interoperability and troubleshooting in a mixed switch topology, featuring switches running Cumulus Linux on the same network as switches running Cisco and Arista network OSes. The article uses the syntax of `ifupdown2`.

## Environment

- Cumulus Linux 2.1 and later

## Example Mixed Switch Topology

The three examples described below use the following diagram, with all testing performed on actual equipment. Both sides use the same interfaces; for example, swp19 (switch port 19) on the Cumulus Linux switch connects to g0/19 (Gigabit Ethernet 0/19) on the Cisco 3560.

{{<img src="/images/knowledge-base/cisco-bond-interop-lab-setup.png">}}

## Cumulus Linux and Cisco IOS

The following example utilizes slow LACPDUs (that is, `bond-lacp-rate` is set to 0):

| Quanta LY2 w/Cumulus Linux 4.2.0 | Cisco WS-C3560X-24 12.2(55)SE5 |
| -------------------------------- | ------------------------------ |
| <pre>auto bond1<br><br>iface bond1<br>    bond-slaves glob swp19-20<br>    bond-miimon 100<br>    bond-min-links 1<br>    bond-mode 802.3ad<br>    bond-xmit-hash-policy layer3+4 bond-lacp-rate 0<br><br>auto vlan10<br>iface vlan10<br>    bridge-ports bond1.10<br>    address 10.10.10.11/24<br>    bridge-stp on</pre> | <pre>vlan 10<br><br>interface GigabitEthernet0/19<br> switchport trunk encapsulation dot1q switchport mode trunk channel-group 1 mode active interface GigabitEthernet0/20 switchport trunk encapsulati on dot1q switchport mode trunk channel-group 1 mode active<br><br>interface Port-channel1<br> switchport trunk encapsulation dot1q switchport mode trunk<br><br>interface Vlan10<br> ip address 10.10.10.10 255.2</pre> |

## Cumulus Linux and Arista EOS

The following example utilizes fast LACPDUs (where `bond-lacp-rate` is set to 1):

| Quanta LY2 w/Cumulus Linux 4.2.0 | Arista DCS-7148S-R 4.13.5F |
| -------------------------------- | -------------------------- |
| <pre>auto bond2<br><br>iface bond2<br>    bond-slaves glob swp37-38<br>    bond-miimon 100<br>    bond-min-links 1<br>    bond-mode 802.3ad<br>    bond-xmit-hash-policy layer3+4 bond-lacp-rate 1<br><br>auto vlan12<br>iface vlan12<br>    bridge_ports bond2.12<br>    address 12.12.12.11/24<br>    bridge-stp on</pre> | <pre>interface Ethernet37<br><br>   switchport mode trunk<br>   channel-group 2 mode active interface Ethernet38 switchport mode trunk channel-group 2 mode active<br><br>interface Port-Channel2<br>   switchport trunk allowed vlan 12 switchport mode trunk<br><br>interface Vlan12<br>   ip address 12.12.12.12/24</pre> |
<!-- vale off -->
## Cumulus Linux and Cisco NX-OS
<!-- vale on -->
The following example utilizes fast LACPDUs (where `bond-lacp-rate` is set to 1):

| Quanta LY2 w/Cumulus Linux 4.2.0 | Cisco Nexus3064 5.0(3)U2(2c) |
| -------------------------------- | ---------------------------- |
| <pre>auto bond3<br><br>iface bond3<br>    bond-slaves glob swp39-40<br>    bond-miimon 100<br>    bond-min-links 1<br>    bond-mode 802.3ad<br>    bond-xmit-hash-policy layer3+4 bond-lacp-rate 1<br><br>auto vlan14<br>iface vlan14<br>    bridge-ports bond3.14<br>    address 14.14.14.11/24<br>    bridge-stp on</pre> | <pre>feature interface-vlan<br>feature lacp<br><br>vlan 14<br><br>interface Ethernet1/39<br>  switchport mode trunk<br>  channel-group 3 mode active<br>interface Ethernet1/40<br>  switchport mode trunk<br>  channel-group 3 mode active<br><br>interface port-channel3<br>  switchport mode trunk<br><br>interface Vlan14<br> no shutdown<br> ip address 14.14.14.14/24</pre> |

## Troubleshooting Bond/EtherChannel/LACP Links

The three most common problems with EtherChannels are:

- VLAN mismatches with layer 2 bonds
- Fast vs slow LACP rate of LACPDUs
- Both sides using passive LACP mode instead of active LACP mode

Because Cumulus Linux is Linux, it utilizes the same kernel syntax for bonds that you can find in the {{<exlink url="https://www.kernel.org/doc/Documentation/networking/bonding.txt" text="kernel.org documentation">}}. The [Cumulus Linux bonding documentation]({{<ref "/cumulus-linux-43/Layer-2/Bonding-Link-Aggregation" >}}) contains specific examples. The following guide compares the Cisco 3560 to the Quanta LY2 in the diagram and configuration above.

### Bond Parameters

Here is the recommended way to configure a bond in Cumulus Linux:

    auto bond0
    iface bond0
        bond-slaves swp1 swp2
        bond-mode 802.3ad
        bond-miimon 100
        bond-lacp-rate 1
        bond-min-links 1
        bond-xmit-hash-policy layer3+4

- `bond-slaves` equates to the members of the bond. In this case, swp1 and swp2 are members of bond0; LACP bonds require`bond-mode` 802.3ad.
- `bond-miimon 100` is the failure inspection frequency. The default value is 0, but NVIDIA recommends 100.
- `bond-lacp-rate 1` means fast LACP, see {{<link url="#fast-vs-slow-lacp-rates" text="Fast vs Slow LACP Rates">}} below; NVIDIA recommends using fast LACP.
- `bond-min-links` is an integer indicating the number of links that must be up for the bond to become active.
- `bond-xmit-hash-policy` must be set to layer3+4 so it is evenly distributed.

To read more information about the bond parameters, read the {{<exlink url="https://www.kernel.org/doc/Documentation/networking/bonding.txt" text="kernel.org documentation">}}.

### VLAN Mismatch

The following configuration has a VLAN mismatch. Can you find it?

| Quanta LY2 w/Cumulus Linux 4.2.0 | Cisco WS-C3560X-24 12.2(55)SE5 |
| -------------------------------- | ------------------------------ |
| <pre>auto bond1<br>iface bond1<br>    bond-slaves glob swp19-20<br>    bond-miimon 100<br>    bond-min-links 1<br>    bond-mode 802.3ad<br>    bond-xmit-hash-policy layer3+4 bond-lacp-rate 0<br><br>auto vlan10<br>iface vlan10<br>    bridge-ports bond1.100<br>    address 10.10.10.11/24<br>    bridge-stp on</pre> | <pre>vlan 10<br><br>interface GigabitEthernet0/19<br> switchport trunk encapsulation dot1q switchport mode trunk channel-group 1 mode active interface GigabitEthernet0/20 switchport trunk encapsulation dot1q switchport mode trunk channel-group 1 mode active<br><br>interface Port-channel1<br> switchport trunk encapsulation dot1q switchport mode trunk<br><br>interface Vlan10<br> ip address 10.10.10.10 255.255.255.0</pre> |

As illustrated above, the bridge called *vlan10* indicates the member of this bridge is bond1.100. The name *vlan10* does not mean that you have to tag the bridge members with *vlan10*. The name has nothing to do with what 802.1q tags are within the bridge. The subinterface .100 (bond1.100) indicates that tagged ingress packets become a member of VLAN 100, but in a bridge named *vlan10*. This syntax is correct but might not be the result you want. You could name the bridge anything, such as *mgmt-bridge*, or *outofband*.

Unlike Cisco IOS, Cumulus Linux drops packets unless you join the tagged subinterface to a bridge or layer 3 interface. Many IOS and IOS-look-alikes do something like this:

    switchport trunk allowed vlan 5

This allows only vlan5 and nothing else. Cumulus Linux does the opposite, where it drops everything unless it allows it in.

You can find more information on configuring VLAN tagging in the [Cumulus Linux user guide]({{<ref "/cumulus-linux-43/Layer-2/Ethernet-Bridging-VLANs" >}}).

### Fast vs Slow LACP Rates

The Cumulus Linux documentation recommends:

    bond-lacp-rate 1

This means *fast*; according to the {{<exlink url="https://www.kernel.org/doc/Documentation/networking/bonding.txt" text="kernel.org documentation">}}, it means "Request partner to transmit LACPDUs every 1 second."

In some cases, the other vendor cannot perform fast LACPDUs or there might be some other unknown requirement requiring slow LACP. To configure slow rate, use:

    bond-lacp-rate 0

According to kernel.org, this means "Request partner to transmit LACPDUs every 30 seconds."

### Troubleshooting Fast vs Slow

To see a bond configuration and what it runs, use this command:

    cat /proc/net/bonding/bond1

The following output is a snippet of the information received:

    cumulus@switch:~$ cat /proc/net/bonding/bond1
    Ethernet Channel Bonding Driver: v3.7.1 (April 27, 2011)

    Bonding Mode: IEEE 802.3ad Dynamic link aggregation
    Transmit Hash Policy: layer3+4 (1)
    MII Status: up
    MII Polling Interval (ms): 100
    Up Delay (ms): 0
    Down Delay (ms): 0

    802.3ad info
    LACP rate: slow

On the Cisco switch, you check the port channel like this:

    show etherchannel summary

The following output is a snippet of the information received:

    Group  Port-channel  Protocol    Ports
    ------+-------------+-----------+-----------------------------------------------
    1      Po1(SU)         LACP      Gi0/19(P)   Gi0/20(P)

Notice that the port channel is up on both ports and looks good. To see the LACPDU's speed on the Cisco side, run the following command:

    show etherchannel detail

The following output is a snippet of the information received:

    Local information:
                                LACP port     Admin     Oper    Port        Port
    Port      Flags   State     Priority      Key       Key     Number      State
    Gi0/19    SA      bndl      32768         0x1       0x1     0x114       0x3D

    Partner's information:

                      LACP port                        Admin  Oper   Port    Port
    Port      Flags   Priority  Dev ID          Age    key    Key    Number  State
    Gi0/19    SA      255       089e.01ce.e216   3s    0x0    0x11   0x1     0x3D

Where the *SA* flags mean:

    A - Device is in active mode
    S - Device is sending Slow LACPDUs

Making sure both sides match is imperative for traffic to pass and the bond to stay up and be stable. In the case above, they were both utilizing slow LACPDUs. The following table helps you match:

| Cumulus Linux   | Cisco | Rate             |
| --------------- |------ | ---------------- |
| LACP rate: slow | S     | every 30 seconds |
| LACP rate: fast | F     | every second     |

### Active vs Passive Modes

Cumulus Linux does not currently support passive mode. Because active mode works with active and passive configurations, and Cumulus Linux does not have a knob to change it, there is no interoperability issue between switches running Cumulus Linux and switches from other network OS vendors.
