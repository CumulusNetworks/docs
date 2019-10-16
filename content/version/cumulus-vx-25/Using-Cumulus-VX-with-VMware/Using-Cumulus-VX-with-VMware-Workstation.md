---
title: Using Cumulus VX with VMware Workstation
author: Cumulus Networks
weight: 39
aliases:
 - /display/VX25/Using+Cumulus+VX+with+VMware+Workstation
 - /pages/viewpage.action?pageId=5115422
pageID: 5115422
product: Cumulus VX
version: 2.5 ESR
siteSlug: cumulus-vx-25
imgData: cumulus-vx-25
---
The process to integrate and use the Cumulus VX OVA image with VMware
Workstation on a Windows machine is similar to VMware Fusion, as
described above. This process was tested with VMware Workstation 11,
which is the latest release, but older versions should also work
correctly.

The steps to integrate the Cumulus VX OVA image with VMware Workstation
are as follows:

1.  Download the Cumulus VX [OVA
    image](https://cumulusnetworks.com/cumulus-vx/download/).

2.  Download VMware Workstation from
    [www.vmware.com/products/workstation](https://www.vmware.com/products/workstation)
    and install it.

3.  Open VMware Workstation and click **File** \> **Open**. Browse for
    the Cumulus VX OVA image, select it and click **Open**.

4.  In the next dialog that appears, assign a name to the VM (the
    default name is the name of the imported image) as well as location
    where you want to save the imported VM. By default it is saved in
    the `~\Documents\Virtual Machines\` directory.

5.  Click **Import** to start the import process. It take couple seconds
    to import the VM into VMware Workstation and create the VMX image.

    {{<figure src="https://dkahegywkrw3e.cloudfront.net/images/cumulus-vx/VMware_WS.png">}}

6.  Once imported, a dialog with the current VM settings appears. Click
    **Edit virtual machine settings** and make sure to match the network
    adapter settings as follows:

      - Network Adapter (1): *NAT*

      - Network Adapter 2: *Host-only* (equivalent to *Internal
        Network*)

      - Network Adapter 3: *Host-only* (equivalent to *Internal
        Network*)

      - Network Adapter 4: *Host-only* (equivalent to *Internal
        Network*)

7.  When you finish customizing the network settings, click **Power on
    this virtual machine** and log in using the *cumulus* user
    credentials. You can use the Cumulus VX VM with VMware Workstation
    now and you can make changes as needed.

8.  To build a two-leaf/two-spine topology, you must create three more
    VMs and name them as follows:

      - Cumulus VX-leaf1

      - Cumulus VX-leaf2

      - Cumulus VX-spine1

      - Cumulus VX-spine2

9.  Repeat the steps above for each VM, importing the original OVA image
    each time, assigning it the correct name, and configuring its
    settings.

## Configuring Network Interfaces and Quagga

The next step is to configure the 2 leaf/2 spine topology. This includes
setting up the network interfaces, and Quagga, and assumes the previous
sections have been completed.

### Configuring leaf1 VM

To configure leaf1:

1.  Log into the VM using the following credentials:

      - username: cumulus

      - password: CumulusLinux\!

2.  Configure the interfaces:

    1.  Log in as root, using the password CumulusLinux\!

            cumulus@leaf1:~$ sudo -i

    2.  Open `/etc/network/interfaces` in a text editor.

    3.  Edit the interfaces as shown below, and save the file:

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

3.  Configure Quagga

    1.  Open the `/etc/quagga/daemons` file in a text editor.

    2.  Set `zebra`, `bgpd`, and `ospfd` to yes, and save the file.

            zebra=yes
            bgpd=yes
            ospfd=yes
            ...

    3.  Create the `/etc/quagga/Quagga.conf` file in a text editor.

    4.  Configure the file as shown below, and save the file:

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

4.  Restart the networking service

        root@leaf1:~$ service networking restart

5.  Restart Quagga

        root@leaf1:~$ service quagga restart

### Configuring leaf2, spine1, and spine2 VMs

The configuration steps for `leaf2`, `spine1`, and `spine2` are the same
as those listed above for `leaf1`, however the file configurations are
different. Listed below are the configurations for each VM.

  - `leaf2`

      - `/etc/network/interfaces` file:

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
              address 10.4.2.1/25

      - `/etc/quagga/Quagga.conf` file:

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

  - `spine1`

      - `/etc/network/interfaces` file:

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

      - `/etc/quagga/Quagga.conf` file:

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
        ```

  - `spine2`

      - `/etc/network/interfaces` file:

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

      - `/etc/quagga/Quagga.conf` file:

            service integrated-vtysh-config

            interface swp1
              ip ospf network point-to-point

            interface swp2
              ip ospf network point-to-point

            router-id 10.2.1.4

            router ospf
              ospf router-id 10.2.1.4
              network 10.2.1.4/32 area 0.0.0.0

{{%notice note%}}

Remember to restart the networking and Quagga services on all VMs before
continuing.

{{%/notice%}}

## Testing the Connections

Once the VMs have been restarted, you can ping across VMs to test:

  - From `leaf1`:

      - Ping `leaf2`:

            root@leaf1:~# ping 10.2.1.2

      - Ping `spine1`:

            root@leaf1:~# ping 10.2.1.3

      - Ping `spine2`:

            root@leaf1:~# ping 10.2.1.4

## Further Information

For the next steps regarding configuring Cumulus VX, check out these
community articles, and the rest of the Cumulus Documentation:

- [Automation: Network Automation with Cumulus VX](https://forums.cumulusnetworks.com/cumulus-vx-230884/testing-network-automation-with-cumulus-vx-6727777)
- [Routing protocols: Unnumbered OSPF/BGP with Cumulus VX](https://forums.cumulusnetworks.com/cumulus-vx-230884/unnumbered-ospf-bgp-configuration-on-vmware-esxi-with-cumulus-vx-6728629)
- [Network redundancy: Multi-chassis Link Aggregation (MLAG) with Cumulus VX](https://forums.cumulusnetworks.com/cumulus-vx-230884/spinning-up-a-virtual-mlag-environment-6722798)
- [Network virtualization: Cumulus VX with VMware NSX](https://forums.cumulusnetworks.com/cumulus-vx-230884/integrating-cumulus-vx-with-vmware-nsx-using-vmware-esxi-6732766)
- [Cumulus Linux Documentation](/cumulus-linux)
