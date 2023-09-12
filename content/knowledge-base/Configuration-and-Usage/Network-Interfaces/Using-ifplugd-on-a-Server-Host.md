---
title: Using ifplugd on a Server Host
author: NVIDIA
weight: 418
toc: 4
---

By default, Linux (other than Cumulus Linux, as this article discusses server hosts) does not remove the IP address on connected interfaces. Further, static routes do not associate the interface when a link goes down (as in NO-CARRIER). Read more {{<link url="Monitor-Interface-Administrative-State-and-Physical-State-on-Cumulus-Linux" text="about determining the administrative/physical state on Linux">}}.

To understand what this means, first review this persistent configuration of an Ubuntu 14.10 VM, which gets stored in `/etc/network/interfaces` (not `network-manager`):

    auto eth1 iface eth1
    inet static 
        address 5.5.5.5 
        netmask 255.255.255.0 
        broadcast 5.5.5.255 
        up route add -net 3.3.0.0/16 gw 5.5.5.1 dev eth1

On this VM, eth1 is UP because the output below indicates *LOWER\_UP*. In addition, its state is *UP*.

    user@ubuntu:~$ ip link show eth1
    3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000 link/ether 00:0c:29:8e:9e:3a brd ff:ff:ff:ff:ff:ff

In looking at the routing table:

    user@ubuntu:~$ ip route show
    default via 192.168.72.2 dev eth0
    3.3.0.0/16 via 5.5.5.1 dev eth1
    5.5.5.0/24 dev eth1  proto kernel  scope link  src 5.5.5.5
    169.254.0.0/16 dev eth1  scope link  metric 1000
    192.168.72.0/24 dev eth0  proto kernel  scope link  src 192.168.72.136

Notice the following:

- The connected route of 5.5.5.0/24 on eth1 (because the assigned address is 5.5.5.5 and is on the 255.255.255.0 subnet)
- A 3.3.0.0/16 static route configured on this Ubuntu VM

Next, simulate no connection on eth1 (for example, someone pulled out the cable). You can do this by assigning the Ethernet device in the VM to a dead interface:

    user@ubuntu:~$ ip link show eth1
    3: eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT group default qlen 1000
        link/ether 00:0c:29:8e:9e:3a brd ff:ff:ff:ff:ff:f

The *NO-CARRIER* and the *DOWN* state indicate that this link is administratively up, but physically down. Now check the routing table:

    user@ubuntu:~$ ip route show
    default via 192.168.72.2 dev eth0
    3.3.0.0/16 via 5.5.5.1 dev eth1
    5.5.5.0/24 dev eth1  proto kernel  scope link  src 5.5.5.5
    169.254.0.0/16 dev eth1  scope link  metric 1000
    192.168.72.0/24 dev eth0  proto kernel  scope link  src 192.168.72.136

Notice that **nothing changed** in the configuration. While this is helpful in some situations &mdash; for example, your Web connections do not reset when your wireless card moves between APs and momentarily goes down &mdash; it is not good in others and can cause traffic to be black-holed. For servers this is not usually a problem unless you are doing something fancy like having dual gateways (two or more equal cost routes). In this case, the server attempts to load balance on the dead link as the route was not removed for that interface, resulting in 50% of your connections failing as they try to use the link that is dead.

## Demoing ifplugd

With the link on the Ubuntu VM reset and the link set to UP in VMware Fusion (the hypervisor), you can start `ifplugd`.

    user@ubuntu:~$ sudo service ifplugd start
     * Network Interface Plugging Daemon...                                          
     * start eth1...                                                         
     [ OK ] 
    user@ubuntu:~$                                               
    
    user@ubuntu:~$ service ifplugd status 
    * eth1: ifplugd process for device eth1 running as pid 4512. 
    user@ubuntu:~$ ip link show eth1 3: eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT group default qlen 1000 link/ether 00:0c:29:8e:9e:3a brd ff:ff:ff:ff:ff:ff

At this point, the cable has been "cut," which you can see in the routing table:

    user@ubuntu:~$ ip link show eth1
    3: eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT group default qlen 1000
        link/ether 00:0c:29:8e:9e:3a brd ff:ff:ff:ff:ff:ff
    user@ubuntu:~$ ip route show
    default via 192.168.72.2 dev eth0
    169.254.0.0/16 dev eth0  scope link  metric 1000
    192.168.72.0/24 dev eth0  proto kernel  scope link  src 192.168.72.136

