---
title: Using Cumulus VX with KVM
author: Cumulus Networks
weight: 15
aliases:
 - /display/VX25/Using+Cumulus+VX+with+KVM
 - /pages/viewpage.action?pageId=5115403
pageID: 5115403
product: Cumulus VX
version: '2.5'
imgData: cumulus-vx-25
siteSlug: cumulus-vx-25
---
Once you install the hypervisor and [download the qcow2
image](https://cumulusnetworks.com/cumulus-vx/download/), you will clone
it a few times to create a two-leaf/two-spine virtual network using
[QEMU](http://wiki.qemu.org/Main_Page)/[KVM](http://www.linux-kvm.org/page/Downloads)
on a Linux server:

{{% imgOld 0 %}}

{{%notice note%}}

This configuration was tested on a server running Debian 3.2.60-1+deb7u3
x86\_64 GNU/Linux with 3.2.0-4-amd64 \#1 SMP processors.

{{%/notice%}}

The interfaces are connected as follows:

  - leaf1:swp1---\> spine1:swp1

  - leaf1:swp2---\>spine2:swp1

  - leaf2:swp1---\>spine1:swp2

  - leaf2:swp2---\>spine2:swp2

Copy the `qcow2` file you downloaded earlier onto a Linux server four
times, and name them as follows:

  - leaf1.qcow2

  - leaf2.qcow2

  - spine1.qcow2

  - spine2.qcow2

Power on leaf1 and configure it as follows:

    sudo /usr/bin/kvm   -curses                             \
                        -name leaf1                       \
                        -pidfile leaf1.pid                \
                        -smp 1                              \
                        -m 256                              \
                        -net nic,vlan=10,macaddr=00:01:00:00:01:00,model=virtio \
                        -net user,vlan=10,net=192.168.0.0/24,hostfwd=tcp::1401-:22 \
                        -netdev socket,udp=127.0.0.1:1602,localaddr=127.0.0.1:1601,id=dev0 \
                        -device virtio-net-pci,mac=00:02:00:00:00:01,addr=6.0,multifunction=on,netdev=dev0,id=swp1 \
                        -netdev socket,udp=127.0.0.1:1606,localaddr=127.0.0.1:1605,id=dev1 \
                        -device virtio-net-pci,mac=00:02:00:00:00:02,addr=6.1,multifunction=off,netdev=dev1,id=swp2 \
                        leaf1.qcow2

Power on leaf2 and configure it as follows:

``` Code
sudo /usr/bin/kvm   -curses                             \
                 -name leaf2                       \
                 -pidfile leaf2.pid                \
                 -smp 1                              \
                 -m 256                              \
                 -net nic,vlan=10,macaddr=00:01:00:00:02:00,model=virtio \
                 -net user,vlan=10,net=192.168.0.0/24,hostfwd=tcp::1402-:22 \
                 -netdev socket,udp=127.0.0.1:1604,localaddr=127.0.0.1:1603,id=dev0 \
                 -device virtio-net-pci,mac=00:02:00:00:00:03,addr=6.0,multifunction=on,netdev=dev0,id=swp1 \
                 -netdev socket,udp=127.0.0.1:1608,localaddr=127.0.0.1:1607,id=dev1 \
                 -device virtio-net-pci,mac=00:02:00:00:00:04,addr=6.1,multifunction=off,netdev=dev1,id=swp2 \
                 leaf2.qcow2
```

Power on spine1 and configure it as follows:

    sudo /usr/bin/kvm   -curses                             \
                    -name spine1                       \
                    -pidfile spine1.pid                \
                    -smp 1                              \
                    -m 256                              \
                    -net nic,vlan=10,macaddr=00:01:00:00:03:00,model=virtio \
                    -net user,vlan=10,net=192.168.0.0/24,hostfwd=tcp::1403-:22 \
                    -netdev socket,udp=127.0.0.1:1601,localaddr=127.0.0.1:1602,id=dev0 \
                    -device virtio-net-pci,mac=00:02:00:00:00:05,addr=6.0,multifunction=on,netdev=dev0,id=swp1 \
                    -netdev socket,udp=127.0.0.1:1603,localaddr=127.0.0.1:1604,id=dev1 \
                    -device virtio-net-pci,mac=00:02:00:00:00:06,addr=6.1,multifunction=off,netdev=dev1,id=swp2 \
                    spine1.qcow2

Power on spine2 and configure it as follows:

    sudo /usr/bin/kvm   -curses                             \
                    -name spine2                       \
                    -pidfile spine2.pid                \
                    -smp 1                              \
                    -m 256                              \
                    -net nic,vlan=10,macaddr=00:01:00:00:04:00,model=virtio \
                    -net user,vlan=10,net=192.168.0.0/24,hostfwd=tcp::1404-:22 \
                    -netdev socket,udp=127.0.0.1:1605,localaddr=127.0.0.1:1606,id=dev0 \
                    -device virtio-net-pci,mac=00:02:00:00:00:07,addr=6.0,multifunction=on,netdev=dev0,id=swp1 \
                    -netdev socket,udp=127.0.0.1:1607,localaddr=127.0.0.1:1608,id=dev1 \
                    -device virtio-net-pci,mac=00:02:00:00:00:08,addr=6.1,multifunction=off,netdev=dev1,id=swp2 \
                    spine2.qcow2

## <span>Configuring Network Interfaces and Quagga</span>

The next step is to configure the 2 leaf/2 spine topology. This includes
setting up the network interfaces, and Quagga, and assumes the previous
sections have been completed.

### <span>Configuring leaf1 VM</span>

To configure leaf1:

1.  Log into the VM using the following credentials:
    
      - username: cumulus
    
      - password: CumulusLinux\!

2.  Configure the interfaces:
    
    1.  Log in as root, using the password CumulusLinux\!
        
            cumulus@leaf1:~$ sudo -i
    
    2.  Open `/etc/network/interfaces` in a text editor.
    
    3.  Edit the interfaces as shown below, and save the file:
        
            # The loopback network interface
            auto lo
              iface lo inet loopback
              address 10.2.1.1/32
            
            # The primary network interface
            auto eth0
              iface eth0 inet dhcp
            
            auto swp1
              iface swp1
              address 10.2.1.1/32
            
            auto swp2
              iface swp2
              address 10.2.1.1/32
            
            auto swp3
              iface swp3
              address 10.4.1.1/24

3.  Configure Quagga
    
    1.  Open the `/etc/quagga/daemons` file in a text editor.
    
    2.  Set `zebra`, `bgpd`, and `ospfd` to yes, and save the file.
        
            zebra=yes
            bgpd=yes
            ospfd=yes
            ...
    
    3.  Create the `/etc/quagga/Quagga.conf` file in a text editor.
    
    4.  Configure the file as shown below, and save the file:
        
            service integrated-vtysh-config
            
            interface swp1
              ip ospf network point-to-point
            
            interface swp2
              ip ospf network point-to-point
            
            router-id 10.2.1.1
            
            router ospf
              ospf router-id 10.2.1.1
              network 10.2.1.1/32 area 0.0.0.0
              network 10.4.1.0/24 area 0.0.0.0

4.  Restart the networking service
    
        root@leaf1:~$ service networking restart

5.  Restart Quagga
    
        root@leaf1:~$ service quagga restart

### <span>Configuring leaf2, spine1, and spine2 VMs</span>

The configuration steps for `leaf2`, `spine1`, and `spine2` are the same
as those listed above for `leaf1`, however the file configurations are
different. Listed below are the configurations for each VM.

  - `leaf2`
    
      - `/etc/network/interfaces` file:
        
            # The loopback network interface
            auto lo
              iface lo inet loopback
              address 10.2.1.2/32
            
            # The primary network interface
            auto eth0
              iface eth0 inet dhcp
            
            auto swp1
              iface swp1
              address 10.2.1.2/32
            
            auto swp2
              iface swp2
              address 10.2.1.2/32
            
            auto swp3
              iface swp3
              address 10.4.2.1/25
    
      - `/etc/quagga/Quagga.conf` file:
        
            service integrated-vtysh-config 
            
            interface swp1
              ip ospf network point-to-point
            
            interface swp2
              ip ospf network point-to-point
            
            router-id 10.2.1.2
            
            router ospf
              ospf router-id 10.2.1.2                                                           
              network 10.2.1.2/32 area 0.0.0.0  
              network 10.4.2.0/24 area 0.0.0.0

  - `spine1`
    
      - `/etc/network/interfaces` file:
        
            # The loopback network interface
            auto lo
              iface lo inet loopback
              address 10.2.1.3/32
            
            # The primary network interface
            auto eth0
              iface eth0 inet dhcp
            
            auto swp1
              iface swp1
              address 10.2.1.3/32
            
            auto swp2
              iface swp2
              address 10.2.1.3/32
            
            auto swp3
              iface swp3
    
      - `/etc/quagga/Quagga.conf` file:
        
        ``` 
        service integrated-vtysh-config 
        
        interface swp1
          ip ospf network point-to-point
        
        interface swp2
          ip ospf network point-to-point
        
        router-id 10.2.1.3
        
        router ospf
          ospf router-id 10.2.1.3
          network 10.2.1.3/32 area 0.0.0.0  
        ```

  - `spine2`
    
      - `/etc/network/interfaces` file:
        
            # The loopback network interface
            auto lo
              iface lo inet loopback
              address 10.2.1.4/32
            
            # The primary network interface
            auto eth0
              iface eth0 inet dhcp
            
            auto swp1
              iface swp1
              address 10.2.1.4/32
            
            auto swp2
              iface swp2
              address 10.2.1.4/32
            
            auto swp3
              iface swp3
    
      - `/etc/quagga/Quagga.conf` file:
        
            service integrated-vtysh-config 
            
            interface swp1
              ip ospf network point-to-point
            
            interface swp2
              ip ospf network point-to-point
            
            router-id 10.2.1.4
            
            router ospf
              ospf router-id 10.2.1.4
              network 10.2.1.4/32 area 0.0.0.0

{{%notice note%}}

Remember to restart the networking and Quagga services on all VMs before
continuing.

{{%/notice%}}

## <span>Testing the Connections</span>

Once the VMs have been restarted, you can ping across VMs to test:

  - From `leaf1`:
    
      - Ping `leaf2`:
        
            root@leaf1:~# ping 10.2.1.2
    
      - Ping `spine1`:
        
            root@leaf1:~# ping 10.2.1.3
    
      - Ping `spine2`:
        
            root@leaf1:~# ping 10.2.1.4

{{%notice note%}}

The QEMU/KVM commands used here are minimal. You can add more parameters
as needed, like `-enable-kvm`, `-serial` or `-monitor`.

{{%/notice%}}

## <span>Bridging Switch Port Interfaces</span>

If you intend to bridge the switch ports in the VM, you should place
each switch port in the bridge in its own virtual network on the host.
Otherwise, you may see this error:

    br0: recevied package on swp1 with own address as source address

## <span>Using CumulusVX with Libvirt and QEMU/KVM</span>

### <span>Using Libvirt</span>

1.  Confirm `libvert` and `qemu` are installed correctly:
    
    1.  Check the Linux version running:
        
            uname -a
    
    2.  Run the following commands to install libvert:
        
            cumulus@switch:~$ sudo add-apt-repository ppa:linuxsimba/libvirt-udp-tunnel 
            cumulus@switch:~$ sudo apt-get update -y
            cumulus@switch:~$ sudo apt-get install libvirt-bin libvirt-dev ansible qemu-utils qemu git htop tree
            cumulus@switch:~$ sudo /etc/init.d/libvirt-bin restart
    
    The linuxsimba/libvirt-udp-tunnel package repository provides an
    updated libvirtd version that provides certain enhancements required
    to launch Cumulus VX. The example below shows the installation
    output:
    
        SERVER:~/TAM/Vz-LK$ sudo apt-get install libvirt-bin libvirt-dev ansible qemu-utils qemu git htop tree
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

2.  After the installation has been complete, logout, then login, and
    verify the `libvert` version:
    
        cumulus@switch:~$ libvirtd --version
        libvirtd (libvirt) 1.2.16
        Version should be 1.2.16.

3.  Create and define a virsh pool to point to the libvirt based vagrant
    images:
    
    ``` 
    virsh pool-define-as --name NAME --type dir --target /var/lib/libvirt/images
    virsh pool-autostart NAMEvirsh pool-build NAMEvirsh pool-start NAME    
    ```

### <span>Launch the Vagrant Instance</span>

1.  Create the appropriate VagrantFile. This can be done using topology
    converter.

2.  Installing most recent version of vagrant-libvirt plugin – Required
    for best KVM support:
    
        cumulus@switch:~$ git clone https://github.com/pradels/vagrant-libvirt
        cumulus@switch:~$ gem build vagrant-libvirt.gemspec
        cumulus@switch:~$ vagrant plugin install vagrant-libvirt-*.gem
        cumulus@switch:~$ /usr/bin/vagrant plugin list

3.  Install vagrant's `libvirt/cumulus/mutate` plugins:
    
        cumulus@switch:~$ vagrant plugin install vagrant-cumulus
        Installing the 'vagrant-cumulus' plugin. This can take a few minutes...
        Installed the plugin 'vagrant-cumulus (0.1)'!
        
        cumulus@switch:~$ vagrant plugin install vagrant-mutate
        Installing the 'vagrant-mutate' plugin. This can take a few minutes...
        Installed the plugin 'vagrant-mutate (1.1.0)'!
    
      - libvirt plugin - Used to allow libvirt to read VagrantFile
    
      - cumulus plugin - Used to run cumulus specific commands within
        VagrantFile
    
      - mutate plugin - Used to convert a VagrantBox image to a Libvirt
        image
    
    After installing these plugins:
    
        cumulus@switch:~$ vagrant status
        Current machine states:
        
        oob                       not created (virtualbox)
        spine1                    not created (virtualbox)
        spine2                    not created (virtualbox)
        leaf1                     not created (virtualbox)
        leaf2                     not created (virtualbox)
        server1                   not created (virtualbox)
        server2                   not created (virtualbox)
    
    This environment represents multiple VMs. The VMs are all listed
    above with their current state. For more information about a
    specific VM, run `vagrant status NAME`.

4.  Convert VagrantBox image to Libvirt image
    
        cumulus@switch:~$ vagrant box list
        CumulusCommunity/cumulus-vx (virtualbox, 2.5.6)
        cumulus@switch:~$ vagrant mutate CumulusCommunity/cumulus-vx libvirt
        Converting CumulusCommunity/cumulus-vx from virtualbox to libvirt.
            (100.00/100%)
        The box CumulusCommunity/cumulus-vx (libvirt) is now ready to use.
         
        SERVER:~/TAM/Vz-LK$ vagrant box list
        CumulusCommunity/cumulus-vx (libvirt, 2.5.6)
        CumulusCommunity/cumulus-vx (virtualbox, 2.5.6)

5.  Bring up image using --provider libvirt:
    
        cumulus@switch:~/TAM/Vz-LK$ vagrant up oob --provider libvirt
        Bringing machine 'oob' up with 'libvirt' provider...
        ==> oob: Creating image (snapshot of base box volume).
        ==> oob: Creating domain with the following settings...
        ==> oob:  -- Name:              Vz-LK_oob
        ==> oob:  -- Domain type:       kvm
        ==> oob:  -- Cpus:              1
        ==> oob:  -- Memory:            200M
        ==> oob:  -- Management MAC:    
        ==> oob:  -- Loader:            
        ==> oob:  -- Base box:          CumulusCommunity/cumulus-vx
        ==> oob:  -- Storage pool:      default
        ==> oob:  -- Image:             /var/lib/libvirt/images/Vz-LK_oob.img (2G)
        ==> oob:  -- Volume Cache:      default
        ==> oob:  -- Kernel:            
        ==> oob:  -- Initrd:            
        ==> oob:  -- Graphics Type:     vnc
        ==> oob:  -- Graphics Port:     5900
        ==> oob:  -- Graphics IP:       127.0.0.1
        ==> oob:  -- Graphics Password: Not defined
        ==> oob:  -- Video Type:        cirrus
        ==> oob:  -- Video VRAM:        9216
        ==> oob:  -- Keymap:            en-us
        ==> oob:  -- TPM Path:          
        ==> oob:  -- INPUT:             type=mouse, bus=ps2
        ==> oob:  -- Command line : 
        ==> oob: Creating shared folders metadata...
        ==> oob: Starting domain.
        ==> oob: Waiting for domain to get an IP address...
        ==> oob: Waiting for SSH to become available...
            oob: 
            oob: Vagrant insecure key detected. Vagrant will automatically replace
            oob: this with a newly generated keypair for better security.
            oob: 
            oob: Inserting generated public key within guest...
            oob: Removing insecure key from the guest if it's present...
            oob: Key inserted! Disconnecting and reconnecting using new SSH key...
        ==> oob: Setting hostname...
        ==> oob: Configuring and enabling network interfaces...
          ==> oob: Running provisioner: shell...

## <span>Further Information</span>

For the next steps regarding configuring Cumulus VX, check out these
community articles, and the rest of the Cumulus Documentation:

Management Network with Cumulus VX:  
<https://community.cumulusnetworks.com/cumulus/topics/using-a-management-vm-with-cumulus-vx>

Automation: Network Automation with Cumulus VX  
<https://community.cumulusnetworks.com/cumulus/topics/testing-network-automation-with-cumulus-vx-3028v0i4u6aw4>

Routing protocols: Unnumbered OSPF/BGP with Cumulus VX  
<https://community.cumulusnetworks.com/cumulus/topics/un-numbered-ospf-bgp-setup-on-vmware-esxi-with-cumulus-vx>

Network redundancy: Multi-chassis Link Aggregation (MLAG) with Cumulus
VX  
<https://community.cumulusnetworks.com/cumulus/topics/spinning-up-a-virtual-mlag-environment>

Network virtualization: Cumulus VX with VMware NSX  
<https://community.cumulusnetworks.com/cumulus/topics/integrating-cumulus-vx-with-vmware-nsx-using-vmware-esxi>

Cumulus Linux Documentation  
<http://docs.cumulusnetworks.com/display/DOCS/>

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
