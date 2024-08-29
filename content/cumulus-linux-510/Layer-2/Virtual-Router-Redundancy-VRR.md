---
title: Virtual Router Redundancy - VRR
author: NVIDIA
weight: 510
toc: 3
---
VRR enables hosts to communicate with any redundant switch without reconfiguration by running dynamic router protocols or router redundancy protocols. Redundant switches respond to <span class="a-tooltip">[ARP](## "Address Resolution Protocol")</span> requests from hosts. The switches respond in an identical manner, but if one fails, the other redundant switches continue to respond. You use VRR with <span class="a-tooltip">[MLAG](## "Multi-chassis Link Aggregation")</span>.

Use VRR when you connect multiple devices to a single logical connection, such as an MLAG bond. A device that connects to an MLAG bond believes there is a single device on the other end of the bond and only forwards one copy of the transit frames. If the destination of this frame is the virtual MAC address and you are running VRRP, the frame can go to the link connected to the VRRP standby device, which does not forward the frame to the right destination. With the virtual MAC active on both MLAG devices, either MLAG device handles the frame it receives.

{{%notice note%}}
You cannot configure both VRR and VRRP on the same switch.
{{%/notice%}}

The diagram below illustrates a basic VRR-enabled network configuration.

{{< img src = "/images/cumulus-linux/mlag-dual-connect.png" >}}

The network includes three servers and two Cumulus Linux switches. The switches use {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}}.
- As the bridges in each of the redundant switches connect, they each receive and reply to ARP requests for the virtual router IP address.
- Each ARP request by a server receives replies from each switch; these replies are identical, and the server receiving the replies either ignores replies after the first, or accepts them and overwrites the previous identical reply.
- VRR uses the default fabric-wide MAC address 00:00:5E:00:01:01. If necessary, you can {{<link url="#change-the-vrr-mac-address" text="change the VRR MAC address">}}.

### Configure the Switches

The switches implement the layer 2 network interconnecting the servers and the redundant switches. To configure the switches, add a bridge with the following interfaces to each switch:

- One bond interface or switch port interface to each server. For networks using MLAG, use bond interfaces. Otherwise, use switch port interfaces.
- One or more interfaces to each peer switch. To accommodate higher bandwidth between the switches and to offer link redundancy, multiple inter-peer links are typically bonded interfaces. The VLAN interface must have a unique IP address for both the physical and virtual interface; the switch uses the unique address when it initiates an ARP request.

