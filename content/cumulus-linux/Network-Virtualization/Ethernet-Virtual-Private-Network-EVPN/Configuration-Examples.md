---
title: Configuration Examples
author: Cumulus Networks
weight: 358
aliases:
 - /display/DOCS/EVPN+Configuration+Examples
 - /pages/viewpage.action?pageId=12910740
product: Cumulus Linux
version: '4.0'
---
This section shows the following configuration examples:

- Basic Clos (4x2) for bridging
- Clos with MLAG and centralized routing
- Clos with MLAG and asymmetric routing
- Basic Clos with symmetric routing and exit leafs

## Basic Clos (4x2) for Bridging

The following example configuration shows a basic Clos topology for bridging.

{{< img src = "/images/cumulus-linux/evpn-basic-clos.png" >}}

### leaf01 and leaf02 Configurations

<details>

<summary>leaf01 /etc/network/interfaces </summary>

```
cumulus@leaf01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.7/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  920
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.10
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.8

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto VxLanA-1
iface VxLanA-1
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1001
    bridge-pvid 1

auto vlan1
iface vlan1
    vlan-id 1
    vlan-raw-device VxLanA-1
    ip-forward off

auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device VxLanA-1
    ip-forward off

auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device VxLanA-1
    ip-forward off
```

</details>

<details>

<summary>leaf02 /etc/network/interfaces </summary>

```
cumulus@leaf02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.8/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.9
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.7

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto VxLanA-1
iface VxLanA-1
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1001
    bridge-pvid 1

auto vlan1
iface vlan1
    vlan-id 1
    vlan-raw-device VxLanA-1
    ip-forward off

auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device VxLanA-1
    ip-forward off

auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device VxLanA-1
    ip-forward off
```

</details>

<details>

<summary>leaf01 /etc/frr/frr.conf </summary>

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65542
 bgp router-id 10.0.0.7
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>leaf02 /etc/frr/frr.conf </summary>

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65543
 bgp router-id 10.0.0.8
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### leaf03 and leaf04 Configurations

<details>

<summary>leaf03 /etc/network/interfaces </summary>

```
cumulus@leaf03:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.9/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.9

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.10
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.10

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto VxLanA-1
iface VxLanA-1
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1001
    bridge-pvid 1

auto vlan1
iface vlan1
    vlan-id 1
    vlan-raw-device VxLanA-1
    ip-forward off

auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device VxLanA-1
    ip-forward off

auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device VxLanA-1
    ip-forward off
```

</details>

<details>

<summary>leaf04 /etc/network/interfaces </summary>

```
cumulus@leaf04:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.10/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.9

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.9
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.9

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto VxLanA-1
iface VxLanA-1
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1001
    bridge-pvid 1

auto vlan1
iface vlan1
    vlan-id 1
    vlan-raw-device VxLanA-1
    ip-forward off

auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device VxLanA-1
    ip-forward off

auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device VxLanA-1
    ip-forward off
```

</details>

<details>

<summary>leaf03 /etc/frr/frr.conf </summary>

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65544
 bgp router-id 10.0.0.9
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>leaf04 /etc/frr/frr.conf </summary>

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65545
 bgp router-id 10.0.0.10
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### spine01 and spine02 Configurations

<details>

<summary>spine01 /etc/network/interfaces </summary>

```
cumulus@spine01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.5/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202

auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202

auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202

```

</details>

<details>

<summary>spine02 /etc/network/interfaces </summary>

```
cumulus@spine02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.6/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202

auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202

auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202
```

</details>

<details>

<summary>spine01 /etc/frr/frr.conf </summary>

```
cumulus@spine01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.5
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>spine02 /etc/frr/frr.conf </summary>

```
cumulus@spine02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.6
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

## Clos Configuration with MLAG and Centralized Routing

The following example configuration shows a basic Clos topology with
centralized routing. MLAG is configured between leaf switches.

{{< img src = "/images/cumulus-linux/evpn-centralized.png" >}}

### leaf01 and leaf02 Configurations

