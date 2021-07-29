---
title: Network Command Line Utility - NCLU
author: NVIDIA
weight: 110
toc: 3
---
The Network Command Line Utility (NCLU) is a command line interface that simplifies the networking configuration process for all users.

NCLU resides in the Linux user space and provides consistent access to networking commands directly through bash, making configuration and troubleshooting simple and easy; no need to edit files or enter modes and sub-modes. NCLU provides these benefits:

- Embeds help, examples, and automatic command checking with suggestions in case you enter a typo.
- Runs directly from and integrates with bash, while being interoperable with the regular way of accessing underlying configuration files and automation.
- Configures dependent features automatically so that you do not have to.

{{<img src = "/images/cumulus-linux/nclu-architecture.png">}}

The NCLU wrapper utility called `net` is capable of configuring layer 2 and layer 3 features of the networking stack, installing ACLs and VXLANs, restoring configuration files, as well as providing monitoring and troubleshooting functionality for these features. You can configure both the `/etc/network/interfaces` and `/etc/frr/frr.conf` files with `net`, in addition to running show and clear commands related to `ifupdown2` and FRRouting.

## NCLU Basics

Use the following workflow to stage and commit changes to Cumulus Linux with NCLU:

1. Use the `net add` and `net del` commands to stage and remove configuration changes.
2. Use the `net pending` command to review staged changes.
3. Use `net commit` and `net abort` to commit and delete staged changes.

{{%notice note%}}

`net commit` applies the changes to the relevant configuration files, such as `/etc/network/interfaces`, then runs necessary follow on commands to enable the configuration, such as `ifreload -a`.

If two different users try to commit a change at the same time, NCLU displays a warning but implements the change according to the first commit received. The second user needs to abort the commit.

{{%/notice%}}

When you have a running configuration, you can review and update the configuration with the following commands:

- `net show` is a series of commands for viewing various parts of the network configuration. For example, use `net show configuration` to view the complete network configuration, `net show commit history` to view a history of commits using NCLU, and `net show bgp` to view BGP status.
- `net clear` provides a way to clear `net show` counters, BGP and OSPF neighbor content, and more.
- `net rollback` provides a mechanism to revert back to an earlier configuration.
- `net commit confirm` requires you to press *Enter* to commit changes using NCLU. If you run `net commit confirm` but do not press *Enter* within 10 seconds, the commit automatically reverts and no changes are made.
- `net commit description <description>` enables you to provide a descriptive summary of the changes you are about to commit.
- `net commit permanent` retains the {{<link url="Back-up-and-Restore" text="backup file">}} taken when committing the change. Otherwise, the backup files created from NCLU commands are cleaned up periodically.
- `net del all` deletes all configurations.

    {{%notice note%}}

The `net del all` command does not remove {{<link url="Management-VRF" text="management VRF">}} configurations; NCLU does not interact with eth0 interfaces and management VRF.

    {{%/notice%}}

### Tab Completion, Verification, and Inline Help

In addition to tab completion and partial keyword command identification, NCLU includes verification checks to ensure you use the correct syntax. The examples below show the output for incorrect commands:

```
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
```

NCLU has a comprehensive built in help system. In addition to the net man page, you can use `?`and `help` to display available commands:

```
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
    net commit [verbose] [confirm [<number-seconds>]] [description <wildcard>]
    net commit permanent <wildcard>
    net del all
    net help [verbose]
    net pending [json]
    net rollback (<number>|last)
    net rollback description <wildcard-snapshot>
    net show commit (history|<number>|last)
    net show rollback (<number>|last)
    net show rollback description <wildcard-snapshot>
    net show configuration [commands|files|acl|bgp|multicast|ospf|ospf6]
    net show configuration interface [<interface>] [json]

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
    net (add|del) bgp ipv4 labeled-unicast neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp ipv4 unicast neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp ipv6 labeled-unicast neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp ipv6 unicast neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp vrf <text> bestpath as-path multipath-relax [as-set|no-as-set]
    net (add|del) bgp vrf <text> bestpath compare-routerid
    net (add|del) bgp vrf <text> bestpath med missing-as-worst
    net (add|del) bgp vrf <text> ipv4 labeled-unicast neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp vrf <text> ipv4 unicast neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp vrf <text> ipv6 labeled-unicast neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp vrf <text> ipv6 unicast neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net (add|del) bgp vrf <text> neighbor <bgppeer> addpath-tx-bestpath-per-AS
    net add bgp debug bestpath <ip/prefixlen>
    net del bgp debug bestpath [<ip/prefixlen>]
    net show bgp (<ipv4>|<ipv4/prefixlen>|<ipv6>|<ipv6/prefixlen>) [bestpath|multipath] [json]
    net show bgp vrf <text> (<ipv4>|<ipv4/prefixlen>|<ipv6>|<ipv6/prefixlen>) [bestpath|multipath] [json]
```

