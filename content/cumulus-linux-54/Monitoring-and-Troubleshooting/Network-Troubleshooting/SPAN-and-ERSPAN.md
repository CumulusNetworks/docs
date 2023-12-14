---
title: SPAN and ERSPAN
author: NVIDIA
weight: 1145
toc: 4
---
<span class="a-tooltip">[SPAN](## "Switched Port Analyzer")</span> enables you to mirror all packets that come in from or go out of an interface (the *SPAN source*), and copy and transmit the packets out of a local port or CPU (the *SPAN destination*) for monitoring. The SPAN destination port is also referred to as a mirror-to-port (MTP). The original packet is still switched, while a mirrored copy of the packet goes out of the MTP.

<span class="a-tooltip">[ERSPAN](## "Encapsulated Remote SPAN")</span> enables the mirrored packets to go to a monitoring node located anywhere across the routed network. The switch finds the outgoing port of the mirrored packets by looking up the destination IP address in its routing table. The switch encapsulates the original layer 2 packet with GRE for IP delivery. The encapsulated packets have the following format:

```
 ----------------------------------------------------------
| MAC_HEADER | IP_HEADER | GRE_HEADER | L2_Mirrored_Packet |
 ----------------------------------------------------------
```

You can configure SPAN and ERSPAN in one of the following ways:
- With NVUE Commands
- With ACL rules
- Manually editing the `/etc/cumulus/switchd.d/port-mirror.conf` file (for advanced users)

{{%notice note%}}
- Mirrored traffic is not guaranteed. A congested MTP results in discarded mirrored packets.
- A oversubscribed SPAN and ERSPAN destination interface might result in data plane buffer depletion and buffer drops. Exercise caution when enabling SPAN and ERSPAN when the aggregate speed of all source ports exceeds the destination port.
- Because SPAN and ERSPAN happens in hardware, you cannot use eth0 as a destination.
- Cumulus Linux does not support IPv6 ERSPAN destinations.
- ERSPAN does not cause the kernel to send ARP requests to resolve the next hop for the ERSPAN destination. If an ARP entry for the destination or next hop does not already exist in the kernel, you need to manually resolve this before sending mirrored traffic (use `ping` or `arping`).
- Mirroring to the same interface that you are monitoring causes a recursive flood of traffic and might impact traffic on other interfaces.
- Cumulus VX does not support ACL rules for SPAN, ERSPAN, or port mirroring. To capture packets in Cumulus VX, use the `tcpdump` command line network traffic analyzer.
{{%/notice%}}

## NVUE Configuration

- To configure SPAN with NVUE, run the `nv set system port-mirror session <session-id> span <option>` command.
- To configure ERSPAN with NVUE, run the `nv set system port-mirror session <session-id> erspan <option>` command.

SPAN and ERSPAN configuration requires a session ID, which is a number between 0 and 7.

You can set the following SPAN and ERSPAN options:
- Source port (`source-port`)
- Destination port (`destination`)
- Direction (`ingress` or `egress`)
- Source IP address for ERSPAN encapsulation (`destination source-ip`)
- Destination IP address for ERSPAN encapsulation (`destination dest-ip`)

You can also truncate the mirrored frames at specified number of bytes. The size must be between 4 and 4088 bytes and a multiple of 4.

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

The following commands truncate the mirrored frames for SPAN at 40 bytes:

```
cumulus@switch:~$ nv set system port-mirror session 1 span truncate size 40
cumulus@switch:~$ nv config apply
```

### Show Session Configuration

To show SPAN and ERSPAN configuration for a specific session, run the `nv show system port-mirror session <session-id>` command.
To show SPAN and ERSPAN configuration for all sessions, run the `nv show system port-mirror` command.

### Delete Sessions

To delete a SPAN or ERSPAN session, run the `nv unset system port-mirror session <session-id>` command. For example:

```
cumulus@switch:~$ nv unset system port-mirror session 1
cumulus@switch:~$ nv config apply
```

You can delete all SPAN or ERSPAN sessions with the `nv unset system port-mirror` command. For example:

```
cumulus@switch:~$ nv unset system port-mirror
cumulus@switch:~$ nv config apply
```
<!-- vale off -->
## cl-acltool Configuration
<!-- vale on -->
You can configure SPAN and ERSPAN with `cl-acltool`, the {{<link url="Netfilter-ACLs" text="same utility used for security ACL configuration">}}. The match criteria for SPAN and ERSPAN is usually an interface; for more granular match terms, use {{<link url="#selective-spanning" text="selective spanning">}}. The SPAN source interface can be a port, a subinterface, or a bond interface. You can match ingress traffic on interfaces. On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, you can match egress traffic.

{{%notice note%}}
Always place your rule files under `/etc/cumulus/acl/policy.d/`.
{{%/notice%}}

### Limitations

- On a switch with the Spectrum-2 ASIC or later, Cumulus Linux supports four SPAN destinations in atomic mode or eight SPAN destinations in non-atomic mode. On a switch with the Spectrum 1 ASIC, Cumulus Linux supports only a single SPAN destination in atomic mode or three SPAN destinations in non-atomic mode.
- Cumulus Linux does not support SPAN ACL rules for an output interface that is a subinterface.
- Multiple rules (SPAN sources) can point to the same SPAN destination, but a given SPAN source *cannot* specify two SPAN destinations.

### SPAN for Switch Ports

Follow the procedure below to set up, install, and verify SPAN rules.

The example commands span (mirror) swp4 input traffic and swp4 output traffic to destination swp19.

1. Create a rules file in `/etc/cumulus/acl/policy.d/`:

   ```
   cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/span.rules
   [iptables]
   -A FORWARD --in-interface swp1 -j SPAN --dport swp2
   -A FORWARD --out-interface swp1 -j SPAN --dport swp2
   EOF'
   ```

   {{%notice note%}}
Using `cl-acltool` with the `--out-interface` rule applies to transit traffic only; it does not apply to traffic sourced from the switch.
{{%/notice%}}

2. Verify all the rules that are currently installed:

   ```
   cumulus@switch:~$ sudo iptables -L -v
   Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination
        0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere
        0     0 DROP       all  --  swp+   any     loopback/8           anywhere
        0     0 DROP       all  --  swp+   any     base-address.mcast.net/8  anywhere
        0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere
        0     0 SETCLASS   ospf --  swp+   any     anywhere             anywhere             SETCLASS  class:7
        0     0 POLICE     ospf --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:2000 burst:2000
        0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpt:bgp SETCLASS  class:7
        0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bgp POLICE  mode:pkt rate:2000 burst:2000
        0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp spt:bgp SETCLASS  class:7
        0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp spt:bgp POLICE  mode:pkt rate:2000 burst:2000
        0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpt:5342 SETCLASS  class:7
        0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:5342 POLICE  mode:pkt
   ...
   Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination
        0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere
        0     0 DROP       all  --  swp+   any     loopback/8           anywhere
        0     0 DROP       all  --  swp+   any     base-address.mcast.net/8  anywhere
        0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere
    26864 4672K SPAN       all  --  swp1   any     anywhere             anywhere             dport:swp2  <---- input packets on swp1

   40722   47M  SPAN       all  --  any    swp1     anywhere             anywhere             dport:swp2  <---- output packets on swp1

   Chain OUTPUT (policy ACCEPT 67398 packets, 5757K bytes)
     pkts bytes target     prot opt in     out     source               destination
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
Running the following command is incorrect. The command removes **all** existing control-plane rules or other installed rules and only installs the rules defined in `span.rules`:

```
cumulus@switch:~$ sudo cl-acltool -i  -P /etc/cumulus/acl/policy.d/span.rules
```
{{%/notice%}}

4. Verify that the you installed the SPAN rules:

   ```
   cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
   38025 7034K SPAN       all  --  swp1   any     anywhere             anywhere             dport:swp2
   50832   55M SPAN       all  --  any    swp1    anywhere             anywhere             dport:swp2
   ```

### SPAN Sessions that Reference an Outgoing Interface

SPAN sessions that reference an outgoing interface create the mirrored packets according to the ingress interface before the routing decision. For example, the following rule captures traffic that is ultimately destined to leave swp1 but mirrors the packets when they arrive on swp49. The rule transmits packets that reference the original VLAN tag, and source and destination MAC address at the time that swp49 originally receives the packet.

```
-A FORWARD --out-interface swp1 -j SPAN --dport swp2
```

### SPAN for Bonds

To configure SPAN for all packets going out of `bond0` locally to `bond1`:

1. Create a rules file in `/etc/cumulus/acl/policy.d/`:

   ```
   cumulus@switch:~$ sudo bash -c 'cat <<EOF > /etc/cumulus/acl/policy.d/span_bond.rules
   [iptables]
   -A FORWARD --out-interface bond0 -j SPAN --dport bond1
   EOF'
   ```

   {{%notice note%}}
Using `cl-acltool` with the `--out-interface` rule applies to transit traffic only; it does not apply to traffic sourced from the switch.
{{%/notice%}}

2. Install the rules:

   ```
   cumulus@switch:~$ sudo cl-acltool -i
   [sudo] password for cumulus:
   Reading rule file /etc/cumulus/acl/policy.d/00control_plane.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/00control_plane.rules ...
   Reading rule file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/99control_plane_catch_all.rules ...
   Reading rule file /etc/cumulus/acl/policy.d/span_bond.rules ...
   Processing rules in file /etc/cumulus/acl/policy.d/span_bond.rules ...
   Installing acl policy
   done.
   ```

3. Verify that you installed the SPAN rules:

   ```
   cumulus@switch:~$ sudo iptables -L -v | grep SPAN
       19  1938 SPAN       all  --  any    bond0   anywhere         anywhere         dport:bond1
   ```

### CPU port as the SPAN Destination

You can set the CPU port as a SPAN destination interface to mirror data plane traffic to the CPU. The SPAN traffic goes to a separate network interface mirror where you can analyze it with `tcpdump`. This is a useful feature if you do not have any free external ports on the switch for monitoring. SPAN traffic does not appear on switch ports.

Cumulus Linux controls how much traffic reaches the CPU so that mirrored traffic does not overwhelm the CPU.

{{%notice note%}}
Cumulus Linux does not support egress mirroring for control plane generated traffic to the CPU port.
{{%/notice%}}

To use the CPU port as the SPAN destination, create a file in the `/etc/cumulus/acl/policy.d/` directory and add the rules. The following example rule matches on swp1 ingress traffic that has the source IP Address 10.10.1.1. When a match occurs, the traffic mirrors to the CPU:

```
[iptables]
     -A FORWARD -i swp1 -s 10.10.1.1 -j SPAN --dport cpu
```

This example rule matches on swp1 egress traffic that has the source IP Address 10.10.1.1.
When a match occurs, the traffic mirrors to the CPU:

```
[iptables]
     -A FORWARD -o swp1 -s 10.10.1.1 -j SPAN --dport cpu
```

Install the rules:

```
cumulus@switch:~$ sudo cl-acltool -i
```

You can use `tcpcdump` to monitor traffic mirrored to the CPU on the switch. You can also use filters for `tcpdump`. To use `tcpcdump` to monitor traffic mirrored to the CPU, run the following command:

```
cumulus@switch:~$ sudo tcpdump -i mirror
```

### Example SPAN Rules

To mirror forwarded packets from all ports matching source IP address 20.0.1.0 and destination IP address 20.0.1.2 to port swp1s1:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -d 20.0.1.2 -j SPAN --dport swp1s2
```

To mirror ICMP packets from all ports to swp1s2:

```
-A FORWARD --in-interface swp+ -s 20.0.0.2 -p icmp -j SPAN --dport swp1s2
```

To mirror forwarded UDP packets received from port swp1s0, towards destination IP address 20.0.1.2 and destination port 53:

```
-A FORWARD --in-interface swp1s0 -d 20.0.1.2 -p udp --dport 53 -j SPAN --dport swp1s2
```

To mirror all forwarded TCP packets with only SYN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL SYN -j SPAN --dport swp1s2
```

To mirror all forwarded TCP packets with only FIN set:

```
-A FORWARD --in-interface swp+ -p tcp --tcp-flags ALL FIN -j SPAN --dport swp1s2
```

### ERSPAN

This section describes how to configure ERSPAN.

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

If a SPAN destination IP address is not available, or if the interface type prevents you from using a laptop as a SPAN destination, refer to [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Configure-ERSPAN-to-a-Cumulus-Linux-Switch" >}}).

{{%notice note%}}
- If you use {{<exlink url="https://www.wireshark.org" text="Wireshark">}} to review the ERSPAN output, you might see the Wireshark error message `Unknown version, please report or test to use fake ERSPAN preference` and the trace might be unreadable. To resolve this issue, go to **Protocols \ ERSPAN** from the Wireshark General preferences and check the **Force to decode fake ERSPAN frame** option.
- To set up a {{<exlink url="https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureFilterSection.html" text="capture filter">}} on the destination switch that filters for a specific IP protocol, use `ip.proto == 47` to filter for GRE-encapsulated (IP protocol 47) traffic.
{{%/notice%}}

### Example ERSPAN Rules

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

### Selective Spanning

To reduce the volume of copied data, you can configure SPAN and ERSPAN traffic rules to limit the traffic it spans.

Cumulus Linux supports selective spanning for `iptables` only.

You can match on the following fields:

- IPv4 SIP/DIP
- IP protocol
- Layer 4 (TCP/UDP) src/dst port
- TCP flags
- An ingress port or wildcard (swp+)

ERSPAN supports a maximum of two `--src-ip --dst-ip` pairs. Exceeding this limit produces an error when you install the rules with `cl-acltool`.

### Remove Rules

To remove your SPAN or ERSPAN rules, remove the rules file, then reload the default rules. For example:

```
cumulus@switch:~$ sudo rm  /etc/cumulus/acl/policy.d/span.rules
cumulus@switch:~$ sudo cl-acltool -i
```

To verify that the you removed the rules:

```
cumulus@switch:~$ sudo cl-acltool -L all | grep SPAN
```

## Manual Configuration (Advanced)

You can configure SPAN and ERSPAN by editing the `/etc/cumulus/switchd.d/port-mirror.conf` file.

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