<details>

<summary>leaf01 /etc/network/interfaces </summary>

```
cumulus@leaf01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.7/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.8

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.2/24
    address 2001:fee1::2/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.2/24
    address 2001:fee1:0:1::2/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.2/24
    address 2001:fee1:0:2::2/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.2/24
    address 2001:fee1:0:3::2/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

</details>

<details>

<summary>leaf02 /etc/network/interfaces </summary>

```
cumulus@leaf02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.8/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.7

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.3/24
    address 2001:fee1::3/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.3/24
    address 2001:fee1:0:1::3/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.3/24
    address 2001:fee1:0:2::3/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.3/24
    address 2001:fee1:0:3::3/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

</details>

<details>
<summary>leaf01 /etc/frr/frr.conf </summary>

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65542
 bgp router-id 10.0.0.7
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-default-gw
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>leaf02 /etc/frr/frr.conf </summary>

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65543
 bgp router-id 10.0.0.8
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-default-gw
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### leaf03 and leaf04 Configurations

<details>

<summary>leaf03 /etc/network/interfaces </summary>

```
cumulus@leaf03:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.9/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.9

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.10

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device bridge
    ip-forward off

auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device bridge
    ip-forward off

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    vlan-id 1002
    vlan-raw-device bridge
    ip-forward off

auto vlan1003
iface vlan1003
    vlan-id 1003
    vlan-raw-device bridge
    ip-forward off

```

</details>

<details>

<summary>leaf04 /etc/network/interfaces </summary>

```
cumulus@leaf04:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.10/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.9

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.9

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device bridge
    ip-forward off

auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device bridge
    ip-forward off

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    vlan-id 1002
    vlan-raw-device bridge
    ip-forward off

auto vlan1003
iface vlan1003
    vlan-id 1003
    vlan-raw-device bridge
    ip-forward off
```

</details>

<details>

<summary>leaf03 /etc/frr/frr.conf </summary>

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65544
 bgp router-id 10.0.0.9
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>leaf04 /etc/frr/frr.conf </summary>

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65545
 bgp router-id 10.0.0.10
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### spine01 and spine02 Configurations

<details>

<summary>spine01 /etc/network/interfaces </summary>

```
cumulus@spine01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.5/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202

auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202

auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202<
```

</details>

<details>

<summary>spine02 /etc/network/interfaces </summary>

```
cumulus@spine02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.6/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202

auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202

auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202

```

</details>

<details>

<summary>spine01 /etc/frr/frr.conf </summary>

```
cumulus@spine01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.5
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>spine02 /etc/frr/frr.conf </summary>

```
cumulus@spine02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.6
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

## Clos Configuration with MLAG and EVPN Asymetric Routing

The following example configuration is a basic Clos topology with EVPN asymmetric routing. MLAG is configured between leaf switches.

{{< img src = "/images/cumulus-linux/evpn-asymmetric.png" >}}

### leaf01 and leaf02 Configurations

<details>

<summary>leaf01 /etc/network/interfaces </summary>

```
cumulus@leaf01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.7/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.8

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.7
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.2/24
    address 2001:fee1::2/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.2/24
    address 2001:fee1:0:1::2/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.2/24
    address 2001:fee1:0:2::2/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.2/24
    address 2001:fee1:0:3::2/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

</details>

<details>

<summary>leaf02 /etc/network/interfaces </summary>

```
cumulus@leaf02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.8/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.7

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.8
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.3/24
    address 2001:fee1::3/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.3/24
    address 2001:fee1:0:1::3/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.3/24
    address 2001:fee1:0:2::3/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.3/24
    address 2001:fee1:0:3::3/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

</details>

<details>

<summary>leaf01 /etc/frr/frr.conf </summary>

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65542
 bgp router-id 10.0.0.7
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>leaf02 /etc/frr/frr.conf </summary>

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65543
 bgp router-id 10.0.0.8
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### leaf03 and leaf04 Configurations

<details>

<summary>leaf03 /etc/network/interfaces </summary>