{{%notice note%}}

You can configure multiple interfaces at the same time:

```
cumulus@switch:~$ net add int swp7-9,12,15-17,22 mtu 9216
```

{{%/notice%}}

### Search for Specific Commands

To search for specific NCLU commands so that you can identify the correct syntax to use, run the `net help verbose | <term>` command. For example, to show only commands that include `clag` (for MLAG):

```
cumulus@leaf01:mgmt:~$ net help verbose | grep clag
    net example clag basic-clag
    net example clag l2-with-server-vlan-trunks
    net example clag l3-uplinks-virtual-address
    net add clag peer sys-mac <mac-clag> interface <interface> (primary|secondary) [backup-ip <ipv4>]
    net add clag peer sys-mac <mac-clag> interface <interface> (primary|secondary) [backup-ip <ipv4> vrf <text>]
    net del clag peer
    net add clag port bond <interface> interface <interface> clag-id <0-65535>
    net del clag port bond <interface>
    net show clag [our-macs|our-multicast-entries|our-multicast-route|our-multicast-router-ports|peer-macs|peer-multicast-entries|peer-multicast-route|peer-multicast-router-ports|params|backup-ip|id] [verbose] [json]
    net show clag macs [<mac>] [json]
    net show clag neighbors [verbose]
    net show clag peer-lacp-rate
    net show clag verify-vlans [verbose]
    net show clag status [verbose] [json]
    net add bond <interface> clag id <0-65535>
    net add interface <interface> clag args <wildcard>
    net add interface <interface> clag backup-ip (<ipv4>|<ipv4> vrf <text>)
    net add interface <interface> clag enable (yes|no)
    net add interface <interface> clag peer-ip (<ipv4>|<ipv6>|linklocal)
    net add interface <interface> clag priority <0-65535>
    net add interface <interface> clag sys-mac <mac>
    net add loopback lo clag vxlan-anycast-ip <ipv4>
    net del bond <interface> clag id [<0-65535>]
    net del interface <interface> clag args [<wildcard>]
    ...
```

### Add ? (Question Mark) Ability to NCLU

While tab completion is enabled by default, you can also configure NCLU to use the **?** (question mark character) to look at available commands. To enable this feature for the *cumulus* user, open the following file:

```
cumulus@switch:~$ sudo nano ~/.inputrc
```
<!-- vale off -->
Uncomment the very last line in the `.inputrc` file so that the file changes from this:
<!-- vale on -->
```
# Uncomment to use ? as an alternative to
# ?: complete
```

to this:

```
# Uncomment to use ? as an alternative to
?: complete
```

Save the file and reconnect to the switch. The ? (question mark) ability does not work on all subsequent sessions on the switch.

```
cumulus@switch:~$ net
    abort     :  abandon changes in the commit buffer
    add       :  add/modify configuration
    clear     :  clear counters, BGP neighbors, etc
    commit    :  apply the commit buffer to the system
    del       :  remove configuration
    example   :  detailed examples of common workflows
    help      :  Show this screen and exit
    pending   :  show changes staged in the commit buffer
    rollback  :  revert to a previous configuration state
    show      :  show command output
```

{{%notice note%}}

When the question mark is typed, NCLU autocompletes and shows all available options, but the question mark does not actually appear on the terminal. This is expected behavior.

{{%/notice%}}
<!-- vale off -->
### Built-in Examples
<!-- vale on -->
NCLU has built in examples to guide you through basic configuration setup:

