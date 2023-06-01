---
title: Virtual Routing and Forwarding - VRF
author: NVIDIA
weight: 940
toc: 3
---
Virtual routing and forwarding (VRF) enables you to use multiple independent routing tables that work simultaneously on the same switch. Other implementations call this feature *VRF-Lite*.

You typically use VRFs in the data center to carry multiple isolated traffic streams for multi-tenant environments. The traffic streams can cross over only at configured boundary points, such as a firewall or [IDS](## "Intrusion Detection System"). You can also use VRFs to burst traffic from private clouds to enterprise networks where the burst point is at layer 3.

VRF is fully supported in the Linux kernel and has the following characteristics:

- The VRF is a layer 3 master network device with its own associated routing table.
- You can associate any layer 3 interface with a VRF, such as an SVI, swp port or bond, or a VLAN subinterface of a swp port or bond.
- The layer 3 interfaces associated with the VRF belong to that VRF; IP rules direct [FIB](## "Forwarding Information Base") lookups to the routing table for the VRF device.
- The VRF device can have its own IP address, known as a *VRF-local loopback*.
- By default, applications on the switch run against the default VRF. Services started by `systemd` run in the default VRF unless you use the VRF instance.
- Connected and local routes go in appropriate VRF tables.
- Neighbor entries continue to be per-interface. You can view all entries for a VRF device.
- A VRF does not map to its own network namespace; however, you can nest VRFs in a network namespace.
- You can use existing Linux tools, such as `tcpdump`, to interact with a VRF.

## Configure a VRF

Cumulus Linux calls each routing table a *VRF table*, which has its own table ID.

To configure VRF, you associate a subset of interfaces to a VRF routing table and configure an instance of the routing protocol (BGP or OSPFv2) for each routing table. Configuring a VRF is similar to configuring other network interfaces. Keep in mind the following:

- A VRF table can have an IP address, which is a loopback interface for the VRF.
- Cumulus Linux adds the associated rules automatically.
- You can add a default route to avoid skipping across tables when the kernel forwards a packet.
- VRF table names can be a maximum of 15 characters. However, you **cannot** use the name *mgmt*; Cumulus Linux uses this name for the {{<link url="Management-VRF" text="management VRF">}}.
- Cumulus Linux supports up to 255 VRFs on a switch.

The following example commands configure VRF BLUE and assigns a table ID automatically.

{{< tabs "TabID44 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf BLUE table auto
cumulus@switch:~$ nv set interface swp1 ip vrf BLUE
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file to add the VRF and assign a table ID automatically:

```
...
auto swp1
iface swp1
  vrf BLUE

auto BLUE
iface BLUE
  vrf-table auto
...
```

To load the new configuration, run `ifreload -a`:

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

### Specify a Table ID

Instead of assigning a table ID for the VRF automatically, you can specify your own table ID in the configuration. Cumulus Linux saves the table ID to name mapping in the `/etc/iproute2/rt_tables.d/` directory. Instead of using the `auto` option as shown above, specify the table ID. For example:

{{< tabs "TabID89 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf BLUE table 1016
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file:

```
...
auto swp1
iface swp1
  vrf BLUE

auto BLUE
iface BLUE
  vrf-table 1016
...
```

To load the new configuration, run `ifreload -a`:

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
The table ID range **must** be between 1001 to 1255. Cumulus Linux reserves this range for VRF table IDs.
{{%/notice%}}

### Bring a VRF Up After You Run ifdown

If you take down a VRF using `ifdown`, run one of the following commands to bring the VRF back up:

- `ifup --with-depends <vrf-name>`
- `ifreload -a`

For example:

```
cumulus@switch:~$ sudo ifdown BLUE
cumulus@switch:~$ sudo ifup --with-depends BLUE
```

### Use the vrf Command

Run the `vrf` command to show information about VRF tables not available in other Linux commands, such as `iproute`.

To show a list of VRF tables, run the `vrf list` command:

```
cumulus@switch:~$ vrf list
VRF              Table
---------------- -----
BLUE            1016
```

To show a list of processes and PIDs for a specific VRF table, run the `ip vrf pids <vrf-name>` command. For example:

```
cumulus@switch:~$ ip vrf pids BLUE
VRF: BLUE
-----------------------
dhclient           2508
sshd               2659
bash               2681
su                 2702
bash               2720
vrf                2829
```

To determine which VRF table associates with a particular PID, run the `ip vrf identify <pid>` command. For example:

```
cumulus@switch:~$ ip vrf identify 2829
BLUE
```

#### IPv4 and IPv6 Commands in a VRF Context

You can execute non-VRF-specific Linux commands and perform other tasks against a given VRF table. This typically applies to single-use commands started from a login shell, as they affect only AF_INET and AF_INET6 sockets opened by the command that executes; it has no impact on netlink sockets, associated with the `ip` command.

To execute such a command against a VRF table, run `ip vrf exec <vrf-name> <command>`. For  example, to SSH from the switch to a device accessible through VRF *BLUE*:

```
cumulus@switch:~$ sudo ip vrf exec BLUE ssh user@host
```

### Services in VRFs

For services that need to run against a specific VRF, Cumulus Linux uses `systemd` instances, where the instance is the VRF. You start a service within a VRF with the `systemctl start <service>@<vrf-name>` command. For example, to run the `dhcpd` service in the BLUE VRF:

```
cumulus@switch:~$ sudo systemctl start dhcpd@BLUE
```

In most cases, you need to stop the instance running in the default VRF before a VRF instance can start. This is because the instance running in the default VRF owns the port across all VRFs (it is VRF global). Cumulus Linux stops `systemd`-based services when you restart networking or run an `ifdown`/`ifup` sequence. Refer to {{<link url="Management-VRF" text="management VRF">}} for details.

The following services work with VRF instances:

- `chef-client`
- `collectd`
- `dhcpd`
- `dhcrelay`
- `hsflowd`
- `netq-agent`
- `ntp` (can only run in the default or management VRF)
- `puppet`
- `snmptrapd`
- `ssh`
- `zabbix-agent`

{{%notice note%}}
If `systemd` instances do not work; use a service-specific configuration option instead. For example, to configure `rsyslogd` to send messages to remote systems over a VRF:

```
action(type="omfwd" Target="hostname or ip here" Device="mgmt" Port=514
Protocol="udp")
```
{{%/notice%}}

## VRF Route Leaking

You typically use VRFs when you want multiple independent routing and forwarding tables; however, you might want to reach destinations in one VRF from another VRF, as in the following cases:
- To make a service, such as a firewall available to multiple VRFs.
- To enable routing to external networks or the Internet for multiple VRFs, where the external network itself is reachable through a specific VRF.

Cumulus Linux supports dynamic VRF route leaking (not static route leaking).

{{%notice note%}}
- You can assign an interface to only one VRF; Cumulus Linux routes any packets arriving on that interface using the associated VRF routing table.
- You cannot route leak overlapping addresses.
- You can use VRF route leaking with EVPN in a symmetric routing configuration only.
- You cannot use VRF route leaking between the tenant VRF and the default VRF with onlink next hops (BGP unnumbered).
{{%/notice%}}

### Configure Route Leaking

With route leaking, a destination VRF wants to know the routes of a source VRF. As routes come and go in the source VRF, they dynamically leak to the destination VRF through BGP. If BGP learns the routes in the source VRF, you do not need to perform any additional configuration. If OSPF learns the routes in the source VRF, if you configure the routes statically, or you need to reach directly connected networks, you need to *redistribute* the routes first into BGP (in the source VRF).

You can also use route leaking to reach remote destinations as well as directly connected destinations in another VRF. Multiple VRFs can import routes from a single source VRF and a VRF can import routes from multiple source VRFs. You can use this method when a single VRF provides connectivity to external networks or a shared service for other VRFs. You can control the routes leaked dynamically across VRFs with a route map.

Because route leaking happens through BGP, the underlying mechanism relies on the BGP constructs of the Route Distinguisher (RD) and Route Targets (RTs). However, you do not need to configure these parameters; Cumulus Linux derives them automatically when you enable route leaking between a pair of VRFs.

When you use route leaking:

- You cannot reach the loopback address of a VRF (the address assigned to the VRF device) from another VRF.
- You must use the `redistribute` command in BGP to leak non-BGP routes (connected or static routes); you cannot use the `network` command.
- Cumulus Linux does not leak routes in the management VRF with the next hop as eth0 or the management interface.
- You can leak routes in a VRF that iBGP or multi-hop eBGP learns even if their next hops become unreachable. NVIDIA recommends route leaking for routes that BGP learns through single-hop eBGP.
- You cannot configure VRF instances of BGP in multiple autonomous systems (AS) or an AS that is not the same as the global AS.
- Do not use the default VRF as a shared service VRF. Create another VRF for shared services.
- An EVPN symmetric routing configuration has certain limitations when leaking routes between the default VRF and non-default VRFs. The default VRF has routes to VTEP addresses that you cannot leak to any tenant VRFs. If you need to leak routes between the default VRF and a non-default VRF, you must filter out routes to the VTEP addresses to prevent leaking these routes. Use caution with such a configuration. Run common services in a separate VRF (service VRF) instead of the default VRF to simplify configuration and avoid using route maps for filtering.

In the following example commands, routes in the BGP routing table of VRF `BLUE` dynamically leak into VRF `RED`.

{{< tabs "TabID266 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf list BLUE
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65001 vrf RED
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# import vrf BLUE
switch(config-router-af)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65001 vrf RED
 !
 address-family ipv4 unicast
  import vrf BLUE
...
```

{{< /tab >}}
{{< /tabs >}}

### Exclude Certain Prefixes

To exclude certain prefixes from the import process, configure the prefixes in a route map.

The following example configures a route map to match the source protocol BGP and imports the routes from VRF BLUE to VRF RED. For the imported routes, the community is 11:11 in VRF RED.

{{< tabs "TabID313 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf list BLUE
cumulus@switch:~$ nv set router policy route-map BLUEtoRED rule 10 match type ipv4
cumulus@switch:~$ nv set router policy route-map BLUEtoRED rule 10 match source-protocol bgp 
cumulus@switch:~$ nv set router policy route-map BLUEtoRED rule 10 action permit
cumulus@switch:~$ nv set router policy route-map BLUEtoRED rule 10 set community 11:11
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf route-map BLUEtoRED
cumulus@switch:~$ nv config
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65001 vrf RED
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# import vrf BLUE
switch(config-router-af)# route-map BLUEtoRED permit 10
switch(config-route-map)# match source-protocol bgp
switch(config-route-map)# set community 11:11
switch(config-route-map)# exit
switch(config)# router bgp 65001 vrf RED
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# import vrf route-map BLUEtoRED
switch(config-router-af)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

### Verify Route Leaking Configuration

To check the status of VRF route leaking, run the vtysh `show ip bgp vrf <vrf-name> ipv4|ipv6 unicast route-leak` command or the `net show bgp vrf <vrf-name> ipv4|ipv6 unicast route-leak` command. For example:

```
cumulus@switch:~$ sudo vtysh
switch# show ip bgp vrf RED ipv4 unicast route-leak
This VRF is importing IPv4 Unicast routes from the following VRFs:
  BLUE
Import RT(s): 0.0.0.0:3
This VRF is exporting IPv4 Unicast routes to the following VRFs:
  RED
RD: 10.1.1.1:2
Export RT: 10.1.1.1:2
```

- To view the BGP routing table, run the vtysh `show ip bgp vrf <vrf-name> ipv4|ipv6 unicast` command or the `net show bgp vrf <vrf-name> ipv4|ipv6 unicast` command.
- To view the FRR IP routing table, run the vtysh `show ip route vrf <vrf-name>` command or the `net show route vrf <vrf-name>` command. These commands show all routes, including routes leaked from other VRFs.

The following example commands show all routes in VRF `RED`, including routes leaked from VRF `BLUE`:

```
cumulus@switch:~$ sudo vtysh
switch# show ip route vrf RED
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, P - PIM, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR,
       > - selected route, * - FIB route

VRF RED:
K * 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 6d07h01m
C>* 10.1.1.1/32 is directly connected, BLUE, 6d07h01m
B>* 10.0.100.1/32 [200/0] is directly connected, RED(vrf RED), 6d05h10m
B>* 10.0.200.0/24 [20/0] via 10.10.2.2, swp1.11, 5d05h10m
B>* 10.0.300.0/24 [200/0] via 10.20.2.2, swp1.21(vrf RED), 5d05h10m
C>* 10.10.2.0/30 is directly connected, swp1.11, 6d07h01m
C>* 10.10.3.0/30 is directly connected, swp2.11, 6d07h01m
C>* 10.10.4.0/30 is directly connected, swp3.11, 6d07h01m
B>* 10.20.2.0/30 [200/0] is directly connected, swp1.21(vrf RED), 6d05h10m
```

### Delete Route Leaking Configuration

The following example commands delete leaked routes from VRF `BLUE` to VRF `RED`:

{{< tabs "TabID407 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv unset vrf RED router bgp address-family ipv4-unicast route-import from-vrf list BLUE
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65001 vrf RED
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# no import vrf BLUE
switch(config-router-af)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Cumulus Linux no longer supports kernel commands. To avoid issues with VRF route leaking in FRR, do not use the kernel commands.
{{%/notice%}}

## FRRouting in a VRF

Cumulus Linux supports {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}}, {{<link url="Open-Shortest-Path-First-v2-OSPFv2" text="OSPFv2">}} and {{<link url="Static-Routing" text="static routing">}} for both IPv4 and IPv6 within a VRF context. Various [FRR](## "FRRouting") routing constructs, such as routing tables, nexthops, router-id, and related processing are also VRF-aware.

{{<link url="FRRouting" text="FRR">}} learns of VRFs on the system as well as interface attachment to a VRF through notifications from the kernel.

The following sections show example VRF configurations with BGP and OSPF. For an example VRF configuration with static routing, see {{<link url="Static-Routing" text="static routing">}}.

### BGP

Because BGP is VRF-aware, Cumulus Linux supports per-VRF neighbors, both iBGP and eBGP, as well as numbered and unnumbered interfaces. Non-interface-based VRF neighbors bind to the VRF, so you can have overlapping address spaces in different VRFs. Each VRF can have its own parameters, such as address families and redistribution. Incoming connections rely on the Linux kernel for VRF-global sockets. You can track BGP neighbors with {{<link url="Bidirectional-Forwarding-Detection-BFD" text="BFD">}}, both for single and multiple hops. You can configure multiple BGP instances, associating each with a VRF.

The following example shows a {{<link url="Border-Gateway-Protocol-BGP#bgp-unnumbered" text="BGP unnumbered interface configuration">}} in VRF RED. In BGP unnumbered, there are no addresses on any interface. However, debugging tools like `traceroute` need at least a single IP address per node as the source IP address. Typically, this address is the loopback device. With VRF, you can associate an IP address with the VRF device, which acts as the loopback interface for that VRF.

{{< tabs "TabID1081 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf RED table auto
cumulus@switch:~$ nv set vrf RED loopback ip address 10.10.10.1/32
cumulus@switch:~$ nv set interface swp51 ip vrf RED
cumulus@switch:~$ nv set vrf RED router bgp router-id 10.10.10.1
cumulus@switch:~$ nv set vrf RED router bgp autonomous-system 65001
cumulus@switch:~$ nv set vrf RED router bgp neighbor swp51 remote-as external 
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv4-unicast redistribute connected enable on
cumulus@switch:~$ nv set vrf RED router bgp neighbor swp51 address-family ipv4-unicast enable on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

`/etc/network/interfaces` file configuration:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto RED 
iface RED
    address 10.10.10.1/32
    vrf-table auto
auto swp51
iface swp51
    vrf RED
...
```

vtysh commands:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router bgp 65001 vrf RED
switch(config-router)# bgp router-id 10.10.10.1
switch(config-router)# neighbor swp51 interface remote-as external
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# redistribute connected
switch(config-router-af)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router bgp 65001 vrf RED
 bgp router-id 10.10.10.1
 neighbor swp51 interface remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  exit-address-family
...
```

{{< /tab >}}
{{< /tabs >}}

### OSPF

A VRF-aware OSPFv2 configuration supports numbered and unnumbered interfaces, and layer 3 interfaces such as SVIs, subinterfaces and physical interfaces. The VRF supports types 1 through 5 (ABR and ASBR - external LSAs) and types 9 through 11 (opaque LSAs) link state advertisements, redistribution of other routing protocols, connected and static routes, and route maps. You can track OSPF neighbors with {{<link url="Bidirectional-Forwarding-Detection-BFD" text="BFD">}}.

{{%notice note%}}
Cumulus Linux does not support multiple VRFs in multi-instance OSPF.
{{%/notice%}}

The following example shows an OSPF configuration in VRF RED.

{{< tabs "TabID564 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf RED loopback ip address 10.10.10.1/31
cumulus@switch:~$ nv set interface swp51 ip address 10.0.1.0/31
cumulus@switch:~$ nv set vrf RED router ospf enable on
cumulus@switch:~$ nv set vrf RED router ospf router-id 10.10.10.1
cumulus@switch:~$ nv set vrf RED router ospf redistribute connected
cumulus@switch:~$ nv set vrf RED router ospf redistribute bgp
cumulus@switch:~$ nv set vrf RED router ospf area 0.0.0.0 network 10.10.10.1/32
cumulus@switch:~$ nv set vrf RED router ospf area 0.0.0.0 network 10.0.1.0/31
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

The `/etc/network/interfaces` file configuration:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto RED
iface RED
    address 10.10.10.1/32
    vrf-table auto
auto swp51
iface swp51
  address 10.0.1.0/31
```

vtysh commands:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf vrf RED
switch(config-router)# ospf router-id 10.10.10.1
switch(config-router)# redistribute connected
switch(config-router)# redistribute bgp
switch(config-router)# network 10.10.10.1/32 area 0.0.0.0
switch(config-router)# network 10.0.1.0/31 area 0.0.0.0
switch(config-router)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf vrf RED
  ospf router-id 10.10.10.1
  network 10.10.10.1/32 area 0.0.0.0
  network 10.0.1.0/31 area 0.0.0.0
  redistribute connected
  redistribute bgp
...
```

{{< /tab >}}
{{< /tabs >}}

## DHCP with VRF

Because you can use VRF to bind IPv4 and IPv6 sockets to non-default VRF tables, you can start DHCP servers and relays in any non-default VRF table using the `dhcpd` and `dhcrelay` services. `systemd` must manage these services and the `/etc/vrf/systemd.conf` file must list the services. By default, this file already lists these two services, as well as others. You can add more services as needed, such as `dhcpd6` and `dhcrelay6` for IPv6.

If you edit `/etc/vrf/systemd.conf`, run `sudo systemctl daemon-reload` to generate the `systemd` instance files for the newly added services. Then you can start the service in the VRF using `systemctl start <service>@<vrf-name>.service`, where `<service>` is the name of the service (such as `dhcpd` or `dhcrelay`) and `<vrf-name>` is the name of the VRF.

For example, to start the `dhcrelay` service after you configure a VRF named *BLUE*, run:

```
cumulus@switch:~$ sudo systemctl start dhcrelay@BLUE.service
```

To enable the service at boot time, you must also enable the service:

```
cumulus@switch:~$ sudo systemctl enable dhcrelay@BLUE.service
```

In addition, you need to create a separate default file in the `/etc/default` directory for every instance of a DHCP server or relay in a non-default VRF. To run multiple instances of any of these services, you need a separate file for each instance. The files must have the following names:

- `isc-dhcp-server-<vrf-name>`
- `isc-dhcp-server6-<vrf-name>`
- `isc-dhcp-relay-<vrf-name>`
- `isc-dhcp-relay6-<vrf-name>`

See the example configuration below for more details.

{{%notice note%}}
- Cumulus Linux does **not** support DHCP server and relay across VRFs; the server and host cannot be in different VRF tables. In addition, the server and relay cannot be in different VRF tables.
- Typically, a service running in the default VRF owns a port across all VRFs. If you prefer the VRF local instance, first disable and stop the global instance.
- VRF is a layer 3 routing feature; only run programs that use AF\_INET and AF\_INET6 sockets in a VRF. VRF context does not affect any other aspects of the operation of a program.
- This method only works with `systemd`-based services.
{{%/notice%}}

### Example Configuration

In the following example, there is one IPv4 network with a VRF named *RED* and one IPv6 network with a VRF named *BLUE*.

|IPv4 DHCP Server/relay network|IPv6 DHCP Server/relay network|
|---|---|
|{{< img src = "/images/cumulus-linux/vrf-RED-dhcp4.png" >}}|{{< img src = "/images/cumulus-linux/vrf-BLUE-dhcp6.png" >}}|

Configure each DHCP server and relay as follows:

{{< tabs "TabID1258 ">}}
{{< tab "DHCP Server ">}}

1. Create the file `isc-dhcp-server-RED` in `/etc/default/`. Here is sample content:

    ```
    # Defaults for isc-dhcp-server initscript
    # sourced by /etc/init.d/isc-dhcp-server
    # installed at /etc/default/isc-dhcp-server by the maintainer scripts
    #
    # This is a POSIX shell fragment
    #
    # Path to dhcpd's config file (default: /etc/dhcp/dhcpd.conf).
    DHCPD_CONF="-cf /etc/dhcp/dhcpd-RED.conf"
    # Path to dhcpd's PID file (default: /var/run/dhcpd.pid).
    DHCPD_PID="-pf /var/run/dhcpd-RED.pid"
    # Additional options to start dhcpd with.
    # Don't use options -cf or -pf here; use DHCPD_CONF/ DHCPD_PID instead
    #OPTIONS=""
    # On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
    # Separate multiple interfaces with spaces, e.g. "eth0 eth1".
    INTERFACES="swp2"
    ```

2. Enable the DHCP server:

    ```
    cumulus@switch:~$ sudo systemctl enable dhcpd@RED.service
    ```

3. Start the DHCP server:

    ```
    cumulus@switch:~$ sudo systemctl start dhcpd@RED.service
    ```

4. Check status:

    ```
    cumulus@switch:~$ sudo systemctl status dhcpd@RED.service
    ```

You can create this configuration using the `vrf` command (see {{<link url="#ipv4-and-ipv6-commands-in-a-vrf-context" text="IPv4 and IPv6 Commands in a VRF Context">}} above for more details):

```
cumulus@switch:~$ sudo ip vrf exec RED /usr/sbin/dhcpd -f -q -cf /
    /etc/dhcp/dhcpd-RED.conf -pf /var/run/dhcpd-RED.pid swp2
```

{{< /tab >}}
{{< tab "DHCP6 Server ">}}

1. Create the file `isc-dhcp-server6-BLUE` in `/etc/default/`. Here is sample content:

    ```
    # Defaults for isc-dhcp-server initscript
    # sourced by /etc/init.d/isc-dhcp-server
    # installed at /etc/default/isc-dhcp-server by the maintainer scripts
    #
    # This is a POSIX shell fragment
    #
    # Path to dhcpd's config file (default: /etc/dhcp/dhcpd.conf).
    DHCPD_CONF="-cf /etc/dhcp/dhcpd6-BLUE.conf"
    # Path to dhcpd's PID file (default: /var/run/dhcpd.pid).
    DHCPD_PID="-pf /var/run/dhcpd6-BLUE.pid"
    # Additional options to start dhcpd with.
    # Don't use options -cf or -pf here; use DHCPD_CONF/ DHCPD_PID instead
    #OPTIONS=""
    # On what interfaces should the DHCP server (dhcpd) serve DHCP requests?
    # Separate multiple interfaces with spaces, e.g. "eth0 eth1".
    INTERFACES="swp3"
    ```

2. Enable the DHCP server:

    ```
    cumulus@switch:~$ sudo systemctl enable dhcpd6@BLUE.service
    ```

3. Start the DHCP server:

    ```
    cumulus@switch:~$ sudo systemctl start dhcpd6@BLUE.service
    ```

4. Check status:

    ```
    cumulus@switch:~$ sudo systemctl status dhcpd6@BLUE.service
    ```

You can create this configuration using the `vrf` command (see {{<link url="#ipv4-and-ipv6-commands-in-a-vrf-context" text="IPv4 and IPv6 Commands in a VRF Context">}} above for more details):

```
cumulus@switch:~$ sudo ip vrf exec BLUE dhcpd -6 -q -cf /
  /etc/dhcp/dhcpd6-BLUE.conf -pf /var/run/dhcpd6-BLUE.pid swp3
```

{{< /tab >}}
{{< tab "DHCP Relay ">}}

1. Create the file `isc-dhcp-relay-RED` in `/etc/default/`. Here is sample content:

    ```
    # Defaults for isc-dhcp-relay initscript
    # sourced by /etc/init.d/isc-dhcp-relay
    # installed at /etc/default/isc-dhcp-relay by the maintainer scripts
    #
    # This is a POSIX shell fragment
    #
    # What servers should the DHCP relay forward requests to?
    SERVERS="102.0.0.2"
    # On what interfaces should the DHCP relay (dhrelay) serve DHCP requests?
    # Always include the interface towards the DHCP server.
    # This variable requires a -i for each interface configured above.
    # This will be used in the actual dhcrelay command
    # For example, "-i eth0 -i eth1"
    INTF_CMD="-i swp2s2 -i swp2s3"
    # Additional options that are passed to the DHCP relay daemon?
    OPTIONS=""
    ```

2. Enable the DHCP relay:

    ```
    cumulus@switch:~$ sudo systemctl enable dhcrelay@RED.service
    ```

3. Start the DHCP relay:

    ```
    cumulus@switch:~$ sudo systemctl start dhcrelay@RED.service
    ```

4. Check status:

    ```
    cumulus@switch:~$ sudo systemctl status dhcrelay@RED.service
    ```

You can create this configuration using the `vrf` command (see {{<link url="#ipv4-and-ipv6-commands-in-a-vrf-context" text="IPv4 and IPv6 Commands in a VRF Context">}} above for more details):

```
cumulus@switch:~$ sudo ip vrf exec RED /usr/sbin/dhcrelay -d -q -i /
    swp2s2 -i swp2s3 102.0.0.2
```

{{< /tab >}}
{{< tab "DHCP6 Relay ">}}

1. Create the file `isc-dhcp-relay6-BLUE` in `/etc/default/`. Here is sample content:

    ```
    # Defaults for isc-dhcp-relay initscript
    # sourced by /etc/init.d/isc-dhcp-relay
    # installed at /etc/default/isc-dhcp-relay by the maintainer scripts
    #
    # This is a POSIX shell fragment
    #
    # What servers should the DHCP relay forward requests to?
    #SERVERS="103.0.0.2"
    # On what interfaces should the DHCP relay (dhrelay) serve DHCP requests?
    # Always include the interface towards the DHCP server.
    # This variable requires a -i for each interface configured above.
    # This will be used in the actual dhcrelay command
    # For example, "-i eth0 -i eth1"
    INTF_CMD="-l swp18s0 -u swp18s1"
    # Additional options that are passed to the DHCP relay daemon?
    OPTIONS="-pf /var/run/dhcrelay6@BLUE.pid"
    ```

2. Enable the DHCP relay:

    ```
    cumulus@switch:~$ sudo systemctl enable dhcrelay6@BLUE.service
    ```

3. Start the DHCP relay:

    ```
    cumulus@switch:~$ sudo systemctl start dhcrelay6@BLUE.service
    ```

4. Check status:

    ```
    cumulus@switch:~$ sudo systemctl status dhcrelay6@BLUE.service
    ```

You can create this configuration using the `vrf` command (see {{<link url="#ipv4-and-ipv6-commands-in-a-vrf-context" text="IPv4 and IPv6 Commands in a VRF Context">}} above for more details):

```
cumulus@switch:~$ sudo ip vrf exec BLUE /usr/sbin/dhcrelay -d -q -6 -l /
    swp18s0 -u swp18s1 -pf /var/run/dhcrelay6@BLUE.pid
```

{{< /tab >}}
{{< /tabs >}}

## Use ping or traceroute on a VRF

You can run `ping` or `traceroute` on a VRF from the default VRF.

To ping a VRF from the default VRF, run the `ping` `-I <vrf-name>` command. For example:

```
cumulus@switch:~$ ping -I BLUE
```

To run `traceroute` on a VRF from the default VRF, run the `traceroute -i <vrf-name>` command. For example:

```
cumulus@switch:~$ sudo traceroute -i BLUE
```

## Troubleshooting

You can use vtysh or Linux show commands to troubleshoot VRFs.

{{< tabs "TabID642 ">}}
{{< tab "vtysh Commands ">}}

To show all VRFs learned by FRR from the kernel, run the `show vrf` command. The table ID shows the corresponding routing table in the kernel.

```
cumulus@switch:~$ sudo vtysh
...
switch# show vrf
vrf RED id 14 table 1012
vrf BLUE id 21 table 1013
```

To show the VRFs configured in BGP (including the default VRF), run the `show bgp vrfs` command. A non-zero ID is a VRF that you define in the `/etc/network/interfaces` file.

```
cumulus@switch:~$ sudo vtysh
...
switch# show bgp vrfs
Type  Id     RouterId       #PeersCfg  #PeersEstb  Name
DFLT  0      6.0.0.7                0           0  Default
 VRF  14     6.0.2.7                6           6  RED
 VRF  21     6.0.3.7                6           6  BLUE

Total number of VRFs (including default): 3
```

To show interfaces known to FRR and attached to a specific VRF, run the `show interface vrf <vrf-name>` command. For example:

```
cumulus@switch:~$ sudo vtysh

switch# show interface vrf vrf1012
Interface br2 is up, line protocol is down
  PTM status: disabled
  vrf: RED
  index 13 metric 0 mtu 1500
  flags: <UP,BROADCAST,MULTICAST>
  inet 20.7.2.1/24

  inet6 fe80::202:ff:fe00:a/64
  ND advertised reachable time is 0 milliseconds
  ND advertised retransmit interval is 0 milliseconds
  ND router advertisements are sent every 600 seconds
  ND router advertisements lifetime tracks ra-interval
  ND router advertisement default router preference is medium
  Hosts use stateless autoconfig for addresses.
```

To show VRFs configured in OSPF, run the `show ip ospf vrfs` command. For example:

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip ospf vrfs
Name                            Id     RouterId
Default-IP-Routing-Table        0      0.0.0.0
RED                             57     0.0.0.10
BLUE                            58     0.0.0.20
Total number of OSPF VRFs (including default): 3
```

To show all OSPF routes in a VRF, run the `show ip ospf vrf all route` command. For example:

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip ospf vrf all route
============ OSPF network routing table ============
N    7.0.0.0/24            [10] area: 0.0.0.0
                           directly attached to swp2

============ OSPF router routing table =============

============ OSPF external routing table ===========

============ OSPF network routing table ============
N    8.0.0.0/24            [10] area: 0.0.0.0
                           directly attached to swp1

============ OSPF router routing table =============

============ OSPF external routing table ===========
```

To see the routing table for each VRF, use the `show ip route vrf all` command. The OSPF route is in the row that starts with O.

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip route vrf all
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, P - PIM, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel,
       > - selected route, * - FIB route
VRF BLUE:
K>* 0.0.0.0/0 [0/8192] unreachable (ICMP unreachable)
O   7.0.0.0/24 [110/10] is directly connected, swp2, 00:28:35
C>* 7.0.0.0/24 is directly connected, swp2
C>* 7.0.0.5/32 is directly connected, BLUE
C>* 7.0.0.100/32 is directly connected, BLUE
C>* 50.1.1.0/24 is directly connected, swp31s1
VRF RED:
K>* 0.0.0.0/0 [0/8192] unreachable (ICMP unreachable)
O
8.0.0.0/24 [110/10]
is directly connected, swp1, 00:23:26
C>* 8.0.0.0/24 is directly connected, swp1
C>* 8.0.0.5/32 is directly connected, RED
C>* 8.0.0.100/32 is directly connected, RED
C>* 50.0.1.0/24 is directly connected, swp31s0
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To list all VRFs, and include the VRF ID and table ID, run the `ip -d link show type vrf` command. For example:

```
cumulus@switch:~$ ip -d link show type vrf
14: vrf1012: <NOARP,MASTER,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN mode DEFAULT group default qlen 1000
    link/ether 46:96:c7:64:4d:fa brd ff:ff:ff:ff:ff:ff promiscuity 0
    vrf table 1012 addrgenmode eui64
21: vrf1013: <NOARP,MASTER,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN mode DEFAULT group default qlen 1000
    link/ether 7a:8a:29:0f:5e:52 brd ff:ff:ff:ff:ff:ff promiscuity 0
    vrf table 1013 addrgenmode eui64
28: vrf1014: <NOARP,MASTER,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UNKNOWN mode DEFAULT group default qlen 1000
    link/ether e6:8c:4d:fc:eb:b1 brd ff:ff:ff:ff:ff:ff promiscuity 0
    vrf table 1014 addrgenmode eui64
```

To show the interfaces attached to a specific VRF, run the `ip -d link show vrf <vrf-name>` command. For example:

```
cumulus@switch:~$ ip -d link show vrf vrf1012
8: swp1.2@swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master vrf1012 state UP mode DEFAULT group default
    link/ether 00:02:00:00:00:07 brd ff:ff:ff:ff:ff:ff promiscuity 0
    vlan protocol 802.1Q id 2 <REORDER_HDR>
    vrf_slave addrgenmode eui64
9: swp2.2@swp2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master vrf1012 state UP mode DEFAULT group default
    link/ether 00:02:00:00:00:08 brd ff:ff:ff:ff:ff:ff promiscuity
    vlan protocol 802.1Q id 2 <REORDER_HDR>
    vrf_slave addrgenmode eui64
10: swp3.2@swp3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master vrf1012 state UP mode DEFAULT group default
    link/ether 00:02:00:00:00:09 brd ff:ff:ff:ff:ff:ff promiscuity 0
    vlan protocol 802.1Q id 2 <REORDER_HDR>
    vrf_slave addrgenmode eui64
11: swp4.2@swp4: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master vrf1012 state UP mode DEFAULT group default
    link/ether 00:02:00:00:00:0a brd ff:ff:ff:ff:ff:ff promiscuity 0
    vlan protocol 802.1Q id 2 <REORDER_HDR>
    vrf_slave addrgenmode eui64
12: swp5.2@swp5: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master vrf1012 state UP mode DEFAULT group default
    link/ether 00:02:00:00:00:0b brd ff:ff:ff:ff:ff:ff promiscuity 0
    vlan protocol 802.1Q id 2 <REORDER_HDR>
    vrf_slave addrgenmode eui64
13: br2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master vrf1012 state DOWN mode DEFAULT group default
    link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff promiscuity 0
    bridge forward_delay 100 hello_time 200 max_age 2000 ageing_time 30000 stp_state 0 priority 32768
    vlan_filtering 0 vlan_protocol 802.1Q bridge_id 8000.0:0:0:0:0:0 designated_root 8000.0:0:0:0:0:0
    root_port 0 root_path_cost 0 topology_change 0 topology_change_detected 0 hello_timer    0.00
    tcn_timer    0.00 topology_change_timer    0.00 gc_timer  202.23 vlan_default_pvid 1 group_fwd_mask 0
    group_address 01:80:c2:00:00:00 mcast_snooping 1 mcast_router 1 mcast_query_use_ifaddr 0 mcast_querier 0
    mcast_hash_elasticity 4096 mcast_hash_max 4096 mcast_last_member_count 2 mcast_startup_query_count 2
    mcast_last_member_interval 100 mcast_membership_interval 26000 mcast_querier_interval 25500
    mcast_query_interval 12500 mcast_query_response_interval 1000 mcast_startup_query_interval 3125
    nf_call_iptables 0 nf_call_ip6tables 0 nf_call_arptables 0
    vrf_slave addrgenmode eui64
```

To show IPv4 routes in a VRF, run the `ip route show table <vrf-name>` command. For example:

```
cumulus@switch:~$ ip route show table RED
unreachable default  metric 240
broadcast 20.7.2.0 dev br2  proto kernel  scope link  src 20.7.2.1 dead linkdown
20.7.2.0/24 dev br2  proto kernel  scope link  src 20.7.2.1 dead linkdown
local 20.7.2.1 dev br2  proto kernel  scope host  src 20.7.2.1
broadcast 20.7.2.255 dev br2  proto kernel  scope link  src 20.7.2.1 dead linkdown
broadcast 169.254.2.8 dev swp1.2  proto kernel  scope link  src 169.254.2.9
169.254.2.8/30 dev swp1.2  proto kernel  scope link  src 169.254.2.9
local 169.254.2.9 dev swp1.2  proto kernel  scope host  src 169.254.2.9
broadcast 169.254.2.11 dev swp1.2  proto kernel  scope link  src 169.254.2.9
broadcast 169.254.2.12 dev swp2.2  proto kernel  scope link  src 169.254.2.13
169.254.2.12/30 dev swp2.2  proto kernel  scope link  src 169.254.2.13
local 169.254.2.13 dev swp2.2  proto kernel  scope host  src 169.254.2.13
broadcast 169.254.2.15 dev swp2.2  proto kernel  scope link  src 169.254.2.13
broadcast 169.254.2.16 dev swp3.2  proto kernel  scope link  src 169.254.2.17
169.254.2.16/30 dev swp3.2  proto kernel  scope link  src 169.254.2.17
local 169.254.2.17 dev swp3.2  proto kernel  scope host  src 169.254.2.17
broadcast 169.254.2.19 dev swp3.2  proto kernel  scope link  src 169.254.2.17
```

To show IPv6 routes in a VRF, run the `ip -6 route show table <vrf-name>` command. For example:

```
cumulus@switch:~$ ip -6 route show table RED
local fe80:: dev lo  proto none  metric 0  pref medium
local fe80:: dev lo  proto none  metric 0  pref medium
local fe80:: dev lo  proto none  metric 0  pref medium
local fe80:: dev lo  proto none  metric 0  pref medium
local fe80::202:ff:fe00:7 dev lo  proto none  metric 0  pref medium
local fe80::202:ff:fe00:8 dev lo  proto none  metric 0  pref medium
local fe80::202:ff:fe00:9 dev lo  proto none  metric 0  pref medium
local fe80::202:ff:fe00:a dev lo  proto none  metric 0  pref medium
fe80::/64 dev br2  proto kernel  metric 256 dead linkdown  pref medium
fe80::/64 dev swp1.2  proto kernel  metric 256  pref medium
fe80::/64 dev swp2.2  proto kernel  metric 256  pref medium
fe80::/64 dev swp3.2  proto kernel  metric 256  pref medium
ff00::/8 dev br2  metric 256 dead linkdown  pref medium
ff00::/8 dev swp1.2  metric 256  pref medium
ff00::/8 dev swp2.2  metric 256  pref medium
ff00::/8 dev swp3.2  metric 256  pref medium
unreachable default dev lo  metric 240  error -101 pref medium
```

To see a list of links associated with a particular VRF table, run the `ip link list <vrf-name>` command. For example:

```
cumulus@switch:~$ ip link list RED

VRF: RED
--------------------
swp1.10@swp1     UP             6c:64:1a:00:5a:0c <BROADCAST,MULTICAST,UP,LOWER_UP>
swp2.10@swp2     UP             6c:64:1a:00:5a:0d <BROADCAST,MULTICAST,UP,LOWER_UP>
```

To see a list of routes associated with a particular VRF table, run the `ip route list <vrf-name>` command. For example:

```
cumulus@switch:~$ ip route list RED

VRF: RED
--------------------
unreachable default  metric 8192
10.1.1.0/24 via 10.10.1.2 dev swp2.10
10.1.2.0/24 via 10.99.1.2 dev swp1.10
broadcast 10.10.1.0 dev swp2.10  proto kernel  scope link  src 10.10.1.1
10.10.1.0/28 dev swp2.10  proto kernel  scope link  src 10.10.1.1
local 10.10.1.1 dev swp2.10  proto kernel  scope host  src 10.10.1.1
broadcast 10.10.1.15 dev swp2.10  proto kernel  scope link  src 10.10.1.1
broadcast 10.99.1.0 dev swp1.10  proto kernel  scope link  src 10.99.1.1
10.99.1.0/30 dev swp1.10  proto kernel  scope link  src 10.99.1.1
local 10.99.1.1 dev swp1.10  proto kernel  scope host  src 10.99.1.1
broadcast 10.99.1.3 dev swp1.10  proto kernel  scope link  src 10.99.1.1

local fe80:: dev lo  proto none  metric 0  pref medium
local fe80:: dev lo  proto none  metric 0  pref medium
local fe80::6e64:1aff:fe00:5a0c dev lo  proto none  metric 0  pref medium
local fe80::6e64:1aff:fe00:5a0d dev lo  proto none  metric 0  pref medium
fe80::/64 dev swp1.10  proto kernel  metric 256  pref medium
fe80::/64 dev swp2.10  proto kernel  metric 256  pref medium
ff00::/8 dev swp1.10  metric 256  pref medium
ff00::/8 dev swp2.10  metric 256  pref medium
unreachable default dev lo  metric 8192  error -101 pref medium
```

{{%notice tip%}}
You can also show routes in a VRF using the `ip [-6] route show vrf <vrf-name>` command. This command omits local and broadcast routes, which can clutter the output.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Considerations

- Cumulus Linux bases table selection on the incoming interface only; packet attributes or output-interface-based selection are not available.
- Setting the router ID outside of BGP using the `router-id` option causes all BGP instances to get the same router ID. If you want each BGP instance to have its own router ID, specify the `router-id` under the BGP instance using `bgp router-id`. If you specify both `router-id` and `bgp router-id`, the ID under the BGP instance overrides the one you provide outside BGP.
- You cannot configure {{<link url="Basic-Configuration/#enable-evpn-between-bgp-neighbors" text="EVPN address families">}} within a VRF.
- When you take down a VRF using `ifdown`, Cumulus Linux removes all routes associated with that VRF from FRR but it does *not* remove the routes from the kernel.