```
cumulus@leaf03:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.9/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 36.0.0.9

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.10

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.9
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.2/24
    address 2001:fee1::2/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.2/24
    address 2001:fee1:0:1::2/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.2/24
    address 2001:fee1:0:2::2/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.2/24
    address 2001:fee1:0:3::2/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

</details>

<details>

<summary>leaf04 /etc/network/interfaces </summary>

```
cumulus@leaf04:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.10/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 36.0.0.9

auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202

auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202

auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.9

auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000

auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001

auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.10
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1

auto vrf1
iface vrf1
    vrf-table auto

auto vlan1000
iface vlan1000
    address 45.0.0.3/24
    address 2001:fee1::3/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1

auto vlan1001
iface vlan1001
    address 45.0.1.3/24
    address 2001:fee1:0:1::3/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1

auto vrf2
iface vrf2
    vrf-table auto

auto vlan1002
iface vlan1002
    address 45.0.2.3/24
    address 2001:fee1:0:2::3/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2

auto vlan1003
iface vlan1003
    address 45.0.3.3/24
    address 2001:fee1:0:3::3/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2
```

</details>

<details>

<summary>leaf03 /etc/frr/frr.conf </summary>

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65544
 bgp router-id 10.0.0.9
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>leaf04 /etc/frr/frr.conf </summary>

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65545
 bgp router-id 10.0.0.10
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### spine01 and spine02 Configurations

<details>

<summary>spine01 /etc/network/interfaces </summary>

```
cumulus@spine01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.5/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202

auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202

auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202
```

</details>

<details>

<summary>spine02 /etc/network/interfaces </summary>

```
cumulus@spine02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)

# The primary network interface
auto eth0
iface eth0 inet dhcp

# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if

auto lo
iface lo
    address 10.0.0.6/32
    alias BGP un-numbered Use for Vxlan Src Tunnel

auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202

auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202

auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202

auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202
```

</details>

<details>

<summary>spine01 /etc/frr/frr.conf </summary>

```
cumulus@spine01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.5
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>spine02 /etc/frr/frr.conf </summary>

```
cumulus@spine02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.6
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

## Basic Clos Configuration with EVPN Symmetric Routing

The following example configuration is a basic Clos topology with EVPN
symmetric routing with external prefix (type-5) routing via dual,
non-MLAG exit leafs connected to an edge router. Here is the topology
diagram:

{{< img src = "/images/cumulus-linux/evpn-symmetric.png" >}}

### leaf01 and leaf02 Configurations

<details>

<summary>leaf01 /etc/network/interfaces </summary>

```
cumulus@leaf01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2

auto lo:1
iface lo:1
    address 10.0.0.1/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000

# L2 interfaces - ports, vxlan and bridge
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3
    bridge-access 110

auto swp4
iface swp4
    bridge-access 110

auto swp5
iface swp5
    bridge-access 210

auto swp6
iface swp6
    bridge-access 210

auto vni110
iface vni110
    vxlan-id 10110
    vxlan-local-tunnelip 10.0.0.1
    bridge-access 110

auto vni210
iface vni210
    vxlan-id 10210
    vxlan-local-tunnelip 10.0.0.1
    bridge-access 210

auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.1
    bridge-access 4001

auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.1
    bridge-access 4002

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3 swp4 swp5 swp6 vni110 vni210 vni4001 vni4002
    bridge-stp on
    bridge-vids 110 210

# Tenants (VRFs)
auto vrf1
iface vrf1
    vrf-table auto

auto vrf2
iface vrf2
    vrf-table auto

# Tenant SVIs - anycast GW
auto vlan110
iface vlan110
    address 172.16.120.1/24
    vlan-id 110
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1

auto vlan210
iface vlan210
    address 172.16.130.1/24
    vlan-id 210
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2

# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2
```

</details>

<details>

<summary>leaf02 /etc/network/interfaces </summary>

```
cumulus@leaf02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2

auto lo:1
iface lo:1
    address 10.0.0.2/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000