```
cumulus@switch:~$ net example
    acl              :  access-list
    bgp              :  Border Gateway Protocol
    bond             :  bond, port-channel, etc
    bridge           :  a layer2 bridge
    clag             :  Multi-Chassis Link Aggregation
    dhcp             :  Dynamic Host Configuration Protocol
    dot1x            :  Configure, Enable, Delete or Show IEEE 802.1X EAPOL
    evpn             :  Ethernet VPN
    link-settings    :  Physical link parameters
    management-vrf   :  Management VRF
    mlag             :  Multi-Chassis Link Aggregation
    ospf             :  Open Shortest Path First (OSPFv2)
    snmp-server      :  Configure the SNMP server
    syslog           :  Set syslog logging
    vlan-interfaces  :  IP interfaces for VLANs
    voice-vlan       :  VLAN used for IP Phones
    vrr              :  add help text
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
switch1# net pending
switch1# net commit

Verification
============
switch1# net show interface
switch1# net show bridge macs
```

## Configure User Accounts

You can configure user accounts in Cumulus Linux with read-only or edit permissions for NCLU:

- You create user accounts with **read-only** permissions for NCLU by adding them to the `netshow` group. A user in the `netshow` group can run NCLU `net show` commands, such as `net show interface` or `net show config`, and certain general Linux commands, such as `ls`, `cd` or `man`, but cannot run `net add`, `net del` or `net commit` commands.
- You create user accounts with **edit** permissions for NCLU by adding them to the `netedit` group. A user in the `netedit` group can run NCLU configuration commands, such `net add`, `net del` or `net commit` in addition to NCLU `net show` commands.

The examples below add a new user account and modify an existing user account called *myuser*.

To add a new user account with NCLU show permissions:

```
cumulus@switch:~$ sudo adduser --ingroup netshow myuser
Adding user `myuser' ...
Adding new user `myuser' (1001) with group `netshow'...
...
```

To add NCLU show permissions to a user account that already exists:

```
cumulus@switch:~$ sudo addgroup myuser netshow
Adding user `myuser' to group `netshow' ...
Adding user myuser to group netshow
Done
```

To add a new user account with NCLU edit permissions:

```
cumulus@switch:~$ sudo adduser --ingroup netedit myuser
Adding user `myuser' ...
Adding new user `myuser' (1001) with group `netedit'
...
```

To add NCLU edit permissions to a user account that already exists:

```
cumulus@switch:~$ sudo addgroup myuser netedit
Adding user `myuser' to group `netedit' ...
Adding user myuser to group netedit
Done
```

{{%notice note%}}

You can use the `adduser` command for local user accounts only. You can use the `addgroup` command for both local and remote user accounts. For a remote user account, you must use the mapping username, such as `tacacs3` or `radius_user`, not the {{<link url="TACACS" text="TACACS">}} or {{<link url="RADIUS-AAA" text="RADIUS">}} account name.

{{%/notice%}}

If the user tries to run commands that are not allowed, the following error displays:

```
myuser@switch:~$ net add hostname host01
ERROR: User username does not have permission to make networking changes.
```
<!-- vale off -->
## Edit the netd.conf File
<!-- vale on -->
Instead of using the NCLU commands described above, you can manually configure users and groups to be able to run NCLU commands.

Edit the `/etc/netd.conf` file to add users to the *users\_with\_edit* and *users\_with\_show* lines in the file, then save the file.

For example, if you want the user *netoperator* to be able to run both edit and show commands, add the user to the `users_with_edit` and `users_with_show` lines in the `/etc/netd.conf` file:

```
cumulus@switch:~$ sudo nano /etc/netd.conf

# Control which users/groups are allowed to run 'add', 'del',
# 'clear', 'net abort', 'net commit' and restart services
# to apply those changes
users_with_edit = root, cumulus, netoperator
groups_with_edit = netedit

