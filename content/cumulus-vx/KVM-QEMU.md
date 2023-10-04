---
title: KVM-QEMU
author: NVIDIA
weight: 15
product: Cumulus VX
version: '5.x'
---
Performing virtualization in Linux requires three components:

{{% vx/kvm-components %}}

This section describes how to install and set up Cumulus VX with KVM/QEMU and Libvirt on a Linux server to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

<!-- vale off -->
These steps were tested with Cumulus VX 4.2, KVM/QEMU version 1:4.2-3ubuntu6.3, and Libvirt version 6.0.0 on Ubuntu Linux version 20.04.
<!-- vale on -->

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes you have Linux and KVM experience.

### Download and Install the Software

1. Download the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/cumulus-vx/" text="Cumulus VX Qcow2 image for KVM">}}.

2. Run the following commands to install KVM, QEMU and Libvirt:

   ```
   local@host:~$ sudo apt update -y
   local@host:~$ sudo apt install -qy qemu ebtables dnsmasq-base qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virt-manager python3-pip
   local@host:~$ sudo apt install -qy libxslt-dev libxml2-dev libvirt-dev zlib1g-dev
   ```

3. Confirm that your Linux kernel and BIOS settings permit the use of KVM hardware acceleration:

   ```
   local@host:~$ kvm-ok
   INFO: /dev/kvm exists
   KVM acceleration can be used
   ```

### Create the VMs and Network Connections

1. Copy the `qcow2` image onto a Linux server three times to create the three VMs. Name them as follows:

   - leaf01.qcow2
   - leaf02.qcow2
   - spine01.qcow2

2. Run the following commands to configure each VM. Make sure you specify the location of the VM at the end of the command. In the example commands below, you install the VMs in `/var/lib/libvirt/images/`.

{{%notice note%}}
The following commands define the CPU, memory, and disk requirements for Cumulus VX, which requires at least 768MB of RAM and 6GB of disk space.

CumulusVX versions 4.3 and later requires 2 vCPUs.
{{%/notice%}}

   {{< tabs "TabID01 ">}}

{{< tab "leaf01.qcow2 ">}}

```
local@host:~$ sudo /usr/bin/kvm -curses -vga virtio -name leaf01 -pidfile leaf01.pid -smp 2 -m 768 -net nic,macaddr=00:01:00:00:01:00,model=virtio -net user,net=192.168.0.0/24,hostfwd=tcp::1401-:22 -netdev socket,udp=127.0.0.1:1602,localaddr=127.0.0.1:1601,id=dev0 -device virtio-net-pci,mac=00:02:00:00:00:01,addr=6.0,multifunction=on,netdev=dev0,id=swp1 -netdev socket,udp=127.0.0.1:1606,localaddr=127.0.0.1:1605,id=dev1 -device virtio-net-pci,mac=00:02:00:00:00:02,addr=6.1,multifunction=off,netdev=dev1,id=swp2 -netdev socket,udp=127.0.0.1:1610,localaddr=127.0.0.1:1609,id=dev2 -device virtio-net-pci,mac=00:02:00:00:00:09,addr=6.2,multifunction=off,netdev=dev2,id=swp3 /var/lib/libvirt/images/leaf01.qcow2
```

{{< /tab >}}

{{< tab "leaf02.qcow2 ">}}

```
local@host:~$ sudo /usr/bin/kvm -curses -vga virtio -name leaf02 -pidfile leaf02.pid -smp 2 -m 768 -net nic,macaddr=00:01:00:00:02:00,model=virtio -net user,net=192.168.0.0/24,hostfwd=tcp::1402-:22 -netdev socket,udp=127.0.0.1:1604,localaddr=127.0.0.1:1603,id=dev0 -device virtio-net-pci,mac=00:02:00:00:00:03,addr=6.0,multifunction=on,netdev=dev0,id=swp1 -netdev socket,udp=127.0.0.1:1605,localaddr=127.0.0.1:1606,id=dev1 -device virtio-net-pci,mac=00:02:00:00:00:04,addr=6.1,multifunction=off,netdev=dev1,id=swp2 -netdev socket,udp=127.0.0.1:1609,localaddr=127.0.0.1:1610,id=dev2 -device virtio-net-pci,mac=00:02:00:00:00:10,addr=6.2,multifunction=off,netdev=dev2,id=swp3 /var/lib/libvirt/images/leaf02.qcow2
```

{{< /tab >}}

{{< tab "spine01.qcow2 ">}}

```
local@host:~$ sudo /usr/bin/kvm -curses -vga virtio -name spine01 -pidfile spine01.pid -smp 2 -m 768 -net nic,macaddr=00:01:00:00:03:00,model=virtio -net user,net=192.168.0.0/24,hostfwd=tcp::1403-:22 -netdev socket,udp=127.0.0.1:1601,localaddr=127.0.0.1:1602,id=dev0 -device virtio-net-pci,mac=00:02:00:00:00:05,addr=6.0,multifunction=on,netdev=dev0,id=swp1 -netdev socket,udp=127.0.0.1:1603,localaddr=127.0.0.1:1604,id=dev1 -device virtio-net-pci,mac=00:02:00:00:00:06,addr=6.1,multifunction=off,netdev=dev1,id=swp2 -netdev socket,udp=127.0.0.1:1609,localaddr=127.0.0.1:1610,id=dev2 -device virtio-net-pci,mac=00:02:00:00:00:11,addr=6.2,multifunction=off,netdev=dev2,id=swp3 /var/lib/libvirt/images/spine01.qcow2
```

{{< /tab >}}

{{< /tabs >}}

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
