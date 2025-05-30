---
title: Access Control List Configuration
author: NVIDIA
weight: 220
toc: 3
---
Cumulus Linux provides several tools to configure <span class="a-tooltip">[ACLs](## "Access Control Lists")</span>:
- NVUE is a Cumulus Linux-specific userspace tool you can use to configure custom ACLs.
- `iptables`, `ip6tables`, and `ebtables` are Linux userspace tools you use to administer filtering rules for IPv4 packets, IPv6 packets, and Ethernet frames (layer 2 using MAC addresses).
- `cl-acltool` is a Cumulus Linux-specific userspace tool you can use to administer filtering rules and configure default ACLs. `cl-acltool` operates on various configuration files and uses `iptables`, `ip6tables`, and `ebtables` to install rules into the kernel. In addition, `cl-acltool` programs rules in hardware for switch port interfaces, which `iptables`, `ip6tables` and `ebtables` cannot do on their own.

## Traffic Rules

### Chains

ACLs in Cumulus Linux classify and control packets to, from, and across the switch, asserting policies at layer 2, 3 and 4 of the {{<exlink url="https://en.wikipedia.org/wiki/OSI_model" text="OSI model">}} by inspecting packet and frame headers according to a list of rules. The `iptables`, `ip6tables`, and `ebtables` userspace applications provide syntax you use to define rules.

The rules inspect or operate on packets at several points (*chains*) in the life of the packet through the system:

{{< img src = "/images/cumulus-linux/acl-chains.png" >}}

- **PREROUTING** touches packets before the switch routes them.
- **INPUT** touches packets after the switch determines that the packets are for the local system but before the control plane software receives them.
- **FORWARD** touches transit traffic as it moves through the switch.
- **OUTPUT** touches packets from the control plane software before they leave the switch.
- **POSTROUTING** touches packets immediately before they leave the switch but after a routing decision.

### Tables

When you build rules to affect the flow of traffic, *tables* can access the individual chains. Linux provides three tables by default:

- **Filter** classifies traffic or filters traffic
- **NAT** applies Network Address Translation rules
- **Mangle** alters packets as they move through the switch

Each table has a set of default chains that modify or inspect packets at different points of the path through the switch. Chains contain the individual rules to influence traffic.

### Rules

Rules classify the traffic you want to control. You apply rules to chains, which attach to tables.

{{< img src = "/images/cumulus-linux/acl-tables-chains-rules.png" >}}

Rules have several different components:

{{< img src = "/images/cumulus-linux/acl-anatomy-rule-50.png" >}}

- **Table:** The first argument is the *table*.
- **Chain:** The second argument is the *chain*. Each table supports several different chains. See {{<link url="#tables" text="Tables">}} above.
- **Matches:** The third argument is the *match*. You can specify multiple matches in a single rule. However, the more matches you use in a rule, the more memory the rule consumes.
- **Jump:** The *jump* specifies the target of the rule; what action to take if the packet matches the rule. If you omit this option in a rule, matching the rule has no effect on the packet, but the counters on the rule increment.
- **Targets:** The *target* is a user-defined chain (other than the one this rule is in), one of the special built-in targets that decides the fate of the packet immediately (like DROP), or an extended target. See {{<link url="#supported-rule-types" text="Supported Rule Types">}} below for different target examples.

### How Rules Parse and Apply

The switch reads all the rules from each chain from `iptables`, `ip6tables`, and `ebtables` and enters them in order into either the filter table or the mangle table. The switch reads the rules from the kernel in the following order:

- IPv6 (`ip6tables`)
- IPv4 (`iptables`)
- `ebtables`

When you combine and put rules into one table, the order determines the relative priority of the rules; `iptables` and `ip6tables` have the highest precedence and `ebtables` has the lowest.

The Linux packet forwarding construct is an overlay for how the silicon underneath processes packets. Be aware of the following:

- The switch silicon reorders rules when `switchd` writes to the ASIC, whereas traditional `iptables` execute the list of rules in order.
- All rules, except for POLICE and SETCLASS rules, are terminating; after a rule matches, the action occurs and no more rules process.

- When processing traffic, rules affecting the FORWARD chain that specify an ingress interface process before rules that match on an egress interface. As a workaround, rules that only affect the egress interface can have an ingress interface wildcard (only *swp+* and *bond+*) that matches any interface you apply so that you can maintain order of operations with other input interface rules. For example, with the following rules:

    ```
    -A FORWARD -i swp1 -j ACCEPT
    -A FORWARD -o swp1 -j ACCEPT   <-- This rule processes LAST (because of egress interface matching)
    -A FORWARD -i swp2 -j DROP
    ```

    If you modify the rules like this, they process in order:

    ```
    -A FORWARD -i swp1 -j ACCEPT
    -A FORWARD -i swp+ -o $PORTA -j ACCEPT   <-- These rules are performed in order (because of wildcard match on the ingress interface)
    -A FORWARD -i swp2 -j DROP
    ```

- When using rules that do a mangle and a filter lookup for a packet, Cumulus Linux processes them in parallel and combines the action.
- If there is no ingress interface or egress interface match, Cumulus Linux installs FORWARD chain rules in ingress by default.
- When using the OUTPUT chain, you must assign rules to the source. For example, if you assign a rule to the switch port in the direction of traffic but the source is a bridge (VLAN), the rule does not affect the traffic and you must apply it to the bridge.
- If you need to apply a rule to all transit traffic, use the FORWARD chain, not the OUTPUT chain.
- The switch puts `ebtable` rules into either the IPv4 or IPv6 memory space depending on whether the rule uses IPv4 or IPv6 to make a decision. The switch only puts layer 2 rules that match the MAC address into the IPv4 memory space.

### Rule Placement in Memory

INPUT and ingress (`FORWARD -i`) rules occupy the same memory space. A rule counts as ingress if you set the `-i` option. If you set both input and output options (`-i` and `-o`), the switch considers the rule as ingress and occupies that memory space. For example:

```
-A FORWARD -i swp1 -o swp2 -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT
```

{{%notice note%}}
If you set an output flag with the INPUT chain, you see an error. For example:

```
-A FORWARD,INPUT -i swp1 -o swp2 -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT
error: line 2 : output interface specified with INPUT chain error processing rule '-A FORWARD,INPUT -i swp1 -o swp2 -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT'
```

If you remove the `-o` option and the interface, it is a valid rule.
{{%/notice%}}
<!-- vale off -->
### Nonatomic Update Mode and Atomic Update Mode
<!-- vale on -->
Cumulus Linux enables *atomic update mode* by default. However, this mode limits the number of ACL rules that you can configure.

{{< img src = "/images/cumulus-linux/acl-update-operation-atomic.png" >}}

To increase the number of configurable ACL rules, configure the switch to operate in *nonatomic mode*.

{{< img src = "/images/cumulus-linux/acl-update-operation-nonatomic.png" >}}

Instead of reserving 50% of your TCAM space for atomic updates, nonatomic mode runs incremental updates that use available free space to write the new TCAM rules, then swap over to the new rules. Cumulus Linux deletes the old rules and frees up the original TCAM space. If there is insufficient free space to complete this task, the regular nonatomic (non-incremental) update runs, which interrupts traffic.

{{< img src = "/images/cumulus-linux/acl-update-del.png" >}}

{{< img src = "/images/cumulus-linux/acl-update-add.png" >}}

Nonatomic updates offer better scaling because all TCAM resources actively impact traffic. With atomic updates, half of the hardware resources are on standby and do not actively impact traffic.

*Incremental nonatomic updates* are table based, so they do not interrupt network traffic when you install new rules. The rules map to the following tables and update in this order:

- mirror (ingress only)
- ipv4-mac (can be both ingress and egress)
- ipv6 (ingress only)

The incremental nonatomic update operation follows this order:

1. Updates are incremental, one table at a time without stopping traffic.
2. Cumulus Linux checks if the rules in a table are different from installation time; if a table does not have any changes, it does not reinstall the rules.
3. If there are changes in a table, the new rules populate in new groups or slices in hardware, then that table switches over to the new groups or slices.
4. Finally, old resources for that table free up. This process repeats for each of the tables listed above.
5. If there are insufficient resources to hold both the new rule set and old rule set, Cumulus Linux tries regular nonatomic mode, which interrupts network traffic.
6. If the regular nonatomic update fails, Cumulus Linux reverts back to the previous rules.

To set nonatomic mode:

{{< tabs "TabID146 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system acl mode non-atomic 
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
- On Spectrum-2 and later, NVUE reloads `switchd` after you run and apply the `nv set system acl mode` command. Reloading `switchd` does **not** interrupt network services.
- On Spectrum 1, NVUE restarts `switchd` after you run and apply the `nv set system acl mode` command. Restarting `switchd` causes all network ports to reset in addition to resetting the switch hardware configuration.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/cumulus/switchd.conf` file to add `acl.non_atomic_update_mode = TRUE`:

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
   ...
   acl.non_atomic_update_mode = TRUE
   ```

2. On Spectrum-2 and later, reload `switchd` for the changes to take effect. Reloading `switchd` does **not** interrupt network services.

   ```
   cumulus@switch:~$ sudo systemctl reload switchd.service
   ```

   On Spectrum 1, restart `switchd` for the changes to take effect. Restarting `switchd` causes all network ports to reset in addition to resetting the switch hardware configuration.

   ```
   cumulus@switch:~$ sudo systemctl restart switchd.service
   ```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
During regular *non-incremental nonatomic updates*, traffic stops, then continues after all the new configuration is in the hardware.
{{%/notice%}}

### iptables, ip6tables, and ebtables

Do not use `iptables`, `ip6tables`, `ebtables` directly; installed rules only apply to the Linux kernel and Cumulus Linux does not hardware accelerate. When you run `cl-acltool -i`, Cumulus Linux resets all rules and deletes anything that is not in `/etc/cumulus/acl/policy.conf`.

For example, the following rule appears to work:

```
cumulus@switch:~$ sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
```

The `cl-acltool -L` command shows the rule:

```
cumulus@switch:~$ sudo cl-acltool -L ip
-------------------------------
Listing rules of type iptables:
-------------------------------

TABLE filter :
Chain INPUT (policy ACCEPT 72 packets, 5236 bytes)
pkts bytes target prot opt in out source destination
0 0 DROP icmp -- any any anywhere anywhere icmp echo-request
```

However, Cumulus Linux does not synchronize the rule to hardware. Running `cl-acltool -i` or `reboot` removes the rule without replacing it. To ensure that Cumulus Linux hardware accelerates all rules that can be in hardware, add them to `/etc/cumulus/acl/policy.conf` and install them with the `cl-acltool -i` command.

### Estimate the Number of Rules

To estimate the number of rules you can create from an ACL entry, first determine if the ACL entry is ingress or egress. Then, determine if the entry is an `IPv4-mac` or `IPv6` type rule. This determines the slice to which the rule belongs. Use the following to determine how many entries the switch uses for each type.

By default, each entry occupies one double wide entry, except if the entry is one of the following:
- An entry with multiple comma-separated input interfaces splits into one rule for each input interface. For example, this entry splits into two rules:

  ```
  -A FORWARD -i swp1s0,swp1s1 -p icmp -j ACCEPT
  ```

- An entry with multiple comma-separated output interfaces splits into one rule for each output interface. This entry splits into two rules:

    ```
    -A FORWARD -i swp+ -o swp1s0,swp1s1 -p icmp -j ACCEPT
    ```

- An entry with both input and output comma-separated interfaces splits into one rule for each combination of input and output interface. This entry splits into four rules:

    ```
    -A FORWARD -i swp1s0,swp1s1 -o swp1s2,swp1s3 -p icmp -j ACCEPT
    ```

- An entry with multiple layer 4 port ranges splits into one rule for each range. For example, this entry splits into two rules:

    ```
    -A FORWARD -i swp+ -p tcp -m multiport --dports 1050:1051,1055:1056 -j ACCEPT
    ```

   {{%notice note%}}
You can only use port ranges for ingress rules.
{{%/notice%}}

### Match on VLAN IDs on Layer 2 Interfaces

You can match on VLAN IDs on layer 2 interfaces for ingress rules. The following example matches on a VLAN and DSCP class, and sets the internal class of the packet. For extended matching on IP fields, combine this rule with ingress iptable rules.

```
[ebtables]
-A FORWARD -p 802_1Q --vlan-id 100 -j mark --mark-set 102

[iptables]
-A FORWARD -i swp31 -m mark --mark 102 -m dscp --dscp-class CS1 -j SETCLASS --class 2
```

{{%notice note%}}
- Cumulus Linux reserves `mark` values between 0 and 100; for example, if you use `--mark-set 10`, you see an error. Use mark values between 101 and 4196.
- You cannot mark multiple VLANs with the same value.
- If you enable {{<link url="EVPN-Multihoming" text="EVPN-MH">}} and configure VLAN match rules in ebtables with a `mark` target, the ebtables rule might overwrite the `mark` set by traffic class rules you configure for EVPN-MH on ingress. Egress EVPN MH traffic class rules that match the ingress traffic class `mark` might not get hit. To work around this issue, add ebtable rules to `ACCEPT` the packets already marked by EVPN-MH traffic class rules on ingress.
{{%/notice%}}

## Install and Manage ACL Rules with NVUE

Instead of crafting a rule by hand, then installing it with `cl-acltool`, you can use NVUE commands. Cumulus Linux converts the commands to the `/etc/cumulus/acl/policy.d/50_nvue.rules` file. The rules you create with NVUE are independent of the default files `/etc/cumulus/acl/policy.d/00control_plane.rules` and `99control_plane_catch_all.rules`.

{{%notice note%}}
Cumulus Linux 5.0 and later uses the `-t mangle -A PREROUTING` chain for ingress rules and the `-t mangle -A POSTROUTING` chain for egress rules instead of the `- A FORWARD` chain used in previous releases.
{{%/notice%}}

Consider the following `iptables` rule:

```
-t mangle -A PREROUTING -i swp1 -s 10.0.14.2/32 -d 10.0.15.8/32 -p tcp -j ACCEPT
```

To create this rule with NVUE, follow the steps below. NVUE adds all options in the rule automatically.

1. Set the rule type, the matching protocol, source IP address and port, destination IP address and port, and the action. You must provide a name for the rule (EXAMPLE1 in the commands below):

   ```
   cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
   cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
   cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip source-ip 10.0.14.2/32
   cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp source-port ANY
   cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip dest-ip 10.0.15.8/32
   cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp dest-port ANY
   cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action permit
   ```

   For firewall IPv4 type ACLs on the control plane, you can match on the hashlimit module (`hashimit`), the connection state (`connection-state`), and the recent module (`recent-list`). Refer to {{<link url="Firewall-Rules/#add-firewall-rules" text="Firewall Rules">}}.

2. Apply the rule to an inbound or outbound interface with the `nv set interface <interface> acl` command.
   
   - For rules affecting the -t mangle -A PREROUTING chain (-A FORWARD in previous releases), apply the rule to an inbound or outbound interface: For example:

   ```
   cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
   cumulus@switch:~$ nv config apply
   ```

   - For rules affecting the INPUT or OUPUT chain (-A INPUT or -A OUTPUT), apply the rule to a control plane interface. For example:

   ```
   cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound control-plane
   cumulus@switch:~$ nv config apply
   ```

To see the installed rule, either examine the `/etc/cumulus/acl/policy.d/50_nvue.rules` file or run the NVUE `nv show acl <rule-name> rule <ID>` command:

```
cumulus@switch:~$ sudo cat /etc/cumulus/acl/policy.d/50_nvue.rules
[iptables]

## ACL EXAMPLE1 in dir inbound on interface swp1 ##
-t mangle -A PREROUTING -i swp1 -s 10.0.14.2/32 -d 10.0.15.8/32 -p tcp -j ACCEPT
...
```

```
cumulus@switch:~$ nv show acl EXAMPLE1 rule 10 
                     operational   applied     
-------------------  ------------  ------------
match                                          
  ip                                           
    source-ip        10.0.14.2/32  10.0.14.2/32
    dest-ip          10.0.15.8/32  10.0.15.8/32
    protocol         tcp           tcp         
    tcp                                        
      [source-port]  ANY           ANY         
      [dest-port]    ANY           ANY
```

To remove this rule, run the `nv unset acl <acl-name>` and `nv unset interface <interface> acl <acl-name>` commands. These commands delete the rule from the `/etc/cumulus/acl/policy.d/50_nvue.rules` file.

```
cumulus@switch:~$ nv unset acl EXAMPLE1
cumulus@switch:~$ nv unset interface swp1 acl EXAMPLE1
cumulus@switch:~$ nv config apply
```

To show ACL statistics per interface, such as the total number of bytes that match the ACL rule, run the `nv show interface <interface-id> acl <acl-id> statistics` or `nv show interface <interface-id> acl <acl-id> statistics <rule-id>` command.

To see the list of all NVUE ACL commands, run the `nv list-commands acl` command.

<!-- vale off -->
## Install and Manage ACL Rules with cl-acltool
<!-- vale on -->
You can manage Cumulus Linux ACLs with `cl-acltool`. Rules write first to the `iptables` chains, as described above, and then synchronize to hardware through `switchd`.

To examine the current state of chains and list all installed rules, run:

```
cumulus@switch:~$ sudo cl-acltool -L all
 -------------------------------
Listing rules of type iptables:
-------------------------------
TABLE filter :
Chain INPUT (policy ACCEPT 432K packets, 31M bytes)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere            
    0     0 DROP       all  --  swp+   any     127.0.0.0/8          anywhere            
    0     0 DROP       all  --  swp+   any     base-address.mcast.net/4  anywhere            
    0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere            
    0     0 ACCEPT     all  --  swp+   any     anywhere             anywhere            

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 457K packets, 35M bytes)
 pkts bytes target     prot opt in     out     source               destination
...
```

To list installed rules using native `iptables`, `ip6tables` and `ebtables`, use the `-L` option with the respective commands:

```
cumulus@switch:~$ sudo iptables -L
cumulus@switch:~$ sudo ip6tables -L
cumulus@switch:~$ sudo ebtables -L
```

To remove all installed rules, run:

```
cumulus@switch:~$ sudo cl-acltool -F all
```

To remove only the IPv4 `iptables` rules, run:

```
cumulus@switch:~$ sudo cl-acltool -F ip
```

If the install fails, ACL rules in the kernel and hardware roll back to the previous state. You also see errors from programming rules in the kernel or ASIC.

## Install Packet Filtering (ACL) Rules

`cl-acltool` takes access control list (ACL) rule input in files. Each ACL policy file includes `iptables`, `ip6tables` and `ebtables` categories under the tags `[iptables]`, `[ip6tables]` and `[ebtables]`. You must assign each rule in an ACL policy to one of the rule categories.

See `man cl-acltool(5)` for ACL rule details. For `iptables` rule syntax, see `man iptables(8)`. For `ip6tables` rule syntax, see `man ip6tables(8)`. For `ebtables` rule syntax, see `man ebtables(8)`.

See `man cl-acltool(5)` and `man cl-acltool(8)` for more details on using `cl-acltool`.

{{%notice note%}}
By default:

- ACL policy files are in `/etc/cumulus/acl/policy.d/`.
- All `*.rules` files in `/etc/cumulus/acl/policy.d/` directory are also in `/etc/cumulus/acl/policy.conf`.
- All files in the `policy.conf` file install when the switch boots up.
- The `policy.conf` file expects rule files to have a `.rules` suffix as part of the file name.
{{%/notice%}}

Here is an example ACL policy file:

```
[iptables]
-A INPUT -i swp1 -p tcp --dport 80 -j ACCEPT
-A FORWARD -i swp1 -p tcp --dport 80 -j ACCEPT

[ip6tables]
-A INPUT -i swp1 -p tcp --dport 80 -j ACCEPT
-A FORWARD -i swp1 -p tcp --dport 80 -j ACCEPT

[ebtables]
-A INPUT -p IPv4 -j ACCEPT
-A FORWARD -p IPv4 -j ACCEPT
```

You can use wildcards or variables to specify chain and interface lists.

{{%notice note%}}
- You can only use *swp+* and *bond+* as wildcard names.
- swp+ rules apply as an aggregate, *not* per port. If you want to apply per port policing, specify a specific port instead of the wildcard.
{{%/notice%}}

```
INGRESS = swp+
INPUT_PORT_CHAIN = INPUT,FORWARD

[iptables]
-A $INPUT_PORT_CHAIN -i $INGRESS -p tcp --dport 80 -j ACCEPT

[ip6tables]
-A $INPUT_PORT_CHAIN -i $INGRESS -p tcp --dport 80 -j ACCEPT

[ebtables]
-A INPUT -p IPv4 -j ACCEPT
```

You can write ACL rules for the system into multiple files under the default `/etc/cumulus/acl/policy.d/` directory. The ordering of rules during installation follows the sort order of the files according to their file names.

Use multiple files to stack rules. The example below shows two rule files that separate rules for management and datapath traffic:

```
cumulus@switch:~$ ls /etc/cumulus/acl/policy.d/
00sample_mgmt.rules 01sample_datapath.rules
cumulus@switch:~$ cat /etc/cumulus/acl/policy.d/00sample_mgmt.rules

INGRESS_INTF = swp+
INGRESS_CHAIN = INPUT

[iptables]
# protect the switch management
-A $INGRESS_CHAIN -i $INGRESS_INTF -s 10.0.14.2 -d 10.0.15.8 -p tcp -j ACCEPT
-A $INGRESS_CHAIN -i $INGRESS_INTF -s 10.0.11.2 -d 10.0.12.8 -p tcp -j ACCEPT
-A $INGRESS_CHAIN -i $INGRESS_INTF -d 10.0.16.8 -p udp -j DROP

cumulus@switch:~$ cat /etc/cumulus/acl/policy.d/01sample_datapath.rules
INGRESS_INTF = swp+
INGRESS_CHAIN = INPUT, FORWARD

[iptables]
-A $INGRESS_CHAIN -i $INGRESS_INTF -s 192.0.2.5 -p icmp -j ACCEPT
-A $INGRESS_CHAIN -i $INGRESS_INTF -s 192.0.2.6 -d 192.0.2.4 -j DROP
-A $INGRESS_CHAIN -i $INGRESS_INTF -s 192.0.2.2 -d 192.0.2.8 -j DROP
```

Install all ACL policies under a directory:

```
cumulus@switch:~$ sudo cl-acltool -i -P ./rules
Reading files under rules
Reading rule file ./rules/01_http_rules.txt ...
Processing rules in file ./rules/01_http_rules.txt ...
Installing acl policy ...
Done.
```

Apply all rules and policies included in `/etc/cumulus/acl/policy.conf`:

```
cumulus@switch:~$ sudo cl-acltool -i
```

## Specify the Policy Files to Install

By default, Cumulus Linux installs any `.rules` file you configure in `/etc/cumulus/acl/policy.d/`. To add other policy files to an ACL, you need to include them in `/etc/cumulus/acl/policy.conf`. For example, for Cumulus Linux to install a rule in a policy file called `01_new.datapathacl`, add `include /etc/cumulus/acl/policy.d/01_new.rules` to `policy.conf`:

```
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
```

## Hardware Limitations for ACL Rules

The maximum number of rules that the switch hardware can store depends on:

- The combination of IPv4 and IPv6 rules; Cumulus Linux does not support the maximum number of rules for both IPv4 and IPv6 simultaneously.
- The number of default rules that Cumulus Linux provides.
- Whether the rules apply on ingress or egress.
- Whether the rules are in {{<link url="#nonatomic-update-mode-and-atomic-update-mode" text="atomic or nonatomic mode">}}; Cumulus Linux uses nonatomic mode rules when you enable nonatomic updates.
- Other resources that share the same table space, such as multicast route entries and internal VLAN counters.

If you exceed the maximum number of rules or run out of related memory resources for the ACL table, `cl-acltool -i` generates one of the following errors:

```
error: hw sync failed (sync_acl hardware installation failed) Rolling back .. failed.
error: hw sync failed (Bulk counter init failed with No More Resources). Rolling back ..
```

To troubleshoot this issue and manage resources with high VLAN and ACL scale, refer to {{<link url="#troubleshooting-acl-rule-installation-failures" text="Troubleshooting ACL Rule Installation Failures">}}.

NVIDIA Spectrum switches use a <span class="a-tooltip">[TCAM](## "Ternary Content Addressable Memory")</span> or <span class="a-tooltip">[ATCAM](## "Algorithmic TCAM")</span> to quickly look up various tables that include ACLs, multicast routes, and certain internal VLAN counters. Depending on the size of the network ACLs, multicast routes, and VLAN counters, you might need to adjust some parameters to fit your network requirements into the tables.

### TCAM Profiles on Spectrum 1

The NVIDIA Spectrum 1 ASIC (model numbers 2xx0) has one common TCAM space for both ingress and egress ACLs, which the switch also uses for multicast route entries.

Cumulus Linux controls the ACL and multicast route entry scale on NVIDIA Spectrum 1 switches with different TCAM profiles in combination with the ACL {{<link url="#nonatomic-update-mode-and-atomic-update-mode" text="atomic and nonatomic update setting">}}.

|Profile |Atomic Mode IPv4 Rules |Atomic Mode IPv6 Rules |Nonatomic Mode IPv4 Rules |Nonatomic Mode IPv6 Rules | Multicast Route Entries |
|------------|-------------------|-------------------|-------------------|-------------------------|-----------------|
|default |500 |250 |1000 |500| 1000 |
|ipmc-heavy|750 |500 |1500 |1000| 8500 |
|acl-heavy |1750 |1000 |3500 |2000| 450|
|ipmc-max |1000 |500 |2000 |1000 | 13000|
|ip-acl-heavy |6000 |0 |12000 |0| 0|

{{%notice note%}}
- Even though the table above specifies the ip-acl-heavy profile supports no IPv6 rules, Cumulus Linux does not prevent you from configuring IPv6 rules. However, there is no guarantee that IPv6 rules work under the ip-acl-heavy profile.
- The ip-acl-heavy profile shows an updated number of supported atomic mode and nonatomic mode IPv4 rules. The previously published numbers were 7500 for atomic mode and 15000 for nonatomic mode IPv4 rules.
{{%/notice%}}

To configure the profile you want to use, set the `tcam_resource.profile` parameter in the `/etc/mlx/datapath/tcam_profile.conf` file, then restart `switchd`:

```
cumulus@switch:~$ sudo nano /etc/mlx/datapath/tcam_profile.conf
...
tcam_resource.profile = ipmc-max
```

```
cumulus@switch:~$ sudo systemctl restart switchd.service
```

{{%notice note%}}
Spectrum 1 TCAM resource profiles that control ACLs and multicast route scale are different from {{<link url="Forwarding-Table-Size-and-Profiles" text="forwarding resource profiles">}} that control MAC table, IPv4, and IPv6 entry scale.
{{%/notice%}}

### ATCAM on Spectrum-2 and Later

Switches with Spectrum-2 and later use a newer <span class="a-tooltip">[KVD](## "Key Value Database")</span> scheme and an <span class="a-tooltip">[ATCAM](## "Algorithmic TCAM")</span> design that is more flexible and allows a higher ACL scale than Spectrum 1. There is no TCAM resource profile on Spectrum-2 and later.

The following table shows the tested ACL rule limits. Because the KVD and ATCAM space is shared with forwarding table entries, multicast route entries, and VLAN flow counters, these ACL limits might vary based on your use of other tables.

These limits are valid when using any Spectrum-2 and later forwarding profile, except for the l2-heavy-3 and v6-lpm-heavy1 profiles, which reduce the ACL scale significantly.

For Spectrum-2 and later, all profiles support the same number of rules.

|Atomic Mode IPv4 Rules |Atomic Mode IPv6 Rules |Nonatomic Mode IPv4 Rules |Nonatomic Mode IPv6 Rules |
|-------------------|-------------------|-------------------|-------------------------|
|12500 |6250 |25000 |12500|

For information about nonatomic and atomic mode, refer to {{<link url="#nonatomic-update-mode-and-atomic-update-mode" text="Nonatomic Update Mode and Atomic Update Mode">}}.

## ATCAM Resource Exhaustion

If you see error messages similar to `No More Resources .. Rolling back` when you try to apply ACLs, refer to {{<link url="#troubleshooting-acl-rule-installation-failures" text="Troubleshooting ACL Rule Installation Failures">}} for information on troublshooting and managing resources.

## Supported Rule Types

The `iptables`/`ip6tables`/`ebtables` construct tries to layer the Linux implementation on top of the underlying hardware but they are not always directly compatible. Here are the supported rules for chains in `iptables`, `ip6tables` and `ebtables`.

To learn more about any of the options shown in the tables below, run `iptables -h [name of option]`. The same help syntax works for options for `ip6tables` and `ebtables`.

```
root@leaf1# ebtables -h tricolorpolice
...
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
```

### iptables and ip6tables Rule Support

|Rule Element|Supported|Unsupported|
|--- |--- |--- |
|**Matches**|Src/Dst, IP protocol<br>In/out interface<br>IPv4: ecn, icmp, frag, ttl,<br>IPv6: icmp6, hl,<br>IP common: tcp ({{<link url="#filter-specific-tcp-flags" text="with flags">}}), udp, multiport, DSCP, addrtype|Rules with input/output Ethernet interfaces do not apply<br>Inverse matches|
|**Standard Targets**|ACCEPT, DROP|RETURN, QUEUE, STOP, Fall Thru, Jump|
|**Extended Targets**|LOG (IPv4/IPv6); UID is not supported for LOG<br>TCP SEQ, TCP options or IP options<br>ULOG<br>SETQOS<br>DSCP<br>Unique to Cumulus Linux:<br>SPAN<br>ERSPAN (IPv4/IPv6)<br>POLICE<br>TRICOLORPOLICE<br>SETCLASS||

### ebtables Rule Support

|Rule Element|Supported|Unsupported|
|--- |--- |--- |
|**Matches**|ether type<br>input interface/wildcard<br>output interface/wildcard<br>Src/Dst MAC<br>IP: src, dest, tos, proto, sport, dport<br>IPv6: tclass, icmp6: type, icmp6: code range, src/dst addr, sport, dport<br>802.1p (CoS)<br>VLAN|Inverse matches<br>Proto length|
|**Standard Targets**|ACCEPT, DROP|RETURN, CONTINUE, Jump, Fall Thru|
|**Extended Targets**|ULOG<br>LOG<br>Unique to Cumulus Linux:<br>SPAN<br>ERSPAN<br>POLICE<br>TRICOLORPOLICE<br>SETCLASS|

### Other Unsupported Rules

- Rules that have no matches and accept all packets in a chain are currently ignored.
- Chain default rules (that are ACCEPT) are also ignored.

#### Considerations

Splitting rules across the ingress TCAM and the egress TCAM causes the ingress IPv6 part of the rule to match packets going to all destinations, which can interfere with the regular expected linear rule match in a sequence. For example:

A higher rule can prevent a lower rule from matching:

Rule 1: `-A FORWARD -o vlan100 -p icmp6 -j ACCEPT`

Rule 2: `-A FORWARD -o vlan101 -p icmp6 -s 01::02 -j ACCEPT`

Rule 1 matches all icmp6 packets from to all out interfaces in the ingress TCAM.

This prevents rule 2 from matching, which is more specific but with a different out interface. Make sure to put more specific matches above more general matches even if the output interfaces are different.

When you have two rules with the same output interface, the lower rule might match depending on the presence of the previous rules.

Rule 1: `-A FORWARD -o vlan100 -p icmp6 -j ACCEPT`

Rule 2: `-A FORWARD -o vlan101 -s 00::01 -j DROP`

Rule 3: `-A FORWARD -o vlan101 -p icmp6 -j ACCEPT`

Rule 3 still matches for an icmp6 packet with sip 00:01 going out of vlan101. Rule 1 interferes with the normal function of rule 2 and/or rule 3.

When you have two adjacent rules with the same match and different output interfaces, such as:

Rule 1: `-A FORWARD -o vlan100 -p icmp6 -j ACCEPT`

Rule 2: `-A FORWARD -o vlan101 -p icmp6 -j DROP`

Rule 2 never matches on ingress. Both rules share the same mark.

## Common Examples

### Data Plane Policers

You can configure quality of service for traffic on the data plane. By using QoS policers, you can rate limit traffic so incoming packets get dropped if they exceed specified thresholds.

{{%notice note%}}
Counters on POLICE ACL rules in `iptables` do not show dropped packets due to those rules.
{{%/notice%}}

{{< tabs "653 ">}}
{{< tab "NVUE Commands ">}}

The following example rate limits the incoming traffic on swp1 to 400 packets per second with a burst of 200 packets per second:

```
cumulus@switch:~$ nv set acl example1 type ipv4
cumulus@switch:~$ nv set acl example1 rule 10 action police
cumulus@switch:~$ nv set acl example1 rule 10 action police mode packet
cumulus@switch:~$ nv set acl example1 rule 10 action police burst 200
cumulus@switch:~$ nv set acl example1 rule 10 action police rate 400
cumulus@switch:~$ nv set interface swp1 acl example1 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "/etc/cumulus/control-plane/policers.conf File ">}}

Use the `POLICE` target with `iptables`. `POLICE` takes these arguments:

- `--set-rate value` specifies the maximum rate in kilobytes (KB) or packets.
- `--set-burst value` specifies the number of packets or kilobytes (KB) allowed to arrive sequentially.
- `--set-mode string` sets the mode in *KB* (kilobytes) or *pkt* (packets) for rate and burst size.

For example, to rate limit the incoming traffic on swp1 to 400 packets per second with a burst of 200 packets per second and set this rule in your appropriate `.rules` file:

```
-t mangle -A PREROUTING -i swp1  -j POLICE --set-mode pkt --set-rate 400 --set-burst 200
```

{{< /tab >}}
{{< /tabs >}}

### Control Plane Policers

You can configure quality of service for traffic on the control plane and rate limit traffic so incoming packets drop if they exceed certain thresholds in the following ways:
- Run NVUE commands.
- Edit the `/etc/cumulus/control-plane/policers.conf` file.

{{%notice note%}}
Cumulus Linux 5.0 and later no longer uses INPUT chain rules to configure control plane policers.
{{%/notice%}}

{{< tabs "676 ">}}
{{< tab "NVUE Commands ">}}

To configure control plane policers:
- Set the Committed Information Rate (CIR) with the `nv set system control-plane policer <trap-group> rate` command. The CIR is the allowed incoming rate for the trap group. The incoming rate is the maximum rate in packets per second.
- Set the Committed Burst Rate (CBR) for the trap group with the `nv set system control-plane policer <trap-group> burst` command. The burst rate is the number of packets or kilobytes (KB) allowed to arrive sequentially after the CIR rate is exceeded.

The trap group can be: `arp`, `bfd`, `pim-ospf-rip`, `bgp`, `clag`, `icmp-def`, `dhcp-ptp`, `igmp`, `ssh`, `icmp6-neigh`, `icmp6-def-mld`, `lacp`, `lldp`, `rpvst`, `eapol`, `ip2me`, `acl-log`, `nat`, `stp`, `l3-local`, `span-cpu`, `catch-all`, or `NONE`.

The following example changes the PIM trap group forwarding rate and burst rate to 400 packets per second, and the IGMP trap group forwarding rate to 400 packets per second and burst rate to 200 packets per second:

```
cumulus@switch:~$ nv set system control-plane policer pim-ospf-rip rate 400
cumulus@switch:~$ nv set system control-plane policer pim-ospf-rip burst 400
cumulus@switch:~$ nv set system control-plane policer pim-ospf-rip state on
cumulus@switch:~$ nv set system control-plane policer igmp rate 400
cumulus@switch:~$ nv set system control-plane policer igmp burst 200
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "/etc/cumulus/control-plane/policers.conf File ">}}

To rate limit traffic using the `/etc/cumulus/control-plane/policers.conf` file, you:
- Enable an individual policer for a trap group (set `enable` to `TRUE`).
- Set the Committed Information Rate (CIR). The CIR is the allowed incoming rate for the trap group. The incoming rate is the maximum rate in packets per second.
- Set the Committed Burst Rate (CBR) for the trap group. The burst rate is the number of packets or kilobytes (KB) allowed to arrive sequentially after the CIR rate is exceeded.

After you edit the `/etc/cumulus/control-plane/policers.conf` file, you must reload the file with the `/usr/lib/cumulus/switchdctl --load /etc/cumulus/control-plane/policers.conf` command.

{{%notice note%}}
When `enable` is FALSE for a trap group, the trap group and `catch-all` trap group have a shared policer. When `enable` is TRUE, Cumulus Linux creates an individual policer for the trap group.
{{%/notice%}}

The following example changes the PIM trap group forwarding rate and burst rate to 400 packets per second, and the IGMP trap group forwarding rate to 400 packets per second and burst rate to 200 packets per second:

```
cumulus@switch:~$ sudo nano /etc/cumulus/control-plane/policers.conf
...
copp.pim_ospf_rip.enable = TRUE
copp.pim_ospf_rip.rate = 400
copp.pim_ospf_rip.burst = 400
...
copp.igmp.enable = TRUE
copp.igmp.rate = 400
copp.igmp.burst = 200
...
```

```
cumulus@switch:~$ /usr/lib/cumulus/switchdctl --load /etc/cumulus/control-plane/policers.conf
```

{{< /tab >}}
{{< /tabs >}}

To show the control plane police configuration and statistics, run the NVUE `nv show system control-plane policer --view=brief` command.

{{%notice note%}}
Cumulus Linux provides default control plane policer values. You can adjust these values to accommodate higher scale requirements for specific protocols as needed.
{{%/notice%}}

{{< expand "Policers Default Values" >}}
```
cumulus@leaf01:mgmt:~$ sudo cat /etc/cumulus/control-plane/policers.conf
copp.arp.enable = TRUE
copp.arp.rate = 800
copp.arp.burst = 800

copp.bfd.enable = TRUE
copp.bfd.rate = 2000
copp.bfd.burst = 2000

copp.pim_ospf_rip.enable = TRUE
copp.pim_ospf_rip.rate = 2000
copp.pim_ospf_rip.burst = 2000

copp.bgp.enable = TRUE
copp.bgp.rate = 2000
copp.bgp.burst = 2000

copp.clag.enable = TRUE
copp.clag.rate = 2000
copp.clag.burst = 2000

copp.icmp_def.enable = TRUE
copp.icmp_def.rate = 100
copp.icmp_def.burst = 40

copp.dhcp_ptp.enable = TRUE
copp.dhcp_ptp.rate = 2000
copp.dhcp_ptp.burst = 2000

copp.igmp.enable = TRUE
copp.igmp.rate = 1000
copp.igmp.burst = 1000

copp.ssh.enable = TRUE
copp.ssh.rate = 1000
copp.ssh.burst = 1000

copp.icmp6_neigh.enable = TRUE
copp.icmp6_neigh.rate = 500
copp.icmp6_neigh.burst = 500

copp.icmp6_def_mld.enable = TRUE
copp.icmp6_def_mld.rate = 300
copp.icmp6_def_mld.burst = 100

copp.lacp.enable = TRUE
copp.lacp.rate = 2000
copp.lacp.burst = 2000

copp.lldp.enable = TRUE
copp.lldp.rate = 200
copp.lldp.burst = 200

copp.rpvst.enable = TRUE
copp.rpvst.rate = 2000
copp.rpvst.burst = 2000

copp.eapol.enable = TRUE
copp.eapol.rate = 2000
copp.eapol.burst = 2000

copp.ip2me.enable = TRUE
copp.ip2me.rate = 1000
copp.ip2me.burst = 1000

copp.acl_log.enable = TRUE
copp.acl_log.rate = 100
copp.acl_log.burst = 100

copp.nat.enable = TRUE
copp.nat.rate = 200
copp.nat.burst = 200

copp.stp.enable = TRUE
copp.stp.rate = 2000
copp.stp.burst = 2000

copp.l3_local.enable = TRUE
copp.l3_local.rate = 400
copp.l3_local.burst = 100

copp.span_cpu.enable = TRUE
copp.span_cpu.rate = 100
copp.span_cpu.burst = 100

copp.catch_all.enable = TRUE
copp.catch_all.rate = 100
copp.catch_all.burst = 100
```

{{< /expand >}}

### Control Plane ACLs

You can configure control plane ACLs to apply a single rule for all packets forwarded to the CPU regardless of the source interface or destination interface on the switch. Control plane ACLs allow you to regulate traffic forwarded to applications on the switch with more granularity than traps and to configure ACLs to block SSH from specific addresses or subnets.

Cumulus Linux applies inbound control plane ACLs in the INPUT chain and outbound control plane ACLs in the OUTPUT chain.

{{%notice note%}}
Cumulus Linux does not support a **deny all** control plane rule.  This type of rule blocks traffic for interprocess communication and impacts overall system functionality.
{{%/notice%}}

The following example command applies the input control plane ACL called ACL1.

```
cumulus@switch:~$ nv set system control-plane acl ACL1 inbound
cumulus@switch:~$ nv config apply
```

The following example command applies the output control plane ACL called ACL2.

```
cumulus@switch:~$ nv set system control-plane acl ACL2 outbound
cumulus@switch:~$ nv config apply
```

To show statistics for all control-plane ACLs, run the `nv show system control-plane acl` command:

```
cumulus@switch:~$ nv show system control-plane acl
ACL Name   Rule ID  In Packets  In Bytes  Out Packets  Out Bytes
---------  -------  ----------  --------  -----------  ---------
acl1       1        0           0         0            0
           65535    0           0         0            0
acl2       1        0           0         0            0
           65535    0           0         0            0 
```

To show statistics for a specific control-plane ACL, run the `nv show system control-plane acl <acl_name> statistics` command:

```
cumulus@switch:~$ nv show system control-plane acl ACL1 statistics
Rule  In Packet  In Byte  Out Packet  Out Byte  Summary 

----  ---------  -------  ----------  --------  --------------------------- 

1     0          0 Bytes  0           0 Bytes   match.ip.dest-ip:   9.1.2.3 

2     0          0 Bytes  0           0 Bytes   match.ip.source-ip: 7.8.2.3 
```

### Set DSCP on Transit Traffic

The examples here use the *mangle* table to modify the packet as it transits the switch. DSCP is in {{<exlink url="https://en.wikipedia.org/wiki/Differentiated_services#Configuration_guidelines" text="decimal notation">}} in the examples below.

{{< tabs "730 ">}}
{{< tab "iptables rule ">}}

```
[iptables]

#Set SSH as high priority traffic.
-t mangle -A PREROUTING -i swp+ -p tcp -m multiport --dports 22 -j SETQOS --set-dscp 46

#Set everything coming in swp1 as AF13
-t mangle -A PREROUTING -i swp1  -j SETQOS --set-dscp 14

#Set Packets destined for 10.0.100.27 as best effort
-t mangle -A PREROUTING -i swp+ -d 10.0.100.27/32 -j SETQOS --set-dscp 0

#Example using a range of ports for TCP traffic
-t mangle -A PREROUTING -i swp+ -s 10.0.0.17/32 -d 10.0.100.27/32 -p tcp -m multiport --sports 10000:20000 -m multiport --dports 10000:20000 -j SETQOS --set-dscp 34
```

Apply the rule:

```
cumulus@switch:~$ sudo cl-acltool -i
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

To set SSH as high priority traffic:

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp dest-port 22
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action set dscp 46
cumulus@switch:~$ nv set interface swp1-48 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

To set everything coming in swp1 as AF13:

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action set dscp 14
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

To set Packets destined for 10.0.100.27 as best effort:

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip dest-ip 10.0.100.27/32
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action set dscp 0
cumulus@switch:~$ nv set interface swp1-48 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

To use a range of ports for TCP traffic:

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip source-ip 10.0.0.17/32
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp source-port 10000:20000
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip dest-ip 10.0.100.27/32
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp dest-port 10000:20000
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action set dscp 34
cumulus@switch:~$ nv set interface swp1-48 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
To specify all ports on the switch in NVUE (swp+ in an iptables rule), you must set the range of interfaces on the switch as in the examples above (`nv set interface swp1-48`). This command creates as many rules in the `/etc/cumulus/acl/policy.d/50_nvue.rules` file as the number of interfaces in the range you specify.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

### Filter Specific TCP Flags

The example rule below drops ingress IPv4 TCP packets when you set the SYN bit and reset the RST, ACK, and FIN bits. The rule applies inbound on interface swp1. After configuring this rule, you cannot establish new TCP sessions that originate from ingress port swp1. You can establish TCP sessions that originate from any other port.

{{< tabs "991 ">}}
{{< tab "iptables rule ">}}

```
-t mangle -A PREROUTING -i swp1 -p tcp --tcp-flags  ACK,SYN,FIN,RST SYN -j DROP
```

Apply the rule:

```
cumulus@switch:~$ sudo cl-acltool -i
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 20 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 20 match ip tcp flags syn
cumulus@switch:~$ nv set acl EXAMPLE1 rule 20 match ip tcp mask rst
cumulus@switch:~$ nv set acl EXAMPLE1 rule 20 match ip tcp mask syn
cumulus@switch:~$ nv set acl EXAMPLE1 rule 20 match ip tcp mask fin
cumulus@switch:~$ nv set acl EXAMPLE1 rule 20 match ip tcp mask ack
cumulus@switch:~$ nv set acl EXAMPLE1 rule 20 action deny 
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

### Control Who Can SSH into the Switch

Run the following commands to control who can SSH into the switch.
In the following example, 10.10.10.1/32 is the interface IP address (or loopback IP address) of the switch and 10.255.4.0/24 can SSH into the switch.

{{< tabs "852 ">}}
{{< tab "iptables rule ">}}

```
-A INPUT -i swp+ -s 10.255.4.0/24 -d 10.10.10.1/32 -j ACCEPT
-A INPUT -i swp+ -d 10.10.10.1/32 -j DROP
```

Apply the rule:

```
cumulus@switch:~$ sudo cl-acltool -i
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl example2 type ipv4
cumulus@switch:~$ nv set acl example2 rule 10 match ip source-ip 10.255.4.0/24 
cumulus@switch:~$ nv set acl example2 rule 10 match ip dest-ip 10.10.10.1/32
cumulus@switch:~$ nv set acl example2 rule 10 action permit
cumulus@switch:~$ nv set acl example2 rule 20 match ip source-ip ANY 
cumulus@switch:~$ nv set acl example2 rule 20 match ip dest-ip 10.10.10.1/32
cumulus@switch:~$ nv set acl example2 rule 20 action deny
cumulus@switch:~$ nv set system control-plane acl example2 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

### Block Traffic towards the eth0 Interface

To block traffic towards the eth0 interface, apply an ACL on the system control plane instead of on the eth0 interface. The following example creates an ACL called DENY-IN that blocks traffic from ingressing eth0 with source IP address 192.168.200.10:

```
cumulus@switch:~$ nv set acl DENY-IN rule 10 action deny
cumulus@switch:~$ nv set acl DENY-IN rule 10 match ip source-ip 192.168.200.10
cumulus@switch:~$ nv set acl DENY-IN type ipv4
cumulus@switch:~$ nv set system control-plane acl DENY-IN inbound
cumulus@switch:~$ nv config apply
```

### Match on ECN Bits in the TCP IP Header

<span class="a-tooltip">[ECN](## "Explicit Congestion Notification")</span> allows end-to-end notification of network congestion without dropping packets. You can add ECN rules to match on the <span class="a-tooltip">[ECE](## "ECN-Echo")</span>, <span class="a-tooltip">[CWR](## "Congestion Window Received")</span>, and <span class="a-tooltip">[ECT](## "ECN Capable Transport")</span> flags in the TCP IPv4 header.

By default, ECN rules match a packet with the bit set. You can reverse the match by using an explanation point (!).

#### Match on the ECE Bit

After an endpoint receives a packet with the <span class="a-tooltip">[CE](## "Congestion Experienced")</span> bit set by a router, it sets the ECE bit in the returning ACK packet to notify the other endpoint that it needs to slow down.

To match on the ECE bit:

{{< tabs "TabID947 ">}}
{{< tab "iptables rule">}}

Create a rules file in the `/etc/cumulus/acl/policy.d` directory and add the following rule under `[iptables]`:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/30-tcp-flags.rules
[iptables]
-t mangle -A PREROUTING -i swp1 -p tcp -m ecn  --ecn-tcp-ece  -j ACCEPT
```

Apply the rule:

```
cumulus@switch:~$ sudo cl-acltool -i
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl example2 type ipv4
cumulus@switch:~$ nv set acl example2 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl example2 rule 10 match ip ecn flags tcp-ece
cumulus@switch:~$ nv set acl example2 rule 10 action permit
cumulus@switch:~$ nv set interface swp1 acl example2 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

#### Match on the CWR Bit

The **CWR** bit notifies the other endpoint of the connection that it received and reacted to an ECE.

To match on the CWR bit:

{{< tabs "TabID915 ">}}
{{< tab "iptables rule ">}}

Create a rules file in the `/etc/cumulus/acl/policy.d` directory and add the following rule under `[iptables]`:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/30-tcp-flags.rules
[iptables]
-t mangle -A PREROUTING -i swp1 -p tcp -m ecn  --ecn-tcp-cwr  -j ACCEPT
```

Apply the rule:

```
cumulus@switch:~$ sudo cl-acltool -i
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl example2 type ipv4
cumulus@switch:~$ nv set acl example2 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl example2 rule 10 match ip ecn flags tcp-cwr
cumulus@switch:~$ nv set acl example2 rule 10 action permit
cumulus@switch:~$ nv set interface swp1 acl example2 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

#### Match on the ECT Bit

The **ECT** codepoints negotiate if the connection is ECN capable by setting one of the two bits to 1. Routers also use the ECT bit to indicate that they are experiencing congestion by setting both the ECT codepoints to 1.

To match on the ECT bit:

{{< tabs "TabID979 ">}}
{{< tab "iptables rule">}}

Create a rules file in the `/etc/cumulus/acl/policy.d` directory and add the following rule under `[iptables]`:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/30-tcp-flags.rules
[iptables]
-t mangle -A PREROUTING -i swp1 -p tcp -m ecn  --ecn-ip-ect 1 -j ACCEPT
```

Apply the rule:

```
cumulus@switch:~$ sudo cl-acltool -i
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl example2 type ipv4
cumulus@switch:~$ nv set acl example2 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl example2 rule 10 match ip ecn ip-ect 1
cumulus@switch:~$ nv set acl example2 rule 10 action permit
cumulus@switch:~$ nv set interface swp1 acl example2 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

## Example Configuration

The following example demonstrates how Cumulus Linux applies several different rules.

{{< img src = "/images/cumulus-linux/acl-config-example.png" >}}

### Egress Rule

The following rule blocks any TCP traffic with destination port 200 going through leaf01 to server01 (rule 1 in the diagram above).

{{< tabs "1179 ">}}
{{< tab "iptables Rule ">}}

```
[iptables]
-t mangle -A POSTROUTING -o swp1 -p tcp -m multiport --dports 200 -j DROP
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp dest-port 200
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action deny
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 outbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

### Ingress Rule

The following rule blocks any UDP traffic with source port 200 going from server01 through leaf01 (rule 2 in the diagram above).

{{< tabs "1206 ">}}
{{< tab "iptables Rule ">}}

```
[iptables] 
-t mangle -A PREROUTING -i swp1 -p udp -m multiport --sports 200 -j DROP
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol udp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip udp source-port 200
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action deny
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

### Input Rule

The following rule blocks any UDP traffic with source port 200 and destination port 50 going from server02 to the leaf02 control plane (rule 3 in the diagram above).

{{< tabs "1065 ">}}
{{< tab "iptables Rule ">}}

```
[iptables] 
-A INPUT -i swp2 -p udp -m multiport --dports 50 -j DROP
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol udp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip udp dest-port 50
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action deny
cumulus@switch:~$ nv set interface swp2 acl EXAMPLE1 inbound control-plane
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

### Output Rule

The following rule blocks any TCP traffic with source port 123 and destination port 123 going from leaf02 to server02 (rule 4 in the diagram above).

{{< tabs "1092 ">}}
{{< tab "iptables Rule ">}}

```
[iptables] 
-A OUTPUT -o swp2 -p tcp -m multiport --sports 123 -m multiport --dports 123 -j DROP
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp source-port 123
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp dest-port 123
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action deny
cumulus@switch:~$ nv set interface swp2 acl EXAMPLE1 outbound control-plane
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}
<!--
### Combined Rules

{{< tabs "1118 ">}}
{{< tab "iptables Rule ">}}

The following rule blocks any TCP traffic with source port 123 and destination port 123 going from any switch port egress or generated from the switch.

```
[iptables] 
-A OUTPUT,FORWARD -o swp+ -p tcp --sport 123 --dport 123 -j DROP
```

This also becomes two ACLs and is the same as:

```
[iptables]
-A FORWARD -o swp+ -p tcp --sport 123 --dport 123 -j DROP 
-A OUTPUT -o swp+ -p tcp --sport 123 --dport 123 -j DROP
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp source-port 123
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 match ip tcp dest-port 123
cumulus@switch:~$ nv set acl EXAMPLE1 rule 10 action deny
cumulus@switch:~$ nv set interface swp1-48 acl EXAMPLE1 outbound
cumulus@switch:~$ nv set acl EXAMPLE2 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE2 rule 10 match ip protocol tcp
cumulus@switch:~$ nv set acl EXAMPLE2 rule 10 match ip tcp source-port 123
cumulus@switch:~$ nv set acl EXAMPLE2 rule 10 match ip tcp dest-port 123
cumulus@switch:~$ nv set acl EXAMPLE2 rule 10 action deny
cumulus@switch:~$ nv set interface swp1-48 acl EXAMPLE2 outbound control-plane
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}
-->
### Layer 2 Rules (ebtables)

The following rule blocks any traffic with source MAC address 00:00:00:00:00:12 and destination MAC address 08:9e:01:ce:e2:04 going from any switch port egress or ingress.

{{< tabs "1118 ">}}
{{< tab "iptables Rule ">}}

```
[ebtables]
-A FORWARD -s 00:00:00:00:00:12 -d 08:9e:01:ce:e2:04 -j DROP
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set acl EXAMPLE type mac
cumulus@switch:~$ nv set acl EXAMPLE rule 10 match mac source-mac 00:00:00:00:00:12
cumulus@switch:~$ nv set acl EXAMPLE rule 10 match mac dest-mac 08:9e:01:ce:e2:04
cumulus@switch:~$ nv set acl EXAMPLE rule 10 action deny
cumulus@switch:~$ nv set interface swp1-48 acl EXAMPLE inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

## Considerations

### Not All Rules Supported

Cumulus Linux does not support all `iptables`, `ip6tables`, or `ebtables` rules. Refer to {{<link url="#iptables-and-ip6tables-rule-support" text="Supported Rules">}} for specific rule support.

### ACL Log Policer Limits Traffic

To protect the CPU from overloading, Cumulus Linux limits traffic copied to the CPU to 1 packet per second by an ACL Log Policer.

### Bridge Traffic Limitations

Bridge traffic that matches LOG ACTION rules do not log to syslog; the kernel and hardware identify packets using different information.

### You Cannot Forward Log Actions

You cannot forward logged packets. The hardware cannot both forward a packet and send the packet to the control plane (or kernel) for logging. A log action must also have a drop action.

### SPAN Sessions that Reference an Outgoing Interface

SPAN sessions that reference an outgoing interface create mirrored packets based on the ingress interface before the routing/switching decision. See {{<link url="SPAN-and-ERSPAN#span-sessions-that-reference-an-outgoing-interface" text="SPAN Sessions that Reference an Outgoing Interface">}} and {{<link url="SPAN-and-ERSPAN/#use-the-cpu-port-as-the-span-destination" text="Use the CPU Port as the SPAN Destination">}} in the Network Troubleshooting section.
<!-- vale off -->
### iptables Interactions with cl-acltool
<!-- vale on -->
Because Cumulus Linux is a Linux operating system, you can use the `iptables` commands. However, consider using `cl-acltool` instead for the following reasons:
- Without using `cl-acltool`, rules do not install into hardware.
- Running `cl-acltool -i` (the installation command) resets all rules and deletes anything that is not in the `/etc/cumulus/acl/policy.conf` file.

For example, running the following command works:

```
cumulus@switch:~$ sudo iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
```

The rules appear when you run `cl-acltool -L`:

```
cumulus@switch:~$ sudo cl-acltool -L ip
-------------------------------
Listing rules of type iptables:
-------------------------------
TABLE filter :
Chain INPUT (policy ACCEPT 72 packets, 5236 bytes)
pkts bytes target  prot opt in   out   source    destination

0     0 DROP    icmp --  any  any   anywhere  anywhere      icmp echo-request
```

However, running `cl-acltool -i` or `reboot` removes them. To ensure that Cumulus Linux can hardware accelerate all rules that can be in hardware, place them in the `/etc/cumulus/acl/policy.conf` file, then run `cl-acltool -i`.
<!--
### Hardware Limitations

Due to hardware limitations in the Spectrum ASIC, {{<link url="Bidirectional-Forwarding-Detection-BFD" text="BFD policers">}} and the BFD-related control plane share rules. The following default rules share the same policer in the `00control_plan.rules` file:

```
[iptables]
-A $INGRESS_CHAIN -p udp --dport $BFD_ECHO_PORT -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000
-A $INGRESS_CHAIN -p udp --dport $BFD_PORT -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000
-A $INGRESS_CHAIN -p udp --dport $BFD_MH_PORT -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000

[ip6tables]
-A $INGRESS_CHAIN -i $INGRESS_INTF -p udp --dport $BFD_ECHO_PORT -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000 --set-class 7
-A $INGRESS_CHAIN -i $INGRESS_INTF -p udp --dport $BFD_PORT -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000 --set-class 7
-A $INGRESS_CHAIN -i $INGRESS_INTF -p udp --dport $BFD_MH_PORT -j POLICE --set-mode pkt --set-rate 2000 --set-burst 2000 --set-class 7
```

To work around this limitation, set the rate and burst for all these rules to the same values with the `--set-rate` and `--set-burst` options.
-->
### Where to Assign Rules

- If you assign a switch port to a bond, you must assign any egress rules to the bond.
- When using the OUTPUT chain, you must assign rules to the source. For example, if you assign a rule to the switch port in the direction of traffic but the source is a bridge (VLAN), the rule does not affect the traffic and you must apply the rule to the bridge.
- If you need to apply a rule to all transit traffic, use the FORWARD chain, not the OUTPUT chain.

### Troubleshooting ACL Rule Installation Failures

On Spectrum-2 and later, in addition to ACLs, items stored in KVD and ATCAM include internal counters for VLANs and interfaces in a bridge. If the network includes more than 1000 VLAN interfaces, the counters might occupy a significant amount of space and reduce the amount of available space for ACLs.

If ACL space is exhausted, you might see error messages similar to the following when you try to apply ACLs:

```
cumulus@switch:$ sudo cl-acltool -i -p 00control_plane.rules
Using user provided rule file 00control_plane.rules
Reading rule file 00control_plane.rules ...
Processing rules in file 00control_plane.rules ...
error: hw sync failed (sync_acl hardware installation failed)
Installing acl policy... Rolling back ..
failed.
```

```
error: hw sync failed (Bulk counter init failed with No More Resources). Rolling back ..
```

You might also see messages similar to the following in the `/var/log/syslog` file:

```
2023-12-07T16:31:32.386792-05:00 mlx-4700-51 sx_sdk: 1951 [FLOW_COUNTER] [NOTICE ]:
Spectrum_flow_counter_bulk_set: cm_bulk_block_add failed toallocated bulk size 64
```

You might also see messages similar to the following in the `/var/log/switchd.log` file:

```
2023-12-07T16:31:32.387219-05:00 mlx-4700-51 switchd[7354]: hal_mlx_sdk_counter_wrap.c:366 ERR
sx_api_flow_counter_bulk_set create failed with: No More Resources
2023-12-07T16:31:32.387338-05:00 mlx-4700-51 switchd[7354]: hal_mlx_flx_acl.c:9531 ERR
flow_counter_bulk_set create failed with: No More Resources
2023-12-07T16:31:32.387415-05:00 mlx-4700-51 switchd[7354]: hal_mlx_flx_acl.c:3202 ERR BULK
counter init failed with No More Resources
2023-12-07T16:31:32.387481-05:00 mlx-4700-51 switchd[7354]: hal_mlx_flx_acl.c:2765
 hal_mlx_flx_chain_desc_install returned 0
2023-12-07T16:31:32.387554-05:00 mlx-4700-51 switchd[7354]: hal_mlx_flx_acl.c:1981 ERR
acl_plan_install returned 0
2023-12-07T16:31:32.393928-05:00 mlx-4700-51 switchd[7354]: sync_acl.c:225 ERR BULK counter init
failed with No More Resources
2023-12-07T16:31:32.394047-05:00 mlx-4700-51 switchd[7354]: sync_acl.c:6669 ERR BULK counter init
failed with No More Resources
```

For information on ACL resource limitations, refer to {{<link url="#hardware-limitations-for-acl-rules" text="Hardware Limitations for ACL Rules">}}.

On Spectrum-2 and later, you might see resource errors when you try to configure more than 1000 VLAN interfaces because certain VLAN counters share space with ACL memory in the ATCAM.

To free up resources, you can:
- Reduce the number of specified VLANs or VLAN interfaces to the number you really need in the network.
- Free up VLAN flow counter space; edit the `/etc/mlx/datapath/stats.conf` file to uncomment and set the `hal.mlx.stats.vlan.enable` option to `FALSE`, then reload `switchd`:

  ```
  cumulus@switch:$ sudo nano /etc/mlx/datapath/stats.conf
  # Once the stat controls are enabled/disabled,
  # run 'systemctl reload switchd' for changes to take effect
  hal.mlx.stats.vlan.enable = FALSE
  ```

  ```
  cumulus@switch:$ sudo systemctl reload switchd.service
  ```

The flow counters are internal counters for debugging; you do not see the counters in `nv show interface <interface> counters` or `cl-netstat` commands.

To see how much space the flow counters consume, examine the `Flow Counters` line in the `cl-resource-query` output.

### ACLs Do not Match when the Output Port on the ACL is a Subinterface

The ACL does not match on packets when you configure a subinterface as the output port. The ACL matches on packets only if the primary port is as an output port. If a subinterface is an output or egress port, the packets match correctly.

For example:

```
-A FORWARD -o swp49s1.100 -j ACCEPT
```

### Egress ACL Matching on Bonds

Cumulus Linux does not support ACL rules that match on an outbound *bond* interface. For example, you cannot create the following rule:

```
[iptables]
-A FORWARD -o <bond_intf> -j DROP
```

To work around this issue, duplicate the ACL rule on each physical port of the bond. For example:

```
[iptables]
-A FORWARD -o <bond-member-port-1> -j DROP
-A FORWARD -o <bond-member-port-2> -j DROP
```

### SSH Traffic to the Management VRF

To allow SSH traffic to the management VRF, use `-i mgmt`, not `-i eth0`. For example:

```
-A INPUT -i mgmt -s 10.0.14.2/32 -p tcp --dport ssh -j ACCEPT
```
<!-- vale off -->
### INPUT Chain Rules and swp+
<!-- vale on -->
In INPUT chain rules, the `-i swp+` match works only if the destination of the packet is towards a layer 3 swp interface; the match does not work if the packet terminates at an SVI interface (for example, vlan10). To allow traffic towards specific SVIs, use rules without any interface match or rules with individual `-i <SVI>` matches.

## Related Information

- {{<exlink url="http://www.netfilter.org/" text="Netfilter website">}}
- {{<exlink url="http://www.netfilter.org/documentation/HOWTO//packet-filtering-HOWTO-6.html" text="Netfilter.org packet filtering how-to">}}
