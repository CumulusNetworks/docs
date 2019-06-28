---
title: Vagrant and VirtualBox
author: Cumulus Networks
weight: 59
aliases:
 - /display/VX/Vagrant+and+VirtualBox
 - /pages/viewpage.action?pageId=5126719
pageID: 5126719
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
This document describes how to install and set up Cumulus Linux within a
Vagrant environment, using VirtualBox as the hypervisor.

{{%notice note%}}

These sections assume a basic level of Vagrant, VirtualBox, and Linux
experience. For detailed instructions, refer to the [Vagrant
documentation](https://www.vagrantup.com/docs/) and the [getting started
guide](https://www.vagrantup.com/intro/getting-started/index.html).

{{%/notice%}}

## <span>Configure the Vagrant Environment</span>

{{%notice note%}}

This section assumes that you have installed the VirtualBox hypervisor.
For detailed instructions, refer to the
[VirtualBox](/cumulus-vx/Getting_Started/VirtualBox) installation
section.

{{%/notice%}}

{{%notice note%}}

Cumulus VX requires Vagrant version 1.7 or later. The installation steps
below use Vagrant version 1.9.4 for the example commands.

{{%/notice%}}

To set up the Vagrant environment:

1.  Download and install Vagrant: [Vagrant
    Downloads](https://www.vagrantup.com/downloads.html).

2.  In a terminal, add the Cumulus VX Vagrant box image. Ensure option
    `2` is specified.
    
    {{%notice note%}}
    
    Vagrant downloads and installs the latest Cumulus VX VirtualBox
    image.
    
    {{%/notice%}}
    
        local@host:~$ vagrant box add cumuluscommunity/cumulus-vx
        ==> box: Loading metadata for box 'cumuluscommunity/cumulus-vx'
        box: URL: https://atlas.hashicorp.com/cumuluscommunity/cumulus-vx
        This box can work with multiple providers! The providers that it
        can work with are listed below. Please review the list and choose
        the provider you will be working with.
        1) libvirt
        2) virtualbox
        Enter your choice: 2
        ==> box: Adding box 'CumulusCommunity/cumulus-vx' (v3.3.0) for provider: virtual box
         
        ...

{{%notice note%}}

