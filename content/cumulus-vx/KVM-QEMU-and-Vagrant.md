---
title: KVM-QEMU and Vagrant
author: NVIDIA
weight: 20
product: Cumulus VX
version: '5.x'
---
Running Cumulus VX with KVM-QEMU and Vagrant requires four components:

{{% vx/kvm-components %}}
- **Vagrant** is an orchestration tool that makes it easier to manage groups of VMs by interconnecting them programmatically. Vagrant helps to tie all the components together and provides a user-friendly language to launch suites of VMs. Vagrant allows multiple Cumulus VX VMs to interconnect to simulate a network. Vagrant also allows Cumulus VX VMs to interconnect with other VMs (such as Ubuntu or CentOS) to emulate real world networks.

This section describes how to install and set up Cumulus VX with KVM-QEMU, Libvirt, and Vagrant on a Linux server to create the two leaf and one spine topology shown below.

{{% vx/intro %}}

<!-- vale off -->
These steps were tested with Cumulus VX 4.2, KVM/QEMU version 1:4.2-3ubuntu6.3, Libvirt version 6.0.0, and Vagrant version 2.2.9 on Ubuntu Linux version 20.04.
<!-- vale on -->

## Create and Configure the VMs

The following procedure creates leaf01, leaf02, and spine01 and the network connections between them. This section assumes you have Linux, KVM, and Vagrant experience.

### Download and Install the Software

{{%notice info%}}
Install Vagrant **after** you install libvirt so that Vagrant can detect all the necessary files.
{{%/notice%}}

1. Run the following commands to install KVM-QEMU and libvirt.

   ```
   local@host:~$ sudo apt update -y
   local@host:~$ sudo apt install -qy qemu ebtables dnsmasq-base qemu-kvm libvirt-clients libvirt-daemon-system bridge-utils virt-manager python3-pip
   local@host:~$ sudo apt install -qy libxslt-dev libxml2-dev libvirt-dev zlib1g-dev ruby-dev
   ```

2. Add users to the `libvirt` group so they can perform `virsh` commands.

   ```
   local@host:~$ sudo usermod -a -G libvirt <username>
   ```

3. Run the following commands to install Vagrant and the necessary plugins:

   ```
   local@host:~$ sudo wget https://releases.hashicorp.com/vagrant/2.2.9/vagrant_2.2.9_x86_64.deb
   local@host:~$ sudo dpkg -i vagrant_2.2.9_x86_64.deb
   local@host:~$ sudo vagrant plugin install vagrant-libvirt
   ```

5. Confirm that your Linux kernel and BIOS settings permit the use of KVM hardware acceleration:

   ```
   local@host:~$ kvm-ok
   INFO: /dev/kvm exists
   KVM acceleration can be used
   ```

### Create VMs and Network Connections

1. Create a folder to contain the Vagrant environment, then change directories into that folder.

   ```
   local@host:~$ mkdir vagrant
   local@host:~$ cd vagrant
   ```

2. Initialize the Vagrant environment to create a file called `Vagrantfile` in the folder you just created.

   ```
   local@host:~/vagrant$ vagrant init
   A `Vagrantfile` has been placed in this directory. You are now
   ready to `vagrant up` your first virtual environment! Please read
   the comments in the Vagrantfile as well as documentation on
   `vagrantup.com` for more information on using Vagrant.
   ```

3. Edit the `Vagrantfile` and replace the contents of the file with the following:

{{%notice note%}}
- The following is a complete Vagrantfile for the two leaf and one spine example topology. For more information on writing a Vagrantfile, reference the {{% exlink text="Hashicorp Vagrant" url="https://www.vagrantup.com/docs/vagrantfile" %}} documentation.
- This Vagrantfile defines CPU, memory, and disk requirements for Cumulus VX, which requires at least 768MB of RAM and 6GB of disk space.
- For CumulusVX versions 4.3 and later requires 2 vCPUs.
{{%/notice%}}

