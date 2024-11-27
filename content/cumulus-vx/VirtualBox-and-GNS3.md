---
title: VirtualBox and GNS3
author: NVIDIA
weight: 30
product: Cumulus VX
version: '5.x'
---

This section describes how to install and set up Cumulus VX with VirtualBox and GNS3 to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

<!-- vale off -->
These steps were tested with Cumulus VX 4.2, VirtualBox version 6.1.12, and GNS3 version 2.2.11 on macOS version 10.14.6.
<!-- vale on -->

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes you have VirtualBox and GNS3 experience.

### Download and Install the Software

1. Download and install {{<exlink url="https://www.virtualbox.org" text="VirtualBox">}}.
2. Download and install {{<exlink url="https://www.gns3.com/software" text="GNS3">}}.
3. Download the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/cumulus-vx/" text="VirtualBox OVA image">}}.

### Create VMs in VirtualBox

{{%notice note%}}
The Cumulus VX OVA image defines the CPU, memory, and disk requirements. Cumulus VX requires at least 768MB of RAM and 6GB of disk space.

CumulusVX versions 4.3 and later requires 2 vCPUs.

{{%/notice%}}

{{% vx/virtualbox-steps %}}

### Configure GNS3

1. Open the GNS3 application and create a new project.
2. From the **GNS3** menu, select **Preferences**.
3. From the left pane of the Preferences dialog, select **VirtualBox**. Then, in the **Path to VBoxManage** field, enter the location where you installed VBoxManage. For example: `/usr/bin/VBoxManage`.
4. From the left pane, select **VirtualBox VMs**, then click **New**. The **VM list** shows the VirtualBox VMs you set up earlier.

   {{< img src="/images/cumulus-vx/gns3-new.png" width="300" >}}

5. From the **VM list**, select leaf01, then click **Finish**. The VM you selected appears in the center pane. Repeat this step for leaf02 and spine01.

6. Enable GNS3 to work with the network interfaces of the VirtualBox VMs:

   1. In the center pane, select leaf01 then click **Edit**.
   2. In the VirtualBox VM template configuration dialog, click the **Network** tab.
   3. Increase the number of **Adapters** to *4*.
   4. From the **Type** dropdown, select *Paravirtualized Network*.
   5. Select **Allow GNS3 to use any configured VirtualBox adapter**.

      {{< img src="/images/cumulus-vx/gns3-network.png" width="300" >}}

   6. Click **OK** to save your settings and close the dialog.
   7. Repeat these steps for leaf02 and spine01, then click **OK** to close the Preferences dialog.

### Create Network Connections

Create the network connections between leaf01, leaf02, and spine01, as shown in the two leaf, one spine topology {{<link url="VirtualBox-and-GNS3" text="above">}}.

1. Click {{< img src="/images/cumulus-vx/icon-show-all-devices.png" height="18" width="18" >}} (Browse all Devices button), then from the `End Devices` panel, drag leaf01, leaf02, and spine01 to the console.
2. Click the {{< img src="/images/cumulus-vx/icon-cable.png" height="18" width="18" >}} (cable icon), then connect the leafs and spine by selecting the network interfaces, as shown in the Topology Summary below:
   - `e1` in GNS3 corresponds to `swp1` in Cumulus VX
   - `e2` in GNS3 corresponds to `swp2` in Cumulus VX
   - `e3` in GNS3 corresponds to `swp3` in Cumulus VX

{{< img src="/images/cumulus-vx/gns3-network-connections.png" width="500" >}}

3. Start the VMs.

## Log in to the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