# L2 interfaces - ports, vxlan and bridge
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3
    bridge-access 120

auto swp4
iface swp4
    bridge-access 120

auto swp5
iface swp5
    bridge-access 220

auto swp6
iface swp6
    bridge-access 220

auto vni120
iface vni120
    vxlan-id 10120
    vxlan-local-tunnelip 10.0.0.2
    bridge-access 120

auto vni220
iface vni220
    vxlan-id 10220
    vxlan-local-tunnelip 10.0.0.2
    bridge-access 220

auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.2
    bridge-access 4001

auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.2
    bridge-access 4002

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3 swp4 swp5 swp6 vni120 vni220 vni4001 vni4002
    bridge-stp on
    bridge-vids 120 220
# Tenants (VRFs)
auto vrf1
iface vrf1
    vrf-table auto

auto vrf2
iface vrf2
    vrf-table auto

# Tenant SVIs - anycast GW
auto vlan120
iface vlan120
    address 172.16.120.2/24
    vlan-id 120
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1

auto vlan220
iface vlan220
    address 172.16.130.2/24
    vlan-id 220
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2

# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2
```

</details>

<details>

<summary>leaf01 /etc/frr/frr.conf </summary>

```
cumulus@leaf01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65001
 bgp router-id 10.0.0.1
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.1/32
 exit-address-family
!
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>leaf02 /etc/frr/frr.conf </summary>

```
cumulus@leaf02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65002
 bgp router-id 10.0.0.2
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.2/32
 exit-address-family
!
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### leaf03 and leaf04 Configurations

<details>

<summary>leaf03 /etc/network/interfaces </summary>

```
cumulus@leaf03:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2

auto lo:1
iface lo:1
    address 10.0.0.3/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000

# L2 interfaces - ports, vxlan and bridge
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3
    bridge-access 130

auto swp4
iface swp4
    bridge-access 130

auto swp5
iface swp5
    bridge-access 230

auto swp6
iface swp6
    bridge-access 230

auto vni130
iface vni130
    vxlan-id 10130
    vxlan-local-tunnelip 10.0.0.3
    bridge-access 130

auto vni230
iface vni230
    vxlan-id 10230
    vxlan-local-tunnelip 10.0.0.3
    bridge-access 230

auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.3
    bridge-access 4001

auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.3
    bridge-access 4002

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3 swp4 swp5 swp6 vni130 vni230 vni4001 vni4002
    bridge-stp on
    bridge-vids 130 230

# Tenants (VRFs)
auto vrf1
iface vrf1
    vrf-table auto

auto vrf2
iface vrf2
    vrf-table auto

# Tenant SVIs - anycast GW
auto vlan130
iface vlan130
    address 172.16.120.3/24
    vlan-id 130
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1

auto vlan230
iface vlan230
    address 172.16.130.3/24
    vlan-id 230
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2

# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2
```

</details>

<details>

<summary>leaf04 /etc/network/interfaces </summary>

```
cumulus@leaf04:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2

auto lo:1
iface lo:1
    address 10.0.0.4/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000

# L2 interfaces - ports, vxlan and bridge
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3
    bridge-access 140

auto swp4
iface swp4
    bridge-access 140

auto swp5
iface swp5
    bridge-access 240

auto swp6
iface swp6
    bridge-access 240

auto vni140
iface vni140
    vxlan-id 10140
    vxlan-local-tunnelip 10.0.0.4
    bridge-access 140

auto vni240
iface vni240
    vxlan-id 10240
    vxlan-local-tunnelip 10.0.0.4
    bridge-access 240

auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.4
    bridge-access 4001

auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.4
    bridge-access 4002

auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3 swp4 swp5 swp6 vni140 vni240 vni4001 vni4002
    bridge-stp on
    bridge-vids 140 240

# Tenants (VRFs)
auto vrf1
iface vrf1
    vrf-table auto

auto vrf2
iface vrf2
    vrf-table auto

# Tenant SVIs - anycast GW
auto vlan140
iface vlan140
    address 172.16.120.4/24
    vlan-id 140
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1