{{< expand "Vagrantfile" >}}

   ```
   local@host:~/vagrant$ vi Vagrantfile

   #Set the default provider to libvirt in the case they forget --provider=libvirt or if someone destroys a machine it reverts to virtualbox ENV['VAGRANT_DEFAULT_PROVIDER'] = 'libvirt'
   # Check required plugins
   REQUIRED_PLUGINS_LIBVIRT = %w(vagrant-libvirt)
   exit unless REQUIRED_PLUGINS_LIBVIRT.all? do |plugin|
     Vagrant.has_plugin?(plugin) || (
       puts "The #{plugin} plugin is required. Please install it with:"
       puts "$ vagrant plugin install #{plugin}"
       false
     )
   end

   $script = <<-SCRIPT
   echo "### RUNNING CUMULUS EXTRA CONFIG ###"
   source /etc/lsb-release
   echo "  INFO: Detected Cumulus Linux v$DISTRIB_RELEASE Release"

   echo "### Disabling default remap on Cumulus VX..."
   mv -v /etc/hw_init.d/S10rename_eth_swp.sh /etc/S10rename_eth_swp.sh.backup &> /dev/null

   echo "### Giving Vagrant User Ability to Run NCLU Commands ###"
   adduser vagrant netedit
   adduser vagrant netshow

   echo "### DONE ###"
   echo "### Rebooting Device to Apply Remap..."
   nohup bash -c 'sleep 10; shutdown now -r "Rebooting to Remap Interfaces"' &
   SCRIPT

   Vagrant.configure("2") do |config|
     config.ssh.forward_agent = true

     wbid = 1
     offset = wbid * 100

     config.vm.provider :libvirt do |domain|
       domain.management_network_address = "10.255.#{wbid}.0/24"
       domain.management_network_name = "wbr#{wbid}"
     end

     ####DEFINE VM for spine01 #####
     config.vm.define "spine01" do |device|

       device.vm.hostname = "spine01"

       device.vm.box = "CumulusCommunity/cumulus-vx"
       device.vm.box_version = "4.2.0"

       device.vm.provider :libvirt do |v|
         v.memory = 768
         v.cpus = 2
       end
       #   see note here: https://github.com/pradels/vagrant-libvirt#synced-folders
       device.vm.synced_folder ".", "/vagrant", disabled: true

         # link for swp1 --> leaf01:swp1
         device.vm.network "private_network",
               :mac => "44:38:39:00:00:01",
               :libvirt__tunnel_type => 'udp',
               :libvirt__tunnel_local_ip => '127.0.0.1',
               :libvirt__tunnel_local_port => "#{ 8001 + offset }",
               :libvirt__tunnel_ip => '127.0.0.1',
               :libvirt__tunnel_port => "#{ 9001 + offset }",
               :libvirt__iface_name => 'swp1',
               auto_config: false
         # link for swp2 --> leaf02:swp1
         device.vm.network "private_network",
               :mac => "44:38:39:00:00:03",
               :libvirt__tunnel_type => 'udp',
               :libvirt__tunnel_local_ip => '127.0.0.1',
               :libvirt__tunnel_local_port => "#{ 8002 + offset }",
               :libvirt__tunnel_ip => '127.0.0.1',
               :libvirt__tunnel_port => "#{ 9002 + offset }",
               :libvirt__iface_name => 'swp2',
               auto_config: false

       # Run the Config specified in the Node Attributes
       device.vm.provision :shell , privileged: false, :inline => 'echo "$(whoami)" > /tmp/normal_user'

       # Install Rules for the interface re-map
       device.vm.provision :shell , :inline => <<-delete_udev_directory
   if [ -d "/etc/udev/rules.d/70-persistent-net.rules" ]; then
       rm -rfv /etc/udev/rules.d/70-persistent-net.rules &> /dev/null
   fi
   rm -rfv /etc/udev/rules.d/70-persistent-net.rules &> /dev/null
   delete_udev_directory

        device.vm.provision :shell , :inline => <<-udev_rule
   echo "  INFO: Adding UDEV Rule: 44:38:39:00:00:01 --> swp1"
   echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="44:38:39:00:00:01", NAME="swp1", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   udev_rule
        device.vm.provision :shell , :inline => <<-udev_rule
   echo "  INFO: Adding UDEV Rule: 44:38:39:00:00:03 --> swp2"
   echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="44:38:39:00:00:03", NAME="swp2", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   udev_rule

       # Run Any Platform Specific Code and Apply the interface Re-map
       #   (may or may not perform a reboot depending on platform)
       device.vm.provision :shell , :inline => $script

   end
     # DEFINE VM for leaf01 #####
     config.vm.define "leaf01" do |device|

       device.vm.hostname = "leaf01"

       device.vm.box = "CumulusCommunity/cumulus-vx"
       device.vm.box_version = "4.2.0"

       device.vm.provider :libvirt do |v|
         v.memory = 768
         v.cpus = 2
       end
       #   see note here: https://github.com/pradels/vagrant-libvirt#synced-folders
       device.vm.synced_folder ".", "/vagrant", disabled: true

       # NETWORK INTERFACES
         # link for swp1 --> spine01:swp1
         device.vm.network "private_network",
               :mac => "44:38:39:00:00:02",
               :libvirt__tunnel_type => 'udp',
               :libvirt__tunnel_local_ip => '127.0.0.1',
               :libvirt__tunnel_local_port => "#{ 9001 + offset }",
               :libvirt__tunnel_ip => '127.0.0.1',
               :libvirt__tunnel_port => "#{ 8001 + offset }",
               :libvirt__iface_name => 'swp1',
               auto_config: false
         # link for swp2 --> leaf02:swp2
         device.vm.network "private_network",
               :mac => "44:38:39:00:00:05",
               :libvirt__tunnel_type => 'udp',
               :libvirt__tunnel_local_ip => '127.0.0.1',
               :libvirt__tunnel_local_port => "#{ 8003 + offset }",
               :libvirt__tunnel_ip => '127.0.0.1',
               :libvirt__tunnel_port => "#{ 9003 + offset }",
               :libvirt__iface_name => 'swp2',
               auto_config: false
         # link for swp3 --> leaf02:swp3
         device.vm.network "private_network",
               :mac => "44:38:39:00:00:07",
               :libvirt__tunnel_type => 'udp',
               :libvirt__tunnel_local_ip => '127.0.0.1',
               :libvirt__tunnel_local_port => "#{ 8004 + offset }",
               :libvirt__tunnel_ip => '127.0.0.1',
               :libvirt__tunnel_port => "#{ 9004 + offset }",
               :libvirt__iface_name => 'swp3',
               auto_config: false

       # Run the Config specified in the Node Attributes
       device.vm.provision :shell , privileged: false, :inline => 'echo "$(whoami)" > /tmp/normal_user'

       # Install Rules for the interface re-map
       device.vm.provision :shell , :inline => <<-delete_udev_directory
   if [ -d "/etc/udev/rules.d/70-persistent-net.rules" ]; then
       rm -rfv /etc/udev/rules.d/70-persistent-net.rules &> /dev/null
   fi
   rm -rfv /etc/udev/rules.d/70-persistent-net.rules &> /dev/null
   delete_udev_directory

        device.vm.provision :shell , :inline => <<-udev_rule
   echo "  INFO: Adding UDEV Rule: 44:38:39:00:00:02 --> swp1"
   echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="44:38:39:00:00:02", NAME="swp1", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   udev_rule
        device.vm.provision :shell , :inline => <<-udev_rule
   echo "  INFO: Adding UDEV Rule: 44:38:39:00:00:05 --> swp2"
   echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="44:38:39:00:00:05", NAME="swp2", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   udev_rule
        device.vm.provision :shell , :inline => <<-udev_rule
   echo "  INFO: Adding UDEV Rule: 44:38:39:00:00:07 --> swp3"
   echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="44:38:39:00:00:07", NAME="swp3", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   udev_rule

   # Run Any Platform Specific Code and Apply the interface Re-map
       #   (may or may not perform a reboot depending on platform)
       device.vm.provision :shell , :inline => $script

   end

     ##### DEFINE VM for leaf02 #####
     config.vm.define "leaf02" do |device|

       device.vm.hostname = "leaf02"

       device.vm.box = "CumulusCommunity/cumulus-vx"
       device.vm.box_version = "4.2.0"

       device.vm.provider :libvirt do |v|
         v.memory = 768
         v.cpus = 2
       end
       #   see note here: https://github.com/pradels/vagrant-libvirt#synced-folders
       device.vm.synced_folder ".", "/vagrant", disabled: true

       # NETWORK INTERFACES
         # link for swp1 --> spine01:swp2
         device.vm.network "private_network",
               :mac => "44:38:39:00:00:04",
               :libvirt__tunnel_type => 'udp',
               :libvirt__tunnel_local_ip => '127.0.0.1',
               :libvirt__tunnel_local_port => "#{ 9002 + offset }",
               :libvirt__tunnel_ip => '127.0.0.1',
               :libvirt__tunnel_port => "#{ 8002 + offset }",
               :libvirt__iface_name => 'swp1',
               auto_config: false
         # link for swp2 --> leaf01:swp2
         device.vm.network "private_network",
               :mac => "44:38:39:00:00:06",
               :libvirt__tunnel_type => 'udp',
               :libvirt__tunnel_local_ip => '127.0.0.1',
               :libvirt__tunnel_local_port => "#{ 9003 + offset }",
               :libvirt__tunnel_ip => '127.0.0.1',
               :libvirt__tunnel_port => "#{ 8003 + offset }",
               :libvirt__iface_name => 'swp2',
               auto_config: false
         # link for swp3 --> leaf01:swp3
         device.vm.network "private_network",
               :mac => "44:38:39:00:00:08",
               :libvirt__tunnel_type => 'udp',
               :libvirt__tunnel_local_ip => '127.0.0.1',
               :libvirt__tunnel_local_port => "#{ 9004 + offset }",
               :libvirt__tunnel_ip => '127.0.0.1',
               :libvirt__tunnel_port => "#{ 8004 + offset }",
               :libvirt__iface_name => 'swp3',
               auto_config: false

       # Run the Config specified in the Node Attributes
       device.vm.provision :shell , privileged: false, :inline => 'echo "$(whoami)" > /tmp/normal_user'

       # Install Rules for the interface re-map
       device.vm.provision :shell , :inline => <<-delete_udev_directory
   if [ -d "/etc/udev/rules.d/70-persistent-net.rules" ]; then
       rm -rfv /etc/udev/rules.d/70-persistent-net.rules &> /dev/null
   fi
   rm -rfv /etc/udev/rules.d/70-persistent-net.rules &> /dev/null
   delete_udev_directory

        device.vm.provision :shell , :inline => <<-udev_rule
   echo "  INFO: Adding UDEV Rule: 44:38:39:00:00:04 --> swp1"
   echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="44:38:39:00:00:04", NAME="swp1", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   udev_rule
        device.vm.provision :shell , :inline => <<-udev_rule
   echo "  INFO: Adding UDEV Rule: 44:38:39:00:00:06 --> swp2"
   echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="44:38:39:00:00:06", NAME="swp2", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   udev_rule
        device.vm.provision :shell , :inline => <<-udev_rule
   echo "  INFO: Adding UDEV Rule: 44:38:39:00:00:08 --> swp3"
   echo 'ACTION=="add", SUBSYSTEM=="net", ATTR{address}=="44:38:39:00:00:08", NAME="swp3", SUBSYSTEMS=="pci"' >> /etc/udev/rules.d/70-persistent-net.rules
   udev_rule

       # Run Any Platform Specific Code and Apply the interface Re-map
       #   (may or may not perform a reboot depending on platform)
       device.vm.provision :shell , :inline => $script

   end

   end
   ```

{{< /expand >}}

4. Run `vagrant up` to start the VMs:

{{%notice note%}}
KVM starts all Vagrant defined VMs in parallel. In large topologies, this might cause host resource contention issues. Consider starting a subset of VMs at a time using the `vagrant up <hostname> <hostname>` command.
{{%/notice%}}

   ```
   local@host:~/vagrant$ vagrant up
   Bringing machine 'spine01' up with 'libvirt' provider...
   Bringing machine 'leaf01' up with 'libvirt' provider...
   Bringing machine 'leaf02' up with 'libvirt' provider...
   ...
   ```

## Log into the Switches

{{% vx/login-vagrant %}}

## Basic Switch Configuration

{{% vx/basic-config-vagrant-kvm %}}

## Verify Configuration

{{% vx/verify-config %}}

## Next Steps

{{% vx/next-steps %}}
