---
title: Vagrant and VirtualBox
author: Cumulus Networks
weight: 30
---
This section describes how to install and set up Cumulus VX within Vagrant and VirtualBox to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

These steps were tested with VirtualBox version 6.1.12 and Vagrant version 2.2.9 on macOS version 10.14.6.

## Create VMs and Network Connections

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes a basic level of Vagrant, VirtualBox, and Linux experience.

1. Download and install {{<exlink url="https://www.virtualbox.org/wiki/Downloads" text="VirtualBox">}}.

2. Download and install {{<exlink url="https://www.vagrantup.com/downloads.html" text="Vagrant">}}.

3. Create a folder to contain the Vagrant environment, then change directories into that folder.

   ```
   local@host:~$ mkdir vagrant
   local@host:~$ cd vagrant
   ```

4. Initialize the Vagrant environment to create a file called `Vagrantfile` in the folder you just created.

   ```
   local@host:~/vagrant$ vagrant init
   A `Vagrantfile` has been placed in this directory. You are now
   ready to `vagrant up` your first virtual environment! Please read
   the comments in the Vagrantfile as well as documentation on
   `vagrantup.com` for more information on using Vagrant.
   ```

5. Edit the `Vagrantfile`. Add the following section under `Vagrant.configure("2") do |config|` to create leaf01, leaf02 and spine01, and the network connections between them.

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
   ```

6. Run `vagrant up` to start the VMs:

   ```
   local@host:~/vagrant$ vagrant up
   Bringing machine 'leaf01' up with 'virtualbox' provider...
   Bringing machine 'leaf02' up with 'virtualbox' provider...
   Bringing machine 'spine01' up with 'virtualbox' provider...
   ...
   ```

{{%notice note%}}

When using Vagrant with Cumulus VX:

- VirtualBox can support a maximum of 36 network interfaces.
- The first network interface (eth0) is always managed by Vagrant and must be connected to a NAT network.

{{%/notice%}}

## Log into the Switches

1. Log into each switch with the `vagrant ssh` command. For example:

   ```
   local@host:~/vagrant$ vagrant ssh leaf01
   ```

2. Configure each switch to be able to run NCLU commands without `sudo`:

   ```
   cumulus@cumulus:mgmt:~$ sudo usermod -a -G netedit vagrant
   ```

## Basic Switch Configuration

{{% vx/basic-config %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
