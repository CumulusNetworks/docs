---
title: Network Command Line Utility
author: Cumulus Networks
weight: 87
aliases:
 - /display/CL31/Network+Command+Line+Utility
 - /pages/viewpage.action?pageId=5122114
pageID: 5122114
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
{{%notice warning%}}

**Early Access Feature**

`nclu` is an [early access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
in Cumulus Linux 3.1. Before you can install `nclu`, you must enable the
Early Access repository. For more information about the Cumulus Linux
repository, read [this knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/217422127).

{{%/notice%}}

The Network Command Line Utility, or NCLU, is a command line interface
for Cumulus Networks products, implemented in Cumulus Linux and VX 3.1
and later releases, with the goal of simplifying the networking
configuration process for all users.

The NCLU wrapper utility is called `net`. In 3.1 releases, `net` is
capable of configuring L2 and L3 features of the networking stack, as
well as providing monitoring and troubleshooting functionality for these
features. `/etc/network/interfaces` and `/etc/quagga/Quagga.conf` can
both be configured with `net`, in addition to running show and clear
commands related to ifupdown2 and Quagga.

{{%notice note%}}

In later releases, additional features will be available for
configuration, such as VXLANs and ACLs. However, they are not provided
in Cumulus Linux 3.1.

{{%/notice%}}

{{%notice note%}}

The Cumulus Linux 3.1 release of NCLU supports ifupdown2 and quagga.

{{%/notice%}}

## <span>Installation</span>

To install the `nclu` package, follow the instructions in the [Cumulus
Linux 3.1 release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/224473608#ea).

## <span>Configuration</span>

Configuration of the `net` utility is done in the `/etc/netd.conf` file.
This file can be configured to allow different permission levels for
users to edit configurations and run show commands.

| Configuration Variable | Default Setting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                             |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| show\_linux\_command   | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | When true, displays the linux command running in the background.                        |
| enable\_ifupdown2      | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Enables net wrapping of ifupdown2                                                       |
| enable\_quagga         | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Enables net wrapping of Quagga                                                          |
| users\_with\_edit      | root, cumulus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Sets the Linux users with root edit privileges                                          |
| groups\_with\_edit     | root, cumulus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Sets the Linux groups with root edit privilieges                                        |
| ifupdown\_blacklist    | address-purge, bond-ad-actor-sys-prio, bond-ad-actor-system, bond-mode, bond-num-grat-arp, bond-num-unsol-na, bond-use-carrier, bond-xmit-hash-policy, bridge-bridgeprio, bridge-fd, bridge-hashel, bridge-hashmax, bridge-hello, bridge-maxage, bridge-maxwait, bridge-mclmc, bridge-mclmi, bridge-mcmi, bridge-mcqi, bridge-mcqpi, bridge-mcqri, bridge-mcqv4src, bridge-mcrouter, bridge-mcsqc, bridge-mcsqi, bridge-pathcosts, bridge-port-pvids, bridge-port-vids, bridge-portmcfl, bridge-portmcrouter, bridge-portprios, bridge-waitport, broadcast, hwaddress, link-type, mstpctl-ageing, mstpctl-fdelay, mstpctl-forcevers, mstpctl-hello, mstpctl-maxage, mstpctl-maxhops, mstpctl-portp2p, mstpctl-portpathcost, mstpctl-portrestrrole, mstpctl-portrestrtcn, mstpctl-treeportcost, mstpctl-treeportprio, mstpctl-txholdcount, netmask, pre-down, pre-up, preferred-lifetime, scope, vxlan-ageing, vxlan-learning, up, down | Hides corner case command options from tab complete, to simplify and streamline output. |

{{%notice info%}}

**Net Tab Complete Output**

`net` provides an environment variable for setting where the `net`
output is directed. To only use `stdout`, set the NCLU\_TAB\_STDOUT
environment variable to *true*. The value is not case sensitive.

{{%/notice%}}

## <span>Getting Started</span>

NCLU uses the following workflow for staging and committing changes to
Cumulus Linux 3.1:

1.  Use the `net add` and `net del` commands to stage/remove
    configuration changes.

2.  Use the `net pending` command to review staged changes.

3.  Use `net commit` and `net abort` to commit/delete staged changes.

{{%notice note%}}

`net commit` applies the changes to `/etc/network/interfaces`, as well
as running `ifreload -a`.

{{%/notice%}}

NCLU provides a number of features to assist users. In addition to tab
completion and partial keyword commands identification, verification
checks are set in place to ensure correct syntax is used. The examples
below show the output for incorrect commands:

    cumulus@switch[~]# net add bgp router-id 1.1.1.1/32
    ERROR: Command not found
     
    Did you mean one of the following?
     
        net add bgp router-id <ipv4>
            This command is looking for an IP address, not an IP/prefixlen
     
    cumulus@switch[~]# net add bgp router-id 1.1.1.1
    cumulus@switch[~]# net add int swp10 mtu <TAB>
        <552-9216> : 
    cumulus@switch[~]# net add int swp10 mtu 9300
      ERROR: Command not found

NCLU has a comprehensive help system built in to assist usage. ` ?  `and
`help` can be used to show available commands:

    cumulus@switch[~]# net help
     
    Usage:
        # net <COMMAND> [<ARGS>] [help]
        #
        # net is a command line utility for networking on Cumulus Linux switches.
        #
        # COMMANDS are listed below and have context specific arguments which can
        # be explored by typing "?", "TAB", and "help" anytime while using net.
        #
        # Use 'man net' for a more comprehensive overview.
     
        net abort
        net commit [verbose]
        net help [verbose]
        net pending
        net show configuration [commands|files]
     
    Options:
     
        # Help commands
        help    : context sensitive information; see section below
        example : detailed examples of common workflows
     
        # Configuration commands
        add     : add/modify configuration (staged in commit buffer)
        del     : remove configuration (staged in commit buffer)
     
        # Commit buffer commands
        commit  : apply the commit buffer to the system
        pending : show changes staged in the commit buffer
        abort   : abandon changes in the commit buffer
     
        # Status commands
        show    : show command output
        clear   : clear counters, BGP neighbors, etc
     
    cumulus@switch[~]# net help bestpath
     
    The following commands contain keyword(s) 'bestpath':
     
        net (add|del) bgp bestpath as-path multipath-relax [as-set|no-as-set]
        net add debug bgp bestpath <ip/prefixlen>
        net del debug bgp bestpath [<ip/prefixlen>]
      net show [ip] bgp [ipv4|ipv6] [unicast|multicast] (<ip>|<ip/prefixlen>) [bestpath|multipath] [json]

{{%notice note%}}

Multiple interfaces can be configured at once:

    net add int swp7-9,12,15-17,22 mtu 9216

{{%/notice%}}

### <span>Built-In Examples</span>

The NCLU has a couple of built in examples to guide users through basic
configuration setup:

    cumulus@switch[~]# net example <TAB>
        bgp
        bond
        bridge
        clag
    …
        ospf    :  Open Shortest Path First
     
    cumulus@switch[~]# net example bridge 
     
    Scenario
    ========
    We are configuring switch1 and would like to configure the following
    - configure switch1 as an L2 switch for host-11 and host-12
    - enable vlans 10-20
    - place host-11 in vlan 10
    - place host-12 in vlan 20
    - create an SVI interface for vlan 10
    - create an SVI interface for vlan 20
    - assign IP 10.0.0.1/24 to the SVI for vlan 10
    - assign IP 20.0.0.1/24 to the SVI for vlan 20
    - configure swp3 as a trunk for vlans 10, 11, 12 and 20
     
                  swp3
         *switch1 --------- switch2
            /\
      swp1 /  \ swp2
          /    \
         /      \
     host-11   host-12
     
     
    switch1 net commands
    ====================
    - enable vlans 10-20
    switch1# net add vlan 10-20
     
    - place host-11 in vlan 10
    - place host-12 in vlan 20
    switch1# net add int swp1 bridge-access 10
    switch1# net add int swp2 bridge-access 20
     
    - create an SVI interface for vlan 10
    - create an SVI interface for vlan 20
    - assign IP 10.0.0.1/24 to the SVI for vlan 10
    - assign IP 20.0.0.1/24 to the SVI for vlan 20
    switch1# net add vlan-interface vlan10 address 10.0.0.1/24
    switch1# net add vlan-interface vlan20 address 20.0.0.1/24
     
    - configure swp3 as a trunk for vlans 10, 11, 12 and 20
    switch1# net add int swp3 bridge-trunk vlans 10-12,20
     
    # Review and commit changes
    switch1# net pending
    switch1# net commit
     
     
    Verification
    ============
    switch1# net show bridge
    switch1# net show l2
