---
title: Vagrant and Libvirt with KVM or QEMU
author: Cumulus Networks
weight: 61
aliases:
 - /display/VX/Vagrant+and+Libvirt+with+KVM+or+QEMU
 - /pages/viewpage.action?pageId=5126718
pageID: 5126718
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
The solution described in this chapter requires four components:

  - **libvirt** provides an abstraction language to define and launch
    VMs, but is normally used just to launch single VMs. It uses XML to
    represent and define the VM.

  - **KVM** w <span style="color: #000000;"> orks exclusively with QEMU
    and </span> <span style="color: #000000;"> p </span> erforms
    hardware acceleration for x86 VMs with Intel and AMD CPUs. KVM and
    QEMU are hypervisors that emulate the VMs; t
    <span style="color: #000000;"> he pair is often called KVM/QEMU or
    just KVM. </span>

  - **QEMU** is a machine emulator that can allow the host machine to
    emulate the CPU architecture of the guest machine. Because QEMU does
    not provide hardware acceleration, it works well with KVM.

  - **Vagrant** is an orchestration tool that makes it easier to manage
    groups of VMs by interconnecting them programmatically. Vagrant
    helps to tie all the components together and provides a
    user-friendly language to launch suites of VMs. Vagrant allows
    multiple Cumulus VX VMs to be interconnected to simulate a network.
    Vagrant also allows Cumulus VX VMs to be interconnected with other
    VMs (such as Ubuntu or CentOS) to emulate real world networks.

{{% imgOld 0 %}}

The following sections describe how to install `libvirt`, KVM/QEMU, and
Vagrant on a Linux server.

## <span>Install libvirt</span>

1.  Check the Linux version of the host. This guide is validated and
    verified for Ubuntu 16.04 LTS starting from a clean install:
    
        user@ubuntubox:~$ lsb_release -a
        No LSB modules are available.
        Distributor ID: Ubuntu
        Description:    Ubuntu 16.04 LTS
        Release:    16.04
        Codename:   xenial
    
        user@ubuntubox:~$ uname -a
        Linux ubuntubox 4.4.0-22-generic #40-Ubuntu SMP Thu May 12 22:03:46 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
    
    After verifying the version, install `libvirt` and `QEMU`. The
    following commands install the necessary components to get `libvirt`
    and `QEMU` operational.
    
        user@ubuntubox:~$ sudo apt-get update -y
        user@ubuntubox:~$ sudo apt-get install libvirt-bin libvirt-dev qemu-utils qemu
        user@ubuntubox:~$ sudo /etc/init.d/libvirt-bin restart
    
    Click here if running Ubuntu 14.04...
    
    The version of `libvirt` which ships in Ubuntu 14.04 is too old to
    be used in many of the simulations built by Cumulus.
    
    The `linuxsimba`/`libvirt-udp-tunnel` package repository provides an
    updated `libvirtd` version that provides enhancements required to
    launch Cumulus VX. The example below shows how to add the
    repository:
    
        user@ubuntubox:~$ sudo add-apt-repository ppa:linuxsimba/libvirt-udp-tunnel 
    
    This repository contains a version of `libvirt` that has the
    necessary patches to support the construction of UDP tunnels, which
    are used for the point-to-point links in a VM simulation.
    
    This version of `libvirt` needs to have a default storage pool
    created using the process below.
    
        user@ubuntubox:~$ sudo virsh pool-define-as --name default --type dir --target /var/lib/libvirt/images
        user@ubuntubox:~$ sudo virsh pool-autostart default
        user@ubuntubox:~$ sudo virsh pool-build default
        user@ubuntubox:~$ sudo virsh pool-start default

2.  After the installation completes, log out, then log in and verify
    the `libvirt` version.
    
        user@ubuntubox:~$ libvirtd --version
        libvirtd (libvirt) 1.3.1
    
    {{%notice note%}}
    
    <span style="color: #222222;"> `libvirt` versions 1.2.20 or higher
    have native support for the UDP tunnels, which are used for the
    point-to-point links in VM simulation. </span>
    
    {{%/notice%}}

3.  Add your user to the `libvirtd` group (if not already present) so
    your user can perform `virsh` commands.
    
        user@ubuntubox:~$ sudo addgroup libvirtd
        user@ubuntubox:~$ sudo usermod -a -G libvirtd USERNAME
    
    {{%notice note%}}
    
    To apply the new group to your existing user, log out and in again.
    
    {{%/notice%}}

4.  Confirm that your Linux kernel and BIOS settings permit the use of
    KVM hardware acceleration.
    
        user@ubuntubox:~$ kvm-ok
        INFO: /dev/kvm exists
        KVM acceleration can be used

After completing these steps, `libvirt` and KVM/QEMU are installed. The
Linux server is now ready to run VMs.

## <span>Install Vagrant</span>

