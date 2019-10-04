---
title: Installing a New Cumulus Linux Image
author: Cumulus Networks
weight: 201
aliases:
 - /display/CL25ESR/Installing+a+New+Cumulus+Linux+Image
 - /pages/viewpage.action?pageId=5115997
pageID: 5115997
product: Cumulus Linux
version: 2.5 ESR
imgData: cumulus-linux-25esr
siteSlug: cumulus-linux-25esr
---
Before you install Cumulus Linux, the switch can be in two different
states:

  - The switch has no image on it (so the switch is only running
    [ONIE](http://www.onie.org/)) or you desire or require a clean
    installation. In this case, you can install Cumulus Linux in one of
    the following ways, using:
      - [DHCP/a Web server with DHCP options](#installing-via-a-dhcp-web-server-method-with-dhcp-options)
      - [DHCP/a Web server without DHCP options](#installing-via-a-dhcp-web-server-method-without-dhcp-options)
      - [A Web server with no DHCP](#installing-via-a-web-server-with-no-dhcp)
      - [FTP or TFTP without a Web server](#installing-via-ftp-or-tftp-without-a-web-server)
      - [Local file installation](#installing-via-a-local-file)
      - [USB](#installing-via-usb)
  - The switch already has Cumulus Linux installed on it, so you only
    need to [upgrade it](/version/cumulus-linux-25esr/Installation-Upgrading-and-Package-Management/Managing-Cumulus-Linux-Disk-Images/Upgrading-Cumulus-Linux)

{{%notice tip%}}

[ONIE](http://www.onie.org/) is an open source project, equivalent to
PXE on servers, that enables the installation of network operating
systems (NOS) on bare metal switches.

{{%/notice%}}

## Understanding these Examples

  - This sections in this chapter are ordered from the most repeatable
    to the least repeatable methods. For instance, DHCP can scale to
    hundreds of switch installs with zero manual input, compared to
    something like USB installs. Installing via USB is fine for a single
    switch here and there but is not scalable.

  - You can name your Cumulus Linux installer binary using any of the
    [ONIE naming schemes mentioned
    here](http://opencomputeproject.github.io/onie/design-spec/discovery.html#default-file-name-search-order).

  - In the examples below, \[PLATFORM\] can be any supported Cumulus
    Linux platform, such as *x86\_64*, *arm*, or *powerpc*.

## Installing via a DHCP/Web Server Method with DHCP Options

Installing Cumulus Linux in this manner is as simple as setting up a
DHCP/Web server on your laptop and connecting the eth0 management port
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
entire URL to the Web server (this could be the same system). However,
there are many other ways to use DHCP even if you don't have full
control over DHCP. [See the ONIE user guide](https://opencomputeproject.github.io/onie/design-spec/discovery.html#partial-installer-urls)
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

Don't have a Web server? There is a [free Apache
example](https://www.apachefriends.org/index.html) you can utilize.

## Installing via a DHCP/Web Server Method without DHCP Options

If you have a laptop on same network and the switch can pull DHCP from
the corporate network, but you cannot modify DHCP options (maybe it's
controlled by another team), do the following:

1.  Place the Cumulus Linux binary in a directory on the Web server.

2.  Run the `onie-nos-install` command manually, since DHCP options
    can't be modified:
    
        ONIE:/ #onie-nos-install http://10.0.1.251/path/to/cumulus-install-[PLATFORM].bin

## Installing via a Web Server with no DHCP

Use the following method if your laptop is on the same network as the
switch eth0 interface but no DHCP server is available.

One thing to note is ONIE is in [*discovery
mode*](http://opencomputeproject.github.io/onie/design-spec/discovery.html#installer-discovery-methods),
so if you are setting a static IPv4 address for the eth0 management
port, you need to disable discovery mode or else ONIE may get confused.

1.  To disable discovery mode, run:
    
        onie# onie-discovery-stop 
    
    or, on older ONIE versions if that command isn't supported:
    
        onie# /etc/init.d/discover.sh stop 

2.  Assign a static address to eth0 via ONIE (using `ip addr add`):
    
        ONIE:/ #ip addr add 10.0.1.252/24 dev eth0

3.  Place the Cumulus Linux installer image in a directory on your Web
    server.

4.  Run the `onie-nos-install` command manually since there are no DHCP
    options:
    
        ONIE:/ #onie-nos-install http://10.0.1.251/path/to/cumulus-install-[PLATFORM].bin

## Installing via FTP or TFTP without a Web Server

1.  Set up DHCP or static addressing for eth0, as in the examples above.

2.  If you are utilizing static addressing, disable ONIE discovery mode.

3.  Place the Cumulus Linux installer image into a TFTP or FTP
    directory.

4.  If you are not utilizing DHCP options, run one of the following
    commands (`tftp` for TFTP or `ftp` for FTP):
    
        ONIE# onie-nos-install ftp://local-ftp-server/cumulus-install-[PLATFORM].bin
        
        ONIE# onie-nos-install tftp://local-tftp-server/cumulus-install-[PLATFORM].bin

## Installing via a Local File

1.  Set up DHCP or static addressing for eth0, as in the examples above.

2.  If you are utilizing static addressing, disable ONIE discovery mode.

3.  Use [scp](http://en.wikipedia.org/wiki/Secure_copy) to copy the
    Cumulus Linux binary to the switch.
    
    {{%notice tip%}}
    
    Windows users can use [WinScp](http://winscp.net/eng/index.php).
    
    {{%/notice%}}

4.  Run the following command:
    
        ONIE# onie-nos-install /path/to/local/file/cumulus-install-[PLATFORM].bin

## Installing via USB

Following the steps below produces a clean installation of Cumulus
Linux. This wipes out all pre-existing configuration files that may be
present on the switch. Instructions are offered for x86, ARM and PowerPC
platforms, and also cover the installation of a license after the
software installation.

{{%notice note%}}

Make sure to [back up](/version/cumulus-linux-25esr/Installation-Upgrading-and-Package-Management/Managing-Cumulus-Linux-Disk-Images/Upgrading-Cumulus-Linux)
any important configuration files that you may need to restore the
configuration of your switch after the installation finishes.

{{%/notice%}}

### Preparing for USB Installation

1.  Download the appropriate Cumulus Linux image for your x86, ARM or
    PowerPC platform from the [Cumulus Networks Downloads
    page](http://cumulusnetworks.com/downloads/).

1.  Prepare your flash drive by formatting in one of the supported
    formats: FAT32, vFAT or EXT2. 
    <details>
    
    <summary>Optional: Preparing a USB Drive inside Cumulus Linux
    </summary>
    
    {{%notice warning%}}
It is possible that you could severely damage your system with the following utilities, so please use caution when performing the actions below!
    {{%/notice%}}
    
    1. Insert your flash drive into the USB port on the switch running Cumulus Linux and log in to the switch.
    1. Determine and note at which device your flash drive can be found by 
       using output from `cat /proc/partitions` and `sudo fdisk -l [device]`. For example, `sudo fdisk -l /dev/sdb`.
       {{%notice warning%}}
  These instructions assume your USB drive is the `/dev/sdb` device, which is typical if the USB stick was inserted after the machine was already booted. However, if the USB stick was plugged in during the boot process, it is possible the device could be `/dev/sda`. Make sure to modify the commands below to use the proper device for your USB drive!
       {{%/notice%}}
    1. Create a new partition table on the device:
       ```
sudo parted /dev/sdb mklabel msdos
       ```
       {{%notice note%}}
The `parted` utility should already be installed. However, if it is not, install it with `sudo apt-get install parted`.
       {{%/notice%}}
    1. Create a new partition on the device:
       ```
sudo parted /dev/sdb -a optimal mkpart primary 0% 100%
       ```
    1. Format the partition to your filesystem of choice using ONE of the examples below:
       ```
    sudo mkfs.ext2 /dev/sdb1
    sudo mkfs.msdos -F 32 /dev/sdb1
    sudo mkfs.vfat /dev/sdb1
       ```  
       {{%notice note%}}
To use `mkfs.msdos` or `mkfs.vfat`, you need to install the `dosfstools` package from the [Debian software repositories](/version/cumulus-linux-25esr/Installation-Upgrading-and-Package-Management/Adding-and-Updating-Packages/#adding-packages-from-another-repository)  (step 3 here shows you how to add repositories from Debian), as they are not included by default.
       {{%/notice%}}
    1. To continue installing Cumulus Linux, mount the USB drive in order to move files to it.
    
       ```
    sudo mkdir /mnt/usb
    sudo mount /dev/sdb1 /mnt/usb
       ```
    </details>
1.  Copy the image and license files over to the flash drive and rename
    the image file to:
    
      - `onie-installer-x86_64`, if installing on an x86 platform
      - `onie-installer-powerpc`, if installing on a PowerPC platform
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

1.  Insert the USB stick into the switch, then continue with the
    appropriate instructions below for your x86, ARM or PowerPC
    platform.

### Instructions for x86 Platforms

<details>
<summary>Click to expand x86 instructions... </summary>

1.  Prepare the switch for installation:
    
      - If the switch is offline, connect to the console and power on
        the switch.
    
      - If the switch is already online in Cumulus Linux, connect to the
        console and reboot the switch into the ONIE environment with the
        `sudo cl-img-select -i` command, followed by `sudo reboot`. Then
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
        OS-Release:  2.5.3a-3b46bef-201509041633-build
        Architecture: amd64
        Date:  Fri, 04 Sep 2015 17:10:30 -0700
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
    
    ``` 
sudo mkdir /mnt/mountpoint
    ```

8.  Mount the USB drive to the newly created mount point:
    
    ``` 
sudo mount /dev/sdb1 /mnt/mountpoint
    ```

9.  Install your license file with the `cl-license` command:
    
    ``` 
sudo cl-license -i /mnt/mountpoint/license.txt
    ```

10. Check that your license is installed with the `cl-license` command.

11. Reboot the switch to utilize the new license.
    
    ``` 
sudo reboot
    ```
</details>

### Instructions for PowerPC and ARM Platforms

<details>
<summary>Click to expand PowerPC instructions... </summary>

1.  Prepare the switch for installation:
    
      - If the switch is offline, connect to the console and power on
        the switch.
    
      - If the switch is already online in Cumulus Linux, connect to the
        console and reboot the switch into the ONIE environment with the
        `sudo cl-img-select -i` command, followed by `sudo reboot`. Then
        skip to step 4.
    
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
        Platform: powerpc-as6701_32x-r0
        Version : 1.6.1.3
        WARNING: adjusting available memory to 30000000
        ## Booting kernel from Legacy Image at ec040000 …
           Image Name:   as6701_32x.1.6.1.3
           Image Type:   PowerPC Linux Multi-File Image (gzip compressed)
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
        ONIE: Executing installer: file://dev/sdb1/onie-installer-powerpc
        Verifying image checksum ... OK.
        Preparing image archive ... OK.
        Dumping image info…
        Control File Contents
        =====================
        Description: Cumulus Linux
        OS-Release: 2.5.3a-3b46bef-201509041633-build
        Architecture: powerpc
        Date: Fri, 04 Sep 2015 17:08:35 -0700
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
    
    ``` 
sudo mkdir /mnt/mountpoint
    ```

8.  Mount the USB drive to the newly created mount point:
    
    ``` 
sudo mount /dev/sdb1 /mnt/mountpoint
    ```

9.  Install your license file with the `cl-license` command:
    
    ``` 
sudo cl-license -i /mnt/mountpoint/license.txt
    ```

10. Check that your license is installed with the `cl-license` command.

11. Reboot the switch to utilize the new license.
    
    ``` 
sudo reboot
    ```
</details>

## Installing a New Image when Cumulus Linux Is already Installed

Follow these upgrade steps for both major and minor releases, where:

  - A major release upgrade is 2.X.X to 3.X.X (e.g. 1.5.1 to 2.5.0)
  - A minor release upgrade is X.2.X to X.3.X (e.g. 2.2.0 to 2.5.5)

For more information, see [Upgrading Cumulus Linux](/version/cumulus-linux-25esr/Installation-Upgrading-and-Package-Management/Managing-Cumulus-Linux-Disk-Images/Upgrading-Cumulus-Linux/#upgrading-via-binary-install-cl-img-install).

### Entering ONIE Mode from Cumulus Linux

If Cumulus Linux is already installed on the switch, you can enter ONIE
mode in one of two ways, using:

  - ONIE Recovery Mode to manually install an image from the ONIE
    prompt:
    
        cumulus@switch:~$ sudo cl-img-select -r
        cumulus@switch:~$ sudo reboot
  - ONIE Install Mode to attempt to automatically discover the image
    from a DHCP server:
    
        cumulus@switch:~$ sudo cl-img-select -i
        cumulus@switch:~$ sudo reboot
