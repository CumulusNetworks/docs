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

Go to GNS3’s GitHub, download and install [v2.2.6](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.6) named GNS3-2.2.6-all-in-one.exe. During installation use all the default settings, for simplicity of this installation. (GNS3 will install several other programs).**

~~pic1,2~~

After installation, open GNS3 & hit **Cancel** on the Setup Wizard.

~~pic3~~

On the right side panel under Servers Summary, the green button means successful download of the GNS3 GUI; the local GNS3 server is running. If there’s no green button, it may help to restart your machine and restart GNS3. (If still no luck, check your antivirus and your firewall.) 

~~pic4~~

#### 2. Download & Install the GNS3 VM (OVA file) for VMware
The GNS3 VM will run within VMware Workstaion Player (Type 2 Hypervisor) for nested virtualization. From GNS3's GitHub page, Download & Install the GNS3 VM [zip file](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.6) named **GNS3.VM.Wmware.workstation2.2.6.zip**. The GNS3 GUI and the GNS3 VM must be using the same version. 

~~pic5~~

#### 3. Download & Install VMware Workstation Player 14
There are many versions of GNS3 and Workstation Player. From a lot of trial and error, the combination of versions that work together are: GNS3 v2.2.6 & VMware Player 14.  
Download & Install [VMware Workstation Player 14](https://my.vmware.com/en/web/vmware/free#desktop_end_user_computing/vmware_workstation_player/14_0|PLAYER-1418|product_downloads).

~~pic6~~

#### 4. Integrate GNS3 VM & VMware Player for nested virtualization

Extract the files from the GNS3.VM.VMware zip download from earlier, which contains the OVA file. Open Workstation Player, click **Player** > **File** > **Open** to open up a virtual machine. Select the GNS3 VM OVA file. Leave everything at default, and Click **Import** to import the GNS3 VM into Workstation Player.

~~pic7,8~~

 #### 5. Integrate the GNS3 GUI with the GNS3 VM. 

So far GNS3 GUI, a type-2 hypervisor (VMware), and GNS3 VM have been downloaded. Now to integrate the GNS3 GUI with the GNS3 VM.
Open GNS3. The Setup Wizard will appear. Select **Run modern IOS…**, then click **Next** on the next few prompts. 

~~pic9~~

After selecting **Next** a few times, this prompt may appear; follow it’s directions.

~~pic10~~

Go to [https://www.vmware.com/support/developer/vix-api/](https://www.vmware.com/support/developer/vix-api/) like instructed, click on **SDK 1.15**,

~~pic11~~

and select the appropriate VIX software download for your machine.

~~pic12~~

In the meantime, close GNS3 again. After the installation of the VIX download is finished, once again open up GNS3. New Project prompt will appear; name it whatever you’d like. Now we need to integrate the GNS3 GUI with the GNS3 VM. Go to **Edit** > **Preferences** > **GNS3 VM**. Click the Enable the GNS3 VM box. In the Virtualization engine section, select VMware Workstation / Player. In the Settings section, Refresh the VM name and select GNS3 VM. Click **Apply**, then **OK**.

~~pic13~~

Go back to the Setup Wizard (**Help** > **Setup Wizard**) select **Run modern IOS…**, then click **Next** on the Next few prompts... Now the warning message from earlier should not reappear, and the GNS3 VM setup should appear! Select VMware as the virtualization software, and GNS3 VM as your VM name. If desired, keep the default settings, and click **Next**.

~~pic14~~

Servers Summary on the right-hand side should display your GNS3 VM.

~~pic15~~

VMware Player should automatically start. 

~~pic16~~

Now that everything is integrated and acting right, choose **Take Ownership** then **OK** to start the Player.

~~pic17~~

If this warning appears, shut down your machine and make the necessary changes.

~~pic17~~

Startup your machine again, open up GNS3 again, if the prompt about Virtualized Intel VT-x/EPT appears, just choose Yes.

~~pic18~~

“Disable KVM and get lower performances?” Select No

>Your mouse has to be within WMware Player window in order to select anything; if the mouse is outside the VMware Player window, there will be no response.

~~pic19~~

Based on your machine and OS, you may have to update the BIOS or chose specific Virtual Machine Settings within VMware Workstation Player: highlight the VM > right click > **Settings** > **Hardware** > **Processors** > under the Virtualization engine section, check the Virtualize Intel VT -x/EPT or AMD-V/RVI box.

~~pic20~~

At this point, the nested virtualization of GNS3 VM into Workstation Player to be used with the GNS3 GUI is complete. Next step is to incorporate Cumulus VX in GNS3. Close GNS3.

~~pic21~~

#### 6. Download & Install the Cumulus VX Appliance from the GNS3 site

Go to GNS3 site, click Marketplace, and Search for Cumulus VX Appliances or click [here](https://gns3.com/marketplace/appliance/cumulus-vx).

~~pic22~~

#### 7. Download & Install Cumulus VX Appliance from GNS3 site 
Go to GNS3 site, click Marketplace, and Search for Cumulus VX Appliances or just click [here](https://gns3.com/marketplace/appliance/cumulus-vx).

~~pic23~~

#### 8. Download & Install Cumulus VX 
Open GNS3, **File** > **Import Appliance** > select the downloaded Cumulus VS appliance > **OK**. Select the default settings for the next few prompts until reaching the “Required files” prompt. 

~~pic24~~

A list of Cumulus VX versions and files will be shown. (Version 3.7.6 will be used in this demo) Navigate to the Cumulus VX download page [here](https://cumulusnetworks.com/products/cumulus-vx/download/). Select the appropriate version, and download that **.qcow2 file**. This download should take a few minutes.

~~pic25,26~~

Back to the appliance installation in GNS3, click **Import** and import the .qcow2 download. The Status should go from “Missing files” to “Ready to Install”. Highlight the file, click **Next**, & click **Yes** to begin the install.

~~pic27,28~~

 >Take note of the username and password*** & click **Finish**. 
 ~~pic 29~~
 
 #### 9. Configuring Cumulus VX virtual machine!! So far, the nested virtualization of GNS3 VM into Workstation Player to be used with the GNS3 GUI is complete, and a Cumulus VX appliance has been imported into GNS3. In GNS3, click **Browse Switches** icon, and the imported Cumulus VX virtual machine should appear. 
 
~~pic30~~

{{%notice note%}} 
If this is the reader’s first time using GNS3, it’s recommended to read the [“Your First GNS3 Topology”](https://docs.gns3.com/1wr2j2jEfX6ihyzpXzC23wQ8ymHzID4K3Hn99-qqshfg/index.html) doc on GNS3’s site. 
{{%/notice%}} 

Here’s a simple topology. Let’s configure the devices so the end hosts can ping each other.

~~pic31~~

- To download the UbuntuDockerGuest appliance: GNS3 site > Marketplace > Appliances > Ubuntu Docker Guest > Download To Import the appliance into GNS3: [https://docs.gns3.com/1_3RdgLWgfk4ylRr99htYZrGMoFlJcmKAAaUAc8x9Ph8/index.html](https://docs.gns3.com/1_3RdgLWgfk4ylRr99htYZrGMoFlJcmKAAaUAc8x9Ph8/index.html) - This demo uses UbuntuDockerGuest as the host; the VPCS host in GNS3 can be used also….. End hosts are NOT needed to configure the Cumulus devices.

How to change Interface MAC Address in VMware Workstaton Player: Highlight the GNS3 VM > **Settings** > **Network**> select a **Network Adapter** > **Advanced** > from there view or change the MAC Address > **OK**

~~pic24~~

Start all the nodes, and open all the consoles. 
>The console sessions should open up using Solar-PuTTY (during download of GNS3, if you OK’ed all the default settings, Solar-PuTTY was downloaded also). The console sessions for the Cumulus devices take a few moments. 

Right click on a UbuntuGuest, select **Edit config**, and change the network values of the interface. Do this to both hosts. 

~~pic25~~


On the Ubuntu machines, run `ifconfig` to verify your new network changes. For the Cumulus devices: Remember the password and username from earlier? Use those to login. 
>***Username: cumulus Password: CumulusLinux!*** 

Take note that `whoami` shows the username of the Cumulus devices is cumulus; `sudo` will be needed to run privileged commands in the Cumulus devices. 

~~pic26~~

Run `ifconfig` to show there are no network settings yet. Running `cat /etc/networks/interfaces` shows that eth0 is configured using DHCP; also eth0 is the management port. 
Let’s add a Switch and a NAT cloud to the topology so the Cumulus devices can receive an ip address on eth0 via DHCP.

~~pic27~~ 

Run `ifconfig` & there’s now an ip address assigned to eth0. 

{{%notice note%}} 
The rest of this demo will be following the Configure Switch Ports steps from the [Cumulus Linux v3.7 ‘Quick Start Guide’](https://docs.cumulusnetworks.com/cumulus-linux-37/Quick-Start-Guide/) to configure swp1 and swp2. 
{{%/notice%}} 

Edit the /etc/network/interfaces file; remember to use `sudo` in order to edit the network interfaces. 
`auto swp1`
`iface swp1`
`auto swp2`
`iface swp2`

 ~~pic28~~

Save the file, exit the file, reload the configuration using `sudo ifreload -a`, run `ifconfig`. You should now see the addition of swp1 and swp2 interfaces. 

~~pic29~~

Let’s add swp1 and swp2 to a bridge, reload the configuration, view the bridge settings, & display the bridge interface. 
`auto bridge`
`iface bridge`
`bridge-ports swp1 swp2`
`bridge-vlan-aware yes`
Exit the file.
`sudo ifreload -a`
`brctl show`

~~pic 29~~

The Cumulus VX devices have been properly configured, and now the Ubuntu machines can Ping each other!

~~pic30~~

>In this demo, you: 
>- Downloaded GNS3, GNS3 VM, and a Type-2 hypervisor VMvware Workstation Player
>- Configured nested virtualization between GNS3 VM and VMware Player to be used within GNS3
>- Imported a Cumulus VX virtual machine within GNS3
>- Configured the Cumulus VX virtual machine: 2 switch ports & a bridge in order to for two hosts to ping each other

