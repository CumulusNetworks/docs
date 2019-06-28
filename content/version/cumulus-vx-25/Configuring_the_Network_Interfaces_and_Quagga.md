---
title: Configuring the Network Interfaces and Quagga
author: Cumulus Networks
weight: 23
aliases:
 - /display/VX25/Configuring+the+Network+Interfaces+and+Quagga
 - /pages/viewpage.action?pageId=5115426
pageID: 5115426
product: Cumulus VX
version: '2.5'
imgData: cumulus-vx-25
siteSlug: cumulus-vx-25
---
This section covers configuring the network interfaces and Quagga for a
2 leaf/2 spine topology. The steps below assume that the VMs have been
set up. Refer to earlier sections of this guide to set up the VMs.

## <span>Configuring leaf1 VM</span>

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

## <span>Configuring leaf2, spine1, and spine2 VMs</span>

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