# Control which users/groups are allowed to run 'show' commands
users_with_show = root, cumulus, netoperator
groups_with_show = netshow, netedit
```

To configure a new user group to use NCLU, add that group to the `groups_with_edit` and `groups_with_show` lines in the file.

{{%notice warning%}}

Use caution giving edit permissions to groups. For example, do not give edit permissions to the {{<link url="TACACS" text="*tacacs* group">}}.

{{%/notice%}}

## Restart the netd Service

Whenever you modify `netd.conf` or when NSS services change, you must restart the `netd` service for the changes to take effect:

```
cumulus@switch:~$ sudo systemctl restart netd.service
```

## Back Up the Configuration to a Single File

You can easily back up your NCLU configuration to a file by outputting the results of `net show configuration commands` to a file, then retrieving the contents of the file using the `source` command. You can then view the configuration at any time or copy it to other switches and use the `source` command to apply that configuration to those switches.

For example, to copy the configuration of a leaf switch called leaf01, run the following command:

```
cumulus@leaf01:~$ net show configuration commands >> leaf01.txt
```

With the commands all stored in a single file, you can now copy this file to another ToR switch in your network called leaf01 and apply the configuration by running:

```
cumulus@leaf01:~$ source leaf01.txt
```

## Advanced Configuration

NCLU needs no initial configuration; however, if you need to modify certain configuration, you must manually update the `/etc/netd.conf` file. You can configure this file to allow different permission levels for users to edit configurations and run `show` commands. The file also contains a blacklist that hides less frequently used terms from the tabbed autocomplete.

After you edit the `netd.conf` file, restart the `netd` service for the changes to take effect.

```
cumulus@switch:~$ sudo nano /etc/netd.conf
cumulus@switch:~$ sudo systemctl restart netd.service
```
<!-- vale off -->
| Configuration Variable <img width=150/>| Default Setting <img width=250/>|Description <img width=200/>|
|-------------------------------------- |------------------------------- |--------------------------- |
| show_linux_command | False | When true, displays the Linux command running in the background. |
| color_diffs | True | When true, the diffs shown in net pending and net commit use colors. |
| enable_`<component>` | True | When true, enables you to configure the `component` with NCLU. For example, when `enable_frr` is `true`, you can use NCLU to configure FRR. |
| users_with_edit | root, cumulus | Sets the Linux users with root edit privileges.|
| groups_with_edit | root, cumulus | Sets the Linux groups with root edit privileges.|
| users_with_show | root, cumulus | Controls which users are allowed to run show commands.|
| groups_with_show | root, cumulus | Controls which groups are allowed to run show commands.|
| ifupdown_blacklist | address-purge, bond-ad-actor-sys-prio, bond-ad-actor-system, bond-num-grat-arp,bond-num-unsol-na, bond-use-carrier, bond-xmit-hash-policy, bridge-bridgeprio, bridge-fd, bridge-hashel, bridge-hashmax, bridge-hello, bridge-igmp-querier-src, bridge-maxage, bridge-maxwait, bridge-mclmc, bridge-mclmi bridge-mcmi, bridge-mcqi, bridge-mcqpi, bridge-mcqri, bridge-mcrouter, bridge-mcsqc, bridge-mcsqi, bridge-pathcosts, bridge-port-pvids, bridge-port-vids, bridge-portprios, bridge-waitport, broadcast, link-type, mstpctl-ageing, mstpctl-fdelay, mstpctl-forcevers, mstpctl-hello, mstpctl-maxage, mstpctl-maxhops, mstpctl-portp2p, mstpctl-portpathcost, mstpctl-portrestrtcn, mstpctl-treeportcost, mstpctl-treeportprio, mstpctl-txholdcount, netmask, preferred-lifetime, scope, vxlan-ageing, vxlan-learning, vxlan-port, up, down, bridge-gcint, bridge-mcqifaddr, bridge-mcqv4src|Hides corner case command options from tab complete, to simplify and streamline output. |
<!-- vale on -->
{{%notice info%}}

`net` provides an environment variable to set where the `net` output is directed. To only use `stdout`, set the `NCLU_TAB_STDOUT` environment variable to *true*. The value is not case sensitive.

{{%/notice%}}

## Considerations

### Unsupported Interface Names

NCLU does not support interfaces named `dev`.

### Bonds With No Configured Members

If a bond interface is configured and contains no members, NCLU reports that the interface does not exist.

### Large NCLU Inputs

Each NCLU command must be parsed by the system. Large inputs, such as a large paste of NCLU commands can take some time, sometimes minutes, to process.
