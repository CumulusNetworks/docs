---
title: 
author: 
weight: 
aliases:
 - 
  -
 - 
pageID:
---
``` 
~Note~ 

There are 2 ways to use GNS3 with VMware: 
Option 1: Nested Virtualization of GNS3 VM within VMware
Option 2: Running Locally within GNS3 (no nested virtualization)

Both options will be shown in this demo. 
``` 
# **Nested Virtualization of GNS3 VM within VMware Workstation Player** 
{{%notice note%}} 

This demo was done on a Windows 10 device. If your machine isn't Windows, GNS3’s site has Windows, MacOSX, & Linux [installation instructions](https://docs.gns3.com). 

{{%/notice%}} 

#### 1. Download & Install GNS3 

>This demo will be based on GNS3 v.2.2.6 & VMware Workstation Player 14. 

Go to GNS3’s GitHub, download and install [v2.2.6](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.6) named GNS3-2.2.6-all-in-one.exe. During installation use all the default settings, for simplicity of this installation. (GNS3 will install several other programs).

![v226Download](/images/cumulus-vx/GNS3_Player/01_v226download.png)

![Download GNS3](/images/cumulus-vx/GNS3_regular/1_gns3Download_chooseComponents.png)

After installation, open GNS3 & hit **Cancel** on the Setup Wizard.

![setupWizard](/images/cumulus-vx/GNS3_regular/2_gns3Download_hitCancel.png)

On the right side panel under Servers Summary, the green button means successful download of the GNS3 GUI; the local GNS3 server is running. If there’s no green button, it may help to restart your machine and restart GNS3. (If still no luck, check your antivirus and your firewall.) 

![serverSummary](/images/cumulus-vx/GNS3_regular/1_server_summary.png)

#### 2. Download & Install the GNS3 VM (OVA file) for VMware
The GNS3 VM will run within VMware Workstaion Player (Type 2 Hypervisor) for nested virtualization. From GNS3's GitHub page, Download & Install the GNS3 VM [zip file](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.6) named **GNS3.VM.Wmware.workstation2.2.6.zip**. The GNS3 GUI and the GNS3 VM must be using the same version. 

![VMdownload](/images/cumulus-vx/GNS3_Player/02_v226downloadVM.png)

#### 3. Download & Install VMware Workstation Player 14
There are many versions of GNS3 and Workstation Player. From a lot of trial and error, the combination of versions that work together are: GNS3 v2.2.6 & VMware Player 14.  
Download & Install [VMware Workstation Player 14](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/14_0|PLAYER-1418|product_downloads).

![PlayerDownload](/images/cumulus-vx/GNS3_Player/03_PlayerDownload.png)

#### 4. Integrate GNS3 VM & VMware Player for nested virtualization

Extract the files from the GNS3.VM.VMware zip download from earlier, which contains the OVA file. Open Workstation Player, click **Player** > **File** > **Open** to open up a virtual machine. Select the GNS3 VM OVA file. Leave everything at default, and Click **Import** to import the GNS3 VM into Workstation Player.

![OVAfile](/images/cumulus-vx/GNS3_regular/3_gns3OVAfile.png)

![importOVA](/images/cumulus-vx/GNS3_Player/4_gns3_into_workstation.png)

 #### 5. Integrate the GNS3 GUI with the GNS3 VM. 

So far GNS3 GUI, a type-2 hypervisor (VMware), and GNS3 VM have been downloaded. Now to integrate the GNS3 GUI with the GNS3 VM.
Open GNS3. The Setup Wizard will appear. Select **Run modern IOS…**, then click **Next** on the next few prompts. 

![setupWizard](/images/cumulus-vx/GNS3_regular/2_gns3Download_hitCancel.png)

After selecting **Next** a few times, this prompt may appear; follow it’s directions.

![vixError](/images/cumulus-vx/GNS3_Player/04_vixError.png)