auto vlan240
iface vlan240
    address 172.16.130.4/24
    vlan-id 240
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2

# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2
```

</details>

<details>

<summary>leaf03 /etc/frr/frr.conf </summary>

```
cumulus@leaf03:~$ cat /etc/frr/frr.conf 

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65003
 bgp router-id 10.0.0.3
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.3/32
 exit-address-family
!
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>leaf04 /etc/frr/frr.conf </summary>

```
cumulus@leaf04:~$ cat /etc/frr/frr.conf

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65004
 bgp router-id 10.0.0.4
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.4/32
 exit-address-family
!
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
router bgp 65004 vrf vrf1
 bgp router-id 172.16.120.4
 neighbor 172.16.120.100 remote-as external
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
router bgp 65004 vrf vrf2
 bgp router-id 172.16.130.4
 neighbor 172.16.130.100 remote-as external
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### spine01 and spine02 Configurations

<details>

<summary>spine01 /etc/network/interfaces </summary>

```
cumulus@spine01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2

auto lo:1
iface lo:1
    address 172.16.110.1/24

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4

auto swp5
iface swp5

auto swp6
iface swp6
```

</details>

<details>

<summary>spine02 /etc/network/interfaces </summary>

```
cumulus@spine02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2

auto lo:1
iface lo:1
    address 172.16.110.2/24

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4

auto swp5
iface swp5

auto swp6
iface swp6
```

</details>

<details>

<summary>spine01 /etc/frr/frr.conf </summary>

```
cumulus@spine01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
router bgp 65100
 bgp router-id 172.16.110.1
 neighbor LEAF peer-group
 neighbor LEAF remote-as external
 neighbor LEAF timers 10 30
 neighbor swp1 interface peer-group LEAF
 neighbor swp2 interface peer-group LEAF
 neighbor swp3 interface peer-group LEAF
 neighbor swp4 interface peer-group LEAF
 neighbor BORDER-LEAF peer-group
 neighbor BORDER-LEAF remote-as external
 neighbor BORDER-LEAF timers 10 30
 neighbor swp5 interface peer-group BORDER-LEAF
 neighbor swp6 interface peer-group BORDER-LEAF
 !
 address-family ipv4 unicast
  network 172.16.110.1/24
  neighbor LEAF activate
  neighbor BORDER-LEAF activate
  neighbor LEAF route-reflector-client
  neighbor BORDER-LEAF route-reflector-client
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor LEAF activate
  neighbor BORDER-LEAF activate
  neighbor LEAF route-reflector-client
  neighbor BORDER-LEAF route-reflector-client
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>spine02 /etc/frr/frr.conf </summary>

```
cumulus@spine02:~$ cat /etc/frr/frr.conf

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
router bgp 65100
 bgp router-id 172.16.110.2
 neighbor LEAF peer-group
 neighbor LEAF remote-as external
 neighbor LEAF timers 10 30
 neighbor swp1 interface peer-group LEAF
 neighbor swp2 interface peer-group LEAF
 neighbor swp3 interface peer-group LEAF
 neighbor swp4 interface peer-group LEAF
 neighbor BORDER-LEAF peer-group
 neighbor BORDER-LEAF remote-as external
 neighbor BORDER-LEAF timers 10 30
 neighbor swp5 interface peer-group BORDER-LEAF
 neighbor swp6 interface peer-group BORDER-LEAF
 !
 address-family ipv4 unicast
  network 172.16.110.2/24
  neighbor LEAF activate
  neighbor BORDER-LEAF activate
  neighbor LEAF route-reflector-client
  neighbor BORDER-LEAF route-reflector-client
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor LEAF activate
  neighbor BORDER-LEAF activate
  neighbor LEAF route-reflector-client
  neighbor BORDER-LEAF route-reflector-client
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### border-leaf01 and border-leaf02 Configurations

<details>

<summary>border-leaf01 /etc/network/interfaces </summary>

```
cumulus@border-leaf01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

auto lo:1
iface lo:1
    address 10.0.0.5/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000

