---
title: GNS3 and VirtualBox
author: Cumulus Networks
weight: 63
aliases:
 - /display/VX/GNS3-and-VirtualBox
  - /display/VX/GNS3+and+VirtualBox
 - /pages/viewpage.action?pageId=5126714
pageID: 5126714
---

```
~Note~
There are 2 ways to use GNS3 with VirtualBox:
Option 1: Nested Virtualization of GNS3 VM within VirtualBox
Option 2: Running Locally within GNS3 (no nested virtualization)
```


# **Nested Virtualization of GNS3 VM within VirtualBox**


1.  Download & Install GNS3

Go to the [GNS3 site](https://www.gns3.com/) and click Free Download. Sign up or LogIn to your account. Run the .exe, during installation use all the default settings, for simplicity of this download. (GNS3 will download several other programs)
![Download GNS3](/images/cumulus-vx/GNS3_regular/1_gns3Download_chooseComponents.png)
>This demo was done on a Windows 10 device. If your machine isn't Windows, GNS3’s site has Windows, MacOSX, & Linux [installation instructions](https://docs.gns3.com).

After installation, open GNS3 & hit **Cancel** on the Setup Wizard. 
~~pic1~~

On the right side panel under Servers Summary, the green button means successful download of the GNS3 GUI; the local GNS3 server is running. If there’s no green button, it may help to restart your machine and restart GNS3. (If still no luck, check your antivirus and your firewall.)
~~pic2~~

2.  Download & Install the GNS3 VM (OVA file) for Virtualbox    

The GNS3 VM will run within VirtualBox (Type 2 Hypervisor) for nested virtualization. Download & Install the GNS3 VM [zip file](https://www.gns3.com/software/download-vm). The GNS3 GUI and the GNS3 VM must be using the same version.
~~pic3~~

3. Download & Install VirtualBox

[VirtualBox](https://www.virtualbox.org/)

4. Import the GNS3 VM into VirtualBox

Extract the files from the GNS3.VM.VMware download from earlier, which contains the OVA file. Open VirtualBox, click **File** > **Import Appliance** > **Next**. Select the GNS3 VM OVA file that was downloaded earlier. Leave everything at default and Click Import to import the GNS3 VM into VirtualBox.

~~pic4~~

5. So far GNS3 GUI, a type-2 hypervisor (VirtualBox), and GNS3 VM have been downloaded. Now to integrate the GNS3 GUI with the GNS3 VM.

>In the past, VirtualBox nested virtualization was only allowed with an AMD processor. As of late 2019, VirtualBox nested virtualization is allowed with both AMD & Intel processors!

Open GNS3. New Project prompt will appear; name it whatever you’d like. Now we need to integrate the GNS3 GUI with the GNS3 VM. Go to Edit > Preferences > GNS3 VM. Click the Enable the GNS3 VM box. In the Virtualization engine section, select VirtualBox. In the Settings select GNS3 VM. Change the vCPUs and RAM fields if desired. Click Apply, then OK.

~~pic5~~

Now GNS3 will connect with VirtualBox and the GNS3 VM will be started within VirtualBox! The GNS3 VM will automatically start booting up with in VirtualBox.

~~pics6&7~~

6. **Possible Errors:**
    
If there’s no success in getting Virtualbox and GNS3 to communicate, you may get several errors including: Ethernet Adapter, eth0, & DHCP. Pay close attention to the error messages.
- If the error mentions “VirtualBox Host-Only Ethernet Adapter #2”, go to VirtualBox and make sure the Adapter for your GNS3 VM also says ‘VirtualBox Host-Only Ethernet Adapter #2’ under the Network section. If not, click on it and make the changes. 

~~pic8~~
Close and re-Open GNS3. Go through the same GNS3 VM Preferences settings to get GNS3 to communicate with VirtualBox, and hopefully there are no more errors.

-   If the error mentions eth0 or DHCP, you have to Start the VM within VirtualBox and make changes to the network settings. Open VirtualBox, select the GNS3 VM, click Start to start the VM. On the screen mentioning eth0 (like below), hit Enter for OK. Your mouse MUST be within the grey/gray message box for the VM to respond to your keyboard clicks.

~~pic9~~

We need to change the Network settings. While the mouse is within the grey/gray area, use your keyboard to scroll down and Highlight Network, hit Enter.

~~pic10~~

“The server will reboot at the end of the process. Continue?”

Yes.

~~pic11~~

A yaml file appears. It shows network interface configuration, and the lines are commented. Delete the pound symbols (#) to uncomment the lines to enable eth0 and allow DHCP. Hit **[Ctrl+O]** to save the file > Hit **Enter** to save the name > Hit **[Ctrl-X]** to exit the configuration file.

~~pic12~~

Close the VM & Start it again. If “True” is not shown for “KVM support available”, the VM settings in VirtualBox need to be changed to enable Virtualization.

~~pic13~~

Close the window, in VirtualBox, highlight the GNS3 VM, select **Settings** icon > **System** > **Processor** > click the Enable Nested VT-x/AMD-V > **OK**

~~pic14~~

>If by chance you still cannot get GNS3, GNS3 VM, and VirtualBox to work together,, try [version 2.2.3](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.3) of GNS3 & GNS3 VM with VirtualBox v6.1.  
      
    

~~pic15~~

_Hopefully_ there will be no more errors. Close and re-Open both VirtualBox and GNS3.

Try again integrating the GNS3 GUI with the GNS3 VM: Go to **Edit** > **Preferences** > **GNS3 VM**. Click the Enable the GNS3 VM box. In the Virtualization engine section, select VirtualBox. In the Settings select GNS3 VM. Change the vCPUs and RAM fields if desired. Click **Apply**, then **OK**.

~~pic16~~

With the errors gone, GNS3 should be able to communicate with VirtualBox and GNS3 VM running within VirtualBox.

~~pic17~~

7. Download & Install Cumulus VX Appliance from GNS3

Go to GNS3 site, click Marketplace, and Search for Cumulus VX Appliances or just click [here](https://gns3.com/marketplace/appliance/cumulus-vx).

~~pic18~~

8. Download & Install Cumulus VX

Open GNS3, **File** > **Import Appliance** > select the downloaded Cumulus VS appliance > **OK**.

Select the default settings for the next from prompts until reaching the “Required files” prompt.

~~pic19~~

A list of Cumulus VX versions and files will be shown. Version 3.7.6 will be used in this demo..

Navigate to the Cumulus VX download page [here](https://cumulusnetworks.com/products/cumulus-vx/download/). Select the appropriate version, and download that .qcow2 file.

~~pic20&21~~

This download should take a few minutes.

Back to the appliance installation in GNS3, click Import and import the .qcow2 download. The Status should go from “Missing files” to “Ready to Install”. Highlight the file, click Next, & click Yes to begin the install.

~~pic22,23,24~

***Take note of the username and password*** & click **Finish**.

~~pic25~~

9. So far, the nested virtualization of GNS3 VM into Workstation Player to be used with the GNS3 GUI is complete, and a Cumulus VX appliance has been imported into GNS3. Next task, configuring Cumulus VX!!
 
 In GNS3, click Browse Switches icon, and the imported Cumulus VX virtual machine should appear.

~~pic26~~

-   If this is the reader’s first time using GNS3, it’s recommended to read the [“Your First GNS3 Topology”](https://docs.gns3.com/1wr2j2jEfX6ihyzpXzC23wQ8ymHzID4K3Hn99-qqshfg/index.html) doc on GNS3’s site.
    

Here’s a simple topology. Let’s configure the devices so the end hosts can ping each other.

~~pic27~~

-   To download the UbuntuDockerGuest appliance: GNS3 site > Marketplace > Appliances > Ubuntu Docker Guest > Download  
    To Import the appliance into GNS3: [https://docs.gns3.com/1_3RdgLWgfk4ylRr99htYZrGMoFlJcmKAAaUAc8x9Ph8/index.html](https://docs.gns3.com/1_3RdgLWgfk4ylRr99htYZrGMoFlJcmKAAaUAc8x9Ph8/index.html) 
    
-   This demo uses UbuntuDockerGuest as the host; the VPCS host in GNS3 can be used also….. End hosts are NOT needed to configure the Cumulus devices
    
How to change Interface MAC Address in VirtualBox: Highlight the GNS3 VM > **Settings** > **Network**> select a **Network Adapter** > **Advanced** > from there view or change the MAC Address > **OK** 

~~pic28~~

Start all the nodes, and open all the consoles.  

>The console sessions should open up using Solar-PuTTY (during download of GNS3, if you OK’ed all the default settings, Solar-PuTTY was downloaded also). The console sessions for the Cumulus devices take a few moments.

Right click on a UbuntuGuest, select Edit config, and change the network values of the interface. Do this to both hosts.

~~pic29~~

On the Ubuntu machines, run `ifconfig` to verify your new network changes.

For the Cumulus devices: Remember the password and username from earlier? Use those to login.

>***Username: cumulus  
Password: CumulusLinux!***

Take note that `whoami` shows the username of the Cumulus devices is cumulus; `sudo` will be needed to run privileged commands in the Cumulus devices.

~~pic30~~

Run `ifconfig` to show there are no network settings yet. Running `cat /etc/networks/interfaces` shows that eth0 is configured using DHCP; also eth0 is the management port.

Let’s add a Switch and a NAT cloud to the topology so the Cumulus devices can receive an ip address on eth0 via DHCP.

~~pic31~~

Run `ifconfig` & there’s now an ip address assigned to eth0.

~~pic32~~

The rest of this demo will be following the Configure Switch Ports steps from the [Cumulus Linux v3.7 ‘Quick Start Guide’](https://docs.cumulusnetworks.com/cumulus-linux-37/Quick-Start-Guide/) to configure swp1 and swp2.  
  
  

Edit the /etc/network/interfaces file; remember to use `sudo` in order to edit the network interfaces.

`auto swp1`  
`iface swp1`  
`auto swp2`  
`iface swp2`

~~pic33~~
   
  Save the file, exit the file, reload the configuration using `sudo ifreload -a`, run `ifconfig`. You should now see the addition of swp1 and swp2 interfaces.

~~pic34~~

Let’s add swp1 and swp2 to a bridge, reload the configuration, view the bridge settings, & display the bridge interface.
`auto bridge`
`iface bridge`
`bridge-ports swp1 swp2`
`bridge-vlan-aware yes`
Exit the file.
`sudo ifreload -a`
`brctl show`
`ifconfig`

~~pic35~~
  
Now the Ubuntu machines can Ping each other!

~~pic36~~
  
>In this demo, you:
>-   Downloaded GNS3, GNS3 VM, and a Type-2 hypervisor VirtualBox
>-   Configured nested virtualization between GNS3 VM and VirtualBox to be used within GNS3
>-   Imported a Cumulus VX virtual machine within GNS3
>- Configured the Cumulus VX virtual machine: 2 switch ports & a bridge in order to for two hosts to ping each other



# **Running Locally within GNS3 (no nested virtualization)**


