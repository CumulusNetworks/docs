---
title: Managing Cumulus RMP Disk Images
author: Cumulus Networks
weight: 147
aliases:
 - /display/RMP321/Managing+Cumulus+RMP+Disk+Images
 - /pages/viewpage.action?pageId=5127549
pageID: 5127549
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
The Cumulus RMP operating system resides on a switch as a *disk image*.
This section discusses how to manage them.

Cumulus RMP comes preinstalled on your switch. However there may be
instances where you need to perform a full image installation. Before
you install Cumulus RMP, the switch can be in two different states:

  - The switch already has Cumulus RMP installed on it, so you only need
    to [upgrade it](#src-5127549_ManagingCumulusRMPDiskImages-upgr).

  - The switch has no image on it (so the switch is only running
    [ONIE](http://www.onie.org/)) or you desire or require a clean
    installation. In which case, you would install Cumulus RMP in one of
    the following ways, using:
    
      - [DHCP/a web server with DHCP
        options](#src-5127549_ManagingCumulusRMPDiskImages-dhcp_options)
    
      - [DHCP/a web server without DHCP
        options](#src-5127549_ManagingCumulusRMPDiskImages-dhcp_noopts)
    
      - [A web server with no
        DHCP](#src-5127549_ManagingCumulusRMPDiskImages-web_nodhcp)
    
      - [FTP or TFTP without a web
        server](#src-5127549_ManagingCumulusRMPDiskImages-ftp)
    
      - [Local file
        installation](#src-5127549_ManagingCumulusRMPDiskImages-local)
    
      - [USB](#src-5127549_ManagingCumulusRMPDiskImages-usb)

{{%notice tip%}}

[ONIE](http://www.onie.org/) is an open source project, equivalent to
PXE on servers, that allows installation of network operating systems
(NOS) on bare metal switches.

{{%/notice%}}

Unlike Cumulus Linux, there is no license to install on a Cumulus RMP
switch.

## <span>Understanding these Examples</span>

The sections in this chapter are ordered from the most repeatable to the
least repeatable methods. For instance, DHCP can scale to hundreds of
switch installs with zero manual input, compared to something like USB
installs. Installing via USB is fine for a single switch here and there
but is not scalable.

You can name your Cumulus RMP installer binary using any of the [ONIE
naming schemes mentioned
here](http://opencomputeproject.github.io/onie/docs/design-spec/discovery.html#default-file-name-search-order).

## <span id="src-5127549_ManagingCumulusRMPDiskImages-dhcp_options" class="confluence-anchor-link"></span><span>Installing via a DHCP/Web Server Method with DHCP Options</span>

Installing Cumulus RMP in this manner is as simple as setting up a
DHCP/web server on your laptop and connecting the eth0 management port
of the switch to your laptop.

Once you connect the cable, the installation proceeds as follows:

1.  The bare metal switch boots up and asks for an address (DHCP
    request).

2.  The DHCP server acknowledges and responds with DHCP option 114 and
    the location of the installation image.

3.  ONIE downloads the Cumulus RMP binary, installs and reboots.

4.  Success\! You are now running Cumulus RMP.
    
    {{% imgOld 0 %}}

{{%notice note%}}

The most common method is for you to send DHCP option 114 with the
entire URL to the web server (this could be the same system). However,
there are many other ways to use DHCP even if you don't have full
control over DHCP. [See the ONIE user
guide](https://github.com/opencomputeproject/onie/wiki/Design-Spec-SW-Image-Discovery#partial-installer-urls)
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

Don't have a web server? There is a [free Apache
example](https://www.apachefriends.org/index.html) you can utilize.

## <span id="src-5127549_ManagingCumulusRMPDiskImages-dhcp_noopts" class="confluence-anchor-link"></span><span>Installing via a DHCP/Web Server Method without DHCP Options</span>

If you have a laptop on same network and the switch can pull DHCP from
the corporate network, but you cannot modify DHCP options (maybe it's
controlled by another team), do the following:

1.  Place the Cumulus RMP binary in a directory on the web server.

2.  Run the `onie-nos-install` command manually, since DHCP options
    can't be modified:
    
        ONIE:/ #onie-nos-install http://10.0.1.251/path/to/cumulus-install-[PLATFORM].bin

## <span id="src-5127549_ManagingCumulusRMPDiskImages-web_nodhcp" class="confluence-anchor-link"></span><span>Installing via a Web Server with no DHCP</span>

Use the following method if your laptop is on the same network as the
switch eth0 interface but no DHCP server is available.

One thing to note is ONIE is in [*discovery
mode*](http://opencomputeproject.github.io/onie/docs/design-spec/discovery.html#installer-discovery-methods)
, so if you are setting a static IPv4 address for the eth0 management
port, you need to disable discovery mode or else ONIE may get confused.

1.  To disable discovery mode, run:
    
        onie# onie-discovery-stop 
    
    or, on older ONIE versions if that command isn't supported:
    
        onie# /etc/init.d/discover.sh stop 

2.  Assign a static address to eth0 via ONIE (using `ip addr add`):
    
        ONIE:/ #ip addr add 10.0.1.252/24 dev eth0

3.  Place the Cumulus RMP installer image in a directory on your web
    server.

4.  Run the `onie-nos-install` command manually since there are no DHCP
    options:
    
        ONIE:/ #onie-nos-install http://10.0.1.251/path/to/cumulus-install-[PLATFORM].bin

## <span id="src-5127549_ManagingCumulusRMPDiskImages-ftp" class="confluence-anchor-link"></span><span>Installing via FTP or TFTP without a Web Server</span>

1.  Set up DHCP or static addressing for eth0, as in the examples above.

2.  If you are utilizing static addressing, disable ONIE discovery mode.

3.  Place the Cumulus RMP installer image into a TFTP or FTP directory.

4.  If you are not utilizing DHCP options, run one of the following
    commands (`tftp` for TFTP or `ftp` for FTP):
    
        ONIE# onie-nos-install ftp://local-ftp-server/cumulus-install-[PLATFORM].bin
         
        ONIE# onie-nos-install tftp://local-tftp-server/cumulus-install-[PLATFORM].bin

## <span id="src-5127549_ManagingCumulusRMPDiskImages-local" class="confluence-anchor-link"></span><span>Installing via a Local File</span>

1.  Set up DHCP or static addressing for eth0, as in the examples above.

2.  If you are utilizing static addressing, disable ONIE discovery mode.

3.  Use [scp](http://en.wikipedia.org/wiki/Secure_copy) to copy the
    Cumulus RMP binary to the switch.  
    **Note:** Windows users can use
    [WinScp](http://winscp.net/eng/index.php).

4.  Run the following command:
    
        ONIE# onie-nos-install /path/to/local/file/cumulus-install-[PLATFORM].bin

## <span id="src-5127549_ManagingCumulusRMPDiskImages-usb" class="confluence-anchor-link"></span><span>Installing via USB</span>

Follow the steps below to conduct a full installation of Cumulus RMP.
This wipes out all pre-existing configuration files that may be present
on the switch.

{{%notice note%}}

Make sure to back up any important configuration files that you may need
to restore the configuration of your switch after the installation
finishes.

{{%/notice%}}

### <span>Preparing for USB Installation</span>

1.  Download the Cumulus RMP image from the [Cumulus Downloads
    page](http://cumulusnetworks.com/downloads/).

2.  
    
    <details>
    
    Prepare your flash drive by formatting in one of the supported
    formats: FAT32, vFAT or EXT2.
    
    <summary>Optional: Preparing a USB Drive inside Cumulus RMP
    </summary>
    
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
    <li><p>Insert your flash drive into the USB port on the switch running Cumulus RMP and log in to the switch.</p></li>
    <li><p>Determine and note which device your flash drive can be found at using output from <code>cat /proc/partitions</code> and <code>sudo fdisk -l [device]</code>. For example, <code>sudo fdisk -l /dev/sdb</code>. These instructions assume your USB drive is the <code>/dev/sdb</code> device, which is typical. Make sure to modify the commands below to use the proper device for your USB drive.</p></li>
    <li><p>Create a new partition table on the device:</p>
    <pre><code>sudo parted /dev/sdb mklabel msdos</code></pre>
    <p>{{%notice note%}}</p>
    <p>The <code>parted</code> utility should already be installed. However, if it is not, install it with: <code>sudo apt-get install parted</code><code></code></p>
    <p>{{%/notice%}}</p></li>
    <li><p>Create a new partition on the device:</p>
    <pre><code>sudo parted /dev/sdb -a optimal mkpart primary 0% 100%</code></pre></li>
    <li><p>Format the partition to your filesystem of choice using ONE of the examples below:</p>
    <pre><code>sudo mkfs.ext2 /dev/sdb1
    sudo mkfs.msdos -F 32 /dev/sdb1
    sudo mkfs.vfat /dev/sdb1</code></pre>
    <p>{{%notice note%}}</p>
    <p>To use <code>mkfs.msdos</code> or <code>mkfs.vfat</code>, you need to install the <code>dosfstools</code> package from the <a href="http://docs.cumulusnetworks.com/display/DOCS/Adding+and+Updating+Packages#AddingandUpdatingPackages-AddingPackagesfromAnotherRepository" class="external-link">Debian software repositories</a> (step 3 here shows you how to add repositories from Debian), as they are not included by default.</p>
    <p>{{%/notice%}}</p></li>
    <li><p>To continue installing Cumulus RMP, mount the USB drive in order to move files to it.</p>
    <pre><code>sudo mkdir /mnt/usb
    sudo mount /dev/sdb1 /mnt/usb</code></pre></li>
    </ol></td>
    </tr>
    </tbody>
    </table>
    
    </details>

3.  Copy the image file over to the flash drive and rename the image
    file to `onie-installer_x86-64`.
    
    {{%notice note%}}
    
    You can also use any of the [ONIE naming schemes mentioned
    here](http://opencomputeproject.github.io/onie/docs/design-spec/discovery.html#default-file-name-search-order).
    
    {{%/notice%}}
    
    {{%notice warning%}}
    
    When using a Mac or Windows computer to rename the installation file
    the file extension may still be present. Make sure to remove the
    file extension otherwise ONIE will not be able to detect the file\!
    
    {{%/notice%}}

4.  Insert the USB stick into the switch, then prepare the switch for
    installation:
    
      - If the switch is offline, connect to the console and power on
        the switch.
    
      - If the switch is already online in Cumulus RMP, connect to the
        console and reboot the switch into the ONIE environment with the
        `sudo onie-select -i` command, followed by `sudo reboot`. Then
        skip to step 8 below.
    
      - If the switch is already online in ONIE, use the `reboot`
        command.

5.  {{%notice note%}}
    
    SSH sessions to the switch get dropped after this step. To complete
    the remaining instructions, connect to the console of the switch.
    Cumulus RMP switches display their boot process to the console, so
    you need to monitor the console specifically to complete the next
    step.
    
    {{%/notice%}}

6.  Monitor the console and select the ONIE option from the first GRUB
    screen shown below.
    
    {{% imgOld 1 %}}

7.  Cumulus RMP uses GRUB chainloading to present a second GRUB menu
    specific to the ONIE partition. No action is necessary in this menu
    to select the default option *ONIE: Install OS*.
    
    {{% imgOld 2 %}}

8.  At this point, the USB drive should be automatically recognized and
    mounted. The image file should be located and automatic installation
    of Cumulus RMP should begin. Here is some sample output:
    
        ONIE: OS Install Mode  ...
         
        Version : penguin_arctica-2014.05.05-6919d98-201410171013
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
        Date:  Fri, 04 Sep 2015 17:10:30 -0700
        Installer-Version:  1.2
        Platforms: accton_as5712_54x accton_as6712_32x  mlx_sx1400_i73612 dell_s6000_s1220 dell_s4000_c2338 dell_s3000_c2338  cel_redstone_xp cel_smallstone_xp cel_pebble quanta_panther  quanta_ly8_rangeley quanta_ly6_rangeley quanta_ly9_rangeley  
        Homepage: http://www.cumulusnetworks.com/

9.  After installation completes, the switch automatically reboots into
    the newly installed instance of Cumulus RMP.

10. Determine and note at which device your flash drive can be found by
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

11. Create a mount point to mount the USB drive to:
    
    ``` 
     sudo mkdir /mnt/mountpoint
    ```

12. Mount the USB drive to the newly created mount point:
    
    ``` 
     sudo mount /dev/sdb1 /mnt/mountpoint
    ```

## <span id="src-5127549_ManagingCumulusRMPDiskImages-upgrade" class="confluence-anchor-link"></span><span>Upgrading Cumulus RMP</span>

If you already have Cumulus RMP installed on your switch and you are
upgrading to an X.Y.Z release, like 2.5.7 from an earlier release in the
same major and minor release family **only** (like 2.5.4 to 2.5.7), you
can use `apt-get` to upgrade to the new version. (If are upgrading to a
major (X.0) or minor (X.Y) release, you must do a full image install, as
described above.)

To upgrade to a maintenance (X.Y.Z) release using `apt-get`:

1.  Run `apt-get update`.

2.  Run `apt-get dist-upgrade`.

3.  Reboot the switch.

## <span>Related Information</span>

  - [Open Network Install Environment (ONIE) Home
    Page](http://opencomputeproject.github.io/onie/)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
