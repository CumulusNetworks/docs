---
title: Virtual Routing and Forwarding - VRF
author: NVIDIA
weight: 430
product: SONiC
version: 202012
siteSlug: sonic
---

*Virtual routing and forwarding* (VRF) provides for the presence of multiple independent routing tables working simultaneously on the same router or switch. This provides for multiple network paths without the need for multiple switches. VRFs are like VLANs for layer 3. But unlike VLANs, there is no field in the IP header carrying it.

The primary use cases for VRFs in a data center are similar to VLANs at layer 2: using common physical infrastructure to carry multiple isolated traffic streams for multi-tenant environments, where these streams are allowed to cross over only at configured boundary points, typically firewalls or IDS. You can also use it to burst traffic from private clouds to enterprise networks where the burst point is at layer 3.

VRF is fully supported in the Linux kernel, so it has the following characteristics:

- The VRF is presented as a layer 3 master network device with its own associated routing table.
- The layer 3 interfaces (VLAN interfaces, bonds, switch virtual interfaces/SVIs) associated with the VRF are enslaved to that VRF; IP rules direct FIB (forwarding information base) lookups to the routing table for the VRF device.
- The VRF device can have its own IP address, known as a VRF-local loopback.
- Applications can use existing interfaces to operate in a VRF context by binding sockets to the VRF device or passing the ifindex using cmsg. By default, applications on the switch run against the default VRF. Services started by systemd run in the default VRF unless the VRF instance is used. When management VRF is enabled, logins to the switch default to the management VRF. This is a convenience so that you do not have to specify management VRF for each command. Management VRF is enabled by default in Cumulus Linux.
- Listen sockets used by services are VRF-global by default unless the application is configured to use a more limited scope (see services in the management VRF). Connected sockets (like TCP) are then bound to the VRF domain in which the connection originates. The kernel provides a sysctl that allows a single instance to accept connections over all VRFs. For TCP, connected sockets are bound to the VRF on which the first packet is received. This sysctl is enabled for Cumulus Linux.
- Connected and local routes are placed in appropriate VRF tables.
- Neighbor entries continue to be per-interface, and you can view all entries associated with the VRF device.
- A VRF does not map to its own network namespace; however, you can nest VRFs in a network namespace.
- You can use existing Linux tools, such as tcpdump, to interact with a VRF.

## Configure a VRF 

By default, all layer 3 interfaces are placed in the default VRF. This command is used to bind an interface to a VRF. The VRF name must always start with *Vrf*.

{{<tabs "VRF">}}

{{<tab "SONiC CLI">}}

Create the VRF:

    admin@leaf01:~$ sudo config vrf add VrfHedgehog

Then bind some interfaces to the VRF:

    admin@switch:~$ sudo config interface vrf bind VrfHedgehog
    admin@switch:~$ sudo config interface vrf bind Ethernet24 VrfHedgehog

{{</tab>}}

{{<tab "config_db.json">}}