# Physical interfaces
auto swp1s0
iface swp1s0

auto swp1s1
iface swp1s1

auto swp1s2
iface swp1s2
    bridge-vids 2001 2002

auto swp1s3
iface swp1s3
    bridge-access 150

auto swp2s0
iface swp2s0
    bridge-access 250

auto vni150
iface vni150
    vxlan-id 10150
    vxlan-local-tunnelip 10.0.0.5
    bridge-access 150

auto vni250
iface vni250
    vxlan-id 10250
    vxlan-local-tunnelip 10.0.0.5
    bridge-access 250

# Tenant VRFs
auto vrf1
iface vrf1
    vrf-table auto

auto vrf2
iface vrf2
    vrf-table auto

# VxLAN interfaces (VLAN to VNI mappings)
# Need only the L3 VxLAN interfaces
auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.5
    bridge-access 4001

auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.5
    bridge-access 4002

# Bridge
auto bridge
iface bridge
      bridge-vlan-aware yes
      bridge-ports swp4 swp5 vni160 vni260 vni4001 vni4002
      bridge-stp on
      bridge-vids 160 260 2001 2002

# Tenant SVIs - anycast GW
auto vlan160
iface vlan160
    address 172.16.120.1/24
    vlan-id 160
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1

auto vlan260
iface vlan260
    address 172.16.130.2/24
    vlan-id 260
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2

# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2

# External-facing L3 VLAN interface per tenant (towards WAN edge)
#auto swp1s2.4001
#iface swp1s2.4001
#    address 172.16.100.2/30
#    vrf vrf1
#
#auto swp1s2.4002
#iface swp1s2.4002
#    address 172.16.100.6/30
#    vrf vrf2
#
# configuration below is a workaround for RN-766
#
auto vlan2001
iface vlan2001
    vlan-id 2001
    vlan-raw-device bridge
    vrf vrf1
    address 172.16.100.2/30

auto vlan2002
iface vlan2002
    vlan-id 2002
    vlan-raw-device bridge
    vrf vrf2
    address 172.16.100.6/30

auto vni16001
iface vni16001
    vxlan-id 16001
    vxlan-local-tunnelip 10.0.0.5
    bridge-access 2001

auto vni16002
iface vni16002
    vxlan-id 16002
    vxlan-local-tunnelip 10.0.0.5
    bridge-access 2002
```

</details>

<details>

<summary>border-leaf02 /etc/network/interfaces </summary>

```
cumulus@border-leaf02:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2

auto lo:1
iface lo:1
    address 10.0.0.6/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000

# Physical interfaces
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4
    bridge-access 160

auto swp5
iface swp5
    bridge-access 260

auto vni160
iface vni160
    vxlan-id 10160
    vxlan-local-tunnelip 10.0.0.6
    bridge-access 160

auto vni260
iface vni260
    vxlan-id 10260
    vxlan-local-tunnelip 10.0.0.6
    bridge-access 260

# Tenant VRFs
auto vrf1
iface vrf1
    vrf-table auto

auto vrf2
iface vrf2
    vrf-table auto

# VxLAN interfaces (VLAN to VNI mappings)
# Need only the L3 VxLAN interfaces
auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.6
    bridge-access 4001

auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.6
    bridge-access 4002

# Bridge
auto bridge
iface bridge
      bridge-vlan-aware yes
      bridge-ports swp4 swp5 vni160 vni260 vni4001 vni4002
      bridge-stp on
      bridge-vids 160 260 2001 2002

# Tenant SVIs - anycast GW
auto vlan160
iface vlan160
    address 172.16.120.1/24
    vlan-id 160
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1

auto vlan260
iface vlan260
    address 172.16.130.2/24
    vlan-id 260
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2

# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1

auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2

