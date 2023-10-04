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

## SPAN

To configure SPAN to mirror ports on your switch, you create a port mirror session. The session ID is a number between 0 and 7.

You set the following SPAN options:
- Source port
- Destination port
- Direction (ingress or egress)

{{< tabs "TabID43 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set system port-mirror session <session-id> span <option>` command. The NVUE commands save the configuration in the `/etc/cumulus/switchd.d/port-mirror.conf` file.

To reduce the volume of data, you can truncate the mirrored frames at a specified number of bytes. The size must be between 4 and 4088 bytes and a multiple of 4.

### Example Commands

To mirror all packets received on swp1, and copy and transmit the packets to swp2 for monitoring:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port swp1
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp2
cumulus@switch:~$ nv config apply
```

To mirror all packets that go out of swp1, and copy and transmit the packets to swp2 for monitoring:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction egress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port swp1
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp2
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
SPAN sessions that reference an outgoing interface create the mirrored packets according to the ingress interface before the routing decision. For example, the above commands capture traffic that is ultimately destined to leave swp1 but mirrors the packets when they arrive on swp2. Packets that reference the original VLAN tag, and the source and destination MAC address transfer when swp2 originally receives the packet.
{{%/notice%}}

To mirror packets from all ports to swp53:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port swp1-54
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp53
cumulus@switch:~$ nv config apply
```

To mirror all packets received on bond1, and copy and transmit the packets to swp53 for monitoring:

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 span source-port bond1
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp53
cumulus@switch:~$ nv config apply
```

To truncate the mirrored frames at 40 bytes:

```
cumulus@switch:~$ nv set system port-mirror session 1 span truncate size 40
cumulus@switch:~$ nv config apply
```

### Delete SPAN Sessions

You can delete all SPAN sessions with the `nv unset system port-mirror` command. For example:

```
cumulus@switch:~$ nv unset system port-mirror
cumulus@switch:~$ nv config apply
```

To delete a specific SPAN session, run the `nv unset system port-mirror session <session-id>` command. For example:

```
cumulus@switch:~$ nv unset system port-mirror session 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.d/port-mirror.conf` file, then load the configuration.

The following example configuration mirrors all packets received on swp1, and copies and transmits the packets to swp2 for monitoring:

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

SPAN sessions that reference an outgoing interface create the mirrored packets according to the ingress interface before the routing decision. For example, the following rule captures traffic that is ultimately destined to leave swp1 but mirrors the packets when they arrive on swp49. The rule transmits packets that reference the original VLAN tag, and source and destination MAC address at the time that swp49 originally receives the packet.

```
[session_1]
session-id = 1
mirror.session.1.direction = egress
mirror.session.1.src = swp1
mirror.session.1.dest = swp49
mirror.session.1.type = span
```

{{< /tab >}}
{{< /tabs >}}

### Selective SPAN with ACLs

You can configure selective SPAN with ACLs to mirror a subset of traffic according to:
- Source or destination IP address
- IP protocol
- TCP or UDP source or destination port
- TCP flags
- An ingress port

{{< tabs "TabID209 ">}}
{{< tab "NVUE Commands ">}}

To match swp1 ingress traffic that has the source IP address 10.10.1.1 and mirror the traffic to swp2 when a match occurs:

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip source-ip 10.10.1.1
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action span swp2
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
```

To match OSPF packets coming in on swp1 and mirror the traffic to swp2 when a match occurs:

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip protocol ospf
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action span swp2
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
```

To match UDP packets coming in on bond1 and mirror the traffic to swp53 when a match occurs:

```
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip protocol udp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action span swp53
cumulus@switch:~$ nv set interface bond1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

{{%notice note%}}
- Always place your rule files in the `/etc/cumulus/acl/policy.d/` directory.
- Using `cl-acltool` with the `--out-interface` rule applies to transit traffic only; it does not apply to traffic sourced from the switch.
- `--out-interface` rules cannot target bond interfaces, only the bond members tied to them. For example, to mirror all packets going out of bond1 to swp53, where bond1 members are swp1 and swp2, create the rule `-A FORWARD --out-interface swp1,swp2 -j SPAN --dport swp53`.
{{%/notice%}}

1. Create a rules file in the `/etc/cumulus/acl/policy.d/` directory. The following example rules mirror ICMP packets that ingress swp1 to swp54 and UDP packets that egress swp4 to swp53:

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/span.rules
   [iptables]
   -A FORWARD --in-interface swp1 -p icmp -j SPAN --dport swp54
   -A FORWARD --out-interface swp4 -p udp -j SPAN --dport swp53
   ```

2. Install the rules:

   ```
   cumulus@switch:~$ sudo cl-acltool -i
   ```

   {{%notice warning%}}
Do not run the `cl-acltool -i` command with `-P` option. The `-P` option removes **all** existing control plane rules or other installed rules and only installs the rules defined in the specified file.
{{%/notice%}}

3. Verify that you installed the SPAN rules:

   ```
   cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
   38025 7034K SPAN       icmp --  swp1   any     anywhere             anywhere             dport:swp54
   50832   55M SPAN       udp  --  any    swp4    anywhere             anywhere             dport:swp53
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

{{< /tab >}}
{{< /tabs >}}

### CPU port as the SPAN Destination

You can set the CPU port as a SPAN destination interface to mirror data plane traffic to the CPU. The SPAN traffic goes to a separate network interface mirror where you can analyze it with `tcpdump`. This is a useful feature if you do not have any free external ports on the switch for monitoring. SPAN traffic does not appear on switch ports.

Cumulus Linux controls how much traffic reaches the CPU so that mirrored traffic does not overwhelm the CPU.

You configure the CPU port as the SPAN destination with ACLs.

To monitor traffic mirrored to the CPU, run the `tcpcdump -i mirror` command.

{{%notice note%}}
- Cumulus Linux does not support egress mirroring for control plane generated traffic to the CPU port.
- When you set the CPU port as a SPAN destination interface, Cumulus Linux mirrors packets that match the rule on *both* ingress and egress only one time to the destination interface.
{{%/notice%}}

{{< tabs "TabID271 ">}}
{{< tab "NVUE Commands ">}}

To match swp1 ingress traffic that has the source IP address 10.10.1.1 and mirror the traffic to the CPU when a match occurs:

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action span cpu
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip source-ip 10.10.1.1
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

To match swp1 egress traffic that has the source IP address 10.10.1.1 and mirror the traffic to the CPU when a match occurs:

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action span cpu
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip source-ip 10.10.1.1
cumulus@switch:~$ nv set acl EXAMPLE1 type ipv4
cumulus@switch:~$ nv set interface swp1 acl EXAMPLE1 outbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Create a file in the `/etc/cumulus/acl/policy.d/` directory and add rules.

   To match swp1 ingress traffic that has the source IP address 10.10.1.1 and mirror the traffic to the CPU when a match occurs:

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/span-cpu.rules
   [iptables]
     -A FORWARD -i swp1 -s 10.10.1.1 -j SPAN --dport cpu
   ```

   To match swp1 egress traffic that has the source IP address 10.10.1.1 and mirror the traffic to the CPU when a match occurs:

   ```
   -A FORWARD -o swp1 -s 10.10.1.1 -j SPAN --dport cpu
   ```

2. Install the rule:

   ```
   cumulus@switch:~$ sudo cl-acltool -i
   ```

   {{%notice warning%}}
Do not run the `cl-acltool -i` command with `-P` option. The `-P` option removes **all** existing control plane rules or other installed rules and only installs the rules defined in the specified file.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## ERSPAN

To configure ERSPAN to mirror ports on your switch, you create a port mirror session. The session ID is a number between 0 and 7.

You can set the following ERSPAN options:
- Source port
- Direction (ingress or egress)
- Source IP address for ERSPAN encapsulation
- Destination IP address for ERSPAN encapsulation

{{< tabs "TabID347 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set system port-mirror session <session-id> erspan <option>` command. The NVUE commands save the configuration in the `/etc/cumulus/switchd.d/port-mirror.conf` file.

To reduce the volume of data, you can truncate the mirrored frames at a specified number of bytes. The size must be between 4 and 4088 bytes and a multiple of 4.

### Example Commands

The following examples configure ERSPAN encapsulation from source IP address 10.10.10.1 to destination IP address 10.10.10.234.

To mirror all packets that arrive on swp1:

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan direction ingress
cumulus@switch:~$ nv set system port-mirror session 1 erspan source-port swp1
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination source-ip 10.10.10.1
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination dest-ip 10.10.10.234
cumulus@switch:~$ nv config apply
```

To mirror all packets that go out of swp1:

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan direction egress
cumulus@switch:~$ nv set system port-mirror session 1 erspan source-port swp1
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination source-ip 10.10.10.1
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination dest-ip 10.10.10.234
cumulus@switch:~$ nv config apply
```

### Delete ERSPAN Sessions

You can delete all ERSPAN sessions with the `nv unset system port-mirror` command. For example:

```
cumulus@switch:~$ nv unset system port-mirror
cumulus@switch:~$ nv config apply
```

To delete a specific ERSPAN session, run the `nv unset system port-mirror session <session-id>` command. For example:

```
cumulus@switch:~$ nv unset system port-mirror session 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/cumulus/switchd.d/port-mirror.conf` file, then load the configuration.

The following example ERSPAN configuration mirrors all packets received on swp1:

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
mirror.session.1.dest = 10.10.10.1 10.10.10.234
mirror.session.1.type = erspan
```

Run the following command to the load the configuration:

```
cumulus@switch:~$ /usr/lib/cumulus/switchdctl --load /etc/cumulus/switchd.d/port-mirror.conf -prefix mirror
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- If you use {{<exlink url="https://www.wireshark.org" text="Wireshark">}} to review the ERSPAN output, you might see the Wireshark error message `Unknown version, please report or test to use fake ERSPAN preference` and the trace might be unreadable. To resolve this issue, go to **Protocols \ ERSPAN** from the Wireshark General preferences and check the **Force to decode fake ERSPAN frame** option.
- To set up a {{<exlink url="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html" text="capture filter">}} on the destination switch that filters for a specific IP protocol, use `ip.proto == 47` to filter for GRE-encapsulated (IP protocol 47) traffic.
{{%/notice%}}

### Selective ERSPAN with ACLs

You can configure selective ERSPAN with ACLs to mirror a subset of traffic according to:
- Source or destination IP address
- IP protocol
- TCP or UDP source or destination port
- TCP flags
- An ingress port

{{< tabs "TabID414 ">}}
{{< tab "NVUE Commands ">}}

The following command mirrors inbound ICMP packets from all swp interfaces. The source IP address for ERSPAN encapsulation is 10.10.10.1 and the destination IP address for ERSPAN encapsulation is 10.10.10.234.

```
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 type ipv4
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 match ip protocol icmp
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action erspan source-ip 10.10.10.1
cumulus@switch:~$ nv set acl EXAMPLE1 rule 1 action erspan dest-ip 10.10.10.234
cumulus@switch:~$ nv set interface swp1-54 acl EXAMPLE1 inbound
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Create a rules file in `/etc/cumulus/acl/policy.d/`. The following rule configures ERSPAN for all ICMP packets that ingress swp1. The source IP address for ERSPAN encapsulation is 10.10.10.1 and the destination IP address for ERSPAN encapsulation is 10.10.10.234.

     ```
     cumulus@switch:~$ sudo nano /etc/cumulus/acl/policy.d/erspan.rules
     [iptables]
     -A FORWARD --in-interface swp1 -p icmp -j ERSPAN --src-ip 10.10.10.1 --dst-ip 10.10.10.234
     ```

     `src-ip` can be any IP address, even if it does not exist in the routing table.

     `dst-ip` must be an IP address reachable through the routing table and front-panel port (not the management port) or SVI. Use ping or ip route get <ip> to verify that the destination IP address is reachable.

2. Install the rules:

   ```
   cumulus@switch:~$ sudo cl-acltool -i
   ```

   {{%notice warning%}}
Do not run the `cl-acltool -i` command with `-P` option. The `-P` option removes **all** existing control plane rules or other installed rules and only installs the rules defined in the specified file.
{{%/notice%}}

3. Verify that you installed the ERSPAN rules:

     ```
     cumulus@switch:~$ sudo iptables -L -v | grep ERSPAN
     29     0 ERSPAN     icmp --  swp1   any     anywhere             anywhere             ERSPAN src-ip:10.10.10.1 dst-ip:10.10.10.234
     ```

### Example Rules

In the following example rules, the source IP address for ERSPAN encapsulation is 10.10.10.1 and the destination IP address for ERSPAN encapsulation is 10.10.10.234.

To mirror forwarded packets from all ports matching the source IP address 20.0.0.2 and the destination IP address 20.0.1.2:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -d 20.0.1.2 -j ERSPAN --src-ip 10.10.10.1 --dst-ip 10.10.10.234
```

To mirror ICMP packets from all ports:

```
-A FORWARD --in-interface swp+ -p icmp -j ERSPAN --src-ip 10.10.10.1 --dst-ip 10.10.10.234
```

To mirror forwarded UDP packets with destination port 53 arriving on swp1:

```
-A FORWARD --in-interface swp1 -p udp --dport 53 -j ERSPAN --src-ip 10.10.10.1 --dest-ip 10.10.10.234
```

To mirror all forwarded TCP packets with only SYN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL SYN -j ERSPAN --src-ip 10.10.10.1 --dst-ip 10.10.10.234
```

To mirror all forwarded TCP packets with only FIN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL FIN -j ERSPAN --src-ip 10.10.10.1 --dst-ip 10.10.10.234
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
    0     0 SPAN       all  --  any    swp1    10.10.10.1    anywhere    /* rule_id:1,acl_name:EXAMPLE1,dir:outbound,interface_id:swp1 */ dport:cpu
```

## Limitations

- On a switch with the Spectrum-2 ASIC or later, Cumulus Linux supports four SPAN destinations in atomic mode or eight SPAN destinations in non-atomic mode. On a switch with the Spectrum 1 ASIC, Cumulus Linux supports only a single SPAN destination in atomic mode or three SPAN destinations in non-atomic mode.
- WJH buffer drop monitoring uses a SPAN destination; if you configure {{<link title="What Just Happened (WJH)" >}}, ensure that you do not exceed the total number of SPAN destinations allowed for your switch ASIC type.
- Multiple SPAN sources can point to the same SPAN destination, but a SPAN source *cannot* specify two SPAN destinations.
- Cumulus Linux does not support IPv6 ERSPAN destinations.
- You cannot use eth0 as a destination.
- You cannot mirror packets that *egress* a bond interface (such as bond1); you can only mirror packets that *egress* bond members (such as swp1, swp2 and so on).
- Mirrored traffic is not guaranteed. A congested MTP results in discarded mirrored packets.
- A oversubscribed SPAN and ERSPAN destination interface might result in data plane buffer depletion and buffer drops. Exercise caution when enabling SPAN and ERSPAN when the aggregate speed of all source ports exceeds the destination port.
- ERSPAN does not cause the kernel to send ARP requests to resolve the next hop for the ERSPAN destination. If an ARP entry for the destination or next hop does not already exist in the kernel, you need to manually resolve this before sending mirrored traffic (use `ping` or `arping`).
- Mirroring to the same interface that you are monitoring causes a recursive flood of traffic and might impact traffic on other interfaces.
- Cumulus VX does not support ACL-based SPAN, ERSPAN, or port mirroring. To capture packets in Cumulus VX, use the `tcpdump` command line network traffic analyzer.