Configure the VRF in the VRF table in `/etc/sonic/config_db.json`. Bind interfaces to the VRF by specifying the VRF name for the interface in the INTERFACE table.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

   "INTERFACE": {
   ...
        "Ethernet24": {
            "vrf_name": "VrfHedgehog"
        },
   ...
    "VRF": {
        "VrfHedgehog": {}
    }
    ...
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

To see the VRFs configured on the switch, and the interfaces bound to them, run:

```
admin@switch:~$ show vrf
VRF          Interfaces
-----------  ------------
VrfHedgehog  Ethernet24
```

## Management VRF

*Management VRF* is a subset of VRF that provides a separation between the out-of-band management network and the in-band data plane network. For all VRFs, the main routing table is the default table for all of the data plane switch ports. With management VRF, a second table called *mgmt* is used for routing through the Ethernet ports of the switch. FIB rules are installed for DNS servers because this is the typical deployment case.

SONiC only supports eth0 (or eth1, depending on the switch platform) for out-of-band management. The Ethernet ports are software-only ports that are not hardware accelerated by switchd. VLAN subinterfaces, bonds, bridges, and the front panel switch ports are not supported as OOB management interfaces.

When you enable the management VRF on a switch, the `interfaces-config` service restarts, which in turn regenerates the `/etc/network/interfaces` file and restarts the `networking` service. This creates a new interface and `l3mdev` CGROUP with the name as *mgmt* and enslaves the management interface *eth0* into this master interface *mgmt*.

The management VRF is not enabled by default.

{{%notice note%}}

Note that the VRF names *mgmt* and *management* are reserved for the management VRF; data plane VRFs should not use either of these reserved VRF names.

{{%/notice%}}

To configure the management interface:

{{<tabs "MgmtVRF">}}

{{<tab "SONiC CLI">}}

    admin@switch:~$ sudo config vrf add mgmt

{{</tab>}}

{{<tab "config_db.json">}}

Configure the management VRF in the MGMT_VRF_CONFIG table in `/etc/sonic/config_db.json`.

```
admin@switch:~$ sudo vi /etc/sonic/config_db.json

 "MGMT_VRF_CONFIG": {
        "vrf_global": {
            "mgmtVrfEnabled": "true"
        }
    },
    ...
}
```

{{</tab>}}

{{</tabs>}}

Save your changes to the configuration:

    admin@switch:~$ sudo config save -y

To disable the management VRF, run `config vrf del mgmt`. This command restarts the `interfaces-config` service which in turn regenerates the `/etc/network/interfaces` file and restarts the `networking` service. It also deletes the interface *mgmt*, deletes the `l3mdev` CGROUP named *mgmt* and returns the management interface eth0 into the default VRF.

    admin@switch:~$ sudo config vrf del mgmt
    admin@switch:~$ sudo config save -y

### Management VRF Show commands

The `show mgmt-vrf` command indicates whether or not the management VRF is enabled. It also displays the details about the the links (eth0, mgmt, lo-m) that are related to management VRF.

```
admin@switch:~$ show mgmt-vrf 
ManagementVRF : Enabled

Management VRF interfaces in Linux:
304: mgmt: <NOARP,MASTER,UP,LOWER_UP> mtu 65536 qdisc noqueue state UP mode DEFAULT group default qlen 1000
    link/ether 2e:82:3b:b8:1c:77 brd ff:ff:ff:ff:ff:ff promiscuity 0
    vrf table 5000 addrgenmode eui64 numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master mgmt state UP mode DEFAULT group default qlen 1000
    link/ether 44:38:39:00:01:7a brd ff:ff:ff:ff:ff:ff
305: lo-m: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue master mgmt state UNKNOWN mode DEFAULT group default qlen 1000
    link/ether 02:ed:a2:eb:ba:90 brd ff:ff:ff:ff:ff:ff
```

{{%notice tip%}}

The management interface eth0 shows the `master` as `mgmt` since it is part of management VRF.

{{%/notice%}}

The `show mgmt-vrf routes` command displays the routes that are present in the routing table 5000, which is dedicated to the management VRF.

```
admin@switch:~$ show mgmt-vrf routes

Routes in Management VRF Routing Table:
default via 192.168.200.1 dev eth0
broadcast 127.0.0.0 dev lo-m proto kernel scope link src 127.0.0.1
127.0.0.0/8 dev lo-m proto kernel scope link src 127.0.0.1
local 127.0.0.1 dev lo-m proto kernel scope host src 127.0.0.1
broadcast 127.255.255.255 dev lo-m proto kernel scope link src 127.0.0.1
broadcast 192.168.200.0 dev eth0 proto kernel scope link src 192.168.200.11
192.168.200.0/24 dev eth0 proto kernel scope link src 192.168.200.11
local 192.168.200.11 dev eth0 proto kernel scope host src 192.168.200.11
broadcast 192.168.200.255 dev eth0 proto kernel scope link src 192.168.200.11
```

The `show management_interface address` command displays the IP addresses configured for the management interface eth0 and the management network default gateway.

    admin@switch:~$ show management_interface address 
    Management IP address = 10.16.210.75/24
    Management NetWork Default Gateway = 10.16.210.254
    Management IP address = FC00:2::32/64
    Management Network Default Gateway = fc00:2::1
