---
title: Vagrant and KVM-QEMU
author: Cumulus Networks
weight: 40
---
Running Cumulus VX with Vagrant and KVM requires four components:

- **KVM** works exclusively with QEMU and performs hardware acceleration for x86 VMs with Intel and AMD CPUs. KVM and QEMU are hypervisors that emulate the VMs; the pair is often called KVM/QEMU or just KVM.
- **QEMU** is a machine emulator that can allow the host machine to emulate the CPU architecture of the guest machine. Because QEMU does not provide hardware acceleration, it works well with KVM.
- **libvirt** provides an abstraction language to define and launch VMs, but is normally used just to launch single VMs. It uses XML to represent and define the VM.
- **Vagrant** is an orchestration tool that makes it easier to manage groups of VMs by interconnecting them programmatically. Vagrant helps to tie all the components together and provides a user-friendly language to launch suites of VMs. Vagrant allows multiple Cumulus VX VMs to be interconnected to simulate a network. Vagrant also allows Cumulus VX VMs to be interconnected with other VMs (such as Ubuntu or CentOS) to emulate real world networks.

This section describes how to install and set up Cumulus VX with KVM/QEMU, Libvirt, and Vagrant on a Linux server to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with KVM/QEMU version 1:4.2-3ubuntu6.3, Libvirt version 6.0.0, and Vagrant version 2.2.9 on Linux version 20.04.

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes a basic level of Linux, KVM, and Vagrant experience.

### Download and Install the Software

   You must install Vagrant **after** you install libvirt. Vagrant might not detect the necessary files if it is installed before libvirt.

1. Run the following commands to install KVM/QEMU and libvirt.

   ```
   apt update -y
   apt install -qy qemu ebtables dnsmasq-base qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virt-manager python3-pip
   apt install -qy libxslt-dev libxml2-dev libvirt-dev zlib1g-dev ruby-dev
   #apt-get build-dep ruby-libvirt

   ```

   ```
   user@ubuntubox:~$ sudo apt-get update -y
   user@ubuntubox:~$ sudo apt-get install libvirt-bin libvirt-dev qemu-utils qemu
   user@ubuntubox:~$ sudo /etc/init.d/libvirt-bin restart
   ```

2. Add your user to the libvirtd group so your user can perform `virsh` commands.

   ```
   user@ubuntubox:~$ sudo addgroup libvirtd
   user@ubuntubox:~$ sudo usermod -a -G libvirtd USERNAME
   ```

   To apply the new group to your existing user, log out, then log back in.

3. Install Vagrant:

   ```
   user@ubuntubox: wget https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb
   user@ubuntubox: dpkg -i vagrant_2.2.9_x86_64.deb
   ```

4. Install the necessary plugins for Vagrant:

   ```
   user@ubuntubox: vagrant plugin install vagrant-libvirt
   ```

5. Confirm that your Linux kernel and BIOS settings permit the use of KVM hardware acceleration.

   ```
   user@ubuntubox:~$ kvm-ok
   INFO: /dev/kvm exists
   KVM acceleration can be used
   ```
   
### Create VMs and Network Connections

{{% vx/vagrant-setup %}}

## Log into the Switches

{{% vx/login-vagrant %}}

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
