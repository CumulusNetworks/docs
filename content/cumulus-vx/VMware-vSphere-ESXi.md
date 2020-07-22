---
title: VMware vSphere ESXi
author: Cumulus Networks
weight: 20
---
This section describes how to install and set up Cumulus VX in VMWare vSphere to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with VMware vSphere (ESXi) Standard version 7.0b on macOS version 10.14.6.

## Create the VMs

The following procedure describes how to create a VM in VMWare vSphere for each switch in the example topology (Leaf01, Leaf02, and Spine01). This section assumes a basic level of VMWare vSphere experience.

1. Download and install the VMWare vSphere ESXi hypervisor. Refer to the {{<exlink url="http://www.vmware.com/products/vsphere.html" text="VMWare vSphere documentation">}}.

2. Download the OVA disk image for use with VMware from the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus Networks website">}}.

3. Download the VMware OVFtools utility from the {{<exlink url="https://my.vmware.com/web/vmware/details?productId=352&downloadGroup=OVFTOOL350" text="VMware downloads page">}} and install it on the client. You can view installation instructions on the VMware website.

4. Connect the vSphere client to the vSphere ESXi server using the IP address and user credentials of the ESXi server.

5. In the vSphere client window, click **File > Deploy OVF Template** to open the import window.

6. Select **Browse**, locate the Cumulus VX OVA file, then click **Next** to continue.

7. Review the template details, then click **Next**.

8. In the text box, edit the name of the VM to `Leaf01`, then click **Next**.

    {{< img src = "/images/cumulus-vx/VX_esxi_deploy3_name.png" >}}

9. As the Cumulus VX image is preconfigured, no more set up options are required. Click **Next** through the next few windows until you see the `Ready to Complete` window:

    {{< img src = "/images/cumulus-vx/VX_esxi_deploy4_ready.png" >}}

10. If you want the VM to start immediately after the import process is complete, select the `Power on after deployment` option, then click **Finish**.

   The Cumulus VX OVA image is imported into vSphere ESXi and deployed as a VM. The length of the import process depends on the system configuration. You can view the progress in the `Recent Tasks` pane at the bottom of the client window. After the deployment process is complete, the newly created VM appears in the list of VMs in the left pane.

   {{< img src = "/images/cumulus-vx/VX_esxi_deploy5_deploying.png" >}}

11. Repeat the previous steps to create two additional VMs: `Leaf02` and `Spine01`.

{{%notice note%}}

If the wrong storage interface type is selected, you might see an error similar to:

`Setting up installer ...Failure: Unable to find storage device for file system with label 'ONIE-BOOT'`

Configure ESXi to use the SATA controller.

{{%/notice%}}

## Create Connections Between VMs

Add section here

## Basic Switch Configuration

{{% vx/basic-config %}}

## Next Steps

{{% vx/next-steps %}}
