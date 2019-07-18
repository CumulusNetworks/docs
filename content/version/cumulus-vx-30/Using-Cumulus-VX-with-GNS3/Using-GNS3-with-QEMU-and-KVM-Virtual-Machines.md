---
title: Using GNS3 with QEMU and KVM Virtual Machines
author: Cumulus Networks
weight: 65
aliases:
 - /display/VX30/Using+GNS3+with+QEMU+and+KVM+Virtual+Machines
 - /pages/viewpage.action?pageId=5126603
pageID: 5126603
product: Cumulus VX
version: '3.0'
imgData: cumulus-vx-30
siteSlug: cumulus-vx-30
---
Before you run your virtual network under GNS3, make sure you have done
the following:

  - Download and install [KVM](http://www.linux-kvm.org/page/Downloads).

  - Download the the [Cumulus VX QCOW2
    image](https://cumulusnetworks.com/cumulus-vx/download/).

  - Download and install
    [GNS3](https://community.gns3.com/login.jspa?referer=/community/software/download).

<!-- end list -->

1.  Start GNS3.

2.  In GNS3, select **GNS3** \> **Preferences**. The Preferences dialog
    pops up. From the left pane, select **QEMU VMs**, then click
    **New**. In **VM list**, a list of KVM VMs that you already set up
    earlier appears.
    
      - In the **Type** list, keep *Default*, then click **Next**.
    
      - In the **Name** box, enter the name, then click **Next**.
    
      - Select the path to the **Qemu binary** and **RAM** size, then
        click **Next**.
    
      - Browse to select the **Disk image**, selecting the [qcow2
        image](https://cumulusnetworks.com/cumulus-vx/download/) you
        downloaded earlier.
    
      - Click **Finish** to save the configuration and close the New
        QEMU VM template dialog.

3.  Repeat the previous step for every VM you want to include, or re-use
    the single VM imported. For the example topology above, they are:
    Cumulus VX-spine1, Cumulus VX-spine2, Cumulus VX-leaf1, Cumulus
    VX-leaf2.

4.  Enable GNS3 to work with the QEMU VMs' network interfaces. Configure
    each VM's network settings, using the GNS3 interface:
    
      - Select a VM in the center pane, then click **Edit**.
    
      - In the QEMU VM configuration dialog, click the **Network** tab.
    
      - Increase the number of **Adapters** to *4*.
    
      - Select the **Type** to be *Legacy paravirtualized*.
    
      - <span style="color: #222222;"> Check the **Use the legacy
        networking mode** <span style="color: #222222;"> check box
        </span> . </span>
    
      - Click **Advanced Settings**. In the options field, enter:  
        `-net user,vlan=0,net=192.168.0.0/24,hostfwd=tcp::1401-:22`
        
        {{%notice note%}}
        
        Each node needs a different port. You can do this by
        incrementing 1401 to 1402 for the second CL node.
        
        {{%/notice%}}
    
      - Click **OK** to save your settings and close the dialog.
        
        {{%notice note%}}
        
        This enables SSH to port 1401 (ssh -p 1401 cumulus@127.0.0.1).
        
        {{%/notice%}}
    
      - Click **OK** to save your settings and close the dialog.

5.  Start each VM, then SSH into it and configure the [network
    interfaces and
    Quagga](http://docs.cumulusnetworks.com/display/VX/Configuring+the+Network+Interfaces+and+Quagga).

6.  To interconnect the VMs, select the cable icon from the left pane,
    then select the VMs to connect directly. To do this, select which
    network interface you want connected for each VM.
    
      - Cumulus VX-spine1:  
        e1\<-\> e1 Cumulus VX-leaf1  
        e2\<-\>e1 Cumulus VX-leaf2
    
      - Cumulus VX-spine2:  
        e1\<-\>e2 Cumulus VX-leaf1  
        e2\<-\>e2 Cumulus VX-leaf2
    
      - Cumulus VX-leaf1:  
        e1\<-\>e1 Cumulus VX-spine1  
        e2\<-\>e1 Cumulus VX-spine2  
        e3\<-\>e0 PC1 (VPCS)
    
      - Cumulus VX-leaf2:  
        e1\<-\>e2 Cumulus VX-spine1  
        e2\<-\>e2 Cumulus VX-spine2  
        e3\<-\>e0 PC2 (VPCS)

{{%notice note%}}

e1 in GNS3 corresponds to swp1 in Cumulus VX, e2 to swp2, and so forth.

{{%/notice%}}

You can also drag and drop virtual PCs (VPCS) and connect them to the
Cumulus VX switch.

To open a console to a VPC, right click on the VPCS icon and select
**Console**.

In the console, you can configure the IP address and default gateway for
the VPCS. For example:

    ip 10.4.1.101/25 10.4.1.1

Start all the VMs.

You should be able to ping between the VMs, and between the virtual PCs
as well.

## <span>Caveats</span>

  - Once you start the VMs, they run headless. You can SSH into a VM
    as:  
    `ssh -p port-nr root@127.0.0.1`

  - `port-nr` is the one specified for this node in step 4 above.

  - It takes a couple of minutes for the VMs to spin up and be ready for
    SSH connections.

  - Console access does not work with GNS3 in this configuration. For a
    workaround, run QEMU/KVM from the command line; see below for
    details.

## <span>KVM/QEMU from the Command Line</span>

In order to use console access with GNS3 and QEMU/KVM VMs, you use the
qemu binary that is bundled with GNS3. On OSX, this binary is located
at:
/Applications/GNS3.app/Contents/Resources/qemu/bin/qemu-system-x86\_64.

When using the command line to access QEMU, start the two-leaf/two-spine
topology by starting each VM manually.

One each node is up, configure the [network interfaces](#src-5126603)
and [routing](#src-5126603), then restart the VMs or their services, as
described earlier. Once this is done, every node should be able to
communicate with each other.

To start Cumulus VX-spine1:

    /Applications/GNS3.app/Contents/Resources/qemu/bin/qemu-system-x86_64 -name 
      "Cumulus VX-spine1" -m 256 -hda 
      /Users/cumulus/GNS3/projects/gns_vm_release_test/project-files/qemu/4e87d26e-c5a2-43a0-b659-c34f62ebc9df/hda_disk.qcow2 
      -serial telnet:127.0.0.1:2003,server,nowait -monitor 
      tcp:127.0.0.1:55603,server,nowait -net 
      user,vlan=0,net=192.168.0.0/24,hostfwd=tcp::1403-:22 -net none -net nic,vlan=0,macaddr=00:00:ab:c9:df:00,model=virtio -net
      nic,vlan=1,macaddr=00:00:ab:c9:df:01,model=virtio -net udp,vlan=1,name=gns3-1,sport=10001,dport=10000,daddr=127.0.0.1 -net
      nic,vlan=2,macaddr=00:00:ab:c9:df:02,model=virtio -net udp,vlan=2,name=gns3-2,sport=10002,dport=10003,daddr=127.0.0.1 -net
      nic,vlan=3,macaddr=00:00:ab:c9:df:03,model=virtio &

To start Cumulus VX-spine2:

    /Applications/GNS3.app/Contents/Resources/qemu/bin/qemu-system-x86_64 -name 
      "Cumulus VX-spine2" -m 256 -hda 
      /Users/cumulus/GNS3/projects/gns_vm_release_test/project-files/qemu/8e83fef2-cb87-4df5-aa66-5511c0330919/hda_disk.qcow2 
      -serial telnet:127.0.0.1:2004,server,nowait -monitor 
      tcp:127.0.0.1:55604,server,nowait -net 
      user,vlan=0,net=192.168.0.0/24,hostfwd=tcp::1404-:22 -net none -net nic,vlan=0,macaddr=00:00:ab:09:19:00,model=virtio -net
      nic,vlan=1,macaddr=00:00:ab:09:19:01,model=virtio -net udp,vlan=1,name=gns3-1,sport=10005,dport=10004,daddr=127.0.0.1 -net
      nic,vlan=2,macaddr=00:00:ab:09:19:02,model=virtio -net udp,vlan=2,name=gns3-2,sport=10006,dport=10007,daddr=127.0.0.1 -net
      nic,vlan=3,macaddr=00:00:ab:09:19:03,model=virtio &

To start Cumulus VX-leaf1:

    /Applications/GNS3.app/Contents/Resources/qemu/bin/qemu-system-x86_64 -name 
      "Cumulus VX-leaf1" -m 256 -hda 
      /Users/cumulus/GNS3/projects/gns_vm_release_test/project-files/qemu/d5399bd9-af1d-4baa-9821-6e18b795f16b/hda_disk.qcow2 
      -serial telnet:127.0.0.1:2001,server,nowait -monitor 
      tcp:127.0.0.1:55605,server,nowait -net 
      user,vlan=0,net=192.168.0.0/24,hostfwd=tcp::1401-:22 -net none -net nic,vlan=0,macaddr=00:00:ab:f1:6b:00,model=virtio -net
      nic,vlan=1,macaddr=00:00:ab:f1:6b:01,model=virtio -net udp,vlan=1,name=gns3-1,sport=10000,dport=10001,daddr=127.0.0.1 -net
      nic,vlan=2,macaddr=00:00:ab:f1:6b:02,model=virtio -net udp,vlan=2,name=gns3-2,sport=10004,dport=10005,daddr=127.0.0.1 -net
      nic,vlan=3,macaddr=00:00:ab:f1:6b:03,model=virtio &

To start Cumulus VX-leaf2:

    /Applications/GNS3.app/Contents/Resources/qemu/bin/qemu-system-x86_64 -name 
      "Cumulus VX-leaf2" -m 256 -hda 
      /Users/cumulus/GNS3/projects/gns_vm_release_test/project-files/qemu/b0aca41a-dda7-4944-957f-4b0f94dee683/hda_disk.qcow2 
      -serial 
      telnet:127.0.0.1:2002,server,nowait -monitor 
      tcp:127.0.0.1:55606,server,nowait -net user,vlan=0,net=192.168.0.0/24,hostfwd=tcp::1402-:22 -net none -net
      nic,vlan=0,macaddr=00:00:ab:e6:83:00,model=virtio -net 
      nic,vlan=1,macaddr=00:00:ab:e6:83:01,model=virtio -net udp,vlan=1,name=gns3-1,sport=10003,dport=10002,daddr=127.0.0.1 -net
      nic,vlan=2,macaddr=00:00:ab:e6:83:02,model=virtio -net udp,vlan=2,name=gns3-2,sport=10007,dport=10006,daddr=127.0.0.1 -net
      nic,vlan=3,macaddr=00:00:ab:e6:83:03,model=virtio &

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