# External-facing L3 VLAN interface per tenant (towards WAN edge)
# auto swp3.4001
# iface swp3.4001
#     address 172.16.101.2/30
#     vrf vrf1
#  
# auto swp3.4002
# iface swp3.4002
#     address 172.16.101.6/30
#     vrf vrf2
#
# configuration below is a workaround for RN-766
#
auto vlan2001
iface vlan2001
    vlan-id 2001
    vlan-raw-device bridge
    vrf vrf1
    address 172.16.101.2/30

auto vlan2002
iface vlan2002
    vlan-id 2002
    vlan-raw-device bridge
    vrf vrf2
    address 172.16.101.6/30

auto vni16001
iface vni16001
    vxlan-id 16001
    vxlan-local-tunnelip 10.0.0.6
    bridge-access 2001

auto vni16002
iface vni16002
    vxlan-id 16002
    vxlan-local-tunnelip 10.0.0.6
    bridge-access 2002
```

</details>

<details>

<summary>border-leaf01 /etc/frr/frr.conf </summary>

```
cumulus@border-leaf01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1s0
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp1s1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65005
 bgp router-id 10.0.0.5
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 1200 4800
 neighbor swp1s0 interface peer-group SPINE
 neighbor swp1s1 interface peer-group SPINE
 neighbor 172.16.100.1 remote-as external
 neighbor 172.16.100.5 remote-as external
 !
 address-family ipv4 unicast
  network 10.0.0.5/32
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
router bgp 65005 vrf vrf1
 bgp router-id 172.16.100.2
 neighbor 172.16.100.1 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
router bgp 65005 vrf vrf2
 bgp router-id 172.16.100.6
 neighbor 172.16.100.5 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

<details>

<summary>border-leaf02 /etc/frr/frr.conf </summary>

```
cumulus@border-leaf02:~$ cat /etc/frr/frr.conf 

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65005
 bgp router-id 10.0.0.6
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 neighbor 172.16.101.1 remote-as external
 neighbor 172.16.101.5 remote-as external
 !
 address-family ipv4 unicast
  network 10.0.0.6/32
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
router bgp 65005 vrf vrf1
 bgp router-id 172.16.100.2
 neighbor 172.16.100.1 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
router bgp 65005 vrf vrf2
 bgp router-id 172.16.100.6
 neighbor 172.16.100.5 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
line vty
 exec-timeout 0 0
!
```

</details>

### router01 Configurations

<details>

<summary>router01 /etc/network/interfaces </summary>

```
cumulus@router01:~$ cat /etc/network/interfaces

# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2

auto lo:1
iface lo:1
    address 120.0.0.1/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000

auto swp1
iface swp1

auto swp1.2001
iface swp1.2001
    address 172.16.100.1/24

auto swp1.2002
iface swp1.2002
    address 172.16.100.5/24

auto swp2
iface swp2

auto swp2.2001
iface swp2.2001
    address 172.16.101.1/24

auto swp2.2002
iface swp2.2002
    address 172.16.101.5/24

auto swp3
iface swp3
    address 81.1.1.1/24

auto swp4
iface swp4
    address 81.1.2.1/24

auto swp5
iface swp5
    address 81.1.3.1/24

auto swp6
iface swp6
    address 81.1.4.1/24
```

</details>

<details>

<summary>router01 /etc/frr/frr.conf </summary>

```
cumulus@router01:~$ cat /etc/frr/frr.conf

log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
router bgp 65200
 bgp router-id 120.0.0.1
 neighbor 172.16.100.2 remote-as external
 neighbor 172.16.100.6 remote-as external
 neighbor 172.16.101.2 remote-as external
 neighbor 172.16.101.6 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected route-map HOST_ALLOW
 exit-address-family
!
ip prefix-list HOSTS seq 1 permit 81.1.1.0/24
ip prefix-list HOSTS seq 2 permit 81.1.2.0/24
ip prefix-list HOSTS seq 3 permit 81.1.3.0/24
ip prefix-list HOSTS seq 4 permit 81.1.4.0/24
ip prefix-list HOSTS seq 5 deny any
!
route-map HOST_ALLOW permit 1
 match ip address prefix-list HOSTS
!
!
line vty
 exec-timeout 0 0
!
```
