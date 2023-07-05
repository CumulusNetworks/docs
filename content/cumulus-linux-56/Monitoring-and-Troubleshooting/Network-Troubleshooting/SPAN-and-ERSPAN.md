---
title: SPAN and ERSPAN
author: NVIDIA
weight: 1145
toc: 4
---
Cumulus Linux supports both <span style="background-color:#F5F5DC">[SPAN](## "Switched Port Analyzer")</span> and <span style="background-color:#F5F5DC">[ERSPAN](## "Encapsulated Remote SPAN")</span>.
- SPAN mirrors all packets that come in from or go out of an interface (the *SPAN source*), and copy and transmit the packets out of a local port or CPU (the *SPAN destination*) for monitoring. The SPAN destination port is also referred to as a mirror-to-port (MTP). The original packet is still switched, while a mirrored copy of the packet goes out of the MTP.
- ERSPAN sends the mirrored packets to a monitoring node located anywhere across the routed network. The switch finds the outgoing port of the mirrored packets by looking up the destination IP address in its routing table. The switch encapsulates the original layer 2 packet with GRE for IP delivery. The encapsulated packets have the following format:

```
 ----------------------------------------------------------
| MAC_HEADER | IP_HEADER | GRE_HEADER | L2_Mirrored_Packet |
 ----------------------------------------------------------
```

To reduce the volume of data, you can truncate the mirrored frames at a specified number of bytes. You can also configure SPAN and ERSPAN traffic rules (ACLs) to limit the traffic you mirror. You can limit traffic according to:
- Source or destination IP address
- IP protocol
- TCP or UDP source or destination port
- TCP flags
- An ingress port

You can configure SPAN and ERSPAN with either NVUE commands or `cl-acltool` rules. Do not run both NVUE commands and `cl-acltool` at the same time to configure SPAN and ERSPAN.

If you are an advanced user, you can {{<link url="#manual-configuration-advanced" text="edit the /etc/cumulus/switchd.d/port-mirror.conf file">}}; however, NVIDIA recommends you either run NVUE commands or use `cl-acltool`.

{{%notice note%}}
- On a switch with the Spectrum-2 ASIC or later, Cumulus Linux supports four SPAN destinations in atomic mode or eight SPAN destinations in non-atomic mode. On a switch with the Spectrum 1 ASIC, Cumulus Linux supports only a single SPAN destination in atomic mode or three SPAN destinations in non-atomic mode.
- WJH packet drop monitoring uses a SPAN destination; If you configure {{<link title="What Just Happened (WJH)" >}}, ensure that you do not exceed the total number of SPAN destinations allowed for your switch ASIC type.
- Multiple SPAN sources can point to the same SPAN destination, but a SPAN source *cannot* specify two SPAN destinations.
- Cumulus Linux does not support IPv6 ERSPAN destinations.
- You cannot use eth0 as a destination.
- You cannot mirror packets that *egress* a bond interface (such as bond1); you can only mirror packets that *egress* bond members (such as swp1, swp2 and so on).
- Mirrored traffic is not guaranteed. A congested MTP results in discarded mirrored packets.
- A oversubscribed SPAN and ERSPAN destination interface might result in data plane buffer depletion and buffer drops. Exercise caution when enabling SPAN and ERSPAN when the aggregate speed of all source ports exceeds the destination port.
- ERSPAN does not cause the kernel to send ARP requests to resolve the next hop for the ERSPAN destination. If an ARP entry for the destination or next hop does not already exist in the kernel, you need to manually resolve this before sending mirrored traffic (use `ping` or `arping`).
- Mirroring to the same interface that you are monitoring causes a recursive flood of traffic and might impact traffic on other interfaces.
- Cumulus VX does not support ACL-based SPAN, ERSPAN, or port mirroring. To capture packets in Cumulus VX, use the `tcpdump` command line network traffic analyzer.
{{%/notice%}}

## SPAN

This section describes how to configure SPAN on your switch.

{{< tabs "TabID32 ">}}
{{< tab "NVUE Commands ">}}

To configure SPAN with NVUE, run the `nv set system port-mirror session <session-id> span <option>` command.

SPAN configuration with NVUE requires a session ID, which is a number between 0 and 7.

You can set the following SPAN options:
- Source port
- Destination port
- Direction (ingress or egress)

The NVUE commands save the configuration in the `/etc/cumulus/switchd.d/port-mirror.conf` file.

### Example Commands

The following example commands mirror all packets received on swp1, and copy and transmit the packets to swp2 for monitoring:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port swp1
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp2
cumulus@switch:~$ nv config apply
```

The following example commands mirror all packets that go out of swp1, and copy and transmit the packets to swp2 for monitoring:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction egress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port swp1
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp2
cumulus@switch:~$ nv config apply
```

The following example commands mirror packets from all ports to swp53:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port ANY
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp53
cumulus@switch:~$ nv config apply
```

To reduce the volume of copied data, you can truncate the mirrored frames at a specified number of bytes. The size must be between 4 and 4088 bytes and a multiple of 4. The following commands truncate the mirrored frames for SPAN at 40 bytes:

```
cumulus@switch:~$ nv set system port-mirror session 1 span truncate size 40
cumulus@switch:~$ nv config apply
```

You can configure ACL rules to limit traffic according to source or destination IP address, IP protocol, TCP or UDP source or destination port, or TCP flags.

The following example command matches on swp1 ingress traffic that has the source IP address 10.10.1.1. When a match occurs, the traffic mirrors to swp2:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port swp1
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip source-ip 10.10.1.1
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp2
cumulus@switch:~$ nv config apply
```

The following example command matches OSPF packets coming in on swp1. When a match occurs, the traffic mirrors to swp2:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port swp1
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip protocol ospf
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp2
cumulus@switch:~$ nv config apply
```

The following example matches UDP packets coming in on bond1. When a match occurs, the traffic mirrors to swp53.

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port bond1
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip protocol udp
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp53
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "cl-acltool Configuration ">}}

{{%notice note%}}
- Always place your rule files in the `/etc/cumulus/acl/policy.d/` directory.
- Using `cl-acltool` with the `--out-interface` rule applies to transit traffic only; it does not apply to traffic sourced from the switch.
- `--out-interface` rules cannot target bond interfaces, only the bond members tied to them. For example, to mirror all packets going out of bond1 to swp53, where bond1 members are swp1 and swp2, create the rule `-A FORWARD --out-interface swp1,swp2 -j SPAN --dport swp53`.
{{%/notice%}}

1. Create a rules file in the `/etc/cumulus/acl/policy.d/` directory. The following example mirrors swp1 input traffic and swp4 output traffic to destination swp2.

   ```
   cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/span.rules
   [iptables]
   -A FORWARD --in-interface swp1 -j SPAN --dport swp2
   -A FORWARD --out-interface swp4 -j SPAN --dport swp2
   ```

3. Install the rules:

   ```
   cumulus@switch:~$ sudo cl-acltool -i
   Reading rule file /etc/cumulus/acl/policy.d/00control_plane.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/00control_plane.rules ...
   Reading rule file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
   Reading rule file /etc/cumulus/acl/policy.d/span.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/span.rules ...
   Installing acl policy
   done.
   ```

   {{%notice warning%}}
Do not run the `cl-acltool -i` command with `-P` option: `sudo cl-acltool -i  -P /etc/cumulus/acl/policy.d/span.rules`. The `-P` option removes **all** existing control plane rules or other installed rules and only installs the rules defined in the specified file.
{{%/notice%}}

4. Verify that the you installed the SPAN rules:

   ```
   cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
   38025 7034K SPAN       all  --  swp1   any     anywhere             anywhere             dport:swp2
   50832   55M SPAN       all  --  any    swp4    anywhere             anywhere             dport:swp2
   ```

SPAN sessions that reference an outgoing interface create the mirrored packets according to the ingress interface before the routing decision. For example, the following rule captures traffic that is ultimately destined to leave swp1 but mirrors the packets when they arrive on swp49. The rule transmits packets that reference the original VLAN tag, and source and destination MAC address at the time that swp49 originally receives the packet.

```
-A FORWARD --out-interface swp1 -j SPAN --dport swp49
```

### Example Rules

To mirror forwarded packets from all ports matching source IP address 20.0.1.0 and destination IP address 20.0.1.2 to port swp1:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -d 20.0.1.2 -j SPAN --dport swp1
```

To mirror ICMP packets from all ports to swp1:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -p icmp -j SPAN --dport swp1
```

To mirror forwarded UDP packets received from port swp1, towards destination IP address 20.0.1.2 and destination port 53:

```
-A FORWARD --in-interface swp1 -d 20.0.1.2 -p udp --dport 53 -j SPAN --dport swp1
```

To mirror all forwarded TCP packets with only SYN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL SYN -j SPAN --dport swp1
```

To mirror all forwarded TCP packets with only FIN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL FIN -j SPAN --dport swp1
```

To capture traffic that is received on bond1 and mirror the packets when on swp53

```
-A FORWARD --in-interface bond1 -j SPAN --dport swp53
```

{{< /tab >}}
{{< /tabs >}}

## CPU port as the SPAN Destination

You can set the CPU port as a SPAN destination interface to mirror data plane traffic to the CPU. The SPAN traffic goes to a separate network interface mirror where you can analyze it with `tcpdump`. This is a useful feature if you do not have any free external ports on the switch for monitoring. SPAN traffic does not appear on switch ports.

Cumulus Linux controls how much traffic reaches the CPU so that mirrored traffic does not overwhelm the CPU.

{{%notice note%}}
- Cumulus Linux does not support egress mirroring for control plane generated traffic to the CPU port.
- When you use an `cl-acltool` rule to set the CPU port as a SPAN destination interface, the rule applies on both ingress and egress. For packets that match the rule on *both* ingress and egress, Cumulus Linux mirrors the traffic only once to the destination interface.
{{%/notice%}}

{{< tabs "TabID271 ">}}
{{< tab "NVUE Commands ">}}

The following example rule matches on swp1 ingress traffic that has the source IP address 10.10.1.1. When a match occurs, the traffic mirrors to the CPU:

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action span cpu
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip source-ip 10.10.1.1
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

The following example rule matches on swp1 egress traffic that has the source IP address 10.10.1.1. When a match occurs, the traffic mirrors to the CPU:

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action span cpu
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip source-ip 10.10.1.1
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 outbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "cl-acltool Configuration ">}}

Create a file in the `/etc/cumulus/acl/policy.d/` directory and add the rules, then install the rule with the `sudo cl-acltool -i` command.

The following example rule matches on swp1 ingress traffic that has the source IP address 10.10.1.1. When a match occurs, the traffic mirrors to the CPU:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/span-cpu.rules
[iptables]
     -A FORWARD -i swp1 -s 10.10.1.1 -j SPAN --dport cpu
```

```
cumulus@switch:~$ sudo cl-acltool -i
```

The following example rule matches on swp1 egress traffic that has the source IP address 10.10.1.1. When a match occurs, the traffic mirrors to the CPU:

```
cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/span-cpu.rules
[iptables]
     -A FORWARD -o swp1 -s 10.10.1.1 -j SPAN --dport cpu
```

```
cumulus@switch:~$ sudo cl-acltool -i
```

{{< /tab >}}
{{< /tabs >}}

To use `tcpcdump` to monitor traffic mirrored to the CPU, run the following command:

```
cumulus@switch:~$ sudo tcpdump -i mirror
```

## ERSPAN

{{< tabs "TabID347 ">}}
{{< tab "NVUE Commands ">}}

To configure ERSPAN with NVUE, run the `nv set system port-mirror session <session-id> erspan <option>` command.

ERSPAN configuration requires a session ID, which is a number between 0 and 7.

You can set the following ERSPAN options:
- Source port
- Destination port
- Direction (ingress or egress)
- Source IP address for ERSPAN encapsulation
- Destination IP address for ERSPAN encapsulation

You can also truncate the mirrored frames at specified number of bytes. The size must be between 4 and 4088 bytes and a multiple of 4.

The NVUE commands save the configuration in the `/etc/cumulus/switchd.d/port-mirror.conf` file.

### Example Commands

The following example commands mirror all packets that swp1 receives, and copy and transmit the packets from source IP address 10.10.10.1 to destination IP address 10.10.10.234 through a GRE tunnel:

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan source-port swp1
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination source-ip 10.10.10.1
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination dest-ip 10.10.10.234
cumulus@switch:~$ nv config apply
```

The following example commands mirror all packets that go out of swp1, and copy and transmit the packets from source IP address 10.10.10.1 to destination IP address 10.10.10.234 through a GRE tunnel:

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan direction egress
cumulus@switch:~$ nv set system port-mirror session 1 erspan source-port swp1
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination source-ip 10.10.10.1
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination dest-ip 10.10.10.234
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "cl-acltool Configuration ">}}

1. Create a rules file in `/etc/cumulus/acl/policy.d/`. The following rule configures ERSPAN for all packets coming in from swp1 to destination 10.10.10.234.

     ```
     cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/erspan.rules
     [iptables]
     -A FORWARD --in-interface swp1 -j ERSPAN --src-ip 10.0.0.1 --dst-ip 10.10.10.234  --ttl 64
     EOF'
     ```

2. Install the rules:

   ```
   cumulus@switch:~$ sudo cl-acltool -i
   Reading rule file /etc/cumulus/acl/policy.d/00control_plane.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/00control_plane.rules ...
   Reading rule file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
   Reading rule file /etc/cumulus/acl/policy.d/erspan.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/erspan.rules ...
   Installing acl policy
   done.
   ```

3. Verify that you installed the ERSPAN rules:

     ```
     cumulus@switch:~$ sudo iptables -L -v | grep SPAN
     69  6804 ERSPAN     all  --  swp1   any     anywhere      anywhere       ERSPAN src-ip:10.0.0.1 dst-ip:10.10.10.234
     ```

- `src-ip` can be any IP address, even if it does not exist in the routing table.
- `dst-ip` must be an IP address reachable through the routing table and front-panel port (not the management port) or SVI. Use ping or ip route get <ip> to verify that the destination IP address is reachable. Set the `--ttl` option.

{{%notice note%}}
- If you use {{<exlink url="https://www.wireshark.org" text="Wireshark">}} to review the ERSPAN output, you might see the Wireshark error message `Unknown version, please report or test to use fake ERSPAN preference` and the trace might be unreadable. To resolve this issue, go to **Protocols \ ERSPAN** from the Wireshark General preferences and check the **Force to decode fake ERSPAN frame** option.
- To set up a {{<exlink url="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html" text="capture filter">}} on the destination switch that filters for a specific IP protocol, use `ip.proto == 47` to filter for GRE-encapsulated (IP protocol 47) traffic.
{{%/notice%}}

### Example Rules

To mirror forwarded packets from all ports matching the source IP address 10.0.0.1 and the destination IP address 10.10.10.234:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -d 20.0.1.2 -j ERSPAN --src-ip 10.0.0.1 --dst-ip 10.10.10.234
```

To mirror ICMP packets from all ports:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -p icmp -j ERSPAN --src-ip 10.0.0.1 --dst-ip 10.10.10.234
```

To mirror forwarded UDP packets from port swp1s0, towards destination IP address 10.10.10.234 and destination port 53:

```
-A FORWARD --in-interface swp1s0 -d 20.0.1.2 -p udp --dport 53 -j ERSPAN --src-ip 10.0.0.1 --10.10.10.234
```

To mirror all forwarded TCP packets with only SYN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL SYN -j ERSPAN --src-ip 10.0.0.1 --dst-ip 10.10.10.234
```

To mirror all forwarded TCP packets with only FIN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL FIN -j ERSPAN --src-ip 10.0.0.1 --dst-ip 10.10.10.234
```

{{< /tab >}}
{{< /tabs >}}

## Delete SPAN and ERSPAN Rules

{{< tabs "TabID443 ">}}
{{< tab "NVUE Commands ">}}

You can delete all SPAN and ERSPAN sessions with the `nv unset system port-mirror` command. For example:

```
cumulus@switch:~$ nv unset system port-mirror
cumulus@switch:~$ nv config apply
```

To delete a specific SPAN or ERSPAN session, run the `nv unset system port-mirror session <session-id>` command. For example:

```
cumulus@switch:~$ nv unset system port-mirror session 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "cl-acltool Configuration ">}}