Cumulus Networks provides several preconfigured demos to run with
Vagrant using Ansible to configure the VMs. To run these demos, download
and install [Ansible 1.7 or
newer](https://pypi.python.org/pypi/ansible).

{{%/notice%}}

## <span>Configure a Cumulus VX VM with Vagrant</span>

1.  In a terminal, create a folder to contain the Vagrant environment,
    then change directories into that folder.
    
        local@host:~$ mkdir vagrant
        local@host:~$ cd vagrant

2.  Initialize the Vagrant environment so you can provision your VMs.
    This creates a file called `Vagrantfile` within the folder you just
    created.
    
        local@host:~/vagrant$ vagrant init

3.  Configure Vagrant to spin up a Cumulus VX VM. Modify the newly
    created `Vagrantfile` to configure the VMs, then save the file:
    
        local@host:~/vagrant$ sudo vi Vagrantfile 
         
        Vagrant.configure(2) do |config|
          config.vm.box = "CumulusCommunity/cumulus-vx"
        end
    
    {{%notice note%}}
    
    Cumulus VX 3.y.z images require at least 512MB to be fully
    functional. The default Vagrant memory size is 512MB. If performance
    issues exist, increase the amount of memory by setting the
    `v.memory` variable in the `Vagrantfile` to *512* or more. You can
    also adjust the memory size in the VirtualBox UI when the VM is
    powered off.
    
    {{%/notice%}}

4.  Run `vagrant up` to start the VM:
    
        local@host:~/vagrant$ vagrant up
        Bringing machine 'default' up with 'virtualbox' provider...
        ==> default: Importing base box 'cumulus-vx-3.3.0'...
        ==> default: Matching MAC address for NAT networking...
        ==> default: Setting the name of the VM: temp_default_1437562573479_23184
        ==> default: Clearing any previously set network interfaces...
        ==> default: Preparing network interfaces based on configuration...
            default: Adapter 1: nat
        ==> default: Forwarding ports...
            default: 22 => 2222 (adapter 1)
        ==> default: Booting VM...
        ==> default: Waiting for machine to boot. This may take a few minutes...
            default: SSH address: 127.0.0.1:2222
            default: SSH username: vagrant
            default: SSH auth method: private key
            default: Warning: Connection timeout. Retrying...
            default:
            default: Vagrant insecure key detected. Vagrant will automatically replace
            default: this with a newly generated keypair for better security.
            default:
            default: Inserting generated public key within guest...
            default: Removing insecure key from the guest if it's present...
            default: Key inserted! Disconnecting and reconnecting using new SSH key...
        ==> default: Machine booted and ready!
        ==> default: Checking for guest additions in VM...
        ==> default: Mounting shared folders...
            default: /vagrant => /Users/cumulus/vx-example

After you start a VM, you can log in using the `ssh` option:

    local@host:~/vagrant$ vagrant ssh

The `vagrant ssh` command logs in as the preconfigured `vagrant` user. A
shared file system is automatically mounted inside the VM under the
`/vagrant` mount point; you can transfer files between the host and
Cumulus VX instance from there.

To shut down the VM, use the `destroy` command:

    local@host:~/vagrant$ vagrant destroy

For more information on configuring VMs with Vagrant, see
[docs.vagrantup.com/v2/](https://docs.vagrantup.com/v2/).

You can explore the various demos available as part of the
cldemo-vagrant family of repositories located here:
<https://github.com/CumulusNetworks/cldemo-vagrant#available-demos>.

## <span>Additional Configuration Options</span>

### <span>Add Switch Port Interfaces to a Cumulus VX VM</span>

By default Vagrant only configures the first network interface (eth0)
for its own use. You must configure additional network interfaces, such
as the Cumulus Linux switch port interfaces, in the `Vagrantfile`.
Normally, you configure these interfaces to use a private network. By
default, Vagrant provides one preconfigured private network, although
you can choose to create additional private networks. You can connect
one or more network interfaces to a private network.

The following example creates a Cumulus VX VM where the interfaces swp1
through swp4 are created and connected to the preconfigured private
network:

    Vagrant.configure(2) do |config|
      config.vm.box = "CumulusCommunity/cumulus-vx"
     
      config.vm.network "private_network", virtualbox__intnet: "swp1", auto_config: false
      config.vm.network "private_network", virtualbox__intnet: "swp2", auto_config: false
      config.vm.network "private_network", virtualbox__intnet: "swp3", auto_config: false
      config.vm.network "private_network", virtualbox__intnet: "swp4", auto_config: false
    end

For more information on creating and using private networks, see
[docs.vagrantup.com/v2/networking/private\_network.html](https://docs.vagrantup.com/v2/networking/private_network.html)
and
[docs.vagrantup.com/v2/virtualbox/networking.html](https://docs.vagrantup.com/v2/virtualbox/networking.html).

### <span>Create Multiple Cumulus VX VMs</span>

Vagrant can create and configure multiple VMs with a single command. For
example, you can use Vagrant to create multiple Cumulus VX VMs and then
connect the network interfaces of those VMs together.

The following example creates two Cumulus VX VMs, leaf1 and leaf2, where
the interfaces swp1 through swp4 are connected together via separate
private networks:

    Vagrant.configure(2) do |config|
     
      config.vm.define "leaf1" do |leaf1|
        leaf1.vm.box = "CumulusCommunity/cumulus-vx"
     
        # Internal network for swp* interfaces.
        leaf1.vm.network "private_network", virtualbox__intnet: "swp1", auto_config: false
        leaf1.vm.network "private_network", virtualbox__intnet: "swp2", auto_config: false
        leaf1.vm.network "private_network", virtualbox__intnet: "swp3", auto_config: false
        leaf1.vm.network "private_network", virtualbox__intnet: "swp4", auto_config: false
      end
     
      config.vm.define "leaf2" do |leaf2|
        leaf2.vm.box = "CumulusCommunity/cumulus-vx"
     
        # Internal network for swp* interfaces.
        leaf2.vm.network "private_network", virtualbox__intnet: "swp1", auto_config: false
        leaf2.vm.network "private_network", virtualbox__intnet: "swp2", auto_config: false
        leaf2.vm.network "private_network", virtualbox__intnet: "swp3", auto_config: false
        leaf2.vm.network "private_network", virtualbox__intnet: "swp4", auto_config: false
      end
     
    end

When you run `vagrant up`, both VMs are created. You can log in to each
VM and configure the interfaces as you want; the interfaces will pass
traffic between themselves as if they are two physical switches
connected together by four cables.

## <span>Limitations</span>

At this time, there are some limitations to using Vagrant with Cumulus
VX:

  - VirtualBox can only support a maximum of 36 network interfaces.

  - The first network interface (eth0) is always managed by Vagrant and
    must be connected to a NAT network.

## <span>Test Configuration</span>

Cumulus VX for Vagrant has been tested in the following environments:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Host OS</p></th>
<th><p>Vagrant Version(s)</p></th>
<th><p>VirtualBox Version(s)</p></th>
<th><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>OS X 10.10</p></td>
<td><p>1.7.3<br />
1.7.4</p></td>
<td><p>4.3<br />
5.0</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>Ubuntu 14.04</p></td>
<td><p>1.7.4</p></td>
<td><p>4.3</p></td>
<td><p> </p></td>
</tr>
<tr class="odd">
<td><p>Ubuntu 16.04</p></td>
<td><p>1.8.5<br />
1.8.6<br />
1.8.7<br />
1.9.1</p></td>
<td><p>5.0.26</p></td>
<td><p> </p></td>
</tr>
<tr class="even">
<td><p>Windows 7</p></td>
<td><p>1.7.3</p></td>
<td><p>5.0</p></td>
<td><p>While both VirtualBox and Vagrant are fully supported on Windows hosts, Vagrant provisioning with Ansible is not.<br />
Cumulus VX demos that use Ansible do not work on Windows.</p></td>
</tr>
</tbody>
</table>
