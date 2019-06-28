---
title: Installing a New Cumulus Linux Image
author: Cumulus Networks
weight: 43
aliases:
 - /display/CL332/Installing+a+New+Cumulus+Linux+Image
 - /pages/viewpage.action?pageId=5868958
pageID: 5868958
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
---
Before you install Cumulus Linux, the switch can be in two different
states:

  - The switch has no image on it (so the switch is only running
    [ONIE](http://www.onie.org/)) or you desire or require a clean
    installation. In this case, you can install Cumulus Linux in one of
    the following ways, using:
    
      - [DHCP/a web server with DHCP
        options](#src-5868958_InstallingaNewCumulusLinuxImage-dhcp_options)
    
      - [DHCP/a web server without DHCP
        options](#src-5868958_InstallingaNewCumulusLinuxImage-dhcp_noopts)
    
      - [A web server with no
        DHCP](#src-5868958_InstallingaNewCumulusLinuxImage-web_nodhcp)
    
      - [FTP or TFTP without a web
        server](#src-5868958_InstallingaNewCumulusLinuxImage-ftp)
    
      - [Local file
        installation](#src-5868958_InstallingaNewCumulusLinuxImage-local)
    
      - [USB](#src-5868958_InstallingaNewCumulusLinuxImage-usb)

  - The switch already has Cumulus Linux installed on it, so you only
    need to [upgrade
    it](/version/cumulus-linux-332/Installation_Management/Upgrading_Cumulus_Linux).

{{%notice tip%}}

[ONIE](http://www.onie.org/) is an open source project, equivalent to
PXE on servers, that enables the installation of network operating
systems (NOS) on bare metal switches.

{{%/notice%}}

## <span>Understanding these Examples</span>

The sections in this chapter are ordered from the most repeatable to the
least repeatable methods. For instance, DHCP can scale to hundreds of
switch installs with zero manual input, compared to something like USB
installs. Installing via USB is fine for a single switch here and there
but is not scalable.

  - You can name your Cumulus Linux installer binary using any of the
    [ONIE naming schemes mentioned
    here](http://opencomputeproject.github.io/onie/design-spec/discovery.html#default-file-name-search-order).

  - In the examples below, \[PLATFORM\] can be any supported Cumulus
    Linux platform, such as *x86\_64*, or *arm*.

## <span id="src-5868958_InstallingaNewCumulusLinuxImage-dhcp_options" class="confluence-anchor-link"></span><span>Installing via a DHCP/Web Server Method with DHCP Options</span>

Installing Cumulus Linux in this manner is as simple as setting up a
DHCP/web server on your laptop and connecting the eth0 management port
of the switch to your laptop.

Once you connect the cable, the installation proceeds as follows:

1.  The bare metal switch boots up and asks for an address (DHCP
    request).

2.  The DHCP server acknowledges and responds with DHCP option 114 and
    the location of the installation image.

3.  ONIE downloads the Cumulus Linux binary, installs and reboots.

4.  Success\! You are now running Cumulus Linux.
    
    {{% imgOld 0 %}}

{{%notice note%}}

The most common method is for you to send DHCP option 114 with the
entire URL to the web server (this could be the same system). However,
there are many other ways to use DHCP even if you don't have full
control over DHCP. [See the ONIE user
guide](https://opencomputeproject.github.io/onie/design-spec/discovery.html#partial-installer-urls)
for help.

{{%/notice%}}

Here's an example DHCP configuration with an [ISC DHCP
server](http://www.isc.org/downloads/dhcp/):

    subnet 172.0.24.0 netmask 255.255.255.0 {
      range 172.0.24.20 172.0.24.200;
      option default-url = "http://172.0.24.14/onie-installer-[PLATFORM]";
    }

Here's an example DHCP configuration with
[dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) (static address
assignment):

    dhcp-host=sw4,192.168.100.14,6c:64:1a:00:03:ba,set:sw4
    dhcp-option=tag:sw4,114,"http://roz.rtplab.test/onie-installer-[PLATFORM]"

If you don't have a web server, you can use [this free Apache
example](https://www.apachefriends.org/index.html).

## <span id="src-5868958_InstallingaNewCumulusLinuxImage-dhcp_noopts" class="confluence-anchor-link"></span><span> Installing via a DHCP/Web Server Method without DHCP Options</span>

If you have a laptop on the same network and the switch can pull DHCP
from the corporate network, but you cannot modify DHCP options (maybe
it's controlled by another team), do the following:

1.  Place the Cumulus Linux binary in a directory on the web server.

2.  Run the installer manually, since DHCP options can't be modified,
    either from ONIE or the Cumulus Linux command prompt.
    
      - From ONIE, run the `onie-nos-install` command:
        
            ONIE:/ #onie-nos-install http://10.0.1.251/path/to/cumulus-install-[PLATFORM].bin
    
      - From Cumulus Linux, run the `onie-install` command:
        
            cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/path/to/cumulus-install-[PLATFORM].bin && sudo reboot

## <span id="src-5868958_InstallingaNewCumulusLinuxImage-web_nodhcp" class="confluence-anchor-link"></span><span>Installing via a Web Server with no DHCP</span>

If your laptop is on the same network as the switch eth0 interface but
no DHCP server is available, you can still install directly from Cumulus
Linux or using ONIE.

### <span>Installing from Cumulus Linux</span>

From Cumulus Linux, run the `onie-install` command:

    cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/path/to/cumulus-install-[PLATFORM].bin && sudo reboot

### <span>Installing from ONIE</span>

Do the following steps to run the install using ONIE. Note that ONIE is
in [*discovery
mode*](http://opencomputeproject.github.io/onie/design-spec/discovery.html#installer-discovery-methods):

1.  To disable discovery mode, run:
    
        onie# onie-discovery-stop
    
    or, on older ONIE versions if that command isn't supported:
    
        onie# /etc/init.d/discover.sh stop

2.  Assign a static address to eth0 via ONIE (using `ip addr add`):
    
        ONIE:/ #ip addr add 10.0.1.252/24 dev eth0

3.  Place the Cumulus Linux installer image in a directory on your web
    server.

4.  Run the installer manually, since there are no DHCP options:
    
        ONIE:/ #onie-nos-install http://10.0.1.251/path/to/cumulus-install-[PLATFORM].bin

## <span id="src-5868958_InstallingaNewCumulusLinuxImage-ftp" class="confluence-anchor-link"></span><span> Installing via FTP or TFTP without a Web Server</span>

If your laptop is on the same network as the switch eth0 interface but
no DHCP server is available, you can still install directly from Cumulus
Linux or using ONIE.

### <span>Installing from Cumulus Linux</span>

If you are not utilizing DHCP options, run one of the following commands
(`tftp` for TFTP or `ftp` for FTP), from the Cumulus Linux command
prompt:

    cumulus@switch:~$ sudo onie-install -a -i ftp://local-ftp-server/cumulus-install-[PLATFORM].bin && sudo reboot
     
    cumulus@switch:~$ sudo onie-install -a -i tftp://local-tftp-server/cumulus-install-[PLATFORM].bin && sudo reboot

### <span>Installing from ONIE</span>

To install without DHCP options using ONIE, do the following:

1.  Set up DHCP or static addressing for eth0, as in the examples above.

2.  If you are utilizing static addressing, disable ONIE discovery mode.

3.  Place the Cumulus Linux installer image into a TFTP or FTP
    directory.

4.  If you are not utilizing DHCP options, run one of the following
    commands (`tftp` for TFTP or `ftp` for FTP):
    
        ONIE# onie-nos-install ftp://local-ftp-server/cumulus-install-[PLATFORM].bin
         
        ONIE# onie-nos-install tftp://local-tftp-server/cumulus-install-[PLATFORM].bin

## <span id="src-5868958_InstallingaNewCumulusLinuxImage-local" class="confluence-anchor-link"></span><span> Installing via a Local File</span>

You can still install referencing a local file, directly from Cumulus
Linux or using ONIE.

### <span>Installing from Cumulus Linux</span>

From Cumulus Linux, run the `onie-install` command:

    cumulus@switch:~$ sudo onie-install -a -i /path/to/local/file/cumulus-install-[PLATFORM].bin && sudo reboot

### <span>Installing from ONIE</span>

1.  Set up DHCP or static addressing for eth0, as in the examples above.

2.  If you are utilizing static addressing, disable ONIE discovery mode.

3.  Use [scp](http://en.wikipedia.org/wiki/Secure_copy) to copy the
    Cumulus Linux binary to the switch.
    
    {{%notice tip%}}
    
    Windows users can use [WinScp](http://winscp.net/eng/index.php).
    
    {{%/notice%}}

4.  Run the installer manually from ONIE:
    
        ONIE:/ #onie-nos-install /path/to/local/file/cumulus-install-[PLATFORM].bin

## <span id="src-5868958_InstallingaNewCumulusLinuxImage-usb" class="confluence-anchor-link"></span><span>Installing via USB</span>

Following the steps below produces a clean installation of Cumulus
Linux. This wipes out all pre-existing configuration files that may be
present on the switch. Instructions are offered for x86 and ARM
platforms, and also cover the installation of a license after the
software installation.

{{%notice note%}}

Make sure to [back
up](/version/cumulus-linux-332/Installation_Management/Upgrading_Cumulus_Linux)
any important configuration files that you may need to restore the
configuration of your switch after the installation finishes.

{{%/notice%}}

### <span>Preparing for USB Installation</span>

1.  Download the appropriate Cumulus Linux image for your x86 or ARM
    platform from the [Cumulus Networks Downloads
    page](http://cumulusnetworks.com/downloads/).

2.  Prepare your flash drive by formatting in one of the supported
    formats: FAT32, vFAT or EXT2.
    
    Optional: Preparing a USB Drive inside Cumulus Linux
    
    <table>
    <colgroup>
    <col style="width: 100%" />
    </colgroup>
    <tbody>
    <tr class="odd">
    <td><p>{{%notice warning%}}</p>
    <p>It is possible that you could severely damage your system with the following utilities, so please use caution when performing the actions below!</p>
    <p>{{%/notice%}}</p>
    <ol>
    <li><p>Insert your flash drive into the USB port on the switch running Cumulus Linux and log in to the switch.</p></li>
    <li><p>Determine and note at which device your flash drive can be found by using output from <code>cat /proc/partitions</code> and <code>sudo fdisk -l [device]</code>. For example, <code>sudo fdisk -l /dev/sdb</code>.</p>
    <p>{{%notice warning%}}</p>
    <p>These instructions assume your USB drive is the <code>/dev/sdb</code> device, which is typical if the USB stick was inserted after the machine was already booted. However, if the USB stick was plugged in during the boot process, it is possible the device could be <code>/dev/sda</code>. Make sure to modify the commands below to use the proper device for your USB drive!</p>
    <p>{{%/notice%}}</p></li>
    <li><p>Create a new partition table on the device:</p>
    <pre><code>sudo parted /dev/sdb mklabel msdos</code></pre>
    <p>{{%notice note%}}</p>
    <p>The <code>parted</code> utility should already be installed. However, if it is not, install it with: <code>sudo -E apt-get install parted</code></p>
    <p>{{%/notice%}}</p></li>
    <li><p>Create a new partition on the device:</p>
    <pre><code>sudo parted /dev/sdb -a optimal mkpart primary 0% 100%</code></pre></li>
    <li><p>Format the partition to your filesystem of choice using ONE of the examples below:</p>
    <pre><code>sudo mkfs.ext2 /dev/sdb1
    sudo mkfs.msdos -F 32 /dev/sdb1
    sudo mkfs.vfat /dev/sdb1</code></pre>
    <p>{{%notice note%}}</p>
    <p>To use <code>mkfs.msdos</code> or <code>mkfs.vfat</code>, you need to install the <code>dosfstools</code> package from the <a href="http://docs.cumulusnetworks.com/display/CL332/Adding+and+Updating+Packages#AddingandUpdatingPackages-AddingPackagesfromAnotherRepository" class="external-link">Debian software repositories</a> (step 3 here shows you how to add repositories from Debian), as they are not included by default.</p>
    <p>{{%/notice%}}</p></li>
    <li><p>To continue installing Cumulus Linux, mount the USB drive in order to move files to it.</p>
    <pre><code>sudo mkdir /mnt/usb
    sudo mount /dev/sdb1 /mnt/usb</code></pre></li>
    </ol></td>
    </tr>
    </tbody>
    </table>

3.  Copy the image and license files over to the flash drive and rename
    the image file to:
    
      - `onie-installer-x86_64`, if installing on an x86 platform
    
      - `onie-installer-arm`, if installing on an ARM platform
    
    {{%notice note%}}
    
    You can also use any of the [ONIE naming schemes mentioned
    here](http://opencomputeproject.github.io/onie/design-spec/discovery.html#default-file-name-search-order).
    
    {{%/notice%}}
    
    {{%notice warning%}}
    
    When using a Mac or Windows computer to rename the installation file
    the file extension may still be present. Make sure to remove the
    file extension otherwise ONIE will not be able to detect the file\!
    
    {{%/notice%}}

4.  Insert the USB stick into the switch, then continue with the
    appropriate instructions below for your x86 or ARM platform.

### <span>Instructions for x86 Platforms</span>

Click to expand x86 instructions...

1.  Prepare the switch for installation:
    
      - If the switch is offline, connect to the console and power on
        the switch.
    
      - If the switch is already online in Cumulus Linux, connect to the
        console and reboot the switch into the ONIE environment with the
        `sudo onie-select -i` command, followed by `sudo reboot`. Then
        skip to step 4 below.
    
      - If the switch is already online in ONIE, use the `reboot`
        command.
    
    {{%notice note%}}
    
    SSH sessions to the switch get dropped after this step. To complete
    the remaining instructions, connect to the console of the switch.
    Cumulus Linux switches display their boot process to the console, so
    you need to monitor the console specifically to complete the next
    step.
    
    {{%/notice%}}

2.  Monitor the console and select the ONIE option from the first GRUB
    screen shown below.
    
    {{% imgOld 1 %}}

3.  Cumulus Linux on x86 uses GRUB chainloading to present a second GRUB
    menu specific to the ONIE partition. No action is necessary in this
    menu to select the default option *ONIE: Install OS*.
    
    {{% imgOld 2 %}}

4.  At this point, the USB drive should be automatically recognized and
    mounted. The image file should be located and automatic installation
    of Cumulus Linux should begin. Here is some sample output:
    
        ONIE: OS Install Mode  ...
         
        Version : quanta_common_rangeley-2014.05.05-6919d98-201410171013
        Build  Date: 2014-10-17T10:13+0800
        Info: Mounting kernel filesystems...  done.
        Info: Mounting LABEL=ONIE-BOOT on /mnt/onie-boot  ...
        initializing eth0...
        scsi 6:0:0:0: Direct-Access  SanDisk Cruzer Facet 1.26 PQ: 0 ANSI: 6
        sd 6:0:0:0: [sdb] 31266816 512-byte logical blocks: (16.0 GB/14.9 GiB)
        sd 6:0:0:0: [sdb] Write Protect is off
        sd 6:0:0:0: [sdb] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
        sd 6:0:0:0: [sdb] Attached SCSI disk
         
        <...snip...>
         
        ONIE:  Executing installer: file://dev/sdb1/onie-installer-x86_64
        Verifying image checksum ... OK.
        Preparing image archive ... OK.
        Dumping image info...
        Control File Contents
        =====================
        Description: Cumulus  Linux
        OS-Release:  3.0.0-3b46bef-201509041633-build
        Architecture: amd64
        Date:  Fri, 27 May 2016 17:10:30 -0700
        Installer-Version:  1.2
        Platforms: accton_as5712_54x accton_as6712_32x  mlx_sx1400_i73612 dell_s6000_s1220 dell_s4000_c2338 dell_s3000_c2338  cel_redstone_xp cel_smallstone_xp cel_pebble quanta_panther  quanta_ly8_rangeley quanta_ly6_rangeley quanta_ly9_rangeley  
        Homepage: http://www.cumulusnetworks.com/

5.  After installation completes, the switch automatically reboots into
    the newly installed instance of Cumulus Linux.

6.  Determine and note at which device your flash drive can be found by
    using output from `cat /proc/partitions` and `sudo fdisk -l
    [device]`. For example, `sudo fdisk -l /dev/sdb`.
    
    {{%notice warning%}}
    
    These instructions assume your USB drive is the `/dev/sdb` device,
    which is typical if the USB stick was inserted after the machine was
    already booted. However, if the USB stick was plugged in during the
    boot process, it is possible the device could be `/dev/sda`. Make
    sure to modify the commands below to use the proper device for your
    USB drive\!
    
    {{%/notice%}}

7.  Create a mount point to mount the USB drive to:
    
        sudo mkdir /mnt/mountpoint

8.  Mount the USB drive to the newly created mount point:
    
        sudo mount /dev/sdb1 /mnt/mountpoint

9.  Install your license file with the `cl-license` command:
    
        sudo cl-license -i /mnt/mountpoint/license.txt

10. Check that your license is installed with the `cl-license` command.

11. Reboot the switch to utilize the new license.
    
        sudo reboot

### <span>Instructions for ARM Platforms</span>

Click to expand ARM instructions...

1.  Prepare the switch for installation:
    
      - If the switch is offline, connect to the console and power on
        the switch.
    
      - If the switch is already online in Cumulus Linux, connect to the
        console and reboot the switch into the ONIE environment with the
        `sudo onie-select -i` command, followed by `sudo reboot`. Then
        skip to step 4 below.
    
      - If the switch is already online in ONIE, use the `reboot`
        command.
    
    {{%notice note%}}
    
    SSH sessions to the switch get dropped after this step. To complete
    the remaining instructions, connect to the console of the switch.
    Cumulus Linux switches display their boot process to the console, so
    you need to monitor the console specifically to complete the next
    step.
    
    {{%/notice%}}

2.  Interrupt the normal boot process before the countdown (shown below)
    completes. Press any key to stop the autobooting.
    
        U-Boot 2013.01-00016-gddbf4a9-dirty (Feb 14 2014 - 16:30:46) Accton: 1.4.0.5
         
        CPU0: P2020, Version: 2.1, (0x80e20021)
        Core: E500, Version: 5.1, (0x80211051)
        Clock Configuration:
         CPU0:1200 MHz, CPU1:1200 MHz, 
         CCB:600 MHz,
         DDR:400 MHz (800 MT/s data rate) (Asynchronous), LBC:37.500 MHz
        L1: D-cache 32 kB enabled
         I-cache 32 kB enabled
         
        <...snip…>
         
        USB: USB2513 hub OK
        Hit any key to stop autoboot: 0

3.  A command prompt appears, so you can run commands. Execute the
    following command:
    
        run onie_bootcmd

4.  At this point the USB drive should be automatically recognized and
    mounted. The image file should be located and automatic installation
    of Cumulus Linux should begin. Here is some sample output:
    
        Loading Open Network Install Environment …
        Platform: arm-as4610_54p-r0
        Version : 1.6.1.3
        WARNING: adjusting available memory to 30000000
        ## Booting kernel from Legacy Image at ec040000 …
           Image Name:   as6701_32x.1.6.1.3
           Image Type:   ARM Linux Multi-File Image (gzip compressed)
           Data Size:    4456555 Bytes = 4.3 MiB
           Load Address: 00000000
           Entry Point:  00000000
           Contents:
              Image 0: 3738543 Bytes = 3.6 MiB
              Image 1: 706440 Bytes = 689.9 KiB
              Image 2: 11555 Bytes = 11.3 KiB
           Verifying Checksum ... OK
        ## Loading init Ramdisk from multi component Legacy Image at ec040000 …
        ## Flattened Device Tree from multi component Image at EC040000
           Booting using the fdt at 0xec47d388
           Uncompressing Multi-File Image ... OK
           Loading Ramdisk to 2ff53000, end 2ffff788 ... OK
           Loading Device Tree to 03ffa000, end 03fffd22 ... OK
         
        <...snip...>
         
        ONIE: Starting ONIE Service Discovery
        ONIE: Executing installer: file://dev/sdb1/onie-installer-arm
        Verifying image checksum ... OK.
        Preparing image archive ... OK.
        Dumping image info…
        Control File Contents
        =====================
        Description: Cumulus Linux
        OS-Release: 3.0.0-3b46bef-201509041633-build
        Architecture: arm
        Date: Fri, 27 May 2016 17:08:35 -0700
        Installer-Version: 1.2
        Platforms: accton_as4600_54t, accton_as6701_32x, accton_5652, accton_as5610_52x, dni_6448, dni_7448, dni_c7448n, cel_kennisis, cel_redstone, cel_smallstone, cumulus_p2020, quanta_lb9, quanta_ly2, quanta_ly2r, quanta_ly6_p2020
        Homepage: http://www.cumulusnetworks.com/

5.  After installation completes, the switch automatically reboots into
    the newly installed instance of Cumulus Linux.

6.  Determine and note at which device your flash drive can be found by
    using output from `cat /proc/partitions` and `sudo fdisk -l
    [device]`. For example, `sudo fdisk -l /dev/sdb`.
    
    {{%notice warning%}}
    
    These instructions assume your USB drive is the `/dev/sdb` device,
    which is typical if the USB stick was inserted after the machine was
    already booted. However, if the USB stick was plugged in during the
    boot process, it is possible the device could be `/dev/sda`. Make
    sure to modify the commands below to use the proper device for your
    USB drive\!
    
    {{%/notice%}}

7.  Create a mount point to mount the USB drive to:
    
        sudo mkdir /mnt/mountpoint

8.  Mount the USB drive to the newly created mount point:
    
        sudo mount /dev/sdb1 /mnt/mountpoint

9.  Install your license file with the `cl-license` command:
    
        sudo cl-license -i /mnt/mountpoint/license.txt

10. Check that your license is installed with the `cl-license` command.

11. Reboot the switch to utilize the new license.
    
        sudo reboot

## <span id="src-5868958_InstallingaNewCumulusLinuxImage-alreadyinstalled" class="confluence-anchor-link"></span><span>Installing a New Image when Cumulus Linux Is already Installed</span>

At times it may be necessary to put the switch into ONIE in order to do
an install. This may be required when moving between major releases or
re-installing from an early version of 3.y.z. For more information, see
[Upgrading Cumulus
Linux](Upgrading_Cumulus_Linux.html#src-5868962_UpgradingCumulusLinux-binary_upgrade).

### <span id="src-5868958_InstallingaNewCumulusLinuxImage-oniemode" class="confluence-anchor-link"></span><span>Entering ONIE Mode from Cumulus Linux</span>

If Cumulus Linux is already installed on the switch, you can enter ONIE
mode in one of two ways, using:

  - ONIE Recovery Mode to manually install an image from the ONIE
    prompt:
    
        cumulus@switch:~$ sudo onie-select -r
        cumulus@switch:~$ sudo reboot

  - ONIE Install Mode to attempt to automatically discover the image
    from a DHCP server:
    
        cumulus@switch:~$ sudo onie-select -i
        cumulus@switch:~$ sudo reboot
