---
title: Using Cumulus VX with Vagrant
author: Cumulus Networks
weight: 17
aliases:
 - /display/VX25/Using+Cumulus+VX+with+Vagrant
 - /pages/viewpage.action?pageId=5115405
pageID: 5115405
product: Cumulus VX
version: '2.5'
imgData: cumulus-vx-25
siteSlug: cumulus-vx-25
---
## <span>Requirements</span>

  - Cumulus VX requires [Vagrant 1.7 or
    newer](https://www.vagrantup.com/downloads.html)

  - Understand these [VirtualBox
    considerations](Using_Cumulus_VX_with_VirtualBox.html#src-5115389_UsingCumulusVXwithVirtualBox-reqs)

## <span>Setting Up the Vagrant Environment</span>

You can use Cumulus VX within a Vagrant environment, running the VMs
with VirtualBox. To get started you need to download some software as
well as the Cumulus VX Vagrant box. You can download all of the source
code used to build Cumulus VX for Vagrant, the `vagrant-cumulus` plugin
and the pre-configured demos from [the Cumulus Networks public Github
repository](https://github.com/CumulusNetworks/cumulus-vx-vagrant).

1.  Download and install
    [VirtualBox](https://www.virtualbox.org/wiki/Downloads).

2.  Download and install
    [Vagrant](https://www.vagrantup.com/downloads.html).

3.  Download the [Cumulus VX box file for
    Vagrant](https://cumulusnetworks.com/cumulus-vx/download/).

4.  Install the Cumulus Linux plugin for Vagrant:
    
        $ vagrant plugin install vagrant-cumulus
        Installing the 'vagrant-cumulus' plugin. This can take a few minutes...
        Installed the plugin 'vagrant-cumulus (0.1)'!

5.  Download and add the Cumulus VX Vagrant box file. Include the full
    path to the Box file:
    
        $ vagrant box add cumulus-vx-2.5.3 /Users/cumulus/Desktop/vagrant/CumulusVX-2.5.3-4eb681f3df86c478.box      ✘
        ==> box: Box file was not detected as metadata. Adding it directly...
        ==> box: Adding box 'cumulus-vx-2.5.3' (v0) for provider:
            box: Unpacking necessary files from: file:///Users/cumulus/Desktop/vagrant/CumulusVX-2.5.3-4eb681f3df86c478.box

6.  If you'd like to try any of the preconfigured demos you should also
    install [Ansible 1.7 or
    newer](https://pypi.python.org/pypi/ansible), which Vagrant uses to
    configure the virtual machines.

## <span>Configuring a Cumulus VX Virtual Machine with Vagrant</span>

Vagrant uses a configuration file (`Vagrantfile`) to create and
configure one or more virtual machines. Create a `Vagrantfile` with the
following configuration:

    Vagrant.configure(2) do |config|
      config.vm.box = "cumulus-vx-2.5.3"
    end

Save this file and run `vagrant up` to start a Cumulus VX virtual
machine:

    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Importing base box 'cumulus-vx-2.5.3'...
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

### <span>Logging in to the VM</span>

Once you create the virtual machine, log in to it using:

    vagrant ssh

This automatically logs you in as the pre-configured `vagrant` user. A
shared filesystem is automatically mounted inside the virtual machine
under the `/vagrant` mount point; you can transfer files between the
host and Cumulus VX from here.

When you are finished with the virtual machine, you can shut it down by
running:

    vagrant destroy

You can find all the documentation for configuring virtual machines with
Vagrant at [docs.vagrantup.com/v2/](https://docs.vagrantup.com/v2/).

### <span>Adding Switch Port Interfaces to a Cumulus VX Virtual Machine</span>

By default Vagrant only configures the first network interface (eth0)
for its own use. Additional network interfaces, such as the Cumulus
Linux switch port interfaces, must be configured in the Vagrantfile.
Normally you should configure these interfaces to use a private network.
By default Vagrant provides one pre-configured private network, although
you can choose to create additional private networks if you wish. You
can connect one or more network interfaces to a private network.

The following example creates a Cumulus VX virtual machine where the
interfaces swp1 through swp4 are created and connected to the
pre-configured private network:

    Vagrant.configure(2) do |config|
      config.vm.box = "cumulus-vx-2.5.3"
     
      config.vm.network "private_network", virtualbox__intnet: true # swp1
      config.vm.network "private_network", virtualbox__intnet: true # swp2
      config.vm.network "private_network", virtualbox__intnet: true # swp3
      config.vm.network "private_network", virtualbox__intnet: true # swp4
    end

You can find more information on creating and using private networks at
[docs.vagrantup.com/v2/networking/private\_network.html](https://docs.vagrantup.com/v2/networking/private_network.html)
and
[docs.vagrantup.com/v2/virtualbox/networking.html](https://docs.vagrantup.com/v2/virtualbox/networking.html).

### <span>Creating Multiple Cumulus VX Virtual Machines</span>

Vagrant can create and configure multiple virtual machines with a single
command. For example, you can use Vagrant to create multiple Cumulus VX
virtual machines and then connect the network interfaces of those
virtual machines together.

The following example creates two Cumulus VX virtual machines, leaf1 and
leaf2, where the interfaces swp1 through swp4 are connected together via
separate private networks:

    Vagrant.configure(2) do |config|
     
      config.vm.define "leaf1" do |leaf1|
        leaf1.vm.box = "cumulus-vx-2.5.3"
     
     
        # Internal network for swp* interfaces.
        leaf1.vm.network "private_network", virtualbox__intnet: "swp1"
        leaf1.vm.network "private_network", virtualbox__intnet: "swp2"
        leaf1.vm.network "private_network", virtualbox__intnet: "swp3"
        leaf1.vm.network "private_network", virtualbox__intnet: "swp4"
      end
     
      config.vm.define "leaf2" do |leaf2|
        leaf2.vm.box = "cumulus-vx-2.5.3"
     
        # Internal network for swp* interfaces.
        leaf2.vm.network "private_network", virtualbox__intnet: "swp1"
        leaf2.vm.network "private_network", virtualbox__intnet: "swp2"
        leaf2.vm.network "private_network", virtualbox__intnet: "swp3"
        leaf2.vm.network "private_network", virtualbox__intnet: "swp4"
      end
     
    end

When you run `vagrant up`, both virtual machines are created. You can
log in to each virtual machine and configure the interfaces as you wish,
and the interfaces will pass traffic between themselves as though they
were two physical switches connected together by four cables.

## <span>Limitations</span>

At this time, there are some limitations to using Vagrant with Cumulus
VX:

  - You cannot run KVM virtual machines under Vagrant.

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
<td><p>Windows 7</p></td>
<td><p>1.7.3</p></td>
<td><p>5.0</p></td>
<td><p>While both VirtualBox and Vagrant are fully supported on Windows hosts, Vagrant provisioning with Ansible is not.<br />
Cumulus VX demos that use Ansible will not work on Windows.</p></td>
</tr>
</tbody>
</table>

## <span>Preconfigured Cumulus VX Examples</span>

Cumulus Networks makes it easy to build a two-leaf/two-spine topology
within a Vagrant environment, requiring very little programming
knowledge. You can get started with these sample configurations:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Name</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://github.com/CumulusNetworks/cumulus-vx-vagrant/tree/master/vagrant/demos/ccw-2s" class="external-link">2-Switch</a></p></td>
<td><p>Creates a simple two switch topology with four shared links. Ideal for initial testing and experimentation.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://github.com/CumulusNetworks/cumulus-vx-vagrant/tree/master/vagrant/demos/clos-bgp" class="external-link">clos-bgp</a></p></td>
<td><p>Creates a two-leaf/two-spine network with BGP unnumbered interfaces.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://github.com/CumulusNetworks/cumulus-vx-vagrant/tree/master/vagrant/demos/clos-ospf" class="external-link">clos-ospf</a></p></td>
<td><p>Creates a two-leaf/two-spine network with OSPF unnumbered interfaces.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://github.com/CumulusNetworks/cumulus-vx-vagrant/tree/master/vagrant/demos/mlag" class="external-link">MLAG</a></p></td>
<td><p>Creates 2 "racks" of 5 hosts, connected to a large layer 2 network configured with MLAG.</p>
<p>{{%notice note%}}</p>
<p>If you are configuring MLAG, in order to start the <code>clagd</code> service, you must specify the <code>clagd-args --vm</code> option in <code>/etc/network/interfaces</code>:</p>
<pre><code>auto peer16.4000
iface peer16.4000 inet static
    address 11.0.5.2
    netmask 255.255.255.0
    clagd-enable yes
    clagd-peer-ip 11.0.5.1
    clagd-sys-mac 44:38:39:ff:ff:ff
    clagd-args --vm</code></pre>
<p>{{%/notice%}}</p></td>
</tr>
</tbody>
</table>

### <span>Getting the Demos from GitHub</span>

The demos are stored on GitHub, so you can just run `git clone` to get
them all:

    $ git clone https://github.com/CumulusNetworks/cumulus-vx-vagrant
    Cloning into 'cumulus-vx-vagrant'...
    remote: Counting objects: 584, done.
    remote: Total 584 (delta 0), reused 0 (delta 0), pack-reused 584
    Receiving objects: 100% (584/584), 97.42 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (229/229), done.
    Checking connectivity... done.
    $ ls
    CumulusVX-2.5.3-4eb681f3df86c478.box cumulus-vx-vagrant

### <span>Modifying the Demos</span>

You can modify the two leaf/two spine topology by changing the
`numSpines` and `numLeaves` variables in `properties.yml`:

    :numLeaves: 2
    :numSpines: 2
     
    # IP Address Base for loopback
    :ipAddrPrefix: "10.0.1."

You can modify the MLAG demo by changing the variables in the
`properties.yml` file:

    # Number of nodes to provision. Change these values to modify the size of the
    # network configuration. Be careful, changing these values can dramatically
    # affect the number of VMs created.
    :hostsPerRack: 5
    :racksPerPod:  2
    :podsPerDC:    1

### <span>About the OSPF Unnumbered Interfaces Configuration</span>

For the OSPF unnumbered configuration, the basic idea is to assign *the
same* IP address for each network node. Assign the IP address first to
the loopback interface, then assign that same IP address to every other
network interface except the management interface, eth0, as it is on a
separate network and requires its own IP address.

### <span>About the BGP Unnumbered Interfaces Configuration</span>

Cumulus Networks introduced the ability to configure BGP using interface
names instead of the IP address of the remote peer. The remote peer's
IPv6 link-local address is then determined using IPv6 router
advertisement, which is then used to set up a BGP session based on this
address. Finally, IPv4 and IPv6 addresses are exchanged over this
session.

To advertise IPv4 prefixes over an IPv6 session, Cumulus VX uses
Extended Next-Hop Encoding (RFC-5549). Cumulus VX also enables the
ability to specify whether the session is an iBGP or eBGP session,
without specifying the remote node's ASN. Both of these simplifications
lead to a phenomenal simplification in configuring BGP.
