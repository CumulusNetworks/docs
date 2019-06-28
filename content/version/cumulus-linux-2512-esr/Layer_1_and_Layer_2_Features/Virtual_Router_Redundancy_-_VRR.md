---
title: Virtual Router Redundancy - VRR
author: Cumulus Networks
weight: 105
aliases:
 - /display/CL25ESR/Virtual+Router+Redundancy+-+VRR
 - /pages/viewpage.action?pageId=5116083
pageID: 5116083
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
VRR provides virtualized router redundancy in network configurations,
which enables the hosts to communicate with any redundant router
without:

  - Needing to be reconfigured

  - Having to run dynamic router protocols

  - Having to run router redundancy protocols

A basic VRR-enabled network configuration is shown below. The network
consists of several hosts, two routers running Cumulus Linux and
configured with
[MLAG](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Multi-Chassis_Link_Aggregation_-_MLAG),
and the rest of the network:

{{% imgOld 0 %}}

An actual implementation will have many more server hosts and network
connections than are shown here. But this basic configuration provides a
complete description of the important aspects of the VRR setup.

## <span>Configuring the Network</span>

Configuring this network is fairly straightforward. First create the
bridge subinterface, then create the secondary address for the virtual
router. Configure each router with a bridge; edit each router’s
`/etc/network/interfaces` file and add a configuration similar to the
following:

    auto bridge.500
    iface bridge.500
        address 192.168.0.252/24
        address-virtual 00:00:5e:00:01:01 192.168.0.254/24 2001:aa::1/48

{{%notice note%}}

Notice the simpler configuration of the bridge with `ifupdown2`. For
more information, see [Configuring and Managing Network
Interfaces](/version/cumulus-linux-2512-esr/Configuring_and_Managing_Network_Interfaces/).

You should always use `ifupdown2` to configure VRR, because it ensures
correct ordering when bringing up the virtual and physical interfaces
and it works best with [VLAN-aware
bridges](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments).

