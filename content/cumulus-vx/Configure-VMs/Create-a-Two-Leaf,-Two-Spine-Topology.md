---
title: 'Create a Two-Leaf, Two-Spine Topology'
author: Cumulus Networks
weight: 34
product: Cumulus VX
version: '3.7'
---
The following sections describe how to configure network interfaces and FRRouting for a two-leaf/two-spine Cumulus VX network topology:

- Two spine VMs that represent two spine (aggregation layer) switches on the network.
- Two leaf VMs that represent two leaf (access layer) switches on the network.

{{< img src = "/images/cumulus-vx/network-topology.png  >}}

These instructions assume that you have installed the relevant images and hypervisors, created four VMs with appropriate names, and that the VMs are running. Refer to {{<link url="Getting-Started" text="Getting Started">}}.

## Configure CumulusVX-leaf1

You can configure each of the VMs using the Network Command Line Utility (NCLU) or by editing the `/etc/network/interfaces` and `/etc/frr/frr.conf` files as the sudo user.

{{%notice tip%}}

The following configuration uses unnumbered IP addressing, where you use the same /32 IPv4 address on multiple ports. OSPF unnumbered does not have an equivalent to RFC-5549, so you need to use an IPv4 address to bring up the adjacent OSPF neighbors, allowing you to reuse the same IP address. You can see some example
{{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/202796476-OSPF-Unnumbered-Sample-Configurations" text="unnumbered OSPF configurations">}} in the knowledge base.

{{%/notice%}}

To configure CumulusVX-leaf1:

1. Log into the CumulusVX-leaf1 VM using the default credentials:

   - username: cumulus
   - password: CumulusLinux\!

2. As the sudo user, edit the `/etc/frr/daemons` file in a text editor. Set `zebra`, `bgpd`, and `ospfd` to **yes**, and save the file.

   ```
   zebra=yes
   bgpd=yes
   ospfd=yes
   ...
   ```

3. Run the following commands to configure the switch:

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

   These commands configure both `/etc/network/interfaces` and `/etc/frr/frr.conf`. The output of each file is shown below.

   {{%notice note%}}

To edit the configuration files directly as the sudo user, copy the configurations below.

{{%/notice%}}

   ```
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

4. Restart the networking service:

   ```
   cumulus@switch:~$ sudo systemctl restart networking
   ```

5. Restart FRRouting:

   ```
   cumulus@switch:~$ sudo systemctl restart frr.service
   ```

## Configure the Remaining VMs

The configuration steps for CumulusVX-leaf2, CumulusVX-spine1, and CumulusVX-spine2 are the same as CumulusVX-leaf1; however, the file configurations are different. Listed below are the configurations for each additional VM:

{{< tabs "TabID01 ">}}

{{< tab "CumulusVX-leaf2 ">}}

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

{{< tab "CumulusVX-spine1 ">}}

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

{{< tab "CumulusVX-spine2 ">}}

```
cumulus@switch:~$ net add loopback lo ip address 10.2.1.4/32
cumulus@switch:~$ net add interface swp1 ip address 10.2.1.4/32
cumulus@switch:~$ net add interface swp2 ip address 10.2.1.4/32
cumulus@switch:~$ net add interface swp3 ip address 10.4.4.1/24
cumulus@switch:~$ net add interface swp1 ospf network point-to-point
cumulus@switch:~$ net add interface swp2 ospf network point-to-point
cumulus@switch:~$ net add ospf router-id 10.2.1.4
cumulus@switch:~$ net add ospf network 10.2.1.4/32 area 0.0.0.0
cumulus@switch:~$ net add ospf network 10.4.4.0/24 area 0.0.0.0
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit

# The loopback network interface
auto lo
iface lo inet loopback
    address 10.2.1.4/32

# The primary network interface
auto eth0
iface eth0 inet dhcp

auto swp1
iface swp1
    address 10.2.1.4/32

auto swp2
iface swp2
    address 10.2.1.4/32

auto swp3
iface swp3
    address 10.4.4.1/24

service integrated-vtysh-config

interface swp1
  ip ospf network point-to-point

  interface swp2
   ip ospf network point-to-point

   router-id 10.2.1.4

   router ospf
   ospf router-id 10.2.1.4
   network 10.2.1.4/32 area 0.0.0.0
   network 10.4.4.0/24 area 0.0.0.0
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

Restart the networking and FRRouting services on all VMs before continuing.

{{%/notice%}}

## Create Point-to-Point Connections Between VMs

To use the two-leaf/two-spine Cumulus VX network topology you configured above, you need to configure the network adapter settings for each VM to create point-to-point connections. The following example shows how to create point-to-point connections between each VM in VirtualBox. If you are not using VirtualBox, refer to your hypervisor documentation to configure network adapter settings.

Follow these steps for each of the four VMs.

{{%notice note%}}

Make sure that the VM is powered off.

{{%/notice%}}

1. In the VirtualBox Manager window, select the VM.

2. Click **Settings**, then click **Network**.

3. Click **Adapter 2**.

4. Click the **Enable Network Adapter** check box.

5. From the **Attached to** list, select **Internal Network**.  

    {{< img src = "/images/cumulus-vx/adapterSettings.png >}}

6. In the **Name** field, type a name for the internal network, then click **OK**. The internal network name must match the internal network name on the corresponding network adapter on the VM to be connected to this VM. For example, in the two-leaf/two-spine Cumulus VX network topology, Adapter 2 (swp1) on CumulusVX-leaf1 is connected to Adapter 2 (swp1) on CumulusVX-spine1; the name must be the same for Adapter 2 on both VMs. Use the internal network names and the connections shown in the illustration and table below.

7. Click **Adapter 3** and repeat steps 4 thru 6. Use the internal network names and the connections shown in the illustration and table below.

{{< img src = "/images/cumulus-vx/mapping.png >}}

| Switch           | swp  | VirtualBox Interface | VirtualBox Network Type | Name     |
| ---------------- | ---- | -------------------- | ----------------------- | -------- |
| CumulusVX-leaf1  |      | Adapter 1            | NAT                     |          |
|                  | swp1 | Adapter 2            | Internal                | Intnet-1 |
|                  | swp2 | Adapter 3            | Internal                | Intnet-3 |
|                  | swp3 | Adapter 4            | Internal                | Intnet-5 |
| CumulusVX-leaf2  |      | Adapter 1            | NAT                     |          |
|                  | swp1 | Adapter 2            | Internal                | Intnet-2 |
|                  | swp2 | Adapter 3            | Internal                | Intnet-4 |
|                  | swp3 | Adapter 4            | Internal                | Intnet-6 |
| CumulusVX-spine1 |      | Adapter 1            | NAT                     |          |
|                  | swp1 | Adapter 2            | Internal                | Intnet-1 |
|                  | swp2 | Adapter 3            | Internal                | Intnet-2 |
|                  | swp3 | Adapter 4 (disabled) |                         |          |
| CumulusVX-spine2 |      | Adapter 1            | NAT                     |          |
|                  | swp1 | Adapter 2            | Internal                | Intnet-3 |
|                  | swp2 | Adapter 3            | Internal                | Intnet-4 |
|                  | swp3 | Adapter 4 (disabled) |                         |          |

## Test the Network Topology Connections

After you restart the VMs, ping across VMs to test the connections:

1. Run the following commands from CumulusVX-leaf1:

   - Ping CumulusVX-leaf2:

   ```
   cumulus@CumulusVX-leaf1:~$ ping 10.2.1.2
   ```

   - Ping CumulusVX-spine1:

   ```
   cumulus@CumulusVX-leaf1:~$ ping 10.2.1.3
   ```

   - Ping CumulusVX-spine2:

   ```
   cumulus@CumulusVX-leaf1:~$ ping 10.2.1.4
   ```