Remove the rules file, then reload the default rules. For example:

```
cumulus@switch:~$ sudo rm  /etc/cumulus/acl/policy.d/span.rules
cumulus@switch:~$ sudo cl-acltool -i
```

To verify that the you removed the rules:

```
cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
```

{{< /tab >}}
{{< /tabs >}}

## Show SPAN and ERSPAN Configuration

To show SPAN and ERSPAN configuration for a specific session, run the NVUE `nv show system port-mirror session <session-id>` command. To show SPAN and ERSPAN configuration for all sessions, run the NVUE `nv show system port-mirror` command.

```
cumulus@switch:~$ nv show system port-mirror session 1
                 operational  applied  pending
---------------  -----------  -------  -------
erspan                                        
  enable                               off    
span                                          
  enable                               on     
  direction                            ingress
  [destination]                               
  [source-port]                        swp1   
  truncate                                    
    enable                             off  
```

You can also run the `sudo cl-acltool -L all | grep SPAN` or `sudo cl-acltool -L all | grep ERSPAN` command.

```
cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
    0     0 SPAN       all  --  any    swp1    10.10.1.1            anywhere             /* rule_id:1,acl_name:EXAMPLE1,dir:outbound,interface_id:swp1 */ dport:cpu
```

## Manual Configuration (Advanced)

