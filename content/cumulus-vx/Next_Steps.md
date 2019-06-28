---
title: Next Steps
author: Cumulus Networks
weight: 23
aliases:
 - /display/VX/Next+Steps
 - /pages/viewpage.action?pageId=5126707
pageID: 5126707
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
This section provides some additional configuration specific to Cumulus
VX and shows some basic commands you can try to get started with Cumulus
Linux. Additional resources for further reading and more advanced
configuration are also provided.

## <span>Perform Additional Configuration</span>

To provide easier access in video-focused hypervisors (such as
VirtualBox), Cumulus VX is configured by default to redirect the grub
menu and the kernel output to the video console. Follow the steps below
to send both the grub menu and the kernel output back to the serial
console.

If the VM has **not** been booted:

1.  Interrupt the boot process at the GRUB prompt.

2.  Modify the Linux command line directly, removing all references to
    the console entries:
    
    **Original Version:**
    
    {{% imgOld 0 %}}
    
    **Configured Version:**
    
    {{% imgOld 1 %}}
    
    {{%notice note%}}
    
    The example images above are for the ONIE-RESCUE entry, not the
    standard boot entry. The configuration process is the same for both
    entries.
    
    {{%/notice%}}

3.  Start the VM.

If the VM is already running:

1.  Run the following commands as the sudo user:
    
        cumulus@switch:~$ sed -i 's/^#//' /etc/default/grub.d/00-installer-defaults.cfg
        cumulus@switch:~$ sed -r -i '/^GRUB_CMDLINE_LINUX=/ s/(console=ttyS0,115200n8) (console=tty0)/\2 \1/' /etc/default/grub
        cumulus@switch:~$ update-grub 

2.  Restart the VM to implement the change.

## <span>Try Basic Commands</span>

After you have configured the Cumulus VX instances and performed
additional configuration, use the wider Cumulus Linux documentation
suite to help you configure and test features, and fine tune the network
topology.

This section provides some basic commands to get you started. You can
run the commands on each VM to see system information, as well as
interface and LLDP details and to change the hostname of a switch.

To get information about the switch itself, run the `net show system`
command:

    cumulus@switch:~$ net show system
    Cumulus VX
    Cumulus Linux 3.5.0
    Build: Cumulus Linux 3.5.0
    Uptime: 4:29:09.270000

To show every available interface that is physically UP, run the `net
show interface` command:

    cumulus@switch:~$ net show interface
           Name    Master    Speed    MTU    Mode           Remote Host       Remote Port    Summary
    -----  ------  --------  -------  -----  -------------  ----------------  -------------  -------------------------------------
    UP     lo                N/A      65536  Loopback                                        IP: 127.0.0.1/8, 10.2.1.1/32, ::1/128
    UP     eth0              1G       1500   Mgmt                                            IP: 10.0.2.15/24(DHCP)
    UP     swp1              1G       1500   Interface/L3   CumulusVX-spine1  swp1           IP: 10.2.1.1/32
    UP     swp2              1G       1500   Interface/L3   CumulusVX-spine2  swp1           IP: 10.2.1.1/32
    UP     swp3              1G       1500   Interface/L3                                    IP: 10.4.1.1/24
    ADMDN  swp4              N/A      1500   NotConfigured
    ADMDN  swp5              N/A      1500   NotConfigured
    ADMDN  swp6              N/A      1500   NotConfigured
    ADMDN  swp7              N/A      1500   NotConfigured 

To get topology verification, run the `net show lldp` command.

The example output below shows the two-leaf/two-spine Cumulus VX network
topology from CumulusVX-leaf1, where local port **swp1** is connected to
remote port **swp1** on **CumulusVX-spine1** and local port **swp2** is
connected to remote port **swp1** on **CumulusVX-spine2**.

    cumulus@switch:~$ net show lldp
    LocalPort    Speed    Mode          RemotePort    RemoteHost        Summary
    -----------  -------  ------------  ------------  ----------------  ---------------
    swp1         1G       Interface/L3  swp1          CumulusVX-spine1  IP: 10.2.1.1/32
    swp2         1G       Interface/L3  swp1          CumulusVX-spine2  IP: 10.2.1.1/32

To change the hostname, run the `net add hostname` command.

This command updates both the `/etc/hostname` and `/etc/hosts` files.

    cumulus@switch:~$ net add hostname <hostname>

## <span>Further Information</span>

Check out these community articles and the rest of the Cumulus Linux
documentation:

  - [Automation: Network automation with Cumulus
    VX](https://forums.cumulusnetworks.com/cumulus-vx-230884/testing-network-automation-with-cumulus-vx-6727777)

  - [Routing protocols: Unnumbered OSPF/BGP with Cumulus
    VX](https://forums.cumulusnetworks.com/cumulus-vx-230884/unnumbered-ospf-bgp-configuration-on-vmware-esxi-with-cumulus-vx-6728629)

  - [Network redundancy: Multi-chassis Link Aggregation (MLAG) with
    Cumulus
    VX](https://forums.cumulusnetworks.com/cumulus-vx-230884/spinning-up-a-virtual-mlag-environment-6722798)

  - [Network virtualization: Cumulus VX with VMware
    NSX](https://forums.cumulusnetworks.com/cumulus-vx-230884/integrating-cumulus-vx-with-vmware-nsx-using-vmware-esxi-6732766)

  - [Cumulus Linux
    documentation](http://docs.cumulusnetworks.com/display/DOCS/)

  - [Cumulus Networks knowledge
    base](https://support.cumulusnetworks.com/hc/en-us/)
