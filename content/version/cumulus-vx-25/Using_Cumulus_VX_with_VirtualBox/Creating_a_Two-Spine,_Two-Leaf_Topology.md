---
title: 'Creating a Two-Spine, Two-Leaf Topology'
author: Cumulus Networks
weight: 51
aliases:
 - '/display/VX25/Creating+a+Two-Spine,+Two-Leaf+Topology'
 - /pages/viewpage.action?pageId=5115392
pageID: 5115392
product: Cumulus VX
version: '2.5'
imgData: cumulus-vx-25
siteSlug: cumulus-vx-25
---
To create a two-spine/two-leaf configuration, you start by importing the
OVA image into VirtualBox four times, as each instance of the VM
represents one leaf or spine switch (Cumulus VX-leaf1, Cumulus VX-leaf2,
Cumulus VX-spine1 and Cumulus VX-spine2). Then you configure each VM's
network interfaces and routing settings.

## <span>Configuring the leaf1 VM</span>

Import the Cumulus VX-leaf1 VM into VirtualBox, then configure its
settings.

1.  Double-click the OVA image file to open VirtualBox.

2.  Check **Reinitialize the MAC addresses of all network cards**,
    unless you have a strong reason not to do so.
    
    {{% imgOld 0 %}}

3.  Click **Import** to start importing the image into VirtualBox.