If you are an advanced user, you can edit the `/etc/cumulus/switchd.d/port-mirror.conf` file to configure SPAN and ERSPAN.

The following example SPAN configuration mirrors all packets received on swp1, and copies and transmits the packets to swp2 for monitoring:

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/port-mirror.conf
Copyright © 2021 NVIDIA CORPORATION & AFFILIATES. ALL RIGHTS RESERVED.
#
# This software product is a proprietary product of Nvidia Corporation and its affiliates
# (the "Company") and all right, title, and interest in and to the software
# product, including all associated intellectual property rights, are and
# shall remain exclusively with the Company.
#
# This software product is governed by the End User License Agreement
# provided with the software product.
#
# [session_n]
# session-id = n
# mirror.session.n.direction = (ingress | egress)
# mirror.session.n.src = <swpx, bond>
# mirror.session.n.dest = (swpx | <src-ip> <dst-ip>)
# mirror.session.n.type = (span | erspan | none)
#
# Default is all sessions off
# mirror.session.all.type = none
[session_1]
session-id = 1
mirror.session.1.direction = ingress
mirror.session.1.src = swp1
mirror.session.1.dest = swp2
mirror.session.1.type = span
```

After you edit the configuration file, run the following command to the load the configuration:

```
cumulus@switch:~$ /usr/lib/cumulus/switchdctl --load /etc/cumulus/switchd.d/port-mirror.conf -prefix mirror
```