{{%notice note%}}
Cumulus Linux only supports VRR on an <span class="a-tooltip">[SVI](## "Switched Virtual Interface")</span>. You cannot configure VRR on a physical interface or virtual subinterface.
{{%/notice%}}

The example commands below create a VLAN-aware bridge interface for a VRR-enabled network. The example assumes you have already configured a VLAN-aware bridge with VLAN 10 and that VLAN 10 has an IP address and uses the default fabric-wide VRR MAC address 00:00:5e:00:01:01.

{{< tabs "TabID53 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@switch:~$ nv set interface vlan10 ip vrr state up
cumulus@switch:~$ nv config apply
```

Use the same commands for IPv6 addresses; for example:

```
cumulus@switch:~$ nv set interface vlan10 ip vrr address 2001:db8::1/32
cumulus@switch:~$ nv set interface vlan10 ip vrr state up
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:5e:00:01:01 10.1.10.1/24
    vlan-raw-device br_default
    vlan-id 10
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}
<!-- vale off-->
### Change the VRR MAC Address
<!-- vale on -->

Cumulus Linux sets a fabric-wide MAC address to ensure consistency across VRR switches, which is especially useful in an EVPN multi-fabric environment. If you prefer, you can change the VRR MAC address globally with one NVUE command. You can also override the global setting for a specific VLAN.

To set the VRR MAC address globally with one NVUE command, either:
- Set the fabric-wide VRR MAC address to a value in the reserved range between 00:00:5E:00:01:00 and 00:00:5E:00:01:FF. Be sure to use an address in this reserved range to prevent MAC address conflicts with other interfaces in the same bridged network. 
- Set a fabric ID, from which Cumulus Linux derives the MAC address. You can specify a number between 1 and 255. Cumulus Linux adds the number to the MAC address 00:00:5E:00:01:00 in hex. For example, if you specify 255, the VRR MAC address is 00:00:5E:00:01:FF.

The default VRR MAC address is 00:00:5E:00:01:01, which the switch derives from a fabric ID setting of 1.

To change a VRR MAC address globally on the switch, run the `nv set system global fabric-mac <mac-address>` command:

```
cumulus@switch:mgmt:~$ nv set system global fabric-mac 00:00:5E:00:01:FF
cumulus@switch:mgmt:~$ nv config apply
```

To set a fabric ID, run the `nv set system global fabric-id <number>` command:

```
cumulus@switch:mgmt:~$ nv set system global fabric-id 255
cumulus@switch:mgmt:~$ nv config apply
```

To override the global setting for a specific VLAN, run the `nv set interface <vlan> ip vrr mac-address <mac-address>` command:

```
cumulus@switch:mgmt:~$ nv set interface vlan10 ip vrr mac-address 00:00:5E:00:01:00
cumulus@switch:mgmt:~$ nv config apply
```

To change the VRR MAC address manually, edit the `/etc/network/interfaces` file and update the MAC address in the `address-virtual` line for each VLAN. Cumulus Linux does not provide a fabric ID option in the `/etc/network/interfaces` file.

The following example shows vlan10, vlan20, and vlan30:

```
cumulus@switch:mgmt:~$ sudo nano /etc/network/interfaces
...
auto vlan10
iface vlan10
    address 10.1.10.5/24
    address-virtual 00:00:5E:00:01:FF 10.1.10.1/24
    hwaddress 44:38:39:22:01:c1
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.5/24
    address-virtual 00:00:5E:00:01:FF 10.1.20.1/24
    hwaddress 44:38:39:22:01:c1
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.5/24
    address-virtual 00:00:5E:00:01:FF 10.1.30.1/24
    hwaddress 44:38:39:22:01:c1
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30
...
```

{{%notice note%}}
Make sure to set the same VRR MAC address on both MLAG peers.
{{%/notice%}}

### EVPN Routing with VRR

In an EVPN routing environment, if you want to configure multiple subnets as VRR addresses on a VLAN, you must configure them with the same VRR MAC address.

The following example commands configure both 10.1.10.1/24 and 10.1.11.1/24 on VLAN 10 using the default fabric-wide VRR MAC address 00:00:5e:00:01:01.

{{< tabs "TabID164 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:mgmt:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@switch:mgmt:~$ nv set interface vlan10 ip vrr address 10.1.11.1/24
cumulus@switch:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file; for example:

```
cumulus@switch:mgmt:~$ sudo nano /etc/network/interfaces
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address 10.1.11.2/24
    address-virtual 00:00:5e:00:01:01 10.1.10.1/24 10.1.11.1/24
    hwaddress 44:38:39:22:01:7a
    vlan-raw-device br_default
    vlan-id 10
...
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
To reduce BGP EVPN processing during convergence, NVIDIA recommends that you use the same fabric-wide MAC address across all VLANs and VRR subnets.
{{%/notice%}}

### Configure the Servers

Each server must have two network interfaces. The switches configure the interfaces as bonds running <span class="a-tooltip">[LACP](## "Link Aggregation Control Protocol")</span>; the servers must also configure the two interfaces using teaming, port aggregation, port group, or EtherChannel running LACP. Configure the servers either statically or with DHCP, with a gateway address that is the IP address of the virtual router; this default gateway address never changes.

Configure the links between the servers and the switches in *active-active* mode for <span class="a-tooltip">[FHRP](## "First Hop Redundancy Protocol")</span>.

### Troubleshooting

To verify the configuration on the switch, run the `nv show interface` command:

```
cumulus@leaf01:mgmt:~$ nv show interface
Interface       State  Speed  MTU    Type      Remote Host      Remote Port  Summary                                 
--------------  -----  -----  -----  --------  ---------------  -----------  ----------------------------------------
BLUE            up            65575  vrf                                     IP Address:                  127.0.0.1/8
                                                                             IP Address:                      ::1/128
RED             up            65575  vrf                                     IP Address:                  127.0.0.1/8
                                                                             IP Address:                      ::1/128
bond1           up     1G     9000   bond                                                                            
bond2           up     1G     9000   bond                                                                            
bond3           up     1G     9000   bond                                                                            
br_default      up            9216   bridge                                  IP Address:  fe80::4638:39ff:fe22:17a/64
eth0            up     1G     1500   eth       oob-mgmt-switch  swp10        IP Address:            192.168.200.11/24
                                                                             IP Address:  fe80::4638:39ff:fe22:17a/64
lo              up            65536  loopback                                IP Address:                 10.0.1.12/32
                                                                             IP Address:                10.10.10.1/32
                                                                             IP Address:                  127.0.0.1/8
                                                                             IP Address:                      ::1/128
mgmt            up            65575  vrf                                     IP Address:                  127.0.0.1/8
                                                                             IP Address:                      ::1/128
peerlink        up     2G     9216   bond                                                                            
peerlink.4094   up            9216   sub                                     IP Address: fe80::4ab0:2dff:fed1:e4e1/64
swp1            up     1G     9000   swp 
...
```

### Configuration Example

The following example creates an {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} configuration that incorporates VRR.

{{< tabs "TabID200 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID106 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:mgmt:~$ nv set interface swp1-3,swp49-51
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond member swp1
cumulus@leaf01:mgmt:~$ nv set interface bond2 bond member swp2
cumulus@leaf01:mgmt:~$ nv set interface bond3 bond member swp3
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf01:mgmt:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf01:mgmt:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf01:mgmt:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf01:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf01:mgmt:~$ nv set system global anycast-mac 44:38:39:FF:00:AA
cumulus@leaf01:mgmt:~$ nv set mlag backup 10.10.10.2
cumulus@leaf01:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf01:mgmt:~$ nv set interface vlan20 ip address 10.1.20.2/24
cumulus@leaf01:mgmt:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf01:mgmt:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf01:mgmt:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf01:mgmt:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf01:mgmt:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf01:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ nv set interface lo ip address 10.10.10.2/32
cumulus@leaf02:mgmt:~$ nv set interface swp1-3,swp49-51
cumulus@leaf02:mgmt:~$ nv set interface bond1 bond member swp1
cumulus@leaf02:mgmt:~$ nv set interface bond2 bond member swp2
cumulus@leaf02:mgmt:~$ nv set interface bond3 bond member swp3
cumulus@leaf02:mgmt:~$ nv set interface bond1 bond mlag id 1
cumulus@leaf02:mgmt:~$ nv set interface bond2 bond mlag id 2
cumulus@leaf02:mgmt:~$ nv set interface bond3 bond mlag id 3
cumulus@leaf02:mgmt:~$ nv set interface bond1-3 bridge domain br_default
cumulus@leaf02:mgmt:~$ nv set interface peerlink bond member swp49-50
cumulus@leaf02:mgmt:~$ nv set system global anycast-mac 44:38:39:FF:00:AA
cumulus@leaf02:mgmt:~$ nv set mlag backup 10.10.10.1
cumulus@leaf02:mgmt:~$ nv set mlag peer-ip linklocal
cumulus@leaf02:mgmt:~$ nv set bridge domain br_default vlan 10,20,30
cumulus@leaf02:mgmt:~$ nv set interface vlan10 ip address 10.1.10.3/24
cumulus@leaf02:mgmt:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24
cumulus@leaf02:mgmt:~$ nv set interface vlan10 ip vrr state up
cumulus@leaf02:mgmt:~$ nv set interface vlan20 ip address 10.1.20.3/24
cumulus@leaf02:mgmt:~$ nv set interface vlan20 ip vrr address 10.1.20.1/24
cumulus@leaf02:mgmt:~$ nv set interface vlan20 ip vrr state up
cumulus@leaf02:mgmt:~$ nv set interface vlan30 ip address 10.1.30.2/24
cumulus@leaf02:mgmt:~$ nv set interface vlan30 ip vrr address 10.1.30.1/24
cumulus@leaf02:mgmt:~$ nv set interface vlan30 ip vrr state up
cumulus@leaf02:mgmt:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/nvue.d/startup.yaml">}}

{{< tabs "TabID178 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml 
- set:
    bridge:
      domain:
        br_default:
          vlan:
            10,20,30: {}
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
      eth0:
        ip:
          address:
            dhcp: {}
          vrf: mgmt
        type: eth
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
          vrr:
            address:
              10.1.10.1/24: {}
            enable: on
            state:
              up: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.2/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            enable: on
            state:
              up: {}
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.2/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            enable: on
            state:
              up: {}
        type: svi
        vlan: 30
    mlag:
      backup:
        10.10.10.2: {}
      enable: on
      init-delay: 100
      peer-ip: linklocal
    router:
      vrr:
        enable: on
    service:
      ntp:
        mgmt:
          server:
            0.cumulusnetworks.pool.ntp.org: {}
            1.cumulusnetworks.pool.ntp.org: {}
            2.cumulusnetworks.pool.ntp.org: {}
            3.cumulusnetworks.pool.ntp.org: {}
    system:
      aaa:
        class:
          nvapply:
            action: allow
            command-path:
              /:
                permission: all
          nvshow:
            action: allow
            command-path:
              /:
                permission: ro
          sudo:
            action: allow
            command-path:
              /:
                permission: all
        role:
          nvue-admin:
            class:
              nvapply: {}
          nvue-monitor:
            class:
              nvshow: {}
          system-admin:
            class:
              nvapply: {}
              sudo: {}
        user:
          cumulus:
            full-name: cumulus,,,
            hashed-password: $6$j04yw0gknNcfsUxt$OPF0Z9ilC5IF30kJAaQ5lWEhqk67uAugMvKRomBM8az8hZGbyAKmRdfUJrKCmakKxqdd/sq/smbtkD/xQB8rW.
            role: system-admin
      api:
        state: enabled
      config:
        auto-save:
          enable: on
      control-plane:
        acl:
          acl-default-dos:
            inbound: {}
          acl-default-whitelist:
            inbound: {}
      global:
        anycast-mac: 44:38:39:FF:00:AA
        fabric-mac: 00:00:5E:00:01:01
        system-mac: 44:38:39:22:01:7a
      hostname: leaf01
      reboot:
        mode: cold
      ssh-server:
        state: enabled
      wjh:
        channel:
          forwarding:
            trigger:
              l2: {}
              l3: {}
              tunnel: {}
        enable: on
```

{{< /tab >}}
{{< tab "leaf02 ">}}

```
cumulus@leaf02:mgmt:~$ sudo cat /etc/nvue.d/startup.yaml
- set:
    bridge:
      domain:
        br_default:
          vlan:
            10,20,30: {}
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
      eth0:
        ip:
          address:
            dhcp: {}
          vrf: mgmt
        type: eth
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
          vrr:
            address:
              10.1.10.1/24: {}
            enable: on
            state:
              up: {}
        type: svi
        vlan: 10
      vlan20:
        ip:
          address:
            10.1.20.3/24: {}
          vrr:
            address:
              10.1.20.1/24: {}
            enable: on
            state:
              up: {}
        type: svi
        vlan: 20
      vlan30:
        ip:
          address:
            10.1.30.3/24: {}
          vrr:
            address:
              10.1.30.1/24: {}
            enable: on
            state:
              up: {}
        type: svi
        vlan: 30
    mlag:
      backup:
        10.10.10.1: {}
      enable: on
      init-delay: 100
      peer-ip: linklocal
    router:
      vrr:
        enable: on
    service:
      ntp:
        mgmt:
          server:
            0.cumulusnetworks.pool.ntp.org: {}
            1.cumulusnetworks.pool.ntp.org: {}
            2.cumulusnetworks.pool.ntp.org: {}
            3.cumulusnetworks.pool.ntp.org: {}
    system:
      aaa:
        class:
          nvapply:
            action: allow
            command-path:
              /:
                permission: all
          nvshow:
            action: allow
            command-path:
              /:
                permission: ro
          sudo:
            action: allow
            command-path:
              /:
                permission: all
        role:
          nvue-admin:
            class:
              nvapply: {}
          nvue-monitor:
            class:
              nvshow: {}
          system-admin:
            class:
              nvapply: {}
              sudo: {}
        user:
          cumulus:
            full-name: cumulus,,,
            hashed-password: $6$/jEbjL96YZO24NK/$3H1mMl1S1Udxcv9l4jQUXFgZN2bVAxEaDLLzy.dbpHjH80TIq0YhTbCMG.Y0p5s7wtUIEHrWaaBaBRsfSkKwM/
            role: system-admin
      api:
        state: enabled
      config:
        auto-save:
          enable: on
      control-plane:
        acl:
          acl-default-dos:
            inbound: {}
          acl-default-whitelist:
            inbound: {}
      global:
        anycast-mac: 44:38:39:FF:00:AA
        fabric-mac: 00:00:5E:00:01:01
        system-mac: 44:38:39:22:01:78
      hostname: leaf02
      reboot:
        mode: cold
      ssh-server:
        state: enabled
      wjh:
        channel:
          forwarding:
            trigger:
              l2: {}
              l3: {}
              tunnel: {}
        enable: on
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "/etc/network/interfaces">}}

{{< tabs "TabID190 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:mgmt:~$ sudo cat /etc/network/interfaces
...
auto lo
iface lo inet loopback
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
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.2
    clagd-sys-mac 44:38:39:FF:00:AA
    clagd-args --initDelay 100
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
auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:5e:00:01:00 10.1.10.1/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:5e:00:01:00 10.1.20.1/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 20
auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:5e:00:01:00 10.1.30.1/24
    hwaddress 44:38:39:22:01:b1
    vlan-raw-device br_default
    vlan-id 30
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
cumulus@leaf02:mgmt:~$ sudo cat /etc/network/interfaces
...
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
auto peerlink
iface peerlink
    bond-slaves swp49 swp50
    bond-mode 802.3ad
    bond-lacp-bypass-allow no
auto peerlink.4094
iface peerlink.4094
    clagd-peer-ip linklocal
    clagd-backup-ip 10.10.10.1
    clagd-sys-mac 44:38:39:FF:00:AA
    clagd-args --initDelay 100
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
auto vlan10
iface vlan10
    address 10.1.10.3/24
    address-virtual 00:00:5e:00:01:00 10.1.10.1/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 10
auto vlan20
iface vlan20
    address 10.1.20.3/24
    address-virtual 00:00:5e:00:01:00 10.1.20.1/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 20
uto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:5e:00:01:00 10.1.30.1/24
    hwaddress 44:38:39:22:01:af
    vlan-raw-device br_default
    vlan-id 30
auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 peerlink
    hwaddress 44:38:39:22:01:af
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
```

{{< /tab >}}
{{< tab "server01 ">}}

```
cumulus@server01:mgmt:~$ sudo cat /etc/network/interfaces
...
auto eth0
iface eth0 inet dhcp
  post-up sysctl -w net.ipv6.conf.eth0.accept_ra=2

auto eth1
iface eth1

auto eth2
iface eth2

auto bond1
iface bond1
 bond-miimon 100
 bond-mode 802.3ad
 bond-min-links 1
 bond-slaves eth1 eth2
 post-up ip route add 10.0.0.0/8 via 10.1.20.1

auto bond1.10
iface bond1.10
 address 10.1.10.101/24

auto bond1.20
iface bond1.20
 address 10.1.20.101/24

auto bond1.30
iface bond1.30
 address 10.1.30.101/24
```

{{< /tab >}}
{{< tab "server02 ">}}

```
cumulus@server02:mgmt:~$ sudo cat /etc/network/interfaces
...
auto eth0
iface eth0 inet dhcp
  post-up sysctl -w net.ipv6.conf.eth0.accept_ra=2

auto eth1
iface eth1

auto eth2
iface eth2

auto bond1
iface bond1
bond-miimon 100
 bond-mode 802.3ad
 bond-min-links 1
 bond-slaves eth1 eth2
 post-up ip route add 10.0.0.0/8 via 10.1.20.1

auto bond1.10
iface bond1.10
 address 10.1.10.102/24

auto bond1.20
iface bond1.20
 address 10.1.20.102/24

auto bond1.30
iface bond1.30
 address 10.1.30.102/24
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Try It " >}}
    {{< simulation name="Try It CL510 - VRR" showNodes="leaf01,leaf02,server01,server02" >}}

The simulation is pre-configured using {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/NVIDIA-User-Experience-NVUE/" text="NVUE">}} commands.

To validate the configuration, run the `nv show interface <vlan> ip vrr` command:

```
cumulus@leaf02:mgmt:~$ nv show interface vlan10 ip vrr
             operational        applied            description
-----------  -----------------  -----------------  ------------------------------------------------------
enable                          on                 Turn the feature 'on' or 'off'.  The default is 'off'.
mac-address  00:00:5e:00:01:00  00:00:5e:00:01:00  Override anycast-mac
mac-id                          none               Override anycast-id
[address]    10.1.10.1/24       10.1.10.1/24       Virtual addresses with prefixes
state        up                 up                 The state of the interface
```

{{< /tab >}}
{{< /tabs >}}
