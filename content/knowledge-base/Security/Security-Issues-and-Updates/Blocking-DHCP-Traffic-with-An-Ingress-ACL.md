---
title: Blocking DHCP Traffic with an Ingress ACL
author: NVIDIA
weight: 454
toc: 5
---
## Issue

Due to the forwarding pipeline in Cumulus Linux, you cannot use a traditional ACL to block DHCP traffic. The switch discards DHCP traffic in hardware and the CPU software forwards (traps) it. If you apply an IP ACL to match DHCP traffic, the statistics counter shows it as matching but the switch does not drop the traffic.

The following example shows an ACL for swp1:

```
cumulus@switch:~$ nv set acl BLOCK_DHCP rule 10 action deny
cumulus@switch:~$ nv set acl BLOCK_DHCP rule 10 match ip protocol udp
cumulus@switch:~$ nv set acl BLOCK_DHCP rule 10 match ip source-port 68
cumulus@switch:~$ nv set acl BLOCK_DHCP type ipv4
cumulus@switch:~$ nv set interface swp1 acl BLOCK_DHCP inbound
```

With the above ACL, if the host attached on swp1 requests an IP address using DHCP, there is a match on DHCP traffic; however the switch does not block this traffic because this is a hardware counter only and the forwarding pipeline uses a software path:

```
cumulus@switch:/home/cumulus# nv show interface swp1 acl BLOCK_DHCP statistics
Rule  In Packet  In Byte    Out Packet  Out Byte  Summary
----  ---------  ---------  ----------  --------  ------------------------
10    2          692 Bytes                        match.ip.protocol:   udp <<<<
                                                  match.ip.source-port: 68
```

## Resolution

Create an IP access list to match on the physdev device.

1. Run the following command to enable `netfilter` to process tagged packets:

   ```
   cumulus@switch:~$ sudo sysctl -w net.bridge.bridge-nf-filter-vlan-tagged=1
   ```

   To make this setting persistent, add the line `net.bridge.bridge-nf-filter-vlan-tagged = 1` to the `/etc/sysctl.conf` file:

   ```
   cumulus@switch:~$ sudo cat /etc/sysctl.conf | grep vlan
   net.bridge.bridge-nf-filter-vlan-tagged = 1
   ```

2. Add a file called `75BlockDHCP.rules` in the `/etc/cumulus/acl/policy.d/` directory with the following content:

   ```
   [iptables]
   -A FORWARD -m physdev --physdev-in swp1 -p udp --sport 68 -j DROP
   ```

   {{%notice note%}}
This example blocks ingress DHCP on swp1. To apply the rule to all interfaces, use the wildcard syntax `swp+`.
{{%/notice%}}

3. Apply the rule:

   ```
   cumulus@switch:~$ sudo cl-acltool -i
   ```

4. Verify the rule.

   ```
   cumulus@switch:~$ sudo cl-acltool -L ip | grep udp
    0     0 DROP       udp  --  any    any     anywhere   anywhere  PHYSDEV match --physdev-in swp1 udp spt:bootpc
   ```

   {{%notice note%}}
This counter does not increment.
{{%/notice%}}
