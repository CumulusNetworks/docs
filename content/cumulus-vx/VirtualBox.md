---
title: VirtualBox
author: Cumulus Networks
weight: 25
product: Cumulus VX
version: '4.x'
---
This section describes how to install and set up Cumulus VX in VirtualBox to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with Cumulus VX 4.2 and VirtualBox version 6.1.12 on macOS version 10.14.6.

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes you have VirtualBox experience.

### Download and Install the Software

1. Download and install {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox">}}.

2. Download the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="OVA VirtualBox image">}}.

### Create the VMs

{{% notice note %}}

The Cumulus VX OVA image defines the CPU, memory, and disk requirements. Cumulus VX requires at least 768MB of RAM and 6GB of disk space.

{{% /notice %}}

{{% vx/virtualbox-steps %}}

### Create Network Connections

VirtualBox network adapters start with eth0, then swp1, swp2 and swp3. Settings for Adapter 1 are applied to eth0, settings for Adapter 2 are applied to swp1, and so on.

Configure the network adapter settings for leaf01, leaf02, and spine01 to create point-to-point connections, as shown below.

{{< figure src = "/images/cumulus-vx/VX-Connections.png" >}}

Follow these steps for each VM (leaf01, leaf02, and spine01):

1. In the VirtualBox Manager window, select the VM.

2. Click **Settings**, then click **Network**.

3. Configure the **Adapters** on each VM as shown below, then click **OK** to save the network connections.

   - Make sure you select the **Paravirtualized Network (virtio net)** network Adapter Type.

   - Due to how VirtualBox manages link-local multicast frames, you must enable **Promiscuous Mode** on all adapters (except Adapter 1) to allow for LACP bonding to operate properly.

   - Do not change the MAC address, which is automatically created.

   **leaf01 configuration**

      {{< tabs "TabID01 ">}}

{{< tab "Adapter 1 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter1-leaf01.png" width="400" >}}

{{< /tab >}}

{{< tab "Adapter 2 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter2-leaf01.png" width="400" >}}

{{< /tab >}}

{{< tab "Adapter 3 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter3-leaf01.png" width="400" >}}

{{< /tab >}}

{{< tab "Adapter 4 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter4-leaf01.png"  width="400" >}}

{{< /tab >}}

{{< /tabs >}}

   **leaf02 configuration**

   {{< tabs "TabID02 ">}}

{{< tab "Adapter 1 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter1-leaf02.png"  width="400" >}}

{{< /tab >}}

{{< tab "Adapter 2 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter2-leaf02.png"  width="400" >}}

{{< /tab >}}

{{< tab "Adapter 3 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter3-leaf02.png"  width="400" >}}

{{< /tab >}}

{{< tab "Adapter 4 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter4-leaf02.png"  width="400" >}}

{{< /tab >}}

{{< /tabs >}}

   **spine01 configuration**

   {{< tabs "TabID03 ">}}

{{< tab "Adapter 1 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter1-spine01.png"  width="400" >}}

{{< /tab >}}

{{< tab "Adapter 2 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter2-spine01.png"  width="400" >}}

{{< /tab >}}

{{< tab "Adapter 3 ">}}

{{< img src="/images/cumulus-vx/vbox-adapter3-spine01.png"  width="400" >}}

{{< /tab >}}

{{< /tabs >}}

4. Power on the VMs.

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
