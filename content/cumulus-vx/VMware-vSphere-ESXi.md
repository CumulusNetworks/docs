---
title: VMware vSphere ESXi
author: Cumulus Networks
weight: 30
---
This section describes how to install and set up Cumulus VX in VMWare vSphere to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with VMware vSphere (ESXi) Standard version 7.0b and web client version ??.

## Create and Configure the VMs

The following procedure describes how to create a VM in VMWare vSphere for each switch in the example topology (leaf01, leaf02, and spine01). This section assumes you have a basic level of VMWare vSphere experience.

### Download and Install the Software

1. Download and install the {{<exlink url="https://my.vmware.com/web/vmware/details?productId=352&downloadGroup=OVFTOOL350" text="VMware OVFtools utility">}} on the vSphere Client.
2. Download the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="OVA disk image for use with VMware">}}.

### Create the VMs

1. Connect the vSphere client to the vSphere ESXi server using the IP address and user credentials of the ESXi server.

2. From the **File** menu of the vSphere client window, click **Deploy OVF Template** to open the import window.

3. Select **Browse**, locate the Cumulus VX OVA image, then click **Next** to continue.

4. Review the template details, then click **Next**.

5. Edit the name of the VM to `leaf01`, then click **Next**.

    {{< img src="/images/cumulus-vx/VX_esxi_deploy3_name.png" width="300" >}}

6. As the Cumulus VX image is preconfigured, no more set up options are required. Click **Next** until you see the `Ready to Complete` window:

    {{< img src="/images/cumulus-vx/VX_esxi_deploy4_ready.png" width="300" >}}

7. If you want the VM to start immediately after the import process is complete, select the `Power on after deployment` option, then click **Finish**.

   The Cumulus VX OVA image is imported into vSphere ESXi and deployed as a VM. The length of the import process depends on the system configuration. You can view the progress in the `Recent Tasks` pane at the bottom of the client window. After the deployment process is complete, the newly created VM appears in the list of VMs in the left pane.

   {{< img src="/images/cumulus-vx/VX_esxi_deploy5_deploying.png" width="500" >}}

8. Repeat the previous steps to create two additional VMs: `leaf02` and `spine01`.

If the wrong storage interface type is selected, you might see the error `Setting up installer ...Failure: Unable to find storage device for file system with label 'ONIE-BOOT'`. Configure ESXi to use the SATA controller.

### Create Network Connections

Add section here

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
