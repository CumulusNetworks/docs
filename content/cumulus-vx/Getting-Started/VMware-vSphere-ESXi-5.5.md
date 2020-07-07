---
title: VMware vSphere - ESXi 5.5
author: Cumulus Networks
weight: 37
pageID: 5126689
---
The following sections describe how to import and set up a two-leaf and two-spine Cumulus VX topology with VMware vSphere. These sections assume a basic level of VMware vSphere experience. For detailed instructions, refer to the {{<exlink url="https://docs.vmware.com/en/VMware-vSphere/index.html" text="VMware vSphere documentation">}}.

## Create a Cumulus VX VM with VMware vSphere ESXi

This section assumes that you have downloaded the Cumulus VX disk image for VMware hypervisors and that the VMware vSphere is installed. For more download locations and steps, refer to the {{<link url="Getting-Started" text="Getting Started">}}.

{{%notice note%}}

You might encounter an issue if the wrong storage interface type is selected (SATA or IDE). For example this log message indicates the filesystem cannot be found. Configure ESXi to use the SATA controller.

```
Info: Fetching http://192.168.100.1/onie-installer-cumulus_vx ...
ONIE: Executing installer: http://192.168.100.1/onie-installer-cumulus_vx
Verifying image checksum ...OK.
Preparing image archive ... OK.
Verifying image compatibility ...OK.
Verifying system ram ...OK.
Setting up installer ...Failure: Unable to find storage device for file system with label 'ONIE-BOOT'
Info: Check the output of 'blkid'.
```

{{%/notice%}}

This configuration was tested using vSphere ESXi 5.5 and a Windows vSphere client; however, the VM is configured to support ESXi 4.0 and higher.

1. Download the VMware OVFtools utility from the {{<exlink url="https://my.vmware.com/web/vmware/details?productId=352&downloadGroup=OVFTOOL350" text="VMware downloads page">}} and install it on the client. You can view installation instructions on the VMware website.

2. Connect the vSphere client to the vSphere ESXi server using the IP address and user credentials of the ESXi server.

3. In the vSphere client window, click **File \> Deploy OVF Template** to open the import window.

4. Select **Browse**, locate the Cumulus VX OVA file, then click **Next** to continue.

5. Review the template details, then click **Next**.

6. In the text box, edit the name of the VM to `CumulusVX-leaf1`, then click **Next**.

    {{< img src = "/images/cumulus-vx/VX_esxi_deploy3_name.png" >}}

7. As the Cumulus VX image is preconfigured, no more set up options are required. Click **Next** through the next few windows until you see the `Ready to Complete` window:

    {{< img src = "/images/cumulus-vx/VX_esxi_deploy4_ready.png" >}}

8. If you want the VM to start immediately after the import process is complete, select the `Power on after deployment` option, then click **Finish**.

The Cumulus VX OVA image is imported into vSphere ESXi and deployed as a VM. The length of the import process depends on the system configuration. You can view the progress in the `Recent Tasks` pane at the bottom of the client window. After the deployment process is complete, the newly created VM appears in the list of VMs in the left pane.

{{< img src = "/images/cumulus-vx/VX_esxi_deploy5_deploying.png" >}}

9. The two-leaf and two-spine network topology requires you to create four VMs. Repeat the previous steps to create three additional VMs. Replace the name `CumulusVX-leaf1` with:

   - `CumulusVX-leaf2`
   - `CumulusVX-spine1`
   - `CumulusVX-spine2`

2. After you have created all four VMs, follow the steps detailed in [Create a Two-Leaf, Two-Spine Topology](/cumulus-vx/Create-a-Two-Leaf-Two-Spine-Topology) to configure the network interfaces and routing.
