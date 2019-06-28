---
title: VirtualBox
author: Cumulus Networks
weight: 43
aliases:
 - /display/VX/VirtualBox
 - /pages/viewpage.action?pageId=5126701
pageID: 5126701
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
The following sections describe how to import and set up a
two-leaf/two-spine Cumulus VX topology with VirtualBox.

{{%notice note%}}

These sections assume a basic level of VirtualBox experience. For
detailed instructions, refer to the [VirtualBox
documentation](https://www.virtualbox.org/wiki/Documentation).

{{%/notice%}}

## <span>Create a Cumulus VX VM with VirtualBox</span>

{{%notice note%}}

This section assumes that you have downloaded the Cumulus VX disk image
for VirtualBox and that VirtualBox is installed. For more download
locations and steps, refer to the [Getting
Started](/cumulus-vx/Getting_Started/) page.

{{%/notice%}}

1.  Open VirtualBox and click **File \> Import Appliance**.

2.  Browse for the downloaded VirtualBox image, click the **Open**
    button, then click **Continue**.

3.  Review the Appliance settings. Change the name of the VM to
    `CumulusVX-leaf1`, then click **Import** to begin the import
    process.  
    
    {{% imgOld 0 %}}

## <span>Next Steps</span>

{{%notice note%}}

This section assumes that you are configuring a two-leaf/two-spine
network topology, that you have completed the steps in [Create a Cumulus
VX VM with
VirtualBox](#src-5126701_VirtualBox-CreateaCumulusVXVirtualMachinewithVirtualBox)
above, and that you now have a VM called `CumulusVX-leaf1`.

{{%/notice%}}

1.  Right click the created `CumulusVX-leaf1` VM, then select **Clone**.

2.  Change the name of the VM to `CumulusVX-leaf2`, then click
    **Continue**.

3.  Select **Full Clone** and click **Clone**.

4.  Repeat steps 1-3 for two additional VMs:
    
      - `CumulusVX-spine1`
    
      - `CumulusVX-spine2`

5.  After you have created all four VMs, follow the steps in [Create a
    Two-Leaf, Two-Spine
    Topology](/cumulus-vx/Create_a_Two-Leaf_Two-Spine_Topology) to
    configure the network interfaces and routing.

{{%notice note%}}

You can also add a VM to one or more internal virtual networks in
VirtualBox by cloning the VM. However, consider the following if you
prefer to clone VMs:

  - To set up configurations quickly across multiple nodes, configure
    the settings for the original VM, then clone it using **Machine \>
    Clone**. For example, if a management VM is being created for the
    new topology, set the `eth0` port to be on a virtual network that
    the management VM is on. When you clone the new VM, the port will be
    duplicated, creating an out-of-band (OOB) network.

  - When you clone the VM, save the new VM on disk storage by referring
    to the original disk image, instead of copying it to the new VM.

  - Always reset MAC addresses on the virtual NICs, unless a critical
    reason not to exists.

{{%/notice%}}

## <span>VirtualBox Caveats and Errata</span>

Consider the following caveats and expected behaviors when using Cumulus
VX with VirtualBox:

  - You must select an OS type to export a setup. However, a bug exists
    in VirtualBox when the OS type `other` or `unknown` is selected;
    while the VM works, the exported appliance does not import
    correctly.

  - Make sure to enable hardware virtualization in the host OS BIOS
    before starting the VM if you are using VirtualBox as the
    hypervisor, as some operating systems might not enable it by
    default.

  - An error message might appear when booting a VirtualBox OVA image
    for the first time stating that the interfaces file must be
    modified. If this occurs, click **OK** and continue booting. This is
    expected VirtualBox behavior, which is likely due to the physical
    interface against which the VM is being bridged and is highly
    dependent on the physical computer you are using. Some systems use
    `en0` as the wireless interface, others use `en3`, and a plugged-in
    Ethernet port would be `en1`. The OVA requests the first interface,
    which might not be up and active on your system when you import the
    image, causing the error message.

### <span>Network Interface Limitations</span>

By default, the VirtualBox Manager only displays the first 8 virtual
NICs, and you can only modify the first 4. However, if you plan on using
more than 8 virtual network interfaces, you can run the `VBoxManage`
command to configure and use up to 36 virtual NICs:

1.  With the VM powered off, edit the VM settings.

2.  Select the **System** tab.

3.  On the **Motherboard** tab, in the **Chipset** list, select `ICH9`,
    then check **Enable I/O APIC**.  
    
    {{% imgOld 1 %}}

4.  Click **OK** to save the settings.

{{%notice tip%}}

Alternately, use the `VBoxManage modifyvm` command to update these
settings:

    user@localhost:~$ VBoxManage modifyvm cumulus-vx-2.5.3-vbox --ioapic on
    user@localhost:~$ VBoxManage modifyvm cumulus-vx-2.5.3-vbox --chipset ich9

{{%/notice%}}

After you configure the chipset and enable the I/O APIC, use the
` VBoxManage showvminfo  `command to verify that the 36 virtual NICs are
available:

    user@localhost:~$ VBoxManage showvminfo cumulus-vx-2.5.3-vbox | grep "\(NIC\|IOAPIC\|Chipset\)"
    Chipset:         ich9
    IOAPIC:          on
    NIC 1:           MAC: 0800273A02E3, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: virtio, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
    NIC 2:           MAC: 0800279EC543, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: virtio, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
    NIC 3:           MAC: 08002743C9A3, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: virtio, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
    NIC 4:           MAC: 08002735DC73, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: virtio, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
    NIC 5:            disabled
    NIC 6:            disabled
    NIC 7:            disabled
    NIC 8:            disabled
    NIC 9:            disabled
    NIC 10:           disabled
    NIC 11:           disabled
    NIC 12:           disabled
    NIC 13:           disabled
    NIC 14:           disabled
    NIC 15:           disabled
    NIC 16:           disabled
    NIC 17:           disabled
    NIC 18:           disabled
    NIC 19:           disabled
    NIC 20:           disabled
    NIC 21:           disabled
    NIC 22:           disabled
    NIC 23:           disabled
    NIC 24:           disabled
    NIC 25:           disabled
    NIC 26:           disabled
    NIC 27:           disabled
    NIC 28:           disabled
    NIC 29:           disabled
    NIC 30:           disabled
    NIC 31:           disabled
    NIC 32:           disabled
    NIC 33:           disabled
    NIC 34:           disabled
    NIC 35:           disabled
    NIC 36:           disabled

The above output shows that `NIC 1` corresponds to the `eth0` management
interface, while `NICs 2-36` correspond to the `swp1-35` switch port
interfaces. You can configure the interfaces with the `VBoxManage
modifyvm` commands. See the [VirtualBox networking
documentation](https://www.virtualbox.org/manual/ch06.html) and
[VBoxManage command
reference](https://www.virtualbox.org/manual/ch08.html#idp104314528) for
more information on configuring virtual NICs.
