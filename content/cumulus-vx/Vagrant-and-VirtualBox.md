---
title: Vagrant and VirtualBox
author: Cumulus Networks
weight: 30
---
This document describes how to install and set up Cumulus VX within a Vagrant environment for each switch in the two-leaf and one spine topology shown below, using VirtualBox as the hypervisor.

{{% vx/intro %}}

These steps were tested with VirtualBox version 6.1.12 and Vagrant version 2.2.9 on macOS version 10.14.6.

## Create the VMs and the Network Connections

The following procedure creates leaf01, leaf02, and spine01 and the connections between them, as shown in the example topology. This section assumes a basic level of Vagrant, VirtualBox, and Linux experience.

1. Download and install VirtualBox. Refer to the {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox documentation">}}.

3. Download and install {{<exlink url="https://www.vagrantup.com/downloads.html" text="Vagrant">}}.

5. Create a folder to contain the Vagrant environment, then change directories into that folder.

   ```
   local@host:~$ mkdir vagrant
   local@host:~$ cd vagrant
   ```

6. Initialize the Vagrant environment to create a file called `Vagrantfile` in the folder you just created.

   ```
   local@host:~/vagrant$ vagrant init
   ```

7. Edit the `Vagrantfile` to create the VMs and the network connections. The following example creates leaf01, leaf02 and spine01, where the interfaces swp1 through swp3 are connected through separate private networks, as shown in the example topology above. Add this section at the end of the `Vagrantfile`.

   ```
   local@host:~/vagrant$ vi Vagrantfile

   Vagrant.configure("2") do |config|

   config.vm.define "leaf01" do |leaf01|
      leaf01.vm.box = "CumulusCommunity/cumulus-vx"

      # Internal network for swp* interfaces.
      leaf01.vm.network "private_network", virtualbox__intnet: "intnet-1", auto_config: false
      leaf01.vm.network "private_network", virtualbox__intnet: "intnet-3", auto_config: false
      leaf01.vm.network "private_network", virtualbox__intnet: "intnet-4", auto_config: false
   end

   config.vm.define "leaf02" do |leaf02|
      leaf02.vm.box = "CumulusCommunity/cumulus-vx"

      # Internal network for swp* interfaces.
      leaf02.vm.network "private_network", virtualbox__intnet: "intnet-2", auto_config: false
      leaf02.vm.network "private_network", virtualbox__intnet: "intnet-3", auto_config: false
      leaf02.vm.network "private_network", virtualbox__intnet: "intnet-4", auto_config: false
   end

   config.vm.define "spine01" do |spine01|
      spine01.vm.box = "CumulusCommunity/cumulus-vx"

      # Internal network for swp* interfaces.
      spine01.vm.network "private_network", virtualbox__intnet: "intnet-1", auto_config: false
      spine01.vm.network "private_network", virtualbox__intnet: "intnet-2", auto_config: false
   end

   end
   ```

   Cumulus VX images require at least 512MB. If performance issues exist, increase the amount of memory by setting the `v.memory` variable in the `Vagrantfile`. You can also adjust the memory size in the VirtualBox UI when the VM is powered off.

9. Run `vagrant up` to start the VMs:

   ```
   local@host:~/vagrant$ vagrant up
   ```

{{%notice note%}}

When using Vagrant with Cumulus VX:

- VirtualBox can support a maximum of 36 network interfaces.
- The first network interface (eth0) is always managed by Vagrant and must be connected to a NAT network.

{{%/notice%}}

## Log into the Switch

Log into each switch with the `vagrant ssh` command. For example:

```
local@host:~/vagrant$ vagrant ssh leaf01
```

To have permissions to run `cumulus` commands, run the `sudo su cumulus -` command. When prompted to change the password, enter the default cumulus user password `cumulus`, enter a new password, then confirm the password.

If you are using Cumulus VX 4.1.1 or earlier, the default password is `CumulusLinux!`. You are **not** prompted to change the default password.

## Basic Switch Configuration

{{% vx/basic-config %}}

## Next Steps

{{% vx/next-steps %}}
