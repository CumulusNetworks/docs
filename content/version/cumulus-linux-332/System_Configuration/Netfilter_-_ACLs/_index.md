---
title: Netfilter - ACLs
author: Cumulus Networks
weight: 69
aliases:
 - /display/CL332/Netfilter+-+ACLs
 - /pages/viewpage.action?pageId=5868887
pageID: 5868887
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
---
[Netfilter](http://www.netfilter.org/) is the packet filtering framework
in Cumulus Linux as well as most other Linux distributions. There are a
number of tools available for configuring ACLs in Cumulus Linux,
including:

  - `iptables`, `ip6tables` and `ebtables` are Linux userspace tools to
    administer filtering rules for IPv4 packets, IPv6 packets and
    Ethernet frames (layer 2 using MAC addresses) respectively.

  - [NCLU](/version/cumulus-linux-332/System_Configuration/Network_Command_Line_Utility),
    a Cumulus Linux-specific userspace tool for configuring custom ACLs.

  - `cl-acltool`, another Cumulus Linux-specific userspace tool to
    administer filtering rules and for configuring the default ACLs.

NCLU and `cl-acltool` operate on various configuration files, and use
`iptables`, `ip6tables` and `ebtables` to install rules into the kernel.
In addition to programming rules in the kernel, NCLU and `cl-acltool`
program rules in hardware for interfaces involving switch port
interfaces, which `iptables`, `ip6tables` and `ebtables` cannot do on
their own.

{{%notice note%}}

In many instances, you can use NCLU to configure ACLs; however,
`cl-acltool` must be used in some cases. The examples below show when to
use which tool.

{{%/notice%}}

{{%notice tip%}}

If you need help getting started setting up ACLs, run `net example acl`
to see a basic configuration:

Click to see the example ...

    cumulus@leaf01:~$ net example acl 
     
    Scenario
    ========
    We would like to use access-lists on 'switch' to
    - Restrict inbound traffic on swp1 to traffic from 10.1.1.0/24 destined for 10.1.2.0/24
    - Restrict outbound traffic on swp2 to http, https, or ssh
     
     
         *switch
            /\
      swp1 /  \ swp2
          /    \
         /      \
     host-11   host-12
     
     
     
    switch net commands
    ====================
     
    Create an ACL that accepts traffic from 10.1.1.0/24 destined for 10.1.2.0/24
    and drops all other traffic
     
    switch# net add acl ipv4 MYACL accept source-ip 10.1.1.0/24 dest-ip 10.1.2.0/24
    switch# net add acl ipv4 MYACL drop source-ip any dest-ip any
     
    Apply MYACL inbound on swp1
     
    switch# net add interface swp1 acl ipv4 MYACL inbound
     
    Create an ACL that accepts http, https, or ssh traffic and drops all
    other traffic.
     
    switch# net add acl ipv4 WEB_OR_SSH accept tcp source-ip any source-port any dest-ip any dest-port http
    switch# net add acl ipv4 WEB_OR_SSH accept tcp source-ip any source-port http dest-ip any dest-port any
    switch# net add acl ipv4 WEB_OR_SSH accept tcp source-ip any source-port any dest-ip any dest-port https
    switch# net add acl ipv4 WEB_OR_SSH accept tcp source-ip any source-port https dest-ip any dest-port any
    switch# net add acl ipv4 WEB_OR_SSH accept tcp source-ip any source-port any dest-ip any dest-port ssh
    switch# net add acl ipv4 WEB_OR_SSH accept tcp source-ip any source-port ssh dest-ip any dest-port any
    switch# net add acl ipv4 WEB_OR_SSH drop source-ip any dest-ip any
     
    Apply WEB_OR_SSH outbound on swp2
    switch# net add interface swp2 acl ipv4 WEB_OR_SSH outbound
     
    commit the staged changes
    switch# net commit
     
    Verification
    ============
    switch# net show configuration acl

{{%/notice%}}

## <span>Understanding Traffic Rules In Cumulus Linux</span>

### <span>Understanding Chains</span>

Netfilter describes the mechanism for which packets are classified and
controlled in the Linux kernel. Cumulus Linux uses the Netfilter
framework to control the flow of traffic to, from and across the switch.
Netfilter does not require a separate software daemon to run because it
is part of the Linux kernel itself. Netfilter asserts policies at layers
2, 3 and 4 of the [OSI model](https://en.wikipedia.org/wiki/OSI_model)
by inspecting packet and frame headers based on a list of rules. Rules
are defined using syntax provided by the `iptables`, `ip6tables` and
`ebtables` userspace applications.

The rules created by these programs inspect or operate on packets at
several points in the life of the packet through the system. These five
points are known as *chains* and are shown here:

{{% imgOld 0 %}}

The chains and their uses are:

  - **PREROUTING**: Touches packets before they are routed

  - **INPUT:** Touches packets once they are determined to be destined
    for the local system but before they are received by the control
    plane software

  - **FORWARD**: Touches transit traffic as it moves through the box

  - **OUTPUT**: Touches packets that are sourced by the control plane
    software before they are put on the wire

  - **POSTROUTING**: Touches packets immediately before they are put on
    the wire but after the routing decision has been made

### <span>Understanding Tables</span>

When building rules to affect the flow of traffic, the individual chains
can be accessed by *tables*. Linux provides three tables by default:

  - **Filter**: Classifies traffic or filters traffic

  - **NAT**: Applies Network Address Translation rules
    
    {{%notice note%}}
    
    Cumulus Linux does not support NAT.
    
    {{%/notice%}}

  - **Mangle**: Alters packets as they move through the switch

Each table has a set of default chains that can be used to modify or
inspect packets at different points of the path through the switch.
Chains contain the individual rules to influence traffic. Each table and
the default chains they support are shown below. Tables and chains in
green are supported by Cumulus Linux, those in red are not supported
(that is, they are not hardware accelerated) at this time.

{{% imgOld 1 %}}

{{% imgOld 2 %}}

{{% imgOld 3 %}}

### <span>Understanding Rules</span>

Rules are the items that actually classify traffic to be acted upon.
Rules are applied to chains, which are attached to tables, similar to
the graphic below.

{{% imgOld 4 %}}

Rules have several different components; the examples below highlight
those different components.

{{% imgOld 5 %}}

  - **Table:** The first argument is the *table*. Notice the second
    example does not specify a table, that is because the filter table
    is implied if a table is not specified.

  - **Chain:** The second argument is the *chain*. Each table supports
    several different chains. See Understanding Tables above.

  - **Matches:** The third argument(s) are called the *matches*. You can
    specify multiple matches in a single rule. However, the more matches
    you use in a rule, the more memory that rule consumes.

  - **Jump:** The *jump* specifies the target of the rule; that is, what
    action to take if the packet matches the rule. If this option is
    omitted in a rule, then matching the rule will have no effect on the
    packet's fate, but the counters on the rule will be incremented.

  - **Target(s):** The *target* can be a user-defined chain (other than
    the one this rule is in), one of the special built-in targets that
    decides the fate of the packet immediately (like DROP), or an
    extended target. See the [Supported Rule Types and Common
    Usages](#src-5868887_Netfilter-ACLs-supported) section below for
    examples of different targets.

### <span>How Rules Are Parsed and Applied</span>

All the rules from each chain are read from `iptables`, `ip6tables` and
`ebtables` and entered in order into either the filter table or the
mangle table. The rules are read from the kernel in the following order:

  - IPv6 (`ip6tables`)

  - IPv4 (`iptables`)

  - `ebtables`

When rules are combined and put into one table, the order determines the
relative priority of the rules; `iptables` and `ip6tables` have the
highest precedence and `ebtables` has the lowest.

The Linux packet forwarding construct is an overlay for how the silicon
underneath processes packets; to that end, here are some things to be
aware of:

  - The order of operations for how rules are processed is not perfectly
    maintained when you compare how `iptables` and the switch silicon
    process packets. The switch silicon reorders rules when `switchd`
    writes to the ASIC, whereas traditional `iptables` executes the list
    of rules in order.

  - All rules are terminating. This means once a rule is matched, the
    action is carried out, and no more rules are processed. The
    exception to this is when a SETCLASS rule is placed immediately
    before another rule; this exists multiple times in the default ACL
    configuration.  
    In the example below, the SETCLASS action applied with the
    `--in-interface` option, creates the internal ASIC classification,
    and **continues to process** the next rule, which does the
    rate-limiting for the matched protocol:
    
        -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p udp --dport $BFD_ECHO_PORT -j SETCLASS --class 7
        -A $INGRESS_CHAIN -p udp --dport $BFD_ECHO_PORT -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000
    
    {{%notice warning%}}
    
    If multiple contiguous rules with the same match criteria are
    applied to `--in-interface`, **only** the first rule gets processed
    and then terminates processing. This would also be a
    misconfiguration, because there is no reason to have duplicate rules
    with different actions.
    
    {{%/notice%}}

  - When processing traffic, rules affecting the FORWARD chain that
    specify an ingress interface are performed prior to rules that match
    on an egress interface. As a workaround, rules that only affect the
    egress interface can have an ingress interface wildcard (currently,
    only *swp+* and *bond+* are supported as wildcard names; see below)
    that matches any interface applied so that you can maintain order of
    operations with other input interface rules. Take the following
    rules, for example:
    
        -A FORWARD -i $PORTA -j ACCEPT
        -A FORWARD -o $PORTA -j ACCEPT   <-- This rule is performed LAST (because of egress interface matching)
        -A FORWARD -i $PORTB -j DROP
    
    If you modify the rules like this, they are performed in order:
    
        -A FORWARD -i $PORTA -j ACCEPT
        -A FORWARD -i swp+ -o $PORTA -j ACCEPT   <-- These rules are performed in order (because of wildcard match on ingress interface)
        -A FORWARD -i $PORTB -j DROP

  - When using rules that do a mangle and a filter lookup for a packet,
    Cumulus Linux does them in parallel and combines the action.

  - If a switch port is assigned to a bond, any egress rules must be
    assigned to the bond.

  - When using the OUTPUT chain, rules must be assigned to the source.
    For example, if a rule is assigned to the switch port in the
    direction of traffic but the source is a bridge (VLAN), the traffic
    won't be affected by the rule and must be applied to the bridge.

  - If all transit traffic needs to have a rule applied, use the FORWARD
    chain, not the OUTPUT chain.

  - `ebtables` rules are put into either the IPv4 or IPv6 memory space
    depending on whether the rule utilizes IPv4 or IPv6 to make a
    decision. Layer 2-only rules, which match the MAC address, are put
    into the IPv4 memory space.

### <span>Rule Placement in Memory</span>

INPUT and ingress (`FORWARD -i`) rules occupy the same memory space. A
rule counts as ingress if the `-i` option is set. If both input and
output options (`-i` and `-o`) are set, the rule is considered as
ingress and occupies that memory space. For example:

    -A FORWARD -i swp1 -o swp2 -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT

{{%notice note%}}

If you set an output flag with the INPUT chain you will get an error.
For example, running `cl-acltool -i` on the following rule:

    -A FORWARD,INPUT -i swp1 -o swp2 -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT

generates the following error:

    error: line 2 : output interface specified with INPUT chain error processing rule '-A FORWARD,INPUT -i swp1 -o swp2 -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT'

However, simply removing the `-o` option and interface would make it a
valid rule.

{{%/notice%}}

### <span id="src-5868887_Netfilter-ACLs-nonatomic" class="confluence-anchor-link"></span><span>Enabling Nonatomic Updates</span>

You can enable nonatomic updates for `switchd`, which offer better
scaling because all TCAM resources are used to actively impact traffic.
With atomic updates, half of the hardware resources are on standby and
do not actively impact traffic.

Nonatomic updates are now table based, so they don't interrupt network
traffic when new rules are installed. The rules are mapped into the
following tables and are updated in this order:

  - mirror (ingress only)

  - ipv4-mac (can be both ingress and egress)

  - ipv6 (ingress only)

Updates are done incrementally, one table at a time without stopping
traffic. Cumulus Linux checks if a table's rules have changed since the
last time they were installed; if a table does not have any changes,
then it is not reinstalled. If there are changes in a table, then the
new rules are populated in new groups or slices in hardware, then that
table is switched over to the new groups or slices. Finally, old
resources for that table are freed. This process is repeated for each of
the tables listed above. If a failure occurs during an update, the
regular nonatomic mode is attempted, which interrupts network traffic.
If that also fails, Cumulus Linux reverts back to the previous rules.

To always start `switchd` with nonatomic updates:

1.  Edit `/etc/cumulus/switchd.conf`.

2.  Add the following line to the file:
    
        acl.non_atomic_update_mode = TRUE 

3.  [Restart
    `switchd`](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5114824):
    
        cumulus@switch:~$ sudo systemctl restart switchd.service

{{%notice note%}}

During nonatomic updates, traffic is stopped first, and enabled after
the new configuration is written into the hardware completely.

{{%/notice%}}

### <span>Using iptables/ip6tables/ebtables Directly</span>

Using `iptables`/`ip6tables`/`ebtables` directly is not recommended
because any rules installed in these cases only are applied to the Linux
kernel and are not hardware accelerated via synchronization to the
switch silicon. Also running `cl-acltool -i` (the installation command)
resets all rules and deletes anything that is not stored in
`/etc/cumulus/acl/policy.conf`.

For example, performing:

    cumulus@switch:~$ sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

Appears to work, and the rule appears when you run `cl-acltool -L`:

    cumulus@switch:~$ sudo cl-acltool -L ip
    -------------------------------
    Listing rules of type iptables: 
    ------------------------------- 
     
    TABLE filter :
    Chain INPUT (policy ACCEPT 72 packets, 5236 bytes) 
    pkts bytes target prot opt in out source destination 
    0 0 DROP icmp -- any any anywhere anywhere icmp echo-request

However, the rule is not synced to hardware when applied in this fashion
and running `cl-acltool -i` or `reboot` removes the rule without
replacing it. To ensure all rules that can be in hardware are hardware
accelerated, place them in `/etc/cumulus/acl/policy.conf` and install
them by running `cl-acltool -i`.

### <span>Estimating the Number of Rules</span>

To estimate the number of rules that could be created from an ACL entry,
first determine if that entry is an ingress or an egress. Then determine
if it is IPv4-mac or IPv6 type rule. This determines the slice to which
the rule belongs. Then use the following to determine how many entries
are used up for each type.

By default, each entry occupies one double wide entry, except if the
entry is one of the following:

  - An entry with multiple comma-separated input interfaces is split
    into one rule for each input interface (listed after
    `--in-interface` below). For example, this entry splits into two
    rules:
    
        -A FORWARD --in-interface swp1s0,swp1s1 -p icmp -j ACCEPT

  - An entry with multiple comma-separated output interfaces is split
    into one rule for each output interface (listed after
    `--out-interface` below). This entry splits into two rules:
    
        -A FORWARD --in-interface swp+ --out-interface swp1s0,swp1s1 -p icmp -j ACCEPT

  - An entry with both input and output comma-separated interfaces is
    split into one rule for each combination of input and output
    interface (listed after `--in-interface` and `--out-interface`
    below). This entry splits into four rules:
    
        -A FORWARD --in-interface swp1s0,swp1s1 --out-interface swp1s2,swp1s3 -p icmp -j ACCEPT

  - An entry with multiple L4 port ranges is split into one rule for
    each range (listed after `--dports` below). For example, this entry
    splits into two rules:
    
        -A FORWARD --in-interface swp+ -p tcp -m multiport --dports 1050:1051,1055:1056 -j ACCEPT

### <span>Matching SVI/Bridged Interfaces in Rules</span>

Cumulus Linux supports matching ACL rules for both ingress and egress
interfaces on both
[VLAN-aware](/version/cumulus-linux-332/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)
and [traditional
mode](/version/cumulus-linux-332/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges)
bridges, including bridge SVIs ([switch VLAN
interfaces](Ethernet_Bridging_-_VLANs.html#src-5868972_EthernetBridging-VLANs-svi))
for input and output. However, keep the following in mind:

  - If a traditional mode bridge has a mix of different VLANs, or has
    both access and trunk members, output interface matching is not
    supported.

  - For `iptables` rules, all IP packets in a bridge are matched, not
    just routed packets.

  - You cannot match both input and output interfaces in a rule.

  - For routed packets, Cumulus Linux cannot match the output bridge for
    SPAN/ERSPAN.

Following are example rules for a VLAN-aware bridge:

    [ebtables]
    -A FORWARD -i br0.100 -p IPv4 --ip-protocol icmp -j DROP
    -A FORWARD -o br0.100 -p IPv4 --ip-protocol icmp -j ACCEPT
     
    [iptables]
    -A FORWARD -i br0.100 -p icmp -j DROP
    -A FORWARD --out-interface br0.100 -p icmp -j ACCEPT
    -A FORWARD --in-interface br0.100 -j POLICE --set-mode  pkt  --set-rate  1 --set-burst 1 --set-class 0

And here are example rules for a traditional mode bridge:

    [ebtables]
    -A FORWARD -i br0 -p IPv4 --ip-protocol icmp -j DROP
    -A FORWARD -o br0 -p IPv4 --ip-protocol icmp -j ACCEPT
     
     
    [iptables]
    -A FORWARD -i br0 -p icmp -j DROP
    -A FORWARD --out-interface br0 -p icmp -j ACCEPT
    -A FORWARD --in-interface br0 -j POLICE --set-mode  pkt  --set-rate  1 --set-burst 1 --set-class 0

## <span>Installing and Managing ACL Rules with NCLU</span>

NCLU provides an easy way to create custom ACLs in Cumulus Linux. The
rules you create live in the `/var/lib/cumulus/nclu/nclu_acl.conf` file,
which gets converted to a rules file,
`/etc/cumulus/acl/policy.d/50_nclu_acl.rules`. This way, the rules you
create with NCLU are independent of the two default files in
`/etc/cumulus/acl/policy.d`, `00control_plane.rules` and
`99control_plane_catch_all.rules`, as the content in these files may get
updated after you upgrade Cumulus Linux.

Instead of crafting a rule by hand then installing it using
`cl-acltool`, NCLU handles many of the options automatically. For
example, consider the following `iptables` rule:

    -A FORWARD -i swp1 -o swp2 -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT

You would create this rule, called *EXAMPLE1*, using NCLU like this:

    cumulus@switch:~$ net add acl ipv4 EXAMPLE1 accept tcp source-ip 10.0.14.2/32 source-port dest-ip 10.0.15.8/32 dest-port any
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

All options, such as the `-j` and `-p`, even `FORWARD` in the above
rule, are added automatically when you apply the rule to the control
plane; NCLU figures it all out for you.

You can also set a priority value, which specifies the order in which
the rules get executed, and the order in which they appear in the rules
file. Lower numbers are executed first. To add a new rule in the middle,
first run `net show config acl`, which displays the priority numbers.
Otherwise, new rules get appended to the end of the list of rules in the
`nclu_acl.conf` and `50_nclu_acl.rules` files.

{{%notice note%}}

If you need to hand edit a rule, don’t edit the `50_nclu_acl.rules`
file. Instead, edit the `nclu_acl.conf` file.

{{%/notice%}}

After you add the rule, you need to apply it to an inbound or outbound
interface using `net add int acl`; swp1 is the inbound interface in our
example:

    cumulus@switch:~$ net add int swp1 acl ipv4 EXAMPLE1 inbound
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

After you commit your changes, you can verify the rule you created with
NCLU by running `net show configuration acl`:

    cumulus@switch:~$ net show configuration acl 
    acl ipv4 EXAMPLEv4 priority 10 accept tcp source-ip 10.0.14.2/32 source-port any dest-ip 10.0.15.8/32 dest-port any
     
    interface swp1
      acl ipv4 EXAMPLE1 inbound

Or you can see all of the rules installed by running `cat` on the
`50_nclu_acl.rules` file:

    cumulus@switch:~$ cat /etc/cumulus/acl/policy.d/50_nclu_acl.rules 
    [iptables]
    # swp1: acl ipv4 EXAMPLE1 inbound
    -A FORWARD --in-interface swp1 --out-interface swp2 -j ACCEPT -p tcp -s 10.0.14.2/32 -d 10.0.15.8/32 --dport 110

For INPUT and FORWARD rules, apply the rule to a control plane interface
using `net add control-plane`:

    cumulus@switch:~$ net add control-plane acl ipv4 EXAMPLE1 inbound
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To remove a rule, use `net del acl ipv4|ipv6|mac RULENAME`:

    cumulus@switch:~$ net del acl ipv4 EXAMPLE1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This deletes all rules from the `50_nclu_acl.rules` file with that name.
It also deletes the interfaces referenced in the `nclu_acl.conf` file.

## <span>Installing and Managing ACL Rules with cl-acltool</span>

You can manage Cumulus Linux ACLs with `cl-acltool`. Rules are first
written to the `iptables` chains, as described above, and then synced to
hardware via `switchd`.

{{%notice note%}}

Use `iptables`/`ip6tables`/`ebtables` and `cl-acltool` to manage rules
in the default files, `00control_plane.rules` and
`99control_plane_catch_all.rules`; they’re not aware of rules created
using NCLU.

{{%/notice%}}

To examine the current state of chains and list all installed rules,
run:

    cumulus@switch:~$ sudo cl-acltool -L all 
    ------------------------------- 
    Listing rules of type iptables: 
    ------------------------------- 
     
    TABLE filter : 
    Chain INPUT (policy ACCEPT 90 packets, 14456 bytes) 
    pkts bytes target prot opt in out source destination 
    0 0 DROP all -- swp+ any 240.0.0.0/5 anywhere 
    0 0 DROP all -- swp+ any loopback/8 anywhere 
    0 0 DROP all -- swp+ any base-address.mcast.net/8 anywhere 
    0 0 DROP all -- swp+ any 255.255.255.255 anywhere ...

To list installed rules using native `iptables`, `ip6tables` and
`ebtables`, use the `-L` option with the respective commands:

    cumulus@switch:~$ sudo iptables -L 
    cumulus@switch:~$ sudo ip6tables -L 
    cumulus@switch:~$ sudo ebtables -L

To flush all installed rules, run:

    cumulus@switch:~$ sudo cl-acltool -F all

To flush only the IPv4 `iptables` rules, run:

    cumulus@switch:~$ sudo cl-acltool -F ip

If the install fails, ACL rules in the kernel and hardware are rolled
back to the previous state. Errors from programming rules in the kernel
or ASIC are reported appropriately.

## <span>Installing Packet Filtering (ACL) Rules</span>

`cl-acltool` takes access control list (ACL) rules input in files. Each
ACL policy file contains `iptables`, `ip6tables` and `ebtables`
categories under the tags `[iptables]`, `[ip6tables]` and `[ebtables]`
respectively.

Each rule in an ACL policy must be assigned to one of the rule
categories above.

See `man cl-acltool(5)` for ACL rule details. For `iptables` rule
syntax, see `man iptables(8)`. For `ip6tables` rule syntax, see `man
ip6tables(8)`. For `ebtables` rule syntax, see `man ebtables(8)`.

See `man cl-acltool(5)` and `man cl-acltool(8)` for further details on
using `cl-acltool`; however, some examples are listed here, and more are
listed [later in this chapter](#src-5868887_Netfilter-ACLs-exm).

{{%notice note%}}

By default:

  - ACL policy files are located in `/etc/cumulus/acl/policy.d/`.

  - All `*.rules` files in this directory are included in
    `/etc/cumulus/acl/policy.conf`.

  - All files included in this `policy.conf` file are installed when the
    switch boots up.

  - The `policy.conf` file expects rules files to have a `.rules` suffix
    as part of the file name.

{{%/notice%}}

Here is an example ACL policy file:

    [iptables] 
    -A INPUT --in-interface swp1 -p tcp --dport 80 -j ACCEPT 
    -A FORWARD --in-interface swp1 -p tcp --dport 80 -j ACCEPT 
     
    [ip6tables] 
    -A INPUT --in-interface swp1 -p tcp --dport 80 -j ACCEPT 
    -A FORWARD --in-interface swp1 -p tcp --dport 80 -j ACCEPT 
      
    [ebtables] 
    -A INPUT -p IPv4 -j ACCEPT 
    -A FORWARD -p IPv4 -j ACCEPT

You can use wildcards or variables to specify chain and interface lists
to ease administration of rules.

{{%notice note%}}

**Interface Wildcards**

Currently only *swp+* and *bond+* are supported as wildcard names. There
may be kernel restrictions in supporting more complex wildcards likes
*swp1+ etc*.

{{%/notice%}}

    INGRESS = swp+ 
    INPUT_PORT_CHAIN = INPUT,FORWARD 
     
    [iptables] 
    -A $INPUT_PORT_CHAIN --in-interface $INGRESS -p tcp --dport 80 -j ACCEPT 
      
    [ip6tables] 
    -A $INPUT_PORT_CHAIN --in-interface $INGRESS -p tcp --dport 80 -j ACCEPT 
     
    [ebtables] 
    -A INPUT -p IPv4 -j ACCEPT

ACL rules for the system can be written into multiple files under the
default `/etc/cumulus/acl/policy.d/` directory. The ordering of rules
during installation follows the sort order of the files based on their
file names.

Use multiple files to stack rules. The example below shows two rules
files separating rules for management and datapath traffic:

    cumulus@switch:~$ ls /etc/cumulus/acl/policy.d/ 
    00sample_mgmt.rules 01sample_datapath.rules 
    cumulus@switch:~$ cat /etc/cumulus/acl/policy.d/00sample_mgmt.rules 
      
    INGRESS_INTF = swp+ 
    INGRESS_CHAIN = INPUT 
      
    [iptables] 
    # protect the switch management 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -s 10.0.11.2 -d 10.0.12.8 -p tcp -j ACCEPT 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -d 10.0.16.8 -p udp -j DROP 
     
    cumulus@switch:~$ cat /etc/cumulus/acl/policy.d/01sample_datapath.rules 
    INGRESS_INTF = swp+ 
    INGRESS_CHAIN = INPUT, FORWARD 
     
    [iptables] 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -s 192.0.2.5 -p icmp -j ACCEPT 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -s 192.0.2.6 -d 192.0.2.4 -j DROP 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -s 192.0.2.2 -d 192.0.2.8 -j DROP

Install all ACL policies under a directory:

    cumulus@switch:~$ sudo cl-acltool -i -P ./rules 
    Reading files under rules 
    Reading rule file ./rules/01_http_rules.txt ... 
    Processing rules in file ./rules/01_http_rules.txt ... 
    Installing acl policy ... 
    Done.

Install all rules and policies included in
`/etc/cumulus/acl/policy.conf`:

    cumulus@switch:~$ sudo cl-acltool -i

## <span>Specifying which Policy Files to Install</span>

By default, any `.rules` file you configure in
`/etc/cumulus/acl/policy.d/` get installed by Cumulus Linux. To add
other policy files to an ACL, you need to include them in
`/etc/cumulus/acl/policy.conf`. For example, in order for Cumulus Linux
to install a rule in a policy file called `01_new.datapathacl`, you
would add `include /etc/cumulus/acl/policy.d/01_new.rules` to
`policy.conf`, as in this example:

    cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.conf 
     
    # 
    # This file is a master file for acl policy file inclusion 
    # 
    # Note: This is not a file where you list acl rules. 
    # 
    # This file can contain: 
    # - include lines with acl policy files 
    #   example: 
    #     include <filepath> 
    # 
    # see manpage cl-acltool(5) and cl-acltool(8) for how to write policy files 
    # 
     
    include /etc/cumulus/acl/policy.d/01_new.datapathacl

## <span>Hardware Limitations on Number of Rules</span>

The maximum number of rules that can be handled in hardware is a
function of the following factors:

  - The platform type (switch silicon, like Tomahawk or Spectrum — see
    the [HCL](http://cumulusnetworks.com/support/hcl) to determine which
    platform type applies to a particular switch)

  - The mix of IPv4 and/or IPv6 rules; Cumulus Linux doesn't support the
    maximum number of rules for both IPv4 and IPv6 simultaneously

  - The number of default rules provided by Cumulus Linux

  - Whether the rules are applied on ingress or egress

  - Whether the rules are in atomic or nonatomic mode; nonatomic mode
    rules are used when nonatomic updates are enabled ([see
    above](#src-5868887_Netfilter-ACLs-nonatomic))

If the maximum number of rules for a particular table is exceeded,
`cl-acltool -i` generates the following error:

    error: hw sync failed (sync_acl hardware installation failed) Rolling back .. failed.

{{%notice note%}}

On Broadcom platforms, IPv6 egress rules are not supported.

{{%/notice%}}

In the tables below, the default rules count toward the limits listed.
The raw limits below assume only one ingress and one egress table are
present.

### <span>Broadcom Tomahawk Limits</span>

| Direction                        | Atomic Mode IPv4 Rules | Atomic Mode IPv6 Rules | Nonatomic Mode IPv4 Rules | Nonatomic Mode IPv6 Rules |
| -------------------------------- | ---------------------- | ---------------------- | ------------------------- | ------------------------- |
| Ingress raw limit                | 512                    | 512                    | 1024                      | 1024                      |
| Ingress limit with default rules | 256 (36 default)       | 256 (29 default)       | 768 (36 default)          | 768 (29 default)          |
| Egress raw limit                 | 256                    | 0                      | 512                       | 0                         |
| Egress limit with default rules  | 256 (29 default)       | 0                      | 512 (29 default)          | 0                         |

### <span>Broadcom Trident II+ Limits</span>

| Direction                        | Atomic Mode IPv4 Rules | Atomic Mode IPv6 Rules | Nonatomic Mode IPv4 Rules | Nonatomic Mode IPv6 Rules |
| -------------------------------- | ---------------------- | ---------------------- | ------------------------- | ------------------------- |
| Ingress raw limit                | 4096                   | 4096                   | 8192                      | 8192                      |
| Ingress limit with default rules | 2048 (36 default)      | 3072 (29 default)      | 6144 (36 default)         | 6144 (29 default)         |
| Egress raw limit                 | 256                    | 0                      | 512                       | 0                         |
| Egress limit with default rules  | 256 (29 default)       | 0                      | 512 (29 default)          | 0                         |

### <span>Broadcom Trident II Limits</span>

| Direction                        | Atomic Mode IPv4 Rules | Atomic Mode IPv6 Rules | Nonatomic Mode IPv4 Rules | Nonatomic Mode IPv6 Rules |
| -------------------------------- | ---------------------- | ---------------------- | ------------------------- | ------------------------- |
| Ingress raw limit                | 1024                   | 1024                   | 2048                      | 2048                      |
| Ingress limit with default rules | 512 (36 default)       | 768 (29 default)       | 1536 (36 default)         | 1536 (29 default)         |
| Egress raw limit                 | 256                    | 0                      | 512                       | 0                         |
| Egress limit with default rules  | 256 (29 default)       | 0                      | 512 (29 default)          | 0                         |

### <span>Broadcom Helix4 Limits</span>

| Direction                        | Atomic Mode IPv4 Rules | Atomic Mode IPv6 Rules | Nonatomic Mode IPv4 Rules | Nonatomic Mode IPv6 Rules |
| -------------------------------- | ---------------------- | ---------------------- | ------------------------- | ------------------------- |
| Ingress raw limit                | 1024                   | 512                    | 2048                      | 1024                      |
| Ingress limit with default rules | 768 (36 default)       | 384 (29 default)       | 1792 (36 default)         | 896 (29 default)          |
| Egress raw limit                 | 256                    | 0                      | 512                       | 0                         |
| Egress limit with default rules  | 256 (29 default)       | 0                      | 512 (29 default)          | 0                         |

### <span>Mellanox Spectrum Limits</span>

The Mellanox Spectrum ASIC has one common
[TCAM](https://en.wikipedia.org/wiki/Content-addressable_memory#Ternary_CAMs)
for both ingress and egress, and it may be used for other
non-ACL-related resources. However, the number of supported rules varies
with the [TCAM profile](Routing.html#src-5869207_Routing-tcam) specified
for the switch.

| Profile    | Atomic Mode IPv4 Rules | Atomic Mode IPv6 Rules | Nonatomic Mode IPv4 Rules | Nonatomic Mode IPv6 Rules |
| ---------- | ---------------------- | ---------------------- | ------------------------- | ------------------------- |
| default    | 1750                   | 750                    | 3500                      | 1500                      |
| ipmc-heavy | 200                    | 80                     | 400                       | 160                       |
| acl-heavy  | 3000                   | 2000                   | 6000                      | 2500                      |

## <span id="src-5868887_Netfilter-ACLs-supported" class="confluence-anchor-link"></span><span>Supported Rule Types</span>

The `iptables`/`ip6tables`/`ebtables` construct tries to layer the Linux
implementation on top of the underlying hardware but they are not always
directly compatible. Here are the supported rules for chains in
`iptables`, `ip6tables` and `ebtables`.

{{%notice note%}}

To learn more about any of the options shown in the tables below, run
`iptables -h [name of option]`. The same help syntax works for options
for `ip6tables` and `ebtables`.

Click to see an example of help syntax for an ebtables target

    root@leaf1# ebtables -h tricolorpolice
    <...snip...>
    tricolorpolice option:
     --set-color-mode STRING setting the mode in blind or aware
     --set-cir INT setting committed information rate in kbits per second
     --set-cbs INT setting committed burst size in kbyte
     --set-pir INT setting peak information rate in kbits per second
     --set-ebs INT setting excess burst size in kbyte
     --set-conform-action-dscp INT setting dscp value if the action is accept for conforming packets
     --set-exceed-action-dscp INT setting dscp value if the action is accept for exceeding packets
     --set-violate-action STRING setting the action (accept/drop) for violating packets
     --set-violate-action-dscp INT setting dscp value if the action is accept for violating packets
    Supported chains for the filter table:
    INPUT FORWARD OUTPUT

{{%/notice%}}

### <span>iptables/ip6tables Rule Support</span>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Rule Element</p></th>
<th><p>Supported</p></th>
<th><p>Unsupported</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Matches</strong></p></td>
<td><ul>
<li><p>Src/Dst, IP protocol</p></li>
<li><p>In/out interface</p></li>
<li><p>IPv4: icmp, ttl,</p></li>
<li><p>IPv6: icmp6, frag, hl,</p></li>
<li><p>IP common: tcp (<a href="#src-5868887_Netfilter-ACLs-filteringtcp">with flags</a>), udp, multiport,TOS, DSCP, addrtype</p></li>
</ul></td>
<td><ul>
<li><p>Rules with input/output Ethernet interfaces are ignored</p></li>
<li><p>Inverse matches</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>Standard Targets</strong></p></td>
<td><ul>
<li><p>ACCEPT, DROP</p></li>
</ul></td>
<td><ul>
<li><p>RETURN, QUEUE, STOP, Fall Thru, Jump</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Extended Targets</strong></p></td>
<td><ul>
<li><p>LOG (IPv4/IPv6); UID is not supported for LOG</p></li>
<li><p>TCP SEQ, TCP options or IP options</p></li>
<li><p>ULOG</p></li>
<li><p>SETQOS</p></li>
<li><p>DSCP</p></li>
</ul>
<p><em>Unique to Cumulus Linux:</em></p>
<ul>
<li><p>SPAN</p></li>
<li><p>ERSPAN (IPv4/IPv6)</p></li>
<li><p>POLICE</p></li>
<li><p>TRICOLORPOLICE</p></li>
<li><p>SETCLASS</p></li>
</ul></td>
<td><p> </p></td>
</tr>
</tbody>
</table>

### <span>ebtables Rule Support</span>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Rule Element</p></th>
<th><p>Supported</p></th>
<th><p>Unsupported</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Matches</strong></p></td>
<td><ul>
<li><p>ether type</p></li>
<li><p>input interface/wildcard</p></li>
<li><p>output interface/wildcard</p></li>
<li><p>src/dst MAC</p></li>
<li><p>IP: src, dest, tos, proto, sport, dport</p></li>
<li><p>IPv6: tclass, icmp6: type, icmp6: code range, src/dst addr, sport, dport</p></li>
</ul></td>
<td><ul>
<li><p>Inverse matches</p></li>
<li><p>Proto length</p></li>
<li><p>VLAN</p></li>
<li><p>802.1p (CoS)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p><strong>Standard Targets</strong></p></td>
<td><ul>
<li><p>ACCEPT, DROP</p></li>
</ul></td>
<td><ul>
<li><p>Return, Continue, Jump, Fall Thru</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p><strong>Extended Targets</strong></p></td>
<td><ul>
<li><p>Ulog</p></li>
<li><p>log</p></li>
</ul>
<p><em>Unique to Cumulus Linux:</em></p>
<ul>
<li><p>span</p></li>
<li><p>erspan</p></li>
<li><p>police</p></li>
<li><p>tricolorpolice</p></li>
<li><p>setclass</p></li>
</ul></td>
<td><p> </p></td>
</tr>
</tbody>
</table>

### <span>Other Unsupported Rules</span>

  - Rules that have no matches and accept all packets in a chain are
    currently ignored. This probably has side effects in the sense that
    the rules below them do get hit, when normally they wouldn't.

  - Chain default rules (which are ACCEPT) are also ignored.

## <span>Common Examples</span>

### <span>Policing Control Plane and Data Plane Traffic</span>

You can configure quality of service for traffic on both the control
plane and the data plane. By using QoS policers, you can rate limit
traffic so incoming packets get dropped if they exceed specified
thresholds.

{{%notice note%}}

Counters on POLICE ACL rules in `iptables` do not currently show the
packets that are dropped due to those rules.

{{%/notice%}}

Use the `POLICE` target with `iptables`. `POLICE` takes these arguments:

  - `--set-class value`: Sets the system internal class of service queue
    configuration to *value*.

  - `--set-rate value`: Specifies the maximum rate in kilobytes (KB) or
    packets.

  - `--set-burst value`: Specifies the number of packets or kilobytes
    (KB) allowed to arrive sequentially.

  - `--set-mode string`: Sets the mode in *KB* (kilobytes) or *pkt*
    (packets) for rate and burst size.

For example, to rate limit the incoming traffic on swp1 to 400
packets/second with a burst of 100 packets/second and set the class of
the queue for the policed traffic as 0, set this rule in your
appropriate `.rules` file:

    -A INPUT --in-interface swp1 -j POLICE --set-mode pkt --set-rate 400 --set-burst 100 --set-class 0

Here is another example of control plane ACL rules to lock down the
switch. You specify them in
`/etc/cumulus/acl/policy.d/00control_plane.rules`:

View the contents of the file ...

    INGRESS_INTF = swp+ 
    INGRESS_CHAIN = INPUT 
    INNFWD_CHAIN = INPUT,FORWARD 
    MARTIAN_SOURCES_4 = "240.0.0.0/5,127.0.0.0/8,224.0.0.0/8,255.255.255.255/32" 
    MARTIAN_SOURCES_6 = "ff00::/8,::/128,::ffff:0.0.0.0/96,::1/128" 
     
      
    # Custom Policy Section 
    SSH_SOURCES_4 = "192.168.0.0/24" 
    NTP_SERVERS_4 = "192.168.0.1/32,192.168.0.4/32" 
    DNS_SERVERS_4 = "192.168.0.1/32,192.168.0.4/32" 
    SNMP_SERVERS_4 = "192.168.0.1/32" 
     
      
    [iptables] 
    -A $INNFWD_CHAIN --in-interface $INGRESS_INTF -s $MARTIAN_SOURCES_4 -j DROP 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p ospf -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000 --set-class 7 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p tcp --dport bgp -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000 --set-class 7 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p tcp --sport bgp -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000 --set-class 7 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p icmp -j POLICE --set-mode pkt --set-rate 100 --set-burst 40 --set-class 2 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p udp --dport bootps:bootpc -j POLICE --set-mode pkt --set-rate 100 --set-burst 100 --set-class 2 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p tcp --dport bootps:bootpc -j POLICE --set-mode pkt --set-rate 100 --set-burst 100 --set-class 2 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p igmp -j POLICE --set-mode pkt --set-rate 300 --set-burst 100 --set-class 6 
     
      
    # Custom policy 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p tcp --dport 22 -s $SSH_SOURCES_4 -j ACCEPT 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p udp --sport 123 -s $NTP_SERVERS_4 -j ACCEPT 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p udp --sport 53 -s $DNS_SERVERS_4 -j ACCEPT 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p udp --dport 161 -s $SNMP_SERVERS_4 -j ACCEPT 
     
      
    # Allow UDP traceroute when we are the current TTL expired hop 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -p udp --dport 1024:65535 -m ttl --ttl-eq 1 -j ACCEPT 
    -A $INGRESS_CHAIN --in-interface $INGRESS_INTF -j DROP

### <span>Setting DSCP on Transit Traffic</span>

The examples here use the *mangle* table to modify the packet as it
transits the switch. DSCP is expressed in [decimal
notation](https://en.wikipedia.org/wiki/Differentiated_services#Commonly_used_DSCP_values)
in the examples below.

    [iptables]
     
    #Set SSH as high priority traffic.
    -t mangle -A FORWARD -p tcp --dport 22  -j DSCP --set-dscp 46 
     
    #Set everything coming in SWP1 as AF13
    -t mangle -A FORWARD --in-interface swp1 -j DSCP --set-dscp 14
     
    #Set Packets destined for 10.0.100.27 as best effort
    -t mangle -A FORWARD -d 10.0.100.27/32 -j DSCP --set-dscp 0
     
    #Example using a range of ports for TCP traffic
    -t mangle -A FORWARD -p tcp -s 10.0.0.17/32 --sport 10000:20000 -d 10.0.100.27/32 --dport 10000:20000 -j DSCP --set-dscp 34

### <span>Verifying DSCP Values on Transit Traffic</span>

The examples here use the DSCP match criteria in combination with other
IP, TCP and interface matches to identify traffic and count the number
of packets.

    [iptables]
     
    #Match and count the packets that match SSH traffic with DSCP EF
    -A FORWARD -p tcp --dport 22 -m dscp --dscp 46 -j ACCEPT
     
    #Match and count the packets coming in SWP1 as AF13
    -A FORWARD --in-interface swp1 -m dscp --dscp 14 -j ACCEPT
    #Match and count the packets with a destination 10.0.0.17 marked best effort
    -A FORWARD -d 10.0.100.27/32 -m dscp --dscp 0 -j ACCEPT
     
    #Match and count the packets in a port range with DSCP AF41
    -A FORWARD -p tcp -s 10.0.0.17/32 --sport 10000:20000 -d 10.0.100.27/32 --dport 10000:20000 -m dscp --dscp 34 -j ACCEPT

### <span>Checking the Packet and Byte Counters for ACL Rules</span>

To verify the counters, using the above example rules, first send test
traffic matching the patterns through the network. The following example
generates traffic with [mz](http://www.perihel.at/sec/mz/), which can be
installed on host servers or even on Cumulus Linux switches. Once
traffic is sent to validate the counters, they are matched on switch1
use `cl-acltool`.

    # Send 100 TCP packets on host1 with a DSCP value of EF with a destination of host2 TCP port 22:
     
    cumulus@host1$ mz eth1 -A 10.0.0.17 -B 10.0.100.27 -c 100 -v -t tcp "dp=22,dscp=46"
     IP:  ver=4, len=40, tos=184, id=0, frag=0, ttl=255, proto=6, sum=0, SA=10.0.0.17, DA=10.0.100.27,
          payload=[see next layer]
     TCP: sp=0, dp=22, S=42, A=42, flags=0, win=10000, len=20, sum=0,
          payload=
     
    # Verify the 100 packets are matched on switch1
     
    cumulus@switch1$ sudo cl-acltool -L ip
    -------------------------------
    Listing rules of type iptables:
    -------------------------------
    TABLE filter :
    Chain INPUT (policy ACCEPT 9314 packets, 753K bytes)
     pkts bytes target     prot opt in     out     source               destination
    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination
      100  6400 ACCEPT     tcp  --  any    any     anywhere             anywhere             tcp dpt:ssh DSCP match 0x2e
        0     0 ACCEPT     all  --  swp1   any     anywhere             anywhere             DSCP match 0x0e
        0     0 ACCEPT     all  --  any    any     10.0.0.17            anywhere             DSCP match 0x00
        0     0 ACCEPT     tcp  --  any    any     10.0.0.17            10.0.100.27          tcp spts:webmin:20000 dpts:webmin:2002

    # Send 100 packets with a small payload on host1 with a DSCP value of AF13 with a destination of host2:
     
    cumulus@host1$ mz eth1 -A 10.0.0.17 -B 10.0.100.27 -c 100 -v -t ip
     IP:  ver=4, len=20, tos=0, id=0, frag=0, ttl=255, proto=0, sum=0, SA=10.0.0.17, DA=10.0.100.27,
          payload=
     
    # Verify the 100 packets are matched on switch1
     
    cumulus@switch1$ sudo cl-acltool -L ip
    -------------------------------
    Listing rules of type iptables:
    -------------------------------
    TABLE filter :
    Chain INPUT (policy ACCEPT 9314 packets, 753K bytes)
     pkts bytes target     prot opt in     out     source               destination
    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination
      100  6400 ACCEPT     tcp  --  any    any     anywhere             anywhere             tcp dpt:ssh DSCP match 0x2e
      100  7000 ACCEPT     all  --  swp3   any     anywhere             anywhere             DSCP match 0x0e
      100  6400 ACCEPT     all  --  any    any     10.0.0.17            anywhere             DSCP match 0x00
        0     0 ACCEPT     tcp  --  any    any     10.0.0.17            10.0.100.27          tcp spts:webmin:20000 dpts:webmin:2002

    # Send 100 packets on host1 with a destination of host2:
     
    cumulus@host1$ mz eth1 -A 10.0.0.17 -B 10.0.100.27 -c 100 -v -t ip
     IP:  ver=4, len=20, tos=56, id=0, frag=0, ttl=255, proto=0, sum=0, SA=10.0.0.17, DA=10.0.100.27,
          payload=
     
    # Verify the 100 packets are matched on switch1
     
    cumulus@switch1$ sudo cl-acltool -L ip
    -------------------------------
    Listing rules of type iptables:
    -------------------------------
    TABLE filter :
    Chain INPUT (policy ACCEPT 9314 packets, 753K bytes)
     pkts bytes target     prot opt in     out     source               destination
    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination
      100  6400 ACCEPT     tcp  --  any    any     anywhere             anywhere             tcp dpt:ssh DSCP match 0x2e
      100  7000 ACCEPT     all  --  swp3   any     anywhere             anywhere             DSCP match 0x0e
        0     0 ACCEPT     all  --  any    any     10.0.0.17            anywhere             DSCP match 0x00
        0     0 ACCEPT     tcp  --  any    any     10.0.0.17            10.0.100.27          tcp spts:webmin:20000 dpts:webmin:2002Still working

### <span id="src-5868887_Netfilter-ACLs-filteringtcp" class="confluence-anchor-link"></span><span>Filtering Specific TCP Flags</span>

The example solution below creates rules on the INPUT and FORWARD chains
to drop ingress IPv4 and IPv6 TCP packets when the SYN bit is set and
the RST, ACK and FIN bits are reset. The default for the INPUT and
FORWARD chains allows all other packets. The ACL is applied to ports
swp20 and swp21. After configuring this ACL, new TCP sessions that
originate from ingress ports swp20 and swp21 will not be allowed. TCP
sessions that originate from any other port are allowed.

    INGRESS_INTF = swp20,swp21
     
    [iptables]
    -A INPUT,FORWARD --in-interface $INGRESS_INTF -p tcp --syn -j DROP
    [ip6tables]
    -A INPUT,FORWARD --in-interface $INGRESS_INTF -p tcp --syn -j DROP

The `--syn` flag in the above rule matches packets with the SYN bit set
and the ACK, RST and FIN bits are cleared. It is equivalent to using
`-tcp-flags SYN,RST,ACK,FIN SYN`. For example, the above rule could be
re-written as:

    -A INPUT,FORWARD --in-interface $INGRESS_INTF -p tcp --tcp-flags SYN,RST,ACK,FIN SYN -j DROP

## <span>Example Scenario</span>

<span id="src-5868887_Netfilter-ACLs-examples"></span>The following
example scenario demonstrates where several different rules are applied
to show what is possible.

{{% imgOld 6 %}}

Following are the configurations for the two switches used in these
examples. The configuration for each switch appears in
`/etc/network/interfaces` on that switch.

### <span>Switch 1 Configuration</span>

    cumulus@switch1:~$ net show configuration files
     
    ...
     
    /etc/network/interfaces
    =======================
     
     
    auto swp1 
    iface swp1 
     
    auto swp2 
    iface swp2 
     
    auto swp3 
    iface swp3 
     
    auto swp4 
    iface swp4 
     
    auto bond2 
    iface bond2 
        bond-slaves swp3 swp4 
     
    auto br-untagged 
    iface br-untagged 
        address 10.0.0.1/24
        bridge_ports swp1 bond2 
        bridge_stp on
     
    auto br-tag100 
    iface br-tag100 
        address 10.0.100.1/24
        bridge_ports swp2.100 bond2.100 
        bridge_stp on 
     
    ...

### <span>Switch 2 Configuration</span>

    cumulus@switch2:~$ net show configuration files
     
    ...
     
    /etc/network/interfaces
    =======================
     
    auto swp3 
    iface swp3 
     
    auto swp4 
    iface swp4 
     
    auto br-untagged 
    iface br-untagged 
        address 10.0.0.2/24
        bridge_ports bond2 
        bridge_stp on 
     
    auto br-tag100 
    iface br-tag100 
        address 10.0.100.2/24 
        bridge_ports bond2.100 
        bridge_stp on 
     
    auto bond2 
    iface bond2 
        bond-slaves swp3 swp4 
     
    ...

### <span>Egress Rule</span>

The following rule blocks any TCP with destination port 200 traffic
going from host1 or host2 through the switch (corresponding to rule 1 in
the diagram above).

    [iptables] -A FORWARD -o bond2 -p tcp --dport 200 -j DROP

### <span>Ingress Rule</span>

The following rule blocks any UDP traffic with source port 200 going
from host1 through the switch (corresponding to rule 2 in the diagram
above).

    [iptables] -A FORWARD -i swp2 -p udp --sport 200 -j DROP

### <span>Input Rule</span>

The following rule blocks any UDP traffic with source port 200 and
destination port 50 going from host1 to the switch (corresponding to
rule 3 in the diagram above).

    [iptables] -A INPUT -i swp1 -p udp --sport 200 --dport 50 -j DROP

### <span>Output Rule</span>

The following rule blocks any TCP traffic with source port 123 and
destination port 123 going from Switch 1 to host2 (corresponding to rule
4 in the diagram above).

    [iptables] -A OUTPUT -o br-tag100 -p tcp --sport 123 --dport 123 -j DROP

### <span>Combined Rules</span>

The following rule blocks any TCP traffic with source port 123 and
destination port 123 going from any switch port egress or generated from
Switch 1 to host1 or host2 (corresponding to rules 1 and 4 in the
diagram above).

    [iptables] -A OUTPUT,FORWARD -o swp+ -p tcp --sport 123 --dport 123 -j DROP

This also becomes 2 ACLs, and is effectively the same as:

    [iptables]
    -A FORWARD -o swp+ -p tcp --sport 123 --dport 123 -j DROP 
    -A OUTPUT -o swp+ -p tcp --sport 123 --dport 123 -j DROP

### <span>Layer 2-only Rules/ebtables</span>

The following rule blocks any traffic with source MAC address
00:00:00:00:00:12 and destination MAC address 08:9e:01:ce:e2:04 going
from any switch port egress/ingress.

    [ebtables] -A FORWARD -s 00:00:00:00:00:12 -d 08:9e:01:ce:e2:04 -j DROP

## <span>Useful Links</span>

  - [www.netfilter.org](http://www.netfilter.org/)

  - [Netfilter.org packet filtering
    how-to](http://www.netfilter.org/documentation/HOWTO//packet-filtering-HOWTO-6.html)

## <span>Caveats and Errata</span>

### <span>Not All Rules Supported</span>

As mentioned in the [Supported Rules
section](#src-5868887_Netfilter-ACLs-supported) above, not all
`iptables`, `ip6tables` or `ebtables` rules are supported. Refer to that
section for specific rule support.

### <span>ACL Log Policer Limits Traffic</span>

Traffic copied to the CPU is limited to 1 pkt/s by an ACL Log Policer,
to protect the CPU from overloading.

### <span>Bridge Traffic Limitations</span>

Bridge traffic that matches LOG ACTION rules are not logged in syslog,
as the kernel and hardware identify packets using different information.

### <span>Log Actions Cannot Be Forwarded</span>

Logged packets cannot be forwarded. The hardware cannot both forward a
packet and send the packet to the control plane (or kernel) for logging.
To emphasize this, a log action must also have a drop action.

### <span>Broadcom Hardware Limitations</span>

Broadcom platforms have only 24 range checkers. This is a separate
resource from the total number of ACLs allowed. If you are creating a
large ACL configuration, use port ranges for large ranges of more than 5
ports.

### <span>Tomahawk Hardware Limitations</span>

#### <span>Rate Limiting per Pipeline, Not Global</span>

On Tomahawk switches, the field processor (FP) polices on a per-pipeline
basis instead of globally, as with a Trident II switch. If packets come
in to different switch ports that are on different pipelines on the
ASIC, they may be rate limited differently.

For example, your switch is set so BFD if rate limited to 2000 packets
per second. When the BFD packets are received on port1/pipe1 and
port2/pipe2, they would each be rate limited at 2000 pps, thus the
switch is rate limiting at 4000 pps overall. Since there are four
pipelines on a Tomahawk switch, you could see a 4 increase of your
configured rate limits.

#### <span id="src-5868887_Netfilter-ACLs-tomahawk_atomic" class="confluence-anchor-link"></span><span>Atomic Update Mode Enabled by Default</span>

In Cumulus Linux, atomic update mode is enabled by default. If you have
Tomahawk switches and plan to use SPAN and/or mangle rules, you must
disable atomic update mode.

To do so, enable non-atomic update mode by setting the value for
`acl.non_atomic_update_mode` to true in `/etc/cumulus/switchd.conf`:

    acl.non_atomic_update_mode = TRUE

Then [restart
`switchd`](https://docs.cumulusnetworks.com/display/CL30/Configuring+switchd#Configuringswitchd-restartswitchd).

#### <span>Packets Undercounted during ACL Updates</span>

On Tomahawk switches, when updating egress FP rules, some packets do not
get counted. This results in an underreporting of counts during
ping-pong/incremental switchover.

### <span>Trident II+ Hardware Limitations</span>

On a Trident II+ switch, the TCAM allocation for ACLs is limited to 2048
rules in atomic mode for a default setup, instead of 4096 as advertised
for ingress rules.

### <span>iptables Interactions with cl-acltool</span>

Since Cumulus Linux is a Linux operating system, the `iptables` commands
can be used directly and does work. However, you should consider using
`cl-acltool` instead because:

  - Without using `cl-acltool`, rules are not installed into hardware.

  - Running `cl-acltool -i` (the installation command) resets all rules
    and deletes anything that is not stored in
    `/etc/cumulus/acl/policy.conf`.
    
    For example, running the following command works:
    
        cumulus@switch:~$ sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
    
    And the rules appear when you run `cl-acltool -L`:
    
        cumulus@switch:~$ sudo cl-acltool -L ip
        -------------------------------
        Listing rules of type iptables:
        -------------------------------
        TABLE filter :
        Chain INPUT (policy ACCEPT 72 packets, 5236 bytes)
         pkts bytes target  prot opt in   out   source    destination
         
            0     0 DROP    icmp --  any  any   anywhere  anywhere      icmp echo-request
    
    However, running `cl-acltool -i` or `reboot` removes them. To ensure
    all rules that can be in hardware are hardware accelerated, place
    them in `/etc/cumulus/acl/policy.conf` and run `cl-acltool -i`.

### <span>Where to Assign Rules</span>

  - If a switch port is assigned to a bond, any egress rules must be
    assigned to the bond.

  - When using the OUTPUT chain, rules must be assigned to the source.
    For example, if a rule is assigned to the switch port in the
    direction of traffic but the source is a bridge (VLAN), the traffic
    won’t be affected by the rule and must be applied to the bridge.

  - If all transit traffic needs to have a rule applied, use the FORWARD
    chain, not the OUTPUT chain.

### <span>Generic Error Message Displayed after ACL Rule Installation Failure</span>

After an ACL rule installation failure, a generic error message like the
following is displayed:

    cumulus@switch:$ sudo cl-acltool -i -p 00control_plane.rules
    Using user provided rule file 00control_plane.rules
    Reading rule file 00control_plane.rules ...
    Processing rules in file 00control_plane.rules ...
    error: hw sync failed (sync_acl hardware installation failed)
    Installing acl policy... Rolling back ..
    failed.

### <span>Dell S3048-ON Supports only 24K MAC Addresses</span>

The Dell S3048-ON has a limit of 24576 MAC address entries, instead of
32K for other 1G switches.