You must install Vagrant **after** you install `libvirt`. Vagrant might
not properly detect the necessary files if it is installed before
`libvirt`. Cumulus VX requires version 1.7 or later. Version 2.0.2 or
later is recommended.

1.  Install Vagrant from the `deb` package. Cumulus Networks cannot
    guarantee the functionality of any version of Vagrant. In this
    guide, Vagrant version 2.0.2 is used.
    
        user@ubuntubox:~$ wget https://releases.hashicorp.com/vagrant/2.0.2/vagrant_2.0.2_x86_64.deb
        --2018-05-04 09:36:22--  https://releases.hashicorp.com/vagrant/2.0.2/vagrant_2.0.2_x86_64.deb
        Resolving releases.hashicorp.com (releases.hashicorp.com)... 151.101.57.183, 2a04:4e42:e::439
        Connecting to releases.hashicorp.com (releases.hashicorp.com)|151.101.57.183|:443... connected.
        HTTP request sent, awaiting response... 200 OK
        Length: 43678320 (42M) [application/x-debian-package]
        Saving to: ‘vagrant_2.0.2_x86_64.deb’
        vagrant_2.0.2_x86_6 100%[===================>]  41.65M  33.1MB/s    in 1.3s    
        2018-05-04 09:36:23 (33.1 MB/s) - ‘vagrant_2.0.2_x86_64.deb’ saved [43678320/43678320]

2.  Install Vagrant using `dpkg`:
    
        user@ubuntubox:~$ sudo dpkg -i vagrant_2.0.2_x86_64.deb 
        Selecting previously unselected package vagrant.
        (Reading database ... 387062 files and directories currently installed.)
        Preparing to unpack vagrant_2.0.2_x86_64.deb ...
        Unpacking vagrant (1:2.0.2) ...
        Setting up vagrant (1:2.0.2) ...

3.  Verify the Vagrant version:
    
        user@ubuntubox:~$ vagrant --version
        Vagrant 2.0.2

4.  Install the necessary plugins for Vagrant:
    
        user@ubuntubox# vagrant plugin install vagrant-libvirt
        Installing the 'vagrant-libvirt' plugin. This can take a few minutes...
        Installed the plugin 'vagrant-libvirt (0.0.43)'!
         
        user@ubuntubox# vagrant plugin install vagrant-mutate
        Installing the 'vagrant-mutate' plugin. This can take a few minutes...
        Installed the plugin 'vagrant-mutate (1.2.0)'!
    
    {{%notice note%}}
    
    Vagrant plugin installation is unique to each user; make sure to
    install plugins as the user who will run the simulations.
    
    {{%/notice%}}

5.  Install the CumulusCommunity/cumulus-vx box image:
    
        vagrant box add CumulusCommunity/cumulus-vx --provider=libvirt
    
    {{%notice note%}}
    
    Vagrant box image installation is unique to each user; make sure to
    install images as the user who will run the simulations.
    
    {{%/notice%}}

6.  Test that everything is working:
    
        user@ubuntubox:~$ mkdir ./testdir ; cd ./testdir
        user@ubuntubox:~/testdir$ vagrant init CumulusCommunity/cumulus-vx
         
        A `Vagrantfile` has been placed in this directory. You are now ready to `vagrant up` your first virtual environment! Please readthe comments in the Vagrantfile as well as documentation on`vagrantup.com` for more information on using Vagrant.
         
        user@ubuntubox:~/testdir$ vagrant up --provider=libvirt
        <...snip...>
        user@ubuntubox:~/testdir$ vagrant status
        Current machine states:
                default running (libvirt)

7.  <span style="color: #222222;"> To show all running KVM/`libvirt`
    VMs:  
    </span>
    
        user@ubuntubox:~/testdir$ virsh list --all 
         
        Id    Name                           State 
        ---------------------------------------------------- 
        2     test_default                   running 
         
        #Look at libvirt's XML definition of the VM used to create the VM:
        user@ubuntubox:~/testdir$ virsh dumpxml [name of domain]

8.  The `libvirt` domain is running. To stop this machine, you can run
    `vagrant halt`. To destroy the machine, you can run `vagrant
    destroy.`
    
        user@ubuntubox:~/testdir$ vagrant destroy -f

After completing these steps, Vagrant is now set up.

## <span>Create the Vagrantfile and Launch KVM Instances</span>

