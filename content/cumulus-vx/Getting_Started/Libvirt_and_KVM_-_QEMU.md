---
title: Libvirt and KVM - QEMU
author: Cumulus Networks
weight: 45
aliases:
 - /display/VX/Libvirt+and+KVM+-+QEMU
 - /pages/viewpage.action?pageId=5126704
pageID: 5126704
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
The following sections describe how to set up a two-leaf/two-spine
Cumulus VX topology with QEMU/KVM on a Linux server.

{{%notice note%}}

These sections assume a basic level of Linux and KVM experience. For
detailed instructions, refer to the
[QEMU](http://wiki.qemu.org/Main_Page) and
[KVM](http://www.linux-kvm.org/page/Documents) documentation.

{{%/notice%}}

## <span>Overview</span>

Performing virtualization in Linux requires three components:

  - **Libvirt** provides an abstraction language to define a VM. It uses
    XML to represent and define the VM.

  - **KVM** w <span style="color: #000000;"> orks exclusively with QEMU
    </span> <span style="color: #000000;"> and p </span> erforms
    hardware acceleration for x86 VMs with Intel and AMD CPUs.
    <span style="color: #000000;"> The pair is often called </span>
    <span style="color: #000000;"> KVM/QEMU </span>
    <span style="color: #000000;"> or just KVM. </span>

  - **QEMU** is a machine emulator that allows the host machine to
    emulate the CPU architecture of the guest machine. Because QEMU does
    not provide hardware acceleration, it works well with KVM.

## <span>Install libvirt</span>

1.  Review the Linux version of the host:
    
    {{%notice note%}}
    
    This guide is validated and verified for Ubuntu Trusty 14.04.5 LTS
    starting from a clean install.
    
    {{%/notice%}}
    
        local@host:~$ uname -a
        Linux ubuntu-trusty-64 3.13.0-93-generic #140-Ubuntu SMP Mon Jul 18 21:21:05 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

2.  Run the following commands to install `libvirt:`
    
        local@host:~$ sudo add-apt-repository ppa:linuxsimba/libvirt-udp-tunnel 
        local@host:~$ sudo apt-get update -y
        local@host:~$ sudo apt-get install libvirt-bin libvirt-dev qemu-utils qemu
        local@host:~$ sudo /etc/init.d/libvirt-bin restart
    
    {{%notice note%}}
    
    The `linuxsimba`/`libvirt-udp-tunnel` package repository provides an
    updated `libvirtd` version that includes enhancements required to
    launch Cumulus VX. The example below shows the installation output:
    
        local@host:~/$ sudo apt-get install libvirt-bin libvirt-dev qemu-utils qemu
        Reading package lists... Done
        Building dependency tree       
        Reading state information... Done
        tree is already the newest version.
        git is already the newest version.
        qemu-utils is already the newest version.
        qemu-utils set to manually installed.
        The following packages were automatically installed and are no longer required:
          bsdtar libarchive13 liblzo2-2 libnettle4 linux-headers-4.2.0-34
          linux-headers-4.2.0-34-generic linux-image-4.2.0-34-generic
          linux-image-extra-4.2.0-34-generic ruby-childprocess ruby-erubis ruby-ffi
          ruby-i18n ruby-log4r ruby-net-scp ruby-net-ssh
        Use 'apt-get autoremove' to remove them.
        The following extra packages will be installed:
          libvirt0 python-paramiko python-support qemu-system qemu-system-arm
          qemu-system-mips qemu-system-misc qemu-system-ppc qemu-system-sparc
          qemu-user sshpass
        Suggested packages:
          radvd lvm2 qemu-user-static samba vde2 openbios-ppc openhackware qemu-slof
        The following NEW packages will be installed:
          htop python-paramiko python-support qemu qemu-system qemu-system-arm
          qemu-system-mips qemu-system-misc qemu-system-ppc qemu-system-sparc
          qemu-user sshpass
        The following packages will be upgraded:
          ansible libvirt-bin libvirt-dev libvirt0
        4 upgraded, 12 newly installed, 0 to remove and 18 not upgraded.
        Need to get 31.1 MB of archives.
        After this operation, 166 MB of additional disk space will be used.
        Do you want to continue? [Y/n] Y
    
    {{%/notice%}}

3.  After the installation process is complete, log out, then log back
    in to verify the `libvirt` version.
    
    {{%notice note%}}
    
    In this guide, `libvirt` 1.2.16 was verified.
    
    {{%/notice%}}
    
        local@host:~# libvirtd --version
        libvirtd (libvirt) 1.2.16

## <span>Configure Cumulus VX VMs with QEMU/KVM</span>

{{%notice note%}}

This section assumes that you have installed QEMU/KVM and the Cumulus VX
disk image for KVM. For download locations and steps, refer to the
[Getting Started](/cumulus-vx/Getting_Started/) page.

{{%/notice%}}

{{%notice note%}}

This configuration is tested on a server running Debian 3.2.60-1+deb7u3
x86\_64 GNU/Linux with 3.2.0-4-amd64 \#1 SMP processors.

{{%/notice%}}

After you follow the steps below, the interfaces will be connected as
follows:

  - leaf1:swp1---\>spine1:swp1

  - leaf1:swp2---\>spine2:swp1

  - leaf2:swp1---\>spine1:swp2

  - leaf2:swp2---\>spine2:swp2

<!-- end list -->

1.  Copy the `qcow2` image onto a Linux server four times to create the
    four VMs, then name them as follows:
    
      - leaf1.qcow2
    
      - leaf2.qcow2
    
      - spine1.qcow2
    
      - spine2.qcow2

2.  Power on `leaf1.qcow2` and configure it as follows:
    
        sudo /usr/bin/kvm   -curses                             \
                            -name leaf1                       \
                            -pidfile leaf1.pid                \
                            -smp 1                              \
                            -m 256                              \
                            -net nic,vlan=10,macaddr=00:01:00:00:01:00,model=virtio \
                            -net user,vlan=10,net=192.168.0.0/24,hostfwd=tcp::1401-:22 \
                            -netdev socket,udp=127.0.0.1:1602,localaddr=127.0.0.1:1601,id=dev0 \
                            -device virtio-net-pci,mac=00:02:00:00:00:01,addr=6.0,multifunction=on,netdev=dev0,id=swp1 \
                            -netdev socket,udp=127.0.0.1:1606,localaddr=127.0.0.1:1605,id=dev1 \
                            -device virtio-net-pci,mac=00:02:00:00:00:02,addr=6.1,multifunction=off,netdev=dev1,id=swp2 \
                            -netdev socket,udp=127.0.0.1:1610,localaddr=127.0.0.1:1609,id=dev2 \
                            -device virtio-net-pci,mac=00:02:00:00:00:09,addr=6.2,multifunction=off,netdev=dev2,id=swp3 \
                            leaf1.qcow2

3.  Power on `leaf2.qcow2` and configure it as follows:
    
        sudo /usr/bin/kvm   -curses                             \
                            -name leaf2                       \
                            -pidfile leaf2.pid                \
                            -smp 1                              \
                            -m 256                              \
                            -net nic,vlan=10,macaddr=00:01:00:00:02:00,model=virtio \
                            -net user,vlan=10,net=192.168.0.0/24,hostfwd=tcp::1402-:22 \
                            -netdev socket,udp=127.0.0.1:1604,localaddr=127.0.0.1:1603,id=dev0 \
                            -device virtio-net-pci,mac=00:02:00:00:00:03,addr=6.0,multifunction=on,netdev=dev0,id=swp1 \
                            -netdev socket,udp=127.0.0.1:1608,localaddr=127.0.0.1:1607,id=dev1 \
                            -device virtio-net-pci,mac=00:02:00:00:00:04,addr=6.1,multifunction=off,netdev=dev1,id=swp2 \
                            -netdev socket,udp=127.0.0.1:1612,localaddr=127.0.0.1:1611,id=dev2 \
                            -device virtio-net-pci,mac=00:02:00:00:00:10,addr=6.2,multifunction=off,netdev=dev2,id=swp3 \
                            leaf2.qcow2

4.  Power on `spine1.qcow2` and configure it as follows:
    
        sudo /usr/bin/kvm   -curses                             \
                            -name spine1                       \
                            -pidfile spine1.pid                \
                            -smp 1                              \
                            -m 256                              \
                            -net nic,vlan=10,macaddr=00:01:00:00:03:00,model=virtio \
                            -net user,vlan=10,net=192.168.0.0/24,hostfwd=tcp::1403-:22 \
                            -netdev socket,udp=127.0.0.1:1601,localaddr=127.0.0.1:1602,id=dev0 \
                            -device virtio-net-pci,mac=00:02:00:00:00:05,addr=6.0,multifunction=on,netdev=dev0,id=swp1 \
                            -netdev socket,udp=127.0.0.1:1603,localaddr=127.0.0.1:1604,id=dev1 \
                            -device virtio-net-pci,mac=00:02:00:00:00:06,addr=6.1,multifunction=off,netdev=dev1,id=swp2 \
                            -netdev socket,udp=127.0.0.1:1609,localaddr=127.0.0.1:1610,id=dev2 \
                            -device virtio-net-pci,mac=00:02:00:00:00:11,addr=6.2,multifunction=off,netdev=dev2,id=swp3 \
                            spine1.qcow2

5.  Power on spine2 and configure it as follows:
    
        sudo /usr/bin/kvm   -curses                             \
                            -name spine2                       \
                            -pidfile spine2.pid                \
                            -smp 1                              \
                            -m 256                              \
                            -net nic,vlan=10,macaddr=00:01:00:00:04:00,model=virtio \
                            -net user,vlan=10,net=192.168.0.0/24,hostfwd=tcp::1404-:22 \
                            -netdev socket,udp=127.0.0.1:1605,localaddr=127.0.0.1:1606,id=dev0 \
                            -device virtio-net-pci,mac=00:02:00:00:00:07,addr=6.0,multifunction=on,netdev=dev0,id=swp1 \
                            -netdev socket,udp=127.0.0.1:1607,localaddr=127.0.0.1:1608,id=dev1 \
                            -device virtio-net-pci,mac=00:02:00:00:00:08,addr=6.1,multifunction=off,netdev=dev1,id=swp2 \
                            -netdev socket,udp=127.0.0.1:1611,localaddr=127.0.0.1:1612,id=dev2 \
                            -device virtio-net-pci,mac=00:02:00:00:00:12,addr=6.2,multifunction=off,netdev=dev2,id=swp3 \
                            spine2.qcow2
    
    {{%notice note%}}
    
    The QEMU/KVM commands used here are minimal. You can add more
    parameters, such as `-enable-kvm`, `-serial` or `-monitor`, as
    needed.
    
    {{%/notice%}}
    
    {{%notice note%}}
    
    **Bridging Switch Port Interfaces**
    
    If you intend to bridge the switch ports in the VM, place each
    switch port in the bridge in its own virtual network on the host.
    Otherwise, you might see this error:
    
        br0: received package on swp1 with own address as source address
    
    {{%/notice%}}

## <span>Next Steps</span>

{{%notice note%}}

This section assumes that you are configuring a two-leaf/two-spine
network topology, that you have completed the steps in [Create a Cumulus
VX Virtual Machine with VMware vSphere - ESXi
5.5](VMware_vSphere_-_ESXi_5.5.html#src-5126689_VMwarevSphere-ESXi5.5-CreateaCumulusVXVirtualMachinewithVMwarevSphere-ESXi5.5)
above, and that you now have a VM called `CumulusVX-leaf1`.

{{%/notice%}}

After you create all four VMs, follow the steps in [Create a Two-Leaf,
Two-Spine Topology](/cumulus-vx/Create_a_Two-Leaf_Two-Spine_Topology) to
configure the network interfaces and routing.
