---
title: 'Configure the Topology'
author: Cumulus Networks
weight: 26
product: Cumulus VX
version: '3.7'
---
After you have set up the Cumulus VX on your preferred platform (installed the relevant platforms and Cumulus VX images, and created three VMs with point-to-point connections between them), follow these steps to configure network interfaces and FRRouting on the two-leaf and one spine topology:

- The spine VM represents the spine (aggregation layer) switch on the network
- The two leaf VMs represent the leaf (access layer) switches on the network

{{< figure src = "/images/cumulus-vx/network-topology.png" >}}

The following configuration uses unnumbered IP addressing, with the same /32 IPv4 address on multiple ports. OSPF unnumbered does not have an equivalent to RFC-5549, so you need to use an IPv4 address to bring up the adjacent OSPF neighbors, allowing you to reuse the same IP address. You can see some example
{{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/202796476-OSPF-Unnumbered-Sample-Configurations" text="unnumbered OSPF configurations">}} in the knowledge base.

## Configure leaf01

You can configure each of the VMs with the Network Command Line Utility (NCLU) or by editing the `/etc/network/interfaces` and `/etc/frr/frr.conf` files.

1. Log into the leaf01 VM using the default credentials:

   - username: cumulus
   - password: CumulusLinux!

2. As the sudo user, edit the `/etc/frr/daemons` file in a text editor. Set `zebra`, `bgpd`, and `ospfd` to **yes**, and save the file.

   ```
   cumulus@switch:~$ sudo nano /etc/frr/daemons

   zebra=yes
   bgpd=yes
   ospfd=yes
   ...
   ```

3. Run the following commands to configure the switch:

   {{< tabs "TabID01 ">}}

   {{< tab "NCLU Commands ">}}

   ```
   cumulus@switch:~$ net add loopback lo ip address 10.2.1.1/32
   cumulus@switch:~$ net add interface swp1 ip address 10.2.1.1/32
   cumulus@switch:~$ net add interface swp2 ip address 10.2.1.1/32
   cumulus@switch:~$ net add interface swp3 ip address 10.4.1.1/24
   cumulus@switch:~$ net add interface swp1 ospf network point-to-point
   cumulus@switch:~$ net add interface swp2 ospf network point-to-point
   cumulus@switch:~$ net add ospf router-id 10.2.1.1
   cumulus@switch:~$ net add ospf network 10.2.1.1/32 area 0.0.0.0
   cumulus@switch:~$ net add ospf network 10.4.1.0/24 area 0.0.0.0
   cumulus@switch:~$ net pending
   cumulus@switch:~$ net commit
   ```

   These commands configure both `/etc/network/interfaces` and `/etc/frr/frr.conf`.

   {{< /tab >}}

   {{< tab "Edit the Configuration Files Manually ">}}

   As the sudo user, edit the `/etc/network/interfaces` and the `/etc/frr/frr.conf` files. Copy the configurations below.

   ```
   cumulus@switch:~$ sudo nano /etc/network/interfaces

   # The loopback network interface
   auto lo
   iface lo inet loopback
      address 10.2.1.1/32

   # The primary network interface
   auto eth0
   iface eth0 inet dhcp

   auto swp1
   iface swp1
      address 10.2.1.1/32

    auto swp2
    iface swp2
       address 10.2.1.1/32

   auto swp3
   iface swp3
      address 10.4.1.1/24
   ```

   ```
   cumulus@switch:~$ sudo nano /etc/frr/frr.conf

   service integrated-vtysh-config

   interface swp1
    ip ospf network point-to-point

   interface swp2
       ip ospf network point-to-point

        router-id 10.2.1.1
  
        router ospf
          ospf router-id 10.2.1.1
          network 10.2.1.1/32 area 0.0.0.0
          network 10.4.1.0/24 area 0.0.0.0
   ```

    {{< /tab >}}

    {{< /tabs >}}

4. Restart the networking service and then FRRouting:

   ```
   cumulus@switch:~$ sudo systemctl restart networking
   cumulus@switch:~$ sudo systemctl restart frr.service
   ```

5. Configure leaf02 and spine01. The configuration steps for leaf02 and spine01 are the same as leaf01; however, the file configurations are different. Listed below are the configurations for leaf02 and leaf02:

{{< tabs "TabID02 ">}}

{{< tab "leaf02 ">}}

NCLU Commands:

```
cumulus@switch:~$ net add loopback lo ip address 10.2.1.2/32
cumulus@switch:~$ net add interface swp1 ip address 10.2.1.2/32
cumulus@switch:~$ net add interface swp2 ip address 10.2.1.2/32
cumulus@switch:~$ net add interface swp3 ip address 10.4.2.1/24
cumulus@switch:~$ net add interface swp1 ospf network point-to-point
cumulus@switch:~$ net add interface swp2 ospf network point-to-point
cumulus@switch:~$ net add ospf router-id 10.2.1.2
cumulus@switch:~$ net add ospf network 10.2.1.2/32 area 0.0.0.0
cumulus@switch:~$ net add ospf network 10.4.2.0/24 area 0.0.0.0
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

`etc/network/interfaces` File:

```
# The loopback network interface
auto lo
iface lo inet loopback
    address 10.2.1.2/32

# The primary network interface
auto eth0
iface eth0 inet dhcp
auto swp1
iface swp1
    address 10.2.1.2/32

auto swp2
iface swp2
    address 10.2.1.2/32

auto swp3
iface swp3
    address 10.4.2.1/24
```

`/etc/frr/frr.conf` File:

```
service integrated-vtysh-config

interface swp1
ip ospf network point-to-point

interface swp2
    ip ospf network point-to-point

    router-id 10.2.1.2

    router ospf
    ospf router-id 10.2.1.2
    network 10.2.1.2/32 area 0.0.0.0  
    network 10.4.2.0/24 area 0.0.0.0
```

{{< /tab >}}

{{< tab "spine01 ">}}

NCLU Commands:

```
cumulus@switch:~$ net add loopback lo ip address 10.2.1.3/32
cumulus@switch:~$ net add interface swp1 ip address 10.2.1.3/32
cumulus@switch:~$ net add interface swp2 ip address 10.2.1.3/32
cumulus@switch:~$ net add interface swp3 ip address 10.4.3.1/24
cumulus@switch:~$ net add interface swp1 ospf network point-to-point
cumulus@switch:~$ net add interface swp2 ospf network point-to-point
cumulus@switch:~$ net add ospf router-id 10.2.1.3
cumulus@switch:~$ net add ospf network 10.2.1.3/32 area 0.0.0.0
cumulus@switch:~$ net add ospf network 10.4.3.0/24 area 0.0.0.0
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

`/etc/network/interfaces` File:

```
# The loopback network interface
auto lo
iface lo inet loopback
    address 10.2.1.3/32

# The primary network interface
auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1
    address 10.2.1.3/32

auto swp2
iface swp2
    address 10.2.1.3/32

auto swp3
iface swp3
    address 10.4.3.1/24
```

`/etc/frr/frr.conf` File:

```
service integrated-vtysh-config

interface swp1
  ip ospf network point-to-point

interface swp2
  ip ospf network point-to-point

  router-id 10.2.1.3

router ospf
  ospf router-id 10.2.1.3
  network 10.2.1.3/32 area 0.0.0.0
  network 10.4.3.0/24 area 0.0.0.0
```

{{< /tab >}}

{{< /tabs >}}

6. Restart the networking service and then FRRouting on leaf02 and spine01:

   ```
   cumulus@switch:~$ sudo systemctl restart networking
   cumulus@switch:~$ sudo systemctl restart frr.service
   ```