1.  Create the desired Vagrantfile using the Cumulus [topology
    converter](https://github.com/CumulusNetworks/topology_converter) or
    by downloading the Cumulus-created
    [cldemo-vagrant](https://github.com/CumulusNetworks/cldemo-vagrant)
    reference topology. The following steps use the cldemo-vagrant
    topology.
    
    If you plan on simulating Cumulus VX 2.5.x read this note...
    
    Make sure your Vagrantfiles do not attempt to set the hostname of
    the VM as that is not supported for older versions of Cumulus VX. If
    you see a `device.vm.name` line as in the following example, remove
    it:
    
        user@ubuntubox:~$ sudo vi Vagrantfile
         
        ... 
         
        device.vm.hostname = "leaf01"
         
        ...
    
        user@ubuntubox:~$ git clone https://github.com/CumulusNetworks/cldemo-vagrant.git
        Cloning into 'cldemo-vagrant'...
        remote: Counting objects: 1015, done.
        remote: Compressing objects: 100% (23/23), done.
        remote: Total 1015 (delta 4), reused 11 (delta 1), pack-reused 991
        Receiving objects: 100% (1015/1015), 1.83 MiB | 1.00 MiB/s, done.
        Resolving deltas: 100% (557/557), done.
        Checking connectivity... done.

2.  After the repo is cloned, change to its directory:
    
        user@ubuntubox:~$ cd cldemo-vagrant/
        user@ubuntubox:~/cldemo-vagrant$

3.  Copy the Vagrantfile-KVM into place.
    
        user@ubuntubox:~/cldemo-vagrant$ cp ./Vagrantfile-kvm ./Vagrantfile
        user@ubuntubox:~/cldemo-vagrant$

4.  Check the status of the VMs to see that none of them have been
    created yet:
    
        user@ubuntubox:~/cldemo-vagrant$ vagrant status
        Current machine states:
        oob-mgmt-server           not created (libvirt)
        oob-mgmt-switch           not created (libvirt)
        exit02                    not created (libvirt)
        exit01                    not created (libvirt)
        spine02                   not created (libvirt)
        spine01                   not created (libvirt)
        leaf04                    not created (libvirt)
        leaf02                    not created (libvirt)
        leaf03                    not created (libvirt)
        leaf01                    not created (libvirt)
        edge01                    not created (libvirt)
        server01                  not created (libvirt)
        server03                  not created (libvirt)
        server02                  not created (libvirt)
        server04                  not created (libvirt)
        internet                  not created (libvirt)
        This environment represents multiple VMs. The VMs are all listed
        above with their current state. For more information about a specific
        VM, run `vagrant status NAME`.
    
    {{%notice note%}}
    
    All Vagrant commands performed against a simulation such as `vagrant
    up` or `vagrant destroy` must be issued from the directory that
    contains the Vagrantfile.
    
    {{%/notice%}}

5.  Bring up all the images using `--provider libvirt:`
    
        user@ubuntubox:~/cldemo-vagrant$ vagrant up --provider=libvirt
        Bringing machine 'oob-mgmt-server' up with 'libvirt' provider...
        Bringing machine 'oob-mgmt-switch' up with 'libvirt' provider...
        Bringing machine 'exit02' up with 'libvirt' provider...
        Bringing machine 'exit01' up with 'libvirt' provider...
        Bringing machine 'spine02' up with 'libvirt' provider...
        Bringing machine 'spine01' up with 'libvirt' provider...
        Bringing machine 'leaf04' up with 'libvirt' provider...
        Bringing machine 'leaf02' up with 'libvirt' provider...
        Bringing machine 'leaf03' up with 'libvirt' provider...
        Bringing machine 'leaf01' up with 'libvirt' provider...
        Bringing machine 'edge01' up with 'libvirt' provider...
        Bringing machine 'server01' up with 'libvirt' provider...
        Bringing machine 'server03' up with 'libvirt' provider...
        Bringing machine 'server02' up with 'libvirt' provider...
        Bringing machine 'server04' up with 'libvirt' provider...
        Bringing machine 'internet' up with 'libvirt' provider...

6.  After following all the steps above, the VMs are created and
    accessible. Issue the following command to access the out-of-band
    management server VM:
    
        user@ubuntubox:~/cldemo-vagrant$ vagrant ssh oob-mgmt-server
                                                         _
              _______   x x x                           | |
         ._  <_______~ x X x   ___ _   _ _ __ ___  _   _| |_   _ ___
        (' \  ,' || `,        / __| | | | '_ ` _ \| | | | | | | / __|
         `._:^   ||   :>     | (__| |_| | | | | | | |_| | | |_| \__ \
             ^T~~~~~~T'       \___|\__,_|_| |_| |_|\__,_|_|\__,_|___/
             ~"     ~"
         
        ############################################################################
        #
        #                     Out Of Band Management Station
        #
        ############################################################################
        cumulus@oob-mgmt-server:~$ 

7.  Experiment with your simulation.

8.  Explore the various demos available as part of the cldemo-vagrant
    family of repositories located here:
    <https://github.com/CumulusNetworks/cldemo-vagrant#available-demos>

9.  Destroy the simulation when finished.
    
        user@ubuntubox:~/cldemo-vagrant$ vagrant destroy -f

<span style="color: #222222;">  
</span>