Go to [https://www.vmware.com/support/developer/vix-api/](https://www.vmware.com/support/developer/vix-api/) like instructed, click on **SDK 1.15**,

![DownloadVix](/images/cumulus-vx/GNS3_Player/05_downloadVIX.png)

and select the appropriate VIX software download for your machine.

![DownloadVix](/images/cumulus-vx/GNS3_Player/06_downloadVIX.png)

In the meantime, close GNS3 again. After the installation of the VIX download is finished, once again open up GNS3. New Project prompt will appear; name it whatever you’d like. Now we need to integrate the GNS3 GUI with the GNS3 VM. Go to **Edit** > **Preferences** > **GNS3 VM**. Click the Enable the GNS3 VM box. In the Virtualization engine section, select VMware Workstation / Player. In the Settings section, Refresh the VM name and select GNS3 VM. Click **Apply**, then **OK**.

![preferences](/images/cumulus-vx/GNS3_regular/5_gns3VM_preferences.png)

Go back to the Setup Wizard (**Help** > **Setup Wizard**) select **Run modern IOS…**, then click **Next** on the Next few prompts... Now the warning message from earlier should not reappear, and the GNS3 VM setup should appear! Select VMware as the virtualization software, and GNS3 VM as your VM name. If desired, keep the default settings, and click **Next**.

![SetupWizard](/images/cumulus-vx/GNS3_Player/NewSetupWizard.png)

Servers Summary on the right-hand side should display your GNS3 VM.

![ServersSummaryWithVM](/images/cumulus-vx/GNS3_Player/ServersSummaryWithVM.png)

VMware Player should automatically start. 

![GNS3VMinPlayer](/images/cumulus-vx/GNS3_Player/GNS3VMinVMware.png)

Now that everything is integrated and acting right, choose **Take Ownership** then **OK** to start the Player.

![TakeOwnership](/images/cumulus-vx/GNS3_Player/TakeOwnership.png)

If this warning appears, shut down your machine and make the necessary changes.

![BIOSchange](/images/cumulus-vx/GNS3_Player/BIOS.png)

Startup your machine again, open up GNS3 again, if the prompt about Virtualized Intel VT-x/EPT appears, just choose Yes.

![virtualizedIntel](/images/cumulus-vx/GNS3_Player/virtualizedIntel.png)

“Disable KVM and get lower performances?” Select No

>Your mouse has to be within WMware Player window in order to select anything; if the mouse is outside the VMware Player window, there will be no response.

![KVM](/images/cumulus-vx/GNS3_Player/KVM.png)

Based on your machine and OS, you may have to update the BIOS or chose specific Virtual Machine Settings within VMware Workstation Player: highlight the VM > right click > **Settings** > **Hardware** > **Processors** > under the Virtualization engine section, check the Virtualize Intel VT -x/EPT or AMD-V/RVI box.

![VMsettings](/images/cumulus-vx/GNS3_Player/VMsettings.png)

At this point, the nested virtualization of GNS3 VM into Workstation Player to be used with the GNS3 GUI is complete. Next step is to incorporate Cumulus VX in GNS3. Close GNS3.

![KVM_True](/images/cumulus-vx/GNS3_Player/KVM_True.png)

#### 6. Download & Install the Cumulus VX Appliance from the GNS3 site

Go to GNS3 site, click Marketplace, and Search for Cumulus VX Appliances or click [here](https://gns3.com/marketplace/appliance/cumulus-vx).

![cumulusappliance](/images/cumulus-vx/GNS3_regular/6_gns3_cumulusvx.png)

#### 7. Download & Install Cumulus VX 
Open GNS3, **File** > **Import Appliance** > select the downloaded Cumulus VS appliance > **OK**. Select the default settings for the next few prompts until reaching the “Required files” prompt. 

![downloadAppliance](/images/cumulus-vx/GNS3_regular/8_downloadAppliance.png)

A list of Cumulus VX versions and files will be shown. (Version 3.7.6 will be used in this demo) Navigate to the Cumulus VX download page [here](https://cumulusnetworks.com/products/cumulus-vx/download/). Select the appropriate version, and download that **.qcow2 file**. This download should take a few minutes.

![cumulusVX](/images/cumulus-vx/GNS3_regular/9_downloadAppliance.png)

![qcow2](/images/cumulus-vx/GNS3_regular/10_downloadAppliance.png)

Back to the appliance installation in GNS3, click **Import** and import the .qcow2 download. The Status should go from “Missing files” to “Ready to Install”. Highlight the file, click **Next**, & click **Yes** to begin the install.

![import](/images/cumulus-vx/GNS3_regular/11_import.png)

![downloadAppliance](/images/cumulus-vx/GNS3_regular/11_downloadAppliance.png)

![downloadAppliance](/images/cumulus-vx/GNS3_regular/12_downloadAppliance.png)

>***Take note of the username and password*** & click **Finish**. 
 
![username&password](/images/cumulus-vx/GNS3_regular/13_downloadAppliance.png)
 
#### 8. Configuring Cumulus VX virtual machine!! 
So far, the nested virtualization of GNS3 VM into Workstation Player to be used with the GNS3 GUI is complete, and a Cumulus VX appliance has been imported into GNS3. In GNS3, click **Browse Switches** icon, and the imported Cumulus VX virtual machine should appear. 
 
![BrowseAppliances](/images/cumulus-vx/GNS3_regular/14_useTheAppliance.png)

{{%notice note%}} 

If this is the reader’s first time using GNS3, it’s recommended to read the [“Your First GNS3 Topology”](https://docs.gns3.com/1wr2j2jEfX6ihyzpXzC23wQ8ymHzID4K3Hn99-qqshfg/index.html) doc on GNS3’s site. 

{{%/notice%}} 

Here’s a simple topology. Let’s configure the devices so the end hosts can ping each other.

![topology](/images/cumulus-vx/GNS3_regular/15_topology.png)

- To download the UbuntuDockerGuest appliance: GNS3 site > Marketplace > Appliances > Ubuntu Docker Guest > Download To Import the appliance into GNS3: [https://docs.gns3.com/1_3RdgLWgfk4ylRr99htYZrGMoFlJcmKAAaUAc8x9Ph8/index.html](https://docs.gns3.com/1_3RdgLWgfk4ylRr99htYZrGMoFlJcmKAAaUAc8x9Ph8/index.html) - This demo uses UbuntuDockerGuest as the host; the VPCS host in GNS3 can be used also….. End hosts are NOT needed to configure the Cumulus devices.

How to change Interface MAC Address in VMware Workstaton Player: Highlight the GNS3 VM > **Settings** > **Network**> select a **Network Adapter** > **Advanced** > from there view or change the MAC Address > **OK**

![macAddress](/images/cumulus-vx/GNS3_Player/macAdd.png)

Start all the nodes, and open all the consoles. 
>The console sessions should open up using Solar-PuTTY (during download of GNS3, if you OK’ed all the default settings, Solar-PuTTY was downloaded also). The console sessions for the Cumulus devices take a few moments. 

Right click on a UbuntuGuest, select **Edit config**, and change the network values of the interface. Do this to both hosts. 

![vpcs](/images/cumulus-vx/GNS3_regular/18_VPCS_ip.png)

On the Ubuntu machines, run `ifconfig` to verify your new network changes. For the Cumulus devices: Remember the password and username from earlier? Use those to login.

>***Username: cumulus 
Password: CumulusLinux!*** 

Take note that `whoami` shows the username of the Cumulus devices is cumulus; `sudo` will be needed to run privileged commands in the Cumulus devices. 

![login](/images/cumulus-vx/GNS3_regular/16_login.png)

Run `ifconfig` to show there are no network settings yet. Running `cat /etc/networks/interfaces` shows that eth0 is configured using DHCP; also eth0 is the management port. 
Let’s add a Switch and a NAT cloud to the topology so the Cumulus devices can receive an ip address on eth0 via DHCP.

![NEWtopology](/images/cumulus-vx/GNS3_regular/19_topologyNew.png) 

Run `ifconfig` & there’s now an ip address assigned to eth0. 

{{%notice note%}}

The rest of this demo will be following the Configure Switch Ports steps from the [Cumulus Linux v3.7 ‘Quick Start Guide’](https://docs.cumulusnetworks.com/cumulus-linux-37/Quick-Start-Guide/) to configure swp1 and swp2.

{{%/notice%}} 

Edit the /etc/network/interfaces file; remember to use `sudo` in order to edit the network interfaces. 
`auto swp1`
`iface swp1`
`auto swp2`
`iface swp2`

![NetworkInterfaces](/images/cumulus-vx/GNS3_regular/21_swp1_swp2.png)

Save the file, exit the file, reload the configuration using `sudo ifreload -a`, run `ifconfig`. You should now see the addition of swp1 and swp2 interfaces. 

![ifreload](/images/cumulus-vx/GNS3_regular/22_ifreload.png)

Let’s add swp1 and swp2 to a bridge, reload the configuration, view the bridge settings, & display the bridge interface. 
`auto bridge`
`iface bridge`
`bridge-ports swp1 swp2`
`bridge-vlan-aware yes`
Exit the file.
`sudo ifreload -a`
`brctl show`

![brctlshow](/images/cumulus-vx/GNS3_regular/23_brctlshow.png)

The Cumulus VX devices have been properly configured, and now the Ubuntu machines can Ping each other!

![ping](/images/cumulus-vx/GNS3_regular/24_successfulPing.png)

>In this demo, you: 
>- Downloaded GNS3, GNS3 VM, and a Type-2 hypervisor VMvware Workstation Player
>- Configured nested virtualization between GNS3 VM and VMware Player to be used within GNS3
>- Imported a Cumulus VX virtual machine within GNS3
>- Configured the Cumulus VX virtual machine: 2 switch ports & a bridge in order to for two hosts to ping each other




# **Running Locally within GNS3 (no nested virtualization)**

{{%notice note%}}

This demo was done on a Windows 10 device. If your machine isn't Windows, GNS3’s site has Windows, MacOSX, & Linux [installation instructions](https://docs.gns3.com).

{{%/notice%}}

#### 1. Download & Install VMware Workstation Player

There are many versions of GNS3 and Workstation Player. From a lot of trial and error, the combination of versions that work together are: GNS3 v2.2.6 & VM Player 14. Download & Install [WMware Workstation Player 14](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/14_0|PLAYER-1418|product_downloads)

![Player14](/images/cumulus-vx/GNS3_Player/03_PlayerDownload.png)

#### 2. Download and Install the Cumulus VX OVA image(s) for WMware Workstation Player
    
Navigate to the [Cumulus VX]((https://cumulusnetworks.com/products/cumulus-vx/download/)) download page. Select the appropriate version, and download that VMware OVA image. Version 3.7.6 will be used in this demo.

![cumulusOVA](/images/cumulus-vx/GNS3_regular/9_downloadAppliance.png)

![OVA](/images/cumulus-vx/GNS3_Player/2_ovaImage.png)

#### 3. Create a Cumulus VX VM in Workstation Player & Edit Settings 
Open VMware Workstation Player. **Player** > **File** > **Open** > select the Cumulus VX OVA file.

![NewVMware](/images/cumulus-vx/GNS3_Player/1_PlayerFileOpen.png)

![ova](/images/cumulus-vx/GNS3_Player/3_ovas.png)

Change the name of the new VM to ***CumulusVX-leaf1***, and Click **Import** to import the Cumulus VX VM into Workstation Player.

![importOVA](/images/cumulus-vx/GNS3_Player/4_import_ova.png)

![importOVA](/images/cumulus-vx/GNS3_Player/5_importingTheVM.png)

Configure the Network Adapter settings: Right Click the VM > **Settings** > **Hardware**  
Network Adapter (1): NAT  
Network Adapter(2): Host-only (equivalent to Internal Network)  
Network Adapter(3): Host-only (equivalent to Internal Network)  
Network Adapter(4): Host-only (equivalent to Internal Network)

How to change Interface MAC Address in VMware Workstation Player: Highlight the GNS3 VM > right click > **Settings** > **Hardware** > select a **Network Adapter** > **Advanced** > from there view or change the MAC Address

![macAddy](/images/cumulus-vx/GNS3_Player/macAdd.png)

Create and edit the Network Connections of 3 more VMs named: ***CumulusVX-leaf2***, ***CumulusVX-spine1***, & ***CumulusVX-spine2***.

![theVMs](/images/cumulus-vx/GNS3_Player/theVMs.png)

This demo will show how to configure the Cumulus VX VMs in a Two-Leaf, Two-Spine Topology.

![2leaf2spine](/images/cumulus-vx/GNS3_Player/6_spineleafTopology.png)

#### 4.  Download & Install GNS3
>This demo will be based on GNS3 v2.2.6 & VMware Workstation Player 14.

Go to GNS3’s GitHub, download and install [v2.2.6](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.6) named **GNS3-2.2.6-all-in-one.exe**. 

![v226Download](/images/cumulus-vx/GNS3_Player/01_v226download.png)

During installation use all the default settings, for simplicity of this installation. (GNS3 will install several other programs).

![Download GNS3](/images/cumulus-vx/GNS3_regular/1_gns3Download_chooseComponents.png)

After installation, open GNS3 & hit **Cancel** on the Setup Wizard.

![setupWizard](/images/cumulus-vx/GNS3_regular/2_gns3Download_hitCancel.png)

On the right side panel under Servers Summary, the green button means successful download of the GNS3 GUI; the local GNS3 server is running. If there’s no green button, it may help to restart your machine and restart GNS3. (If still no luck, check your antivirus and your firewall.) 

![serverSummary](/images/cumulus-vx/GNS3_regular/1_server_summary.png)

#### 5.Run your virtual network in GNS3

Start GNS3.  
**Edit** > **Preferences** > **VMwareVMs** > **New** > select Run this VMware VM on my local computer > **Next** > wait for the VMware VM list to populate > select 1 of the 4 previously Cumulus VX VMs imported into VMware > **Finish**

![vmwareVM](/images/cumulus-vx/GNS3_Player/7_vmwareVM.png)

Repeat for ***CumulusVX-leaf2***, ***Cumulus VX-spine1***, & ***Cumulus VX-spine2***

![4VMs](/images/cumulus-vx/GNS3_Player/8_4templates.png)

Edit the VM templates that were added: in the same Preferences prompt, highlight ***CumulusVX-leaf1*** > **Edit** > **Network** > Adapters: 4 > check the ‘Allow GNS3 to use any configured VMware adapter’ box > **OK**

Repeat these Edit Preferences steps for ***CumulusVX-leaf2***, ***Cumulus VX-spine1***, & ***Cumulus VX-spine2***

![templates](/images/cumulus-vx/GNS3_Player/9_templates.png)

#### 6. Configuring & Using Cumulus VX in GNS3!

In GNS3, click Browse End Devices icon, and the imported Cumulus VX appliances should appear.

![BrowseDevices](/images/cumulus-vx/GNS3_regular/14_useTheAppliance.png)

{{%notice note%}}

If this is the reader’s first time using GNS3, it’s recommended to read the [“Your First GNS3 Topology”](https://docs.gns3.com/1wr2j2jEfX6ihyzpXzC23wQ8ymHzID4K3Hn99-qqshfg/index.html) doc on GNS3’s site.

{{%/notice%}} 

Here’s a Two-Leaf, Two-Spine Topology:

![GNS3topology](/images/cumulus-vx/GNS3_Player/topologyinGNS3.png)

Connect the devices, start the nodes, & open the consoles.

> e1 in GNS3 corresponds to spw1 in Cumulus VX, e2 to swp2, and so on.

{{%notice note%}}

A note about the VMware Player VMs: when you click inside the VM, the VM will “take control” of your mouse and you cannot use/see the mouse anymore. To be able to use/see your mouse again, hit the **[Ctrl+Alt]**.

{{%/notice%}}

Hit **Enter** so the VM will “take control” of your mouse and you can login.

![loggedIn](/images/cumulus-vx/GNS3_Player/10_loggedIn.png)

>***Username: cumulus  
Password: CumulusLinux!***

{{%notice note%}}

- Head over to [Two-Leaf, Two-Spine Topology](https://docs.cumulusnetworks.com/cumulus-vx/Create-a-Two-Leaf-Two-Spine-Topology/) to configure the network interfaces and routing.

{{%/notice%}}

You can also drag & drop virtual PCs (VPCS) and connect them to the Cumulus VX VMs.  
1) Add the VPCS  
2) Start the VPCS, start the Console  
3) Configure the IP address & default gateway  

![VPCSConfigure](/images/cumulus-vx/GNS3_VirtualBox/21_VPCS.png)

4) Start all the VMs
5) After configuration of the VMs and VPCs, you should be able to ping between the VMs & the VPCS  

![VPCS&VMs](/images/cumulus-vx/GNS3_VirtualBox/22_vpcsAndVM.png)