Notice both routes no longer appear in the output above. Next, the cable is back in, so the link goes back to administratively UP and physically UP:

    user@ubuntu:~$ ip link show eth1
    3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
        link/ether 00:0c:29:8e:9e:3a brd ff:ff:ff:ff:ff:ff
    user@ubuntu:~$ ip route show
    default via 192.168.72.2 dev eth0
    3.3.0.0/16 via 5.5.5.1 dev eth1
    5.5.5.0/24 dev eth1  proto kernel  scope link  src 5.5.5.5
    169.254.0.0/16 dev eth0  scope link  metric 1000
    192.168.72.0/24 dev eth0  proto kernel  scope link  src 192.168.72.136

Notice that everything looks as it did before. `ifplugd` has helped the server act more like a router (or layer 3 switch) and enables the connected and static routes to disappear.
<!-- vale off -->
## Configuring ifplugd on Ubuntu 14.10
<!-- vale on -->
The following examples use {{<exlink url="https://launchpad.net/ubuntu/+source/ifupdown" text="ifupdown">}} (not {{<exlink url="https://github.com/CumulusNetworks/ifupdown2" text="ifupdown2">}} in NVIDIA and not {{<exlink url="https://wiki.debian.org/NetworkManager" text="network-manager">}}.

1.  Run `apt-get update` to grab the latest package information:  

        user@ubuntu:~$ sudo apt-get update

2.  Install `ifplugd`:  

        user@ubuntu:~$ sudo apt-get install ifplugd
        Reading package lists... Done
        Building dependency tree       
        Reading state information... Done
        Suggested packages:
          waproamd
        The following NEW packages will be installed:
          ifplugd
        0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
        Need to get 0 B/65.1 kB of archives.
        After this operation, 276 kB of additional disk space will be used.
        Preconfiguring packages ...
        Selecting previously unselected package ifplugd.
        (Reading database ... 193504 files and directories currently installed.)
        Preparing to unpack .../ifplugd_0.28-19ubuntu1_amd64.deb ...
        Unpacking ifplugd (0.28-19ubuntu1) ...
        Processing triggers for man-db (2.7.0.2-2) ...
        Processing triggers for ureadahead (0.100.0-16) ...
        user@ubuntu:~$

3.  Modify the default configuration for `ifplugd`. Use `vi`, `nano`, or your preferred text editor. You should see the following output if you are running `ifplugd` only for eth1 (normally you separate two or more interfaces with spaces, for example, `eth1 eth2 eth3`):

        cat /etc/default/ifplugd
        #(REMOVE GIANT COMMENT BLOCK FOR BREVITY)
        INTERFACES=""
        HOTPLUG_INTERFACES="eth1"
        ARGS="-q -f -u0 -d0 -w -I"
        SUSPEND_ACTION="none"

    Explanation of flags:

    | Flag | Description |
    | ---- | ----------- |
    | \-q  | Do not call the script for network shutdown when the daemon quits. |
    | \-f  | Ignore detection failures, retry instead. This option treats failures as "no link."  |
    | \-u0 | Specifies the delay for configuring the interface. |
    | \-d0 | Specifies the delay for de-configuring the interface. |
    | \-w  | When daemonizing (creating a background process), wait until the background process finishes with the initial link beat detection. When you enable this option, the parent process returns the link status on exit. *2* means it detects a link beat, *3* means it does not detect a link beat; everything else is an error. |
    | \-I  | Do not exit on a nonzero return value of the program executed on link change.  |
    | \-M  | Do not fail when the network interface is not available. Instead, use `netlink` to monitor device availability. The is useful for PCMCIA devices and similar. |

    To start `ifplugd`, use the `service ifplugd start` command:

        user@ubuntu:~$ sudo service ifplugd start
         * Network Interface Plugging Daemon...                                          
         * start eth1...                                                         
         [ OK ] 

    To check if `ifplugd` is running, use the `service ifplugd status` command:

        user@ubuntu:~$ sudo service ifplugd status
         * eth1:                                                                        
         ifplugd process for device eth1 running as pid 16327.
         * eth1:                                                                        
         ifplugd process for device eth1 running as pid 16327.
