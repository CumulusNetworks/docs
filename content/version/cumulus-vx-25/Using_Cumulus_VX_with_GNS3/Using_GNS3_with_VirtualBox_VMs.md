---
title: Using GNS3 with VirtualBox VMs
author: Cumulus Networks
weight: 67
aliases:
 - /display/VX25/Using+GNS3+with+VirtualBox+VMs
 - /pages/viewpage.action?pageId=5115408
pageID: 5115408
product: Cumulus VX
version: '2.5'
imgData: cumulus-vx-25
siteSlug: cumulus-vx-25
---
Before you run your virtual network under GNS3, make sure you have done
the following:

  - Download and install [VirtualBox](https://www.virtualbox.org).

  - Download the the [VirtualBox OVA
    image](https://cumulusnetworks.com/cumulus-vx/download/) and import
    all the VMs that you want to run in GNS3 into VirtualBox.

  - Download and install
    [GNS3](https://community.gns3.com/login.jspa?referer=/community/software/download).

{{%notice note%}}

GNS3 overwrites the interface names that are configured in VirtualBox,
so, if you want to use the VMs in VirtualBox and GNS3, then you should
consider cloning them first.

{{%/notice%}}

1.  Start GNS3.

2.  In GNS3, select **GNS3** \> **Preferences**. The Preferences dialog
    pops up. From the left pane, select **VirtualBox**.

3.  In the **Path to VBoxManage** field, enter the location of where
    VBoxManage is installed. For example: `/usr/bin/VBoxManage`.

4.  From the left pane, select **VirtualBox VMs**, then click **New**.
    In **VM list**, a list of VirtualBox VMs that you already set up
    earlier appears.
    
    {{% imgOld 0 %}}

5.  From the **VM list**, select the VM that you want to run in GNS3,
    then click **Finish**. The VM you selected appears in the center
    pane. Repeat this step for every VM in the topology that you want to
    run in GNS3. For the example topology above, they are: Cumulus
    VX-spine1, Cumulus VX-spine2, Cumulus VX-leaf1 and Cumulus VX-leaf2.
    
    {{% imgOld 1 %}}

6.  Enable GNS3 to work with the VirtualBox VMs’ network interfaces.
    Configure each VM's network settings, using the GNS3 interface:
    
      - Select a VM in the center pane, then click **Edit**.
    
      - In the VirtualBox VM configuration dialog, click the **Network**
        tab.
        
        {{% imgOld 2 %}}
    
      - Increase the number of **Adapters** to *4*.
    
      - Select the **Type** to be *Paravirtualized Network*.
    
      - Select **Allow GNS3 to use any configured VirtualBox adapter**.
    
      - Click **OK** to save your settings and close the dialog.
        
        {{%notice note%}}
        
        GNS3 overwrites the interface names that are configured in
        VirtualBox, so, if you want to use the VM in VirtualBox, then
        you might want to consider cloning them first.
        
        {{%/notice%}}

7.  To connect VMs, select the cable icon from the left pane, then
    select the VMs to connect directly. To do this, select which network
    interface you want connected for each VM.
    
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
    
    e1 in GNS3 corresponds to swp1 in Cumulus VX, e2 to swp2, and so
    forth.
    
    {{%/notice%}}

You can also drag and drop virtual PCs (VPCS) and connect them to the
Cumulus VX switch.

To open a console to a virtual PC, right click on the VPCS icon and
select Console.

In the console, you can configure the IP address and default gateway for
the VPCS. For example:

    ip 10.4.1.101/25 10.4.1.1

Start all the VMs.

You should be able to ping between the VMs, and between the virtual PCs
as well.
