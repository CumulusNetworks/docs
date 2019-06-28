---
title: Using Cumulus VX with VMware Fusion
author: Cumulus Networks
weight: 37
aliases:
 - /display/VX25/Using+Cumulus+VX+with+VMware+Fusion
 - /pages/viewpage.action?pageId=5115423
pageID: 5115423
product: Cumulus VX
version: '2.5'
imgData: cumulus-vx-25
siteSlug: cumulus-vx-25
---
The process to integrate and use the Cumulus VX OVA image with VMware
Fusion is pretty straightforward. The procedure was tested on VMware
Fusion 7.0, the latest release, but it should work on older versions in
a similar manner.

The steps are as follows:

1.  Download the Cumulus VX [OVA
    image](https://cumulusnetworks.com/cumulus-vx/download/).

2.  Download VMware Fusion from
    [www.vmware.com/products/fusion](http://www.vmware.com/products/fusion)
    and install it.

3.  Open VMware Fusion and click **File** \> **Import**. This opens a
    dialog that prompts you to add an existing virtual machine.

4.  Click **Choose File** and add the Cumulus VX image you just
    downloaded, then click **Continue**.

5.  In the next dialog that appears, assign a name to the VM (the
    default name is the name of the imported image) as well as location
    where you want to save the imported VM. By default, it is saved in
    the *Virtual Machines* folder under the *Home* directory.

6.  Click **Save** to start the import process. It takes a few seconds
    to import the VM into VMware Fusion and create the VMX image.

7.  Once imported, a dialog with the current VM settings appears. Click
    **Customize Settings** and edit the network adapter settings as
    follows:
    
      - Network Adapter (1): *Share with my Mac* (equivalent to *NAT* in
        VirtualBox)
    
      - Network Adapter 2: *Private to my Mac* (equivalent to *Internal
        Network*)
    
      - Network Adapter 3: *Private to my Mac* (equivalent to *Internal
        Network*)
    
      - Network Adapter 4: *Private to my Mac* (equivalent to *Internal
        Network*)
    
    {{% imgOld 0 %}}

8.  When you finish customizing the network settings, click **Start Up**
    to power on the VM and use it as you desire.

9.  To build a two-leaf/two-spine topology, you must create three more
    VMs and name them as follows:
    
      - Cumulus VX-leaf1
    
      - Cumulus VX-leaf2
    
      - Cumulus VX-spine1
    
      - Cumulus VX-spine2

10. Repeat the steps above for each VM, importing the original OVA image
    each time, assigning it the correct name, and configuring its
    settings.

## <span>Configuring Network Interfaces and Quagga</span>

The next step is to configure the 2 leaf/2 spine topology. This includes
setting up the network interfaces, and Quagga, and assumes the previous
sections have been completed.

### <span>Configuring leaf1 VM</span>

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

### <span>Configuring leaf2, spine1, and spine2 VMs</span>

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

## <span>Testing the Connections</span>

Once the VMs have been restarted, you can ping across VMs to test:

  - From `leaf1`:
    
      - Ping `leaf2`:
        
            root@leaf1:~# ping 10.2.1.2
    
      - Ping `spine1`:
        
            root@leaf1:~# ping 10.2.1.3
    
      - Ping `spine2`:
        
            root@leaf1:~# ping 10.2.1.4

## <span>Further Information</span>

For the next steps regarding configuring Cumulus VX, check out these
community articles, and the rest of the Cumulus Documentation:

Management Network with Cumulus VX:  
<https://community.cumulusnetworks.com/cumulus/topics/using-a-management-vm-with-cumulus-vx>

Automation: Network Automation with Cumulus VX  
<https://community.cumulusnetworks.com/cumulus/topics/testing-network-automation-with-cumulus-vx-3028v0i4u6aw4>

Routing protocols: Unnumbered OSPF/BGP with Cumulus VX  
<https://community.cumulusnetworks.com/cumulus/topics/un-numbered-ospf-bgp-setup-on-vmware-esxi-with-cumulus-vx>

Network redundancy: Multi-chassis Link Aggregation (MLAG) with Cumulus
VX  
<https://community.cumulusnetworks.com/cumulus/topics/spinning-up-a-virtual-mlag-environment>

Network virtualization: Cumulus VX with VMware NSX  
<https://community.cumulusnetworks.com/cumulus/topics/integrating-cumulus-vx-with-vmware-nsx-using-vmware-esxi>

Cumulus Linux Documentation  
<http://docs.cumulusnetworks.com/display/DOCS/>
