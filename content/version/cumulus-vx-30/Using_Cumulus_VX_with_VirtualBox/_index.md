---
title: Using Cumulus VX with VirtualBox
author: Cumulus Networks
weight: 13
aliases:
 - /display/VX30/Using+Cumulus+VX+with+VirtualBox
 - /pages/viewpage.action?pageId=5126581
pageID: 5126581
product: Cumulus VX
version: '3.0'
imgData: cumulus-vx-30
siteSlug: cumulus-vx-30
---
Once you [install VirtualBox](https://www.virtualbox.org/wiki/Downloads)
and [download the OVA
image](https://cumulusnetworks.com/cumulus-vx/download/), you will
import it into VirtualBox, then clone it a few times to create a
two-leaf/two-spine virtual network.

The resulting configuration contains four VMs:

  - Two spine VMs, which represent two spine (aggregation layer)
    switches on the network

  - Two leaf VMs, which represent two leaf (access layer) switches on
    the network

{{% imgOld 0 %}}

Follow [these
steps](/version/cumulus-vx-30/Using_Cumulus_VX_with_VirtualBox/Creating_a_Two-Spine_Two-Leaf_Topology)
to create this configuration.

{{%notice note%}}

This configuration was tested on a server running Debian 3.2.60-1+deb7u3
x86\_64 GNU/Linux with 3.2.0-4-amd64 \#1 SMP processors.

{{%/notice%}}

{{%notice warning%}}

If you are running VirtualBox on a host OS other than Linux, before you
launch the VM, you should explicitly assign each Cumulus VX interface to
a virtual adapter or internal network; don't keep the VirtualBox default
assignments.

{{%/notice%}}

## <span>Using a Single Switch Configuration</span>

On its own, the Cumulus VX virtual machine is a standalone virtualized
instance of a network switch. Once you download and import it into your
hypervisor, you will see a single node. Since the default
`/etc/network/interfaces` file in the VM only attempts to use DHCP on
the eth0 interface, it will try to get an IP address on that one port.
From here you can use the VM as you see fit.

The virtual NIC to VM device mappings are as follows:

|                        |                                         |
| ---------------------- | --------------------------------------- |
| **This Virtual NIC …** | **Maps to this Cumulus Linux Device …** |
| Adapter 1              | eth0                                    |
| Adapter 2              | swp1                                    |
| Adapter 3              | swp2                                    |
| Adapter 4              | swp3                                    |

Once you install the VM, you can reconfigure how the NICs are used
depending on what sort of connectivity you need.

<span id="src-5126581_UsingCumulusVXwithVirtualBox-reqs"></span>

## <span>VirtualBox-specific Considerations</span>

Keep in mind the following expected behaviors regarding VirtualBox and
the VM.

### <span>Exporting VirtualBox Configurations</span>

If you want to export your setup, you **must** select an OS type.
However, there appears to be a bug in VirtualBox when the VM has an OS
type of *other* or *unknown*. The VM works; however, the exported
appliance will not import correctly.

### <span>Enabling Hardware Virtualization in the BIOS</span>

If you are using VirtualBox as your hypervisor, make sure you enable
hardware virtualization in the host OS BIOS before starting the VM, as
some operating systems may not do so by default.

### <span>Interfaces Error when Booting</span>

If you see an error message when you boot a VirtualBox OVA image for the
first time, saying you must modify the interfaces file, you can click
**OK** and continue booting. This issue is likely due to the physical
interface the VM is being bridged against, and is highly dependent of
the physical computer you are using. Some systems use en0 as the
wireless interface, on others the wireless uses en3 and a plugged-in
Ethernet port would be en1. The OVA requests the first interface, which
may not actually be up and active on your system when you import the
image. This is expected VirtualBox behavior.

### <span>Network Interface Limitations</span>

By default, the VirtualBox Manager only displays the first 8 virtual
NICs, and you can modify only the first 4. However, if you plan on using
more than 8 virtual network interfaces, you can run the `VBoxManage`
command to configure and use up to 36 virtual NICs.

First, you need to update the VM's motherboard settings:

1.  With the VM powered off, edit the VM's settings.

2.  Choose the **System** tab.

3.  On the **Motherboard** tab, in the **Chipset** list, select *ICH9*,
    then check **Enable I/O APIC**.
    
    {{% imgOld 1 %}}

4.  Click **OK** to save your settings.

{{%notice tip%}}

Alternately, you can use the `VBoxManage modifyvm` command to update
these settings:

    $ VBoxManage modifyvm cumulus-vx-2.5.3-vbox --ioapic on
    $ VBoxManage modifyvm cumulus-vx-2.5.3-vbox --chipset ich9

{{%/notice%}}

After you configure the chipset and enable the I/O APIC, you can verify
that 36 virtual NICs are available. Run `VBoxManage showvminfo`:

    $ VBoxManage showvminfo cumulus-vx-2.5.3-vbox | grep "\(NIC\|IOAPIC\|Chipset\)"
    Chipset:         ich9
    IOAPIC:          on
    NIC 1:           MAC: 0800273A02E3, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: virtio, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
    NIC 2:           MAC: 0800279EC543, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: virtio, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
    NIC 3:           MAC: 08002743C9A3, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: virtio, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
    NIC 4:           MAC: 08002735DC73, Attachment: Bridged Interface 'eth0', Cable connected: on, Trace: off (file: none), Type: virtio, Reported speed: 0 Mbps, Boot priority: 0, Promisc Policy: deny, Bandwidth group: none
    NIC 5:           disabled
    NIC 6:           disabled
    NIC 7:           disabled
    NIC 8:           disabled
    NIC 9:           disabled
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

In the above output, NIC 1 corresponds to the eth0 management interface,
while NICs 2-36 correspond to the swp1-35 switch port interfaces. You
can configure all of these interfaces with VBoxManage modifyvm commands.
See the [VirtualBox networking
documentation](https://www.virtualbox.org/manual/ch06.html) and
[VBoxManage command
reference](https://www.virtualbox.org/manual/ch08.html#idp104314528) for
more information on configuring virtual NICs.
