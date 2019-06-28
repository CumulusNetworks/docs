---
title: Using Cumulus VX with VMware vSphere - ESXi 5.5
author: Cumulus Networks
weight: 35
aliases:
 - /display/VX30/Using+Cumulus+VX+with+VMware+vSphere+-+ESXi+5.5
 - /pages/viewpage.action?pageId=5126615
pageID: 5126615
product: Cumulus VX
version: '3.0'
imgData: cumulus-vx-30
siteSlug: cumulus-vx-30
---
Follow the steps below to import the Cumulus VX VM image into vSphere
ESXi. This configuration was tested using vSphere ESXi 5.5 and a Windows
vSphere client; however, the VM is configured to support ESXi 4 or
higher.

1.  Download the Cumulus VX [OVA
    image](https://cumulusnetworks.com/cumulus-vx/download/).

2.  Install and set up your vSphere ESXi server and vSphere client. You
    can find all the required downloads at
    [www.vmware.com/products/vsphere-operations-management](https://www.vmware.com/products/vsphere-operations-management/).

3.  While the OVA image you will import works out of the box for vSphere
    ESXi, you must first download the VMware OVFtools utility from
    [my.vmware.com/web/vmware/details?productId=352\&downloadGroup=OVFTOOL350](https://my.vmware.com/web/vmware/details?productId=352&downloadGroup=OVFTOOL350)
    and install it on the client.

4.  Connect your vSphere client to your vSphere ESXi server using the
    ESXi server's IP address and user credentials.

5.  Click **File** \> **Deploy OVF Template**. Browse to navigate to the
    location of the Cumulus VX OVA file you downloaded to your local
    machine.
    
    {{% imgOld 0 %}}

6.  Click **Next** to go to the next step. The next dialog displays
    basic information about the VM.
    
    {{% imgOld 1 %}}

7.  Click **Next**. In the **Name** box, edit the name of the VM. If you
    are setting up the two-leaf/two-spine topology, name this VM
    *CumulusVX-leaf1*.
    
    {{% imgOld 2 %}}

8.  Since the Cumulus VX VM image is already preconfigured, you don't
    have to set up any more options. Click **Next** a few more times
    until you reach the Ready to Complete dialog, where you can choose
    to power on the VM after deployment by checking **Power on after
    deployment**.
    
    {{% imgOld 3 %}}

9.  Click **Finish** to start importing the Cumulus VX OVA image into
    vSphere ESXi and deploying as a VM. This length of the import
    process depends on your system configuration. You can follow the
    progress in the Recent Tasks pane at the bottom of the client
    window.
    
    {{% imgOld 4 %}}

10. Once the deployment process is complete, the newly created VM
    appears in the list of VMs in the left pane. You can power it on by
    right clicking on the VM name and then choosing **Power** \> **Power
    On**.
    
    {{% imgOld 5 %}}

11. If you want to make any changes to the VM configuration, before you
    power it on, right click, then choose **Edit Settings**. Keep in
    mind the Cumulus VX VM image is configured to run straight out of
    the box.

12. Verify the VM is powered on by looking at the bottom of the Recent
    Tasks pane to ensure that the Power on virtual machine task has
    completed.

13. To interact with the VM, open a console. Click **Open Console** in
    the Commands pane for the VM. The console displays the Cumulus login
    prompt.
    
    {{% imgOld 6 %}}

14. After you log in to the VM, you can configure the network interfaces
    and routing (using Quagga for routing).

15. When you finish configuring the interfaces and routing, restart
    networking, then start Quagga; otherwise, simply restart the VM.
    
        cumulus@switch:~$ sudo service networking restart
        cumulus@switch:~$ sudo service quagga start

16. To build the two-leaf/two-spine topology, you have to create three
    more VMs:
    
      - CumulusVX-leaf2
    
      - CumulusVX-spine1
    
      - CumulusVX-spine2

17. Repeat the steps above for each VM, importing the original OVA
    image, assigning it the correct name, and configuring its settings.

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
