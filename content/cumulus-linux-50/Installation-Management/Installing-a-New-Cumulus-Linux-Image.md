---
title: Installing a New Cumulus Linux Image
author: NVIDIA
weight: 40
toc: 3
---
{{%notice warning%}}

The default password for the *cumulus* user account is `cumulus`. The first time you log into Cumulus Linux, you are **required** to change this default password. Be sure to update any automation scripts before installing a new image. Cumulus Linux provides command line options to change the default password automatically during the installation process. Refer to [ONIE Installation Options](#onie-installation-options).

{{%/notice%}}

You can install a new Cumulus Linux image using {{<exlink url="http://www.onie.org/" text="ONIE">}}, an open source project (equivalent to PXE on servers) that enables the installation of network operating systems (NOS) on bare metal switches.

Before you install Cumulus Linux, the switch can be in two different states:

- No image is installed on the switch (the switch is only running ONIE).
- Cumulus Linux is already installed on the switch but you want to use ONIE to reinstall Cumulus Linux or upgrade to a newer version.

The sections below describe some of the different ways you can install the Cumulus Linux image. Steps are provided for both installing directly from ONIE (if no image is installed on the switch) and from Cumulus Linux (if the image is already installed on the switch). For additional methods to find and install the Cumulus Linux image, see the {{<exlink url="http://opencomputeproject.github.io/onie/design-spec/discovery.html" text="ONIE Design Specification">}}.

You can download a Cumulus Linux image from the {{<exlink url="http://cumulusnetworks.com/downloads/" text="Cumulus Linux Downloads">}} page.

{{%notice warning%}}

Installing the Cumulus Linux image is destructive; configuration files on the switch are not saved; copy them to a different server before installing.

{{%/notice%}}

In the following procedures:

- You can name your Cumulus Linux image using any of the
{{<exlink url="http://opencomputeproject.github.io/onie/design-spec/discovery.html#default-file-name-search-order" text="ONIE naming schemes">}} mentioned here.
- Run the `sudo onie-install -h` command to show the ONIE installer options.
<!--- After you install the Cumulus Linux image, you need to install the license file. Refer to {{<link url="Quick-Start-Guide#install-the-license" text="Install the License">}}.-->

## Install Using a DHCP/Web Server with DHCP Options

To install Cumulus Linux using a DHCP/web server *with* DHCP options, set up a DHCP/web server on your laptop and connect the eth0 management port of the switch to your laptop. After you connect the cable, the installation proceeds as follows:

1. The switch boots up and requests an IP address (DHCP request).
2. The DHCP server acknowledges and responds with DHCP option 114 and the location of the installation image.
3. ONIE downloads the Cumulus Linux image, installs, and reboots.
4. Success! You are now running Cumulus Linux.

{{< img src = "/images/cumulus-linux/install-image-onie-dhcp.png" >}}

{{%notice note%}}

The most common method is to send DHCP option 114 with the entire URL to the web server (this can be the same system). However, there are many other ways to use DHCP even if you do not have full control over DHCP. See the ONIE user guide for help with {{<exlink url="https://opencomputeproject.github.io/onie/design-spec/discovery.html#partial-installer-urls" text="partial installer URLs">}} and {{<exlink url="https://opencomputeproject.github.io/onie/user-guide/index.html#advanced-dhcp-2-vivso" text="advanced DHCP options">}}; both articles list more supported DHCP options.

{{%/notice%}}

Here is an example DHCP configuration with an {{<exlink url="http://www.isc.org/downloads/dhcp/" text="ISC DHCP server">}}:

```
subnet 172.0.24.0 netmask 255.255.255.0 {
  range 172.0.24.20 172.0.24.200;
  option default-url = "http://172.0.24.14/onie-installer-x86_64";
}
```

Here is an example DHCP configuration with {{<exlink url="http://www.thekelleys.org.uk/dnsmasq/doc.html" text="dnsmasq">}} (static address assignment):

```
dhcp-host=sw4,192.168.100.14,6c:64:1a:00:03:ba,set:sw4
dhcp-option=tag:sw4,114,"http://roz.rtplab.test/onie-installer-x86_64"
```

If you do not have a web server, you can use {{<exlink url="https://www.apachefriends.org/index.html" text="this free Apache example">}}.

## Install Using a DHCP/Web Server without DHCP Options

Follow the steps below if you can log into the switch on a serial console (ONIE), or log in on the console or with ssh (Install from Cumulus Linux).

{{< tabs "TabID75 ">}}

{{< tab "Install from ONIE ">}}

1. Place the Cumulus Linux image in a directory on the web server.
2. Run the `onie-nos-install` command:

    ```
    ONIE:/ #onie-nos-install http://10.0.1.251/path/to/cumulus-install-x86_64.bin
    ```

{{< /tab >}}

{{< tab "Install from Cumulus Linux ">}}

1. Place the Cumulus Linux image in a directory on the web server.

2. From the Cumulus Linux command prompt, run the `onie-install` command, then reboot the switch.

    ```
    cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/path/to/cumulus-install-x86_64.bin
    ```

{{< /tab >}}

{{< /tabs >}}

## Install Using a Web Server with no DHCP

Follow the steps below if you can log into the switch on a serial console (ONIE), or you can log in on the console or with ssh (Install from Cumulus Linux) but *no* DHCP server is available.

{{%notice note%}}

You need a console connection to access the switch; you cannot perform this procedure remotely.

{{%/notice%}}

{{< tabs "TabID111 ">}}

{{< tab "Install from ONIE ">}}

1. ONIE is in *{{<exlink url="http://opencomputeproject.github.io/onie/design-spec/discovery.html#installer-discovery-methods" text="discovery mode">}}*. You must disable discovery mode with the following command:

    ```
    onie# onie-discovery-stop
    ```

    On older ONIE versions, if the `onie-discovery-stop` command is not supported, run:

    ```
    onie# /etc/init.d/discover.sh stop
    ```

2. Assign a static address to eth0 with the `ip addr add` command:

    ```
    ONIE:/ #ip addr add 10.0.1.252/24 dev eth0
    ```

3. Place the Cumulus Linux image in a directory on your web server.

4. Run the installer manually (because there are no DHCP options):

    ```
    ONIE:/ #onie-nos-install http://10.0.1.251/path/to/cumulus-install-x86_64.bin
    ```

{{< /tab >}}

{{< tab "Install from Cumulus Linux ">}}

1. Place the Cumulus Linux image in a directory on your web server.

2. From the Cumulus Linux command prompt, run the `onie-install` command, then reboot the switch.

    ```
    cumulus@switch:~$ sudo onie-install -a -i http://10.0.1.251/path/to/cumulus-install-x86_64.bin
    ```

{{< /tab >}}

{{< /tabs >}}

## Install Using FTP Without a Web Server

Follow the steps below if your laptop is on the same network as the switch eth0 interface but *no* DHCP server is available.

{{< tabs "TabID162 ">}}

{{< tab "Install from ONIE ">}}

1. Set up DHCP or static addressing for eth0. The following example assigns a static address to eth0:

    ```
    ONIE:/ #ip addr add 10.0.1.252/24 dev eth0
    ```

2. If you are using static addressing, disable ONIE discovery mode:

    ```
    onie# onie-discovery-stop
    ```

    On older ONIE versions, if the `onie-discovery-stop` command is not supported, run:

    ```
    onie# /etc/init.d/discover.sh stop
    ```

3. Place the Cumulus Linux image into a TFTP or FTP directory.

4. If you are not using DHCP options, run one of the following commands (`tftp` for TFTP or `ftp` for FTP):

    ```
    ONIE# onie-nos-install ftp://local-ftp-server/cumulus-install-x86_64.bin

    ONIE# onie-nos-install tftp://local-tftp-server/cumulus-install-x86_64.bin
    ```

{{< /tab >}}

{{< tab "Install from Cumulus Linux ">}}

1. Place the Cumulus Linux image into a TFTP or FTP directory.

2. From the Cumulus Linux command prompt, run one of the following
    commands (`tftp` for TFTP or `ftp` for FTP), then reboot the switch.

    ```
    cumulus@switch:~$ sudo onie-install -a -i ftp://local-ftp-server/cumulus-install-x86_64.bin

    cumulus@switch:~$ sudo onie-install -a -i tftp://local-ftp-server/cumulus-install-x86_64.bin
    ```

{{< /tab >}}

{{< /tabs >}}

## Install Using a Local File

Follow the steps below to install the Cumulus Linux image referencing a local file.

{{< tabs "TabID217 ">}}

{{< tab "Install from ONIE ">}}

1. Set up DHCP or static addressing for eth0. The following example assigns a static address to eth0:

    ```
    ONIE:/ #ip addr add 10.0.1.252/24 dev eth0
    ```

2. If you are using static addressing, disable ONIE discovery mode.

    ```
    onie# onie-discovery-stop
    ```

    On older ONIE versions, if the `onie-discovery-stop` command is not supported, run:

    ```
    onie# /etc/init.d/discover.sh stop
    ```

3. Use {{<exlink url="http://en.wikipedia.org/wiki/Secure_copy" text="scp">}} to copy the Cumulus Linux image to the switch.

4. Run the installer manually from ONIE:

    ```
    ONIE:/ #onie-nos-install /path/to/local/file/cumulus-install-x86_64.bin
    ```

{{< /tab >}}

{{< tab "Install from Cumulus Linux ">}}

1. Copy the Cumulus Linux image to the switch.

2. From the Cumulus Linux command prompt, run the `onie-install` command, then reboot the switch.

    ```
    cumulus@switch:~$ sudo onie-install -a -i /path/to/local/file/cumulus-install-x86_64.bin
    ```

{{< /tab >}}

{{< /tabs >}}

## Install Using a USB Drive

Follow the steps below to install the Cumulus Linux image using a USB drive.
{{%notice tip%}}

Installing Cumulus Linux using a USB drive is fine for a single switch here and there but is not scalable. DHCP can scale to hundreds of switch installs with zero manual input unlike USB installs.

{{%/notice%}}

### Prepare for USB Installation

1. From the {{<exlink url="http://cumulusnetworks.com/downloads/" text="Cumulus Linux Downloads page">}}, download the appropriate Cumulus Linux image for your platform.
2.  From a computer, prepare your USB drive by formatting it using one of the supported formats: FAT32, vFAT or EXT2.

    {{< expand "Optional: Prepare a USB Drive inside Cumulus Linux"  >}}

a. Insert your USB drive into the USB port on the switch running Cumulus Linux and log in to the switch. Examine output from `cat /proc/partitions` and `sudo fdisk -l [device]` to determine on which device your USB drive can be found. For example, `sudo fdisk -l /dev/sdb`.

   These instructions assume your USB drive is the `/dev/sdb` device, which is typical if you insert the USB drive after the machine is already booted. However, if you insert the USB drive during the boot process, it is possible that your USB drive is the `/dev/sda` device. Make sure to modify the commands below to use the proper device for your USB drive.

b. Create a new partition table on the USB drive. (The `parted` utility should already be installed. However, if it is not, install it with `sudo -E apt-get install parted`.)

   ```
   sudo parted /dev/sdb mklabel msdos
   ```

c. Create a new partition on the USB drive:

   ```
   sudo parted /dev/sdb -a optimal mkpart primary 0% 100%
   ```

d. Format the partition to your filesystem of choice using *one* of the examples below:

   ```
   sudo mkfs.ext2 /dev/sdb1
   sudo mkfs.msdos -F 32 /dev/sdb1
   sudo mkfs.vfat /dev/sdb1
   ```

   To use `mkfs.msdos` or `mkfs.vfat`, you need to install the `dosfstools` package from the
{{<link url="Adding-and-Updating-Packages" text="Debian software repositories">}}, as they are not included by default.

e. To continue installing Cumulus Linux, mount the USB drive to move files:

   ```
   sudo mkdir /mnt/usb
   sudo mount /dev/sdb1 /mnt/usb
   ```

{{< /expand >}}

3. Copy the Cumulus Linux image to the USB drive, then rename the image file to `onie-installer-x86_64`.

    You can also use any of the {{<exlink url="http://opencomputeproject.github.io/onie/design-spec/discovery.html#default-file-name-search-order" text="ONIE naming schemes mentioned here">}}.

    When using a Mac or Windows computer to rename the installation file, the file extension might still be present. Make sure to remove the file extension otherwise ONIE is not able to detect the file.

4. Insert the USB drive into the switch, then prepare the switch for installation:

    - If the switch is offline, connect to the console and power on the switch.
    - If the switch is already online in ONIE, use the `reboot` command.

    SSH sessions to the switch get dropped after this step. To complete the remaining instructions, connect to the console of the switch. Cumulus Linux switches display their boot process to the console; you need to monitor the console specifically to complete the next step.

5. Monitor the console and select the ONIE option from the first GRUB screen shown below.

    {{< img src = "/images/cumulus-linux/install-image-GNUx86-1.png" >}}

6. Cumulus Linux on x86 uses GRUB chainloading to present a second GRUB menu specific to the ONIE partition. No action is necessary in this menu to select the default option *ONIE: Install OS*.

    {{< img src = "/images/cumulus-linux/install-image-GNUx86-2.png" >}}

7. The USB drive is recognized and mounted automatically. The image file is located and automatic installation of Cumulus Linux begins.

8. After installation completes, the switch automatically reboots into the newly installed instance of Cumulus Linux.

## ONIE Installation Options

You can run several installer command line options from ONIE to perform basic switch configuration automatically after installation completes and Cumulus Linux boots for the first time. These options enable you to:

- Set a unique password for the *cumulus* user<!-- - Apply a Cumulus Linux license-->
- Provide an initial network configuration
- Execute a ZTP script to perform necessary configuration

{{%notice note%}}

The `onie-nos-install` command does *not* allow you specify command line parameters. You must access the switch from the console and transfer a disk image to the switch. You must then make the disk image executable and install the image directly from the ONIE command line with the options you want to use.

The following example commands transfer a disk image to the switch, make the image executable, and install the image with the `--password` option to change the default cumulus user password:

```
ONIE:/ # wget http://myserver.datacenter.com/cumulus-linux-5.0.0-mlx-amd64.bin
ONIE:/ # chmod 755 cumulus-linux-5.0.0-mlx-amd64.bin
ONIE:/ # ./cumulus-linux-5.0.0-mlx-amd64.bin --password 'MyP4$$word'
```

{{%/notice%}}

You can run more than one option in the same command.

### Set the cumulus User Password

The default *cumulus* user account password is `cumulus`. When you log into Cumulus Linux for the first time, you must provide a new password for the *cumulus* account, then log back into the system. This password change is **required**.

To automate this process, you can specify a new password from the command line of the installer with the `--password '<clear text-password>'` option. For example, to change the default *cumulus* user password to `MyP4$$word`:

```
ONIE:/ # ./cumulus-linux-5.0.0-mlx-amd64.bin --password 'MyP4$$word'
```

To provide a hashed password instead of a clear text password, use the `--hashed-password '<hash>'` option. Using an encrypted hash is recommended to maintain a secure management network.

1. Generate a sha-512 password hash with the following python command. The example command generates a sha-512 password hash for the password `MyP4$$word`.

   ```
   user@host:~$ python3 -c "import crypt; print(crypt.crypt('MyP4$$word',salt=crypt.mksalt()))"
   $6$hs7OPmnrfvLNKfoZ$iB3hy5N6Vv6koqDmxixpTO6lej6VaoKGvs5E8p5zNo4tPec0KKqyQnrFMII3jGxVEYWntG9e7Z7DORdylG5aR/
   ```

1. Specify the new password from the command line of the installer with the `--hashed-password '<hash>'` command:

   ```
   ONIE:/ # ./cumulus-linux-5.0.0-mlx-amd64.bin  --hashed-password '$6$hs7OPmnrfvLNKfoZ$iB3hy5N6Vv6koqDmxixpTO6lej6VaoKGvs5E8p5zNo4tPec0KKqyQnrFMII3jGxVEYWntG9e7Z7DORdylG5aR/'
   ```

{{%notice note%}}

If you specify both the `--password` and `--hashed-password` options, the `--hashed-password` option takes precedence and the `--password` option is ignored.

{{%/notice%}}

<!--### Apply a Cumulus Linux License

To apply a license and start the `switchd` service automatically after Cumulus Linux boots for the first time after installation, use the `--license <license-string>` option. For example:

```
ONIE:/ # ./cumulus-linux-5.0.0-mlx-amd64.bin  --license 'customer@datacenter.com|4C3YMCACDiK0D/EnrxlXpj71FBBNAg4Yrq+brza4ZtJFCInvalid'
```-->

### Provide Initial Network Configuration

To provide initial network configuration automatically when Cumulus Linux boots for the first time after installation, use the `--interfaces-file <filename>` option. For example, to copy the contents of a file called `network.intf` into the `/etc/network/interfaces` file and run the `ifreload -a` command:

```
ONIE:/ # ./cumulus-linux-5.0.0-mlx-amd64.bin  --interfaces-file network.intf
```

### Execute a ZTP Script

To run a ZTP script that contains commands to execute after Cumulus Linux boots for the first time after installation, use the `--ztp <filename>` option. For example, to run a ZTP script called `initial-conf.ztp`:

```
ONIE:/ # ./cumulus-linux-5.0.0-mlx-amd64.bin --ztp initial-conf.ztp
```

The ZTP script must contain the `CUMULUS-AUTOPROVISIONING` string near the beginning of the file and must reside on the ONIE filesystem. Refer to {{<link url="Zero-Touch-Provisioning-ZTP" text="Zero Touch Provisioning - ZTP">}}.

If you use the `--ztp` option together with any of the other command line options, the ZTP script takes precedence and the other command line options are ignored.

## Edit the Cumulus Linux Image (Advanced)

The Cumulus Linux disk image file contains a BASH script that includes a set of variables. You can set these variables to be able to install a fully-configured system with a single image file.

{{< expand "To edit the image"  >}}

### Example Image File

The Cumulus Linux disk image file is a self-extracting executable. The executable part of the file is a BASH script and is located at the beginning of the file. Towards the beginning of this BASH script are a set of variables set to an empty string:

```
...
CL_INSTALLER_PASSWORD=''
CL_INSTALLER_HASHED_PASSWORD=''
CL_INSTALLER_LICENSE=''
CL_INSTALLER_INTERFACES_FILENAME=''
CL_INSTALLER_INTERFACES_CONTENT=''
CL_INSTALLER_ZTP_FILENAME=''
CL_INSTALLER_QUIET=""
CL_INSTALLER_FORCEINST=""
CL_INSTALLER_INTERACTIVE=""
CL_INSTALLER_EXTRACTDIR=""
CL_INSTALLER_PAYLOAD_SHA256="72a8c3da28cda7a610e272b67fa1b3a54c50248bf6abf720f73ff3d10e79ae76"
```

The variables you can set are described below:

| Variable | Description |
| -------- | ----------- |
| `CL_INSTALLER_PASSWORD` |Defines the clear text password.<br>This variable is equivalent to the ONIE installer command line option `--password`.  |
| `CL_INSTALLER_HASHED_PASSWORD` | Defines the hashed password.<br>This variable is equivalent to the ONIE installer command line option `--hashed-password`.<br>If you set both the `CL_INSTALLER_PASSWORD` and `CL_INSTALLER_HASHED_PASSWORD` variable, the `CL_INSTALLER_HASHED_PASSWORD` takes precedence. |
| `CL_INSTALLER_INTERFACES_FILENAME` | Defines the name of the file on the ONIE filesystem you want to use as the `/etc/network/interfaces` file. <br>This variable is equivalent to the ONIE installer command line option `--interfaces-file`.|
| `CL_INSTALLER_INTERFACES_CONTENT` | Describes the network interfaces available on your system and how to activate them. Setting this variable defines the contents of the `/etc/network/interfaces` file.<br>There is no equivalent ONIE installer command line option.<br>If you set both the `CL_INSTALLER_INTERFACES_FILENAME` and `CL_INSTALLER_INTERFACES_CONTENT` variables, the `CL_INSTALLER_INTERFACES_FILENAME` takes precedence. |
| `CL_INSTALLER_ZTP_FILENAME` | Defines the name of the ZTP file on the ONIE filesystem you want to execute at first boot after installation. <br>This variable is equivalent to the ONIE installer command line option `--ztp`|
<!-- | `CL_INSTALLER_LICENSE` | Defines the Cumulus Linux license you want to install.<br>This variable is equivalent to the ONIE installer command line option `--license`.| -->

### Edit the Image File

Because the Cumulus Linux image file is mostly a binary file, you cannot use standard text editors to edit the file directly. Instead, you must split the file into two parts, edit the first part, then put the two parts back together.

1. Copy the first 20 lines to an empty file:

```
head -20 cumulus-linux-5.0.0-mlx-amd64.bin > cumulus-linux-5.0.0-mlx-amd64.bin.1
```

2. Remove the first 20 lines of the image, then copy the remaining lines into another empty file:

```
sed -e '1,20d' cumulus-linux-5.0.0-mlx-amd64.bin > cumulus-linux-5.0.0-mlx-amd64.bin.2
```

The original file is now split, with the first 20 lines in `cumulus-linux-5.0.0-mlx-amd64.bin.1` and the remaining lines in `cumulus-linux-5.0.0-mlx-amd64.bin.2`.

3. Use a text editor to change the variables in `cumulus-linux-5.0.0-mlx-amd64.bin.1`.

4. Put the two pieces back together using `cat`:

```
cat cumulus-linux-5.0.0-mlx-amd64.bin.1 cumulus-linux-5.0.0-mlx-amd64.bin.2 > cumulus-linux-5.0.0-mlx-amd64.bin.final
```

This is an example of a modified image file:

```
...
CL_INSTALLER_PASSWORD='MyP4$$word'
CL_INSTALLER_HASHED_PASSWORD=''
CL_INSTALLER_LICENSE='customer@datacenter.com|4C3YMCACDiK0D/EnrxlXpj71FBBNAg4Yrq+brza4ZtJFCInvalid'
CL_INSTALLER_INTERFACES_FILENAME=''
CL_INSTALLER_INTERFACES_CONTENT='# This file describes the network interfaces available on your system and how to activate them.

source /etc/network/interfaces.d/*.intf

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp
	vrf mgmt

auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-pvid 1
    bridge-vids 10 11
    bridge-vlan-aware yes

auto mgmt
iface mgmt
	address 127.0.0.1/8
	address ::1/128
	vrf-table auto
'
CL_INSTALLER_ZTP_FILENAME=''
...
```

You can install this edited image file in the usual way, by using the ONIE install waterfall or the `onie-nos-install` command.

If you install the modified installation image and specify installer command line parameters, the command line parameters take precedence over the variables modified in the image.

{{< /expand >}}

## Related Information

- {{<exlink url="http://opencomputeproject.github.io/onie/design-spec/" text="ONIE Design Specification">}}
- {{<exlink url="http://cumulusnetworks.com/downloads/" text="Cumulus Linux Downloads page">}}
- {{<exlink url="https://cumulusnetworks.com/cumulus-on-a-stick/" text="Cumulus on a Stick">}}
- {{<link url="Managing-Cumulus-Linux-Disk-Images" text="Managing Cumulus Linux Disk Images">}}
