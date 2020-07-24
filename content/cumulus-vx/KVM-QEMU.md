---
title: KVM-QEMU
author: Cumulus Networks
weight: 35
---
Performing virtualization in Linux requires three components:

- **Libvirt** provides an abstraction language to define a VM. It uses XML to represent and define the VM.
- **KVM** works exclusively with QEMU and performs hardware acceleration for x86 VMs with Intel and AMD CPUs. The pair is often called KVM/QEMU or just KVM.
- **QEMU** is a machine emulator that allows the host machine to emulate the CPU architecture of the guest machine. Because QEMU does not provide hardware acceleration, it works well with KVM.

This section describes how to install and set up Cumulus VX with KVM/QEMU and Libvirt on a Linux server to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with KVM/QEMU version ??? and Libvirt version 6.5.0 on Linux version ???.

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes a basic level of Linux and KVM experience.

1. Download the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus VX Qcow2 image for KVM">}}.

2. Run the following commands to install KVM/QEMU and Libvirt:

   ```
   local@host:~$ sudo apt update -y
   local@host:~$ sudo apt install -qy qemu ebtables dnsmasq-base qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virt-manager python3-pip
   local@host:~$ sudo apt install -qy libxslt-dev libxml2-dev libvirt-dev zlib1g-dev
   ```

5. Copy the `qcow2` image onto a Linux server three times to create the three VMs. Name them as follows:

   - leaf01.qcow2
   - leaf02.qcow2
   - spine01.qcow2

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

## Log into the Switches

{{% vx/login %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
