---
title: Manage Network Operating System Images
author: Cumulus Networks
weight: 35
aliases:
 - /display/NETQ141/Manage+Network+Operating+System+Images
 - /pages/viewpage.action?pageId=10453545
pageID: 10453545
---
You can manage your network operating system (NOS) images with the NetQ
Image and Provisioning Management (IPM) application. On initial
installation, IPM points to the latest image of the Cumulus Linux
operating system and a default ONIE script. You can add additional NOS
images, add images, map switches to particular images, as well as view
the available images and their mappings.

## Command Overview

IPM enables you to add, delete, and view all of the DHCP configurations.
The command syntax is:

    tipctl add nos [-h|--help] MAC NOS
    tipctl del nos [-h|--help] mac MAC
    tipctl del nos [-h|--help] nos NOS 
    tipctl reset nos [-h|--help]
    tipctl show nos all [--with-date|-h|--help]
    tipctl show nos mac [--with-date|-h|--help] MAC
    tipctl show nos nos [--with-date|-h|--help] NOS

The *-h* option is a short cut for the *--help*
option. The *--with-date* option lists the timestamp when the
last mapping occurred.

## Import NOS Images

While IPM is preconfigured to use the latest Cumulus Linux NOS, you can
add prior NOS images to manage switches installed with earlier releases.
The NOS images are stored in the */var/tips/www/onie/images/* directory.

To import an image to the local repository:

1.  Log in to the NetQ Telemetry Server using your security credentials.

2.  Run the Easy Script to copy the image to the
    */var/tips/www/onie/images/* directory.

This example shows the import of a NOS image.

    <username>@<hostname>:~/Downloads$ ssh <username>@<telemetry-server-name-or-ip-address>
    <username>@<ts>:~$ tips-easy --images <path>/<image-filename>
    <username>@<ts>:~$ tipctl show nos

## View Stored Images

You can view all of the images stored in IPM using the `tipctl show nos`
command. You can filter the results by MAC address and NOS image.
Additionally, you can display the date at which mapping was performed.

This example shows all images in the directory.

    cumulus@ts:~$ tipctl show nos all
    Category   Match             Base
    ---------- ----------------- -------------------------------
    onie_mac   00:11:22:33:44:55 cumulus-rmp-3.6.1-bcm-amd64.bin
    onie_mac   70:72:cf:f5:5b:fe cumulus-linux-bcm-amd64.bin

This example shows only the images mapped to switches associated with a
MAC address of *70:72:cf:f5:5b:fe*.

    cumulus@ts:~$ tipctl show nos mac 70:72:cf:f5:5b:fe
    Category   Match             Base
    ---------- ----------------- -------------------------------
    onie_mac   70:72:cf:f5:5b:fe cumulus-linux-bcm-amd64.bin

This example shows only the images mapped to switches associated with a
NOS of *cumulus-rmp-3.6.1-bcm-amd64.bin*.

    cumulus@ts:~$ tipctl show nos mac 70:72:cf:f5:5b:fe
    Category   Match             Base
    ---------- ----------------- -------------------------------
    onie_mac   00:11:22:33:44:55 cumulus-rmp-3.6.1-bcm-amd64.bin

## Apply Images

Once you have all of the NOS images loaded into IPM, you can then map
the images to the various switches in your network using the `tipctl add
nos` command.

This example shows how to map a switch with MAC address of
*70:72:cf:f5:5b:fe* to the NOS image *cumulus-rmp-3.6.1-bcm-amd64.bin* ,
and then verify the mapping.

    cumulus@ts:~$ tipctl add nos 70:72:cf:f5:5b:fe cumulus-rmp-3.6.1-bcm-amd64.bin
    cumulus@ts:~$ tipctl show nos mac 70:72:cf:f5:5b:fe
    Category   Match             Base
    ---------- ----------------- -------------------------------
    onie_mac   00:11:22:33:44:55 cumulus-rmp-3.6.1-bcm-amd64.bin

If you want to add a NOS to multiple switches, create an automation
script that runs the `add nos` command.

## Manage Images

IPM enables you to manage your local image repository, including
mapping, deleting, and viewing images. Mapping images was covered above.
Viewing and deleting images are described here.

### View Images in Repository

You can view the NOS image repository located in the
*/var/tips/www/onie/images/* directory on the Telemetry Server.

This example shows how to view the contents of the NOS repository.

    cumulus@ts:~$ tipctl show repo nos
    NOS
    -------------------------------------------------------------------
    cumulus-linux-3.6.1-bcm-armel.bin
    cumulus-rmp-3.6.1-bcm-amd64.bin
    cumulus-linux-3.6.1-bcm-amd64.bin
    cumulus-linux-3.6.1-mlx-amd64.bin
    cumulus-linux-3.6.1-vx-amd64.bin
    cumulus-linux-3.6.1-vx-amd64.box
    cumulus-linux-3.6.1-vx-amd64-libvirt.box
    cumulus-linux-3.6.1-vx-amd64-1527285785.a89d37cz7d41081-libvirt.box
    cumulus-linux-3.6.1-vx-amd64.ova
    cumulus-linux-3.6.1-vx-amd64-vmware.ova
    cumulus-linux-3.6.1-vx-amd64-1527285785.a89d37cz7d41081-qa.qcow2
    cumulus-linux-3.6.1-vx-amd64.qcow2
    cumulus-linux-bcm-amd64.bin

### Remove Image Mappings

You can remove all mappings to a NOS image or the mapping to a
particular switch.This example shows how to remove the mapping of a NOS
image from all of your switches currently using this image, and then
verify that no switches are mapped to that NOS.

    cumulus@ts:~$ tipctl del nos nos <nos-filename>
    cumulus@ts:~$ tipctl show nos nos <nos-filename>

This example shows how to remove the mapping of a NOS image from a
switch with a MAC address of A0:00:00:00:00:12.

    cumulus@ts:~$ tipctl del nos mac a0:00:00:00:00:12
    cumulus@ts:~$ tipctl show nos mac a0:00:00:00:00:12

### Delete Images from Repository

If you are no longer using a particular NOS, you can remove it from your
local repository to simplify your management processes and prevent
mismatching of switches with incorrect NOS versions.This example shows
how to remove an image from your local repository.

    cumulus@<ts>:~$ cd ~/var/tips/www/onie/images/
    cumulus@<ts>:~/var/tips/www/onie/images/$ ls
    cumulus@<ts>:~/var/tips/www/onie/images/$ rm <image-filename> 

