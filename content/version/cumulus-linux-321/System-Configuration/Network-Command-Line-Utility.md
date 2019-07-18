---
title: Network Command Line Utility
author: Cumulus Networks
weight: 57
aliases:
 - /display/CL321/Network+Command+Line+Utility
 - /pages/viewpage.action?pageId=5126772
pageID: 5126772
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
The Network Command Line Utility, or NCLU, is a command line interface
for Cumulus Networks products, implemented in Cumulus Linux and VX 3.1
and later releases, with the goal of simplifying the networking
configuration process for all users.

NCLU resides in the Linux user space, as seen below. It provides
consistent access to networking commands directly via bash, thereby
making configuration and troubleshooting simple and easy — no need to
edit files or enter modes and sub-modes. In addition, NCLU does more
than traditional command line interfaces by:

  - Embedding help, examples and automatic command checking with
    suggestions in case you’ve entered a typo

  - Running directly from and integrating with bash, while being
    interoperable with the regular way of accessing underlying
    configuration files and automation

  - Automatically configuring dependent features so you don’t have to

{{% imgOld 0 %}}

The NCLU wrapper utility is called `net`. `net` is capable of
configuring L2 and L3 features of the networking stack, installing ACLs
and VXLANs, rolling back and deleting snapshots, as well as providing
monitoring and troubleshooting functionality for these features.
`/etc/network/interfaces` and `/etc/quagga/Quagga.conf` can both be
configured with `net`, in addition to running show and clear commands
related to `ifupdown2` and Quagga.

## <span>Installing NCLU</span>

If you upgraded Cumulus Linux from a version earlier than 3.2 instead of
performing a full binary install, you need to install the `nclu` package
on your switch:

    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get install nclu
    cumulus@switch:~$ sudo apt-get upgrade

{{%notice note%}}

The `nclu` package installs a new bash completion script, and displays
the following message when it is manually installed:

    null

{{%/notice%}}

## <span>Getting Started</span>

NCLU uses the following workflow for staging and committing changes to
Cumulus Linux:

1.  Use the `net add` and `net del` commands to stage/remove
    configuration changes.

2.  Use the `net pending` command to review staged changes.

3.  Use `net commit` and `net abort` to commit/delete staged changes.

{{%notice note%}}

`net commit` applies the changes to the relevant configuration files,
such as `/etc/network/interfaces`, then runs necessary follow on
commands to enable the configuration, such as `ifreload -a`.

{{%/notice%}}

Once you have a running configuration, you can review and update it
using:

  - `net show`: A series of commands for viewing various parts of the
    network configuration, such as `net show configuration`, `net show
    commit history` and `net show bgp` to view the complete network
    configuration, a history of commits using NCLU and BGP status,
    respectively.

  - `net clear`: A way to clear `netstat` counters, BGP and OSPF
    neighbor content, and more.

  - `net rollback`: Provides a mechanism to revert back to an earlier
    configuration.

### <span>Tab Completion, Verification and Inline Help</span>

NCLU provides a number of features to assist users. In addition to tab
completion and partial keyword commands identification, verification
checks are set in place to ensure correct syntax is used. The examples
below show the output for incorrect commands:

    cumulus@switch:~$ net add bgp router-id 1.1.1.1/32
    ERROR: Command not found
     
    Did you mean one of the following?
     
        net add bgp router-id <ipv4>
            This command is looking for an IP address, not an IP/prefixlen
     
    cumulus@switch:~$ net add bgp router-id 1.1.1.1
    cumulus@switch:~$ net add int swp10 mtu <TAB>
        <552-9216> : 
    cumulus@switch:~$ net add int swp10 mtu 9300
    ERROR: Command not found
     
    Did you mean one of the following?
        net add interface <interface> mtu <552-9216>

