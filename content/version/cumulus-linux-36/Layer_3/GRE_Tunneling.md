---
title: GRE Tunneling
author: Cumulus Networks
weight: 195
aliases:
 - /display/CL36/GRE+Tunneling
 - /pages/viewpage.action?pageId=8362432
pageID: 8362432
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
{{%notice warning%}}

**Early Access Feature**

GRE Tunneling is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus Linux 3.6.

{{%/notice%}}

Generic Routing Encapsulation (GRE) is a tunneling protocol that
encapsulates network layer protocols inside virtual point-to-point links
over an Internet Protocol network. The two endpoints are identified by
the tunnel source and tunnel destination addresses at each endpoint.

GRE packets travel directly between the two endpoints through a virtual
tunnel. As a packet comes across other routers, there is no interaction
with its payload; the routers only parse the outer IP packet. When the
packet reaches the endpoint of the GRE tunnel, the outer packet is
de-encapsulated, the payload is parsed, then forwarded to its ultimate
destination.

GRE uses multiple protocols over a single-protocol backbone and is less
demanding than some of the alternative solutions, such as VPN. You can
use GRE to transport protocols that the underlying network does not
support, work around networks with limited hops, connect non-contiguous
subnets, and allow VPNs across wide area networks.

{{%notice note%}}

**Notes**

  - GRE Tunneling is supported for Mellanox (Spectrum ASIC) switches
    only.

  - Only static routes are supported as a destination for the tunnel
    interface.

  - IPv6 endpoints are not supported.

{{%/notice%}}

The following example shows two sites that use IPv4 addresses. Using GRE
tunneling, the two end points can encapsulate an IPv4 or IPv6 payload
inside an IPv4 packet. The packet is routed based on the destination in
the outer IPv4 header.

{{% imgOld 0 %}}

## <span> Contents</span>

This chapter covers ...

## <span>Configuring GRE Tunneling</span>

To configure GRE tunneling, you create a GRE tunnel interface with
routes for tunneling on both endpoints as follows:

1.  Create a tunnel interface by specifying an interface name, the
    tunnel mode as `gre`, the source (local) and destination (remote)
    underlay IP address, and the `ttl` (optional).

2.  Bring the GRE tunnel interface up.

3.  Assign an IP address to the tunnel interface.

4.  Add route entries to encapsulate the packets using the tunnel
    interface.

The following configuration example shows the commands used to set up a
bidirectional GRE tunnel between two endpoints: `Tunnel-R1` and
`Tunnel-R2`.  
The local tunnel endpoint for `Tunnel-R1` is 10.0.0.9 and the remote
endpoint is 10.0.0.2.  
The local tunnel endpoint for `Tunnel-R2` is 10.0.0.2 and the remote
endpoint is 10.0.0.9.

{{% imgOld 1 %}}

<span style="color: #000000;">  
</span>

**Tunnel-R1 commands:**

    cumulus@switch:~$ sudo ip tunnel add Tunnel-R2 mode gre remote 10.0.0.2 local 10.0.0.9 ttl 255
    cumulus@switch:~$ sudo ip link set Tunnel-R2 up
    cumulus@switch:~$ sudo ip addr add 10.0.100.1 dev Tunnel-R2
    cumulus@switch:~$ sudo ip route add 10.0.100.0/24 dev Tunnel-R2

**Tunnel-R2 commands:**

    cumulus@switch:~$ sudo ip Tunnel add Tunnel-R1 mode gre remote 10.0.0.9 local 10.0.0.2 ttl 255
    cumulus@switch:~$ sudo ip link set Tunnel-R1 up
    cumulus@switch:~$ sudo ip addr add 10.0.200.1 dev Tunnel-R1
    cumulus@switch:~$ sudo ip route add 10.0.200.0/24 dev Tunnel-R1

To apply the GRE tunnel configuration automatically at reboot, instead
of running the commands from the command line (as above), you can add
the following commands directly in the `/etc/network/interfaces` file.

    cumulus@switch:~$ sudo nano /etc/network/interfaces
    # Tunnel-R1 configuration 
    auto swp1 #underlay interface for tunnel
    iface swp1
        link-speed 10000
        link-duplex full
        link-autoneg off
        address 10.0.0.9/24
     
    auto Tunnel-R2 #overlay interface for tunnel
    iface Tunnel-R2 inet static
        address 10.0.100.1/24
        # Run pre-up command before bringing the interface up. If this command fails, then ifup aborts, refraining from marking the interface as configured, prints an error message, and exits with status 0. This behavior may change in the future.
        pre-up ip tunnel add Tunnel-R2 mode gre remote 10.0.0.2 local   10.0.0.9 ttl 255
        # Run post-up command after bringing the interface up. If this command fails then ifup aborts, refraining from marking the interface as configured (even though it has really been configured), prints an error message, and exits with status 0. This behavior may change in the future.
        post-up ip route add 10.0.100.0/24 dev Tunnel-R2
        # Run post-down command after taking the interface down. If this command fails then ifdown aborts, marks the interface as deconfigured, and exits with status 0. This behavior may change in the future.
        post-down ip tunnel del Tunnel-R2
     
    # Tunnel-R2 configuration
    auto swp1 #underlay interface for tunnel
    iface swp1
        link-speed 10000
        link-duplex full
        link-autoneg off
        address 10.0.0.2/24
    auto Tunnel-R1 #overlay interface for tunnel
    iface Tunnel-R1 inet static
        address 10.0.200.1/24
        pre-up ip tunnel add Tunnel-R1 mode gre local 10.0.0.2 remote 10.0.0.9 ttl 255
        post-up ip route add 10.0.200.0/24 dev Tunnel-R1
        post-down ip tunnel del Tunnel-R1

For more information about the `pre-up`, `post-up`, and `post-down`
commands, run the `man interfaces` command.

## <span>Verifying GRE Tunnel Settings</span>

Use the `ip tunnel show` command to check GRE tunnel settings:

    cumulus@switch:~$ ip tunnel show
    gre0: gre/ip remote any local any ttl inherit nopmtudisc
    Tunnel-R1: gre/ip remote 10.0.0.2 local 10.0.0.9 ttl 255

## <span>Deleting a GRE Tunnel Interface</span>

Use the `ip tunnel del` command to delete a GRE tunnel, remove the
tunnel interface, and remove the routes configured with the tunnel
interface. For example:

    cumulus@switch:~$ sudo ip tunnel del Tunnel-R2 mode gre remote 10.0.0.2 local 10.0.0.9 ttl 255

{{%notice note%}}

You can delete a GRE tunnel directly from the `/etc/network/interfaces`
file instead of using the `ip tunnel del` command. Make sure you run the
`ifreload - a` command after you update the interfaces file.

{{%/notice%}}

## <span>Changing GRE Tunnel Settings</span>

Use the `ip tunnel change` command to make changes to the GRE tunnel
settings. The following example changes the remote underlay IP address
from the original setting to 11.0.0.4:

    cumulus@switch:~$ sudo ip tunnel change Tunnel-R2 mode gre local 10.0.0.2 remote 10.0.0.4

{{%notice note%}}

You can make changes to GRE tunnel settings directly in the
`/etc/network/interfaces` file instead of using the `ip tunnel change`
command. Make sure you run the `ifreload - a` command after you update
the interfaces file.

{{%/notice%}}
