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
- You can only configure point to point GRE tunnels.
{{%/notice%}}

The following example shows two sites that use IPv4 addresses. Using GRE tunneling, the two end points can encapsulate an IPv4 or IPv6 payload inside an IPv4 packet. The switch routes the packet based on the destination in the outer IPv4 header.

{{< img src = "/images/cumulus-linux/gre-tunnel-example.png" >}}

## Configure GRE Tunneling

To configure GRE tunneling, you create a GRE tunnel interface with routes for tunneling on both endpoints as follows:

1. Create a tunnel interface by specifying an interface name, the tunnel mode as `gre`, the source (local) and destination (remote) underlay IP address, and the `ttl` (optional).
2. Bring the GRE tunnel interface up.
3. Assign an IP address to the tunnel interface.
4. Add route entries to encapsulate the packets using the tunnel interface.

The following configuration example shows the commands used to set up a bidirectional GRE tunnel between two endpoints: `TunnelR1` and `TunnelR2`. The local tunnel endpoint for `TunnelR1` is 10.0.0.9 and the remote endpoint is 10.0.0.2. The local tunnel endpoint for `TunnelR2` is 10.0.0.2 and the remote endpoint is 10.0.0.9.

{{< img src = "/images/cumulus-linux/gre-tunnel-config.png" >}}

{{< tabs "TabID35 ">}}
{{< tab "NVUE Commands">}}

{{< tabs "TabID38 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface tunnelR2 ip address 10.0.100.1/24
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel mode gre
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel dest-ip 10.0.0.2
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel source-ip 10.0.0.9
cumulus@leaf01:~$ nv set interface tunnelR2 tunnel ttl 255
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "leaf03 ">}}

```
cumulus@leaf03:~$ nv set interface tunnelR2 ip address 10.0.200.1/24
cumulus@leaf03:~$ nv set interface tunnelR2 tunnel mode gre
cumulus@leaf03:~$ nv set interface tunnelR2 tunnel dest-ip 10.0.0.9
cumulus@leaf03:~$ nv set interface tunnelR2 tunnel source-ip 10.0.0.2
cumulus@leaf03:~$ nv set interface tunnelR2 tunnel ttl 255
cumulus@leaf03:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{< tabs "TabID58 ">}}
{{< tab "leaf01 ">}}

Edit the `/etc/network/interfaces` file to add the following configuration:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto swp1 #underlay interface for tunnel
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off
    address 10.0.0.9/24
auto TunnelR2
iface TunnelR2
    tunnel-mode gre
    tunnel-endpoint 10.0.0.2
    tunnel-local 10.0.0.9
    tunnel-ttl 255
    address 10.0.100.1
    up ip route add 10.0.100.0/24 dev Tunnel-R2
```

Run the `ifreload -a` command to load the configuration.

{{< /tab >}}
{{< tab "leaf03 ">}}

Edit the `/etc/network/interfaces` file to add the following configuration:

```
cumulus@leaf03:~$ sudo nano /etc/network/interfaces
...
auto swp1 #underlay interface for tunnel
iface swp1
    link-speed 10000
    link-duplex full
    link-autoneg off
    address 10.0.0.2/24
auto TunnelR1
iface TunnelR1
    tunnel-mode gre
    tunnel-endpoint 10.0.0.9
    tunnel-local 10.0.0.2
    tunnel-ttl 255
    address 10.0.200.1
    up ip route add 10.0.200.0/24 dev Tunnel-R1
```

Run the `ifreload -a` command to load the configuration.

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

To delete a GRE tunnel, remove the tunnel interface, and remove the routes configured with the tunnel interface, either run the NVU `nv unset` commands or remove the tunnel configuration from the `/etc/network/interfaces` file and run the `ifreload -a` command.

## Troubleshooting

To check GRE tunnel settings, run the NVUE `nv show interface <interface>` command, or the Linux `ip tunnel show` or `ifquery --check` command. For example:

```
cumulus@switch:~$ ip tunnel show
gre0: gre/ip remote any local any ttl inherit nopmtudisc
Tunnel-R1: gre/ip remote 10.0.0.2 local 10.0.0.9 ttl 255
```

```
cumulus@switch:~$ ifquery --check TunnelR1
auto TunnelR1
iface TunnelR1                                                 [pass]
        up ip route add 10.0.200.0/24 dev TunnelR1                 []
        tunnel-ttl 255                                          [pass]
        tunnel-endpoint 10.0.0.9                                [pass]
        tunnel-local 10.0.0.2                                   [pass]
        tunnel-mode gre                                         [pass]
        address 10.0.200.1/32                                   [pass]
```