4.  Configure the VM settings. In the VM list, select this VM and click
    **Settings**.
    
      - On the **General** tab, change the **Name** to *Cumulus
        VX-leaf1*.
    
      - On the **Network** tab, configure the virtual NICs:
        
          - On the **Adapter1** tab, in the **Attached to** list, select
            *NAT*. This provides the VM with outside connectivity;
            depending upon your virtual network, you may need to choose
            a [different
            option](https://www.virtualbox.org/manual/ch06.html).
        
          - On the **Adapter2** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *l1s1*,
            which indicates that the Cumulus VX-leaf1 VM connects to the
            Cumulus VX-spine1 VM.
        
          - On the **Adapter3** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *l1s2*,
            which indicates that the Cumulus VX-leaf1 VM connects to the
            Cumulus VX-spine2 VM.
        
          - On the **Adapter4** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *leaf1*.

5.  Click **OK** to apply your settings.
    
    {{% imgOld 1 %}}

## <span>Configuring the leaf2 VM</span>

Import the Cumulus VX-leaf2 VM into VirtualBox, reinitializing the MAC
addresses as stated above, then configure its settings.

1.  In the VM list, select this VM and click **Settings**.
    
      - On the **General** tab, change the **Name** to *Cumulus
        VX-leaf2*.
    
      - On the **Network** tab, configure the virtual NICs:
        
          - On the **Adapter1** tab, in the **Attached to** list, select
            *NAT*. This provides the VM with outside connectivity;
            depending upon your virtual network, you may need to choose
            a [different
            option](https://www.virtualbox.org/manual/ch06.html).
        
          - On the **Adapter2** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *l2s1*,
            which indicates that the Cumulus VX-leaf2 VM connects to the
            Cumulus VX-spine1 VM.
        
          - On the **Adapter3** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *l2s2*,
            which indicates that the Cumulus VX-leaf2 VM connects to the
            Cumulus VX-spine2 VM.
        
          - On the **Adapter4** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *leaf2*.

2.  Click **OK** to apply your settings.
    
    {{% imgOld 2 %}}

## <span>Configuring the spine1 VM</span>

Import the Cumulus VX-spine1 VM into VirtualBox, reinitializing the MAC
addresses as stated above, then configure its settings.

1.  In the VM list, select this VM and click **Settings**.
    
      - On the **General** tab, change the **Name** to *Cumulus
        VX-spine1*.
    
      - On the **Network** tab, configure the virtual NICs:
        
          - On the **Adapter1** tab, in the **Attached to** list, select
            *NAT*. This provides the VM with outside connectivity;
            depending upon your virtual network, you may need to choose
            a [different
            option](https://www.virtualbox.org/manual/ch06.html).
        
          - On the **Adapter2** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *l1s1*,
            which indicates that the Cumulus VX-spine1 VM connects to
            the Cumulus VX-leaf1 VM.
        
          - On the **Adapter3** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *l2s1*,
            which indicates that the Cumulus VX-spine1 VM connects to
            the Cumulus VX-leaf2 VM.
        
          - On the **Adapter4** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *spine1*.

2.  Click **OK** to apply your settings.
    
    {{% imgOld 3 %}}

## <span>Configuring the spine2 VM</span>

Import the Cumulus VX-spine2 VM into VirtualBox, reinitializing the MAC
addresses as stated above, then configure its settings.

1.  In the VM list, select this VM and click **Settings**.
    
      - On the **General** tab, change the **Name** to *Cumulus
        VX-spine2*.
    
      - On the **Network** tab, configure the virtual NICs:
        
          - On the **Adapter1** tab, in the **Attached to** list, select
            *NAT*. This provides the VM with outside connectivity;
            depending upon your virtual network, you may need to choose
            a [different
            option](https://www.virtualbox.org/manual/ch06.html).
        
          - On the **Adapter2** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *l1s2*,
            which indicates that the Cumulus VX-spine2 VM connects to
            the Cumulus VX-leaf1 VM.
        
          - On the **Adapter3** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *l2s2*,
            which indicates that the Cumulus VX-spine2 VM connects to
            the Cumulus VX-leaf2 VM.
        
          - On the **Adapter4** tab, in the **Attached to** list, select
            *Internal Network*. Then, change the **Name** to *spine2*.

2.  Click **OK** to apply your settings.
    
    {{% imgOld 4 %}}

## <span>Configuring Network Interfaces and Quagga</span>

The next step is to configure the 2 leaf/2 spine topology. This includes
setting up the network interfaces, and Quagga, and assumes the previous
sections have been completed.

### <span>Configuring leaf1 VM</span>

To configure leaf1:

1.  Power on and log into the VM using the following credentials:
    
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

3.  Configure Quagga:
    
    1.  Open the `/etc/quagga/daemons` file in a text editor.
    
    2.  Set `zebra`, `bgpd`, and `ospfd` to *yes*, and save the file.
        
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

4.  Restart the networking service:
    
        root@leaf1:~$ service networking restart

5.  Restart Quagga:
    
        root@leaf1:~$ service quagga restart

### <span>Configuring leaf2, spine1, and spine2 VMs</span>

The configuration steps for leaf2, spine1, and spine2 are the same as
those listed above for leaf1, however the file configurations are
different. Listed below are the configurations for each VM.

#### <span>leaf2</span>

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

#### <span>spine1</span>

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

#### <span>spine2</span>

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

Once the VMs have been restarted, you can ping across VMs to test. From
leaf1:

  - Ping leaf2:
    
        root@leaf1:~# ping 10.2.1.2

  - Ping spine1:
    
        root@leaf1:~# ping 10.2.1.3

  - Ping spine2:
    
        root@leaf1:~# ping 10.2.1.4

## <span>Further Information</span>

For the next steps regarding configuring Cumulus VX, check out these
community articles, and the rest of the Cumulus Documentation:

  - Management network with Cumulus VX:  
    <https://community.cumulusnetworks.com/cumulus/topics/using-a-management-vm-with-cumulus-vx>

  - Network automation with Cumulus VX:  
    <https://community.cumulusnetworks.com/cumulus/topics/testing-network-automation-with-cumulus-vx-3028v0i4u6aw4>

  - Routing protocols: Unnumbered OSPF/BGP with Cumulus VX:  
    <https://community.cumulusnetworks.com/cumulus/topics/un-numbered-ospf-bgp-setup-on-vmware-esxi-with-cumulus-vx>

  - Network redundancy: Multi-chassis Link Aggregation (MLAG) with
    Cumulus VX:  
    <https://community.cumulusnetworks.com/cumulus/topics/spinning-up-a-virtual-mlag-environment>

  - Network virtualization: Cumulus VX with VMware NSX:  
    <https://community.cumulusnetworks.com/cumulus/topics/integrating-cumulus-vx-with-vmware-nsx-using-vmware-esxi>

  - Cumulus Linux documentation:  
    <http://docs.cumulusnetworks.com/display/DOCS/>
