---
title: VMware Fusion
author: Cumulus Networks
weight: 39
aliases:
 - /display/VX/VMware+Fusion
 - /pages/viewpage.action?pageId=5126696
pageID: 5126696
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
The following sections describe how to import and set up a
two-leaf/two-spine Cumulus VX topology with VMware Fusion.

{{%notice note%}}

These sections assume a basic level of VMware Fusion experience. For
detailed instructions, refer to the [VMware Fusion
documentation](https://www.vmware.com/support/pubs/fusion_pubs.html).

{{%/notice%}}

## <span>Create a Cumulus VX VM with VMware Fusion</span>

{{%notice note%}}

This section assumes that the you have downloaded the Cumulus VX disk
image for VMware hypervisors and that VMware Fusion is installed. For
more download locations and steps, refer to the [Getting
Started](/cumulus-vx/Getting_Started/) page.

{{%/notice%}}

1.  Open VMware Fusion and click **File \> Import...** to open the
    virtual machine wizard.

2.  Click the **Choose File...** button, select the downloaded OVA, then
    click **Open**.

3.  Click **Continue** to start the import process.

4.  In the text box, edit the name of the VM to `CumulusVX-leaf1`,
    assign the directory location to save the imported VM, then click
    **Save**.
    
    {{%notice note%}}
    
    By default, the VM is saved in the `Virtual Machines` folder under
    the `Home` directory.
    
    {{%/notice%}}

5.  Click **Customize Settings**, then configure the network adapter
    settings:
    
      - Network Adapter 1: Share with my Mac (equivalent to NAT in
        VirtualBox)
    
      - Network Adapter 2: Private to my Mac (equivalent to Internal
        Network)
    
      - Network Adapter 3: Private to my Mac (equivalent to Internal
        Network)
    
      - Network Adapter 4: Private to my Mac (equivalent to Internal
        Network)
        
        {{% imgOld 0 %}}

## <span>Next Steps</span>

{{%notice note%}}

This section assumes that you are configuring a two-leaf/two-spine
network topology, that you have completed the steps in [Create a Cumulus
VX VM with VMware
Fusion](#src-5126696_VMwareFusion-CreateaCumulusVXVirtualMachinewithVMwareFusion)
above, and now have a VM called `CumulusVX-leaf1`.

{{%/notice%}}

1.  The two-leaf/two-spine network topology requires four Cumulus VX VMs
    to be created. Repeat the steps outlined in [Create a Cumulus VX VM
    with VMware
    Fusion](#src-5126696_VMwareFusion-CreateaCumulusVXVirtualMachinewithVMwareFusion)
    to create three additional VMs, replacing the name `CumulusVX-leaf1`
    with:
    
      - `CumulusVX-leaf2`
    
      - `CumulusVX-spine1`
    
      - `CumulusVX-spine2`

2.  After you have created all four VMs, follow the steps in [Create a
    Two-Leaf, Two-Spine
    Topology](/cumulus-vx/Create_a_Two-Leaf_Two-Spine_Topology) to
    configure the network interfaces and routing.
