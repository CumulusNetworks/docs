---
title: VMware Workstation
author: Cumulus Networks
weight: 41
aliases:
 - /display/VX/VMware+Workstation
 - /pages/viewpage.action?pageId=5126698
pageID: 5126698
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
The following sections describe how to import and set up a
two-leaf/two-spine Cumulus VX topology with VMware Workstation.

{{%notice note%}}

These sections assume a basic level of VMware Workstation experience.
For detailed instructions, refer to the [VMware Workstation
documentation](https://www.vmware.com/support/pubs/ws_pubs.html).

{{%/notice%}}

## <span>Create a Cumulus VX VM with VMware Workstation</span>

{{%notice note%}}

This section assumes that you have downloaded the Cumulus VX disk image
for VMware hypervisors and that VMware Workstation is installed. For
more download locations and steps, refer to the [Getting
Started](/cumulus-vx/Getting_Started/) page.

{{%/notice%}}

1.  Open VMware Workstation and click **File \> Open...** to open the
    virtual machine wizard.

2.  Click the **Choose File...** button, select the downloaded OVA, then
    click **Open**.

3.  In the text box, edit the name of the VM to `CumulusVX-leaf1` and
    assign the directory location to save the imported VM.
    
    {{%notice note%}}
    
    By default, the VM is saved in the `~\Documents\Virtual Machines\`
    folder.
    
    {{%/notice%}}

4.  Click **Import** to start the import process. This might take a few
    seconds.

5.  Click **Edit virtual machine settings** and configure the network
    adapter settings:
    
      - Network Adapter (1): NAT
    
      - Network Adapter 2: Host-only (equivalent to Internal Network)
    
      - Network Adapter 3: Host-only (equivalent to Internal Network)
    
      - Network Adapter 4: Host-only (equivalent to Internal Network)
        
        {{% imgOld 0 %}}

## <span>Next Steps</span>

{{%notice note%}}

This section assumes that you are configuring a two-leaf/two-spine
network topology, that you have completed the steps in [Create a Cumulus
VX VM with VMware
Workstation](#src-5126698_VMwareWorkstation-CreateaCumulusVXVirtualMachinewithVMwareWorkstation)
above, and that you now have a VM called `CumulusVX-leaf1`.

{{%/notice%}}

1.  The two-leaf/two-spine network topology requires four Cumulus VX VMs
    to be created. Using the Snapshot Manager, clone the virtual machine
    (Ctrl + M) three times to create three additional VMs, replacing the
    name `CumulusVX-leaf1` with:
    
      - `CumulusVX-leaf2`
    
      - `CumulusVX-spine1`
    
      - `CumulusVX-spine2`

2.  After you have created all four VMs, follow the steps in [Create a
    Two-Leaf, Two-Spine
    Topology](/cumulus-vx/Create_a_Two-Leaf_Two-Spine_Topology) to
    configure the network interfaces and routing.
