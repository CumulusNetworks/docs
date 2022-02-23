---
title: GRE Tunneling
author: NVIDIA
weight: 970
toc: 3
---
[GRE](## "Generic Routing Encapsulation") is a tunneling protocol that encapsulates network layer protocols inside virtual point-to-point links over an Internet Protocol network. The tunnel source and tunnel destination addresses on each side identify the two endpoints.

GRE packets travel directly between the two endpoints through a virtual tunnel. As a packet comes across other routers, there is no interaction with its payload; the routers only parse the outer IP packet. When the packet reaches the endpoint of the GRE tunnel, the switch de-encapsulates the outer packet, parses the payload, then forwards it to its ultimate destination.

GRE uses multiple protocols over a single-protocol backbone and is less demanding than some of the alternative solutions, such as VPN. You can use GRE to transport protocols that the underlying network does not support, work around networks with limited hops, connect non-contiguous subnets, and allow VPNs across wide area networks.

{{%notice note%}}
- You can use only static IPv4 routes as a destination for the tunnel interface.
- You can only configure IPv4 endpoints.
- You can only configure point to point GRE tunnels; only one remote tunnel per interface.
- You cannot configure two tunnels with same local and remote tunnel IP addresses.
- GRE tunneling cannot coexist with VXLAN or MPLS on the switch.
- Cumulus Linux supports a maximum of 256 GRE tunnels.
{{%/notice%}}

The following example shows two sites that use IPv4 addresses. Using GRE tunneling, the two end points can encapsulate an IPv4 or IPv6 payload inside an IPv4 packet. The switch routes the packet based on the destination in the outer IPv4 header.

{{< img src = "/images/cumulus-linux/gre-tunnel-example.png" >}}

## Configure GRE Tunneling

To configure GRE tunneling, you create a GRE tunnel interface with routes for tunneling on both endpoints as follows:

- Create a tunnel interface by specifying an interface name, the tunnel mode as `gre`, the source (local) and destination (remote) underlay IP address, and the `ttl` (optional).
- Assign an IP address to the tunnel interface.
- Add route entries to encapsulate the packets using the tunnel interface.

The following configuration example shows the commands used to set up a bidirectional GRE tunnel between two endpoints: `tunnelR1` and `tunnelR2`. The local tunnel endpoint for `tunnelR1` is 10.10.10.1 and the remote endpoint is 10.10.10.3. The local tunnel endpoint for `tunnelR2` is 10.10.10.3 and the remote endpoint is 10.10.10.1.

{{< img src = "/images/cumulus-linux/gre-tunnel-config1.png" >}}

{{%notice note%}}
In NVUE, if you create a the GRE interface with a name that starts with `tunnel`, NVUE automatically sets the interface type to `tunnel`. If you create a GRE interface with a name that does *not* start with `tunnel`, you must set the interface type to `tunnel` with the `nv set interface <interface-name> type tunnel` command.
{{%/notice%}}

{{< tabs "TabID35 ">}}
{{< tab "NVUE Commands">}}

{{< tabs "TabID38 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp1 ip address 10.2.1.1/24
cumulus@leaf01:~$ nv set interface tunnelR2 ip address 10.1.100.1/30
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel mode gre
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel dest-ip 10.10.10.3
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel source-ip 10.10.10.1
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel ttl 255
cumulus@leaf01:~$ nv set vrf default router static 10.1.1.0/24 via tunnelR2
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface lo ip address 10.10.10.3/32
cumulus@leaf03:~$ nv set interface swp1 ip address 10.1.1.1/24
cumulus@leaf03:~$ nv set interface tunnelR1 ip address 10.1.100.2/30
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel mode gre
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel dest-ip 10.10.10.1
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel source-ip 10.10.10.3
cumulus@leaf03:~$ nv set interface tunnelR1 tunnel ttl 255
cumulus@leaf03:~$ nv set vrf default router static 10.2.1.0/24 via tunnelR1
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID58 ">}}
{{< tab "leaf01 ">}}

1. Edit the `/etc/network /interfaces` file to add the tunnel interface:

   ```
   cumulus@leaf01:~$ sudo nano /etc/network/interfaces
   ...
   auto lo
   iface lo inet loopback
      address 10.10.10.1/32
   auto swp1
   iface swp1
      address 10.2.1.1/24
   auto tunnelR2
   iface tunnelR2
      address 10.1.100.1/30
      tunnel-mode gre
      tunnel-local 10.10.10.1
      tunnel-endpoint 10.10.10.3
      tunnel-ttl 255
   ```

2. Run the `ifreload -a` command to load the configuration:

   ```
   cumulus@leaf01:mgmt:~$ sudo ifreload -a
   ```

3. Run vtysh commands to configure the static route:

   ```
   cumulus@leaf01:mgmt:~$ sudo vtysh
   ...
   leaf01# configure terminal
   leaf01(config)# ip route 10.1.1.0/24 tunnelR2
   leaf01(config)# exit
   leaf01# write memory
   leaf01# exit
   cumulus@leaf01:mgmt:~$
   ```

   The vtysh commands save the static route configuration in the `/etc/frr/frr.conf` file. For example:

   ```
   cumulus@leaf01:mgmt:~$ sudo cat /etc/frr/frr.conf
   ...
   vrf default
   ip route 10.1.1.0/24 tunnelR2
   exit-vrf
   ...
   ```

{{< /tab >}}
{{< tab "leaf03 ">}}

1. Edit the `/etc/network /interfaces` file to add the tunnel interface:

   ```
   cumulus@leaf03:~$ sudo nano /etc/network/interfaces
   ...
   auto lo
   iface lo inet loopback
      address 10.10.10.3/32
   auto swp1
   iface swp1
      address 10.1.1.1/24
   auto tunnelR1
   iface tunnelR1
      address 10.1.100.2/30
      tunnel-mode gre
      tunnel-local 10.10.10.3
      tunnel-endpoint 10.10.10.1
      tunnel-ttl 255
   ```

2. Run the `ifreload -a` command to load the configuration.

   ```
   cumulus@leaf03:mgmt:~$ sudo ifreload -a
   ```

3. Run vtysh commands to configure the static route:

   ```
   cumulus@leaf03:mgmt:~$ sudo vtysh
   ...
   leaf01# configure terminal
   leaf01(config)# ip route 10.2.1.0/24 tunnelR1
   leaf01(config)# exit
   leaf01# write memory
   leaf01# exit
   cumulus@leaf03:mgmt:~$
   ```

   The vtysh commands save the static route configuration in the `/etc/frr/frr.conf` file. For example:

   ```
   cumulus@leaf03:mgmt:~$ sudo cat /etc/frr/frr.conf
   ...
   vrf default
   ip route 10.2.1.0/24 tunnelR1
   exit-vrf
   vrf mgmt
   exit-vrf
   ...
   ```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

To delete a GRE tunnel, remove the tunnel interface, and remove the routes configured with the tunnel interface. Either run the NVU `nv unset` commands or remove the tunnel configuration from the `/etc/network/interfaces` file and run the `ifreload -a` command.

## Troubleshooting

To check GRE tunnel settings, run the NVUE `nv show interface <interface> tunnel` command, or run the Linux `ip tunnel show` or `ifquery --check` command. For example:

```
cumulus@leaf01:mgmt:~$ nv show interface tunnelR2 tunnel
           operational  applied     description
---------  -----------  ----------  -------------------------------
dest-ip    10.10.10.3   10.10.10.3  Destination underlay IP address
mode       gre          gre         tunnel mode
source-ip  10.10.10.1   10.10.10.1  Source underlay IP address
ttl                     255         time to live
```

```
cumulus@leaf01:mgmt:~$ ip tunnel show
gre0: gre/ip remote any local any ttl inherit nopmtudisc
tunnelR2: gre/ip remote 10.10.10.3 local 10.10.10.1 ttl 255
```

```
cumulus@leaf01:mgmt:~$ ifquery --check tunnelR2
auto tunnelR2
iface tunnelR2                                                      [pass]
        tunnel-mode gre                                             [pass]
        tunnel-local 10.10.10.1/32                                  [pass]
        tunnel-endpoint 10.10.10.3/32                               [pass]
        tunnel-ttl 255                                              [pass]
        address 10.1.100.1/30                                       [pass]
```