NCLU has a comprehensive help system built in to assist usage. In
addition to the net man page, you can use ` ?  `and `help` to display
available commands:

    cumulus@switch:~$ net help
     
    Usage:
        # net <COMMAND> [<ARGS>] [help]
        #
        # net is a command line utility for networking on Cumulus Linux switches.
        #
        # COMMANDS are listed below and have context specific arguments which can
        # be explored by typing "<TAB>" or "help" anytime while using net.
        #
        # Use 'man net' for a more comprehensive overview.
     
     
        net abort
        net commit [verbose] [confirm] [description <wildcard>]
        net commit delete (<number>|<number-range>)
        net help [verbose]
        net pending
        net rollback (<number>|last)
        net show commit (history|<number>|<number-range>|last)
        net show rollback (<number>|last)
        net show configuration [commands|files|acl|bgp|ospf|ospf6|interface <interface>]
     
     
    Options:
     
     
        # Help commands
        help     : context sensitive information; see section below
        example  : detailed examples of common workflows
     
     
        # Configuration commands
        add      : add/modify configuration
        del      : remove configuration
     
     
        # Commit buffer commands
        abort    : abandon changes in the commit buffer
        commit   : apply the commit buffer to the system
        pending  : show changes staged in the commit buffer
        rollback : revert to a previous configuration state
     
     
        # Status commands
        show     : show command output
        clear    : clear counters, BGP neighbors, etc
     
    cumulus@switch:~$ net help bestpath
    The following commands contain keyword(s) 'bestpath'
     
        net (add|del) bgp bestpath as-path multipath-relax [as-set|no-as-set]
        net (add|del) bgp bestpath compare-routerid
        net (add|del) bgp bestpath med missing-as-worst
        net (add|del) bgp vrf <text> bestpath as-path multipath-relax [as-set|no-as-set]
        net (add|del) bgp vrf <text> bestpath compare-routerid
        net (add|del) bgp vrf <text> bestpath med missing-as-worst
        net add bgp debug bestpath <ip/prefixlen>
        net del bgp debug bestpath [<ip/prefixlen>]
        net show bgp (<ipv4>|<ipv4/prefixlen>) [bestpath|multipath] [json]
        net show bgp (<ipv6>|<ipv6/prefixlen>) [bestpath|multipath] [json]
        net show bgp vrf <text> (<ipv4>|<ipv4/prefixlen>) [bestpath|multipath] [json]

{{%notice note%}}

Multiple interfaces can be configured at once:

    cumulus@switch:~$ net add int swp7-9,12,15-17,22 mtu 9216

{{%/notice%}}

### <span>Built-In Examples</span>

The NCLU has a number of built in examples to guide users through basic
configuration setup:

    cumulus@switch:~$ net example 
        acl              :  access-list
        bgp              :  Border Gateway Protocol
        bond             :  Bond, port-channel, etc
        bridge           :  interface
        clag             :  Multi-Chassis Link Aggregation
        link-settings    :  Physical link parameters
        lnv              :  Lightweight Network Virtualization
        management-vrf   :  Management VRF
        ospf             :  Open Shortest Path First (OSPFv2)
        vlan-interfaces  :  IP interfaces for VLANs
     
    cumulus@switch:~$ net example bridge 
     
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
    switch1# net add int swp1 bridge access 10
    switch1# net add int swp2 bridge access 20
    - create an SVI interface for vlan 10
    - create an SVI interface for vlan 20
    - assign IP 10.0.0.1/24 to the SVI for vlan 10
    - assign IP 20.0.0.1/24 to the SVI for vlan 20
    switch1# net add vlan 10 ip address 10.0.0.1/24
    switch1# net add vlan 20 ip address 20.0.0.1/24
    - configure swp3 as a trunk for vlans 10, 11, 12 and 20
    switch1# net add int swp3 bridge trunk vlans 10-12,20
    # Review and commit changes
    switch1# net pending
    switch1# net commit
     
    Verification
    ============
    switch1# net show interface
    switch1# net show bridge macs

