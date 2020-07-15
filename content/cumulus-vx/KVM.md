---
title: KVM
author: Cumulus Networks
weight: 25
---
To use Cumulus VX with KVM, you need to perform the following configuration:

- Create the VMs
- Create connections between the VMs ???
- Test the connections
- Configure OSPF and FRRouting

Follow these steps to create a Cumulus VX VM with KVM on a Linux server. These sections assume a basic level of Linux and KVM experience. For detailed instructions, refer to the {{<exlink url="http://wiki.qemu.org/Main_Page" text="QEMU">}} and {{<exlink url="http://www.linux-kvm.org/page/Documents" text="KVM">}} documentation.

Performing virtualization in Linux requires three components:

- **Libvirt** provides an abstraction language to define a VM. It uses XML to represent and define the VM.
- **KVM** works exclusively with QEMU and performs hardware acceleration for x86 VMs with Intel and AMD CPUs. The pair is often called KVM/QEMU or just KVM.
- **QEMU** is a machine emulator that allows the host machine to emulate the CPU architecture of the guest machine. Because QEMU does not provide hardware acceleration, it works well with KVM.

## Create the VMs

1. Install QEMU/KVM. Refer to the {{<exlink url="http://www.qemu-project.org/download/" text="KVM documentation">}}  

2. Download Cumulus VX disk image for KVM from the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus Networks website">}}.

3. Run the following commands to install `libvirt:`

   ```
   local@host:~$ sudo add-apt-repository ppa:linuxsimba/libvirt-udp-tunnel
   local@host:~$ sudo apt-get update -y
   local@host:~$ sudo apt-get install libvirt-bin libvirt-dev qemu-utils qemu
   local@host:~$ sudo /etc/init.d/libvirt-bin restart
   ```

   The `linuxsimba`/`libvirt-udp-tunnel` package repository provides an updated `libvirtd` version that includes enhancements required to launch Cumulus VX. The example below shows the installation output:

   ```
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
   ```

4. After the installation process is complete, log out, then log back in to verify the `libvirt` version. In this guide, `libvirt` 1.2.16 was verified.

   ```
   local@host:~# libvirtd --version
   libvirtd (libvirt) 1.2.16
   ```

5. Copy the `qcow2` image onto a Linux server four times to create the four VMs. Name them as follows:

   - Leaf01.qcow2
   - Leaf02.qcow2
   - Spine01.qcow2

6. Power on each VX and configure each one as follows:

   {{< tabs "TabID01 ">}}

   {{< tab "leaf01.qcow2 ">}}

```
sudo /usr/bin/kvm   -curses                             \
                    -name leaf01                       \
                    -pidfile leaf01.pid                \
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
                    leaf01.qcow2
   ```

{{< /tab >}}

{{< tab "leaf02.qcow2 ">}}

```
sudo /usr/bin/kvm   -curses                             \
                    -name leaf02                       \
                    -pidfile leaf02.pid                \
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
                    leaf02.qcow2
```

{{< /tab >}}

{{< tab "spine01.qcow2 ">}}

```
sudo /usr/bin/kvm   -curses                             \
                    -name spine01                       \
                    -pidfile spine01.pid                \
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
                    spine01.qcow2
```

{{< /tab >}}

{{< /tabs >}}

The QEMU/KVM commands used here are minimal. You can add more parameters, such as `-enable-kvm`, `-serial` or `-monitor`, as needed.

{{%notice note%}}

If you intend to bridge the switch ports in the VM, place each switch port in the bridge in its own virtual network on the host. Otherwise, you might see this error:

```
br0: received package on swp1 with own address as source address
```

{{%/notice%}}

## Test Connections between VMs

{{% vx-test-connections %}}

## Configure OSPF and FRRouting

{{% vx-conf-routing %}}

## Next Steps