If you are using the [traditional
mode](https://support.cumulusnetworks.com/hc/en-us/articles/204909397)
bridge driver, the configuration would look like this:

    auto bridge500
    iface bridge500
        address 192.168.0.252/24
        address-virtual 00:00:5e:00:01:01 192.168.0.254/24 2001:aa::1/48
        bridge-ports bond1.500 bond2.500 bond3.500

{{%/notice%}}

The IP address assigned to the bridge is the unique address for the
bridge. The parameters of this configuration are:

  - *`bridge.500`*: 500 represents a VLAN subinterface of the bridge,
    sometimes called a switched virtual interface, or SVI.

  - *`192.168.0.252/24`* : The unique IP address assigned to this
    bridge. It is unique because, unlike the 192.168.0.254 address, it
    is assigned only to this bridge, not the bridge on the other router.

  - *`00:00:5e:00:01:01`*: The MAC address of the virtual router. This
    must be the same on all virtual routers. Cumulus Linux has a
    reserved range for VRR MAC addresses. See below for details.

  - *`192.168.0.254/24`*, *`2001:aa::1/48`*: The IPv4 and IPv6 addresses
    of the virtual router, including the routing prefixes. These
    addresses must be the same on all the virtual routers and must match
    the default gateway address configured on the servers as well as the
    size of the subnet.

  - `address-virtual`: This keyword enables and configures VRR.

The above bridge configuration enables VRR by creating a *MAC VLAN
interface* on the SVI. This MAC VLAN interface is:

  - Named *bridge-500-v0*, which is the name of the SVI with dots
    changed to dashes and *-v0* appended to the end.

  - Assigned a MAC address of *00:00:5e:00:01:01*.

  - Assigned an IPv4 address of *192.168.0.254* and an IPv6 address of
    *2001:aa::1/48*.

### <span>Reserved MAC Address Range</span>

In order to prevent MAC address conflicts with other interfaces in the
same bridged network, Cumulus Networks has [reserved a range of MAC
addresses](https://support.cumulusnetworks.com/hc/en-us/articles/203837076)
specifically to use with VRR. This range of MAC addresses is
00:00:5E:00:01:00 to 00:00:5E:00:01:ff.

You may notice that this is the same range reserved for VRRP, since VRR
serves a similar function. Cumulus Networks recommends you use this
range of MAC addresses when configuring VRR.

### <span>Configuring the Hosts</span>

Each host should have two network interfaces. The routers configure the
interfaces as bonds running LACP; the hosts should also configure its
two interfaces using teaming, port aggregation, port group, or
EtherChannel running LACP. Configure the hosts, either statically or via
DHCP, with a gateway address that is the IP address of the virtual
router; this default gateway address never changes.

Configure the links between the hosts and the routers in *active-active*
mode for First Hop Redundancy Protocol.

### <span>Configuring the Routers</span>

The routers implement the layer 2 network interconnecting the hosts, as
well as the redundant routers. If you are using
[MLAG](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Multi-Chassis_Link_Aggregation_-_MLAG),
configure each router with a bridge interface, named *bridge* in our
example, with these different types of interfaces:

  - One bond interface to each host (swp1-swp5 in the image above).

  - One or more interfaces to each peer router (peerbond in the image
    above). Multiple inter-peer links are typically bonded interfaces in
    order to accommodate higher bandwidth between the routers and to
    offer link redundancy.

{{%notice note%}}

If you are not using MLAG, then the bridge should have one switch port
interface to each host instead of a bond.

{{%/notice%}}

### <span>Other Network Connections</span>

Other interfaces on the router can connect to other subnets and are
accessed through layer 3 forwarding (swp7 in the image above).

### <span>Handling ARP Requests</span>

The entire purpose of this configuration is to have all the redundant
routers respond to ARP requests from hosts for the virtual router IP
address (192.168.0.254 in the example above) with the virtual router MAC
address (00:00:5e:00:01:01 in the example above). All of the routers
should respond in an identical manner, but if one router fails, the
other redundant routers will continue to respond in an identical manner,
leaving the hosts with the impression that nothing has changed.

Since the bridges in each of the redundant routers are connected, they
will each receive and reply to ARP requests for the virtual router IP
address. Each ARP request made by a host will receive multiple replies
(typically two). But these replies will be identical and so the host
that receives these replies will not get confused over which response is
"correct" and will either ignore replies after the first, or accept them
and overwrite the previous reply with identical information.

### <span>Monitoring Peer Links and Uplinks</span>

When an uplink on a switch in active-active mode goes down, the peer
link may get congested. When this occurs, you should monitor the uplink
and shut down all host-facing ports using `ifplugd` (or another script).

When the peer link goes down in a MLAG environment, one of the switches
becomes secondary and all host-facing dual-connected bonds go down. The
host side bond sees two different system MAC addresses, so the link to
primary is active on host. If any traffic from outside this environment
goes to the secondary MLAG switch, traffic will be black-holed. To avoid
this, shut down all the uplinks when the peer link goes down using
`ifplugd`.

## <span id="src-5116083_VirtualRouterRedundancy-VRR-ifplugd" class="confluence-anchor-link"></span><span>Using ifplugd</span>

`ifplugd` is a link state monitoring daemon that can execute
user-specified scripts on link transitions (not admin-triggered
transitions, but transitions when a cable is plugged in or removed).

Run the following commands to install the `ifplugd` service:

    cumulus@switch:$ sudo apt-get update
    cumulus@switch:$ sudo apt-get install ifplugd

Next, configure `ifplugd`. The example below indicates that when the
peerbond goes down in a MLAG environment, `ifplugd` brings down all the
uplinks. Run the following `ifplugd` script on both the primary and
secondary
[MLAG](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Multi-Chassis_Link_Aggregation_-_MLAG)
switches.

To configure `ifplugd`, modify `/etc/default/ifplugd` and add the
appropriate peerbond interface name. `/etc/default/ifplugd` will look
like this:

``` 
 INTERFACES="peerbond"
 HOTPLUG_INTERFACES=""
 ARGS="-q -f -u0 -d1 -w -I"
    SUSPEND_ACTION="stop"
```

Next, modify the `/etc/ifplugd/action.d/ifupdown` script.

    #!/bin/sh
    set -e
    case "$2" in
    up)
         clagrole=$(clagctl | grep "Our Priority" | awk '{print $8}')
            if [ "$clagrole" = "secondary" ]
            then
                #List all the interfaces below to bring up when clag peerbond comes up.
                for interface in swp1 bond1 bond3 bond4
              do
                  echo "bringing up : $interface"  
                    ip link set $interface up
                done
            fi
        ;;
    down)
           clagrole=$(clagctl | grep "Our Priority" | awk '{print $8}')
            if [ "$clagrole" = "secondary" ]
            then
                #List all the interfaces below to bring down when clag peerbond goes down.
                for interface in swp1 bond1 bond3 bond4
                do
                    echo "bringing down : $interface"
                    ip link set $interface down
                done
            fi
        ;;
    esac

Finally, restart `ifplugd` for your changes to take effect:

    cumulus@switch:$ sudo service ifplugd restart

## <span>Notes</span>

  - The default shell is `/bin/sh`, which is `dash` and not `bash`. This
    makes for faster execution of the script since `dash` is small and
    quick, but consequently less featureful than `bash`. For example, it
    doesn't handle multiple uplinks.