## <span>Adding More NCLU Users or Groups</span>

If you've created custom users or groups on your Cumulus Linux switches,
you can configure those users to be able to run NCLU commands.

To do so, edit the `/etc/netd.conf` file, and add those users to the
*users\_with\_edit* and *users\_with\_show* lines in the file, then save
the file.

    cumulus@switch:~$ sudo nano /etc/netd.conf
     
    # Control which users/groups are allowed to run 'add', 'del',
    # 'clear', 'net abort', 'net commit' and restart services (quagga, etc)
    # to apply those changes
    users_with_edit = root, cumulus
    groups_with_edit = root, cumulus
     
     
    # Control which users/groups are allowed to run 'show' commands
    users_with_show = root, cumulus
    groups_with_show = root, cumulus

Similarly, to configure a new user group to use NCLU, add that group to
the *groups\_with\_edit* and *groups\_with\_show* lines in the file.

## <span>Restarting the netd Service</span>

Whenever you modify `netd.conf`, you must restart the `netd` service for
the changes to take effect:

    cumulus@switch:~$ sudo systemctl restart netd.service

## <span>Advanced Configuration</span>

NCLU needs no initial configuration; it's ready to go in Cumulus Linux.
However, if you need to modify its configuration, you must manually
update the `/etc/netd.conf` file. This file can be configured to allow
different permission levels for users to edit configurations and run
show commands. It also contains a blacklist that hides less frequently
used terms from the tabbed autocomplete.

| Configuration Variable | Default Setting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                                                             |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| show\_linux\_command   | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | When true, displays the Linux command running in the background.                        |
| enable\_ifupdown2      | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Enables `net` wrapping of `ifupdown2` commands.                                         |
| enable\_quagga         | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Enables `net` wrapping of Quagga commands.                                              |
| users\_with\_edit      | root, cumulus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Sets the Linux users with root edit privileges.                                         |
| groups\_with\_edit     | root, cumulus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Sets the Linux groups with root edit privileges.                                        |
| users\_with\_show      | root, cumulus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Controls which users are allowed to run `show` commands.                                |
| groups\_with\_show     | root, cumulus                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Controls which groups are allowed to run `show` commands.                               |
| ifupdown\_blacklist    | address-purge, bond-ad-actor-sys-prio, bond-ad-actor-system, bond-mode, bond-num-grat-arp, bond-num-unsol-na, bond-use-carrier, bond-xmit-hash-policy, bridge-bridgeprio, bridge-fd, bridge-hashel, bridge-hashmax, bridge-hello, bridge-maxage, bridge-maxwait, bridge-mclmc, bridge-mclmi, bridge-mcmi, bridge-mcqi, bridge-mcqpi, bridge-mcqri, bridge-mcrouter, bridge-mcsqc, bridge-mcsqi, bridge-pathcosts, bridge-port-pvids, bridge-port-vids, bridge-portprios, bridge-stp, bridge-waitport, broadcast, hwaddress, link-type, mstpctl-ageing, mstpctl-fdelay, mstpctl-forcevers, mstpctl-hello, mstpctl-maxage, mstpctl-maxhops, mstpctl-portp2p, mstpctl-portpathcost, mstpctl-portrestrrole, mstpctl-portrestrtcn, mstpctl-treeportcost, mstpctl-treeportprio, mstpctl-txholdcount, netmask, preferred-lifetime, scope, vxlan-ageing, vxlan-learning, up, down, bridge-ageing, bridge-gcint, bridge-mcqifaddr, bridge-mcqv4src | Hides corner case command options from tab complete, to simplify and streamline output. |

{{%notice info%}}

**Net Tab Complete Output**

`net` provides an environment variable for setting where the `net`
output is directed. To only use `stdout`, set the NCLU\_TAB\_STDOUT
environment variable to *true*. The value is not case sensitive.

{{%/notice%}}

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
